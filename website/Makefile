# 用 uv 自动带上 markdown 依赖；也可先 pip install markdown 再用 python3 直接跑。
RUN ?= uv run --with markdown python3

all: build

build:
	$(RUN) build.py

serve: build
	cd public && python3 -m http.server 8000

clean:
	rm -rf public

.PHONY: all build serve clean
