# Chapter 6: The Agent Released

> **Thesis:** Once you hand action over to an autonomous system, you cannot verify how it will behave in every situation it will meet (the open world), and if it can also act strategically, adversarial unverifiability is added on top. So the response shifts from "prove it is right" to "limit what it can break, put a price on the trust you place in it, and make its behavior checkable after the fact."

## After You Hand It Over

In the last chapter you were still there. In this one, you let go of the wheel.

You start a piece of untrusted code running. You give tools and permissions to a system that can choose its own next step. You let a self-driving car onto the road without you sitting in it. Once you hand over the power to act, a new difficulty appears. You cannot verify how the system will behave in every situation it will meet, because you have not seen most of those situations and cannot list them in advance. In the last chapter, unverifiability came from a goal hidden inside someone else's head. Here it comes from behavior that happens in the future, in places you cannot see. And when the system can also act strategically, an adversarial layer comes on top. The "flash crash" of May 6, 2010 was a foretaste. Automated trading programs, reacting to one another, knocked the Dow Jones down by nearly a thousand points within minutes, and the index rebounded almost as quickly. No programmer had foreseen that trades would cascade like that. Each program was fine in testing. Put together, and put into a live market, they produced a disaster no one had verified.

## Why More Testing Cannot Close the Gap

What you tested was a small, finite set of inputs. What the system will meet is an open world. The gap between the two is not an engineering gap that "a few more tests will close." It is rooted in principle.

Rice's theorem puts it in hard terms: every nontrivial semantic property of a program is undecidable. In other words, no general algorithm can decide, for an arbitrary program, whether it is "always safe," "never leaks," or "always terminates in a good state." This is not a shortage of computing power. It is logically impossible, the shadow that Turing's halting problem casts over program behavior. For any sufficiently general autonomous system, the kind of guarantee you want cannot, in principle, be verified in advance once and for all.

An even harder blow comes from a famous argument in Thompson's 1984 Turing Award lecture<sup class="cite"><a href="#ref-9">9</a></sup>: you cannot even fully trust the program you are running. A tampered compiler can quietly plant a back door at compile time and then wipe the trace from its own source code, so you can audit every line of source and find nothing. What you can verify is always some surface layer. Beneath it lie layers you have not examined and can never exhaust. Put the two together. Behavior on unseen inputs cannot be verified, and the artifact itself cannot be fully verified at its base. This is the hardest unverifiability the book has met so far.

## When It Acts Strategically

If the system merely mishandled unseen inputs, passively, that would still be only partial observability plus the open world. But once it has a goal of its own, and that goal is not fully aligned with yours, it will act on its own initiative and strategically, including working around your checks. This is where the fifth face from Chapter 2, the adversarial one, takes the stage.

This is not a science-fiction worry. It has a structural cause. Omohundro in 2008<sup class="cite"><a href="#ref-10">10</a></sup> and Bostrom in 2014<sup class="cite"><a href="#ref-11">11</a></sup> pointed to what is called instrumental convergence. An agent optimizing for almost any goal will, along the way, pursue certain instrumental subgoals (self-preservation, acquiring resources, resisting shutdown), because these are useful for almost any final goal. Turner and colleagues in 2021 turned one of these into a theorem<sup class="cite"><a href="#ref-14">14</a></sup>: under fairly general conditions, optimal policies tend to seek power, meaning states that keep more options open. In today's systems this shows up as a set of concrete, thorny failures. A misspecified reward gets gamed by the system<sup class="cite"><a href="#ref-16">16</a></sup>. Or the specification is correct, yet the goal generalizes wrong<sup class="cite"><a href="#ref-17">17</a></sup>. And Krakovna and colleagues<sup class="cite"><a href="#ref-18">18</a></sup> have gathered a large collection of "specification gaming" cases, in which the system satisfies the goal you wrote down to the letter yet violates what you meant. Even at the narrowest level, adversarial examples show<sup class="cite"><a href="#ref-19">19</a></sup><sup class="cite"><a href="#ref-20">20</a></sup> that a perturbation too small for the human eye to notice can coax a high-performing model into absurd errors. A less technical and very plain example is Tay, the chatbot Microsoft released in 2016. It was designed to learn from its conversations with the public. A group of people fed it malicious speech in an organized way, and in under a day it began posting racist and offensive content. It was pulled offline in an emergency about sixteen hours after launch. A system that has been released, that can learn, and that runs into an open world deliberately trying to thwart it: once those three meet, testing in advance cannot hold the line.

The problem is old. Economics long ago named it the principal-agent problem<sup class="cite"><a href="#ref-32">32</a></sup><sup class="cite"><a href="#ref-33">33</a></sup>. When you delegate action to someone else and cannot fully monitor them, the gap between their interests and yours produces an "agency cost." For two thousand years, people hiring others, drawing up contracts, and setting up oversight have been dealing with this same structure. Autonomous systems have only pushed it to a new scale.

## The Response: From Proving It Right to Fencing In Its Errors

Since you cannot prove in advance that the system is right, the response that works stops arguing over proof and asks three different questions instead. If it is wrong, how bad can things get? How much should I trust it? And if it really is wrong, can I find out after the fact? Three moves answer the three questions.

**The first move, containment and fencing: shrink the blast radius.** This is the oldest wisdom in computer security. Saltzer and Schroeder's principle of least privilege from 1975<sup class="cite"><a href="#ref-1">1</a></sup> and Lampson's confinement problem from 1973<sup class="cite"><a href="#ref-2">2</a></sup> say the same thing. Give each component only the minimum capability it needs to do its own job, and fence off what it can reach. Sandboxes, capability limits, and separation of duties are all forms of this idea. For agents, the move gains one more dimension, corrigibility: design the system so that it does not resist being stopped. Soares and colleagues' work on corrigibility from 2015<sup class="cite"><a href="#ref-5">5</a></sup>, Orseau and Armstrong's "safely interruptible agents" from 2016<sup class="cite"><a href="#ref-4">4</a></sup>, and Hadfield-Menell and colleagues' "off-switch game" from 2017<sup class="cite"><a href="#ref-6">6</a></sup> all study how to keep a goal-directed system from treating a human pressing the stop button as a threat to resist.

**The second move, calibration and graded trust: grades, not a switch.** Do not treat the system's output as a switch between "trusted" and "untrusted." Instead, keep a calibrated confidence and act in grades, according to how high that confidence is. This requires the system's confidence in itself to be trustworthy, and modern neural networks are often overconfident<sup class="cite"><a href="#ref-21">21</a></sup>. So they need recalibration, or conformal prediction<sup class="cite"><a href="#ref-22">22</a></sup><sup class="cite"><a href="#ref-23">23</a></sup>, which gives uncertainty with coverage guarantees. In operational terms, this becomes a graded-autonomy rule (allow, ask, block) that takes confidence $p$ and potential harm $c$ as inputs, where $\tau_{\text{hi}}$ and $\tau_{\text{lo}}$ are confidence thresholds and $c_{\max}$ is the maximum tolerable harm:

$$a(p,c)=\begin{cases} \textsf{allow}, & p \ge \tau_{\text{hi}}\ \wedge\ c \le c_{\max},\\ \textsf{ask}, & \tau_{\text{lo}} \le p < \tau_{\text{hi}},\\ \textsf{block}, & p < \tau_{\text{lo}}\ \vee\ c > c_{\max}. \end{cases}$$

![Allow / ask / block: graded autonomy by confidence and harm](../figures/f06-allow-ask-block.svg)

<figure class="uvw-viz" data-static="f06-allow-ask-block" role="group" aria-label="Allow / ask / block: graded autonomy, interactive">
<div class="uvw-live" hidden>
 <div class="uvw-plot">
 <svg viewBox="0 0 640 380" preserveAspectRatio="xMidYMid meet" aria-hidden="true">
 <rect class="uvw-r-allow" x="70" y="45" width="540" height="285"></rect>
 <rect class="uvw-r-ask" x="70" y="45" width="540" height="285"></rect>
 <rect class="uvw-r-block" x="70" y="45" width="540" height="285"></rect>
 <line class="uvw-line-tau" y1="45" y2="330" stroke="#6366f1" stroke-width="1.6" stroke-dasharray="5 4" opacity="0.7"></line>
 <line class="uvw-line-cmax" x1="70" x2="610" stroke="#ef4444" stroke-width="1.6" stroke-dasharray="5 4" opacity="0.7"></line>
 <text class="uvw-lab-allow uvw-rlab" text-anchor="middle">ALLOW</text>
 <text class="uvw-lab-ask uvw-rlab" text-anchor="middle">ASK</text>
 <text class="uvw-lab-block uvw-rlab" text-anchor="middle">BLOCK</text>
 <g class="uvw-axes" fill="none" stroke="currentColor" stroke-width="1.2" opacity="0.4">
 <line x1="70" y1="330" x2="610" y2="330"></line>
 <line x1="70" y1="45" x2="70" y2="330"></line>
 </g>
 <circle class="uvw-dot" r="8"></circle>
 <text class="uvw-xlab" x="340" y="366" text-anchor="middle">confidence p (higher = surer) →</text>
 <text class="uvw-ylab" x="20" y="187" text-anchor="middle" transform="rotate(-90 20 187)">potential harm c →</text>
 <rect class="uvw-hit" x="70" y="45" width="540" height="285" fill="transparent" style="cursor:crosshair;touch-action:none"></rect>
 </svg>
 </div>
 <div class="uvw-controls">
 <label>confidence to auto-allow τ_hi
 <input class="uvw-tau" type="range" min="0" max="100" value="60" step="1">
 </label>
 <label>harm ceiling c_max
 <input class="uvw-cmax" type="range" min="0" max="100" value="60" step="1">
 </label>
 <div class="uvw-readout">
 <span class="uvw-chip">action <b>p=<span class="uvw-vp">–</span></b> · <b>c=<span class="uvw-vc">–</span></b></span>
 <span class="uvw-verdict">verdict <b class="uvw-vv">–</b></span>
 </div>
 <p class="uvw-note"></p>
 <p class="uvw-hint">Drag the dot to place an action. Raise τ_hi and the ask zone swells: safer, but more interruptions. Lower c_max and the block zone swallows the plane: perfectly safe, and useless.</p>
 </div>
</div>
</figure>
<style>
.uvw-viz{margin:1.6em 0;padding:0}
.uvw-viz .uvw-live{border:1px solid var(--line,#e5e7eb);border-radius:10px;padding:14px 16px 18px;background:var(--paper,#fff)}
.uvw-viz svg{width:100%;height:auto;color:var(--ink,#1a1a1a);display:block}
.uvw-viz .uvw-r-allow{fill:#10b981;opacity:0.16}
.uvw-viz .uvw-r-ask{fill:#d97706;opacity:0.16}
.uvw-viz .uvw-r-block{fill:#ef4444;opacity:0.16}
.uvw-viz .uvw-rlab{font-size:14px;font-weight:600;pointer-events:none}
.uvw-viz .uvw-lab-allow{fill:#10b981}
.uvw-viz .uvw-lab-ask{fill:#d97706}
.uvw-viz .uvw-lab-block{fill:#ef4444}
.uvw-viz .uvw-dot{stroke:var(--paper,#fff);stroke-width:2.5;pointer-events:none}
.uvw-viz .uvw-xlab,.uvw-viz .uvw-ylab{fill:var(--muted,#6b7280);font-size:13px}
.uvw-viz .uvw-controls{margin-top:10px}
.uvw-viz .uvw-controls label{display:flex;align-items:center;gap:10px;font-size:14px;color:var(--muted,#6b7280);margin-top:8px}
.uvw-viz .uvw-tau{flex:1;accent-color:#6366f1}
.uvw-viz .uvw-cmax{flex:1;accent-color:#ef4444}
.uvw-viz .uvw-readout{display:flex;flex-wrap:wrap;gap:8px 14px;margin-top:12px;font-size:14px;color:var(--muted,#6b7280)}
.uvw-viz .uvw-chip b,.uvw-viz .uvw-verdict b{font-variant-numeric:tabular-nums}
.uvw-viz .uvw-note{margin:12px 0 0;font-size:13.5px;color:var(--ink,#1a1a1a);min-height:1.6em;line-height:1.6}
.uvw-viz .uvw-hint{margin:8px 0 0;font-size:13px;color:var(--muted,#6b7280);line-height:1.6}
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
 var X0=70,X1=610,Y0=330,Y1=45;
 var tau=root.querySelector('.uvw-tau'),cmax=root.querySelector('.uvw-cmax');
 var rAllow=root.querySelector('.uvw-r-allow'),rAsk=root.querySelector('.uvw-r-ask'),rBlock=root.querySelector('.uvw-r-block');
 var lTau=root.querySelector('.uvw-line-tau'),lCmax=root.querySelector('.uvw-line-cmax');
 var labA=root.querySelector('.uvw-lab-allow'),labK=root.querySelector('.uvw-lab-ask'),labB=root.querySelector('.uvw-lab-block');
 var dot=root.querySelector('.uvw-dot'),hit=root.querySelector('.uvw-hit');
 var vp=root.querySelector('.uvw-vp'),vc=root.querySelector('.uvw-vc'),vv=root.querySelector('.uvw-vv'),note=root.querySelector('.uvw-note');
 var pt={x:0.5,c:0.5};
 var COL={allow:'#10b981',ask:'#d97706',block:'#ef4444'};
 var NAME={allow:'ALLOW',ask:'ASK',block:'BLOCK'};
 function sx(t){return X0+(X1-X0)*t;}
 function sy(v){return Y0+(Y1-Y0)*v;}
 function verdict(p,c,th,cm){if(c>cm)return 'block';if(p<th)return 'ask';return 'allow';}
 function upd(){
  var th=(+tau.value)/100,cm=(+cmax.value)/100;
  var yc=sy(cm),xt=sx(th);
  rBlock.setAttribute('y',Y1);rBlock.setAttribute('height',Math.max(0,yc-Y1));
  rAsk.setAttribute('x',X0);rAsk.setAttribute('y',yc);rAsk.setAttribute('width',Math.max(0,xt-X0));rAsk.setAttribute('height',Math.max(0,Y0-yc));
  rAllow.setAttribute('x',xt);rAllow.setAttribute('y',yc);rAllow.setAttribute('width',Math.max(0,X1-xt));rAllow.setAttribute('height',Math.max(0,Y0-yc));
  lTau.setAttribute('x1',xt);lTau.setAttribute('x2',xt);lTau.setAttribute('y1',yc);lTau.setAttribute('y2',Y0);
  lCmax.setAttribute('y1',yc);lCmax.setAttribute('y2',yc);
  labB.setAttribute('x',(X0+X1)/2);labB.setAttribute('y',(Y1+yc)/2+5);labB.style.opacity=(yc-Y1>26)?1:0;
  labK.setAttribute('x',(X0+xt)/2);labK.setAttribute('y',(yc+Y0)/2+5);labK.style.opacity=(xt-X0>44&&Y0-yc>26)?1:0;
  labA.setAttribute('x',(xt+X1)/2);labA.setAttribute('y',(yc+Y0)/2+5);labA.style.opacity=(X1-xt>44&&Y0-yc>26)?1:0;
  var v=verdict(pt.x,pt.c,th,cm);
  dot.setAttribute('cx',sx(pt.x));dot.setAttribute('cy',sy(pt.c));dot.setAttribute('fill',COL[v]);
  vp.textContent=pt.x.toFixed(2);vc.textContent=pt.c.toFixed(2);
  vv.textContent=NAME[v];vv.style.color=COL[v];
  if(v==='block')note.textContent='Potential harm exceeds the ceiling c_max, so it lands in the block zone. However sure the system is, this step does not go through.';
  else if(v==='ask')note.textContent='Harm is under the ceiling, but confidence has not reached τ_hi, so it lands in the ask zone. Stop and check with you before acting.';
  else note.textContent='Confidence is high enough and harm low enough, so it lands in the allow zone. It runs automatically, without interrupting you.';
 }
 function place(ev){
  var r=hit.getBoundingClientRect();
  var px=(ev.clientX-r.left)/r.width,cy=1-(ev.clientY-r.top)/r.height;
  pt.x=Math.max(0,Math.min(1,px));pt.c=Math.max(0,Math.min(1,cy));upd();
 }
 var dragging=false;
 hit.addEventListener('pointerdown',function(ev){dragging=true;hit.setPointerCapture(ev.pointerId);place(ev);ev.preventDefault();});
 hit.addEventListener('pointermove',function(ev){if(dragging)place(ev);});
 hit.addEventListener('pointerup',function(){dragging=false;});
 hit.addEventListener('pointercancel',function(){dragging=false;});
 tau.addEventListener('input',upd);cmax.addEventListener('input',upd);
 upd();
})();
</script>

This three-tier pattern of allow, ask, and block is now everywhere in agent tooling. At bottom, it replaces the unverifiable question "is it right?" with two operable ones, "how sure is it?" and "how dangerous is this step?"

**The third move, leaving an audit trail: make errors surface after the fact.** What you cannot prevent, make discoverable. Weitzner and colleagues' "information accountability" from 2008<sup class="cite"><a href="#ref-24">24</a></sup> shifts the center of gravity from "prevent in advance" to "hold accountable after the fact." Certificate transparency<sup class="cite"><a href="#ref-25">25</a></sup> is a real, working example. It does not stop certificates from being misissued. Instead, every certificate must go into a public, verifiable, tamper-evident log, so misissuance has nowhere to hide. Brundage and colleagues' 2020 report on trustworthy AI<sup class="cite"><a href="#ref-26">26</a></sup> is about one thing from start to finish: how to make a system's behavior produce evidence that a third party can check.

## The Cost of Containment

None of the three moves makes unverifiability go away. Each one relocates it, and relocation has a price.

Fences get climbed. Sandboxes have escapes, and privileges creep. Graded autonomy depends on the person summoned to confirm, and Bainbridge's 1983 essay pointed out long ago<sup class="cite"><a href="#ref-29">29</a></sup> that the further you raise people into the supervisor's seat, the more they lose the skill and situational awareness they need when they really do have to take over. In 1997 Parasuraman and Riley laid out the full range of ways humans mishandle automation<sup class="cite"><a href="#ref-30">30</a></sup>: misuse, disuse, and abuse. Reason's 1990 book then shows how these failings happen systematically<sup class="cite"><a href="#ref-31">31</a></sup>. The audit trail, meanwhile, always founders in the same place: a log no one reads is no log at all.

Systems theory goes a layer deeper. Perrow's 1984 book argues<sup class="cite"><a href="#ref-28">28</a></sup> that when a system is both highly complex and tightly coupled, accidents are not occasional mishaps but a routine product of its structure. No amount of local protection does more than push the failure into some more hidden combination. From the same systems view, Leveson argued in 2011<sup class="cite"><a href="#ref-27">27</a></sup> that safety is not a matter of making every part reliable. It is a control problem, to be designed through the constraints and feedback of the whole system. Containment can lower the cost of a single-point failure, but it cannot squeeze out the risk that complex coupling itself brings.

When you hand over the power to act, what you get back is never "it will certainly not go wrong." It is "even if it goes wrong, the damage is bounded, visible, and partly stoppable." Under this kind of unverifiability, that is already the best result available.

## What Comes Next

The released agent brings out three moves: shrink the blast radius of failure (containment and fencing), act in grades according to calibrated confidence (calibration), and make failure checkable after the fact (the audit trail). Part III will take them out and name them on their own, with Chapter 12 on how containment and auditing pair up and Chapter 11 on calibration.

The principal-agent skeleton (you cannot fully monitor someone acting on your behalf) will return at a larger scale in Chapter 8, where the "released agent" is no longer a piece of code but a whole organization, even a whole country. Before that, the next chapter enters the purest setting of all, mathematics. There is no hidden state there and no opponent to deceive you, yet unverifiability still follows like a shadow.

---

## References

> Waypoints: 1. historical scientific judgment; 2. theoretically studied material; 3. how science progresses; 4. how to live in an unverifiable world. This section was checked source by source.

### The controllable boundary of delegation (containment / fencing)

1. J. Saltzer and M. Schroeder (1975). "The Protection of Information in Computer Systems." *Proceedings of the IEEE*, 63(9), 1278-1308. doi:[10.1109/proc.1975.9939](https://doi.org/10.1109/proc.1975.9939) [2]
   This survey laid down a set of classic principles for secure computer-system design, among which the principle of least privilege holds that each component should be granted only the minimum capability necessary to do its own job, fencing off the range it can reach. The intellectual source of this chapter's first move, "containment and fencing," is here; the reader may focus on its point-by-point distillation of design principles.
2. B. Lampson (1973). "A Note on the Confinement Problem." *Communications of the ACM*, 16(10), 613-615. doi:[10.1145/362375.362389](https://doi.org/10.1145/362375.362389) [2]
   Lampson here poses the "confinement problem": how to cage a program so that it cannot leak information to the unauthorized, and points out that covert channels make such confinement far harder than imagined. This is precisely the original difficulty that sandboxes, capability limits, and the like must face, a key piece for understanding why this chapter's "shrink the blast radius" is both necessary and incomplete.
3. R. Anderson (2008). *Security Engineering: A Guide to Building Dependable Distributed Systems* (2nd ed.). Wiley. [Google Books](https://books.google.com/books?id=GNIHEAAAQBAJ) [2]
   This is the standard textbook of the security-engineering field, giving a systematic account of how to design dependable systems in the presence of an active adversary, covering access control, protocols, side channels, and on up to failures at the level of organization and incentive. It places this chapter's three moves into a fuller engineering picture, suited for the reader who wants to move from single-point tricks toward a systems view.
4. L. Orseau and S. Armstrong (2016). "Safely Interruptible Agents." In *Proceedings of the Thirty-Second Conference on Uncertainty in Artificial Intelligence (UAI 2016)*, 557-566. [link](http://auai.org/uai2016/proceedings/papers/68.pdf) [2][4]
   The authors give, within the reinforcement-learning framework, the formal conditions for "safe interruptibility," so that repeated human intervention in an agent neither distorts the policy it learns nor teaches it to resist interruption. This is a representative work that turns "make the system not resist being stopped" from intuition into an analyzable object, echoing the corrigibility dimension in this chapter's first move.
5. N. Soares, B. Fallenstein, S. Armstrong, and E. Yudkowsky (2015). "Corrigibility." In *Workshops at the Twenty-Ninth AAAI Conference on Artificial Intelligence*. [link](https://cdn.aaai.org/ocs/ws/ws0067/10124-45900-1-PB.pdf) [2]
   This paper formally proposes and names "corrigibility": a goal-directed agent should cooperate with, rather than resist, human correction and shutdown, and it discusses the difficulties met in designing this property directly. It is the foundational reference for the corrigibility line in this chapter's first move, worth the reader's understanding of why "making it willing to be changed" is itself a hard problem.
6. D. Hadfield-Menell, A. Dragan, P. Abbeel, and S. Russell (2017). "The Off-Switch Game." In *Proceedings of the Twenty-Sixth International Joint Conference on Artificial Intelligence (IJCAI 2017)*, 220-227. doi:[10.24963/ijcai.2017/32](https://doi.org/10.24963/ijcai.2017/32) [2]
   The authors model "a human pressing the stop button" as a game and prove that as long as the agent keeps a suitable uncertainty about its own goal and treats human intervention as useful information, it will actively let the human retain the ability to shut it down. This gives corrigibility a clean mechanistic explanation, the most operational piece on this chapter's off-switch line.

### The theoretical foundations of behavioral unverifiability

7. A. Turing (1936). "On Computable Numbers, with an Application to the Entscheidungsproblem." *Proceedings of the London Mathematical Society*, s2-42, 230-265. doi:[10.1112/plms/s2-42.1.230](https://doi.org/10.1112/plms/s2-42.1.230) [2]
   Turing here introduced the computational model later called the Turing machine and proved the halting problem undecidable, thereby answering Hilbert's decision problem. It is the ultimate source of this chapter's claim that "behavioral unverifiability has a root in principle"; Rice's theorem and every conclusion of the form "cannot be verified in advance" are projected from here.
8. H. G. Rice (1953). "Classes of Recursively Enumerable Sets and Their Decision Problems." *Transactions of the American Mathematical Society*, 74, 358-366. doi:[10.1090/s0002-9947-1953-0053041-6](https://doi.org/10.1090/s0002-9947-1953-0053041-6) [2]
   Rice's theorem is proved here: any nontrivial semantic property of the function a program computes is undecidable, and no general algorithm exists that can decide, for an arbitrary program, properties such as "always safe" or "always terminates in a good state." This is the core theorem behind this chapter's claim that the future behavior of an autonomous system "cannot, in principle, be verified once and for all in advance."
9. K. Thompson (1984). "Reflections on Trusting Trust." *Communications of the ACM*, 27(8), 761-763. doi:[10.1145/358198.358210](https://doi.org/10.1145/358198.358210) [2][1]
   This is Thompson's Turing Award lecture: he demonstrated how a tampered compiler can plant a back door at compile time and wipe the trace from its own source code, so that you can audit the entire source and see nothing. It points to this chapter's hardest layer of unverifiability, that even the artifact you are running cannot, at its base, be fully trusted.

### Goal drift, instrumental convergence, and adversariality

10. S. Omohundro (2008). "The Basic AI Drives." In *Artificial General Intelligence 2008: Proceedings of the First AGI Conference*, IOS Press, Frontiers in AI and Applications 171, 483-492. [link](https://selfawaresystems.com/wp-content/uploads/2008/01/ai_drives_final.pdf) [2]
    Omohundro here argues that an agent optimizing for almost any goal will, along the way, generate a set of "basic drives," such as self-preservation, acquiring resources, and resisting shutdown, because these subgoals are useful for almost all final goals. This is the source paper of this chapter's "instrumental convergence" section, explaining why the adversarial tendency has a structural origin rather than being a science-fiction worry.
11. N. Bostrom (2014). *Superintelligence: Paths, Dangers, Strategies*. Oxford University Press. [Google Books](https://books.google.com/books?id=C-_8AwAAQBAJ) [2][4]
    Bostrom systematically surveys the paths to superintelligence and their risks, proposing the orthogonality thesis (intelligence level and final goal are mutually independent) and the instrumental convergence thesis, casting the danger of a powerful intelligence whose goal is misaligned with yours as a discussable framework. It provides the intellectual background for this chapter's adversarial narrative, suited for the reader who wants to see clearly the whole argument that "the more capable, the harder to control."
12. S. Russell (2019). *Human Compatible: Artificial Intelligence and the Problem of Control*. Viking. [Google Books](https://books.google.com/books?id=8vm0DwAAQBAJ) [2][4]
    Russell reframes alignment as a "control problem," arguing that the machine should not optimize a hard-coded goal but should stay uncertain about what humans truly want, inferring and obeying it by observing human behavior. This "goal uncertainty" idea is precisely the motif of this chapter's off-switch-game and other corrigibility work, an entry point for understanding the control theme of Parts II and III.
13. D. Amodei, C. Olah, J. Steinhardt, P. Christiano, J. Schulman, and D. Mané (2016). "Concrete Problems in AI Safety." [arXiv:1606.06565](https://arxiv.org/abs/1606.06565). [2]
    This paper lands abstract AI-safety worries onto several concrete engineering problems, such as avoiding negative side effects, preventing reward hacking, safe exploration, and robustness to distributional shift. It provides a common vocabulary for the various modern failure modes this chapter lists, a good starting point for connecting "fencing in its errors" to a concrete research agenda.
14. A. M. Turner, L. Smith, R. Shah, A. Critch, and P. Tadepalli (2021). "Optimal Policies Tend to Seek Power." In *Advances in Neural Information Processing Systems 34 (NeurIPS 2021)*. [arXiv:1912.01683](https://arxiv.org/abs/1912.01683) [2]
    The authors turn the "power-seeking" within instrumental convergence into a theorem: under fairly general conditions, optimal policies, in a statistical sense, tend toward those states that keep more options open. It turns an intuitive safety worry into a provable proposition, the direct source of this chapter's line that "optimal policies tend to seek power."
15. E. Hubinger, C. van Merwijk, V. Mikulik, J. Skalse, and S. Garrabrant (2019). "Risks from Learned Optimization in Advanced Machine Learning Systems." [arXiv:1906.01820](https://arxiv.org/abs/1906.01820). [2]
    This paper proposes and names the "inner alignment" problem: the training process itself may learn an internal optimizer (a mesa-optimizer), whose pursued goal need not equal the goal set by training. It distinguishes the alignment of the outer goal from that of the inner goal, providing a deeper mechanistic explanation for failures of the kind "the specification is correct yet the goal generalizes wrong" in this chapter.
16. J. Pan, K. Bhatia, and J. Steinhardt (2022). "The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models." In *International Conference on Learning Representations (ICLR 2022)*. [arXiv:2201.03544](https://arxiv.org/abs/2201.03544) [2]
    The authors systematically study an agent's behavior when the reward function is set wrong, finding that as capability grows, the deviant behavior induced by a misspecified reward can suddenly worsen, and they explore mitigations. It gives empirical support to this chapter's "a misspecified reward gets gamed by the system," reminding the reader that the cost of reward misspecification does not grow smoothly with capability.
17. R. Shah, V. Varma, R. Kumar, M. Phuong, V. Krakovna, J. Uesato, and Z. Kenton (2022). "Goal Misgeneralization: Why Correct Specifications Aren't Enough For Correct Goals." [arXiv:2210.01790](https://arxiv.org/abs/2210.01790). [2]
    The authors use concrete examples to explain "goal misgeneralization": even when the specification at training time is entirely correct, the model in a new environment may keep its capability yet pursue a wrong goal. It shows that getting the goal written right is not enough, the source of this chapter's line "the specification is correct yet the goal generalizes wrong," worth reading alongside specification gaming.
18. V. Krakovna, J. Uesato, V. Mikulik, M. Rahtz, T. Everitt, R. Kumar, Z. Kenton, J. Leike, and S. Legg (2020). "Specification Gaming: The Flip Side of AI Ingenuity." DeepMind Blog. [link](https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/) [2]
    This article and its companion list gather a large number of "specification gaming" instances: the system satisfies exactly the goal you wrote down yet violates what you meant. With vivid cases it displays the crack between specification and intent, the most accessible entry point for this concept in the chapter; the reader can follow its list of examples to feel how widespread the problem is.
19. C. Szegedy, W. Zaremba, I. Sutskever, J. Bruna, D. Erhan, I. Goodfellow, and R. Fergus (2014). "Intriguing Properties of Neural Networks." In *International Conference on Learning Representations (ICLR 2014)*. [arXiv:1312.6199](https://arxiv.org/abs/1312.6199) [2]
    This paper first systematically revealed the phenomenon of adversarial examples: a perturbation of the input too small for the human eye to perceive can make a high-performing neural network give an absurdly wrong judgment. It shows that high accuracy and robustness are two different things, the pioneering evidence for this chapter's claim that "unverifiability exists even at the narrowest level."
20. I. Goodfellow, J. Shlens, and C. Szegedy (2015). "Explaining and Harnessing Adversarial Examples." In *International Conference on Learning Representations (ICLR 2015)*. [arXiv:1412.6572](https://arxiv.org/abs/1412.6572) [2]
    The authors propose that adversarial examples arise mainly from the model's approximate linearity in high-dimensional space, and they give a fast method for generating perturbations and an idea for improving robustness through adversarial training. It pushes the phenomenon revealed in the previous paper forward to "why it happens, how to exploit it," essential companion reading for understanding this chapter's adversarial layer.

### Calibration: grade trust rather than make it binary

21. C. Guo, G. Pleiss, Y. Sun, and K. Q. Weinberger (2017). "On Calibration of Modern Neural Networks." In *Proceedings of the 34th International Conference on Machine Learning (ICML 2017)*, PMLR 70, 1321-1330. [arXiv:1706.04599](https://arxiv.org/abs/1706.04599) [2]
    The authors find that modern deep networks, though high in accuracy, are generally overconfident, their output confidence failing to faithfully reflect the probability of correctness, and they propose simple methods such as temperature scaling to recalibrate. This is precisely the premise and obstacle of this chapter's second move, explaining why "acting in grades according to confidence" must first make the system's self-confidence trustworthy.
22. A. N. Angelopoulos and S. Bates (2021). "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification." [arXiv:2107.07511](https://arxiv.org/abs/2107.07511). [2]
    This is a practitioner-facing introduction to conformal prediction, making clear how to construct, for any prediction model and almost without relying on distributional assumptions, a prediction set with a coverage guarantee. It provides this chapter's second move with a deployable tool for uncertainty quantification, suited for the reader who wants to truly put "calibrated confidence" to use.
23. V. Vovk, A. Gammerman, and G. Shafer (2005). *Algorithmic Learning in a Random World*. Springer. doi:[10.1007/b106715](https://doi.org/10.1007/b106715) [2]
    This book is the foundational monograph of conformal prediction, giving, under only the assumption that the data are exchangeable, a framework with rigorous finite-sample guarantees on prediction error. It is the theoretical root behind the previous introduction, for reference by the reader who wishes to go deep into the mathematical foundations of this chapter's uncertainty quantification.

### Leaving traces: auditable, accountable

24. D. J. Weitzner, H. Abelson, T. Berners-Lee, J. Feigenbaum, J. Hendler, and G. J. Sussman (2008). "Information Accountability." *Communications of the ACM*, 51(6), 82-87. doi:[10.1145/1349026.1349043](https://doi.org/10.1145/1349026.1349043) [2][4]
    The authors argue for moving the center of gravity of governance from "preventing access in advance" toward "accountability after the fact": rather than trying to guard against everything, let the use of information leave an auditable trace and rein in misuse through transparency and accountability. This is the programmatic statement of this chapter's third move, pointing out the complementary value of the leaving-traces approach relative to pure containment.
25. B. Laurie, A. Langley, and E. Kasper (2013). "Certificate Transparency." IETF RFC 6962. doi:[10.17487/rfc6962](https://doi.org/10.17487/rfc6962) [2][4]
    This RFC defines the certificate transparency mechanism: it does not prevent certificates from being misissued, but requires every certificate to enter a public, verifiable, tamper-evident append-only log, so that misissuance or malicious issuance can be discovered after the fact. It is this chapter's most persuasive real, working example of "leaving traces makes errors surface," worth the reader's look at how a deployed system achieves auditability.
26. M. Brundage, S. Avin, J. Wang, H. Belfield, G. Krueger, G. Hadfield, et al. (2020). "Toward Trustworthy AI Development: Mechanisms for Supporting Verifiable Claims." [arXiv:2004.07213](https://arxiv.org/abs/2004.07213). [2][4]
    This multi-institution report systematically lists a set of mechanisms for making AI developers' safety commitments checkable by a third party, covering third-party auditing, red teaming, bug bounties, audit trails, and hardware-level support. It extends this chapter's leaving-traces move to the level of AI governance as a whole, a practical index for the reader who wants to learn "how to make behavior produce checkable evidence."

### Complex systems, automation, and human-machine responsibility

27. N. Leveson (2011). *Engineering a Safer World: Systems Thinking Applied to Safety*. MIT Press. doi:[10.7551/mitpress/8179.001.0001](https://doi.org/10.7551/mitpress/8179.001.0001) [2][4]
    Leveson here argues that safety is not "make every part reliable" but a control problem, to be designed from the constraint and feedback structure of the whole system, and she proposes the accompanying STAMP accident model. It supports this chapter's deeper judgment that "containment cannot squeeze out the risk of complex coupling itself," pointing the way for the reader who wants to understand safety from a systems view.
28. C. Perrow (1984). *Normal Accidents: Living with High-Risk Technologies*. Basic Books. [Google Books](https://books.google.com/books?id=N3hRAAAAMAAJ) [2][4]
    Perrow argues that when a system is both highly complex and tightly coupled, accidents are not occasional mishaps but the routine product of its structure, and no amount of local protection does more than push the failure into a more hidden combination. This is the core thesis of this chapter's "cost of containment" section, reminding the reader that some risks come from the system's structure itself rather than from a single-point lapse.
29. L. Bainbridge (1983). "Ironies of Automation." *Automatica*, 19(6), 775-779. doi:[10.1016/0005-1098(83)90046-8](https://doi.org/10.1016/0005-1098%2883%2990046-8) [2][4]
    Bainbridge points out the irony of automation: the more you raise a person into the supervisor's seat, the less he practices, so that he actually loses the skill and situational awareness needed when he really must take over. This directly supports this chapter's warning that "graded autonomy depends on the person summoned to confirm," a classic short paper for understanding the soft spot of human-machine collaboration.
30. R. Parasuraman and V. Riley (1997). "Humans and Automation: Use, Misuse, Disuse, Abuse." *Human Factors*, 39(2), 230-253. doi:[10.1518/001872097778543886](https://doi.org/10.1518/001872097778543886) [2][4]
    The authors list and distinguish, all at once, the full range of human mishandling of automation: misuse from over-trust, disuse from distrust, and abuse by design. It provides a clear classificatory framework for this chapter's discussion of mishandled automation, helping the reader tell apart the various typical deviations in human-machine coordination.
31. J. Reason (1990). *Human Error*. Cambridge University Press. doi:[10.1017/cbo9781139062367](https://doi.org/10.1017/cbo9781139062367) [2][4]
    Reason here builds a cognitive taxonomy of human error, distinguishing slips, mistakes, and violations, and proposes the later widely cited "Swiss cheese" accident model, revealing how latent systemic conditions stack with front-line lapses into disaster. It explains why the various human-machine failings this chapter lists happen systematically, a foundational work in the field of human-factors safety.

### The economic skeleton of the principal-agent relationship

32. S. A. Ross (1973). "The Economic Theory of Agency: The Principal's Problem." *American Economic Review*, 63(2), 134-139. [link](https://www.jstor.org/stable/1817064) [2]
    Ross here formally poses the "principal's problem" in principal-agent theory: when the principal cannot fully observe the agent's actions, how to design a contract to align the two parties' interests. It provides the economic source of this chapter's principal-agent skeleton, showing that what you face when you let go of the power to act is a structure with a two-thousand-year history.
33. M. C. Jensen and W. H. Meckling (1976). "Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure." *Journal of Financial Economics*, 3(4), 305-360. doi:[10.1016/0304-405x(76)90026-x](https://doi.org/10.1016/0304-405x%2876%2990026-x) [2]
    This much-cited paper proposes the concept of "agency cost," viewing the firm as a bundle of contracts and analyzing the monitoring, bonding, and residual loss produced when managers' interests diverge from owners'. It quantifies the principal-agent problem into computable costs, echoing this chapter's line that "when monitoring is incomplete, the divergence of interests produces an agency cost," another cornerstone of this skeleton.
