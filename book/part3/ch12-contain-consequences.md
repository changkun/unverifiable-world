# 第 12 章　管住后果

> **论点**：当你无法防止错误，就经营它的后果。缩小一个错误的、未经验证的东西能造成的破坏（衰减，事前），并确保万一出错你会发现（留痕，事后）。

前面三对招，再放低标准，也都还在努力把事情做对。这最后一对，索性承认你做不对，转而经营「做错」。既然防不住错误，那就缩小它能造成的破坏（衰减，事前），并确保它一旦发生你查得到（留痕，事后）。

## 衰减：缩小爆炸半径

第一招的纯形式：不去保证那个未经验证的东西不出错，而是把它出错时能波及的范围，事前就圈死。

这是计算机安全最深的家底。萨尔策与施罗德 1975 年的最小权限、兰普森 1973 年的围堵、丹尼斯与范霍恩 1966 年的能力机制，到丹宁 1976 年的信息流格、贝尔-拉帕杜拉与比巴的安全模型，主旨一致：只给一个组件完成本职所必需的最小能力，其余一概不给，这样它就算被攻破或出错，也掀不起大浪。沙箱（戈德堡等人 1996）、职责分离、纵深防御，都是它的化身。系统可靠性工程里，它是熔断器与隔板（奈加德的《Release It!》）、是爆炸半径设计、是金丝雀发布与错误预算（谷歌 SRE）；金融里，它是头寸限额与止损；塔勒布的反脆弱，讲的也是把下行限死。

统一的观念是：把担子从「让它不出错」（那需要你没有的验证），移到「让它出错也扛得住」。一个常见的量化直觉是纵深防御，若 $k$ 层防护各自独立地以概率 $p$ 失守，全部同时失守的概率是

$$p^{k},$$

随层数指数下降。但请立刻接上第 10 章那个警告：这个 $p^k$ 只在各层失效相互独立时成立。若各层栽在同一个弱点上（同一个被绕过的内核、同一个管理员口令），相关性会让纵深防御瞬间退化成单层。

它的标准败法正是这里：被绕过的衰减。沙箱有逃逸，权限会悄悄蔓延，看似层层设防，实则各层共用一道暗门。另一种较少被提的败法是围得太死，防护严到把正常功能也掐断，于是人们绕过它来干活，安全形同虚设。

## 留痕：让错误事后现形

第二招的纯形式：防不住的，就让它一旦发生必被发现。把检查从事前挪到事后。

它最硬核的技术，来自密码学。默克尔 1980 年的哈希树、哈伯与斯托尔奈塔 1991 年的链式时间戳，让一份记录一旦写下就无法被悄悄篡改，任何改动都会在校验时暴露；克罗斯比与瓦拉赫 2009 年的防篡改日志、施奈尔与凯尔西 1998 年在不可信机器上保护日志、贝拉雷与迈纳 1999 年的前向安全签名，把这套做得更牢；证书透明度（RFC 6962）和中本聪 2008 年的比特币，本质都是一本全球范围、只能追加、人人可验的审计账。核对一条记录是否在这样一棵树里，代价只有 $O(\log n)$，又是第 2 章那道「验比造廉」的红利。

而这一招其实古老得多。复式记账就是人类最早的防篡改账本之一，索尔在《清算》里论证，算得清自己账目的能力，与国家的兴衰直接相关。现代财务审计、独立稽核，都是同一姿势。科学里，它是预注册（诺塞克 2018）与可复现（呼应第 3 章的复制危机）：把假说和方法在看到数据前就登记下来，事后无法移动靶子。

统一的观念是：放弃「事前阻止坏事」（要验证），改为「事后必能发现坏事」（只要一本忠实的账）。它的好处是双重的，既让错误可被纠正，也因为「跑不掉」而产生威慑。

它的标准败法也只有一条，却极常见：无人响应的检测。没人去读的审计日志、被一律忽略的告警，等于没有。检测而不响应，是做戏。（另一条隐患是日志本身可被篡改，这正是上面那些密码学手段要堵的。）

## 八招齐了：第三部的收束

把这最后一对并看：衰减在事前缩小失败的代价，留痕在事后保证失败被发现。它们都不再试图让那个未经验证的东西正确，而是改造失败本身的形貌，一个压低爆炸半径，一个把检查挪到事后。

到这里，八招集齐，四对成双：

- **压缩未知**（第 9 章）：证书与界、最优筛查。
- **借来的判断**（第 10 章）：神谕入回路、冗余共识。
- **换一个能处理的问题**（第 11 章）：代理替换、标定。
- **管住后果**（第 12 章）：衰减围栏、留痕审计。

这就是那张对照表，本书的载荷。它在四个现场、加科学，反复以不同的行话出现，却始终是这八样。第 4 章立下的铁律，每一招都尽量交代了它的机制、跨域形态与标准败法，而非仅凭表面相似。

但一个尖锐的问题悬而未决：为什么偏偏是这八招？是我凑出来的一张清单，还是它们各自对应着某种更基本、躲不开的东西？如果只是清单，那这本书顶多是本有用的归类手册；如果背后真有结构，那「收敛」才算被解释。第四部去追这个问题，先尝试把八招挂到一个共同的骨架上，再诚实地清算：这究竟是一条定律，还是一个很强的经验模式。

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实；个别未能确证者标「（细节待核）」。

1. J. Saltzer & M. Schroeder (1975).《The Protection of Information in Computer Systems》. Proceedings of the IEEE. [②]
2. B. Lampson (1973).「A Note on the Confinement Problem」. Communications of the ACM. [②]
3. D. Bell & L. LaPadula (1973).《Secure Computer Systems: Mathematical Foundations》. The MITRE Corporation. [②]
4. K. Biba (1977).《Integrity Considerations for Secure Computer Systems》. The MITRE Corporation. [②]
5. D. Denning (1976).「A Lattice Model of Secure Information Flow」. Communications of the ACM. [②]
6. D. Clark & D. Wilson (1987).「A Comparison of Commercial and Military Computer Security Policies」. IEEE Symposium on Security and Privacy. [②]
7. J. Dennis & E. Van Horn (1966).「Programming Semantics for Multiprogrammed Computations」. Communications of the ACM. [②]
8. N. Provos, M. Friedl & P. Honeyman (2003).「Preventing Privilege Escalation」. 12th USENIX Security Symposium. [②]
9. I. Goldberg, D. Wagner, R. Thomas & E. Brewer (1996).「A Secure Environment for Untrusted Helper Applications」. 6th USENIX Security Symposium. [②]
10. C. Perrow (1984).《Normal Accidents: Living with High-Risk Technologies》. Basic Books. [②①]
11. N. Leveson (2011).《Engineering a Safer World: Systems Thinking Applied to Safety》. MIT Press. [②]
12. J. Reason (1990).《Human Error》. Cambridge University Press. [②]
13. E. Hollnagel, D. Woods & N. Leveson (2006).《Resilience Engineering: Concepts and Precepts》. Ashgate. [②④]
14. A. Avizienis, J.-C. Laprie, B. Randell & C. Landwehr (2004).「Basic Concepts and Taxonomy of Dependable and Secure Computing」. IEEE Transactions on Dependable and Secure Computing. [②]
15. M. Nygard (2007).《Release It! Design and Deploy Production-Ready Software》. Pragmatic Bookshelf. [②④]
16. R. Anderson (2020).《Security Engineering: A Guide to Building Dependable Distributed Systems》（第三版）. Wiley. [②④]
17. N. N. Taleb (2012).《Antifragile: Things That Gain from Disorder》. Random House. [④]
18. R. Merkle (1980).「Protocols for Public Key Cryptosystems」. IEEE Symposium on Security and Privacy. [②]
19. S. Haber & W. S. Stornetta (1991).「How to Time-Stamp a Digital Document」. Journal of Cryptology. [②]
20. B. Schneier & J. Kelsey (1998).「Cryptographic Support for Secure Logs on Untrusted Machines」. 7th USENIX Security Symposium. [②]
21. B. Schneier & J. Kelsey (1999).「Secure Audit Logs to Support Computer Forensics」. ACM Transactions on Information and System Security. [②]
22. M. Bellare & S. Miner (1999).「A Forward-Secure Digital Signature Scheme」. CRYPTO '99. [②]
23. S. Crosby & D. Wallach (2009).「Efficient Data Structures for Tamper-Evident Logging」. 18th USENIX Security Symposium. [②]
24. B. Laurie, A. Langley & E. Kasper (2013).《RFC 6962: Certificate Transparency》. IETF. [②]
25. L. Lamport, R. Shostak & M. Pease (1982).「The Byzantine Generals Problem」. ACM Transactions on Programming Languages and Systems. [②]
26. M. Castro & B. Liskov (1999).「Practical Byzantine Fault Tolerance」. 3rd USENIX Symposium on Operating Systems Design and Implementation（OSDI）. [②]
27. S. Nakamoto (2008).《Bitcoin: A Peer-to-Peer Electronic Cash System》. 白皮书. [②]
28. D. Weitzner, H. Abelson, T. Berners-Lee, J. Feigenbaum, J. Hendler & G. Sussman (2008).「Information Accountability」. Communications of the ACM. [②④]
29. J. Soll (2014).《The Reckoning: Financial Accountability and the Rise and Fall of Nations》. Basic Books. [①]
30. B. Beyer, C. Jones, J. Petoff & N. Murphy (2016).《Site Reliability Engineering: How Google Runs Production Systems》. O'Reilly. [④]
31. J. Ioannidis (2005).「Why Most Published Research Findings Are False」. PLoS Medicine. [③]
32. Open Science Collaboration (2015).「Estimating the Reproducibility of Psychological Science」. Science. [③]
33. B. Nosek, C. Ebersole, A. DeHaven & D. Mellor (2018).「The Preregistration Revolution」. PNAS. [③]
