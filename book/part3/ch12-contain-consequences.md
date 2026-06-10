# 第 12 章　管住后果

> **论点**：当你无法防止错误，就经营它的后果。缩小一个错误的、未经验证的东西能造成的破坏（衰减，事前），并确保万一出错你会发现（留痕，事后）。

前面三对招，再放低标准，也都还在努力把事情做对。这最后一对，索性承认你做不对，转而经营失败。既然防不住错误，那就缩小它能造成的破坏（衰减，事前），并确保它一旦发生你查得到（留痕，事后）。

## 衰减：缩小爆炸半径

第一招的纯形式：放弃保证那个未经验证的东西不出错，转而把它出错时的波及范围，事前就圈死。

这是计算机安全最深的家底。萨尔策与施罗德 1975 年的最小权限（principle of least privilege）<sup class="cite"><a href="#ref-1">1</a></sup>、兰普森 1973 年的围堵（confinement）<sup class="cite"><a href="#ref-2">2</a></sup>、丹尼斯与范霍恩 1966 年的能力机制（capability）<sup class="cite"><a href="#ref-7">7</a></sup>，到丹宁 1976 年的信息流格（information flow lattice）<sup class="cite"><a href="#ref-5">5</a></sup>、贝尔-拉帕杜拉<sup class="cite"><a href="#ref-3">3</a></sup>与比巴<sup class="cite"><a href="#ref-4">4</a></sup>的安全模型，主旨一致：只给一个组件完成本职所必需的最小能力，其余一概不给，这样它就算被攻破或出错，也掀不起大浪。沙箱（sandbox，戈德堡等人 1996）<sup class="cite"><a href="#ref-9">9</a></sup>、职责分离、纵深防御，都是它的化身。系统可靠性工程里，它是熔断器与隔板（奈加德的《Release It!》<sup class="cite"><a href="#ref-15">15</a></sup>）、是爆炸半径（blast radius）设计、是金丝雀发布与错误预算（error budget，谷歌 SRE<sup class="cite"><a href="#ref-30">30</a></sup>）；金融里，它是头寸限额与止损；塔勒布的反脆弱（antifragility）<sup class="cite"><a href="#ref-17">17</a></sup>，讲的也是把下行限死。

统一的观念是：把担子从「让它不出错」（那需要你没有的验证）转移到「让它出错也扛得住」。一个常见的量化直觉是纵深防御（defense in depth），若 $k$ 层防护各自独立地以概率 $p$ 失守，全部同时失守的概率是

$$p^{k},$$

随层数指数下降。但请立刻接上第 10 章那个警告：这个 $p^k$ 只在各层失效相互独立时成立。若各层栽在同一个弱点上（同一个被绕过的内核、同一个管理员口令），相关性会让纵深防御瞬间退化成单层。2011 年的福岛核事故就是这道理的写照：电站本有主电源加备用柴油发电机的多重冗余，但一场海啸把它们一并淹没，本该相互独立的几道防线栽在同一个原因上，纵深防御形同虚设。

![纵深防御与瑞士奶酪模型：漏洞对齐，失败贯穿](../figures/f12-defense-depth.svg)

它的标准败法正是这里：被绕过的衰减。沙箱有逃逸，权限会悄悄蔓延，看似层层设防，实则各层共用一道暗门。另一种较少被提的败法是防护过度，把正常功能也堵死，结果人们反而绕过它来干活，安全反而形同虚设。

## 留痕：让错误事后现形

第二招的纯形式：防不住的，就让它一旦发生必被发现。把检查从事前改为事后。

它最硬核的技术，来自密码学。默克尔 1980 年的哈希树（Merkle tree）<sup class="cite"><a href="#ref-18">18</a></sup>、哈伯与斯托尔奈塔 1991 年的链式时间戳<sup class="cite"><a href="#ref-19">19</a></sup>，让一份记录一旦写下就无法被悄悄篡改，任何改动都会在校验时暴露；克罗斯比与瓦拉赫 2009 年的防篡改日志（tamper-evident log）<sup class="cite"><a href="#ref-23">23</a></sup>、施奈尔与凯尔西 1998 年在不可信机器上保护日志<sup class="cite"><a href="#ref-20">20</a></sup>、贝拉雷与迈纳 1999 年的前向安全签名（forward-secure signature）<sup class="cite"><a href="#ref-22">22</a></sup>，把这套做得更牢；证书透明度（Certificate Transparency，RFC 6962）<sup class="cite"><a href="#ref-24">24</a></sup>和中本聪 2008 年的比特币<sup class="cite"><a href="#ref-27">27</a></sup>，本质都是一本全球范围、只能追加、人人可验的审计账。核对一条记录是否在这样一棵树里，代价只有 $O(\log n)$，又是第 2 章那道「验比造廉」的红利。

而这一招其实古老得多。复式记账（double-entry bookkeeping）就是人类最早的防篡改账本之一，索尔在《清算》<sup class="cite"><a href="#ref-29">29</a></sup>里论证，算得清自己账目的能力，与国家的兴衰直接相关。现代财务审计、独立稽核，都是同一姿势。科学里，它是预注册（preregistration，诺塞克 2018）<sup class="cite"><a href="#ref-33">33</a></sup>与可复现（呼应第 3 章的复制危机）：把假说和方法在看到数据前就登记下来，事后无法移动靶子。

统一的观念是：放弃「事前阻止坏事」（要验证），改为「事后必能发现坏事」（只要一本忠实的账）。它的好处是双重的，既让错误可被纠正，也因为「跑不掉」而产生威慑力。

它的标准败法也只有一条，却极常见：无人响应的检测。没人去读的审计日志、被一律忽略的告警，等于没有。2017 年的 Equifax 数据泄露是教科书级的案例：一个已知漏洞迟迟没有补丁，入侵者在系统里潜伏了约七十六天才被察觉，约一亿四千七百万人的个人信息就此外泄。痕迹其实都在日志里，只是没人看。检测而不响应，是形同虚设。（另一条隐患是日志本身可被篡改，这正是上面那些密码学手段要堵的。）

## 八招齐了：第三部的收束

把这最后一对并看：衰减在事前缩小失败的代价，留痕在事后保证失败被发现。它们都不再试图让那个未经验证的东西正确，而是改造失败本身的形貌，一个压低爆炸半径，一个把检查改为事后。

到这里，八招集齐，四对成双：

- **压缩未知**（第 9 章）：证书与界、最优筛查。
- **借来的判断**（第 10 章）：神谕入回路、冗余共识。
- **换一个能处理的问题**（第 11 章）：代理替换、标定。
- **管住后果**（第 12 章）：衰减围栏、留痕审计。

这就是那张对照表，本书的载荷。它在四个现场加科学中反复以不同的行话出现，却始终是这八样。第 4 章立下的铁律，每一招都尽量交代了它的机制、跨域形态与标准败法，而非仅凭表面相似。

但一个尖锐的问题悬而未决：为什么偏偏是这八招？是我凑出来的一张清单，还是它们各自对应着某种更基本、躲不开的东西？如果只是清单，这本书顶多是个有用的归类手册；如果背后真有结构，那「收敛」才算被解释。第四部去追这个问题，先尝试把八招挂到一个共同的骨架上，再正面清算：这究竟是一条定律，还是一个很强的经验模式。

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实。

1. J. Saltzer & M. Schroeder (1975).《The Protection of Information in Computer Systems》. Proceedings of the IEEE. [②]
   这篇综述把保护机制的设计原则系统化，其中最小权限原则成为「衰减」一招的源头：只给一个组件完成本职所必需的能力，其余一概不给。本章「缩小爆炸半径」的整个思路即由此发端，是理解为何要事前圈死失败范围的第一篇必读文献。
2. B. Lampson (1973).「A Note on the Confinement Problem」. Communications of the ACM. [②]
   兰普森提出「围堵问题」：如何确保一个被调用的程序无法泄露或滥用它所接触的信息，包括隐蔽信道这类难堵的旁路。它给「把出错的东西关进笼子」立下了精确的问题陈述，正是本章衰减一招要解决的核心。
3. D. Bell & L. LaPadula (1973).《Secure Computer Systems: Mathematical Foundations》. The MITRE Corporation. [②]
   贝尔-拉帕杜拉模型用形式化方式刻画机密性：信息只能由低密级流向同级或更高密级，著名的「不上读、不下写」规则即出于此。它示范了如何把「失败的波及范围」写成可证明的格结构，是安全模型理论化的奠基之作。
4. K. Biba (1977).《Integrity Considerations for Secure Computer Systems》. The MITRE Corporation. [②]
   比巴模型是贝尔-拉帕杜拉的对偶，关注完整性而非机密性：信息只能由高可信向低可信流动，以防低可信数据污染关键组件。两者并看，说明同一套格论框架可以从两个方向限定失败的扩散。
5. D. Denning (1976).「A Lattice Model of Secure Information Flow」. Communications of the ACM. [②]
   丹宁把信息流安全统一进一个格模型：为数据标上安全标签，要求流动只能沿格的偏序方向进行，从而在编译期或运行期静态地约束信息能去哪里。它为前面几种安全模型提供了共同的数学语言，是信息流控制的理论核心。
6. D. Clark & D. Wilson (1987).「A Comparison of Commercial and Military Computer Security Policies」. IEEE Symposium on Security and Privacy. [②]
   克拉克与威尔逊指出商业场景更看重完整性而非军方式的机密性，并提出以良构事务和职责分离为核心的完整性模型。它把「衰减」从军用密级扩展到商业账务等日常场景，说明限定失败范围的形态随领域而变。
7. J. Dennis & E. Van Horn (1966).「Programming Semantics for Multiprogrammed Computations」. Communications of the ACM. [②]
   这篇早期论文提出了能力（capability）的概念：访问权以不可伪造的令牌形式直接附着在引用上，持有令牌才能操作对象。它是能力安全模型的源头，为「只给必需的最小能力」提供了机制层面的实现路径。
8. N. Provos, M. Friedl & P. Honeyman (2003).「Preventing Privilege Escalation」. 12th USENIX Security Symposium. [②]
   作者们讨论如何用权限分离把特权操作隔离到极小的、受信的代码段，使主体程序即便被攻破也只能在低权限下活动，OpenSSH 的特权分离是其代表实践。它把最小权限落到了真实系统的工程细节上。
9. I. Goldberg, D. Wagner, R. Thomas & E. Brewer (1996).「A Secure Environment for Untrusted Helper Applications」. 6th USENIX Security Symposium. [②]
   这篇论文介绍 Janus，用系统调用拦截为不可信程序构造受限的运行环境，是用户态沙箱的早期范例。本章把沙箱列为衰减一招的化身，此文正是沙箱思想的代表性出处。
10. C. Perrow (1984).《Normal Accidents: Living with High-Risk Technologies》. Basic Books. [②①]
   佩罗提出「正常事故」论：在高度复杂且紧密耦合的系统里，灾难性事故不是偶然而是结构性必然，无法靠加防护根除。它从反面支撑本章的立场：当错误防不胜防，重心就该移到经营后果而非妄图杜绝失败。
11. N. Leveson (2011).《Engineering a Safer World: Systems Thinking Applied to Safety》. MIT Press. [②]
   莱韦森用系统论重构安全工程，提出 STAMP 模型，把事故看成控制结构失效而非单一部件故障，强调用约束去限定危险状态。它为「事前圈死失败范围」提供了系统层面的方法论。
12. J. Reason (1990).《Human Error》. Cambridge University Press. [②]
   里森系统分析人因失误，提出著名的「瑞士奶酪模型」：每层防护都有漏洞，唯当多层漏洞偶然对齐时事故才贯穿而出。它正是本章纵深防御直觉的来源，也提醒各层漏洞一旦相关，多层就退化成单层。
13. E. Hollnagel, D. Woods & N. Leveson (2006).《Resilience Engineering: Concepts and Precepts》. Ashgate. [②④]
   这本文集奠定「韧性工程」：系统的安全不在于消灭故障，而在于具备吸收扰动、在失败后仍维持运转和恢复的能力。它与本章主旨高度契合，把重心从「不出错」明确转向「出错也扛得住」。
14. A. Avizienis, J.-C. Laprie, B. Randell & C. Landwehr (2004).「Basic Concepts and Taxonomy of Dependable and Secure Computing」. IEEE Transactions on Dependable and Secure Computing. [②]
   这篇被广泛引用的分类学厘清了故障、错误、失效的链条，以及容错、防错、查错等手段的关系。它为本章讨论的各种衰减与留痕手段提供了一套公认的术语框架，适合作为概念校准的参考。
15. M. Nygard (2007).《Release It! Design and Deploy Production-Ready Software》. Pragmatic Bookshelf. [②④]
   奈加德把可靠性工程写成实战手册，提出熔断器、隔板、超时、舱壁隔离等稳定性模式，以阻止局部故障级联成全局崩溃。本章正文以它为爆炸半径设计的代表，是把衰减思想用于生产系统的直接读物。
16. R. Anderson (2020).《Security Engineering: A Guide to Building Dependable Distributed Systems》（第三版）. Wiley. [②④]
   安德森这本巨著横跨密码学、访问控制、经济激励到现实攻防，是安全工程的权威综合教材。本章涉及的最小权限、审计、防篡改等几乎所有主题都能在其中找到更完整的展开，适合作为通读底本。
17. N. N. Taleb (2012).《Antifragile: Things That Gain from Disorder》. Random House. [④]
   塔勒布提出「反脆弱」：有些系统不只在波动中存活，还从波动中受益，关键在限死下行、保留上行。本章引它说明衰减的极致姿态就是把损失封顶，是从风险经营角度理解「管住后果」的视角。
18. R. Merkle (1980).「Protocols for Public Key Cryptosystems」. IEEE Symposium on Security and Privacy. [②]
   默克尔在此提出了用哈希树（默克尔树）做树状认证的思想：把大量数据归并成一个根哈希，任一项的真伪只需 $O(\log n)$ 的路径即可校验。它是本章「留痕」一招的技术基石，也是后来证书透明度与区块链的共同祖先。
19. S. Haber & W. S. Stornetta (1991).「How to Time-Stamp a Digital Document」. Journal of Cryptology. [②]
   两位作者提出用哈希把文档时间戳串成链，使任何事后篡改都会破坏链的连续性而暴露。这是链式防篡改记录的开创性工作，直接启发了后来的区块链结构，是理解留痕为何「改不掉」的关键。
20. B. Schneier & J. Kelsey (1998).「Cryptographic Support for Secure Logs on Untrusted Machines」. 7th USENIX Security Symposium. [②]
   本文设计了在可能被攻陷的机器上保护日志的方案：即便攻击者事后取得控制权，也无法不被察觉地删改此前的记录。它把防篡改日志推进到不可信环境，是本章留痕一招的硬核技术之一。
21. B. Schneier & J. Kelsey (1999).「Secure Audit Logs to Support Computer Forensics」. ACM Transactions on Information and System Security. [②]
   这是上一篇工作的期刊版扩展，更完整地论述了支持取证的安全审计日志构造。它说明留痕不仅要忠实记录，还要在事后能经得起对抗性的核验，对应本章「让错误事后现形」的目标。
22. M. Bellare & S. Miner (1999).「A Forward-Secure Digital Signature Scheme」. CRYPTO '99. [②]
   贝拉雷与迈纳提出前向安全签名：密钥定期演进，即使当前密钥泄露，攻击者也无法伪造此前时段的签名。它为留痕提供了关键保障，使过去的记录在私钥失守后仍不可被冒名篡改。
23. S. Crosby & D. Wallach (2009).「Efficient Data Structures for Tamper-Evident Logging」. 18th USENIX Security Symposium. [②]
   作者们设计了可高效追加与审计的防篡改日志结构，让验证者无需信任日志服务器即可确认记录的完整与一致。它把前述密码学手段整合成可落地的数据结构，是留痕一招走向工程化的代表作。
24. B. Laurie, A. Langley & E. Kasper (2013).《RFC 6962: Certificate Transparency》. IETF. [②]
   证书透明度用公开、只能追加、可被任何人审计的默克尔日志记录所有签发的 TLS 证书，使误签或恶意证书无所遁形。它是本章「全球范围、人人可验的审计账」的现实样板，展示留痕如何规模化部署。
25. L. Lamport, R. Shostak & M. Pease (1982).「The Byzantine Generals Problem」. ACM Transactions on Programming Languages and Systems. [②]
   这篇经典论文形式化了拜占庭容错问题：在部分节点可能任意作恶时，诚实节点如何就一个值达成一致，并给出了可容错节点数的理论界。它是公开可验账本所依赖的共识理论根基，被本章列入「理论上被研究过的东西」。
26. M. Castro & B. Liskov (1999).「Practical Byzantine Fault Tolerance」. 3rd USENIX Symposium on Operating Systems Design and Implementation（OSDI）. [②]
   卡斯特罗与利斯科夫给出第一个在真实异步网络中实用的拜占庭容错算法 PBFT，把理论上的共识做到了可工程化的性能。它说明一本人人可验、容忍作恶节点的账本并非空想，为留痕的可信基础提供了实现支撑。
27. S. Nakamoto (2008).《Bitcoin: A Peer-to-Peer Electronic Cash System》. 白皮书. [②]
   中本聪的白皮书提出比特币：用工作量证明驱动一条去中心化、只能追加的区块链，让无需互信的各方就交易历史达成共识。本章视其本质为一本全球可验的审计账，是留痕思想在开放网络上的极端实现。
28. D. Weitzner, H. Abelson, T. Berners-Lee, J. Feigenbaum, J. Hendler & G. Sussman (2008).「Information Accountability」. Communications of the ACM. [②④]
   作者们主张从「事前封锁访问」转向「事后问责」：允许信息流动，但要求用途可被审计、违规可被追溯并追究责任。这与本章把检查从事前挪到事后的「留痕」姿态完全同构，是该理念在隐私治理上的纲领性表述。
29. J. Soll (2014).《The Reckoning: Financial Accountability and the Rise and Fall of Nations》. Basic Books. [①]
   索尔以财务史论证：一个政权能否算清并如实呈现自己的账目，与其兴衰直接相关，复式记账是其中关键的问责技术。它把留痕的脉络上溯到人类最早的防篡改账本，说明审计账的力量由来已久。
30. B. Beyer, C. Jones, J. Petoff & N. Murphy (2016).《Site Reliability Engineering: How Google Runs Production Systems》. O'Reilly. [④]
   这本书系统介绍谷歌的 SRE 实践，包括错误预算、金丝雀发布、监控告警与可控的故障演练。本章借其错误预算与金丝雀发布说明衰减如何在大规模生产中制度化，是把「管住后果」工程化的现代范本。
31. J. Ioannidis (2005).「Why Most Published Research Findings Are False」. PLoS Medicine. [③]
   约阿尼迪斯用统计建模论证：在低先验、小样本、多重比较与研究自由度过大的条件下，大量已发表的研究结论很可能为假阳性。这是一篇分析性论证而非实证复制研究，为本章提到的预注册与可复现给出了问题诊断。
32. Open Science Collaboration (2015).「Estimating the Reproducibility of Psychological Science」. Science. [③]
   这是一项大规模实证：多组研究者尝试复制上百项心理学研究，结果相当一部分未能复现。它把约阿尼迪斯的理论担忧落成可见的数据，是「复制危机」的标志性证据，呼应本章对事后可验的重视。
33. B. Nosek, C. Ebersole, A. DeHaven & D. Mellor (2018).「The Preregistration Revolution」. PNAS. [③]
   诺塞克等人倡导预注册：在看到数据之前就公开登记假说与分析方法，使探索性与验证性研究分离，事后无法移动靶子。它是科学领域的「留痕」实践，把检验从事前的信任挪到事后的核对，与本章主旨直接对应。
