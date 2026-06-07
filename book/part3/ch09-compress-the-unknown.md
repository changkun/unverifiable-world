# 第 9 章　压缩未知

> **论点**：两招直接攻击不确定性。在你能查的切片上给出有保证的界（证书），把有限的查验花在最能消解不确定的地方（最优筛查）。

## 两招的纯形式

**证书／界** 的跨域形态：学习里的 PAC 界、数值误差界、数学里验到高度 T、软件里「类型即性质之证」。

**最优筛查** 的跨域形态：选哪个实验、fuzz 哪个输入、审计哪笔交易、问用户哪个问题。

统一观念：信息有代价，把它分配到最大化「不确定性下降」处。

## 写法提醒（防路径依赖）

把筛查写成一个方法族（实验设计、主动学习、审计抽样、fuzzing）；基于 GP 的方法只是其中一种实现，别让它独占叙述。

## 败法

一个空洞的界（为真却无用），或优化了一个被误设的信息度量的筛查。

## 接口

这一对缩小未知；下一对转而去借你没有的判断。

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
