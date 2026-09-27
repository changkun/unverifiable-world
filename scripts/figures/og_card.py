# -*- coding: utf-8 -*-
"""社交分享预览图（Open Graph card, 1200x630）。

与网站封面同一张「雾中推算航迹」海图（海图本体取自 website/cover.py，改封面即改这里）：
左侧是书名、英文书名、作者与一句话，右侧是雾中的航迹与四部船位。
生成 website/og.svg；加 --png 时再用无头浏览器（Playwright）渲染成 website/og.png：

    python3 scripts/figures/og_card.py
    uv run --with playwright python3 scripts/figures/og_card.py --png
"""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "website"))
import cover  # noqa: E402

OUT_SVG = os.path.join(ROOT, "website", "og.svg")
OUT_PNG = os.path.join(ROOT, "website", "og.png")
W, H = 1200, 630
OUTER, INNER = 18, 30

TITLE = "这个无法验证的世界"
SUB = "An Unverifiable World"
AUTHOR = "欧长坤　著"
BLURB = "当对错无从验证，有限的主体如何行动得当？"

# 海图取景：封面坐标系里的一块，缩放后放在分享图右侧
SCALE = 0.85
SRC_X, SRC_Y = 60, 340          # 取景窗左上角（封面坐标）
DST_X, DST_Y = 660, INNER + 6   # 放到分享图上的位置


def part_labels():
    """从 SUMMARY.md 取各部标题（去掉「第 N 部」前缀）。"""
    labels = []
    for ln in open(os.path.join(ROOT, "SUMMARY.md"), encoding="utf-8"):
        m = re.match(r"^##\s+第.+?部[\s　]+(.+?)\s*$", ln)
        if m:
            labels.append(m.group(1))
    return labels


def build():
    fog = cover.CHART_VARS_LIGHT.split("--cv-fog:")[1].split(";")[0].split()
    fr, fg, fb = (int(v) / 255 for v in fog)
    tx = DST_X - SRC_X * SCALE
    ty = DST_Y - SRC_Y * SCALE
    vx, vy, vr = cover.DR[-1]
    px, py, _ = cover.DR[-2]
    import math
    ang = math.degrees(math.atan2(vy - py, vx - px))

    style = (cover.CHART_VARS_LIGHT + cover.CHART_RULES + """
.t{font-family:"Songti SC","Noto Serif SC","Noto Serif CJK SC","Source Han Serif SC",STSong,serif;font-weight:700;fill:var(--cv-ink)}
.en{font-family:Georgia,"Times New Roman",serif;fill:var(--cv-ink-2)}
.au{font-family:"Songti SC","Noto Serif SC","Noto Serif CJK SC",serif;fill:var(--cv-ink)}
.bl{font-family:"PingFang SC","Hiragino Sans GB","Noto Sans CJK SC",sans-serif;fill:var(--cv-ink-2)}
.kk{font-family:"PingFang SC","Hiragino Sans GB","Noto Sans CJK SC",sans-serif;font-weight:600;fill:var(--cv-acc)}
""")
    defs = (
        cover.STIPPLE
        + f'<clipPath id="og-clip"><rect x="{INNER}" y="{INNER}" width="{W - 2 * INNER}" height="{H - 2 * INNER}"/></clipPath>'
        # 海图左缘渐隐进纸面，给书名让出位置
        + '<linearGradient id="og-fade" x1="0" y1="0" x2="1" y2="0">'
          '<stop offset="0" stop-color="var(--cv-paper)" stop-opacity="1"/>'
          '<stop offset=".42" stop-color="var(--cv-paper)" stop-opacity="1"/>'
          '<stop offset=".6" stop-color="var(--cv-paper)" stop-opacity=".55"/>'
          '<stop offset=".72" stop-color="var(--cv-paper)" stop-opacity="0"/></linearGradient>'
        # 雾：右上最浓，向左下变薄；雾团用分形噪声
        + '<linearGradient id="og-fogmask-g" x1="1" y1="0" x2=".35" y2="1">'
          '<stop offset="0" stop-color="#fff" stop-opacity=".78"/>'
          '<stop offset=".45" stop-color="#fff" stop-opacity=".5"/>'
          '<stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
        + f'<mask id="og-fogmask"><rect width="{W}" height="{H}" fill="url(#og-fogmask-g)"/></mask>'
        + '<filter id="og-noise" x="0" y="0" width="100%" height="100%">'
          '<feTurbulence type="fractalNoise" baseFrequency="0.0045 0.014" numOctaves="3" seed="4"/>'
          f'<feColorMatrix values="0 0 0 0 {fr:.3f} 0 0 0 0 {fg:.3f} 0 0 0 0 {fb:.3f} 2.4 0 0 0 -0.85"/></filter>'
    )
    chart = (f'<g clip-path="url(#og-clip)">'
             f'<g transform="translate({tx:.1f} {ty:.1f}) scale({SCALE})">{cover.chart_body("zh", part_labels())}</g>'
             f'<g mask="url(#og-fogmask)"><rect width="{W}" height="{H}" fill="rgb({" ".join(fog)})" opacity=".62"/>'
             f'<rect width="{W}" height="{H}" filter="url(#og-noise)"/></g>'
             # 船在雾上，仍看得见
             f'<g transform="translate({tx:.1f} {ty:.1f}) scale({SCALE})">'
             f'<circle class="cv-sa" cx="{vx}" cy="{vy}" r="{vr}" stroke-width="1.6" opacity=".55"/>'
             f'<g transform="translate({vx} {vy}) rotate({ang:.1f}) scale(1.5)">'
             f'<path d="M12 0L5 -5.2H-9V5.2H5Z" fill="var(--cv-vessel)" stroke="var(--cv-paper)" stroke-width="1.2" stroke-linejoin="round"/></g></g>'
             f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#og-fade)"/>'
             f'</g>')
    lx = 84
    text = (f'<text class="kk" x="{lx}" y="150" font-size="19" letter-spacing="6">全书四部 · 十五章</text>'
            f'<text class="t" x="{lx - 3}" y="244" font-size="62" letter-spacing="3">{TITLE}</text>'
            f'<rect x="{lx}" y="282" width="56" height="3" fill="var(--cv-acc)"/>'
            f'<text class="en" x="{lx}" y="340" font-size="36">{SUB}</text>'
            f'<text class="au" x="{lx}" y="404" font-size="27" letter-spacing="2">{AUTHOR}</text>'
            f'<text class="bl" x="{lx}" y="512" font-size="23">{BLURB}</text>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
           f'<style>{style}</style><defs>{defs}</defs>'
           f'<g class="cv"><rect class="cv-paper" width="{W}" height="{H}"/>{chart}{text}'
           f'{cover.graduations(W, H, OUTER, INNER, 30)}</g></svg>')
    with open(OUT_SVG, "w", encoding="utf-8") as fh:
        fh.write(svg)
    return OUT_SVG


def render_png(svg_path=OUT_SVG, png_path=OUT_PNG):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        pg.goto("file://" + os.path.abspath(svg_path))
        pg.wait_for_timeout(300)
        pg.screenshot(path=png_path, clip={"x": 0, "y": 0, "width": W, "height": H})
        b.close()
    return png_path


if __name__ == "__main__":
    print(build())
    if "--png" in sys.argv:
        print(render_png())
