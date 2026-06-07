# -*- coding: utf-8 -*-
"""F3（第 3 章）：证实与证伪的不对称。

生成 book/figures/f03-falsification.svg
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from svg import SVG, INK, MUTED, FILLS, STROKES

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "book", "figures", "f03-falsification.svg")


def build():
    W, H = 800, 430
    s = SVG(W, H)
    s.text(W / 2, 34, "证实与证伪的不对称", size=22, weight="bold")
    s.text(W / 2, 60, "命题：「所有天鹅都是白的」", size=15, fill=MUTED)

    bw, bh, by = 350, 250, 90
    lx, rx = 20, W - 20 - bw

    # 左：证实之路（够不到）
    s.rect(lx, by, bw, bh, fill=FILLS[2], stroke=STROKES[2], sw=2)
    s.text(lx + bw / 2, by + 32, "证实之路", size=18, weight="bold")
    s.textbox(lx + bw / 2, by + 74, [
        "见 1 只白天鹅 ✓",
        "见 100 万只白天鹅 ✓",
        "见 10 亿只白天鹅 ✓",
        "…… 仍未证实",
    ], size=14, fill=MUTED, lh=1.7)
    s.text(lx + bw / 2, by + bh - 30, "量词「所有」要检遍无穷，永远够不到", size=13, fill=STROKES[3])

    # 右：证伪之路（一击）
    s.rect(rx, by, bw, bh, fill=FILLS[1], stroke=STROKES[1], sw=2)
    s.text(rx + bw / 2, by + 32, "证伪之路", size=18, weight="bold")
    s.textbox(rx + bw / 2, by + 90, [
        "见 1 只黑天鹅 ✗",
        "命题当即被推翻",
    ], size=15, fill=INK, lh=1.9)
    s.text(rx + bw / 2, by + bh - 30, "一个反例足矣（澳洲，1697 年）", size=13, fill=STROKES[1])

    # 中间不对称标记
    s.text(W / 2, by + bh / 2, "≠", size=30, weight="bold", fill=INK)

    s.text(W / 2, H - 18, "科学只能不被证伪，不能被证实", size=14, fill=MUTED, italic=True)
    s.save(os.path.abspath(OUT))
    return os.path.abspath(OUT)


if __name__ == "__main__":
    print("wrote", build())
