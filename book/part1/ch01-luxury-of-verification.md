# 第 1 章　验证的奢侈

> **论点**：事前就能确认某事为真、正确或安全的「完整验证」，在人类与机器的生活里是例外，不是常态。

## 关键节拍

先承认验证廉价的那些场景，正是它们训练出了我们的错觉：算术、排序、一张可以核对的收据。

再指出错觉破裂的地方：规模、开放世界、他人之心、未来。

重述：大多数有后果的行动，都踩在未经验证的地面上。

## 例子

你能验证 7×8；你无法验证婚姻会长久、代码库没有 bug、理论为真、公司是健康的。

## 接口

既然验证通常不可得，第一个该问的是它为什么不可得，而答案不止一种。引出第 2 章。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实；个别未能确证者标「（细节待核）」。

1. A. M. Turing (1936). 「On Computable Numbers, with an Application to the Entscheidungsproblem」. Proceedings of the London Mathematical Society, s2-42, 230-265. [②]（所在 series 2 第 42 卷横跨 1936 至 1937 年，部分书目标作 1937，正文采用通行的 1936。证明 Entscheidungsproblem 与停机问题不可判定，是「理论上被研究过的验证极限」的奠基。）

2. A. Church (1936). 「An Unsolvable Problem of Elementary Number Theory」. American Journal of Mathematics, 58(2), 345-363. [②]（以 lambda 演算独立给出判定问题不可解的证明，比 Turing 早数月发表，与 Turing 共同奠定可计算性的理论边界。）

3. K. Gödel (1931). 「Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I」. Monatshefte für Mathematik und Physik, 38, 173-198. [②]（不完备性定理：一致的形式系统无法在系统内被完全验证。）

4. H. G. Rice (1953). 「Classes of Recursively Enumerable Sets and Their Decision Problems」. Transactions of the American Mathematical Society, 74, 358-366. [②]（Rice 定理：程序的一切非平凡语义性质均不可判定，把停机问题的不可验证性推广为普遍结论。）

5. S. A. Cook (1971). 「The Complexity of Theorem-Proving Procedures」. Proceedings of the 3rd Annual ACM Symposium on Theory of Computing (STOC), 151-158. [②]（确立 NP 完全性概念。即便验证在原则上可判定，其计算代价仍可能使事前完整验证在实践中不可行。）

6. C. A. R. Hoare (1969). 「An Axiomatic Basis for Computer Programming」. Communications of the ACM, 12(10), 576-580. [②①]（形式化程序正确性证明的公理基础，既是验证理论的代表作，也含对验证可行边界的工程判断。）

7. J. C. King (1976). 「Symbolic Execution and Program Testing」. Communications of the ACM, 19(7), 385-394. [②]（符号执行：以符号代替具体输入系统化探查路径，亦揭示路径爆炸等使穷尽验证受限的根本困难。）

8. E. M. Clarke 与 E. A. Emerson (1981). 「Design and Synthesis of Synchronization Skeletons Using Branching Time Temporal Logic」. Logics of Programs (Lecture Notes in Computer Science 131), Springer, 52-71. [②]（模型检验的奠基论文，系工作坊论文（非期刊），收入 LNCS 第 131 卷。自动验证仅适用于有限状态系统，界定了机器验证的可达范围。）

9. R. A. DeMillo, R. J. Lipton 与 A. J. Perlis (1979). 「Social Processes and Proofs of Theorems and Programs」. Communications of the ACM, 22(5), 271-280. [①②]（论证形式化程序验证不可能扮演数学证明那样的角色，验证的可信赖性来自社会过程而非机械证明。）

10. J. H. Fetzer (1988). 「Program Verification: The Very Idea」. Communications of the ACM, 31(9), 1048-1063. [①②]（DeMillo 论争的续篇：区分作为逻辑结构的算法与作为因果模型的程序，主张程序验证作为完全可靠的方法连理论可能性都不成立。引发 1989 年大规模技术通信论战。）

11. F. P. Brooks (1987). 「No Silver Bullet: Essence and Accidents of Software Engineering」. IEEE Computer, 20(4), 10-19. [①]（原为 1986 年 IFIP 第 10 届世界计算机大会邀请论文（Information Processing 86, 1069-1076）。资深工程师对软件本质复杂性、对「无银弹」即无法一举验证消除缺陷的判断。）

12. D. L. Parnas (1985). 「Software Aspects of Strategic Defense Systems」. Communications of the ACM, 28(12), 1326-1335. [①]（Parnas 辞去星球大战计划顾问后撰文，论证此类系统软件无法被充分验证而值得信赖；同年另以系列短文见于 American Scientist。工程师对验证极限的公开判断。）

13. E. W. Dijkstra (1972). 「The Humble Programmer」（1972 ACM 图灵奖演讲）. Communications of the ACM, 15(10), 859-866. [①]（图灵奖得主主张程序应被正确地构造而非调试出正确，反映对事后验证局限的判断。）

14. E. W. Dijkstra (1972).《Notes on Structured Programming》（载于 O.-J. Dahl, E. W. Dijkstra, C. A. R. Hoare 编《Structured Programming》）. Academic Press. [①]（「测试只能证明缺陷的存在，不能证明其不存在」即出于此文；该论断最早见于手稿 EWD249（1970），1972 年收入《Structured Programming》正式出版。）

15. N. G. Leveson 与 C. S. Turner (1993). 「An Investigation of the Therac-25 Accidents」. IEEE Computer, 26(7), 18-41. [①④]（Therac-25 放疗机软件致死事故的权威调查。工程现实中安全攸关系统未经充分验证即投用的后果，兼示在无法完全验证的世界里行动的代价。）

16. P. Naur 与 B. Randell（编）(1969).《Software Engineering: Report on a Conference Sponsored by the NATO Science Committee》. Scientific Affairs Division, NATO. [①]（会议于 1968 年 10 月在德国 Garmisch 召开，1969 年出版。「软件危机」提法的源头，集中记录从业者对软件无法被可靠验证与交付的集体判断。）

17. D. Hume (1748).《An Enquiry Concerning Human Understanding》. (London). [④③]（1748 年初版原题《Philosophical Essays Concerning Human Understanding》，1758 年改为今题。归纳问题：未来无法由过去经验事前完全验证，人只能依赖习惯行动。）

18. K. Popper (1959).《The Logic of Scientific Discovery》. Hutchinson. [③]（英文版系作者在德文原著《Logik der Forschung》（1934 年付印，版权页标 1935）基础上扩写而成。证伪主义：科学理论无法被证实，只能被否证，科学藉此进展。）

19. W. V. O. Quine (1951). 「Two Dogmas of Empiricism」. The Philosophical Review, 60(1), 20-43. [③]（经验论两个教条的批判与整体论：任何陈述都无法被孤立地验证或反驳，证据对理论的检验是欠决定的。）

20. T. S. Kuhn (1962).《The Structure of Scientific Revolutions》. University of Chicago Press. [③]（范式与科学革命：科学并非靠对真理的逐步验证累积前进，而是经由范式转换而跃迁。）

21. I. Lakatos (1976).《Proofs and Refutations: The Logic of Mathematical Discovery》（J. Worrall 与 E. Zahar 编）. Cambridge University Press. [③②]（证明与反驳：连数学证明也非一劳永逸的验证，而是经由反例与不断修正的创造性过程而成长。）

22. F. H. Knight (1921).《Risk, Uncertainty and Profit》. Houghton Mifflin. [④]（区分可度量的「风险」与不可度量的「不确定性」，奠定在无法事前验证的局面下决策与利润的理论。）

23. H. A. Simon (1955). 「A Behavioral Model of Rational Choice」. The Quarterly Journal of Economics, 69(1), 99-118. [④]（有限理性：计算能力有限的主体无法穷尽验证所有选项，只能满意即止（satisficing）。）

24. J. von Neumann 与 O. Morgenstern (1944).《Theory of Games and Economic Behavior》. Princeton University Press. [④]（博弈论与期望效用公理化：为在无法事前验证对手与结果的情形下作理性决策提供形式框架。）

25. L. J. Savage (1954).《The Foundations of Statistics》. John Wiley & Sons. [④]（主观概率与个人主义决策论的公理化：在无法客观验证概率的世界里，以主观信念作一致决策。）

26. J. M. Keynes (1937). 「The General Theory of Employment」. The Quarterly Journal of Economics, 51(2), 209-223. [④]（对真正不确定性的经典陈述（「关于此我们根本无从知晓」），强调投资决策在无法验证的未来面前依赖惯例与动物精神。）

27. A. Tversky 与 D. Kahneman (1974). 「Judgment under Uncertainty: Heuristics and Biases」. Science, 185(4157), 1124-1131. [④]（启发式与偏差：人在无法完整验证概率时依赖代表性、可得性等捷径，系统性地偏离规范。）

28. N. N. Taleb (2007).《The Black Swan: The Impact of the Highly Improbable》. Random House. [④]（黑天鹅：罕见而高影响事件无法被事前验证或预测，却主导历史，应据此调整在不确定世界中的生活方式。）
