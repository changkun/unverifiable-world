# -*- coding: utf-8 -*-
"""封面：雾中推算航迹（dead reckoning）的海图。

书封上画一张海图：左下是已测绘的海岸（德尔斐所在的一侧，雾最薄），一条推算航迹
从岸边的定位点出发驶向雾里。航迹上的四个推算船位对应全书四部，每个船位外的
不确定圆一站比一站大；航迹的延长线擦过一处「疑存」礁石的危险线，而那片水域被雾盖着。

- 海图在构建时由本模块按 SUMMARY 的各部标题生成为内联 SVG，颜色全部走 --cv-* 变量，
  随系统深浅色切换，无需脚本；
- 雾是 CSS 渐变叠成的两层，缓慢漂移（只动 transform）；
- 指针悬停处像提灯一样拨开雾（CSS mask，由脚本写 --lx/--ly/--lr），触屏上轻触即可；
- 打开页面时提灯沿航迹走一遍再熄灭，提示这张图可以看；
- 「减少动态效果」下不漂移、不走航迹，提灯仍可用但不带缓动；标签页隐藏时暂停动画。
"""
import html
import math
import random

W, H = 700, 980
FRAME_OUT, FRAME_IN = 22, 34  # 图廓外框与内框（两者之间是经纬度刻度带）

# 海岸线：从左缘走到下缘，水在右上侧。两端伸出图廓，便于等深线与晕渲线延伸到边。
COAST = [(-40, 640), (34, 655), (70, 668), (104, 700), (122, 742), (160, 772),
         (196, 806), (214, 850), (250, 880), (292, 900), (330, 946), (380, 1010)]

FIX = (240, 830)  # 出发的定位点（已验证的位置）
# 推算船位：(x, y, 不确定圆半径)，依次对应第一至第四部
DR = [(300, 730, 12), (362, 632, 22), (428, 540, 36), (500, 452, 54)]
AHEAD = 72        # 最后一个船位之后，航向延长线的长度
REEF = (548, 420, 20)
WRECK = (150, 520)
ROSE = (585, 690, 62)

ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]

TEXT = {
    "zh": {"ed": "疑存", "pa": "概位"},
    "en": {"ed": "ED", "pa": "PA"},
}


def f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def smooth(pts):
    """Catmull-Rom 样条转成三次贝塞尔路径。"""
    d = f"M{f(pts[0][0])} {f(pts[0][1])}"
    for i in range(len(pts) - 1):
        p0 = pts[max(0, i - 1)]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[min(len(pts) - 1, i + 2)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f"C{f(c1[0])} {f(c1[1])} {f(c2[0])} {f(c2[1])} {f(p2[0])} {f(p2[1])}"
    return d


def offset(pts, dist, wobble=0.0, seed=0):
    """把海岸线朝水的一侧（行进方向的左手法线）平移 dist，可加一点起伏。"""
    rnd = random.Random(seed)
    out = []
    for i, (x, y) in enumerate(pts):
        a = pts[max(0, i - 1)]
        b = pts[min(len(pts) - 1, i + 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        n = math.hypot(dx, dy) or 1
        nx, ny = dy / n, -dx / n
        d = dist + (rnd.uniform(-wobble, wobble) if wobble else 0)
        out.append((x + nx * d, y + ny * d))
    return out


def seg_dist(p, a, b):
    ax, ay = a
    bx, by = b
    px, py = p
    dx, dy = bx - ax, by - ay
    t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy or 1)))
    return math.hypot(px - (ax + t * dx), py - (ay + t * dy))


def poly_dist(p, pts):
    return min(seg_dist(p, pts[i], pts[i + 1]) for i in range(len(pts) - 1))


def in_land(p):
    """点是否落在海岸线的陆地一侧（左下）。"""
    x, y = p
    for i in range(len(COAST) - 1):
        (ax, ay), (bx, by) = COAST[i], COAST[i + 1]
        if ax <= x <= bx:
            yc = ay + (by - ay) * (x - ax) / (bx - ax)
            return y > yc
    return x < COAST[0][0] or (x <= COAST[-1][0] and y > COAST[-1][1])


def ahead_point():
    x, y, _ = DR[-1]
    px, py, _ = DR[-2]
    dx, dy = x - px, y - py
    n = math.hypot(dx, dy)
    return (x + dx / n * AHEAD, y + dy / n * AHEAD), (dx / n, dy / n)


def text_w(s, size, cjk_em=1.0, latin_em=0.6, spacing=0.0):
    w = 0.0
    for ch in s:
        w += size * (cjk_em if ord(ch) > 0x2E80 else latin_em) + spacing
    return w


def graduations(w=W, h=H, outer=FRAME_OUT, inner=FRAME_IN, step=32):
    """图廓刻度带：内外框之间黑白相间的分划（封面与分享图共用）。"""
    out = [f'<rect class="cv-s2" x="{outer}" y="{outer}" width="{w - 2 * outer}" '
           f'height="{h - 2 * outer}" stroke-width=".9"/>',
           f'<rect class="cv-s1" x="{inner}" y="{inner}" width="{w - 2 * inner}" '
           f'height="{h - 2 * inner}" stroke-width="1.1"/>']
    half = (inner - outer) / 2
    bars = []
    for k, x in enumerate(range(inner, w - inner, step)):
        if k % 2 == 0:
            bw = min(step, w - inner - x)
            bars.append(f'<rect x="{x}" y="{outer}" width="{bw}" height="{half}"/>')
            bars.append(f'<rect x="{x}" y="{h - outer - half}" width="{bw}" height="{half}"/>')
    for k, y in enumerate(range(inner, h - inner, step)):
        if k % 2 == 0:
            bh = min(step, h - inner - y)
            bars.append(f'<rect x="{outer}" y="{y}" width="{half}" height="{bh}"/>')
            bars.append(f'<rect x="{w - outer - half}" y="{y}" width="{half}" height="{bh}"/>')
    out.append(f'<g class="cv-grad">{"".join(bars)}</g>')
    return "".join(out)


def rose():
    cx, cy, r = ROSE
    out = [f'<circle class="cv-s2" cx="{cx}" cy="{cy}" r="{r}" stroke-width=".9"/>',
           f'<circle class="cv-s3" cx="{cx}" cy="{cy}" r="{r - 16}" stroke-width=".8"/>']
    ticks = []
    for k in range(72):
        a = math.radians(k * 5 - 90)
        major = k % 9 == 0
        r0, r1 = r, r - (9 if major else 4.5)
        ticks.append(f'M{f(cx + r0 * math.cos(a))} {f(cy + r0 * math.sin(a))}'
                     f'L{f(cx + r1 * math.cos(a))} {f(cy + r1 * math.sin(a))}')
    out.append(f'<path class="cv-s2" stroke-width=".8" d="{"".join(ticks)}"/>')
    # 四角星：北向最长、实心；其余描边
    star = []
    for k, L in enumerate((r - 6, r - 26, r - 22, r - 26)):
        a = math.radians(k * 90 - 90)
        tip = (cx + L * math.cos(a), cy + L * math.sin(a))
        l = (cx + 6 * math.cos(a - math.pi / 2), cy + 6 * math.sin(a - math.pi / 2))
        rr = (cx + 6 * math.cos(a + math.pi / 2), cy + 6 * math.sin(a + math.pi / 2))
        cls = "cv-f1" if k == 0 else "cv-rose-pt"
        star.append(f'<path class="{cls}" d="M{f(tip[0])} {f(tip[1])}L{f(l[0])} {f(l[1])}'
                    f'L{cx} {cy}L{f(rr[0])} {f(rr[1])}Z"/>')
    out.extend(star)
    out.append(f'<circle class="cv-fp cv-s1" cx="{cx}" cy="{cy}" r="2.6" stroke-width=".9"/>')
    out.append(f'<text class="cv-f1 cv-serif" x="{cx}" y="{cy - r - 7}" font-size="15" '
               f'text-anchor="middle">N</text>')
    return "".join(out)


def track(part_labels, lang):
    out = []
    pts = [FIX] + [(x, y) for x, y, _ in DR]
    (ax, ay), (ux, uy) = ahead_point()
    # 不确定圆（虚线）
    for x, y, r in DR:
        out.append(f'<circle class="cv-sa cv-unc" cx="{x}" cy="{y}" r="{r}" stroke-width="1.1"/>')
    # 航迹：定位点到第一船位是实线（刚离岸，仍看得清），此后照样是实线，延长线为虚线
    out.append(f'<path class="cv-halo" stroke-width="6" d="M{FIX[0]} {FIX[1]}'
               + "".join(f"L{x} {y}" for x, y in pts[1:]) + '"/>')
    out.append(f'<path class="cv-sa" stroke-width="2" stroke-linejoin="round" d="M{FIX[0]} {FIX[1]}'
               + "".join(f"L{x} {y}" for x, y in pts[1:]) + '"/>')
    lx, ly, _ = DR[-1]
    out.append(f'<path class="cv-sa" stroke-width="1.6" stroke-dasharray="5 5" '
               f'd="M{lx} {ly}L{f(ax)} {f(ay)}"/>')
    # 箭头
    px, py = -uy, ux
    tip = (ax + ux * 10, ay + uy * 10)
    out.append(f'<path class="cv-fa" d="M{f(tip[0])} {f(tip[1])}L{f(ax + px * 5)} {f(ay + py * 5)}'
               f'L{f(ax - px * 5)} {f(ay - py * 5)}Z"/>')
    # 定位点：圆圈加点（海图上「已测定的船位」）
    out.append(f'<circle class="cv-fp cv-sa" cx="{FIX[0]}" cy="{FIX[1]}" r="6.5" stroke-width="1.6"/>'
               f'<circle class="cv-fa" cx="{FIX[0]}" cy="{FIX[1]}" r="2"/>')
    # 推算船位：航迹上的半圆标记
    for (x, y, _r), (px0, py0) in zip(DR, pts[:-1]):
        dx, dy = x - px0, y - py0
        n = math.hypot(dx, dy)
        ang = math.degrees(math.atan2(dy, dx))
        out.append(f'<path class="cv-fp cv-sa" stroke-width="1.5" transform="translate({x} {y}) rotate({f(ang)})" '
                   f'd="M0 -6A6 6 0 0 1 0 6Z"/>')
    # 各部标签：放在航迹西侧，罗马数字与标题同一行，由浏览器排宽度
    boxes = []
    for i, ((x, y, r), label) in enumerate(zip(DR, part_labels)):
        xe = x - r - 12
        tw = text_w(label, 11.5, cjk_em=1.05, latin_em=0.72, spacing=1.2) + 26
        out.append(f'<text x="{f(xe)}" y="{y + 4}" text-anchor="end">'
                   f'<tspan class="cv-fa cv-serif" font-size="15">{ROMAN[i]}</tspan>'
                   f'<tspan class="cv-f2 cv-label" font-size="11.5" letter-spacing="1.2" dx="7">{html.escape(label)}</tspan></text>')
        boxes.append((xe - tw, y - 12, xe + 4, y + 10))
    return "".join(out), boxes


def reef(lang):
    x, y, r = REEF
    out = [f'<circle class="cv-s1 cv-danger" cx="{x}" cy="{y}" r="{r}" stroke-width="1.1"/>']
    for dx, dy in ((-6, -3), (5, -6), (1, 6)):
        cx, cy = x + dx, y + dy
        out.append(f'<path class="cv-s1" stroke-width="1.2" d="M{cx - 4} {cy}H{cx + 4}M{cx} {cy - 4}V{cy + 4}"/>')
    out.append(f'<text class="cv-f1 cv-label" x="{x + r + 6}" y="{y + 4}" font-size="11" letter-spacing=".8">'
               f'{html.escape(TEXT[lang]["ed"])}</text>')
    return "".join(out)


def wreck(lang):
    x, y = WRECK
    return (f'<ellipse class="cv-s1 cv-danger" cx="{x}" cy="{y}" rx="22" ry="12" stroke-width="1"/>'
            f'<path class="cv-s1" stroke-width="1.3" d="M{x - 13} {y}H{x + 13}M{x - 6} {y - 6}V{y + 6}'
            f'M{x} {y - 7}V{y + 7}M{x + 6} {y - 6}V{y + 6}"/>'
            f'<text class="cv-f1 cv-label" x="{x + 28}" y="{y + 4}" font-size="11" letter-spacing=".8">'
            f'{html.escape(TEXT[lang]["pa"])}</text>')


def land(lang):
    coast = smooth(COAST)
    poly = coast + f"L{COAST[-1][0]} 1040L-60 1040Z"
    out = [f'<path class="cv-land" d="{poly}"/>',
           f'<path d="{poly}" fill="url(#cv-stip)"/>']
    # 岸线晕渲：一组越来越淡、越来越疏的平行线
    for d, op in ((5, .55), (11, .4), (18, .28), (27, .17), (38, .09)):
        out.append(f'<path class="cv-s2" stroke-width=".8" opacity="{op}" d="{smooth(offset(COAST, d))}"/>')
    out.append(f'<path class="cv-s1" stroke-width="1.3" d="{coast}"/>')
    # 山丘的等高线
    for i, (rx, ry) in enumerate(((58, 30), (40, 20), (22, 11))):
        out.append(f'<ellipse class="cv-s3" cx="84" cy="{900 - i * 3}" rx="{rx}" ry="{ry}" '
                   f'stroke-width=".8" transform="rotate(-18 84 900)"/>')
    # 德尔斐：岸上的一座小神庙（海图上的显著物标，不加注记）
    tx, ty = 150, 854
    out.append(f'<path class="cv-s1" stroke-width="1" d="M{tx - 10} {ty - 8}L{tx} {ty - 14}L{tx + 10} {ty - 8}Z'
               f'M{tx - 9} {ty - 7}V{ty}M{tx - 3} {ty - 7}V{ty}M{tx + 3} {ty - 7}V{ty}M{tx + 9} {ty - 7}V{ty}'
               f'M{tx - 11} {ty + 1}H{tx + 11}"/>')
    return "".join(out)


def depths():
    """浅水着色与两条等深线（10、20）。"""
    c10 = offset(COAST, 44, 5, seed=3)
    c20 = offset(COAST, 104, 12, seed=5)
    shallow = smooth(COAST) + "L" + smooth(list(reversed(c10)))[1:] + "Z"
    out = [f'<path class="cv-shallow" d="{shallow}"/>',
           f'<path class="cv-s2" stroke-width=".9" stroke-dasharray="1.5 3.5" stroke-linecap="round" d="{smooth(c10)}"/>',
           f'<path class="cv-s3" stroke-width=".9" stroke-dasharray="7 3 1.5 3" d="{smooth(c20)}"/>']
    return out, c10, c20


def soundings(boxes):
    rnd = random.Random(11)
    out = []
    track_pts = [FIX] + [(x, y) for x, y, _ in DR] + [ahead_point()[0]]
    step = 50
    for gy in range(int(FRAME_IN + 40), int(H - FRAME_IN - 20), step):
        for gx in range(int(FRAME_IN + 26), int(W - FRAME_IN - 20), step):
            if rnd.random() < 0.3:
                continue
            p = (gx + rnd.uniform(-17, 17), gy + rnd.uniform(-15, 15))
            x, y = p
            if y < 348 or in_land(p):
                continue
            dc = poly_dist(p, COAST)
            if dc < 16:
                continue
            if poly_dist(p, track_pts) < 18:
                continue
            if any(math.hypot(x - cx, y - cy) < r + 12 for cx, cy, r in DR):
                continue
            if math.hypot(x - ROSE[0], y - ROSE[1]) < ROSE[2] + 22:
                continue
            if math.hypot(x - REEF[0], y - REEF[1]) < REEF[2] + 26:
                continue
            if abs(x - WRECK[0] - 16) < 50 and abs(y - WRECK[1]) < 22:
                continue
            if x > 400 and y > 880:  # 作者名
                continue
            if any(bx0 - 6 < x < bx1 + 14 and by0 - 8 < y < by1 + 8 for bx0, by0, bx1, by1 in boxes):
                continue
            if abs(x - 150) < 24 and 834 < y < 866:
                continue
            d = 2 + dc / 9.5 + rnd.uniform(-2.5, 2.5)
            whole = max(2, int(d))
            frac = rnd.random() < 0.28 and whole < 30
            sub = f'<tspan class="cv-sub" font-size="7.5" dy="2.5">{rnd.randint(1, 9)}</tspan>' if frac else ""
            out.append(f'<text x="{f(x)}" y="{f(y)}">{whole}{sub}</text>')
    return f'<g class="cv-snd" font-size="11" text-anchor="middle">{"".join(out)}</g>'


def graticule():
    return (f'<path class="cv-s3 cv-grat" stroke-width=".6" d="M{FRAME_IN} 318H{W - FRAME_IN}'
            f'M{FRAME_IN} 760H{W - FRAME_IN}M268 {FRAME_IN}V{H - FRAME_IN}"/>')


STIPPLE = ('<pattern id="cv-stip" width="7" height="7" patternUnits="userSpaceOnUse">'
           '<circle class="cv-stip" cx="1.5" cy="1.5" r=".75"/><circle class="cv-stip" cx="5" cy="5" r=".55"/></pattern>')


def chart_body(lang, part_labels):
    """海图上的全部内容（不含图廓），坐标系为 W x H。引用 #cv-stip 点纹。"""
    depth_parts, _, _ = depths()
    trk, boxes = track(part_labels, lang)
    return ("".join(depth_parts) + graticule() + land(lang) + soundings(boxes)
            + rose() + wreck(lang) + reef(lang) + trk)


def chart_svg(lang, part_labels):
    """海图主体（雾下的一层）。"""
    defs = (f'<clipPath id="cv-clip"><rect x="{FRAME_IN}" y="{FRAME_IN}" width="{W - 2 * FRAME_IN}" '
            f'height="{H - 2 * FRAME_IN}"/></clipPath>' + STIPPLE)
    body = chart_body(lang, part_labels)
    return (f'<svg class="cv-chart" viewBox="0 0 {W} {H}" aria-hidden="true" focusable="false">'
            f'<defs>{defs}</defs><rect class="cv-paper" width="{W}" height="{H}"/>'
            f'<g clip-path="url(#cv-clip)">{body}</g>{graduations()}</svg>')


def vessel_svg():
    """浮在雾上的一层：此刻的船位与它发出的雾号圈。"""
    x, y, r = DR[-1]
    px, py, _ = DR[-2]
    ang = math.degrees(math.atan2(y - py, x - px))
    return (f'<svg class="cv-top" viewBox="0 0 {W} {H}" aria-hidden="true" focusable="false">'
            f'<circle class="cv-ping" cx="{x}" cy="{y}" r="{r}"/>'
            f'<circle class="cv-ping cv-ping2" cx="{x}" cy="{y}" r="{r}"/>'
            f'<g transform="translate({x} {y}) rotate({f(ang)})">'
            '<path class="cv-vessel" d="M12 0L5 -5.2H-9V5.2H5Z"/></g></svg>')


def fog_html():
    return ('<div class="cv-fog" aria-hidden="true"><div class="cv-fog-base"></div>'
            '<div class="cv-fog-drift"><div class="cv-fog-a"></div><div class="cv-fog-b"></div></div></div>')


def cover_art(lang, title, subtitle, author_line, part_labels):
    """整张封面（装饰性，对读屏隐藏；书名等由旁边的扉页以真实标题给出）。"""
    if lang == "en" and " " in title:
        i = title.rfind(" ")
        tl = f"<span>{html.escape(title[:i])}</span> <span>{html.escape(title[i + 1:])}</span>"
    else:
        tl = html.escape(title)
    return (f'<div class="cv" data-cover aria-hidden="true">'
            f'{chart_svg(lang, part_labels)}{fog_html()}{vessel_svg()}'
            f'<div class="cv-letter"><div class="cv-title">{tl}</div>'
            f'<div class="cv-subtitle">{html.escape(subtitle)}</div></div>'
            f'<div class="cv-author">{html.escape(author_line)}</div>'
            f'</div>')


def _noise(seed, fx, fy, gain, bias):
    """可横向无缝平铺的分形噪声，转成透明度，给雾团当 mask。"""
    svg = (f"<svg xmlns='http://www.w3.org/2000/svg' width='700' height='980'>"
           f"<filter id='n' x='0' y='0' width='100%' height='100%'>"
           f"<feTurbulence type='fractalNoise' baseFrequency='{fx} {fy}' numOctaves='3' seed='{seed}' stitchTiles='stitch'/>"
           f"<feColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 {gain} 0 0 0 {bias}'/></filter>"
           f"<rect width='100%' height='100%' filter='url(%23n)'/></svg>")
    return 'url("data:image/svg+xml;utf8,' + svg.replace('"', "'").replace("<", "%3C").replace(">", "%3E") + '")'


# 海图的配色：浅色是纸本海图，深色是夜航海图。
CHART_VARS_LIGHT = r""":root{
 --cv-paper:#f3efe5;--cv-ink:#1d2a3b;--cv-ink-2:#566274;--cv-ink-3:#9ba3ae;--cv-acc:#b4452b;
 --cv-land:#e7dfcd;--cv-shallow:#dfe7ea;--cv-fog:234 236 237;--cv-shadow:rgba(28,34,48,.28);
 --cv-desk:#efece4;--cv-vessel:#b4452b;
}
"""
CHART_VARS = CHART_VARS_LIGHT + r"""@media (prefers-color-scheme: dark){:root{
 --cv-paper:#16202f;--cv-ink:#d9dfe8;--cv-ink-2:#9aa6b8;--cv-ink-3:#4f5c70;--cv-acc:#e2b36a;
 --cv-land:#1c283a;--cv-shallow:#1a2638;--cv-fog:44 58 80;--cv-shadow:rgba(0,0,0,.6);
 --cv-desk:#11141a;--cv-vessel:#f0c37a;
}}
"""
# 海图各元素的样式，只依赖 --cv-* 变量；分享图（og）用同一套。
CHART_RULES = r""".cv .cv-paper{fill:var(--cv-paper)}
.cv .cv-land{fill:var(--cv-land)}
.cv .cv-shallow{fill:var(--cv-shallow)}
.cv .cv-stip{fill:var(--cv-ink-3);opacity:.7}
.cv .cv-s1{fill:none;stroke:var(--cv-ink)}.cv .cv-s2{fill:none;stroke:var(--cv-ink-2)}.cv .cv-s3{fill:none;stroke:var(--cv-ink-3)}
.cv .cv-sa{fill:none;stroke:var(--cv-acc)}.cv .cv-halo{fill:none;stroke:var(--cv-paper)}
.cv .cv-f1{fill:var(--cv-ink)}.cv .cv-f2{fill:var(--cv-ink-2)}.cv .cv-fa{fill:var(--cv-acc)}.cv .cv-fp{fill:var(--cv-paper)}
.cv .cv-rose-pt{fill:none;stroke:var(--cv-ink-2);stroke-width:.9}
.cv .cv-grad rect{fill:var(--cv-ink-2);opacity:.6}
.cv .cv-grat{opacity:.55}
.cv .cv-unc{stroke-dasharray:3 4;opacity:.75}
.cv .cv-danger{stroke-dasharray:1.6 3.2;stroke-linecap:round}
.cv .cv-snd{fill:var(--cv-ink-2);font-family:Georgia,"Times New Roman",serif;font-style:italic}
.cv .cv-label{font-family:-apple-system,"PingFang SC","Hiragino Sans GB","Noto Sans CJK SC","Segoe UI",Helvetica,Arial,sans-serif;text-transform:uppercase}
.cv .cv-serif{font-family:Georgia,"Times New Roman","Songti SC",serif}
"""

NOISE_CSS = (":root{--cv-noise-a:" + _noise(4, 0.0042, 0.012, 2.6, -0.95)
             + ";--cv-noise-b:" + _noise(9, 0.007, 0.02, 2.4, -0.9) + "}")

# 封面页专用样式（追加在全站 CSS 之后）。
CSS = NOISE_CSS + CHART_VARS + CHART_RULES + r"""
/* ===== 封面：雾中海图 ===== */
.cover-page{margin:0;min-height:100svh}
.spread{display:grid;grid-template-columns:minmax(0,1.02fr) minmax(0,1fr);min-height:100svh}
.verso{display:grid;place-items:center;padding:40px 48px;background:var(--cv-desk);border-right:1px solid var(--line)}
.recto{display:flex;flex-direction:column;justify-content:center;padding:40px clamp(36px,5.6vw,92px);max-width:660px}

.cv{position:relative;container-type:inline-size;aspect-ratio:700/980;
 width:min(100%,540px,calc((100svh - 96px) * 700 / 980));border-radius:3px;overflow:hidden;
 background:var(--cv-paper);cursor:crosshair;touch-action:manipulation;-webkit-tap-highlight-color:transparent;
 box-shadow:0 1px 2px rgba(0,0,0,.08),0 26px 60px -18px var(--cv-shadow),inset 5px 0 0 rgba(0,0,0,.06),inset 9px 0 12px -8px rgba(0,0,0,.18)}
.cv > svg{position:absolute;inset:0;width:100%;height:100%;display:block}

/* 雾：底层是一道由右上向左下变薄的渐变，上面两层缓慢漂移的雾团；整体被提灯的 mask 挖开 */
.cv-fog{position:absolute;inset:3.47% 4.86%;pointer-events:none;
 --lx:50%;--ly:40%;--lr:0;
 -webkit-mask-image:radial-gradient(circle calc(var(--lr) * 26cqi + .5px) at var(--lx) var(--ly),rgba(0,0,0,.04) 0,rgba(0,0,0,.18) 42%,rgba(0,0,0,1) 100%);
 mask-image:radial-gradient(circle calc(var(--lr) * 26cqi + .5px) at var(--lx) var(--ly),rgba(0,0,0,.04) 0,rgba(0,0,0,.18) 42%,rgba(0,0,0,1) 100%)}
.cv-fog-base{position:absolute;inset:0;
 background:linear-gradient(197deg,rgb(var(--cv-fog)/.84) 0%,rgb(var(--cv-fog)/.8) 34%,rgb(var(--cv-fog)/.7) 47%,
  rgb(var(--cv-fog)/.55) 58%,rgb(var(--cv-fog)/.36) 68%,rgb(var(--cv-fog)/.16) 78%,rgb(var(--cv-fog)/.04) 86%,rgb(var(--cv-fog)/0) 92%)}
.cv-fog-drift{position:absolute;inset:0;overflow:hidden;
 -webkit-mask-image:linear-gradient(197deg,#000 0%,#000 48%,rgba(0,0,0,.7) 66%,rgba(0,0,0,.25) 80%,transparent 90%);
 mask-image:linear-gradient(197deg,#000 0%,#000 48%,rgba(0,0,0,.7) 66%,rgba(0,0,0,.25) 80%,transparent 90%)}
.cv-fog-a,.cv-fog-b{position:absolute;top:0;bottom:0;left:0;width:200%;will-change:transform;background:rgb(var(--cv-fog))}
.cv-fog-a{opacity:.92;-webkit-mask:var(--cv-noise-a) repeat-x 0 0/50% 100%;mask:var(--cv-noise-a) repeat-x 0 0/50% 100%;
 animation:cvDrift 110s linear infinite}
.cv-fog-b{opacity:.7;-webkit-mask:var(--cv-noise-b) repeat-x 0 0/50% 100%;mask:var(--cv-noise-b) repeat-x 0 0/50% 100%;
 animation:cvDrift 170s linear infinite reverse}
@keyframes cvDrift{from{transform:translateX(0)}to{transform:translateX(-50%)}}

/* 浮在雾上：船与雾号圈 */
.cv-top .cv-vessel{fill:var(--cv-vessel);stroke:var(--cv-paper);stroke-width:1.4;stroke-linejoin:round}
.cv-top .cv-ping{fill:none;stroke:var(--cv-vessel);stroke-width:1.3;opacity:0;transform-box:fill-box;transform-origin:center;
 animation:cvPing 7s cubic-bezier(.2,.6,.3,1) 1.2s infinite}
.cv-top .cv-ping2{animation-delay:1.75s;stroke-width:.9}
@keyframes cvPing{0%{transform:scale(.18);opacity:0}6%{opacity:.8}46%{transform:scale(1.04);opacity:0}100%{transform:scale(1.04);opacity:0}}
.cv.is-paused .cv-fog-a,.cv.is-paused .cv-fog-b,.cv.is-paused .cv-ping{animation-play-state:paused}

/* 书封上的字：书名在雾最浓处，作者在右下的清水里 */
.cv-letter{position:absolute;left:10.5%;right:10%;top:9.5%;pointer-events:none}
.cv-title{font-family:Georgia,"Times New Roman",serif;font-size:10.4cqi;line-height:1.02;color:var(--cv-ink);letter-spacing:-.01em;font-weight:400}
.cv-title span{display:block}
.cv-subtitle{margin-top:4.2cqi;max-width:30em;font-size:2.35cqi;line-height:1.7;letter-spacing:.2em;text-transform:uppercase;color:var(--cv-ink-2);
 font-family:-apple-system,"Segoe UI",Helvetica,Arial,sans-serif}
.cv-subtitle::before{content:"";display:block;width:9cqi;height:1.5px;background:var(--cv-acc);margin-bottom:3.4cqi}
.lang-zh .cv-title{font-family:"Songti SC","Noto Serif SC","Noto Serif CJK SC","Source Han Serif SC",STSong,serif;font-weight:600;font-size:7.7cqi;letter-spacing:.05em;line-height:1.3;white-space:nowrap}
.cv-author{position:absolute;right:9%;bottom:6.4%;font-family:Georgia,"Times New Roman",serif;font-size:3.4cqi;color:var(--cv-ink);letter-spacing:.04em;pointer-events:none}
.lang-zh .cv-author{font-family:"Songti SC","Noto Serif SC","Noto Serif CJK SC",serif;letter-spacing:.2em}

/* 扉页 */
.rt-kicker{margin:0 0 22px;font:600 11.5px/1 -apple-system,"PingFang SC","Segoe UI",Helvetica,Arial,sans-serif;letter-spacing:.3em;text-transform:uppercase;color:var(--cv-acc)}
.rt-title{margin:0;font-family:Georgia,"Times New Roman",serif;font-weight:400;font-size:clamp(38px,4.1vw,62px);line-height:1.02;letter-spacing:-.015em;color:var(--ink)}
.rt-title span{display:block}
.lang-zh .rt-title{font-family:"Songti SC","Noto Serif SC","Noto Serif CJK SC",serif;font-weight:600;font-size:clamp(28px,3.1vw,46px);letter-spacing:.04em;line-height:1.25;white-space:nowrap}
.rt-sub{margin:18px 0 0;max-width:24em;font-size:18px;line-height:1.5;color:var(--muted)}
.lang-zh .rt-sub{font-family:Georgia,"Times New Roman",serif;letter-spacing:.06em;font-size:18px}
.rt-author{margin:22px 0 0;font-size:16px;color:var(--ink)}
.rt-author::before{content:"";display:block;width:36px;height:2px;margin-bottom:14px;background:var(--cv-acc)}
.rt-blurb{margin:16px 0 0;max-width:30em;font-size:15.5px;line-height:1.6;color:var(--muted);font-style:italic}
.lang-zh .rt-blurb{font-style:normal}
.recto .actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:24px}
.recto .btn{padding:9px 18px;font-size:15px;border-radius:8px;display:inline-flex;align-items:center;gap:8px}
.recto .btn svg{transition:transform .18s ease}
.recto .btn.primary:hover svg{transform:translateX(3px)}
.rt-parts{list-style:none;margin:30px 0 0;padding:0;border-top:1px solid var(--line);max-width:30em}
.rt-parts li{border-bottom:1px solid var(--line)}
.rt-parts a{display:grid;grid-template-columns:2.6em minmax(0,1fr) auto;align-items:baseline;gap:8px;padding:7px 2px;color:var(--ink)}
.rt-parts a:hover{text-decoration:none}
.rt-parts a:hover .rt-pt{text-decoration:underline;text-underline-offset:.2em}
.rt-num{font-family:Georgia,serif;font-size:18px;color:var(--cv-acc)}
.rt-pt{font-size:15.5px}
.rt-range{font-size:12.5px;color:var(--muted);font-variant-numeric:tabular-nums;font-family:-apple-system,"Segoe UI",Helvetica,Arial,sans-serif}
.rt-back{margin:10px 0 0;font-size:13.5px;color:var(--muted)}
.rt-back a{color:var(--muted);text-decoration:underline;text-decoration-color:var(--line);text-underline-offset:.2em}
.rt-back a:hover{color:var(--ink)}
.rt-foot{margin-top:20px;display:flex;flex-direction:column;align-items:flex-start;gap:8px;font-size:13px;color:var(--muted)}
.rt-foot .downloads,.rt-foot .share{margin:0;justify-content:flex-start}
.rt-foot .lic{margin:0}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}

@media(min-width:821px) and (max-height:880px){
 .recto{padding-top:24px;padding-bottom:24px}
 .rt-kicker{margin-bottom:14px}
 .rt-title{font-size:clamp(34px,min(4.1vw,6.6vh),62px)}
 .lang-zh .rt-title{font-size:clamp(28px,min(3.1vw,5.2vh),46px)}
 .rt-sub{font-size:17px;margin-top:12px}
 .rt-author{margin-top:16px}.rt-author::before{margin-bottom:10px}
 .rt-blurb{margin-top:12px}
 .recto .actions{margin-top:18px}
 .rt-parts{margin-top:20px}.rt-parts a{padding:5px 2px}
 .rt-foot{margin-top:14px;gap:6px}
}
@media(min-width:821px) and (max-height:700px){
 .rt-parts,.rt-back{display:none}
}
@media(min-width:821px) and (max-height:500px){
 .verso{padding:16px 24px}
 .cv{width:min(100%,450px,calc((100svh - 32px) * 700 / 980))}
 .rt-kicker,.rt-sub,.rt-author{display:none}
 .rt-title{font-size:30px}.lang-zh .rt-title{font-size:26px}
 .rt-blurb{font-size:13.5px;margin-top:8px}
 .recto .actions{margin-top:12px}
 .recto .btn{padding:6px 12px;font-size:14px}
 .rt-foot{margin-top:10px}
}
@media(max-width:820px){
 .spread{display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100svh;padding:clamp(12px,2.6svh,28px) 18px}
 .verso{padding:0;background:none;border:0}
 .cv{width:min(86vw,500px,calc((100svh - 262px) * 700 / 980))}
 .recto{padding:0;max-width:none;align-items:center;text-align:center}
 .rt-kicker,.rt-sub,.rt-author,.rt-parts,.rt-back{display:none}
 .rt-title{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}
 .rt-blurb{margin:clamp(12px,2.2svh,20px) auto 0;font-size:15px;line-height:1.55;max-width:26em}
 .recto .actions{justify-content:center;margin-top:clamp(12px,2svh,18px);gap:8px}
 .recto .btn{padding:8px 15px;font-size:14.5px}
 .rt-foot{align-items:center;margin-top:clamp(10px,1.8svh,16px);gap:6px}
 .rt-foot .downloads,.rt-foot .share{justify-content:center}
 .rt-foot .share{margin-top:0}
}
@media(max-width:820px) and (max-height:740px){
 .cv{width:min(80vw,360px,calc((100svh - 292px) * 700 / 980))}
 .rt-blurb{font-size:13.5px;line-height:1.5;margin-top:10px}
 .recto .actions{margin-top:10px}
 .recto .btn{padding:7px 13px;font-size:14px}
}
@media(prefers-reduced-motion:reduce){
 .cv-fog-a,.cv-fog-b,.cv-top .cv-ping{animation:none}
 .cv-top .cv-ping{opacity:0}
}
"""

# 封面页专用脚本：提灯、开场沿航迹走一遍、标签页隐藏时暂停。
JS = r"""
<script>
(function(){
 var cv=document.querySelector('[data-cover]');if(!cv)return;
 var fog=cv.querySelector('.cv-fog');if(!fog)return;
 var rm=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
 var cur={x:.5,y:.4,r:0},tgt={x:.5,y:.4,r:0},raf=0,last=0,hideT=0,tour=null;
 function write(){fog.style.setProperty('--lx',(cur.x*100).toFixed(2)+'%');
  fog.style.setProperty('--ly',(cur.y*100).toFixed(2)+'%');fog.style.setProperty('--lr',cur.r.toFixed(3));}
 function frame(t){var dt=last?Math.min(64,t-last):16.7;last=t;var moving=false;
  if(tour){var p=Math.min(1,(t-tour.t0)/tour.ms),q=p*(tour.pts.length-1),i=Math.min(tour.pts.length-2,Math.floor(q)),u=q-i,
   a=tour.pts[i],b=tour.pts[i+1],e=u*u*(3-2*u);tgt.x=a[0]+(b[0]-a[0])*e;tgt.y=a[1]+(b[1]-a[1])*e;
   tgt.r=p<.12?p/.12*.9:(p>.86?Math.max(0,(1-p)/.14)*.9:.9);if(p>=1){tour=null;tgt.r=0;}moving=true;}
  var k=1-Math.pow(1-.16,dt/16.7);
  ['x','y','r'].forEach(function(n){var d=tgt[n]-cur[n];if(Math.abs(d)<.0008)cur[n]=tgt[n];else{cur[n]+=d*k;moving=true;}});
  write();raf=moving?requestAnimationFrame(frame):0;if(!moving)last=0;}
 function kick(){if(!raf)raf=requestAnimationFrame(frame);}
 function aim(x,y,r){tour=null;tgt.x=x;tgt.y=y;tgt.r=r;
  if(rm){cur.x=x;cur.y=y;cur.r=r;write();return;}kick();}
 function rel(e){var b=fog.getBoundingClientRect();return[(e.clientX-b.left)/b.width,(e.clientY-b.top)/b.height];}
 cv.addEventListener('pointermove',function(e){if(e.pointerType==='touch')return;var p=rel(e);
  if(tgt.r===0&&cur.r<.05){cur.x=p[0];cur.y=p[1];}aim(p[0],p[1],1);});
 cv.addEventListener('pointerleave',function(e){if(e.pointerType==='touch')return;aim(tgt.x,tgt.y,0);});
 cv.addEventListener('pointerdown',function(e){if(e.pointerType==='mouse')return;var p=rel(e);
  if(cur.r<.05){cur.x=p[0];cur.y=p[1];}aim(p[0],p[1],1.1);clearTimeout(hideT);
  hideT=setTimeout(function(){aim(tgt.x,tgt.y,0);},2800);});
 document.addEventListener('visibilitychange',function(){cv.classList.toggle('is-paused',document.hidden);});
 // 开场：提灯从定位点沿航迹走到礁石，再熄灭
 if(!rm){var pts=__TOUR__;cur.x=pts[0][0];cur.y=pts[0][1];
  setTimeout(function(){if(tgt.r!==0||tour)return;tour={pts:pts,t0:performance.now(),ms:4200};kick();},650);}
})();
</script>
"""


def tour_points():
    """开场提灯的路线，换算成雾层（图廓内框）内的相对坐标。"""
    pts = [FIX] + [(x, y) for x, y, _ in DR] + [(REEF[0], REEF[1])]
    iw, ih = W - 2 * FRAME_IN, H - 2 * FRAME_IN
    return [[round((x - FRAME_IN) / iw, 4), round((y - FRAME_IN) / ih, 4)] for x, y in pts]


def cover_js():
    import json
    return JS.replace("__TOUR__", json.dumps(tour_points()))
