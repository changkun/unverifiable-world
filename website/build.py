#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把《这个无法验证的世界》构建成一个多语言静态阅读网站。

- 中文版读取仓库根目录的 SUMMARY.md，生成在 public/ 根目录；
- 英文版读取 SUMMARY.en.md，生成在 public/en/；
- 每章 Markdown 渲染为 HTML（数学交给 KaTeX 客户端渲染，SVG 图原生显示，
  原始 HTML/JS 原样透传以支持动画）；
- 每页含常驻顶栏、语言切换、侧栏目录、底部上一页/下一页，手机端含抽屉菜单；
- 翻页时有轻量的滑入/滑出动画（尊重「减少动态效果」偏好）。

全部输出使用相对路径，因此可直接部署到任何子路径下（如 changkun.de/xxx/）。

依赖：python3 与 `markdown`（pip install markdown，或用 uv 自动带上）。
用法：python3 website/build.py   →   输出到 website/public/
"""
from dataclasses import dataclass
import html
import json as _json
import os
import posixpath
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cover  # noqa: E402  封面海图（website/cover.py）

try:
    import markdown
except ImportError:
    sys.exit("缺少依赖：请先运行  pip install markdown")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "website", "public")
FIG_SRC = os.path.join(ROOT, "book", "figures")
FIG_EN_SRC = os.path.join(FIG_SRC, "en")
# 部署后的站点根地址，用于社交分享的绝对 URL（og:url / og:image）。换部署路径就改这里。
BASE = "https://changkun.de/unverifiable-world"


@dataclass(frozen=True)
class Lang:
    code: str
    html_lang: str
    og_locale: str
    summary: str
    out_subdir: str
    title: str
    subtitle: str
    author: str
    blurb: str
    labels: dict


ZH = Lang(
    code="zh",
    html_lang="zh-CN",
    og_locale="zh_CN",
    summary=os.path.join(ROOT, "SUMMARY.md"),
    out_subdir="",
    title="这个无法验证的世界",
    subtitle="An Unverifiable World",
    author="欧长坤",
    blurb="当对错无从验证，有限的主体如何行动得当？",
    labels={
        "toc": "目录",
        "menu": "目录",
        "start": "开始阅读",
        "author_line": "{author}　著",
        "license": "本作品采用 CC BY-NC-ND 4.0 许可",
        "share": "分享：",
        "wechat": "微信",
        "qr_title": "用微信扫码打开",
        "qr_text": "手机微信「扫一扫」打开本页，再点右上角分享给好友或朋友圈",
        "close": "关闭",
        "tweet": "《{title}》 — {blurb}",
        "cover": "封面",
        "next_chapter": "下一章：",
        "finished": "读完了，返回目录",
        "language": "English",
        "lang_short": "EN",
        "theme": "切换深浅色",
        "refs_heading": "参考文献",
        "download": "下载全书",
        "kicker": "全书{parts}部 · {chapters}章",
        "chapters": "第 {a}–{b} 章",
        "chapter": "第 {a} 章",
    },
)

EN = Lang(
    code="en",
    html_lang="en",
    og_locale="en_US",
    summary=os.path.join(ROOT, "SUMMARY.en.md"),
    out_subdir="en",
    title="An Unverifiable World",
    subtitle="How bounded actors act when no oracle can say they are right",
    author="Changkun Ou",
    blurb="How should bounded actors act when right and wrong cannot be verified?",
    labels={
        "toc": "Contents",
        "menu": "Contents",
        "start": "Start reading",
        "author_line": "{author}",
        "license": "Licensed under CC BY-NC-ND 4.0",
        "share": "Share:",
        "wechat": "WeChat",
        "qr_title": "Open with WeChat",
        "qr_text": "Scan this page in WeChat, then use WeChat's share menu.",
        "close": "Close",
        "tweet": "{title} — {blurb}",
        "cover": "Cover",
        "next_chapter": "Next chapter:",
        "finished": "Finished. Back to contents",
        "language": "中文",
        "lang_short": "中文",
        "theme": "Toggle theme",
        "refs_heading": "References",
        "missing_title": "Translation pending",
        "missing_body": "This English chapter has not been translated yet. The Chinese original remains available.",
        "read_original": "Read the Chinese original",
        "download": "Download the book",
        "kicker": "{parts} parts · {chapters} chapters",
        "chapters": "Chapters {a}–{b}",
        "chapter": "Chapter {a}",
    },
)

LANGS = (ZH, EN)
DEFAULT_LANG = ZH


def other_lang(lang):
    for candidate in LANGS:
        if candidate.code != lang.code:
            return candidate
    return lang


def public_path(lang, filename):
    if filename == "index.html":
        return f"{lang.out_subdir}/" if lang.out_subdir else ""
    if lang.out_subdir:
        return f"{lang.out_subdir}/{filename}"
    return filename


def absolute_url(path):
    return BASE + ("/" + path if path else "/")


def rel_lang_link(from_lang, to_lang, filename):
    from_dir = from_lang.out_subdir or "."
    target = posixpath.join(to_lang.out_subdir, filename) if to_lang.out_subdir else filename
    return posixpath.relpath(target, from_dir)


def asset_prefix(lang):
    # 每个语种在自己的输出目录下都有一份 figures/，故相对前缀恒为空。
    return ""


def lang_out_dir(lang):
    return os.path.join(OUT, lang.out_subdir) if lang.out_subdir else OUT


def copy_figures(lang):
    """每个语种在自己的输出目录放一份 figures/。英文版先铺中文图作兜底，
    再用 book/figures/en/ 下的英文图覆盖，确保任何一张图都不会缺失。"""
    if not os.path.isdir(FIG_SRC):
        return
    dst = os.path.join(lang_out_dir(lang), "figures")
    if os.path.isdir(dst):
        shutil.rmtree(dst)
    shutil.copytree(FIG_SRC, dst, ignore=shutil.ignore_patterns("en"))
    if lang.code == EN.code and os.path.isdir(FIG_EN_SRC):
        for f in os.listdir(FIG_EN_SRC):
            if f.endswith(".svg"):
                shutil.copy(os.path.join(FIG_EN_SRC, f), os.path.join(dst, f))


def head_meta(lang, title, filename, desc):
    full = f"{title} · {lang.title}" if title and title != lang.title else lang.title
    e = html.escape
    url_path = public_path(lang, filename)
    alternates = []
    for alt in LANGS:
        alt_path = public_path(alt, filename)
        alternates.append(
            f'<link rel="alternate" hreflang="{e(alt.html_lang)}" href="{e(absolute_url(alt_path))}">'
        )
    alternates.append(
        f'<link rel="alternate" hreflang="x-default" href="{e(absolute_url(public_path(DEFAULT_LANG, filename)))}">'
    )
    return (
        f'<meta name="description" content="{e(desc)}">'
        f'<meta property="og:type" content="book">'
        f'<meta property="og:site_name" content="{e(lang.title)}">'
        f'<meta property="og:locale" content="{e(lang.og_locale)}">'
        f'<meta property="og:title" content="{e(full)}">'
        f'<meta property="og:description" content="{e(desc)}">'
        f'<meta property="og:url" content="{e(absolute_url(url_path))}">'
        f'<meta property="og:image" content="{BASE}/og.png">'
        f'<meta property="og:image:width" content="1200">'
        f'<meta property="og:image:height" content="630">'
        f'<meta name="twitter:card" content="summary_large_image">'
        f'<meta name="twitter:title" content="{e(full)}">'
        f'<meta name="twitter:description" content="{e(desc)}">'
        f'<meta name="twitter:image" content="{BASE}/og.png">'
        + "".join(alternates)
    )


# 在样式之前定下深浅色，深色页面不会先闪一下浅色。键与主页、博客共用：
# 只有 'light' 或 'dark' 算选择；没有选择时跟随系统。
THEME_HEAD = """<script>(function(){var t=null;try{t=localStorage.getItem('theme');}catch(e){}
if(t!=='light'&&t!=='dark')t=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';
document.documentElement.setAttribute('data-theme',t);})();</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
"""

MOON = ('<svg class="icon-moon" viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round" d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>')
SUN = ('<svg class="icon-sun" viewBox="0 0 24 24" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="2" '
       'stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42'
       'M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></g></svg>')
MENU = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" d="M4 7h16M4 12h16M4 17h16"/></svg>')


def theme_button(lang, extra=""):
    label = html.escape(lang.labels["theme"])
    cls = "theme-toggle" + (" " + extra if extra else "")
    return f'<button class="{cls}" type="button" aria-label="{label}" title="{label}">{MOON}{SUN}</button>'


KATEX = """
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],throwOnError:false});"></script>
"""

CSS = """
/* changkun.de 的样式：latere.ai 的墨色调（无色相的灰，墨本身即强调色，链接用一处海军蓝），
   界面与正文都用 Inter，中文落到系统的黑体。深浅色由根元素的 data-theme 决定，
   与主页、博客共用 localStorage 的 theme 键。 */
:root{--bg:#ffffff;--bg-raised:#f4f4f4;--bg-code:#f7f7f7;--text:#0d0d0d;--text-prose:#262626;
 --text-secondary:#525252;--text-muted:#666666;--navy:#38538f;--border:rgba(0,0,0,.08);
 --border-strong:rgba(0,0,0,.14);--mark:#fff4d6;--shadow:0 20px 60px rgba(0,0,0,.18);
 --sans:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB','Noto Sans CJK SC','Microsoft YaHei',sans-serif;
 --mono:ui-monospace,'SF Mono',Menlo,Consolas,monospace;
 --ink:var(--text);--muted:var(--text-muted);--line:var(--border);--paper:var(--bg);--hh:69px}
[data-theme="dark"]{--bg:#161616;--bg-raised:#262626;--bg-code:#1d1d1d;--text:#ececec;--text-prose:#d4d4d4;
 --text-secondary:#b4b4b4;--text-muted:#9a9a9a;--navy:#9bb0e4;--border:rgba(255,255,255,.08);
 --border-strong:rgba(255,255,255,.14);--mark:#3a3320;--shadow:0 20px 60px rgba(0,0,0,.6);color-scheme:dark}
*{box-sizing:border-box}
@media(prefers-reduced-motion:no-preference){html,.scroller{scroll-behavior:smooth}}
html{background:var(--bg)}
body{margin:0;background:var(--bg);color:var(--text-secondary);font:16px/1.65 var(--sans);
 -webkit-font-smoothing:antialiased;transition:background-color .3s,color .3s}
::selection{background:#555;color:#fff}
a{color:var(--navy);text-decoration:none}a:hover{text-decoration:underline;text-underline-offset:3px}
a:focus-visible,button:focus-visible{outline:2px solid var(--text);outline-offset:2px;border-radius:4px}
button{font:inherit;color:inherit}

/* 顶栏：与博客的页头相同，左边书名与当前章，右边目录、语言与深浅色两个按钮 */
.topbar{position:relative;z-index:50;height:var(--hh);display:flex;align-items:center;gap:16px;
 padding:16px 16px 16px clamp(16px,2vw,24px);background:var(--bg);border-bottom:1px solid var(--border);transition:background-color .3s}
.topbar .burger{display:none;flex:none;width:36px;height:36px;margin-left:-6px;padding:0;align-items:center;justify-content:center;
 background:none;border:0;border-radius:8px;cursor:pointer;color:var(--text-secondary)}
.topbar .burger:hover{color:var(--text);background:var(--bg-raised)}
.topbar .burger svg{width:20px;height:20px}
.topbar .bk{font-weight:600;color:var(--text);white-space:nowrap}
.topbar .bk:hover{text-decoration:none}
.topbar .cur{color:var(--text-secondary);font-size:14.5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;flex:1;min-width:0}
.topbar .cur::before{content:"/";margin-right:10px;color:var(--text-muted)}
.topbar .toc-link{white-space:nowrap;font-size:15px;color:var(--text-secondary)}
.topbar .toc-link:hover{color:var(--text)}
.topbar .actions{display:flex;align-items:center;gap:8px;flex:none}
.lang-link,.theme-toggle{display:inline-flex;align-items:center;justify-content:center;flex:none;min-width:36px;height:36px;
 padding:0 8px;border:1px solid var(--border-strong);border-radius:8px;background:none;color:var(--text-secondary);
 font-size:13px;font-weight:500;white-space:nowrap;cursor:pointer;transition:color .2s,background-color .2s}
.theme-toggle{width:36px;padding:0}
.lang-link:hover,.theme-toggle:hover{color:var(--text);background:var(--bg-raised);text-decoration:none}
.theme-toggle svg{width:18px;height:18px}
[data-theme="light"] .icon-sun,[data-theme="dark"] .icon-moon{display:none}
/* 封面没有顶栏：按钮在右上角，与主页同一位置 */
.cover-toggle{position:absolute;top:16px;right:16px;z-index:20;background:var(--bg)}

.wrap{display:flex}
.sidebar{width:clamp(260px,20vw,300px);flex:none;border-right:1px solid var(--border);padding:28px 20px;
 overflow-y:auto;overscroll-behavior:contain;background:var(--bg)}
.sidebar .part{font-weight:500;margin:18px 0 6px;font-size:13px;color:var(--text-muted)}
.sidebar ul{list-style:none;padding:0;margin:0}
.sidebar li{margin:1px 0}
.sidebar a{font-size:14px;line-height:1.5;color:var(--text-secondary);display:block;padding:4px 0}
.sidebar a:hover{color:var(--text);text-decoration:none}
.sidebar a.active{color:var(--text);font-weight:600}

.scroller{flex:1;min-width:0}
/* 正文：博客文章的排法 */
.content{min-width:0;padding:48px 56px 90px;max-width:812px;margin:0 auto;font-size:16.5px;line-height:1.85;
 color:var(--text-prose);overflow-wrap:break-word;animation:turnIn .26s ease both}
body.lang-en .content{line-height:1.75}
.content h1{font-size:30px;font-weight:600;line-height:1.3;letter-spacing:-.015em;color:var(--text);margin:0 0 .8em}
.content h2{font-size:23px;font-weight:600;line-height:1.35;letter-spacing:-.01em;color:var(--text);margin:2em 0 .6em}
.content h3{font-size:18.5px;font-weight:600;line-height:1.4;color:var(--text);margin:1.8em 0 .5em}
.content h4{font-size:16.5px;font-weight:600;color:var(--text);margin:1.6em 0 .4em}
.content strong{color:var(--text);font-weight:600}
.content p{margin:0 0 1.1em}
.content a{text-decoration:underline;text-decoration-color:color-mix(in srgb,currentColor 35%,transparent);text-underline-offset:3px}
.content a:hover{text-decoration-color:currentColor}
.content blockquote{margin:1.4em 0;padding:2px 0 2px 18px;border-left:2px solid var(--border-strong);color:var(--text-secondary)}
.content blockquote p:last-child{margin-bottom:0}
.content ul,.content ol{margin:0 0 1.1em;padding-left:1.4em}
.content li{margin:.3em 0}
.content img{max-width:100%;height:auto;display:block;margin:1.6em auto}
.content table{border-collapse:collapse;margin:1.4em 0;font-size:15px;line-height:1.6;width:100%}
.content th,.content td{border-bottom:1px solid var(--border);padding:8px 14px 8px 0;text-align:left;vertical-align:top}
.content th{font-weight:600;color:var(--text);border-bottom-color:var(--border-strong)}
.content code{background:var(--bg-raised);padding:.12em .38em;border-radius:4px;font:.86em var(--mono)}
.content pre{background:var(--bg-code);border:1px solid var(--border);padding:16px 18px;border-radius:10px;overflow:auto;line-height:1.6}
.content pre code{background:none;padding:0;font-size:inherit}
.content hr{border:none;border-top:1px solid var(--border);margin:2em 0}
/* 超宽的独立公式在自身框内横向滚动，避免撑破页面 */
.content .katex-display{overflow-x:auto;overflow-y:hidden;max-width:100%;padding:2px 2px 8px}
.content .katex-display::-webkit-scrollbar{height:6px}
.content .katex-display::-webkit-scrollbar-thumb{background:var(--border-strong);border-radius:3px}
/* 参考文献比正文小一号 */
.content .refs{font-size:14.5px;line-height:1.7;color:var(--text-secondary)}
.content .refs h2{font-size:20px}
.content .refs ol{padding-left:1.5em}
.content .refs li{margin:.5em 0}
.content .refs blockquote{font-size:13px}
.content .refs .katex{font-size:1em}
.content .refs li{scroll-margin-top:16px}
.content .refs li:target{background:var(--mark);border-radius:5px;box-shadow:0 0 0 6px var(--mark)}
/* 正文参考文献角标 */
sup.cite{font-size:.68em;line-height:0;white-space:nowrap}
.content sup.cite a{color:var(--navy);text-decoration:none;font-weight:600;padding:0 1px}
.content sup.cite a:hover{text-decoration:underline}

.nav{display:flex;justify-content:space-between;gap:14px;margin-top:40px;padding-top:18px;border-top:1px solid var(--border);font-size:15px}
.nav a{max-width:46%}.nav .spacer{flex:1}
/* 章末跳转（正文之后、参考文献之前） */
.endnav{display:flex;flex-direction:column;align-items:center;gap:10px;margin:52px 0 6px;padding-top:24px;border-top:1px solid var(--border)}
.content .endnav a{text-decoration:none}
.endnav .go-next{display:inline-block;background:var(--text);color:var(--bg);padding:10px 22px;border-radius:8px;font-size:15px;font-weight:500;text-align:center;transition:opacity .15s}
.endnav .go-next:hover{opacity:.85}
.endnav .go-prev{color:var(--text-muted);font-size:14px}
.endnav .go-prev:hover{color:var(--text)}

/* 翻页动画 */
@keyframes turnIn{from{opacity:0;transform:translateX(16px)}to{opacity:1;transform:none}}
@keyframes turnOut{from{opacity:1;transform:none}to{opacity:0;transform:translateX(-16px)}}
body.turning .content{animation:turnOut .19s ease both}
@media(prefers-reduced-motion:reduce){.content{animation:none}body.turning .content{animation:none}}

/* 抽屉遮罩与手机底栏 */
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.35);z-index:55;touch-action:none}
.overlay.show{display:block}
.mobilebar{display:none}

/* 按钮：主按钮是墨色，其余是描边 */
.btn{display:inline-flex;align-items:center;gap:8px;padding:9px 18px;border-radius:8px;font-size:15px;font-weight:500;
 border:1px solid var(--border-strong);color:var(--text);background:none;transition:background-color .2s,opacity .15s}
.btn:hover{text-decoration:none;background:var(--bg-raised)}
.btn.primary{background:var(--text);color:var(--bg);border-color:var(--text)}
.btn.primary:hover{background:var(--text);opacity:.85}

.downloads{font-size:13.5px;color:var(--text-muted)}
.downloads a{font-weight:500;padding:0 2px}
.toc-page .part{font-weight:600;color:var(--text);margin:28px 0 8px;font-size:16.5px}
.toc-page ul{list-style:none;padding:0}.toc-page li{margin:6px 0;font-size:16px}
.content.toc-page a{text-decoration:none;color:var(--text-secondary)}
.content.toc-page a:hover{color:var(--text)}
.muted{color:var(--text-muted)}

/* 分享 */
.share{display:flex;align-items:center;gap:7px;flex-wrap:wrap;justify-content:center;margin-top:20px;font-size:13px;color:var(--text-muted)}
.share .lbl{margin-right:0}
.share button{cursor:pointer;border:1px solid var(--border-strong);background:none;color:var(--text-secondary);
 border-radius:999px;padding:3px 11px;display:inline-flex;align-items:center;gap:5px;font-size:12.5px;line-height:1.6;transition:color .2s,background-color .2s}
.share button:hover{color:var(--text);background:var(--bg-raised)}
.share .ic{width:15px;height:15px;display:inline-block;vertical-align:-2px}
.qr-modal{display:none;position:fixed;inset:0;z-index:80;align-items:center;justify-content:center;background:rgba(0,0,0,.5)}
.qr-modal.show{display:flex}
.qr-card{background:var(--bg);color:var(--text-secondary);border:1px solid var(--border);border-radius:12px;padding:24px 26px;text-align:center;max-width:300px;box-shadow:var(--shadow)}
.qr-card h4{margin:0 0 4px;font-size:16px;font-weight:600;color:var(--text)}.qr-card p{margin:6px 0 14px;color:var(--text-muted);font-size:13px}
.qr-card #qrbox{display:flex;justify-content:center;min-height:200px;align-items:center;background:#fff;border-radius:8px;padding:8px}
.qr-card .close{margin-top:14px;border:1px solid var(--border-strong);background:none;border-radius:8px;padding:7px 16px;cursor:pointer;font-size:13.5px}
.qr-card .close:hover{background:var(--bg-raised);color:var(--text)}

/* 深色下配图多为浅底 SVG，垫白底以保证可读 */
[data-theme="dark"] .content img{background:#fff;border-radius:6px;padding:10px}

/* 桌面与平板横屏：应用外壳。顶栏和侧栏是固定的框架，正文栏和侧栏各自滚动。
   正文与侧栏用 overscroll-behavior:contain：保留各自的橡皮筋回弹，但不把滚动传给页面，
   所以正文回弹时顶栏和侧栏不动。根元素（html）必须保持默认的 auto：
   Chromium 在视口上设 none 时会连内部滚动容器的回弹一起关掉。页面本身不滚动（overflow:hidden），
   body 上的 none 只是挡住从顶栏发起的滚动传到视口。 */
@media(min-width:821px) and (min-height:500px){
 html.shell{height:100%;overflow:hidden}
 html.shell body{height:100%;height:100dvh;overflow:hidden;overscroll-behavior:none;display:flex;flex-direction:column}
 html.shell .topbar{flex:none}
 html.shell .wrap{flex:1;min-height:0}
 html.shell .scroller{overflow-y:auto;overflow-x:hidden;overscroll-behavior:contain;outline:none}
}

/* 手机、平板竖屏与横屏手机：保留整页滚动（地址栏照常收起），顶栏固定在视口上 */
@media(max-width:820px),(max-height:499px){
 .topbar{position:fixed;top:0;left:0;right:0;gap:12px}
 .wrap{padding-top:var(--hh)}
 /* 正文翻入时右移 16px：裁掉，否则手机会把版面撑宽，整页可以左右晃 */
 .scroller{overflow-x:clip}
 .content .refs li{scroll-margin-top:calc(var(--hh) + 12px)}
 html.drawer-open,html.drawer-open body{overflow:hidden}
 .topbar .burger{display:inline-flex}
 .topbar .toc-link,.topbar .cur{display:none}
 .topbar .bk{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis}
 .sidebar{position:fixed;left:0;top:0;bottom:0;height:auto;z-index:60;width:82vw;max-width:320px;
  transform:translateX(-100%);transition:transform .25s ease}
 .sidebar.open{transform:none;box-shadow:6px 0 30px rgba(0,0,0,.18)}
 .content{padding:28px 16px 96px;font-size:16px}
 .content h1{font-size:26px}
 .content h2{font-size:21px}
 .mobilebar{display:flex;position:fixed;left:0;right:0;bottom:0;z-index:45;height:52px;align-items:center;
  justify-content:space-between;padding:0 8px;background:var(--bg);border-top:1px solid var(--border)}
 .mobilebar a{padding:8px 16px;font-size:20px;color:var(--text)}
 .mobilebar a:hover{text-decoration:none}
 .mobilebar a.disabled{color:var(--border-strong);pointer-events:none}
 .mobilebar .pos{color:var(--text-muted);font-size:13.5px}
 .nav{display:none}
 .content .katex-display{font-size:.9em}
}
"""


def slug(path):
    base = os.path.basename(path)
    return base[:-3] + ".html" if base.endswith(".md") else base


def parse_summary(summary):
    entries, parts = [], []
    cur = None
    for ln in open(summary, encoding="utf-8"):
        ln = ln.rstrip("\n")
        m = re.match(r"^##\s+(.*)$", ln)
        if m:
            cur = (m.group(1).strip(), [])
            parts.append(cur)
            continue
        m = re.match(r"^\s*-\s*\[(.+?)\]\((.+?)\)\s*$", ln)
        if m:
            title, path = m.group(1).strip(), m.group(2).strip()
            entries.append((title, slug(path), os.path.join(ROOT, path)))
            if cur is None:
                cur = ("", [])
                parts.append(cur)
            cur[1].append(len(entries) - 1)
    return entries, parts


def sidebar_html(lang, entries, parts, active=None):
    # 书名与目录已在顶栏，这里只列章节，与《贝叶斯优化》的侧栏相同。
    out = []
    for ptitle, idxs in parts:
        if ptitle:
            out.append(f'<div class="part">{html.escape(ptitle)}</div>')
        out.append("<ul>")
        for i in idxs:
            t, f, _ = entries[i]
            cls = ' class="active"' if f == active else ""
            out.append(f'<li><a{cls} href="{f}">{html.escape(t)}</a></li>')
        out.append("</ul>")
    return "\n".join(out)


def share_html(lang):
    return f"""
<div class="share">
  <span class="lbl">{html.escape(lang.labels["share"])}</span>
  <button data-share="linkedin">LinkedIn</button>
  <button data-share="x">X / Twitter</button>
  <button data-share="wechat">{html.escape(lang.labels["wechat"])}</button>
</div>
"""


def qr_modal(lang):
    return f"""
<div class="qr-modal" id="qrModal">
  <div class="qr-card">
    <h4>{html.escape(lang.labels["qr_title"])}</h4>
    <p>{html.escape(lang.labels["qr_text"])}</p>
    <div id="qrbox"></div>
    <button class="close" id="qrClose">{html.escape(lang.labels["close"])}</button>
  </div>
</div>
"""


def js_block(lang):
    tweet = lang.labels["tweet"].format(title=lang.title, blurb=lang.blurb)
    tt = _json.dumps(tweet, ensure_ascii=False)
    return """
<script>
(function(){
 var sb=document.querySelector('.sidebar'),ov=document.querySelector('.overlay'),bg=document.querySelector('.burger');
 var root=document.documentElement;
 // 深浅色：点一下即是选择并记住；未选择时跟随系统
 Array.prototype.forEach.call(document.querySelectorAll('.theme-toggle'),function(b){
   b.addEventListener('click',function(){var t=root.getAttribute('data-theme')==='dark'?'light':'dark';
     root.setAttribute('data-theme',t);try{localStorage.setItem('theme',t);}catch(e){}});});
 if(window.matchMedia)matchMedia('(prefers-color-scheme: dark)').addEventListener('change',function(e){
   var t=null;try{t=localStorage.getItem('theme');}catch(err){}
   if(t!=='light'&&t!=='dark')root.setAttribute('data-theme',e.matches?'dark':'light');});
 // 让当前章节在侧栏里可见（侧栏比视口高时）
 function revealActive(){if(!sb)return;var a=sb.querySelector('a.active');if(!a)return;
   var s=sb.getBoundingClientRect(),r=a.getBoundingClientRect();
   if(r.top<s.top+48||r.bottom>s.bottom-48)sb.scrollTop+=r.top-s.top-(s.height-r.height)/2;}
 function setDrawer(open){if(!sb)return;sb.classList.toggle('open',open);if(ov)ov.classList.toggle('show',open);
   root.classList.toggle('drawer-open',open);if(bg)bg.setAttribute('aria-expanded',open?'true':'false');if(open)revealActive();}
 function closeDrawer(){setDrawer(false);}
 if(bg)bg.addEventListener('click',function(){setDrawer(!sb.classList.contains('open'));});
 if(ov)ov.addEventListener('click',closeDrawer);
 document.addEventListener('keydown',function(e){if(e.key==='Escape'&&sb&&sb.classList.contains('open'))closeDrawer();});
 revealActive();
 // 桌面外壳：正文栏是独立的滚动容器。浏览器只替根滚动记位置，所以这里自己把
 // 正文栏的位置记进 history.state，供前进/后退（含参考文献角标跳转后返回）与刷新时恢复。
 var sc=document.querySelector('.scroller');
 function inShell(){return !!sc&&/(auto|scroll)/.test(getComputedStyle(sc).overflowY);}
 if(sc){
   var jumpTo=function(y){var b=sc.style.scrollBehavior;sc.style.scrollBehavior='auto';sc.scrollTop=y;sc.style.scrollBehavior=b;};
   var saveY=function(){if(!inShell())return;try{var st=history.state,o={};
     if(st&&typeof st==='object')for(var k in st)o[k]=st[k];
     if(o.uwY===sc.scrollTop)return;o.uwY=sc.scrollTop;history.replaceState(o,'');}catch(e){}};
   var tm=0;sc.addEventListener('scroll',function(){clearTimeout(tm);tm=setTimeout(saveY,160);},{passive:true});
   // 点任何链接前先记一次：翻页、角标跳转都不会丢掉当前位置
   document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href]');if(a)saveY();},true);
   var nav=(performance.getEntriesByType&&performance.getEntriesByType('navigation')[0])||{};
   var st0=history.state;
   if(inShell()&&st0&&typeof st0.uwY==='number'&&(nav.type==='back_forward'||nav.type==='reload')){
     var y0=st0.uwY,touched=false;jumpTo(y0);
     ['wheel','touchstart','keydown','pointerdown'].forEach(function(ev){window.addEventListener(ev,function(){touched=true;},{once:true,passive:true});});
     // 公式与配图渲染完后高度会变，读者还没动过就再定位一次
     window.addEventListener('load',function(){if(!touched)jumpTo(y0);});
   }
   window.addEventListener('popstate',function(e){if(!inShell())return;var s=e.state;
     requestAnimationFrame(function(){
       if(s&&typeof s.uwY==='number')jumpTo(s.uwY);
       else if(location.hash){var el=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(el)el.scrollIntoView();}
       else jumpTo(0);});});
   // 键盘滚动（空格、PageDown、方向键）作用于获得焦点的滚动容器
   if(inShell()){sc.setAttribute('tabindex','-1');
     if(!document.activeElement||document.activeElement===document.body)sc.focus({preventScroll:true});}
 }
 var rm=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
 // 从往返缓存（bfcache）回到本页时，撤掉离开时加上的翻页淡出，否则正文会停在透明状态
 window.addEventListener('pageshow',function(e){if(e.persisted)document.body.classList.remove('turning');});
 if(!rm){Array.prototype.forEach.call(document.querySelectorAll('a[data-turn]'),function(a){
   a.addEventListener('click',function(e){var h=a.getAttribute('href');
     if(!h||h.charAt(0)==='#'||a.classList.contains('disabled'))return;
     e.preventDefault();document.body.classList.add('turning');
     setTimeout(function(){location.href=h;},185);});});}
 var TT=__TT__;
 function openShare(k){var u=encodeURIComponent(location.href);
   if(k==='linkedin')window.open('https://www.linkedin.com/sharing/share-offsite/?url='+u,'_blank','noopener,noreferrer,width=720,height=640');
   else if(k==='x')window.open('https://twitter.com/intent/tweet?text='+encodeURIComponent(TT)+'&url='+u,'_blank','noopener,noreferrer,width=560,height=640');
   else if(k==='wechat')showQR();}
 Array.prototype.forEach.call(document.querySelectorAll('[data-share]'),function(b){
   b.addEventListener('click',function(){openShare(b.getAttribute('data-share'));});});
 var qm=document.getElementById('qrModal'),qc=document.getElementById('qrClose');
 function closeQR(){if(qm)qm.classList.remove('show');}
 if(qc)qc.addEventListener('click',closeQR);
 if(qm)qm.addEventListener('click',function(e){if(e.target===qm)closeQR();});
 function renderQR(){var box=document.getElementById('qrbox');if(!box||!window.QRCode)return;
   box.innerHTML='';new QRCode(box,{text:location.href,width:200,height:200,correctLevel:QRCode.CorrectLevel.M});}
 function showQR(){if(qm)qm.classList.add('show');
   if(window.QRCode){renderQR();return;}
   var s=document.createElement('script');
   s.src='https://cdn.jsdelivr.net/npm/qrcodejs@1.0.0/qrcode.min.js';s.onload=renderQR;document.head.appendChild(s);}
 // 记住用户显式选择的语言，避免之后被自动跳转覆盖
 Array.prototype.forEach.call(document.querySelectorAll('[data-setlang]'),function(el){
   el.addEventListener('click',function(){try{localStorage.setItem('uw_lang',el.getAttribute('data-setlang'));}catch(e){}});});
})();
</script>
""".replace("__TT__", tt)


def topbar(lang, cur_title, filename):
    alt = other_lang(lang)
    return (
        '<header class="topbar">'
        f'<button class="burger" aria-label="{html.escape(lang.labels["menu"])}" aria-expanded="false">{MENU}</button>'
        f'<a class="bk" href="index.html">{html.escape(lang.title)}</a>'
        f'<span class="cur">{html.escape(cur_title)}</span>'
        f'<a class="toc-link" href="toc.html">{html.escape(lang.labels["toc"])}</a>'
        '<span class="actions">'
        f'<a class="lang-link" data-setlang="{html.escape(alt.code)}" hreflang="{html.escape(alt.html_lang)}" href="{html.escape(rel_lang_link(lang, alt, filename))}">{html.escape(lang.labels["lang_short"])}</a>'
        f'{theme_button(lang)}'
        '</span>'
        '</header>'
    )


def mobilebar(prevp, nextp, pos):
    pa = (f'<a data-turn href="{prevp[1]}">←</a>' if prevp else '<a class="disabled">←</a>')
    na = (f'<a data-turn href="{nextp[1]}">→</a>' if nextp else '<a class="disabled">→</a>')
    return f'<nav class="mobilebar">{pa}<span class="pos">{pos}</span>{na}</nav>'


def page(lang, title, body, sidebar, filename, active=None, cur_title="", prevp=None, nextp=None, pos="", extra_class=""):
    display_title = cur_title or title
    full_title = f"{title} · {lang.title}" if title != lang.title else lang.title
    return f"""<!DOCTYPE html>
<html lang="{html.escape(lang.html_lang)}" class="shell">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
{THEME_HEAD}<title>{html.escape(full_title)}</title>
{head_meta(lang, display_title, filename, lang.blurb)}
{KATEX}
<style>{CSS}</style>
</head>
<body class="lang-{html.escape(lang.code)}">
{topbar(lang, display_title, filename)}
<div class="overlay"></div>
<div class="wrap">
<nav class="sidebar">{sidebar}</nav>
<div class="scroller">
<main class="content {extra_class}">{body}</main>
</div>
</div>
{mobilebar(prevp, nextp, pos)}
{qr_modal(lang)}
{js_block(lang)}
</body>
</html>
"""


def download_html(lang):
    """封面上的下载区。仅当对应语种的编译文件存在于 public/downloads/ 时显示。"""
    base = f"unverifiable-world-{lang.code}"
    dl_dir = os.path.join(OUT, "downloads")
    prefix = "../" if lang.out_subdir else ""
    links = []
    for ext, label in (("pdf", "PDF"), ("epub", "EPUB")):
        if os.path.isfile(os.path.join(dl_dir, f"{base}.{ext}")):
            links.append(f'<a href="{prefix}downloads/{base}.{ext}">{label}</a>')
    if not links:
        return ""
    return (f'<p class="downloads">{html.escape(lang.labels["download"])}　'
            + " · ".join(links) + "</p>")


ARROW = ('<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" '
         'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<path d="M3 8h10M9 4l4 4-4 4"/></svg>')

def part_rows(lang, entries, parts):
    """封面扉页用的各部：(罗马数字, 去掉「第 N 部」前缀的标题, 章号范围, 首章文件)。"""
    rows = []
    for ptitle, idxs in parts:
        if not ptitle:
            continue
        m = re.match(r"^Part\s+[IVXLC]+\s*[:：]\s*(.+)$", ptitle) or re.match(r"^第.+?部[\s　]+(.+)$", ptitle)
        name = m.group(1).strip() if m else ptitle
        nums = []
        first = None
        for i in idxs:
            mm = re.match(r"^(\d+)\.", entries[i][0])
            if mm:
                nums.append(int(mm.group(1)))
                if first is None:
                    first = entries[i][1]
        if not nums:
            continue
        rows.append((cover.ROMAN[len(rows)], name, (nums[0], nums[-1]), first))
    return rows


def count_word(lang, n):
    """封面上的计数：中文用汉字数字，英文用小数目的英文单词。"""
    if lang.code == "zh":
        if n <= 10:
            return "零一二三四五六七八九十"[n]
        if n < 20:
            return "十" + "零一二三四五六七八九"[n - 10].replace("零", "")
        return "零一二三四五六七八九"[n // 10] + "十" + ("零一二三四五六七八九"[n % 10] if n % 10 else "")
    words = ("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen "
             "fifteen sixteen seventeen eighteen nineteen twenty").split()
    return words[n] if n < len(words) else str(n)


def cover_body(lang, entries, parts):
    first = entries[0][1] if entries else "toc.html"
    author_line = lang.labels["author_line"].format(author=lang.author)
    rows = part_rows(lang, entries, parts)
    n_ch = sum(b - a + 1 for _, _, (a, b), _ in rows)
    kicker = lang.labels["kicker"].format(parts=count_word(lang, len(rows)), chapters=count_word(lang, n_ch))
    e = html.escape
    alt = other_lang(lang)
    art = cover.cover_art(lang.code, lang.title, lang.subtitle, author_line, [r[1] for r in rows])
    if lang.code == "en" and " " in lang.title:
        i = lang.title.rfind(" ")
        h1 = f"<span>{e(lang.title[:i])}</span> <span>{e(lang.title[i + 1:])}</span>"
    else:
        h1 = e(lang.title)
    items = []
    for num, name, (a, b), f in rows:
        rng = lang.labels["chapters"].format(a=a, b=b) if a != b else lang.labels["chapter"].format(a=a)
        items.append(f'<li><a data-turn href="{f}"><span class="rt-num">{num}</span>'
                     f'<span class="rt-pt">{e(name)}</span><span class="rt-range">{e(rng)}</span></a></li>')
    back = [(t, f) for t, f, _ in entries if not re.match(r"^\d+\.", t)]
    back_html = ""
    if back:
        def short(t):
            return re.split(r"[：:　]", t, maxsplit=1)[0].strip()
        links = '<span aria-hidden="true"> · </span>'.join(
            f'<a data-turn href="{f}">{e(short(t))}</a>' for t, f in back)
        back_html = f'<p class="rt-back">{links}</p>'
    return f"""
<main class="spread">
  <div class="verso">{art}</div>
  <div class="recto">
    <p class="rt-kicker">{e(kicker)}</p>
    <h1 class="rt-title">{h1}</h1>
    <p class="rt-sub">{e(lang.subtitle)}</p>
    <p class="rt-author">{e(author_line)}</p>
    <p class="rt-blurb">{e(lang.blurb)}</p>
    <div class="actions">
      <a class="btn primary" href="{first}">{e(lang.labels["start"])}{ARROW}</a>
      <a class="btn ghost" href="toc.html">{e(lang.labels["toc"])}</a>
      <a class="btn ghost" lang="{e(alt.html_lang)}" data-setlang="{e(alt.code)}" hreflang="{e(alt.html_lang)}" href="{e(rel_lang_link(lang, alt, "index.html"))}">{e(lang.labels["language"])}</a>
    </div>
    <ol class="rt-parts" aria-label="{e(lang.labels["toc"])}">{"".join(items)}</ol>
    {back_html}
    <div class="rt-foot">
      {download_html(lang)}
      {share_html(lang)}
      <p class="lic">{e(lang.labels["license"])}</p>
    </div>
  </div>
</main>
"""


def lang_redirect_script(lang):
    """仅用于默认语言的封面：尊重用户显式选择（localStorage），否则按浏览器语言
    把非该语言的访客跳到另一语种。location.replace 不污染历史。"""
    if lang.code != DEFAULT_LANG.code:
        return ""
    alt = other_lang(lang)
    alt_href = _json.dumps(rel_lang_link(lang, alt, "index.html"))
    code = _json.dumps(lang.code)
    return (
        "<script>(function(){try{"
        "var s=localStorage.getItem('uw_lang');"
        f"if(s){{if(s!=={code})location.replace({alt_href});return;}}"
        "var n=(navigator.language||navigator.userLanguage||'').slice(0,2).toLowerCase();"
        f"if(n&&n!=={code})location.replace({alt_href});"
        "}catch(e){}})();</script>"
    )


def cover_page(lang, entries, parts):
    return f"""<!DOCTYPE html>
<html lang="{html.escape(lang.html_lang)}"><head><meta charset="utf-8">{lang_redirect_script(lang)}
<meta name="viewport" content="width=device-width,initial-scale=1">
{THEME_HEAD}
<title>{html.escape(lang.title)} · {html.escape(lang.subtitle)}</title>
{head_meta(lang, lang.title, "index.html", lang.blurb)}
<style>{CSS}{cover.CSS}</style></head>
<body class="lang-{html.escape(lang.code)} cover-page">{theme_button(lang, "cover-toggle")}{cover_body(lang, entries, parts)}
{qr_modal(lang)}
{js_block(lang)}
{cover.cover_js()}
</body></html>
"""


def toc_page(lang, entries, parts, sidebar):
    out = [f'<h1>{html.escape(lang.labels["toc"])}</h1>']
    for ptitle, idxs in parts:
        if ptitle:
            out.append(f'<div class="part">{html.escape(ptitle)}</div>')
        out.append("<ul>")
        for i in idxs:
            t, f, _ = entries[i]
            out.append(f'<li><a data-turn href="{f}">{html.escape(t)}</a></li>')
        out.append("</ul>")
    out.append(share_html(lang))
    nextp = (entries[0][0], entries[0][1]) if entries else None
    return page(
        lang,
        lang.labels["toc"],
        "\n".join(out),
        sidebar,
        "toc.html",
        cur_title=lang.labels["toc"],
        nextp=nextp,
        pos=lang.labels["toc"],
        extra_class="toc-page",
    )


MD_EXT = ["extra", "tables", "fenced_code", "sane_lists", "attr_list"]


def _fixfig(h, lang):
    prefix = asset_prefix(lang)

    def repl(m):
        return f"src={m.group(1)}{prefix}figures/"

    return re.sub(r"src=(['\"])(?:\.\./)+figures/", repl, h)


def _add_ref_ids(h):
    """按文档顺序给每个 <li> 注入 id="ref-N"，与参考文献的连续编号一一对应，
    供正文角标 <a href="#ref-N"> 跳转。"""
    c = [0]

    def repl(m):
        c[0] += 1
        return f'<li id="ref-{c[0]}"{m.group(1) or ""}>'

    return re.sub(r'<li(\s[^>]*)?>', repl, h)


def missing_translation_html(lang, title, fname):
    original = rel_lang_link(lang, DEFAULT_LANG, fname)
    return f"""
<h1>{html.escape(title)}</h1>
<blockquote>
<p><strong>{html.escape(lang.labels["missing_title"])}</strong></p>
<p>{html.escape(lang.labels["missing_body"])}</p>
</blockquote>
<p><a href="{html.escape(original)}">{html.escape(lang.labels["read_original"])}</a></p>
"""


def split_refs(text, lang):
    markers = [f'## {lang.labels["refs_heading"]}', "## 参考文献", "## References"]
    for marker in markers:
        if marker in text:
            head, refs = text.split(marker, 1)
            return head, marker + refs
    return text, ""


def render_md(lang, mdpath, title, fname):
    """返回 (正文 html, 参考文献 html, 是否为缺失翻译占位)。"""
    if not os.path.isfile(mdpath):
        if lang.code == DEFAULT_LANG.code:
            raise FileNotFoundError(mdpath)
        return missing_translation_html(lang, title, fname), "", True

    text = open(mdpath, encoding="utf-8").read()
    head, refs = split_refs(text, lang)
    prose = markdown.markdown(head, extensions=MD_EXT)
    if refs:
        refs_html = (
            '<section class="refs">'
            + _add_ref_ids(markdown.markdown(refs, extensions=MD_EXT))
            + "</section>"
        )
    else:
        refs_html = ""
    return _fixfig(prose, lang), _fixfig(refs_html, lang), False


def endnav_html(lang, prevp, nextp):
    if nextp:
        nxt = f'<a class="go-next" data-turn href="{nextp[1]}">{html.escape(lang.labels["next_chapter"])} {html.escape(nextp[0])} →</a>'
    else:
        nxt = f'<a class="go-next" data-turn href="toc.html">{html.escape(lang.labels["finished"])} →</a>'
    prv = f'<a class="go-prev" data-turn href="{prevp[1]}">← {html.escape(prevp[0])}</a>' if prevp else ""
    return f'<div class="endnav">{nxt}{prv}</div>'


def build_lang(lang):
    entries, parts = parse_summary(lang.summary)
    n = len(entries)
    out_dir = lang_out_dir(lang)
    os.makedirs(out_dir, exist_ok=True)

    open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8").write(cover_page(lang, entries, parts))
    sidebar = sidebar_html(lang, entries, parts)
    open(os.path.join(out_dir, "toc.html"), "w", encoding="utf-8").write(toc_page(lang, entries, parts, sidebar))

    missing = 0
    for i, (title, fname, mdpath) in enumerate(entries):
        prose, refs, is_missing = render_md(lang, mdpath, title, fname)
        if is_missing:
            missing += 1
        prevp = (entries[i - 1][0], entries[i - 1][1]) if i > 0 else None
        nextp = (entries[i + 1][0], entries[i + 1][1]) if i < n - 1 else None
        prev_a = (
            f'<a data-turn href="{prevp[1]}">← {html.escape(prevp[0])}</a>'
            if prevp
            else f'<a data-turn href="index.html">← {html.escape(lang.labels["cover"])}</a>'
        )
        next_a = (
            f'<a data-turn href="{nextp[1]}">{html.escape(nextp[0])} →</a>'
            if nextp
            else f'<a data-turn href="toc.html">{html.escape(lang.labels["toc"])} →</a>'
        )
        # 章末跳转放在正文之后、参考文献之前；底部再保留一组上一页/下一页。
        body = (
            prose
            + endnav_html(lang, prevp, nextp)
            + refs
            + f'<div class="nav">{prev_a}<span class="spacer"></span>{next_a}</div>'
            + share_html(lang)
        )
        open(os.path.join(out_dir, fname), "w", encoding="utf-8").write(
            page(
                lang,
                title,
                body,
                sidebar_html(lang, entries, parts, active=fname),
                fname,
                active=fname,
                cur_title=title,
                prevp=prevp,
                nextp=nextp,
                pos=f"{i + 1} / {n}",
            )
        )
    return n, missing


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    ogp = os.path.join(ROOT, "website", "og.png")
    if os.path.isfile(ogp):
        shutil.copy(ogp, os.path.join(OUT, "og.png"))

    # 把已编译的 PDF/EPUB（由 scripts/build_book.py 产到 dist/）放进 downloads/，
    # 封面据其存在与否决定是否显示下载链接。
    dist_dir = os.path.join(ROOT, "dist")
    if os.path.isdir(dist_dir):
        dl_dst = os.path.join(OUT, "downloads")
        os.makedirs(dl_dst, exist_ok=True)
        for f in sorted(os.listdir(dist_dir)):
            if f.endswith((".pdf", ".epub")):
                shutil.copy(os.path.join(dist_dir, f), os.path.join(dl_dst, f))

    for lang in LANGS:
        if not os.path.isfile(lang.summary):
            print(f"跳过 {lang.code}: 找不到 {os.path.relpath(lang.summary, ROOT)}")
            continue
        n, missing = build_lang(lang)
        copy_figures(lang)
        note = f"，其中 {missing} 章为英文翻译占位" if missing else ""
        print(f"已生成 {lang.code}: {n} 章 + 封面 + 目录{note}")

    print(f"输出目录：{os.path.relpath(OUT, ROOT)}/")
    print("本地预览： make serve  →  http://localhost:8000")


if __name__ == "__main__":
    main()
