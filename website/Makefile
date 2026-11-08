# 用 uv 自动带上 markdown 依赖；也可先 pip install markdown 再用 python3 直接跑。
RUN ?= uv run --with markdown python3
HOST ?= changkunde
DEST ?= /www/changkun.de/unverifiable-world/

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

# 构建站点并发布到 https://changkun.de/unverifiable-world/。--delete 会删掉服务器上多余的文件，
# 所以 dist/ 里没有 PDF/EPUB 时拒绝发布，以免删掉已发布的下载；先 make book。
deploy: build
	@test -d public/downloads || { echo "dist/ 中没有 PDF/EPUB：先 make book，否则 --delete 会删掉已发布的下载"; exit 1; }
	rsync -az --delete public/ $(HOST):$(DEST)
	@echo "published to https://changkun.de/unverifiable-world/"

clean:
	rm -rf public

.PHONY: all build book release serve deploy clean
