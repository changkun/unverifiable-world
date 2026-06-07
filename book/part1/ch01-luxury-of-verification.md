# 第 1 章　验证的奢侈

> **论点**：事前就能确认某事为真、正确或安全的「完整验证」，在人类与机器的生活里是例外，不是常态。

## 七乘八，和其余的一切

你能验证七乘八等于五十六。你可以重数一遍、换个方法算一遍，或者干脆背出乘法表，几秒钟之内，对错板上钉钉。

现在换几件事。在说出「我愿意」之前，验证这段婚姻会长久；在按下上线之前，验证这个代码库一个 bug 都没有；在投入半生之前，验证你信奉的那个理论为真；在接下这份工作之前，验证这家公司是健康的。这些你都做不到。不是因为你不够努力，是因为这类事情根本不提供「事前验明」这个选项。

本书的第一块基石，就是这个反差：能在事前确认某事为真、为对、为安全的「完整验证」，在人类与机器的生活里是例外，不是常态。我们之所以觉得它该是常态，是因为我们的直觉在一道很窄的门里被训练大了。

## 验证廉价的那道窄门

哪些事我们验得动？算一道算术，给一串数字排序，核对一张收据的总额，判断棋盘上这步走子合不合规则。把这些放在一起看，它们共享几个隐秘的特征：对象是封闭的（所有相关的东西都摆在眼前），是有限的（情形数得过来），答案是局部而即时的（不依赖远处或将来），而且存在一个机械的判定程序（照着做就有是或否）。

正是这道窄门，喂养了我们「凡事可检验」的直觉。学校里反复奖励的，恰是这类有标准答案、可当场批改的题目。于是我们悄悄地把一条经验，「在我练习过的事情里，对错总能查清」，外推成了一条世界观，「事情的对错总能查清」。这条外推是错的，而且错得很有系统。窄门之外，上面那四个特征几乎逐一失效。

## 错觉破裂在四个地方

**规模。** 门里的情形数得过来，门外的数不过来。一个有 $n$ 个分支的程序，可能的执行路径多达 $2^n$ 条，几十个分支就足以让穷尽测试在宇宙寿命内都跑不完。你能验证它在你想到的那几个输入上对，无法验证它在所有输入上对。检验单个情形容易，检验全部情形，量词「所有」一出现，就跨进了另一个世界。

**开放世界。** 门里的对象封闭，门外的世界还在不断送来新东西。你测过的是有限几个场景，系统真正会遇到的，是一个开放、未完待续的环境。自动驾驶在测试场里跑得再好，也没法穷举马路上下一秒会冒出什么。你验证的永远是过去见过的切片，要赌的却是没见过的将来。

**他人之心。** 门里的状态可观测，门外，你要满足的目标常常锁在另一个人的脑子里。用户真正想要什么、上司满不满意、对方爱不爱你，这些是潜在变量，你只能从行为旁敲侧击，无法直接读出，因而也无法直接验证你是否满足了它。

**未来。** 这是最深的一处，休谟在 1748 年就把它挑明了：归纳没有逻辑保证。太阳过去每天升起，并不能在逻辑上证明它明天还升；有限的过去经验，无法事前验证任何关于未来的全称判断。我们依赖的不是证明，而是习惯。凡是结果落在将来的行动，婚姻、投资、播种、托付，都在这道裂口的另一侧。

## 连最硬的两个领域也低头

也许你会想，规模、人心、未来这些软的领域认输也就罢了，数学和软件总该是完整验证的堡垒吧？恰恰是这两个最硬的地方，最清醒地承认了验证的限度。

软件这边，迪杰斯特拉留下一句被引滥却仍然正确的话：测试只能证明缺陷存在，不能证明缺陷不存在。他主张程序应当被正确地构造出来，而不是被调试出正确。可即便是形式化证明这条最严的路，德米洛、利普顿与佩利斯 1979 年那篇争议名文也指出，程序验证无法扮演数学证明那样的角色，它的可信最终来自社会过程，而非机械推导；费泽尔 1988 年把话说得更重，程序作为一个因果模型，与作为逻辑结构的算法之间有一道鸿沟，「完全可靠的程序验证」连理论上都不成立。布鲁克斯的《没有银弹》断言软件的本质复杂性无法被一招消除；帕纳斯辞去星球大战计划的顾问，公开论证那类系统的软件无法被验证到值得托付；而 Therac-25 放疗机因未经充分验证的软件缺陷致人死亡，是这一切判断用人命付的注脚。1968 年北约那场会议干脆造了个词，软件危机。

数学这边更釜底抽薪。哥德尔 1931 年证明，任何足够丰富而一致的形式系统，都存在它自己无法在内部判定的真命题；丘奇与图灵 1936 年各自证明，没有算法能判定任意命题是否可证（判定问题无解）；赖斯定理把它推到极致，程序的任何非平凡语义性质都不可判定。哪怕某个问题原则上可判定，库克 1971 年确立的 NP 完全性也表明，验证的代价可能爆炸到实践中根本跑不动。这些不是工程的暂时短板，是逻辑给验证划下的硬边界。这一层，下一章会专门去拆。

## 重述，以及这不是一句丧气话

把以上合起来：大多数有后果的行动，都踩在未经验证的地面上。

这不是一个让人瘫痪的结论，它是一个起点。承认验证是奢侈品，恰恰是认真对待行动的第一步。奈特 1921 年早就把可度量的「风险」与不可度量的「不确定性」分开，并指出利润正来自后者；凯恩斯谈到真正的不确定时只留下一句「关于此我们根本无从知晓」；西蒙看清有限的主体无法穷尽验证所有选项，于是提出「满意即止」；冯·诺依曼与摩根斯特恩、萨维奇则各自为「在无法事前验证结果时如何理性地下注」搭起了形式框架。一整门关于决策的学问，本就是建立在「验证不可得」这个前提之上的。问题从来不是怎样取消不确定，而是在不确定里怎样行动得当。

## 这一章通向哪里

既然验证通常不可得，第一个该问的就是：它为什么不可得？

答案不止一种，而这正是要紧之处。把「我没法检验它」当成一种处境，是这个领域最常见、也最误事的错。它其实是五种结构全然不同的处境，共用了一句话。下一章，我们把这句话掰成五瓣。

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
