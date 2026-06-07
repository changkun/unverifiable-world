# -*- coding: utf-8 -*-
"""F2（第 2 章）：不可验证的五副面孔，判据 × 解药。

生成 book/figures/f02-five-faces.svg
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from svg import SVG, INK, MUTED, FILLS, STROKES

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "book", "figures", "f02-five-faces.svg")

ROWS = [
    ("不可判定", "原则上没有判定算法", "永无完整解，只能退求切片"),
    ("难解", "有算法，但代价随规模爆炸", "用代价换精度，近似与随机"),
    ("部分可观测", "据以验证的状态被隐藏", "维持信念分布，主动探查"),
    ("预算受限", "可验，但缺时间 / 算力 / 样本", "随资源消退，把预算最优分配"),
    ("对抗", "系统主动挫败你的验证", "当成博弈，最坏情形与随机化"),
]


def build():
    W = 860
    pad, rh, header = 14, 64, 56
    H = pad * 2 + header + len(ROWS) * rh + 40
    s = SVG(W, H)
    s.text(W / 2, 30, "不可验证的五副面孔：判据与解药各不相同", size=21, weight="bold")

    x0 = pad
    cols = [("面孔", 150), ("判据", 360), ("解药（可得的补救）", 336)]
    y = 56
    # 表头
    cx = x0
    for name, w in cols:
        s.text(cx + w / 2, y + header / 2, name, size=15, weight="bold", fill=INK)
        cx += w
    y += header
    # 行
    for i, (face, crit, cure) in enumerate(ROWS):
        cx = x0
        fill = FILLS[i % len(FILLS)]
        stroke = STROKES[i % len(STROKES)]
        s.rect(x0, y, sum(w for _, w in cols), rh, fill=fill, stroke=stroke, sw=1.6)
        # 面孔
        s.text(cx + cols[0][1] / 2, y + rh / 2, face, size=16, weight="bold", fill=INK)
        cx += cols[0][1]
        s.text(cx + cols[1][1] / 2, y + rh / 2, crit, size=14, fill=MUTED)
        cx += cols[1][1]
        s.text(cx + cols[2][1] / 2, y + rh / 2, cure, size=14, fill=MUTED)
        y += rh

    s.text(W / 2, y + 24, "把任一副错认成另一副，就会掏出错误的工具", size=13.5, fill=MUTED, italic=True)
    s.save(os.path.abspath(OUT))
    return os.path.abspath(OUT)


if __name__ == "__main__":
    print("wrote", build())
