# 第 6 章　放出去的智能体

> **论点**：一旦把行动委托给自主系统，你无法验证它在将遇到的一切情形里的未来行为（开放世界）；若它还能耍策略，你又叠上对抗式不可验证，于是应对从「证明它对」转向「限制它能破坏什么、给你的信任定价、让它的行为事后可查」。

## 关键节拍

未来行为缺口：你测了一些输入，它会遇到别的。开放世界问题。

招数集：

- **衰减／围栏**：最小权限、沙箱，缩小爆炸半径。
- **标定**：按分级信任而非二值行动。
- **留痕**：可审计的日志。

## 例子

沙箱化不受信代码、能力限制、分级自治的决策规则（allow／ask／block 这类作为通用模式呈现）、审计链。

## 接口

点明这些与组织那章、数学那章将展示的是同几招，只是换了名字。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实；个别未能确证者标「（细节待核）」。

### 服务委托的可控边界（衰减／围栏）

1. J. Saltzer & M. Schroeder (1975).「The Protection of Information in Computer Systems」. Proceedings of the IEEE, 63(9), 1278-1308. [②]
2. B. Lampson (1973).「A Note on the Confinement Problem」. Communications of the ACM, 16(10), 613-615. [②]
3. R. Anderson (2008).《Security Engineering: A Guide to Building Dependable Distributed Systems》(2nd ed.). Wiley. [②]
4. L. Orseau & S. Armstrong (2016).「Safely Interruptible Agents」. 收于《Proceedings of the Thirty-Second Conference on Uncertainty in Artificial Intelligence (UAI 2016)》, 557-566. [②④]
5. N. Soares, B. Fallenstein, S. Armstrong & E. Yudkowsky (2015).「Corrigibility」. 收于《Workshops at the Twenty-Ninth AAAI Conference on Artificial Intelligence》. [②]
6. D. Hadfield-Menell, A. Dragan, P. Abbeel & S. Russell (2017).「The Off-Switch Game」. 收于《Proceedings of the Twenty-Sixth International Joint Conference on Artificial Intelligence (IJCAI 2017)》, 220-227. [②]

### 行为不可验证的理论根基

7. A. Turing (1936).「On Computable Numbers, with an Application to the Entscheidungsproblem」. Proceedings of the London Mathematical Society, s2-42, 230-265. [②]
8. H. G. Rice (1953).「Classes of Recursively Enumerable Sets and Their Decision Problems」. Transactions of the American Mathematical Society, 74, 358-366. [②]
9. K. Thompson (1984).「Reflections on Trusting Trust」. Communications of the ACM, 27(8), 761-763. [②①]

### 目标偏移、工具性趋同与对抗

10. S. Omohundro (2008).「The Basic AI Drives」. 收于《Artificial General Intelligence 2008: Proceedings of the First AGI Conference》, IOS Press, Frontiers in AI and Applications 171, 483-492. [②]
11. N. Bostrom (2014).《Superintelligence: Paths, Dangers, Strategies》. Oxford University Press. [②④]
12. S. Russell (2019).《Human Compatible: Artificial Intelligence and the Problem of Control》. Viking. [②④]
13. D. Amodei, C. Olah, J. Steinhardt, P. Christiano, J. Schulman & D. Mané (2016).「Concrete Problems in AI Safety」. arXiv:1606.06565. [②]
14. A. M. Turner, L. Smith, R. Shah, A. Critch & P. Tadepalli (2021).「Optimal Policies Tend to Seek Power」. 收于《Advances in Neural Information Processing Systems 34 (NeurIPS 2021)》. [②]
15. E. Hubinger, C. van Merwijk, V. Mikulik, J. Skalse & S. Garrabrant (2019).「Risks from Learned Optimization in Advanced Machine Learning Systems」. arXiv:1906.01820. [②]
16. J. Pan, K. Bhatia & J. Steinhardt (2022).「The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models」. 收于《International Conference on Learning Representations (ICLR 2022)》. [②]
17. R. Shah, V. Varma, R. Kumar, M. Phuong, V. Krakovna, J. Uesato & Z. Kenton (2022).「Goal Misgeneralization: Why Correct Specifications Aren't Enough For Correct Goals」. arXiv:2210.01790. [②]
18. V. Krakovna, J. Uesato, V. Mikulik, M. Rahtz, T. Everitt, R. Kumar, Z. Kenton, J. Leike & S. Legg (2020).「Specification Gaming: The Flip Side of AI Ingenuity」. DeepMind Blog. [②]
19. C. Szegedy, W. Zaremba, I. Sutskever, J. Bruna, D. Erhan, I. Goodfellow & R. Fergus (2014).「Intriguing Properties of Neural Networks」. 收于《International Conference on Learning Representations (ICLR 2014)》. [②]
20. I. Goodfellow, J. Shlens & C. Szegedy (2015).「Explaining and Harnessing Adversarial Examples」. 收于《International Conference on Learning Representations (ICLR 2015)》. [②]

### 标定：把信任分级而非二值

21. C. Guo, G. Pleiss, Y. Sun & K. Q. Weinberger (2017).「On Calibration of Modern Neural Networks」. 收于《Proceedings of the 34th International Conference on Machine Learning (ICML 2017)》, PMLR 70, 1321-1330. [②]
22. A. N. Angelopoulos & S. Bates (2021).「A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification」. arXiv:2107.07511. [②]
23. V. Vovk, A. Gammerman & G. Shafer (2005).《Algorithmic Learning in a Random World》. Springer. [②]

### 留痕：可审计、可问责

24. D. J. Weitzner, H. Abelson, T. Berners-Lee, J. Feigenbaum, J. Hendler & G. J. Sussman (2008).「Information Accountability」. Communications of the ACM, 51(6), 82-87. [②④]
25. B. Laurie, A. Langley & E. Kasper (2013).「Certificate Transparency」. IETF RFC 6962. [②④]
26. M. Brundage, S. Avin, J. Wang, H. Belfield, G. Krueger, G. Hadfield 等 (2020).「Toward Trustworthy AI Development: Mechanisms for Supporting Verifiable Claims」. arXiv:2004.07213. [②④]

### 复杂系统、自动化与人机责任

27. N. Leveson (2011).《Engineering a Safer World: Systems Thinking Applied to Safety》. MIT Press. [②④]
28. C. Perrow (1984).《Normal Accidents: Living with High-Risk Technologies》. Basic Books. [②④]
29. L. Bainbridge (1983).「Ironies of Automation」. Automatica, 19(6), 775-779. [②④]
30. R. Parasuraman & V. Riley (1997).「Humans and Automation: Use, Misuse, Disuse, Abuse」. Human Factors, 39(2), 230-253. [②④]
31. J. Reason (1990).《Human Error》. Cambridge University Press. [②④]

### 委托代理的经济学骨架

32. S. A. Ross (1973).「The Economic Theory of Agency: The Principal's Problem」. American Economic Review, 63(2), 134-139. [②]
33. M. C. Jensen & W. H. Meckling (1976).「Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure」. Journal of Financial Economics, 3(4), 305-360. [②]
