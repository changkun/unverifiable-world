# 第 4 章　摊平的诱惑

> **论点**：五种处境看上去都是「我没法检验」，于是人们很想把不可验证当成一个问题，配一个解法。就问题而言，这是错的；就应对而言，它却指向了对的东西。

第 2 章花了整整一章，把不可验证拆成五种处境。第 3 章又看到，应对这些处境的招数彼此相似。把这两件事放在一起，一个念头几乎必然会冒出来，而且极具诱惑：既然它们都带着「我没法检验」这同一个特征，又都用差不多的办法对付，何不干脆宣布，不可验证就是一个问题，配一个统一的解法？

这一章要做两件事：先指出这个念头错在哪里，再说清它歪打正着地碰对了什么，并由此给全书立下一条举证责任（burden of proof）。

## 摊平错在哪里

摊平（flatten），就是把五种结构不同的处境硬压成一种。它的代价，第 2 章已经预演过了。

把不可判定（undecidable）当成预算问题，以为「多堆点算力就行」。错。停机问题（halting problem）不是算得慢，是根本没有那个算法，再快的机器也变不出一个不存在的程序。

把对抗缺口当成单纯的可观测缺口，以为「我只是还没看清它」。这错得更危险。对面那个系统会顺着你的看法调整自己：你看得越清，它躲得越巧。这是一盘棋，不是一次测量。垃圾邮件过滤就是现成的例子。你按当下垃圾邮件的特征训练好一个分类器，发信方马上就改写措辞、换域名、插乱码，绕过它。谁把这当成静态的识别题，想用只训练一次的模型去解，谁就永远慢半拍。

把难解（intractable）当成不可判定，就会过早放弃一个本可以近似、可以按平均情形处理的问题；反过来，把不可判定当成难解，就会对着一堵逻辑的墙没完没了地砸算力。每一种错认，都会让你掏出错误的工具，付出真实的代价。病灶诊断错了，再好的药也会变成毒药。

所以，就「问题」而言，摊平是错的。五种处境必须分开对待。这是第 2 章用一整章换来的结论，不能在这里轻易交还。

## 摊平歪打正着的那一面

可是，这个念头里有一粒真东西。它在「问题」上错了，在「应对」上却歪打正着。

本书的命题，就是把这粒真东西从那团错误里挑出来，而且说得非常小心：

> 不可验证的来源天差地别，但有限主体（bounded actor）被逼出来的应对，一再收敛到同一小套。

请注意这个说法的克制。它不说「这些问题是同一个问题」：那是摊平，是错的，任何一个领域的专家都会把书摔了。它说的是另一件更强、也更站得住的事：问题各不相同，应对却押韵。全书要交出的，是那张「同一招在多种行话下的对照表」，外加一个解释：为什么偏偏收敛到这几招。

## 本书必须承担的举证责任

话说到这里，最大的风险也就浮出来了。人天生爱类比。莱考夫与约翰逊<sup class="cite"><a href="#ref-14">14</a></sup>让我们看到，连日常语言都是用隐喻搭起来的；根特纳<sup class="cite"><a href="#ref-6">6</a></sup>、霍利约克<sup class="cite"><a href="#ref-9">9</a></sup>、巴尔塔<sup class="cite"><a href="#ref-7">7</a></sup>等人则研究了类比什么时候为真、什么时候只是好看。可正因为类比这么顺手，它也最容易骗人。漂亮的跨领域类比，常常什么也证明不了。最现成的反面教材，是霍夫施塔特的《哥德尔、艾舍尔、巴赫》<sup class="cite"><a href="#ref-1">1</a></sup>那一路写法：跨领域的呼应写得目眩神迷，却常被批评「终究只是类比」，经不起追问。

更扎实的教训来自幂律（power law）热潮。许多系统被宣称服从同一条幂律、共享同一种深层机制，听上去无比统一。可一旦用克劳塞特、沙利齐与纽曼<sup class="cite"><a href="#ref-25">25</a></sup>2009 年那样严格的统计方法去检验，大量「幂律」都站不住。他们重新审视了二十余个被广泛宣称服从幂律的真实数据集，能稳稳通过检验的寥寥无几；多数无法排除对数正态（log-normal）等其他分布，这些分布拟合得同样好，甚至更好。斯坦普夫与波特<sup class="cite"><a href="#ref-26">26</a></sup>2012 年那篇「关于幂律的若干真相」说得很直白：看起来像，不等于是。

所以，本书必须给自己套上一条铁律：任何宣称的收敛，都必须被证明不只是类比。

什么才算「不只是类比」？科学哲学里有现成的标尺。一个跨领域的映射要算实质的，就得是结构保持（structure-preserving）的：不只是表面相似，还要机制对应、失效方式对应、权衡也对应。根特纳<sup class="cite"><a href="#ref-6">6</a></sup>的结构映射（structure-mapping）和巴尔塔<sup class="cite"><a href="#ref-7">7</a></sup>对类比论证（analogical argument）的评估，给出的就是这套标准。还有一条更硬的判据，是稳健性（robustness）：一个结论如果能从多条互相独立的路径反复导出，就更可信。这一思想来自莱文斯<sup class="cite"><a href="#ref-17">17</a></sup>、维姆萨特<sup class="cite"><a href="#ref-18">18</a></sup>、韦斯伯格<sup class="cite"><a href="#ref-19">19</a></sup>发展的稳健性分析（robustness analysis）。

安德森<sup class="cite"><a href="#ref-5">5</a></sup>那句「多者异也」（More Is Different）、福多<sup class="cite"><a href="#ref-27">27</a></sup>关于「特殊科学」（special sciences）的论证，以及卡特赖特<sup class="cite"><a href="#ref-28">28</a></sup>的《斑驳的世界》都表明，跨层次的真实模式确实存在，但它们是挣来的，不是宣布出来的。博克斯<sup class="cite"><a href="#ref-33">33</a></sup>的名言悬在头顶：所有模型都是错的，有些是有用的。本书要争取的，是「有用，且用处经得起检验」，而不是「优雅得让人忘了检验」。

落到操作上，这条铁律意味着：第三部每抽出一招，每做一次跨领域的并置，都要逼问一遍：这个迁移是实质的（同样的机制、同样的失效方式、同样的权衡），还是只是一个漂亮的比方？经得起这番拷问，对照表才成立；经不起，它就只是一本好看的散文。第 13 章会尝试把这种收敛建立在一个共同的底层结构上（风险与信息的分解），但那是一张有待兑现的期票，是要去检验的，不能预先假定。第 14 章则会正面回答：这究竟是一条定律，还是一个很强的经验模式。

## 接下来：第二部的次序

既然不能先宣布收敛、再挑几个例子来凑，唯一靠得住的检验办法，就是走进真实的领域，看做得好的人到底做了什么。要让招数从案例里自己长出来，而不是先立好招式再去套。

这也解释了本书为什么把现场（第二部）放在招式库（第三部）之前。先抽象、再举例，会显得武断，也浪费了案例本该有的说服力。所以第二部不急着命名。它让招数嵌在各自的领域里，彼此缠绕着出现，表面上看起来乱一些；到了第三部，才把每一招单独拎出来，洗干净，起好名字。先归纳，后命名。

四个现场已经备好：一个揣摩用户心思的设计者，一个被放出去自行其是的智能体，一个对着黎曼假设撞墙的数学家，一个看不见自己的庞大组织。它们面对的不可验证，来自五种处境中不同的几种。我们去看看，在神谕始终不来的时候，他们各自伸手拿的是什么。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实。

1. D. Hofstadter (1979).《Gödel, Escher, Bach: An Eternal Golden Braid》. Basic Books. [②]
   霍夫施塔特借哥德尔的不完全性、埃舍尔的视觉悖论与巴赫的赋格，编织出一套关于自指、递归与意识如何从形式系统中浮现的宏大类比。它是跨域类比写作的标杆，也是本章的反面教材：呼应写得目眩神迷，却屡被批评「终究只是类比」，正好提醒读者，漂亮的跨域共鸣本身并不构成论证。

2. H. A. Simon (1969).《The Sciences of the Artificial》. MIT Press. [②③]
   西蒙提出研究「人造物」的科学，主张设计是一门可以系统化的学问，并以有限理性、满意而非最优来刻画真实主体的决策。本书对本章重要，在于它把「有限主体在受约束下如何应对」当成正经的科学对象，正是全书命题里那个「被逼出来的应对」的思想源头。

3. W. C. Wimsatt (2007).《Re-Engineering Philosophy for Limited Beings: Piecewise Approximations to Reality》. Harvard University Press. [②④]
   维姆萨特主张哲学应当为「有限存在者」重写：认知资源有限的主体只能用启发式、近似与稳健性来逼近实在，错误是不可避免却可管理的。书名几乎就是本书副线的注脚，读者可重点看它如何把稳健性当作有限主体辨别真伪模式的核心工具。

4. H. A. Simon (1962).「The Architecture of Complexity」. Proceedings of the American Philosophical Society, 106(6), 467-482. [②③]
   西蒙论证复杂系统多为「近可分解」的层级结构，子系统内部联系紧、子系统之间联系松，这种架构既便于演化也便于理解。它为「跨层次存在真实模式」提供了经典的结构性论据，值得与安德森、福多对照着读。

5. P. W. Anderson (1972).「More Is Different」. Science, 177(4047), 393-396. [②]
   安德森反对还原论的傲慢，指出每一层级都会涌现出新的规律，下一层的定律无法被上一层简单推导出来。本章引用的「多者异也」一语即出于此，它说明跨层次的真实模式确实存在，但要靠各自的科学挣来，而非从基础物理宣布得到。

6. D. Gentner (1983).「Structure-Mapping: A Theoretical Framework for Analogy」. Cognitive Science, 7(2), 155-170. [②]
   根特纳提出结构映射理论：好的类比迁移的是关系结构而非表面属性，系统性的关系网络比孤立的相似点更有价值。这正是本章「实质类比须结构保持」判据的理论来源，读者可由此理解什么叫「机制对应而非表面相似」。

7. P. Bartha (2010).《By Parallel Reasoning: The Construction and Evaluation of Analogical Arguments》. Oxford University Press. [②]
   巴尔塔为类比论证建立一套规范性的评估框架，追问一个类比何时能真正承载推理的重量，关键在于源域与目标域之间是否存在相关的因果或结构联系。它给本章那条「不只是类比」的铁律提供了可操作的判别标准。

8. M. B. Hesse (1966).《Models and Analogies in Science》. University of Notre Dame Press. （扩充版，初版 1963。）[②③]
   赫西分析模型与类比在科学中的认知功能，区分正面、负面与中性类比，指出类比的「中性部分」正是科学预测与发现的生长点。它是类比方法论的早期奠基之作，为后来的结构映射与类比评估铺路。

9. K. J. Holyoak & P. Thagard (1995).《Mental Leaps: Analogy in Creative Thought》. MIT Press. [②]
   霍利约克与萨加德提出类比的多重约束理论，认为人脑在结构、语义与目的三类约束的相互制衡下完成类比映射。本书把类比放进认知与创造的现实过程中考察，有助读者理解类比为何既强大又易出错。

10. D. Gentner, K. J. Holyoak & B. N. Kokinov (Eds.) (2001).《The Analogical Mind: Perspectives from Cognitive Science》. MIT Press. [②]
   这本文集汇集认知科学各路对类比的研究，从计算模型到发展心理到神经机制，系统呈现「类比何时为真、何时只是好看」的研究版图。它是本章关于类比研究脉络的总览性入口。

11. D. Hofstadter & E. Sander (2013).《Surfaces and Essences: Analogy as the Fuel and Fire of Thinking》. Basic Books. [②]
   霍夫施塔特与桑德主张类比是思维的核心引擎，连最基本的范畴化与概念形成都是不断进行的类比。本书把类比的地位推到极致，恰好与本章的警惕形成张力：类比无处不在，正因此更需要一套判据来分辨哪些迁移是实质的。

12. S. Vosniadou & A. Ortony (Eds.) (1989).《Similarity and Analogical Reasoning》. Cambridge University Press. [②]
   这本文集集中讨论相似性与类比推理的关系，追问「相似」究竟意味着什么、它如何驱动推理与学习。它为本章背后的问题，即如何把「看起来像」与「确实是」区分开，提供了概念上的准备。

13. K. Dunbar (1995).「How Scientists Really Reason: Scientific Reasoning in Real-World Laboratories」. 收入 R. J. Sternberg & J. E. Davidson (Eds.),《The Nature of Insight》, 365-395. MIT Press. [①②③]
   邓巴实地观察分子生物学实验室，发现科学家在真实工作中大量使用类比，且近距离的、领域内的类比往往比远距离的更富成效。它以现场证据支撑本章「让招数从案例里自己长出来」的方法选择，说明真实推理与教科书叙述并不相同。

14. G. Lakoff & M. Johnson (1980).《Metaphors We Live By》. University of Chicago Press. [②]
   莱考夫与约翰逊论证隐喻不只是修辞，而是人类概念系统的结构本身，连「时间是金钱」这类日常表达都暗藏成体系的隐喻。本章引它来说明类比与隐喻深植于人类思维，正因如此才更需对其可靠性保持戒心。

15. A. Tversky & D. Kahneman (1974).「Judgment under Uncertainty: Heuristics and Biases」. Science, 185(4157), 1124-1131. [②④]
   特沃斯基与卡尼曼揭示人在不确定下依赖代表性、可得性、锚定等启发式做判断，这些捷径虽高效却会系统性地导致偏差。它提醒读者，有限主体的应对往往不是最优解而是凑合用的招数，也解释了为何漂亮的类比格外容易骗过我们。

16. R. W. Batterman (2001).《The Devil in the Details: Asymptotic Reasoning in Explanation, Reduction, and Emergence》. Oxford University Press. （精装初版 2001 年 11 月；部分编目著录作 2002。）[②③]
   巴特曼研究渐近推理在解释中的作用，论证许多物理现象的解释恰恰藏在取极限时浮现的「细节」里，普适性正源于此。它为「跨系统的共同结构如何可能」提供了一个精细的哲学案例，呼应本章对收敛之机制的追问。

17. R. Levins (1966).「The Strategy of Model Building in Population Biology」. American Scientist, 54(4), 421-431. [②③]
   莱文斯指出建模无法同时兼顾普适、精确与现实三者，建模者必须取舍，并提出当多个不同假设的模型给出一致结论时，该结论更可信。这正是稳健性分析的源头，本章那条「多路径反复导出更可信」的硬判据由此而来。

18. W. C. Wimsatt (1981).「Robustness, Reliability, and Overdetermination」. 收入 M. B. Brewer & B. E. Collins (Eds.),《Scientific Inquiry and the Social Sciences》, 124-163. Jossey-Bass. [②③]
   维姆萨特系统阐发稳健性概念：能被多种相互独立的手段、模型或视角共同探测到的东西，更可能是真实的而非假象。本文是本章稳健性判据的核心文献，读者可由此理解为何独立路径的汇合能压制错误。

19. M. Weisberg (2006).「Robustness Analysis」. Philosophy of Science, 73(5), 730-742. [②③]
   韦斯伯格重新厘清稳健性分析的逻辑，区分稳健定理与对其经验充分性的检验，澄清它何时能、何时不能为结论提供支持。它让本章的稳健性判据更精确，提醒读者稳健并不自动等于为真，仍需经验把关。

20. S. H. Orzack & E. Sober (1993).「A Critical Assessment of Levins's The Strategy of Model Building in Population Biology (1966)」. The Quarterly Review of Biology, 68(4), 533-546. [②③]
   奥扎克与索伯批判性地审视莱文斯的建模策略，质疑仅凭多模型一致就推断结论为真在逻辑上是否成立，除非这些模型各自已得到独立支持。它是稳健性论证的重要反方，帮助本章把铁律守得更紧，避免把一致误当成证明。

21. N. Goldenfeld & L. P. Kadanoff (1999).「Simple Lessons from Complexity」. Science, 284(5411), 87-89. [②③]
   戈登菲尔德与卡达诺夫提醒，研究复杂系统要在恰当的尺度上选用恰当的模型，普适性虽诱人却不应掩盖具体机制，关键在于「在合适的层面上做对的简化」。它为本章如何谨慎对待跨系统普适规律提供了来自物理学内部的清醒声音。

22. L. P. Kadanoff (1966).「Scaling Laws for Ising Models near Tc」. Physics Physique Fizika, 2(6), 263-272. [②]
   卡达诺夫提出区块自旋的标度图像，说明临界点附近系统在不同尺度上自相似，为后来的重整化群与普适类理论奠基。它是「不同系统共享同一临界行为」这一真实普适性的经典范例，与后文那些立不住的「幂律」恰成对照。

23. P. Bak, C. Tang & K. Wiesenfeld (1987).「Self-Organized Criticality: An Explanation of the 1/f Noise」. Physical Review Letters, 59(4), 381-384. [②]
   巴克、汤与维森费尔德提出自组织临界性，以沙堆模型说明某些系统会自发演化到临界态，从而出现幂律分布与 1/f 噪声。它引爆了后来的幂律热潮，既是跨系统统一叙事的代表，也成为本章「需用严格统计检验」的检验对象。

24. A.-L. Barabási & R. Albert (1999).「Emergence of Scaling in Random Networks」. Science, 286(5439), 509-512. [②③]
   巴拉巴西与阿尔伯特提出无标度网络模型，以增长加优先连接机制解释了许多真实网络中度分布呈幂律。它是网络科学的奠基之作，也属于那批被广泛宣称服从同一幂律的系统，正适合放在本章的批判性透镜下重审。

25. A. Clauset, C. R. Shalizi & M. E. J. Newman (2009).「Power-Law Distributions in Empirical Data」. SIAM Review, 51(4), 661-703. [②]
   克劳塞特、沙利齐与纽曼提出一套严格的统计方法来检验数据是否真服从幂律，包括最大似然拟合与对替代分布的比较。用此方法复核后，许多此前被宣称的「幂律」并不成立。它正是本章那条「任何宣称的收敛都须经得起严格检验」铁律的方法样板。

26. M. P. H. Stumpf & M. A. Porter (2012).「Critical Truths About Power Laws」. Science, 335(6069), 665-666. [②]
   斯坦普夫与波特总结幂律研究的教训，直言看起来像幂律远不等于是幂律，更不等于背后存在共同的深层机制，统计上的拟合与机制上的解释必须分清。本章「看起来像，不等于是」一语即本于此，是收紧举证责任的直接依据。

27. J. A. Fodor (1974).「Special Sciences (or: The Disunity of Science as a Working Hypothesis)」. Synthese, 28(2), 97-115. [②]
   福多论证心理学、经济学等「特殊科学」的规律可多重实现，无法被还原为物理学，因此科学在本质上是不统一的。本章引它支持「跨层次的真实模式确实存在且不可被还原宣布掉」，与安德森、卡特赖特同一阵线。

28. N. Cartwright (1999).《The Dappled World: A Study of the Boundaries of Science》. Cambridge University Press. [②③]
   卡特赖特主张世界是「斑驳的」，物理定律只在它们各自的局部域内成立，并不构成一张覆盖一切的统一图景，普适性是例外而非常态。本书为本章「真实模式是挣来的、不是宣布的」立场提供了有力的形而上学支撑。

29. M. Mitchell (2009).《Complexity: A Guided Tour》. Oxford University Press. [②③]
   米切尔为复杂系统科学写了一部清晰可靠的导览，覆盖信息、计算、演化、网络与涌现等主题，且对该领域常见的夸大保持审慎。它是读者进入复杂性与幂律话题的稳妥入口，态度上与本章的克制相合。

30. D. Sornette (2006).《Critical Phenomena in Natural Sciences: Chaos, Fractals, Selforganization and Disorder》(2nd ed.). Springer. （初版 2000。）[②]
   索尔内特系统梳理自然科学中的临界现象、幂律、分形与自组织背后的数学，给出处理这类重尾与标度行为的技术工具。它代表了跨学科寻找普适标度律的雄心，可与对幂律的批判文献并读，看清主张与检验之间的距离。

31. G. West (2017).《Scale: The Universal Laws of Growth, Innovation, Sustainability, and the Pace of Life in Organisms, Cities, Economies, and Companies》. Penguin Press. [②]
   韦斯特提出从生物体到城市再到公司都遵循某些标度律，例如代谢率随体型的次线性缩放，试图为生命与社会找到统一的定量法则。本书是宏大跨域普适叙事的当代代表，正好供读者用本章的判据去衡量：哪些是实质收敛，哪些只是动人的统一愿景。

32. P. Galison (1997).《Image and Logic: A Material Culture of Microphysics》. University of Chicago Press. [①③]
   加里森研究二十世纪微观物理的实验文化，提出不同子学科在「交易区」用一种工作性的混合语言协作，即便彼此理论框架并不一致也能共事。它示范了不同领域如何在不被强行统一的前提下真实地相互对接，呼应本书对「押韵而非同一」的强调。

33. G. E. P. Box (1976).「Science and Statistics」. Journal of the American Statistical Association, 71(356), 791-799. [③④]
   博克斯在此阐述科学是模型与现实反复对照、逐步逼近的迭代过程，文中写下「所有模型都是错的」；广为流传的完整说法「所有模型都是错的，有些是有用的」则见于他与德雷珀合著的《Empirical Model-Building and Response Surfaces》（1987，第 424 页）。本章把这句话悬于头顶，用以界定全书要争取的目标，是有用且其用处经得起检验，而非优雅得让人忘了检验。

34. T. S. Kuhn (1962).《The Structure of Scientific Revolutions》. University of Chicago Press. [①③]
   库恩提出范式与科学革命的著名框架，区分常规科学的解谜与范式更替时的不可通约，重塑了人们对「科学如何进展」的理解。它是本书思考科学进展与判断的底色之作，提醒读者跨范式的比较从来不是简单的逐项对应。
