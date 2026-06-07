# 第 9 章　压缩未知

> **论点**：两招直接攻击不确定性。在你能查的切片上给出有保证的界（证书），把有限的查验花在最能消解不确定的地方（最优筛查）。

第二部把招数嵌在四个现场里、彼此缠绕地演了一遍。从这一部起，换一种看法：把每一招单独拎出来，洗去领域的行话，以纯形式呈现，再一次性铺满所有现场。这才是本书真正的载荷，那张「同一招在多种行话下的对照表」。

八招两两并成四章。配对不是图省事，配对本身是个论点：每一对拉动的是同一根更基本的杠杆，这一点会在第 13 章兑现。本章这一对，证书与最优筛查，共同攻击的是同一样东西，不确定性。它们从相反的两端去压缩未知：一端是在你查得动的切片上，证出一个有保证的界；另一端是把有限的查验，花在最能消解不确定的地方。

并且，按第 4 章立下的铁律，每抽一招、每做一次跨域并置，都要逼问一遍：这个迁移是实质的（同机制、同败法、同权衡），还是只是个漂亮比方？

## 证书：在切片上证一个界

第一招的纯形式：不去验证整体，而是产出一个有界的、可独立复核的局部保证。你交付的不是「它全对」，而是「在这个范围内，它至多错这么多」，外加一张任何人都能快速验真的凭证。

它的跨域形态惊人地一致。

机器学习里，它叫泛化界。瓦利安特 1984 年的 PAC 框架、瓦普尼克与切尔沃年基斯的 VC 维（布卢默等人 1989 年接上），给出形如「以至少 $1-\delta$ 的概率，真实误差不超过经验误差加一个复杂度惩罚」的保证：

$$R(h)\ \le\ \hat R(h)+\sqrt{\frac{d\big(\ln(2n/d)+1\big)+\ln(4/\delta)}{n}}.$$

你验不了模型在未来所有数据上的表现（那是开放世界），但你能在「已见样本」这个切片上，证出一个对未见数据成立的、带置信度的界。霍夫丁不等式是它的概率引擎，PAC-Bayes（麦卡莱斯特）是它的精化。

软件里，它叫类型与证明。类型系统不证明程序「全对」，它只证明某一条性质（比如不会把整数当指针），换来的是可判定、可机械复核的检查（皮尔斯）。柯里-霍华德对应（霍华德 1980）把「证明」与「程序」划上等号，内库拉 1997 年的「携带证明的代码」更是把这一招用到极致：不受信的代码自带一张安全性证明，宿主只需快速核对证书，而无需自己重新推导。勒罗伊 2009 年经形式验证的 CompCert 编译器、de Moura 与比约纳 2008 年的 Z3 求解器，都是同一思路的工业化。

数值计算里，它叫误差界。希格姆 2002 年的后向误差分析、摩尔 1966 年的区间算术，让你带着「保证包含真值的区间」去计算，最终交付的不是一个可能骗你的浮点数，而是一个有保证的范围。数学里，它就是第 7 章那个验到高度 $T$ 的零点：一个界，不是定理。

统一的观念是：证书是一个局部的、有界的、可独立复核的保证。它最妙的地方在于利用了第 2 章那道验证不对称，找到证书可能极贵，核对证书却极廉。携带证明的代码、NP 问题的解、数学证明，吃的都是这口红利。

它的标准败法只有一种，却很常见：空洞的界。一个为真却无用的保证，「误差不超过百分之百」「该模型的泛化误差有限」，逻辑上无懈可击，操作上一文不值。界的价值不在成立，而在够紧到能据以行动。

## 最优筛查：把查验花在刀刃上

第二招的纯形式：信息有代价，所以把有限的查验，分配到边际上最能压缩不确定性的地方。

它的跨域形态同样齐整。统计与科学里，它叫实验设计：费雪 1935 年的《实验设计》、博克斯等人的《实验者统计学》，教的是如何用最少的试验榨出最多的信息；林德利 1956 年给出「一个实验提供的信息」的度量，沙洛纳与韦尔迪内利把贝叶斯实验设计系统化；瓦尔德 1945 年的序贯检验，让你边收数据边决定要不要继续。香农 1948 年的信息论，是这一切的底层货币。机器学习里，它叫主动学习：下一个该标注哪个样本最划算（科恩等人、塞特尔斯）。软件测试里，它叫 fuzzing：该把算力砸向哪个输入去撞出崩溃（米勒等人 1990 年的开创性实验）。这一招的现代规模令人侧目，谷歌的 OSS-Fuzz 自 2016 年起持续地向上千个开源项目自动喂入海量畸形输入，至今已查出数以万计的缺陷与漏洞，没有哪支人力测试团队能穷举到这个量级，它靠的正是把算力源源不断地投向最可能崩的地方。审计里，它叫抽样：查哪几笔交易最可能发现问题。界面里，它叫该问用户哪个问题（第 5 章）。

这些背后是同一个最优化：让回答与未知之间的期望信息增益最大，

$$q^\star=\arg\max_q\ I(\theta;y_q).$$

而当查验本身要反复进行、还要边查边用时，它就长成了探索与利用的张力，多臂老虎机问题。汤普森 1933 年的采样、罗宾斯 1952 年、赖与罗宾斯 1985 年的最优分配、奥尔等人 2002 年的有限时间分析，给出的是「花多少次试验去减少对哪个选项的不确定」的最优解；它的遗憾随时间只以对数增长，

$$\mathrm{Regret}(T)=O(\ln T).$$

这里要防一个叙述上的路径依赖。最优筛查是一个方法族，实验设计、主动学习、审计抽样、fuzzing、老虎机，都是它。库什纳、莫库斯到琼斯 1998 年的高效全局优化、斯里尼瓦斯等人 2010 年的 GP-UCB，乃至沙赫里亚里 2016 年那篇综述里基于高斯过程的贝叶斯优化，都极其有用，但它们只是这个族里的一支实现，不是「筛查」的全部。把这一招等同于高斯过程，就把一个普遍的姿势缩成了一件工具。

它的标准败法也只有一种：优化了一个被误设的信息度量。你极其高效地收集了信息，却是关于错误问题的信息，或者那个被你最大化的「信息量」，根本不追踪你真正在意的东西。筛查越聪明，错设的度量就把你越快地领向歧途。

## 两招为何成对，以及通向哪里

把这两招并排看：证书在一个切片上把不确定性压到一个有保证的界内；筛查则花掉信息预算，去观测那个最能压缩不确定性的切片。一个是「在能查的地方证紧」，一个是「把查验花在最该查的地方」。它们从两端夹击同一个敌人，未知。这也是它们共用的那根杠杆：在一个信息预算之下，管理你在哪里、以多大力度去削减不确定。第 13 章会正式给这根杠杆命名。

但有时候，无论你怎么压、怎么筛，都不够，因为你压根缺乏做出判断的能力本身。这时就不能再靠自己缩小未知了，得去别处把判断借来。下一对招，正是关于此。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实；个别未能确证者标「（细节待核）」。

1. L. Valiant (1984).「A Theory of the Learnable」. Communications of the ACM, 27(11), 1134-1142. [②]
   瓦利安特在此提出「概率近似正确」（PAC）的学习框架，把「学会一个概念」严格定义为：以高概率、在多项式时间与样本内，得到一个误差足够小的假设。这篇论文为「能不能学、要多少样本才学得动」给出了第一套可证明的语言，是本章「泛化界」一招的源头。
2. V. Vapnik & A. Chervonenkis (1971).「On the Uniform Convergence of Relative Frequencies of Events to Their Probabilities」. Theory of Probability & Its Applications, 16(2), 264-280. [②]
   这篇奠基之作证明了经验频率向真实概率一致收敛的条件，并由此引出后来以两位作者命名的 VC 维，用以刻画一个函数族的「容量」。它解释了为何在有限样本上证出的误差界能对未见数据成立，是泛化界背后的概率与组合根基。
3. V. Vapnik (1995).《The Nature of Statistical Learning Theory》. Springer. [②]
   瓦普尼克在这本书里把统计学习理论整理成一个完整体系：以结构风险最小化为核心，权衡经验误差与模型复杂度，并由此导向支持向量机。它是理解「复杂度惩罚」为何出现在泛化界里的标准读物，把第一招的直觉讲得清楚而连贯。
4. A. Blumer, A. Ehrenfeucht, D. Haussler & M. Warmuth (1989).「Learnability and the Vapnik-Chervonenkis Dimension」. Journal of the ACM, 36(4), 929-965. [②]
   这篇论文把 VC 维正式接入 PAC 框架，证明一个概念类可被 PAC 学习当且仅当其 VC 维有限，并给出依赖 VC 维的样本复杂度界。它是正文那条泛化界公式的直接来源，把「容量有限便可学」这一判据钉死。
5. A. Blumer, A. Ehrenfeucht, D. Haussler & M. Warmuth (1987).「Occam's Razor」. Information Processing Letters, 24(6), 377-380. [②]
   这篇短文给出「奥卡姆剃刀」的学习理论版本：一个能把训练数据压缩得足够短的假设，便能以高概率泛化。它把「简洁即可学」从哲学格言变成可证的命题，为本章「压缩未知」的母题提供了一个干净的注脚。
6. D. McAllester (1999).「PAC-Bayesian Model Averaging」. Proceedings of the 12th Annual Conference on Computational Learning Theory (COLT), 164-170. [②]
   麦卡莱斯特在此提出 PAC-Bayes 界：对一族假设上的后验分布给出泛化保证，惩罚项由后验与先验之间的 KL 散度衡量。它是 PAC 界的一次精化，正文称其为第一招的「精化」即指此，常给出比经典 VC 界更紧的结果。
7. B. Pierce (2002).《Types and Programming Languages》. MIT Press. [②]
   皮尔斯这本教材系统讲解类型系统的理论与构造，核心是类型安全的「进展」与「保型」两条性质，以及它们如何被机械地检查。它正是正文那句「类型系统不证明程序全对，只证某一条性质、换来可判定可复核」的标准依据，是理解证书一招在软件中形态的入门书。
8. W. Howard (1980).「The Formulae-as-Types Notion of Construction」. 收于 J. Seldin & J. Hindley 编《To H. B. Curry: Essays on Combinatory Logic, Lambda Calculus and Formalism》, 479-490. Academic Press. [②]
   霍华德这篇广为流传的文稿（写于 1969 年，1980 年正式发表）确立了「公式即类型、证明即程序」的对应：直觉主义逻辑的命题与类型一一对应，证明与项一一对应。它是柯里-霍华德对应的经典文本，把「检查一段程序的类型」与「检验一个证明」划上等号，正是证书一招的逻辑核心。
9. G. Necula (1997).「Proof-Carrying Code」. Conference Record of the 24th ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages (POPL), 106-119. [②④]
   内库拉提出「携带证明的代码」：不受信的程序自带一张关于自身安全性的形式证明，宿主只需快速核验这张证书，而不必信任代码来源或重新推导。它把第 2 章那道验证不对称用到极致，是本章证书概念最纯粹的工程化身。
10. X. Leroy (2009).「Formal Verification of a Realistic Compiler」. Communications of the ACM, 52(7), 107-115. [②③]
   勒罗伊报告了 CompCert 的成果：一个用 Coq 形式验证过的 C 编译器，其生成代码在语义上与源程序一致这件事，是被机器证明出来的。它表明「带可复核保证的真实软件」并非空想，是证书一招工业化的标志性案例。
11. L. de Moura & N. Bjørner (2008).「Z3: An Efficient SMT Solver」. Tools and Algorithms for the Construction and Analysis of Systems (TACAS), LNCS 4963, 337-340. Springer. [②④]
   这篇论文介绍了 Z3 这一高效的 SMT 求解器，它能判定带有算术、数组等理论的逻辑公式的可满足性，并广泛用于程序验证与符号执行。它把「自动产出可复核证书」做成了一件随手可用的工业工具，是证书一招在实践中得以铺开的引擎之一。
12. N. Higham (2002).《Accuracy and Stability of Numerical Algorithms》(2nd ed.). SIAM. [②]
   希格姆这部权威著作系统讲述数值算法的误差分析，尤其是后向误差分析：与其问「答案偏离真值多少」，不如问「这个答案恰好是哪个被微扰问题的精确解」。它是正文「误差界」一招的标准参考，教人如何为浮点计算配上可信赖的保证。
13. R. Moore (1966).《Interval Analysis》. Prentice-Hall. [②]
   摩尔这本开创性著作确立了区间算术：让每个量带着一个保证包含真值的区间一起参与运算，输出的便不是一个可能骗人的数，而是一个有保证的范围。它把「交付一个界而非一个点」的思路给了数值计算，正是证书一招在该领域的化身。
14. C. Shannon (1948).「A Mathematical Theory of Communication」. Bell System Technical Journal, 27(3), 379-423; 27(4), 623-656. [①②]
   香农这篇创立信息论的论文，用熵度量不确定性，并给出信源编码与信道容量的根本极限。它是「信息有代价、可被度量」这一观念的总源头，正文称之为最优筛查的「底层货币」，本章对信息增益、压缩的全部讨论都以它为单位。
15. J. Rissanen (1978).「Modeling by Shortest Data Description」. Automatica, 14(5), 465-471. [②]
   里萨宁提出最小描述长度（MDL）原则：最好的模型，是能把数据连同模型自身一起编码得最短的那个。它把「压缩即理解」做成可操作的模型选择准则，与本章「压缩未知」的母题正相呼应，也是奥卡姆剃刀的一个信息论实现。
16. M. Li & P. Vitányi (2008).《An Introduction to Kolmogorov Complexity and Its Applications》(3rd ed.). Springer. [②]
   这部标准教材系统讲述柯尔莫哥洛夫复杂度：一个对象的复杂度，等于能生成它的最短程序的长度。这是「压缩」的不可计算理想，与 MDL 那种可操作的近似相对照；它为本章压缩母题提供了理论上的天花板，说明最优压缩本身正是一种无法验证的极限。
17. W. Hoeffding (1963).「Probability Inequalities for Sums of Bounded Random Variables」. Journal of the American Statistical Association, 58(301), 13-30. [②]
   霍夫丁在此给出有界随机变量之和偏离其均值的指数型概率上界。这个不等式是把「经验平均」与「真实期望」之间的差距压进一个置信界的基本工具，正文称其为泛化界的「概率引擎」，证书一招的多数集中度论证都从它起步。
18. E. Candès, J. Romberg & T. Tao (2006).「Robust Uncertainty Principles: Exact Signal Reconstruction from Highly Incomplete Frequency Information」. IEEE Transactions on Information Theory, 52(2), 489-509. [②]
   这篇压缩感知的奠基论文证明：只要信号足够稀疏，便能用远少于传统采样定理所要求的测量数，通过凸优化把它精确重建出来。它是「把查验花在刀刃上、用极少观测榨出全部信息」的一个数学典范，呼应本章压缩与最优筛查两条线索。
19. R. Fisher (1935).《The Design of Experiments》. Oliver and Boyd. [①③]
   费雪这本经典确立了现代实验设计的基本原则：随机化、重复、区组化，以及著名的「女士品茶」思想实验。它教人如何用最少的试验榨出最多可信的信息，是最优筛查一招在统计与科学中的源头读物。
20. G. Box, W. Hunter & J. Hunter (1978).《Statistics for Experimenters: An Introduction to Design, Data Analysis, and Model Building》. John Wiley & Sons. [③④]
   博克斯等人这本广受欢迎的实务著作，把实验设计、数据分析与模型构建讲给真正动手做实验的人，强调析因设计与序贯学习的迭代节奏。它把费雪的原则落到工程现场，是理解「如何把查验安排得最划算」的实践指南。
21. D. Lindley (1956).「On a Measure of the Information Provided by an Experiment」. The Annals of Mathematical Statistics, 27(4), 986-1005. [②]
   林德利用信息论给出「一个实验提供多少信息」的度量，即先验与后验之间的期望信息增益。这正是正文那个最优筛查目标 $\arg\max_q I(\theta;y_q)$ 的理论原型，把「该做哪个实验」变成一个可最大化的量。
22. K. Chaloner & I. Verdinelli (1995).「Bayesian Experimental Design: A Review」. Statistical Science, 10(3), 273-304. [②]
   这篇综述系统梳理了贝叶斯实验设计：以效用函数（常取期望信息增益）为目标，统一地导出各种最优设计准则。它把林德利的度量整合进一个完整框架，是读者快速掌握「期望信息增益最大化」这一筛查内核的入口。
23. A. Wald (1945).「Sequential Tests of Statistical Hypotheses」. The Annals of Mathematical Statistics, 16(2), 117-186. [①②]
   瓦尔德提出序贯概率比检验：边收数据边判断，一旦证据足够强就停下来下结论，从而平均上比固定样本量的检验省得多。它把「要不要继续查」本身变成最优决策，是最优筛查里「边查边用」这一支的先声。
24. W. Thompson (1933).「On the Likelihood that One Unknown Probability Exceeds Another in View of the Evidence of Two Samples」. Biometrika, 25(3-4), 285-294. [①②]
   汤普森在此提出后来以他命名的采样法：按「某个选项确实最优」的后验概率去随机选取它，自然地在探索与利用之间取得平衡。这是多臂老虎机问题最早的解法之一，至今仍是该问题里既简洁又强劲的策略。
25. H. Robbins (1952).「Some Aspects of the Sequential Design of Experiments」. Bulletin of the American Mathematical Society, 58(5), 527-535. [①②]
   罗宾斯这篇论文把多臂老虎机问题正式确立为一个数学对象，并提出最早的序贯分配策略，奠定了「探索与利用如何权衡」这一研究方向。它是后来一整条老虎机文献的起点，本章关于「花多少次去减少哪个不确定」的讨论由此开端。
26. T. Lai & H. Robbins (1985).「Asymptotically Efficient Adaptive Allocation Rules」. Advances in Applied Mathematics, 6(1), 4-22. [②]
   赖与罗宾斯证明了多臂老虎机的遗憾下界：任何合理策略的累积遗憾都至少随时间对数增长，并构造出达到这一下界的渐近最优分配规则。它确立了正文那个 $O(\ln T)$ 是无法逾越的极限，给整类问题划定了天花板。
27. P. Auer, N. Cesa-Bianchi & P. Fischer (2002).「Finite-time Analysis of the Multiarmed Bandit Problem」. Machine Learning, 47(2-3), 235-256. [①②]
   这篇论文给出 UCB1 等基于「乐观面对不确定」的简单算法，并证明其在有限时间内（而非仅渐近）就有对数级的遗憾界。它把赖与罗宾斯的渐近结果落实为可直接使用、可分析的具体策略，是「置信上界」一类方法的标准引用。
28. H. Kushner (1964).「A New Method of Locating the Maximum Point of an Arbitrary Multipeak Curve in the Presence of Noise」. Journal of Basic Engineering, 86(1), 97-106. [①②]
   库什纳这篇早期论文用概率模型刻画一条未知的带噪曲线，并据此选取下一个采样点去寻找极大值，是贝叶斯优化思想的雏形。它说明「该往哪里再测一次」可以被当作一个最优决策来处理，是最优筛查在全局优化里的先驱之作。
29. J. Mockus, V. Tiesis & A. Žilinskas (1978).「The Application of Bayesian Methods for Seeking the Extremum」. 收于 L. Dixon & G. Szegő 编《Towards Global Optimization 2》, 117-129. North-Holland. [②]
   莫库斯等人系统发展了贝叶斯全局优化，并提出「期望改进」这一采集函数：在概率模型下选取最可能带来改进的点去评估。它把库什纳的直觉做成了一套通用方法，是今天贝叶斯优化的直接前身。
30. D. Jones, M. Schonlau & W. Welch (1998).「Efficient Global Optimization of Expensive Black-Box Functions」. Journal of Global Optimization, 13(4), 455-492. [②④]
   这篇论文提出 EGO 算法，用高斯过程为昂贵的黑箱函数建代理模型，再以期望改进准则挑选下一个评估点，使评估次数大幅减少。它是把贝叶斯优化推广开来的标志性工作，但正文也提醒：它只是最优筛查这个方法族里的一支实现，而非全部。
31. C. Rasmussen & C. Williams (2006).《Gaussian Processes for Machine Learning》. MIT Press. [②④]
   这本标准教材系统讲述高斯过程：一种对函数本身赋予先验、并能给出预测不确定性的非参数贝叶斯方法。它是贝叶斯优化所依赖的代理模型的理论底座，读者要理解「不确定性如何被建模并用于决定下一步查哪里」，此书是核心参考。
32. N. Srinivas, A. Krause, S. Kakade & M. Seeger (2010).「Gaussian Process Optimization in the Bandit Setting: No Regret and Experimental Design」. Proceedings of the 27th International Conference on Machine Learning (ICML), 1015-1022. [②]
   斯里尼瓦斯等人提出 GP-UCB 算法，把老虎机里的「置信上界」思路搬到高斯过程优化上，并为其遗憾给出可证的界。它把贝叶斯优化与老虎机理论缝在一起，正好示范了本章两端，证一个界与花掉查验，原本就是一根杠杆。
33. D. Cohn, Z. Ghahramani & M. Jordan (1996).「Active Learning with Statistical Models」. Journal of Artificial Intelligence Research, 4, 129-145. [②④]
   科恩等人给出主动学习的统计框架：在统计模型下，挑选那个能最大程度降低模型方差（或预测不确定性）的样本去标注。它把「下一个该标注哪个最划算」变成可计算的准则，是主动学习作为最优筛查一支的代表性工作。
34. B. Settles (2009).《Active Learning Literature Survey》. Computer Sciences Technical Report 1648, University of Wisconsin-Madison. [②④]
   塞特尔斯这份广为引用的综述系统整理了主动学习的各种查询策略，如不确定性采样、委员会查询、期望误差缩减等，并比较其适用场景。它是快速纵览「标注预算该怎么花」全貌的标准入口，把这一招的各种实现摆在一起对照。
35. B. Miller, L. Fredriksen & B. So (1990).「An Empirical Study of the Reliability of UNIX Utilities」. Communications of the ACM, 33(12), 32-44. [③④]
   米勒等人用随机生成的输入去喂各种 UNIX 工具，结果让相当一部分程序崩溃或挂死，这就是 fuzzing 的开创性实验。它说明「把算力砸向随机或可疑的输入去撞出故障」是一种廉价而有效的查验方式，是最优筛查在软件测试里的起点。
36. B. Shahriari, K. Swersky, Z. Wang, R. Adams & N. de Freitas (2016).「Taking the Human Out of the Loop: A Review of Bayesian Optimization」. Proceedings of the IEEE, 104(1), 148-175. [②④]
   这篇综述全面梳理了基于高斯过程的贝叶斯优化：代理模型、采集函数及其在超参数调优等场景的应用。它是了解该方向现状的标准读物，但正文借它提醒读者，不要把「最优筛查」这一普遍姿势缩成「高斯过程」这一件工具。
