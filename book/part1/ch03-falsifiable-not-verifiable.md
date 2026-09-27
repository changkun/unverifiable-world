# 第 3 章　可证伪，不可证实

> **论点**：经验科学是人类最有纪律的求知方式，而它建立在一个公开的承认之上：理论永远无法被证实（verification），至多只能做到尚未被证伪（falsification）。

上一章提出了一个问题：人类是否拥有一套成熟的、有纪律的方法，能够与不可验证性长期共处？答案是肯定的，这就是经验科学。最出人意料的是，它的首要原则并不是宣称自己能够查明真理，而是公开承认自己永远无法做到这一点。

## 一只黑天鹅

「所有天鹅都是白的。」即便观察过一千只、一百万只白天鹅，这个全称判断（universal statement）依然没有得到证实，因为下一只可能就是黑的。然而，只要见到一只黑天鹅，它便被彻底推翻。这并非虚构的例子。在欧洲，「天鹅皆白」长期被视为确定无疑的常识；直到 1697 年，荷兰探险队在西澳大利亚首次见到黑天鹅，这份「确定」才在一夜之间失效。

这种不对称是全章论证的支点。要证实一个全称命题，就必须检查它所断言的全部情形，而这些情形往往是无穷的、开放的、属于未来的，不可能穷尽。要证伪它，却只需要一个反例。用逻辑的语言表述：$\forall x\,P(x)$ 无法由有限的观察确立，而一个 $\exists x\,\lnot P(x)$ 就足以将它推翻。科学的全部纪律，都建立在认清并利用这种不对称的基础之上。

![证实与证伪的不对称](../figures/f03-falsification.svg)

<figure class="uvw-viz" data-static="f03-falsification" role="group" aria-label="证实与证伪的不对称交互图">
<div class="uvw-live" hidden>
<div class="uvw-claim">
<span class="uvw-claim-text">「所有天鹅都是白的」</span>
<span class="uvw-state uvw-state-open">尚未证伪</span>
</div>
<div class="uvw-bar" role="img" aria-label="确信度进度条">
<div class="uvw-bar-fill"></div>
<span class="uvw-bar-pct">0%</span>
</div>
<div class="uvw-swans" aria-hidden="true"></div>
<div class="uvw-controls">
<button type="button" class="uvw-btn uvw-btn-white">加一只白天鹅</button>
<button type="button" class="uvw-btn uvw-btn-black">加一只黑天鹅</button>
<button type="button" class="uvw-btn uvw-btn-reset">重来</button>
<span class="uvw-count">确认次数 <b class="uvw-v-count">0</b></span>
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
state.textContent='已证伪';
state.className='uvw-state uvw-state-broken';
vCount.textContent=n;
note.textContent='一只黑天鹅就足够了：一个反例即可否证全称命题，此前观察到的所有白天鹅都无法挽回。';
return;
}
var c=Math.min(conf(),CAP);
fill.style.width=c.toFixed(1)+'%';
pct.textContent=Math.round(c)+'%';
state.textContent=n===0?'尚未证伪':'仍未证实';
state.className='uvw-state uvw-state-open';
vCount.textContent=n;
if(n===0){note.textContent='点击「加一只白天鹅」，观察确信度如何逐步逼近，却始终达不到 100%。';}
else{note.textContent='第 '+n+' 只白天鹅：确信度升至 '+Math.round(c)+'%，仍未达到。确认再多，也无法证实这个全称命题。';}
}
function addSwan(cls){var s=document.createElement('span');s.className='uvw-swan '+cls;stream.appendChild(s);}
function setDisabled(d){bWhite.disabled=d;bBlack.disabled=d;}
bWhite.addEventListener('click',function(){if(falsified)return;n++;addSwan('white');render();});
bBlack.addEventListener('click',function(){if(falsified)return;falsified=true;addSwan('black');setDisabled(true);render();});
bReset.addEventListener('click',function(){n=0;falsified=false;stream.innerHTML='';setDisabled(false);render();});
render();
})();
</script>

## 休谟的归纳问题

这一不对称的根源，休谟在 1739 年<sup class="cite"><a href="#ref-4">4</a></sup>就已揭示。我们凭什么相信，过去一直成立的规律将来仍会成立？在逻辑上，这一信念没有依据。从「太阳过去每天都升起」推不出「太阳明天一定升起」，因为这一推论已经预设了「过去的模式会延续到未来」，而这恰是有待证明之事。归纳（induction）没有逻辑上的保证。休谟的结论冷静而彻底：我们所依靠的不是证明，而是习惯。

这便是第 1 章所说「未来」这道裂口的哲学根基。任何关于世界普遍规律的知识，都建立在有限的过去之上，因而都无法在事前得到证实。科学若要成为知识，就不能以「证实」为目标，因为这一目标无从企及。

## 波普尔：以证伪代替证实

波普尔在 1934 年<sup class="cite"><a href="#ref-1">1</a></sup>（德文原版）指出了一条出路：既然证实不可得，那就放弃证实，转而诉诸证伪。一个理论是否科学，不取决于它能得到多少证据的支持（支持总是找得到的），而取决于它是否甘冒风险，作出可能被推翻的预测。占星术，以及那些对一切现象都能自圆其说的学说，是不可证伪的，因而不属于科学。广义相对论预言，星光会被太阳的引力偏折一个确定的角度；1919 年的日食观测完全可能测出别的数值，从而推翻这一预言。正因为这一理论甘冒被推翻的风险，它才是好的科学。

由此，科学成为一台专为「与不可验证性共处」而优化的机器。它从不宣称证明了什么，只是说：这个理论迄今尚未被证伪，因此我们暂且采用它。这是一种认识上的姿态：以可以检验的「尚未被推翻」，替换无法检验的「真」。这一姿态在后文还会出现：第 7 章那位数学家所做的代理替换，放到认识论的尺度上，就是这个样子。

## 一句必要的限定

这里有必要明确一点：波普尔式的证伪主义（falsificationism）在科学哲学中远非定论。本书把它当作一个清晰的入口，而不是终点。

对证伪主义最有力的反驳，来自迪昂与蒯因的整体论（holism，又称 Quine-Duhem 论题）。迪昂在 1906 年<sup class="cite"><a href="#ref-10">10</a></sup>、蒯因在 1951 年<sup class="cite"><a href="#ref-9">9</a></sup>先后指出，任何假说都无法被孤立地检验。每一个预测都依赖于大量辅助假定：仪器运转正常，背景条件成立，近似处理合理。实验一旦失败，研究者总可以把矛头指向某一个辅助假定，从而保全核心假说。因此，「一个反例就干净利落地推翻理论」这幅图景，远不像表面上那样干净。

库恩在 1962 年<sup class="cite"><a href="#ref-5">5</a></sup>更进一步：在常规科学时期，科学家并不急于证伪，反常往往被暂时搁置，直到范式（paradigm）陷入危机，才发生革命式的更替。此后，拉卡托斯在 1970 年<sup class="cite"><a href="#ref-6">6</a></sup>以「研究纲领」（research programme）的进步与退化，取代了非此即彼的证伪标准；费耶阿本德<sup class="cite"><a href="#ref-7">7</a></sup>则更为激进，反对一切统一的方法。

另一条路径是贝叶斯确证论（Bayesian confirmation theory）<sup class="cite"><a href="#ref-24">24</a></sup>：它不作非此即彼的判决，而把证据看作对信念概率的调整，

$$P(H\mid e)=\frac{P(e\mid H)\,P(H)}{P(e)},$$

这也预示了后文的「校准」这一对策。梅奥提出的「严苛检验」（severe testing）<sup class="cite"><a href="#ref-14">14</a></sup>，是证伪主义一个精致的继承者；斯坦福<sup class="cite"><a href="#ref-19">19</a></sup>则提醒我们，在视野之外，还有大量「未被设想的替代方案」（unconceived alternatives）。

列举这些争论，并不是为了驳倒波普尔。本书自身也应当如此行事：提出一个有力的框架，同时标明它的边界。全书所要身体力行的，也就是这种姿态。

## 科学早已发现的几种对策

本节是本章对全书真正的贡献。倘若以「八种对策」的眼光审视科学日常运转所依赖的那套制度，便会发现，科学早已摸索出其中的好几种，只是冠以别的名称。

同行评审体现的是冗余与共识：它不信任单个判断者，而是邀请多位相互独立的审稿人，取其一致意见。重复实验同样属于冗余：一个结果必须由他人在别处独立重现，才会被认真对待。预注册（preregistration）相当于留痕：在看到数据之前便将假说与分析方案登记在案，事后既无法移动靶子，也无法把噪声说成信号。置信区间与误差统计则是证书与界：它们并不声称命题为真，而只是在一个明确的置信水平上给出有界的保证。双盲与随机化，是针对第五种处境（对抗）的防御，只不过这里的对手，往往是研究者自身的偏见与主观期待。显著性阈值则是一种粗糙的校准。

换言之，人类最严肃的求知事业，就是本书收敛命题的一个鲜活例证。这是全书给出的第一个提示，而且分量很重：科学所面对的不可验证性（关于普遍规律、关于未来）有其特定的来源，而它不得不采取的应对，却与软件、数学和组织中的应对押着同一个韵。

## 当机器失灵：可重复性危机

从反面看，这一点更为清楚。这些对策一旦被削弱，科学的自我纠错机制便会失灵，这就是可重复性危机（replication crisis）。2005 年，约阿尼迪斯<sup class="cite"><a href="#ref-28">28</a></sup>发表了题为「为什么大多数已发表的研究结论是假的」的论文；2015 年，开放科学合作组织<sup class="cite"><a href="#ref-29">29</a></sup>对一百项心理学研究进行了大规模重复。二者所揭示的，是同一幅图景。那一百项研究中，97% 当初都报告了显著结果；重复之后，只有约三十六项仍然成立，不到一半。只要预注册缺位（靶子可以事后移动），样本量不足，发表偏倚只放行漂亮的结果，而吃力不讨好的重复研究又乏人问津，这台机器就会空转。

对这场危机的诊断与修补，所用的同样是这几种对策的语言：恢复预注册（重新引入留痕），鼓励并奖励重复研究（重新引入冗余），采用登记报告，提高检验的严苛程度。问题与药方，落在同一套词汇之中。第 10 章讨论借来的判断、第 12 章讨论留痕与审计时，还将回到这一点。

## 小结

科学证明了一点：人能够在缺乏验证的世界中有纪律地求知，而凡是做得好的地方，所依靠的都是那几种对策。就此而言，科学为全书提供了一个概念验证。

然而，这里也潜伏着一个陷阱。五种处境都以同一副面目出现，即「我无法检验它」；应对它们的对策又如此相似。于是，一个极具诱惑力的念头便会产生：何不径直宣布，不可验证性就是一个问题，只需配上一个统一的解法？这一念头关于「问题」的部分是错误的，关于「应对」的部分却不期然地切中了要害。下一章将专门处理这一诱惑。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实。

1. K. Popper (1959).《The Logic of Scientific Discovery》. Hutchinson. [Google Books](https://books.google.com/books?id=iucRkAEACAAJ) [②③]
   波普尔在此系统提出证伪主义：科学理论无法被经验证实，只能被否证，可证伪性因而成为科学与非科学的分界。德文原版《Logik der Forschung》由维也纳 Springer 出版，版权页标 1935 而实际 1934 年底面世（故常记作 1934），这部英文版由作者亲自大幅修订增补。本章「波普尔：以证伪代替证实」一节直接建基于此，读者应着重领会以「尚未被证伪」替换「证实」的认识论姿态。

2. K. Popper (1963).《Conjectures and Refutations: The Growth of Scientific Knowledge》. Routledge and Kegan Paul. [Google Books](https://books.google.com/books?id=IENmxiVBaSoC) [③]
   这部论文集把证伪主义铺展为一整套知识增长观：知识经由大胆猜想与无情反驳而前进，科学的成长不是积累确证，而是不断淘汰错误。比起前作的逻辑骨架，它更直观地展示了「试错」如何驱动科学进展，是理解本章「科学如何进展」这一落足点的好读物。

3. K. Popper (1972).《Objective Knowledge: An Evolutionary Approach》. Clarendon Press. [Google Books](https://books.google.com/books?id=o8oPAQAAIAAJ) [③]
   波普尔在此把知识增长类比为演化式的试错过程，并提出「第三世界」即客观知识本身的领域，独立于个人的主观心智而存在。它把证伪主义推向一种关于客观知识如何无主体地积累的本体论图景，可供有意深究「科学如何进展」的读者延伸阅读。

4. D. Hume (1739).《A Treatise of Human Nature》. John Noon. [Google Books](https://books.google.com/books?id=JzRgzQEACAAJ) [②]
   休谟在此提出归纳问题这一源头性难题：从过去的规律推不出未来的规律，因为这一推论本身预设了「自然齐一」，而那正是待证之事；我们对因果与规律的信念，归根到底来自习惯而非证明。第一、二卷 1739 年由 John Noon 出版，第三卷《Of Morals》1740 年由 Thomas Longman 出版，通常以 1739 标记初版。本章「休谟的归纳问题」一节即奠基于此，是理解科学为何无法以「证实」为目标的哲学底座。

5. T. Kuhn (1962).《The Structure of Scientific Revolutions》. University of Chicago Press. [Google Books](https://books.google.com/books?id=3eP5Y_OOuzwC) [①③]
   库恩借大量科学史案例论证：科学并非匀速逼近真理，而是在「常规科学」时期于一个共享范式内解谜，反常累积到危机后才发生范式更替式的科学革命，且新旧范式之间存在不可通约。它是对波普尔图景的重要修正，说明科学家常常并不急于证伪反常，本章「一句必要的限定」即引此标出证伪主义的边界。

6. I. Lakatos (1970).「Falsification and the Methodology of Scientific Research Programmes」. 收于 I. Lakatos, A. Musgrave 编《Criticism and the Growth of Knowledge》, pp. 91-196. Cambridge University Press. doi:[10.1017/cbo9781139171434.009](https://doi.org/10.1017/cbo9781139171434.009) [①③]
   拉卡托斯以「研究纲领」调和波普尔与库恩：每个纲领有一个受保护的硬核与一圈可调整的辅助假定，评判标准不是单个反例，而是纲领整体随时间是「进步」（持续做出并兑现新预测）还是「退化」（只忙于事后打补丁）。它把非黑即白的证伪换成对纲领进退的历史判断，是本章界定证伪主义边界时的关键参照。

7. P. Feyerabend (1975).《Against Method: Outline of an Anarchistic Theory of Knowledge》. New Left Books. [Google Books](https://books.google.com/books?id=XL_GAAAAIAAJ) [①③④]
   费耶阿本德以伽利略等科学史案例力证：并不存在一套普遍有效的科学方法，重大进展往往恰恰来自违反既有规则，故其著名口号是「怎么都行」。它是对统一方法论最激进的反对，本章引它来标明：连「证伪」这样温和的方法论主张，也有人从根本上拒斥。

8. C. G. Hempel (1965).《Aspects of Scientific Explanation and Other Essays in the Philosophy of Science》. Free Press. [Google Books](https://books.google.com/books?id=BjzbAAAAMAAJ) [②]
   亨佩尔在这部论文集里集大成地阐发科学解释的覆盖律模型，既包括演绎律则式解释，也包括归纳统计式解释，并讨论了确证的逻辑及其悖论。它代表了逻辑经验主义对「理论上被研究过的东西」的系统刻画，为本章关于何为可被检验、可被解释提供了经典背景。

9. W. V. O. Quine (1951).「Two Dogmas of Empiricism」.《The Philosophical Review》, 60(1), 20-43. doi:[10.2307/2181906](https://doi.org/10.2307/2181906) [②]
   蒯因攻击逻辑经验主义的两条教条：分析与综合的截然二分，以及还原论；并提出认识论整体论，主张我们的信念作为一张整体之网共同面对经验，没有哪个陈述能被孤立地证实或否证。结合迪昂的检验整体论（合称 Quine-Duhem 论题），它直接冲击「一个反例干净利落地推翻一个假说」的图景，是本章界定证伪主义边界的核心文献。

10. P. Duhem (1906).《La théorie physique: son objet, sa structure》. Chevalier & Rivière. [Google Books](https://books.google.com/books?id=v3IlAAAAMAAJ) [②]
   迪昂在此提出检验整体论：物理学中的实验从不检验孤立假说，而是检验「假说连同一整套辅助假定与背景理论」，因此一次失败的预测无法判定究竟错在何处。此即后来与蒯因合称的整体论之源头，本章用以说明反例的指向并不像表面那样确定。此处以原始法文版 1906 年为准，第二版 1914 年由 Marcel Rivière 出版，P. P. Wiener 英译《The Aim and Structure of Physical Theory》由 Princeton University Press 1954 年刊行。

11. M. Polanyi (1958).《Personal Knowledge: Towards a Post-Critical Philosophy》. University of Chicago Press. [Google Books](https://books.google.com/books?id=QPPIBQAAQBAJ) [①④]
   波兰尼提出「默会知识」：我们知道的远多于我们能言说的，科学探究中始终有一层无法形式化、只能在实践与师承中习得的个人判断与技艺。它提醒人们，再严格的方法论也无法消去科学家亲身的、不可言传的判断，呼应本章「历史上科学家的判断」与「如何在无法验证的世界里生活」两个落足点。

12. B. C. van Fraassen (1980).《The Scientific Image》. Clarendon Press. doi:[10.1093/0198244274.001.0001](https://doi.org/10.1093/0198244274.001.0001) [②④]
   范弗拉森提出「建构经验论」：科学的目标不是宣称理论为真，而只是「经验适当」，即正确地拯救可观察现象；接受一个理论意味着相信它经验适当，而非相信其不可观察部分确实存在。它把「不可证实」转化为一种成熟的科学态度，与本章把「真」替换为「尚未被推翻」的姿态彼此呼应。

13. I. Hacking (1983).《Representing and Intervening: Introductory Topics in the Philosophy of Natural Science》. Cambridge University Press. doi:[10.1017/cbo9780511814563](https://doi.org/10.1017/cbo9780511814563) [②③]
   哈金把哲学注意力从「表征」转向「干预」，主张实在论的最佳辩护不在理论而在实验：当我们能稳定地操纵电子去探测别的东西时，电子就是真实的（「能喷射，便是真」）。它为科学实在论开辟了以实验实践为基础的新进路，也提醒读者科学进展同样依赖动手干预而非只靠理论检验。

14. D. G. Mayo (1996).《Error and the Growth of Experimental Knowledge》. University of Chicago Press. doi:[10.7208/chicago/9780226511993.001.0001](https://doi.org/10.7208/chicago/9780226511993.001.0001) [③]
   梅奥提出「误差统计」哲学：一个假说只有当它通过了「若为假则极可能不通过」的严苛检验时，我们才有理由接受它。这把波普尔的证伪精神落实为可操作的统计检验程序，是证伪主义一个精致的继承者，本章「严苛检验」一说即源于此（属 Science and Its Conceptual Foundations 丛书）。

15. D. G. Mayo (2018).《Statistical Inference as Severe Testing: How to Get Beyond the Statistics Wars》. Cambridge University Press. doi:[10.1017/9781107286184](https://doi.org/10.1017/9781107286184) [③④]
   梅奥在此以「严苛性」为统一原则重构统计推断，试图越过频率派与贝叶斯派长期的「统计之战」，并据此回应可重复性危机中对显著性检验的批评。它把第 14 项的纲领发展为面向当代统计实践的方法论，对理解如何在不可验证的世界里负责任地使用统计证据尤为切题。

16. L. Laudan (1981).「A Confutation of Convergent Realism」.《Philosophy of Science》, 48(1), 19-49. doi:[10.1086/288975](https://doi.org/10.1086/288975) [①②]
   劳丹列举科学史上一批曾经成功（能预测、能解释）却最终被抛弃的理论，如燃素说、以太说，论证「成功蕴含为真」的推断站不住脚，对收敛实在论构成有力反驳，常被称为「悲观元归纳」。它说明就连经验上很成功的理论也未必接近真理，强化了本章关于科学不以「证实真理」为目标的论点。

17. L. Laudan (1977).《Progress and Its Problems: Towards a Theory of Scientific Growth》. University of California Press. [Google Books](https://books.google.com/books?id=TMuXQgAACAAJ) [③]
   劳丹主张以「问题求解能力」而非逼近真理来衡量科学进步：一个研究传统是否进步，取决于它解决的经验问题与概念问题之净增量。它给出了一种绕开真理概念的进步观，为本章「科学如何进展」提供了一个不依赖证实的替代框架。

18. P. Kitcher (1993).《The Advancement of Science: Science without Legend, Objectivity without Illusions》. Oxford University Press. [Google Books](https://books.google.com/books?id=H3U8DwAAQBAJ) [③]
   基切尔在抛弃科学全知全能的「传说」之后，又拒绝相对主义，转而从科学的社会与认知实践出发重建一种温和而可辩护的客观性与进步观。它示范了如何在承认科学受历史与社会影响的同时，仍守住进步与客观这两个概念，与本章既肯定科学又把边界标清的立场一脉相承。

19. P. K. Stanford (2006).《Exceeding Our Grasp: Science, History, and the Problem of Unconceived Alternatives》. Oxford University Press. doi:[10.1093/0195174089.001.0001](https://doi.org/10.1093/0195174089.001.0001) [①②③④]
   斯坦福提出「未被设想的替代方案」问题：科学史一再表明，过去的科学家总有一些后来才出现、当时根本想不到的理论选项，故我们没有理由相信今天已穷尽了所有可行解释。他以遗传学等史案归纳出这一「新归纳」，直接呼应本书「无法验证的世界」之框架，提醒读者视野之外总有未及设想的可能。

20. N. Goodman (1955).《Fact, Fiction, and Forecast》. Harvard University Press. [Google Books](https://books.google.com/books?id=DcfmEAAAQBAJ) [②]
   古德曼提出「归纳的新谜题」：用「绿」与人造谓词「绿蓝」（grue，意为在某时间点前观察为绿、其后为蓝）同样能拟合迄今全部观察，却导出相反预测，可见归纳无法仅凭证据决定，还须依赖哪些谓词「可投射」。它说明归纳的困难不止于休谟式的辩护问题，更在于规律本身的不确定，深化了本章对归纳何以不可靠的理解。初版年份通行作 1955（HUP 一处简介称 1954，存在轻微歧义，此处从广引的 1955）。

21. C. G. Hempel, P. Oppenheim (1948).「Studies in the Logic of Explanation」.《Philosophy of Science》, 15(2), 135-175. doi:[10.1086/286983](https://doi.org/10.1086/286983) [②]
   亨佩尔与奥本海姆在此奠定演绎律则（D-N）解释模型：一个现象得到科学解释，意味着它能从普遍定律加初始条件中逻辑地推演出来。它是二十世纪科学解释理论的起点，界定了「能被解释」在逻辑上意味着什么，为本章关于科学如何刻画规律提供了底层框架。

22. R. Carnap (1936-1937).「Testability and Meaning」.《Philosophy of Science》, 3(4), 419-471; 4(1), 1-40. doi:[10.1086/286432](https://doi.org/10.1086/286432) [②]
   卡尔纳普在此放松严格的可证实原则，改用更宽的「可检验性」与「可确认性」来界定有意义的经验陈述，并以倾向性谓词等技术处理理论词项与观察的联系。它记录了逻辑经验主义从「可证实」向「可检验」的关键退却，正与本章「证实够不着、改用够得着的」这一主线相呼应。原文分两期刊出，第 3 卷第 4 期（1936）与第 4 卷第 1 期（1937）。

23. W. C. Salmon (1984).《Scientific Explanation and the Causal Structure of the World》. Princeton University Press. doi:[10.1515/9780691221489](https://doi.org/10.1515/9780691221489) [②]
   萨蒙主张科学解释的核心不是逻辑推演而是揭示因果机制：解释一个现象，是把它嵌入世界的因果过程与因果相互作用之网。它是对覆盖律模型的重要修正，把「能解释」的标准从可推演转向可追溯的因果结构，为本章理解科学如何刻画世界补上因果这一维度。

24. C. Howson, P. Urbach (1989).《Scientific Reasoning: The Bayesian Approach》. Open Court. [Google Books](https://books.google.com/books?id=iYoQAQAAIAAJ) [②③]
   豪森与厄巴赫系统主张贝叶斯主义的科学推理观：不作非真即假的二值判决，而把证据看作按贝叶斯定理对信念概率的连续调整，并以此回应归纳与确证的诸多难题。它是本章正文提到的贝叶斯确证论的代表性论著，与证伪、严苛检验形成对照，也预告了全书的「校准」这一对策。

25. E. Sober (2008).《Evidence and Evolution: The Logic Behind the Science》. Cambridge University Press. doi:[10.1017/cbo9780511806285](https://doi.org/10.1017/cbo9780511806285) [②]
   索伯以似然论与统计推断的工具细致分析「证据支持什么」，并讨论何种假说才真正可检验，其中包含对智能设计为何不可检验的剖析。它把抽象的可检验性问题落到具体的科学推断实践（尤以进化论为例），示范了如何严格判断一个主张是否经得起证据的检验。

26. P. Godfrey-Smith (2003).《Theory and Reality: An Introduction to the Philosophy of Science》. University of Chicago Press. doi:[10.7208/chicago/9780226300610.001.0001](https://doi.org/10.7208/chicago/9780226300610.001.0001) [②③]
   戈弗雷-史密斯这部广受好评的科学哲学导论，清晰梳理了从逻辑经验主义、证伪主义、库恩范式到贝叶斯主义与科学实在论之争的整条脉络。它适合作为本章诸多论题的导论性锚点，读者若想在阅读专著之前先建立全局地图，可由此入手。

27. N. Cartwright (1983).《How the Laws of Physics Lie》. Clarendon Press. doi:[10.1093/0198247044.001.0001](https://doi.org/10.1093/0198247044.001.0001) [②③]
   卡特赖特论证物理学的基本定律之所以普适而优美，恰恰因为它们并不如实描述真实世界，而是描述高度理想化的模型；越基本的定律解释力越强，描述上反而越「说谎」。她转而看重更贴近现象的具体定律与因果能力，提醒读者科学定律之「真」远比通常设想的复杂，深化了本章对理论与世界关系的省思。

28. J. P. A. Ioannidis (2005).「Why Most Published Research Findings Are False」.《PLoS Medicine》, 2(8), e124. doi:[10.1371/journal.pmed.0020124](https://doi.org/10.1371/journal.pmed.0020124) [③④]
   约阿尼迪斯用简明的统计建模论证：在效应量小、研究设计灵活、发表偏倚盛行的领域，一个已发表「阳性」结论为假的概率往往高于为真，假阳性可以系统性地多于真阳性。它是可重复性危机的奠基文献，正是本章「当机器失灵」一节的核心证据，说明科学的自我纠错一旦被削弱会如何空转。

29. Open Science Collaboration (2015).「Estimating the Reproducibility of Psychological Science」.《Science》, 349(6251), aac4716. doi:[10.1126/science.aac4716](https://doi.org/10.1126/science.aac4716) [③④]
   开放科学合作组织协同上百名研究者，对一百项已发表的心理学研究做了系统性的直接重复，结果能成功重现原效应的不到半数，且重现出的效应普遍弱于原报告。它把可重复性危机从论证变为大规模实证，是本章「可重复性危机」一节的实证核心，也凸显了重复与预注册这些对策为何不可或缺。
