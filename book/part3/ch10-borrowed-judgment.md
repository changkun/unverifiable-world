# 第 10 章　借来的判断

> **论点**：当自身缺乏验证能力时，可以从外部引入这种能力：或者在决策回路中安置一个可信的判断者（神谕，oracle）；或者召集许多相互独立、各自并不可靠的判断者，信任他们之间的一致（冗余，redundancy／共识，consensus）。

上一章的两种对策，仍是依靠自身的资源来缩小未知。然而有时所缺乏的并不是信息，而是判断力：面对眼前的问题，行动者无法独立作出可靠的判决。本章的两种对策于是转向外部，从别处借来判断。借用的方式有两种：其一是引入一个值得信赖的判断者（神谕）；其二是召集许多彼此并不信任的判断者，转而信任他们之间的一致（冗余）。

## 神谕入回路：引进一个判断者

第一种对策的一般形式是：在缺乏验证能力的那个决策点上，插入一个外部的判断者，由它作出决策者自身无法作出的判决。

这一对策最朴素的形式，是第 5 章讨论过的人在回路（human in the loop），此外还有专家会诊，以及把疑难问题提交上级裁决的做法。然而，它最深刻的形态，却隐藏在两个看似毫不相干的领域之中。

其一是交互式定理证明（interactive theorem proving）。从德布鲁因 1970 年的 AUTOMATH<sup class="cite"><a href="#ref-1">1</a></sup>，到爱丁堡 LCF（戈登、米尔纳与沃兹沃思 1979<sup class="cite"><a href="#ref-2">2</a></sup>），再到今天的 Coq（贝尔托与卡斯特朗 2004<sup class="cite"><a href="#ref-3">3</a></sup>），这些系统采用的都是同一种分工。人提供机器无法给出的证明思路，即那种灵光一现的洞见（神谕）；机器则一丝不苟地核对每一步推理（证书检查，certificate checking）。神谕负责「找」，机器负责「验」，这恰好对应第 7 章讨论过的那种不对称：寻找困难，验证容易。

其二则更令人惊讶：复杂性理论中的交互式证明（interactive proof）。设想一个计算能力很弱的验证者，面对一个能力强大却不可信的证明者：对于一个验证者自己无法计算的问题，它如何才能获得可靠的答案？戈德瓦塞尔、米卡利与拉科夫 1989 年<sup class="cite"><a href="#ref-6">6</a></sup>以及巴拜 1985 年<sup class="cite"><a href="#ref-7">7</a></sup>给出的回答是：反复盘问，辅以随机挑战。验证者提出连它自己也无法预知的随机问题；证明者倘若说谎，迟早会在某一次挑战中暴露。沙米尔 1992 年<sup class="cite"><a href="#ref-15">15</a></sup>证明了一个惊人的结果，即 $\mathrm{IP}=\mathrm{PSPACE}$：仅凭这种「盘问一个不可信的神谕」的方法，弱小的验证者便能可靠地裁决一类极其庞大的问题。布卢姆与坎南 1995 年<sup class="cite"><a href="#ref-17">17</a></sup>的「会检查自身工作的程序」，以及戈德瓦塞尔等人 2015 年<sup class="cite"><a href="#ref-19">19</a></sup>的「给麻瓜的交互式证明」（interactive proofs for muggles），也都属于这一脉络。这是「借来的判断」在数学上最纯粹的形态：即便神谕不可信，只要盘问得法，仍然能够从它那里得到可靠的答案。

贯穿这些例子的共同观念是：引入一个外部判断者，以获得单凭自身所不具备的可靠性。这一对策的典型失效方式也同样直接：神谕不可靠，或者有所偏倚。请来的裁判自己就可能判错；而「谁来验证神谕」这一问题，又会把人引入无穷回归。

## 冗余：从许多不可靠里合成可靠

第二种对策取相反的方向：不引入一个可信的判断者，而是召集许多并不可信的判断者，转而信任他们之间的一致。

这一对策的理论有两块基石。冯·诺依曼 1956 年<sup class="cite"><a href="#ref-4">4</a></sup>证明，以各自都会出错的元件为材料，通过层层叠加冗余，可以构造出可靠性任意高的计算。孔多塞 1785 年<sup class="cite"><a href="#ref-5">5</a></sup>的陪审团定理（Condorcet's jury theorem）则给出了这一机制的算术依据：若每个判断者都略优于随机猜测（正确率 $p>\tfrac12$），并且彼此独立，那么随着人数的增加，多数票正确的概率将趋于必然，

$$P_N\to 1\quad(N\to\infty).$$

这一对策的应用遍及许多领域。在分布式系统中，它表现为拜占庭容错（Byzantine fault tolerance）。皮斯、肖斯塔克与兰波特 1980 年<sup class="cite"><a href="#ref-8">8</a></sup>以及兰波特等人 1982 年<sup class="cite"><a href="#ref-9">9</a></sup>提出的拜占庭将军问题（Byzantine generals problem），所探讨的是：当部分节点可能蓄意作恶（对抗）时，系统如何达成共识，即各节点如何就同一结果取得一致。经典的门槛是，节点数须满足 $n\ge 3f+1$，才能容忍 $f$ 个叛徒。在工程上，卡斯特罗与利斯科夫 1999 年<sup class="cite"><a href="#ref-11">11</a></sup>的 PBFT 把它落实为实用系统；在理论上，费舍尔、林奇与帕特森 1985 年<sup class="cite"><a href="#ref-10">10</a></sup>的不可能性定理则划出了它的边界。

在机器学习中，与之对应的是集成（ensemble）。汉森与萨拉蒙 1990 年<sup class="cite"><a href="#ref-20">20</a></sup>和迪特里希 2000 年<sup class="cite"><a href="#ref-22">22</a></sup>所讨论的集成方法，以及布雷曼 2001 年<sup class="cite"><a href="#ref-23">23</a></sup>提出的随机森林（random forest），做法都是让一群弱模型投票，其结果胜过单个强模型。在人类群体中，它表现为「群体的智慧」（wisdom of crowds；索罗维基 2004<sup class="cite"><a href="#ref-25">25</a></sup>）。1906 年，高尔顿在一个乡村集市上记录了约八百位村民对一头公牛体重的独立估计。没有一个人猜中，但所有估计的平均值为 1197 磅，而公牛的实际重量是 1198 磅：就整体而言，群体的判断几乎分毫不差。洪与佩奇 2004 年<sup class="cite"><a href="#ref-24">24</a></sup>更进一步证明，在适当的条件下，一群多样的普通解题者能够胜过一群能力出众的解题者。至于科学中的同行评审与重复实验（第 3 章）、工程中的 RAID 与法定人数机制、医疗中的第二诊疗意见，也都是这一对策的具体形式。

然而，这一对策依赖于一个值得仔细审视的关键前提：独立性。只有当各个判断的失误互不相关时，冗余才能成立。将许多相互独立的估计加以平均，方差才会随人数的增加而下降，

$$\mathrm{Var}(\bar X)=\frac{\sigma^2}{N};$$

而一旦这些判断之间存在正相关 $\rho$，方差便不再趋于零，而是停留在一个由相关性决定的下限上，本书称之为相关性地板，

$$\mathrm{Var}(\bar X)=\rho\,\sigma^2+\frac{(1-\rho)\,\sigma^2}{N}\ \xrightarrow{N\to\infty}\ \rho\,\sigma^2.$$

![冗余的相关性地板：一旦存在相关，增加判断者也无法越过](../figures/f10-redundancy-floor.svg)

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
    if(r<0.02)note.textContent='相关系数几乎为零：增加判断者仍能持续降低方差，冗余确实在发挥作用。';
    else note.textContent='存在隐藏的相关性，可靠性被限制在地板 ρ 上：无论增加多少判断者，等效的独立判断者数目都只能逼近 1/ρ ≈ '+(1/r).toFixed(1)+'，而无法越过。';
  }
  rhoS.addEventListener('input',upd);nS.addEventListener('input',upd);upd();
})();
</script>

相关性由此击穿了冗余最核心的承诺：无论增加多少判断者，都无法越过相关性设下的这道地板。这并非空谈。在奈特与莱韦森 1986 年<sup class="cite"><a href="#ref-13">13</a></sup>的著名实验中，许多程序员依据同一份规格说明，各自独立地编写程序。按照预期，他们的错误应当互不相关；实际结果却是，他们在相同的地方出错，因为人在面对同一个难点时会犯同样的错误。对此，埃克哈特与李 1985 年<sup class="cite"><a href="#ref-12">12</a></sup>早已从理论上作出了预言。群体思维（groupthink）、来源相同且带有缺陷的训练数据、共模故障（common-mode failure），都是这道地板的具体表现。这便是冗余的典型失效方式：以为独立，其实相关。

## 两种对策的关联

把两种对策放在一起考察：前者引入一个单一而昂贵的神谕，后者汇合众多廉价而独立的判断；二者借来的，都是行动者单凭自身所不具备的判断力。它们共同的作用，是补足所缺的验证能力。二者的失效方式也恰好相对：单一的神谕可能出错，众多的判断则可能暗中相关。

数学史上有一段插曲，把这两种对策连同上一章的证书联系在了一起。阿佩尔与哈肯 1977 年<sup class="cite"><a href="#ref-26">26</a></sup>对四色定理（four color theorem）的证明依赖计算机穷举，因而饱受争议：接受这一证明，无异于要求数学界信任一个神谕。后来，贡蒂耶 2008 年<sup class="cite"><a href="#ref-27">27</a></sup>以机器可以核对的形式证明（formal proof）重做了这一证明，黑尔斯团队<sup class="cite"><a href="#ref-28">28</a></sup>也以同样的方式处理了开普勒猜想。两者都把「信任神谕」转化为「核对证书」。麦肯齐<sup class="cite"><a href="#ref-29">29</a></sup>在《机械化证明》中所追踪的，就是这种信任如何在人、机器与社会过程之间转移。德米洛等人<sup class="cite"><a href="#ref-14">14</a></sup>则主张，证明在本质上是一种社会过程；归根结底，这一主张是把数学的可信性安放在人类判断的冗余之上。

不过，有一点需要看清：到此为止，本章与上一章的对策（「压缩未知」与「借来的判断」）所追求的仍是同一样东西，即对象之真。它们仍然试图知道一件事究竟是对是错。下一章的两种对策则做了一件更为彻底的事：它们不再强求这种真。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实。

1. N. G. de Bruijn (1970). 「The mathematical language AUTOMATH, its usage, and some of its extensions」. 收入《Symposium on Automatic Demonstration》. Springer (Lecture Notes in Mathematics 125), pp. 29-61. doi:[10.1007/bfb0060623](https://doi.org/10.1007/bfb0060623) [②]
   德布鲁因介绍了 AUTOMATH，史上最早能让整篇数学被机器逐步核对的形式语言之一，由人写出证明、机器验证其无误。它是本章「神谕入回路」最早的工程化样本：人提供思路，机器只负责一丝不苟地检查，读者可由此看清「找」与「验」分工的源头。
2. M. Gordon, R. Milner, C. Wadsworth (1979).《Edinburgh LCF: A Mechanized Logic of Computation》. Springer (Lecture Notes in Computer Science 78). doi:[10.1007/3-540-09724-4](https://doi.org/10.1007/3-540-09724-4) [②]
   这本书提出了 LCF 这套交互式证明系统，其设计影响深远：用一个受信任的小内核担保每一步推理的可靠，证明策略再多也无法绕过它。它为本章关于「证书检查」的论述提供了经典范式，读者可看到「可信核对者」如何被收缩成一个尽量小、尽量可靠的部件。
3. Y. Bertot, P. Castéran (2004).《Interactive Theorem Proving and Program Development. Coq'Art: The Calculus of Inductive Constructions》. Springer (Texts in Theoretical Computer Science, EATCS Series). doi:[10.1007/978-3-662-07964-5](https://doi.org/10.1007/978-3-662-07964-5) [②]
   这是 Coq 证明助手的权威教程，系统讲解如何在归纳构造演算之上交互地构造并机器核对证明。它把前两条所代表的传统带到当代实践，是本章后文四色定理、开普勒猜想等形式化工作的工具基础，想动手理解「人给思路、机器验每步」的读者可由此入门。
4. J. von Neumann (1956). 「Probabilistic Logics and the Synthesis of Reliable Organisms from Unreliable Components」. 收入 C. E. Shannon, J. McCarthy 编《Automata Studies》(Annals of Mathematics Studies 34). Princeton University Press, pp. 43-98. doi:[10.1515/9781400882618-003](https://doi.org/10.1515/9781400882618-003) [②]
   冯·诺依曼在此证明，可以用本身会出错的元件，通过堆叠冗余与多数表决，组装出任意逼近可靠的计算。这是本章「冗余」这一对策的奠基石之一，为「从许多不可靠里合成可靠」提供了最早的严格论证，读者应读其对冗余如何压低错误率的核心思路。
5. Marquis de Condorcet (1785).《Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix》. Imprimerie Royale, Paris. [Google Books](https://books.google.com/books?id=Mdb00-cUlXwC) [②④]
   孔多塞在这部关于投票的著作里给出了著名的陪审团定理：若每个判断者都略优于瞎猜且彼此独立，多数票正确的概率会随人数增长趋于必然。它为本章冗余这一对策提供了算术骨架，也预埋了它的命门，读者应留意定理对「独立」这一前提的依赖。
6. S. Goldwasser, S. Micali, C. Rackoff (1989). 「The Knowledge Complexity of Interactive Proof Systems」. SIAM Journal on Computing, 18(1), pp. 186-208. doi:[10.1137/0218012](https://doi.org/10.1137/0218012) [②]
   这篇论文开创了交互式证明与零知识证明的理论框架：一个算力有限的验证者，靠反复盘问加随机挑战，能从一个不可信的证明者那里榨出可靠的判决。它是本章「盘问不可信神谕」最纯的数学源头，读者应读它如何用随机性逼出真话。
7. L. Babai (1985). 「Trading Group Theory for Randomness」. 收入《Proceedings of the 17th Annual ACM Symposium on Theory of Computing (STOC)》, pp. 421-429. doi:[10.1145/22145.22192](https://doi.org/10.1145/22145.22192) [②]
   巴拜在此独立提出了 Arthur-Merlin 这类带随机性的交互式证明，与上一条几乎同时奠定了同一片理论疆域。它强化了本章的核心观念：随机挑战是弱验证者制服强而不可信证明者的关键武器，读者可与上一条对照阅读其互补的视角。
8. M. Pease, R. Shostak, L. Lamport (1980). 「Reaching Agreement in the Presence of Faults」. Journal of the ACM, 27(2), pp. 228-234. doi:[10.1145/322186.322188](https://doi.org/10.1145/322186.322188) [②]
   这篇论文最早严格刻画了在部分节点可能任意作恶时如何达成共识，给出了著名门槛：要容忍 $f$ 个叛徒，节点数须满足 $n\ge 3f+1$。它是本章冗余这一对策在分布式系统里的对抗性版本之源头，读者应读这个门槛背后的不可能性论证。
9. L. Lamport, R. Shostak, M. Pease (1982). 「The Byzantine Generals Problem」. ACM Transactions on Programming Languages and Systems, 4(3), pp. 382-401. doi:[10.1145/357172.357176](https://doi.org/10.1145/357172.357176) [②]
   这篇论文用「拜占庭将军」这个著名比喻把上一条的结果讲成了一则寓言，从此「拜占庭容错」成为对抗性共识的通用名字。它是本章用许多互不信任的判断者求一致这一思路的标志性文本，读者可读它如何把抽象门槛包装成直觉清晰的故事。
10. M. J. Fischer, N. A. Lynch, M. S. Paterson (1985). 「Impossibility of Distributed Consensus with One Faulty Process」. Journal of the ACM, 32(2), pp. 374-382. doi:[10.1145/3149.214121](https://doi.org/10.1145/3149.214121) [②]
   这篇著名的 FLP 不可能性定理证明，在完全异步的系统里，哪怕只有一个进程可能崩溃，也不存在保证终止的确定性共识算法。它为本章冗余这一对策划出了边界，读者应读它如何说明共识并非无条件可得，从而理解后续实用系统为何要靠额外假设来绕开它。
11. M. Castro, B. Liskov (1999). 「Practical Byzantine Fault Tolerance」. 收入《Proceedings of the 3rd USENIX Symposium on Operating Systems Design and Implementation (OSDI)》, pp. 173-186. [链接](https://www.usenix.org/conference/osdi-99/practical-byzantine-fault-tolerance) [②]
   这篇论文提出的 PBFT 算法，第一次把拜占庭容错从理论做成在真实异步网络里跑得动、性能可接受的系统。它是本章冗余这一对策从纸面落到工程的关键一步，读者可读它如何在保住 $n\ge 3f+1$ 门槛的同时把开销压到实用范围，也理解后世区块链共识的直接前身。
12. D. E. Eckhardt, L. D. Lee (1985). 「A Theoretical Basis for the Analysis of Multiversion Software Subject to Coincident Errors」. IEEE Transactions on Software Engineering, SE-11(12), pp. 1511-1517. doi:[10.1109/tse.1985.231895](https://doi.org/10.1109/tse.1985.231895) [②]
   这篇论文从理论上指出，多版本软件即便由不同人独立开发，其错误也未必独立：面对同一处难点，不同版本会倾向于一起出错，使冗余的收益远低于独立假设的预期。它为本章「相关性地板」给出了早于实验的理论预言，读者应读它如何刻画共因错误。
13. J. C. Knight, N. G. Leveson (1986). 「An Experimental Evaluation of the Assumption of Independence in Multiversion Programming」. IEEE Transactions on Software Engineering, SE-12(1), pp. 96-109. doi:[10.1109/tse.1986.6312924](https://doi.org/10.1109/tse.1986.6312924) [②]
   这是那个著名的实验：让许多程序员独立地照同一规格编写程序，本指望错误互不相干，结果发现他们在相同的难点上一起栽倒，独立假设被经验否定。它为上一条的理论预言提供了实证，是本章「以为独立、其实相关」这一败法最有说服力的例证。
14. R. A. De Millo, R. J. Lipton, A. J. Perlis (1979). 「Social Processes and Proofs of Theorems and Programs」. Communications of the ACM, 22(5), pp. 271-280. doi:[10.1145/359104.359106](https://doi.org/10.1145/359104.359106) [③④]
   这篇有名又有争议的论文主张，数学证明之所以可信，靠的不是形式推导的机械正确，而是数学共同体反复检验、传播、采信的社会过程，并据此质疑程序形式验证的前景。它支撑本章的观点：可信归根结底安放在人类判断的冗余之上，读者应读它关于证明本质上是社会过程的论证。
15. A. Shamir (1992). 「IP = PSPACE」. Journal of the ACM, 39(4), pp. 869-877. doi:[10.1145/146585.146609](https://doi.org/10.1145/146585.146609) [②]
   沙米尔证明了交互式证明的威力之惊人：单靠盘问一个不可信证明者，弱验证者能可靠裁决整个 PSPACE 这一极庞大的问题类，即 $\mathrm{IP}=\mathrm{PSPACE}$。它是本章「借来的判断」最有力的数学注脚，读者应读它如何界定「会聪明盘问神谕」所能达到的上限。
16. C. Lund, L. Fortnow, H. Karloff, N. Nisan (1992). 「Algebraic Methods for Interactive Proof Systems」. Journal of the ACM, 39(4), pp. 859-868. doi:[10.1145/146585.146605](https://doi.org/10.1145/146585.146605) [②]
   这篇论文引入了把布尔公式算术化、再用多项式做检查的代数方法，正是它的技术铺垫直接通向了上一条 $\mathrm{IP}=\mathrm{PSPACE}$ 的证明。它揭示了「聪明盘问」的具体机理：把验证问题转译成可随机抽查的代数恒等式，可作本章相关脉络的延伸阅读，读者可循此深入这套手法。
17. M. Blum, S. Kannan (1995). 「Designing Programs That Check Their Work」. Journal of the ACM, 42(1), pp. 269-291. doi:[10.1145/200836.200880](https://doi.org/10.1145/200836.200880) [②]
   这篇论文提出了「程序检查器」的思想：让程序在给出结果时附带一个独立、廉价的核对程序，验证本次输出是否正确，而无需信任程序本身。它把交互式证明的精神带到日常计算，对本章而言，是「不信任产出者、只核对其产出」这一思路的范本，读者应读其检查器的构造。
18. S. Arora, C. Lund, R. Motwani, M. Sudan, M. Szegedy (1998). 「Proof Verification and the Hardness of Approximation Problems」. Journal of the ACM, 45(3), pp. 501-555. doi:[10.1145/278298.278306](https://doi.org/10.1145/278298.278306) [②]
   这是著名的 PCP 定理的核心论文之一：任何证明都能改写成一种特殊格式，使验证者只需随机抽查其中常数个比特，就能以高置信度判断其真伪。它把「抽查就够」推到极致，是「弱验证者如何高效核对庞大证明」这一脉的理论顶点，可作本章的延伸阅读，读者应读其概率可检证明的惊人结论。
19. S. Goldwasser, Y. T. Kalai, G. N. Rothblum (2015). 「Delegating Computation: Interactive Proofs for Muggles」. Journal of the ACM, 62(4), Article 27. doi:[10.1145/2699436](https://doi.org/10.1145/2699436) [②④]
   这篇论文让交互式证明真正服务于「凡人」：一个算力有限的用户把计算外包给强大但不可信的服务器，再用远小于自己重算的代价核对结果是否正确。它是本章思想走向云计算时代的落点，读者应读它如何把「为弱者代理计算并可验证」做成现实可行的协议。
20. L. K. Hansen, P. Salamon (1990). 「Neural Network Ensembles」. IEEE Transactions on Pattern Analysis and Machine Intelligence, 12(10), pp. 993-1001. doi:[10.1109/34.58871](https://doi.org/10.1109/34.58871) [②]
   这篇论文较早地表明，把多个独立训练的神经网络组合起来投票，其整体准确率可显著高于任何单个网络。它是本章冗余这一对策在机器学习里的开端，读者应读它如何把「多数表决降低错误」从逻辑电路搬到学习模型，并再次落到对成员误差去相关的依赖。
21. A. Krogh, J. Vedelsby (1995). 「Neural Network Ensembles, Cross Validation, and Active Learning」. 收入《Advances in Neural Information Processing Systems 7》. MIT Press, pp. 231-238. [链接](https://proceedings.neurips.cc/paper/1994/hash/b8c37e33defde51cf91e1e03e51657da-Abstract.html) [②]
   这篇论文给出了集成误差的经典分解：集成的整体误差等于成员的平均误差减去成员之间的分歧度。它给出了机器学习版的「相关性地板」精确公式，可与本章相互印证，读者应读它如何用数学说明，成员越是多样、越是各错各的，集成才越值钱。
22. T. G. Dietterich (2000). 「Ensemble Methods in Machine Learning」. 收入《Multiple Classifier Systems (MCS 2000)》. Springer (Lecture Notes in Computer Science 1857), pp. 1-15. doi:[10.1007/3-540-45014-9\_1](https://doi.org/10.1007/3-540-45014-9_1) [②]
   这是一篇影响广泛的综述，梳理了集成方法为何有效，并从统计、计算与表示三个角度给出解释。它是读者纵览本章冗余这一对策在机器学习里全貌的便捷入口，把分散的投票、装袋、提升等手法收拢在一个框架下理解。
23. L. Breiman (2001). 「Random Forests」. Machine Learning, 45(1), pp. 5-32. doi:[10.1023/a:1010933404324](https://doi.org/10.1023/a:1010933404324) [②]
   布雷曼提出的随机森林，靠对样本与特征的双重随机化来培育一群彼此去相关的决策树，再投票合成强大而稳健的预测器。它是冗余这一对策最成功的实战范例之一，对本章的意义在于：它的全部威力恰恰来自刻意制造的独立性，读者可读它如何主动压低成员间的相关。
24. L. Hong, S. E. Page (2004). 「Groups of Diverse Problem Solvers Can Outperform Groups of High-Ability Problem Solvers」. Proceedings of the National Academy of Sciences, 101(46), pp. 16385-16389. doi:[10.1073/pnas.0403723101](https://doi.org/10.1073/pnas.0403723101) [②③④]
   洪与佩奇借一个形式化模型论证：在合适条件下，由多样的普通解题者组成的群体，能胜过一群同质的高手，因为多样性带来的视角差异本身就是一种资源。它把本章「独立与多样才是冗余之本」的直觉推广到人类群体，读者应读其「多样性胜过能力」的论点与边界。
25. J. Surowiecki (2004).《The Wisdom of Crowds: Why the Many Are Smarter Than the Few and How Collective Wisdom Shapes Business, Economies, Societies, and Nations》. Doubleday. [Google Books](https://books.google.com/books?id=hHUsHOHqVzEC) [③④]
   索罗维基这本广为流传的书论证：在多样、独立、分散且有恰当聚合机制的条件下，群体的集体判断往往胜过专家个人，他也反复强调一旦丧失独立、陷入趋同，群体就会变蠢。它把本章冗余这一对策带到日常与社会层面，读者应读它对「群体智慧成立的前提」的反复申明。
26. K. Appel, W. Haken (1977). 「Every Planar Map Is Four Colorable. Part I: Discharging」. Illinois Journal of Mathematics, 21(3), pp. 429-490. doi:[10.1215/ijm/1256049011](https://doi.org/10.1215/ijm/1256049011) [①③]
   这是四色定理的证明，史上第一个本质上依赖计算机穷举大量情形的重大数学证明，也因此引发关于「能否信任一个人手无法逐一复核的机器结论」的长久争论。它对本章而言，是「信任神谕」与其代价的标志性案例，读者应读这场争论如何逼出对机器可核对证书的需求。
27. G. Gonthier (2008). 「Formal Proof: The Four-Color Theorem」. Notices of the American Mathematical Society, 55(11), pp. 1382-1393. [链接](https://www.ams.org/notices/200811/tx081101382p.pdf) [②③]
   贡蒂耶用 Coq 把四色定理重做成一份完全形式化、可被机器逐步核对的证明，从而把上一条那种「请信任计算机」的处境，转化为「核对一份证书」。它对本章是关键的对照点，读者应读它如何示范：把不可信的神谕产出，降格为可独立验证的证书，争议便随之消解。
28. T. Hales 等 (2017). 「A Formal Proof of the Kepler Conjecture」. Forum of Mathematics, Pi, 5, 文章号 e2. doi:[10.1017/fmp.2017.1](https://doi.org/10.1017/fmp.2017.1) [②③]
   黑尔斯团队历经多年，用形式化证明系统把饱受争议的开普勒猜想证明彻底机器核对了一遍，了结了同行评审都难以完全担保的疑虑。它与上一条同属一个脉络，对本章的意义在于再次印证：当证明大到人力难核时，把信任从神谕转移到可核对的证书，是恢复确信的出路。
29. D. MacKenzie (2001).《Mechanizing Proof: Computing, Risk, and Trust》. MIT Press. doi:[10.7551/mitpress/4529.001.0001](https://doi.org/10.7551/mitpress/4529.001.0001) [①③④]
   麦肯齐这部社会学史著作追踪了计算机证明与形式验证的兴起，考察「证明」与「确信」如何在数学家、机器与社会过程之间被反复定义与转移。它为本章提供了贯穿性的视角，把神谕、证书、冗余都安放进一个关于信任如何被建立与让渡的更大叙事，读者应读它对「机械化证明改变了我们信任什么」的考察。
