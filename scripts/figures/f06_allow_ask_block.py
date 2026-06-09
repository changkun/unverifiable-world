# -*- coding: utf-8 -*-
"""F5（第 6 章）：允许 / 询问 / 阻止的分级自治。

横轴为系统对自身判断的信心 p，纵轴为该步潜在危害 c。
生成 book/figures/f06-allow-ask-block.svg
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from svg import SVG, INK, MUTED

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "book", "figures", "f06-allow-ask-block.svg")

RED_F, RED_S = "#fee2e2", "#ef4444"
AMB_F, AMB_S = "#fef3c7", "#d97706"
GRN_F, GRN_S = "#dcfce7", "#16a34a"


def build(lang="zh"):
    en = (lang == "en")

    def t(zh, eng):
        return eng if en else zh

    W, H = 720, 480
    if en:
        W = 760
    s = SVG(W, H)
    s.text(W / 2, 32, t("允许 / 询问 / 阻止：按信心与危害分级自治",
                        "Allow / ask / block: graded autonomy by confidence and harm"),
           size=20 if not en else 17, weight="bold")

    px, py, pw, ph = 90, 64, 560, 340
    if en:
        pw = 580
    x_lo = px + pw * 0.36
    x_hi = px + pw * 0.66
    y_cmax = py + ph * 0.42  # 危害上限（其上一律阻止）

    # 阻止：危害过高（顶部整条）
    s.rect(px, py, pw, y_cmax - py, fill=RED_F, stroke="none", rx=0)
    # 下半部分按信心分三段
    s.rect(px, y_cmax, x_lo - px, py + ph - y_cmax, fill=RED_F, stroke="none", rx=0)        # 信心过低 -> 阻止
    s.rect(x_lo, y_cmax, x_hi - x_lo, py + ph - y_cmax, fill=AMB_F, stroke="none", rx=0)    # 中等 -> 询问
    s.rect(x_hi, y_cmax, px + pw - x_hi, py + ph - y_cmax, fill=GRN_F, stroke="none", rx=0)  # 高且低危 -> 允许

    # 边框与分隔
    s.rect(px, py, pw, ph, fill="none", stroke=INK, sw=1.5, rx=0)
    s.line(px, y_cmax, px + pw, y_cmax, stroke=MUTED, sw=1.2, dash="5,4")
    s.line(x_lo, y_cmax, x_lo, py + ph, stroke=MUTED, sw=1.2, dash="5,4")
    s.line(x_hi, y_cmax, x_hi, py + ph, stroke=MUTED, sw=1.2, dash="5,4")

    # 区域标签
    s.text(px + pw / 2, py + (y_cmax - py) / 2, t("阻止 BLOCK（危害过大）", "BLOCK (harm too high)"),
           size=16, weight="bold", fill=RED_S)
    s.text((px + x_lo) / 2, (y_cmax + py + ph) / 2, t("阻止", "block"), size=14, weight="bold", fill=RED_S)
    s.text((x_lo + x_hi) / 2, (y_cmax + py + ph) / 2, t("询问 ASK", "ask"), size=15, weight="bold", fill=AMB_S)
    s.text((x_hi + px + pw) / 2, (y_cmax + py + ph) / 2, t("允许 ALLOW", "allow"), size=15, weight="bold", fill=GRN_S)

    # 轴
    s.text(px + pw / 2, py + ph + 34, t("信心 p  →", "confidence  p  →"), size=14, fill=INK, weight="bold")
    s.text(x_lo, py + ph + 18, t("τlo", "τlo"), size=12, fill=MUTED)
    s.text(x_hi, py + ph + 18, t("τhi", "τhi"), size=12, fill=MUTED)
    # 纵轴标题（旋转）
    from svg import FONT
    s.parts.append(
        f'<text x="{px-26}" y="{py+ph/2}" font-family="{FONT}" font-size="14" '
        f'font-weight="bold" fill="{INK}" text-anchor="middle" '
        f'transform="rotate(-90 {px-26} {py+ph/2})">{t("潜在危害 c  →", "potential harm  c  →")}</text>')
    s.text(px - 10, y_cmax, t("cmax", "cmax"), size=12, fill=MUTED, anchor="end")

    out_path = os.path.abspath(OUT)
    if en:
        out_path = os.path.join(os.path.dirname(out_path), "en", os.path.basename(out_path))
    s.save(out_path)
    return out_path


if __name__ == "__main__":
    build("zh")
    print("en ->", build("en"))
