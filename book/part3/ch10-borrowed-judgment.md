# 第 10 章　借来的判断

> **论点**：当你缺乏验证能力，就从外部引进。要么在回路里放一个可信的判断者（神谕），要么用许多互相独立的不可靠判断者、信任他们的一致（冗余／共识）。

上一对招还在自己身上想办法，缩小未知。但有时你缺的不是信息，而是判断力本身，你压根没有能力对眼前这事下一个可靠的判决。这一对招的应对是：不在自己身上找了，去别处把判断借来。借法有两种，要么引进一个你信得过的判断者（神谕），要么用许多互不信任的判断者，信任他们的一致（冗余）。

## 神谕入回路：引进一个判断者

第一招的纯形式：在你缺乏验证能力的那个决策点上，插入一个外部的判断者，由它来给出你给不出的判决。

最朴素的版本，是第 5 章那个人在回路，是专家会诊、是疑难上交。但这一招最深刻的形态，藏在两个看似无关的地方。

一处是交互式定理证明。德布鲁因 1970 年的 AUTOMATH、爱丁堡 LCF（戈登、米尔纳、沃兹沃思 1979）、到今天的 Coq（贝尔托与卡斯特朗 2004），都是同一种分工：人提供那闪光的、机器给不出的证明思路（神谕），机器则一丝不苟地核对每一步（证书检查）。神谕负责「找」，机器负责「验」，正好咬合第 2 章那道不对称。

另一处更惊人，是复杂性理论里的交互式证明。一个算力贫弱的验证者，面对一个强大却不可信的证明者，如何能问出一个它自己根本算不出的可靠答案？戈德瓦塞尔、米卡利与拉科夫 1989 年、巴拜 1985 年给出的答案是：靠反复盘问加随机挑战。验证者抛出它自己都无法预知的随机问题，证明者若在撒谎，迟早会在某个挑战上露馅。沙米尔 1992 年那个惊人的 $\mathrm{IP}=\mathrm{PSPACE}$ 表明，单靠这种「盘问一个不可信神谕」的方式，弱验证者能可靠地裁决极其庞大的一类问题；布卢姆与坎南 1995 年的「会检查自己工作的程序」、戈德瓦塞尔等人 2015 年「为凡人代理计算」，都是同一脉。这是「借来的判断」最纯的数学化：哪怕神谕不可信，只要你会聪明地盘问它，依然能榨出可靠。

统一的观念是：制造一种你单独不具备的可靠，靠引进一个外部判断者。它的标准败法也很直白：神谕本身不可靠或有偏。你引进的裁判，可能就是个错的裁判，而「谁来验证神谕」这个问题，会把你带进一段退无可退的回归。

## 冗余：从许多不可靠里合成可靠

第二招换了个方向：不引进一个可信的，而是召集许多不可信的，信任他们的一致。

它的理论根基有两块奠基石。冯·诺依曼 1956 年证明，可以用不可靠的元件，组装出任意可靠的计算，只要肯堆冗余。孔多塞 1785 年的陪审团定理给出了它的算术：若每个判断者都略好于瞎猜（正确率 $p>\tfrac12$），且彼此独立，那么多数票正确的概率会随人数趋于必然，

$$P_N\to 1\quad(N\to\infty).$$

这一招的跨域形态铺得极开。分布式系统里，它是拜占庭容错：皮斯、肖斯塔克与兰波特 1980 年、兰波特等人 1982 年的拜占庭将军问题，要在部分节点可能作恶（对抗）的情况下达成共识，经典门槛是节点数 $n\ge 3f+1$ 才能容忍 $f$ 个叛徒，卡斯特罗与利斯科夫 1999 年的 PBFT 把它做进了实用系统（费舍尔、林奇与帕特森 1985 年的不可能性定理则划出了它的边界）。机器学习里，它是集成：汉森与萨拉蒙 1990 年、迪特里希 2000 年的集成方法、布雷曼 2001 年的随机森林，用一群弱模型投票，胜过单个强模型。群体里，它是「群体的智慧」（索罗维基 2004），洪与佩奇 2004 年甚至证明，在合适条件下，多样的普通解题者群体能胜过一群高手。科学里，它是同行评审与重复实验（第 3 章）；工程里，它是 RAID 与法定人数；医疗里，它是第二诊疗意见。

但这一招有一个吃重到必须用整节强调的前提：独立。冗余只在失败去相关时才成立。把许多估计平均，方差才随人数下降，

$$\mathrm{Var}(\bar X)=\frac{\sigma^2}{N};$$

可一旦这些判断之间有正相关 $\rho$，方差就不再趋于零，而是卡在一个地板上，

$$\mathrm{Var}(\bar X)=\rho\,\sigma^2+\frac{(1-\rho)\,\sigma^2}{N}\ \xrightarrow{N\to\infty}\ \rho\,\sigma^2.$$

相关，把冗余的全部价值一笔勾销。你堆再多判断者，也跨不过这道由相关性设下的地板。这不是空谈：奈特与莱韦森 1986 年那个著名实验，让许多程序员独立地为同一规格编写程序，本指望它们的错误互不相干，结果发现他们栽在同样的地方，因为人类面对同一个难点会犯同样的错（埃克哈特与李 1985 年早有理论预言）。群体思维、同源的有缺陷训练数据、共模故障，都是这道地板的现身。这，就是冗余的标准败法：以为独立，其实相关。

## 两招的合流，与一段跨章的呼应

把两招并看：一个引进单一而昂贵的神谕，一个合成众多而廉价的独立判断，借的都是你单独不具备的判断力。它们共用的杠杆，是为自己补上缺失的验证能力；它们的败法也两两相对，单一神谕可能错，众多判断可能暗中相关。

数学里有一段插曲，恰好把这一对招、连同上一章的证书，全串了起来。阿佩尔与哈肯 1977 年的四色定理证明，因为依赖计算机的穷举而饱受争议，那等于要数学界去信任一个神谕。后来贡蒂耶 2008 年用机器可核对的形式证明重做了它，黑尔斯团队对开普勒猜想也如法炮制：把「信任神谕」转化成了「核对证书」。麦肯齐在《机械化证明》里追踪的，正是这种信任如何在人、机器与社会过程之间转移；德米洛等人那句「证明是一种社会过程」，说到底就是把数学的可信，安放在人类判断的冗余之上。

不过要看清一件事：到这里为止，前两对招，压缩未知与借来判断，都还在追求同一样东西，对象的真。它们仍想知道这事到底对不对。下一对招做了一件更彻底的事：它不再索求那个真。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实；个别未能确证者标「（细节待核）」。

1. N. G. de Bruijn (1970). 「The mathematical language AUTOMATH, its usage, and some of its extensions」. 收入《Symposium on Automatic Demonstration》. Springer (Lecture Notes in Mathematics 125), pp. 29-61. [②]
2. M. Gordon, R. Milner, C. Wadsworth (1979).《Edinburgh LCF: A Mechanized Logic of Computation》. Springer (Lecture Notes in Computer Science 78). [②]
3. Y. Bertot, P. Castéran (2004).《Interactive Theorem Proving and Program Development. Coq'Art: The Calculus of Inductive Constructions》. Springer (Texts in Theoretical Computer Science, EATCS Series). [②]
4. J. von Neumann (1956). 「Probabilistic Logics and the Synthesis of Reliable Organisms from Unreliable Components」. 收入 C. E. Shannon, J. McCarthy 编《Automata Studies》(Annals of Mathematics Studies 34). Princeton University Press, pp. 43-98. [②]
5. Marquis de Condorcet (1785).《Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix》. Imprimerie Royale, Paris. [②④]
6. S. Goldwasser, S. Micali, C. Rackoff (1989). 「The Knowledge Complexity of Interactive Proof Systems」. SIAM Journal on Computing, 18(1), pp. 186-208. [②]
7. L. Babai (1985). 「Trading Group Theory for Randomness」. 收入《Proceedings of the 17th Annual ACM Symposium on Theory of Computing (STOC)》, pp. 421-429. [②]
8. M. Pease, R. Shostak, L. Lamport (1980). 「Reaching Agreement in the Presence of Faults」. Journal of the ACM, 27(2), pp. 228-234. [②]
9. L. Lamport, R. Shostak, M. Pease (1982). 「The Byzantine Generals Problem」. ACM Transactions on Programming Languages and Systems, 4(3), pp. 382-401. [②]
10. M. J. Fischer, N. A. Lynch, M. S. Paterson (1985). 「Impossibility of Distributed Consensus with One Faulty Process」. Journal of the ACM, 32(2), pp. 374-382. [②]
11. M. Castro, B. Liskov (1999). 「Practical Byzantine Fault Tolerance」. 收入《Proceedings of the 3rd USENIX Symposium on Operating Systems Design and Implementation (OSDI)》, pp. 173-186. [②]
12. D. E. Eckhardt, L. D. Lee (1985). 「A Theoretical Basis for the Analysis of Multiversion Software Subject to Coincident Errors」. IEEE Transactions on Software Engineering, SE-11(12), pp. 1511-1517. [②]
13. J. C. Knight, N. G. Leveson (1986). 「An Experimental Evaluation of the Assumption of Independence in Multiversion Programming」. IEEE Transactions on Software Engineering, SE-12(1), pp. 96-109. [②]
14. R. A. De Millo, R. J. Lipton, A. J. Perlis (1979). 「Social Processes and Proofs of Theorems and Programs」. Communications of the ACM, 22(5), pp. 271-280. [③④]
15. A. Shamir (1992). 「IP = PSPACE」. Journal of the ACM, 39(4), pp. 869-877. [②]
16. C. Lund, L. Fortnow, H. Karloff, N. Nisan (1992). 「Algebraic Methods for Interactive Proof Systems」. Journal of the ACM, 39(4), pp. 859-868. [②]
17. M. Blum, S. Kannan (1995). 「Designing Programs That Check Their Work」. Journal of the ACM, 42(1), pp. 269-291. [②]
18. S. Arora, C. Lund, R. Motwani, M. Sudan, M. Szegedy (1998). 「Proof Verification and the Hardness of Approximation Problems」. Journal of the ACM, 45(3), pp. 501-555. [②]
19. S. Goldwasser, Y. T. Kalai, G. N. Rothblum (2015). 「Delegating Computation: Interactive Proofs for Muggles」. Journal of the ACM, 62(4), Article 27. [②④]
20. L. K. Hansen, P. Salamon (1990). 「Neural Network Ensembles」. IEEE Transactions on Pattern Analysis and Machine Intelligence, 12(10), pp. 993-1001. [②]
21. A. Krogh, J. Vedelsby (1995). 「Neural Network Ensembles, Cross Validation, and Active Learning」. 收入《Advances in Neural Information Processing Systems 7》. MIT Press, pp. 231-238. [②]
22. T. G. Dietterich (2000). 「Ensemble Methods in Machine Learning」. 收入《Multiple Classifier Systems (MCS 2000)》. Springer (Lecture Notes in Computer Science 1857), pp. 1-15. [②]
23. L. Breiman (2001). 「Random Forests」. Machine Learning, 45(1), pp. 5-32. [②]
24. L. Hong, S. E. Page (2004). 「Groups of Diverse Problem Solvers Can Outperform Groups of High-Ability Problem Solvers」. Proceedings of the National Academy of Sciences, 101(46), pp. 16385-16389. [②③④]
25. J. Surowiecki (2004).《The Wisdom of Crowds: Why the Many Are Smarter Than the Few and How Collective Wisdom Shapes Business, Economies, Societies, and Nations》. Doubleday. [③④]
26. K. Appel, W. Haken (1977). 「Every Planar Map Is Four Colorable. Part I: Discharging」. Illinois Journal of Mathematics, 21(3), pp. 429-490. [①③]
27. G. Gonthier (2008). 「Formal Proof: The Four-Color Theorem」. Notices of the American Mathematical Society, 55(11), pp. 1382-1393. [②③]
28. T. Hales 等 (2017). 「A Formal Proof of the Kepler Conjecture」. Forum of Mathematics, Pi, 5, 文章号 e2. [②③]
29. D. MacKenzie (2001).《Mechanizing Proof: Computing, Risk, and Trust》. MIT Press. [①③④]
