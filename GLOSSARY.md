# 术语表 Glossary

中英对照。正文中术语首次出现时附英文原文，统一收入此表。落足点编码见 [`README.md`](README.md)。

> 下分两部分：前几节按主题精选全书脊柱性术语，便于快速查阅；文末「全书术语对照」一节按英文字母汇总全书正文出现的全部核心术语（逐章提取、去重）。正文中术语首次出现处均已附英文原文。

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

## 全书术语对照（按英文排序）

下表汇总全书正文出现的核心术语，逐条由各章提取并去重。

| 中文 | English | 简释 |
| --- | --- | --- |
| 主动学习 | active learning | 模型主动挑选最有信息量的样本请人标注，以最少标注获得最大收益。 |
| 对抗 | adversarial | 对面系统主动挫败你的验证的处境。 |
| 对抗样本 | adversarial examples | 人眼几乎察觉不到的微小扰动即可让高识别率模型出错。 |
| 示能 | affordance | 物体或界面自身暗示其使用方式的属性，使正确用法不言自明。 |
| 代理成本 | agency cost | 代理人利益与委托人偏离时产生的监督、约束与剩余损失。 |
| 算法层 | algorithmic level | 马尔三层次之一，刻画用什么表示与过程来解决问题。 |
| 模糊 | ambiguity | 埃尔斯伯格意义上连概率本身都不明确的处境，催生多先验与稳健理论。 |
| 类比论证 | analogical argument | 以源域与目标域的相关因果或结构联系为依据的推理，巴尔塔为其建立了规范评估框架。 |
| 反脆弱 | antifragility | 塔勒布概念：系统不只在波动中存活，还从中受益，关键在限死下行、保留上行。 |
| 属性替换 | attribute substitution | 卡尼曼与弗雷德里克：直觉判断时人用一个好评估的属性顶替难评估的目标属性。 |
| 审计文化 | audit culture | 问责与审计逻辑渗入机构，把人耗在制造可检查的痕迹上。 |
| 审计社会 | audit society | 鲍尔的概念，验证沦为仪式，生产掌控的表象而非掌控本身。 |
| 贝叶斯确证论 | Bayesian confirmation theory | 豪森与厄巴赫的进路：不作二值判决，而把证据视为按贝叶斯定理对信念概率的连续调整。 |
| 贝叶斯实验设计 | Bayesian experimental design | 把实验设计写成最大化期望信息或效用的优化问题，挑选最能压缩不确定性的问题。 |
| 贝叶斯优化 | Bayesian optimization | 用概率代理模型刻画昂贵黑箱目标的信念，再用采集函数自动选下一个试点。 |
| 信念状态 | belief state | 关于隐藏状态的概率分布，用每次观测去更新，部分可观测的解药。 |
| 爆炸半径 | blast radius | 一个错误或故障一旦发生所能波及的范围，衰减的目标即事前把它圈死。 |
| 有限主体 | bounded agent | 认知与计算资源有限、只能用近似与启发式应对的决策者，全书命题中被逼出应对的那个主体。 |
| 有界最优 | bounded optimality | 不要求输出最优决策，而是在给定计算资源约束下做到所能做的最好。 |
| 有限理性 | bounded rationality | 真实主体算力、时间与信息有限，故求满意而非全局最优；预算受限面孔的思想源头。 |
| 布拉德利-特里模型 | Bradley-Terry model | 给每个对象赋潜在分数，由分数之差经逻辑斯谛函数定胜负概率的成对比较模型。 |
| 预算受限 | budget-constrained | 本可验证，却缺少所需的时间、算力或样本而无法验证。 |
| 举证责任 | burden of proof | 本书自缚的铁律，任何宣称的跨域收敛都必须被证明不只是表面类比。 |
| 拜占庭容错 | Byzantine fault tolerance | 在部分节点任意作恶时仍能达成共识的能力。 |
| 拜占庭将军问题 | Byzantine generals problem | 对抗性共识的经典寓言式刻画。 |
| 标定的信念 | calibrated belief | 为自己把握程度如实定价的信念状态，区别于非此即彼的二值判决。 |
| 标定 | calibration | 为残余风险或信念赋予一个与实际频率相符的概率。 |
| 坎贝尔定律 | Campbell's law | 一个社会指标越被用于决策，越易遭扭曲并扭曲它本要监测的过程。 |
| 能力机制 | capability | 访问权以不可伪造的令牌形式直接附着在引用上，持有令牌才能操作对象。 |
| 证书 | certificate | 有界、局部、可机械复核的保证，证一个切片而非整体 |
| 证书检查 | certificate checking | 不信任产出者、只独立核对其给出的证据。 |
| 证书透明度 | certificate transparency | 不阻止证书错发，而让每张证书进入公开可验不可篡改的日志以便事后发现。 |
| 眼镜蛇效应 | cobra effect | 针对指标设奖反而催生与目标相悖的策略性行为。 |
| 共模故障 | common-mode failure | 多个冗余部件因共同原因一起失效。 |
| 计算层 | computational level | 马尔三层次之一，刻画要解决什么问题、受什么约束，八招活在此层。 |
| 陪审团定理 | Condorcet's jury theorem | 独立判断者各略优于瞎猜时多数票正确率随人数趋于必然。 |
| 围堵 | confinement | 兰普森提出的问题：确保被调用程序无法泄露或滥用它接触到的信息。 |
| 围堵问题 | confinement problem | 如何把程序关进笼子使其无法向未授权方泄露信息。 |
| 保形预测 | conformal prediction | 沃夫克等：不给点判断，而给带覆盖保证的预测集。 |
| 共形预测 | conformal prediction | 几乎不依赖分布假设、给出带覆盖率保证的预测集合的方法。 |
| 共识 | consensus | 多个可能不可靠的节点就同一判决达成一致。 |
| 归纳的协同 | consilience of inductions | 惠威尔提出，一理论若能意外解释另一类无关事实，则是其为真的有力标志。 |
| 可纠正性 | corrigibility | 让有目标的系统配合而非抵抗人类的修正与关停。 |
| 临界指数 | critical exponents | 刻画系统在临界点附近行为的一组幂律指数，决定其所属普适类。 |
| 临界线 | critical line | 复平面上实部等于二分之一的直线 |
| 临界带 | critical strip | 实部介于 0 与 1 之间的竖带，ζ 非平凡零点所在区域 |
| 柯里-霍华德对应 | Curry-Howard correspondence | 命题即类型、证明即程序的一一对应，把检查类型等同于检验证明。 |
| 决策论 | decision theory | 在不确定下按风险（损失期望）选择策略的理论，本章风险分解的学理根子。 |
| 纵深防御 | defense in depth | 叠加多层独立防护，使全部同时失守的概率随层数指数下降（仅当各层独立）。 |
| 刻意的无知 | deliberate ignorance | 主动选择不去知道某些信息，常是理性的应对而非缺陷。 |
| 刻意练习 | deliberate practice | 有明确目标、即时反馈、不断逼近能力边缘的费力训练。 |
| 实验设计 | design of experiments | 用最少试验榨出最多信息的统计方法，最优筛查在科学中的源头。 |
| 生态理性 | ecological rationality | 理性的形态取决于规则与所处环境结构的契合。 |
| 集成 | ensemble | 组合多个弱模型投票以胜过单个强模型的方法。 |
| 判定问题 | Entscheidungsproblem | 希尔伯特与阿克曼之问：能否有机械程序对任意数学命题判定真伪。 |
| 认识论 | epistemology | 研究知识的本性、来源与限度的哲学分支。 |
| 错误预算 | error budget | 谷歌 SRE 实践：为可容忍的失败划定额度，把可靠性当成可经营的资源。 |
| 本质复杂性 | essential complexity | 布鲁克斯区分的软件固有复杂性，无法被任何单一技术（银弹）消除。 |
| 期望信息增益 | expected information gain | 先验与后验之间期望减少的不确定性，最优筛查的最大化目标。 |
| 探索与利用 | exploration and exploitation | 在收集新信息与利用已知最优之间的张力。 |
| 证伪 | falsification | 用一个反例否证理论；与证实的不对称是科学纪律的支点。 |
| 证伪主义 | falsificationism | 波普尔的科学观：以可证伪性而非可证实性作为科学与非科学的分界。 |
| 快而省启发式 | fast-and-frugal heuristics | 吉仁泽提出的简单决策规则，在合适环境里媲美复杂统计推断。 |
| 摊平 | flatten | 把五副结构不同的不可验证面孔强行碾成一个统一问题的错误冲动，本章的中心概念。 |
| 形式证明 | formal proof | 完全机器可逐步核对的证明，把信任从神谕转为证书。 |
| 形式系统 | formal system | 由公理与推理规则定义的符号系统，哥德尔证明其内部存在不可判定的真命题。 |
| 形式化验证 | formal verification | 把证明压成可机械逐行核对的形式对象 |
| 前向安全签名 | forward-secure signature | 密钥定期演进，当前密钥泄露也无法伪造此前时段的签名。 |
| 四色定理 | four color theorem | 首个本质依赖计算机穷举、引发信任争论的重大数学证明。 |
| 函数方程 | functional equation | 把 ζ 在 s 与 1-s 处联系起来的对称关系 |
| 模糊测试 | fuzzing | 向程序喂入随机或畸形输入以撞出崩溃的查验方法；正文已为拉丁写法。 |
| 博弈论 | game theory | 把利益冲突下的多方互动当作可严格分析的对象，对抗面孔的理论源头。 |
| 泛化界 | generalization bound | 在已见样本切片上证出的、对未见数据成立的带置信度误差上界。 |
| 目标误泛化 | goal misgeneralization | 训练规格正确，模型在新环境却保持能力但追求了错误目标。 |
| 良好判断计划 | Good Judgment Project | 特洛克主持的预测锦标赛项目，发掘并研究超级预测者。 |
| 古德哈特定律 | Goodhart's law | 当代理指标被当作目标去优化时，它便不再是好指标，系统会钻其空子。 |
| 群体思维 | groupthink | 群体趋同导致判断相关、丧失冗余价值的失效模式。 |
| 高斯酉系综 | GUE | 随机矩阵理论中本征值统计与 ζ 零点吻合的系综 |
| 哥德尔完备性定理 | Gödel's completeness theorem | 一阶逻辑中逻辑有效等价于可证 |
| 停机问题 | halting problem | 没有算法能对任意「程序加输入」判定它是否会停下，不可判定的干净样板。 |
| 霍夫丁不等式 | Hoeffding's inequality | 有界随机变量之和偏离均值的指数型概率上界，泛化界的概率引擎。 |
| 整体论 | holism (Quine-Duhem thesis) | 假说从不被孤立检验，预测失败时可归咎于某个辅助假定，故反例的指向并不确定。 |
| 人在回路 | human in the loop | 在每个决策点引入懂目标的人来观察反应并纠偏的应对结构。 |
| 人类监督控制 | human supervisory control | 人退到监督者位置，设定目标、监视运行、必要时干预，而非被规格一次性替代。 |
| 实现层 | implementational level | 马尔三层次之一，刻画落在什么物理硬件上。 |
| 不完备性 | incompleteness | 哥德尔结论：任何足够强的一致形式系统都有既不能证明也不能否证的命题。 |
| 归纳 | induction | 由过去经验推断未来的推理，休谟指出它没有逻辑保证。 |
| 信息问责 | information accountability | 把治理重心从事前阻止访问移向事后留痕追责。 |
| 信息流格 | information flow lattice | 丹宁的模型：给数据标安全标签，流动只能沿格的偏序方向进行。 |
| 信息的价值理论 | information value theory | 把一条信息的价值定义为获得它后能改进的决策收益，使获取信息成为可算的决策。 |
| 信息性原理 | informativeness principle | 霍姆斯特伦提出，报酬应挂靠在对努力有信息量的信号上。 |
| 工具性趋同 | instrumental convergence | 为几乎任何目标优化的智能体都会顺带追求自保、获取资源等子目标。 |
| 交互式机器学习 | interactive machine learning | 让人在快速训练-反馈循环里反复修正模型的现场学习方式。 |
| 交互式证明 | interactive proof | 弱验证者靠盘问加随机挑战从不可信证明者榨出可靠判决。 |
| 交互式定理证明 | interactive theorem proving | 人给证明思路、机器逐步核对的证明方式。 |
| 区间算术 | interval arithmetic | 用区间替代浮点数运算以严格框住舍入误差的方法 |
| 难解 | intractable | 判定程序存在但代价大到实际不可行的问题。 |
| 自动化的反讽 | Ironies of Automation | 自动化越接管日常，越把最难的异常处置留给最缺练习的人，监督者反而最没准备。 |
| 被证成的真信念 | justified true belief | 传统哲学对知识的经典定义，要求信念为真且得到证成。 |
| 开普勒猜想 | Kepler conjecture | 球最密堆积的猜想，由黑尔斯团队完成形式化证明 |
| 奈特式不确定性 | Knightian uncertainty | 无法赋予概率的不确定，区别于可量化的风险。 |
| 潜在变量 | latent variable | 不可直接观测、只能从行为旁敲侧击推断的内在状态。 |
| 可读性 | legibility | 斯科特的概念，国家把社会改造成自己读得懂的样子。 |
| 李判据 | Li's criterion | RH 等价于一列由零点定义的实数全部非负 |
| 局部知识 | local knowledge | 关于特定时间地点、分散在个体手中、难以集中的知识。 |
| 对数正态 | log-normal | 对数服从正态分布的重尾分布，常比幂律更好地拟合被误称为幂律的真实数据。 |
| 卢卡斯批判 | Lucas critique | 计量模型估出的参数依赖既有政策环境，据此改政策时结构关系即崩解。 |
| 极大极小期望效用 | maxmin expected utility | 主体持一组先验，按其中最不利者评估行动，是稳健决策的代表形式化。 |
| 哈希树（默克尔树） | Merkle tree | 把大量数据归并成一个根哈希，任一项真伪只需 O(log n) 的路径即可校验。 |
| 米勒-拉宾 | Miller-Rabin | 误判概率随轮数指数下降的概率素性检验 |
| 极小极大 | minimax | 按最坏情形布防、使最大风险最小的决策准则，对抗与统计决策的核心。 |
| 失标 | miscalibration | 声称的把握与现实对不上，如报90%却只有六成成真。 |
| 混合主动式界面 | mixed-initiative user interface | 系统权衡自动行动的收益与打扰用户的代价，懂得何时出手、何时让位于人。 |
| 多即不同 | More Is Different | 安德森的论点，每一层级会涌现新规律，无法由下层定律简单推导。 |
| 多臂老虎机 | multi-armed bandit | 边查边用、需权衡探索与利用的序贯分配问题。 |
| 多重发现 | multiple discovery | 同一想法被互不知情的人几乎同时各自做出的现象，默顿据此论证其为科学常态。 |
| 多任务委托代理 | multitask principal-agent | 重奖可测任务会诱使代理人放弃不可测却重要的工作。 |
| 互信息 | mutual information | 两个随机变量间共享信息量的度量，此处用来量化回答对目标的信息增益。 |
| 纳什均衡 | Nash equilibrium | 没有任何一方能靠单方面改变策略获益的稳定局面。 |
| 自然主义决策 | naturalistic decision making | 克莱因学派，实战专家靠模式识别快速判断而非比较选项。 |
| 无免费午餐 | no free lunch | 沃尔珀特与麦克里迪证明，在所有目标函数上取平均，任何两个优化算法期望表现相同。 |
| 无免费午餐定理 | no free lunch theorem | 在所有可能问题上平均，没有哪个方法优于另一个；必须借问题结构选杠杆。 |
| NP 完全性 | NP-completeness | 库克确立的计算难度概念，表明即便可判定，验证代价也可能爆炸。 |
| 开放世界 | open world | 系统真实遇到的环境是开放未完待续的，已测场景永远只是有限切片。 |
| 神谕 | oracle | 计算理论中能即时给出正确答案的黑箱，喻指行动前的完美验证；本书的核心隐喻。 |
| 他人之心 | other minds | 要满足的目标常锁在他人脑中，无法直接观测因而无法直接验证。 |
| 过优化 | overoptimization | 对代理奖励优化超过某点后，代理得分仍升而真实表现转跌。 |
| PAC-Bayes 界 | PAC-Bayes bound | 对后验分布给出、以 KL 散度为惩罚的泛化界精化；正文已为拉丁写法。 |
| 配对关联 | pair correlation | 刻画 ζ 零点间相对间距分布的统计量 |
| 范式 | paradigm | 库恩用语，指常规科学时期科学家共享的解谜框架，危机后才发生革命式更替。 |
| 部分可观测 | partially observable | 决策相关的状态对主体隐藏，无法被直接观测到。 |
| 路径爆炸 | path explosion | 程序分支数线性增长时执行路径数指数增长，令穷尽测试不可行。 |
| 模式识别 | pattern recognition | 由反馈打磨出的、对情境类型的整体性快速辨认能力。 |
| 个人知识 | personal knowledge | 波兰尼提出，一切认知都含超出可证范围的个人默会托付。 |
| 悲观元归纳 | pessimistic meta-induction | 劳丹提出，历史上成功的理论后来多被推翻，故经验成功不可靠地担保理论为真。 |
| 似真推理 | plausible reasoning | 在缺乏证明时凭类比、归纳、特例掂量命题分量的推理 |
| 部分可观测马尔可夫决策过程 | POMDP | 在隐藏状态下决策的标准框架，靠维持并更新信念状态求解。 |
| 幂律 | power law | 变量分布呈现重尾的标度关系，常被过度宣称为跨系统共有的深层机制。 |
| 寻求权力 | power-seeking | 倾向于趋向保留更多选项的状态，可被证明是最优策略的统计倾向。 |
| 预注册 | preregistration | 在看到数据前登记假说与分析方案，使靶子无法事后挪动，是「留痕」一招在科学中的形态。 |
| 素性检验 | primality test | 判断一个整数是否为素数的算法 |
| 素数定理 | prime number theorem | 素数计数函数渐近于 x/ln x 的结果 |
| 委托代理 | principal-agent | 委托方雇人代为行动、却无法完全观察其努力的关系结构。 |
| 委托代理问题 | principal-agent problem | 委托他人代为行动却无法完全监督时产生的利益偏离结构。 |
| 最小权限 | principle of least privilege | 只给组件完成本职所必需的最小能力，其余一概不给，以缩小被攻破时的破坏。 |
| 最小权限原则 | principle of least privilege | 只赋予组件完成本职所必需的最小能力。 |
| 概率方法 | probabilistic method | 接受有界出错风险、以概率而非二值判决去行动或证明存在性 |
| 概率素性 | probabilistic primality | 以1-ε的概率判定一个数为素数，而非给出确定判决。 |
| PAC 框架 | probably approximately correct (PAC) | 瓦利安特提出的可学习性框架，正文已为拉丁写法，故只入表不再标。 |
| 程序验证 | program verification | 用形式化方法证明程序满足规约；其可信性与极限是本章核心议题。 |
| 携带证明的代码 | proof-carrying code | 不受信代码自带一张可快速核验的安全性证明，宿主无需重新推导。 |
| 证明者 | prover | 交互式证明中强大但不可信、负责作答的一方。 |
| 代理 | proxy | 用一个可测量的替代指标替换无法测量的真实目标。 |
| 代理替换 | proxy substitution | 把原命题换成一个等价但但愿更可解的陈述 |
| 委员会查询 | query by committee | 维持一组相容假设，专挑令委员会分歧最大的样本标注以压缩版本空间。 |
| 并发竞态 | race condition | 并发执行顺序不确定导致的缺陷，Therac-25 事故的技术根因。 |
| 彻底的不确定性 | radical uncertainty | 凯与金术语，无法赋以概率分布的根本不确定，承奈特凯恩斯传统。 |
| 随机森林 | random forest | 靠样本与特征双重随机化培育去相关决策树再投票的集成法。 |
| 递归可枚举 | recursively enumerable | 其成员可被算法一条条列举，但未必能判定非成员 |
| 冗余 | redundancy | 兰道正名的重复与重叠，独立核查比单一权威更难被同时骗过。 |
| 反思性实践者 | reflective practitioner | 舍恩概念，熟练者在行动当下与情境对话并即时调整。 |
| 反身性 | reflexivity | 公开的度量不只描述世界，还会反过来重塑被度量者的行为。 |
| 遗憾 | regret | 策略累积收益与最优策略之差，老虎机最优解使其仅随时间对数增长。 |
| 基于人类反馈的强化学习 | reinforcement learning from human feedback (RLHF) | 用人的成对比较学一个奖励模型作为偏好代理，再据此优化系统的对齐方法。 |
| 重整化群 | renormalization group | 物理学中逐级粗粒化处理跨尺度系统的方法，解释了普适性的来源。 |
| 复制危机 | replication crisis | 当预注册缺位、样本不足、发表偏倚盛行时，已发表结果大量无法重现，科学自我纠错失效。 |
| 研究纲领 | research programme | 拉卡托斯用语，以纲领整体随时间「进步」或「退化」取代非黑即白的单次证伪。 |
| 显示的偏好 | revealed preference | 由一个人的实际选择所暴露出来的真实偏好。 |
| 奖励钻空 | reward hacking | 智能体钻代理奖励的空子，得高分却背离真实目标。 |
| 奖励模型 | reward model | 从人类偏好数据学出、用作真实偏好代理的打分模型。 |
| 赖斯定理 | Rice's theorem | 程序的任何非平凡语义性质都不可判定，把停机问题的不可判定性推到极致。 |
| 黎曼假设 | Riemann hypothesis | ζ 函数全部非平凡零点都落在临界线上的猜想 |
| 稳健控制 | robust control | 不信任手中模型，针对一族邻近模型中最不利者优化，对设定误差稳健。 |
| 鲁棒优化 | robust optimization | 以极小极大形式统一对抗攻防：内层找最坏扰动，外层训练抵御它。 |
| 稳健性 | robustness | 一个结论能从多条相互独立的路径反复导出时更可信的性质。 |
| 稳健性分析 | robustness analysis | 考察结论在多个不同假设模型下是否一致以判断其可靠性的方法，源自莱文斯。 |
| 稳健性论证 | robustness analysis | 若一结论能由多条彼此独立的路径反复抵达，则更可能为真，而非某手段的人为产物。 |
| 沙箱 | sandbox | 为不可信程序构造受限运行环境，把其能造成的破坏圈死在边界内。 |
| 可满足性问题 | satisfiability | 判断布尔公式是否有可使其为真的赋值，第一个被证明 NP 完全的问题。 |
| 满意化 | satisficing | 西蒙：能力与信息有限时不求最优，搜到一个足够好的方案即停。 |
| 满意即止 | satisficing | 西蒙提出的决策准则，找到满足够用水准的方案即停，不求穷尽最优。 |
| 规模 | scale | 门外情形数不过来，使穷尽验证从一开始就失效的第一类裂口。 |
| 标度律 | scaling law | 把过优化等现象的恶化刻画成可测量的定量曲线规律。 |
| 科学营林 | scientific forestry | 为可读可算把天然林改造成单一树种人工林，终致森林崩溃。 |
| 选择效应 | selection effect | 因观察样本被有意无意筛选而造成的系统性偏差，可使虚假模式显得稳健。 |
| 自指 | self-reference | 系统在自身内部指涉或描述自身的情形，与哥德尔不完备性密切相关。 |
| 严苛检验 | severe testing | 梅奥的误差统计原则：假说唯有通过「若为假则极可能不通过」的检验才值得接受。 |
| 软件危机 | software crisis | 1968 年北约会议提出的术语，指软件普遍超期、超支、难以可靠交付的集体困境。 |
| 特殊科学 | special sciences | 福多用语,指心理学、经济学等其规律可多重实现、无法还原为物理学的学科。 |
| 规格博弈 | specification gaming | 系统精确满足写下的目标却违背本意。 |
| 陈述的偏好 | stated preference | 一个人口头说出的、自称想要的东西。 |
| 严格适当评分规则 | strictly proper scoring rule | 使如实报出真实概率恰好让期望得分最优，把诚实由数学结构强制。 |
| 结构实在论 | structural realism | 沃勒尔的折中立场，理论更替时被保留的是其数学结构而非本体描述。 |
| 结构映射 | structure-mapping | 根特纳的类比理论，好的类比迁移的是关系结构而非表面属性。 |
| 结构保持 | structure-preserving | 实质类比的判据，跨域映射须保持机制、失效方式与权衡的对应而非仅表面相似。 |
| 基质 | substrate | 承载行为的底层载体（碳基、硅基或组织），八招因活在计算层而能跨越它。 |
| 超级预测者 | superforecasters | 靠可学习习惯持续做出高准确度预测的普通人。 |
| 默会维度 | tacit dimension | 波兰尼提出的不可言说之知，我们知道的远多于说得出的。 |
| 防篡改日志 | tamper-evident log | 任何事后改动都会在校验时暴露的日志结构，把检查从事前挪到事后。 |
| 关停博弈 | the off-switch game | 把人按停止键建模为博弈，论证目标不确定的智能体会主动保留被关停的可能。 |
| 人工科学 | the sciences of the artificial | 西蒙主张人造物行为由环境约束而非内部构造决定的设计之学。 |
| 三角定位 | triangulation | 用多个相互独立的视角去交叉印证、定位一个无法直接看清的事实或判断。 |
| 信任的校准 | trust calibration | 使人对系统的信任水平与系统真实可靠度相匹配，避免过度信任或弃用可靠系统。 |
| 类型系统 | type system | 对程序施加可判定检查、保证某类性质的形式机制 |
| 不确定性采样 | uncertainty sampling | 优先挑选模型最拿不准（接近决策边界）的样本去标注的主动学习策略。 |
| 未被设想的替代方案 | unconceived alternatives | 斯坦福的论题：科学史表明总有当时想不到的理论选项，故不应相信已穷尽全部解释。 |
| 不可判定 | undecidable | 原则上不存在任何能在有限步内给出答案的判定程序的问题。 |
| 全称命题 | universal statement | 形如「所有 x 都 P」的判断，无法被有限观察证实，却可被单一反例推翻。 |
| 普适类 | universality class | 微观细节迥异却在临界点附近表现出相同行为的一类系统。 |
| 不可验证 | unverifiable | 命题真假原则上无法在可用资源内被确认的状态 |
| VC 维 | Vapnik-Chervonenkis dimension | 刻画函数族容量的指标，决定可学习性与样本复杂度；正文已为拉丁写法。 |
| 证实 | verification | 用有限观察确立一个全称命题为真；波普尔指出这对经验理论根本不可得。 |
| 验证者 | verifier | 交互式证明中算力有限、负责盘问与裁决的一方。 |
| 韦伊猜想 | Weil conjectures | 函数域上的黎曼假设类比，已被德利涅证明 |
| 群体的智慧 | wisdom of crowds | 多样、独立、分散的群体集体判断常胜过专家个人。 |
