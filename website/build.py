#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把《在无法验证的世界里》构建成一个简单的静态阅读网站。

- 读取仓库根目录的 SUMMARY.md 作为目录结构；
- 每章 Markdown 渲染为 HTML（数学交给 KaTeX 客户端渲染，SVG 图原生显示，
  原始 HTML/JS 原样透传以支持动画）；
- 生成：封面 index.html、目录 toc.html、各章页；
- 每页含常驻顶栏（书名 + 当前章名 + 目录入口，手机端含抽屉菜单）、
  侧栏目录、底部上一页/下一页，手机端另有常驻底部翻页条（含进度）；
- 翻页时有轻量的滑入/滑出动画（尊重「减少动态效果」偏好）。

全部输出使用相对路径，因此可直接部署到任何子路径下（如 changkun.de/xxx/）。

依赖：python3 与 `markdown`（pip install markdown，或用 uv 自动带上）。
用法：python3 website/build.py   →   输出到 website/public/
"""
import html
import os
import re
import shutil
import sys

try:
    import markdown
except ImportError:
    sys.exit("缺少依赖：请先运行  pip install markdown")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUMMARY = os.path.join(ROOT, "SUMMARY.md")
OUT = os.path.join(ROOT, "website", "public")
FIG_SRC = os.path.join(ROOT, "book", "figures")

TITLE = "在无法验证的世界里"
SUBTITLE = "An Unverifiable World"
AUTHOR = "欧长坤"
BLURB = "当对错无从验证，有限的主体如何行动得当？"
# 部署后的站点根地址，用于社交分享的绝对 URL（og:url / og:image）。换部署路径就改这里。
BASE = "https://changkun.de/unverifiable-world"


def head_meta(title, url_path, desc):
    full = f"{title} · {TITLE}" if title and title != TITLE else TITLE
    url = BASE + ("/" + url_path if url_path else "/")
    e = html.escape
    return (
        f'<meta name="description" content="{e(desc)}">'
        f'<meta property="og:type" content="book">'
        f'<meta property="og:site_name" content="{e(TITLE)}">'
        f'<meta property="og:locale" content="zh_CN">'
        f'<meta property="og:title" content="{e(full)}">'
        f'<meta property="og:description" content="{e(desc)}">'
        f'<meta property="og:url" content="{e(url)}">'
        f'<meta property="og:image" content="{BASE}/og.png">'
        f'<meta property="og:image:width" content="1200">'
        f'<meta property="og:image:height" content="630">'
        f'<meta name="twitter:card" content="summary_large_image">'
        f'<meta name="twitter:title" content="{e(full)}">'
        f'<meta name="twitter:description" content="{e(desc)}">'
        f'<meta name="twitter:image" content="{BASE}/og.png">'
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
a{color:#2b4a8b;text-decoration:none}a:hover{text-decoration:underline}

/* 顶栏 */
.topbar{position:sticky;top:0;z-index:50;height:var(--hh);display:flex;align-items:center;gap:12px;
 padding:0 16px;background:rgba(255,255,255,.92);backdrop-filter:blur(6px);border-bottom:1px solid var(--line)}
.topbar .burger{display:none;font-size:22px;line-height:1;background:none;border:none;cursor:pointer;color:var(--ink);padding:4px 6px}
.topbar .bk{font-weight:700;color:var(--ink);white-space:nowrap}
.topbar .cur{color:var(--muted);font-size:14px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;flex:1}
.topbar .cur::before{content:"·　"}
.topbar .toc-link{margin-left:auto;white-space:nowrap;font-size:14.5px}

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


def parse_summary():
    entries, parts = [], []
    cur = None
    for ln in open(SUMMARY, encoding="utf-8"):
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


def sidebar_html(entries, parts, active=None):
    out = [f'<a class="home" href="index.html">{html.escape(TITLE)}</a>',
           f'<div class="sub">{html.escape(AUTHOR)}　·　<a href="toc.html">目录</a></div>']
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


SHARE = """
<div class="share">
  <span class="lbl">分享：</span>
  <button data-share="linkedin">LinkedIn</button>
  <button data-share="x">X / Twitter</button>
  <button data-share="wechat">微信</button>
</div>
"""

QR_MODAL = """
<div class="qr-modal" id="qrModal">
  <div class="qr-card">
    <h4>用微信扫码打开</h4>
    <p>手机微信「扫一扫」打开本页，再点右上角分享给好友或朋友圈</p>
    <div id="qrbox"></div>
    <button class="close" id="qrClose">关闭</button>
  </div>
</div>
"""

import json as _json


def js_block():
    tweet = f"《{TITLE}》 — {BLURB}"
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
 // 分享
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


def topbar(cur_title):
    return (
        '<header class="topbar">'
        '<button class="burger" aria-label="目录">☰</button>'
        f'<a class="bk" href="index.html">{html.escape(TITLE)}</a>'
        f'<span class="cur">{html.escape(cur_title)}</span>'
        '<a class="toc-link" href="toc.html">目录</a>'
        '</header>'
    )


def mobilebar(prevp, nextp, pos):
    pa = (f'<a data-turn href="{prevp[1]}">←</a>' if prevp else '<a class="disabled">←</a>')
    na = (f'<a data-turn href="{nextp[1]}">→</a>' if nextp else '<a class="disabled">→</a>')
    return f'<nav class="mobilebar">{pa}<span class="pos">{pos}</span>{na}</nav>'


def page(title, body, sidebar, active=None, cur_title="", prevp=None, nextp=None, pos="", extra_class="", url_path=""):
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} · {html.escape(TITLE)}</title>
{head_meta(cur_title or title, url_path or active or "", BLURB)}
{KATEX}
<style>{CSS}</style>
</head>
<body>
{topbar(cur_title or title)}
<div class="overlay"></div>
<div class="wrap">
<nav class="sidebar">{sidebar}</nav>
<main class="content {extra_class}">{body}</main>
</div>
{mobilebar(prevp, nextp, pos)}
{QR_MODAL}
{js_block()}
</body>
</html>
"""


def cover_body(entries):
    first = entries[0][1] if entries else "toc.html"
    return f"""
<div class="cover">
  <div class="book">
    <div class="bk-top">
      <div class="t">{html.escape(TITLE)}</div>
      <div class="s">{html.escape(SUBTITLE)}</div>
    </div>
    <img class="bk-art" src="figures/cover-art.svg" alt="">
    <div class="a">{html.escape(AUTHOR)}　著</div>
  </div>
  <p class="blurb">{html.escape(BLURB)}</p>
  <div class="actions">
    <a class="btn primary" href="{first}">开始阅读</a>
    <a class="btn ghost" href="toc.html">目录</a>
  </div>
  {SHARE}
  <p class="muted" style="margin-top:18px;font-size:13.5px">本作品采用 CC BY-NC-ND 4.0 许可</p>
</div>
"""


def cover_page(entries):
    return f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)} · {html.escape(SUBTITLE)}</title>
{head_meta(TITLE, "", BLURB)}
<style>{CSS}</style></head>
<body><div class="wrap" style="display:block">{cover_body(entries)}</div>
{QR_MODAL}
{js_block()}
</body></html>
"""


def toc_page(entries, parts, sidebar):
    out = ['<h1>目录</h1>']
    for ptitle, idxs in parts:
        if ptitle:
            out.append(f'<div class="part">{html.escape(ptitle)}</div>')
        out.append("<ul>")
        for i in idxs:
            t, f, _ = entries[i]
            out.append(f'<li><a data-turn href="{f}">{html.escape(t)}</a></li>')
        out.append("</ul>")
    out.append(SHARE)
    nextp = (entries[0][0], entries[0][1]) if entries else None
    return page("目录", "\n".join(out), sidebar, cur_title="目录",
                nextp=nextp, pos="目录", extra_class="toc-page", url_path="toc.html")


MD_EXT = ["extra", "tables", "fenced_code", "sane_lists", "attr_list"]


def _fixfig(h):
    return h.replace('src="../figures/', 'src="figures/').replace("src='../figures/", "src='figures/")


def render_md(mdpath):
    """返回 (正文 html, 参考文献 html)。后者可能为空。"""
    text = open(mdpath, encoding="utf-8").read()
    if "## 参考文献" in text:
        head, refs = text.split("## 参考文献", 1)
        prose = markdown.markdown(head, extensions=MD_EXT)
        refs_html = '<section class="refs">' + markdown.markdown("## 参考文献" + refs, extensions=MD_EXT) + '</section>'
    else:
        prose, refs_html = markdown.markdown(text, extensions=MD_EXT), ""
    return _fixfig(prose), _fixfig(refs_html)


def endnav_html(prevp, nextp):
    nxt = (f'<a class="go-next" data-turn href="{nextp[1]}">下一章：{html.escape(nextp[0])} →</a>'
           if nextp else '<a class="go-next" data-turn href="toc.html">读完了，返回目录 →</a>')
    prv = (f'<a class="go-prev" data-turn href="{prevp[1]}">← {html.escape(prevp[0])}</a>' if prevp else "")
    return f'<div class="endnav">{nxt}{prv}</div>'


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    if os.path.isdir(FIG_SRC):
        shutil.copytree(FIG_SRC, os.path.join(OUT, "figures"))
    ogp = os.path.join(ROOT, "website", "og.png")
    if os.path.isfile(ogp):
        shutil.copy(ogp, os.path.join(OUT, "og.png"))

    entries, parts = parse_summary()
    n = len(entries)

    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(cover_page(entries))
    open(os.path.join(OUT, "toc.html"), "w", encoding="utf-8").write(
        toc_page(entries, parts, sidebar_html(entries, parts)))

    for i, (title, fname, mdpath) in enumerate(entries):
        prose, refs = render_md(mdpath)
        prevp = (entries[i - 1][0], entries[i - 1][1]) if i > 0 else None
        nextp = (entries[i + 1][0], entries[i + 1][1]) if i < n - 1 else None
        prev_a = (f'<a data-turn href="{prevp[1]}">← {html.escape(prevp[0])}</a>' if prevp
                  else '<a data-turn href="index.html">← 封面</a>')
        next_a = (f'<a data-turn href="{nextp[1]}">{html.escape(nextp[0])} →</a>' if nextp
                  else '<a data-turn href="toc.html">目录 →</a>')
        # 章末跳转放在正文之后、参考文献之前；底部再保留一组上一页/下一页。
        body = (prose + endnav_html(prevp, nextp) + refs
                + f'<div class="nav">{prev_a}<span class="spacer"></span>{next_a}</div>' + SHARE)
        open(os.path.join(OUT, fname), "w", encoding="utf-8").write(
            page(title, body, sidebar_html(entries, parts, active=fname),
                 active=fname, cur_title=title, prevp=prevp, nextp=nextp, pos=f"{i + 1} / {n}"))

    print(f"已生成 {n} 章 + 封面 + 目录 到 {os.path.relpath(OUT, ROOT)}/")
    print("本地预览： make serve  →  http://localhost:8000")


if __name__ == "__main__":
    main()
