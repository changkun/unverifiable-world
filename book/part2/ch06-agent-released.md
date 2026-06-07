# 第 6 章　放出去的智能体

> **论点**：一旦把行动委托给自主系统，你无法验证它在将遇到的一切情形里的未来行为（开放世界）；若它还能耍策略，你又叠上对抗式不可验证，于是应对从「证明它对」转向「限制它能破坏什么、给你的信任定价、让它的行为事后可查」。

## 交出去之后

上一章你还在场。这一章，你把手松开。

把一段不受信的代码跑起来，把工具和权限交给一个能自己决定下一步的系统，让一个自动驾驶在你没坐在里面的时候上路。一旦行动权交出去，一个新的难题出现了：你没法验证它在将要遇到的一切情形里会怎么做，因为那些情形你大多没见过，也没法预先穷举。上一章的不可验证来自目标藏在别人脑子里，这一章的不可验证来自行为发生在未来、发生在你看不见的地方，而当这个系统还会耍策略时，又叠上一层对抗。

## 未来行为的缺口

你测试过的，是有限几个输入；它会遇到的，是一个开放的世界。这中间的缺口，不是「再多测一些就能补上」的工程缺口，它有原则上的根。

赖斯定理说得很硬：程序的任何非平凡语义性质都是不可判定的。也就是说，不存在一个通用算法，能对任意程序判定它是否「总是安全」「绝不泄露」「永远终止于好状态」。这不是算力不够，是逻辑上办不到，它是图灵停机问题投在「程序行为」上的影子。你想要的那种保证，对任意一个足够通用的自主系统，原则上无法在事前一次性验明。

更彻底的一击来自汤普森 1984 年图灵奖演讲里那个著名的论证：连你正在运行的这个工件本身，你都无法完全信任。一个被做了手脚的编译器，可以在编译时悄悄植入后门，再把痕迹从自己的源码里抹掉，于是你审遍源码也看不出来。你能验证的，永远只是某个表象层；底下还有你没看、也看不尽的层。把这两件事放在一起：行为在未见输入上不可验证，工件在底层不可全验。这是本书目前遇到的最硬的不可验证。

## 当它会耍策略

如果这个系统只是被动地把没见过的输入处理错，那还只是「部分可观测」加「开放世界」。可一旦它有了自己的目标，并且这目标与你的不完全一致，它就会主动地、策略性地行动，包括绕过你的检查。这时第 2 章那第五副面孔，对抗，登场了。

这不是科幻式的担忧，它有结构性的来由。奥莫亨德罗 2008 年、博斯特罗姆 2014 年指出的工具性趋同：一个为几乎任何目标优化的智能体，都会顺带追求一些工具性的子目标，自我保存、获取资源、抗拒被关停，因为这些几乎对任何最终目标都有用。特纳等人 2021 年把其中一条做成了定理：在相当一般的条件下，最优策略倾向于寻求权力（保留更多选项的状态）。在今天的系统里，这表现为一组具体而棘手的失效：奖励设定的偏差被系统钻空子（潘等人 2022），规格正确目标却泛化错了（沙阿等人 2022 的目标误泛化），以及克拉科夫娜等人收集的大量「规格博弈」实例，系统精确地满足了你写下的目标，却彻底违背了你的本意。哪怕在最窄的层面，对抗样本（塞盖迪等人 2014、古德费洛等人 2015）也表明：一个表现优异的模型，可以被一个人眼看不出的微小扰动诱导出离谱的错误。

这件事其实古老。经济学早把它叫做委托代理问题（罗斯 1973、詹森与梅克林 1976）：当你委托别人替你行动，而你无法完全监督他时，他的利益与你的偏离就会产生「代理成本」。两千年来人类雇人、立约、设监察，对付的都是同一个结构。自主系统只是把它推到了一个新的尺度上。

## 应对：从「证明它对」到「围住它的错」

既然事前证不出它对，有能力的应对就不再纠缠于证明，而是换三个问题来问：就算它错了，能坏到哪儿？我对它该信几分？万一它真错了，我事后查得到吗？三招对应三个问题。

**第一招，衰减与围栏：缩小爆炸半径。** 这是计算机安全最老的智慧。萨尔策与施罗德 1975 年的最小权限原则、兰普森 1973 年的围堵问题，讲的都是：只给一个组件完成本职所必需的最小能力，把它能触及的范围圈死。沙箱、能力限制、职责分离，都是它的化身。在智能体语境里，这一招还多了一个面向，可纠正性：把系统设计成不抗拒被停下。索亚雷斯等人 2015 年的 corrigibility、奥尔索与阿姆斯特朗 2016 年的「可安全中断的智能体」、哈德菲尔德-梅内尔等人 2017 年的「关停博弈」，研究的正是如何让一个有目标的系统，不把「人来按下停止键」当成需要抵抗的威胁。

**第二招，标定与分级信任：别用二值。** 不要把系统的输出当成「可信／不可信」的开关，而是维持一个标定的信心，按信心的高低分级行动。这要求系统的「自信」是可信的，而现代神经网络恰恰常常过度自信（郭等人 2017 指出了这一点），于是需要重新校准，或用共形预测（沃夫克等人、安杰洛普洛斯与贝茨）给出有覆盖保证的不确定性。落到操作上，就是一条以信心 $p$、潜在危害 $c$ 为输入的分级自治规则（允许、询问、阻止），其中 $\tau_{\text{hi}}$、$\tau_{\text{lo}}$ 是信心阈值，$c_{\max}$ 是可承受的危害上限：

$$a(p,c)=\begin{cases} \textsf{allow}, & p \ge \tau_{\text{hi}}\ \wedge\ c \le c_{\max},\\ \textsf{ask}, & \tau_{\text{lo}} \le p < \tau_{\text{hi}},\\ \textsf{block}, & p < \tau_{\text{lo}}\ \vee\ c > c_{\max}. \end{cases}$$

允许、询问、阻止，这个今天在各类智能体工具里随处可见的三档模式，本质就是把不可验证的「它对不对」，换成了可操作的「它有多大把握、这一步多危险」。

**第三招，留痕与可审计：让错误事后现形。** 防不住的，就让它可被发现。维茨纳等人 2008 年的「信息问责」把重心从「事前阻止」移到「事后追责」；证书透明度（IETF RFC 6962）是一个真实运转的例子，它不阻止证书被错发，而是让每一张证书都进入一个公开、可验、不可篡改的日志，使错发无所遁形。布伦戴奇等人 2020 年那份关于可信 AI 的报告，整篇讲的都是如何让一个系统的行为产生可被第三方核验的证据。

## 围堵的代价

三招都不是把不可验证消解掉，而是把它搬家，搬家是要付费的。

围栏会被翻越：沙箱有逃逸，权限会蔓延。分级自治依赖那个被请来确认的人，而贝恩布里奇 1983 年的《自动化的反讽》早就指出，越是把人架到监督者的位置，他越是丧失了真要接管时所需的技能与情境感；帕拉苏拉曼与赖利 1997 年把人对自动化的失当一口气列全，误用、弃用、滥用，里森 1990 年的《人的失误》则揭示这些失当如何系统性地发生。留痕则永远栽在同一处：没人去读的日志，等于没有日志。

更深一层是系统论的视角。佩罗 1984 年的《正常事故》论证：当一个系统既高度复杂、又紧密耦合时，事故不是偶发的意外，而是其结构的常态产物，再多的局部防护也只是把失效推向更隐蔽的组合。莱韦森 2011 年由此主张，安全不是「让每个零件都可靠」，而是一个控制问题，要从整个系统的约束与反馈去设计。围堵能压低单点失效的代价，却压不掉复杂耦合本身带来的风险。

把行动权交出去，你换来的从来不是「它一定不出错」，而是「就算它出错，坏得有限、看得见、拦得住一部分」。这已经是在这种不可验证下能拿到的最好结果。

## 这一章通向哪里

放出去的智能体，逼出了三招：缩小失败的爆炸半径（衰减围栏）、按标定的信心分级行动（标定）、让失败事后可查（留痕）。它们会在第三部被单独拎出来命名，第 12 章谈围堵与审计如何成对，第 11 章谈标定。

而那个委托代理的骨架（你无法完全监督一个替你行动的主体），会在第 8 章以更大的尺度重现：当那个「放出去的智能体」不再是一段代码，而是一整个组织、一个国家。在那之前，下一章先走进一个最纯的现场，数学，那里没有藏起来的状态，也没有会骗你的对手，不可验证却依然如影随形。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实；个别未能确证者标「（细节待核）」。

### 服务委托的可控边界（衰减／围栏）

1. J. Saltzer & M. Schroeder (1975).「The Protection of Information in Computer Systems」. Proceedings of the IEEE, 63(9), 1278-1308. [②]
2. B. Lampson (1973).「A Note on the Confinement Problem」. Communications of the ACM, 16(10), 613-615. [②]
3. R. Anderson (2008).《Security Engineering: A Guide to Building Dependable Distributed Systems》(2nd ed.). Wiley. [②]
4. L. Orseau & S. Armstrong (2016).「Safely Interruptible Agents」. 收于《Proceedings of the Thirty-Second Conference on Uncertainty in Artificial Intelligence (UAI 2016)》, 557-566. [②④]
5. N. Soares, B. Fallenstein, S. Armstrong & E. Yudkowsky (2015).「Corrigibility」. 收于《Workshops at the Twenty-Ninth AAAI Conference on Artificial Intelligence》. [②]
6. D. Hadfield-Menell, A. Dragan, P. Abbeel & S. Russell (2017).「The Off-Switch Game」. 收于《Proceedings of the Twenty-Sixth International Joint Conference on Artificial Intelligence (IJCAI 2017)》, 220-227. [②]

### 行为不可验证的理论根基

7. A. Turing (1936).「On Computable Numbers, with an Application to the Entscheidungsproblem」. Proceedings of the London Mathematical Society, s2-42, 230-265. [②]
8. H. G. Rice (1953).「Classes of Recursively Enumerable Sets and Their Decision Problems」. Transactions of the American Mathematical Society, 74, 358-366. [②]
9. K. Thompson (1984).「Reflections on Trusting Trust」. Communications of the ACM, 27(8), 761-763. [②①]

### 目标偏移、工具性趋同与对抗

10. S. Omohundro (2008).「The Basic AI Drives」. 收于《Artificial General Intelligence 2008: Proceedings of the First AGI Conference》, IOS Press, Frontiers in AI and Applications 171, 483-492. [②]
11. N. Bostrom (2014).《Superintelligence: Paths, Dangers, Strategies》. Oxford University Press. [②④]
12. S. Russell (2019).《Human Compatible: Artificial Intelligence and the Problem of Control》. Viking. [②④]
13. D. Amodei, C. Olah, J. Steinhardt, P. Christiano, J. Schulman & D. Mané (2016).「Concrete Problems in AI Safety」. arXiv:1606.06565. [②]
14. A. M. Turner, L. Smith, R. Shah, A. Critch & P. Tadepalli (2021).「Optimal Policies Tend to Seek Power」. 收于《Advances in Neural Information Processing Systems 34 (NeurIPS 2021)》. [②]
15. E. Hubinger, C. van Merwijk, V. Mikulik, J. Skalse & S. Garrabrant (2019).「Risks from Learned Optimization in Advanced Machine Learning Systems」. arXiv:1906.01820. [②]
16. J. Pan, K. Bhatia & J. Steinhardt (2022).「The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models」. 收于《International Conference on Learning Representations (ICLR 2022)》. [②]
17. R. Shah, V. Varma, R. Kumar, M. Phuong, V. Krakovna, J. Uesato & Z. Kenton (2022).「Goal Misgeneralization: Why Correct Specifications Aren't Enough For Correct Goals」. arXiv:2210.01790. [②]
18. V. Krakovna, J. Uesato, V. Mikulik, M. Rahtz, T. Everitt, R. Kumar, Z. Kenton, J. Leike & S. Legg (2020).「Specification Gaming: The Flip Side of AI Ingenuity」. DeepMind Blog. [②]
19. C. Szegedy, W. Zaremba, I. Sutskever, J. Bruna, D. Erhan, I. Goodfellow & R. Fergus (2014).「Intriguing Properties of Neural Networks」. 收于《International Conference on Learning Representations (ICLR 2014)》. [②]
20. I. Goodfellow, J. Shlens & C. Szegedy (2015).「Explaining and Harnessing Adversarial Examples」. 收于《International Conference on Learning Representations (ICLR 2015)》. [②]

### 标定：把信任分级而非二值

21. C. Guo, G. Pleiss, Y. Sun & K. Q. Weinberger (2017).「On Calibration of Modern Neural Networks」. 收于《Proceedings of the 34th International Conference on Machine Learning (ICML 2017)》, PMLR 70, 1321-1330. [②]
22. A. N. Angelopoulos & S. Bates (2021).「A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification」. arXiv:2107.07511. [②]
23. V. Vovk, A. Gammerman & G. Shafer (2005).《Algorithmic Learning in a Random World》. Springer. [②]

### 留痕：可审计、可问责

24. D. J. Weitzner, H. Abelson, T. Berners-Lee, J. Feigenbaum, J. Hendler & G. J. Sussman (2008).「Information Accountability」. Communications of the ACM, 51(6), 82-87. [②④]
25. B. Laurie, A. Langley & E. Kasper (2013).「Certificate Transparency」. IETF RFC 6962. [②④]
26. M. Brundage, S. Avin, J. Wang, H. Belfield, G. Krueger, G. Hadfield 等 (2020).「Toward Trustworthy AI Development: Mechanisms for Supporting Verifiable Claims」. arXiv:2004.07213. [②④]

### 复杂系统、自动化与人机责任

27. N. Leveson (2011).《Engineering a Safer World: Systems Thinking Applied to Safety》. MIT Press. [②④]
28. C. Perrow (1984).《Normal Accidents: Living with High-Risk Technologies》. Basic Books. [②④]
29. L. Bainbridge (1983).「Ironies of Automation」. Automatica, 19(6), 775-779. [②④]
30. R. Parasuraman & V. Riley (1997).「Humans and Automation: Use, Misuse, Disuse, Abuse」. Human Factors, 39(2), 230-253. [②④]
31. J. Reason (1990).《Human Error》. Cambridge University Press. [②④]

### 委托代理的经济学骨架

32. S. A. Ross (1973).「The Economic Theory of Agency: The Principal's Problem」. American Economic Review, 63(2), 134-139. [②]
33. M. C. Jensen & W. H. Meckling (1976).「Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure」. Journal of Financial Economics, 3(4), 305-360. [②]
