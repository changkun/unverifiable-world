# -*- coding: utf-8 -*-
"""F-Goodhart（第 8 / 11 章）：代理指标的过度优化崩塌。

随着对代理指标的优化力度加大，代理持续上升，真目标却先升后降，
在某一点之后二者脱钩。生成 book/figures/f08-goodhart-curve.svg
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from svg import SVG, INK, MUTED, STROKES, FONT

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "book", "figures", "f08-goodhart-curve.svg")


def build(lang="zh"):
    en = (lang == "en")

    def t(zh, eng):
        return eng if en else zh

    W, H = 740, 470
    if en:
        W = 820
    s = SVG(W, H)
    s.text(W / 2, 32, t("Goodhart 崩塌：优化代理，真目标却脱钩",
                        "The Goodhart collapse: optimize the proxy, the true target uncouples"),
           size=t(20, 18), weight="bold")

    px, py, pw, ph = 90, 64, 560, 320

    def X(t_):
        return px + t_ * pw

    def Y(v):
        return py + ph - v * ph

    # 坐标轴
    s.line(px, py, px, py + ph, stroke=INK, sw=1.5)
    s.line(px, py + ph, px + pw, py + ph, stroke=INK, sw=1.5)

    N = 100
    proxy = [(X(i / N), Y(min(1.0, (i / N) ** 0.6))) for i in range(N + 1)]
    true = [(X(i / N), Y(max(0.0, min(1.0, 4.0 * (i / N) * (1 - (i / N)))))) for i in range(N + 1)]
    s.polyline(proxy, stroke=STROKES[3], sw=2.6)   # 代理（红）
    s.polyline(true, stroke=STROKES[1], sw=2.6)     # 真目标（绿）

    # 脱钩点（真目标峰值 t=0.5）
    tpk = 0.5
    s.line(X(tpk), py, X(tpk), py + ph, stroke=MUTED, sw=1.2, dash="5,4")
    s.text(X(tpk), py - 6, t("脱钩点", "Decoupling point"), size=12.5, fill=MUTED)

    # 曲线标签
    s.text(X(0.86), Y((0.86) ** 0.6) - 16, t("代理指标", "Proxy metric"),
           size=14, weight="bold", fill=STROKES[3])
    s.text(X(0.84), Y(4.0 * 0.84 * (1 - 0.84)) + 20, t("真目标", "True target"),
           size=14, weight="bold", fill=STROKES[1])

    # 轴标题
    s.text(px + pw / 2, py + ph + 34, t("对代理指标的优化力度  →",
                                        "Optimization pressure on the proxy metric  →"),
           size=14, fill=INK, weight="bold")
    s.parts.append(
        f'<text x="{px-24}" y="{py+ph/2}" font-family="{FONT}" font-size="14" '
        f'font-weight="bold" fill="{INK}" text-anchor="middle" '
        f'transform="rotate(-90 {px-24} {py+ph/2})">{t("表现（归一化）  →", "Performance (normalized)  →")}</text>')

    s.text(W / 2, H - 14, t("指标与真目标的相关只在脱钩点之前成立",
                            "The metric correlates with the true target only before the decoupling point"),
           size=13, fill=MUTED, italic=True)

    out_path = os.path.abspath(OUT)
    if en:
        out_path = os.path.join(os.path.dirname(out_path), "en", os.path.basename(out_path))
    s.save(out_path)
    return out_path


if __name__ == "__main__":
    build("zh")
    print("en ->", build("en"))
