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


def build():
    W, H = 900, 540
    s = SVG(W, H)
    s.text(W / 2, 34, "八招，八处杠杆：作用于风险分解的不同部位", size=21, weight="bold")
    s.text(W / 2, 66, "风险 ≈ P(失败) × 代价(失败)　〔在信息预算 B 之下〕", size=17, weight="bold", fill=INK)

    def card(x, y, w, h, header, lines, fi, si):
        s.rect(x, y, w, h, fill=FILLS[fi], stroke=STROKES[si], sw=2)
        s.text(x + w / 2, y + 28, header, size=15, weight="bold", fill=INK)
        s.line(x + 20, y + 44, x + w - 20, y + 44, stroke=STROKES[si], sw=1)
        s.textbox(x + w / 2, y + 68, lines, size=13, fill=MUTED, lh=1.6)

    y1, h1 = 96, 168
    card(40, y1, 470, h1, "作用于 P(失败)", [
        "证书与界 —— 在能查的切片上压低",
        "神谕入回路 —— 借来你没有的验证能力",
        "冗余共识 —— 让多个判断的失败去相关",
        "标定 —— 把 P(失败) 变成已知、可定价",
    ], 0, 0)
    card(530, y1, 150, h1, "作用于 代价(失败)", [
        "衰减围栏", "缩小失败的", "爆炸半径",
    ], 3, 3)
    card(700, y1, 160, h1, "作用于 信息预算 B", [
        "最优筛查", "把查验最优地", "分配出去",
    ], 2, 2)

    y2, h2 = y1 + h1 + 28, 92
    card(40, y2, 400, h2, "改写「失败」的定义本身", [
        "代理替换 —— 换一个你度量、优化的目标",
    ], 4, 4)
    card(460, y2, 400, h2, "改变检查的时间位置", [
        "留痕审计 —— 把检查从事前挪到事后",
    ], 1, 1)

    s.text(W / 2, H - 28, "命题：若这些就是全部杠杆，收敛便被解释。", size=13.5, fill=INK, italic=True)
    s.text(W / 2, H - 8, "（这是候选的组织结构，不是定理，见第 14 章）", size=12.5, fill=MUTED, italic=True)
    s.save(os.path.abspath(OUT))
    return os.path.abspath(OUT)


if __name__ == "__main__":
    print("wrote", build())
