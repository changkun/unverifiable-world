# 第 2 章　不可验证的五副面孔

> **论点**：「我没法检验它」掩盖了五种结构不同的处境，把它们混为一谈是这个领域的核心错误。

## 五副面孔（各给判据与典型例）

1. **不可判定**：原则上无程序。停机问题、Rice 定理。
2. **难解**：有程序但代价爆炸。RH 可验到高度 T 却不可一般化、最坏情形的 SAT。
3. **部分可观测**：相关状态对主体隐藏。用户的真实偏好、病人的内部状态。
4. **预算受限**：原则上可验可解，但这个主体没有时间、算力或样本。只有二十分钟的评审。
5. **对抗**：系统主动挫败验证。会欺骗的对手、恶意代码。

## 关键

它们「可得的补救」完全不同：不可判定永无完整解，预算受限随资源消失，对抗是博弈而非计算。

## 接口

把五种掐清楚，正是为了让后面的惊讶站得住：尽管来源不同，应对却押韵。

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
