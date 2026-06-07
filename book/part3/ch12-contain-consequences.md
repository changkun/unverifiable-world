# 第 12 章　管住后果

> **论点**：当你无法防止错误，就经营它的后果。缩小一个错误的、未经验证的东西能造成的破坏（衰减，事前），并确保万一出错你会发现（留痕，事后）。

## 两招的纯形式

**衰减**：最小权限、沙箱、爆炸半径设计、职责分离、头寸限额。

**留痕**：审计日志、Merkle 树、复式记账、预注册、可复现。

统一观念：把担子从「防止」（需要你没有的验证）移到「围堵加检测」。

## 败法

被绕过的衰减：沙箱逃逸、权限蔓延。

无人响应的检测：没人读的审计日志、被无视的警报。检测而不响应是做戏。

## 接口

四章、八招、四杠杆；第四部追问这套是否被逼出来的。

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
