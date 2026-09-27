# -*- coding: utf-8 -*-
"""F1（第 1 章）：验证廉价的那一小块，与其外的四处裂口。

生成 book/figures/f01-narrow-door.svg
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from svg import SVG, INK, MUTED, FILLS, STROKES

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "book", "figures", "f01-narrow-door.svg")


def build(lang="zh"):
    en = (lang == "en")

    def t(zh, eng):
        return eng if en else zh

    W, H = 780, 560
    if en:
        W, H = 920, 600
    s = SVG(W, H)
    s.text(W / 2, 34, t("验证：廉价的那一小块，与其外的四处裂口",
                        "Verification: the cheap narrow door, and the four breaches outside"),
           size=22 if not en else 20, weight="bold")

    # 那一小块（绿色）
    dw, dh = 350, 120
    if en:
        dw = 460
    dx, dy = 215, 66
    dx = (W - dw) / 2
    s.rect(dx, dy, dw, dh, fill=FILLS[1], stroke=STROKES[1], sw=2)
    s.text(dx + dw / 2, dy + 30, t("验证廉价的那一小块", "The cheap narrow door of verification"),
           size=18, weight="bold")
    s.text(dx + dw / 2, dy + 60, t("封闭 · 有限 · 可判定 · 即时",
                                   "Closed · Finite · Decidable · Immediate"),
           size=14, fill=MUTED)
    s.text(dx + dw / 2, dy + 90, t("算术 · 排序 · 核对收据 · 棋规合规",
                                   "Arithmetic · Sorting · Checking a receipt · Legal moves"),
           size=13.5, fill=MUTED)

    # 过渡
    s.arrow(W / 2, dy + dh, W / 2, dy + dh + 34, stroke=INK, sw=1.8)
    s.text(W / 2, dy + dh + 52, t("走出这一小块，完整验证成为奢侈品",
                                  "Outside the door, complete verification becomes a luxury"),
           size=14, fill=INK, weight="bold")

    # 四张裂口卡片（琥珀色）
    cards = [
        (t("规模", "Scale"),
         [t("路径爆炸 2ⁿ", "Path explosion 2ⁿ"),
          t("骑士资本 2012：", "Knight Capital 2012:"),
          t("45 分钟亏约 4.4 亿美元", "~$440M lost in 45 min")]),
        (t("开放世界", "Open world"),
         [t("旧代码遇新世界", "Old code meets new world"),
          t("阿丽亚娜 5（1996）", "Ariane 5 (1996)"),
          t("737 MAX：346 人罹难", "737 MAX: 346 dead")]),
        (t("他人之心", "Other minds"),
         [t("目标锁在别人脑中", "Goal locked in another's head"),
          t("潜在偏好测不准", "Latent preferences unmeasurable"),
          t("约四到五成初婚离婚", "40-50% of first marriages divorce")]),
        (t("未来", "The future"),
         [t("休谟：归纳无保证", "Hume: induction has no guarantee"),
          t("过去推不出将来", "Past can't entail the future"),
          t("婚姻 · 投资 · 播种", "Marriage · Investment · Sowing")]),
    ]
    cw, ch, gap = 168, 196, 20
    body_size = 13
    if en:
        cw, ch, gap = 214, 200, 14
        body_size = 11.5
    total = len(cards) * cw + (len(cards) - 1) * gap
    x0 = (W - total) / 2
    y0 = 320
    if en:
        y0 = 350
    for i, (title, lines) in enumerate(cards):
        x = x0 + i * (cw + gap)
        s.rect(x, y0, cw, ch, fill=FILLS[2], stroke=STROKES[2], sw=2)
        s.text(x + cw / 2, y0 + 34, title, size=17, weight="bold", fill=INK)
        s.line(x + 24, y0 + 52, x + cw - 24, y0 + 52, stroke=STROKES[2], sw=1)
        s.textbox(x + cw / 2, y0 + 84, lines, size=body_size, fill=MUTED, lh=1.7)

    out_path = os.path.abspath(OUT)
    if en:
        out_path = os.path.join(os.path.dirname(out_path), "en", os.path.basename(out_path))
    s.save(out_path)
    return out_path


if __name__ == "__main__":
    build("zh")
    print("en ->", build("en"))
