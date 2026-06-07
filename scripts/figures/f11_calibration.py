# -*- coding: utf-8 -*-
"""F8（第 11 章）：标定的可靠性图。

对角线为完美标定（说 p，就真有 p 的比例发生）；过度自信的预测者偏离对角线。
生成 book/figures/f11-calibration.svg
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from svg import SVG, INK, MUTED, STROKES, FONT

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "book", "figures", "f11-calibration.svg")


def build():
    W, H = 620, 560
    s = SVG(W, H)
    s.text(W / 2, 32, "标定：可靠性图", size=21, weight="bold")
    s.text(W / 2, 56, "说有几成把握，就该真有几成成真", size=14, fill=MUTED)

    px, py, side = 110, 86, 380

    def X(p):
        return px + p * side

    def Y(f):
        return py + side - f * side

    # 坐标框
    s.rect(px, py, side, side, fill="#ffffff", stroke=INK, sw=1.5, rx=0)
    for v in (0.0, 0.25, 0.5, 0.75, 1.0):
        s.text(X(v), py + side + 18, f"{v:.2f}", size=11, fill=MUTED)
        s.text(px - 14, Y(v), f"{v:.2f}", size=11, fill=MUTED, anchor="end")

    # 完美标定对角线
    s.line(X(0), Y(0), X(1), Y(1), stroke=STROKES[1], sw=2.4, dash="6,5")
    s.text(X(0.7), Y(0.78), "完美标定", size=13, fill=STROKES[1], weight="bold")

    # 过度自信曲线：observed = 0.5 + (pred-0.5)*0.55（向 0.5 收缩）
    pts = [(X(p / 100), Y(0.5 + (p / 100 - 0.5) * 0.55)) for p in range(0, 101)]
    s.polyline(pts, stroke=STROKES[3], sw=2.6)
    s.text(X(0.74), Y(0.5 + 0.24 * 0.55) + 18, "过度自信", size=13, fill=STROKES[3], weight="bold")

    # 标注：高把握处实际偏低
    s.circle(X(0.9), Y(0.5 + 0.4 * 0.55), 4, fill=STROKES[3])
    s.text(X(0.88), Y(0.5 + 0.4 * 0.55) + 18, "报 0.9，实际约 0.72", size=11.5, fill=MUTED, anchor="end")

    s.text(px + side / 2, py + side + 40, "预测的概率 p", size=14, fill=INK, weight="bold")
    s.parts.append(
        f'<text x="{px-44}" y="{py+side/2}" font-family="{FONT}" font-size="14" '
        f'font-weight="bold" fill="{INK}" text-anchor="middle" '
        f'transform="rotate(-90 {px-44} {py+side/2})">实际发生的频率</text>')

    s.save(os.path.abspath(OUT))
    return os.path.abspath(OUT)


if __name__ == "__main__":
    print("wrote", build())
