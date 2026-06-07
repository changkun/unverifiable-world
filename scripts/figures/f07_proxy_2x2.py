# -*- coding: utf-8 -*-
"""F6（第 7/11 章）：代理替换的 2×2，忠实 × 更易。

生成 book/figures/f07-proxy-2x2.svg
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from svg import SVG, INK, MUTED, STROKES, FILLS

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "book", "figures", "f07-proxy-2x2.svg")


def build():
    W, H = 720, 520
    s = SVG(W, H)
    s.text(W / 2, 34, "代理替换的两种相反败法", size=22, weight="bold")
    s.text(W / 2, 60, "一个好代理必须同时落在右上：既忠实，又更易", size=14, fill=MUTED)

    x0, y0 = 150, 100   # 网格左上
    cw, ch = 250, 170   # 单元尺寸

    cells = [
        # (col, row, 标题, 例子, 填充, 描边)
        (0, 0, "忠实 · 不更易", ["数学的等价改写（第 7 章）", "你只是把困难改了名"], FILLS[2], STROKES[2]),
        (1, 0, "理想代理 ✓", ["既忠实又更易", "罕见，全部手艺所在"], FILLS[1], STROKES[1]),
        (0, 1, "无用", ["不忠实又不更易", "没人会要"], "#f3f4f6", "#9ca3af"),
        (1, 1, "Goodhart（第 8 章）", ["更易却不忠实", "你优化代理，真目标却烂掉"], FILLS[3], STROKES[3]),
    ]
    for col, row, title, lines, fill, stroke in cells:
        x = x0 + col * cw
        y = y0 + row * ch
        s.rect(x, y, cw - 12, ch - 12, fill=fill, stroke=stroke, sw=2)
        s.text(x + (cw - 12) / 2, y + 34, title, size=17, weight="bold", fill=INK)
        s.textbox(x + (cw - 12) / 2, y + 72, lines, size=13.5, fill=MUTED)

    # 轴标签
    s.text(x0 + cw, y0 - 18, "更易（更可处理）→", size=14, fill=INK, weight="bold")
    # 纵轴：忠实
    s.parts.append(
        f'<text x="{x0 - 28}" y="{y0 + ch}" font-family="{__import__("svg").FONT}" '
        f'font-size="14" font-weight="bold" fill="{INK}" text-anchor="middle" '
        f'transform="rotate(-90 {x0 - 28} {y0 + ch})">忠实（真指向原目标）→</text>')

    s.save(os.path.abspath(OUT))
    return os.path.abspath(OUT)


if __name__ == "__main__":
    print("wrote", build())
