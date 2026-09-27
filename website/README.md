# 阅读网站

把《这个无法验证的世界》构建成一个简单的多语言静态阅读网站：封面、目录、各章页（带侧栏目录、语言切换与上一页／下一页）。

- **数学**：行内 `$...$`、独立 `$$...$$` 交给 KaTeX 在浏览器端渲染。
- **图片**：`book/figures/` 下的 SVG 原生显示。
- **动画**：Markdown 里的原始 HTML/JS 原样透传，可直接嵌入动画 SVG、GIF、`<video>`、Lottie 或任意脚本动画。
- **多语言**：中文输出在 `public/` 根目录，英文输出在 `public/en/`。每页会生成 `hreflang` alternate 元信息，并在顶栏提供语言切换。
- **封面**：[`cover.py`](cover.py) 在构建时按 SUMMARY 各部生成一张「雾中推算航迹」海图（内联 SVG，随系统深浅色），配 CSS 雾层与指针提灯；旁边是带各部目录的扉页。
- **路径**：输出全用相对路径，因此可直接部署到任何子路径下（如 `changkun.de/xxx/`），无需改 baseURL。

## 构建

只需 Python 3 与 `markdown` 一个依赖。

```bash
make build      # 用 uv 自动带上依赖；输出到 website/public/
make serve      # 构建并本地预览 http://localhost:8000
make clean
```

不用 `uv` 的话：`pip install markdown` 后 `make build RUN=python3`，或直接 `python3 build.py`。

## 可下载的 PDF / EPUB

整本书可编译成 PDF 与 EPUB（中英各一份），供读者从封面直接下载。

```bash
make book       # 编译到仓库根 dist/：unverifiable-world-{zh,en}.{pdf,epub}
make release    # 先 make book 再 make build：把 dist/ 收进 public/downloads/ 并在封面显示下载入口
```

`make book` 调用 [`scripts/build_book.py`](../scripts/build_book.py)，依赖 **pandoc**、**xelatex**（含 CJK 字体，默认 Songti SC）、**rsvg-convert**。它按 SUMMARY 顺序拼接各章，把正文角标转成上标、把每章末编号参考文献保留为编号列表，并把 `book/figures/`（英文版用 `book/figures/en/`）下的 SVG 栅格化为高清 PNG 供 PDF 嵌入。`dist/` 不纳入版本管理；`build.py` 仅在对应文件存在时才在封面渲染下载链接，因此未编译时站点照常工作。

只产其中一种：`python3 scripts/build_book.py zh pdf`（语种 `zh`/`en` 与格式 `pdf`/`epub` 可任意组合）。

## 部署

`make build` 后，`website/public/` 是一份纯静态站点（HTML + figures/ + en/），把它整目录放到你的网站对应子路径下即可，部署方式与 `modern-cpp-tutorial`、`under-the-hood` 一致。本站不需要任何密钥或后端：KaTeX 从公共 CDN 加载，其余皆为静态文件。若希望完全离线、不依赖 CDN，可把 KaTeX 的 css/js 下载到 `public/` 并改 `build.py` 里的 `KATEX` 常量为本地路径。

## 内容来源

中文目录结构取自仓库根目录的 [`SUMMARY.md`](../SUMMARY.md)，正文取自 [`book/`](../book/)。

英文目录结构取自 [`SUMMARY.en.md`](../SUMMARY.en.md)，正文取自 [`book/en/`](../book/en/)。英文章节文件缺失时，构建器会生成一页明确的 “Translation pending” 占位页，并链接回对应中文原文；补齐同名 Markdown 文件后重新 `make build` 即可替换占位页。
