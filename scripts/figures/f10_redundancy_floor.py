# -*- coding: utf-8 -*-
"""F7（第 10 章）：冗余的相关性地板。

把 N 个判断平均，归一化方差 = ρ + (1-ρ)/N。相关 ρ>0 时，方差不再趋于 0，
而是卡在地板 ρ 上。生成 book/figures/f10-redundancy-floor.svg
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from svg import SVG, INK, MUTED, STROKES, FONT

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "book", "figures", "f10-redundancy-floor.svg")


def build(lang="zh"):
    en = (lang == "en")

    def t(zh, eng):
        return eng if en else zh

    W, H = 740, 470
    if en:
        W, H = 820, 470
    s = SVG(W, H)
    s.text(W / 2, 32,
           t("冗余的相关性地板：一旦存在相关，增加判断者也无法越过",
             "The correlation floor of redundancy: once correlation is present, piling on more judges cannot get past it"),
           size=t(19, 14.5), weight="bold")

    px, py, pw, ph = 84, 64, 580, 320
    if en:
        px, py, pw, ph = 92, 70, 600, 314
    Nmax = 40

    def X(n):
        return px + (n - 1) / (Nmax - 1) * pw

    def Y(v):
        return py + ph - v * ph  # v in [0,1]

    # 轴
    s.line(px, py, px, py + ph, stroke=INK, sw=1.5)
    s.line(px, py + ph, px + pw, py + ph, stroke=INK, sw=1.5)
    for v in (0.0, 0.3, 0.6, 1.0):
        s.line(px - 5, Y(v), px, Y(v), stroke=INK, sw=1)
        s.text(px - 12, Y(v), f"{v:.1f}", size=11, fill=MUTED, anchor="end")

    rhos = [(0.0, STROKES[1], t("ρ = 0（真独立）", "ρ = 0 (truly independent)")),
            (0.1, STROKES[2], "ρ = 0.1"),
            (0.3, STROKES[3], t("ρ = 0.3（暗中相关）", "ρ = 0.3 (secretly correlated)"))]
    for rho, col, _ in rhos:
        pts = [(X(n), Y(rho + (1 - rho) / n)) for n in range(1, Nmax + 1)]
        s.polyline(pts, stroke=col, sw=2.6)
        if rho > 0:  # 地板虚线
            s.line(X(1), Y(rho), X(Nmax), Y(rho), stroke=col, sw=1, dash="4,4")

    # 标签
    s.text(X(Nmax) - 4, Y(0.0) - 14, t("ρ=0：→ 0", "ρ=0: → 0"), size=12.5, fill=STROKES[1], anchor="end")
    s.text(X(Nmax) - 4, Y(0.1) - 10, t("地板 0.1", "floor 0.1"), size=12, fill=STROKES[2], anchor="end")
    s.text(X(Nmax) - 4, Y(0.3) - 10, t("地板 0.3", "floor 0.3"), size=12, fill=STROKES[3], anchor="end")

    s.text(px + pw / 2, py + ph + 34, t("判断者数目 N  →", "number of judges N  →"), size=14, fill=INK, weight="bold")
    s.parts.append(
        f'<text x="{px-40}" y="{py+ph/2}" font-family="{FONT}" font-size="13.5" '
        f'font-weight="bold" fill="{INK}" text-anchor="middle" '
        f'transform="rotate(-90 {px-40} {py+ph/2})">'
        f'{t("归一化方差 Var/σ²  →", "normalized variance Var/σ²  →")}</text>')

    s.text(W / 2, H - 14,
           t("Var/σ² = ρ + (1−ρ)/N，N→∞ 时趋于 ρ，而非 0",
             "Var/σ² = ρ + (1−ρ)/N → ρ as N→∞, not 0"),
           size=13, fill=MUTED, italic=True)

    out_path = os.path.abspath(OUT)
    if en:
        out_path = os.path.join(os.path.dirname(out_path), "en", os.path.basename(out_path))
    s.save(out_path)
    return out_path


if __name__ == "__main__":
    build("zh")
    print("en ->", build("en"))
