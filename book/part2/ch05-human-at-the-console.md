# 第 5 章　控制台前的人

> **论点**：当你必须满足的是一个人的真实偏好或意图时，你面对的是永久的部分可观测，潜在目标无法直接读出，而有能力的应对是把一个有判断力的主体放进回路，并省着、且聪明地去问它。

## 你要的不是你说的

一个被反复讲烂、却始终成立的场景：用户描述了他想要的东西，工程师严丝合缝地造了出来，交付那天，用户看着它说，不，这不是我要的。

没有人撒谎。用户说的是真话，工程师也照做了。出问题的地方在更深处：用户真正想要的那个东西，从一开始就没有、也无法被完整地说出口。这一章看的，是当你必须满足的目标藏在另一个人的脑子里时，有能力的人怎么办。这里的不可验证，属于第 2 章那五副面孔中的「部分可观测」：相关的状态对你隐藏着，而且不是暂时隐藏，是永久隐藏。你没法把目标从一个人的脑子里读出来，于是也没法验证你究竟满足了它没有。

## 潜在的偏好

把这件事说准。用户的真实偏好，是一个潜在变量。它驱动着他的反应，却从不直接显现，你只能从他的行为里旁敲侧击地推断。

更麻烦的是，这个潜在目标常常连用户自己都读不出来。心理学家斯洛维奇有一个不讨喜却扎实的论断：偏好在很多时候不是被表达的，而是在被询问的那一刻才被构造出来。你问一个人想要什么，他给你的答案，往往是被你的问法、被当时的选项、被他刚好想到的参照点一起塑造成形的，而不是从某个早已存在的、定义清晰的偏好库里取出来的。这意味着「先把需求问清楚，再去实现」这个看似稳妥的次序，建立在一个常常不成立的假设上：假设那个需求作为一个确定的对象，先于询问而存在。

于是你面对的不是一个「信息暂时缺失、补齐即可」的处境。哪怕用户全程配合、知无不言，目标依然测不准。这是部分可观测最纯的人形版本。

## 问一次为什么不够

如果偏好是个固定的靶子，问一次、问清楚，原则上就够了。它不是。

经济学早就分开了两样东西：陈述的偏好（一个人说他要什么）和显示的偏好（一个人的实际选择暴露出他要什么），二者经常对不上。需求文档是有损压缩：把一个活的、随情境变化的意图，压成一份静态的条目清单，丢掉的恰恰是那些当时没想到、却在见到成品后立刻能指出来的东西。而且意图本身会漂移，人在看到一个具体实现之后，偏好会被这个实现重新校准，他现在想要的，已经不是项目启动时想要的了。

所以「问一次」失败，不是因为你问得不够好，而是因为这个对象的性质决定了单次询问无法锁定它。能对付它的，只有一种结构：不断地行动、观察、再修正。

## 第一招：把判断者放进回路

第一种应对，是承认你读不出目标，于是改为在每个决策点引入那个唯一知道目标的主体，让它来纠偏。行动，观察反应，更新，再行动。把人放进回路。

这条回路在很多领域各自被重新发明过。人因工程里，谢里登的「人类监督控制」把人定位成一个在自动化之上做监督与干预的判断者，而不是被一份规格一次性替代掉的角色。可用性工程里，古尔德与刘易斯 1985 年那篇经验之谈，把它压成三条朴素到几乎像废话、却被无数项目违反的原则：尽早且持续地关注用户，做经验性的测量，迭代式地设计。尼尔森后来把它工程化成一整套可用性方法。推荐系统从用户的点击、停留、跳过里学习他没说出口的口味，本质上也是同一条回路。霍维茨 1999 年的混合主动式界面、费尔斯与奥尔森 2003 年提出的交互式机器学习，讲的都是人与系统轮流出招、彼此校准的同一件事。

这里要防一个叙述上的塌缩：交互式获取不是某一种具体技术，它是一个方法族。实验设计、主动学习、序贯决策，乃至强化学习里的探索，都是这条「行动-观察-更新」回路在不同假设下的实例。把它写成「就是 A/B 测试」或「就是某个算法」，会把一个普遍的姿势矮化成一件工具。

## 第二招：把每一次提问花在刀刃上

回路要转，就得不断向人提问，而提问是有代价的。用户的耐心、注意力、时间，都是稀缺的；问得太多太笨，人会烦、会敷衍、会离开。于是第二招登场：既然查验昂贵，就把有限的提问花在信息量最大的地方。

这一招有干净的理论。林德利 1956 年给出一个实验所提供的信息的度量，霍华德 1966 年提出信息的价值理论，把「该不该花代价去获取这条信息」变成一个可计算的决策。贝叶斯实验设计（查洛纳与韦尔迪内利的综述是一份好地图）把它系统化：在所有可问的问题里，挑那个期望最能压缩你不确定性的。形式上，若 $\theta$ 是你想推断的潜在偏好，$y_q$ 是问题 $q$ 的回答，你要挑的是让期望信息增益最大的 $q$：

$$q^\star=\arg\max_q\; \mathbb{E}_{y_q}\big[\,\mathrm{H}(\theta)-\mathrm{H}(\theta\mid y_q)\,\big]=\arg\max_q\; I(\theta;y_q),$$

也就是让回答与目标之间的互信息最大。机器学习里这套思想叫主动学习：科恩等人 1996 年的统计式主动学习、宁与高 1994 年的不确定性采样、宋等人 1992 年的委员会查询，都是在问同一个问题，下一个标注该花在哪个样本上最划算。当用户难以打分、却很容易在两个选项里挑一个更好时，成对比较（布拉德利-特里模型，$P(a\succ b)=\sigma(s_a-s_b)$）就成了信息效率最高的问法之一。

同样要防塌缩。沙赫里亚里等人 2016 年那篇综述的标题颇有意味，《把人移出回路》，讲的是用高斯过程做贝叶斯优化，自动地选下一个该试的点。它极其有用，但它只是这个方法族里的一种实现，不是「最优筛查」的全部。把这一招等同于高斯过程，就像把交通等同于汽车。

## 当代的化身，和它的反噬

把这两招合起来，就得到了今天大模型对齐的主力方法。基于人类反馈的强化学习（克里斯蒂亚诺等人 2017 年奠基，斯蒂农等人 2020 年用于摘要，欧阳等人 2022 年的 InstructGPT）做的正是：用人的成对比较去学一个奖励模型，再用这个模型作为人类偏好的代理去优化系统。它把「行动-观察-更新」和「把提问花在刀刃上」缝在了一起。

而它的失效方式，恰好预演了本书后面几章的主题。那个学出来的奖励模型，是真实偏好的一个代理，于是它会被钻空子：系统学会取悦奖励模型，而不是取悦人，输出看起来更好、实则更糟，这正是第 11 章要正面处理的 Goodhart 败法。回路里的那个「神谕」（人）本身也不可靠，会疲劳、会前后不一、会有系统性偏差，把判断者放进回路并不等于放进了真理。贝恩布里奇 1983 年那篇《自动化的反讽》早就点破：你越是把人推到监督者的位置，他越是缺少保持判断力所需的实操与情境感，等真要他接管时，他反而最没准备。信任的校准（李与西 2004 年的研究）于是成了一个独立的难题：人既可能过度依赖一个不该信的系统，也可能弃用一个其实可靠的系统。

把人放进回路，不是把不可验证消解掉，而是把它搬了个家：从「我能不能验证目标」搬成了「我能不能信任回路里这个也不完美的判断者」。

## 这一章通向哪里

控制台前的人，教给我们两招：在自己缺乏验证能力时，把一个有判断力的主体请进回路（神谕入回路），以及把昂贵的查验花在信息量最大处（最优筛查）。这两招在本书里会反复回来，第三部会把它们从这个现场里拎出来单独命名，第 10 章谈借来的判断，第 9 章谈把查验花在刀刃上。

但这一章自始至终有一个前提：你还在场，回路还在转，你随时能观察、能纠偏。下一章把这个前提抽走。当你必须把行动权交出去，让一个系统在你看不见的地方、面对你没预演过的情形自行其是时，验证的难题会换一副更硬的面孔。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实；个别未能确证者标「（细节待核）」。

1. D. V. Lindley (1956).「On a Measure of the Information Provided by an Experiment」. The Annals of Mathematical Statistics, 27(4), 986-1005. [②]
2. R. A. Bradley, M. E. Terry (1952).「Rank Analysis of Incomplete Block Designs: I. The Method of Paired Comparisons」. Biometrika, 39(3/4), 324-345. [②]
3. R. A. Howard (1966).「Information Value Theory」. IEEE Transactions on Systems Science and Cybernetics, 2(1), 22-26. [②④]
4. J. Mockus, V. Tiesis, A. Zilinskas (1978).「The Application of Bayesian Methods for Seeking the Extremum」. Towards Global Optimization, 2, 117-129. North-Holland. [②]
5. K. Chaloner, I. Verdinelli (1995).「Bayesian Experimental Design: A Review」. Statistical Science, 10(3), 273-304. [②]
6. D. Cohn, Z. Ghahramani, M. Jordan (1996).「Active Learning with Statistical Models」. Journal of Artificial Intelligence Research, 4, 129-145. [②]
7. H. S. Seung, M. Opper, H. Sompolinsky (1992).「Query by Committee」. COLT '92, 287-294. [②]
8. D. D. Lewis, W. A. Gale (1994).「A Sequential Algorithm for Training Text Classifiers」. SIGIR '94, 3-12. [②]
9. B. Settles (2009).《Active Learning Literature Survey》. Computer Sciences Technical Report 1648, University of Wisconsin-Madison. [②④]
10. B. Settles (2011).「From Theories to Queries: Active Learning in Practice」. JMLR Workshop and Conference Proceedings, 16, 1-18. [②④]
11. P. Slovic (1995).「The Construction of Preference」. American Psychologist, 50(5), 364-371. [②④]
12. T. B. Sheridan (1992).《Telerobotics, Automation, and Human Supervisory Control》. MIT Press. [②④]
13. L. Bainbridge (1983).「Ironies of Automation」. Automatica, 19(6), 775-779. [②④]
14. R. Parasuraman, T. B. Sheridan, C. D. Wickens (2000).「A Model for Types and Levels of Human Interaction with Automation」. IEEE Transactions on Systems, Man, and Cybernetics, Part A, 30(3), 286-297. [②④]
15. J. D. Lee, K. A. See (2004).「Trust in Automation: Designing for Appropriate Reliance」. Human Factors, 46(1), 50-80. [②④]
16. M. R. Endsley (1995).「Toward a Theory of Situation Awareness in Dynamic Systems」. Human Factors, 37(1), 32-64. [②④]
17. S. K. Card, T. P. Moran, A. Newell (1983).《The Psychology of Human-Computer Interaction》. Lawrence Erlbaum Associates. [②④]
18. D. A. Norman (1988).《The Psychology of Everyday Things》. Basic Books. [④]
19. J. Nielsen (1993).《Usability Engineering》. Academic Press. [④]
20. J. D. Gould, C. Lewis (1985).「Designing for Usability: Key Principles and What Designers Think」. Communications of the ACM, 28(3), 300-311. [④]
21. H. Beyer, K. Holtzblatt (1998).《Contextual Design: Defining Customer-Centered Systems》. Morgan Kaufmann. [④]
22. E. Horvitz (1999).「Principles of Mixed-Initiative User Interfaces」. CHI '99, 159-166. [②④]
23. J. A. Fails, D. R. Olsen Jr. (2003).「Interactive Machine Learning」. IUI '03, 39-45. [②④]
24. S. Amershi, D. Weld, M. Vorvoreanu, A. Fourney, B. Nushi, P. Collisson, J. Suh, S. Iqbal, P. Bennett, K. Inkpen, J. Teevan, R. Kikin-Gil, E. Horvitz (2019).「Guidelines for Human-AI Interaction」. CHI '19. [②④]
25. W. B. Knox, P. Stone (2009).「Interactively Shaping Agents via Human Reinforcement: The TAMER Framework」. K-CAP '09. [②④]
26. D. Hadfield-Menell, S. J. Russell, P. Abbeel, A. Dragan (2016).「Cooperative Inverse Reinforcement Learning」. NeurIPS 2016. [②④]
27. P. F. Christiano, J. Leike, T. B. Brown, M. Martic, S. Legg, D. Amodei (2017).「Deep Reinforcement Learning from Human Preferences」. NeurIPS 2017. [②④]
28. N. Stiennon, L. Ouyang, J. Wu, D. M. Ziegler, R. Lowe, C. Voss, A. Radford, D. Amodei, P. Christiano (2020).「Learning to Summarize from Human Feedback」. NeurIPS 2020. [②④]
29. L. Ouyang et al. (2022).「Training Language Models to Follow Instructions with Human Feedback」. NeurIPS 2022. [②④]
30. C. Wirth, R. Akrour, G. Neumann, J. Fürnkranz (2017).「A Survey of Preference-Based Reinforcement Learning Methods」. Journal of Machine Learning Research, 18(136), 1-46. [②④]
31. B. Shahriari, K. Swersky, Z. Wang, R. P. Adams, N. de Freitas (2016).「Taking the Human Out of the Loop: A Review of Bayesian Optimization」. Proceedings of the IEEE, 104(1), 148-175. [②④]
