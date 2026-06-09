# 在无法验证的世界里

> 在没有任何东西能确认你做对了的地方，有限的主体如何行动。

古希腊人出征前去德尔斐求神谕（oracle）；计算机科学家把那个能即时给出正确答案的黑箱也叫神谕。两者共享同一个幻想：动手之前，先把对错验明。这本书讲的，是这个幻想破灭之后的世界。

它的核心论点不是「不同领域面对的是同一个问题」，而是更强、也更站得住的命题：

> **不可验证性（unverifiability）的来源天差地别，但有限主体被逼出来的应对，反复收敛到同一小套。**

全书的贡献，是那张「同一招在多种行话下的对照表」，外加一个解释：为什么偏偏是这几招。

---

## 全书脊柱：八招

面对不可验证，你只能动有限的几根杠杆。本书识别出**八招**，每一招攻击「风险 ≈ 失败概率 × 失败代价」分解里的不同一项：

| 招数 | 攻击的是 | 跨域化名（举例） | 经典败法 |
| --- | --- | --- | --- |
| 代理替换 (proxy substitution) | 你度量什么 | 测试代替正确性证明、benchmark 代替智能、KPI、等价改写 | Goodhart |
| 证书 / 界 (certificate / bound) | 在一个切片上压不确定性 | PAC 界、数值误差界、类型系统、验到高度 T 的零点 | 界外失效 |
| 神谕入回路 (oracle in the loop) | 补上你没有的验证能力 | 主动学习、人在回路、交互式定理证明 | 神谕本身不可靠 |
| 最优筛查 (optimal screening) | 最优地花信息预算 | 实验设计、审计抽样、fuzzing、主动学习采集 | 误设的信息度量 |
| 衰减 / 围栏 (decay / fencing) | 失败的爆炸半径 | 沙箱、最小权限、职责分离、熔断 | 围栏被绕过 |
| 标定 / 概率接受 (calibration) | 显式给残余风险定价 | Miller–Rabin、conformal prediction | 标定漂移 |
| 留痕 / 可审计 (audit trail) | 把检查从事前挪到事后 | Merkle 树、审计日志、预注册 | 没人真去查 |
| 冗余 / 共识 (redundancy / consensus) | 让失败去相关 | 拜占庭容错、同行评审、副本、第二诊疗意见 | 失败其实相关 |

这根脊柱（风险分解 × 八招）是否成立，是全书最大的赌注。诚实的交付边界：目前没有证据说它是**定理**；它至少是一个很强的**经验模式**。第 14 章正面清算这个问题。

## 不可验证的五副面孔

书必须先把差异讲透，才配谈综合。「我没法检验它」其实掩着五种结构不同的处境：

1. **不可判定 (undecidable)** —— 原则上没有判定程序（停机问题、Rice 定理）
2. **难解 (intractable)** —— 能验但代价爆炸（NP 完全、RH 可验到高度 T）
3. **部分可观测 (partially observable)** —— 状态对你隐藏（用户的真实偏好、组织里分布的知识）
4. **预算受限 (budget-limited)** —— 能验，但没那个时间 / 算力 / 样本
5. **对抗 (adversarial)** —— 系统主动挫败验证（会欺骗的对手、有隐藏信息的市场）

---

## 目录

序：[没有神谕的世界](book/00-preface.md)

**第一部　不可验证**（立问题，讲清来源各不相同）
- [1. 验证的奢侈](book/part1/ch01-luxury-of-verification.md)
- [2. 不可验证的五副面孔](book/part1/ch02-five-faces.md)
- [3. 可证伪，不可证实](book/part1/ch03-falsifiable-not-verifiable.md)
- [4. 摊平的诱惑](book/part1/ch04-temptation-to-flatten.md)

**第二部　化身**（走进四个现场，让招数缠绕浮现）
- [5. 控制台前的人](book/part2/ch05-human-at-the-console.md)
- [6. 放出去的智能体](book/part2/ch06-agent-released.md)
- [7. 撞墙的数学家](book/part2/ch07-mathematician-at-the-wall.md)
- [8. 看不见自己的组织](book/part2/ch08-organization-blind-to-itself.md)

**第三部　收敛**（把每招洗净、命名，铺成对照表）
- [9. 压缩未知](book/part3/ch09-compress-the-unknown.md)
- [10. 借来的判断](book/part3/ch10-borrowed-judgment.md)
- [11. 换一个能处理的问题](book/part3/ch11-swap-the-problem.md)
- [12. 管住后果](book/part3/ch12-contain-consequences.md)

**第四部　杠杆**（为什么偏偏是这几招，并诚实清算）
- [13. 八根杠杆](book/part4/ch13-eight-levers.md)
- [14. 是定理，还是模式？](book/part4/ch14-theorem-or-pattern.md)
- [15. 不靠验证的知识](book/part4/ch15-knowledge-without-verification.md)

跋：[学会在没有把握时行动](book/99-afterword.md)

（另见 [`SUMMARY.md`](SUMMARY.md)，供 mdBook / Honkit 构建使用。）

## 全书结构

四部按论证推进排，不按主题堆：

- **第一部** 立问题，并讲清不可验证的来源各不相同，这是后面做综合的「信用额度」。
- **第二部** 走进四个现场，让招数嵌在各自的行话里、彼此缠绕地出现（归纳在前）。
- **第三部** 把每一招从领域里拔出来、洗净、单独命名，一次性铺满所有现场（命名在后）。这是全书的载荷。
- **第四部** 回答「为什么偏偏是这几招」，并诚实清算这究竟是定理还是模式，最后落到认识论。

「现场在前、招式在后」是刻意的：先抽象会显得武断，也浪费案例的说服力。

## 仓库结构

```
book/            正文：每章一个 Markdown 文件，章末自带「参考文献」
  00-preface.md  序
  part1/ … part4/  四部
  99-afterword.md  跋
  en/            英文译稿（按同名章节逐步补齐）
scripts/         工具脚本
  check_citations.py   核查参考文献并下载开放获取 PDF
  figures/             配图的生成脚本（自制图可重新编译）
SUMMARY.md       目录（mdBook / Honkit）
SUMMARY.en.md    英文目录（网站英文版）
GLOSSARY.md      术语表（中英对照）
IMAGES.md        配图索引（来源、许可、下载、生成脚本）
LICENSE          CC BY-NC-ND 4.0
```

## 排版与约定

- 全文 Markdown；数学用 LaTeX（行内 `$...$`、独立 `$$...$$`，KaTeX 渲染，公式内不含中文）；图用脚本生成的 SVG/PNG。
- 中文排版：书／期刊名用《》，论文／报告／预印本用「」；不使用破折号（—／——）。
- 术语首次出现时附英文原文，统一收入 [`GLOSSARY.md`](GLOSSARY.md)。
- 每章自带「参考文献」，每条按落足点标注并附一段中文内容总结。落足点编码：
  - ① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活

## 参考文献与下载

全书参考文献已逐条网络核实。要核查并下载可开放获取的原文：

```bash
python3 scripts/check_citations.py            # 核查并下载到 sources/pdf/
python3 scripts/check_citations.py --no-download   # 只核查
python3 scripts/check_citations.py --chapter ch07  # 只处理某章
```

脚本经 arXiv 编号或 Crossref 解析 DOI，再用 Unpaywall 找开放获取 PDF；结果见 `sources/REPORT.md` 与 `sources/citations.csv`（`sources/` 不纳入版本库）。

## 配图

配图以自制为主，生成脚本在 [`scripts/figures/`](scripts/figures)，可随时重新编译；每张图的来源、许可与生成方式列在 [`IMAGES.md`](IMAGES.md)。

## 谱系（定位用）

- 最近的祖宗：Herbert Simon,《The Sciences of the Artificial》（有限理性、主体与环境的界面）。
- 组织那章：James C. Scott,《Seeing Like a State》（可读性 legibility）。
- 要警惕的反面：《哥德尔、埃舍尔、巴赫》—— 跨域类比漂亮却常被批「只是类比」；本书与它的区别，必须就是那根能被压力测试的脊柱。

## 许可

本作品采用 [CC BY-NC-ND 4.0](LICENSE)（署名—非商业性使用—禁止演绎）。你可自由共享，但须署名、不得商用、不得修改后分发。

## 进度

序、十五章正文与跋均已成稿，全书 532 条参考文献已网络核实并逐条加中文内容总结。正在进行：逐章扩写（补真实案例与研究数据）、术语表汇编、配图。第 7 章第 4 节那段第一人称（作者在黎曼假设等价改写上的工作）为代拟，待作者以真实材料替换。
