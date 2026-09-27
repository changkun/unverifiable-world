# -*- coding: utf-8 -*-
"""F2（第 2 章）：不可验证的五种处境，判据 × 补救。

生成 book/figures/f02-five-faces.svg
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from svg import SVG, INK, MUTED, FILLS, STROKES

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "book", "figures", "f02-five-faces.svg")


def build(lang="zh"):
    en = (lang == "en")

    def t(zh, eng):
        return eng if en else zh

    rows = [
        (t("不可判定", "Undecidable"),
         t("原则上没有判定算法", ["in principle there exists", "no algorithm to decide it"]),
         t("永无完整解，只能退求切片", ["never a complete solution,", "only a retreat to slices"])),
        (t("难解", "Intractable"),
         t("有算法，但代价随规模爆炸", ["an algorithm exists, but its", "cost explodes with scale"]),
         t("用代价换精度，近似与随机", ["cost traded for precision,", "approximation, randomization"])),
        (t("部分可观测", "Partially observable"),
         t("据以验证的状态被隐藏", ["the state you would verify", "against is hidden from you"]),
         t("维持信念分布，主动探查", ["infer a belief distribution,", "probe actively"])),
        (t("预算受限", "Budget-constrained"),
         t("可验，但缺时间 / 算力 / 样本", ["verifiable, but you lack", "time / compute / samples"]),
         t("随资源消退，把预算最优分配", ["recedes as resources grow;", "allocate the budget optimally"])),
        (t("对抗", "Adversarial"),
         t("系统主动挫败你的验证", ["the system actively works", "to defeat your verification"]),
         t("当成博弈，最坏情形与随机化", ["a game of chess, won by", "strategy and randomization"])),
    ]

    W = 1060 if en else 860
    pad, header = 14, 56
    rh = 78 if en else 64
    H = pad * 2 + header + len(rows) * rh + 40
    s = SVG(W, H)
    s.text(W / 2, 30,
           t("不可验证的五种处境：判据与补救各不相同",
             "The five faces of unverifiability: their criteria and their remedies differ"),
           size=20 if en else 21, weight="bold")

    x0 = pad
    if en:
        cols = [(t("处境", "Face"), 200),
                (t("判据", "Criterion"), 416),
                (t("补救手段", "Remedy (the cure available)"), 416)]
    else:
        cols = [(t("处境", "Face"), 150),
                (t("判据", "Criterion"), 360),
                (t("补救手段", "Remedy (the cure available)"), 336)]
    y = 56
    # 表头
    cx = x0
    for name, w in cols:
        s.text(cx + w / 2, y + header / 2, name, size=15, weight="bold", fill=INK)
        cx += w
    y += header
    # 行
    crit_size = 13.5 if en else 14
    for i, (face, crit, cure) in enumerate(rows):
        cx = x0
        fill = FILLS[i % len(FILLS)]
        stroke = STROKES[i % len(STROKES)]
        s.rect(x0, y, sum(w for _, w in cols), rh, fill=fill, stroke=stroke, sw=1.6)
        # 处境
        s.text(cx + cols[0][1] / 2, y + rh / 2, face,
               size=15 if en else 16, weight="bold", fill=INK)
        cx += cols[0][1]
        _cell(s, cx + cols[1][1] / 2, y, rh, crit, crit_size)
        cx += cols[1][1]
        _cell(s, cx + cols[2][1] / 2, y, rh, cure, crit_size)
        y += rh

    s.text(W / 2, y + 24,
           t("把任一种错认成另一种，就会掏出错误的工具",
             "Mistake one face for another, and you reach for the wrong tool"),
           size=13.5, fill=MUTED, italic=True)

    out_path = os.path.abspath(OUT)
    if en:
        out_path = os.path.join(os.path.dirname(out_path), "en", os.path.basename(out_path))
    s.save(out_path)
    return out_path


def _cell(s, cx, y, rh, content, size):
    """单行字符串或多行列表，垂直居中于行内。"""
    if isinstance(content, str):
        s.text(cx, y + rh / 2, content, size=size, fill=MUTED)
        return
    lh = size * 1.45
    top = y + rh / 2 - (len(content) - 1) * lh / 2
    for i, ln in enumerate(content):
        s.text(cx, top + i * lh, ln, size=size, fill=MUTED)


if __name__ == "__main__":
    build("zh")
    print("en ->", build("en"))
