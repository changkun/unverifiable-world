# Chapter 13: The Eight Levers

> **Thesis:** The eight moves are not an arbitrary list; each one pulls a different lever within the decomposition of risk and information, and that is exactly why they feel "complete."

Part III handed over that table: eight moves, four pairs, appearing again and again under different jargon across four concrete sites plus science. But a list, however tidy, is still only a list. What this chapter presses on is this: why these eight, and not others? Did I assemble them, or does each of them lodge at some unavoidable position? If the latter, then the convergence has been explained; otherwise this book is at best a handy manual of classification.

I want to put forward a candidate explanation. Let me say the unflattering part first: it is an organizing scheme, not a proof. When you have finished the chapter, please bring along that skeptical knife from Chapter 14.

## A Crude Decomposition

Strip "acting under unverifiability" down to its barest form, and what you are really managing is risk. Borrowing the old language of decision theory (Wald<sup class="cite"><a href="#ref-1">1</a></sup>, Savage<sup class="cite"><a href="#ref-4">4</a></sup>, von Neumann and Morgenstern<sup class="cite"><a href="#ref-3">3</a></sup>), risk can be written, roughly, as

$$\text{Risk}\ \approx\ \Pr(\text{fail})\ \times\ \text{Cost}(\text{fail}),$$

and all of this proceeds under an information budget $B$: the checks, samples, computation, and time you can spend to cut down uncertainty are all finite.

The formula looks simple, but the point is this: the places on its right-hand side where you can intervene are a countable few. You can alter the definition of "failure" itself, or the probability of failure, or your knowledge of that probability, or the cost of failure, or how this information budget is spent, or the timing at which checking happens. My proposition is: the eight moves occupy exactly one position each, with no ninth slot left to fill.

## Eight Moves, Eight Positions

Match each move to the lever it pulls:

| Move | The lever it pulls | Its position in the decomposition of risk |
| --- | --- | --- |
| proxy substitution | changes the target you measure and optimize | rewrites the definition of "failure" itself |
| certificate / bound | presses uncertainty into a guaranteed bound on one slice | drives $\Pr(\text{fail})$ near zero locally |
| oracle in the loop | brings in a verifying power you do not have on your own | lowers $\Pr(\text{fail})$ with outside help |
| redundancy / consensus | makes the failures of several judgments decorrelate | lowers the joint failure probability $\Pr(\text{all\ fail})$ |
| optimal screening | spends the information budget where the marginal return is highest | allocates $B$ to maximize the cut in uncertainty |
| calibration | puts a truthful price on residual risk | makes $\Pr(\text{fail})$ known, so you can bet on it |
| decay / fencing | shrinks the blast radius | lowers $\text{Cost}(\text{fail})$ |
| audit trail | moves checking from before the fact to after it | shifts the timing of checking, turning an irrecoverable failure into a recoverable one |

![The eight moves mapped onto different parts of the decomposition of risk (a candidate organizing scheme, not a theorem)](../figures/f13-eight-levers.svg)

Read this table, and the feeling that it is "an assembled list" should loosen a little. The eight moves are not eight tools gathered at random; they take up, between them, the positions of "$\Pr$, knowledge of $\Pr$, cost, budget allocation, timing of checking, definition of the target," filling almost one by one the places where that decomposition can be acted upon. The proposition can then be put this way: if these really are all the levers there are, then this set of moves is complete, and the convergence is thereby explained, since any capable actor will sooner or later rediscover them, because there is nothing else to pull.

## Why This Can Cross Substrates

If the above holds, it explains, in passing, the puzzle the book opened with: why mathematicians, engineers, and organizations would, without prior agreement, reach for these same eight moves.

In studying vision, Marr<sup class="cite"><a href="#ref-17">17</a></sup> distinguished three levels: the computational level (what problem is to be solved, under what constraints), the algorithmic level (what representations and processes are used), and the implementational level (what hardware it runs on). The eight moves live at the computational level; they are the answer to "given the constraint of unverifiability, which few places can logically still be acted upon," and that answer does not depend on whether you are a carbon-based mathematician, a silicon-based program, or a bureaucracy made of people. The substrate varies wildly, yet the constraint at the computational level is one and the same, so the responses converge. Simon's bounded rationality<sup class="cite"><a href="#ref-12">12</a></sup> and his "sciences of the artificial"<sup class="cite"><a href="#ref-13">13</a></sup> speak of precisely this kind of behavior: shaped by the constraints of the environment rather than by the internal makeup of the actor.

Here we must also bring in the no free lunch theorem (Wolpert and Macready<sup class="cite"><a href="#ref-25">25</a></sup>). It says: averaged over all possible problems, no method outperforms another. This knife cuts both ways. On one side, it supports the book's restraint: there is no universal solution, you must lean on the specific structure of the problem to choose a lever, which is exactly why the five faces must be treated separately. On the other side, it warns: anyone who claims to have "found the unifying key," myself included, should rein in some of their pride. When you cannot even pin down the probability of failure, the levers grow robust versions: Gilboa and Schmeidler's maxmin expected utility<sup class="cite"><a href="#ref-20">20</a></sup>, Hansen and Sargent's robust control<sup class="cite"><a href="#ref-30">30</a></sup>, decision-making under Knightian uncertainty, are all moves that still mount a defense against the worst case even when $\Pr$ itself is ambiguous.

## A Strong Claim That Must Be Amplified

Now amplify the unflattering part.

The scheme above is a candidate organizing structure, not a theorem. That decomposition of risk is informal; I have given no rigorous model of actor and environment, and so I cannot prove that the optimal strategy is exactly these eight levers. "These are all the levers there are" is an assertion, not an established result. I have no evidence that this table is exhaustive, nor can I rule out that it is merely a post hoc framework: a narrative flexible enough to stuff many sets of moves into. Some of the assignments in the table (for instance, redundancy both lowers joint failure and looks like a special kind of screening) even overlap, which itself shows that this decomposition is not yet clean.

I place it here because it has organizing force and explanatory appeal, not because it has been proved. It meets the standard of a good conjecture: clear, refutable, able to unify a large mass of phenomena. But it has not yet risen to a theorem.

So the final question becomes unavoidable: is this cross-domain convergence a law forced out by something, or merely a strong but, in the end, empirical pattern? The next chapter settles the account with it, head-on.

---

## References

> Waypoints: 1. historical scientific judgment; 2. theoretically studied material; 3. how science progresses; 4. how to live in an unverifiable world. This section was checked source by source.

1. A. Wald (1950). *Statistical Decision Functions*. John Wiley & Sons. [2][4]
   Wald recast statistical inference as a decision problem against nature: the decision-maker must choose a strategy under risk (the expectation of loss), using the minimax criterion of minimizing the maximum risk to cope with the unknown state. This book founded statistical decision theory, and the scholarly root of this chapter's crude decomposition, "risk is roughly failure probability times cost," lies right here.
2. A. Wald (1939). "Contributions to the Theory of Statistical Estimation and Testing Hypotheses." *The Annals of Mathematical Statistics*, 10(4), 299-326. [2]
   This is Wald's early paper unifying estimation and testing within a loss-function framework, preceding his later monograph, already introducing the ideas of a risk function and a least favorable prior. It marks the starting point of the turn toward "talking about statistics in the language of decision," and is valuable for understanding why this chapter draws on decision theory.
3. J. von Neumann and O. Morgenstern (1944). *Theory of Games and Economic Behavior*. Princeton University Press. [2]
   Von Neumann and Morgenstern founded game theory and derived the expected utility theorem from a set of axioms: preferences satisfying the rationality axioms can be represented as maximizing the expectation of a utility. This is the normative baseline for "betting under uncertainty," cited here as one source of the chapter's calculus of risk.
4. L. J. Savage (1954). *The Foundations of Statistics*. John Wiley & Sons. [2][4]
   Savage, using a set of axioms about preferences over actions, derived subjective probability and utility together, building Bayesian decision theory on personalist probability. It is the founding work of the modern framework of "subjective probability plus expected utility," and also the target that Ellsberg's paradox later challenges.
5. F. H. Knight (1921). *Risk, Uncertainty and Profit*. Houghton Mifflin. [2]
   Knight distinguished quantifiable "risk" from "uncertainty" to which no probability can be assigned, and argued that entrepreneurial profit comes precisely from bearing the latter. This distinction is the key conceptual source when this chapter speaks of "cannot even pin down the probability of failure," and Knightian uncertainty runs through the later series of robust decision works.
6. J. M. Keynes (1921). *A Treatise on Probability*. Macmillan. [2]
   Keynes developed a logical interpretation of probability, treating it as a rational degree of belief between propositions, and stressed that many probabilities are neither numerical nor necessarily comparable. It laid the groundwork for later non-additive, imprecise probabilities, reminding the reader that the epistemic status of probability itself is far more complex than any formula.
7. F. P. Ramsey (1931). "Truth and Probability." *The Foundations of Mathematics and other Logical Essays* (R. B. Braithwaite, ed.). Kegan Paul, Trench, Trubner & Co., 156-198. [2]
   Ramsey was the first to argue that a person's degree of belief can be measured operationally through their betting behavior, and that avoiding a sure-loss combination (a Dutch book) requires those degrees of belief to obey the axioms of probability. This is the founding work of subjective probability, and it provides the philosophical and operational basis for this chapter's "putting a truthful price on residual risk."
8. B. de Finetti (1937). "La prévision: ses lois logiques, ses sources subjectives." *Annales de l'Institut Henri Poincaré*, 7(1), 1-68. [2]
   De Finetti proposed subjective probability and backed it with the Dutch-book argument and the representation theorem for exchangeability, arguing that probability is "only" a coherent personal degree of belief. Together with Ramsey it forms the cornerstone of Bayesianism, an essential source for understanding calibration and honest pricing.
9. F. J. Anscombe and R. J. Aumann (1963). "A Definition of Subjective Probability." *The Annals of Mathematical Statistics*, 34(1), 199-205. [2]
   The two authors, by introducing objective randomizing devices (such as roulette lotteries), gave an axiomatization of subjective probability and utility more compact than Savage's. This framework later became the standard stage for ambiguity decision theory, and the several ambiguity-aversion works cited in this chapter are built upon it.
10. D. Ellsberg (1961). "Risk, Ambiguity, and the Savage Axioms." *The Quarterly Journal of Economics*, 75(4), 643-669. [2]
    Ellsberg used two famous ball-drawing experiments to show that people systematically prefer known probabilities and avoid "ambiguity," a behavior that violates Savage's axioms and cannot be explained by any single subjective probability. It established ambiguity as an independent phenomenon, and is the direct motivation for the subsequent robust and multiple-prior theories.
11. R. D. Luce and H. Raiffa (1957). *Games and Decisions: Introduction and Critical Survey*. John Wiley & Sons. [2][4]
    This book is a classic introduction to, and critical survey of, game theory and decision theory, both laying out expected utility and game solution concepts clearly and candidly discussing the limits of applicability of each axiom. It suits the reader as a general entry point into the chapter's decision-theoretic background, at once systematic and critical.
12. H. A. Simon (1955). "A Behavioral Model of Rational Choice." *The Quarterly Journal of Economics*, 69(1), 99-118. [2]
    Simon here proposed bounded rationality and "satisficing": an actor limited by cognition and information does not seek the global optimum, but searches until it finds an option good enough and then stops. This is the core support for this chapter's argument that "constraints at the computational level shape behavior," explaining why different substrates converge on the same set of responses.
13. H. A. Simon (1969). *The Sciences of the Artificial*. MIT Press. [2][3]
    Simon argued that the behavior of an artifact is determined more by the constraints of the environment it inhabits than by its internal construction, and called for founding "design" as a discipline of artificial systems. This chapter draws on it to argue that the eight moves live at Marr's computational level, being shaped by the constraints of the environment rather than the internal makeup of the actor.
14. K. R. Popper (1959). *The Logic of Scientific Discovery*. Hutchinson. [2][3]
    Popper systematically proposed falsificationism: a scientific theory cannot be empirically verified, only refuted, so falsifiability becomes the line between science and non-science. When this chapter admits at the close that its decomposition "rises to a good conjecture but not yet to a theorem," it is using precisely this measure of refutability.
15. A. Tversky and D. Kahneman (1974). "Judgment under Uncertainty: Heuristics and Biases." *Science*, 185(4157), 1124-1131. [2]
    Tversky and Kahneman documented the heuristics people use in judging probability (representativeness, availability, anchoring) and the systematic biases they bring. It shows how real actors deviate from the Bayesian ideal, forming a contrast with moves such as calibration and optimal screening that require an honest estimate of probability.
16. D. Kahneman and A. Tversky (1979). "Prospect Theory: An Analysis of Decision under Risk." *Econometrica*, 47(2), 263-291. [2]
    Prospect theory holds that people evaluate outcomes by gains and losses relative to a reference point, rather than by final wealth, are more sensitive to losses, and distort probability weights in a nonlinear way. It is a descriptive correction to expected utility, reminding the reader that cost and probability do not multiply neutrally in real decisions.
17. D. Marr (1982). *Vision: A Computational Investigation into the Human Representation and Processing of Visual Information*. W. H. Freeman. [2][3]
    Marr proposed three levels for analyzing an information-processing system: the computational level (what problem is to be solved), the algorithmic level (what representations and processes are used), and the implementational level (what hardware it runs on). This chapter draws on exactly this hierarchy to argue that the eight moves live at the computational level and can therefore cross carbon-based, silicon-based, and organizational substrates.
18. J. O. Berger (1985). *Statistical Decision Theory and Bayesian Analysis*. Springer-Verlag. [2][4]
    Berger systematically organized the statistical decision theory at the meeting point of the Bayesian and frequentist schools, covering loss functions, risk, admissibility, and robust Bayesian analysis. It is the standard reference for grounding this chapter's informal decomposition of risk in rigorous statistical language.
19. D. E. Bell, H. Raiffa and A. Tversky (eds.) (1988). *Decision Making: Descriptive, Normative, and Prescriptive Interactions*. Cambridge University Press. [2][4]
    This collection is organized around three orientations in decision research: descriptive (how people actually decide), normative (how rationality ought to proceed), and prescriptive (how to help people decide better), and discusses how the three interact. It gives the reader a map for placing the work of each school, echoing this chapter's repeated weighing between the normative and the empirical.
20. I. Gilboa and D. Schmeidler (1989). "Maxmin Expected Utility with Non-Unique Prior." *Journal of Mathematical Economics*, 18(2), 141-153. [2][4]
    Gilboa and Schmeidler gave an axiomatization for ambiguity decision-making: the actor holds a set of priors and evaluates an action by the least favorable among them, that is, a maxmin expected utility over the set of priors. This is exactly the move this chapter describes as "still mounting a defense against the worst case even when $\Pr$ itself is ambiguous," a representative formalization of robust decision-making.
21. D. Schmeidler (1989). "Subjective Probability and Expected Utility without Additivity." *Econometrica*, 57(3), 571-587. [2]
    Schmeidler introduced non-additive subjective probability (capacities) and the corresponding Choquet expected utility, making ambiguity aversion representable in a consistent way. Together with the preceding entry it is a founding work of ambiguity decision theory, loosening, along another technical route, the constraint that probability must be additive.
22. P. Walley (1991). *Statistical Reasoning with Imprecise Probabilities*. Chapman and Hall. [2][4]
    Walley systematically developed the theory of imprecise probabilities, characterizing belief under insufficient evidence with upper and lower probabilities (or a set of probabilities), and gave the corresponding criteria for coherence and inference. It provides a complete statistical language for the predicament of "cannot even pin down the probability," and is the deep theoretical backing for the calibration and robustness lines of thought.
23. G. Gigerenzer and D. G. Goldstein (1996). "Reasoning the Fast and Frugal Way: Models of Bounded Rationality." *Psychological Review*, 103(4), 650-669. [2]
    Gigerenzer and Goldstein argued that simple "fast and frugal" heuristics can, in real environments, often match or even outperform complex models, exhibiting a kind of ecological rationality. It completes Simon's bounded rationality from the positive side, explaining why simple rules may be exactly the reasonable choice when the information budget is limited.
24. D. H. Wolpert (1996). "The Lack of A Priori Distinctions between Learning Algorithms." *Neural Computation*, 8(7), 1341-1390. [2]
    Wolpert proved the no free lunch result for supervised learning: averaged over all possible target functions, any learning algorithm has the same generalization performance. It shows that there is no universal learner independent of problem structure, and is the source, on the learning side, of this chapter's no free lunch argument.
25. D. H. Wolpert and W. G. Macready (1997). "No Free Lunch Theorems for Optimization." *IEEE Transactions on Evolutionary Computation*, 1(1), 67-82. [2]
    Wolpert and Macready extended no free lunch to optimization: averaged over all possible objectives, no optimization algorithm outperforms another. This chapter uses this double-edged knife both to support the restraint that "one must lean on problem structure to choose a lever" and to warn anyone claiming to have found the unifying key to rein in their pride.
26. I. Gilboa and D. Schmeidler (2001). *A Theory of Case-Based Decisions*. Cambridge University Press. [2][4]
    The two authors proposed case-based decision theory: when an actor cannot articulate the state space and probability is out of the question, decisions can be driven by recall of and analogy to past similar cases. It provides another normative model for the predicament in which the probability framework breaks down entirely, broadening this chapter's imagination of how deep "unverifiable" can go.
27. T. F. Bewley (2002). "Knightian Decision Theory. Part I." *Decisions in Economics and Finance*, 25(2), 79-110. [2][4]
    Bewley formalized Knightian uncertainty as the incompleteness of preferences: when the evidence is insufficient to rank two options, the actor may decline to choose, supplemented by an inertia assumption that maintains the status quo. It gives a clean axiomatic expression to "uncertainty that cannot be priced," and is the modern continuation of this chapter's Knightian theme.
28. P. Klibanoff, M. Marinacci and S. Mukerji (2005). "A Smooth Model of Decision Making under Ambiguity." *Econometrica*, 73(6), 1849-1892. [2]
    The three authors proposed a "smooth" model of ambiguity decision-making: by layering a further utility function over a second-order distribution on priors, it separates ambiguity attitude from risk attitude and avoids the non-smooth kink of maxmin. It makes the degree of ambiguity aversion tunable and analyzable, a finer notch within the spectrum of robust decision-making.
29. F. Maccheroni, M. Marinacci and A. Rustichini (2006). "Ambiguity Aversion, Robustness, and the Variational Representation of Preferences." *Econometrica*, 74(6), 1447-1498. [2][4]
    The authors gave the unified representation of variational preferences, gathering maxmin expected utility, multiplier (robust control) preferences, and others as special cases, with ambiguity attitude characterized by a penalty term on deviation. It mathematically links the several robust moves mentioned in this chapter into one family, its value lying in revealing their common skeleton.
30. L. P. Hansen and T. J. Sargent (2008). *Robustness*. Princeton University Press. [2][4]
    Hansen and Sargent brought robust control from control theory into economic decision-making: the decision-maker distrusts the model in hand and so optimizes against the least favorable among a family of nearby models, seeking robustness to specification error. This is the main source of this chapter's "robust control" move, displaying a dynamic form of mounting a defense against the worst case.
31. P. P. Wakker (2010). *Prospect Theory: For Risk and Ambiguity*. Cambridge University Press. [2]
    Wakker systematized and axiomatized prospect theory, handling decision weights under risk and ambiguity in a unified way, and provided operational methods of measurement. It stitches descriptive prospect theory together with normative ambiguity theory, and is the authoritative monograph for the reader going deeper into the theme of probability weighting.
32. I. Gilboa and M. Marinacci (2013). "Ambiguity and the Bayesian Paradigm." *Advances in Economics and Econometrics: Theory and Applications, Tenth World Congress* (D. Acemoglu, M. Arellano and E. Dekel, eds.). Cambridge University Press. [2][4]
    This survey traces the whole line of ambiguity decision-making and faces a fundamental question head-on: in what sense the Bayesian paradigm suffices, and where it needs to be replaced by models such as multiple priors. It is the best navigation into this chapter's cluster of ambiguity and robustness literature, and matches this chapter's restraint in attitude.
33. P. Bossaerts and C. Murawski (2017). "Computational Complexity and Human Decision-Making." *Trends in Cognitive Sciences*, 21(12), 917-929. [2]
    The two authors argued that many real decision problems are intractable in computational complexity (such as the knapsack and other NP-hard problems), and that the brain's performance and strategies are shaped by this hard constraint. It provides hard evidence for bounded rationality from the angle of computational complexity, echoing this chapter's core claim that "constraints at the computational level force convergence."
