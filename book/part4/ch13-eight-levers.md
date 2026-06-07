# 第 13 章　八根杠杆

> **论点**：八招不是随意的清单；每一招拉动风险与信息分解里一根不同的杠杆，这正是它们让人觉得「齐了」的原因。

第三部交出了那张对照表：八招，四对，在四个现场加科学里反复以不同行话出现。但一张清单再齐整，也只是清单。这一章要追问的是：为什么偏偏是这八招？是我凑出来的，还是它们各自卡在某个躲不开的位置上？如果是后者，收敛才算被解释，否则本书顶多是本好用的归类手册。

我要提出一个候选的解释。先把丑话说在前头：它是一个组织结构，不是一个证明。读完整章，请带着第 14 章那把怀疑的刀。

## 一个粗糙的分解

把「在不可验证下行动」剥到最简，你真正在管理的，是风险。借决策论的老话（瓦尔德、萨维奇、冯·诺依曼与摩根斯特恩），风险可以粗略地写成

$$\text{Risk}\ \approx\ \Pr(\text{fail})\ \times\ \text{Cost}(\text{fail}),$$

而这一切，是在一个信息预算 $B$ 之下进行的，你能用来削减不确定的查验、样本、算力、时间，都是有限的。

这个式子看着简单，关键在于：它右边能被你下手的地方，是可数的几处。你要么动「失败」的定义本身，要么动失败的概率，要么动你对那个概率的认知，要么动失败的代价，要么动这笔信息预算怎么花，要么动检查发生的时间。我的命题是：八招，恰好一招一个位置，再没有第九个空位可填。

## 八招，八个位置

把每一招对到它所拉动的那根杠杆：

| 招 | 它拉动的杠杆 | 在风险分解中的位置 |
| --- | --- | --- |
| 代理替换 | 改变你度量、优化的目标 | 改写「失败」的定义本身 |
| 证书与界 | 在一个切片上把不确定压到有保证的界内 | 在局部将 $\Pr(\text{fail})$ 压近零 |
| 神谕入回路 | 引进你单独不具备的验证能力 | 借外力降 $\Pr(\text{fail})$ |
| 冗余共识 | 让多个判断的失败去相关 | 降联合失败概率 $\Pr(\text{all\ fail})$ |
| 最优筛查 | 把信息预算花在边际收益最高处 | 分配 $B$，最大化对不确定的削减 |
| 标定 | 给残余风险定一个诚实的价 | 让 $\Pr(\text{fail})$ 变成已知、可据以下注 |
| 衰减围栏 | 缩小爆炸半径 | 降 $\text{Cost}(\text{fail})$ |
| 留痕审计 | 把检查从事前挪到事后 | 改检查的时间位置，把不可恢复的失败变可恢复 |

读这张表，那个「凑出来的清单」的感觉应当松动一些。八招不是八件随手收集的工具，它们分占了「$\Pr$、对 $\Pr$ 的认知、代价、预算分配、检查时点、目标定义」这几处，几乎是把那个分解式能下手的地方一一占满。命题于是可以这样下：若这些确实就是全部的杠杆，那这套招就是完整的，而收敛也就被解释了，任何有能力的主体，迟早都会重新发现它们，因为除此之外没有别的可拉。

## 为什么这能跨越基质

如果上面成立，它顺带解释了本书最初那个谜：为什么数学家、工程师、组织会不约而同。

马尔在研究视觉时区分过三个层次：计算层（要解决什么问题、受什么约束）、算法层（用什么表示和过程）、实现层（落在什么硬件上）。八招活在计算层。它们是「给定不可验证这个约束，逻辑上还能动哪几处」的答案，而这个答案不依赖你是碳基的数学家、硅基的程序，还是由人组成的官僚机构。基质千差万别，计算层的约束却是同一个，于是应对收敛。西蒙的有限理性、他的「人工科学」，讲的正是这种由环境约束、而非由主体内部塑造的行为。

这里还得请出无免费午餐定理（沃尔珀特与麦克里迪）。它说：在所有可能问题上平均，没有哪个方法优于另一个。这把刀两面都割。一面，它支持本书的克制，没有万能解，你必须借问题的具体结构来选杠杆，这正是为什么五副面孔要分开对待。另一面，它也警告：任何宣称「找到了统一钥匙」的人，包括我，都该收敛一点傲气。当你连失败概率都钉不住时，杠杆还会长出稳健版本，吉尔博亚与施迈德勒的极大极小期望效用、汉森与萨金特的稳健控制、奈特式不确定性下的决策，都是在 $\Pr$ 本身都模糊时，仍要按最坏情形布防的招法。

## 一句必须放大的强声明

现在把丑话放大。

上面这套，是一个候选的组织结构，不是一个定理。那个风险分解是非形式的，我没有给出一个严格的主体与环境模型，再证明最优策略恰好是这八根杠杆。「这些就是全部的杠杆」是一句断言，不是一个已确立的结果。我没有证据说这张表是穷尽的，也无法排除它只是一个事后框架，一个足够灵活、能把许多套招都塞进去的叙事。表里某些归位（比如冗余既降联合失败、又像是一种特殊的筛查）甚至有重叠，这本身就说明这个分解还不够干净。

我把它放在这里，是因为它有组织力、有解释上的吸引力，而不是因为它被证明了。它够得上一个好猜想的标准：清晰、可反驳、能统起大量现象。但它还没够上定理。

那么，最后那个问题就躲不掉了：这种跨领域的收敛，到底是某种东西逼出来的一条定律，还是仅仅一个很强、却终究是经验的模式？下一章，正面、诚实地清算它。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实；个别未能确证者标「（细节待核）」。

1. A. Wald (1950).《Statistical Decision Functions》. John Wiley & Sons. [②④]
2. A. Wald (1939). 「Contributions to the Theory of Statistical Estimation and Testing Hypotheses」.《The Annals of Mathematical Statistics》, 10(4), 299-326. [②]
3. J. von Neumann & O. Morgenstern (1944).《Theory of Games and Economic Behavior》. Princeton University Press. [②]
4. L. J. Savage (1954).《The Foundations of Statistics》. John Wiley & Sons. [②④]
5. F. H. Knight (1921).《Risk, Uncertainty and Profit》. Houghton Mifflin. [②]
6. J. M. Keynes (1921).《A Treatise on Probability》. Macmillan. [②]
7. F. P. Ramsey (1931). 「Truth and Probability」.《The Foundations of Mathematics and other Logical Essays》(R. B. Braithwaite 编). Kegan Paul, Trench, Trubner & Co., 156-198. [②]
8. B. de Finetti (1937). 「La prévision: ses lois logiques, ses sources subjectives」.《Annales de l'Institut Henri Poincaré》, 7(1), 1-68. [②]
9. F. J. Anscombe & R. J. Aumann (1963). 「A Definition of Subjective Probability」.《The Annals of Mathematical Statistics》, 34(1), 199-205. [②]
10. D. Ellsberg (1961). 「Risk, Ambiguity, and the Savage Axioms」.《The Quarterly Journal of Economics》, 75(4), 643-669. [②]
11. R. D. Luce & H. Raiffa (1957).《Games and Decisions: Introduction and Critical Survey》. John Wiley & Sons. [②④]
12. H. A. Simon (1955). 「A Behavioral Model of Rational Choice」.《The Quarterly Journal of Economics》, 69(1), 99-118. [②]
13. H. A. Simon (1969).《The Sciences of the Artificial》. MIT Press. [②③]
14. K. R. Popper (1959).《The Logic of Scientific Discovery》. Hutchinson. [②③]
15. A. Tversky & D. Kahneman (1974). 「Judgment under Uncertainty: Heuristics and Biases」.《Science》, 185(4157), 1124-1131. [②]
16. D. Kahneman & A. Tversky (1979). 「Prospect Theory: An Analysis of Decision under Risk」.《Econometrica》, 47(2), 263-291. [②]
17. D. Marr (1982).《Vision: A Computational Investigation into the Human Representation and Processing of Visual Information》. W. H. Freeman. [②③]
18. J. O. Berger (1985).《Statistical Decision Theory and Bayesian Analysis》. Springer-Verlag. [②④]
19. D. E. Bell, H. Raiffa & A. Tversky (编) (1988).《Decision Making: Descriptive, Normative, and Prescriptive Interactions》. Cambridge University Press. [②④]
20. I. Gilboa & D. Schmeidler (1989). 「Maxmin Expected Utility with Non-Unique Prior」.《Journal of Mathematical Economics》, 18(2), 141-153. [②④]
21. D. Schmeidler (1989). 「Subjective Probability and Expected Utility without Additivity」.《Econometrica》, 57(3), 571-587. [②]
22. P. Walley (1991).《Statistical Reasoning with Imprecise Probabilities》. Chapman and Hall. [②④]
23. G. Gigerenzer & D. G. Goldstein (1996). 「Reasoning the Fast and Frugal Way: Models of Bounded Rationality」.《Psychological Review》, 103(4), 650-669. [②]
24. D. H. Wolpert (1996). 「The Lack of A Priori Distinctions between Learning Algorithms」.《Neural Computation》, 8(7), 1341-1390. [②]
25. D. H. Wolpert & W. G. Macready (1997). 「No Free Lunch Theorems for Optimization」.《IEEE Transactions on Evolutionary Computation》, 1(1), 67-82. [②]
26. I. Gilboa & D. Schmeidler (2001).《A Theory of Case-Based Decisions》. Cambridge University Press. [②④]
27. T. F. Bewley (2002). 「Knightian Decision Theory. Part I」.《Decisions in Economics and Finance》, 25(2), 79-110. [②④]
28. P. Klibanoff, M. Marinacci & S. Mukerji (2005). 「A Smooth Model of Decision Making under Ambiguity」.《Econometrica》, 73(6), 1849-1892. [②]
29. F. Maccheroni, M. Marinacci & A. Rustichini (2006). 「Ambiguity Aversion, Robustness, and the Variational Representation of Preferences」.《Econometrica》, 74(6), 1447-1498. [②④]
30. L. P. Hansen & T. J. Sargent (2008).《Robustness》. Princeton University Press. [②④]
31. P. P. Wakker (2010).《Prospect Theory: For Risk and Ambiguity》. Cambridge University Press. [②]
32. I. Gilboa & M. Marinacci (2013). 「Ambiguity and the Bayesian Paradigm」.《Advances in Economics and Econometrics: Theory and Applications, Tenth World Congress》(D. Acemoglu, M. Arellano & E. Dekel 编). Cambridge University Press. [②④]
33. P. Bossaerts & C. Murawski (2017). 「Computational Complexity and Human Decision-Making」.《Trends in Cognitive Sciences》, 21(12), 917-929. [②]
