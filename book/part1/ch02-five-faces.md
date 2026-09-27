# 第 2 章　不可验证的五种处境

> **论点**：「我无法检验它」这句话之下，掩盖着五种结构不同的处境；将它们混为一谈，是这一领域的核心错误。

「我无法检验它」这句话，听起来描述的是一种处境，实际上却涵盖了五种。它们的结构各不相同，有效的补救也各不相同。将它们混为一谈，是这一领域最核心的错误。

本章的任务，是把这五种处境逐一区分开来，并对每一种作出准确的刻画。这看起来不过是分类上的洁癖，全书后半部分的可信度却系于此。本书最终要论证的是：不可验证性的来源尽管千差万别，应对的办法却收敛到同一小组对策上。要使这一论断不致流于廉价，就必须先把「千差万别」坐实。差异阐明得越透彻，其后的收敛就越出人意料，也越需要解释。读者不妨把这五种处境记在心上，全书将一再回到它们。

![不可验证的五种处境：判据与补救各不相同](../figures/f02-five-faces.svg)

## 第一种：不可判定

判据：在原则上就不存在判定它的算法。问题不在于难，而在于没有。

这是验证最彻底的一种失败。1928 年，希尔伯特与阿克曼<sup class="cite"><a href="#ref-4">4</a></sup>明确提出了判定问题（Entscheidungsproblem）：是否存在一个机械程序，能够对任意数学命题判定其真伪？八年之后，丘奇<sup class="cite"><a href="#ref-2">2</a></sup>借助 lambda 演算，图灵<sup class="cite"><a href="#ref-1">1</a></sup>借助他所设想的抽象机器，各自证明了答案是否定的。图灵的停机问题（halting problem）表述得尤为简洁：不存在这样一个算法，它对任意一组「程序加输入」都能判定该程序是否会停机。属于同一谱系的，还有哥德尔 1931 年<sup class="cite"><a href="#ref-3">3</a></sup>证明的不完备性（incompleteness）、莱斯定理<sup class="cite"><a href="#ref-6">6</a></sup>（Rice's theorem，程序的任何非平凡语义性质都不可判定），以及马季亚谢维奇 1970 年<sup class="cite"><a href="#ref-7">7</a></sup>对希尔伯特第十问题给出的否定回答。这些结果并非纸上空谈。「这段程序是否会做坏事」这一问题可以归约为停机问题，因此在理论上不存在一款能够毫无差错地查出所有恶意程序的杀毒软件。这是逻辑为整个反病毒行业划定的上限。

这种处境的补救有一个独有的性质：它永远不会有完整的解。再多的时间、再快的机器都无济于事，因为障碍在于逻辑，而不在于资源。所能做的只有退而求其次：验证有限的局部，或者把自己限制在确实可以判定的片段之内（例如只含加法的算术）。这一点在第 7 章中还将反复出现。

## 第二种：难解

判据：算法存在，但其代价随规模爆炸式增长，大到在实践中无法算完。

这一种处境与上一种差之毫厘，谬以千里：它可以判定，却不可行。库克于 1971 年<sup class="cite"><a href="#ref-8">8</a></sup>、列文于 1973 年<sup class="cite"><a href="#ref-9">9</a></sup>各自确立了 NP 完全性（NP-completeness），卡普则在 1972 年<sup class="cite"><a href="#ref-10">10</a></sup>列出了著名的二十一个 NP 完全问题；这些工作共同为这一处境提供了精确的刻画。可满足性问题（satisfiability）以及无数组合优化问题，在原则上都有解法，但这些解法在最坏情形下的耗时，随输入规模呈指数增长，

$$T(n)\sim 2^{n},$$

只需几十个变量，就足以令最快的超级计算机望洋兴叹。不妨从数量级上获得一点直观印象：国际象棋的博弈树约有 $10^{120}$ 个分支（香农数），围棋的合法局面约有 $2\times10^{170}$ 个，而整个可观测宇宙中的原子数也不过约 $10^{80}$ 个。这些棋类规则简单，在原则上可以穷举，但这个「原则上」远远超出了物理上的可能。$\mathsf{P}$ 是否等于 $\mathsf{NP}$，所追问的就是这堵墙是否注定存在。

它的补救与不可判定（undecidable）截然不同。在这里，投入更多资源是有意义的。更重要的是，可以用「接受得少一些」换取「负担得起的代价」：以近似解代替精确解，以平均情形代替最坏情形，此外还有启发式搜索与随机化。难解（intractable）催生了一整套「打折」的智慧，而这在不可判定的处境中是不存在的。

## 第三种：部分可观测

判据：验证所依据的状态，对你隐而不见。

这里的困难不在于缺乏判定程序，也不在于代价过高，而在于看不到应当看到的东西。用户真正的偏好，病人体内正在发生的变化，对手手中的牌，这些状态驱动着结果，却不向观察者显现。控制论很早就对这一处境作了形式化的处理。1965 年，阿斯特罗姆<sup class="cite"><a href="#ref-15">15</a></sup>研究了状态信息不完整时的最优控制问题；斯莫尔伍德与桑迪克在 1973 年<sup class="cite"><a href="#ref-16">16</a></sup>、凯尔布林等人在 1998 年<sup class="cite"><a href="#ref-18">18</a></sup>，又先后把它发展为部分可观测马尔可夫决策过程（POMDP）这一标准框架。此外，帕帕季米特里乌与齐齐克利斯于 1987 年<sup class="cite"><a href="#ref-17">17</a></sup>证明，这类问题的求解同样是难解的。因此，第三种处境常常与第二种叠加在一起。

它的补救自成一类：不再追求一个确定的判决，而是维持一个关于隐藏状态的信念分布（belief state），并以每一次观测对其加以更新，

$$b'(s')\ \propto\ \Pr(o\mid s')\sum_{s}\Pr(s'\mid s,a)\,b(s).$$

这一处境的补救在于推断与探查，而不在于一味追加算力。第 5 章通篇都在这种处境之中展开。

## 第四种：预算受限

判据：在原则上可以验证、可以求解，但就这一主体而言，此时此地缺乏所需的时间、算力或样本。

这一种处境最为朴素，也最为普遍。审稿人只有二十分钟阅读一篇论文；医生只有几分钟作出诊断；交易员必须在行情消失之前下单。验证在理论上完全可行，落到一个有限的主体身上却无法实现。这一处境的思想渊源，可以追溯到奈特 1921 年<sup class="cite"><a href="#ref-19">19</a></sup>对风险与不确定性的区分，以及西蒙 1955 年<sup class="cite"><a href="#ref-20">20</a></sup>提出的有限理性（bounded rationality）。其后的研究为它提供了形式化的表述：迪安与博迪在 1988 年<sup class="cite"><a href="#ref-22">22</a></sup>提出随时算法（anytime algorithm，可以随时中断，并给出当前的最优解）；罗素与苏布拉马尼安则在 1995 年<sup class="cite"><a href="#ref-23">23</a></sup>提出了「有界最优」（bounded optimality）的概念。

它的补救具有一个其他处境所没有的特征：这种处境会随资源的增加而消退，只要时间与算力充足，它便不复存在。因此，应对它的关键在于分配，即把稀缺的预算投向边际收益最高之处。后文将要讨论的「最优筛查」这一对策，就源于这一思路。

## 第五种：对抗

判据：你所面对的系统，在主动挫败你的验证。

在前四种处境中，困难都来自世界的某种中立属性：逻辑、规模、可见性或资源。第五种则不同：对方是一个具有智能的行动者，它针对你的检查进行优化。会说谎的对手，会伪装的恶意代码，会操纵指标的被考核者，都属于这种情形。这一处境的经典理论，包括冯·诺依曼与摩根斯特恩 1944 年<sup class="cite"><a href="#ref-24">24</a></sup>的博弈论（game theory），以及随后瓦尔德 1945 年<sup class="cite"><a href="#ref-26">26</a></sup>的极小极大准则（minimax）和纳什 1950 年<sup class="cite"><a href="#ref-25">25</a></sup>的均衡（Nash equilibrium）。在机器学习中，它的当代形态是塞盖迪等人 2014 年<sup class="cite"><a href="#ref-29">29</a></sup>发现的对抗样本（adversarial examples），以及马德里等人 2018 年<sup class="cite"><a href="#ref-31">31</a></sup>用以统一攻防双方的鲁棒优化（robust optimization）。一个识别率极高的模型，可能被人眼无法察觉的微小扰动彻底误导，原因在于有人专门去寻找那个扰动。研究者做过一个被反复复现的演示：在停车标志上贴几张精心设计、形似涂鸦的小贴纸，就能使顶尖的图像识别系统稳定地将其识别为限速标志。同一块标志，人看到的是「停」，机器看到的却是「行」，差别仅在于对手把贴纸贴在了哪里。

它的补救属于战略，而不属于计算。与其把某个量算得更准，不如求解

$$\min_{x}\ \max_{y}\ L(x,y),$$

也就是按最坏情形布防，借助随机化使对手无从预测，追求的是在博弈中站得住脚，而不是在某个固定输入上达到最优。把对抗（adversarial）当作单纯的可观测缺口（「我只是还没看清它」）来处理，是可能酿成致命后果的误判，因为另一方的系统会根据你的判断调整自身。

## 五种处境，五种补救

将五种处境并列比较，要紧的不是名称，而是补救：适用于一种处境的补救，移用到另一种处境上并不奏效。

- 不可判定：永远没有完整的解，只能退而验证有限的局部。
- 难解：可以用代价换取精度，投入更多资源是有意义的。
- 部分可观测：依靠推断信念与主动探查。
- 预算受限：随资源增加而消退，关键在于分配。
- 对抗：本质上是一场博弈，依靠战略与随机化。

倘若有人断言「这件事多投入一些算力就能解决」，他多半是把一种处境错认成了另一种。把不可判定当作预算问题，把对抗当作可观测问题，都属于这类错认，而且代价高昂。

这些处境还会相互叠加与复合。第 6 章讨论的那个放出去的智能体，既面临开放世界的不可预测性（近乎不可判定的行为），又面临对手的策略性（对抗）；第 8 章讨论的组织，则须同时应对部分可观测与对抗。现实中的处境，往往是几种处境的混合。

正因为来源如此参差、补救如此各异，下一个问题便显得格外尖锐：人类是否拥有一套成熟的方法，能够长期地、有纪律地与不可验证性共处？答案是肯定的。这套方法就是科学，而它的首要原则，便是公开承认自己永远无法验证。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实。

### 不可判定（②③）

1. A. M. Turing (1936).「On Computable Numbers, with an Application to the Entscheidungsproblem」. Proceedings of the London Mathematical Society, s2-42(1), 230-265. doi:[10.1112/plms/s2-42.1.230](https://doi.org/10.1112/plms/s2-42.1.230) [②③]
   图灵在此引入「可计算数」与抽象计算机器的概念，并由停机问题的不可解推出判定问题没有机械解法。这篇论文是「不可判定」这种处境最干净的样板：障碍是逻辑的而非资源的，本章正以图灵机器与停机问题作为该种处境的标准例证。
2. A. Church (1936).「An Unsolvable Problem of Elementary Number Theory」. American Journal of Mathematics, 58(2), 345-363. doi:[10.2307/2371045](https://doi.org/10.2307/2371045) [②③]
   丘奇用他发展的 lambda 演算证明初等数论中存在不可解问题，从而独立地否决了判定问题，发表上还早于图灵约七个月。它与图灵的结果互为印证，共同坐实了「原则上就不存在判定算法」并非个别现象，本章把两者并列为不可判定一族的开端。
3. K. Gödel (1931).「Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I」. Monatshefte für Mathematik und Physik, 38, 173-198. doi:[10.1007/bf01700692](https://doi.org/10.1007/bf01700692) [②③]
   哥德尔在此证明不完备性定理：任何足够强的一致形式系统中都存在既不能证明也不能否证的命题。它是不可判定谱系的源头，表明形式方法本身有原则上的极限，本章把它列为这种处境最早的一记警钟。
4. D. Hilbert & W. Ackermann (1928).《Grundzüge der theoretischen Logik》. Springer. [Google Books](https://books.google.com/books?id=fRn8wAEACAAJ) [②③]
   这本数理逻辑教科书第一次明确提出判定问题，即追问是否存在一个机械程序，能对任意数学命题判定真伪。正是这个问题催生了丘奇与图灵的否定证明，本章以它作为不可判定处境的出发点，读者可借此看清当年的乐观期待与随后的逻辑碰壁。
5. E. L. Post (1944).「Recursively Enumerable Sets of Positive Integers and Their Decision Problems」. Bulletin of the American Mathematical Society, 50(5), 284-316. doi:[10.1090/s0002-9904-1944-08111-1](https://doi.org/10.1090/s0002-9904-1944-08111-1) [②③]
   波斯特在此系统研究递归可枚举集及其判定问题，并提出后来催生不可解度理论的思路。它把「不可判定」从单个问题推进到对不可解性结构的分级研究，本章引它说明该种处境有自身的层次与谱系，而非铁板一块。
6. H. G. Rice (1953).「Classes of Recursively Enumerable Sets and Their Decision Problems」. Transactions of the American Mathematical Society, 74(2), 358-366. doi:[10.1090/s0002-9947-1953-0053041-6](https://doi.org/10.1090/s0002-9947-1953-0053041-6) [②]
   莱斯定理在此确立：程序所计算的任何非平凡语义性质都不可判定。它把图灵式的不可判定从个别问题推广为一条普遍铁律，本章引它说明，想机械地验证程序「做的对不对」这类问题，原则上就堵死了。
7. Y. V. Matiyasevich (1970).「Enumerable Sets Are Diophantine」. Soviet Mathematics. Doklady, 11(2), 354-357. [链接](https://www.mathnet.ru/eng/dan35274) [②③]
   马季亚谢维奇在此补上最后一环，证明每个递归可枚举集都是丢番图集，由此完成希尔伯特第十问题不可解的证明，即 MRDP 定理。它说明连「丢番图方程有无整数解」这样具体的数学问题都没有判定算法，本章引它佐证不可判定并不限于自指或元数学，而是渗进了寻常数学。

### 难解（②③）

8. S. A. Cook (1971).「The Complexity of Theorem-Proving Procedures」. Proceedings of the 3rd Annual ACM Symposium on Theory of Computing (STOC), 151-158. doi:[10.1145/800157.805047](https://doi.org/10.1145/800157.805047) [②③]
   库克在此开创 NP 完全性概念，证明可满足性问题是 NP 中最难的一类。它给「难解」这种处境下了精确定义：问题有解法，代价却随规模爆炸。本章以它划清第二种与第一种的界限，即「可判定却不可行」不同于「根本没有算法」。
9. L. A. Levin (1973).「Universal Sequential Search Problems」. Problems of Information Transmission, 9(3), 265-266. [链接](https://www.mathnet.ru/eng/ppi914) [②③]
   列文在铁幕另一侧独立得到与库克相同的结果，给出通用搜索问题的完全性刻画，两者合称 Cook-Levin 定理。它说明 NP 完全性的发现是收敛而非偶然，本章引它强化「难解」这种处境的客观性：这是问题结构本身的性质，不因研究路径而异。
10. R. M. Karp (1972).「Reducibility Among Combinatorial Problems」. In R. E. Miller & J. W. Thatcher (Eds.),《Complexity of Computer Computations》(pp. 85-103). Plenum Press. doi:[10.1007/978-1-4684-2001-2\_9](https://doi.org/10.1007/978-1-4684-2001-2_9) [②③]
   卡普用多项式归约证明了二十一个常见组合问题都是 NP 完全的，把库克的单个结果扩展成一张相互归约的网。它表明难解不是个别难题的怪癖，而是横跨调度、划分、覆盖等大量实际问题的普遍现象，本章引它说明这种处境在工程中无处不在。
11. J. Hartmanis & R. E. Stearns (1965).「On the Computational Complexity of Algorithms」. Transactions of the American Mathematical Society, 117, 285-306. doi:[10.1090/s0002-9947-1965-0170805-7](https://doi.org/10.1090/s0002-9947-1965-0170805-7) [②]
   这篇论文用图灵机的运行时间为算法定级，奠定了按资源消耗划分复杂度类的框架，「计算复杂度」一词也由此确立。它提供了度量「难解」所必需的标尺，本章引它说明第二种处境之所以能被精确谈论，前提是先有了刻画代价随规模如何增长的语言。
12. M. R. Garey & D. S. Johnson (1979).《Computers and Intractability: A Guide to the Theory of NP-Completeness》. W. H. Freeman. [Google Books](https://books.google.com/books?id=fjxGAQAAIAAJ) [②]
   这本书系统整理了 NP 完全性理论与证明技巧，并附上一份广为引用的难解问题清单，长期被当作该领域的标准参考。对想由头了解「难解」这种处境的读者，它既是入门指南也是工具书，本章把它列为该主题最可靠的落脚处。
13. M. Sipser (2012).《Introduction to the Theory of Computation》(3rd ed.). Cengage Learning. [Google Books](https://books.google.com/books?id=H94JzgEACAAJ) [②]
   这本广受采用的本科教材清晰讲解自动机、可计算性与复杂度，把图灵机、停机问题、P 与 NP 等概念串成一条连贯的线。它正好覆盖本章前两种处境的理论底子，是想从头打基础的读者最稳妥的起点，初版可上溯到 1997 年。
14. S. Arora & B. Barak (2009).《Computational Complexity: A Modern Approach》. Cambridge University Press. doi:[10.1017/cbo9780511804090](https://doi.org/10.1017/cbo9780511804090) [②]
   这本研究生教材覆盖了从经典复杂度类到随机化、交互证明、近似与去随机化等现代主题，视野远超入门教科书。对想深入「难解」这种处境，尤其想理解人们如何用近似与随机绕开最坏情形的读者，它是更进一步的权威读物。

### 部分可观测（②④）

15. K. J. Åström (1965).「Optimal Control of Markov Processes with Incomplete State Information」. Journal of Mathematical Analysis and Applications, 10, 174-205. doi:[10.1016/0022-247x(65)90154-x](https://doi.org/10.1016/0022-247x%2865%2990154-x) [②]
   阿斯特罗姆在此研究状态信息不完整下的最优控制，提出用关于隐藏状态的概率分布即「信念状态」来概括所有可得信息。这是 POMDP 理论的源头之一，也正是本章为「部分可观测」开出的解药：不追求确定判决，而是维持并更新一个信念。
16. R. D. Smallwood & E. J. Sondik (1973).「The Optimal Control of Partially Observable Markov Processes over a Finite Horizon」. Operations Research, 21(5), 1071-1088. doi:[10.1287/opre.21.5.1071](https://doi.org/10.1287/opre.21.5.1071) [②]
   这篇论文给出有限时域 POMDP 的经典结构性结果，并据此设计出可计算最优策略的方法。它把阿斯特罗姆的信念状态思想推进为可操作的算法，本章引它说明「靠推断信念」并非空话，而有成形的求解技术支撑。
17. C. H. Papadimitriou & J. N. Tsitsiklis (1987).「The Complexity of Markov Decision Processes」. Mathematics of Operations Research, 12(3), 441-450. doi:[10.1287/moor.12.3.441](https://doi.org/10.1287/moor.12.3.441) [②]
   这篇论文系统刻画了马尔可夫决策过程各变体的计算复杂度，证明引入部分可观测会让求解显著变难。它把第三种与第二种处境扣在一起：看不见正确状态的处境，求解本身往往又是难解的，本章正以此说明处境会彼此叠加。
18. L. P. Kaelbling, M. L. Littman & A. R. Cassandra (1998).「Planning and Acting in Partially Observable Stochastic Domains」. Artificial Intelligence, 101(1), 99-134. doi:[10.1016/s0004-3702(98)00023-x](https://doi.org/10.1016/s0004-3702%2898%2900023-x) [②④]
   这篇论文把 POMDP 整理为人工智能里的标准框架，统一了信念更新、规划与行动，并给出可实践的算法。它是「部分可观测」处境最常被引用的代表性文献，本章第 5 章对该种处境的展开正以此为底本，读者可由它系统了解推断加探查的整套做法。

### 预算受限（①④，含有限理性与 anytime 算法）

19. F. H. Knight (1921).《Risk, Uncertainty and Profit》. Houghton Mifflin. [Google Books](https://books.google.com/books?id=XrcJAAAAIAAJ) [①④]
   奈特在此区分可用概率刻画的「风险」与无法量化的「不确定性」，后者即没有可靠概率可依的处境。这一区分是本书谈不可验证的思想起点之一，它提醒读者：有些处境的难处不在算得不够准，而在连下注所需的概率都不存在。
20. H. A. Simon (1955).「A Behavioral Model of Rational Choice」. The Quarterly Journal of Economics, 69(1), 99-118. doi:[10.2307/1884852](https://doi.org/10.2307/1884852) [①④]
   西蒙在此提出有限理性：真实主体的算力、时间与信息都有限，于是不去求全局最优，而是「满意即止」。这是「预算受限」处境的概念源头，本章借它点明，许多验证在理论上可行，落到一个有限的主体身上却必须打折，从而引出后面关于预算分配的思路。
21. M. Boddy & T. Dean (1989).「Solving Time-Dependent Planning Problems」. Proceedings of the 11th International Joint Conference on Artificial Intelligence (IJCAI). [链接](https://www.ijcai.org/Proceedings/89-2/Papers/021.pdf) [②④]
   这篇论文延续作者的随时算法工作，研究如何在计算时间本身受限时安排规划，让系统随时可中断并交出当前最优解。它与下一条同源，本章引这一系列工作来说明「预算受限」处境的应对核心是把有限的时间花在边际收益最高处。
22. T. Dean & M. Boddy (1988).「An Analysis of Time-Dependent Planning」. Proceedings of the 7th National Conference on Artificial Intelligence (AAAI), 49-54. [链接](https://cdn.aaai.org/AAAI/1988/AAAI88-009.pdf) [②④]
   这篇论文正式提出随时算法的概念：算法可在任意时刻被打断并给出当前最优解，质量随计算时间稳步提升。它是「预算受限」处境的代表性形式化，本章引它说明这种处境的独特之处在于会随资源增长而消退，因而应对的关键落在分配而非纯算力。
23. S. J. Russell & D. Subramanian (1995).「Provably Bounded-Optimal Agents」. Journal of Artificial Intelligence Research, 2, 575-609. doi:[10.1613/jair.133](https://doi.org/10.1613/jair.133) [②④]
   这篇论文把有限理性形式化为「有界最优」：不再要求智能体输出最优决策，而是要求它在给定的计算资源约束下做到所能做的最好。它给西蒙的直觉提供了精确定义，本章引它说明「预算受限」处境也能被严肃地理论化，而非只是无可奈何的妥协。

### 对抗（②①④，含决策论与对抗机器学习）

24. J. von Neumann & O. Morgenstern (1944).《Theory of Games and Economic Behavior》. Princeton University Press. [Google Books](https://books.google.com/books?id=AzEHaJOyPNAC) [②①]
   这本书奠定了博弈论，把多方在利益冲突下的互动当作可严格分析的对象，并系统化了零和博弈的极小极大定理。它是「对抗」处境的理论源头，本章正以它支撑该种的核心主张：面对会针对你优化的对手，要按最坏情形布防，而非在某个固定输入上求最优。
25. J. F. Nash (1950).「Equilibrium Points in N-Person Games」. Proceedings of the National Academy of Sciences, 36(1), 48-49. doi:[10.1073/pnas.36.1.48](https://doi.org/10.1073/pnas.36.1.48) [②]
   纳什在这篇短文中证明，任意有限的多人博弈都存在均衡点，即没有任何一方能靠单方面改变策略获益的稳定局面。纳什均衡把博弈分析从零和推广到一般情形，本章引它作为「对抗」处境的核心概念，帮助读者理解策略性互动如何收敛到可预期的稳定结构。
26. A. Wald (1945).「Statistical Decision Functions Which Minimize the Maximum Risk」. Annals of Mathematics, 46(2), 265-280. doi:[10.2307/1969022](https://doi.org/10.2307/1969022) [②]
   瓦尔德在此奠定统计决策理论，提出以极小极大准则选择决策，即在最坏情形下使风险最小。它把「按最坏情形布防」从博弈搬进统计推断，本章引它说明对抗处境的解药是一种战略姿态：当对手会顺着你的判断调整时，求稳比求某一处的最优更要紧。
27. L. J. Savage (1954).《The Foundations of Statistics》. Wiley. [Google Books](https://books.google.com/books?id=wqzV4GoYMgEC) [②①]
   萨维奇在此为主观期望效用理论建立公理基础，论证一个理性主体的偏好可被表示为对主观概率求期望效用。它是不确定性下决策的标准框架，本章引它代表「用概率与效用为不确定性立账」的正统立场，也为下一条揭示该立场的边界做了铺垫。
28. D. Ellsberg (1961).「Risk, Ambiguity, and the Savage Axioms」. The Quarterly Journal of Economics, 75(4), 643-669. doi:[10.2307/1884324](https://doi.org/10.2307/1884324) [①④]
   埃尔斯伯格用一个简单赌局实验揭示：人们普遍回避概率本身不明的「模糊」选项，这种行为违反了萨维奇的公理。它从经验层面印证了奈特对风险与不确定性的区分，本章引它说明概率框架并非万能，有些不可验证的处境连概率都给不出。
29. C. Szegedy, W. Zaremba, I. Sutskever, J. Bruna, D. Erhan, I. Goodfellow & R. Fergus (2014).「Intriguing Properties of Neural Networks」. International Conference on Learning Representations (ICLR). [arXiv:1312.6199](https://arxiv.org/abs/1312.6199). [②]
   这篇论文首次系统揭示对抗样本：对图像施加人眼几乎察觉不到的微小扰动，就能让识别率极高的神经网络出错。它把「对抗」处境带进现代机器学习，本章引它说明，只要有人专门去找那个扰动，再准的模型也会被骗，这正是对抗不同于单纯可观测缺口的地方。
30. I. J. Goodfellow, J. Shlens & C. Szegedy (2015).「Explaining and Harnessing Adversarial Examples」. International Conference on Learning Representations (ICLR). [arXiv:1412.6572](https://arxiv.org/abs/1412.6572). [②]
   这篇论文把对抗样本归因于模型在高维空间的线性性，提出快速生成扰动的 FGSM 方法，并用对抗训练加以防御。它既解释了对抗样本为何普遍，又给出最早的应对手段，本章引它说明对抗处境的攻与防是一对此消彼长、需要持续博弈的过程。
31. A. Madry, A. Makelov, L. Schmidt, D. Tsipras & A. Vladu (2018).「Towards Deep Learning Models Resistant to Adversarial Attacks」. International Conference on Learning Representations (ICLR). [arXiv:1706.06083](https://arxiv.org/abs/1706.06083). [②④]
   马德里等人把对抗鲁棒性写成一个极小极大优化问题：内层找最坏扰动，外层训练抵御它，并以投影梯度下降作为标准攻击。它用鲁棒优化的语言统一了攻与防，正好把本章对抗处境与最坏情形决策的主张落到机器学习里，是该方向影响深远的一篇。
32. B. Biggio & F. Roli (2018).「Wild Patterns: Ten Years after the Rise of Adversarial Machine Learning」. Pattern Recognition, 84, 317-331. doi:[10.1016/j.patcog.2018.07.023](https://doi.org/10.1016/j.patcog.2018.07.023) [②]
   这篇综述回顾对抗机器学习十年的发展，指出该领域在深度学习走红前就已起步，并梳理了攻击模型、威胁建模与防御的整体脉络。对想从全局把握「对抗」处境的读者，它是权威的总览，本章引它作为该种处境最适合通读的落脚点。
