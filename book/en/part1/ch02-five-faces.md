# Chapter 2: The Five Faces of Unverifiability

> **Thesis:** "I cannot check it" conceals five structurally different situations, and to run them together is the central error of this field.

A single "I cannot check it" sounds like one situation, but it hides five. They are structurally different, and the remedies available to each are different too; running them together is the most central error in this field.

What this chapter sets out to do is to pry the five apart and pin each one down precisely. This may look like nothing more than a taxonomist's fastidiousness, but it is in fact the line of credit the whole second half of the book draws on. The book ultimately wants to argue that, however wildly the sources of unverifiability differ, the responses converge on the same small set. For that claim not to look cheap, the precondition is to make "wildly different" stick first. The more thoroughly the differences are drawn, the more the later convergence becomes something worth marveling at, worth explaining. Hold these five faces firmly in mind; they will be named again and again across the book.

![The five faces of unverifiability: their criteria and their remedies differ](../figures/f02-five-faces.svg)

## The First Face: Undecidable

The criterion: in principle there exists no algorithm to decide it. Not hard, but absent.

This is verification's hardest failure. Hilbert and Ackermann in 1928<sup class="cite"><a href="#ref-4">4</a></sup> stated the decision problem (Entscheidungsproblem) explicitly, asking whether there could be a mechanical procedure to decide the truth or falsity of any mathematical proposition. Eight years later, Church<sup class="cite"><a href="#ref-2">2</a></sup> with the lambda calculus and Turing<sup class="cite"><a href="#ref-1">1</a></sup> with that abstract machine of his each proved that there could not. Turing's halting problem is especially clean: no algorithm can decide, for an arbitrary "program plus input," whether it will halt. Gödel's incompleteness of 1931<sup class="cite"><a href="#ref-3">3</a></sup>, Rice's theorem<sup class="cite"><a href="#ref-6">6</a></sup> (no nontrivial semantic property of a program is decidable), and Matiyasevich's 1970 refutation<sup class="cite"><a href="#ref-7">7</a></sup> of Hilbert's tenth problem all belong to this family. This is no idle talk on paper: precisely because "will this stretch of program do something harmful" reduces to the halting problem, there can in theory be no antivirus software that perfectly and infallibly detects every malicious program. This is the ceiling logic has drawn for the antivirus industry.

The remedy for this face has a property unlike any other: there will never be a complete solution. No amount of time, no faster machine will do, because the obstacle is logical, not one of resources. All you can do is settle for less, verifying a finite slice, or confining yourself to those fragments that genuinely are decidable (arithmetic with addition only, say). This point will go on echoing all the way to Chapter 7.

## The Second Face: Intractable

The criterion: an algorithm exists, but its cost explodes with scale, too large to finish in practice.

This face and the last are a hair apart and worlds apart: decidable, yet infeasible. The NP-completeness established independently by Cook in 1971<sup class="cite"><a href="#ref-8">8</a></sup> and Levin in 1973<sup class="cite"><a href="#ref-9">9</a></sup>, and Karp's famous twenty-one NP-complete problems of 1972<sup class="cite"><a href="#ref-10">10</a></sup>, give it a precise characterization. The satisfiability problem in the worst case, and countless combinatorial optimization problems, all have solution methods in principle, but in the worst case the time those methods take grows exponentially with the size of the input,

$$T(n)\sim 2^{n},$$

and a few dozen variables are enough to leave the fastest supercomputer sighing at an ocean it cannot cross. An intuition for the order of magnitude: the game tree of chess has about $10^{120}$ branches (the Shannon number), the legal positions of Go number about $2\times10^{170}$, while the atoms in the entire observable universe come to only about $10^{80}$. These board games have simple rules and are exhaustible in principle, but that "in principle" lies far beyond physical possibility. Whether $\mathsf{P}$ equals $\mathsf{NP}$ is precisely the question of whether this wall is destined to stand.

Its remedy is wholly unlike that for the undecidable. Here, putting in more resources is meaningful, and, more to the point, you can trade "accepting a little less" for "a cost you can afford": approximate solutions in place of exact ones, the average case in place of the worst case, heuristic search, randomization. Intractability forces out a whole repertoire of "discounting" wisdom, which the undecidable case has none of.

## The Third Face: Partially Observable

The criterion: the very state you would verify against is hidden from you.

It is not that there is no decision procedure, nor that the cost is too great, but that you simply cannot see the thing you ought to see. The user's true preferences, what is happening inside the patient's body, the cards in the opponent's hand, these are the states that drive the outcome, yet they do not reveal themselves to you. Control theory formalized this early: Åström in 1965<sup class="cite"><a href="#ref-15">15</a></sup> studied optimal control under incomplete state information, and Smallwood and Sondik in 1973<sup class="cite"><a href="#ref-16">16</a></sup>, along with Kaelbling and colleagues in 1998<sup class="cite"><a href="#ref-18">18</a></sup>, developed it into the standard framework of the partially observable Markov decision process (POMDP). Papadimitriou and Tsitsiklis in 1987<sup class="cite"><a href="#ref-17">17</a></sup> further proved that solving this class of problems is itself intractable, so the third face often stacks atop the second.

Its remedy is a class of its own: you no longer pursue a definite verdict, but maintain a belief distribution over the hidden state (a belief state), and use each observation to update it,

$$b'(s')\ \propto\ \Pr(o\mid s')\sum_{s}\Pr(s'\mid s,a)\,b(s).$$

Inference and probing, rather than "computing harder," are the cure for this face. The whole of Chapter 5 lives inside it.

## The Fourth Face: Budget-Constrained

The criterion: in principle it can be verified and solved, but you, this actor, here and now, do not have the time, the computation, or the samples.

This face is the plainest and also the most common. A reviewer has only twenty minutes to read a paper; a doctor only a few minutes to make a diagnosis; a trader must place the order before the quote disappears. Verification is wholly feasible in theory, yet infeasible once it lands on a bounded actor. The risk-uncertainty distinction of Knight in 1921<sup class="cite"><a href="#ref-19">19</a></sup> and the bounded rationality of Simon in 1955<sup class="cite"><a href="#ref-20">20</a></sup> are its intellectual source; the anytime algorithm of Dean and Boddy in 1988<sup class="cite"><a href="#ref-22">22</a></sup> (interruptible at any moment, yielding the current best solution) and the "bounded optimality" of Russell and Subramanian in 1995<sup class="cite"><a href="#ref-23">23</a></sup> are its formalization.

Its remedy has a feature no other face shares: this face recedes as resources grow. Give it enough time and computation and it disappears. Just for that reason, the heart of dealing with it lies in allocation, spending the scarce budget where the marginal return is highest. This line of thought is exactly where the later move of "optimal screening" comes from.

## The Fifth Face: Adversarial

The criterion: the system you face is actively working to defeat your verification.

In the first four faces, the difficulty comes from a neutral property of the world: logical, of scale, of visibility, of resources. The fifth is different: across from you sits an intelligence optimizing against your check. The opponent who lies, the malicious code that disguises itself, the examinee who manipulates the metric. The game theory of von Neumann and Morgenstern in 1944<sup class="cite"><a href="#ref-24">24</a></sup>, the equilibrium of Nash in 1950 (the Nash equilibrium)<sup class="cite"><a href="#ref-25">25</a></sup>, and the minimax criterion of Wald in 1945<sup class="cite"><a href="#ref-26">26</a></sup> are its classical theory; the adversarial examples discovered by Szegedy and colleagues in 2014<sup class="cite"><a href="#ref-29">29</a></sup>, and the robust optimization with which Madry and colleagues in 2018<sup class="cite"><a href="#ref-31">31</a></sup> unified attack and defense, are its contemporary incarnation in machine learning. A model with an extremely high recognition rate can be fooled disastrously by a perturbation imperceptible to the human eye, because someone has gone looking specifically for that perturbation. Researchers have produced a demonstration reproduced again and again: stick a few carefully designed stickers, looking like idle graffiti, onto a stop sign, and a top-tier image-recognition system can be made to read it steadily as a speed-limit sign. The same sign: a human sees stop, the machine sees go, and the difference lies only in where the adversary places the stickers.

Its remedy is strategy, not computation. What you must do is not to compute some quantity more accurately, but to

$$\min_{x}\ \max_{y}\ L(x,y),$$

defend against the worst case, use randomization to deprive the adversary of any prediction about you, and seek to stand firm in the game rather than be optimal on some fixed input. To treat the adversarial as a mere observability gap ("I just have not seen it clearly yet") is a misjudgment that can cost lives, because it will adjust itself to track your judgment.

## Five Faces, Five Cures

Set them side by side, and what matters is not the names but that their remedies are mutually incommensurable:

- The undecidable: never a complete solution, only a retreat to slices.
- The intractable: cost can be traded for precision, and more resources are meaningful.
- The partially observable: rely on inferring beliefs and active probing.
- The budget-constrained: recedes as resources grow, the heart of it lies in allocation.
- The adversarial: it is a game of chess, won by strategy and randomization.

Whoever tells you "this thing is solved by piling on more computation" has most likely mistaken one face for another. To treat the undecidable as a budget problem, or the adversarial as an observability problem, is this kind of misidentification, and a costly one.

These faces also stack and compound. The agent let loose in Chapter 6 runs into both the unpredictability of an open world (behavior that is nearly undecidable) and the strategic cunning of an opponent (adversarial); the organization in Chapter 8 bears the partially observable and the adversarial together. Real situations are often a blend of several faces.

Precisely because the sources are so uneven and the remedies so various, the next question to ask grows sharp: do humans have a mature method for coexisting with the unverifiable over the long run, with discipline? They do. That method is called science, and its very first house rule is to admit openly that it can never verify itself.

---

## References

> Waypoints: 1. historical scientific judgment; 2. theoretically studied material; 3. how science progresses; 4. how to live in an unverifiable world. This section was checked source by source.

### Undecidable [2][3]

1. A. M. Turing (1936). "On Computable Numbers, with an Application to the Entscheidungsproblem." *Proceedings of the London Mathematical Society*, s2-42(1), 230-265. [2][3]
   Turing here introduces the notions of "computable numbers" and the abstract computing machine, and from the unsolvability of the halting problem derives that the decision problem has no mechanical solution. This paper is the cleanest exemplar of the "undecidable" face: the obstacle is logical, not one of resources, and this chapter takes Turing's machine and the halting problem as the standard illustration of the face.
2. A. Church (1936). "An Unsolvable Problem of Elementary Number Theory." *American Journal of Mathematics*, 58(2), 345-363. [2][3]
   Church, using the lambda calculus he developed, proved that elementary number theory contains an unsolvable problem and thereby independently refuted the decision problem, publishing about seven months ahead of Turing. His result and Turing's confirm each other, jointly making it stick that "in principle there exists no decision algorithm" is no isolated phenomenon; this chapter places the two side by side as the opening of the undecidable family.
3. K. Gödel (1931). "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I." *Monatshefte für Mathematik und Physik*, 38, 173-198. [2][3]
   Gödel here proves the incompleteness theorem: any sufficiently strong consistent formal system contains propositions that can be neither proved nor refuted. It is the headwater of the undecidable lineage, showing that formal methods themselves have an in-principle limit, and this chapter lists it as the earliest warning bell of this face.
4. D. Hilbert & W. Ackermann (1928). *Grundzüge der theoretischen Logik*. Springer. [2][3]
   This textbook of mathematical logic states the decision problem explicitly for the first time, that is, it asks whether there exists a mechanical procedure that can decide the truth or falsity of any mathematical proposition. It was precisely this question that gave rise to the negative proofs of Church and Turing, and this chapter takes it as the point of departure for the undecidable face, by which the reader can see clearly the optimistic expectation of that era and the logical wall it then ran into.
5. E. L. Post (1944). "Recursively Enumerable Sets of Positive Integers and Their Decision Problems." *Bulletin of the American Mathematical Society*, 50(5), 284-316. [2][3]
   Post here systematically studies recursively enumerable sets and their decision problems, and proposes the line of thought that would later give rise to the theory of degrees of unsolvability. It advances the "undecidable" from a single problem to a graded study of the structure of unsolvability, and this chapter cites it to show that this face has its own levels and lineage, rather than being a monolithic block.
6. H. G. Rice (1953). "Classes of Recursively Enumerable Sets and Their Decision Problems." *Transactions of the American Mathematical Society*, 74(2), 358-366. [2]
   Rice's theorem establishes here that any nontrivial semantic property of what a program computes is undecidable. It generalizes Turing-style undecidability from a particular problem into a universal iron law, and this chapter cites it to show that the wish to verify mechanically whether a program "does the right thing" is, in principle, blocked off.
7. Y. V. Matiyasevich (1970). "Enumerable Sets Are Diophantine." *Soviet Mathematics. Doklady*, 11(2), 354-357. [2][3]
   Matiyasevich here supplies the last link, proving that every recursively enumerable set is Diophantine and thereby completing the proof of the unsolvability of Hilbert's tenth problem, that is, the MRDP theorem. It shows that even a concrete mathematical question like "whether a Diophantine equation has integer solutions" has no decision algorithm, and this chapter cites it to corroborate that the undecidable is not confined to self-reference or metamathematics but has seeped into ordinary mathematics.

### Intractable [2][3]

8. S. A. Cook (1971). "The Complexity of Theorem-Proving Procedures." *Proceedings of the 3rd Annual ACM Symposium on Theory of Computing (STOC)*, 151-158. [2][3]
   Cook here founds the concept of NP-completeness, proving that the satisfiability problem is the hardest class within NP. It gives a precise definition to the "intractable" face: the problem has a solution method, but the cost explodes with scale. This chapter uses it to draw the line between the second face and the first, that is, "decidable yet infeasible" differs from "no algorithm at all."
9. L. A. Levin (1973). "Universal Sequential Search Problems." *Problems of Information Transmission*, 9(3), 265-266. [2][3]
   Levin, on the other side of the Iron Curtain, independently obtained the same result as Cook, giving a completeness characterization of universal search problems; together the two are called the Cook-Levin theorem. It shows that the discovery of NP-completeness was a convergence rather than an accident, and this chapter cites it to reinforce the objectivity of the "intractable" face: this is a property of the structure of the problem itself, not something that varies with the path of research.
10. R. M. Karp (1972). "Reducibility Among Combinatorial Problems." In R. E. Miller & J. W. Thatcher (Eds.), *Complexity of Computer Computations* (pp. 85-103). Plenum Press. [2][3]
    Karp used polynomial reduction to prove that twenty-one common combinatorial problems are all NP-complete, extending Cook's single result into a web of mutual reductions. It shows that intractability is not the quirk of a few individual hard problems but a universal phenomenon spanning a great many practical problems of scheduling, partition, covering, and the like, and this chapter cites it to show that this face is everywhere in engineering.
11. J. Hartmanis & R. E. Stearns (1965). "On the Computational Complexity of Algorithms." *Transactions of the American Mathematical Society*, 117, 285-306. [2]
    This paper grades algorithms by the running time of a Turing machine, laying the framework for dividing complexity classes according to resource consumption; the very term "computational complexity" was established by it. It provides the measuring stick necessary to gauge the "intractable," and this chapter cites it to show that the second face can be spoken of precisely only because there is first a language for characterizing how cost grows with scale.
12. M. R. Garey & D. S. Johnson (1979). *Computers and Intractability: A Guide to the Theory of NP-Completeness*. W. H. Freeman. [2]
    This book systematically organizes the theory of NP-completeness and its proof techniques, and appends a widely cited list of intractable problems; it has long served as the standard reference for the field. For the reader who wishes to understand the "intractable" face from the ground up, it is both an introductory guide and a working handbook, and this chapter lists it as the most reliable foothold on the subject.
13. M. Sipser (2012). *Introduction to the Theory of Computation* (3rd ed.). Cengage Learning. [2]
    This widely adopted undergraduate textbook clearly explains automata, computability, and complexity, threading the Turing machine, the halting problem, P and NP, and other concepts into one coherent line. It covers exactly the theoretical groundwork of this chapter's first two faces, and is the surest starting point for the reader who wishes to build a foundation from scratch; the first edition can be traced back to 1997.
14. S. Arora & B. Barak (2009). *Computational Complexity: A Modern Approach*. Cambridge University Press. [2]
    This graduate textbook covers everything from the classical complexity classes to modern topics such as randomization, interactive proofs, approximation, and derandomization, with a scope far beyond an introductory text. For the reader who wishes to go deep into the "intractable" face, and especially to understand how people use approximation and randomness to skirt the worst case, it is the more advanced authoritative reading.

### Partially Observable [2][4]

15. K. J. Åström (1965). "Optimal Control of Markov Processes with Incomplete State Information." *Journal of Mathematical Analysis and Applications*, 10, 174-205. [2]
    Åström here studies optimal control under incomplete state information, proposing that all available information be summarized by a probability distribution over the hidden state, that is, a "belief state." This is one of the headwaters of POMDP theory, and exactly the cure this chapter prescribes for "partially observable": not to pursue a definite verdict, but to maintain and update a belief.
16. R. D. Smallwood & E. J. Sondik (1973). "The Optimal Control of Partially Observable Markov Processes over a Finite Horizon." *Operations Research*, 21(5), 1071-1088. [2]
    This paper gives the classic structural results for the finite-horizon POMDP, and on that basis designs a method for computing the optimal policy. It advances Åström's belief-state idea into an operable algorithm, and this chapter cites it to show that "relying on inferring beliefs" is no empty phrase but is backed by established solution techniques.
17. C. H. Papadimitriou & J. N. Tsitsiklis (1987). "The Complexity of Markov Decision Processes." *Mathematics of Operations Research*, 12(3), 441-450. [2]
    This paper systematically characterizes the computational complexity of the variants of the Markov decision process, proving that introducing partial observability makes solving them markedly harder. It clasps the third face together with the second: the situation of not being able to see the correct state is itself often intractable to solve, and this chapter uses it precisely to show that the faces stack atop one another.
18. L. P. Kaelbling, M. L. Littman & A. R. Cassandra (1998). "Planning and Acting in Partially Observable Stochastic Domains." *Artificial Intelligence*, 101(1), 99-134. [2][4]
    This paper organizes the POMDP into a standard framework within artificial intelligence, unifying belief updating, planning, and acting, and gives practicable algorithms. It is the most frequently cited representative work for the "partially observable" face, and Chapter 5's development of this face takes it as its base text; from it the reader can come to a systematic grasp of the whole practice of inference plus probing.

### Budget-Constrained [1][4], including bounded rationality and the anytime algorithm

19. F. H. Knight (1921). *Risk, Uncertainty and Profit*. Houghton Mifflin. [1][4]
    Knight here distinguishes "risk," which can be characterized by probability, from "uncertainty," which cannot be quantified at all, the latter being a situation with no reliable probability to rely on. This distinction is one of the intellectual starting points for the book's discussion of the unverifiable, and it reminds the reader that the difficulty of some situations lies not in computing too imprecisely but in the absence of even the probability needed to place a bet.
20. H. A. Simon (1955). "A Behavioral Model of Rational Choice." *The Quarterly Journal of Economics*, 69(1), 99-118. [1][4]
    Simon here proposes bounded rationality: a real actor is limited in computation, time, and information, and so, rather than seeking the global optimum, "stops when satisfied." This is the conceptual source of the "budget-constrained" face, and this chapter borrows it to make the point that many verifications are feasible in theory but must be discounted once they land on a bounded actor, thereby leading into the later line of thought about budget allocation.
21. M. Boddy & T. Dean (1989). "Solving Time-Dependent Planning Problems." *Proceedings of the 11th International Joint Conference on Artificial Intelligence (IJCAI)*. [2][4]
    This paper continues the authors' work on anytime algorithms, studying how to arrange planning when computation time itself is limited, so that the system can be interrupted at any moment and hand over the current best solution. It shares a source with the next entry, and this chapter cites this body of work to show that the core of responding to the "budget-constrained" face is to spend the limited time where the marginal return is highest.
22. T. Dean & M. Boddy (1988). "An Analysis of Time-Dependent Planning." *Proceedings of the 7th National Conference on Artificial Intelligence (AAAI)*, 49-54. [2][4]
    This paper formally proposes the concept of the anytime algorithm: the algorithm can be interrupted at any moment and yield the current best solution, with quality improving steadily as computation time increases. It is the representative formalization of the "budget-constrained" face, and this chapter cites it to show that the distinctive feature of this face is that it recedes as resources grow, so that the key to responding lies in allocation rather than in raw computation.
23. S. J. Russell & D. Subramanian (1995). "Provably Bounded-Optimal Agents." *Journal of Artificial Intelligence Research*, 2, 575-609. [2][4]
    This paper formalizes bounded rationality as "bounded optimality": rather than requiring the agent to output the optimal decision, it requires the agent to do the best it can under a given constraint on computational resources. It gives Simon's intuition a precise definition, and this chapter cites it to show that the "budget-constrained" face too can be theorized seriously, rather than being merely a helpless compromise.

### Adversarial [2][1][4], including decision theory and adversarial machine learning

24. J. von Neumann & O. Morgenstern (1944). *Theory of Games and Economic Behavior*. Princeton University Press. [2][1]
    This book founds game theory, treating the interaction of many parties under conflicting interests as an object of rigorous analysis, and systematizes the minimax theorem for zero-sum games. It is the theoretical source of the "adversarial" face, and this chapter uses it to support the core claim of the face: in facing an opponent who optimizes against you, defend against the worst case rather than seek the optimum on some fixed input.
25. J. F. Nash (1950). "Equilibrium Points in N-Person Games." *Proceedings of the National Academy of Sciences*, 36(1), 48-49. [2]
    Nash proves in this short paper that any finite many-person game has an equilibrium point, that is, a stable configuration in which no party can profit by unilaterally changing its strategy. The Nash equilibrium extends game analysis from the zero-sum to the general case, and this chapter cites it as a core concept of the "adversarial" face, helping the reader understand how strategic interaction converges to a predictable, stable structure.
26. A. Wald (1945). "Statistical Decision Functions Which Minimize the Maximum Risk." *Annals of Mathematics*, 46(2), 265-280. [2]
    Wald here founds statistical decision theory, proposing that decisions be chosen by the minimax criterion, that is, so as to minimize risk in the worst case. It carries "defend against the worst case" from games into statistical inference, and this chapter cites it to show that the cure for the adversarial face is a strategic posture: when the opponent will adjust to track your judgment, seeking robustness matters more than seeking the optimum at some single point.
27. L. J. Savage (1954). *The Foundations of Statistics*. Wiley. [2][1]
    Savage here builds the axiomatic foundations of subjective expected utility theory, arguing that a rational actor's preferences can be represented as the expected utility taken against a subjective probability. It is the standard framework for decision under uncertainty, and this chapter cites it to represent the orthodox stance of "keeping accounts of uncertainty with probability and utility," while also paving the way for the next entry to reveal the boundary of that stance.
28. D. Ellsberg (1961). "Risk, Ambiguity, and the Savage Axioms." *The Quarterly Journal of Economics*, 75(4), 643-669. [1][4]
    Ellsberg, with a simple betting experiment, reveals that people generally avoid the "ambiguous" option whose probability is itself unclear, a behavior that violates Savage's axioms. It corroborates Knight's distinction between risk and uncertainty at the empirical level, and this chapter cites it to show that the probability framework is not omnipotent: some unverifiable situations cannot even yield a probability.
29. C. Szegedy, W. Zaremba, I. Sutskever, J. Bruna, D. Erhan, I. Goodfellow & R. Fergus (2014). "Intriguing Properties of Neural Networks." *International Conference on Learning Representations (ICLR)*. arXiv:1312.6199. [2]
    This paper is the first to reveal adversarial examples systematically: applying a perturbation almost imperceptible to the human eye to an image can make a neural network of extremely high recognition rate err. It brings the "adversarial" face into modern machine learning, and this chapter cites it to show that, so long as someone goes looking specifically for that perturbation, even the most accurate model can be fooled, which is exactly where the adversarial differs from a mere observability gap.
30. I. J. Goodfellow, J. Shlens & C. Szegedy (2015). "Explaining and Harnessing Adversarial Examples." *International Conference on Learning Representations (ICLR)*. arXiv:1412.6572. [2]
    This paper attributes adversarial examples to the model's linearity in high-dimensional space, proposes the FGSM method for rapidly generating perturbations, and defends against them with adversarial training. It both explains why adversarial examples are pervasive and gives the earliest means of response, and this chapter cites it to show that the attack and defense of the adversarial face are a pair locked in mutual rise and fall, demanding a continual game.
31. A. Madry, A. Makelov, L. Schmidt, D. Tsipras & A. Vladu (2018). "Towards Deep Learning Models Resistant to Adversarial Attacks." *International Conference on Learning Representations (ICLR)*. arXiv:1706.06083. [2][4]
    Madry and colleagues write adversarial robustness as a minimax optimization problem: the inner layer finds the worst perturbation, the outer layer trains to resist it, with projected gradient descent as the standard attack. It unifies attack and defense in the language of robust optimization, landing this chapter's claims about the adversarial face and worst-case decision squarely within machine learning, and is a deeply influential paper in this direction.
32. B. Biggio & F. Roli (2018). "Wild Patterns: Ten Years after the Rise of Adversarial Machine Learning." *Pattern Recognition*, 84, 317-331. [2]
    This survey reviews a decade of adversarial machine learning, noting that the field got under way before deep learning became fashionable, and lays out the overall thread of attack models, threat modeling, and defense. For the reader who wishes to grasp the "adversarial" face in full, it is an authoritative overview, and this chapter cites it as the best foothold for reading the face through.
