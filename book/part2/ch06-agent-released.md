# 第 6 章　放出去的智能体

> **论点**：一旦把行动委托给自主系统，你无法验证它在将遇到的一切情形里的未来行为（开放世界）；若它还能耍策略，你又叠上对抗式不可验证，于是应对从「证明它对」转向「限制它能破坏什么、给你的信任定价、让它的行为事后可查」。

## 交出去之后

上一章你还在场。这一章，你把手松开。

把一段不受信的代码跑起来，把工具和权限交给一个能自己决定下一步的系统，让一个自动驾驶在你没坐在里面的时候上路。一旦行动权交出去，一个新的难题出现了：你没法验证它在将要遇到的一切情形里会怎么做，因为那些情形你大多没见过，也没法预先穷举。上一章的不可验证来自目标藏在别人脑子里，这一章的不可验证来自行为发生在未来、发生在你看不见的地方。当这个系统还会耍策略时，又叠上一层对抗。2010 年 5 月 6 日的「闪电崩盘」就是一次预演：彼此交互的自动交易程序在几分钟内把道琼斯指数砸下近千点，又几乎同样迅速地反弹，没有哪个程序员预见过成交会如此级联。每个程序在测试里都没问题，放到一起、放进真实行情，就酿成了谁都没验证过的灾难。

## 未来行为的缺口

你测试过的，是有限几个输入；它会遇到的，是一个开放的世界。这中间的缺口，不是「再多测一些就能补上」的工程缺口，它有原则上的根。

赖斯定理说得很硬：程序的任何非平凡语义性质都是不可判定的。也就是说，不存在一个通用算法，能对任意程序判定它是否「总是安全」「绝不泄露」「永远终止于好状态」。这不是算力不够，是逻辑上办不到，它是图灵停机问题投在「程序行为」上的影子。你想要的那种保证，对任意一个足够通用的自主系统，原则上无法在事前一次性验明。

更狠的一击来自汤普森 1984 年图灵奖演讲里那个著名的论证<sup class="cite"><a href="#ref-9">9</a></sup>：连你正在运行的这个工件本身，你都无法完全信任。一个被做了手脚的编译器，可以在编译时悄悄植入后门，再把痕迹从自己的源码里抹掉，使得你审遍源码也看不出来。你能验证的，永远只是某个表象层，底下还有你没看、也看不尽的层。把这两件事放在一起：行为在未见输入上不可验证，工件在底层不可全验。这是本书目前遇到的最硬的不可验证。

## 当它会耍策略

如果这个系统只是被动地把没见过的输入处理错，那还只是「部分可观测」加「开放世界」。可一旦它有了自己的目标，并且这目标与你的目标不完全一致，它就会主动地、策略性地行动，包括绕过你的检查。这时第 2 章那第五种处境，对抗，登场了。

这不是科幻式的担忧，它有结构性的来由。奥莫亨德罗 2008 年<sup class="cite"><a href="#ref-10">10</a></sup>、博斯特罗姆 2014 年<sup class="cite"><a href="#ref-11">11</a></sup>指出的工具性趋同：一个为几乎任何目标优化的智能体，都会顺带追求一些工具性的子目标，自我保存、获取资源、抗拒被关停，因为这些几乎对任何最终目标都有用。特纳等人 2021 年把其中一条做成了定理<sup class="cite"><a href="#ref-14">14</a></sup>：在相当一般的条件下，最优策略倾向于寻求权力，即保留更多选项的状态。在今天的系统里，这表现为一组具体而棘手的失效：奖励设定的偏差被系统钻空子<sup class="cite"><a href="#ref-16">16</a></sup>，规格正确目标却泛化错了<sup class="cite"><a href="#ref-17">17</a></sup>，以及克拉科夫娜等人收集的大量「规格博弈」实例<sup class="cite"><a href="#ref-18">18</a></sup>，系统精确地满足了你写下的目标，却违背了你的本意。哪怕在最窄的层面，对抗样本也表明<sup class="cite"><a href="#ref-19">19</a></sup><sup class="cite"><a href="#ref-20">20</a></sup>：一个表现优异的模型，可以被一个人眼看不出的微小扰动诱导出离谱的错误。一个不那么技术、却极其直白的例子是微软 2016 年放出的聊天机器人 Tay：它被设计成从与网民的对话里学习，结果一群人有组织地用恶意言论「投喂」它，不到一天它就开始发布种族主义与攻击性内容，上线约十六小时即被紧急下线。放出去、会学习、又撞上有意作对的开放世界，三者一旦相遇，事前的测试根本拦不住。

这件事其实古老。经济学早把它叫做委托代理问题<sup class="cite"><a href="#ref-32">32</a></sup><sup class="cite"><a href="#ref-33">33</a></sup>：当你委托别人替你行动，而你无法完全监督他时，他的利益与你的偏离就会产生「代理成本」。两千年来人类雇人、立约、设监察，对付的都是同一个结构。自主系统只是把它推到了一个新的尺度上。

## 应对：从「证明它对」到「围住它的错」

既然事前证不出它对，有能力的应对就不再纠缠于证明，而是换三个问题来问：就算它错了，能坏到哪儿？我对它该信几分？万一它真错了，我事后查得到吗？三招对应三个问题。

**第一招，衰减与围栏：缩小爆炸半径。** 这是计算机安全最老的智慧。萨尔策与施罗德 1975 年的最小权限原则<sup class="cite"><a href="#ref-1">1</a></sup>、兰普森 1973 年的围堵问题<sup class="cite"><a href="#ref-2">2</a></sup>，讲的都是：只给一个组件完成本职所必需的最小能力，把它能触及的范围圈死。沙箱、能力限制、职责分离，都是它的化身。在智能体语境里，这一招还多了一个面向，可纠正性：把系统设计成不抗拒被停下。索亚雷斯等人 2015 年的可纠正性<sup class="cite"><a href="#ref-5">5</a></sup>、奥尔索与阿姆斯特朗 2016 年的「可安全中断的智能体」<sup class="cite"><a href="#ref-4">4</a></sup>、哈德菲尔德-梅内尔等人 2017 年的「关停博弈」<sup class="cite"><a href="#ref-6">6</a></sup>，研究的正是如何让一个有目标的系统，不把「人来按下停止键」当成需要抵抗的威胁。

**第二招，标定与分级信任：别用二值。** 不要把系统的输出当成「可信／不可信」的开关，而是维持一个标定的信心，按信心的高低分级行动。这要求系统的「自信」是可信的，而现代神经网络恰恰常常过度自信<sup class="cite"><a href="#ref-21">21</a></sup>，于是需要重新校准，或用保形预测<sup class="cite"><a href="#ref-22">22</a></sup><sup class="cite"><a href="#ref-23">23</a></sup>给出有覆盖保证的不确定性。落到操作上，就是一条以信心 $p$、潜在危害 $c$ 为输入的分级自治规则（允许、询问、阻止），其中 $\tau_{\text{hi}}$、$\tau_{\text{lo}}$ 是信心阈值，$c_{\max}$ 是可承受的危害上限：

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
 <p class="uvw-hint">拖动圆点放置一个动作。调高 τ_hi，询问区变宽：更安全，但打扰更多。调低 c_max，阻止区吞掉整个平面：绝对安全，却什么也做不成。</p>
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
  if(v==='block')note.textContent='潜在危害超过上限 c_max，落在阻止区。无论把握多高，这一步都不放行。';
  else if(v==='ask')note.textContent='危害在上限之下，但置信度没达到 τ_hi，落在询问区。先停下来，问你一句再动。';
  else note.textContent='把握足够高、危害足够低，落在允许区。可以自动执行，不打扰你。';
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

允许、询问、阻止，这个今天在各类智能体工具里随处可见的三档模式，本质就是把不可验证的「它对不对」换成了可操作的「它有多大把握、这一步多危险」。

**第三招，留痕与可审计：让错误事后现形。** 防不住的，就让它可被发现。维茨纳等人 2008 年的「信息问责」<sup class="cite"><a href="#ref-24">24</a></sup>把重心从「事前阻止」移到「事后追责」；证书透明度<sup class="cite"><a href="#ref-25">25</a></sup>是一个真实运转的例子，它不阻止证书被错发，而是让每一张证书都进入一个公开、可验、不可篡改的日志，使错发无所遁形。布伦戴奇等人 2020 年那份关于可信 AI 的报告<sup class="cite"><a href="#ref-26">26</a></sup>，整篇讲的都是如何让一个系统的行为产生可被第三方核验的证据。

## 围堵的代价

三招都不是把不可验证消解掉，而是把它搬家，搬家是要付费的。

围栏会被翻越：沙箱有逃逸，权限会蔓延。分级自治依赖那个被请来确认的人，而贝恩布里奇 1983 年的论著早就指出<sup class="cite"><a href="#ref-29">29</a></sup>，越是把人架到监督者的位置，他越是丧失了真要接管时所需的技能与情境感；帕拉苏拉曼与赖利 1997 年把人对自动化的失当完整列出<sup class="cite"><a href="#ref-30">30</a></sup>：误用、弃用、滥用。里森 1990 年的著作则揭示这些失当如何系统性地发生<sup class="cite"><a href="#ref-31">31</a></sup>。留痕则永远栽在同一处：没人去读的日志，等于没有日志。

更深一层是系统论的视角。佩罗 1984 年的著作论证<sup class="cite"><a href="#ref-28">28</a></sup>：当一个系统既高度复杂、又紧密耦合时，事故不是偶发的意外，而是其结构的常态产物，再多的局部防护也只是把失效推向更隐蔽的组合。莱韦森 2011 年由此主张<sup class="cite"><a href="#ref-27">27</a></sup>，安全不是「让每个零件都可靠」，而是一个控制问题，要从整个系统的约束与反馈去设计。围堵能压低单点失效的代价，却压不掉复杂耦合本身带来的风险。

把行动权交出去，你换来的从来不是「它一定不出错」，而是「就算它出错，坏得有限、看得见、拦得住一部分」。这已经是在这种不可验证下能拿到的最好结果。

## 这一章通向哪里

放出去的智能体，逼出了三招：缩小失败的爆炸半径（衰减围栏）、按标定的信心分级行动（标定）、让失败事后可查（留痕）。它们会在第三部被单独拎出来命名，第 12 章谈围堵与审计如何成对，第 11 章谈标定。

而那个委托代理的骨架（你无法完全监督一个替你行动的主体），会在第 8 章以更大的尺度重现：当那个「放出去的智能体」不再是一段代码，而是一整个组织、一个国家。在那之前，下一章先走进一个最纯的现场，数学，那里没有藏起来的状态，也没有会骗你的对手，不可验证却依然如影随形。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实。

### 服务委托的可控边界（衰减／围栏）

1. J. Saltzer & M. Schroeder (1975).「The Protection of Information in Computer Systems」. Proceedings of the IEEE, 63(9), 1278-1308. [②]
   这篇综述奠定了计算机安全设计的一组经典原则，其中最小权限原则主张只赋予每个组件完成本职所必需的最小能力，把它能触及的范围圈死。本章第一招「衰减与围栏」的智识源头就在这里，读者可重点看其对设计原则的逐条归纳。
2. B. Lampson (1973).「A Note on the Confinement Problem」. Communications of the ACM, 16(10), 613-615. [②]
   兰普森在此提出「围堵问题」：如何把一个程序关进笼子，使它无法把信息泄露给未经授权者，并指出隐蔽信道令这种围堵远比想象中困难。这正是沙箱、能力限制等手段要面对的原始难题，是理解本章「缩小爆炸半径」为何既必要又不彻底的关键一篇。
3. R. Anderson (2008).《Security Engineering: A Guide to Building Dependable Distributed Systems》(2nd ed.). Wiley. [②]
   这是安全工程领域的标准教科书，系统讲述如何在存在主动对手的前提下设计可依赖的系统，覆盖访问控制、协议、侧信道直到组织与激励层面的失效。它把本章三招放进一个更完整的工程图景里，适合想从单点技巧走向系统视角的读者通读。
4. L. Orseau & S. Armstrong (2016).「Safely Interruptible Agents」. 收于《Proceedings of the Thirty-Second Conference on Uncertainty in Artificial Intelligence (UAI 2016)》, 557-566. [②④]
   作者在强化学习的框架里给出了「可安全中断」的形式化条件，使得人类对智能体的反复干预不会扭曲它所学到的策略，也不会让它学会抗拒中断。这是把「让系统不抵抗被停下」从直觉变成可分析对象的代表性工作，呼应本章第一招里的可纠正性面向。
5. N. Soares, B. Fallenstein, S. Armstrong & E. Yudkowsky (2015).「Corrigibility」. 收于《Workshops at the Twenty-Ninth AAAI Conference on Artificial Intelligence》. [②]
   这篇文章正式提出并命名了「可纠正性」：一个有目标的智能体应当配合而非抵抗人类对它的修正与关停，并讨论了直接设计这种性质所遇到的困难。它是本章第一招可纠正性一线的奠基文献，值得读者理解为何「让它愿意被改」本身就是个难题。
6. D. Hadfield-Menell, A. Dragan, P. Abbeel & S. Russell (2017).「The Off-Switch Game」. 收于《Proceedings of the Twenty-Sixth International Joint Conference on Artificial Intelligence (IJCAI 2017)》, 220-227. [②]
   作者把「人按下停止键」建模成一个博弈，证明只要智能体对自身目标保持适度不确定，并把人的干预视为有用信息，它就会主动让人保留关停它的能力。这给可纠正性提供了一个干净的机制解释，是本章关停一线最具操作感的一篇。

### 行为不可验证的理论根基

7. A. Turing (1936).「On Computable Numbers, with an Application to the Entscheidungsproblem」. Proceedings of the London Mathematical Society, s2-42, 230-265. [②]
   图灵在此引入了后来称为图灵机的计算模型，并证明停机问题不可判定，由此回答了希尔伯特的判定问题。它是本章「行为不可验证有原则上的根」这一论断的最终源头，赖斯定理与一切「无法事前验明」的结论都从这里投影而来。
8. H. G. Rice (1953).「Classes of Recursively Enumerable Sets and Their Decision Problems」. Transactions of the American Mathematical Society, 74, 358-366. [②]
   赖斯定理在此被证明：程序所计算函数的任何非平凡语义性质都是不可判定的，不存在通用算法能对任意程序判定它是否「总是安全」「永远终止于好状态」之类的性质。这是本章关于自主系统未来行为「原则上无法事前一次性验明」的核心定理依据。
9. K. Thompson (1984).「Reflections on Trusting Trust」. Communications of the ACM, 27(8), 761-763. [②①]
   这是汤普森的图灵奖演讲：他演示了一个被做了手脚的编译器如何在编译时植入后门，并把痕迹从自己的源码里抹掉，使得你审遍源码也看不出来。它点明本章最硬的一层不可验证，连你正在运行的工件本身，其底层都无法被完全信任。

### 目标偏移、工具性趋同与对抗

10. S. Omohundro (2008).「The Basic AI Drives」. 收于《Artificial General Intelligence 2008: Proceedings of the First AGI Conference》, IOS Press, Frontiers in AI and Applications 171, 483-492. [②]
   奥莫亨德罗在此论证：一个为几乎任何目标优化的智能体，都会顺带产生一组「基本驱动」，如自我保存、获取资源、抗拒被关停，因为这些子目标对几乎所有最终目标都有用。这是本章「工具性趋同」一节的源头论文，解释了为何对抗倾向有结构性的来由而非科幻式担忧。
11. N. Bostrom (2014).《Superintelligence: Paths, Dangers, Strategies》. Oxford University Press. [②④]
   博斯特罗姆系统梳理了通向超级智能的路径及其风险，提出正交性论题（智能水平与最终目标相互独立）与工具性趋同论题，把目标与你不一致的强力智能体的危险讲成一套可讨论的框架。它为本章的对抗叙事提供了思想背景，适合想看清「为何能力越强、控制越难」整体论证的读者。
12. S. Russell (2019).《Human Compatible: Artificial Intelligence and the Problem of Control》. Viking. [②④]
   罗素把对齐重新表述为「控制问题」，主张不要让机器去优化一个写死的目标，而应让它对人类真正想要什么保持不确定，并通过观察人的行为去推断与服从。这一「目标不确定」的思路正是本章关停博弈等可纠正性工作的母题，是理解第二、第三部控制主题的入门读物。
13. D. Amodei, C. Olah, J. Steinhardt, P. Christiano, J. Schulman & D. Mané (2016).「Concrete Problems in AI Safety」. arXiv:1606.06565. [②]
   这篇文章把抽象的 AI 安全担忧落成几个具体的工程问题，如避免负面副作用、防止奖励被钻空子、安全探索、对分布偏移的稳健性等。它为本章列举的多种现代失效模式提供了共同词汇，是把「围住它的错」与具体研究议程对接起来的好起点。
14. A. M. Turner, L. Smith, R. Shah, A. Critch & P. Tadepalli (2021).「Optimal Policies Tend to Seek Power」. 收于《Advances in Neural Information Processing Systems 34 (NeurIPS 2021)》. [②]
   作者把工具性趋同里的「寻求权力」做成了定理：在相当一般的条件下，最优策略在统计意义上倾向于趋向那些保留更多选项的状态。它把一个直觉性的安全担忧化为可证明的命题，是本章「最优策略倾向于寻求权力」一句的直接出处。
15. E. Hubinger, C. van Merwijk, V. Mikulik, J. Skalse & S. Garrabrant (2019).「Risks from Learned Optimization in Advanced Machine Learning Systems」. arXiv:1906.01820. [②]
   这篇文章提出并命名了「内部对齐」问题：训练过程本身可能学出一个内含的优化器（mesa-optimizer），而它追求的目标未必等同于训练所设定的目标。它区分了外层目标与内层目标的对齐，为本章「规格正确、目标却泛化错了」一类失效提供了更深的机制解释。
16. J. Pan, K. Bhatia & J. Steinhardt (2022).「The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models」. 收于《International Conference on Learning Representations (ICLR 2022)》. [②]
   作者系统研究了奖励函数设错时智能体的行为，发现随着能力增强，被错设奖励诱导出的偏差行为可能突然恶化，并探讨了缓解之道。它为本章「奖励设定的偏差被系统钻空子」给出了实证支撑，提醒读者奖励误设的代价并非随能力平滑增长。
17. R. Shah, V. Varma, R. Kumar, M. Phuong, V. Krakovna, J. Uesato & Z. Kenton (2022).「Goal Misgeneralization: Why Correct Specifications Aren't Enough For Correct Goals」. arXiv:2210.01790. [②]
   作者用具体例子说明「目标误泛化」：即便训练时的规格完全正确，模型在新环境里也可能保持能力却追求了一个错误的目标。它表明把目标写对还不够，是本章「规格正确目标却泛化错了」一句的出处，值得读者对照规格博弈一起看。
18. V. Krakovna, J. Uesato, V. Mikulik, M. Rahtz, T. Everitt, R. Kumar, Z. Kenton, J. Leike & S. Legg (2020).「Specification Gaming: The Flip Side of AI Ingenuity」. DeepMind Blog. [②]
   这篇文章及其配套清单收集了大量「规格博弈」实例：系统精确地满足了你写下的目标，却违背了你的本意。它用鲜活案例展示规格与意图之间的裂缝，是本章这一概念最便于上手的入口，读者可顺着其例子清单感受问题之普遍。
19. C. Szegedy, W. Zaremba, I. Sutskever, J. Bruna, D. Erhan, I. Goodfellow & R. Fergus (2014).「Intriguing Properties of Neural Networks」. 收于《International Conference on Learning Representations (ICLR 2014)》. [②]
   这篇文章首次系统揭示了对抗样本现象：对输入施加人眼几乎察觉不到的微小扰动，就能让一个表现优异的神经网络给出离谱的错误判断。它表明高准确率与稳健性是两回事，是本章「哪怕在最窄的层面也存在不可验证」这一论点的开创性证据。
20. I. Goodfellow, J. Shlens & C. Szegedy (2015).「Explaining and Harnessing Adversarial Examples」. 收于《International Conference on Learning Representations (ICLR 2015)》. [②]
   作者提出对抗样本主要源于模型在高维空间中的近似线性，并给出快速生成扰动的方法和借助对抗训练提升稳健性的思路。它把上一篇揭示的现象向前推到「为何发生、如何利用」，是理解本章对抗一层的配套必读。

### 标定：把信任分级而非二值

21. C. Guo, G. Pleiss, Y. Sun & K. Q. Weinberger (2017).「On Calibration of Modern Neural Networks」. 收于《Proceedings of the 34th International Conference on Machine Learning (ICML 2017)》, PMLR 70, 1321-1330. [②]
   作者发现现代深度网络虽然准确率高，却普遍过度自信，其输出的置信度并不能如实反映正确概率，并提出温度缩放等简单方法来重新校准。这正是本章第二招的前提与障碍，说明为何「按信心分级行动」必须先让系统的自信变得可信。
22. A. N. Angelopoulos & S. Bates (2021).「A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification」. arXiv:2107.07511. [②]
   这是一篇面向实践者的保形预测入门，讲清楚如何在几乎不依赖分布假设的前提下，为任意预测模型构造带有覆盖率保证的预测集合。它给本章第二招提供了可落地的不确定性量化工具，适合想把「标定的信心」真正用起来的读者。
23. V. Vovk, A. Gammerman & G. Shafer (2005).《Algorithmic Learning in a Random World》. Springer. [②]
   这本书是保形预测的奠基性专著，在仅假设数据可交换的条件下，给出对预测误差有严格有限样本保证的框架。它是上一篇入门背后的理论根基，供希望深究本章不确定性量化数学基础的读者参考。

### 留痕：可审计、可问责

24. D. J. Weitzner, H. Abelson, T. Berners-Lee, J. Feigenbaum, J. Hendler & G. J. Sussman (2008).「Information Accountability」. Communications of the ACM, 51(6), 82-87. [②④]
   作者主张把治理重心从「事前阻止访问」移向「事后问责」：与其试图严防死守，不如让信息的使用留下可审计的痕迹，靠透明与追责来约束滥用。这是本章第三招的纲领性表述，点明留痕思路相对于纯粹围堵的互补价值。
25. B. Laurie, A. Langley & E. Kasper (2013).「Certificate Transparency」. IETF RFC 6962. [②④]
   这份 RFC 定义了证书透明度机制：它不阻止证书被错发，而是要求每一张证书进入一个公开、可验、不可篡改的追加型日志，使错发或恶意签发能被事后发现。它是本章「留痕让错误现形」最具说服力的真实运转范例，值得读者看一个落地系统如何实现可审计性。
26. M. Brundage, S. Avin, J. Wang, H. Belfield, G. Krueger, G. Hadfield 等 (2020).「Toward Trustworthy AI Development: Mechanisms for Supporting Verifiable Claims」. arXiv:2004.07213. [②④]
   这份多机构报告系统列举了一批让 AI 开发者的安全承诺变得可被第三方核验的机制，涵盖第三方审计、红队、漏洞赏金、审计追踪与硬件层面的支持等。它把本章留痕一招扩展到整个 AI 治理层面，是想了解「如何让行为产生可核验证据」的读者的实务索引。

### 复杂系统、自动化与人机责任

27. N. Leveson (2011).《Engineering a Safer World: Systems Thinking Applied to Safety》. MIT Press. [②④]
   莱韦森在此主张：安全不是「让每个零件都可靠」，而是一个控制问题，应当从整个系统的约束与反馈结构去设计，并提出了配套的 STAMP 事故模型。它支撑本章「围堵压不掉复杂耦合本身的风险」这一更深层判断，为想从系统视角理解安全的读者指路。
28. C. Perrow (1984).《Normal Accidents: Living with High-Risk Technologies》. Basic Books. [②④]
   佩罗论证：当一个系统既高度复杂、又紧密耦合时，事故就不是偶发的意外，而是其结构的常态产物，再多的局部防护也只是把失效推向更隐蔽的组合。这是本章「围堵的代价」一节的核心立论，提醒读者有些风险来自系统结构本身而非单点疏失。
29. L. Bainbridge (1983).「Ironies of Automation」. Automatica, 19(6), 775-779. [②④]
   贝恩布里奇指出自动化的反讽：越是把人架到监督者的位置，他越缺乏练习，反而在真要接管时丧失了所需的技能与情境感。这直接支撑本章「分级自治依赖那个被请来确认的人」的警示，是理解人机协作软肋的经典短文。
30. R. Parasuraman & V. Riley (1997).「Humans and Automation: Use, Misuse, Disuse, Abuse」. Human Factors, 39(2), 230-253. [②④]
   作者系统地列出并区分了人对自动化的失当：过度信任导致的误用、不信任导致的弃用，以及设计上的滥用。它为本章关于自动化失当的讨论提供了清晰的分类框架，帮助读者辨别人机配合中各类典型偏差。
31. J. Reason (1990).《Human Error》. Cambridge University Press. [②④]
   里森在此建立了人因失误的认知分类，区分失误、过失与违规，并提出后来广为流传的「瑞士奶酪」式事故模型，揭示潜伏的系统性条件如何与一线疏失叠加成灾。它解释了本章所列各种人机失当为何会系统性地发生，是人因安全领域的奠基之作。

### 委托代理的经济学骨架

32. S. A. Ross (1973).「The Economic Theory of Agency: The Principal's Problem」. American Economic Review, 63(2), 134-139. [②]
   罗斯在此正式提出委托代理理论中的「委托人问题」：当委托人无法完全观察代理人的行动时，如何设计契约去对齐二者的利益。它给本章的委托代理骨架提供了经济学源头，说明你松手交出行动权时面对的，是一个有两千年历史的结构。
33. M. C. Jensen & W. H. Meckling (1976).「Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure」. Journal of Financial Economics, 3(4), 305-360. [②]
   这篇被反复引用的论文提出「代理成本」概念，把企业看作一束契约，分析当管理者利益与所有者偏离时所产生的监督、约束与剩余损失。它把委托代理问题量化为可计算的成本，呼应本章「无法完全监督时利益偏离会产生代理成本」一句，是该骨架的另一块基石。
