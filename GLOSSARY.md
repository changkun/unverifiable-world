# 术语表 Glossary

中英对照。正文中术语首次出现时附英文原文，统一收入此表。落足点编码见 [`README.md`](README.md)。

> 建设中：下表先收录全书脊柱性术语；随逐章扩写，所有首次出现的术语会陆续补全并按章索引。

## 核心框架 Core framework

| 中文 | English | 简释 |
| --- | --- | --- |
| 不可验证性 | unverifiability | 无法在事前确认某事为真、为对、为安全的处境 |
| 神谕 | oracle | 求知前能给出答案的来源；在复杂性理论中指即时返回正确答案的黑箱 |
| 有限主体 | finite / bounded agent | 时间、算力、信息、知识均受限的行动者 |
| 标定信念 | calibrated belief | 其声称的把握与现实发生频率相符的信念 |

## 五副面孔 The five faces

| 中文 | English | 简释 |
| --- | --- | --- |
| 不可判定 | undecidable | 原则上不存在判定算法（停机问题、Rice 定理） |
| 难解 | intractable | 有算法但代价随规模爆炸（NP 完全） |
| 部分可观测 | partially observable | 据以验证的状态对主体隐藏（POMDP） |
| 预算受限 | budget-limited | 原则上可验，但此主体缺时间／算力／样本（有限理性） |
| 对抗 | adversarial | 系统主动挫败验证（博弈、对抗样本） |

## 八招 The eight moves

| 中文 | English | 攻击的杠杆 |
| --- | --- | --- |
| 代理替换 | proxy substitution | 改变你度量／优化的目标 |
| 证书 / 界 | certificate / bound | 在一个切片上压不确定性 |
| 神谕入回路 | oracle in the loop | 引进你没有的验证能力 |
| 最优筛查 | optimal screening | 最优分配信息预算 |
| 衰减 / 围栏 | decay / fencing / containment | 缩小失败的爆炸半径 |
| 标定 / 概率接受 | calibration | 给残余风险定价 |
| 留痕 / 可审计 | audit trail | 把检查从事前挪到事后 |
| 冗余 / 共识 | redundancy / consensus | 让失败去相关 |

## 重要概念与定律 Key concepts & laws

| 中文 | English | 出处／简释 |
| --- | --- | --- |
| 判定问题 | Entscheidungsproblem | 希尔伯特之问；丘奇、图灵 1936 证其无解 |
| 不完备性定理 | incompleteness theorems | 哥德尔 1931 |
| 归纳问题 | problem of induction | 休谟；有限证据无法证实全称命题 |
| 证伪主义 | falsificationism | 波普尔；理论只能被否证，不能被证实 |
| 古德哈特定律 | Goodhart's law | 指标一旦成为目标即失去其作为指标的可靠性 |
| 可读性 | legibility | 斯科特；国家把社会重塑成可读的形态 |
| 工具性趋同 | instrumental convergence | 不同终极目标趋向相同的工具性子目标 |
| 期望信息增益 | expected information gain (EIG) | 选择最能压缩不确定性的查验 |
| 严格适当评分规则 | strictly proper scoring rule | 使如实报告概率成为最优策略 |
| 保形预测 | conformal prediction | 给出带覆盖保证的预测集 |
| 拜占庭容错 | Byzantine fault tolerance | 部分节点作恶下仍达成共识 |
| 最小权限 | least privilege | 只授予完成本职所必需的最小能力 |
| 有限理性 | bounded rationality | 西蒙；受限主体的满意化决策 |
| 无免费午餐定理 | no free lunch theorem | 所有问题上平均，无算法占优 |
