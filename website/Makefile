# 用 uv 自动带上 markdown 依赖；也可先 pip install markdown 再用 python3 直接跑。
RUN ?= uv run --with markdown python3

all: build

build:
	$(RUN) build.py

# 编译可下载的 PDF / EPUB（中英各一份）到仓库根的 dist/，需要 pandoc、xelatex、rsvg-convert。
book:
	python3 ../scripts/build_book.py

# 先编书再构建站点：build.py 会把 dist/ 的 PDF/EPUB 收进 public/downloads/ 并在封面显示下载链接。
release: book build

serve: build
	cd public && python3 -m http.server 8000

clean:
	rm -rf public

.PHONY: all build book release serve clean
