# Chapter 4: The Temptation to Flatten

> **Thesis:** Because all five faces show up as "I cannot check it," it is tempting to treat unverifiability as one problem with one solution. About the problem, that is wrong. About the response, it points toward something right.

Chapter 2 spent a whole chapter pulling unverifiability apart into five faces. Chapter 3 then noticed that the moves for coping with those faces resemble one another. Put the two together and a thought arises almost inevitably, and a very tempting one. The faces all share the same feature, "I cannot check it," and they are all handled by much the same means. So why not just declare that unverifiability is one problem and give it one unified solution?

This chapter does two things. First it shows where that thought goes wrong. Then it spells out what the thought gets right by accident, and uses that to set a burden of proof for the whole book.

## Where Flattening Goes Wrong

To flatten is to squash five structurally different faces into one. Chapter 2 has already shown what that costs.

Treat the undecidable as a budget problem, assuming that "more computing power will do it," and you are wrong. The halting problem is not slow to compute. There is no such algorithm, and no faster machine can conjure up a program that does not exist.

Treat an adversarial gap as a mere gap in observation, assuming that "I just haven't seen it clearly yet," and you are wrong in a more dangerous way. The system across from you adjusts to the way you are looking: the more clearly you see, the more cleverly it hides. This is a game against an opponent, not a single measurement. Spam filtering is the textbook case. You train a classifier on the features of today's spam, and the senders immediately change their wording, switch domains, and insert garbled characters to slip past it. Anyone who treats this as a static recognition task and solves it with a one-off model will always be half a step behind.

Treat the intractable as undecidable, and you give up too early on a problem that could have been approximated or handled in the average case. Do the reverse, treating the undecidable as merely intractable, and you will hammer away with computing power at a wall of logic forever. Every such misdiagnosis makes you reach for the wrong tool and pay a real price. Get the diagnosis wrong, and even the finest medicine turns into poison.

So, about the problem, flattening is wrong. The five faces have to be handled separately. That is the conclusion Chapter 2 spent a whole chapter earning, and it cannot be casually given back here.

## What Flattening Gets Right by Accident

Yet there is a grain of truth inside that thought. About the problem, it is wrong. About the response, it happens to get something right.

This book's thesis is that grain of truth, picked out of the surrounding error and stated with great care:

> The sources of unverifiability differ wildly, but the responses a bounded actor is forced into converge, again and again, on the same small set.

Notice how restrained this is. It does not say "these problems are all the same problem." That would be flattening, and it would be wrong. An expert in any one of these fields would throw the book down. It says something different, both stronger and more defensible: the problems all differ, but the responses rhyme. What the book sets out to deliver is that "table of the same move under many vocabularies," together with an explanation of why the convergence lands on these particular moves.

## A Burden of Proof the Book Must Carry

At this point the biggest risk also comes into view. The human mind has a natural love of analogy. Lakoff and Johnson<sup class="cite"><a href="#ref-14">14</a></sup> showed that even everyday language is built out of metaphor, while Gentner<sup class="cite"><a href="#ref-6">6</a></sup>, Holyoak<sup class="cite"><a href="#ref-9">9</a></sup>, Bartha<sup class="cite"><a href="#ref-7">7</a></sup>, and others have studied when an analogy is real and when it only looks good. But because analogy comes so easily, it is also the easiest thing to be fooled by. A beautiful cross-domain analogy often proves nothing at all. The handiest cautionary example is Hofstadter's *Gödel, Escher, Bach*<sup class="cite"><a href="#ref-1">1</a></sup> and the writing in its tradition. Such writing produces cross-domain resonances so dazzling they take your breath away, yet it is often criticized as "in the end just analogy," unable to survive a hard question. A more solid lesson comes from the power-law craze. Many systems were declared to obey the same power law and to share the same deep mechanism, which sounded wonderfully unified. But once they were tested with statistics as strict as those of Clauset, Shalizi, and Newman<sup class="cite"><a href="#ref-25">25</a></sup> in 2009, a great many "power laws" did not hold up. The authors re-examined more than twenty real data sets widely claimed to follow power laws, and only a handful passed the test cleanly. For most, alternatives such as the log-normal could not be ruled out, and often fit at least as well. Stumpf and Porter<sup class="cite"><a href="#ref-26">26</a></sup>, in their 2012 piece "Critical Truths About Power Laws," put it bluntly: looking like one is not the same as being one.

So this book must hold itself to an iron rule: any claimed convergence must be shown to be more than analogy.

What counts as "more than analogy"? The philosophy of science offers a ready yardstick. For a cross-domain mapping to count as substantive, it must be structure-preserving. Surface similarity is not enough. The two sides must correspond in mechanism, in the way they fail, and in their trade-offs. Gentner's<sup class="cite"><a href="#ref-6">6</a></sup> structure-mapping and Bartha's<sup class="cite"><a href="#ref-7">7</a></sup> evaluation of analogical arguments supply this set of standards. There is a still harder test, robustness: a conclusion is more credible if it can be derived again and again by several independent routes. This idea comes from the robustness analysis developed by Levins<sup class="cite"><a href="#ref-17">17</a></sup>, Wimsatt<sup class="cite"><a href="#ref-18">18</a></sup>, and Weisberg<sup class="cite"><a href="#ref-19">19</a></sup>. Anderson's<sup class="cite"><a href="#ref-5">5</a></sup> "More Is Different," Fodor's<sup class="cite"><a href="#ref-27">27</a></sup> argument about the "special sciences," and Cartwright's<sup class="cite"><a href="#ref-28">28</a></sup> *The Dappled World* all show that real patterns across levels do exist, but that they are earned, not declared. Box's<sup class="cite"><a href="#ref-33">33</a></sup> famous line hangs over all of this: all models are wrong, but some are useful. What this book aims for is "useful, and useful in a way that survives testing," not "so elegant that we forget to test it."

In practice, this iron rule means that every time Part III extracts a move, and every time it sets two fields side by side, it has to ask again. Is this transfer substantive (same mechanism, same way of failing, same trade-off), or just a pretty figure of speech? If it survives that questioning, the table stands. If not, the table is only a well-made piece of prose. Chapter 13 will try to ground this convergence in a common underlying structure (the decomposition of risk and information). But that is a promissory note still to be honored, something to be tested, not assumed in advance. Chapter 14 will then take on the question directly: is this a law, or a very strong empirical pattern?

## What Comes Next: The Order of Part II

We cannot just declare the convergence in advance and then pick a few examples to fit it. The only sound way to test it is to walk into real fields and see what skilled practitioners actually did. That means letting the moves grow out of the cases themselves, instead of fixing the moves first and forcing the cases to match.

This is also why the book puts the settings (Part II) before the toolbox of moves (Part III). Abstracting first and illustrating afterward would look arbitrary, and would waste the persuasive force the cases ought to carry. So Part II does not rush to name anything. It lets the moves appear inside their own fields, tangled up with one another and looking somewhat messy on the surface. Only in Part III is each move taken out on its own, cleaned up, and named. Induction first, names after.

Four settings are ready: a designer feeling out what a user has in mind, an agent set loose to act on its own, a mathematician up against the wall of the Riemann hypothesis, and a vast organization that cannot see itself. Their unverifiability comes from different faces among the five. Let us go and see what each of them reaches for when the oracle never comes.

---

## References

> Waypoints: 1. historical scientific judgment; 2. theoretically studied material; 3. how science progresses; 4. how to live in an unverifiable world. This section was checked source by source.

1. D. Hofstadter (1979). *Gödel, Escher, Bach: An Eternal Golden Braid*. Basic Books. [Google Books](https://books.google.com/books?id=yeu2AAAAIAAJ) [2]
   Hofstadter, drawing on Gödel's incompleteness, Escher's visual paradoxes, and Bach's fugues, weaves a grand analogy about how self-reference, recursion, and consciousness emerge from formal systems. It is a benchmark of cross-domain analogical writing, and also this chapter's cautionary case: the resonances are written so dazzlingly that they take the breath away, yet have repeatedly been criticized as "in the end just analogy," a reminder that a beautiful cross-domain resonance does not itself constitute an argument.

2. H. A. Simon (1969). *The Sciences of the Artificial*. MIT Press. [Google Books](https://books.google.com/books?id=hAjtwAEACAAJ) [2][3]
   Simon proposes a science of the "artificial," arguing that design is a subject that can be made systematic, and characterizes the decisions of real actors through bounded rationality and satisficing rather than optimization. Its importance to this chapter lies in treating "how a bounded actor copes under constraints" as a proper object of science, which is the very source of the "responses forced out of an actor" in the book's thesis.

3. W. C. Wimsatt (2007). *Re-Engineering Philosophy for Limited Beings: Piecewise Approximations to Reality*. Harvard University Press. doi:[10.2307/j.ctv1pncnrh](https://doi.org/10.2307/j.ctv1pncnrh) [2][4]
   Wimsatt argues that philosophy should be rewritten for "limited beings": actors with finite cognitive resources can only approximate reality through heuristics, approximations, and robustness, and error is inevitable yet manageable. The title is almost a footnote to this book's secondary thread, and the reader may focus on how it treats robustness as the central tool by which a bounded actor tells real patterns from false ones.

4. H. A. Simon (1962). "The Architecture of Complexity." *Proceedings of the American Philosophical Society*, 106(6), 467-482. [link](https://www.jstor.org/stable/985254) [2][3]
   Simon argues that complex systems are mostly "near-decomposable" hierarchical structures, with tight connections inside subsystems and loose connections between them, an architecture that eases both evolution and understanding. It provides a classic structural argument that "real patterns exist across levels," worth reading alongside Anderson and Fodor.

5. P. W. Anderson (1972). "More Is Different." *Science*, 177(4047), 393-396. doi:[10.1126/science.177.4047.393](https://doi.org/10.1126/science.177.4047.393) [2]
   Anderson opposes the arrogance of reductionism, pointing out that each level brings forth new regularities that the laws of the level below cannot simply derive. This chapter's phrase "More Is Different" comes from here; it shows that real cross-level patterns do exist, but must be earned by their own sciences rather than declared from fundamental physics.

6. D. Gentner (1983). "Structure-Mapping: A Theoretical Framework for Analogy." *Cognitive Science*, 7(2), 155-170. doi:[10.1016/s0364-0213(83)80009-3](https://doi.org/10.1016/s0364-0213%2883%2980009-3) [2]
   Gentner proposes the structure-mapping theory: a good analogy transfers relational structure rather than surface properties, and a systematic web of relations is more valuable than isolated points of similarity. This is the theoretical source of this chapter's criterion that "a substantive analogy must be structure-preserving," and the reader can understand from it what "corresponding in mechanism rather than surface similarity" means.

7. P. Bartha (2010). *By Parallel Reasoning: The Construction and Evaluation of Analogical Arguments*. Oxford University Press. doi:[10.1093/acprof:oso/9780195325539.001.0001](https://doi.org/10.1093/acprof:oso/9780195325539.001.0001) [2]
   Bartha builds a normative framework for evaluating analogical arguments, asking when an analogy can truly bear the weight of inference; the key is whether a relevant causal or structural connection holds between the source domain and the target domain. It supplies an operable criterion for this chapter's iron rule of "more than analogy."

8. M. B. Hesse (1966). *Models and Analogies in Science*. University of Notre Dame Press. (Expanded edition; first published 1963.) [Google Books](https://books.google.com/books?id=SBc0RAAACAAJ) [2][3]
   Hesse analyzes the cognitive functions of models and analogies in science, distinguishing positive, negative, and neutral analogies, and pointing out that the "neutral part" of an analogy is exactly the growth point for scientific prediction and discovery. It is an early founding work of the methodology of analogy, paving the way for the later structure-mapping and analogy evaluation.

9. K. J. Holyoak and P. Thagard (1995). *Mental Leaps: Analogy in Creative Thought*. MIT Press. doi:[10.7551/mitpress/4549.001.0001](https://doi.org/10.7551/mitpress/4549.001.0001) [2]
   Holyoak and Thagard propose a multiconstraint theory of analogy, holding that the human mind completes an analogical mapping under the mutual balancing of three kinds of constraint: structural, semantic, and pragmatic. The book examines analogy within the real processes of cognition and creation, helping the reader understand why analogy is both powerful and error-prone.

10. D. Gentner, K. J. Holyoak, and B. N. Kokinov (Eds.) (2001). *The Analogical Mind: Perspectives from Cognitive Science*. MIT Press. doi:[10.7551/mitpress/1251.001.0001](https://doi.org/10.7551/mitpress/1251.001.0001) [2]
    This collection gathers research on analogy from across the cognitive sciences, from computational models to developmental psychology to neural mechanisms, systematically presenting the research landscape of "when an analogy is true and when it is merely good-looking." It is the chapter's overview entry into the lineage of research on analogy.

11. D. Hofstadter and E. Sander (2013). *Surfaces and Essences: Analogy as the Fuel and Fire of Thinking*. Basic Books. [Google Books](https://books.google.com/books?id=92e30rzcoCkC) [2]
    Hofstadter and Sander argue that analogy is the central engine of thought, that even the most basic categorization and concept formation are ongoing analogy. The book pushes the standing of analogy to its limit, which forms a tension with this chapter's wariness: analogy is everywhere, and precisely for that reason a set of criteria is all the more needed to tell which transfers are substantive.

12. S. Vosniadou and A. Ortony (Eds.) (1989). *Similarity and Analogical Reasoning*. Cambridge University Press. doi:[10.1017/cbo9780511529863](https://doi.org/10.1017/cbo9780511529863) [2]
    This collection concentrates on the relation between similarity and analogical reasoning, asking what "similarity" really means and how it drives reasoning and learning. It provides conceptual preparation for the question behind this chapter: how to tell "looking like" apart from "actually being."

13. K. Dunbar (1995). "How Scientists Really Reason: Scientific Reasoning in Real-World Laboratories." In R. J. Sternberg and J. E. Davidson (Eds.), *The Nature of Insight*, 365-395. MIT Press. doi:[10.7551/mitpress/4879.003.0017](https://doi.org/10.7551/mitpress/4879.003.0017) [1][2][3]
    Dunbar observed molecular biology laboratories in the field and found that scientists make heavy use of analogy in real work, and that near, within-domain analogies are often more fruitful than distant ones. With field evidence it supports this chapter's methodological choice to "let the moves grow out of the cases themselves," showing that real reasoning differs from the textbook account.

14. G. Lakoff and M. Johnson (1980). *Metaphors We Live By*. University of Chicago Press. [Google Books](https://books.google.com/books?id=r6nOYYtxzUoC) [2]
    Lakoff and Johnson argue that metaphor is not mere rhetoric but the very structure of the human conceptual system, and that even everyday expressions like "time is money" conceal systematic metaphors. This chapter cites it to show that analogy and metaphor are deeply rooted in human thought, and that precisely for this reason their reliability calls for more caution.

15. A. Tversky and D. Kahneman (1974). "Judgment under Uncertainty: Heuristics and Biases." *Science*, 185(4157), 1124-1131. doi:[10.1126/science.185.4157.1124](https://doi.org/10.1126/science.185.4157.1124) [2][4]
    Tversky and Kahneman reveal that people make judgments under uncertainty by relying on heuristics such as representativeness, availability, and anchoring, shortcuts that are efficient yet lead to systematic biases. It reminds the reader that a bounded actor's responses are often not optimal solutions but makeshift moves, and also explains why a beautiful analogy is so apt to fool us.

16. R. W. Batterman (2001). *The Devil in the Details: Asymptotic Reasoning in Explanation, Reduction, and Emergence*. Oxford University Press. (Hardcover first published November 2001; some catalogues record it as 2002.) doi:[10.1093/0195146476.001.0001](https://doi.org/10.1093/0195146476.001.0001) [2][3]
    Batterman studies the role of asymptotic reasoning in explanation, arguing that the explanation of many physical phenomena hides precisely in the "details" that emerge when taking a limit, and that universality has its source there. It provides a fine philosophical case for "how a common structure across systems is possible," echoing this chapter's inquiry into the mechanism of convergence.

17. R. Levins (1966). "The Strategy of Model Building in Population Biology." *American Scientist*, 54(4), 421-431. [link](https://www.jstor.org/stable/27836590) [2][3]
    Levins points out that model building cannot at once attain generality, precision, and realism, that the modeler must trade off, and proposes that when several models with different assumptions yield a consistent conclusion, that conclusion is more credible. This is the source of robustness analysis, from which comes this chapter's hard criterion that "what is derived again and again from multiple routes is more credible."

18. W. C. Wimsatt (1981). "Robustness, Reliability, and Overdetermination." In M. B. Brewer and B. E. Collins (Eds.), *Scientific Inquiry and the Social Sciences*, 124-163. Jossey-Bass. [Google Books](https://books.google.com/books?id=KEPlAQAACAAJ) [2][3]
    Wimsatt systematically develops the concept of robustness: what can be jointly detected by several mutually independent means, models, or perspectives is more likely to be real than an artifact. This paper is the core source for this chapter's robustness criterion, and from it the reader can understand why the convergence of independent routes suppresses error.

19. M. Weisberg (2006). "Robustness Analysis." *Philosophy of Science*, 73(5), 730-742. doi:[10.1086/518628](https://doi.org/10.1086/518628) [2][3]
    Weisberg re-clarifies the logic of robustness analysis, distinguishing a robust theorem from the test of its empirical adequacy, and clarifying when it can and cannot lend support to a conclusion. It makes this chapter's robustness criterion more precise, reminding the reader that robust does not automatically equal true, and that empirical checking is still required.

20. S. H. Orzack and E. Sober (1993). "A Critical Assessment of Levins's The Strategy of Model Building in Population Biology (1966)." *The Quarterly Review of Biology*, 68(4), 533-546. doi:[10.1086/418301](https://doi.org/10.1086/418301) [2][3]
    Orzack and Sober critically examine Levins's modeling strategy, questioning whether the agreement of several models alone can logically warrant inferring a conclusion to be true, unless those models have each already received independent support. It is an important counterweight to the robustness argument, helping this chapter hold its iron rule more tightly and avoid mistaking agreement for proof.

21. N. Goldenfeld and L. P. Kadanoff (1999). "Simple Lessons from Complexity." *Science*, 284(5411), 87-89. doi:[10.1126/science.284.5411.87](https://doi.org/10.1126/science.284.5411.87) [2][3]
    Goldenfeld and Kadanoff remind us that studying complex systems calls for using the right model at the right scale, that universality, however alluring, should not obscure the concrete mechanism, and that the key is to "make the right simplification at the right level." It provides this chapter a sober voice from within physics on how to treat cross-system universal regularities with care.

22. L. P. Kadanoff (1966). "Scaling Laws for Ising Models near Tc." *Physics Physique Fizika*, 2(6), 263-272. doi:[10.1103/physicsphysiquefizika.2.263](https://doi.org/10.1103/physicsphysiquefizika.2.263) [2]
    Kadanoff proposes the block-spin scaling picture, showing that near the critical point a system is self-similar across different scales, and laying the foundation for the later renormalization group and the theory of universality classes. It is a classic example of the genuine universality in which "different systems share the same critical behavior," standing in exact contrast to the later "power laws" that fail to hold.

23. P. Bak, C. Tang, and K. Wiesenfeld (1987). "Self-Organized Criticality: An Explanation of the 1/f Noise." *Physical Review Letters*, 59(4), 381-384. doi:[10.1103/physrevlett.59.381](https://doi.org/10.1103/physrevlett.59.381) [2]
    Bak, Tang, and Wiesenfeld propose self-organized criticality, using the sandpile model to show that certain systems evolve spontaneously to a critical state, giving rise to power-law distributions and 1/f noise. It set off the later power law craze, serving both as a representative of the cross-system unifying narrative and as an object of this chapter's call for "strict statistical testing."

24. A.-L. Barabási and R. Albert (1999). "Emergence of Scaling in Random Networks." *Science*, 286(5439), 509-512. doi:[10.1126/science.286.5439.509](https://doi.org/10.1126/science.286.5439.509) [2][3]
    Barabási and Albert propose the scale-free network model, explaining the power-law degree distribution of many real networks through the mechanism of growth plus preferential attachment. It is a founding work of network science, and also belongs to that batch of systems widely claimed to obey the same power law, fit to be re-examined under this chapter's critical lens.

25. A. Clauset, C. R. Shalizi, and M. E. J. Newman (2009). "Power-Law Distributions in Empirical Data." *SIAM Review*, 51(4), 661-703. doi:[10.1137/070710111](https://doi.org/10.1137/070710111) [2]
    Clauset, Shalizi, and Newman propose a rigorous statistical method to test whether data truly obey a power law, including maximum-likelihood fitting and comparison against alternative distributions. After re-checking with this method, many previously claimed "power laws" do not hold. It is exactly the methodological model for this chapter's iron rule that "any claimed convergence must survive strict testing."

26. M. P. H. Stumpf and M. A. Porter (2012). "Critical Truths About Power Laws." *Science*, 335(6069), 665-666. doi:[10.1126/science.1216142](https://doi.org/10.1126/science.1216142) [2]
    Stumpf and Porter sum up the lessons of power-law research, stating bluntly that looking like a power law is far from being one, still less from there being a common deep mechanism behind it, and that statistical fit and mechanistic explanation must be kept apart. This chapter's phrase "looking like one is not the same as being one" derives from here, and is the direct basis for tightening the burden of proof.

27. J. A. Fodor (1974). "Special Sciences (or: The Disunity of Science as a Working Hypothesis)." *Synthese*, 28(2), 97-115. doi:[10.1007/bf00485230](https://doi.org/10.1007/bf00485230) [2]
    Fodor argues that the laws of "special sciences" such as psychology and economics are multiply realizable and cannot be reduced to physics, so that science is in essence disunified. This chapter cites it to support that "real cross-level patterns do exist and cannot be declared away by reduction," in the same camp as Anderson and Cartwright.

28. N. Cartwright (1999). *The Dappled World: A Study of the Boundaries of Science*. Cambridge University Press. doi:[10.1017/cbo9781139167093](https://doi.org/10.1017/cbo9781139167093) [2][3]
    Cartwright argues that the world is "dappled," that physical laws hold only within their own local domains and do not constitute a single unified picture covering everything, and that universality is the exception rather than the norm. The book lends strong metaphysical support to this chapter's stance that "real patterns are earned, not declared."

29. M. Mitchell (2009). *Complexity: A Guided Tour*. Oxford University Press. doi:[10.1093/oso/9780195124415.001.0001](https://doi.org/10.1093/oso/9780195124415.001.0001) [2][3]
    Mitchell writes a clear and reliable guide to the science of complex systems, covering information, computation, evolution, networks, and emergence, while keeping a cautious distance from the field's common overstatements. It is a safe entry point for the reader into the topics of complexity and power laws, and in attitude it accords with this chapter's restraint.

30. D. Sornette (2006). *Critical Phenomena in Natural Sciences: Chaos, Fractals, Selforganization and Disorder* (2nd ed.). Springer. (First edition 2000.) [Google Books](https://books.google.com/books?id=knjtCAAAQBAJ) [2]
    Sornette systematically surveys the mathematics behind critical phenomena, power laws, fractals, and self-organization in the natural sciences, giving technical tools for handling such heavy-tailed and scaling behavior. It represents the ambition to find universal scaling laws across disciplines, and can be read alongside the literature critical of power laws to see the distance between claim and test.

31. G. West (2017). *Scale: The Universal Laws of Growth, Innovation, Sustainability, and the Pace of Life in Organisms, Cities, Economies, and Companies*. Penguin Press. [Google Books](https://books.google.com/books?id=bJPZDAAAQBAJ) [2]
    West proposes that everything from organisms to cities to companies follows certain scaling laws, such as the sublinear scaling of metabolic rate with body size, attempting to find unified quantitative laws for life and society. The book is a contemporary representative of the grand cross-domain universality narrative, fit for the reader to weigh by this chapter's criteria: which are substantive convergences, and which only a moving vision of unity.

32. P. Galison (1997). *Image and Logic: A Material Culture of Microphysics*. University of Chicago Press. [Google Books](https://books.google.com/books?id=6Gcu92U8CwYC) [1][3]
    Galison studies the experimental culture of twentieth-century microphysics, proposing that different subdisciplines collaborate in a "trading zone" through a working pidgin, able to work together even when their theoretical frameworks do not agree. It demonstrates how different fields genuinely connect with one another without being forcibly unified, echoing this book's emphasis on "rhyming rather than being the same."

33. G. E. P. Box (1976). "Science and Statistics." *Journal of the American Statistical Association*, 71(356), 791-799. doi:[10.1080/01621459.1976.10480949](https://doi.org/10.1080/01621459.1976.10480949) [3][4]
    Box here sets out science as an iterative process of repeatedly matching model against reality and gradually closing in, and writes "all models are wrong"; the widely quoted full form, "all models are wrong, but some are useful," appears in Box and Draper's *Empirical Model-Building and Response Surfaces* (1987, p. 424). This chapter hangs that line overhead to define what the whole book strives for: useful, and useful in a way that survives testing, not so elegant that one forgets to test it.

34. T. S. Kuhn (1962). *The Structure of Scientific Revolutions*. University of Chicago Press. [Google Books](https://books.google.com/books?id=3eP5Y_OOuzwC) [1][3]
    Kuhn proposes the famous framework of paradigm and scientific revolution, distinguishing the puzzle-solving of normal science from the incommensurability of paradigm change, and reshaping the understanding of "how science progresses." It is a foundational work coloring this book's thinking about scientific progress and judgment, reminding the reader that comparison across paradigms is never a simple item-by-item correspondence.
