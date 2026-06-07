#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成所有自制配图：依次运行本目录下每个 f*.py 模块的 build()。

输出 SVG 到 book/figures/。用法：
    python3 scripts/figures/build_all.py
"""
import glob
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    mods = sorted(glob.glob(os.path.join(HERE, "f*.py")))
    if not mods:
        print("没有找到 f*.py 配图脚本")
        return
    for path in mods:
        name = os.path.basename(path)[:-3]
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        if hasattr(mod, "build"):
            out = mod.build()
            print(f"✓ {name} -> {os.path.relpath(out, os.path.join(HERE, '..', '..'))}")
        else:
            print(f"· {name} 无 build()，跳过")


if __name__ == "__main__":
    sys.exit(main())
