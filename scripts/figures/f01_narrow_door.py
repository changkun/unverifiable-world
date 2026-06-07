# -*- coding: utf-8 -*-
"""F1（第 1 章）：验证廉价的窄门，与门外的四处裂口。

生成 book/figures/f01-narrow-door.svg
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from svg import SVG, INK, MUTED, FILLS, STROKES

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "book", "figures", "f01-narrow-door.svg")


def build():
    W, H = 780, 560
    s = SVG(W, H)
    s.text(W / 2, 34, "验证：廉价的窄门，与门外的四处裂口", size=22, weight="bold")

    # 窄门（绿色）
    dx, dy, dw, dh = 215, 66, 350, 120
    s.rect(dx, dy, dw, dh, fill=FILLS[1], stroke=STROKES[1], sw=2)
    s.text(dx + dw / 2, dy + 30, "验证廉价的窄门", size=18, weight="bold")
    s.text(dx + dw / 2, dy + 60, "封闭 · 有限 · 可判定 · 即时", size=14, fill=MUTED)
    s.text(dx + dw / 2, dy + 90, "算术 · 排序 · 核对收据 · 棋规合规", size=13.5, fill=MUTED)

    # 过渡
    s.arrow(W / 2, dy + dh, W / 2, dy + dh + 34, stroke=INK, sw=1.8)
    s.text(W / 2, dy + dh + 52, "走出窄门，完整验证成为奢侈品", size=14, fill=INK, weight="bold")

    # 四张裂口卡片（琥珀色）
    cards = [
        ("规模", ["路径爆炸 2ⁿ", "骑士资本 2012：", "45 分钟亏约 4.4 亿美元"]),
        ("开放世界", ["旧代码遇新世界", "阿丽亚娜 5（1996）", "737 MAX：346 人罹难"]),
        ("他人之心", ["目标锁在别人脑中", "潜在偏好测不准", "约四到五成初婚离婚"]),
        ("未来", ["休谟：归纳无保证", "过去推不出将来", "婚姻 · 投资 · 播种"]),
    ]
    cw, ch, gap = 168, 196, 20
    total = len(cards) * cw + (len(cards) - 1) * gap
    x0 = (W - total) / 2
    y0 = 320
    for i, (title, lines) in enumerate(cards):
        x = x0 + i * (cw + gap)
        s.rect(x, y0, cw, ch, fill=FILLS[2], stroke=STROKES[2], sw=2)
        s.text(x + cw / 2, y0 + 34, title, size=17, weight="bold", fill=INK)
        s.line(x + 24, y0 + 52, x + cw - 24, y0 + 52, stroke=STROKES[2], sw=1)
        s.textbox(x + cw / 2, y0 + 84, lines, size=13, fill=MUTED, lh=1.7)

    s.save(os.path.abspath(OUT))
    return os.path.abspath(OUT)


if __name__ == "__main__":
    print("wrote", build())
