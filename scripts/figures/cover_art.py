# -*- coding: utf-8 -*-
"""封面图：在雾里操舵的罗盘 / 星盘环。

外圈刻度向下半圈渐隐入「雾」，几点散落代表不可验证的未知；指针仍指向前方。
透明背景，叠在深色书封上。生成 book/figures/cover-art.svg
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from svg import SVG

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "book", "figures", "cover-art.svg")

GOLD = "#d9c4a0"
GOLD2 = "#bfa775"
BLUE = "#9fb2d4"


def build():
    W = H = 300
    cx = cy = 150
    s = SVG(W, H, bg=None)

    def ring(r, op, sw=1.4, col=GOLD):
        s.parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" '
                       f'stroke-width="{sw}" opacity="{op}"/>')

    # 同心环（星盘）
    ring(122, 0.22, 1.1)
    ring(96, 0.45, 1.3)
    ring(66, 0.7, 1.4)

    # 外圈刻度：上半圈清晰，下半圈渐隐入雾
    for k in range(72):
        a = math.radians(k * 5 - 90)
        # 透明度：上方(指向 -90°附近) 高，下方低
        vertical = math.sin(a)          # -1 底部 .. +1 顶部
        op = max(0.05, 0.55 * (0.5 + 0.5 * (-vertical)))  # 顶部约0.55，底部约0.05
        major = (k % 9 == 0)
        r0 = 122
        r1 = 122 + (12 if major else 6)
        x0, y0 = cx + r0 * math.cos(a), cy + r0 * math.sin(a)
        x1, y1 = cx + r1 * math.cos(a), cy + r1 * math.sin(a)
        s.parts.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" '
                       f'stroke="{GOLD}" stroke-width="{1.6 if major else 1}" opacity="{op:.2f}"/>')

    # 指针（细长菱形），略偏「东北」，指向前方
    ang = math.radians(-64)
    L, w = 86, 9
    px, py = math.cos(ang), math.sin(ang)        # 方向
    qx, qy = -py, px                              # 垂直
    tip = (cx + L * px, cy + L * py)
    tail = (cx - 70 * px, cy - 70 * py)
    left = (cx + w * qx, cy + w * qy)
    right = (cx - w * qx, cy - w * qy)
    # 北半（指向）实心金，南半描边
    s.parts.append(f'<polygon points="{tip[0]:.1f},{tip[1]:.1f} {left[0]:.1f},{left[1]:.1f} '
                   f'{right[0]:.1f},{right[1]:.1f}" fill="{GOLD}" opacity="0.95"/>')
    s.parts.append(f'<polygon points="{tail[0]:.1f},{tail[1]:.1f} {left[0]:.1f},{left[1]:.1f} '
                   f'{right[0]:.1f},{right[1]:.1f}" fill="none" stroke="{BLUE}" '
                   f'stroke-width="1.3" opacity="0.8"/>')
    # 中心枢
    s.parts.append(f'<circle cx="{cx}" cy="{cy}" r="5.5" fill="{GOLD2}"/>')
    s.parts.append(f'<circle cx="{cx}" cy="{cy}" r="11" fill="none" stroke="{GOLD}" '
                   f'stroke-width="1.2" opacity="0.7"/>')

    # 雾里散落的未知（下半圈外的点，越往下越淡）
    pts = [(232, 196, .5), (60, 214, .42), (250, 150, .35), (40, 150, .3),
           (210, 250, .22), (96, 256, .2), (150, 270, .16), (270, 220, .14)]
    for x, y, op in pts:
        s.parts.append(f'<circle cx="{x}" cy="{y}" r="2.4" fill="{BLUE}" opacity="{op}"/>')

    # 一缕地平线 / 雾带（极淡）
    for i, yy in enumerate((242, 252, 262)):
        s.parts.append(f'<line x1="36" y1="{yy}" x2="264" y2="{yy}" stroke="{BLUE}" '
                       f'stroke-width="1" opacity="{0.12 - i*0.03:.2f}"/>')

    s.save(os.path.abspath(OUT))
    return os.path.abspath(OUT)


if __name__ == "__main__":
    print("wrote", build())
