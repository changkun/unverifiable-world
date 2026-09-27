# -*- coding: utf-8 -*-
"""F10（第 13 章）：八招映射到风险分解的不同部位。

风险 ≈ P(失败) × 代价(失败)，在信息预算 B 之下。每一招拉动其中一处杠杆。
生成 book/figures/f13-eight-levers.svg
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from svg import SVG, INK, MUTED, FILLS, STROKES

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "book", "figures", "f13-eight-levers.svg")


def build(lang="zh"):
    en = (lang == "en")

    def t(zh, eng):
        return eng if en else zh

    W, H = 900, 540
    if en:
        W, H = 1180, 540
    s = SVG(W, H)
    s.text(W / 2, 34, t("八招，八处杠杆：作用于风险分解的不同部位",
                        "Eight moves, eight levers: acting on different parts of the risk decomposition"),
           size=21, weight="bold")
    s.text(W / 2, 66, t("风险 ≈ P(失败) × 代价(失败)　〔在信息预算 B 之下〕",
                        "Risk ≈ Pr(fail) × Cost(fail)　[under an information budget B]"),
           size=17, weight="bold", fill=INK)

    def card(x, y, w, h, header, lines, fi, si, hsize=15, lsize=13, lh=1.6):
        s.rect(x, y, w, h, fill=FILLS[fi], stroke=STROKES[si], sw=2)
        s.text(x + w / 2, y + 28, header, size=hsize, weight="bold", fill=INK)
        s.line(x + 20, y + 44, x + w - 20, y + 44, stroke=STROKES[si], sw=1)
        s.textbox(x + w / 2, y + 68, lines, size=lsize, fill=MUTED, lh=lh)

    if not en:
        y1, h1 = 96, 168
        card(40, y1, 470, h1, "作用于 P(失败)", [
            "证书与界：在能查的切片上压低",
            "神谕入回路：借来你没有的验证能力",
            "冗余共识：让多个判断的失败去相关",
            "校准：把 P(失败) 变成已知、可定价",
        ], 0, 0)
        card(530, y1, 150, h1, "作用于 代价(失败)", [
            "限损围栏", "缩小失败的", "爆炸半径",
        ], 3, 3)
        card(700, y1, 160, h1, "作用于 信息预算 B", [
            "最优筛查", "把查验最优地", "分配出去",
        ], 2, 2)

        y2, h2 = y1 + h1 + 28, 92
        card(40, y2, 400, h2, "改写「失败」的定义本身", [
            "代理替换：换一个你度量、优化的目标",
        ], 4, 4)
        card(460, y2, 400, h2, "改变检查的时间位置", [
            "留痕审计：把检查从事前挪到事后",
        ], 1, 1)
    else:
        y1, h1 = 96, 244
        # Card 1: acts on Pr(fail). Each move on 2 lines (name + condensed gloss).
        card(40, y1, 560, h1, "acts on Pr(fail)", [
            "certificate / bound", "  press it near zero on one checkable slice",
            "oracle in the loop", "  borrow a verifying power you lack",
            "redundancy / consensus", "  make several judgments' failures decorrelate",
            "calibration", "  make Pr(fail) known and priceable",
        ], 0, 0, hsize=16, lsize=14, lh=1.55)
        # Card 2: acts on Cost(fail)
        card(620, y1, 270, h1, "acts on Cost(fail)", [
            "containment /", "fencing", "",
            "shrink the blast", "radius of failure",
        ], 3, 3, hsize=16, lsize=14, lh=1.7)
        # Card 3: acts on the information budget B
        card(910, y1, 230, h1, "acts on the budget B", [
            "optimal screening", "",
            "allocate the", "information budget", "where it pays most",
        ], 2, 2, hsize=16, lsize=14, lh=1.7)

        y2, h2 = y1 + h1 + 28, 100
        card(40, y2, 560, h2, "rewrites the definition of “failure”", [
            "proxy substitution: swap the target", "you measure and optimize",
        ], 4, 4, hsize=16, lsize=14, lh=1.55)
        card(620, y2, 520, h2, "shifts the timing of checking", [
            "audit trail: move checking from", "before the fact to after it",
        ], 1, 1, hsize=16, lsize=14, lh=1.55)

    s.text(W / 2, H - 28, t("命题：若这些就是全部杠杆，收敛便被解释。",
                            "Proposition: if these are all the levers, the convergence is explained."),
           size=13.5, fill=INK, italic=True)
    s.text(W / 2, H - 8, t("（这是候选的组织结构，不是定理，见第 14 章）",
                           "(a candidate organizing scheme, not a theorem; see Chapter 14)"),
           size=12.5, fill=MUTED, italic=True)

    out_path = os.path.abspath(OUT)
    if en:
        out_path = os.path.join(os.path.dirname(out_path), "en", os.path.basename(out_path))
    s.save(out_path)
    return out_path


if __name__ == "__main__":
    build("zh")
    print("en ->", build("en"))
