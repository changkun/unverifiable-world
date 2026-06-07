# -*- coding: utf-8 -*-
"""F4（第 5 章）：行动—观察—更新回路，以及把提问花在信息增益最大处。

生成 book/figures/f05-elicitation-loop.svg
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from svg import SVG, INK, MUTED, FILLS, STROKES

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "book", "figures", "f05-elicitation-loop.svg")


def build():
    W, H = 740, 500
    s = SVG(W, H)
    s.text(W / 2, 34, "把判断者放进回路：行动 — 观察 — 更新", size=21, weight="bold")

    bw, bh = 210, 76
    nodes = {
        "act": (70, 86, "① 行动 / 提问", STROKES[0], FILLS[0]),
        "obs": (W - 70 - bw, 86, "② 观察反应", STROKES[1], FILLS[1]),
        "upd": (W - 70 - bw, 320, "③ 更新对 θ 的信念", STROKES[4], FILLS[4]),
        "pick": (70, 320, "④ 选信息量最大的下一问", STROKES[2], FILLS[2]),
    }
    for x, y, label, st, fl in nodes.values():
        s.rect(x, y, bw, bh, fill=fl, stroke=st, sw=2)
        s.text(x + bw / 2, y + bh / 2, label, size=15, weight="bold", fill=INK)

    # 中心：隐藏目标
    cx, cy, cw, ch = W / 2 - 95, H / 2 - 34, 190, 68
    s.rect(cx, cy, cw, ch, fill="#f9fafb", stroke=MUTED, sw=1.5, rx=10)
    s.text(cx + cw / 2, cy + 26, "用户真实偏好 θ", size=15, weight="bold", fill=INK)
    s.text(cx + cw / 2, cy + 48, "（潜在 · 隐藏 · 测不准）", size=12.5, fill=MUTED)

    # 顺时针箭头
    s.arrow(70 + bw, 86 + bh / 2, W - 70 - bw, 86 + bh / 2, stroke=INK)          # act->obs
    s.arrow(W - 70 - bw / 2, 86 + bh, W - 70 - bw / 2, 320, stroke=INK)          # obs->upd
    s.arrow(W - 70 - bw, 320 + bh / 2, 70 + bw, 320 + bh / 2, stroke=INK)        # upd->pick
    s.arrow(70 + bw / 2, 320, 70 + bw / 2, 86 + bh, stroke=INK)                  # pick->act

    s.text(W / 2, H - 40, "提问有代价，故挑期望信息增益最大的那个：", size=14, fill=MUTED)
    s.text(W / 2, H - 16, "q* = argmaxq  I(θ ; yq)", size=15, fill=INK, weight="bold", italic=True)

    s.save(os.path.abspath(OUT))
    return os.path.abspath(OUT)


if __name__ == "__main__":
    print("wrote", build())
