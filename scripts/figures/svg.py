# -*- coding: utf-8 -*-
"""极简 SVG 生成库（纯标准库）。

为本书自制配图提供原语：矩形、文本、直线、箭头、折线、坐标轴。
输出 SVG 可在 GitHub 原生渲染，中文由查看器字体显示，无需嵌入字体，
脚本可重新编译，便于修订与版本管理。
"""
from xml.sax.saxutils import escape

# 统一字体栈：尽量命中各平台的无衬线中文字体
FONT = ("-apple-system, 'PingFang SC', 'Hiragino Sans GB', "
        "'Microsoft YaHei', 'Noto Sans CJK SC', 'Source Han Sans SC', "
        "'Segoe UI', Roboto, Helvetica, Arial, sans-serif")

# 一套克制的配色
INK = "#1a1a1a"
MUTED = "#6b7280"
LINE = "#9ca3af"
FILLS = ["#eef2ff", "#ecfdf5", "#fef3c7", "#fee2e2", "#f3e8ff", "#e0f2fe"]
STROKES = ["#6366f1", "#10b981", "#d97706", "#ef4444", "#a855f7", "#0ea5e9"]


class SVG:
    def __init__(self, width, height, bg="#ffffff"):
        self.w, self.h = width, height
        self.parts = []
        if bg:
            self.rect(0, 0, width, height, fill=bg, stroke="none")

    def rect(self, x, y, w, h, fill="#ffffff", stroke=INK, sw=1.5, rx=8, opacity=1.0):
        self.parts.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
            f'rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"/>'
        )

    def line(self, x1, y1, x2, y2, stroke=LINE, sw=1.5, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.parts.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke}" stroke-width="{sw}"{d}/>'
        )

    def arrow(self, x1, y1, x2, y2, stroke=INK, sw=1.8):
        self._ensure_marker(stroke)
        mid = f"arrow-{stroke.lstrip('#')}"
        self.parts.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke}" stroke-width="{sw}" marker-end="url(#{mid})"/>'
        )

    def polyline(self, pts, stroke=STROKES[0], sw=2.2, fill="none"):
        p = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
        self.parts.append(f'<polyline points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def circle(self, x, y, r, fill=INK, stroke="none", sw=1.0):
        self.parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def text(self, x, y, s, size=15, fill=INK, anchor="middle", weight="normal", italic=False):
        st = "italic" if italic else "normal"
        self.parts.append(
            f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" font-style="{st}" fill="{fill}" '
            f'text-anchor="{anchor}" dominant-baseline="middle">{escape(s)}</text>'
        )

    def textbox(self, x, y, lines, size=14, fill=INK, lh=1.45, anchor="middle"):
        """多行文本，自顶向下排版，y 为第一行基线。"""
        for i, ln in enumerate(lines):
            self.text(x, y + i * size * lh, ln, size=size, fill=fill, anchor=anchor)

    def _ensure_marker(self, stroke):
        mid = f"arrow-{stroke.lstrip('#')}"
        tag = f'<marker id="{mid}"'
        if any(tag in p for p in self.parts):
            return
        self.parts.insert(0,
            f'<defs><marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" '
            f'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{stroke}"/></marker></defs>')

    def render(self):
        body = "\n".join(self.parts)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
                f'viewBox="0 0 {self.w} {self.h}" font-family="{FONT}">\n{body}\n</svg>\n')

    def save(self, path):
        import os
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.render())
        return path
