# Chapter 11: Swap the Problem

> **Thesis:** Stop insisting on verifying the real object. Either swap it for a solvable proxy you can check (proxy substitution), or stop demanding a binary verdict and instead act on a calibrated probability (calibration).

The first two pairs of moves still chase the truth of the object: they compress it, or borrow a judgment to approximate it. This pair gives up that obsession. It no longer asks whether the real thing is right or wrong; it answers a different question instead, either swapping out the object of verification (proxy substitution), or swapping out the form of the verdict (calibration).

## Proxy Substitution: Swap the Object You Verify

The first move in pure form: stop wrestling with the true target you cannot measure, swap it for a proxy you can check and that is good enough, and verify or optimize that proxy.

Its cross-domain shapes turn up in almost every earlier chapter of this book. Mathematicians stand in an equivalent statement for a theorem (Chapter 7); software engineers stand in tests for correctness, and benchmarks for capability; organizations stand in KPIs for health, and GDP for welfare (Chapter 8); machine learning stands in a reward model for human beings' true preferences (the RLHF of Chapter 5). Psychology has a twin as well: Kahneman and Frederick's 2002 "attribute substitution"<sup class="cite"><a href="#ref-32">32</a></sup>, in which a person making an intuitive judgment unconsciously substitutes an easily assessed attribute for the target attribute that is hard to assess. Pólya's maxim, "first solve a related, easier problem," and Simon's satisficing are the methodological prototypes of this move.

The whole essence of the move lies in this: it has two opposite ways of failing. Here is exactly where Chapters 7 and 8 intersect, and the theme runs through the whole book. Lay "faithful" (does the proxy really point at the original target) and "easier" (is the proxy really more tractable than the original problem) along two axes:

![The two opposite ways proxy substitution fails: faithful x easier](../figures/f07-proxy-2x2.svg)

Mathematicians come to grief in the upper right: an equivalent rewriting is faithful beyond reproach, yet not one bit easier to solve; you have only put the same difficulty into a different set of clothes. Organizations come to grief in the lower left: the metric is easy to measure, yet its correspondence with the true target snaps the moment it is treated as a target and optimized.

Why does it snap under optimization? Because the proxy's correlation with the true target holds only on the distribution that is the status quo, and the pressure of optimization pushes you off that distribution, toward the extreme where the two diverge. Goodhart's 1975 law<sup class="cite"><a href="#ref-1">1</a></sup> (a metric loses its reliability the moment it becomes a target), Campbell's 1979 law<sup class="cite"><a href="#ref-3">3</a></sup>, and Lucas's 1976 economic twin<sup class="cite"><a href="#ref-6">6</a></sup> (once a structural relation is made a policy target, it collapses) all describe the same mechanism. Espeland and Sauder's reactivity goes one step further: a metric does not merely distort, it reshapes the thing it measures.

This mechanism replays in machine learning with startling clarity. Amodei and colleagues' 2016 reward hacking<sup class="cite"><a href="#ref-10">10</a></sup>; Pan and colleagues' 2022 empirical study<sup class="cite"><a href="#ref-12">12</a></sup>, which found that more capable agents are better at exploiting the proxy reward, with the true return even undergoing a sharp downward phase transition; Skalse and colleagues' 2022 proof<sup class="cite"><a href="#ref-13">13</a></sup> that nontrivial rewards are almost impossible to make "unhackable"; and Gao and colleagues' 2023 measurement<sup class="cite"><a href="#ref-14">14</a></sup> of a quantitative scaling law for this overoptimization. A good proxy must dodge both ends at once, being faithful and easier, and that is so rare that the rarity itself is the whole of the craft.

## Calibration: Swap the Form of the Verdict

The second move swaps not the object but the form of the verdict: it no longer demands a binary "true or false" ruling, but gives a calibrated probability, acts on it, and accepts a bounded risk.

What does calibration mean? That the things you say you are sure of should truly occur in the proportion of that sureness. Formally,

$$\Pr\big(Y=1 \mid \hat p=p\big)=p,$$

of the things you report at 70%, in the long run about seven in ten should come true. This is an object of knowledge weaker than "right or wrong," yet attainable and checkable.

![The reliability diagram of calibration: how sure you say you are should match how often it comes true](../figures/f11-calibration.svg)

Its cross-domain shapes are equally tidy. In number theory it is probabilistic primality (that "prime with probability $1-\varepsilon$" of Chapter 7). In machine learning it is conformal prediction (Vovk, Gammerman, and Shafer 2005<sup class="cite"><a href="#ref-26">26</a></sup>), which gives you not a point judgment but a prediction set with a coverage guarantee,

$$\Pr\big(Y\in C(X)\big)\ge 1-\alpha.$$

In meteorology and forecasting science it is a whole mature theory of calibration: Brier's 1950 score<sup class="cite"><a href="#ref-15">15</a></sup>, Murphy's 1973 decomposition<sup class="cite"><a href="#ref-17">17</a></sup> into reliability, resolution, and uncertainty, DeGroot and Fienberg's 1983 systematic treatment<sup class="cite"><a href="#ref-18">18</a></sup>, and Gneiting and colleagues' 2007 modern framework<sup class="cite"><a href="#ref-24">24</a></sup> of "maximize sharpness subject to calibration." Weather forecasting is in fact one of the fields where calibration is done best: when a mature forecasting system says "70% chance of rain tomorrow," and you stretch out all the days it said so, about seven in ten did see rain, sureness fitting reality seamlessly, which is the very model of calibration. There is a deep design here too, the strictly proper scoring rule: a scoring function carefully constructed so that telling the truth (reporting your true probability) is exactly what makes your expected score optimal,

$$p=\arg\max_{q}\ \mathbb{E}_{Y\sim p}\big[S(q,Y)\big].$$

Honesty thereby no longer rests on conscience but is enforced by the mathematical structure of the scoring rule (Savage 1971<sup class="cite"><a href="#ref-16">16</a></sup>, Gneiting and Raftery 2007<sup class="cite"><a href="#ref-23">23</a></sup>). Dawid's 1982 proof<sup class="cite"><a href="#ref-19">19</a></sup> that a Bayesian actor can asymptotically self-calibrate, and Foster and Vohra's 1998 proof<sup class="cite"><a href="#ref-22">22</a></sup> that for any sequence there exists an asymptotically calibrating strategy; but Oakes's 1985 "self-calibrating priors do not exist"<sup class="cite"><a href="#ref-20">20</a></sup> draws the limit of this move. Modern neural networks are in fact often miscalibrated (Guo and colleagues 2017<sup class="cite"><a href="#ref-25">25</a></sup>), and so need recalibration. The graded trust of Chapter 6, allow, ask, block, is precisely what calibration looks like once it lands on action.

Calibration has two ways of failing. The shallower is miscalibration: your claimed sureness does not match reality, you report 90% but only six in ten come true, and so every decision built on it is off. The deeper is subtler and more important: calibration tells you the odds, but does not tell you whether you should accept the bet. A perfectly calibrated "70%" stays silent on the question of whether 70% is good enough for you to wager, because that depends on the size of the stake and the ranking of your values, which is a question of value, not of verification. Conflating the two is the most common trap in acting on calibration: you think the probability has made the decision for you, when in fact it has only laid out the odds, and whether to press the button still requires you to bring out a set of values of your own.

## Why the Two Moves Pair, and Where They Lead

Set the two moves side by side: proxy substitution swaps out the object you verify (a different, checkable target), and calibration swaps out the form of the verdict (a probability, rather than true or false). Neither answers the original question; both swap the problem for one that can be handled. The shared lever is changing your demand on "the answer" itself, one changing what you measure, the other changing what the verdict looks like and putting a price on the residual risk.

But even so, these two moves are still straining to get things right, only with a lowered standard of "right." The last pair of moves is more thorough still: it simply stops hoping to get things right, and turns instead to managing getting them wrong. Since error cannot be prevented, shrink its cost, and make sure that once it happens you can find out. That is Chapter 12.

---

## References

> Waypoints: 1. historical scientific judgment; 2. theoretically studied material; 3. how science progresses; 4. how to live in an unverifiable world. This section was checked source by source.

### Proxy substitution: from Goodhart's law to unanticipated consequences

1. C. A. E. Goodhart (1975). "Problems of Monetary Management: The U.K. Experience." *Papers in Monetary Economics*, Vol. I. Reserve Bank of Australia. [2]
   This is the original source of Goodhart's law, from a 1975 monetary-economics conference in Sydney. Discussing the U.K.'s experience of monetary management, Goodhart noted that once a statistical regularity is used as a target for control, the stable relationship previously observed tends to fail. The chapter uses it as the benchmark for proxy distortion: the correlation between a metric and the true target holds only on the distribution that is the status quo, and snaps once it is treated as a target and optimized.

2. R. K. Merton (1936). "The Unanticipated Consequences of Purposive Social Action." *American Sociological Review*, 1(6), 894-904. [2]
   Merton gives a systematic discussion of why purposive social action produces consequences the actor never foresaw, and sorts out several sources such as ignorance, the urgency of interest, and the constraint of values. It is an early sociological source for the side effects of proxy substitution, reminding the reader that when one optimizes a proxy, what really bites is often the consequences that never entered the field of measurement.

3. D. T. Campbell (1979). "Assessing the Impact of Planned Social Change." *Evaluation and Program Planning*, 2(1), 67-90. [2][4]
   The source of Campbell's law: the more a quantitative social indicator is used for social decision-making, the more it is subject to distortion, and the more apt it is to distort and corrupt the social process it was meant to monitor. Alongside Goodhart's law it is another classic cornerstone of proxy distortion, by which the reader can see clearly the path of corruption a metric takes once high stakes are placed on it.

4. S. Kerr (1975). "On the Folly of Rewarding A, While Hoping for B." *Academy of Management Journal*, 18(4), 769-783. [2][4]
   Kerr examines the widespread incentive mismatch in organizations: the behavior A that managers reward is often not the behavior B they truly hope for, so the incentive system stably produces results contrary to its original intent. It is a management classic on the mismatch of incentive and proxy, corresponding exactly to the real face of this chapter's "optimize the proxy, and the true target rots" cell.

5. M. Strathern (1997). "'Improving ratings': audit in the British University system." *European Review*, 5(3), 305-321. [2][4]
   Strathern, drawing on observations of the British university audit system, gives the widely quoted formulation: when a measure becomes a target, it ceases to be a good measure. This chapter's argument that a proxy distorts once treated as a target often takes this as its concise statement, and the reader can find here the original context of that phrasing.

6. R. E. Lucas (1976). "Econometric Policy Evaluation: A Critique." *Carnegie-Rochester Conference Series on Public Policy*, 1, 19-46. [2][3]
   Lucas's critique points out that the parameter relations estimated in an econometric model depend on the existing policy environment, and once policy is changed on that basis, actors' expectations and behavior adjust accordingly, so the original structural relations no longer hold. It is the economic twin of Goodhart's law, used in this chapter to explain why the pressure of optimization pushes a system off the distribution where proxy and true target agree.

7. W. N. Espeland & M. Sauder (2007). "Rankings and Reactivity: How Public Measures Recreate Social Worlds." *American Journal of Sociology*, 113(1), 1-40. [2][4]
   Espeland and Sauder propose the "reactivity" framework: public rankings and quantitative indicators are not merely measurement, they also change the behavior and even the self-conception of the measured, and so reshape the very social reality they were meant to describe. The chapter uses it to push proxy distortion one layer further: a metric not only distorts, it remakes the object it measures.

8. D. Manheim & S. Garrabrant (2018). "Categorizing Variants of Goodhart's Law." arXiv:1803.04585. [2]
   The two authors attempt to split the loose "Goodhart's law" into several distinct mechanisms (regressional, extremal, causal, and adversarial), whose ways of failing and remedies differ. It gives this chapter's "proxy substitution fails in more than one way" a finer taxonomy, helping the reader tell which kind of distortion they face.

9. J. Z. Muller (2018). *The Tyranny of Metrics*. Princeton University Press. [4]
   Muller, through a wealth of cases from medicine, education, policing, and business, criticizes the fashion of reducing everything to quantifiable indicators and holding people accountable by them, pointing out that this metric worship often brings the consequence of surface compliance and substantive harm. It is a popular survey aimed at the general reader, well suited for recognizing the cost of proxy substitution in life and work.

### Proxy distortion recurring in machine learning: reward hacking and overoptimization

10. D. Amodei, C. Olah, J. Steinhardt, P. Christiano, J. Schulman & D. Mané (2016). "Concrete Problems in AI Safety." arXiv:1606.06565. [2]
    This widely influential survey breaks AI safety into several concrete, researchable problems, among them reward hacking and scalable supervision. It clearly translates the proxy-target distortion long familiar in the social sciences into the machine-learning context, and is the starting point of this chapter's passage on "the same mechanism replaying in machine learning."

11. P. F. Christiano, J. Leike, T. B. Brown, M. Martic, S. Legg & D. Amodei (2017). "Deep Reinforcement Learning from Human Preferences." *Advances in Neural Information Processing Systems*, 30 (NeurIPS 2017). [2][4]
    The authors use human preference comparisons over pairs of trajectories to train a reward model, then drive reinforcement learning with it, thereby sidestepping an objective function hard to write by hand. This is the founding work of RLHF, and exactly the proxy-substitution model this chapter calls "standing in a reward model for human beings' true preferences," from which the reader can understand why such a proxy is both useful and dangerous.

12. A. Pan, K. Bhatia & J. Steinhardt (2022). "The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models." ICLR 2022. [2]
    The authors systematically examine the consequences of misspecified rewards, and give a cautionary empirical phenomenon: more capable agents are often better at exploiting the proxy reward, and the true return can even undergo a sharp, sudden phase transition as capability rises. The chapter uses it to show that proxy distortion is not a linear worsening but may flip abruptly at some point.

13. J. Skalse, N. H. R. Howe, D. Krasheninnikov & D. Krueger (2022). "Defining and Characterizing Reward Hacking." *Advances in Neural Information Processing Systems*, 35 (NeurIPS 2022). [2]
    This paper gives a formal definition of reward hacking and proves that in nontrivial cases an "unhackable" proxy reward almost never exists. It provides the theoretical support for this chapter's "good proxies are rare": faithful and robust proxies are scarce for structural reasons, not by some accidental failure of engineering.

14. L. Gao, J. Schulman & J. Hilton (2023). "Scaling Laws for Reward Model Overoptimization." *Proceedings of the 40th International Conference on Machine Learning* (PMLR 202), 10835-10866. [2]
    The authors give a quantitative characterization of reward-model overoptimization, yielding a scaling-law regularity for how true performance varies with the degree of optimization against the proxy reward: past a certain point, the proxy score still rises while true performance turns down. It pushes Goodhart-style distortion from a qualitative observation to a measurable curve, and is the most empirical piece of this chapter's overoptimization argument.

### Calibration: swap the binary verdict for a probability, and constrain it by strictly proper scoring

15. G. W. Brier (1950). "Verification of Forecasts Expressed in Terms of Probability." *Monthly Weather Review*, 78(1), 1-3. [2]
    Brier proposed a score for evaluating probabilistic forecasts (later the Brier score), bringing "how much sureness was reported, and whether it happened in the end" into a computable assessment. It is the starting point of the calibration and strictly-proper-scoring system, and this chapter's argument that "probability is checkable" begins here.

16. L. J. Savage (1971). "Elicitation of Personal Probabilities and Expectations." *Journal of the American Statistical Association*, 66(336), 783-801. [2]
    Savage studies how to design scoring and incentives so that a person is willing to report their subjective probabilities and expectations truthfully. It lays the theoretical foundation for "a proper scoring rule elicits the true probability," corresponding to this chapter's key design: honesty no longer rests on conscience but is enforced by the mathematical structure of the scoring rule.

17. A. H. Murphy (1973). "A New Vector Partition of the Probability Score." *Journal of Applied Meteorology*, 12(4), 595-600. [2]
    Murphy decomposes the Brier score into three components, reliability, resolution, and uncertainty, letting one see separately where a forecast is miscalibrated and where it has discriminating power. This decomposition is the quantitative skeleton of the calibration concept, and this chapter's distinction between "calibration" and "sharpness" rests precisely on such a breakdown.

18. M. H. DeGroot & S. E. Fienberg (1983). "The Comparison and Evaluation of Forecasters." *Journal of the Royal Statistical Society: Series D (The Statistician)*, 32(1-2), 12-22. [2]
    DeGroot and Fienberg give a systematic treatment of the comparison and evaluation of forecasters, clearly distinguishing calibration from refinement (sharpness) and providing a framework for ranking forecasters accordingly. It is the core theoretical source of this chapter's calibration argument, where the reader can see calibration stated rigorously as a checkable object of knowledge.

19. A. P. Dawid (1982). "The Well-Calibrated Bayesian." *Journal of the American Statistical Association*, 77(379), 605-610. [2]
    Dawid proves that a coherent Bayesian actor, under its own subjective beliefs, will asymptotically self-calibrate, that is, in the long run its probability assertions match the actual frequencies. The chapter uses it to show that calibration is not an externally imposed demand but can be an intrinsic product of rational updating.

20. D. Oakes (1985). "Self-Calibrating Priors Do Not Exist." *Journal of the American Statistical Association*, 80(390), 339-342. [2]
    Oakes points out that no prior can guarantee self-calibration for all data sequences, thereby drawing a boundary around Dawid-style optimistic results. It stands as a counterweight to Dawid (1982) and the Foster-Vohra attainability result, and is the basis for this chapter's note that "calibration has its limit."

21. M. J. Schervish (1989). "A General Method for Comparing Probability Assessors." *The Annals of Statistics*, 17(4), 1856-1879. [2]
    Schervish gives a general method for comparing probability assessors, bringing the various proper scoring rules into a unified comparison framework as special cases. It serves to integrate and tidy calibration theory, helping the reader place scattered scoring rules into the same picture.

22. D. P. Foster & R. V. Vohra (1998). "Asymptotic Calibration." *Biometrika*, 85(2), 379-390. [2]
    Foster and Vohra prove that even facing an arbitrary (even adversarial) sequence of outcomes, there exists a forecasting strategy that asymptotically achieves calibration. This is the key theorem on the attainability of calibration, by which this chapter argues that calibration is an object of knowledge weaker than a true-or-false verdict yet genuinely attainable.

23. T. Gneiting & A. E. Raftery (2007). "Strictly Proper Scoring Rules, Prediction, and Estimation." *Journal of the American Statistical Association*, 102(477), 359-378. [2]
    This is the authoritative survey of strictly proper scoring rules: it systematically organizes which scoring functions make truthful reporting exactly the expected-score-optimal strategy, and connects them with prediction and estimation. It is the theoretical pillar of this chapter's calibration argument, and the reader who wants to understand "honesty enforced by mathematical structure" may read this piece.

24. T. Gneiting, F. Balabdaoui & A. E. Raftery (2007). "Probabilistic Forecasts, Calibration and Sharpness." *Journal of the Royal Statistical Society: Series B (Statistical Methodology)*, 69(2), 243-268. [2]
    The authors propose a modern framework for probabilistic prediction, summing up the goal as "maximize sharpness subject to calibration": first require the forecast to be calibrated, then make it as sharp as possible under that constraint. This chapter's standard for judging whether a probabilistic forecast is good or bad adopts this framework directly.

25. C. Guo, G. Pleiss, Y. Sun & K. Q. Weinberger (2017). "On Calibration of Modern Neural Networks." *Proceedings of the 34th International Conference on Machine Learning* (PMLR 70), 1321-1330. [2]
    The authors find that modern deep neural networks, though often more accurate, are frequently miscalibrated, with confidence systematically deviating from the true correctness rate, and propose simple recalibration methods such as temperature scaling. It is the representative work on the calibration problem on the machine-learning side, corresponding exactly to this chapter's "modern neural networks are in fact often miscalibrated, and so need recalibration."

26. V. Vovk, A. Gammerman & G. Shafer (2005). *Algorithmic Learning in a Random World*. Springer. [2]
    This is the founding monograph of conformal prediction: it gives not a single-point judgment but constructs a prediction set with a coverage guarantee, so that the probability of the true value falling in the set has a controllable lower bound. The chapter uses it as one realization of the calibration idea in machine learning, giving the reader an example of a "prediction that carries its own reliability guarantee."

### The methodological roots of judgment, prediction, and the substitution move

27. P. E. Tetlock (2005). *Expert Political Judgment: How Good Is It? How Can We Know?* Princeton University Press. [1][2]
    Tetlock conducts a large-scale, multi-year tracking of expert political forecasting, finding that the long-run accuracy of many experts is unremarkable and often falls short of simple extrapolation baselines. It is the representative work that puts expert judgment under a checkable framework, and gives empirical support to this chapter's "act on a calibrated probability, rather than trust authoritative assertions."

28. P. E. Tetlock & D. Gardner (2015). *Superforecasting: The Art and Science of Prediction*. Crown. [1][4]
    This book popularizes the research findings of the IARPA forecasting tournament, portraying how the standout "superforecasters" decompose problems, give probabilities, and continually fine-tune with evidence. It leans toward practice, telling exactly how to make judgments that can be checked by calibration in an unverifiable world, well suited for the reader to train their own forecasting habits.

29. G. E. P. Box (1976). "Science and Statistics." *Journal of the American Statistical Association*, 71(356), 791-799. [2][3]
    This is the source of the line "all models are wrong, but some are useful." Box argues that statistical modeling is an iterative process of scientific inquiry, which should pursue not absolute correctness but usefulness and improvability. It serves precisely this chapter's contrast of ways of failing: faithful but intractable, or tractable but only approximate.

30. G. Pólya (1945). *How to Solve It: A New Aspect of Mathematical Method*. Princeton University Press. [2][4]
    Pólya sums up a set of problem-solving heuristics, one of which is "first solve a related, easier problem," then approach the original through it. This is the methodological prototype of the substitution move in this chapter's title, and the reader may see proxy substitution as a generalization of this ancient problem-solving art to settings that cannot be directly verified.

31. H. A. Simon (1956). "Rational Choice and the Structure of the Environment." *Psychological Review*, 63(2), 129-138. [2][4]
    Simon proposes bounded rationality and satisficing: when capacity and information are limited, an actor does not seek the optimum but stops upon finding a "good enough" option. It provides the theoretical grounding for "replacing the unattainable optimum with a good-enough proxy," and is the root of this chapter's substitution move in decision science.

32. D. Kahneman & S. Frederick (2002). "Representativeness Revisited: Attribute Substitution in Intuitive Judgment." In T. Gilovich, D. Griffin & D. Kahneman (eds.), *Heuristics and Biases: The Psychology of Intuitive Judgment*, 49-81. Cambridge University Press. [2]
    Kahneman and Frederick propose "attribute substitution": when the target attribute is hard to assess, a person unconsciously substitutes a more easily assessed attribute to answer in its place. This is the psychological twin of this chapter's proxy-substitution mechanism, showing that swapping the problem is not only an engineering strategy but also the default mode in which human intuition operates.
