# 第 11 章　换一个能处理的问题

> **论点**：别再坚持验证真正的对象。要么把它换成你能查的可解代理（代理替换），要么不再索求二值判决、转而按标定的概率行动（标定）。

## 两招的纯形式

**代理／替身**：用测试代正确性、用 benchmark 代能力、用 KPI 代健康、用等价陈述代定理。

**标定**：概率素性、conformal prediction、标定预报、分级信任。

## 结构兑现：「换掉目标」的两种相反败法

代理可以**忠实却不更易**（数学的等价改写：你只是把困难改了个名），也可以**更易却不忠实**（Goodhart：你优化代理，真目标却烂掉）。一个好代理必须既忠实又更易，这罕见，而这正是全部的手艺。

这两种相反败法，正是第 7 章（忠实但不更易）与第 8 章（更易但不忠实）在此对接。

标定的败法：失标（你声称的把握与现实不符），以及更深的一层，标定告诉你赔率，却不告诉你是否该接受它（那是价值问题，不是验证问题）。

## 接口

最后一对放弃「做对」，转而经营「做错」。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实；个别未能确证者标「（细节待核）」。

### 代理替换：从古德哈特定律到非预期后果

1. C. A. E. Goodhart (1975).「Problems of Monetary Management: The U.K. Experience」.《Papers in Monetary Economics》, Vol. I. Reserve Bank of Australia. [②]　（古德哈特定律的原始出处。源于 1975 年 7 月悉尼货币经济学会议，论文集 1976 年由澳大利亚储备银行印行；后亦收入其 1984 年著作。）

2. R. K. Merton (1936).「The Unanticipated Consequences of Purposive Social Action」.《American Sociological Review》, 1(6), 894–904. [②]　（非预期后果的系统化分析，代理替换副作用的社会学源头。）

3. D. T. Campbell (1979).「Assessing the Impact of Planned Social Change」.《Evaluation and Program Planning》, 2(1), 67–90. [②④]　（坎贝尔定律来源，与古德哈特并列的代理失真经典。）

4. S. Kerr (1975).「On the Folly of Rewarding A, While Hoping for B」.《Academy of Management Journal》, 18(4), 769–783. [②④]　（激励与代理错配的管理学经典。）

5. M. Strathern (1997).「'Improving ratings': audit in the British University system」.《European Review》, 5(3), 305–321. [②④]　（给出「当一个度量成为目标，它便不再是好的度量」这一广为流传的表述。）

6. R. E. Lucas (1976).「Econometric Policy Evaluation: A Critique」.《Carnegie-Rochester Conference Series on Public Policy》, 1, 19–46. [②③]　（卢卡斯批判，古德哈特定律的经济学孪生命题：被当作目标后结构关系即失效。）

7. W. N. Espeland & M. Sauder (2007).「Rankings and Reactivity: How Public Measures Recreate Social Worlds」.《American Journal of Sociology》, 113(1), 1–40. [②④]　（「反身性」框架，量化指标如何反过来重塑被测对象。）

8. D. Manheim & S. Garrabrant (2018).「Categorizing Variants of Goodhart's Law」. arXiv:1803.04585. [②]　（首发 2018 年 3 月，后有 v3 修订。对古德哈特定律给出至少四类机制划分。预印本，非期刊。）

9. J. Z. Muller (2018).《The Tyranny of Metrics》. Princeton University Press. [④]　（度量崇拜负面后果的通俗综述。）

### 代理失真在机器学习中的复现：奖励钻空与过优化

10. D. Amodei, C. Olah, J. Steinhardt, P. Christiano, J. Schulman & D. Mané (2016).「Concrete Problems in AI Safety」. arXiv:1606.06565. [②]　（提出 reward hacking、scalable supervision 等问题，将代理目标失真译入机器学习语境。预印本。）

11. P. F. Christiano, J. Leike, T. B. Brown, M. Martic, S. Legg & D. Amodei (2017).「Deep Reinforcement Learning from Human Preferences」.《Advances in Neural Information Processing Systems》, 30 (NeurIPS 2017). [②④]　（用人类偏好学习代理奖励函数，RLHF 的奠基；arXiv:1706.03741。）

12. A. Pan, K. Bhatia & J. Steinhardt (2022).「The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models」. ICLR 2022. [②]　（实证：能力更强的代理更善于钻代理奖励的空子，出现真实回报骤降的相变。会议论文，OpenReview。）

13. J. Skalse, N. H. R. Howe, D. Krasheninnikov & D. Krueger (2022).「Defining and Characterizing Reward Hacking」.《Advances in Neural Information Processing Systems》, 35 (NeurIPS 2022). [②]　（reward hacking 的首个形式化定义；证明非平凡奖励几乎不可能「不可钻空」。NeurIPS 与 arXiv 版题名一致，均为「Reward Hacking」；arXiv:2209.13085。）

14. L. Gao, J. Schulman & J. Hilton (2023).「Scaling Laws for Reward Model Overoptimization」.《Proceedings of the 40th International Conference on Machine Learning》(PMLR 202), 10835–10866. [②]　（对古德哈特式过优化给出定量标度律。）

### 标定：把二值判决换成概率，并以严格适当评分约束之

15. G. W. Brier (1950).「Verification of Forecasts Expressed in Terms of Probability」.《Monthly Weather Review》, 78(1), 1–3. [②]　（Brier 评分的来源，标定与严格适当评分体系的起点。）

16. L. J. Savage (1971).「Elicitation of Personal Probabilities and Expectations」.《Journal of the American Statistical Association》, 66(336), 783–801. [②]　（适当评分规则用于诱出主观概率的理论奠基。）

17. A. H. Murphy (1973).「A New Vector Partition of the Probability Score」.《Journal of Applied Meteorology》, 12(4), 595–600. [②]　（Brier 评分的可靠性、分辨率与不确定性分解，标定概念的量化骨架。）

18. M. H. DeGroot & S. E. Fienberg (1983).「The Comparison and Evaluation of Forecasters」.《Journal of the Royal Statistical Society: Series D (The Statistician)》, 32(1–2), 12–22. [②]　（标定与精炼的系统处理，本章标定论证的核心理论来源。）

19. A. P. Dawid (1982).「The Well-Calibrated Bayesian」.《Journal of the American Statistical Association》, 77(379), 605–610. [②]　（贝叶斯主体渐近自我标定的经典结果。部分来源含讨论延至 613。）

20. D. Oakes (1985).「Self-Calibrating Priors Do Not Exist」.《Journal of the American Statistical Association》, 80(390), 339–342. [②]　（标定的极限性结果，作为 Dawid (1982)、Foster-Vohra 的反向制衡；含 Dawid、Schervish 评论。）

21. M. J. Schervish (1989).「A General Method for Comparing Probability Assessors」.《The Annals of Statistics》, 17(4), 1856–1879. [②]　（把适当评分规则统一为比较预测者的特例，标定理论的集成。）

22. D. P. Foster & R. V. Vohra (1998).「Asymptotic Calibration」.《Biometrika》, 85(2), 379–390. [②]　（证明对任意序列存在渐近标定的预测策略，标定可达性的关键定理。）

23. T. Gneiting & A. E. Raftery (2007).「Strictly Proper Scoring Rules, Prediction, and Estimation」.《Journal of the American Statistical Association》, 102(477), 359–378. [②]　（严格适当评分规则的权威综述，本章标定论证的理论支柱。）

24. T. Gneiting, F. Balabdaoui & A. E. Raftery (2007).「Probabilistic Forecasts, Calibration and Sharpness」.《Journal of the Royal Statistical Society: Series B (Statistical Methodology)》, 69(2), 243–268. [②]　（标定与锐度的现代框架：受制于标定，越锐越好。）

25. C. Guo, G. Pleiss, Y. Sun & K. Q. Weinberger (2017).「On Calibration of Modern Neural Networks」.《Proceedings of the 34th International Conference on Machine Learning》(PMLR 70), 1321–1330. [②]　（现代神经网络标定不良及温度缩放，标定问题在机器学习侧的代表作。）

26. V. Vovk, A. Gammerman & G. Shafer (2005).《Algorithmic Learning in a Random World》. Springer. [②]　（保形预测专著，给出带自身可靠性保证的预测。第二版 2022。）

### 判断、预测与替换动作的方法论根

27. P. E. Tetlock (2005).《Expert Political Judgment: How Good Is It? How Can We Know?》. Princeton University Press. [①②]　（专家预测准确性的大规模实证研究；以原始 2005 版年份为准，2017 年另有新版。）

28. P. E. Tetlock & D. Gardner (2015).《Superforecasting: The Art and Science of Prediction》. Crown. [①④]　（IARPA 预测锦标赛成果的通俗化，偏向预测者判断与如何在无法验证的世界里生活。）

29. G. E. P. Box (1976).「Science and Statistics」.《Journal of the American Statistical Association》, 71(356), 791–799. [②③]　（「所有模型都是错的，但有些有用」之源，服务于本章败法之一：忠实却不易处理 vs 可处理。）

30. G. Pólya (1945).《How to Solve It: A New Aspect of Mathematical Method》. Princeton University Press. [②④]　（「先解一个相关而更易的问题」是本章标题这一替换动作的方法论原型。）

31. H. A. Simon (1956).「Rational Choice and the Structure of the Environment」.《Psychological Review》, 63(2), 129–138. [②④]　（满意化与有限理性，「用足够好的代理取代最优」的理论根据。）

32. D. Kahneman & S. Frederick (2002).「Representativeness Revisited: Attribute Substitution in Intuitive Judgment」. 收入 T. Gilovich, D. Griffin & D. Kahneman (编)《Heuristics and Biases: The Psychology of Intuitive Judgment》, 49–81. Cambridge University Press. [②]　（「属性替换」：用更易评估的属性替换难评估的目标属性，正是本章替换机制的心理学孪生。）
