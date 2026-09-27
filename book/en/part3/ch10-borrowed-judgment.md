# Chapter 10: Borrowed Judgment

> **Thesis:** When you lack the capacity to verify, bring it in from outside. Either put a trusted judge in the loop (an oracle), or use many unreliable judges who are independent of one another, and trust their agreement (redundancy / consensus).

The previous pair of moves still relied on your own resources to shrink the unknown. Sometimes, though, what you lack is not information but judgment itself. You have no way to reach a reliable verdict on the matter in front of you. This pair of moves responds by looking outside yourself and borrowing judgment from elsewhere. There are two ways to borrow it. You can bring in one judge you trust (an oracle). Or you can assemble many judges who do not trust one another, and trust their agreement (redundancy).

## The Oracle in the Loop: Bring In a Judge

The first move in pure form: at the decision point where you lack the ability to verify, insert an outside judge, and let it deliver the verdict you cannot.

The plainest versions are the human in the loop from Chapter 5, the consultation with an expert, and the hard case passed up the chain. But the deepest form of this move is hidden in two places that seem to have nothing to do with each other.

One is interactive theorem proving. From de Bruijn's AUTOMATH of 1970<sup class="cite"><a href="#ref-1">1</a></sup>, through Edinburgh LCF (Gordon, Milner, and Wadsworth, 1979<sup class="cite"><a href="#ref-2">2</a></sup>), to today's Coq (Bertot and Castéran, 2004<sup class="cite"><a href="#ref-3">3</a></sup>), these systems share one division of labor. The human supplies what the machine cannot, the flash of insight behind a proof (the oracle). The machine checks every step with complete rigor (certificate checking). The oracle does the "finding" and the machine does the "verifying," a neat fit with the asymmetry from Chapter 7: finding is hard, checking is cheap.

The other is more surprising still: the interactive proof in complexity theory. Suppose a verifier with very little computing power faces a prover that is powerful but untrustworthy. How can the verifier get a reliable answer to a question it cannot compute on its own? Goldwasser, Micali, and Rackoff in 1989<sup class="cite"><a href="#ref-6">6</a></sup> and Babai in 1985<sup class="cite"><a href="#ref-7">7</a></sup> gave the answer: repeated questioning plus random challenges. The verifier poses random questions that not even it could have predicted. If the prover is lying, sooner or later it will give itself away on one of them. Shamir's remarkable 1992 result<sup class="cite"><a href="#ref-15">15</a></sup>, $\mathrm{IP}=\mathrm{PSPACE}$, shows that this method alone, "interrogating an untrustworthy oracle," lets a weak verifier reliably settle an enormous class of problems. Blum and Kannan's "programs that check their work" of 1995<sup class="cite"><a href="#ref-17">17</a></sup> and Goldwasser and colleagues' "interactive proofs for muggles" of 2015<sup class="cite"><a href="#ref-19">19</a></sup> belong to the same line. This is the purest mathematical form of "borrowed judgment." Even if the oracle cannot be trusted, you can still extract reliability from it, as long as you question it cleverly.

What unifies these is the idea of bringing in an outside judge to create a reliability you do not have on your own. The standard failure mode is just as plain: the oracle itself is unreliable or biased. The referee you bring in may simply be wrong. And the question "who verifies the oracle?" leads into a regress with nowhere to stop.

## Redundancy: Build Reliability from Many Unreliable Parts

The second move goes the other way. Instead of bringing in one trustworthy judge, it gathers many untrustworthy ones and trusts their agreement.

Its theory rests on two cornerstones. In 1956 von Neumann proved<sup class="cite"><a href="#ref-4">4</a></sup> that you can build computation as reliable as you like out of components that are themselves error-prone, by layering on redundancy. Condorcet's jury theorem of 1785<sup class="cite"><a href="#ref-5">5</a></sup> supplies the arithmetic. If every judge is slightly better than chance (accuracy $p>\tfrac12$) and the judges are independent of one another, then the probability that the majority vote is right approaches certainty as the number of judges grows,

$$P_N\to 1\quad(N\to\infty).$$

This move turns up across a very wide range of fields. In distributed systems it is Byzantine fault tolerance. The Byzantine generals problem of Pease, Shostak, and Lamport (1980)<sup class="cite"><a href="#ref-8">8</a></sup> and Lamport and colleagues (1982)<sup class="cite"><a href="#ref-9">9</a></sup> asks how to reach consensus when some nodes may act maliciously (adversarially). The classic threshold: to tolerate $f$ traitors, the number of nodes must satisfy $n\ge 3f+1$. Castro and Liskov's PBFT of 1999<sup class="cite"><a href="#ref-11">11</a></sup> built this into a practical system, while the impossibility theorem of Fischer, Lynch, and Paterson (1985)<sup class="cite"><a href="#ref-10">10</a></sup> marks out its limits.

In machine learning it is the ensemble. The ensemble methods of Hansen and Salamon (1990)<sup class="cite"><a href="#ref-20">20</a></sup> and Dietterich (2000)<sup class="cite"><a href="#ref-22">22</a></sup>, and Breiman's random forest of 2001<sup class="cite"><a href="#ref-23">23</a></sup>, let a crowd of weak models vote and beat a single strong one. Among people it is the "wisdom of crowds" (Surowiecki, 2004<sup class="cite"><a href="#ref-25">25</a></sup>). In 1906, at a country fair, Galton recorded about eight hundred villagers' independent guesses at the weight of an ox. No one guessed the exact weight. Yet the average of all the guesses was 1197 pounds, and the ox actually weighed 1198 pounds. Taken together, the crowd was off by almost nothing. Hong and Page went further, proving in 2004<sup class="cite"><a href="#ref-24">24</a></sup> that under suitable conditions a diverse group of ordinary problem solvers can outperform a group of experts. In science this move is peer review and replicated experiments (Chapter 3). In engineering it is RAID and quorums. In medicine it is the second opinion.

But this move has one crucial precondition, and it deserves a close look: independence. Redundancy works only when failures are uncorrelated. Average many independent estimates, and the variance falls as the number of judges grows,

$$\mathrm{Var}(\bar X)=\frac{\sigma^2}{N};$$

but once there is a positive correlation $\rho$ among the judgments, the variance no longer goes to zero. It gets stuck at a floor,

$$\mathrm{Var}(\bar X)=\rho\,\sigma^2+\frac{(1-\rho)\,\sigma^2}{N}\ \xrightarrow{N\to\infty}\ \rho\,\sigma^2.$$

![The correlation floor of redundancy: once correlation is present, piling on more judges cannot get past it](../figures/f10-redundancy-floor.svg)

<figure class="uvw-viz" data-static="f10-redundancy-floor" role="group" aria-label="The correlation floor of redundancy, interactive">
<div class="uvw-live" hidden>
  <div class="uvw-plot">
    <svg viewBox="0 0 640 380" preserveAspectRatio="xMidYMid meet" aria-hidden="true">
      <g class="uvw-axes" fill="none" stroke="currentColor" stroke-width="1.2" opacity="0.35">
        <line x1="70" y1="330" x2="610" y2="330"></line>
        <line x1="70" y1="45" x2="70" y2="330"></line>
      </g>
      <line class="uvw-floor" x1="70" x2="610" stroke-width="1.6" stroke-dasharray="6 5"></line>
      <text class="uvw-floorlab" x="600" text-anchor="end">floor ρ</text>
      <path class="uvw-curve" fill="none" stroke-width="2.6"></path>
      <line class="uvw-cursor" y1="45" y2="330" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 4" opacity="0.55"></line>
      <circle class="uvw-dot" r="5"></circle>
      <text class="uvw-ylab-top" x="64" y="49" text-anchor="end">1</text>
      <text class="uvw-ylab-bot" x="64" y="334" text-anchor="end">0</text>
      <text class="uvw-ylab" x="24" y="190" text-anchor="middle" transform="rotate(-90 24 190)">normalized variance V</text>
      <text class="uvw-xlab" x="340" y="366" text-anchor="middle">number of judges N →</text>
    </svg>
  </div>
  <div class="uvw-controls">
    <label>correlation ρ
      <input class="uvw-rho" type="range" min="0" max="1" value="0.1" step="0.01">
      <b class="uvw-v-rho">0.10</b>
    </label>
    <label>number of judges N
      <input class="uvw-n" type="range" min="1" max="200" value="20" step="1">
      <b class="uvw-v-n">20</b>
    </label>
    <div class="uvw-readout">
      <span class="uvw-chip uvw-chip-var">normalized variance V <b class="uvw-v-var">–</b></span>
      <span class="uvw-chip uvw-chip-eff">effective independent judges <b class="uvw-v-eff">–</b></span>
    </div>
    <p class="uvw-note"></p>
  </div>
</div>
</figure>
<style>
.uvw-viz{margin:1.6em 0;padding:0}
.uvw-viz .uvw-live{border:1px solid var(--line,#e5e7eb);border-radius:10px;padding:14px 16px 18px;background:var(--paper,#fff)}
.uvw-viz svg{width:100%;height:auto;color:var(--ink,#1a1a1a);display:block}
.uvw-viz .uvw-curve{stroke:#6366f1}
.uvw-viz .uvw-floor{stroke:#d97706}
.uvw-viz .uvw-floorlab{fill:#d97706;font-size:12px}
.uvw-viz .uvw-dot{fill:#a855f7}
.uvw-viz .uvw-ylab,.uvw-viz .uvw-xlab,.uvw-viz .uvw-ylab-top,.uvw-viz .uvw-ylab-bot{fill:var(--muted,#6b7280);font-size:13px}
.uvw-viz .uvw-ylab-top,.uvw-viz .uvw-ylab-bot{font-size:12px}
.uvw-viz .uvw-controls{margin-top:10px}
.uvw-viz .uvw-controls label{display:flex;align-items:center;gap:10px;font-size:14px;color:var(--muted,#6b7280);margin-top:6px}
.uvw-viz .uvw-controls label b{font-variant-numeric:tabular-nums;color:var(--ink,#1a1a1a);min-width:2.6em;text-align:right}
.uvw-viz .uvw-rho{flex:1;accent-color:#d97706}
.uvw-viz .uvw-n{flex:1;accent-color:#6366f1}
.uvw-viz .uvw-readout{display:flex;flex-wrap:wrap;gap:8px 14px;margin-top:12px;font-size:14px}
.uvw-viz .uvw-chip b{font-variant-numeric:tabular-nums}
.uvw-viz .uvw-chip-var b{color:#6366f1}
.uvw-viz .uvw-chip-eff b{color:#10b981}
.uvw-viz .uvw-note{margin:12px 0 0;font-size:13.5px;color:var(--muted,#6b7280);min-height:2.4em;line-height:1.6}
</style>
<script>
(function(){
  var root=document.currentScript.previousElementSibling;
  while(root&&!(root.classList&&root.classList.contains('uvw-viz')))root=root.previousElementSibling;
  if(!root)return;
  var live=root.querySelector('.uvw-live');if(!live)return;
  var key=root.getAttribute('data-static');
  if(key){var imgs=document.querySelectorAll('img[src*="'+key+'"]');for(var i=0;i<imgs.length;i++){var p=imgs[i].closest('p')||imgs[i];p.style.display='none';}}
  live.hidden=false;
  var rhoS=root.querySelector('.uvw-rho'),nS=root.querySelector('.uvw-n');
  var curve=root.querySelector('.uvw-curve'),floor=root.querySelector('.uvw-floor'),floorLab=root.querySelector('.uvw-floorlab');
  var dot=root.querySelector('.uvw-dot'),cur=root.querySelector('.uvw-cursor');
  var vRho=root.querySelector('.uvw-v-rho'),vN=root.querySelector('.uvw-v-n');
  var vVar=root.querySelector('.uvw-v-var'),vEff=root.querySelector('.uvw-v-eff'),note=root.querySelector('.uvw-note');
  var X0=70,X1=610,Y0=330,Y1=45,Nmin=1,Nmax=200;
  function sx(n){return X0+(X1-X0)*(n-Nmin)/(Nmax-Nmin);}
  function sy(v){return Y0+(Y1-Y0)*v;}
  function V(n,r){return r+(1-r)/n;}
  function build(r){var d='';for(var i=0;i<=400;i++){var n=Nmin+(Nmax-Nmin)*i/400;d+=(i?'L':'M')+sx(n).toFixed(1)+' '+sy(V(n,r)).toFixed(1)+' ';}return d;}
  function upd(){
    var r=+rhoS.value,n=Math.round(+nS.value);
    vRho.textContent=r.toFixed(2);vN.textContent=n;
    curve.setAttribute('d',build(r));
    var fy=sy(r);
    floor.setAttribute('y1',fy);floor.setAttribute('y2',fy);
    floorLab.setAttribute('y',(fy-6).toFixed(1));floorLab.textContent='floor ρ = '+r.toFixed(2);
    var v=V(n,r);
    dot.setAttribute('cx',sx(n));dot.setAttribute('cy',sy(v));
    cur.setAttribute('x1',sx(n));cur.setAttribute('x2',sx(n));
    var eff=n/(1+(n-1)*r);
    vVar.textContent=v.toFixed(3);
    vEff.textContent=eff.toFixed(1);
    if(r<0.02)note.textContent='Correlation is near zero, so adding judges keeps driving the variance down. Redundancy is still doing real work.';
    else note.textContent='A hidden correlation caps reliability at the floor ρ: no matter how many judges you add, the effective independent judges approach 1/ρ ≈ '+(1/r).toFixed(1)+', and cannot get past it.';
  }
  rhoS.addEventListener('input',upd);nS.addEventListener('input',upd);upd();
})();
</script>

Correlation wipes out the central promise of redundancy. Add as many judges as you like, and you still cannot get below the floor that correlation sets. This is not an abstraction. In a famous 1986 experiment, Knight and Leveson<sup class="cite"><a href="#ref-13">13</a></sup> had many programmers write programs independently to the same specification. The expectation was that their errors would be uncorrelated. Instead, the programmers stumbled in the same places, because people facing the same hard spot make the same mistakes. (Eckhardt and Lee had predicted this in theory as early as 1985<sup class="cite"><a href="#ref-12">12</a></sup>.) Groupthink, flawed training data drawn from a common source, common-mode failure: each of these is the floor showing itself. This is the standard failure mode of redundancy: believing in independence where there is actually correlation.

## How These Two Moves Meet

Put the two moves side by side. One brings in a single, expensive oracle. The other combines many cheap, independent judgments. Both borrow a power of judgment you do not have on your own. What they share is filling the gap in your own ability to verify. Their failure modes mirror each other, too. The single oracle may be wrong, and the many judgments may be secretly correlated.

One episode in mathematics ties this pair of moves to the previous chapter's certificate. Appel and Haken's 1977 proof of the four color theorem<sup class="cite"><a href="#ref-26">26</a></sup> stirred lasting controversy because it depended on exhaustive case-checking by computer. In effect, it asked the mathematical community to trust an oracle. Later, Gonthier in 2008<sup class="cite"><a href="#ref-27">27</a></sup> redid it as a formal proof that a machine can check, and Hales's team<sup class="cite"><a href="#ref-28">28</a></sup> did the same for the Kepler conjecture. Both turned "trusting an oracle" into "checking a certificate." In *Mechanizing Proof*, MacKenzie<sup class="cite"><a href="#ref-29">29</a></sup> traces how this trust shifts among people, machines, and social processes. And the thesis of DeMillo and colleagues<sup class="cite"><a href="#ref-14">14</a></sup>, that a proof is at bottom a social process, amounts to resting the credibility of mathematics on the redundancy of human judgment.

One thing should be clear, though. So far, the first two pairs of moves, compressing the unknown and borrowing judgment, are still after the same thing: the truth about the object. They still want to know whether the thing is right or wrong. The next pair of moves does something more radical. It stops demanding that truth.

---

## References

> Waypoints: 1. historical scientific judgment; 2. theoretically studied material; 3. how science progresses; 4. how to live in an unverifiable world. This section was checked source by source.

1. N. G. de Bruijn (1970). "The mathematical language AUTOMATH, its usage, and some of its extensions." In *Symposium on Automatic Demonstration*. Springer (Lecture Notes in Mathematics 125), pp. 29-61. doi:[10.1007/bfb0060623](https://doi.org/10.1007/bfb0060623) [2]
   De Bruijn introduced AUTOMATH, one of the earliest formal languages able to let an entire body of mathematics be checked step by step by a machine, with the human writing the proof and the machine verifying that it is sound. It is the earliest engineered specimen of this chapter's "oracle in the loop": the human supplies the idea, the machine does nothing but scrupulously check, and the reader can see in it the source of the division of labor between "finding" and "verifying."
2. M. Gordon, R. Milner, C. Wadsworth (1979). *Edinburgh LCF: A Mechanized Logic of Computation*. Springer (Lecture Notes in Computer Science 78). doi:[10.1007/3-540-09724-4](https://doi.org/10.1007/3-540-09724-4) [2]
   This book proposed the LCF interactive proof system, whose design has been deeply influential: a small trusted kernel guarantees the reliability of every inference step, and no number of proof tactics can ever get around it. It supplies the classic paradigm for this chapter's account of "certificate checking," and the reader can see how the "trusted checker" is contracted into a part as small and as reliable as possible.
3. Y. Bertot, P. Castéran (2004). *Interactive Theorem Proving and Program Development. Coq'Art: The Calculus of Inductive Constructions*. Springer (Texts in Theoretical Computer Science, EATCS Series). doi:[10.1007/978-3-662-07964-5](https://doi.org/10.1007/978-3-662-07964-5) [2]
   This is the authoritative tutorial for the Coq proof assistant, explaining systematically how to construct and machine-check proofs interactively atop the calculus of inductive constructions. It carries the tradition represented by the previous two entries into contemporary practice and is the tool foundation for this chapter's later formalization work on the four color theorem and the Kepler conjecture; the reader who wants to understand "human gives the idea, machine verifies every step" hands-on can start here.
4. J. von Neumann (1956). "Probabilistic Logics and the Synthesis of Reliable Organisms from Unreliable Components." In C. E. Shannon and J. McCarthy, eds., *Automata Studies* (Annals of Mathematics Studies 34). Princeton University Press, pp. 43-98. doi:[10.1515/9781400882618-003](https://doi.org/10.1515/9781400882618-003) [2]
   Von Neumann here proves that one can assemble computation of arbitrarily reliable performance out of components that are themselves error-prone, by stacking redundancy and majority voting. This is one cornerstone of this chapter's "redundancy" move, supplying the earliest rigorous argument for "synthesizing reliability from many unreliable parts," and the reader should read its core idea of how redundancy drives down the error rate.
5. Marquis de Condorcet (1785). *Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix*. Imprimerie Royale, Paris. [Google Books](https://books.google.com/books?id=Mdb00-cUlXwC) [2][4]
   In this work on voting, Condorcet gives the famous jury theorem: if every judge is slightly better than chance and they are independent of one another, the probability that the majority vote is correct tends toward certainty as numbers grow. It supplies the arithmetic skeleton of this chapter's redundancy move and also plants its weak point in advance; the reader should note the theorem's dependence on the premise of "independence."
6. S. Goldwasser, S. Micali, C. Rackoff (1989). "The Knowledge Complexity of Interactive Proof Systems." *SIAM Journal on Computing*, 18(1), pp. 186-208. doi:[10.1137/0218012](https://doi.org/10.1137/0218012) [2]
   This paper founded the theoretical framework of interactive and zero-knowledge proofs: a verifier of limited computational power, through repeated interrogation plus random challenge, can wring a reliable verdict out of an untrustworthy prover. It is the purest mathematical source of this chapter's "interrogating an untrustworthy oracle," and the reader should read how it uses randomness to force out a truthful answer.
7. L. Babai (1985). "Trading Group Theory for Randomness." In *Proceedings of the 17th Annual ACM Symposium on Theory of Computing (STOC)*, pp. 421-429. doi:[10.1145/22145.22192](https://doi.org/10.1145/22145.22192) [2]
   Babai here independently proposed the Arthur-Merlin class of interactive proofs with randomness, staking out the same theoretical territory at almost the same moment as the previous entry. It reinforces this chapter's central idea: the random challenge is the key weapon by which a weak verifier subdues a strong and untrustworthy prover, and the reader can read it alongside the previous entry for the complementary perspective.
8. M. Pease, R. Shostak, L. Lamport (1980). "Reaching Agreement in the Presence of Faults." *Journal of the ACM*, 27(2), pp. 228-234. doi:[10.1145/322186.322188](https://doi.org/10.1145/322186.322188) [2]
   This paper first rigorously characterized how to reach consensus when some nodes may behave arbitrarily maliciously, giving the famous threshold: to tolerate $f$ traitors, the number of nodes must satisfy $n\ge 3f+1$. It is the source of this chapter's redundancy move in its adversarial version within distributed systems, and the reader should read the impossibility argument behind this threshold.
9. L. Lamport, R. Shostak, M. Pease (1982). "The Byzantine Generals Problem." *ACM Transactions on Programming Languages and Systems*, 4(3), pp. 382-401. doi:[10.1145/357172.357176](https://doi.org/10.1145/357172.357176) [2]
   This paper used the famous "Byzantine generals" metaphor to recast the result of the previous entry as a parable, and from then on "Byzantine fault tolerance" became the common name for adversarial consensus. It is the signature text for this chapter's idea of seeking agreement from many mutually distrustful judges, and the reader can read how it dresses an abstract threshold in an intuitively clear story.
10. M. J. Fischer, N. A. Lynch, M. S. Paterson (1985). "Impossibility of Distributed Consensus with One Faulty Process." *Journal of the ACM*, 32(2), pp. 374-382. doi:[10.1145/3149.214121](https://doi.org/10.1145/3149.214121) [2]
   This famous FLP impossibility theorem proves that in a fully asynchronous system, even if only one process may crash, there exists no deterministic consensus algorithm guaranteed to terminate. It marks out the boundary for this chapter's redundancy move, and the reader should read how it shows that consensus is not unconditionally available, thereby understanding why later practical systems must rely on extra assumptions to get around it.
11. M. Castro, B. Liskov (1999). "Practical Byzantine Fault Tolerance." In *Proceedings of the 3rd USENIX Symposium on Operating Systems Design and Implementation (OSDI)*, pp. 173-186. [link](https://www.usenix.org/conference/osdi-99/practical-byzantine-fault-tolerance) [2]
   The PBFT algorithm proposed in this paper was the first to turn Byzantine fault tolerance from theory into a system that runs in a real asynchronous network with acceptable performance. It is the key step by which this chapter's redundancy move descended from paper to engineering, and the reader can read how it kept the $n\ge 3f+1$ threshold while squeezing the overhead into a practical range, and can also recognize the direct precursor of later blockchain consensus.
12. D. E. Eckhardt, L. D. Lee (1985). "A Theoretical Basis for the Analysis of Multiversion Software Subject to Coincident Errors." *IEEE Transactions on Software Engineering*, SE-11(12), pp. 1511-1517. doi:[10.1109/tse.1985.231895](https://doi.org/10.1109/tse.1985.231895) [2]
   This paper argued theoretically that multiversion software, even when developed independently by different people, need not have independent errors: facing the same hard point, different versions tend to fail together, making the gain from redundancy far lower than the independence assumption would predict. It supplies a theoretical prediction of this chapter's "correlation floor" ahead of the experiment, and the reader should read how it characterizes common-cause error.
13. J. C. Knight, N. G. Leveson (1986). "An Experimental Evaluation of the Assumption of Independence in Multiversion Programming." *IEEE Transactions on Software Engineering*, SE-12(1), pp. 96-109. doi:[10.1109/tse.1986.6312924](https://doi.org/10.1109/tse.1986.6312924) [2]
   This is the famous experiment: many programmers were set to write programs independently to the same specification, expecting the errors to be mutually uncorrelated, but it was found that they stumbled together at the same hard points, and the independence assumption was refuted by experience. It supplies the empirical confirmation of the theoretical prediction of the previous entry, and is the most persuasive instance of this chapter's failure mode of "believing in independence where in truth there is correlation."
14. R. A. De Millo, R. J. Lipton, A. J. Perlis (1979). "Social Processes and Proofs of Theorems and Programs." *Communications of the ACM*, 22(5), pp. 271-280. doi:[10.1145/359104.359106](https://doi.org/10.1145/359104.359106) [3][4]
   This famous and controversial paper argues that what makes a mathematical proof credible is not the mechanical correctness of formal derivation but the social process by which the mathematical community repeatedly tests, propagates, and accepts it, and on this basis it questions the prospects of formal program verification. It supports this chapter's view that credibility is in the end placed on the redundancy of human judgment, and the reader should read its argument that a proof is, at bottom, a social process.
15. A. Shamir (1992). "IP = PSPACE." *Journal of the ACM*, 39(4), pp. 869-877. doi:[10.1145/146585.146609](https://doi.org/10.1145/146585.146609) [2]
   Shamir proved how astonishing the power of interactive proof is: by interrogating an untrustworthy prover alone, a weak verifier can reliably adjudicate the whole of PSPACE, an enormous class of problems, that is, $\mathrm{IP}=\mathrm{PSPACE}$. It is the most forceful mathematical footnote to this chapter's "borrowed judgment," and the reader should read how it delimits the ceiling reachable by "cleverly interrogating an oracle."
16. C. Lund, L. Fortnow, H. Karloff, N. Nisan (1992). "Algebraic Methods for Interactive Proof Systems." *Journal of the ACM*, 39(4), pp. 859-868. doi:[10.1145/146585.146605](https://doi.org/10.1145/146585.146605) [2]
   This paper introduced the algebraic method of arithmetizing Boolean formulas and then checking them with polynomials, and it was precisely this technical groundwork that led directly to the proof of $\mathrm{IP}=\mathrm{PSPACE}$ in the previous entry. It reveals the concrete mechanism of "clever interrogation": translating the verification problem into an algebraic identity that can be spot-checked at random. It stands as further reading around this chapter's lineage, and the reader can follow it into this set of techniques.
17. M. Blum, S. Kannan (1995). "Designing Programs That Check Their Work." *Journal of the ACM*, 42(1), pp. 269-291. doi:[10.1145/200836.200880](https://doi.org/10.1145/200836.200880) [2]
   This paper proposed the idea of the "program checker": let a program, when it gives a result, carry an independent and cheap checking routine that verifies whether this particular output is correct, without trusting the program itself. It brings the spirit of interactive proof to everyday computation, and for this chapter it is the model of the idea of "not trusting the producer, only checking its product"; the reader should read the construction of its checker.
18. S. Arora, C. Lund, R. Motwani, M. Sudan, M. Szegedy (1998). "Proof Verification and the Hardness of Approximation Problems." *Journal of the ACM*, 45(3), pp. 501-555. doi:[10.1145/278298.278306](https://doi.org/10.1145/278298.278306) [2]
   This is one of the core papers of the famous PCP theorem: any proof can be rewritten into a special format such that the verifier need only randomly spot-check a constant number of bits in it to judge its truth or falsity with high confidence. It pushes "spot-checking is enough" to the extreme and is the theoretical pinnacle of "how a weak verifier can efficiently check an enormous proof," a natural piece of further reading around this chapter; the reader should read the astonishing conclusion of its probabilistically checkable proofs.
19. S. Goldwasser, Y. T. Kalai, G. N. Rothblum (2015). "Delegating Computation: Interactive Proofs for Muggles." *Journal of the ACM*, 62(4), Article 27. doi:[10.1145/2699436](https://doi.org/10.1145/2699436) [2][4]
   This paper makes interactive proof genuinely serve "mortals": a user of limited computational power outsources a computation to a powerful but untrustworthy server, then checks whether the result is correct at a cost far smaller than recomputing it. It is where this chapter's ideas land in the age of cloud computing, and the reader should read how it turns "delegating computation for the weak, verifiably" into a practically feasible protocol.
20. L. K. Hansen, P. Salamon (1990). "Neural Network Ensembles." *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 12(10), pp. 993-1001. doi:[10.1109/34.58871](https://doi.org/10.1109/34.58871) [2]
   This paper showed, relatively early, that combining several independently trained neural networks to vote can give an overall accuracy significantly higher than any single network. It is the beginning of this chapter's redundancy move within machine learning, and the reader should read how it carries "majority voting lowers error" from logic circuits over to learning models, and again lands on the dependence on decorrelating member errors.
21. A. Krogh, J. Vedelsby (1995). "Neural Network Ensembles, Cross Validation, and Active Learning." In *Advances in Neural Information Processing Systems 7*. MIT Press, pp. 231-238. [link](https://proceedings.neurips.cc/paper/1994/hash/b8c37e33defde51cf91e1e03e51657da-Abstract.html) [2]
   This paper gives the classic decomposition of ensemble error: the overall error of the ensemble equals the average error of the members minus the disagreement among the members. It gives a machine-learning version of the precise "correlation floor" formula that chimes with this chapter, and the reader should read how it shows mathematically that the more diverse the members are, the more each errs in its own way, the more the ensemble is worth.
22. T. G. Dietterich (2000). "Ensemble Methods in Machine Learning." In *Multiple Classifier Systems (MCS 2000)*. Springer (Lecture Notes in Computer Science 1857), pp. 1-15. doi:[10.1007/3-540-45014-9\_1](https://doi.org/10.1007/3-540-45014-9_1) [2]
   This is a widely influential survey that sorts out why ensemble methods work and explains it from three angles: statistical, computational, and representational. It is a convenient entry point for the reader to survey the whole landscape of this chapter's redundancy move within machine learning, gathering the scattered techniques of voting, bagging, and boosting under one framework to be understood together.
23. L. Breiman (2001). "Random Forests." *Machine Learning*, 45(1), pp. 5-32. doi:[10.1023/a:1010933404324](https://doi.org/10.1023/a:1010933404324) [2]
   Breiman's random forest cultivates a crowd of mutually decorrelated decision trees through double randomization over samples and features, then votes to synthesize a powerful and robust predictor. It is one of the most successful practical specimens of the redundancy move, and its significance for this chapter is that its whole power comes precisely from deliberately manufactured independence; the reader can read how it actively drives down the correlation among members.
24. L. Hong, S. E. Page (2004). "Groups of Diverse Problem Solvers Can Outperform Groups of High-Ability Problem Solvers." *Proceedings of the National Academy of Sciences*, 101(46), pp. 16385-16389. doi:[10.1073/pnas.0403723101](https://doi.org/10.1073/pnas.0403723101) [2][3][4]
   Hong and Page argue, by way of a formal model, that under suitable conditions a group made up of diverse ordinary problem solvers can beat a group of homogeneous experts, because the difference in perspective that diversity brings is itself a resource. It generalizes this chapter's intuition that "independence and diversity are the heart of redundancy" to human groups, and the reader should read its thesis of "diversity beats ability" and its boundaries.
25. J. Surowiecki (2004). *The Wisdom of Crowds: Why the Many Are Smarter Than the Few and How Collective Wisdom Shapes Business, Economies, Societies, and Nations*. Doubleday. [Google Books](https://books.google.com/books?id=hHUsHOHqVzEC) [3][4]
   This widely circulated book by Surowiecki argues that under conditions of diversity, independence, decentralization, and a proper aggregation mechanism, the collective judgment of a crowd often beats that of an individual expert, and he repeatedly stresses that once independence is lost and convergence sets in, the crowd turns stupid. It brings this chapter's redundancy move to the everyday and social level, and the reader should read its repeated insistence on "the preconditions under which the wisdom of crowds holds."
26. K. Appel, W. Haken (1977). "Every Planar Map Is Four Colorable. Part I: Discharging." *Illinois Journal of Mathematics*, 21(3), pp. 429-490. doi:[10.1215/ijm/1256049011](https://doi.org/10.1215/ijm/1256049011) [1][3]
   This is the proof of the four color theorem, the first major mathematical proof in history to depend essentially on computer exhaustion of a great many cases, and for that reason it set off a long-running argument over "whether one can trust a machine conclusion that no human hand can check case by case." For this chapter it is the signature case of "trusting an oracle" and its cost, and the reader should read how this argument forced out the demand for a machine-checkable certificate.
27. G. Gonthier (2008). "Formal Proof: The Four-Color Theorem." *Notices of the American Mathematical Society*, 55(11), pp. 1382-1393. [link](https://www.ams.org/notices/200811/tx081101382p.pdf) [2][3]
   Gonthier used Coq to redo the four color theorem as a fully formalized proof that can be checked step by step by machine, thereby converting the "please trust the computer" predicament of the previous entry into "checking a certificate." It is a key point of contrast for this chapter, and the reader should read how it demonstrates that demoting the output of an untrustworthy oracle to an independently verifiable certificate dissolves the controversy along with it.
28. T. Hales et al. (2017). "A Formal Proof of the Kepler Conjecture." *Forum of Mathematics, Pi*, 5, article e2. doi:[10.1017/fmp.2017.1](https://doi.org/10.1017/fmp.2017.1) [2][3]
   Hales's team, after many years, used formal proof systems to machine-check the much-disputed proof of the Kepler conjecture all the way through, settling doubts that even peer review could not fully guarantee. It belongs to the same lineage as the previous entry, and its significance for this chapter is to confirm once more that when a proof grows too large for human checking, shifting trust from the oracle to a checkable certificate is the way back to certainty.
29. D. MacKenzie (2001). *Mechanizing Proof: Computing, Risk, and Trust*. MIT Press. doi:[10.7551/mitpress/4529.001.0001](https://doi.org/10.7551/mitpress/4529.001.0001) [1][3][4]
   This work of sociological history by MacKenzie tracks the rise of computer proof and formal verification, examining how "proof" and "certainty" are repeatedly defined and shifted among mathematicians, machines, and social processes. It supplies this chapter with a connecting perspective, placing oracle, certificate, and redundancy alike within a larger narrative of how trust is established and ceded, and the reader should read its examination of "how mechanized proof changed what we trust."
