# -*- coding: utf-8 -*-
"""F4（第 5 章）：行动—观察—更新回路，以及把提问花在信息增益最大处。

生成 book/figures/f05-elicitation-loop.svg
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from svg import SVG, INK, MUTED, FILLS, STROKES

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "book", "figures", "f05-elicitation-loop.svg")


def build(lang="zh"):
    en = (lang == "en")

    def t(zh, eng):
        return eng if en else zh

    W, H = 740, 500
    if en:
        W = 820
    s = SVG(W, H)
    s.text(W / 2, 34, t("把判断者放进回路：行动 — 观察 — 更新",
                        "Putting the judge in the loop: act, observe, update"),
           size=21 if not en else 19, weight="bold")

    bw, bh = 210, 76
    if en:
        bw = 288
    nodes = {
        "act": (70, 86, t("① 行动 / 提问", "① Act / ask"), STROKES[0], FILLS[0]),
        "obs": (W - 70 - bw, 86, t("② 观察反应", "② Observe the reaction"), STROKES[1], FILLS[1]),
        "upd": (W - 70 - bw, 320, t("③ 更新对 θ 的信念", "③ Update belief about θ"), STROKES[4], FILLS[4]),
        "pick": (70, 320, t("④ 选信息量最大的下一问", "④ Pick the most informative next question"), STROKES[2], FILLS[2]),
    }
    for x, y, label, st, fl in nodes.values():
        s.rect(x, y, bw, bh, fill=fl, stroke=st, sw=2)
        s.text(x + bw / 2, y + bh / 2, label, size=15 if not en else 13.5, weight="bold", fill=INK)

    # 中心：隐藏目标
    cw, ch = 190, 68
    if en:
        cw = 226
    cx, cy = W / 2 - cw / 2, H / 2 - 34
    s.rect(cx, cy, cw, ch, fill="#f9fafb", stroke=MUTED, sw=1.5, rx=10)
    s.text(cx + cw / 2, cy + 26, t("用户真实偏好 θ", "User's true preference θ"), size=15, weight="bold", fill=INK)
    s.text(cx + cw / 2, cy + 48, t("（潜在 · 隐藏 · 测不准）", "(latent · hidden · unmeasurable)"), size=12.5, fill=MUTED)

    # 顺时针箭头
    s.arrow(70 + bw, 86 + bh / 2, W - 70 - bw, 86 + bh / 2, stroke=INK)          # act->obs
    s.arrow(W - 70 - bw / 2, 86 + bh, W - 70 - bw / 2, 320, stroke=INK)          # obs->upd
    s.arrow(W - 70 - bw, 320 + bh / 2, 70 + bw, 320 + bh / 2, stroke=INK)        # upd->pick
    s.arrow(70 + bw / 2, 320, 70 + bw / 2, 86 + bh, stroke=INK)                  # pick->act

    s.text(W / 2, H - 40, t("提问有代价，故挑期望信息增益最大的那个：",
                            "Asking is costly, so pick the one with the greatest expected information gain:"),
           size=14, fill=MUTED)
    s.text(W / 2, H - 16, "q* = argmaxq  I(θ ; yq)", size=15, fill=INK, weight="bold", italic=True)

    out_path = os.path.abspath(OUT)
    if en:
        out_path = os.path.join(os.path.dirname(out_path), "en", os.path.basename(out_path))
    s.save(out_path)
    return out_path


if __name__ == "__main__":
    build("zh")
    print("en ->", build("en"))
