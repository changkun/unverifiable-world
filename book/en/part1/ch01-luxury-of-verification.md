# Chapter 1: The Luxury of Verification

> **Thesis:** The complete verification that can confirm in advance that something is true, correct, or safe is the exception in the lives of humans and machines, not the norm.

## Seven Times Eight, and Everything Else

You can verify that seven times eight is fifty-six. You can recount it, compute it a second way, or simply recite the multiplication table; within seconds, right and wrong are nailed down.

Now switch to a few other things. Before you say "I do," verify that the marriage will last; before you hit deploy, verify that the codebase has not a single bug; before you give half your life to it, verify that the theory you believe is true; before you take the job, verify that the company is healthy. None of these can you do. Not because you have not tried hard enough, but because things of this kind simply do not offer the option of verifying in advance.

The first cornerstone of this book is that contrast: the complete verification that can confirm in advance that something is true, right, or safe is the exception in the lives of humans and machines, not the norm. We feel it ought to be the norm only because our intuition was shaped inside a very narrow door.

## The Narrow Door Where Verification Is Cheap

Which things can we actually verify? Working an arithmetic problem, sorting a string of numbers, checking the total on a receipt, judging whether a move on the board is legal. Set these side by side and they share a few hidden features: the object is closed (everything relevant is laid out in front of you), it is finite (the cases can be counted), the answer is local and immediate (it does not depend on the distant or the future), and there exists a mechanical decision procedure (follow it and you get a yes or a no).

It is precisely this narrow door that feeds our intuition that "everything can be checked." What school rewards over and over is exactly this kind of problem: one with a standard answer, gradable on the spot. So we quietly extrapolate an experience, "in the things I have practiced, right and wrong can always be sorted out," into a worldview, "the rightness or wrongness of things can always be sorted out." That extrapolation is wrong, and wrong in a systematic way. Outside the narrow door, those four features fail almost one by one.

## The Illusion Breaks in Four Places

![Verification: the cheap narrow door, and the four breaches outside it](../figures/f01-narrow-door.svg)

**Scale.** Inside the door the cases can be counted; outside, they cannot. A program with $n$ branches may have as many as $2^n$ possible execution paths, and a few dozen branches are enough to make exhaustive testing impossible to finish within the lifetime of the universe. This path explosion rules "test it all" out from the start. You can verify that it is correct on the handful of inputs you thought of; you cannot verify that it is correct on all inputs. On August 1, 2012, when Knight Capital deployed a new trading program, one of its eight servers had not been updated, and a stretch of long-dormant, long-since-deprecated old code was accidentally woken by a reused flag; over roughly forty-five minutes after the opening bell it spewed out millions of orders, costing the firm about 440 million dollars and nearly bankrupting it overnight. No one had verified that dead path, because no one imagined it would still run. Checking a single case is easy; checking every case, the moment the quantifier "all" appears, you have crossed into another world.

**Open world.** Inside the door the object is closed; outside, the world keeps sending new things. What you tested was a finite handful of scenarios; what the system actually meets is an open, to-be-continued environment. On June 4, 1996, the Ariane 5 rocket made its maiden flight and destroyed itself in the air about thirty-seven seconds after launch. The cause was a piece of inertial navigation code carried over directly from the Ariane 4, never re-verified for the new trajectory, which forced a 64-bit floating-point number into a 16-bit integer; the new rocket's higher horizontal velocity made that number overflow, and along with the four scientific satellites aboard, the loss exceeded 370 million dollars. The code had run correctly for years in the old world; in a new world it turned lethal. The MCAS system on the Boeing 737 MAX is a more harrowing version of the same breach: it behaved normally across test flight after test flight, yet on real routes it read a single faulty angle-of-attack sensor and pushed the nose down again and again; two crashes (Lion Air 610 in 2018, Ethiopian 302 in 2019) took 346 lives between them. What you verify is always the slice you have seen before; what you must wager on is the future you have not.

**Other minds.** Inside the door the state is observable; outside, the goal you must satisfy is often locked inside another person's head. The scene at the start of this chapter, "built it right, but it was not what I wanted," has its root here: what the user truly wants, whether the boss is satisfied, whether the other person loves you, these are latent variables; you can only infer them obliquely from behavior, you cannot read them directly, and so you cannot directly verify whether you have satisfied them. Even the most solemn of life's commitments cannot escape it: by demographic estimates, roughly forty to fifty percent of American first marriages end in divorce, and no one, in the moment of saying "I do," can verify that it will last.

**The future.** This is the deepest of them, and Hume laid it bare back in 1748<sup class="cite"><a href="#ref-17">17</a></sup>: induction carries no logical guarantee. That the sun has risen every day in the past does not logically prove it will rise tomorrow; finite past experience cannot verify in advance any universal claim about the future. What we rely on is not proof but habit. Every action whose outcome falls in the future, marriage, investment, sowing, entrusting, lies on the far side of this breach.

## Even the Two Hardest Fields Bow

Perhaps you will think that the soft domains, scale and the human heart and the future, may as well concede, but mathematics and software ought to be the fortresses of complete verification. It is precisely these two hardest places that have most soberly admitted the limits of verification.

On the software side, Dijkstra<sup class="cite"><a href="#ref-13">13</a></sup> left a line that has been quoted to death and is still correct: testing can only prove that defects are present, never that they are absent. He held that a program should be correctly constructed, not debugged into correctness. Yet even formal proof, the strictest road, has its limit. DeMillo, Lipton, and Perlis, in their controversial and famous 1979 paper<sup class="cite"><a href="#ref-9">9</a></sup>, argued that program verification cannot play the role mathematical proof plays, that its credibility ultimately comes from a social process rather than mechanical deduction; Fetzer in 1988 put it more harshly<sup class="cite"><a href="#ref-10">10</a></sup>, that a program, as a causal model, is separated by a gulf from the algorithm as a logical structure, and that "a completely reliable program verification" does not hold even in theory. Brooks's "No Silver Bullet"<sup class="cite"><a href="#ref-11">11</a></sup> asserts that the essential complexity of software cannot be eliminated by any single stroke; Parnas resigned as an adviser to the Star Wars program and publicly argued that the software of such systems cannot be verified to the point of being worthy of trust<sup class="cite"><a href="#ref-12">12</a></sup>; and the Therac-25 radiotherapy machine, which between 1985 and 1987 went out of control six times because of a concurrency race condition and delivered radiation hundreds of times above normal into patients' bodies, killing at least three<sup class="cite"><a href="#ref-15">15</a></sup>, is the footnote all these judgments paid in human lives. A 1968 NATO conference simply coined a word for it: the software crisis<sup class="cite"><a href="#ref-16">16</a></sup>.

Mathematics cuts deeper still. Gödel proved in 1931<sup class="cite"><a href="#ref-3">3</a></sup> that any sufficiently rich and consistent formal system contains true propositions it cannot decide internally; Church and Turing each proved in 1936<sup class="cite"><a href="#ref-2">2</a></sup><sup class="cite"><a href="#ref-1">1</a></sup> that no algorithm can decide whether an arbitrary proposition is provable (the Entscheidungsproblem has no solution); Rice's theorem<sup class="cite"><a href="#ref-4">4</a></sup> pushed it to the limit, that any nontrivial semantic property of a program is undecidable. Even where a problem is decidable in principle, the NP-completeness Cook established in 1971<sup class="cite"><a href="#ref-5">5</a></sup> shows that the cost of verification can explode until it simply will not run in practice. These are not temporary engineering shortfalls; they are the hard boundary logic has drawn around verification. The next chapter takes this layer apart on its own.

## Restated, and This Is Not a Counsel of Despair

Put it all together: most consequential actions step onto unverified ground.

This is not a conclusion that paralyzes; it is a starting point. To admit that verification is a luxury is precisely the first step in taking action seriously. Knight, back in 1921, already separated measurable "risk" from immeasurable "uncertainty"<sup class="cite"><a href="#ref-22">22</a></sup> and pointed out that profit comes precisely from the latter; Keynes, speaking of genuine uncertainty, left only the line "we simply do not know"<sup class="cite"><a href="#ref-26">26</a></sup>; Simon, seeing that a bounded actor cannot exhaustively verify every option, proposed "satisficing"<sup class="cite"><a href="#ref-23">23</a></sup>; von Neumann and Morgenstern, and Savage, each built a formal framework for how to bet rationally when outcomes cannot be verified in advance<sup class="cite"><a href="#ref-24">24</a></sup><sup class="cite"><a href="#ref-25">25</a></sup>. An entire discipline of decision is built on the very premise that verification is unavailable. The question was never how to abolish uncertainty, but how to act well within it.

## Where This Chapter Leads

Since verification is usually unavailable, the first thing to ask is: why is it unavailable?

There is more than one answer, and that is exactly what matters. Treating "I cannot check it" as a single situation is the most common and most misleading mistake in this field. It is in fact five structurally different situations sharing one sentence. In the next chapter, we break that sentence into five.

---

## References

> Waypoints: 1. historical scientific judgment; 2. theoretically studied material; 3. how science progresses; 4. how to live in an unverifiable world. This section was checked source by source.

1. A. M. Turing (1936). "On Computable Numbers, with an Application to the Entscheidungsproblem." *Proceedings of the London Mathematical Society*, s2-42, 230-265. [2]
   Turing, modeling computation with an abstract machine, proved that no algorithm can decide whether an arbitrary proposition is provable, and from this derived the undecidability of the halting problem. This is the founding work that raised the limit of verification from engineering experience to a mathematical theorem; the section "Even the Two Hardest Fields Bow" uses it precisely to show that the Entscheidungsproblem has no solution. The series 2, volume 42 in which it appears spans 1936 to 1937, and some bibliographies date it to 1937; the text uses the conventional 1936.

2. A. Church (1936). "An Unsolvable Problem of Elementary Number Theory." *American Journal of Mathematics*, 58(2), 345-363. [2]
   Church, using the lambda calculus he founded, independently proved that elementary number theory contains an unsolvable decision problem, publishing several months before Turing. His work converges with Turing's by a different route, jointly framing the theoretical boundary of "what is computable," and reminds the reader that the unavailability of verification was established along two independent paths in 1936.

3. K. Gödel (1931). "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I." *Monatshefte für Mathematik und Physik*, 38, 173-198. [2]
   Gödel proved that any sufficiently rich and consistent formal system contains true propositions it can neither prove nor refute. This means that "verifying every truth one by one inside the system" is impossible in principle, the deepest cornerstone of this chapter's argument that verification has a hard boundary, and one the next chapter takes apart on its own.

4. H. G. Rice (1953). "Classes of Recursively Enumerable Sets and Their Decision Problems." *Transactions of the American Mathematical Society*, 74, 358-366. [2]
   Rice's theorem pushes the undecidability of the halting problem to its limit: no general decision algorithm exists for any nontrivial semantic property of a program. It tells the reader that questions about "what this program will actually do" are almost uniformly not mechanically verifiable, the key support for this chapter's passage on how even the hardest fields bow.

5. S. A. Cook (1971). "The Complexity of Theorem-Proving Procedures." *Proceedings of the 3rd Annual ACM Symposium on Theory of Computing (STOC)*, 151-158. [2]
   Cook here established the concept of NP-completeness, proving that the satisfiability problem carries a universal computational hardness for a large class of problems. It reveals another limit of verification: even when a problem is decidable in principle, the cost of solving or checking it may explode until it simply cannot run in practice, matching this chapter's account of how "scale" fails.

6. C. A. R. Hoare (1969). "An Axiomatic Basis for Computer Programming." *Communications of the ACM*, 12(10), 576-580. [2][1]
   Hoare proposed an axiomatic system, later called Hoare logic, for rigorously proving program correctness with preconditions, postconditions, and inference rules. It represents the ambition of the strictest line, to carry verification all the way through, and lets the reader see both how far formal verification can go and why, in engineering reality, it has always struggled to cover everything.

7. J. C. King (1976). "Symbolic Execution and Program Testing." *Communications of the ACM*, 19(7), 385-394. [2]
   King proposed symbolic execution: replacing concrete inputs with symbolic variables and systematically deriving, along a program's branches, the conditions each path must satisfy. The technique both widened the coverage of automated testing and laid bare the "path explosion" in which the number of paths grows exponentially with branches, the very difficulty this chapter uses to explain why exhaustive verification is limited.

8. E. M. Clarke and E. A. Emerson (1981). "Design and Synthesis of Synchronization Skeletons Using Branching Time Temporal Logic." *Logics of Programs (Lecture Notes in Computer Science 131)*, Springer, 52-71. [2]
   This workshop paper proposed using branching-time temporal logic to check automatically whether a system satisfies a given property, founding model checking. It represents the branch in which machine verification truly landed, but its power presumes a finite system state, and so it draws exactly the boundary between what automated verification can reach and what it cannot. The paper appears in LNCS volume 131, a conference proceedings rather than a journal.

9. R. A. DeMillo, R. J. Lipton, and A. J. Perlis (1979). "Social Processes and Proofs of Theorems and Programs." *Communications of the ACM*, 22(5), 271-280. [1][2]
   The three authors argue that mathematical proof is credible because of the social process by which the mathematical community repeatedly reads, reuses, and tests it, whereas the long and mechanical verification of programs lacks such a process and therefore cannot play the role of mathematical proof. This is the famous challenge to the idea that formal verification can give software certainty, cited here to show that the credibility of verification ultimately comes from the social rather than from pure mechanical deduction.

10. J. H. Fetzer (1988). "Program Verification: The Very Idea." *Communications of the ACM*, 31(9), 1048-1063. [1][2]
    Fetzer pushed the challenge deeper: an algorithm is a logical structure and can be rigorously proved, whereas a program running on a real machine is a causal model whose behavior is bound by hardware and the world, and between the two lies an unbridgeable gulf. On this basis he argued that "a completely reliable program verification" does not hold even in theory. The paper set off a large-scale debate in the 1989 Technical Correspondence, and is an important part of this chapter's demarcation of the logical boundary of verification.

11. F. P. Brooks (1987). "No Silver Bullet: Essence and Accidents of Software Engineering." *IEEE Computer*, 20(4), 10-19. [1]
    Brooks distinguishes the essential complexity of software from the accidental, asserting that no single technique can yield an order-of-magnitude gain in software productivity within a decade, because essential complexity cannot be eliminated by one stroke. It supports this chapter's judgment that defects cannot be verified away in a single blow by some silver bullet. The piece was originally an invited paper for the 10th IFIP World Computer Congress in 1986, first published in Information Processing 86, 1069-1076.

12. D. L. Parnas (1985). "Software Aspects of Strategic Defense Systems." *Communications of the ACM*, 28(12), 1326-1335. [1]
    Parnas, after resigning as an adviser to the Star Wars program, wrote to argue point by point that the software of such systems cannot be verified, by testing or by proof, to a degree worthy of trust. This is a top engineer's public judgment on the limits of verification, made at the cost of his resignation, cited in this chapter as a real-world footnote to how even the hardest fields bow. That same year he also published a series of short essays in American Scientist.

13. E. W. Dijkstra (1972). "The Humble Programmer" (1972 ACM Turing Award Lecture). *Communications of the ACM*, 15(10), 859-866. [1]
    This is Dijkstra's Turing Award lecture, arguing that the programmer should stay humble, face the limited capacity of the human mind, and treat a program as something that ought to be correctly constructed rather than patched into correctness after the fact. It reflects a founder's sober judgment on the limits of after-the-fact verification, in resonance with this chapter's claim.

14. E. W. Dijkstra (1972). *Notes on Structured Programming* (in O.-J. Dahl, E. W. Dijkstra, C. A. R. Hoare, eds., *Structured Programming*). Academic Press. [1]
    This chapter's much-quoted yet still-correct line, "testing can only prove the presence of defects, never their absence," comes from here. Dijkstra sets out structured programming systematically, arguing that correctness is gained through disciplined construction rather than exhaustive testing. The claim first appeared in manuscript EWD249 (1970) and was formally published in *Structured Programming* in 1972.

15. N. G. Leveson and C. S. Turner (1993). "An Investigation of the Therac-25 Accidents." *IEEE Computer*, 26(7), 18-41. [1][4]
    The two authors give an authoritative investigation of the series of accidents in which the Therac-25 radiotherapy machine, through a software defect, overdosed patients with radiation and even killed them, analyzing the chained causes of race conditions, excessive trust in software, and the absence of an independent safety mechanism. At the cost of human lives it shows what follows when a safety-critical system is put into use without adequate verification, a heavy footnote to this chapter on the cost of verification.

16. P. Naur and B. Randell (eds.) (1969). *Software Engineering: Report on a Conference Sponsored by the NATO Science Committee*. Scientific Affairs Division, NATO. [1]
    This conference report records practitioners' collective anxiety that the software of the time was routinely late, over budget, and hard to deliver reliably; the term "software crisis" and the very idea of "software engineering" as a discipline came from it. It is the source of this chapter's phrase "software crisis," concentrating a generation of engineers' judgment that software could not be reliably verified. The conference was held in Garmisch, Germany, in October 1968, and the report was published in 1969.

17. D. Hume (1748). *An Enquiry Concerning Human Understanding*. (London). [4][3]
    Hume here laid bare the problem of induction: to infer from "it has repeatedly been so in the past" that "it will still be so in the future" carries no logical guarantee; whether the sun will rise tomorrow cannot be proved in advance, and people act as usual out of habit, not proof. This is the source of the "future" breach in this chapter, and a starting point the whole book returns to. The 1748 first edition was originally titled *Philosophical Essays Concerning Human Understanding*, changed to the present title in 1758.

18. K. Popper (1959). *The Logic of Scientific Discovery*. Hutchinson. [3]
    Popper set out falsificationism systematically: a scientific theory cannot be empirically verified, only falsified, so falsifiability becomes the line between science and non-science, and science advances precisely by trying again and again to overturn theories. It bears directly on this chapter's waypoint "how science progresses," revealing that even science does not accumulate by positive verification. The English edition was expanded by the author from the German original *Logik der Forschung* (printed 1934, copyright page marked 1935).

19. W. V. O. Quine (1951). "Two Dogmas of Empiricism." *The Philosophical Review*, 60(1), 20-43. [3]
    Quine attacks the two dogmas of empiricism, the sharp analytic-synthetic divide and reductionism, and proposes holism: a theory is a web of belief that meets experience as a whole, and no single statement can be verified or refuted in isolation. It shows that evidence underdetermines theory, deepening this chapter's discussion of how science progresses and why verification cannot be done statement by statement.

20. T. S. Kuhn (1962). *The Structure of Scientific Revolutions*. University of Chicago Press. [3]
    Kuhn introduced the concept of the paradigm, describing how science alternates between the accumulation of normal science and the crisis brought on by accumulated anomalies, finally undergoing revolution through a paradigm shift. His point is that science does not advance by the stepwise verification of truth in linear accumulation, but through incommensurable paradigm leaps. It gives this chapter's "how science progresses" a picture complementary to, and in contrast with, Popper's.

21. I. Lakatos (1976). *Proofs and Refutations: The Logic of Mathematical Discovery* (J. Worrall and E. Zahar, eds.). Cambridge University Press. [3][2]
    Lakatos, through a classroom dialogue tracing the evolution of Euler's formula for polyhedra, shows how mathematical concepts and theorems grow in the back-and-forth of counterexample, re-proof, and revised definition. It overturns the impression that a mathematical proof is a once-and-for-all verification, suggesting that even the most certain field advances through criticism, echoing this chapter's general account of the limits of verification.

22. F. H. Knight (1921). *Risk, Uncertainty and Profit*. Houghton Mifflin. [4]
    Knight separates "risk," measurable by probability, from genuine "uncertainty," which cannot be measured at all, and argues that the entrepreneur's profit comes precisely from bearing the latter. This distinction is the key to this chapter's turn, after admitting that verification is a luxury, toward a theory of action; it explains how decision and reward acquire meaning when outcomes cannot be verified in advance.

23. H. A. Simon (1955). "A Behavioral Model of Rational Choice." *The Quarterly Journal of Economics*, 69(1), 99-118. [4]
    Simon proposed a behavioral model of bounded rationality: an actor limited in both information and computational power cannot exhaustively compare all options, and can only set an adequate level, stopping at the first option that meets it, which is to satisfice. This is one concrete answer to this chapter's question of how to act well within uncertainty, turning the unavailability of verification into an operable decision rule.

24. J. von Neumann and O. Morgenstern (1944). *Theory of Games and Economic Behavior*. Princeton University Press. [4]
    The two authors founded game theory and derived expected utility from a set of axioms, arguing that a rational actor should choose according to expected utility. It built a formal framework for how to bet rationally when the opponent's intent and the outcome cannot be verified in advance, one of the pillars of the discipline of decision, built on the unavailability of verification, that this chapter describes.

25. L. J. Savage (1954). *The Foundations of Statistics*. John Wiley & Sons. [4]
    Savage built axiomatic foundations for subjective probability and personalist decision theory, proving that as long as preferences satisfy certain consistency conditions, an actor behaves as if maximizing expected utility under some subjective probability and utility. It gives a standard of rationality for betting consistently in a world where probabilities cannot be objectively verified, and together with von Neumann's framework it supports this chapter's discussion of decision under uncertainty.

26. J. M. Keynes (1937). "The General Theory of Employment." *The Quarterly Journal of Economics*, 51(2), 209-223. [4]
    Keynes, replying to critics of the *General Theory*, stressed that genuine uncertainty cannot be measured by probability, that of some things "we simply do not know." He pointed out that an investment decision, facing an unverifiable future, can only rely on convention and animal spirits. This chapter's classic statement of genuine uncertainty comes from here, and it corroborates that the discipline of decision takes the unavailability of verification as its premise.

27. A. Tversky and D. Kahneman (1974). "Judgment under Uncertainty: Heuristics and Biases." *Science*, 185(4157), 1124-1131. [4]
    Tversky and Kahneman showed experimentally that in judging probability people often rely on heuristic shortcuts such as representativeness, availability, and anchoring, and so deviate systematically from the norms of probability. It completes this chapter's picture at the descriptive level: in a world where probability cannot be fully verified, how people actually judge, and where they consistently go wrong.

28. N. N. Taleb (2007). *The Black Swan: The Impact of the Highly Improbable*. Random House. [4]
    Taleb calls those rare, extreme-impact events that are explained away only in hindsight "black swans," arguing that they cannot be verified or predicted in advance yet often dominate the course of history. On this basis he proposes that one give up the fantasy of precise prediction and instead build arrangements that are not destroyed by surprise, and may even benefit from it. This echoes the ending of this chapter: the problem is not to abolish uncertainty, but how to live steadily within it.
