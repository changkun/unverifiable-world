# Chapter 3: Falsifiable, Not Verifiable

> **Thesis:** The most disciplined way humans have to seek knowledge, empirical science, rests on a public admission: a theory can never be verified, only left unfalsified.

The previous chapter asked whether humans have a mature, disciplined way to live alongside the unverifiable for the long haul. There is one: empirical science. And the most surprising thing about it is that its first principle is not the claim that it can establish the truth, but precisely the public admission that it can never do so.

## A Black Swan

"All swans are white." You have seen a thousand white swans, you have seen a million, and this universal statement is still not verified, because the next one may be black. But you need only see a single black swan, and it is overturned completely. This is no made-up example: in Europe, "all swans are white" was long taken as unquestioned common sense, until in 1697 a Dutch expedition saw a black swan for the first time in Western Australia, and that "certainty" was voided overnight.

This asymmetry is the pivot of the whole chapter. To verify a universal proposition you must check every case it asserts, and those cases are typically infinite, open, and lodged in the future, so the thing simply cannot be done. But to falsify it, a single counterexample suffices. Written out in logic: $\forall x\,P(x)$ cannot be established by any finite set of observations, but a single $\exists x\,\lnot P(x)$ is enough to shatter it. The entire discipline of science is built on recognizing and exploiting this asymmetry.

![The asymmetry between verification and falsification](../figures/f03-falsification.svg)

## Hume's Impassable Threshold

The root of this was already dug out by Hume in 1739<sup class="cite"><a href="#ref-4">4</a></sup>. On what grounds do we believe that a regularity that has held in the past will go on holding in the future? There is no logical warrant for it. From "the sun has risen every day in the past" you cannot infer "the sun must rise tomorrow," because the inference itself presupposes that "past patterns will continue into the future," which is exactly the thing to be proved. Induction carries no logical guarantee. Hume's conclusion is calm and complete: what we rely on is not proof, but habit.

This is the philosophical footing of the "future" breach from Chapter 1. Any knowledge of the world's general regularities is built on a finite past, and therefore cannot be verified in advance. If science is to count as knowledge, it cannot take "verification" as its goal, for that goal is simply out of reach.

## Popper: Trading the Unreachable for the Reachable

Popper, in 1934<sup class="cite"><a href="#ref-1">1</a></sup> (in the original German), offered a way out: since verification is unattainable, stop demanding it, and use falsification instead. Whether a theory is scientific does not turn on how much evidence can support it (support can always be found), but on whether it has stuck its neck out and made risky predictions that could be overturned. Astrology, and any doctrine that explains away everything, is unfalsifiable and therefore unscientific; general relativity predicted that starlight would be bent by the sun's gravity through a specific angle, and the 1919 eclipse observation could perfectly well have measured a different value and so refuted the prediction. It is precisely because the theory dared to risk being overturned that it is good science.

So science became a machine optimized specifically for living alongside the unverifiable. It never claims to have proved anything; it says only that this theory has not yet been falsified, so we shall use it for now. This is a posture, a posture of trading the unmeasurable "true" for the measurable "not yet overturned." Look familiar? This is exactly what the mathematician's proxy substitution in Chapter 7 looks like at the scale of epistemology.

## A Necessary Qualification

It must be said plainly, right here: Popperian falsificationism is far from settled in the philosophy of science, and this book treats it as a clear point of entry, not as a final word.

Its most forceful objection comes from the holism of Duhem and Quine (also called the Quine-Duhem thesis). Duhem in 1906<sup class="cite"><a href="#ref-10">10</a></sup> and Quine in 1951<sup class="cite"><a href="#ref-9">9</a></sup> pointed out that you can never test a hypothesis in isolation. Any prediction depends on a large bundle of auxiliary assumptions (the instrument is not broken, the background conditions hold, the approximation is reasonable), and once an experiment fails, you can always turn the blame toward some auxiliary assumption and keep the core hypothesis intact. So the picture in which "a single counterexample cleanly overturns a theory" is not as clean as it looks. Kuhn in 1962<sup class="cite"><a href="#ref-5">5</a></sup> went further: scientists in a period of normal science are in no hurry to falsify at all; anomalies are set aside until a paradigm crisis brings about a revolutionary replacement. Lakatos in 1970<sup class="cite"><a href="#ref-6">6</a></sup> used the progress and degeneration of a "research programme" to replace black-and-white falsification; Feyerabend<sup class="cite"><a href="#ref-7">7</a></sup> simply opposed any unified method at all. Another route is Bayesian confirmation theory<sup class="cite"><a href="#ref-24">24</a></sup>, which wants no two-valued verdict but instead treats evidence as an adjustment to the probability of a belief,

$$P(H\mid e)=\frac{P(e\mid H)\,P(H)}{P(e)},$$

which in turn foreshadows the later move of calibration. Mayo's "severe testing"<sup class="cite"><a href="#ref-14">14</a></sup> is a refined heir of falsificationism, while Stanford<sup class="cite"><a href="#ref-19">19</a></sup> reminds us that a great many "unconceived alternatives" still lie beyond our view.

Laying these disputes out does not dismantle Popper; it enacts what this book itself ought to do: state a powerful framework while marking its boundaries. This posture is exactly the move the whole book sets out to rehearse.

## Science Discovered Those Moves Long Ago

Here is this chapter's real gift to the book. If you look at the everyday machinery of science with the eye of the eight moves, you find that it worked several of them out long ago, only under different names.

Peer review is redundancy and consensus: it distrusts any single judge and uses several mutually independent reviewers, taking their agreement. Replication is also redundancy: a result is not taken seriously until someone else reproduces it independently elsewhere. Preregistration is an audit trail: before the data are seen, the hypothesis and the analysis plan are registered, so the target cannot be moved afterward and noise cannot be talked up into signal. Confidence intervals and error statistics are certificates and bounds: they do not claim a proposition is true, only that, at an explicit confidence level, a bounded guarantee holds. Double-blinding and randomization are defenses against the fifth face (adversarial), and here the adversary is often the researcher's own bias and subjective expectation. The significance threshold is a crude form of calibration.

In other words, humanity's most serious enterprise of inquiry is itself a living sample of this book's convergence claim. This is the book's first and quite weighty hint: although the unverifiability science faces (about general regularities, about the future) has its own particular source, the responses it is forced into rhyme with the responses in software, mathematics, and organizations.

## When the Machine Fails: The Replication Crisis

The reverse view makes it clearer. When these moves are weakened, science's self-correction breaks down, and that is the replication crisis. Ioannidis, in his 2005 paper<sup class="cite"><a href="#ref-28">28</a></sup> "Why Most Published Research Findings Are False," and the Open Science Collaboration's 2015 large-scale replication<sup class="cite"><a href="#ref-29">29</a></sup> of a hundred psychology studies (97 percent of which had originally reported significant results, of which only about thirty-six still held after redoing them, fewer than half) lay this scene bare: when preregistration is absent (the target can be moved afterward), sample sizes are too small, publication bias passes only the pretty results, and few people undertake the thankless work of replication, the machine spins in neutral.

The diagnosis and repair of this crisis are carried out in the very language of those moves: restoring preregistration (putting the audit trail back), encouraging and rewarding replication (putting the redundancy back), registered reports, and raising the severity of testing. Problem and remedy fall onto the same vocabulary. This point will return in Chapter 10 on borrowed judgment and Chapter 12 on audit trails and auditing.

## Where This Chapter Leads

Science has proved one thing: a person can seek knowledge in a disciplined way in a world without verification, and wherever this is done well, it relies on those very moves. This is a proof of concept for the whole book.

But a trap lurks here too. Precisely because all five faces appear with the same expression, "I cannot check it," and precisely because the moves for handling them are so similar, a deeply tempting thought arises: why not simply declare that unverifiability is one problem with one unified solution? The part of this thought about the "problem" is wrong; the part about the "response" stumbles onto something right. The next chapter is devoted to this temptation.

---

## References

> Waypoints: 1. historical scientific judgment; 2. theoretically studied material; 3. how science progresses; 4. how to live in an unverifiable world. This section was checked source by source.

1. K. Popper (1959). *The Logic of Scientific Discovery*. Hutchinson. [2][3]
   Popper here sets out falsificationism systematically: a scientific theory cannot be empirically verified, only refuted, so falsifiability becomes the line between science and non-science. The original German edition, *Logik der Forschung*, was published by Springer in Vienna, with the copyright page marked 1935 though it actually appeared in late 1934 (hence often dated 1934); this English edition was substantially revised and expanded by the author himself. The section "Popper: Trading the Unreachable for the Reachable" is built directly on this, and the reader should attend above all to the epistemological posture of replacing "verification" with "not yet falsified."

2. K. Popper (1963). *Conjectures and Refutations: The Growth of Scientific Knowledge*. Routledge and Kegan Paul. [3]
   This essay collection unfolds falsificationism into a whole view of the growth of knowledge: knowledge advances through bold conjecture and merciless refutation, and the growth of science is not the accumulation of confirmations but the ceaseless weeding out of errors. Compared with the logical skeleton of the earlier work, it shows more vividly how "trial and error" drives scientific progress, and is good reading for understanding this chapter's waypoint of how science progresses.

3. K. Popper (1972). *Objective Knowledge: An Evolutionary Approach*. Clarendon Press. [3]
   Popper here likens the growth of knowledge to an evolutionary process of trial and error, and proposes a "third world," the domain of objective knowledge itself, existing independently of any individual subjective mind. It pushes falsificationism toward an ontological picture of how objective knowledge can accumulate without a subject, and offers further reading for those who wish to pursue how science progresses in depth.

4. D. Hume (1739). *A Treatise of Human Nature*. John Noon. [2]
   Hume here raises the problem of induction, that source-level difficulty: from a past regularity one cannot infer a future regularity, because the inference itself presupposes the "uniformity of nature," which is precisely what is to be proved; our belief in causation and regularity comes, in the end, from habit rather than proof. Books I and II were published by John Noon in 1739, and Book III, *Of Morals*, by Thomas Longman in 1740, with the first edition conventionally dated 1739. The section "Hume's Impassable Threshold" is founded on this, the philosophical footing for understanding why science cannot take "verification" as its goal.

5. T. Kuhn (1962). *The Structure of Scientific Revolutions*. University of Chicago Press. [1][3]
   Kuhn, drawing on a great many cases from the history of science, argues that science does not approach truth at a steady pace, but solves puzzles within a shared paradigm during periods of "normal science," and only after anomalies accumulate into crisis does a paradigm-shifting scientific revolution occur, with old and new paradigms being incommensurable. It is an important correction to Popper's picture, showing that scientists are often in no hurry to falsify an anomaly. This chapter's "A Necessary Qualification" cites it to mark the boundary of falsificationism.

6. I. Lakatos (1970). "Falsification and the Methodology of Scientific Research Programmes." In I. Lakatos and A. Musgrave (eds.), *Criticism and the Growth of Knowledge*, pp. 91-196. Cambridge University Press. [1][3]
   Lakatos uses the "research programme" to reconcile Popper and Kuhn: each programme has a protected hard core and a surrounding belt of adjustable auxiliary assumptions, and the standard of judgment is not a single counterexample but whether the programme as a whole is, over time, "progressing" (continuing to make and fulfill new predictions) or "degenerating" (busy only with patching after the fact). It replaces black-and-white falsification with a historical judgment about a programme's advance or retreat, a key reference when this chapter delimits the boundary of falsificationism.

7. P. Feyerabend (1975). *Against Method: Outline of an Anarchistic Theory of Knowledge*. New Left Books. [1][3][4]
   Feyerabend argues forcefully, through cases from the history of science such as Galileo, that there is no universally valid set of scientific methods, and that major advances often come precisely from breaking existing rules, hence his famous slogan "anything goes." It is the most radical opposition to a unified methodology, cited in this chapter to make plain that even a methodological claim as mild as "falsification" is rejected at the root by some.

8. C. G. Hempel (1965). *Aspects of Scientific Explanation and Other Essays in the Philosophy of Science*. Free Press. [2]
   In this essay collection Hempel gives a culminating account of the covering-law model of scientific explanation, including both deductive-nomological and inductive-statistical explanation, and discusses the logic of confirmation and its paradoxes. It represents logical empiricism's systematic characterization of the "theoretically studied material," and supplies this chapter with a classic background on what counts as testable and explicable.

9. W. V. O. Quine (1951). "Two Dogmas of Empiricism." *The Philosophical Review*, 60(1), 20-43. [2]
   Quine attacks the two dogmas of logical empiricism, the sharp divide between analytic and synthetic and reductionism, and proposes epistemological holism, holding that our beliefs face experience together as one whole web, and that no single statement can be verified or refuted in isolation. Combined with Duhem's holism of testing (jointly called the Quine-Duhem thesis), it strikes directly at the picture in which "a single counterexample cleanly overturns a hypothesis," a core reference for this chapter's delimiting of the boundary of falsificationism.

10. P. Duhem (1906). *La théorie physique: son objet, sa structure*. Chevalier & Rivière. [2]
    Duhem here proposes the holism of testing: an experiment in physics never tests an isolated hypothesis but rather "the hypothesis together with a whole set of auxiliary assumptions and background theories," so a failed prediction cannot determine exactly where the error lies. This is the source of what was later, with Quine, called holism, used in this chapter to show that the bearing of a counterexample is not as definite as it appears. The original 1906 French edition is taken as authoritative here; the second edition was published by Marcel Rivière in 1914, and P. P. Wiener's English translation, *The Aim and Structure of Physical Theory*, was issued by Princeton University Press in 1954.

11. M. Polanyi (1958). *Personal Knowledge: Towards a Post-Critical Philosophy*. University of Chicago Press. [1][4]
    Polanyi proposes "tacit knowledge": we know far more than we can tell, and in scientific inquiry there is always a layer of personal judgment and craft that cannot be formalized and can only be acquired through practice and apprenticeship. It reminds us that no methodology, however strict, can eliminate the scientist's own, inarticulable judgment, echoing this chapter's waypoints of historical scientific judgment and how to live in an unverifiable world.

12. B. C. van Fraassen (1980). *The Scientific Image*. Clarendon Press. [2][4]
    Van Fraassen proposes "constructive empiricism": the aim of science is not to claim a theory is true but only that it is "empirically adequate," that is, that it correctly saves the observable phenomena; to accept a theory is to believe it empirically adequate, not to believe its unobservable parts actually exist. It turns "unverifiable" into a mature scientific attitude, resonating with this chapter's posture of replacing "true" with "not yet overturned."

13. I. Hacking (1983). *Representing and Intervening: Introductory Topics in the Philosophy of Natural Science*. Cambridge University Press. [2][3]
    Hacking shifts philosophical attention from "representing" to "intervening," arguing that the best defense of realism lies not in theory but in experiment: when we can stably manipulate electrons to probe other things, electrons are real ("if you can spray them, they are real"). It opens a new approach to scientific realism grounded in experimental practice, and reminds the reader that scientific progress likewise depends on hands-on intervention, not on theoretical testing alone.

14. D. G. Mayo (1996). *Error and the Growth of Experimental Knowledge*. University of Chicago Press. [3]
    Mayo proposes the philosophy of "error statistics": we have reason to accept a hypothesis only when it has passed a severe test, one that "would very probably have failed if the hypothesis were false." This makes Popper's spirit of falsification operational as a statistical testing procedure, and is a refined heir of falsificationism; this chapter's notion of "severe testing" comes from here (part of the Science and Its Conceptual Foundations series).

15. D. G. Mayo (2018). *Statistical Inference as Severe Testing: How to Get Beyond the Statistics Wars*. Cambridge University Press. [3][4]
    Mayo here reconstructs statistical inference around "severity" as a unifying principle, attempting to get past the long-running "statistics wars" between frequentists and Bayesians, and on this basis responds to criticisms of significance testing in the replication crisis. It develops the programme of item 14 into a methodology facing contemporary statistical practice, and is especially apt for understanding how to use statistical evidence responsibly in an unverifiable world.

16. L. Laudan (1981). "A Confutation of Convergent Realism." *Philosophy of Science*, 48(1), 19-49. [1][2]
    Laudan lists a batch of theories from the history of science that were once successful (able to predict, able to explain) yet were finally abandoned, such as phlogiston and the ether, arguing that the inference "success implies truth" does not hold up, a forceful rebuttal to convergent realism often called the "pessimistic meta-induction." It shows that even empirically very successful theories need not be close to the truth, reinforcing this chapter's claim that science does not take "verifying the truth" as its goal.

17. L. Laudan (1977). *Progress and Its Problems: Towards a Theory of Scientific Growth*. University of California Press. [3]
    Laudan argues for measuring scientific progress by "problem-solving capacity" rather than approach to truth: whether a research tradition progresses turns on the net gain in the empirical and conceptual problems it solves. It offers a view of progress that bypasses the concept of truth, supplying this chapter's how-science-progresses with an alternative framework that does not depend on verification.

18. P. Kitcher (1993). *The Advancement of Science: Science without Legend, Objectivity without Illusions*. Oxford University Press. [3]
    Kitcher, having discarded the "legend" of science as all-knowing and all-powerful, also refuses relativism, and instead rebuilds a moderate and defensible objectivity and view of progress from science's social and cognitive practice. It demonstrates how one can, while admitting that science is shaped by history and society, still hold onto the two concepts of progress and objectivity, in line with this chapter's stance of affirming science while marking its boundaries.

19. P. K. Stanford (2006). *Exceeding Our Grasp: Science, History, and the Problem of Unconceived Alternatives*. Oxford University Press. [1][2][3][4]
    Stanford raises the problem of "unconceived alternatives": the history of science shows again and again that past scientists always had theoretical options that only appeared later and were utterly unthinkable at the time, so we have no reason to believe that we have today exhausted all viable explanations. He distills this "new induction" from historical cases such as genetics, directly echoing this book's framework of "an unverifiable world," and reminding the reader that there is always an unconceived possibility beyond our view.

20. N. Goodman (1955). *Fact, Fiction, and Forecast*. Harvard University Press. [2]
    Goodman raises the "new riddle of induction": "green" and the artificial predicate "grue" (meaning observed as green before a certain time and blue thereafter) both fit all observations to date equally well, yet yield opposite predictions, which shows that induction cannot be settled by evidence alone but must also depend on which predicates are "projectible." It shows that the difficulty of induction is not only the Humean problem of justification but, more deeply, the indeterminacy of the regularity itself, deepening this chapter's understanding of why induction is unreliable. The first-edition year is commonly given as 1955 (one HUP blurb gives 1954, a slight ambiguity; the widely cited 1955 is followed here).

21. C. G. Hempel and P. Oppenheim (1948). "Studies in the Logic of Explanation." *Philosophy of Science*, 15(2), 135-175. [2]
    Hempel and Oppenheim here lay the foundation of the deductive-nomological (D-N) model of explanation: that a phenomenon is scientifically explained means that it can be logically derived from general laws plus initial conditions. It is the starting point of twentieth-century theories of scientific explanation, defining what "being explicable" means logically, and supplying this chapter with an underlying framework for how science characterizes regularities.

22. R. Carnap (1936-1937). "Testability and Meaning." *Philosophy of Science*, 3(4), 419-471; 4(1), 1-40. [2]
    Carnap here loosens the strict principle of verifiability, using the broader notions of "testability" and "confirmability" to demarcate meaningful empirical statements, and handles the connection between theoretical terms and observation through devices such as disposition predicates. It records logical empiricism's key retreat from "verifiable" to "testable," resonating exactly with this chapter's main line of "verification is out of reach, so use the reachable instead." The text was published in two parts, volume 3 issue 4 (1936) and volume 4 issue 1 (1937).

23. W. C. Salmon (1984). *Scientific Explanation and the Causal Structure of the World*. Princeton University Press. [2]
    Salmon argues that the heart of scientific explanation is not logical derivation but the disclosure of causal mechanisms: to explain a phenomenon is to embed it in the world's web of causal processes and causal interactions. It is an important correction to the covering-law model, shifting the standard of "being explicable" from derivability to traceable causal structure, supplying this chapter's understanding of how science characterizes the world with the dimension of causation.

24. C. Howson and P. Urbach (1989). *Scientific Reasoning: The Bayesian Approach*. Open Court. [2][3]
    Howson and Urbach systematically advocate a Bayesian view of scientific reasoning: rather than a true-or-false two-valued verdict, they treat evidence as a continuous adjustment, by Bayes's theorem, to the probability of a belief, and on this basis respond to many difficulties of induction and confirmation. It is the representative work on the Bayesian confirmation theory mentioned in this chapter's text, forming a contrast with falsification and severe testing, and foreshadowing the book's move of calibration.

25. E. Sober (2008). *Evidence and Evolution: The Logic Behind the Science*. Cambridge University Press. [2]
    Sober uses the tools of likelihood theory and statistical inference to analyze in detail "what evidence supports," and discusses which hypotheses are genuinely testable, including an anatomy of why intelligent design is untestable. It brings the abstract question of testability down to concrete scientific inferential practice (especially with evolution as the example), demonstrating how to judge rigorously whether a claim can withstand the test of evidence.

26. P. Godfrey-Smith (2003). *Theory and Reality: An Introduction to the Philosophy of Science*. University of Chicago Press. [2][3]
    Godfrey-Smith's widely praised introduction to the philosophy of science lays out clearly the whole thread from logical empiricism, falsificationism, and Kuhn's paradigm to Bayesianism and the dispute over scientific realism. It serves well as an introductory anchor for the many topics of this chapter, and the reader who wants to build a global map before reading the monographs can begin here.

27. N. Cartwright (1983). *How the Laws of Physics Lie*. Clarendon Press. [2][3]
    Cartwright argues that the fundamental laws of physics are universal and elegant precisely because they do not faithfully describe the real world but rather describe highly idealized models; the more fundamental a law, the greater its explanatory power, yet the more it "lies" in description. She turns instead to value the concrete laws and causal capacities closer to the phenomena, reminding the reader that the "truth" of scientific laws is far more complex than usually supposed, deepening this chapter's reflection on the relation between theory and world.

28. J. P. A. Ioannidis (2005). "Why Most Published Research Findings Are False." *PLoS Medicine*, 2(8), e124. [3][4]
    Ioannidis argues, through concise statistical modeling, that in fields with small effect sizes, flexible study designs, and rampant publication bias, the probability that a published "positive" finding is false is often higher than the probability that it is true, and false positives can systematically outnumber true ones. It is a founding document of the replication crisis, and the core evidence for this chapter's section "When the Machine Fails," showing how science's self-correction spins in neutral once it is weakened.

29. Open Science Collaboration (2015). "Estimating the Reproducibility of Psychological Science." *Science*, 349(6251), aac4716. [3][4]
    The Open Science Collaboration, coordinating over a hundred researchers, conducted systematic direct replications of a hundred published psychology studies, with the result that fewer than half successfully reproduced the original effect, and the reproduced effects were generally weaker than originally reported. It turns the replication crisis from argument into large-scale evidence, the empirical core of this chapter's "replication crisis" section, and underscores why moves such as replication and preregistration are indispensable.
