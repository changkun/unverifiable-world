# 第 14 章　是定理，还是模式？

> **论点**：这是全书必须正面回答的核心问题。跨领域的收敛究竟是一条定律（有某种力量迫使任何面对不可验证局面的有限主体走向这套对策），还是仅仅是一个很强的经验模式（我们反复观察到它，却无法证明它必然如此，而且选择效应或许就足以解释这种「押韵」）？

行文至此，本书必须对自己有所交代。本章要把贯穿全书的那个问题明确地提出来。

这种跨领域的收敛是一条定律吗？倘若如此，就意味着有某种力量迫使任何面对不可验证（unverifiable）局面的有限主体（bounded actor）必然走向这套对策。抑或它只是一个很强的经验模式？倘若如此，就意味着我们虽然反复观察到它，却未能证明它必然如此；而且，仅凭选择效应（selection effect），或许就足以解释这种「押韵」。

我将尽可能把双方的理由都陈述到最强的程度，包括不利于我的一方。如果本章有所偏向，也应当偏向怀疑。

## 支持「定律」的理由

第一条理由来自上一章的杠杆分解。如果八种对策确实占满了风险分解式中所有可供干预的位置，收敛就不是巧合，而是结构使然：任何善于应对的主体迟早都会重新发现它们，因为别无选择。这一论证一旦成立，分量极重。

第二条理由是独立的重复发现。默顿在科学社会学中研究过「多重发现」（multiple discovery）现象：同一个想法，常常由彼此不知情的人几乎同时各自得出<sup class="cite"><a href="#ref-12">12</a></sup>。微积分有牛顿与莱布尼茨，自然选择有达尔文与华莱士；贝尔与格雷甚至是在同一天带着电话走进专利局的。此类例子在科学史上屡见不鲜，多到难以归于巧合。本书的八种对策同样在密码学、统计学、数论、组织理论与安全工程中一再被重新发明，而这些领域在当时并无多少往来。一种事物若总是被人各自独立地发现，它就更像是必然的产物，而不像是相互借用的结果。

第三条理由来自科学内部确凿的先例。物理学中的重整化群（renormalization group）与普适类（universality class）表明，结构迥异的系统在临界点附近会收敛到完全相同的行为；而在那里，这确实是一条定理<sup class="cite"><a href="#ref-17">17</a></sup><sup class="cite"><a href="#ref-18">18</a></sup>。有一个具体而引人注目的例子：液体在临界点附近的行为与磁体在居里点附近的行为，由同一组「临界指数」（critical exponents）刻画。分子与磁矩毫不相干，却落入了同一个普适类，原因在于决定临界行为的是对称性、维度这类粗粒度的特征，而不是微观细节。维姆萨特的稳健性分析（robustness analysis）认为，一个能够沿多条相互独立的路径反复得出的结论，更有可能为真<sup class="cite"><a href="#ref-20">20</a></sup>。与此相通，惠威尔 1840 年提出的「归纳的协同」（consilience of inductions）<sup class="cite"><a href="#ref-11">11</a></sup>，以及维格纳那篇论「数学不可思议的有效性」的文章<sup class="cite"><a href="#ref-22">22</a></sup>，讨论的都是跨领域的汇合所带来的可信度。收敛向来是科学判断某种东西「真实存在」的古老信号之一。

## 支持「模式」或更弱结论的理由

下面转向不利于我的一方。在我看来，这一方的分量并不比前一方轻。

最具破坏力的反驳是：这些领域并不像表面上那样彼此独立。它们共享同一个数学基础，概率论、最优化与信息论深植于每一个领域的根基之中；它们共享同一种人类认知，毕竟这些学科都出自同一种大脑；它们还相互借鉴、彼此引用，从来不是封闭隔绝的：香农的信息论几乎渗入了所有领域，决策论的语言也扩散到各处。倘若收敛仅仅是因为各领域都取材于同一个数学工具箱，都受同一种心智的塑造，又始终在相互模仿，那么「独立的重复发现」这一理由就要大打折扣。所谓收敛，或许只是共同起源的回声。

第二，杠杆分解很可能是一个事后搭建的框架。它是否只是足够灵活，以至于能够容纳许多不同的对策组合？上一章的那张表已经暴露了这一点：冗余被归入降低联合失败概率一栏，却又近似于一种特殊的筛查。归类上的重叠说明，这把尺子还不够刚硬。丹尼特提出过一个关键问题：一个模式在什么条件下才算是真实的，而不是被强加的<sup class="cite"><a href="#ref-13">13</a></sup>？他给出的判据是预测力与压缩力：真实的模式能够让人预言新的东西。迄今为止，我的框架主要是在整理已知的对策，尚未预言出一种前所未见、后来又得到证实的新对策。这是它尚未通过的检验。

第三是选择效应。我是带着「寻找收敛」的眼光考察这些领域的，因此很可能在不知不觉间滤除了不相契合的领域与反例，只保留了彼此押韵的部分。可重复性危机（replication crisis）是最响亮的警示：看似极其稳健的经验模式，可能不过是系统性偏倚的产物<sup class="cite"><a href="#ref-29">29</a></sup><sup class="cite"><a href="#ref-30">30</a></sup>。我没有理由认为自己能够免于这种偏倚。

第四，即便收敛是真实的，它也未必指向一条深层的定律。劳丹的悲观元归纳（pessimistic meta-induction）提醒我们，历史上一个又一个成功的理论后来都被推翻了<sup class="cite"><a href="#ref-6">6</a></sup>。收敛于一个模式，并不等于收敛于真理。卡特赖特认为，基础定律并不如实地描述世界<sup class="cite"><a href="#ref-14">14</a></sup>；安德森的「多者异也」（more is different）则指出，更高的层次有其自身的规律<sup class="cite"><a href="#ref-15">15</a></sup>。本书所说的收敛，或许只是「特殊科学」（special sciences）尺度上的一种规律性，谈不上基本定律。沃勒尔的结构实在论（structural realism）提供了一种折中<sup class="cite"><a href="#ref-7">7</a></sup>：真正得以留存的，或许是那个结构（也就是这些杠杆），即便我为它所作的阐释是错误的。

## 定论的条件

要真正了结这一问题，需要我目前无法提供的东西：一个关于「有限主体加不可验证系统」的形式模型，以及一条定理，证明在该模型之下，最优的（或唯一的）策略恰好就是这几根杠杆。据我所知，这样的模型尚不存在。与之最接近的一条真正的定理是无免费午餐（no free lunch）定理<sup class="cite"><a href="#ref-24">24</a></sup>，而它指向的恰是相反的方向：没有任何一种方法处处占优。在这样的模型与定理出现之前，这一问题仍然悬而未决，我也无意假装它已有定论。

因此，我应当如实说明本书所提供的是什么：一个猜想，一个有力、有用、边界清楚的猜想，以及一套能够贯通许多领域的共同词汇。它不是定理。这也是本书一路所倡导的姿态：给出一个经过校准的信念（calibrated belief），而不作非此即彼的裁决。

## 一本无法验证自身的书

至此，自序言起便潜伏在全书之下的那个问题浮出了水面：一本讨论「如何在无法验证时行动」的书，无法验证它自己的核心命题。

这听起来像是一种尴尬的自指（self-reference），却是本书最坦诚的时刻。面对一个连自己都无法验证的核心论断，它别无选择，只能践行它通篇所描述的做法。它陈述一个经过校准的信念（我认为这种收敛是真实的，但无法给出证明）。它划定主张的边界（这是猜想，而不是定理）。它公开接受反驳：只要找到一个不发生收敛的领域，或者一个打破这一分解的反例，那便是它的黑天鹅。然后，它照旧继续论述，照旧把这套词汇交到读者手中，因为这套词汇是有用的，即便尚未得到证实。

换言之，本书把它所讨论的对策用在了自己身上。它运用了代理替换，以「展示并组织收敛」替代「证明收敛」；运用了校准，为自己的把握程度定价；还运用了证伪式的留痕，把可以被推翻的断言白纸黑字地写下来。自指的系统无法在内部完全证成自身，对于这种处境，我们早该习以为常<sup class="cite"><a href="#ref-26">26</a></sup><sup class="cite"><a href="#ref-27">27</a></sup><sup class="cite"><a href="#ref-25">25</a></sup>。然而，无法在内部自证，并不意味着不能行动。倘若本书的论点成立，它「以自己所描述的方式写成自己」这一事实便不是缺陷，反而构成一份微弱却贴切的旁证。

于是只剩下最后一个问题。如果验证通常无法获得，连本书也只能给出一个未经证实的信念，那么，我们平日称为「知识」的大量东西，究竟是什么？下一章将转向认识论，全书的论证也将在那里收束。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实。

1. T. S. Kuhn (1962).《The Structure of Scientific Revolutions》. University of Chicago Press. [Google Books](https://books.google.com/books?id=3eP5Y_OOuzwC) [③①]
   库恩指出科学并非线性累积，而是在常规科学（在既有范式内解谜）与科学革命（范式更替）之间交替推进，新旧范式之间存在「不可通约性」。此书初版 1962，最初亦作为《国际统一科学百科全书》的单行本刊出。它是理解「科学如何进展」的奠基文本，也提示本章：跨域收敛究竟是被同一范式塑造，还是独立逼出的，正是本书要拷问的问题。

2. K. R. Popper (1959).《The Logic of Scientific Discovery》. Hutchinson. [Google Books](https://books.google.com/books?id=iucRkAEACAAJ) [③①]
   波普尔系统提出证伪主义：科学理论无法被经验证实，只能被否证，可证伪性因而成为科学与非科学的分界，也成为科学进展的判据。此书为德文原著《Logik der Forschung》（1934，版权页标 1935）的英文增订本，1959 年由伦敦 Hutchinson 出版。它是 Kuhn、Lakatos、Feyerabend 后续论辩的共同起点，也为本书「公开邀请反驳、写下可被推翻的断言」这一姿态提供了根据。

3. I. Lakatos (1970).「Falsification and the Methodology of Scientific Research Programmes」. 收于 I. Lakatos & A. Musgrave (编)《Criticism and the Growth of Knowledge》. Cambridge University Press. doi:[10.1017/cbo9781139171434.009](https://doi.org/10.1017/cbo9781139171434.009) [③]
   拉卡托斯调和波普尔与库恩，提出评价单位不是单个理论而是「研究纲领」：纲领有一个被保护的硬核与可调整的保护带，若它能持续预言并兑现新事实，便是进步的，否则就是退化的。此文源自 1965 年伦敦 Bedford College 的学术讨论会，论文集 1970 年由剑桥大学出版社出版。其「进步／退化」判据，恰好为本章「定理还是模式」之争提供了一个可操作的方法论框架。

4. P. Feyerabend (1975).《Against Method: Outline of an Anarchistic Theory of Knowledge》. New Left Books. [Google Books](https://books.google.com/books?id=XL_GAAAAIAAJ) [③①]
   费耶阿本德以「认识论的无政府主义」反对任何普适、固定的科学方法，主张在实际科学史中「怎么都行」，并指出重大突破往往恰是因为打破了既定方法论规则。此书 1975 年由伦敦 New Left Books（即后来的 Verso）初版。它构成「跨域收敛是否被某条方法论定理逼出」的最强反方立场：若根本没有统一方法，收敛就更难被解释为必然。

5. L. Laudan (1977).《Progress and Its Problems: Towards a Theory of Scientific Growth》. University of California Press. [Google Books](https://books.google.com/books?id=TMuXQgAACAAJ) [③]
   劳丹主张衡量科学进步的标尺不是逼近真理，而是「解题效力」：一套理论解决了多少经验问题、又制造了多少概念难题。这把对科学进步的判断从形而上学的真理负担中解脱出来，落到可比较的功能指标上。它正面切合「科学如何进展」，也支持本章的克制立场，收敛到一个有用的模式，未必等于收敛到真理。

6. L. Laudan (1981).「A Confutation of Convergent Realism」. Philosophy of Science, 48(1). doi:[10.1086/288975](https://doi.org/10.1086/288975) [③②]
   劳丹以一份历史清单提出「悲观元归纳」：历史上许多曾经成功、能做出准确预言的理论，其核心词项后来被判定根本不指称任何东西（如以太、燃素），因此经验上的成功并不可靠地担保理论为真。此文载于卷 48，第 19 至 49 页。它直接质疑「跨域收敛指向真理」这一定理性主张，是本章最关键的反方文献之一。

7. J. Worrall (1989).「Structural Realism: The Best of Both Worlds?」. Dialectica, 43(1-2). doi:[10.1111/j.1746-8361.1989.tb00933.x](https://doi.org/10.1111/j.1746-8361.1989.tb00933.x) [③②]
   沃勒尔提出结构实在论，试图在「无奇迹论证」与「悲观元归纳」之间取中：理论更替时被保留下来的不是关于本体的描述，而是其数学结构（如菲涅耳的光学方程在以太被抛弃后仍然成立）。此文载于卷 43 第 1 至 2 期，第 99 至 124 页。它为本章给出一种折中读法，即便我套在杠杆外面的说辞是错的，真正被保留的也许正是那个结构本身。

8. I. Hacking (1983).《Representing and Intervening: Introductory Topics in the Philosophy of Natural Science》. Cambridge University Press. doi:[10.1017/cbo9780511814563](https://doi.org/10.1017/cbo9780511814563) [③②]
   哈金把科学哲学的重心从「表征」（理论如何描述世界）转向「介入」（实验如何操纵世界），提出一种实验实在论：若我们能稳定地用某个实体去干预、制造别的现象（能喷它，它就是真的），就有理由相信它存在。此书 1983 年由剑桥大学出版社出版。它为本章提供了「收敛模式从何而来」的另一条解释，即收敛可能源于共同的实验实践，而非理论上的必然。

9. W. V. O. Quine (1951).「Two Dogmas of Empiricism」. The Philosophical Review, 60(1). doi:[10.2307/2181906](https://doi.org/10.2307/2181906) [②③]
   蒯因攻击逻辑经验主义的两条教条：分析与综合的截然二分，以及还原论。他主张知识是一张面对经验整体受检的「信念之网」，任何单个命题都无法被孤立地证实或证伪。此文载于卷 60 第 1 期，第 20 至 43 页。其确证整体论是本书核心处境的哲学根基，没有哪个论断能被单独拎出来彻底验证。

10. M. Polanyi (1958).《Personal Knowledge: Towards a Post-Critical Philosophy》. University of Chicago Press. [Google Books](https://books.google.com/books?id=QPPIBQAAQBAJ) [①④]
   波兰尼提出「默会知识」：我们知道的远多于我们能言说的，一切明言的知识都依托一层无法完全形式化的个人判断与技能。科学认知因此离不开科学家的个人参与和投入。此书 1958 年由芝加哥大学出版社出版。它直接关乎本书落点，当验证无法穷尽时，科学家如何凭判断作出经过校准的信念并据以行动。

11. W. Whewell (1840).《The Philosophy of the Inductive Sciences, Founded Upon Their History》. John W. Parker. [Google Books](https://books.google.com/books?id=T0hmAAAAcAAJ) [③②]
   惠威尔在此提出「归纳的协同」（consilience of inductions）：当一个由某类事实归纳出的理论，竟也能解释另一类原本无关的事实时，这种意外的汇合是理论为真的有力标志。此书为两卷本，1840 年由伦敦 John W. Parker 出版。它是「跨域收敛即可信」这一思路最早的方法论表述，为本章支持「定律」一方提供了历史源头。

12. R. K. Merton (1961).「Singletons and Multiples in Scientific Discovery: A Chapter in the Sociology of Science」. Proceedings of the American Philosophical Society, 105(5). [链接](https://www.jstor.org/stable/985546) [①③]
   默顿系统考察科学史上的「多重发现」现象：同一发现常被互不知情的人几乎同时各自做出，他据此论证这类多重发现并非例外，而是科学发现的常态，发现更多取决于知识积累的状态而非个别天才。此文载于卷 105 第 5 期，第 470 至 486 页。它是「收敛是一种强经验模式」的关键社会学证据，本章正是借它来掂量独立重复发现的分量。

13. D. C. Dennett (1991).「Real Patterns」. The Journal of Philosophy, 88(1). doi:[10.2307/2027085](https://doi.org/10.2307/2027085) [②③]
   丹尼特问：一个模式何时算「真实」，而非被观察者强加？他给出的判据是压缩与预测，若把数据描述为某个模式能带来真正的信息压缩、并支持对新情形的预言，这个模式就是实在的。此文载于卷 88 第 1 期，第 27 至 51 页。这正是本章「定理还是强经验模式」的核心概念工具，本章也据此承认：杠杆分解尚未预言出一种前所未见、后被证实的新对策，是它仍待通过的考验。

14. N. Cartwright (1983).《How the Laws of Physics Lie》. Oxford University Press. doi:[10.1093/0198247044.001.0001](https://doi.org/10.1093/0198247044.001.0001) [②③]
   卡特赖特主张物理学的基础定律之所以普适，恰恰因为它们并不如实描述真实世界，越是基本的定律越要靠大量理想化与近似才能套上现象，真正描述具体系统的是局部的、唯象的定律。此书 1983 年由 Clarendon Press／牛津大学出版社初版。它从根上质疑：本章所见的收敛背后，是否真的站着一条「定理」，还是只是模型层面的整齐。

15. P. W. Anderson (1972).「More Is Different」. Science, 177(4047). doi:[10.1126/science.177.4047.393](https://doi.org/10.1126/science.177.4047.393) [②③]
   安德森反对还原论的「构成主义」推论：即便万物都由基本粒子按基本定律构成，也不意味着从这些定律就能推出高层级的行为。每提升一个尺度，都会涌现出全新的、自成体系的规律。此文载于卷 177 第 4047 期，第 393 至 396 页（1972 年 8 月 4 日）。它支持本章一种弱化读法，本书的收敛或许只是某个「特殊科学」尺度上的规律性，而非基本定律。

16. H. A. Simon (1962).「The Architecture of Complexity」. Proceedings of the American Philosophical Society, 106(6). [链接](https://www.jstor.org/stable/985254) [②③]
   西蒙论证：能稳定演化、长存的复杂系统，往往呈层级结构且「近可分解」，即子系统内部的交互远强于子系统之间，他用钟表匠的寓言说明带稳定中间件的系统更易被组装出来。此文载于卷 106 第 6 期，第 467 至 482 页。它给跨域收敛提供了又一种「共同起源」式解释，不同领域之所以撞见相似结构，可能因为复杂系统本就受同一组架构约束。

17. K. G. Wilson (1979).「Problems in Physics with Many Scales of Length」. Scientific American, 241(2). doi:[10.1038/scientificamerican0879-158](https://doi.org/10.1038/scientificamerican0879-158) [②③]
   威尔逊面向一般读者讲解重整化群：当一个系统横跨许多长度尺度（如临界点附近），可以逐级「粗粒化」来处理，由此解释了为何微观细节天差地别的系统会落入同一「普适类」、表现出完全相同的临界行为。此文载于卷 241 第 2 期，第 158 至 179 页（1979 年 8 月）。它是本章支持「定律」一方最硬的物理学例证，因为在那里，不同系统收敛到同一行为是一条可证的定理。

18. R. W. Batterman (2002).《The Devil in the Details: Asymptotic Reasoning in Explanation, Reduction, and Emergence》. Oxford University Press. doi:[10.1093/0195146476.001.0001](https://doi.org/10.1093/0195146476.001.0001) [②③]
   巴特曼分析物理学中的「渐近推理」：许多解释（尤其普适性现象）依赖于取某个极限（如尺度趋于零或无穷）时浮现的奇异行为，这类解释无法被简单还原到底层理论，恰恰栖身于细节消失之处。此书由牛津大学出版社出版（封面年份多标 2002，部分书评依出版前目录作 2001）。它为本章的「定律」一方提供哲学剖析：跨域收敛之所以可能成立，机制或许正在于这种与微观细节无关的渐近普适性。

19. R. Levins (1968).《Evolution in Changing Environments: Some Theoretical Explorations》. Princeton University Press. doi:[10.1515/9780691209418](https://doi.org/10.1515/9780691209418) [②③]
   莱文斯以一系列理论模型探讨生物如何在波动、不确定的环境中演化，引入「适应度集」等工具分析在多变环境下何种策略最优，并贯穿一种以多个简化模型逼近复杂现实的建模风格。此书 1968 年由普林斯顿大学出版社出版（Monographs in Population Biology 第 2 号）。它代表的多模型、近似式建模思路，是 Wimsatt 稳健性论证的生物学先声，呼应本章对「多条独立路径汇合」的重视。

20. W. C. Wimsatt (1981).「Robustness, Reliability, and Overdetermination」. 收于 M. B. Brewer & B. E. Collins (编)《Scientific Inquiry and the Social Sciences》. Jossey-Bass. [Google Books](https://books.google.com/books?id=KEPlAQAACAAJ) [③②]
   维姆萨特系统阐述「稳健性分析」：若一个结论能由多条彼此独立的探测、推导或测量路径反复抵达，那它更可能是真的，而非某一手段的人为产物，这种「多重决定」是分辨真实事物与假象的关键。此文收于该论文集，第 125 至 163 页。它是本章「跨域收敛为何可信」的方法论核心，也正是支持「定律」一方所倚重的论证。

21. W. C. Wimsatt (2007).《Re-Engineering Philosophy for Limited Beings: Piecewise Approximations to Reality》. Harvard University Press. doi:[10.2307/j.ctv1pncnrh](https://doi.org/10.2307/j.ctv1pncnrh) [③④]
   维姆萨特主张把科学哲学改造成适合「有限存在者」的工具：真实的认知者算力有限、易错、受困于自身视角，因而依赖启发式、近似与分片的逼近来一点点接近现实，而非追求理想化的完备理性。此书 2007 年由哈佛大学出版社出版。它与本书的主旨高度同频，正面回答「有限主体如何在无法验证的世界里推进科学、并据此生活」。

22. E. P. Wigner (1960).「The Unreasonable Effectiveness of Mathematics in the Natural Sciences」. Communications on Pure and Applied Mathematics, 13(1). doi:[10.1002/cpa.3160130102](https://doi.org/10.1002/cpa.3160130102) [②③]
   维格纳惊叹于一个事实：为纯粹内在动机发展出的数学，竟一再精确地刻画自然规律，他称这种契合为一份「我们既不理解也不配享有的奇妙馈赠」。此文载于卷 13 第 1 期，第 1 至 14 页，源自 1959 年 Courant 讲座。它是「定理还是模式」之问的原型，数学的跨域有效到底是必然，还是一桩我们尚无法解释的巨大押韵。

23. H. Putnam (1975).《Mathematics, Matter and Method: Philosophical Papers, Volume 1》. Cambridge University Press. [Google Books](https://books.google.com/books?id=HjI9AAAAIAAJ) [②③]
   这部论文集收录普特南早期的数学哲学与科学实在论文章，其中「What is Mathematical Truth?」一文给出「无奇迹论证」的经典表述：实在论是唯一不把科学的成功当作奇迹的哲学，若理论中的实体不存在，其预言的成功便无从解释。此文见第 60 至 78 页。它是本章「定律」一方的正面武器，恰与劳丹的悲观元归纳针锋相对。

24. D. H. Wolpert & W. G. Macready (1997).「No Free Lunch Theorems for Optimization」. IEEE Transactions on Evolutionary Computation, 1(1). doi:[10.1109/4235.585893](https://doi.org/10.1109/4235.585893) [②③]
   沃尔珀特与麦克里迪证明「无免费午餐」定理：在所有可能的目标函数上取平均，任何两个优化算法的期望表现都完全相同，因而不存在普适占优的算法，任何算法的优势都靠对问题结构的特定假设换来。此文载于卷 1 第 1 期，第 67 至 82 页。它是本章引以为对照的一条真定理，且偏偏指向反方，提醒我们「最优策略唯一」式的结论需要极强的前提。

25. D. R. Hofstadter (1979).《Gödel, Escher, Bach: An Eternal Golden Braid》. Basic Books. [Google Books](https://books.google.com/books?id=yeu2AAAAIAAJ) [②④]
   霍夫斯塔特借哥德尔的不完备性、埃舍尔的视觉悖论与巴赫的卡农，编织出一个共同母题：自指与「奇异环」，并由此探讨心智与意义如何从无意义的形式层级中涌现。此书 1979 年由 Basic Books 出版，获普利策非虚构奖。它把自指与递归收束讲成一门艺术，呼应本章那一刻，一本书无法在内部自证，却照样「以它所描述的方式」写自己。

26. E. Nagel & J. R. Newman (1958).《Gödel's Proof》. New York University Press. [Google Books](https://books.google.com/books?id=lW4EzQEACAAJ) [②④]
   纳格尔与纽曼用尽量少的技术细节，向一般读者讲清哥德尔第一与第二不完备性定理的证明思路：任何足够强的一致形式系统，都存在它无法证明的真命题，且无法在系统内部证明自身的一致性。此书 1958 年由纽约大学出版社出版。它为本章关于「形式系统的内禀界限」与「自指系统无法内部自证」的论述，提供了可读而准确的依据。

27. G. J. Chaitin (1982).「Gödel's Theorem and Information」. International Journal of Theoretical Physics, 21(12). doi:[10.1007/bf02084159](https://doi.org/10.1007/bf02084159) [②③]
   蔡廷用算法信息论重新解读不完备性：一个形式系统的公理蕴含的信息量是有限的，因此无法证明任何复杂度超过该信息量的命题（如某串足够长的随机比特确属随机），不完备性由此被还原为一种信息上限。此文载于卷 21 第 12 期，第 941 至 954 页。它从信息的角度坐实了形式系统的内禀界限，为「无法验证的世界」提供又一层形式根据。

28. M. Mitchell (2009).《Complexity: A Guided Tour》. Oxford University Press. doi:[10.1093/oso/9780195124415.001.0001](https://doi.org/10.1093/oso/9780195124415.001.0001) [②③]
   米切尔为一般读者梳理复杂系统科学：从信息、计算、演化到网络，介绍涌现、自组织等在生物、计算、社会系统中反复出现的共通主题，并坦诚这一领域尚缺统一理论。此书 2009 年由牛津大学出版社出版。它为本章呈现跨域共通模式的研究现状提供了可靠的入门地图，也提示这些模式至今仍多是经验观察而非定理。

29. J. P. A. Ioannidis (2005).「Why Most Published Research Findings Are False」. PLoS Medicine, 2(8). doi:[10.1371/journal.pmed.0020124](https://doi.org/10.1371/journal.pmed.0020124) [③④]
   约阿尼迪斯用一个统计模型论证：在小样本、小效应、研究自由度大、利益与偏倚普遍存在的条件下，一个已发表「阳性」结论为真的概率往往低于五成。此文载于卷 2 第 8 期，e124（2005 年 8 月）。它是元科学的经典警钟，提醒本章，看似稳健的经验模式可能只是系统性偏倚的产物，作者没有理由假设自己对此免疫。

30. Open Science Collaboration (2015).「Estimating the Reproducibility of Psychological Science」. Science, 349(6251). doi:[10.1126/science.aac4716](https://doi.org/10.1126/science.aac4716) [③④]
   开放科学合作组织协同上百名研究者，重复了一百项已发表的心理学研究，结果只有约三分之一的重复实验得到与原研究方向一致且显著的效应，且重复效应量普遍小于原始报告。此文载于卷 349 第 6251 期，文章号 aac4716。它把「可重复性危机」从担忧变成可量化的事实，为本章「强经验模式是否真的稳健」提供了直接而有分量的经验数据。
