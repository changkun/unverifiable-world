# Chapter 3: Falsifiable, Not Verifiable

> **Thesis:** Empirical science, the most disciplined way humans have of seeking knowledge, rests on a public admission: a theory can never be verified, only left unfalsified.

The previous chapter asked whether humans have a mature, disciplined way of living with the unverifiable over the long run. They do: empirical science. The most surprising thing about it is that its first principle is not a claim that it can establish the truth. It is a public admission that it never can.

## A Black Swan

"All swans are white." You have seen a thousand white swans, then a million, and this universal statement is still not verified, because the next swan might be black. Yet a single black swan is enough to overturn it completely. This is not a made-up example. In Europe, "all swans are white" was long taken as unquestioned common sense, until in 1697 a Dutch expedition saw a black swan for the first time, in Western Australia, and that "certainty" collapsed overnight.

This asymmetry is the pivot of the whole chapter. To verify a universal statement, you must check every case it covers. Those cases are usually infinite, open, and in the future, so it cannot be done. To falsify the statement, one counterexample is enough. In the language of logic, no finite set of observations can establish $\forall x\,P(x)$, but a single $\exists x\,\lnot P(x)$ is enough to shatter it. The whole discipline of science is built on recognizing and exploiting this asymmetry.

![The asymmetry between verification and falsification](../figures/f03-falsification.svg)

<figure class="uvw-viz" data-static="f03-falsification" role="group" aria-label="Interactive figure: the asymmetry between verification and falsification">
<div class="uvw-live" hidden>
<div class="uvw-claim">
<span class="uvw-claim-text">&ldquo;All swans are white&rdquo;</span>
<span class="uvw-state uvw-state-open">Not falsified</span>
</div>
<div class="uvw-bar" role="img" aria-label="Confidence progress bar">
<div class="uvw-bar-fill"></div>
<span class="uvw-bar-pct">0%</span>
</div>
<div class="uvw-swans" aria-hidden="true"></div>
<div class="uvw-controls">
<button type="button" class="uvw-btn uvw-btn-white">Add a white swan</button>
<button type="button" class="uvw-btn uvw-btn-black">Add a black swan</button>
<button type="button" class="uvw-btn uvw-btn-reset">Reset</button>
<span class="uvw-count">Confirmations <b class="uvw-v-count">0</b></span>
</div>
<p class="uvw-note"></p>
</div>
</figure>
<style>
.uvw-viz{margin:1.6em 0;padding:0}
.uvw-viz .uvw-live{border:1px solid var(--line,#e5e7eb);border-radius:10px;padding:16px 16px 18px;background:var(--paper,#fff);color:var(--ink,#1a1a1a)}
.uvw-viz .uvw-claim{display:flex;flex-wrap:wrap;align-items:center;gap:10px 14px}
.uvw-viz .uvw-claim-text{font-size:16px;font-weight:600}
.uvw-viz .uvw-state{font-size:13px;font-weight:700;letter-spacing:.04em;padding:3px 10px;border-radius:999px;border:1px solid currentColor}
.uvw-viz .uvw-state-open{color:#10b981}
.uvw-viz .uvw-state-broken{color:#dc2626}
.uvw-viz .uvw-bar{position:relative;margin-top:14px;height:30px;border-radius:8px;background:var(--line,#e5e7eb);overflow:hidden}
.uvw-viz .uvw-bar-fill{height:100%;width:0;background:#10b981;border-radius:8px 0 0 8px}
.uvw-viz .uvw-bar-pct{position:absolute;top:0;right:10px;line-height:30px;font-size:13px;font-weight:700;font-variant-numeric:tabular-nums;color:var(--ink,#1a1a1a)}
.uvw-viz .uvw-swans{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px;min-height:26px}
.uvw-viz .uvw-swan{width:22px;height:22px;border-radius:50%;box-sizing:border-box}
.uvw-viz .uvw-swan.white{background:#ffffff;border:2px solid #9ca3af}
.uvw-viz .uvw-swan.black{background:#111827;border:2px solid #dc2626}
.uvw-viz .uvw-controls{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin-top:16px}
.uvw-viz .uvw-btn{font:inherit;font-size:14px;cursor:pointer;padding:7px 13px;border-radius:8px;border:1px solid var(--line,#e5e7eb);background:var(--paper,#fff);color:var(--ink,#1a1a1a)}
.uvw-viz .uvw-btn:hover{border-color:var(--muted,#6b7280)}
.uvw-viz .uvw-btn:disabled{opacity:.45;cursor:not-allowed}
.uvw-viz .uvw-btn-white{border-color:#9ca3af}
.uvw-viz .uvw-btn-black{border-color:#dc2626;color:#dc2626}
.uvw-viz .uvw-count{font-size:14px;color:var(--muted,#6b7280);margin-left:auto}
.uvw-viz .uvw-count b{color:var(--ink,#1a1a1a);font-variant-numeric:tabular-nums}
.uvw-viz .uvw-note{margin:14px 0 0;font-size:13.5px;color:var(--muted,#6b7280);min-height:2.6em;line-height:1.6}
@media (prefers-reduced-motion: no-preference){.uvw-viz .uvw-bar-fill{transition:width .35s ease}}
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
var bWhite=root.querySelector('.uvw-btn-white'),bBlack=root.querySelector('.uvw-btn-black'),bReset=root.querySelector('.uvw-btn-reset');
var stream=root.querySelector('.uvw-swans');
var fill=root.querySelector('.uvw-bar-fill'),pct=root.querySelector('.uvw-bar-pct');
var state=root.querySelector('.uvw-state'),vCount=root.querySelector('.uvw-v-count'),note=root.querySelector('.uvw-note');
var n=0,falsified=false,CAP=99;
function conf(){return 100*(1-1/(n+1));}
function render(){
if(falsified){
fill.style.width='0%';
pct.textContent='0%';
state.textContent='Falsified';
state.className='uvw-state uvw-state-broken';
vCount.textContent=n;
note.textContent='One black swan is enough. A universal claim closes the moment a single counterexample appears, and no number of white swans can reopen it.';
return;
}
var c=Math.min(conf(),CAP);
fill.style.width=c.toFixed(1)+'%';
pct.textContent=Math.round(c)+'%';
state.textContent=n===0?'Not falsified':'Still not verified';
state.className='uvw-state uvw-state-open';
vCount.textContent=n;
if(n===0){note.textContent='Click "Add a white swan" and watch confidence creep upward yet never reach 100%.';}
else{note.textContent='White swan '+n+': confidence rises to '+Math.round(c)+'%, always a step short. No amount of confirmation can verify a universal claim.';}
}
function addSwan(cls){var s=document.createElement('span');s.className='uvw-swan '+cls;stream.appendChild(s);}
function setDisabled(d){bWhite.disabled=d;bBlack.disabled=d;}
bWhite.addEventListener('click',function(){if(falsified)return;n++;addSwan('white');render();});
bBlack.addEventListener('click',function(){if(falsified)return;falsified=true;addSwan('black');setDisabled(true);render();});
bReset.addEventListener('click',function(){n=0;falsified=false;stream.innerHTML='';setDisabled(false);render();});
render();
})();
</script>

## Hume and the Problem of Induction

Hume got to the root of this in 1739<sup class="cite"><a href="#ref-4">4</a></sup>. What entitles us to believe that a regularity that held in the past will go on holding in the future? Logic gives no warrant for it. From "the sun has risen every day in the past" you cannot infer "the sun must rise tomorrow," because that inference already assumes that past patterns will continue into the future, which is what was to be proved. Induction has no logical guarantee. Hume's conclusion is calm and complete: what we rely on is habit, not proof.

This is the philosophical footing of the "future" break in Chapter 1. All knowledge of the world's general regularities is built on a finite past, so none of it can be verified in advance. If science is to count as knowledge, it cannot make verification its goal, because that goal is out of reach.

## Popper's Way Out

In 1934 Popper<sup class="cite"><a href="#ref-1">1</a></sup> (writing in German) offered a way out: since verification cannot be had, stop demanding it, and use falsification instead. Whether a theory is scientific does not depend on how much evidence supports it, since support can always be found. It depends on whether the theory sticks its neck out and makes risky predictions that could turn out wrong. Astrology, like any doctrine that can explain away everything, is unfalsifiable and therefore unscientific. General relativity predicted that the sun's gravity would bend starlight by a specific angle, and the 1919 eclipse observations might well have measured a different value and refuted the prediction. The theory was good science because it dared to risk being overturned.

So science became a machine built for living with the unverifiable. It never claims to have proved anything. It says only that this theory has not yet been falsified, so we will use it for now. This is a posture, one that trades the unmeasurable "true" for the measurable "not yet overturned." Look familiar? It is the same proxy substitution the mathematician uses in Chapter 7, carried up to the level of epistemology.

## A Necessary Qualification

This needs to be said plainly, and right away: Popper's falsificationism is far from settled in the philosophy of science. This book treats it as a clear point of entry, not as the final word.

The strongest objection comes from the holism of Duhem and Quine (also called the Quine-Duhem thesis). Duhem in 1906<sup class="cite"><a href="#ref-10">10</a></sup> and Quine in 1951<sup class="cite"><a href="#ref-9">9</a></sup> pointed out that you can never test a hypothesis in isolation. Every prediction depends on a large bundle of auxiliary assumptions (the instrument works, the background conditions hold, the approximation is reasonable). When an experiment fails, you can always shift the blame to one of those auxiliary assumptions and keep the core hypothesis intact. So the picture in which "a single counterexample cleanly overturns a theory" is not as clean as it looks. Kuhn in 1962<sup class="cite"><a href="#ref-5">5</a></sup> went further. During periods of normal science, he argued, scientists are in no hurry to falsify anything. Anomalies are set aside until a crisis in the paradigm brings about a revolutionary replacement. Lakatos in 1970<sup class="cite"><a href="#ref-6">6</a></sup> replaced black-and-white falsification with the progress or degeneration of a "research programme." Feyerabend<sup class="cite"><a href="#ref-7">7</a></sup> rejected any unified method at all. Another route is Bayesian confirmation theory<sup class="cite"><a href="#ref-24">24</a></sup>. It wants no yes-or-no verdict, and instead treats evidence as something that adjusts the probability of a belief,

$$P(H\mid e)=\frac{P(e\mid H)\,P(H)}{P(e)},$$

which in turn anticipates the later move of calibration. Mayo's "severe testing"<sup class="cite"><a href="#ref-14">14</a></sup> is a refined heir to falsificationism, while Stanford<sup class="cite"><a href="#ref-19">19</a></sup> reminds us that many "unconceived alternatives" still lie beyond our view.

Laying out these disputes does not demolish Popper. It does what this book ought to do: state a powerful framework while marking its limits. The whole book sets out to practice that same posture.

## Science Found These Moves Long Ago

Here is what this chapter really gives the book. Look at the everyday machinery of science through the lens of the eight moves, and you find that science worked out several of them long ago, under other names.

Peer review is redundancy and consensus. It distrusts any single judge, uses several independent reviewers, and looks for agreement among them. Replication is also redundancy: a result is not taken seriously until someone else reproduces it independently, somewhere else. Preregistration is an audit trail. The hypothesis and the analysis plan are registered before anyone sees the data, so the target cannot be moved afterward and noise cannot be talked up into a signal. Confidence intervals and error statistics are certificates and bounds. They do not claim that a statement is true, only that a bounded guarantee holds at a stated confidence level. Double-blinding and randomization are defenses against the fifth face (adversarial), where the adversary is often the researcher's own bias and expectations. The significance threshold is a crude form of calibration.

In other words, humanity's most serious enterprise of inquiry is itself a living example of this book's convergence claim. This is the book's first hint, and a weighty one. The unverifiability that science faces (about general regularities, about the future) has its own particular source. Yet the responses science has been forced into rhyme with the responses in software, mathematics, and organizations.

## When the Machine Fails: The Replication Crisis

Looking at it the other way around makes this clearer. When these moves are weakened, science stops correcting itself, and the result is the replication crisis. Ioannidis's 2005 paper<sup class="cite"><a href="#ref-28">28</a></sup>, "Why Most Published Research Findings Are False," made the problem plain, and so did the Open Science Collaboration's 2015 large-scale replication<sup class="cite"><a href="#ref-29">29</a></sup> of a hundred psychology studies. Of those studies, 97 percent had originally reported significant results, yet when they were redone, only about thirty-six still held, fewer than half. The machine spins in neutral when preregistration is missing (so the target can be moved afterward), when samples are too small, when publication bias lets only the attractive results through, and when few people take on the thankless work of replication.

The diagnosis and the repair are both written in the language of those moves: restoring preregistration (putting the audit trail back), encouraging and rewarding replication (putting redundancy back), registered reports, and more severe testing. The problem and the remedy come down to the same vocabulary. This point returns in Chapter 10, on borrowed judgment, and in Chapter 12, on audit trails and auditing.

## What Comes Next

Science has shown one thing: you can seek knowledge in a disciplined way in a world without verification, and wherever this is done well, it relies on these same moves. That is a proof of concept for the whole book.

But there is a trap here too. All five faces wear the same expression, "I cannot check it," and the moves for handling them look so alike that a very tempting thought arises: why not just declare that unverifiability is one problem, with one unified solution? About the problem, this thought is wrong. About the response, it stumbles onto something right. The next chapter is devoted to this temptation.

---

## References

> Waypoints: 1. historical scientific judgment; 2. theoretically studied material; 3. how science progresses; 4. how to live in an unverifiable world. This section was checked source by source.

1. K. Popper (1959). *The Logic of Scientific Discovery*. Hutchinson. [Google Books](https://books.google.com/books?id=iucRkAEACAAJ) [2][3]
   Popper here sets out falsificationism systematically: a scientific theory cannot be empirically verified, only refuted, so falsifiability becomes the line between science and non-science. The original German edition, *Logik der Forschung*, was published by Springer in Vienna, with the copyright page marked 1935 though it actually appeared in late 1934 (hence often dated 1934); this English edition was substantially revised and expanded by the author himself. The section "Popper's Way Out" is built directly on this, and the reader should attend above all to the epistemological posture of replacing "verification" with "not yet falsified."

2. K. Popper (1963). *Conjectures and Refutations: The Growth of Scientific Knowledge*. Routledge and Kegan Paul. [Google Books](https://books.google.com/books?id=IENmxiVBaSoC) [3]
   This essay collection unfolds falsificationism into a whole view of the growth of knowledge: knowledge advances through bold conjecture and merciless refutation, and the growth of science is not the accumulation of confirmations but the ceaseless weeding out of errors. Compared with the logical skeleton of the earlier work, it shows more vividly how "trial and error" drives scientific progress, and is good reading for understanding this chapter's waypoint of how science progresses.

3. K. Popper (1972). *Objective Knowledge: An Evolutionary Approach*. Clarendon Press. [Google Books](https://books.google.com/books?id=o8oPAQAAIAAJ) [3]
   Popper here likens the growth of knowledge to an evolutionary process of trial and error, and proposes a "third world," the domain of objective knowledge itself, existing independently of any individual subjective mind. It pushes falsificationism toward an ontological picture of how objective knowledge can accumulate without a subject, and offers further reading for those who wish to pursue how science progresses in depth.

4. D. Hume (1739). *A Treatise of Human Nature*. John Noon. [Google Books](https://books.google.com/books?id=JzRgzQEACAAJ) [2]
   Hume here raises the problem of induction, that source-level difficulty: from a past regularity one cannot infer a future regularity, because the inference itself presupposes the "uniformity of nature," which is precisely what is to be proved; our belief in causation and regularity comes, in the end, from habit rather than proof. Books I and II were published by John Noon in 1739, and Book III, *Of Morals*, by Thomas Longman in 1740, with the first edition conventionally dated 1739. The section "Hume and the Problem of Induction" is founded on this, the philosophical footing for understanding why science cannot take "verification" as its goal.

5. T. Kuhn (1962). *The Structure of Scientific Revolutions*. University of Chicago Press. [Google Books](https://books.google.com/books?id=3eP5Y_OOuzwC) [1][3]
   Kuhn, drawing on a great many cases from the history of science, argues that science does not approach truth at a steady pace, but solves puzzles within a shared paradigm during periods of "normal science," and only after anomalies accumulate into crisis does a paradigm-shifting scientific revolution occur, with old and new paradigms being incommensurable. It is an important correction to Popper's picture, showing that scientists are often in no hurry to falsify an anomaly. This chapter's "A Necessary Qualification" cites it to mark the boundary of falsificationism.

6. I. Lakatos (1970). "Falsification and the Methodology of Scientific Research Programmes." In I. Lakatos and A. Musgrave (eds.), *Criticism and the Growth of Knowledge*, pp. 91-196. Cambridge University Press. doi:[10.1017/cbo9781139171434.009](https://doi.org/10.1017/cbo9781139171434.009) [1][3]
   Lakatos uses the "research programme" to reconcile Popper and Kuhn: each programme has a protected hard core and a surrounding belt of adjustable auxiliary assumptions, and the standard of judgment is not a single counterexample but whether the programme as a whole is, over time, "progressing" (continuing to make and fulfill new predictions) or "degenerating" (busy only with patching after the fact). It replaces black-and-white falsification with a historical judgment about a programme's advance or retreat, a key reference when this chapter delimits the boundary of falsificationism.

7. P. Feyerabend (1975). *Against Method: Outline of an Anarchistic Theory of Knowledge*. New Left Books. [Google Books](https://books.google.com/books?id=XL_GAAAAIAAJ) [1][3][4]
   Feyerabend argues forcefully, through cases from the history of science such as Galileo, that there is no universally valid set of scientific methods, and that major advances often come precisely from breaking existing rules, hence his famous slogan "anything goes." It is the most radical opposition to a unified methodology, cited in this chapter to make plain that even a methodological claim as mild as "falsification" is rejected at the root by some.

8. C. G. Hempel (1965). *Aspects of Scientific Explanation and Other Essays in the Philosophy of Science*. Free Press. [Google Books](https://books.google.com/books?id=BjzbAAAAMAAJ) [2]
   In this essay collection Hempel gives a culminating account of the covering-law model of scientific explanation, including both deductive-nomological and inductive-statistical explanation, and discusses the logic of confirmation and its paradoxes. It represents logical empiricism's systematic characterization of the "theoretically studied material," and supplies this chapter with a classic background on what counts as testable and explicable.

9. W. V. O. Quine (1951). "Two Dogmas of Empiricism." *The Philosophical Review*, 60(1), 20-43. doi:[10.2307/2181906](https://doi.org/10.2307/2181906) [2]
   Quine attacks the two dogmas of logical empiricism, the sharp divide between analytic and synthetic and reductionism, and proposes epistemological holism, holding that our beliefs face experience together as one whole web, and that no single statement can be verified or refuted in isolation. Combined with Duhem's holism of testing (jointly called the Quine-Duhem thesis), it strikes directly at the picture in which "a single counterexample cleanly overturns a hypothesis," a core reference for this chapter's delimiting of the boundary of falsificationism.

10. P. Duhem (1906). *La théorie physique: son objet, sa structure*. Chevalier & Rivière. [Google Books](https://books.google.com/books?id=v3IlAAAAMAAJ) [2]
    Duhem here proposes the holism of testing: an experiment in physics never tests an isolated hypothesis but rather "the hypothesis together with a whole set of auxiliary assumptions and background theories," so a failed prediction cannot determine exactly where the error lies. This is the source of what was later, with Quine, called holism, used in this chapter to show that the bearing of a counterexample is not as definite as it appears. The original 1906 French edition is taken as authoritative here; the second edition was published by Marcel Rivière in 1914, and P. P. Wiener's English translation, *The Aim and Structure of Physical Theory*, was issued by Princeton University Press in 1954.

11. M. Polanyi (1958). *Personal Knowledge: Towards a Post-Critical Philosophy*. University of Chicago Press. [Google Books](https://books.google.com/books?id=QPPIBQAAQBAJ) [1][4]
    Polanyi proposes "tacit knowledge": we know far more than we can tell, and in scientific inquiry there is always a layer of personal judgment and craft that cannot be formalized and can only be acquired through practice and apprenticeship. It reminds us that no methodology, however strict, can eliminate the scientist's own, inarticulable judgment, echoing this chapter's waypoints of historical scientific judgment and how to live in an unverifiable world.

12. B. C. van Fraassen (1980). *The Scientific Image*. Clarendon Press. doi:[10.1093/0198244274.001.0001](https://doi.org/10.1093/0198244274.001.0001) [2][4]
    Van Fraassen proposes "constructive empiricism": the aim of science is not to claim a theory is true but only that it is "empirically adequate," that is, that it correctly saves the observable phenomena; to accept a theory is to believe it empirically adequate, not to believe its unobservable parts actually exist. It turns "unverifiable" into a mature scientific attitude, resonating with this chapter's posture of replacing "true" with "not yet overturned."

13. I. Hacking (1983). *Representing and Intervening: Introductory Topics in the Philosophy of Natural Science*. Cambridge University Press. doi:[10.1017/cbo9780511814563](https://doi.org/10.1017/cbo9780511814563) [2][3]
    Hacking shifts philosophical attention from "representing" to "intervening," arguing that the best defense of realism lies not in theory but in experiment: when we can stably manipulate electrons to probe other things, electrons are real ("if you can spray them, they are real"). It opens a new approach to scientific realism grounded in experimental practice, and reminds the reader that scientific progress likewise depends on hands-on intervention, not on theoretical testing alone.

14. D. G. Mayo (1996). *Error and the Growth of Experimental Knowledge*. University of Chicago Press. doi:[10.7208/chicago/9780226511993.001.0001](https://doi.org/10.7208/chicago/9780226511993.001.0001) [3]
    Mayo proposes the philosophy of "error statistics": we have reason to accept a hypothesis only when it has passed a severe test, one that "would very probably have failed if the hypothesis were false." This makes Popper's spirit of falsification operational as a statistical testing procedure, and is a refined heir of falsificationism; this chapter's notion of "severe testing" comes from here (part of the Science and Its Conceptual Foundations series).

15. D. G. Mayo (2018). *Statistical Inference as Severe Testing: How to Get Beyond the Statistics Wars*. Cambridge University Press. doi:[10.1017/9781107286184](https://doi.org/10.1017/9781107286184) [3][4]
    Mayo here reconstructs statistical inference around "severity" as a unifying principle, attempting to get past the long-running "statistics wars" between frequentists and Bayesians, and on this basis responds to criticisms of significance testing in the replication crisis. It develops the programme of item 14 into a methodology facing contemporary statistical practice, and is especially apt for understanding how to use statistical evidence responsibly in an unverifiable world.

16. L. Laudan (1981). "A Confutation of Convergent Realism." *Philosophy of Science*, 48(1), 19-49. doi:[10.1086/288975](https://doi.org/10.1086/288975) [1][2]
    Laudan lists a batch of theories from the history of science that were once successful (able to predict, able to explain) yet were finally abandoned, such as phlogiston and the ether, arguing that the inference "success implies truth" does not hold up, a forceful rebuttal to convergent realism often called the "pessimistic meta-induction." It shows that even empirically very successful theories need not be close to the truth, reinforcing this chapter's claim that science does not take "verifying the truth" as its goal.

17. L. Laudan (1977). *Progress and Its Problems: Towards a Theory of Scientific Growth*. University of California Press. [Google Books](https://books.google.com/books?id=TMuXQgAACAAJ) [3]
    Laudan argues for measuring scientific progress by "problem-solving capacity" rather than approach to truth: whether a research tradition progresses turns on the net gain in the empirical and conceptual problems it solves. It offers a view of progress that bypasses the concept of truth, supplying this chapter's how-science-progresses with an alternative framework that does not depend on verification.

18. P. Kitcher (1993). *The Advancement of Science: Science without Legend, Objectivity without Illusions*. Oxford University Press. [Google Books](https://books.google.com/books?id=H3U8DwAAQBAJ) [3]
    Kitcher, having discarded the "legend" of science as all-knowing and all-powerful, also refuses relativism, and instead rebuilds a moderate and defensible objectivity and view of progress from science's social and cognitive practice. It demonstrates how one can, while admitting that science is shaped by history and society, still hold onto the two concepts of progress and objectivity, in line with this chapter's stance of affirming science while marking its boundaries.

19. P. K. Stanford (2006). *Exceeding Our Grasp: Science, History, and the Problem of Unconceived Alternatives*. Oxford University Press. doi:[10.1093/0195174089.001.0001](https://doi.org/10.1093/0195174089.001.0001) [1][2][3][4]
    Stanford raises the problem of "unconceived alternatives": the history of science shows again and again that past scientists always had theoretical options that only appeared later and were utterly unthinkable at the time, so we have no reason to believe that we have today exhausted all viable explanations. He distills this "new induction" from historical cases such as genetics, directly echoing this book's framework of "an unverifiable world," and reminding the reader that there is always an unconceived possibility beyond our view.

20. N. Goodman (1955). *Fact, Fiction, and Forecast*. Harvard University Press. [Google Books](https://books.google.com/books?id=DcfmEAAAQBAJ) [2]
    Goodman raises the "new riddle of induction": "green" and the artificial predicate "grue" (meaning observed as green before a certain time and blue thereafter) both fit all observations to date equally well, yet yield opposite predictions, which shows that induction cannot be settled by evidence alone but must also depend on which predicates are "projectible." It shows that the difficulty of induction is not only the Humean problem of justification but, more deeply, the indeterminacy of the regularity itself, deepening this chapter's understanding of why induction is unreliable. The first-edition year is commonly given as 1955 (one HUP blurb gives 1954, a slight ambiguity; the widely cited 1955 is followed here).

21. C. G. Hempel and P. Oppenheim (1948). "Studies in the Logic of Explanation." *Philosophy of Science*, 15(2), 135-175. doi:[10.1086/286983](https://doi.org/10.1086/286983) [2]
    Hempel and Oppenheim here lay the foundation of the deductive-nomological (D-N) model of explanation: that a phenomenon is scientifically explained means that it can be logically derived from general laws plus initial conditions. It is the starting point of twentieth-century theories of scientific explanation, defining what "being explicable" means logically, and supplying this chapter with an underlying framework for how science characterizes regularities.

22. R. Carnap (1936-1937). "Testability and Meaning." *Philosophy of Science*, 3(4), 419-471; 4(1), 1-40. doi:[10.1086/286432](https://doi.org/10.1086/286432) [2]
    Carnap here loosens the strict principle of verifiability, using the broader notions of "testability" and "confirmability" to demarcate meaningful empirical statements, and handles the connection between theoretical terms and observation through devices such as disposition predicates. It records logical empiricism's key retreat from "verifiable" to "testable," resonating exactly with this chapter's main line of "verification is out of reach, so use the reachable instead." The text was published in two parts, volume 3 issue 4 (1936) and volume 4 issue 1 (1937).

23. W. C. Salmon (1984). *Scientific Explanation and the Causal Structure of the World*. Princeton University Press. doi:[10.1515/9780691221489](https://doi.org/10.1515/9780691221489) [2]
    Salmon argues that the heart of scientific explanation is not logical derivation but the disclosure of causal mechanisms: to explain a phenomenon is to embed it in the world's web of causal processes and causal interactions. It is an important correction to the covering-law model, shifting the standard of "being explicable" from derivability to traceable causal structure, supplying this chapter's understanding of how science characterizes the world with the dimension of causation.

24. C. Howson and P. Urbach (1989). *Scientific Reasoning: The Bayesian Approach*. Open Court. [Google Books](https://books.google.com/books?id=iYoQAQAAIAAJ) [2][3]
    Howson and Urbach systematically advocate a Bayesian view of scientific reasoning: rather than a true-or-false two-valued verdict, they treat evidence as a continuous adjustment, by Bayes's theorem, to the probability of a belief, and on this basis respond to many difficulties of induction and confirmation. It is the representative work on the Bayesian confirmation theory mentioned in this chapter's text, forming a contrast with falsification and severe testing, and foreshadowing the book's move of calibration.

25. E. Sober (2008). *Evidence and Evolution: The Logic Behind the Science*. Cambridge University Press. doi:[10.1017/cbo9780511806285](https://doi.org/10.1017/cbo9780511806285) [2]
    Sober uses the tools of likelihood theory and statistical inference to analyze in detail "what evidence supports," and discusses which hypotheses are genuinely testable, including an anatomy of why intelligent design is untestable. It brings the abstract question of testability down to concrete scientific inferential practice (especially with evolution as the example), demonstrating how to judge rigorously whether a claim can withstand the test of evidence.

26. P. Godfrey-Smith (2003). *Theory and Reality: An Introduction to the Philosophy of Science*. University of Chicago Press. doi:[10.7208/chicago/9780226300610.001.0001](https://doi.org/10.7208/chicago/9780226300610.001.0001) [2][3]
    Godfrey-Smith's widely praised introduction to the philosophy of science lays out clearly the whole thread from logical empiricism, falsificationism, and Kuhn's paradigm to Bayesianism and the dispute over scientific realism. It serves well as an introductory anchor for the many topics of this chapter, and the reader who wants to build a global map before reading the monographs can begin here.

27. N. Cartwright (1983). *How the Laws of Physics Lie*. Clarendon Press. doi:[10.1093/0198247044.001.0001](https://doi.org/10.1093/0198247044.001.0001) [2][3]
    Cartwright argues that the fundamental laws of physics are universal and elegant precisely because they do not faithfully describe the real world but rather describe highly idealized models; the more fundamental a law, the greater its explanatory power, yet the more it "lies" in description. She turns instead to value the concrete laws and causal capacities closer to the phenomena, reminding the reader that the "truth" of scientific laws is far more complex than usually supposed, deepening this chapter's reflection on the relation between theory and world.

28. J. P. A. Ioannidis (2005). "Why Most Published Research Findings Are False." *PLoS Medicine*, 2(8), e124. doi:[10.1371/journal.pmed.0020124](https://doi.org/10.1371/journal.pmed.0020124) [3][4]
    Ioannidis argues, through concise statistical modeling, that in fields with small effect sizes, flexible study designs, and rampant publication bias, the probability that a published "positive" finding is false is often higher than the probability that it is true, and false positives can systematically outnumber true ones. It is a founding document of the replication crisis, and the core evidence for this chapter's section "When the Machine Fails," showing how science's self-correction spins in neutral once it is weakened.

29. Open Science Collaboration (2015). "Estimating the Reproducibility of Psychological Science." *Science*, 349(6251), aac4716. doi:[10.1126/science.aac4716](https://doi.org/10.1126/science.aac4716) [3][4]
    The Open Science Collaboration, coordinating over a hundred researchers, conducted systematic direct replications of a hundred published psychology studies, with the result that fewer than half successfully reproduced the original effect, and the reproduced effects were generally weaker than originally reported. It turns the replication crisis from argument into large-scale evidence, the empirical core of this chapter's "replication crisis" section, and underscores why moves such as replication and preregistration are indispensable.
