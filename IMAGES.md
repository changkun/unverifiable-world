# 配图索引 Image Index

本书配图以**自制为主**，生成脚本在 [`scripts/figures/`](scripts/figures)，可随时重新编译，便于修订与复现。网络来源的图片只在此登记来源与下载链接，不直接纳入版本库（规避版权风险）。

## 约定

- **自制图**：脚本 + 输出文件均纳入版本库；输出放 `book/figures/`，脚本放 `scripts/figures/`，命名一一对应。
- **网络图**：仅在下表登记标题、来源 URL、作者、许可协议；如需使用，按链接自行下载，并确认许可允许。
- 生成全部自制图：`python3 scripts/figures/build_all.py`（生成 SVG 与 PNG 到 `book/figures/`）。

## 图片清单

| 编号 | 章节 | 标题 | 类型 | 来源 / 许可 | 生成脚本 | 文件 | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F1 | 序 / 第 1 章 | 验证廉价的窄门 vs 门外的四处裂口 | 自制 | 本书原创，CC BY-NC-ND 4.0 | `scripts/figures/f01_narrow_door.py` | `book/figures/f01-narrow-door.svg` | 待生成 |
| F2 | 第 2 章 | 不可验证的五副面孔（判据 × 补救） | 自制 | 本书原创 | `scripts/figures/f02_five_faces.py` | `book/figures/f02-five-faces.svg` | 待生成 |
| F3 | 第 3 章 | 证实 vs 证伪的不对称 | 自制 | 本书原创 | `scripts/figures/f03_falsification.py` | `book/figures/f03-falsification.svg` | 待生成 |
| F4 | 第 5 章 | 行动—观察—更新回路 + 期望信息增益 | 自制 | 本书原创 | `scripts/figures/f05_elicitation_loop.py` | `book/figures/f05-elicitation-loop.svg` | 待生成 |
| F5 | 第 6 章 | 允许 / 询问 / 阻止的分级自治 | 自制 | 本书原创 | `scripts/figures/f06_allow_ask_block.py` | `book/figures/f06-allow-ask-block.svg` | 待生成 |
| F6 | 第 7 章 | 代理替换的 2×2：忠实 × 更易 | 自制 | 本书原创 | `scripts/figures/f07_proxy_2x2.py` | `book/figures/f07-proxy-2x2.svg` | 待生成 |
| F7 | 第 10 章 | 冗余的相关性地板（方差随 N 与 ρ） | 自制（数据图） | 本书原创 | `scripts/figures/f10_redundancy_floor.py` | `book/figures/f10-redundancy-floor.svg` | 待生成 |
| F8 | 第 11 章 | 标定曲线（可靠性图） | 自制（数据图） | 本书原创 | `scripts/figures/f11_calibration.py` | `book/figures/f11-calibration.svg` | 待生成 |
| F9 | 第 12 章 | 纵深防御：失守概率随层数（独立 vs 相关） | 自制（数据图） | 本书原创 | `scripts/figures/f12_defense_depth.py` | `book/figures/f12-defense-depth.svg` | 待生成 |
| F10 | 第 13 章 | 八招 → 风险分解的四根杠杆 | 自制 | 本书原创 | `scripts/figures/f13_eight_levers.py` | `book/figures/f13-eight-levers.svg` | 待生成 |

> 清单会随逐章扩写增补。每新增一张图，先在此登记，再附脚本与输出。
