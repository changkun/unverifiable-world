#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把《这个无法验证的世界》/《An Unverifiable World》编译成可下载的 PDF 与 EPUB。

两个语种各产两份文件，写到仓库根的 dist/：
    unverifiable-world-zh.pdf / .epub
    unverifiable-world-en.pdf / .epub

做法：按 SUMMARY 顺序拼接各章 Markdown，做三件预处理，再交给 pandoc：
  1. 正文角标 <sup class="cite"><a href="#ref-N">N</a></sup> → pandoc 上标 ^N^
     （相邻的合并为 ^a,b^）；PDF/EPUB 都能正确显示，仍对应章末编号参考文献。
  2. 每个标题降一级，章/序/跋标题标记为不编号，配图标题前缀由文本承担编号，
     于是 LaTeX 不再自动编号，避免「第 1 章 第 1 章」式重复。
  3. 配图 ../figures/fXX.svg 改写为高分辨率 PNG（xelatex 不能直接嵌 SVG）；
     英文版优先用 book/figures/en/ 下的英文图，缺失则回退中文图。

依赖：pandoc、xelatex（含 CJK 字体 Songti SC）、rsvg-convert。没有 xelatex 时自动改用
同属 XeTeX 的 tectonic（brew install tectonic，免 sudo）；也可用环境变量
PDF_ENGINE=xelatex|tectonic 指定。
用法：python3 scripts/build_book.py            # 两个语种、两种格式
      python3 scripts/build_book.py zh pdf     # 只产中文 PDF（语种/格式可选）
"""
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG_SRC = os.path.join(ROOT, "book", "figures")
FIG_EN_SRC = os.path.join(FIG_SRC, "en")
DIST = os.path.join(ROOT, "dist")
TMP = os.path.join(DIST, ".tmp")


class Lang:
    def __init__(self, code, summary, title, subtitle, author, lang_tag, cjk):
        self.code = code
        self.summary = os.path.join(ROOT, summary)
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.lang_tag = lang_tag
        self.cjk = cjk  # 是否需要 CJK 主字体（正文以中文为主）


ZH = Lang("zh", "SUMMARY.md", "这个无法验证的世界", "An Unverifiable World",
          "欧长坤", "zh-CN", cjk=True)
EN = Lang("en", "SUMMARY.en.md", "An Unverifiable World",
          "How bounded actors act when no oracle can say they are right",
          "Changkun Ou", "en-US", cjk=False)
LANGS = {"zh": ZH, "en": EN}

CJK_FONT = "Songti SC"          # macOS 系统自带；如换平台改这里
FIG_PNG_WIDTH = 2000            # 配图 PNG 宽度，约合 6in 版面 330dpi


def pdf_engine():
    """xelatex 优先；没有时退到 tectonic（同为 XeTeX，fontspec/xeCJK 行为一致）。"""
    want = os.environ.get("PDF_ENGINE")
    if want:
        return want
    return "xelatex" if shutil.which("xelatex") or not shutil.which("tectonic") else "tectonic"


def need(tool):
    if shutil.which(tool) is None:
        sys.exit(f"缺少依赖：找不到 {tool}")


def parse_summary(summary):
    """返回 [(kind, title, path)]，kind ∈ {'part','entry'}，按文件顺序。"""
    items = []
    with open(summary, encoding="utf-8") as f:
        for ln in f:
            ln = ln.rstrip("\n")
            m = re.match(r"^##\s+(.*)$", ln)
            if m:
                items.append(("part", m.group(1).strip(), None))
                continue
            m = re.match(r"^\s*-\s*\[(.+?)\]\((.+?)\)\s*$", ln)
            if m:
                items.append(("entry", m.group(1).strip(),
                              os.path.join(ROOT, m.group(2).strip())))
    return items


def fig_for(lang, name):
    """按语种解析某配图源 SVG，英文缺失则回退中文。"""
    if lang.code == "en":
        cand = os.path.join(FIG_EN_SRC, name)
        if os.path.isfile(cand):
            return cand
    return os.path.join(FIG_SRC, name)


def rasterize(svg_path, png_path):
    subprocess.run(["rsvg-convert", "-w", str(FIG_PNG_WIDTH),
                    svg_path, "-o", png_path], check=True)


def demote_headings(text):
    return re.sub(r"(?m)^(#{1,6})(\s)", r"#\1\2", text)


def mark_first_heading_unnumbered(text):
    """正文降级后，首个 '## ' 标题（章/序/跋题）标记为不编号。"""
    def repl(m):
        return m.group(0).rstrip() + " {.unnumbered}\n"
    return re.sub(r"(?m)^##\s+.*\n", repl, text, count=1)


def convert_citations(text):
    text = re.sub(
        r'<sup class="cite"><a href="#ref-\d+">(\d+)</a></sup>',
        r"^\1^", text)
    # 合并相邻角标：^2^^1^ → ^2,1^
    prev = None
    while prev != text:
        prev = text
        text = re.sub(r"\^(\d[\d,]*)\^\^(\d+)\^", r"^\1,\2^", text)
    return text


def strip_web_widgets(text):
    """删除只在网页阅读器里生效的交互可视化块（<figure class="uvw-viz">…</style>…
    </script>）。它们的静态 SVG 兜底图（紧邻其前的 ![](figures/…svg)）会保留，
    因此 PDF/EPUB 仍有配图；否则 pandoc 会把控件文字抽进正文，污染书稿。"""
    return re.sub(r'\n?<figure class="uvw-viz".*?</script>\n?', "\n",
                  text, flags=re.S)


def rewrite_figures(text, lang, media_dir, used):
    """把 ![cap](../figures/NAME.svg) 改写为本地高清 PNG 的绝对路径。"""
    def repl(m):
        cap, name = m.group(1), m.group(2)
        png = os.path.join(media_dir, name[:-4] + ".png")
        if name not in used:
            rasterize(fig_for(lang, name), png)
            used.add(name)
        return f"![{cap}]({png})"
    return re.sub(r"!\[([^\]]*)\]\((?:\.\./)*figures/([a-z0-9-]+\.svg)\)",
                  repl, text)


def yaml_meta(lang):
    hi = ["  \\setcounter{secnumdepth}{0}", "  \\pagestyle{plain}"]
    if lang.cjk:
        # 带圈数字 ①②③④（落足点标记）与正文里偶见的希腊字母 ζ/ε 走 CJK 字体；
        # Latin 主字体（Latin Modern）没有这些字形。
        hi.append('  \\xeCJKDeclareCharClass{CJK}{"0370->"03FF, "2460->"24FF}')
        # 结构性词汇本地化：目录标题与配图题注。
        hi.append("  \\renewcommand{\\contentsname}{目录}")
        hi.append("  \\renewcommand{\\figurename}{图}")
    lines = [
        "---",
        f'title: "{lang.title}"',
        f'subtitle: "{lang.subtitle}"',
        f'author: "{lang.author}"',
        "header-includes: |",
        *hi,
        "---",
        "",
    ]
    return "\n".join(lines)


def assemble(lang):
    """生成拼接后的 Markdown，返回其路径；同时把配图 PNG 落到 media_dir。"""
    work = os.path.join(TMP, lang.code)
    media_dir = os.path.join(work, "media")
    if os.path.isdir(work):
        shutil.rmtree(work)
    os.makedirs(media_dir)

    used = set()
    chunks = [yaml_meta(lang)]
    for kind, title, path in parse_summary(lang.summary):
        if kind == "part":
            chunks.append(f"\n# {title} {{.unnumbered}}\n")
            continue
        if not os.path.isfile(path):
            print(f"  ! 缺章节，跳过：{os.path.relpath(path, ROOT)}")
            continue
        text = open(path, encoding="utf-8").read()
        text = strip_web_widgets(text)
        text = convert_citations(text)
        text = demote_headings(text)
        text = mark_first_heading_unnumbered(text)
        text = rewrite_figures(text, lang, media_dir, used)
        chunks.append("\n" + text.strip() + "\n")

    md_path = os.path.join(work, "book.md")
    assembled = "\n".join(chunks)
    # 兜底：网页交互控件绝不能漏进书稿，否则 pandoc 会把控件文字抽进正文。
    assert "uvw-viz" not in assembled, "web-only interactive widget leaked into the book build"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(assembled)
    return md_path


def build_pdf(lang, md_path, out_path):
    cmd = [
        "pandoc", md_path,
        "--from=markdown",
        f"--pdf-engine={pdf_engine()}",
        "--top-level-division=part",
        "--toc", "--toc-depth=2",
        "-V", "documentclass=book",
        "-V", "classoption=oneside",
        "-V", "geometry=paperwidth=6in,paperheight=9in,margin=0.85in",
        "-V", "fontsize=11pt",
        "-V", "linestretch=1.15",
        "-V", "colorlinks=true",
        "-o", out_path,
    ]
    # 仅中文版加载 CJK 主字体（xeCJK）；英文版不加载，否则 xeCJK 会把弯引号
    # 当成中文标点、吞掉其后的英文空格。英文正文已确认无任何 CJK 字符。
    if lang.cjk:
        cmd[6:6] = ["-V", f"CJKmainfont={CJK_FONT}"]
    else:
        cmd[6:6] = ["-V", f"lang={lang.lang_tag}"]
    subprocess.run(cmd, check=True)


def build_epub(lang, md_path, out_path):
    cmd = [
        "pandoc", md_path,
        "--from=markdown",
        "--to=epub3",
        "--toc", "--toc-depth=2",
        "--epub-chapter-level=2",
        "--mathml",
        "-o", out_path,
    ]
    subprocess.run(cmd, check=True)


def main(argv):
    need("pandoc")
    need("rsvg-convert")
    want_langs = [a for a in argv if a in LANGS]
    want_fmts = [a for a in argv if a in ("pdf", "epub")]
    langs = [LANGS[c] for c in (want_langs or ["zh", "en"])]
    fmts = want_fmts or ["pdf", "epub"]
    if "pdf" in fmts:
        need(pdf_engine())

    os.makedirs(DIST, exist_ok=True)
    for lang in langs:
        if not os.path.isfile(lang.summary):
            print(f"跳过 {lang.code}：找不到 {os.path.relpath(lang.summary, ROOT)}")
            continue
        print(f"== {lang.code} ==")
        md_path = assemble(lang)
        if "pdf" in fmts:
            out = os.path.join(DIST, f"unverifiable-world-{lang.code}.pdf")
            build_pdf(lang, md_path, out)
            print(f"  ✓ {os.path.relpath(out, ROOT)}")
        if "epub" in fmts:
            out = os.path.join(DIST, f"unverifiable-world-{lang.code}.epub")
            build_epub(lang, md_path, out)
            print(f"  ✓ {os.path.relpath(out, ROOT)}")
    print(f"输出目录：{os.path.relpath(DIST, ROOT)}/")


if __name__ == "__main__":
    main(sys.argv[1:])
