#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把《在无法验证的世界里》构建成一个多语言静态阅读网站。

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

try:
    import markdown
except ImportError:
    sys.exit("缺少依赖：请先运行  pip install markdown")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "website", "public")
FIG_SRC = os.path.join(ROOT, "book", "figures")
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
    title="在无法验证的世界里",
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
        "refs_heading": "参考文献",
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
        "refs_heading": "References",
        "missing_title": "Translation pending",
        "missing_body": "This English chapter has not been translated yet. The Chinese original remains available.",
        "read_original": "Read the Chinese original",
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
    return "../" if lang.out_subdir else ""


def lang_out_dir(lang):
    return os.path.join(OUT, lang.out_subdir) if lang.out_subdir else OUT


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


KATEX = """
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],throwOnError:false});"></script>
"""

CSS = """
:root{--ink:#1a1a1a;--muted:#6b7280;--line:#e5e7eb;--accent:#3b4252;--bg:#fbfbf9;--paper:#ffffff;--hh:52px}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);
 font-family:"Noto Serif SC","Songti SC",Georgia,"Times New Roman",serif;line-height:1.85;font-size:18px}
body.lang-en{font-family:Georgia,"Times New Roman",serif;line-height:1.78}
a{color:#2b4a8b;text-decoration:none}a:hover{text-decoration:underline}

/* 顶栏 */
.topbar{position:sticky;top:0;z-index:50;height:var(--hh);display:flex;align-items:center;gap:12px;
 padding:0 16px;background:rgba(255,255,255,.92);backdrop-filter:blur(6px);border-bottom:1px solid var(--line)}
.topbar .burger{display:none;font-size:22px;line-height:1;background:none;border:none;cursor:pointer;color:var(--ink);padding:4px 6px}
.topbar .bk{font-weight:700;color:var(--ink);white-space:nowrap}
.topbar .cur{color:var(--muted);font-size:14px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;flex:1}
.topbar .cur::before{content:"·　"}
body.lang-en .topbar .cur::before{content:"· "}
.topbar .toc-link,.topbar .lang-link{white-space:nowrap;font-size:14.5px}
.topbar .lang-link{border-left:1px solid var(--line);padding-left:12px;color:#374151}

.wrap{display:flex;max-width:1180px;margin:0 auto}
.sidebar{width:280px;flex:none;border-right:1px solid var(--line);padding:24px 20px;
 position:sticky;top:var(--hh);height:calc(100vh - var(--hh));overflow-y:auto;background:var(--paper)}
.sidebar .home{font-weight:700;font-size:16px;display:block;margin-bottom:2px;color:var(--ink)}
.sidebar .sub{color:var(--muted);font-size:12.5px;margin-bottom:16px}
.sidebar .part{font-weight:700;margin:15px 0 6px;font-size:13.5px;color:var(--accent)}
.sidebar ul{list-style:none;padding:0;margin:0}
.sidebar li{margin:3px 0}
.sidebar a{font-size:14.5px;color:#374151;display:block;padding:2px 0}
.sidebar a.active{color:#2b4a8b;font-weight:700}

.content{flex:1;min-width:0;padding:44px 56px 90px;max-width:820px;margin:0 auto;animation:turnIn .26s ease both}
.content h1{font-size:30px;line-height:1.3;margin:.2em 0 .6em}
.content h2{font-size:23px;margin:1.8em 0 .6em;padding-bottom:.2em;border-bottom:1px solid var(--line)}
.content h3{font-size:19px;margin:1.4em 0 .5em}
.content p{margin:1em 0}
.content blockquote{margin:1.2em 0;padding:.4em 1.1em;border-left:3px solid #cbd5e1;color:#374151;background:#f8fafc}
.content img{max-width:100%;height:auto;display:block;margin:1.6em auto}
.content table{border-collapse:collapse;margin:1.4em 0;font-size:15.5px;width:100%}
.content th,.content td{border:1px solid var(--line);padding:7px 11px;text-align:left;vertical-align:top}
.content th{background:#f3f4f6}
.content code{background:#f3f4f6;padding:.1em .35em;border-radius:4px;font-size:.9em}
.content pre{background:#f6f8fa;padding:14px 16px;border-radius:8px;overflow:auto}
.content pre code{background:none;padding:0}
.content hr{border:none;border-top:1px solid var(--line);margin:2em 0}
/* 超宽的独立公式在自身框内横向滚动，避免撑破页面 */
.content .katex-display{overflow-x:auto;overflow-y:hidden;max-width:100%;padding:2px 2px 8px}
.content .katex-display::-webkit-scrollbar{height:6px}
.content .katex-display::-webkit-scrollbar-thumb{background:#d1d5db;border-radius:3px}
/* 参考文献比正文小一号 */
.content .refs{font-size:15px;line-height:1.72;color:#374151}
.content .refs h2{font-size:21px}
.content .refs ol{padding-left:1.5em}
.content .refs li{margin:.5em 0}
.content .refs blockquote{font-size:13px;background:#f8fafc}
.content .refs .katex{font-size:1em}
.content .refs li{scroll-margin-top:64px}
.content .refs li:target{background:#fff7e0;border-radius:5px;box-shadow:0 0 0 6px #fff7e0}
/* 正文参考文献角标 */
sup.cite{font-size:.68em;line-height:0;white-space:nowrap}
sup.cite a{color:#2b4a8b;text-decoration:none;font-weight:600;padding:0 1px}
sup.cite a:hover{text-decoration:underline}

.nav{display:flex;justify-content:space-between;gap:14px;margin-top:40px;padding-top:18px;border-top:1px solid var(--line);font-size:15px}
.nav a{max-width:46%}.nav .spacer{flex:1}
/* 章末跳转（正文之后、参考文献之前） */
.endnav{display:flex;flex-direction:column;align-items:center;gap:10px;margin:52px 0 6px;padding-top:24px;border-top:1px solid var(--line)}
.endnav .go-next{display:inline-block;background:#2b4a8b;color:#fff;padding:11px 26px;border-radius:10px;font-size:16px;text-align:center}
.endnav .go-next:hover{text-decoration:none;background:#23407c}
.endnav .go-prev{color:var(--muted);font-size:14px}

/* 翻页动画 */
@keyframes turnIn{from{opacity:0;transform:translateX(16px)}to{opacity:1;transform:none}}
@keyframes turnOut{from{opacity:1;transform:none}to{opacity:0;transform:translateX(-16px)}}
body.turning .content{animation:turnOut .19s ease both}
@media(prefers-reduced-motion:reduce){.content{animation:none}body.turning .content{animation:none}}

/* 抽屉遮罩与手机底栏 */
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.35);z-index:55}
.overlay.show{display:block}
.mobilebar{display:none}

/* 封面 */
.cover{display:flex;flex-direction:column;align-items:center;justify-content:center;
 min-height:100svh;width:100%;text-align:center;padding:clamp(14px,3vh,40px) 20px}
.book{height:clamp(290px,50vh,470px);width:auto;aspect-ratio:5/7;max-width:84vw;border-radius:6px;
 background:linear-gradient(135deg,#2b3a55 0%,#1b2233 100%);color:#f4f4f2;
 box-shadow:0 24px 60px rgba(20,30,50,.35),inset 4px 0 0 rgba(255,255,255,.12),inset 8px 0 14px rgba(0,0,0,.25);
 display:flex;flex-direction:column;justify-content:space-between;padding:clamp(20px,3.6vh,42px) clamp(18px,5vw,34px)}
.book .t{font-size:clamp(20px,5.6vw,27px);font-weight:700;line-height:1.4;letter-spacing:1px;text-wrap:balance}
.book .s{font-size:13px;color:#aab4c8;letter-spacing:2px;text-transform:uppercase;margin-top:14px}
.book .bk-top{text-align:center}
.book .bk-art{width:62%;align-self:center;margin:6px auto;opacity:.96;filter:drop-shadow(0 4px 14px rgba(0,0,0,.35))}
.book .a{font-size:15px;color:#dfe5ef;text-align:center}
.cover .blurb{color:var(--muted);max-width:520px;margin:30px auto 8px;font-size:16px}
.cover .actions{margin-top:22px;display:flex;gap:14px;flex-wrap:wrap;justify-content:center}
.btn{display:inline-block;padding:10px 22px;border-radius:8px;font-size:15.5px;border:1px solid #2b4a8b}
.btn.primary{background:#2b4a8b;color:#fff}.btn.primary:hover{text-decoration:none;background:#23407c}
.btn.ghost{color:#2b4a8b;background:#fff}.btn.ghost:hover{text-decoration:none;background:#f0f4fb}

.toc-page .part{font-weight:700;color:var(--accent);margin:24px 0 8px;font-size:17px}
.toc-page ul{list-style:none;padding:0}.toc-page li{margin:7px 0;font-size:16.5px}
.muted{color:var(--muted)}

/* 分享 */
.share{display:flex;align-items:center;gap:7px;flex-wrap:wrap;justify-content:center;margin-top:20px;font-size:12.5px;color:var(--muted)}
.share .lbl{margin-right:0}
.share button{font:inherit;cursor:pointer;border:1px solid var(--line);background:#fff;color:#4b5563;
 border-radius:999px;padding:3px 11px;display:inline-flex;align-items:center;gap:5px;font-size:12px;line-height:1.6}
.share button:hover{border-color:#2b4a8b;color:#2b4a8b}
.share .ic{width:15px;height:15px;display:inline-block;vertical-align:-2px}
.qr-modal{display:none;position:fixed;inset:0;z-index:80;align-items:center;justify-content:center;background:rgba(0,0,0,.5)}
.qr-modal.show{display:flex}
.qr-card{background:#fff;border-radius:14px;padding:24px 26px;text-align:center;max-width:300px;box-shadow:0 20px 60px rgba(0,0,0,.3)}
.qr-card h4{margin:0 0 4px;font-size:16px}.qr-card p{margin:6px 0 14px;color:var(--muted);font-size:13px}
.qr-card #qrbox{display:flex;justify-content:center;min-height:200px;align-items:center}
.qr-card .close{margin-top:14px;border:none;background:#f1f5f9;border-radius:8px;padding:7px 16px;cursor:pointer;font:inherit;font-size:13.5px}

@media(max-width:820px){
 body{font-size:17px}
 .topbar .burger{display:block}
 .topbar .toc-link{display:none}
 .topbar .bk{max-width:45vw;overflow:hidden;text-overflow:ellipsis}
 .topbar .lang-link{padding-left:10px}
 .sidebar{position:fixed;left:0;top:0;height:100vh;z-index:60;width:82vw;max-width:320px;
  transform:translateX(-100%);transition:transform .25s ease;box-shadow:6px 0 30px rgba(0,0,0,.18)}
 .sidebar.open{transform:none}
 .content{padding:26px 20px 96px}
 .mobilebar{display:flex;position:fixed;left:0;right:0;bottom:0;z-index:45;height:52px;align-items:center;
  justify-content:space-between;padding:0 8px;background:rgba(255,255,255,.95);backdrop-filter:blur(6px);
  border-top:1px solid var(--line)}
 .mobilebar a{padding:8px 16px;font-size:20px;color:#2b4a8b}
 .mobilebar a.disabled{color:#cbd5e1;pointer-events:none}
 .mobilebar .pos{color:var(--muted);font-size:13.5px}
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
    out = [
        f'<a class="home" href="index.html">{html.escape(lang.title)}</a>',
        f'<div class="sub">{html.escape(lang.author)} · <a href="toc.html">{html.escape(lang.labels["toc"])}</a></div>',
    ]
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
 function closeDrawer(){if(sb)sb.classList.remove('open');if(ov)ov.classList.remove('show');}
 if(bg)bg.addEventListener('click',function(){sb.classList.toggle('open');ov.classList.toggle('show');});
 if(ov)ov.addEventListener('click',closeDrawer);
 var rm=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
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
})();
</script>
""".replace("__TT__", tt)


def topbar(lang, cur_title, filename):
    alt = other_lang(lang)
    return (
        '<header class="topbar">'
        f'<button class="burger" aria-label="{html.escape(lang.labels["menu"])}">☰</button>'
        f'<a class="bk" href="index.html">{html.escape(lang.title)}</a>'
        f'<span class="cur">{html.escape(cur_title)}</span>'
        f'<a class="toc-link" href="toc.html">{html.escape(lang.labels["toc"])}</a>'
        f'<a class="lang-link" hreflang="{html.escape(alt.html_lang)}" href="{html.escape(rel_lang_link(lang, alt, filename))}">{html.escape(lang.labels["lang_short"])}</a>'
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
<html lang="{html.escape(lang.html_lang)}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(full_title)}</title>
{head_meta(lang, display_title, filename, lang.blurb)}
{KATEX}
<style>{CSS}</style>
</head>
<body class="lang-{html.escape(lang.code)}">
{topbar(lang, display_title, filename)}
<div class="overlay"></div>
<div class="wrap">
<nav class="sidebar">{sidebar}</nav>
<main class="content {extra_class}">{body}</main>
</div>
{mobilebar(prevp, nextp, pos)}
{qr_modal(lang)}
{js_block(lang)}
</body>
</html>
"""


def cover_body(lang, entries):
    first = entries[0][1] if entries else "toc.html"
    author_line = lang.labels["author_line"].format(author=lang.author)
    return f"""
<div class="cover">
  <div class="book">
    <div class="bk-top">
      <div class="t">{html.escape(lang.title)}</div>
      <div class="s">{html.escape(lang.subtitle)}</div>
    </div>
    <img class="bk-art" src="{asset_prefix(lang)}figures/cover-art.svg" alt="">
    <div class="a">{html.escape(author_line)}</div>
  </div>
  <p class="blurb">{html.escape(lang.blurb)}</p>
  <div class="actions">
    <a class="btn primary" href="{first}">{html.escape(lang.labels["start"])}</a>
    <a class="btn ghost" href="toc.html">{html.escape(lang.labels["toc"])}</a>
    <a class="btn ghost" hreflang="{html.escape(other_lang(lang).html_lang)}" href="{html.escape(rel_lang_link(lang, other_lang(lang), "index.html"))}">{html.escape(lang.labels["language"])}</a>
  </div>
  {share_html(lang)}
  <p class="muted" style="margin-top:18px;font-size:13.5px">{html.escape(lang.labels["license"])}</p>
</div>
"""


def cover_page(lang, entries):
    return f"""<!DOCTYPE html>
<html lang="{html.escape(lang.html_lang)}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(lang.title)} · {html.escape(lang.subtitle)}</title>
{head_meta(lang, lang.title, "index.html", lang.blurb)}
<style>{CSS}</style></head>
<body class="lang-{html.escape(lang.code)}"><div class="wrap" style="display:block">{cover_body(lang, entries)}</div>
{qr_modal(lang)}
{js_block(lang)}
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

    open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8").write(cover_page(lang, entries))
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
    if os.path.isdir(FIG_SRC):
        shutil.copytree(FIG_SRC, os.path.join(OUT, "figures"))
    ogp = os.path.join(ROOT, "website", "og.png")
    if os.path.isfile(ogp):
        shutil.copy(ogp, os.path.join(OUT, "og.png"))

    for lang in LANGS:
        if not os.path.isfile(lang.summary):
            print(f"跳过 {lang.code}: 找不到 {os.path.relpath(lang.summary, ROOT)}")
            continue
        n, missing = build_lang(lang)
        note = f"，其中 {missing} 章为英文翻译占位" if missing else ""
        print(f"已生成 {lang.code}: {n} 章 + 封面 + 目录{note}")

    print(f"输出目录：{os.path.relpath(OUT, ROOT)}/")
    print("本地预览： make serve  →  http://localhost:8000")


if __name__ == "__main__":
    main()
