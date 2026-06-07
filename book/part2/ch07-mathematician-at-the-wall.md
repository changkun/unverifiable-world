# 第 7 章　撞墙的数学家

> **论点**：数学里你遇到最纯的不可验证（难解，有时不可判定），而有能力的应对是：验证有限切片并证明界（证书）、把目标换成等价但但愿更可解的陈述（代理替换）、用接受 ε 误差的概率方法。

## 撞墙

难题之难，常常不在它有多硬，而在你量不出自己离它还有多远。

爬山的人能看见山顶，调试程序的人能收到报错，他们至少知道方向对不对、是近了还是远了。证明一个数学猜想不给你这些。你可能离答案只剩一个念头，也可能隔着一个世纪，而手边没有任何仪表告诉你是哪一种。黎曼 1859 年那篇只有八页的论文里，把后来以他名字命名的猜想当作一句顺带的话写下，又补了一句：人们当然希望有一个严格的证明；在几次徒劳的短暂尝试之后，我暂时把这件事搁下了，因为它对我接下来的目的并非必需。这一搁，搁了一百六十多年。

这一章要看的，是数学家在这堵墙前到底做什么。我选数学作为现场，是因为它给出的，是不可验证最纯的一种形态。这里没有藏起来的状态，没有会骗你的对手，没有时间不够用的借口。命题要么真，要么假，黑白分明。然而恰恰在这个最干净的地方，验证依然系统地不可得。看清楚一个有能力的人在这里如何行动，后面那些更脏的现场（控制台前的人、放出去的智能体、看不见自己的组织）里发生的事，就有了一个参照。

## 验证的鸿沟

先把这堵墙的形状说准。

核对一个证明是容易的，找到一个证明是难的。给你一份写全的形式推导，逐行对照公理和推理规则检查，是一道机械活，原则上一台机器就能完成，而且一定能在有限步内给出是或否。找到那份推导，则是另一回事。这道不对称是整章的地基。

它有一个精确的逻辑表述。1936 年，丘奇与图灵各自证明了判定问题（Entscheidungsproblem）无解：不存在一个算法，能对任意一阶逻辑命题判定它是否逻辑有效，等价地说（凭哥德尔完备性定理），是否可证。对一个足够丰富、可递归公理化且一致的系统（比如皮亚诺算术或 ZFC），它的定理集是递归可枚举但不可递归的：你能把所有证明一条条列举出来，却没有一个程序能判定某命题不是定理。检验可判定，定理性不可判定，二者之差就是那道鸿沟。

> **深入一层（可跳过）**：「足够丰富」这个限定是吃重的。存在确实可判定的理论，普雷斯伯格算术（只有加法的自然数）、塔斯基的实闭域，在这些世界里有判定程序，凡命题皆可机械裁决。不可判定不是逻辑的普遍宿命，而是表达力到达某个门槛后的代价。RH 所在的解析数论，远在那个门槛之上。

更扎人的一层是：不仅证明搜索难，连「我是否接近」都没有判定程序。这正是 RH 折磨人的地方。它抵抗的不只是求解，还有对进度的估计。在第 2 章的五副面孔里，这一章站在「不可判定」与「难解」的交界：有些问题原则上无程序，有些有程序但代价大到不可能在宇宙寿命内跑完。墙后面是什么，你看不见。于是有能力的人不再正面凿墙，他们改换姿势。下面三种姿势，会反复出现在本书别的章里，只是换了名字。

## 证书与界

第一种姿势：不再验证整体，只验证一个切片，并为它证一个有保证的界。

回到 ζ 函数。黎曼把欧拉的素数级数延拓成整个复平面上的函数，写下它的完备形式

$$\xi(s) = \tfrac{1}{2}\,s(s-1)\,\pi^{-s/2}\,\Gamma\!\left(\tfrac{s}{2}\right)\zeta(s),\qquad \xi(s)=\xi(1-s).$$

这个对称的函数方程把临界带左右对折。猜想说的是：$\zeta$ 的全部非平凡零点都落在临界线 $\operatorname{Re}(s)=\tfrac12$ 上（平凡零点在负偶数处）。全部，这个量词是无法验证的所在。

但有限多个零点可以验证。这里要分清两件常被混为一谈的事。古尔东在 2004 年算出了头 $10^{13}$ 个零点都在线上，这是一次数值计算，用的是高精度浮点，给人极强的信心，却不是一张证书：它没有把舍入误差严格框住。普拉特 2017 年做的是另一回事，他用区间算术，把虚部直到约 $3.06\times10^{10}$ 高度的所有零点严格地锁在临界线上；普拉特与特鲁吉安 2021 年把这个严格高度推到 $3\times10^{12}$。后两者是证书：一个有界的、局部的、可机械复核的保证。它为真，但它不是定理。零点验到再高，也跨不过「全部」那道坎。

这种姿势在数学里有它体面的先例。1896 年，阿达马与德拉瓦莱普桑各自证明了素数定理 $\pi(x)\sim x/\ln x$，靠的是一个比 RH 弱得多、却够得着的界：$\zeta$ 在直线 $\operatorname{Re}(s)=1$ 上不取零。证不了零点都在 $\tfrac12$，那就先证它们都不在 $1$。这是用一个能证的弱命题，换取通往强命题路上的一段实在进展。

同一种姿势横跨到软件里，面目立刻熟悉。类型系统不证明程序「全对」，它只证明某一条性质（不会把整数当指针解引用），换来的是可判定的检查。形式化验证走得更远，黑尔斯团队在 2017 年完成了开普勒猜想的机器可核对证明，把一个连人类裁判都吵了多年的论证，压成一份逐行可验的证书。代价向来一致：证书买到的是一个切片上的确定，赌上的是普遍性。切片不是定理。于是有人转而去动那个目标本身。

## 代理替换

第二种姿势：别再死守原来的命题，把它换成一个等价、但但愿更好对付的陈述。

RH 的等价改写多得惊人。李建军 1997 年给出一个判据：RH 成立，当且仅当一列实数 $\lambda_n\ge 0$ 对所有 $n\ge1$ 成立，其中

$$\lambda_n=\sum_{\rho}\left[1-\left(1-\tfrac{1}{\rho}\right)^{n}\right],$$

求和取遍非平凡零点。一个关于零点位置的几何陈述，被翻译成一列数的正性。奈曼与博伊林给出另一个：RH 等价于示性函数 $\chi_{(0,1)}$ 落在一族被伸缩的小数部分函数张成的 $L^2(0,1)$ 闭包里，把零点问题翻译成一个逼近问题；巴埃斯-杜阿尔特 2003 年把它收紧成只用整数伸缩的序列版本，对应一列距离 $d_n\to0$。拉加里亚斯 2002 年甚至给出一个初等到能写在明信片上的等价：对所有 $n$，$\sigma(n)\le H_n+\exp(H_n)\ln H_n$，其中 $H_n$ 是调和数，$\sigma$ 是因子和。

我自己也在这条路上走过一程。把 RH 搬进李判据、搬进奈曼-博伊林-巴埃斯-杜阿尔特的逼近框架、再搬进算子谱与随机过程的语言，每一次都怀着同一个指望：换一种语言，也许困难就在新坐标里露出一个把手。每一次得到的诚实结论也都一样，等价是真的，难度一分没少。我没有把问题解开，我只是把它改了个名字换了身衣服。

这就是代理替换在数学里的标准败法，值得给它起个准名字：一个忠实却不更易的代理。等价保证了它指向的还是同一个真目标（忠实），可它一点没比原问题更可解（不更易）。这一招的成败，全压在能不能同时拿到忠实与更易这两样上，而二者兼得极其罕见。罕见到，那正是全部的手艺所在。

把这两个维度摊成一张表，本章埋的一根线就显出来了：

|        | 更易                          | 不更易                              |
| ------ | --------------------------- | -------------------------------- |
| **忠实** | 理想代理（罕见，手艺全在此）              | 数学的等价改写：你只是把困难改了名（本章）            |
| **不忠实** | Goodhart：你优化代理，真目标却烂掉（第 8、11 章） | 无用，没人会要                         |

数学家栽在左下到右上的对角线左端：忠实但不更易。后面看组织那一章，会栽在另一端：一个更易却不忠实的代理，你拼命优化它，真正在意的东西反而坏掉。同一招，两个相反的失效方向。第 11 章会把这两端正式对接。眼下记住一点就够：换目标不是作弊，也不是出路，它是一种姿势，成不成另说。

## 概率方法

第三种姿势最违反数学的本能：不再要一个二值的判决，转而握住一个标定的概率，接受有界的出错风险去行动。

素性检验是最干净的例子。要判断一个大数是不是素数，确定性算法代价高昂；米勒-拉宾换了个问法。若 $n$ 是合数，一个随机选取的底至多以 $1/4$ 的概率被它蒙混过去，于是独立做 $k$ 轮，误判概率降到 $\le (1/4)^k$。索洛维-施特拉森更早（1977 年）给出一个误差 $\le (1/2)^k$ 的版本，拉宾的版本是 1980 年。「以 $1-\varepsilon$ 的概率为素数」是一个和「已证明为素数」根本不同的认识对象，但在工程上它足够好，而且要多好有多好，再加几轮就是了。

要紧的是看清这里到底放弃了什么。放弃的是「确定性的种类」，不是「严格性」。那个 $(1/4)^k$ 的界本身是一条定理，证得严严实实。你没有降低标准，你换了一种能在预算内交付的标准。概率方法在纯数学里同样登堂入室：埃尔德什的概率方法（Alon 与 Spencer 写成了一本经典）能证明某个对象存在，靠的是证它出现的概率为正，却始终不把那个对象拿给你看。存在性被证明了，构造却缺席。

这种姿势一路通到 RH 的信念本身。蒙哥马利 1973 年研究零点的配对关联，得出（并猜想）归一化后的零点对关联函数形如

$$R_2(u)=1-\left(\frac{\sin \pi u}{\pi u}\right)^{2}.$$

戴森在普林斯顿一眼认出，这正是随机矩阵高斯酉系综（GUE）本征值的配对关联。奥德利兹科 1987 年用海量零点做数值，把这个吻合验得令人窒息。这些都不是证明，却是极强的证据，它让数学家相信 RH，相信的方式和物理学家相信一条尚未被证伪的定律没有本质区别。数学的内部，竟也长出了一套在不可验证中形成信念的办法。

## 数学家怎么判断

于是来到这一章真正的人的部分：当神谕永远不来，有判断力的人靠什么持有信念、决定往哪使劲。

数学对外是演绎的，对内是似真的。波利亚专门写了《数学与似真推理》，讲数学家如何在没有证明时凭类比、归纳、特例去掂量一个命题的分量；阿达马调查了数学发明的心理，记下酝酿与顿悟的节律；庞加莱留下那个著名的瞬间，踏上公共马车踏板的刹那，富克斯函数与非欧几何的联系毫无征兆地涌上心头。这些不是证明的替代品，而是证明之前那段没有仪表的路上，人实际依赖的东西。

为什么数学家在证明出现之前就相信 RH？因为证据在各个方向上累积并互相印证：海量零点验在线上；众多等价形式没有一个垮掉；它的类比版本已被攻克（韦伊猜想，即函数域上的黎曼假设，被德利涅证明）；统计行为精确符合随机矩阵的预言。没有哪一条是证明，合在一起却构成一种有纪律的信念。

数学界自己也反思过这种信念的地位。瑟斯顿 1994 年的《论数学中的证明与进展》主张，数学推进的是人类的理解，而不只是形式证明的库存；贾菲与奎因 1993 年那场关于「理论数学」的争论，正是在问：猜想驱动、证据先行的工作，在多大程度上算数学。陶哲轩追问什么是好的数学，答案里没有一条是「已被证明」。把这些放在一起看，一个判断「某命题多半为真、值得投入」的能力，本身就是一种标定的信念，而这恰是第四部要正面命名的东西。一个有能力的主体，在神谕缺席时，并不瘫痪，也不假装确定，他持有一个标好刻度的信念，然后照样行动。

## 这一章通向哪里

撞上最纯的不可验证，数学家没有等到一个判定程序。他得到的是：证书（验一个切片、证一个界），代理替换（把目标换成等价陈述，并诚实地承认它往往忠实却不更易），概率接受（放弃二值判决、握住标定的概率行动），以及一套在证明之前持有信念的判断力。

这些都不是数学独有的应急手段。把不受信的代码关进沙箱、给一个组织做审计、在界面背后揣摩用户没说出口的偏好，伸手去够的，是同样这几样东西，只是换了行话。第三部会把每一招从它生长的领域里拎出来，单独命名、跨域并置，那张对照表是全书的载荷。

还有一句诚实话留在这里。这本书自己的核心命题，那个「应对会收敛到同一小套」的论断，我此刻也无法验证。我对它的相信，和数学家对 RH 的相信，是同一种东西：一个建立在跨域证据上、标好了刻度、却没有证明的信念。第 14 章会回到这件事，并让这本书亲自去做它一直在描述的那件事。

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
