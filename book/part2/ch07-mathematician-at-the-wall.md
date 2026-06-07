# 第 7 章　撞墙的数学家

> **论点**：数学里你遇到最纯的不可验证（难解，有时不可判定），而有能力的应对是：验证有限切片并证明界（证书）、把目标换成等价但但愿更可解的陈述（代理替换）、用接受 ε 误差的概率方法。

## 关键节拍

证明搜索里的验证缺口：找到证明后能核对，但找到、或知道自己接近，才是难的。

证书：ζ 的零点被验证到极高的高度（一个界，不是定理）。

类型系统与形式验证作为「证某条性质、而非全对」（与软件交叉）。

代理替换：把一个难题换成等价改写。

概率素性：Miller-Rabin，「以 1 减 ε 概率为素数」。

## 第一人称

写你自己在 RH 上的工作。你探过的那些等价改写（Li 判据、Nyman-Beurling-Báez-Duarte、Brownian／Koszul 等重构），正是「代理替换」的现身：你把「证 RH」换成「证这个等价陈述」。而你每次诚实的结论，它们是已知改写、与 RH 等价却不更可解，恰是这一招的标准败法：一个忠实（真等价）却并不更容易的代理。这一节让全章有了第一人称的重量，也示范了全书的诚实。

## 伏笔

代理替换在数学里的败法是「忠实但不更易」；它将与组织那章里 Goodhart 的败法「更易但不忠实」两两相对，第 11 章兑现。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实；个别未能确证者标「（细节待核）」。

1. G. Polya (1945).《How to Solve It: A New Aspect of Mathematical Method》. Princeton University Press. [①]
2. G. Polya (1954).《Mathematics and Plausible Reasoning》（2 卷）. Princeton University Press. [①④]
3. J. Hadamard (1945).《An Essay on the Psychology of Invention in the Mathematical Field》. Princeton University Press. [①]
4. H. Poincaré (1902).《La Science et l'Hypothèse》. Flammarion. [①]
5. H. Poincaré (1908).《Science et Méthode》. Flammarion. [①]
6. G. H. Hardy (1940).《A Mathematician's Apology》. Cambridge University Press. [①]
7. E. P. Wigner (1960).「The Unreasonable Effectiveness of Mathematics in the Natural Sciences」. Communications on Pure and Applied Mathematics, 13(1). [②③]
8. I. Lakatos (1976).《Proofs and Refutations: The Logic of Mathematical Discovery》. Cambridge University Press. [①③]
9. B. Riemann (1859).「Über die Anzahl der Primzahlen unter einer gegebenen Größe」. Monatsberichte der Berliner Akademie. [②③]
10. H. M. Edwards (1974).《Riemann's Zeta Function》. Academic Press. [②]
11. E. C. Titchmarsh, rev. D. R. Heath-Brown (1986).《The Theory of the Riemann Zeta-function》（第 2 版）. Oxford University Press. [②]
12. E. Bombieri (2000).「Problems of the Millennium: The Riemann Hypothesis」. Clay Mathematics Institute. [②④]
13. J. B. Conrey (2003).「The Riemann Hypothesis」. Notices of the American Mathematical Society, 50(3). [②③]
14. X.-J. Li (1997).「The Positivity of a Sequence of Numbers and the Riemann Hypothesis」. Journal of Number Theory, 65(2). [②④]
15. E. Bombieri & J. C. Lagarias (1999).「Complements to Li's Criterion for the Riemann Hypothesis」. Journal of Number Theory, 77(2). [②④]
16. L. Báez-Duarte (2003).「A Strengthening of the Nyman-Beurling Criterion for the Riemann Hypothesis」. Atti della Accademia Nazionale dei Lincei, Rendiconti Lincei Mat. Appl., 14(1). [②④]
17. X. Gourdon (2004).「The 10^13 First Zeros of the Riemann Zeta Function, and Zeros Computation at Very Large Height」. 在线技术报告（numbers.computation.free.fr）. [②④]
18. D. J. Platt (2017).「Isolating Some Non-trivial Zeros of Zeta」. Mathematics of Computation, 86(307). [②④]
19. M. O. Rabin (1980).「Probabilistic Algorithm for Testing Primality」. Journal of Number Theory, 12(1). [②④]
20. R. Solovay & V. Strassen (1977).「A Fast Monte-Carlo Test for Primality」. SIAM Journal on Computing, 6(1). [②④]
21. W. P. Thurston (1994).「On Proof and Progress in Mathematics」. Bulletin of the American Mathematical Society, 30(2). [①③]
22. A. Jaffe & F. Quinn (1993).「"Theoretical Mathematics": Toward a Cultural Synthesis of Mathematics and Theoretical Physics」. Bulletin of the American Mathematical Society, 29(1). [①③]
23. J. von Neumann (1947).「The Mathematician」. 收于 R. B. Heywood（编）,《The Works of the Mind》. University of Chicago Press. [①③]
24. K. Appel & W. Haken (1977).「Every Planar Map Is Four Colorable, Part I: Discharging」. Illinois Journal of Mathematics, 21(3). [②③]
25. T. Hales et al. (2017).「A Formal Proof of the Kepler Conjecture」. Forum of Mathematics, Pi, 5. [②③④]
26. N. Alon & J. H. Spencer (1992).《The Probabilistic Method》. Wiley. [②④]
27. P. J. Davis & R. Hersh (1981).《The Mathematical Experience》. Birkhäuser. [①③]
28. W. T. Gowers (2000).「The Two Cultures of Mathematics」. 收于《Mathematics: Frontiers and Perspectives》. American Mathematical Society. [①③]
29. T. Tao (2007).「What Is Good Mathematics?」. Bulletin of the American Mathematical Society, 44(4). [①③]
30. H. L. Montgomery (1973).「The Pair Correlation of Zeros of the Zeta Function」. 收于《Analytic Number Theory》, Proc. Sympos. Pure Math., XXIV. American Mathematical Society. [②③]
31. P. Sarnak (2004).「Problems of the Millennium: The Riemann Hypothesis」. Clay Mathematics Institute. [②③④]
32. J. C. Lagarias (2002).「An Elementary Problem Equivalent to the Riemann Hypothesis」. The American Mathematical Monthly, 109(6). [②④]
33. A. M. Odlyzko (1987).「On the Distribution of Spacings Between Zeros of the Zeta Function」. Mathematics of Computation, 48(177). [②④]
