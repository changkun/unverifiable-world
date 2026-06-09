# -*- coding: utf-8 -*-
"""F6（第 7/11 章）：代理替换的 2×2，忠实 × 更易。

生成 book/figures/f07-proxy-2x2.svg
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from svg import SVG, INK, MUTED, STROKES, FILLS

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "book", "figures", "f07-proxy-2x2.svg")


def build(lang="zh"):
    en = (lang == "en")

    def t(zh, eng):
        return eng if en else zh

    W, H = 720, 520
    if en:
        W, H = 760, 540
    s = SVG(W, H)
    s.text(W / 2, 34, t("代理替换的两种相反败法",
                        "The Two Opposite Ways Proxy Substitution Fails"),
           size=22 if not en else 20, weight="bold")
    s.text(W / 2, 60, t("一个好代理必须同时落在右上：既忠实，又更易",
                        "A good proxy must land in the upper right: both faithful and easier"),
           size=14 if not en else 13, fill=MUTED)

    x0, y0 = 150, 100   # 网格左上
    cw, ch = 250, 170   # 单元尺寸
    if en:
        x0, y0 = 168, 104
        cw, ch = 268, 180

    cells = [
        # (col, row, 标题, 例子, 填充, 描边)
        (0, 0, t("忠实 · 不更易", "Faithful · Not easier"),
         t(["数学的等价改写（第 7 章）", "你只是把困难改了名"],
           ["An equivalent rewriting (Ch. 7):", "you only renamed", "the difficulty"]),
         FILLS[2], STROKES[2]),
        (1, 0, t("理想代理 ✓", "Ideal proxy ✓"),
         t(["既忠实又更易", "罕见，全部手艺所在"],
           ["Both faithful and easier;", "rare, and the rarity itself", "is the whole of the craft"]),
         FILLS[1], STROKES[1]),
        (0, 1, t("无用", "Useless"),
         t(["不忠实又不更易", "没人会要"],
           ["Neither faithful nor easier;", "no one would want it"]),
         "#f3f4f6", "#9ca3af"),
        (1, 1, t("Goodhart（第 8 章）", "Goodhart (Ch. 8)"),
         t(["更易却不忠实", "你优化代理，真目标却烂掉"],
           ["Easier but not faithful;", "optimize the proxy and the", "true target snaps"]),
         FILLS[3], STROKES[3]),
    ]
    for col, row, title, lines, fill, stroke in cells:
        x = x0 + col * cw
        y = y0 + row * ch
        s.rect(x, y, cw - 12, ch - 12, fill=fill, stroke=stroke, sw=2)
        s.text(x + (cw - 12) / 2, y + 34, title, size=17, weight="bold", fill=INK)
        s.textbox(x + (cw - 12) / 2, y + 72, lines, size=13.5 if not en else 12.5, fill=MUTED)

    # 轴标签
    s.text(x0 + cw, y0 - 18, t("更易（更可处理）→", "Easier (more tractable) →"),
           size=14 if not en else 13, fill=INK, weight="bold")
    # 纵轴：忠实
    ax = x0 - 28 if not en else x0 - 34
    s.parts.append(
        f'<text x="{ax}" y="{y0 + ch}" font-family="{__import__("svg").FONT}" '
        f'font-size="{14 if not en else 13}" font-weight="bold" fill="{INK}" text-anchor="middle" '
        f'transform="rotate(-90 {ax} {y0 + ch})">'
        f'{t("忠实（真指向原目标）→", "Faithful (points at the original target) →")}</text>')

    out_path = os.path.abspath(OUT)
    if en:
        out_path = os.path.join(os.path.dirname(out_path), "en", os.path.basename(out_path))
    s.save(out_path)
    return out_path


if __name__ == "__main__":
    build("zh")
    print("en ->", build("en"))
