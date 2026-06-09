# -*- coding: utf-8 -*-
"""F3（第 3 章）：证实与证伪的不对称。

生成 book/figures/f03-falsification.svg
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from svg import SVG, INK, MUTED, FILLS, STROKES

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "book", "figures", "f03-falsification.svg")


def build(lang="zh"):
    en = (lang == "en")

    def t(zh, eng):
        return eng if en else zh

    W, H = 800, 430
    if en:
        W = 880
    s = SVG(W, H)
    s.text(W / 2, 34, t("证实与证伪的不对称",
                        "The asymmetry between verification and falsification"),
           size=22 if not en else 21, weight="bold")
    s.text(W / 2, 60, t("命题：「所有天鹅都是白的」",
                        'Statement: "All swans are white"'), size=15, fill=MUTED)

    bw, bh, by = 350, 250, 90
    if en:
        bw = 410
    lx, rx = 20, W - 20 - bw

    # 左：证实之路（够不到）
    s.rect(lx, by, bw, bh, fill=FILLS[2], stroke=STROKES[2], sw=2)
    s.text(lx + bw / 2, by + 32, t("证实之路", "The path to verification"),
           size=18, weight="bold")
    s.textbox(lx + bw / 2, by + 74, [
        t("见 1 只白天鹅 ✓", "See 1 white swan ✓"),
        t("见 100 万只白天鹅 ✓", "See 1,000,000 white swans ✓"),
        t("见 10 亿只白天鹅 ✓", "See 1,000,000,000 white swans ✓"),
        t("…… 仍未证实", "…… still not verified"),
    ], size=14, fill=MUTED, lh=1.7)
    if en:
        s.textbox(lx + bw / 2, by + bh - 46, [
            'The quantifier "all" demands checking',
            "infinitely many cases, never reached",
        ], size=12.5, fill=STROKES[3], lh=1.35)
    else:
        s.text(lx + bw / 2, by + bh - 30, "量词「所有」要检遍无穷，永远够不到",
               size=13, fill=STROKES[3])

    # 右：证伪之路（一击）
    s.rect(rx, by, bw, bh, fill=FILLS[1], stroke=STROKES[1], sw=2)
    s.text(rx + bw / 2, by + 32, t("证伪之路", "The path to falsification"),
           size=18, weight="bold")
    s.textbox(rx + bw / 2, by + 90, [
        t("见 1 只黑天鹅 ✗", "See 1 black swan ✗"),
        t("命题当即被推翻", "The statement is overturned completely"),
    ], size=15, fill=INK, lh=1.9)
    if en:
        s.text(rx + bw / 2, by + bh - 30,
               "A single counterexample suffices (W. Australia, 1697)",
               size=12.5, fill=STROKES[1])
    else:
        s.text(rx + bw / 2, by + bh - 30, "一个反例足矣（澳洲，1697 年）",
               size=13, fill=STROKES[1])

    # 中间不对称标记
    s.text(W / 2, by + bh / 2, "≠", size=30, weight="bold", fill=INK)

    s.text(W / 2, H - 18, t("科学只能不被证伪，不能被证实",
                            "Science can never be verified, only left unfalsified"),
           size=14, fill=MUTED, italic=True)

    out_path = os.path.abspath(OUT)
    if en:
        out_path = os.path.join(os.path.dirname(out_path), "en", os.path.basename(out_path))
    s.save(out_path)
    return out_path


if __name__ == "__main__":
    build("zh")
    print("en ->", build("en"))
