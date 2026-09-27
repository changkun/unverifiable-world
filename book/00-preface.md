# 序　没有神谕的世界

古希腊人在出征、婚嫁或建城之前，往往先赴德尔斐求取神谕。神谕的意义并不在于它是否准确，而在于它所许诺的东西：在行动之前，总有一处地方能够给出答案。两千年后，计算机科学借用了这个词。在计算理论中，神谕（oracle，教材中多译作「谕示」）指一个黑箱：向它提交一个自身无法求解的问题，它即刻返回正确答案。两种神谕背后是同一个设想：行动之前，先把对错确定下来。

本书讨论的，正是这一设想落空之后的世界。

我们几乎从不验证。我们行动，然后或早或晚地得知结果，或者始终无从得知。「凡事皆可检验」之所以显得理所当然，是因为我们最早的训练来自一类特别狭窄的任务：算术、排序、核对收据。在这类任务中，答案近在咫尺，于是我们误以为整个世界皆是如此。然而一旦越出这一狭小的范围，验证便成了一种奢侈。七乘八可以验证；可是在说出「我愿意」之前，无人能够验证这段婚姻能否长久；在软件发布之前，无人能够验证代码中没有缺陷；在投身之前，也无人能够验证一个理论为真、一家公司健康、一个决定正确。大多数要紧的行动，都发生在未经验证的地面上。神谕沉默，行动却不能等待。

面对这一处境，常见的反应有两种：哀叹，或者假装。哀叹者认为，既然一切都无法确定，任何判断都不过是臆测。假装者则为自己造一个假神谕：把某个可以测量的数字奉为圭臬，仿佛它就是那个无法测量的真相。本书不取这两种态度，而是追问一个更有意义的问题：在没有神谕的情况下，那些善于应对的人，包括科学家、工程师、数学家以及治理国家与机构的人，实际上是怎样做的？

若在足够多的领域中追问下去，就会得到一个出人意料的观察，本书正是由此而来：不可验证性的来源千差万别，行之有效的应对却一再收敛到同一小组对策上。

这一观察决定了全书的两层结构，后面各章都以它为基础。

第一层：问题是异质的。「我无法检验它」这句话之下，掩盖着五种结构迥异的处境。有的在原则上就不存在判定程序（不可判定，undecidable）；有的虽有程序，代价却高到无法承受（难解，intractable）；有的是所需的状态对你隐而不见（部分可观测，partially observable）；有的原则上可以验证，只是缺少足够的时间、算力或样本（预算受限，budget-constrained）；还有的是对方在主动挫败你的检验（对抗，adversarial）。将这五种处境混为一谈，是这一领域最常见的错误。第一部的任务，就是把它们逐一区分开来。

第二层：应对是收敛的。无论问题属于哪一种处境，善于应对者所采取的办法总是那么几种：以可测的代理指标（proxy）替代不可测的真实目标；在可检验的局部证明一个界；把代价高昂的检查用在信息量最大之处；引入一个外部的判断者；缩小失败的爆炸半径；为残余的风险给出一个经过校准（calibration）的概率；把检查从事前移到事后；以若干相互独立的判断抵消单点失误。本书将它们归纳为八种对策，并论证它们两两成对，共分四对。第二部进入四个具体场景，让这些对策在各自领域的术语中交错出现；第三部则把每一种对策从具体语境中抽离出来，加以整理和命名，汇成一张跨领域的对照表，这张表是全书最主要的贡献；第四部追问：为什么恰恰是这几种对策。

有一点需要事先说明。这种收敛究竟是一条定律（有某种力量迫使任何有限主体都走向这几种对策），还是仅仅是一个很强的经验模式（我们反复观察到它，却无法证明它必然如此）？就目前而言，我没有证据表明它是定律。本书所提供的，是一个边界清楚的猜想，以及一套能够贯通许多领域的共同词汇，而不是一条定理。第 14 章将专门讨论这一问题。

由此产生了一个无法回避、也不应回避的自指：一本讨论「如何在无法验证时行动」的书，其核心命题本身同样无法验证。因此，它只能践行它所描述的做法：陈述一个经过校准的信念，划定主张的边界，接受反驳，然后继续推进。本书将亲自运用它所研究的方法。倘若它是对的，这种自我示范就不是缺陷，而是唯一站得住脚的写法。

最后留下一个画面，跋将回到这里。一艘船在浓雾中转向。船长有海图、罗盘和对洋流的估算，却没有能够看穿雾气的眼睛。转舵之前，她无法确认前方是否有暗礁。雾不会散去，神谕也不会降临。可是航行不能因此停止。本书想要理解的，不是如何等待雾散，而是一位好的船长在雾中究竟如何掌舵。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实。

1. H. A. Simon (1969).《The Sciences of the Artificial》. MIT Press. [Google Books](https://books.google.com/books?id=hAjtwAEACAAJ) [②④]
   西蒙在此区分自然科学与「人造物的科学」，论证设计是一门以有限理性应对复杂环境的学问，并提出近似分解、层级结构与满意化等思路。它为本书的核心立场提供了底色：行动主体并不追求验明一切，而是在算力与信息受限下设计出够用的应对，正对应本节标注的「理论上被研究过的东西」与「如何在无法验证的世界里生活」。
2. F. H. Knight (1921).《Risk, Uncertainty and Profit》. Houghton Mifflin. [Google Books](https://books.google.com/books?id=XrcJAAAAIAAJ) [②]
   奈特在此划出影响深远的一道界线：「风险」是概率已知、可被度量的不确定，而真正的「不确定」连概率分布都无从给定。他进而把企业利润归因于承担后一类不可度量的不确定。这条区分是本书谈论「不可验证」的概念源头之一，提醒读者把测得出概率的处境与连概率都测不出的处境分开。
3. N. N. Taleb (2007).《The Black Swan: The Impact of the Highly Improbable》. Random House. [Google Books](https://books.google.com/books?id=gWW4SkJjM08C) [②④]
   塔勒布论证，极少数难以预见、影响巨大、事后又被强行解释为可预测的「黑天鹅」事件，主导了历史与市场的走向，而常规的钟形分布统计会系统性地低估它们。本书可读其对预测局限的诊断：当尾部事件无法事先验证时，与其追求精确预报，不如调整自身对意外的暴露方式。
4. W. C. Wimsatt (2007).《Re-Engineering Philosophy for Limited Beings: Piecewise Approximations to Reality》. Harvard University Press. doi:[10.2307/j.ctv1pncnrh](https://doi.org/10.2307/j.ctv1pncnrh) [②③④]
   维姆萨特主张，认知能力有限的存在者不可能掌握完备真理，只能借助偏倚却好用的启发式、稳健性分析与分段近似来逼近实在，而科学正是这样一种逐步生成的工程。这本书几乎是本章主旨的哲学对应物，值得读其对「稳健性」与多重独立路径相互印证的论述，呼应本节标注的三个落足点。
5. J. M. Keynes (1921).《A Treatise on Probability》. Macmillan. [Google Books](https://books.google.com/books?id=NEwWPAAACAAJ) [②]
   凯恩斯把概率理解为命题之间的一种逻辑关系，即给定证据下信念的合理程度，并指出许多概率根本无法用数字精确衡量，甚至彼此不可比较。他还引入「证据权重」来刻画证据多寡本身。该书提供了一个早于现代决策论的视角：当证据稀薄时，量化的信心未必成立，正是不可验证处境的题中之义。
6. L. J. Savage (1954).《The Foundations of Statistics》. Wiley. [Google Books](https://books.google.com/books?id=wqzV4GoYMgEC) [②]
   萨维奇为主观期望效用奠定公理基础：只要一个人的偏好满足若干一致性公理，他的选择就如同在按某个主观概率最大化期望效用。这是把不确定纳入理性计算的标准框架。该书是理解后续争论的基准：唯有先看清它对一致性的要求，才能看懂埃尔斯伯格等人如何指出真实判断对它的偏离。
7. D. Ellsberg (1961).「Risk, Ambiguity, and the Savage Axioms」. Quarterly Journal of Economics, 75(4), 643-669. doi:[10.2307/1884324](https://doi.org/10.2307/1884324) [②]
   埃尔斯伯格用著名的摸球实验表明，人们普遍偏好概率已知的赌局而回避概率不明的赌局，这种「模糊厌恶」系统性地违反萨维奇公理，无法用任何单一主观概率来调和。本文是奈特式区分的实验证据，说明连概率本身都不确定时，理性主体的反应不同于面对纯粹风险，对应本节「理论上被研究过的东西」。
8. H. A. Simon (1955).「A Behavioral Model of Rational Choice」. Quarterly Journal of Economics, 69(1), 99-118. doi:[10.2307/1884852](https://doi.org/10.2307/1884852) [②④]
   西蒙在这篇奠基性论文中提出「有限理性」与「满意化」：受认知与信息限制的主体并不穷举所有选项求最优，而是设定一个抱负水平，找到第一个达标的方案便停手。这是本书反复借用的母题，说明在无法完全验证时，「够好即止」往往是理性的形态而非失败。
9. H. A. Simon (1947).《Administrative Behavior: A Study of Decision-Making Processes in Administrative Organization》. Macmillan. [Google Books](https://books.google.com/books?id=lfjsAAAAMAAJ) [②④]
   西蒙在此把组织理解为放大个体有限理性的决策结构，论证组织通过设定前提、划分职责与建立惯例，使成员在不完全信息下仍能做出可接受的选择。本书把有限理性从个人推广到机构层面，对应本书第二部对「现场」中应对机制的关注：制度本身就是一种集体的应对装置。
10. A. Tversky & D. Kahneman (1974).「Judgment under Uncertainty: Heuristics and Biases」. Science, 185(4157), 1124-1131. doi:[10.1126/science.185.4157.1124](https://doi.org/10.1126/science.185.4157.1124) [②]
   特沃斯基与卡尼曼指出，人在不确定下依赖代表性、可得性与锚定等少数启发式来估计概率，这些捷径通常有效，却会导致可预测的系统性偏差。本文开启了「启发式与偏差」研究纲领，是理解人类判断在何处可靠、何处失灵的起点，对应本节「理论上被研究过的东西」。
11. D. Kahneman & A. Tversky (1979).「Prospect Theory: An Analysis of Decision under Risk」. Econometrica, 47(2), 263-291. doi:[10.2307/1914185](https://doi.org/10.2307/1914185) [②④]
   前景理论用一个相对参照点的价值函数与对概率的非线性加权，刻画真实选择如何偏离期望效用：人们对损失比对等量收益更敏感，并高估小概率、低估中高概率。它是对萨维奇式规范理论的描述性修正，本书可读其对「人实际如何在风险下取舍」的精细刻画。
12. D. Kahneman (2011).《Thinking, Fast and Slow》. Farrar, Straus and Giroux. [Google Books](https://books.google.com/books?id=ZuKTvERuPG8C) [②④]
   卡尼曼以「系统一」（快速、直觉）与「系统二」（缓慢、费力）的双过程框架，综述了数十年关于判断偏差与决策的研究。该书是这一研究传统面向读者的总览，适合用来建立对认知局限的整体图景，理解为何即便专家也需要外部纠错机制，呼应本节「如何在无法验证的世界里生活」。
13. G. Gigerenzer & D. G. Goldstein (1996).「Reasoning the Fast and Frugal Way: Models of Bounded Rationality」. Psychological Review, 103(4), 650-669. doi:[10.1037/0033-295x.103.4.650](https://doi.org/10.1037/0033-295x.103.4.650) [②④]
   吉仁泽与戈尔茨坦提出「快速节俭」启发式，论证只用少量线索、按序停止搜索的简单规则，在现实环境中常能逼近甚至超越复杂统计模型的表现。这与卡尼曼传统的「启发式即偏差」形成对照：本书可读其对「简单何以有效」的辩护，理解有限理性也可以是一种生态上的优势。
14. G. Gigerenzer, P. M. Todd & the ABC Research Group (1999).《Simple Heuristics That Make Us Smart》. Oxford University Press. [Google Books](https://books.google.com/books?id=4ObhBwAAQBAJ) [②④]
   这本论文集系统铺陈「适应性工具箱」的纲领：心智配备一组针对特定环境的简单启发式，其有效性来自与环境结构的契合，即「生态理性」。它把前一篇的单点论证扩展为完整研究计划，本书可读其大量实证案例，看简单规则如何在信息不足时稳健地做出好判断。
15. F. A. Hayek (1945).「The Use of Knowledge in Society」. American Economic Review, 35(4), 519-530. [链接](https://www.jstor.org/stable/1809376) [②④]
   哈耶克论证，社会所需的知识本质上是分散的、与具体时空相关的，无法汇总到任何一个中央计划者手中，而价格机制恰恰是把这些分散信息协调起来的去中心装置。本文重要在于揭示一种不可验证的根源：相关信息从未被任何单一主体完整掌握，对应本书所说的「部分可观测」处境。
16. M. Polanyi (1958).《Personal Knowledge: Towards a Post-Critical Philosophy》. Routledge & Kegan Paul. [Google Books](https://books.google.com/books?id=QPPIBQAAQBAJ) [①③④]
   波兰尼论证，一切认识都含有不可言传的「默会知识」与认识者的个人投入，纯客观、可完全形式化的知识是一种幻象。该书重要在于解释科学家的判断为何无法被规则完全替代，对应本节三个落足点，呼应本书对专家直觉与亲历判断的关注。
17. P. E. Meehl (1954).《Clinical versus Statistical Prediction: A Theoretical Analysis and a Review of the Evidence》. University of Minnesota Press. doi:[10.1037/11281-000](https://doi.org/10.1037/11281-000) [①④]
   米尔综述大量研究后得出一个令专家不安的结论：简单的统计或精算式预测，在准确度上往往不逊于甚至超过临床专家的直觉判断。该书是「把判断外包给可核查的规则」这一对策的经典证据，提示读者专家的自信与其实际准确度未必相符，对应本节「历史上科学家的判断」。
18. D. A. Schön (1983).《The Reflective Practitioner: How Professionals Think in Action》. Basic Books. [Google Books](https://books.google.com/books?id=E85qAAAAMAAJ) [①④]
   舍恩提出「行动中的反思」，论证专业人士面对独特而模糊的实践情境时，靠的不是套用既定理论，而是在行动中即时地与情境对话、不断重构问题。该书重要在于刻画了一种无法事先验证的专业能力，与米尔的统计预测形成张力，对应本书对实践者如何在雾中操舵的关心。
19. G. A. Klein (1998).《Sources of Power: How People Make Decisions》. MIT Press. [Google Books](https://books.google.com/books?id=OI39nQEACAAJ) [①④]
   克莱因通过对消防员、护士等真实专家的现场研究，提出「识别启动决策」模型：富有经验者在时间压力下并不比较选项，而是凭模式识别直接生成一个可行方案再做心理模拟。该书是自然主义决策的代表作，说明专家直觉在何种条件下可靠，为本书对专业判断的讨论提供经验支撑。
20. P. E. Tetlock (2005).《Expert Political Judgment: How Good Is It? How Can We Know?》. Princeton University Press. [Google Books](https://books.google.com/books?id=NAeCzQEACAAJ) [①④]
   泰特洛克历经多年追踪政治与经济专家的预测，发现其平均准确度往往不如简单的外推，且认知风格比专业本身更能解释优劣：思路驳杂、自我怀疑的「狐狸」胜过执守单一大理论的「刺猬」。该书重要在于用可核查的记分把专家判断真正置于检验之下，对应本节「历史上科学家的判断」。
21. P. E. Tetlock & D. Gardner (2015).《Superforecasting: The Art and Science of Prediction》. Crown. [Google Books](https://books.google.com/books?id=hC_qBQAAQBAJ) [①④]
   本书是泰特洛克预测锦标赛研究的延续，刻画出一类「超级预测者」：他们把大问题拆解、给出可计分的概率、依新证据频繁微调，并以团队互校来提升准确度。它把预测从天赋还原为可习得的实践，正对应本书所倡的事后校准与多重独立判断，呼应本节「如何在无法验证的世界里生活」。
22. N. N. Taleb (2001).《Fooled by Randomness: The Hidden Role of Chance in Life and in the Markets》. Texere. [Google Books](https://books.google.com/books?id=nnWxAAAAIAAJ) [②④]
   塔勒布论证人们惯于把随机产生的结果误读为技能或必然，尤其在金融市场中把幸存者当成高手，从而低估了运气与噪声的作用。本书可读其对「事后归因」陷阱的剖析，提醒读者在无法验证因果时，成功的事实本身并不证明判断正确。
23. N. N. Taleb (2012).《Antifragile: Things That Gain from Disorder》. Random House. [Google Books](https://books.google.com/books?id=5fqbz_qGi0AC) [④]
   塔勒布提出「反脆弱」概念：有些系统不仅能承受波动，还能从无序与冲击中获益，与之相对的是脆弱与仅仅强韧。他主张在无法预测的世界里，应通过保留可选项、限制下行风险来主动从意外中受益。该书直接关联本书所谈的「缩小失败的爆炸半径」，对应本节「如何在无法验证的世界里生活」。
24. C. E. Lindblom (1959).「The Science of "Muddling Through"」. Public Administration Review, 19(2), 79-88. doi:[10.2307/973677](https://doi.org/10.2307/973677) [④]
   林德布洛姆论证现实中的公共政策并非自上而下的理性全局优化，而是「渐进主义」：在现状附近做有限的小幅调整、边走边比较、与已有手段挂钩。本文重要在于把「步步为营、随时纠偏」正名为一种应对复杂的合理策略，对应本书把检查从事前挪到事后、用小步迭代控制风险的思路。
25. K. R. Popper (1959).《The Logic of Scientific Discovery》. Hutchinson. [Google Books](https://books.google.com/books?id=iucRkAEACAAJ) [③]
   波普尔系统提出证伪主义：科学理论无法被经验证实，只能被经验否证，因此可证伪性才是划分科学与非科学的标准。该书是本书主旨的哲学源头之一，正面回应「凡事可验证」的幻想，说明即便是科学也并非靠验证为真，而是靠经得起反驳来前进，对应本节「科学如何进展」。
26. T. S. Kuhn (1962).《The Structure of Scientific Revolutions》. University of Chicago Press. [Google Books](https://books.google.com/books?id=3eP5Y_OOuzwC) [①③]
   库恩提出，科学并非线性累积，而是在「常规科学」与「科学革命」之间交替：研究在某一范式下解谜，待反常累积到危机，才会发生范式转换。他还指出竞争范式之间存在不可通约性。该书重要在于揭示科学进步中判断与共同体的作用，而非纯粹的逻辑验证，对应本节「历史上科学家的判断」与「科学如何进展」。
27. W. V. Quine (1951).「Two Dogmas of Empiricism」. The Philosophical Review, 60(1), 20-43. doi:[10.2307/2181906](https://doi.org/10.2307/2181906) [③]
   蒯因攻击逻辑经验主义的两条教条，即分析与综合命题的截然二分，以及每个命题可单独还原为经验。他主张信念以整体方式面对经验法庭，任何陈述都可在调整别处的前提下被保留。本文是「证据不充分决定理论」的经典论证，说明单凭观察无法唯一地裁定理论，对应本节「科学如何进展」。
28. P. Duhem (1954).《The Aim and Structure of Physical Theory》. Princeton University Press. doi:[10.1515/9780691233857](https://doi.org/10.1515/9780691233857) [③]
   迪昂论证物理学的实验从来不是对单一假说的检验，而是对整套理论与辅助假设的检验，因此一个反例无法明确指出错在何处。这就是后来与蒯因并称的「迪昂蒯因论题」的源头。该书重要在于从科学实践内部说明判决性实验的局限，是理解科学为何无法靠单点验证为真的关键，对应本节「科学如何进展」。
29. I. Hacking (1983).《Representing and Intervening: Introductory Topics in the Philosophy of Natural Science》. Cambridge University Press. doi:[10.1017/cbo9780511814563](https://doi.org/10.1017/cbo9780511814563) [③]
   哈金把科学哲学的重心从「表征」即理论与真理，转向「介入」即实验与操作，主张当我们能稳定地操纵某种实体去干预世界时，便有理由相信它实在，这就是著名的实验实在论。该书重要在于提示验证并不只是被动观察，而是动手介入，呼应本书把行动而非验证置于核心的视角，对应本节「科学如何进展」。
