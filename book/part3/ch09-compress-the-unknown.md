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

它的跨域形态同样齐整。统计与科学里，它叫实验设计：费雪 1935 年的《实验设计》、博克斯等人的《实验者统计学》，教的是如何用最少的试验榨出最多的信息；林德利 1956 年给出「一个实验提供的信息」的度量，沙洛纳与韦尔迪内利把贝叶斯实验设计系统化；瓦尔德 1945 年的序贯检验，让你边收数据边决定要不要继续。香农 1948 年的信息论，是这一切的底层货币。机器学习里，它叫主动学习：下一个该标注哪个样本最划算（科恩等人、塞特尔斯）。软件测试里，它叫 fuzzing：该把算力砸向哪个输入去撞出崩溃（米勒等人 1990 年的开创性实验）。审计里，它叫抽样：查哪几笔交易最可能发现问题。界面里，它叫该问用户哪个问题（第 5 章）。

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
2. V. Vapnik & A. Chervonenkis (1971).「On the Uniform Convergence of Relative Frequencies of Events to Their Probabilities」. Theory of Probability & Its Applications, 16(2), 264-280. [②]
3. V. Vapnik (1995).《The Nature of Statistical Learning Theory》. Springer. [②]
4. A. Blumer, A. Ehrenfeucht, D. Haussler & M. Warmuth (1989).「Learnability and the Vapnik-Chervonenkis Dimension」. Journal of the ACM, 36(4), 929-965. [②]
5. A. Blumer, A. Ehrenfeucht, D. Haussler & M. Warmuth (1987).「Occam's Razor」. Information Processing Letters, 24(6), 377-380. [②]
6. D. McAllester (1999).「PAC-Bayesian Model Averaging」. Proceedings of the 12th Annual Conference on Computational Learning Theory (COLT), 164-170. [②]
7. B. Pierce (2002).《Types and Programming Languages》. MIT Press. [②]
8. W. Howard (1980).「The Formulae-as-Types Notion of Construction」. 收于 J. Seldin & J. Hindley 编《To H. B. Curry: Essays on Combinatory Logic, Lambda Calculus and Formalism》, 479-490. Academic Press. [②]
9. G. Necula (1997).「Proof-Carrying Code」. Conference Record of the 24th ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages (POPL), 106-119. [②④]
10. X. Leroy (2009).「Formal Verification of a Realistic Compiler」. Communications of the ACM, 52(7), 107-115. [②③]
11. L. de Moura & N. Bjørner (2008).「Z3: An Efficient SMT Solver」. Tools and Algorithms for the Construction and Analysis of Systems (TACAS), LNCS 4963, 337-340. Springer. [②④]
12. N. Higham (2002).《Accuracy and Stability of Numerical Algorithms》(2nd ed.). SIAM. [②]
13. R. Moore (1966).《Interval Analysis》. Prentice-Hall. [②]
14. C. Shannon (1948).「A Mathematical Theory of Communication」. Bell System Technical Journal, 27(3), 379-423; 27(4), 623-656. [①②]
15. J. Rissanen (1978).「Modeling by Shortest Data Description」. Automatica, 14(5), 465-471. [②]
16. M. Li & P. Vitányi (2008).《An Introduction to Kolmogorov Complexity and Its Applications》(3rd ed.). Springer. [②]
17. W. Hoeffding (1963).「Probability Inequalities for Sums of Bounded Random Variables」. Journal of the American Statistical Association, 58(301), 13-30. [②]
18. E. Candès, J. Romberg & T. Tao (2006).「Robust Uncertainty Principles: Exact Signal Reconstruction from Highly Incomplete Frequency Information」. IEEE Transactions on Information Theory, 52(2), 489-509. [②]
19. R. Fisher (1935).《The Design of Experiments》. Oliver and Boyd. [①③]
20. G. Box, W. Hunter & J. Hunter (1978).《Statistics for Experimenters: An Introduction to Design, Data Analysis, and Model Building》. John Wiley & Sons. [③④]
21. D. Lindley (1956).「On a Measure of the Information Provided by an Experiment」. The Annals of Mathematical Statistics, 27(4), 986-1005. [②]
22. K. Chaloner & I. Verdinelli (1995).「Bayesian Experimental Design: A Review」. Statistical Science, 10(3), 273-304. [②]
23. A. Wald (1945).「Sequential Tests of Statistical Hypotheses」. The Annals of Mathematical Statistics, 16(2), 117-186. [①②]
24. W. Thompson (1933).「On the Likelihood that One Unknown Probability Exceeds Another in View of the Evidence of Two Samples」. Biometrika, 25(3-4), 285-294. [①②]
25. H. Robbins (1952).「Some Aspects of the Sequential Design of Experiments」. Bulletin of the American Mathematical Society, 58(5), 527-535. [①②]
26. T. Lai & H. Robbins (1985).「Asymptotically Efficient Adaptive Allocation Rules」. Advances in Applied Mathematics, 6(1), 4-22. [②]
27. P. Auer, N. Cesa-Bianchi & P. Fischer (2002).「Finite-time Analysis of the Multiarmed Bandit Problem」. Machine Learning, 47(2-3), 235-256. [①②]
28. H. Kushner (1964).「A New Method of Locating the Maximum Point of an Arbitrary Multipeak Curve in the Presence of Noise」. Journal of Basic Engineering, 86(1), 97-106. [①②]
29. J. Mockus, V. Tiesis & A. Žilinskas (1978).「The Application of Bayesian Methods for Seeking the Extremum」. 收于 L. Dixon & G. Szegő 编《Towards Global Optimization 2》, 117-129. North-Holland. [②]
30. D. Jones, M. Schonlau & W. Welch (1998).「Efficient Global Optimization of Expensive Black-Box Functions」. Journal of Global Optimization, 13(4), 455-492. [②④]
31. C. Rasmussen & C. Williams (2006).《Gaussian Processes for Machine Learning》. MIT Press. [②④]
32. N. Srinivas, A. Krause, S. Kakade & M. Seeger (2010).「Gaussian Process Optimization in the Bandit Setting: No Regret and Experimental Design」. Proceedings of the 27th International Conference on Machine Learning (ICML), 1015-1022. [②]
33. D. Cohn, Z. Ghahramani & M. Jordan (1996).「Active Learning with Statistical Models」. Journal of Artificial Intelligence Research, 4, 129-145. [②④]
34. B. Settles (2009).《Active Learning Literature Survey》. Computer Sciences Technical Report 1648, University of Wisconsin-Madison. [②④]
35. B. Miller, L. Fredriksen & B. So (1990).「An Empirical Study of the Reliability of UNIX Utilities」. Communications of the ACM, 33(12), 32-44. [③④]
36. B. Shahriari, K. Swersky, Z. Wang, R. Adams & N. de Freitas (2016).「Taking the Human Out of the Loop: A Review of Bayesian Optimization」. Proceedings of the IEEE, 104(1), 148-175. [②④]
