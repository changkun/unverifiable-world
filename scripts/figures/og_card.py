# -*- coding: utf-8 -*-
"""社交分享预览图（Open Graph card, 1200x630）。

深色书封基调 + 罗盘意象 + 书名/副书名/作者/一句话。生成 website/og.svg，
随后由部署脚本转成 website/og.png 供 og:image 使用。
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from svg import SVG, FONT

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "website", "og.svg")
GOLD = "#d9c4a0"
BLUE = "#9fb2d4"
W, H = 1200, 630
TITLE = "在无法验证的世界里"
SUB = "AN UNVERIFIABLE WORLD"
AUTHOR = "欧长坤　著"
BLURB = "在没有任何东西能确认你做对了的地方，有限的主体如何行动。"


def build():
    s = SVG(W, H, bg=None)
    s.parts.insert(0,
        '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#2b3a55"/><stop offset="1" stop-color="#161d2c"/>'
        '</linearGradient></defs>')
    s.parts.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#g)"/>')
    s.parts.append(f'<rect x="22" y="22" width="{W-44}" height="{H-44}" rx="10" fill="none" '
                   f'stroke="{GOLD}" stroke-width="1.4" opacity="0.35"/>')

    # 罗盘（居中偏下）
    cx, cy = 600, 358
    for r, op in ((118, .22), (92, .45), (64, .7)):
        s.parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{GOLD}" '
                       f'stroke-width="1.3" opacity="{op}"/>')
    for k in range(72):
        a = math.radians(k * 5 - 90)
        op = max(0.06, 0.5 * (0.5 - 0.5 * math.sin(a)))
        major = (k % 9 == 0)
        r0, r1 = 118, 118 + (11 if major else 6)
        s.parts.append(
            f'<line x1="{cx+r0*math.cos(a):.1f}" y1="{cy+r0*math.sin(a):.1f}" '
            f'x2="{cx+r1*math.cos(a):.1f}" y2="{cy+r1*math.sin(a):.1f}" '
            f'stroke="{GOLD}" stroke-width="{1.4 if major else 1}" opacity="{op:.2f}"/>')
    ang = math.radians(-64)
    px, py = math.cos(ang), math.sin(ang)
    qx, qy = -py, px
    tip = (cx + 84 * px, cy + 84 * py)
    tail = (cx - 66 * px, cy - 66 * py)
    L = (cx + 8.5 * qx, cy + 8.5 * qy)
    R = (cx - 8.5 * qx, cy - 8.5 * qy)
    s.parts.append(f'<polygon points="{tip[0]:.1f},{tip[1]:.1f} {L[0]:.1f},{L[1]:.1f} {R[0]:.1f},{R[1]:.1f}" fill="{GOLD}"/>')
    s.parts.append(f'<polygon points="{tail[0]:.1f},{tail[1]:.1f} {L[0]:.1f},{L[1]:.1f} {R[0]:.1f},{R[1]:.1f}" fill="none" stroke="{BLUE}" stroke-width="1.3" opacity="0.8"/>')
    s.parts.append(f'<circle cx="{cx}" cy="{cy}" r="5.5" fill="#bfa775"/>')

    # 文字
    s.text(W/2, 132, TITLE, size=66, weight="bold", fill="#f4f4f2")
    s.text(W/2, 192, SUB, size=22, fill="#aab4c8")
    s.parts.append(f'<line x1="{W/2-30}" y1="216" x2="{W/2+30}" y2="216" stroke="{GOLD}" stroke-width="2.5" opacity="0.8"/>')
    s.text(W/2, 542, BLURB, size=27, fill="#cdd5e3")
    s.text(W/2, 586, AUTHOR, size=22, fill="#9aa6bd")
    s.save(os.path.abspath(OUT))
    return os.path.abspath(OUT)


if __name__ == "__main__":
    print("wrote", build())
