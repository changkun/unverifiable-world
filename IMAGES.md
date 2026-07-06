# 配图索引 Image Index

本书配图全部**自制**，生成脚本在 [`scripts/figures/`](scripts/figures)，输出 SVG 在 [`book/figures/`](book/figures)，可随时重新编译，便于修订与复现。版权归本书所有，随书采用 CC BY-NC-ND 4.0。

目前无网络来源图片纳入版本库。若日后引用网图，将在本表登记标题、来源 URL、作者与许可协议，仅作下载索引，不直接入库（规避版权风险）。

## 重新生成

```bash
python3 scripts/figures/build_all.py          # 生成全部图到 book/figures/
python3 scripts/figures/f07_proxy_2x2.py      # 或单独生成某一张
```

所有图共用零依赖的 SVG 生成库 [`scripts/figures/svg.py`](scripts/figures/svg.py)（纯标准库，中文由查看器字体渲染）。

## 图片清单（自制，CC BY-NC-ND 4.0）

| 编号 | 章节 | 标题 | 生成脚本 | 输出文件 |
| --- | --- | --- | --- | --- |
| F1 | 第 1 章 | 验证：廉价的那一小块，与外头的四处裂口 | `scripts/figures/f01_narrow_door.py` | `book/figures/f01-narrow-door.svg` |
| F2 | 第 2 章 | 不可验证的五种处境：判据 × 解药 | `scripts/figures/f02_five_faces.py` | `book/figures/f02-five-faces.svg` |
| F3 | 第 3 章 | 证实与证伪的不对称 | `scripts/figures/f03_falsification.py` | `book/figures/f03-falsification.svg` |
| F4 | 第 5 章 | 行动、观察、更新回路与期望信息增益 | `scripts/figures/f05_elicitation_loop.py` | `book/figures/f05-elicitation-loop.svg` |
| F5 | 第 6 章 | 允许 / 询问 / 阻止的分级自治 | `scripts/figures/f06_allow_ask_block.py` | `book/figures/f06-allow-ask-block.svg` |
| F6 | 第 11 章（兼第 7、8 章主题） | 代理替换的 2×2：忠实 × 更易 | `scripts/figures/f07_proxy_2x2.py` | `book/figures/f07-proxy-2x2.svg` |
| F7 | 第 8 章（兼第 11 章主题） | Goodhart 崩塌：优化代理，真目标却脱钩 | `scripts/figures/f08_goodhart_curve.py` | `book/figures/f08-goodhart-curve.svg` |
| F8 | 第 10 章 | 冗余的相关性地板 | `scripts/figures/f10_redundancy_floor.py` | `book/figures/f10-redundancy-floor.svg` |
| F9 | 第 11 章 | 标定的可靠性图 | `scripts/figures/f11_calibration.py` | `book/figures/f11-calibration.svg` |
| F10 | 第 12 章 | 纵深防御与瑞士奶酪模型 | `scripts/figures/f12_defense_depth.py` | `book/figures/f12-defense-depth.svg` |
| F11 | 第 13 章 | 八招映射到风险分解的不同部位 | `scripts/figures/f13_eight_levers.py` | `book/figures/f13-eight-levers.svg` |

> 说明：脚本文件名沿用各自所属章节的编号（如第 7 章的 `f07_`、第 13 章的 `f13_`），与上表「编号」列的呈现顺序不完全一致，以「生成脚本／输出文件」两列为准。
