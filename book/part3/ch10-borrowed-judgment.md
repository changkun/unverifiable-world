# 第 10 章　借来的判断

> **论点**：自己缺乏验证能力，就从外部引进。要么在回路里放一个可信的判断者（神谕，oracle）；要么用许多互相独立的不可靠判断者，信任他们的一致（冗余，redundancy／共识，consensus）。

上一对招还是在自己身上想办法，缩小未知。可有时你缺的不是信息，而是判断力：面对眼前这件事，你根本下不了一个可靠的判决。这一对招的应对是：不再从自己身上找，去别处把判断借来。借法有两种。一种是引进一个你信得过的判断者（神谕）；另一种是召集许多互不信任的判断者，信任他们的一致（冗余）。

## 神谕入回路：引进一个判断者

第一招的纯粹形式：在你缺乏验证能力的那个决策点上，插入一个外部判断者，由它给出你给不出的判决。

最朴素的版本，是第 5 章讲过的人在回路（human in the loop），是专家会诊，是把疑难问题上交。但这一招最深刻的形态，藏在两个看起来毫不相干的地方。

一处是交互式定理证明（interactive theorem proving）。从德布鲁因 1970 年的 AUTOMATH<sup class="cite"><a href="#ref-1">1</a></sup>，到爱丁堡 LCF（戈登、米尔纳、沃兹沃思 1979<sup class="cite"><a href="#ref-2">2</a></sup>），再到今天的 Coq（贝尔托与卡斯特朗 2004<sup class="cite"><a href="#ref-3">3</a></sup>），用的都是同一种分工。人提供灵光一闪、机器给不出的证明思路（神谕）；机器一丝不苟地核对每一步（证书检查，certificate checking）。神谕负责「找」，机器负责「验」，正好对上第 7 章讲过的那种不对称：找起来难，验起来容易。

另一处更让人吃惊：复杂性理论里的交互式证明（interactive proof）。设想一个算力很弱的验证者，面对一个强大却不可信的证明者。一个它自己根本算不出来的问题，它怎样才能问出可靠的答案？戈德瓦塞尔、米卡利与拉科夫 1989 年<sup class="cite"><a href="#ref-6">6</a></sup>、巴拜 1985 年<sup class="cite"><a href="#ref-7">7</a></sup>给出的回答是：反复盘问，加上随机挑战。验证者抛出连它自己都无法预知的随机问题；证明者如果在撒谎，迟早会在某个挑战上露馅。沙米尔 1992 年<sup class="cite"><a href="#ref-15">15</a></sup>那个惊人的结果 $\mathrm{IP}=\mathrm{PSPACE}$ 表明，单靠这种「盘问一个不可信的神谕」的办法，弱小的验证者就能可靠地裁决一类极其庞大的问题。布卢姆与坎南 1995 年<sup class="cite"><a href="#ref-17">17</a></sup>的「会检查自己工作的程序」，戈德瓦塞尔等人 2015 年<sup class="cite"><a href="#ref-19">19</a></sup>的「给麻瓜的交互式证明」（interactive proofs for muggles），都属于同一脉。这是「借来的判断」最纯粹的数学形态：哪怕神谕不可信，只要你会聪明地盘问它，照样能从它那里榨出可靠的答案。

把这些串起来的观念是：引进一个外部判断者，造出一种你单独不具备的可靠。它的典型失效方式也很直白：神谕不可靠，或者有偏。你请来的裁判，自己就可能判错；而「谁来验证神谕」这个问题，会把你拖进无穷回归。

## 冗余：从许多不可靠里合成可靠

第二招换了个方向：不引进一个可信的判断者，而是召集许多不可信的，信任他们的一致。

它的理论有两块基石。冯·诺依曼 1956 年<sup class="cite"><a href="#ref-4">4</a></sup>证明，用各自都会出错的元件，靠层层叠加冗余，可以组装出要多可靠就有多可靠的计算。孔多塞 1785 年<sup class="cite"><a href="#ref-5">5</a></sup>的陪审团定理（Condorcet's jury theorem）则给出了其中的算术：如果每个判断者都比瞎猜略好一点（正确率 $p>\tfrac12$），而且彼此独立，那么随着人数增加，多数票正确的概率会趋于必然，

$$P_N\to 1\quad(N\to\infty).$$

这一招在各个领域里铺得极开。在分布式系统里，它是拜占庭容错（Byzantine fault tolerance）。皮斯、肖斯塔克与兰波特 1980 年<sup class="cite"><a href="#ref-8">8</a></sup>，以及兰波特等人 1982 年<sup class="cite"><a href="#ref-9">9</a></sup>提出的拜占庭将军问题（Byzantine generals problem），问的是在部分节点可能作恶（对抗）的情况下如何达成共识。经典门槛是：节点数须满足 $n\ge 3f+1$，才能容忍 $f$ 个叛徒。卡斯特罗与利斯科夫 1999 年<sup class="cite"><a href="#ref-11">11</a></sup>的 PBFT 把它做进了实用系统；费舍尔、林奇与帕特森 1985 年<sup class="cite"><a href="#ref-10">10</a></sup>的不可能性定理，则划出了它的边界。

在机器学习里，它是集成（ensemble）。汉森与萨拉蒙 1990 年<sup class="cite"><a href="#ref-20">20</a></sup>和迪特里希 2000 年<sup class="cite"><a href="#ref-22">22</a></sup>的集成方法，布雷曼 2001 年<sup class="cite"><a href="#ref-23">23</a></sup>的随机森林（random forest），都是让一群弱模型投票，结果胜过单个强模型。在人群中，它是「群体的智慧」（wisdom of crowds）（索罗维基 2004<sup class="cite"><a href="#ref-25">25</a></sup>）。1906 年，高尔顿在一个乡村集市上，记下了约八百位村民对一头公牛体重的独立竞猜。没有一个人猜准，可所有估计的平均值是 1197 磅，而牛的真实重量是 1198 磅：整个群体合起来，几乎分毫不差。洪与佩奇 2004 年<sup class="cite"><a href="#ref-24">24</a></sup>更进一步证明，在合适的条件下，一群多样的普通解题者能胜过一群高手。在科学里，它是同行评审和重复实验（第 3 章）；在工程里，它是 RAID 和法定人数；在医疗里，它是第二诊疗意见。

但这一招有一个关键前提，值得细看：独立。只有失败互不相关，冗余才成立。把许多相互独立的估计平均起来，方差才会随人数下降，

$$\mathrm{Var}(\bar X)=\frac{\sigma^2}{N};$$

可一旦这些判断之间存在正相关 $\rho$，方差就不再趋于零，而是卡在一个地板上，

$$\mathrm{Var}(\bar X)=\rho\,\sigma^2+\frac{(1-\rho)\,\sigma^2}{N}\ \xrightarrow{N\to\infty}\ \rho\,\sigma^2.$$

![冗余的相关性地板：相关一旦存在，堆人也跨不过去](../figures/f10-redundancy-floor.svg)

<figure class="uvw-viz" data-static="f10-redundancy-floor" role="group" aria-label="冗余的相关性地板交互图">
<div class="uvw-live" hidden>
  <div class="uvw-plot">
    <svg viewBox="0 0 640 380" preserveAspectRatio="xMidYMid meet" aria-hidden="true">
      <g class="uvw-axes" fill="none" stroke="currentColor" stroke-width="1.2" opacity="0.35">
        <line x1="70" y1="330" x2="610" y2="330"></line>
        <line x1="70" y1="45" x2="70" y2="330"></line>
      </g>
      <line class="uvw-floor" x1="70" x2="610" stroke-width="1.6" stroke-dasharray="6 5"></line>
      <text class="uvw-floorlab" x="600" text-anchor="end">地板 ρ</text>
      <path class="uvw-curve" fill="none" stroke-width="2.6"></path>
      <line class="uvw-cursor" y1="45" y2="330" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 4" opacity="0.55"></line>
      <circle class="uvw-dot" r="5"></circle>
      <text class="uvw-ylab-top" x="64" y="49" text-anchor="end">1</text>
      <text class="uvw-ylab-bot" x="64" y="334" text-anchor="end">0</text>
      <text class="uvw-ylab" x="24" y="190" text-anchor="middle" transform="rotate(-90 24 190)">归一化方差 V</text>
      <text class="uvw-xlab" x="340" y="366" text-anchor="middle">判断者数量 N →</text>
    </svg>
  </div>
  <div class="uvw-controls">
    <label>相关系数 ρ
      <input class="uvw-rho" type="range" min="0" max="1" value="0.1" step="0.01">
      <b class="uvw-v-rho">0.10</b>
    </label>
    <label>判断者数量 N
      <input class="uvw-n" type="range" min="1" max="200" value="20" step="1">
      <b class="uvw-v-n">20</b>
    </label>
    <div class="uvw-readout">
      <span class="uvw-chip uvw-chip-var">归一化方差 V <b class="uvw-v-var">–</b></span>
      <span class="uvw-chip uvw-chip-eff">等效独立判断者 <b class="uvw-v-eff">–</b></span>
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
    floorLab.setAttribute('y',(fy-6).toFixed(1));floorLab.textContent='地板 ρ = '+r.toFixed(2);
    var v=V(n,r);
    dot.setAttribute('cx',sx(n));dot.setAttribute('cy',sy(v));
    cur.setAttribute('x1',sx(n));cur.setAttribute('x2',sx(n));
    var eff=n/(1+(n-1)*r);
    vVar.textContent=v.toFixed(3);
    vEff.textContent=eff.toFixed(1);
    if(r<0.02)note.textContent='相关系数几乎为零，多加判断者仍在持续压低方差，冗余还在实实在在地起作用。';
    else note.textContent='存在隐藏的相关性，可靠性被钉在地板 ρ 上：无论再堆多少判断者，等效独立判断者都逼近 1/ρ ≈ '+(1/r).toFixed(1)+'，跨不过去。';
  }
  rhoS.addEventListener('input',upd);nS.addEventListener('input',upd);upd();
})();
</script>

相关会击穿冗余最核心的承诺：判断者堆得再多，也越不过相关性设下的这道地板。这不是空谈。在奈特与莱韦森 1986 年<sup class="cite"><a href="#ref-13">13</a></sup>那个著名的实验里，许多程序员按同一份规格各自独立编写程序。本来指望他们的错误互不相干，结果却发现，他们栽在了同样的地方，因为人面对同一个难点，会犯同样的错（埃克哈特与李 1985 年<sup class="cite"><a href="#ref-12">12</a></sup>早就从理论上预言过）。群体思维（groupthink），同出一源、带着缺陷的训练数据，共模故障（common-mode failure），都是这道地板的现身。这就是冗余的典型失效方式：以为独立，其实相关。

## 两招的交汇

把两招放在一起看。一个引进单一而昂贵的神谕，一个把众多廉价的独立判断合在一起；借来的，都是你单独不具备的判断力。它们共同做的事，是替自己补上缺失的验证能力。它们的失效方式也正好相对：单一的神谕可能出错，众多的判断可能暗中相关。

数学里有一段插曲，把这一对招，连同上一章的证书，都串到了一起。阿佩尔与哈肯 1977 年<sup class="cite"><a href="#ref-26">26</a></sup>对四色定理（four color theorem）的证明，因为依赖计算机穷举而饱受争议：这等于要数学界去信任一个神谕。后来，贡蒂耶 2008 年<sup class="cite"><a href="#ref-27">27</a></sup>用机器可以核对的形式证明（formal proof）把它重做了一遍，黑尔斯团队<sup class="cite"><a href="#ref-28">28</a></sup>对开普勒猜想也如法炮制。两者都把「信任神谕」变成了「核对证书」。麦肯齐<sup class="cite"><a href="#ref-29">29</a></sup>在《机械化证明》里追踪的，就是这种信任如何在人、机器与社会过程之间转移。德米洛等人<sup class="cite"><a href="#ref-14">14</a></sup>主张证明本质上是一种社会过程；说到底，这就是把数学的可信安放在人类判断的冗余之上。

不过有一点要看清：到这里为止，前两对招（压缩未知与借来判断）追求的仍是同一样东西，即对象的真。它们仍然想知道这件事到底对不对。下一对招做了一件更彻底的事：它不再强求那个真。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实。

1. N. G. de Bruijn (1970). 「The mathematical language AUTOMATH, its usage, and some of its extensions」. 收入《Symposium on Automatic Demonstration》. Springer (Lecture Notes in Mathematics 125), pp. 29-61. [②]
   德布鲁因介绍了 AUTOMATH，史上最早能让整篇数学被机器逐步核对的形式语言之一，由人写出证明、机器验证其无误。它是本章「神谕入回路」最早的工程化样本：人提供思路，机器只负责一丝不苟地检查，读者可由此看清「找」与「验」分工的源头。
2. M. Gordon, R. Milner, C. Wadsworth (1979).《Edinburgh LCF: A Mechanized Logic of Computation》. Springer (Lecture Notes in Computer Science 78). [②]
   这本书提出了 LCF 这套交互式证明系统，其设计影响深远：用一个受信任的小内核担保每一步推理的可靠，证明策略再多也无法绕过它。它为本章关于「证书检查」的论述提供了经典范式，读者可看到「可信核对者」如何被收缩成一个尽量小、尽量可靠的部件。
3. Y. Bertot, P. Castéran (2004).《Interactive Theorem Proving and Program Development. Coq'Art: The Calculus of Inductive Constructions》. Springer (Texts in Theoretical Computer Science, EATCS Series). [②]
   这是 Coq 证明助手的权威教程，系统讲解如何在归纳构造演算之上交互地构造并机器核对证明。它把前两条所代表的传统带到当代实践，是本章后文四色定理、开普勒猜想等形式化工作的工具基础，想动手理解「人给思路、机器验每步」的读者可由此入门。
4. J. von Neumann (1956). 「Probabilistic Logics and the Synthesis of Reliable Organisms from Unreliable Components」. 收入 C. E. Shannon, J. McCarthy 编《Automata Studies》(Annals of Mathematics Studies 34). Princeton University Press, pp. 43-98. [②]
   冯·诺依曼在此证明，可以用本身会出错的元件，通过堆叠冗余与多数表决，组装出任意逼近可靠的计算。这是本章「冗余」一招的奠基石之一，为「从许多不可靠里合成可靠」提供了最早的严格论证，读者应读其对冗余如何压低错误率的核心思路。
5. Marquis de Condorcet (1785).《Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix》. Imprimerie Royale, Paris. [②④]
   孔多塞在这部关于投票的著作里给出了著名的陪审团定理：若每个判断者都略优于瞎猜且彼此独立，多数票正确的概率会随人数增长趋于必然。它为本章冗余一招提供了算术骨架，也预埋了它的命门，读者应留意定理对「独立」这一前提的依赖。
6. S. Goldwasser, S. Micali, C. Rackoff (1989). 「The Knowledge Complexity of Interactive Proof Systems」. SIAM Journal on Computing, 18(1), pp. 186-208. [②]
   这篇论文开创了交互式证明与零知识证明的理论框架：一个算力有限的验证者，靠反复盘问加随机挑战，能从一个不可信的证明者那里榨出可靠的判决。它是本章「盘问不可信神谕」最纯的数学源头，读者应读它如何用随机性逼出真话。
7. L. Babai (1985). 「Trading Group Theory for Randomness」. 收入《Proceedings of the 17th Annual ACM Symposium on Theory of Computing (STOC)》, pp. 421-429. [②]
   巴拜在此独立提出了 Arthur-Merlin 这类带随机性的交互式证明，与上一条几乎同时奠定了同一片理论疆域。它强化了本章的核心观念：随机挑战是弱验证者制服强而不可信证明者的关键武器，读者可与上一条对照阅读其互补的视角。
8. M. Pease, R. Shostak, L. Lamport (1980). 「Reaching Agreement in the Presence of Faults」. Journal of the ACM, 27(2), pp. 228-234. [②]
   这篇论文最早严格刻画了在部分节点可能任意作恶时如何达成共识，给出了著名门槛：要容忍 $f$ 个叛徒，节点数须满足 $n\ge 3f+1$。它是本章冗余一招在分布式系统里的对抗性版本之源头，读者应读这个门槛背后的不可能性论证。
9. L. Lamport, R. Shostak, M. Pease (1982). 「The Byzantine Generals Problem」. ACM Transactions on Programming Languages and Systems, 4(3), pp. 382-401. [②]
   这篇论文用「拜占庭将军」这个著名比喻把上一条的结果讲成了一则寓言，从此「拜占庭容错」成为对抗性共识的通用名字。它是本章用许多互不信任的判断者求一致这一思路的标志性文本，读者可读它如何把抽象门槛包装成直觉清晰的故事。
10. M. J. Fischer, N. A. Lynch, M. S. Paterson (1985). 「Impossibility of Distributed Consensus with One Faulty Process」. Journal of the ACM, 32(2), pp. 374-382. [②]
   这篇著名的 FLP 不可能性定理证明，在完全异步的系统里，哪怕只有一个进程可能崩溃，也不存在保证终止的确定性共识算法。它为本章冗余一招划出了边界，读者应读它如何说明共识并非无条件可得，从而理解后续实用系统为何要靠额外假设来绕开它。
11. M. Castro, B. Liskov (1999). 「Practical Byzantine Fault Tolerance」. 收入《Proceedings of the 3rd USENIX Symposium on Operating Systems Design and Implementation (OSDI)》, pp. 173-186. [②]
   这篇论文提出的 PBFT 算法，第一次把拜占庭容错从理论做成在真实异步网络里跑得动、性能可接受的系统。它是本章冗余一招从纸面落到工程的关键一步，读者可读它如何在保住 $n\ge 3f+1$ 门槛的同时把开销压到实用范围，也理解后世区块链共识的直接前身。
12. D. E. Eckhardt, L. D. Lee (1985). 「A Theoretical Basis for the Analysis of Multiversion Software Subject to Coincident Errors」. IEEE Transactions on Software Engineering, SE-11(12), pp. 1511-1517. [②]
   这篇论文从理论上指出，多版本软件即便由不同人独立开发，其错误也未必独立：面对同一处难点，不同版本会倾向于一起出错，使冗余的收益远低于独立假设的预期。它为本章「相关性地板」给出了早于实验的理论预言，读者应读它如何刻画共因错误。
13. J. C. Knight, N. G. Leveson (1986). 「An Experimental Evaluation of the Assumption of Independence in Multiversion Programming」. IEEE Transactions on Software Engineering, SE-12(1), pp. 96-109. [②]
   这是那个著名的实验：让许多程序员独立地照同一规格编写程序，本指望错误互不相干，结果发现他们在相同的难点上一起栽倒，独立假设被经验否定。它为上一条的理论预言提供了实证，是本章「以为独立、其实相关」这一败法最有说服力的例证。
14. R. A. De Millo, R. J. Lipton, A. J. Perlis (1979). 「Social Processes and Proofs of Theorems and Programs」. Communications of the ACM, 22(5), pp. 271-280. [③④]
   这篇有名又有争议的论文主张，数学证明之所以可信，靠的不是形式推导的机械正确，而是数学共同体反复检验、传播、采信的社会过程，并据此质疑程序形式验证的前景。它支撑本章的观点：可信归根结底安放在人类判断的冗余之上，读者应读它关于证明本质上是社会过程的论证。
15. A. Shamir (1992). 「IP = PSPACE」. Journal of the ACM, 39(4), pp. 869-877. [②]
   沙米尔证明了交互式证明的威力之惊人：单靠盘问一个不可信证明者，弱验证者能可靠裁决整个 PSPACE 这一极庞大的问题类，即 $\mathrm{IP}=\mathrm{PSPACE}$。它是本章「借来的判断」最有力的数学注脚，读者应读它如何界定「会聪明盘问神谕」所能达到的上限。
16. C. Lund, L. Fortnow, H. Karloff, N. Nisan (1992). 「Algebraic Methods for Interactive Proof Systems」. Journal of the ACM, 39(4), pp. 859-868. [②]
   这篇论文引入了把布尔公式算术化、再用多项式做检查的代数方法，正是它的技术铺垫直接通向了上一条 $\mathrm{IP}=\mathrm{PSPACE}$ 的证明。它揭示了「聪明盘问」的具体机理：把验证问题转译成可随机抽查的代数恒等式，可作本章相关脉络的延伸阅读，读者可循此深入这套手法。
17. M. Blum, S. Kannan (1995). 「Designing Programs That Check Their Work」. Journal of the ACM, 42(1), pp. 269-291. [②]
   这篇论文提出了「程序检查器」的思想：让程序在给出结果时附带一个独立、廉价的核对程序，验证本次输出是否正确，而无需信任程序本身。它把交互式证明的精神带到日常计算，对本章而言，是「不信任产出者、只核对其产出」这一思路的范本，读者应读其检查器的构造。
18. S. Arora, C. Lund, R. Motwani, M. Sudan, M. Szegedy (1998). 「Proof Verification and the Hardness of Approximation Problems」. Journal of the ACM, 45(3), pp. 501-555. [②]
   这是著名的 PCP 定理的核心论文之一：任何证明都能改写成一种特殊格式，使验证者只需随机抽查其中常数个比特，就能以高置信度判断其真伪。它把「抽查就够」推到极致，是「弱验证者如何高效核对庞大证明」这一脉的理论顶点，可作本章的延伸阅读，读者应读其概率可检证明的惊人结论。
19. S. Goldwasser, Y. T. Kalai, G. N. Rothblum (2015). 「Delegating Computation: Interactive Proofs for Muggles」. Journal of the ACM, 62(4), Article 27. [②④]
   这篇论文让交互式证明真正服务于「凡人」：一个算力有限的用户把计算外包给强大但不可信的服务器，再用远小于自己重算的代价核对结果是否正确。它是本章思想走向云计算时代的落点，读者应读它如何把「为弱者代理计算并可验证」做成现实可行的协议。
20. L. K. Hansen, P. Salamon (1990). 「Neural Network Ensembles」. IEEE Transactions on Pattern Analysis and Machine Intelligence, 12(10), pp. 993-1001. [②]
   这篇论文较早地表明，把多个独立训练的神经网络组合起来投票，其整体准确率可显著高于任何单个网络。它是本章冗余一招在机器学习里的开端，读者应读它如何把「多数表决降低错误」从逻辑电路搬到学习模型，并再次落到对成员误差去相关的依赖。
21. A. Krogh, J. Vedelsby (1995). 「Neural Network Ensembles, Cross Validation, and Active Learning」. 收入《Advances in Neural Information Processing Systems 7》. MIT Press, pp. 231-238. [②]
   这篇论文给出了集成误差的经典分解：集成的整体误差等于成员的平均误差减去成员之间的分歧度。它给出了机器学习版的「相关性地板」精确公式，可与本章相互印证，读者应读它如何用数学说明，成员越是多样、越是各错各的，集成才越值钱。
22. T. G. Dietterich (2000). 「Ensemble Methods in Machine Learning」. 收入《Multiple Classifier Systems (MCS 2000)》. Springer (Lecture Notes in Computer Science 1857), pp. 1-15. [②]
   这是一篇影响广泛的综述，梳理了集成方法为何有效，并从统计、计算与表示三个角度给出解释。它是读者纵览本章冗余一招在机器学习里全貌的便捷入口，把分散的投票、装袋、提升等手法收拢在一个框架下理解。
23. L. Breiman (2001). 「Random Forests」. Machine Learning, 45(1), pp. 5-32. [②]
   布雷曼提出的随机森林，靠对样本与特征的双重随机化来培育一群彼此去相关的决策树，再投票合成强大而稳健的预测器。它是冗余一招最成功的实战范例之一，对本章的意义在于：它的全部威力恰恰来自刻意制造的独立性，读者可读它如何主动压低成员间的相关。
24. L. Hong, S. E. Page (2004). 「Groups of Diverse Problem Solvers Can Outperform Groups of High-Ability Problem Solvers」. Proceedings of the National Academy of Sciences, 101(46), pp. 16385-16389. [②③④]
   洪与佩奇借一个形式化模型论证：在合适条件下，由多样的普通解题者组成的群体，能胜过一群同质的高手，因为多样性带来的视角差异本身就是一种资源。它把本章「独立与多样才是冗余之本」的直觉推广到人类群体，读者应读其「多样性胜过能力」的论点与边界。
25. J. Surowiecki (2004).《The Wisdom of Crowds: Why the Many Are Smarter Than the Few and How Collective Wisdom Shapes Business, Economies, Societies, and Nations》. Doubleday. [③④]
   索罗维基这本广为流传的书论证：在多样、独立、分散且有恰当聚合机制的条件下，群体的集体判断往往胜过专家个人，他也反复强调一旦丧失独立、陷入趋同，群体就会变蠢。它把本章冗余一招带到日常与社会层面，读者应读它对「群体智慧成立的前提」的反复申明。
26. K. Appel, W. Haken (1977). 「Every Planar Map Is Four Colorable. Part I: Discharging」. Illinois Journal of Mathematics, 21(3), pp. 429-490. [①③]
   这是四色定理的证明，史上第一个本质上依赖计算机穷举大量情形的重大数学证明，也因此引发关于「能否信任一个人手无法逐一复核的机器结论」的长久争论。它对本章而言，是「信任神谕」与其代价的标志性案例，读者应读这场争论如何逼出对机器可核对证书的需求。
27. G. Gonthier (2008). 「Formal Proof: The Four-Color Theorem」. Notices of the American Mathematical Society, 55(11), pp. 1382-1393. [②③]
   贡蒂耶用 Coq 把四色定理重做成一份完全形式化、可被机器逐步核对的证明，从而把上一条那种「请信任计算机」的处境，转化为「核对一份证书」。它对本章是关键的对照点，读者应读它如何示范：把不可信的神谕产出，降格为可独立验证的证书，争议便随之消解。
28. T. Hales 等 (2017). 「A Formal Proof of the Kepler Conjecture」. Forum of Mathematics, Pi, 5, 文章号 e2. [②③]
   黑尔斯团队历经多年，用形式化证明系统把饱受争议的开普勒猜想证明彻底机器核对了一遍，了结了同行评审都难以完全担保的疑虑。它与上一条同属一个脉络，对本章的意义在于再次印证：当证明大到人力难核时，把信任从神谕转移到可核对的证书，是恢复确信的出路。
29. D. MacKenzie (2001).《Mechanizing Proof: Computing, Risk, and Trust》. MIT Press. [①③④]
   麦肯齐这部社会学史著作追踪了计算机证明与形式验证的兴起，考察「证明」与「确信」如何在数学家、机器与社会过程之间被反复定义与转移。它为本章提供了贯穿性的视角，把神谕、证书、冗余都安放进一个关于信任如何被建立与让渡的更大叙事，读者应读它对「机械化证明改变了我们信任什么」的考察。
