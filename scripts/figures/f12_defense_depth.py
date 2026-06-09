# -*- coding: utf-8 -*-
"""F9（第 12 章）：纵深防御的瑞士奶酪模型。

每层防护都有漏洞；唯当各层漏洞偶然对齐，失败才贯穿而出（Reason 1990）。
生成 book/figures/f12-defense-depth.svg
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from svg import SVG, INK, MUTED, STROKES

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "book", "figures", "f12-defense-depth.svg")

CHEESE_F, CHEESE_S = "#fef3c7", "#d9a206"
BG = "#ffffff"


def build(lang="zh"):
    en = (lang == "en")

    def t(zh, eng):
        return eng if en else zh

    W, H = 780, 420
    if en:
        W = 900
    s = SVG(W, H)
    s.text(W / 2, 32,
           t("纵深防御与瑞士奶酪模型：漏洞对齐，失败贯穿",
             "Defense in depth and the Swiss cheese model: when the holes line up, failure runs straight through"),
           size=t(19, 17), weight="bold")

    sy, sh, sw = 78, 250, 120
    xs = [90, 260, 430, 600]
    if en:
        sw = 150
        xs = [60, 270, 480, 690]
    labels = [
        t("最小权限", "least privilege"),
        t("沙箱隔离", "sandbox isolation"),
        t("职责分离", "separation of duties"),
        t("审计告警", "audit & alerting"),
    ]
    align_y = sy + 175  # 对齐的那条「贯穿线」

    # 先画奶酪片
    for i, x in enumerate(xs):
        s.rect(x, sy, sw, sh, fill=CHEESE_F, stroke=CHEESE_S, sw=2)
        s.text(x + sw / 2, sy + sh + 22, labels[i], size=13, fill=MUTED)

    # 漏洞（白色圆，盖在奶酪上）。每片都在 align_y 处开一个洞 -> 对齐
    holes = [
        [sy + 60, sy + 120, align_y],
        [sy + 95, align_y, sy + 215],
        [sy + 50, align_y, sy + 200],
        [sy + 130, align_y, sy + 225],
    ]
    for i, x in enumerate(xs):
        for hy in holes[i]:
            s.circle(x + sw / 2, hy, 17, fill=BG, stroke=CHEESE_S, sw=1.2)

    # 贯穿的危险轨迹（红箭头穿过对齐的洞）
    s.arrow(40, align_y, W - 30, align_y, stroke=STROKES[3], sw=2.6)
    s.text(40, align_y - 16, t("危险", "hazard"), size=13, fill=STROKES[3], weight="bold", anchor="start")
    s.text(W - 30, align_y - 16, t("事故", "accident"), size=13, fill=STROKES[3], weight="bold", anchor="end")

    s.text(W / 2, H - 16,
           t("层层独立时漏洞难对齐；共模故障让多层一齐失守（如主备电源同遭水淹）",
             "Independent layers rarely align; a common-mode failure drowns many at once (e.g. main and backup power flooded together)"),
           size=12.5, fill=MUTED, italic=True)

    out_path = os.path.abspath(OUT)
    if en:
        out_path = os.path.join(os.path.dirname(out_path), "en", os.path.basename(out_path))
    s.save(out_path)
    return out_path


if __name__ == "__main__":
    build("zh")
    print("en ->", build("en"))
