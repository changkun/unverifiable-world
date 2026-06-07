#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把《在无法验证的世界里》构建成一个简单的静态阅读网站。

- 读取仓库根目录的 SUMMARY.md 作为目录结构；
- 每章 Markdown 渲染为 HTML（数学交给 KaTeX 客户端渲染，SVG 图原生显示，
  原始 HTML/JS 原样透传以支持动画）；
- 生成：封面 index.html、目录 toc.html、各章页（带侧栏目录与上一页/下一页）。

全部输出使用相对路径，因此可直接部署到任何子路径下（如 changkun.de/xxx/）。

依赖：python3 与 `markdown`（pip install markdown）。
用法：python3 website/build.py   →   输出到 website/public/
"""
import html
import os
import re
import shutil
import sys

try:
    import markdown
except ImportError:
    sys.exit("缺少依赖：请先运行  pip install markdown")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUMMARY = os.path.join(ROOT, "SUMMARY.md")
OUT = os.path.join(ROOT, "website", "public")
FIG_SRC = os.path.join(ROOT, "book", "figures")

TITLE = "在无法验证的世界里"
SUBTITLE = "In a World Without Verification"
AUTHOR = "欧长坤"
BLURB = "在没有任何东西能确认你做对了的地方，有限的主体如何行动。"

KATEX = """
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],throwOnError:false});"></script>
"""

CSS = """
:root{--ink:#1a1a1a;--muted:#6b7280;--line:#e5e7eb;--accent:#3b4252;--bg:#fbfbf9;--paper:#ffffff}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);
 font-family:"Noto Serif SC","Songti SC",Georgia,"Times New Roman",serif;line-height:1.85;font-size:18px}
a{color:#2b4a8b;text-decoration:none}a:hover{text-decoration:underline}
.wrap{display:flex;max-width:1180px;margin:0 auto;min-height:100vh}
.sidebar{width:280px;flex:none;border-right:1px solid var(--line);padding:28px 20px;
 position:sticky;top:0;height:100vh;overflow-y:auto;background:var(--paper)}
.sidebar .home{font-weight:700;font-size:17px;display:block;margin-bottom:4px;color:var(--ink)}
.sidebar .sub{color:var(--muted);font-size:12.5px;margin-bottom:18px}
.sidebar .part{font-weight:700;margin:16px 0 6px;font-size:14px;color:var(--accent)}
.sidebar ul{list-style:none;padding:0;margin:0}
.sidebar li{margin:3px 0}
.sidebar a{font-size:14.5px;color:#374151;display:block;padding:2px 0}
.sidebar a.active{color:#2b4a8b;font-weight:700}
.content{flex:1;min-width:0;padding:46px 56px 90px;max-width:820px;margin:0 auto}
.content h1{font-size:30px;line-height:1.3;margin:.2em 0 .6em}
.content h2{font-size:23px;margin:1.8em 0 .6em;padding-bottom:.2em;border-bottom:1px solid var(--line)}
.content h3{font-size:19px;margin:1.4em 0 .5em}
.content p{margin:1em 0}
.content blockquote{margin:1.2em 0;padding:.4em 1.1em;border-left:3px solid #cbd5e1;color:#374151;background:#f8fafc}
.content img{max-width:100%;height:auto;display:block;margin:1.6em auto}
.content table{border-collapse:collapse;margin:1.4em 0;font-size:15.5px;width:100%}
.content th,.content td{border:1px solid var(--line);padding:7px 11px;text-align:left;vertical-align:top}
.content th{background:#f3f4f6}
.content code{background:#f3f4f6;padding:.1em .35em;border-radius:4px;font-size:.9em}
.content pre{background:#f6f8fa;padding:14px 16px;border-radius:8px;overflow:auto}
.content pre code{background:none;padding:0}
.content hr{border:none;border-top:1px solid var(--line);margin:2em 0}
.nav{display:flex;justify-content:space-between;margin-top:56px;padding-top:20px;border-top:1px solid var(--line);font-size:15px}
.nav a{max-width:46%}
/* 封面 */
.cover{display:flex;flex-direction:column;align-items:center;justify-content:center;
 min-height:100vh;width:100%;text-align:center;padding:40px}
.book{width:330px;max-width:80vw;aspect-ratio:5/7;border-radius:6px;
 background:linear-gradient(135deg,#2b3a55 0%,#1b2233 100%);color:#f4f4f2;
 box-shadow:0 24px 60px rgba(20,30,50,.35),inset 4px 0 0 rgba(255,255,255,.12),inset 8px 0 14px rgba(0,0,0,.25);
 display:flex;flex-direction:column;justify-content:space-between;padding:42px 34px;position:relative}
.book .t{font-size:30px;font-weight:700;line-height:1.35;letter-spacing:1px}
.book .s{font-size:13px;color:#aab4c8;letter-spacing:2px;text-transform:uppercase;margin-top:14px}
.book .a{font-size:15px;color:#dfe5ef;margin-top:auto}
.book .rule{width:42px;height:3px;background:#8aa0c8;margin:18px auto 0}
.cover .blurb{color:var(--muted);max-width:520px;margin:30px auto 8px;font-size:16px}
.cover .actions{margin-top:22px;display:flex;gap:14px;flex-wrap:wrap;justify-content:center}
.btn{display:inline-block;padding:10px 22px;border-radius:8px;font-size:15.5px;border:1px solid #2b4a8b}
.btn.primary{background:#2b4a8b;color:#fff}.btn.primary:hover{text-decoration:none;background:#23407c}
.btn.ghost{color:#2b4a8b;background:#fff}.btn.ghost:hover{text-decoration:none;background:#f0f4fb}
.toc-page .part{font-weight:700;color:var(--accent);margin:24px 0 8px;font-size:17px}
.toc-page ul{list-style:none;padding:0}.toc-page li{margin:7px 0;font-size:16.5px}
.muted{color:var(--muted)}
@media(max-width:820px){.sidebar{display:none}.content{padding:28px 20px 70px}body{font-size:17px}}
"""


def slug(path):
    base = os.path.basename(path)
    return base[:-3] + ".html" if base.endswith(".md") else base


def parse_summary():
    """返回 (entries, parts)。entries: [(title, htmlfile, mdpath)]；parts: [(part_title, [idx...])]"""
    entries, parts = [], []
    cur = None
    for ln in open(SUMMARY, encoding="utf-8"):
        ln = ln.rstrip("\n")
        m = re.match(r"^##\s+(.*)$", ln)
        if m:
            cur = (m.group(1).strip(), [])
            parts.append(cur)
            continue
        m = re.match(r"^\s*-\s*\[(.+?)\]\((.+?)\)\s*$", ln)
        if m:
            title, path = m.group(1).strip(), m.group(2).strip()
            idx = len(entries)
            entries.append((title, slug(path), os.path.join(ROOT, path)))
            if cur is None:
                cur = ("", [])
                parts.append(cur)
            cur[1].append(idx)
    return entries, parts


def sidebar_html(entries, parts, active=None):
    out = [f'<a class="home" href="index.html">{html.escape(TITLE)}</a>',
           f'<div class="sub">{html.escape(AUTHOR)}　·　<a href="toc.html">目录</a></div>']
    for ptitle, idxs in parts:
        if ptitle:
            out.append(f'<div class="part">{html.escape(ptitle)}</div>')
        out.append("<ul>")
        for i in idxs:
            t, f, _ = entries[i]
            cls = ' class="active"' if f == active else ""
            out.append(f'<li><a{cls} href="{f}">{html.escape(t)}</a></li>')
        out.append("</ul>")
    return "\n".join(out)


def page(title, body, sidebar, extra_class=""):
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} · {html.escape(TITLE)}</title>
{KATEX}
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<nav class="sidebar">{sidebar}</nav>
<main class="content {extra_class}">{body}</main>
</div>
</body>
</html>
"""


def cover_page(entries):
    # 封面整页呈现，不显示侧栏
    return f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title><style>{CSS}</style></head>
<body><div class="wrap" style="display:block">{cover_body(entries)}</div></body></html>
"""


def cover_body(entries):
    first = entries[0][1] if entries else "toc.html"
    return f"""
<div class="cover">
  <div class="book">
    <div>
      <div class="t">{html.escape(TITLE)}</div>
      <div class="s">{html.escape(SUBTITLE)}</div>
      <div class="rule"></div>
    </div>
    <div class="a">{html.escape(AUTHOR)}　著</div>
  </div>
  <p class="blurb">{html.escape(BLURB)}</p>
  <div class="actions">
    <a class="btn primary" href="{first}">开始阅读</a>
    <a class="btn ghost" href="toc.html">目录</a>
  </div>
  <p class="muted" style="margin-top:26px;font-size:13.5px">本作品采用 CC BY-NC-ND 4.0 许可</p>
</div>
"""


def toc_page(entries, parts, sidebar):
    out = ['<h1>目录</h1>']
    for ptitle, idxs in parts:
        if ptitle:
            out.append(f'<div class="part">{html.escape(ptitle)}</div>')
        out.append("<ul>")
        for i in idxs:
            t, f, _ = entries[i]
            out.append(f'<li><a href="{f}">{html.escape(t)}</a></li>')
        out.append("</ul>")
    return page("目录", "\n".join(out), sidebar, extra_class="toc-page")


MD_EXT = ["extra", "tables", "fenced_code", "sane_lists", "attr_list"]


def render_md(mdpath):
    text = open(mdpath, encoding="utf-8").read()
    body = markdown.markdown(text, extensions=MD_EXT)
    # 图片路径：../figures/x.svg -> figures/x.svg（输出为扁平结构）
    body = body.replace('src="../figures/', 'src="figures/').replace("src='../figures/", "src='figures/")
    return body


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    # 拷贝插图
    if os.path.isdir(FIG_SRC):
        shutil.copytree(FIG_SRC, os.path.join(OUT, "figures"))

    entries, parts = parse_summary()

    # 封面
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(cover_page(entries))
    # 目录
    open(os.path.join(OUT, "toc.html"), "w", encoding="utf-8").write(
        toc_page(entries, parts, sidebar_html(entries, parts)))

    # 各章
    for i, (title, fname, mdpath) in enumerate(entries):
        body = render_md(mdpath)
        prev_a = (f'<a href="{entries[i-1][1]}">← {html.escape(entries[i-1][0])}</a>' if i > 0
                  else '<a href="index.html">← 封面</a>')
        next_a = (f'<a href="{entries[i+1][1]}">{html.escape(entries[i+1][0])} →</a>' if i < len(entries) - 1
                  else '<a href="toc.html">目录 →</a>')
        body += f'<div class="nav">{prev_a}{next_a}</div>'
        open(os.path.join(OUT, fname), "w", encoding="utf-8").write(
            page(title, body, sidebar_html(entries, parts, active=fname)))

    print(f"已生成 {len(entries)} 章 + 封面 + 目录 到 {os.path.relpath(OUT, ROOT)}/")
    print("本地预览： (cd website/public && python3 -m http.server 8000)  然后访问 http://localhost:8000")


if __name__ == "__main__":
    main()
