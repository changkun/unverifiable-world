# 第 2 章　不可验证的五副面孔

> **论点**：「我没法检验它」掩盖了五种结构不同的处境，把它们混为一谈是这个领域的核心错误。

一句「我没法检验它」，听上去像一种处境，其实掩着五种。它们结构全然不同，可得的补救也全然不同，把它们混为一谈，是这个领域最核心的错误。

这一章要做的，是把五种掰开、各自掐准。这件事看似只是分类的洁癖，实则是全书后半部分的信用额度。本书最终要论证的是，尽管不可验证的来源天差地别，应对却收敛到同一小套。这个论断要想不显得廉价，前提就是先把「天差地别」坐实。差异讲得越透，后面那份收敛才越是值得惊讶、值得解释。所以请把这五副面孔记牢，它们会在全书反复点名。

## 第一副：不可判定

判据：原则上就不存在判定它的算法。不是难，是没有。

这是验证最硬的失败。希尔伯特与阿克曼 1928 年明确提出判定问题，问能否有一个机械程序，对任意数学命题判定其真伪。八年后，丘奇用 lambda 演算、图灵用他那台抽象机器，各自证明：不能。图灵的停机问题尤其干净，没有算法能对任意「程序加输入」判定它是否会停下。哥德尔 1931 年的不完备性、赖斯定理（程序的任何非平凡语义性质都不可判定）、马蒂亚谢维奇 1970 年对希尔伯特第十问题的否决，都属于这一族。

这副面孔的补救有一个独一无二的性质：它永远不会有完整解。再多的时间、再快的机器都不行，因为障碍是逻辑的，不是资源的。你能做的，只有退而求其次，验证有限的切片，或把自己限制在那些确实可判定的片段里（比如只有加法的算术）。这一点会一直回响到第 7 章。

## 第二副：难解

判据：算法存在，但它的代价随规模爆炸，大到实践中跑不完。

这一副和上一副差之毫厘，谬以千里：可判定，却不可行。库克 1971 年、列文 1973 年各自确立的 NP 完全性，卡普 1972 年那著名的二十一个 NP 完全问题，给了它精确的刻画。最坏情形的可满足性问题、无数组合优化问题，原则上都有解法，可那解法在最坏情形下的耗时随输入规模呈指数增长，

$$T(n)\sim 2^{n},$$

几十个变量就足以让最快的超算望洋兴叹。$\mathsf{P}$ 是否等于 $\mathsf{NP}$，正是在问这道墙是不是注定的。

它的补救与不可判定完全不同。这里多投入资源是有意义的，更要紧的是，你可以用「接受少一点」来换「付得起的代价」：近似解代替精确解、平均情形代替最坏情形、启发式、随机化。难解逼出的是一整套「打折」的智慧，这在不可判定那里是没有的。

## 第三副：部分可观测

判据：你要据以验证的那个状态，对你是隐藏的。

不是没有判定程序，也不是代价太大，而是你压根看不到该看的东西。用户真正的偏好、病人体内正在发生什么、对手手里的牌，这些状态驱动着结果，却不对你显现。控制论很早就形式化了它：阿斯特罗姆 1965 年研究状态信息不完整下的最优控制，斯莫尔伍德与桑迪克 1973 年、凯尔布林等人 1998 年把它发展成部分可观测马尔可夫决策过程（POMDP）这一标准框架。帕帕迪米特里乌与齐齐克利斯 1987 年还证明，求解这类问题本身又是难解的，于是第三副面孔常和第二副叠在一起。

它的补救自成一类：你不再追求一个确定的判决，而是维持一个关于隐藏状态的信念分布，并用每一次观测去更新它，

$$b'(s')\ \propto\ \Pr(o\mid s')\sum_{s}\Pr(s'\mid s,a)\,b(s).$$

推断与探查，而不是「算得更狠」，才是这一副的解药。第 5 章整章都在这副面孔里。

## 第四副：预算受限

判据：原则上可验、可解，但你这个主体，此时此地，没有那个时间、算力或样本。

这一副最朴素，也最普遍。一个评审只有二十分钟看一篇论文；一个医生只有几分钟做判断；一个交易员必须在行情消失前下单。验证在理论上完全可行，落到一个有限的主体身上却不可行。奈特 1921 年、西蒙 1955 年的有限理性是它的思想源头；迪安与博迪 1988 年的 anytime 算法（随时可中断、给出当前最优解）、拉塞尔与苏布拉马尼安 1995 年的「有界最优」，是它的形式化。

它的补救有一个别的面孔都没有的特征：这副面孔会随资源增长而消退。给足时间和算力，它就消失了。正因如此，对付它的核心是分配，把稀缺的预算花在边际收益最高处。这条思路，正是后面「最优筛查」那一招的来历。

## 第五副：对抗

判据：你面对的那个系统，在主动地挫败你的验证。

前四副里，难处来自世界的中立属性，逻辑的、规模的、可见性的、资源的。第五副不同：对面有一个智能，在针对你的检查做优化。会撒谎的对手、会伪装的恶意代码、会操纵指标的被考核者。冯·诺依曼与摩根斯特恩 1944 年的博弈论、纳什 1950 年的均衡、瓦尔德 1945 年的极小极大准则，是它的经典理论；塞盖迪等人 2014 年发现的对抗样本、马德里等人 2018 年用鲁棒优化统一攻防，是它在机器学习里的当代化身。一个识别率极高的模型，可以被人眼看不出的微小扰动骗得一塌糊涂，因为有人专门去找那个扰动。

它的补救是战略，不是计算。你要做的不是把某个量算得更准，而是

$$\min_{x}\ \max_{y}\ L(x,y),$$

按最坏情形布防，用随机化剥夺对手对你的预测，追求在博弈里站得住而非在某个固定输入上最优。把对抗当成单纯的可观测缺口（「我只是还没看清它」）来处理，是会出人命的误判，因为它会顺着你的看法调整自己。

## 五副面孔，五种解药

把它们并排放好，要紧的不是名字，是它们的补救彼此不可通约：

- 不可判定，永无完整解，只能退求切片。
- 难解，可用代价换精度，多投资源有意义。
- 部分可观测，靠推断信念、主动探查。
- 预算受限，随资源消退，核心在分配。
- 对抗，是一盘棋，靠战略与随机。

谁要是对你说「这事多堆点算力就解决了」，那他多半是把某一副面孔错认成了另一副。把不可判定当成预算问题，把对抗当成可观测问题，都是这种错认，而且代价高昂。

这些面孔还会叠加、复合。第 6 章那个放出去的智能体，同时撞上开放世界的不可预测（近乎不可判定的行为）和对手的策略性（对抗）；第 8 章那个组织，把部分可观测和对抗一起扛。真实处境往往是好几副面孔的混合。

正因为来源如此参差，补救如此各异，下一个该问的问题就尖锐起来了：人类有没有一套成熟的办法，长期地、有纪律地与不可验证共处？有的。那套办法叫科学，而它的第一条家规，恰恰是公开承认自己永远无法验证。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实；个别未能确证者标「（细节待核）」。

### 不可判定（②③）

1. A. M. Turing (1936).「On Computable Numbers, with an Application to the Entscheidungsproblem」. Proceedings of the London Mathematical Society, s2-42(1), 230–265.（载《伦敦数学会会刊》第二辑第 42 卷；「s2」即 series 2，第二辑，卷号 42。常被引为 1936 或 1937 年，以读交年 1936 为准。）[②③]
2. A. Church (1936).「An Unsolvable Problem of Elementary Number Theory」. American Journal of Mathematics, 58(2), 345–363.（早于图灵约七个月，以 lambda 演算给出判定问题不可解的证明。）[②③]
3. K. Gödel (1931).「Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I」. Monatshefte für Mathematik und Physik, 38, 173–198.（不完备性定理来源，不可判定性谱系的源头。）[②③]
4. D. Hilbert & W. Ackermann (1928).《Grundzüge der theoretischen Logik》. Springer.（判定问题（Entscheidungsproblem）在此书中首次明确提出，是图灵与丘奇工作的直接背景。）[②③]
5. E. L. Post (1944).「Recursively Enumerable Sets of Positive Integers and Their Decision Problems」. Bulletin of the American Mathematical Society, 50(5), 284–316.（递归可枚举集与不可解度理论的奠基文献。）[②③]
6. H. G. Rice (1953).「Classes of Recursively Enumerable Sets and Their Decision Problems」. Transactions of the American Mathematical Society, 74(2), 358–366.（Rice 定理来源：递归可枚举集的任何非平凡性质都不可判定。）[②]
7. Y. V. Matiyasevich (1970).「Enumerable Sets Are Diophantine」. Soviet Mathematics. Doklady, 11(2), 354–357.（俄文原载 Доклады АН СССР 191 卷，1970，第 279 至 282 页；此处引英译本。完成希尔伯特第十问题不可解的证明，即 MRDP 定理。）[②③]

### 难解（②③）

8. S. A. Cook (1971).「The Complexity of Theorem-Proving Procedures」. Proceedings of the 3rd Annual ACM Symposium on Theory of Computing (STOC), 151–158.（NP 完全性概念的开创性论文。）[②③]
9. L. A. Levin (1973).「Universal Sequential Search Problems」. Problems of Information Transmission, 9(3), 265–266.（俄文原载 Проблемы передачи информации 9(3)，第 115 至 116 页。与 Cook 独立得出 NP 完全性，即 Cook–Levin 定理。）[②③]
10. R. M. Karp (1972).「Reducibility Among Combinatorial Problems」. In R. E. Miller & J. W. Thatcher (Eds.),《Complexity of Computer Computations》(pp. 85–103). Plenum Press.（著名的「Karp 的 21 个 NP 完全问题」，确立难解性的普遍性。）[②③]
11. J. Hartmanis & R. E. Stearns (1965).「On the Computational Complexity of Algorithms」. Transactions of the American Mathematical Society, 117, 285–306.（时间复杂度类的奠基，「计算复杂度」一词由此确立。）[②]
12. M. R. Garey & D. S. Johnson (1979).《Computers and Intractability: A Guide to the Theory of NP-Completeness》. W. H. Freeman.（难解性理论的标准参考书。）[②]
13. M. Sipser (2012).《Introduction to the Theory of Computation》(3rd ed.). Cengage Learning.（初版 1997 年，PWS Publishing。可计算性与复杂度的标准教科书，以广为使用的第三版为准。）[②]
14. S. Arora & B. Barak (2009).《Computational Complexity: A Modern Approach》. Cambridge University Press.（现代计算复杂度的权威研究生教材。）[②]

### 部分可观测（②④）

15. K. J. Åström (1965).「Optimal Control of Markov Processes with Incomplete State Information」. Journal of Mathematical Analysis and Applications, 10, 174–205.（部分可观测下最优控制的奠基，信念状态思想，POMDP 理论源头之一。）[②]
16. R. D. Smallwood & E. J. Sondik (1973).「The Optimal Control of Partially Observable Markov Processes over a Finite Horizon」. Operations Research, 21(5), 1071–1088.（给出有限时域 POMDP 值函数分段线性凸的经典结果。）[②]
17. C. H. Papadimitriou & J. N. Tsitsiklis (1987).「The Complexity of Markov Decision Processes」. Mathematics of Operations Research, 12(3), 441–450.（系统刻画 MDP 与 POMDP 各变体的计算复杂度，连接「部分可观测」与「难解」两副面孔。）[②]
18. L. P. Kaelbling, M. L. Littman & A. R. Cassandra (1998).「Planning and Acting in Partially Observable Stochastic Domains」. Artificial Intelligence, 101(1), 99–134.（POMDP 框架的权威综述与算法，部分可观测处境的代表性文献。）[②④]

### 预算受限（①④，含有限理性与 anytime 算法）

19. F. H. Knight (1921).《Risk, Uncertainty and Profit》. Houghton Mifflin.（确立「风险」与不可量化的「不确定性」之分，不可验证处境的思想起点。）[①④]
20. H. A. Simon (1955).「A Behavioral Model of Rational Choice」. The Quarterly Journal of Economics, 69(1), 99–118.（有限理性（bounded rationality）的首次形式化，预算受限处境的概念源头。）[①④]
21. M. Boddy & T. Dean (1989).「Solving Time-Dependent Planning Problems」. Proceedings of the 11th International Joint Conference on Artificial Intelligence (IJCAI).（与下条同源的 anytime 算法工作；署名顺序在两篇之间不同。）[②④]
22. T. Dean & M. Boddy (1988).「An Analysis of Time-Dependent Planning」. Proceedings of the 7th National Conference on Artificial Intelligence (AAAI), 49–54.（提出 anytime 算法，预算（计算时间）受限处境的代表性形式化；AAAI-88 原刊署名为 Dean & Boddy。）[②④]
23. S. J. Russell & D. Subramanian (1995).「Provably Bounded-Optimal Agents」. Journal of Artificial Intelligence Research, 2, 575–609.（把有限理性形式化为「有界最优」，预算受限处境的理论刻画。）[②④]

### 对抗（②①④，含决策论与对抗机器学习）

24. J. von Neumann & O. Morgenstern (1944).《Theory of Games and Economic Behavior》. Princeton University Press.（博弈论奠基之作，对抗性处境的理论源头，含极小极大定理的系统化。）[②①]
25. J. F. Nash (1950).「Equilibrium Points in N-Person Games」. Proceedings of the National Academy of Sciences, 36(1), 48–49.（Nash 均衡，对抗与多方博弈的核心理论概念。）[②]
26. A. Wald (1945).「Statistical Decision Functions Which Minimize the Maximum Risk」. Annals of Mathematics, 46(2), 265–280.（统计决策理论与极小极大（最坏情形）准则的奠基，连接对抗与预算受限处境。）[②]
27. L. J. Savage (1954).《The Foundations of Statistics》. Wiley.（主观期望效用理论的系统奠基，不确定性下决策的标准框架。）[②①]
28. D. Ellsberg (1961).「Risk, Ambiguity, and the Savage Axioms」. The Quarterly Journal of Economics, 75(4), 643–669.（Ellsberg 悖论，揭示「模糊」不同于「风险」，呼应 Knight 之分。）[①④]
29. C. Szegedy, W. Zaremba, I. Sutskever, J. Bruna, D. Erhan, I. Goodfellow & R. Fergus (2014).「Intriguing Properties of Neural Networks」. International Conference on Learning Representations (ICLR). arXiv:1312.6199.（首次系统揭示神经网络对抗样本现象，对抗性处境的开端。）[②]
30. I. J. Goodfellow, J. Shlens & C. Szegedy (2015).「Explaining and Harnessing Adversarial Examples」. International Conference on Learning Representations (ICLR). arXiv:1412.6572.（提出 FGSM 与对抗训练，对抗样本研究的核心文献。）[②]
31. A. Madry, A. Makelov, L. Schmidt, D. Tsipras & A. Vladu (2018).「Towards Deep Learning Models Resistant to Adversarial Attacks」. International Conference on Learning Representations (ICLR). arXiv:1706.06083.（以鲁棒优化（极小极大）统一对抗攻防，连接对抗与最坏情形决策。）[②④]
32. B. Biggio & F. Roli (2018).「Wild Patterns: Ten Years after the Rise of Adversarial Machine Learning」. Pattern Recognition, 84, 317–331.（对抗机器学习十年综述，对抗性处境的权威总览。）[②]
