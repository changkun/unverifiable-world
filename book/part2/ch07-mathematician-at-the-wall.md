# 第 7 章　撞墙的数学家

> **论点**：数学中的不可验证（unverifiable）以最纯粹的形态出现：它是难解的（intractable），有时还是不可判定的（undecidable）。行之有效的应对有三种：验证一个有限的局部，并为之证明一个界（证书，certificate）；把目标替换为与之等价、却更易处理的陈述（代理替换，proxy substitution）；采用容许 ε 误差的概率方法（probabilistic method）。

## 无从估量的距离

难题之所以难，往往不在于它有多艰深，而在于人们无从估量自己离它还有多远。

登山者看得见山顶，调试程序的人能收到报错信息；他们至少知道方向是否正确，离目标是更近了还是更远了。证明一个数学猜想，却没有这样的凭借。离答案也许只差一个想法，也许还隔着一个世纪，而手边没有任何仪表能够指明究竟是哪一种情形。1859 年，黎曼在一篇仅有八页的论文中<sup class="cite"><a href="#ref-9">9</a></sup>，几乎是顺带地写下了后来以他的名字命名的猜想，并补充说，人们当然希望对此有一个严格的证明，但他在几次短暂而徒劳的尝试之后暂且把这件事搁置了，因为它对于他接下来的研究目的并非必需。这一搁置，至今已有一百六十余年。

本章考察的是，数学家站在这堵墙前实际做了些什么。之所以选择数学作为考察的场景，是因为它呈现了不可验证最纯粹的形态。这里没有隐藏的状态，没有蓄意欺骗的对手，也不存在时间不足的托辞；命题非真即假，界限分明。然而，即便在这个最纯净的领域，验证依然系统性地不可得。倘若能够看清善于应对者在这里如何行动，本部其余几个更为驳杂的场景（控制台前的人、放出去的智能体、看不见自己的组织）便有了一个参照。

## 验证的鸿沟

首先需要准确地刻画这堵墙的形状。

核对一个证明容易，找到一个证明困难。给定一份完整写出的形式推导，逐行对照公理与推理规则加以检查，是一项机械的工作：原则上可以交由机器完成，并且必定在有限步之内给出「是」或「否」的回答。找到这份推导，则完全是另一回事。这种不对称是本章的基石。

它有一个精确的逻辑表述。1936 年，丘奇与图灵各自证明了判定问题（Entscheidungsproblem）不可解：不存在一个算法，能够对一阶逻辑中的任意命题判定它是否逻辑有效；而根据哥德尔完备性定理（Gödel's completeness theorem），判定有效性等价于判定可证性。再考虑一个足够丰富、可递归公理化且一致的形式系统（例如皮亚诺算术或 ZFC）：它的定理集是递归可枚举的（recursively enumerable），却不是递归的。换言之，我们可以把全部证明逐一枚举出来，却不存在一个程序，能够对每一个非定理都在有限步之内判定它不是定理。对证明的检验是可判定的，定理性却不可判定；两者之间的落差，就是那道鸿沟。

> **深入一层（可跳过）**：「足够丰富」这一限定至关重要。可判定的理论确实存在，例如普雷斯伯格算术（只含加法的自然数理论）和塔斯基的实闭域理论。在这些理论中存在判定程序，任何命题都可以机械地加以裁决。由此可见，不可判定性并非逻辑的普遍宿命，而是表达力越过某一门槛之后必须付出的代价。黎曼假设所属的解析数论，远在这一门槛之上。

更令人困扰的是：不仅证明难以找到，就连「我离答案是否已经接近」这一问题也没有判定程序。黎曼假设（Riemann hypothesis，下文简称 RH）之所以令人苦恼，原因就在于此：它抗拒的不只是求解，还有对进展的估计。就第 2 章所区分的五种处境而言，本章处在「不可判定」与「难解」的交界：有些问题在原则上就不存在判定程序；有些虽有程序，代价却大到在宇宙的寿命之内也无法运行完毕。墙后是什么，无从看见；于是，高明的数学家不再正面凿墙，而是改换姿态。下面三种姿态会在本书其他章节中反复出现，只是名称不同。

## 证书与界

第一种姿态：放弃对整体的验证，只验证一个有限的局部，并为它证明一个有保证的界，即一个经过严格证明、适用范围明确划定的结论。

回到 ζ 函数。黎曼把欧拉那个与素数相联系的级数，解析延拓为整个复平面上的亚纯函数，并写出了它的完备化形式

$$\xi(s) = \tfrac{1}{2}\,s(s-1)\,\pi^{-s/2}\,\Gamma\!\left(\tfrac{s}{2}\right)\zeta(s),\qquad \xi(s)=\xi(1-s).$$

这一对称的函数方程（functional equation）把临界带（critical strip）沿其中线左右对折。猜想断言：$\zeta$ 的全部非平凡零点都位于临界线（critical line）$\operatorname{Re}(s)=\tfrac12$ 上（平凡零点位于负偶数处）。不可验证之处，就在「全部」这个全称量词上。

然而，有限多个零点是可以验证的。这里必须区分两件常被混为一谈的事。2004 年，古尔东计算了前 $10^{13}$ 个零点，确认它们都位于临界线上<sup class="cite"><a href="#ref-17">17</a></sup>。这是以高精度浮点运算完成的数值计算，足以给人极强的信心，却不构成证书，因为它没有对舍入误差给出严格的界。普拉特在 2017 年所做的是另一件事<sup class="cite"><a href="#ref-18">18</a></sup>：他借助区间算术（interval arithmetic），严格证明了高度（即虚部）不超过约 $3.06\times10^{10}$ 的全部非平凡零点都位于临界线上；2021 年，普拉特与特鲁吉安又把这一高度推进到 $3\times10^{12}$。只有后两项结果才称得上证书：一种有界的、局部的、可以机械复核的保证。这样的保证是真实的，但它不是定理。无论验证推进到多高，有限与「全部」之间的距离都不会因此弥合。

这种姿态在数学中有可敬的先例。1896 年，阿达马与德拉瓦莱普桑各自证明了素数定理（prime number theorem）$\pi(x)\sim x/\ln x$，所依靠的是一个比 RH 弱得多、却力所能及的界：$\zeta$ 在直线 $\operatorname{Re}(s)=1$ 上没有零点。既然无法证明零点都位于实部为 $\tfrac12$ 的直线上，那就先证明它们都不在实部为 $1$ 的直线上。这是以一个能够证明的弱命题，换取通向强命题途中的一段实质进展。

把同一种姿态移到软件领域，其面貌立刻变得熟悉。类型系统（type system）并不证明程序「完全正确」，只证明某一条特定的性质（不会把整数当作指针来解引用），以此换来一种可判定的检查。形式化验证（formal verification）走得更远：2017 年，黑尔斯团队发表了开普勒猜想（Kepler conjecture）的机器可核对证明<sup class="cite"><a href="#ref-25">25</a></sup>，把一个连人类审稿人都争论了多年的论证，转化为可以逐行验证的证书。其代价始终相同：证书换来的是局部的确定，付出的是普遍性；而局部终究不是定理。于是，有人转而改动目标。

## 代理替换

第二种姿态：不再固守原来的命题，而是把它替换为一个与之等价、却更易处理的陈述。这个代替原命题而成为攻坚对象的陈述，便是本书所说的代理。

RH 的等价表述多得惊人。1997 年，李建军给出了一个判据<sup class="cite"><a href="#ref-14">14</a></sup>：RH 成立，当且仅当对所有 $n\ge1$，下列实数均满足 $\lambda_n\ge 0$：

$$\lambda_n=\sum_{\rho}\left[1-\left(1-\tfrac{1}{\rho}\right)^{n}\right],$$

其中求和取遍全部非平凡零点。一个关于零点位置的几何陈述，由此被转译为一列实数的非负性。奈曼与博伊林给出了另一个判据：RH 等价于示性函数 $\chi_{(0,1)}$ 属于一族经伸缩的小数部分函数所张成的子空间在 $L^2(0,1)$ 中的闭包。零点问题于是被转化为一个逼近问题。2003 年，巴埃斯-杜阿尔特把这一判据加强为只使用整数伸缩的序列形式<sup class="cite"><a href="#ref-16">16</a></sup>，相应的条件是一列距离满足 $d_n\to0$。拉加里亚斯在 2002 年甚至给出了一个初等到可以写在明信片上的等价命题<sup class="cite"><a href="#ref-32">32</a></sup>：对所有 $n$，$\sigma(n)\le H_n+\exp(H_n)\ln H_n$，其中 $H_n$ 为调和数，$\sigma$ 为因子和函数。

我自己也曾在这条路上走过一程。我曾把 RH 转写为李判据（Li's criterion）的形式，置入奈曼-博伊林-巴埃斯-杜阿尔特的逼近框架，又改用算子谱与随机过程的语言来表述，每一次都抱着同样的期望：换一种语言，困难或许会在新的坐标中显露出一处可以着力的地方。而每一次得到的结论也都相同：等价确凿无疑，难度却丝毫未减。我并没有解决这个问题，只是为它换了名称，换了表述。

这是代理替换在数学中典型的失效方式，值得为它取一个准确的名字：忠实却不更易的代理。等价性保证了它指向的仍是同一个真实目标（忠实），但它丝毫不比原问题更容易求解（不更易）。这一对策能否奏效，完全取决于能否同时做到忠实与更易；而两者兼得极为罕见，罕见到可以说，这一对策的全部技艺都系于此处。

若以这两个维度列成一张表，一条贯穿本章的线索便显现出来：

|        | 更易                          | 不更易                              |
| ------ | --------------------------- | -------------------------------- |
| **忠实** | 理想代理（罕见，技艺全在于此）              | 数学中的等价改写：只是为困难换了名称（本章）            |
| **不忠实** | Goodhart：优化的是代理，真实目标却随之败坏（第 8、11 章） | 无用，无人问津                         |

数学家的困境位于表中由左下至右上那条对角线的右上端：忠实，却不更易。在后文讨论组织的一章中，失败落在左下端：一个更易却不忠实的代理，越是竭力优化它，真正在意的东西就越是遭到损害。同一种对策，沿两个相反的方向失效。第 11 章将把这两端正式联系起来。此处只需记住一点：替换目标既非作弊，也非出路；它是一种姿态，能否奏效是另一回事。

## 概率方法

第三种姿态最违背数学的本能：不再要求一个非此即彼的判决，转而持有一个经过校准（calibration）的概率，接受有界的出错风险，并照常行动。

素性检验（primality test）是最清楚的例子。判断一个大数是否为素数，确定性算法代价高昂；米勒-拉宾（Miller-Rabin）检验则换了一种问法：若 $n$ 是合数，那么对随机选取的一个底，它通过检验、从而被误判为素数的概率至多为 $1/4$；独立进行 $k$ 轮，误判概率便降至 $\le (1/4)^k$。此前，索洛维与施特拉森已在 1977 年给出误差 $\le (1/2)^k$ 的版本<sup class="cite"><a href="#ref-20">20</a></sup>，拉宾的版本则见于 1980 年<sup class="cite"><a href="#ref-19">19</a></sup>。「以 $1-\varepsilon$ 的概率为素数」与「已证明为素数」是性质截然不同的两种认识；但前者在工程上已经足够，而且所需的精度可以任意提高，多做几轮即可。

关键在于看清这里究竟放弃了什么。放弃的是确定性的类型，而不是严格性：那个 $(1/4)^k$ 的界是一条定理，其证明无懈可击。标准并没有降低，只是换成了一种能在预算之内兑现的标准。概率方法在纯数学中同样登堂入室。埃尔德什的概率方法（Alon 与 Spencer 将其写成了一部经典<sup class="cite"><a href="#ref-26">26</a></sup>）能够证明某个对象存在，所凭借的是证明它出现的概率为正，却并不把这个对象具体构造出来。存在性得到了证明，构造却付之阙如。

这种姿态一直延伸到人们对 RH 的信念。1973 年，蒙哥马利研究零点的配对关联（pair correlation）<sup class="cite"><a href="#ref-30">30</a></sup>，推导并猜想：经归一化之后，零点的配对关联函数形如

$$R_2(u)=1-\left(\frac{\sin \pi u}{\pi u}\right)^{2}.$$

戴森在普林斯顿当即认出，它与随机矩阵理论中高斯酉系综（Gaussian unitary ensemble, GUE）本征值的配对关联完全一致。1987 年，奥德利兹科对大量零点进行数值计算<sup class="cite"><a href="#ref-33">33</a></sup>，证实二者的吻合达到了令人惊叹的程度。这些都不是证明，却是极强的证据。它们使数学家相信 RH；而这种相信，与物理学家相信一条尚未被证伪的定律，并无本质区别。由此可见，数学内部同样发展出了一套在无法验证时形成信念的方法。

## 数学家如何判断

由此进入本章关于人的部分：在神谕始终缺席的情况下，有判断力的人依靠什么持有信念，又依靠什么决定把力气投向何处？

数学对外是演绎的，对内是似真的。波利亚在《数学与猜想》<sup class="cite"><a href="#ref-2">2</a></sup>中专门讨论合情推理：数学家在尚无证明之时，如何借助类比、归纳与特例来估量一个命题的分量。阿达马考察了数学发明的心理<sup class="cite"><a href="#ref-3">3</a></sup>，记录了其中酝酿与顿悟的节律。庞加莱则留下了那个著名的瞬间<sup class="cite"><a href="#ref-5">5</a></sup>：在踏上公共马车踏板的一刹那，富克斯函数与非欧几何之间的联系毫无征兆地浮现在他的脑海中。这些都不能替代证明；它们是在证明到来之前、在那段没有仪表可依的路途上，人们实际依靠的东西。

数学家为何在证明出现之前就相信 RH？因为证据来自多个方向，并且彼此印证：大量零点已被验证位于临界线上；众多等价形式中没有一个被推翻；它的一个类比形式已被证明（有限域上代数簇的黎曼假设，由德利涅证明）；零点的统计行为与随机矩阵理论的预言精确吻合。其中没有任何一条是证明，但合在一起，它们构成了一种有纪律的信念。

数学界自身也曾反思这种信念的地位。1993 年，贾菲与奎因围绕「理论数学」引发了一场争论<sup class="cite"><a href="#ref-22">22</a></sup>，所追问的问题是：猜想驱动、证据先行的工作，在多大程度上算得上数学。瑟斯顿 1994 年的《论数学中的证明与进展》<sup class="cite"><a href="#ref-21">21</a></sup>则主张，数学所推进的是人类的理解，而不只是形式证明的库存。陶哲轩追问何为好的数学<sup class="cite"><a href="#ref-29">29</a></sup>，而他列举的标准中没有一条是「已被证明」。综合这些讨论可以看到，判断「某个命题多半为真、值得投入」的能力，就是一种经过校准的信念；第四部将专门为它命名。善于应对者在神谕缺席时既不会手足无措，也不假装确定：他们持有一个标定了刻度的信念，并照常行动。

## 小结

面对最纯粹的不可验证，数学家并没有等来一个判定程序。他们得到的是以下几样东西：证书（验证一个有限的局部，证明一个界）；代理替换（把目标换成等价的陈述，同时坦然承认它往往忠实却不更易）；概率接受（放弃非此即彼的判决，依据经过校准的概率行动）；以及在证明到来之前持有信念的判断力。

这些都不是数学独有的权宜之计。把不受信任的代码置于沙箱之中，对一个组织进行审计，在界面背后揣摩用户未曾言明的偏好：在这些场合，人们所诉诸的都是同样几种办法，只是术语不同。第三部将把每一种对策从其原生的领域中抽离出来，分别命名，并在不同领域之间对照排列；由此形成的那张对照表，是全书最主要的贡献。

最后还有一点需要在此说明。本书自身的核心命题，即「应对会收敛到同一小组对策」这一论断，我目前同样无法验证。我对它的相信，与数学家对 RH 的相信属于同一类：一个建立在跨领域证据之上、标定了刻度、却没有证明的信念。第 14 章将回到这一问题，让本书亲自践行它一直在描述的做法。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实。

1. G. Pólya (1945).《How to Solve It: A New Aspect of Mathematical Method》. Princeton University Press. doi:[10.1515/9781400828678](https://doi.org/10.1515/9781400828678) [①]
   波利亚把数学解题拆成理解题意、拟订计划、执行、回顾四个阶段，并系统列出类比、特例、逆推、辅助问题等启发式策略。它写的不是定理证明，而是发现证明之前那段没有仪表的探索过程，正是本章「数学家如何判断」一节关心的东西。
2. G. Pólya (1954).《Mathematics and Plausible Reasoning》（2 卷）. Princeton University Press. [Google Books](https://books.google.com/books?id=k906zgEACAAJ) [①④]
   两卷分别讨论数学中的归纳与类比，以及合情推理的逻辑结构，论证数学家在拿到严格证明之前，靠观察特例、归纳模式、权衡证据来形成对命题的信念。本章正文借它点明「数学对外是演绎的，对内是似真的」，是理解合情推理这一概念的源头读物。
3. J. Hadamard (1945).《An Essay on the Psychology of Invention in the Mathematical Field》. Princeton University Press. [Google Books](https://books.google.com/books?id=J7EVAAAAIAAJ) [①]
   阿达马调查了数学家的创造心理，提炼出准备、酝酿、顿悟、验证的发现节律，强调潜意识工作与无预兆的灵感闪现。它为本章描述庞加莱式的顿悟提供了第一手的心理学考察，说明数学判断很大一部分发生在意识与证明之外。
4. H. Poincaré (1902).《La Science et l'Hypothèse》. Flammarion. [Google Books](https://books.google.com/books?id=GvE0DwAAQBAJ) [①]
   庞加莱在这部科学哲学经典里讨论数学假设、约定与几何的地位，主张许多基础选择并非经验强加，而是出于约定与方便。它呈现了一位顶尖数学家如何反思自己学科的认识论根基，与本章关心的「在无法验证处如何持有信念」相通。
5. H. Poincaré (1908).《Science et Méthode》. Flammarion. [Google Books](https://books.google.com/books?id=LqGvtAEACAAJ) [①]
   书中那段关于踏上公共马车踏板时灵感涌现的自述，是数学发现心理学最常被引用的第一手记录，庞加莱借此剖析直觉、选择与潜意识在创造中的作用。本章正文直接用到这个瞬间，说明顿悟如何在没有任何征兆时把分散的线索接通。
6. G. H. Hardy (1940).《A Mathematician's Apology》. Cambridge University Press. [Google Books](https://books.google.com/books?id=beImvXUGD-MC) [①]
   哈代为纯数学的价值辩护，提出好的数学在于其严肃性、深刻与不可避免的美，而非实用。作为一位数论大家对自己手艺的内省，它界定了数学家凭什么判断一项工作值不值得做，与本章末尾追问「什么是好的数学」一脉相承。
7. E. P. Wigner (1960).「The Unreasonable Effectiveness of Mathematics in the Natural Sciences」. Communications on Pure and Applied Mathematics, 13(1). doi:[10.1002/cpa.3160130102](https://doi.org/10.1002/cpa.3160130102) [②③]
   维格纳惊讶于抽象数学概念竟能如此精准地描述物理世界，称这种契合是一份我们既不理解也不配拥有的奇异礼物。这篇短文提出的难题，至今没有公认答案，对本章而言它示范了一种对深层规律的信念如何在缺乏证明的情况下被严肃对待。
8. I. Lakatos (1976).《Proofs and Refutations: The Logic of Mathematical Discovery》. Cambridge University Press. doi:[10.1017/cbo9781139171472](https://doi.org/10.1017/cbo9781139171472) [①③]
   拉卡托斯以欧拉多面体公式为例，用一段虚构的课堂对话重演定义、证明与反例如何彼此修正、共同推进数学。它颠覆了数学是一锤定音演绎的刻板印象，呈现知识在猜想与反驳中曲折成长，正合本章对数学进展真实样貌的关注。
9. B. Riemann (1859).「Über die Anzahl der Primzahlen unter einer gegebenen Größe」. Monatsberichte der Berliner Akademie. [链接](https://www.claymath.org/collections/riemanns-1859-manuscript/) [②③]
   黎曼这篇仅八页的论文把 ζ 函数延拓到复平面、给出函数方程，并把素数分布与 ζ 的非平凡零点联系起来，其中顺带写下的那句关于零点位置的猜想，就是后世的黎曼假设。它是整章的源头文本，本章开篇引用的「徒劳尝试后暂时搁下」正出自此处。
10. H. M. Edwards (1974).《Riemann's Zeta Function》. Academic Press. [Google Books](https://books.google.com/books?id=0b1CswEACAAJ) [②]
   爱德华兹这本专著围绕黎曼 1859 年原文展开，逐步铺陈 ζ 函数理论、素数定理与黎曼假设的来龙去脉，兼顾历史脉络与技术细节。它是进入 ζ 函数与 RH 的经典入门读物，为本章涉及的零点、临界线等概念提供了可靠的背景。
11. E. C. Titchmarsh, rev. D. R. Heath-Brown (1986).《The Theory of the Riemann Zeta-function》（第 2 版）. Oxford University Press. [Google Books](https://books.google.com/books?id=1CyfApMt8JYC) [②]
   这是 ζ 函数解析理论的标准高阶专著，系统处理零点分布、零点密度估计、临界线上的均值定理等结果，希思布朗的修订补入了更晚近的进展。它代表了围绕 RH 已被严格建立的技术成果的总和，是本章谈「证书与界」时的专业背景文献。
12. E. Bombieri (2000).「Problems of the Millennium: The Riemann Hypothesis」. Clay Mathematics Institute. [链接](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf) [②④]
   这是克雷数学研究所为千禧年大奖问题撰写的 RH 官方问题陈述，邦别里精炼地交代了猜想的来历、精确表述及其在数论中的份量。它是了解 RH 为何被列为世纪难题的权威切入点，本章对 RH 地位的判断可在此找到背书。
13. J. B. Conrey (2003).「The Riemann Hypothesis」. Notices of the American Mathematical Society, 50(3). [链接](https://www.ams.org/notices/200303/fea-conrey-web.pdf) [②③]
   康里这篇综述面向广泛读者，梳理了支持 RH 的各类证据，包括零点的数值验证、随机矩阵理论的吻合，以及函数域上类比的已被证明。它把本章三种姿势所依赖的证据汇于一处，是了解数学界为何相信 RH 的便捷读物。
14. X.-J. Li (1997).「The Positivity of a Sequence of Numbers and the Riemann Hypothesis」. Journal of Number Theory, 65(2). doi:[10.1006/jnth.1997.2137](https://doi.org/10.1006/jnth.1997.2137) [②④]
   李建军证明 RH 等价于一列由零点定义的实数 $\lambda_n$ 对所有 $n$ 非负，把零点位置这一几何陈述翻译成一个序列的正性判据。本章正文以它为代理替换的头号例子，说明等价改写如何忠实却未必更易。
15. E. Bombieri & J. C. Lagarias (1999).「Complements to Li's Criterion for the Riemann Hypothesis」. Journal of Number Theory, 77(2). doi:[10.1006/jnth.1999.2392](https://doi.org/10.1006/jnth.1999.2392) [②④]
   两位作者指出李判据其实是任意复数多重集一组一般不等式的特例，并不特属于 ζ 函数，又借古伊南-韦伊显式公式给出 $\lambda_n$ 的算术表达式，把它与韦伊的 RH 判据接上。它深化了对李判据的理解，呈现同一个等价命题如何在不同语言间被反复重写，正是本章代理替换主题的延展。
16. L. Báez-Duarte (2003).「A Strengthening of the Nyman-Beurling Criterion for the Riemann Hypothesis」. Atti della Accademia Nazionale dei Lincei, Rendiconti Lincei Mat. Appl., 14(1). [arXiv:math/0202141](https://arxiv.org/abs/math/0202141) [②④]
   巴埃斯-杜阿尔特把奈曼-博伊林的逼近判据收紧为只用整数伸缩的序列版本，使 RH 等价于一列逼近距离 $d_n$ 趋于零。它是本章列举的又一个等价改写，把零点问题搬进 $L^2$ 逼近的框架，同样印证了忠实代理常常并不更易求解。
17. X. Gourdon (2004).「The 10^13 First Zeros of the Riemann Zeta Function, and Zeros Computation at Very Large Height」. 在线技术报告（numbers.computation.free.fr）. [链接](http://numbers.computation.free.fr/Constants/Miscellaneous/zetazeros1e13-1e24.pdf) [②④]
   古尔东借助 Odlyzko-Schönhage 算法用高精度浮点计算，核验了头 $10^{13}$ 个零点都落在临界线上。本章特意拿它与普拉特对照：它给出极强的数值信心，但未严格框住舍入误差，因而是数值结果而非可机械复核的证书。
18. D. J. Platt (2017).「Isolating Some Non-trivial Zeros of Zeta」. Mathematics of Computation, 86(307). doi:[10.1090/mcom/3198](https://doi.org/10.1090/mcom/3198) [②④]
   普拉特用区间算术把零点严格隔离在临界线上，使误差有可证的上界，从而把数值核验升格为可机械复核的证书。本章用它示范「证书与界」这一姿势：不证整体，只为一个有限切片证一个有保证的界。
19. M. O. Rabin (1980).「Probabilistic Algorithm for Testing Primality」. Journal of Number Theory, 12(1). doi:[10.1016/0022-314x(80)90084-0](https://doi.org/10.1016/0022-314x%2880%2990084-0) [②④]
   拉宾给出米勒-拉宾素性检验：若 $n$ 为合数，随机选取的底至多以 $1/4$ 的概率瞒过它，独立做 $k$ 轮误判概率降到 $(1/4)^k$。本章用它作为概率方法最干净的例子，说明那个误差界本身是被严格证明的定理，放弃的是确定性的种类而非严格性。
20. R. Solovay & V. Strassen (1977).「A Fast Monte-Carlo Test for Primality」. SIAM Journal on Computing, 6(1). doi:[10.1137/0206006](https://doi.org/10.1137/0206006) [②④]
   索洛维与施特拉森更早提出一个基于雅可比符号的概率素性检验，单轮误判概率至多 $1/2$，是随机化算法的奠基工作之一。本章把它与拉宾的版本并置，说明用概率方法换取在预算内可交付的判定，在计算数论里早有先例。
21. W. P. Thurston (1994).「On Proof and Progress in Mathematics」. Bulletin of the American Mathematical Society, 30(2). doi:[10.1090/s0273-0979-1994-00502-6](https://doi.org/10.1090/s0273-0979-1994-00502-6) [①③]
   瑟斯顿主张数学真正推进的是人类对数学的理解，而不只是形式证明的库存，证明只是社群传递与确认理解的一种社会化手段。本章末尾援引它来挑战「数学只等于已证定理」的窄化看法，是反思证明地位的必读文献。
22. A. Jaffe & F. Quinn (1993).「"Theoretical Mathematics": Toward a Cultural Synthesis of Mathematics and Theoretical Physics」. Bulletin of the American Mathematical Society, 29(1). doi:[10.1090/s0273-0979-1993-00413-0](https://doi.org/10.1090/s0273-0979-1993-00413-0) [①③]
   贾菲与奎因提出区分「理论数学」与严格数学，建议把猜想驱动、未经严格证明的工作明确标注出来，以免侵蚀数学的可靠性，由此引发数学界一场广受关注的争论。本章借这场争论提问：证据先行的工作在多大程度上算数学，正切中全书对验证与信念的关切。
23. J. von Neumann (1947).「The Mathematician」. 收于 R. B. Heywood（编）,《The Works of the Mind》. University of Chicago Press. [Google Books](https://books.google.com/books?id=w4wjMwEACAAJ) [①③]
   冯·诺依曼在这篇随笔里反思数学的本性，谈数学如何在抽象与经验源头之间往返，又如何凭审美标准选择方向以及为何远离经验源头会有退化的风险。它从一位横跨多领域的大家视角，说明数学判断中审美与品味的分量，呼应本章对数学家如何决定往哪使劲的讨论。
24. K. Appel & W. Haken (1977).「Every Planar Map Is Four Colorable, Part I: Discharging」. Illinois Journal of Mathematics, 21(3). doi:[10.1215/ijm/1256049011](https://doi.org/10.1215/ijm/1256049011) [②③]
   阿佩尔与哈肯借助大量计算机检查的不可避免构形集，证明了四色定理，这是首个本质依赖计算机的著名数学证明。它引出了一个延续至今的争论：人类无法逐行通读的证明是否仍算证明，与本章对证书与可机械复核保证的讨论直接相关。
25. T. Hales et al. (2017).「A Formal Proof of the Kepler Conjecture」. Forum of Mathematics, Pi, 5. doi:[10.1017/fmp.2017.1](https://doi.org/10.1017/fmp.2017.1) [②③④]
   黑尔斯团队的 Flyspeck 项目用 HOL Light 与 Isabelle 证明助手，完成了开普勒猜想的完全形式化、可机械核对的证明，了结了原证明因人工裁判难以彻底检验而悬而未决的状态。本章用它说明形式化验证如何把有争议的论证压成逐行可验的证书。
26. N. Alon & J. H. Spencer (1992).《The Probabilistic Method》. Wiley. [Google Books](https://books.google.com/books?id=q3lUjheWiMoC) [②④]
   这本经典系统呈现了埃尔德什开创的概率方法：要证某个组合对象存在，便证它随机出现的概率为正，从而断定它必然存在，却往往无法把它具体构造出来。本章借它点出概率方法在纯数学中证明存在性时存在被证明、构造却缺席的特征。
27. P. J. Davis & R. Hersh (1981).《The Mathematical Experience》. Birkhäuser. [Google Books](https://books.google.com/books?id=kcN5PwAACAAJ) [①③]
   戴维斯与赫什从数学家的实际经验出发，讨论数学对象的存在地位、证明的角色与数学的哲学处境，呈现了一种不同于形式主义教条的从业者视角。它为本章理解数学家如何在实践中持有信念、看待真理提供了贴近现场的反思。
28. W. T. Gowers (2000).「The Two Cultures of Mathematics」. 收于《Mathematics: Frontiers and Perspectives》. American Mathematical Society. [链接](https://www.dpmms.cam.ac.uk/~wtg10/2cultures.pdf) [①③]
   高尔斯区分数学中的两种文化：理论构建者与问题解决者，前者以理解为目的去解题，后者以解题为目的去理解，并以代数几何、朗兰兹纲领与组合数论为对照。它说明数学家对何谓深刻、何谓好工作可有不同尺度，呼应本章对数学判断标准的讨论。
29. T. Tao (2007).「What Is Good Mathematics?」. Bulletin of the American Mathematical Society, 44(4). doi:[10.1090/s0273-0979-07-01168-8](https://doi.org/10.1090/s0273-0979-07-01168-8) [①③]
   陶哲轩列举了好数学的众多互不相同的维度，从严格、深刻、漂亮到富于应用、能开辟方向等，论证不存在单一标准，且这些品质长期看往往彼此牵引。本章借它说明判断一项工作值不值得投入本身就是一种能力，其中没有一条标准是已被证明。
30. H. L. Montgomery (1973).「The Pair Correlation of Zeros of the Zeta Function」. 收于《Analytic Number Theory》, Proc. Sympos. Pure Math., XXIV. American Mathematical Society. doi:[10.1090/pspum/024/9944](https://doi.org/10.1090/pspum/024/9944) [②③]
   蒙哥马利研究 ζ 零点归一化后的配对关联，得出并猜想其形式，戴森随即认出这正是随机矩阵高斯酉系综本征值的配对关联。这一对接开启了数论与随机矩阵理论的深刻联系，是本章谈 RH 信念何以建立的关键证据之一。
31. P. Sarnak (2004).「Problems of the Millennium: The Riemann Hypothesis」. Clay Mathematics Institute. [链接](https://www.claymath.org/library/annual_report/xSarnak_RH.pdf) [②③④]
   萨纳克为克雷研究所撰写的这份说明侧重 RH 的推广形式及其在解析数论中的中心作用，并解释为何众多其他结果以它为前提。它从一位活跃于零点统计与随机矩阵联系的专家视角，补足了本章对 RH 重要性与证据网络的理解。
32. J. C. Lagarias (2002).「An Elementary Problem Equivalent to the Riemann Hypothesis」. The American Mathematical Monthly, 109(6). doi:[10.1080/00029890.2002.11919883](https://doi.org/10.1080/00029890.2002.11919883) [②④]
   拉加里亚斯给出一个仅用调和数与因子和函数的初等不等式，证明它对所有 $n$ 成立当且仅当 RH 成立，把深奥的零点问题翻译成几乎能写在明信片上的算术陈述。本章用它示范代理替换可以表面初等，难度却分毫未减。
33. A. M. Odlyzko (1987).「On the Distribution of Spacings Between Zeros of the Zeta Function」. Mathematics of Computation, 48(177). doi:[10.1090/s0025-5718-1987-0866115-0](https://doi.org/10.1090/s0025-5718-1987-0866115-0) [②④]
   奥德利兹科用海量高精度计算考察 ζ 零点的间距分布，发现它与随机矩阵高斯酉系综的预言惊人吻合，为蒙哥马利-戴森的猜想提供了强有力的数值支持。本章用它说明这种统计契合虽非证明，却是让数学家相信 RH 的极强证据。
