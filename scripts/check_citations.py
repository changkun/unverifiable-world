#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
核查并下载全书参考文献。

对 book/**/*.md「## 参考文献」一节里的每条文献：
  1. 解析出标题、年份、arXiv 编号（若有）；
  2. arXiv 条目直接从 arxiv.org 下载 PDF；
  3. 其余用 Crossref 按题名解析 DOI，再用 Unpaywall 查开放获取 PDF 并下载；
  4. 把 PDF 存到 sources/（已 gitignore），并生成核查报告 sources/REPORT.md 与 sources/citations.csv。

只用标准库，无需安装依赖。需要联网。礼貌起见对 API 限速。

用法：
    python3 scripts/check_citations.py                # 全部
    python3 scripts/check_citations.py --no-download  # 只核查不下载
    python3 scripts/check_citations.py --limit 20     # 只处理前 20 条（冒烟测试）
    python3 scripts/check_citations.py --chapter ch07 # 只处理某文件
"""
import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(ROOT, "book")
OUT = os.path.join(ROOT, "sources")
EMAIL = "hi@changkun.de"  # Unpaywall / Crossref 礼貌池要求一个联系邮箱
UA = f"unverifiable-world-citation-checker/1.0 (mailto:{EMAIL})"

TITLE_RE = re.compile(r"[「《]([^」》]+)[」》]")
YEAR_RE = re.compile(r"\((\d{4})(?:[-–]\d{2,4})?\)")
ARXIV_RE = re.compile(r"arXiv:\s*([0-9]{4}\.[0-9]{4,5}|[a-z\-]+/[0-9]{7})", re.I)
ENTRY_RE = re.compile(r"^\s*\d+\.\s+(.*)$")


def http_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def http_download(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    if not data or len(data) < 1024:
        raise ValueError("downloaded file too small")
    with open(dest, "wb") as f:
        f.write(data)
    return len(data)


def slugify(s, n=60):
    s = re.sub(r"[^\w一-鿿]+", "-", s).strip("-")
    return s[:n] or "ref"


def parse_bibliography(md_path):
    """返回该文件「## 参考文献」一节里的条目列表。"""
    text = open(md_path, encoding="utf-8").read()
    if "## 参考文献" not in text:
        return []
    bib = text.split("## 参考文献", 1)[1]
    entries = []
    for line in bib.splitlines():
        m = ENTRY_RE.match(line)
        if not m:
            continue
        body = m.group(1)
        title_m = TITLE_RE.search(body)
        year_m = YEAR_RE.search(body)
        arxiv_m = ARXIV_RE.search(body)
        entries.append({
            "raw": body.strip(),
            "title": title_m.group(1).strip() if title_m else "",
            "year": year_m.group(1) if year_m else "",
            "arxiv": arxiv_m.group(1) if arxiv_m else "",
        })
    return entries


def crossref_lookup(title, year):
    q = urllib.parse.quote(title)
    url = f"https://api.crossref.org/works?query.bibliographic={q}&rows=3&mailto={EMAIL}"
    try:
        items = http_json(url).get("message", {}).get("items", [])
    except Exception as e:
        return None, f"crossref error: {e}"
    for it in items:
        ct = (it.get("title") or [""])[0].lower()
        if not ct:
            continue
        # 粗略题名匹配：去标点后包含关系
        a = re.sub(r"[^a-z0-9]+", "", ct)
        b = re.sub(r"[^a-z0-9]+", "", title.lower())
        if a and b and (a in b or b in a or _ratio(a, b) > 0.85):
            return it.get("DOI"), None
    # 没有强匹配则退回第一条，但标注为弱匹配
    if items:
        return items[0].get("DOI"), "weak-match"
    return None, "no-crossref-match"


def _ratio(a, b):
    # 极简的字符级相似度，避免引入依赖
    sa, sb = set(a[i:i+4] for i in range(len(a)-3)), set(b[i:i+4] for i in range(len(b)-3))
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def unpaywall_pdf(doi):
    url = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={EMAIL}"
    try:
        data = http_json(url)
    except Exception as e:
        return None, f"unpaywall error: {e}"
    loc = data.get("best_oa_location")
    if loc and loc.get("url_for_pdf"):
        return loc["url_for_pdf"], None
    return None, "no-oa-pdf"


def process(entry, do_download):
    rec = dict(entry, doi="", oa_url="", pdf="", status="")
    if not entry["title"]:
        rec["status"] = "no-title-parsed"
        return rec

    # arXiv 优先
    if entry["arxiv"]:
        rec["oa_url"] = f"https://arxiv.org/pdf/{entry['arxiv']}.pdf"
        rec["status"] = "arxiv"
    else:
        doi, note = crossref_lookup(entry["title"], entry["year"])
        time.sleep(0.5)
        if doi:
            rec["doi"] = doi
            pdf, unote = unpaywall_pdf(doi)
            time.sleep(0.5)
            if pdf:
                rec["oa_url"] = pdf
                rec["status"] = "oa" if note != "weak-match" else "oa-weak-match"
            else:
                rec["status"] = (note or "") + "/" + (unote or "")
        else:
            rec["status"] = note or "unresolved"

    if do_download and rec["oa_url"]:
        fname = f"{entry['year']}-{slugify(entry['title'])}.pdf"
        dest = os.path.join(OUT, "pdf", fname)
        if os.path.exists(dest):
            rec["pdf"] = os.path.relpath(dest, ROOT)
            rec["status"] += "/cached"
        else:
            try:
                http_download(rec["oa_url"], dest)
                rec["pdf"] = os.path.relpath(dest, ROOT)
                rec["status"] += "/downloaded"
            except Exception as e:
                rec["status"] += f"/download-failed:{e}"
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-download", action="store_true", help="只核查不下载 PDF")
    ap.add_argument("--limit", type=int, default=0, help="只处理前 N 条")
    ap.add_argument("--chapter", default="", help="只处理文件名含该串的章节")
    args = ap.parse_args()

    os.makedirs(os.path.join(OUT, "pdf"), exist_ok=True)
    files = []
    for dirpath, _, names in os.walk(BOOK):
        for n in sorted(names):
            if n.endswith(".md") and (not args.chapter or args.chapter in n):
                files.append(os.path.join(dirpath, n))
    files.sort()

    rows, n = [], 0
    for f in files:
        rel = os.path.relpath(f, ROOT)
        for i, e in enumerate(parse_bibliography(f), 1):
            if args.limit and n >= args.limit:
                break
            n += 1
            rec = process(e, not args.no_download)
            rec["file"] = rel
            rec["index"] = i
            rows.append(rec)
            print(f"[{n}] {rel} #{i}  {rec['status']:<24} {e['title'][:60]}")
        if args.limit and n >= args.limit:
            break

    # 报告
    csv_path = os.path.join(OUT, "citations.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["file", "index", "year", "title", "doi", "status", "oa_url", "pdf", "arxiv"])
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in w.fieldnames})

    ok = sum(1 for r in rows if r["pdf"])
    resolved = sum(1 for r in rows if r["doi"] or r["arxiv"])
    with open(os.path.join(OUT, "REPORT.md"), "w", encoding="utf-8") as fh:
        fh.write("# 参考文献核查与下载报告\n\n")
        fh.write(f"- 条目总数：{len(rows)}\n- 解析到 DOI/arXiv：{resolved}\n- 成功下载 PDF：{ok}\n\n")
        fh.write("详见 `citations.csv`。PDF 存于 `sources/pdf/`（未纳入版本库）。\n\n")
        fh.write("| 文件 | # | 年 | 标题 | 状态 | PDF |\n|---|---|---|---|---|---|\n")
        for r in rows:
            fh.write(f"| {r['file'].split('/')[-1]} | {r['index']} | {r['year']} | {r['title'][:50]} | {r['status']} | {'✓' if r['pdf'] else ''} |\n")

    print(f"\n完成：{len(rows)} 条，解析 {resolved}，下载 {ok}。报告见 sources/REPORT.md")


if __name__ == "__main__":
    main()
