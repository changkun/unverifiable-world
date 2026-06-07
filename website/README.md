# 阅读网站

把《在无法验证的世界里》构建成一个简单的静态阅读网站：封面、目录、各章页（带侧栏目录与上一页／下一页）。

- **数学**：行内 `$...$`、独立 `$$...$$` 交给 KaTeX 在浏览器端渲染。
- **图片**：`book/figures/` 下的 SVG 原生显示。
- **动画**：Markdown 里的原始 HTML/JS 原样透传，可直接嵌入动画 SVG、GIF、`<video>`、Lottie 或任意脚本动画。
- **路径**：输出全用相对路径，因此可直接部署到任何子路径下（如 `changkun.de/xxx/`），无需改 baseURL。

## 构建

只需 Python 3 与 `markdown` 一个依赖。

```bash
make build      # 用 uv 自动带上依赖；输出到 website/public/
make serve      # 构建并本地预览 http://localhost:8000
make clean
```

不用 `uv` 的话：`pip install markdown` 后 `make build RUN=python3`，或直接 `python3 build.py`。

## 部署

`make build` 后，`website/public/` 是一份纯静态站点（HTML + figures/），把它整目录放到你的网站对应子路径下即可，部署方式与 `modern-cpp-tutorial`、`under-the-hood` 一致。本站不需要任何密钥或后端：KaTeX 从公共 CDN 加载，其余皆为静态文件。若希望完全离线、不依赖 CDN，可把 KaTeX 的 css/js 下载到 `public/` 并改 `build.py` 里的 `KATEX` 常量为本地路径。

## 内容来源

目录结构取自仓库根目录的 [`SUMMARY.md`](../SUMMARY.md)，正文取自 [`book/`](../book/)。改书只改 Markdown，重新 `make build` 即可。
