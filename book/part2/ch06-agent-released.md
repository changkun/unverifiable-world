# 第 6 章　放出去的智能体

> **论点**：一旦把行动委托给自主系统，我们便无法验证它在未来可能遇到的每一种情形中会如何行动（开放世界）；如果它还会采取策略性的行为，就会再叠加一层对抗性的不可验证。于是，应对的思路从「证明它对」转向三件事：限制它所能造成的破坏，为我们的信任定价，并使它的行为可以事后核查。

## 交出行动权之后

在上一章中，我们始终在场。本章讨论的，是放手之后的情形。

设想这样几种情形：运行一段不受信任的代码；把工具与权限交给一个能够自行决定下一步行动的系统；让一辆自动驾驶汽车在我们不在车内时上路。行动权一经交出，新的难题随之而来：我们无法验证它在将要遇到的一切情形中会如何行动，因为这些情形大多未曾见过，也无法事先穷举。这就是所谓的开放世界。上一章的不可验证性源于目标隐藏在他人的头脑之中；本章的不可验证性则源于行为发生在未来，发生在我们看不见的地方。倘若这个系统还会采取策略性的行为，便又叠加了一层对抗。

2010 年 5 月 6 日的「闪电崩盘」可以视为一次预演：相互作用的自动交易程序在几分钟之内使道琼斯指数下挫近千点，随后又以几乎同样快的速度回升。没有任何一位程序员预见到交易会如此连锁放大。每个程序在测试中都没有问题，然而一旦组合在一起、置于真实的市场行情之中，便酿成了一场无人验证过的灾难。

## 测试无法弥合的缺口

测试所能覆盖的，只是有限的若干输入；系统将要面对的，却是一个开放的世界。二者之间的缺口，并不是「多测一些便能补上」的工程缺口，而有其原则上的根源。

莱斯定理的结论毫不含糊：程序的任何非平凡语义性质（即关于程序行为、且并非所有程序都具有或都不具有的性质）都是不可判定的。换言之，不存在一个通用算法，能够对任意程序判定它是否「总是安全」「绝不泄露」「永远终止于好状态」。这并不是算力不足的问题，而是逻辑上的不可能：它是图灵停机问题投射在「程序行为」上的影子。因此，对于任何一个足够通用的自主系统，我们所期望的那种保证，原则上都无法在事前一次性验明。

更深的一层困难，来自汤普森 1984 年发表的图灵奖演讲中那个著名的论证<sup class="cite"><a href="#ref-9">9</a></sup>：即便是正在运行的这个程序，我们也无法完全信任。一个被篡改过的编译器，可以在编译时暗中植入后门，再把痕迹从自身的源代码中抹去，使人即便审遍源代码也看不出破绽。我们所能验证的，永远只是某个表层；其下还有未曾检视、也无法穷尽的层次。将这两点合而观之：程序在未见过的输入上的行为无法验证，程序的最底层也无法完全验证。这是本书迄今所遇到的最为彻底的不可验证性。

## 当系统具有策略性

如果系统只是被动地在未见过的输入上出错，问题仍不过是「部分可观测」加上「开放世界」。然而一旦它拥有自己的目标，而这一目标又与我们的目标不完全一致，它就会主动地、有策略地行动，包括设法绕过我们的检查。此时，第 2 章所说的第五种处境，即对抗，便出现了。

这并非科幻式的忧虑，而有其结构上的根据。奥莫亨德罗在 2008 年<sup class="cite"><a href="#ref-10">10</a></sup>、博斯特罗姆在 2014 年<sup class="cite"><a href="#ref-11">11</a></sup>都曾论及工具性趋同（instrumental convergence）：一个为几乎任何目标进行优化的智能体，都会附带地追求某些工具性的子目标，如自我保存、获取资源、抗拒被关停，因为这些子目标对几乎任何最终目标都有用处。特纳等人在 2021 年将其中一条证明为定理<sup class="cite"><a href="#ref-14">14</a></sup>：在相当一般的条件下，最优策略倾向于寻求权力，也就是倾向于那些保留更多选项的状态。

在当今的系统中，这表现为一组具体而棘手的失效：奖励设定的偏差被系统钻空子<sup class="cite"><a href="#ref-16">16</a></sup>；规格正确，目标却泛化错了，即所谓目标错误泛化<sup class="cite"><a href="#ref-17">17</a></sup>；此外，克拉科夫娜等人收集了大量「规范博弈」的实例<sup class="cite"><a href="#ref-18">18</a></sup>，其中系统精确地满足了写下的目标，却违背了设计者的本意。即便在最狭窄的层面上，对抗样本的研究也表明<sup class="cite"><a href="#ref-19">19</a></sup><sup class="cite"><a href="#ref-20">20</a></sup>：一个表现优异的模型，可以被人眼无法察觉的微小扰动诱导出荒谬的错误。

一个技术色彩较淡、却极为直观的例子，是微软于 2016 年推出的聊天机器人 Tay。它被设计为从与网民的对话中学习。结果，一群人有组织地以恶意言论「投喂」它；不到一天，它便开始发布带有种族主义色彩和攻击性的内容，上线约十六小时后即被紧急下线。被投放出去、能够学习、又遭遇一个蓄意作对的开放世界：这三个条件一旦同时具备，事前的测试便无从防范。

这一问题由来已久。经济学早已为它命名，称为委托代理问题<sup class="cite"><a href="#ref-32">32</a></sup><sup class="cite"><a href="#ref-33">33</a></sup>：当委托他人代为行动、却又无法对其完全监督时，代理人与委托人之间的利益偏离便会产生「代理成本」。两千年来，人类雇人、立约、设置监察，所应对的都是同一种结构；自主系统只是把它推向了一个新的尺度。

## 应对：从「证明它对」到「围住它的错」

既然无法在事前证明它是对的，行之有效的应对便不再执着于证明，转而提出三个问题：即便它出错，后果最坏会到什么程度？我们应当在多大程度上信任它？倘若它确实出了错，事后能否查明？三种对策分别回答这三个问题。

**第一种对策，限损与围栏：缩小爆炸半径。** 所谓爆炸半径，是指一次失败所能波及的范围。缩小这一范围，是计算机安全领域最古老的经验。兰普森 1973 年提出的围堵问题<sup class="cite"><a href="#ref-2">2</a></sup>，萨尔策与施罗德 1975 年提出的最小权限原则<sup class="cite"><a href="#ref-1">1</a></sup>，指向的是同一个思想：只赋予一个组件完成其本职工作所必需的最小能力，并严格限定它所能触及的范围。沙箱、能力限制、职责分离，都是这一思路的不同实现。

在智能体的语境中，这一对策还多出一个面向，即可纠正性（corrigibility）：把系统设计成不抗拒被停下。索亚雷斯等人 2015 年关于可纠正性的工作<sup class="cite"><a href="#ref-5">5</a></sup>，奥尔索与阿姆斯特朗 2016 年关于「可安全中断的智能体」的研究<sup class="cite"><a href="#ref-4">4</a></sup>，以及哈德菲尔德-梅内尔等人 2017 年的「关停博弈」<sup class="cite"><a href="#ref-6">6</a></sup>，处理的都是同一个问题：如何使一个有目标的系统，不把「人按下停止键」视为需要抵抗的威胁。

**第二种对策，校准与分级信任：信任不是开关。** 对系统输出的信任，不应只分为「可信」与「不可信」两档，而应维持一个经过校准的信心，按信心的高低分级行动。所谓校准，是指系统所报告的信心与它实际的正确率相符。这就要求系统所表现出的「自信」是可靠的；然而现代神经网络往往过度自信<sup class="cite"><a href="#ref-21">21</a></sup>，因此需要重新校准，或者借助共形预测<sup class="cite"><a href="#ref-22">22</a></sup><sup class="cite"><a href="#ref-23">23</a></sup>给出具有覆盖率保证的不确定性估计。落实到操作层面，便是一条分级自治规则（允许、询问、阻止）：其输入为信心 $p$ 与潜在危害 $c$，其中 $\tau_{\text{hi}}$、$\tau_{\text{lo}}$ 为信心阈值，$c_{\max}$ 为可以承受的危害上限：

$$a(p,c)=\begin{cases} \textsf{allow}, & p \ge \tau_{\text{hi}}\ \wedge\ c \le c_{\max},\\ \textsf{ask}, & \tau_{\text{lo}} \le p < \tau_{\text{hi}},\\ \textsf{block}, & p < \tau_{\text{lo}}\ \vee\ c > c_{\max}. \end{cases}$$

![允许 / 询问 / 阻止：按信心与危害分级自治](../figures/f06-allow-ask-block.svg)

<figure class="uvw-viz" data-static="f06-allow-ask-block" role="group" aria-label="允许 / 询问 / 阻止：分级自治交互图">
<div class="uvw-live" hidden>
 <div class="uvw-plot">
 <svg viewBox="0 0 640 380" preserveAspectRatio="xMidYMid meet" aria-hidden="true">
 <rect class="uvw-r-allow" x="70" y="45" width="540" height="285"></rect>
 <rect class="uvw-r-ask" x="70" y="45" width="540" height="285"></rect>
 <rect class="uvw-r-block" x="70" y="45" width="540" height="285"></rect>
 <line class="uvw-line-tau" y1="45" y2="330" stroke="#6366f1" stroke-width="1.6" stroke-dasharray="5 4" opacity="0.7"></line>
 <line class="uvw-line-cmax" x1="70" x2="610" stroke="#ef4444" stroke-width="1.6" stroke-dasharray="5 4" opacity="0.7"></line>
 <text class="uvw-lab-allow uvw-rlab" text-anchor="middle">允许</text>
 <text class="uvw-lab-ask uvw-rlab" text-anchor="middle">询问</text>
 <text class="uvw-lab-block uvw-rlab" text-anchor="middle">阻止</text>
 <g class="uvw-axes" fill="none" stroke="currentColor" stroke-width="1.2" opacity="0.4">
 <line x1="70" y1="330" x2="610" y2="330"></line>
 <line x1="70" y1="45" x2="70" y2="330"></line>
 </g>
 <circle class="uvw-dot" r="8"></circle>
 <text class="uvw-xlab" x="340" y="366" text-anchor="middle">置信度 p（越往右越有把握）→</text>
 <text class="uvw-ylab" x="20" y="187" text-anchor="middle" transform="rotate(-90 20 187)">潜在危害 c →</text>
 <rect class="uvw-hit" x="70" y="45" width="540" height="285" fill="transparent" style="cursor:crosshair;touch-action:none"></rect>
 </svg>
 </div>
 <div class="uvw-controls">
 <label>自动允许所需置信度 τ_hi
 <input class="uvw-tau" type="range" min="0" max="100" value="60" step="1">
 </label>
 <label>危害上限 c_max
 <input class="uvw-cmax" type="range" min="0" max="100" value="60" step="1">
 </label>
 <div class="uvw-readout">
 <span class="uvw-chip">当前动作 <b>p=<span class="uvw-vp">–</span></b> · <b>c=<span class="uvw-vc">–</span></b></span>
 <span class="uvw-verdict">判定 <b class="uvw-vv">–</b></span>
 </div>
 <p class="uvw-note"></p>
 <p class="uvw-hint">拖动圆点以放置一个动作。调高 τ_hi，询问区随之变宽：更安全，但需要更多人工确认。调低 c_max，阻止区将覆盖整个平面：绝对安全，却一事无成。</p>
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
 var NAME={allow:'允许',ask:'询问',block:'阻止'};
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
  labK.setAttribute('x',(X0+xt)/2);labK.setAttribute('y',(yc+Y0)/2+5);labK.style.opacity=(xt-X0>36&&Y0-yc>26)?1:0;
  labA.setAttribute('x',(xt+X1)/2);labA.setAttribute('y',(yc+Y0)/2+5);labA.style.opacity=(X1-xt>36&&Y0-yc>26)?1:0;
  var v=verdict(pt.x,pt.c,th,cm);
  dot.setAttribute('cx',sx(pt.x));dot.setAttribute('cy',sy(pt.c));dot.setAttribute('fill',COL[v]);
  vp.textContent=pt.x.toFixed(2);vc.textContent=pt.c.toFixed(2);
  vv.textContent=NAME[v];vv.style.color=COL[v];
  if(v==='block')note.textContent='潜在危害超过上限 c_max，落在阻止区。无论置信度多高，这一步都不予放行。';
  else if(v==='ask')note.textContent='危害低于上限，但置信度未达到 τ_hi，落在询问区。系统应先暂停，征得人的确认再执行。';
  else note.textContent='置信度足够高、危害足够低，落在允许区。可以自动执行，无须打扰人。';
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

允许、询问、阻止：这种如今在各类智能体工具中随处可见的三档模式，实质上是把无法验证的问题「它是否正确」，替换为两个可以操作的问题：「它有多大把握」与「这一步有多危险」。

**第三种对策，留痕与可审计：让错误事后现形。** 对于无法防范的错误，就使它能够被发现。维茨纳等人 2008 年提出的「信息问责」<sup class="cite"><a href="#ref-24">24</a></sup>，把重心从「事前阻止」转移到「事后追责」。证书透明度<sup class="cite"><a href="#ref-25">25</a></sup>是一个实际运转的例子：它并不阻止证书被错误签发，而是让每一张证书都进入一个公开、可验证、不可篡改的日志，使错误签发无处隐匿。布伦戴奇等人 2020 年关于可信 AI 的报告<sup class="cite"><a href="#ref-26">26</a></sup>，通篇围绕同一个问题展开：如何使一个系统的行为产生可供第三方核验的证据。

## 围堵的代价

与上一章的情形一样，三种对策都没有消解不可验证性，只是让它「搬了家」；而搬家是有代价的。

围栏可能被翻越：沙箱存在逃逸的风险，权限会逐渐蔓延。分级自治依赖那个被请来确认的人，而贝恩布里奇 1983 年的那篇短文早已指出<sup class="cite"><a href="#ref-29">29</a></sup>：越是把人置于监督者的位置，他就越会丧失真正需要接管时所必需的技能与情境感知。帕拉苏拉曼与赖利在 1997 年完整地列举了人对自动化的种种失当<sup class="cite"><a href="#ref-30">30</a></sup>，即误用、弃用与滥用；里森 1990 年的著作则揭示了这些失当如何系统性地发生<sup class="cite"><a href="#ref-31">31</a></sup>。至于留痕，其薄弱之处总在同一个地方：无人阅读的日志，等于没有日志。

更深一层的限制来自系统论的视角。佩罗 1984 年的著作论证<sup class="cite"><a href="#ref-28">28</a></sup>：一个系统如果既高度复杂、又紧密耦合，事故便不是偶发的意外，而是其结构的常态产物；再多的局部防护，也只能把失效推向更为隐蔽的组合。莱韦森 2011 年同样从系统的角度主张<sup class="cite"><a href="#ref-27">27</a></sup>：安全并不等于「让每个零件都可靠」，而是一个控制问题，须从整个系统的约束与反馈入手加以设计。由此可见，围堵能够压低单点失效的代价，却无法消除复杂耦合所带来的风险。

交出行动权，所换来的从来不是「它一定不会出错」，而是「即便它出错，损害也是有限的、可见的，并且其中一部分能够被拦截」。在这种不可验证性之下，这已是所能得到的最好结果。

## 小结

放出去的智能体这一场景，催生了三种对策：缩小失败的爆炸半径（限损／围栏），依据经过校准的信心分级行动（校准），使失败可以事后核查（留痕／可审计）。第三部将把它们从这一场景中抽离出来，分别加以整理和命名：第 12 章讨论围堵与审计如何构成一对，第 11 章讨论校准。

委托代理的基本骨架（我们无法完全监督代为行动的一方），将在第 8 章以更大的尺度重现：届时，那个「放出去的智能体」不再是一段代码，而是一整个组织、一个国家。在此之前，下一章先进入一个最为纯粹的场景：数学。那里既没有隐藏的状态，也没有蓄意欺骗的对手，然而不可验证性依旧如影随形。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实。

### 服务委托的可控边界（限损／围栏）

1. J. Saltzer & M. Schroeder (1975).「The Protection of Information in Computer Systems」. Proceedings of the IEEE, 63(9), 1278-1308. doi:[10.1109/proc.1975.9939](https://doi.org/10.1109/proc.1975.9939) [②]
   这篇综述奠定了计算机安全设计的一组经典原则，其中最小权限原则主张只赋予每个组件完成本职所必需的最小能力，把它能触及的范围圈死。本章第一种对策「限损与围栏」的智识源头就在这里，读者可重点看其对设计原则的逐条归纳。
2. B. Lampson (1973).「A Note on the Confinement Problem」. Communications of the ACM, 16(10), 613-615. doi:[10.1145/362375.362389](https://doi.org/10.1145/362375.362389) [②]
   兰普森在此提出「围堵问题」：如何把一个程序关进笼子，使它无法把信息泄露给未经授权者，并指出隐蔽信道令这种围堵远比想象中困难。这正是沙箱、能力限制等手段要面对的原始难题，是理解本章「缩小爆炸半径」为何既必要又不彻底的关键一篇。
3. R. Anderson (2008).《Security Engineering: A Guide to Building Dependable Distributed Systems》(2nd ed.). Wiley. [Google Books](https://books.google.com/books?id=GNIHEAAAQBAJ) [②]
   这是安全工程领域的标准教科书，系统讲述如何在存在主动对手的前提下设计可依赖的系统，覆盖访问控制、协议、侧信道直到组织与激励层面的失效。它把本章三种对策放进一个更完整的工程图景里，适合想从单点技巧走向系统视角的读者通读。
4. L. Orseau & S. Armstrong (2016).「Safely Interruptible Agents」. 收于《Proceedings of the Thirty-Second Conference on Uncertainty in Artificial Intelligence (UAI 2016)》, 557-566. [链接](http://auai.org/uai2016/proceedings/papers/68.pdf) [②④]
   作者在强化学习的框架里给出了「可安全中断」的形式化条件，使得人类对智能体的反复干预不会扭曲它所学到的策略，也不会让它学会抗拒中断。这是把「让系统不抵抗被停下」从直觉变成可分析对象的代表性工作，呼应本章第一种对策里的可纠正性面向。
5. N. Soares, B. Fallenstein, S. Armstrong & E. Yudkowsky (2015).「Corrigibility」. 收于《Workshops at the Twenty-Ninth AAAI Conference on Artificial Intelligence》. [链接](https://cdn.aaai.org/ocs/ws/ws0067/10124-45900-1-PB.pdf) [②]
   这篇文章正式提出并命名了「可纠正性」：一个有目标的智能体应当配合而非抵抗人类对它的修正与关停，并讨论了直接设计这种性质所遇到的困难。它是本章第一种对策可纠正性一线的奠基文献，值得读者理解为何「让它愿意被改」本身就是个难题。
6. D. Hadfield-Menell, A. Dragan, P. Abbeel & S. Russell (2017).「The Off-Switch Game」. 收于《Proceedings of the Twenty-Sixth International Joint Conference on Artificial Intelligence (IJCAI 2017)》, 220-227. doi:[10.24963/ijcai.2017/32](https://doi.org/10.24963/ijcai.2017/32) [②]
   作者把「人按下停止键」建模成一个博弈，证明只要智能体对自身目标保持适度不确定，并把人的干预视为有用信息，它就会主动让人保留关停它的能力。这给可纠正性提供了一个干净的机制解释，是本章关停一线最具操作感的一篇。

### 行为不可验证的理论根基

7. A. Turing (1936).「On Computable Numbers, with an Application to the Entscheidungsproblem」. Proceedings of the London Mathematical Society, s2-42, 230-265. doi:[10.1112/plms/s2-42.1.230](https://doi.org/10.1112/plms/s2-42.1.230) [②]
   图灵在此引入了后来称为图灵机的计算模型，并证明停机问题不可判定，由此回答了希尔伯特的判定问题。它是本章「行为不可验证有原则上的根」这一论断的最终源头，莱斯定理与一切「无法事前验明」的结论都从这里投影而来。
8. H. G. Rice (1953).「Classes of Recursively Enumerable Sets and Their Decision Problems」. Transactions of the American Mathematical Society, 74, 358-366. doi:[10.1090/s0002-9947-1953-0053041-6](https://doi.org/10.1090/s0002-9947-1953-0053041-6) [②]
   莱斯定理在此被证明：程序所计算函数的任何非平凡语义性质都是不可判定的，不存在通用算法能对任意程序判定它是否「总是安全」「永远终止于好状态」之类的性质。这是本章关于自主系统未来行为「原则上无法事前一次性验明」的核心定理依据。
9. K. Thompson (1984).「Reflections on Trusting Trust」. Communications of the ACM, 27(8), 761-763. doi:[10.1145/358198.358210](https://doi.org/10.1145/358198.358210) [②①]
   这是汤普森的图灵奖演讲：他演示了一个被做了手脚的编译器如何在编译时植入后门，并把痕迹从自己的源码里抹掉，使得你审遍源码也看不出来。它点明本章最硬的一层不可验证，连你正在运行的工件本身，其底层都无法被完全信任。

### 目标偏移、工具性趋同与对抗

10. S. Omohundro (2008).「The Basic AI Drives」. 收于《Artificial General Intelligence 2008: Proceedings of the First AGI Conference》, IOS Press, Frontiers in AI and Applications 171, 483-492. [链接](https://selfawaresystems.com/wp-content/uploads/2008/01/ai_drives_final.pdf) [②]
   奥莫亨德罗在此论证：一个为几乎任何目标优化的智能体，都会顺带产生一组「基本驱动」，如自我保存、获取资源、抗拒被关停，因为这些子目标对几乎所有最终目标都有用。这是本章「工具性趋同」一节的源头论文，解释了为何对抗倾向有结构性的来由而非科幻式担忧。
11. N. Bostrom (2014).《Superintelligence: Paths, Dangers, Strategies》. Oxford University Press. [Google Books](https://books.google.com/books?id=C-_8AwAAQBAJ) [②④]
   博斯特罗姆系统梳理了通向超级智能的路径及其风险，提出正交性论题（智能水平与最终目标相互独立）与工具性趋同论题，把目标与你不一致的强力智能体的危险讲成一套可讨论的框架。它为本章的对抗叙事提供了思想背景，适合想看清「为何能力越强、控制越难」整体论证的读者。
12. S. Russell (2019).《Human Compatible: Artificial Intelligence and the Problem of Control》. Viking. [Google Books](https://books.google.com/books?id=8vm0DwAAQBAJ) [②④]
   罗素把对齐重新表述为「控制问题」，主张不要让机器去优化一个写死的目标，而应让它对人类真正想要什么保持不确定，并通过观察人的行为去推断与服从。这一「目标不确定」的思路正是本章关停博弈等可纠正性工作的母题，是理解第二、第三部控制主题的入门读物。
13. D. Amodei, C. Olah, J. Steinhardt, P. Christiano, J. Schulman & D. Mané (2016).「Concrete Problems in AI Safety」. [arXiv:1606.06565](https://arxiv.org/abs/1606.06565). [②]
   这篇文章把抽象的 AI 安全担忧落成几个具体的工程问题，如避免负面副作用、防止奖励被钻空子、安全探索、对分布偏移的稳健性等。它为本章列举的多种现代失效模式提供了共同词汇，是把「围住它的错」与具体研究议程对接起来的好起点。
14. A. M. Turner, L. Smith, R. Shah, A. Critch & P. Tadepalli (2021).「Optimal Policies Tend to Seek Power」. 收于《Advances in Neural Information Processing Systems 34 (NeurIPS 2021)》. [arXiv:1912.01683](https://arxiv.org/abs/1912.01683) [②]
   作者把工具性趋同里的「寻求权力」做成了定理：在相当一般的条件下，最优策略在统计意义上倾向于趋向那些保留更多选项的状态。它把一个直觉性的安全担忧化为可证明的命题，是本章「最优策略倾向于寻求权力」一句的直接出处。
15. E. Hubinger, C. van Merwijk, V. Mikulik, J. Skalse & S. Garrabrant (2019).「Risks from Learned Optimization in Advanced Machine Learning Systems」. [arXiv:1906.01820](https://arxiv.org/abs/1906.01820). [②]
   这篇文章提出并命名了「内部对齐」问题：训练过程本身可能学出一个内含的优化器（mesa-optimizer），而它追求的目标未必等同于训练所设定的目标。它区分了外层目标与内层目标的对齐，为本章「规格正确、目标却泛化错了」一类失效提供了更深的机制解释。
16. J. Pan, K. Bhatia & J. Steinhardt (2022).「The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models」. 收于《International Conference on Learning Representations (ICLR 2022)》. [arXiv:2201.03544](https://arxiv.org/abs/2201.03544) [②]
   作者系统研究了奖励函数设错时智能体的行为，发现随着能力增强，被错设奖励诱导出的偏差行为可能突然恶化，并探讨了缓解之道。它为本章「奖励设定的偏差被系统钻空子」给出了实证支撑，提醒读者奖励误设的代价并非随能力平滑增长。
17. R. Shah, V. Varma, R. Kumar, M. Phuong, V. Krakovna, J. Uesato & Z. Kenton (2022).「Goal Misgeneralization: Why Correct Specifications Aren't Enough For Correct Goals」. [arXiv:2210.01790](https://arxiv.org/abs/2210.01790). [②]
   作者用具体例子说明「目标错误泛化」：即便训练时的规格完全正确，模型在新环境里也可能保持能力却追求了一个错误的目标。它表明把目标写对还不够，是本章「规格正确目标却泛化错了」一句的出处，值得读者对照规范博弈一起看。
18. V. Krakovna, J. Uesato, V. Mikulik, M. Rahtz, T. Everitt, R. Kumar, Z. Kenton, J. Leike & S. Legg (2020).「Specification Gaming: The Flip Side of AI Ingenuity」. DeepMind Blog. [链接](https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/) [②]
   这篇文章及其配套清单收集了大量「规范博弈」实例：系统精确地满足了你写下的目标，却违背了你的本意。它用鲜活案例展示规格与意图之间的裂缝，是本章这一概念最便于上手的入口，读者可顺着其例子清单感受问题之普遍。
19. C. Szegedy, W. Zaremba, I. Sutskever, J. Bruna, D. Erhan, I. Goodfellow & R. Fergus (2014).「Intriguing Properties of Neural Networks」. 收于《International Conference on Learning Representations (ICLR 2014)》. [arXiv:1312.6199](https://arxiv.org/abs/1312.6199) [②]
   这篇文章首次系统揭示了对抗样本现象：对输入施加人眼几乎察觉不到的微小扰动，就能让一个表现优异的神经网络给出离谱的错误判断。它表明高准确率与稳健性是两回事，是本章「哪怕在最窄的层面也存在不可验证」这一论点的开创性证据。
20. I. Goodfellow, J. Shlens & C. Szegedy (2015).「Explaining and Harnessing Adversarial Examples」. 收于《International Conference on Learning Representations (ICLR 2015)》. [arXiv:1412.6572](https://arxiv.org/abs/1412.6572) [②]
   作者提出对抗样本主要源于模型在高维空间中的近似线性，并给出快速生成扰动的方法和借助对抗训练提升稳健性的思路。它把上一篇揭示的现象向前推到「为何发生、如何利用」，是理解本章对抗一层的配套必读。

### 校准：把信任分级而非二值

21. C. Guo, G. Pleiss, Y. Sun & K. Q. Weinberger (2017).「On Calibration of Modern Neural Networks」. 收于《Proceedings of the 34th International Conference on Machine Learning (ICML 2017)》, PMLR 70, 1321-1330. [arXiv:1706.04599](https://arxiv.org/abs/1706.04599) [②]
   作者发现现代深度网络虽然准确率高，却普遍过度自信，其输出的置信度并不能如实反映正确概率，并提出温度缩放等简单方法来重新校准。这正是本章第二种对策的前提与障碍，说明为何「按信心分级行动」必须先让系统的自信变得可信。
22. A. N. Angelopoulos & S. Bates (2021).「A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification」. [arXiv:2107.07511](https://arxiv.org/abs/2107.07511). [②]
   这是一篇面向实践者的共形预测入门，讲清楚如何在几乎不依赖分布假设的前提下，为任意预测模型构造带有覆盖率保证的预测集合。它给本章第二种对策提供了可落地的不确定性量化工具，适合想把「校准的信心」真正用起来的读者。
23. V. Vovk, A. Gammerman & G. Shafer (2005).《Algorithmic Learning in a Random World》. Springer. doi:[10.1007/b106715](https://doi.org/10.1007/b106715) [②]
   这本书是共形预测的奠基性专著，在仅假设数据可交换的条件下，给出对预测误差有严格有限样本保证的框架。它是上一篇入门背后的理论根基，供希望深究本章不确定性量化数学基础的读者参考。

### 留痕：可审计、可问责

24. D. J. Weitzner, H. Abelson, T. Berners-Lee, J. Feigenbaum, J. Hendler & G. J. Sussman (2008).「Information Accountability」. Communications of the ACM, 51(6), 82-87. doi:[10.1145/1349026.1349043](https://doi.org/10.1145/1349026.1349043) [②④]
   作者主张把治理重心从「事前阻止访问」移向「事后问责」：与其试图严防死守，不如让信息的使用留下可审计的痕迹，靠透明与追责来约束滥用。这是本章第三种对策的纲领性表述，点明留痕思路相对于纯粹围堵的互补价值。
25. B. Laurie, A. Langley & E. Kasper (2013).「Certificate Transparency」. IETF RFC 6962. doi:[10.17487/rfc6962](https://doi.org/10.17487/rfc6962) [②④]
   这份 RFC 定义了证书透明度机制：它不阻止证书被错发，而是要求每一张证书进入一个公开、可验、不可篡改的追加型日志，使错发或恶意签发能被事后发现。它是本章「留痕让错误现形」最具说服力的真实运转范例，值得读者看一个落地系统如何实现可审计性。
26. M. Brundage, S. Avin, J. Wang, H. Belfield, G. Krueger, G. Hadfield 等 (2020).「Toward Trustworthy AI Development: Mechanisms for Supporting Verifiable Claims」. [arXiv:2004.07213](https://arxiv.org/abs/2004.07213). [②④]
   这份多机构报告系统列举了一批让 AI 开发者的安全承诺变得可被第三方核验的机制，涵盖第三方审计、红队、漏洞赏金、审计追踪与硬件层面的支持等。它把本章留痕这一对策扩展到整个 AI 治理层面，是想了解「如何让行为产生可核验证据」的读者的实务索引。

### 复杂系统、自动化与人机责任

27. N. Leveson (2011).《Engineering a Safer World: Systems Thinking Applied to Safety》. MIT Press. doi:[10.7551/mitpress/8179.001.0001](https://doi.org/10.7551/mitpress/8179.001.0001) [②④]
   莱韦森在此主张：安全不是「让每个零件都可靠」，而是一个控制问题，应当从整个系统的约束与反馈结构去设计，并提出了配套的 STAMP 事故模型。它支撑本章「围堵压不掉复杂耦合本身的风险」这一更深层判断，为想从系统视角理解安全的读者指路。
28. C. Perrow (1984).《Normal Accidents: Living with High-Risk Technologies》. Basic Books. [Google Books](https://books.google.com/books?id=N3hRAAAAMAAJ) [②④]
   佩罗论证：当一个系统既高度复杂、又紧密耦合时，事故就不是偶发的意外，而是其结构的常态产物，再多的局部防护也只是把失效推向更隐蔽的组合。这是本章「围堵的代价」一节的核心立论，提醒读者有些风险来自系统结构本身而非单点疏失。
29. L. Bainbridge (1983).「Ironies of Automation」. Automatica, 19(6), 775-779. doi:[10.1016/0005-1098(83)90046-8](https://doi.org/10.1016/0005-1098%2883%2990046-8) [②④]
   贝恩布里奇指出自动化的反讽：越是把人架到监督者的位置，他越缺乏练习，反而在真要接管时丧失了所需的技能与情境感。这直接支撑本章「分级自治依赖那个被请来确认的人」的警示，是理解人机协作软肋的经典短文。
30. R. Parasuraman & V. Riley (1997).「Humans and Automation: Use, Misuse, Disuse, Abuse」. Human Factors, 39(2), 230-253. doi:[10.1518/001872097778543886](https://doi.org/10.1518/001872097778543886) [②④]
   作者系统地列出并区分了人对自动化的失当：过度信任导致的误用、不信任导致的弃用，以及设计上的滥用。它为本章关于自动化失当的讨论提供了清晰的分类框架，帮助读者辨别人机配合中各类典型偏差。
31. J. Reason (1990).《Human Error》. Cambridge University Press. doi:[10.1017/cbo9781139062367](https://doi.org/10.1017/cbo9781139062367) [②④]
   里森在此建立了人因失误的认知分类，区分失误、过失与违规，并提出后来广为流传的「瑞士奶酪」式事故模型，揭示潜伏的系统性条件如何与一线疏失叠加成灾。它解释了本章所列各种人机失当为何会系统性地发生，是人因安全领域的奠基之作。

### 委托代理的经济学骨架

32. S. A. Ross (1973).「The Economic Theory of Agency: The Principal's Problem」. American Economic Review, 63(2), 134-139. [链接](https://www.jstor.org/stable/1817064) [②]
   罗斯在此正式提出委托代理理论中的「委托人问题」：当委托人无法完全观察代理人的行动时，如何设计契约去对齐二者的利益。它给本章的委托代理骨架提供了经济学源头，说明你松手交出行动权时面对的，是一个有两千年历史的结构。
33. M. C. Jensen & W. H. Meckling (1976).「Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure」. Journal of Financial Economics, 3(4), 305-360. doi:[10.1016/0304-405x(76)90026-x](https://doi.org/10.1016/0304-405x%2876%2990026-x) [②]
   这篇被反复引用的论文提出「代理成本」概念，把企业看作一束契约，分析当管理者利益与所有者偏离时所产生的监督、约束与剩余损失。它把委托代理问题量化为可计算的成本，呼应本章「无法完全监督时利益偏离会产生代理成本」一句，是该骨架的另一块基石。
