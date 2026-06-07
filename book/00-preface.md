# 序　没有神谕的世界

古希腊人出征、婚嫁、建城之前，会先去德尔斐求一次神谕。神谕的意义不在它有多准，而在它许诺了一件事：在你行动之前，存在一个能告诉你答案的地方。两千年后，计算机科学家借走了这个词。在他们那里，神谕（oracle）是一个黑箱，你把一个自己算不出的问题递进去，它当即吐出正确答案。两种神谕共享同一个幻想：在动手之前，先把对错验明。

这本书讲的，是这个幻想破灭之后的世界。

我们几乎从不验证，我们只是行动，然后或迟或早地知道，或者永远不知道。我们以为「凡事可检验」是常态，是因为我们最早的训练来自一类特别窄的事：算术、给清单排序、核对一张收据。在那些事里，答案唾手可验，于是我们误以为整个世界都该如此。可一旦走出那道窄门，验证立刻变成奢侈品。你能验证七乘八，你无法在说「我愿意」之前验证这段婚姻会长久，无法在上线之前验证这个代码库没有 bug，无法在投身之前验证一个理论为真、一家公司是健康的、一个决定是对的。大多数有后果的行动，都踩在未经验证的地面上。神谕没有回话，而你还是得迈步。

面对这个处境，常见的反应是哀叹或假装。哀叹的人说，既然什么都无法确定，那一切判断都不过是意见；假装的人则给自己造一个假神谕，把一个测得出的数字供起来，假装它就是那个测不出的真相。这本书两样都不做。它问一个更有意思的问题：那些确实有能力的人，科学家、工程师、数学家、治理者，在神谕缺席时，到底做了什么？

把这个问题在足够多的领域里追下去，会撞见一个出人意料的观察，它是全书的由来：尽管不可验证的来源天差地别，有能力的人被逼出来的应对，却反复收敛到同一小套。

这就引出本书的两层结构，请先记住，因为后面所有章节都挂在它上面。

第一层，问题是异质的。「我没法检验它」这句话底下，藏着五种结构全然不同的处境：有些原则上就没有判定程序（不可判定），有些有程序却代价大到不可能（难解），有些是相关状态对你隐藏（部分可观测），有些是你本可验证却没有那个时间、算力或样本（预算受限），还有些是对面那个系统在主动挫败你的验证（对抗）。把这五种混为一谈，是这个领域最常犯的错。第一部会把它们一一掰开。

第二层，应对却收敛。无论问题来自哪一副面孔，有能力的主体伸手去够的，反复是同样几样东西：用一个测得出的代理替换测不出的真目标，在一个能查的切片上证一个界，把昂贵的查验花在信息量最大处，引进一个外部的判断者，缩小失败的爆炸半径，给残余的风险标定一个概率，把检查从事前挪到事后，用多个互相独立的判断去抵消单点的失误。本书把它们点成八招，并论证这八招可以收进四根更基本的杠杆。第二部走进四个现场，让这些招数嵌在各自的行话里、彼此缠绕地出现；第三部再把每一招单独拎出来、洗净、命名，铺成一张跨领域的对照表，那是这本书真正的载荷；第四部追问，为什么偏偏是这几招。

这里必须把一句诚实的保留放在最前面。这套收敛，到底是一条定律（某种东西迫使任何有限的主体都必然走到这几招上），还是仅仅一个很强的经验模式（我们一再看到它，却没能证明它非如此不可）？我此刻没有证据说它是定律。这本书交付的，是一个被诚实地划了边界的猜想，外加一套能把许多领域串起来的共同词汇，而不是一条定理。第 14 章会正面清算这件事。

而这恰恰带来一个无法回避、也不该回避的递归：一本论述「如何在不可验证中行动」的书，自己也无法验证它的核心命题。于是它只能做它通篇所描述的那件事，陈述一个标定的信念，给主张划清边界，邀请你来反驳，然后照样把话说下去。这本书会亲自演练它所讲的那套招。如果它讲对了，这种自我演练就不是缺陷，而是唯一诚实的写法。

最后留一个画面，跋会回到它。一艘船在浓雾里改变航向。船长手上有海图、有罗盘、有对洋流的估算，唯独没有一双能看穿雾的眼睛。她无法在转舵之前验证前方是不是暗礁。雾不会散，神谕不会来。可航行不能因此停下。这本书想弄清楚的，不是怎样等到雾散，而是一个好船长在雾里究竟是怎么操舵的。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实；个别未能确证者标「（细节待核）」。

1. H. A. Simon (1969).《The Sciences of the Artificial》. MIT Press. [②④]
2. F. H. Knight (1921).《Risk, Uncertainty and Profit》. Houghton Mifflin. [②]
3. N. N. Taleb (2007).《The Black Swan: The Impact of the Highly Improbable》. Random House. [②④]
4. W. C. Wimsatt (2007).《Re-Engineering Philosophy for Limited Beings: Piecewise Approximations to Reality》. Harvard University Press. [②③④]
5. J. M. Keynes (1921).《A Treatise on Probability》. Macmillan. [②]
6. L. J. Savage (1954).《The Foundations of Statistics》. Wiley. [②]
7. D. Ellsberg (1961).「Risk, Ambiguity, and the Savage Axioms」. Quarterly Journal of Economics, 75(4), 643-669. [②]
8. H. A. Simon (1955).「A Behavioral Model of Rational Choice」. Quarterly Journal of Economics, 69(1), 99-118. [②④]
9. H. A. Simon (1947).《Administrative Behavior: A Study of Decision-Making Processes in Administrative Organization》. Macmillan. [②④]
10. A. Tversky & D. Kahneman (1974).「Judgment under Uncertainty: Heuristics and Biases」. Science, 185(4157), 1124-1131. [②]
11. D. Kahneman & A. Tversky (1979).「Prospect Theory: An Analysis of Decision under Risk」. Econometrica, 47(2), 263-291. [②④]
12. D. Kahneman (2011).《Thinking, Fast and Slow》. Farrar, Straus and Giroux. [②④]
13. G. Gigerenzer & D. G. Goldstein (1996).「Reasoning the Fast and Frugal Way: Models of Bounded Rationality」. Psychological Review, 103(4), 650-669. [②④]
14. G. Gigerenzer, P. M. Todd & the ABC Research Group (1999).《Simple Heuristics That Make Us Smart》. Oxford University Press. [②④]
15. F. A. Hayek (1945).「The Use of Knowledge in Society」. American Economic Review, 35(4), 519-530. [②④]
16. M. Polanyi (1958).《Personal Knowledge: Towards a Post-Critical Philosophy》. Routledge & Kegan Paul. [①③④]
17. P. E. Meehl (1954).《Clinical versus Statistical Prediction: A Theoretical Analysis and a Review of the Evidence》. University of Minnesota Press. [①④]
18. D. A. Schön (1983).《The Reflective Practitioner: How Professionals Think in Action》. Basic Books. [①④]
19. G. A. Klein (1998).《Sources of Power: How People Make Decisions》. MIT Press. [①④]
20. P. E. Tetlock (2005).《Expert Political Judgment: How Good Is It? How Can We Know?》. Princeton University Press. [①④]
21. P. E. Tetlock & D. Gardner (2015).《Superforecasting: The Art and Science of Prediction》. Crown. [①④]
22. N. N. Taleb (2001).《Fooled by Randomness: The Hidden Role of Chance in Life and in the Markets》. Texere. [②④]
23. N. N. Taleb (2012).《Antifragile: Things That Gain from Disorder》. Random House. [④]
24. C. E. Lindblom (1959).「The Science of "Muddling Through"」. Public Administration Review, 19(2), 79-88. [④]
25. K. R. Popper (1959).《The Logic of Scientific Discovery》. Hutchinson. [③]
26. T. S. Kuhn (1962).《The Structure of Scientific Revolutions》. University of Chicago Press. [①③]
27. W. V. Quine (1951).「Two Dogmas of Empiricism」. The Philosophical Review, 60(1), 20-43. [③]
28. P. Duhem (1954).《The Aim and Structure of Physical Theory》. Princeton University Press. [③]
29. I. Hacking (1983).《Representing and Intervening: Introductory Topics in the Philosophy of Natural Science》. Cambridge University Press. [③]
