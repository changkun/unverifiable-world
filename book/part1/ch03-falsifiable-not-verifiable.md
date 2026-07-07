# 第 3 章　可证伪，不可证实

> **论点**：人类最有纪律的求知方式（经验科学），建立在一个公开的承认上：理论永不可被证实（verification），只能不被证伪（falsification）。

上一章问，人类有没有一套成熟的、有纪律的办法与不可验证长期共处。有，那就是经验科学。而它最让人意外的地方在于，它的首要原则不是宣称自己能查明真理，恰恰是公开承认自己永远做不到。

## 一只黑天鹅

「所有天鹅都是白的。」你看过一千只白天鹅，看过一百万只，这个全称判断（universal statement）依然没有被证实，因为下一只可能是黑的。但你只要看见一只黑天鹅，它就被彻底推翻了。这并不是个虚构的例子：在欧洲，「天鹅皆白」长期被当作确定无疑的常识，直到 1697 年荷兰探险队在西澳大利亚第一次见到黑天鹅，那份「确定」一夜之间作废。

这道不对称是整章的支点。证实一个全称命题需要检遍它所断言的全部情形，而那往往是无穷的、开放的、属于未来的，根本做不到。但证伪它，却只需要一个反例。用逻辑写出来：$\forall x\,P(x)$ 无法被有限的观察确立，但一个 $\exists x\,\lnot P(x)$ 就足以将其击碎。科学的全部纪律，就建立在认清并利用这道不对称之上。

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
note.textContent='一只黑天鹅就够了。全称命题在一个反例前彻底关闭，之前所有的白天鹅都补不回来。';
return;
}
var c=Math.min(conf(),CAP);
fill.style.width=c.toFixed(1)+'%';
pct.textContent=Math.round(c)+'%';
state.textContent=n===0?'尚未证伪':'仍未证实';
state.className='uvw-state uvw-state-open';
vCount.textContent=n;
if(n===0){note.textContent='点「加一只白天鹅」，看确信度如何步步逼近，却永远够不到 100%。';}
else{note.textContent='第 '+n+' 只白天鹅：确信度升到 '+Math.round(c)+'%，仍差一口气。再多确认，也验证不了这个全称命题。';}
}
function addSwan(cls){var s=document.createElement('span');s.className='uvw-swan '+cls;stream.appendChild(s);}
function setDisabled(d){bWhite.disabled=d;bBlack.disabled=d;}
bWhite.addEventListener('click',function(){if(falsified)return;n++;addSwan('white');render();});
bBlack.addEventListener('click',function(){if(falsified)return;falsified=true;addSwan('black');setDisabled(true);render();});
bReset.addEventListener('click',function(){n=0;falsified=false;stream.innerHTML='';setDisabled(false);render();});
render();
})();
</script>

## 休谟那道过不去的坎

这件事的根，休谟在 1739 年<sup class="cite"><a href="#ref-4">4</a></sup>就刨到了。我们凭什么相信，过去一直成立的规律未来还会成立？没有逻辑上的凭据。从「太阳过去每天升起」推不出「太阳明天必升」，因为这个推论本身就预设了「过去的模式会延续到未来」，而这恰是待证的东西。归纳（induction）没有逻辑保证。休谟的结论冷静而彻底，我们依赖的不是证明，是习惯。

这正是第 1 章那「未来」之裂口的哲学底座。任何关于世界普遍规律的知识都建立在有限的过去之上，因而都无法被事前证实。科学若想成为知识，就不能把「证实」当作目标，那个目标根本够不着。

## 波普尔：把够不着的换成够得着的

波普尔在 1934 年<sup class="cite"><a href="#ref-1">1</a></sup>（德文原版）给出了出路：既然证实不可得，就别要它，改用证伪。一个理论是不是科学的，不看它能被多少证据支持（支持总能找到），而看它有没有把脖子伸出来、做出可能被推翻的、有风险的预测。占星术、对一切都自圆其说的学说不可证伪，因而不科学；广义相对论预言星光会被太阳引力偏折一个具体的角度，1919 年的日食观测原本完全可能测出别的数值、从而推翻这个预言，正因为理论敢于冒被推翻的风险，它才是好科学。

于是科学成了一台为「与不可验证共处」专门优化的机器。它从不宣称证明了什么，只说这个理论至今尚未被证伪，所以我们暂且用它。这是一种姿态，一种把测不出的「真」换成测得出的「尚未被推翻」的姿态。眼熟吗？这正是第 7 章那个数学家的代理替换在认识论尺度上的样子。

## 一句必要的限定

必须就地说清：波普尔式的证伪主义（falsificationism）在科学哲学里远非定论，本书把它当作一个清晰的入口，而不是终点。

它最有力的反对来自迪昂与奎因的整体论（holism，又称 Quine-Duhem 论题）。迪昂 1906 年<sup class="cite"><a href="#ref-10">10</a></sup>、奎因 1951 年<sup class="cite"><a href="#ref-9">9</a></sup>指出，你从来无法孤立地检验一个假说。任何预测都依赖一大堆辅助假定（仪器没坏、背景条件成立、近似合理），实验一旦失败，你永远可以把矛头引向某个辅助假定、而保住核心假说。于是「一个反例就干净利落地推翻理论」这幅图景并不像它看上去那么干净。库恩 1962 年<sup class="cite"><a href="#ref-5">5</a></sup>进一步说，常规科学时期的科学家根本不急着证伪，反常会被搁置，直到范式（paradigm）危机才发生革命式的更替；拉卡托斯 1970 年<sup class="cite"><a href="#ref-6">6</a></sup>用「研究纲领」（research programme）的进步与退化来取代非黑即白的证伪；费耶阿本德<sup class="cite"><a href="#ref-7">7</a></sup>干脆反对一切统一方法。另一条路径是贝叶斯确证论（Bayesian confirmation theory）<sup class="cite"><a href="#ref-24">24</a></sup>，它不要二值的判决，而把证据看作对信念概率的调整，

$$P(H\mid e)=\frac{P(e\mid H)\,P(H)}{P(e)},$$

这又预告了后面「标定」那一招。梅奥的「严苛检验」（severe testing）<sup class="cite"><a href="#ref-14">14</a></sup>是证伪主义一个精致的继承者，而斯坦福<sup class="cite"><a href="#ref-19">19</a></sup>则提醒我们还有大量「未被设想的替代方案」（unconceived alternatives）在视野之外。

把这些争论摆出来，不是要拆波普尔的台，而是因为这本书自己就该这样行事：陈述一个有力的框架，同时把它的边界标出来。这种姿态正是全书要演练的那一招。

## 科学早已发现了那几招

现在是这一章给全书的真正馈赠。如果你带着「八招」的眼光去看科学的日常建制，会发现它早就把其中好几招摸索出来，只是用着别的名字。

同行评审是冗余与共识，不信任单个判断者，而用多个互相独立的评审、取其一致。重复实验也是冗余，一个结果要等别人在别处独立重现才被当真。预注册（preregistration）是留痕，在看到数据之前就把假说和分析方案登记下来、事后无法移动靶子、不能把噪声讲成信号。置信区间与误差统计是证书与界，不声称命题为真，只在一个明确的置信水平上给出一个有界的保证。双盲与随机化是对付第五种处境（对抗）的防御，而这里的对手往往是研究者自己的偏见与主观期待。显著性阈值是一种粗糙的标定。

换句话说，人类最严肃的求知事业本身就是本书那个收敛命题的一个活样本。这是全书第一个、也是分量很重的暗示，尽管科学面对的不可验证（关于普遍规律、关于未来）有其特定来源，它被逼出来的应对和软件、数学、组织里的应对押着同一个韵。

## 当机器失灵：复制危机

反过来看更清楚。当这些招数被削弱，科学的自我纠错就会失效，这就是复制危机（replication crisis）。约阿尼迪斯 2005 年<sup class="cite"><a href="#ref-28">28</a></sup>那篇「为什么大多数已发表的研究结论是假的」、开放科学合作组织 2015 年<sup class="cite"><a href="#ref-29">29</a></sup>对一百项心理学研究的大规模重复（原研究里 97% 当初都报告了显著结果，重做之后只有约三十六项还成立，连一半都不到）揭开的正是这一幕，当预注册缺位（靶子可以事后挪动）、样本量不足、发表偏倚只放行漂亮结果、又少有人去做吃力不讨好的重复时，那台机器就空转了。

这场危机的诊断与修补恰恰是用那几招的语言进行的，恢复预注册（把留痕装回去）、鼓励并奖励重复（把冗余装回去）、登记报告、提高检验的严苛度。问题与药方都落在同一套词汇上。这一点在第 10 章谈借来的判断、第 12 章谈留痕与审计时还会回来。

## 这一章通向哪里

科学证明了一件事，人可以有纪律地在没有验证的世界里求知，而且但凡做得好，靠的就是那几招。这是全书的一个概念验证。

但这里也潜伏着一个陷阱。正因为这五种处境都以「我没法检验它」的同一副表情出现，又正因为应对它们的招数如此相似，一个极具诱惑力的念头会冒出来：何不干脆宣布，不可验证就是一个问题、配一个统一的解法？这个念头关于「问题」的部分是错的，关于「应对」的部分却歪打正着。下一章专门处理这个诱惑。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实。

1. K. Popper (1959).《The Logic of Scientific Discovery》. Hutchinson. [②③]
   波普尔在此系统提出证伪主义：科学理论无法被经验证实，只能被否证，可证伪性因而成为科学与非科学的分界。德文原版《Logik der Forschung》由维也纳 Springer 出版，版权页标 1935 而实际 1934 年底面世（故常记作 1934），这部英文版由作者亲自大幅修订增补。本章「波普尔：把够不着的换成够得着的」一节直接建基于此，读者应着重领会以「尚未被证伪」替换「证实」的认识论姿态。

2. K. Popper (1963).《Conjectures and Refutations: The Growth of Scientific Knowledge》. Routledge and Kegan Paul. [③]
   这部论文集把证伪主义铺展为一整套知识增长观：知识经由大胆猜想与无情反驳而前进，科学的成长不是积累确证，而是不断淘汰错误。比起前作的逻辑骨架，它更直观地展示了「试错」如何驱动科学进展，是理解本章「科学如何进展」这一落足点的好读物。

3. K. Popper (1972).《Objective Knowledge: An Evolutionary Approach》. Clarendon Press. [③]
   波普尔在此把知识增长类比为演化式的试错过程，并提出「第三世界」即客观知识本身的领域，独立于个人的主观心智而存在。它把证伪主义推向一种关于客观知识如何无主体地积累的本体论图景，可供有意深究「科学如何进展」的读者延伸阅读。

4. D. Hume (1739).《A Treatise of Human Nature》. John Noon. [②]
   休谟在此提出归纳问题这一源头性难题：从过去的规律推不出未来的规律，因为这一推论本身预设了「自然齐一」，而那正是待证之事；我们对因果与规律的信念，归根到底来自习惯而非证明。第一、二卷 1739 年由 John Noon 出版，第三卷《Of Morals》1740 年由 Thomas Longman 出版，通常以 1739 标记初版。本章「休谟那道过不去的坎」一节即奠基于此，是理解科学为何无法以「证实」为目标的哲学底座。

5. T. Kuhn (1962).《The Structure of Scientific Revolutions》. University of Chicago Press. [①③]
   库恩借大量科学史案例论证：科学并非匀速逼近真理，而是在「常规科学」时期于一个共享范式内解谜，反常累积到危机后才发生范式更替式的科学革命，且新旧范式之间存在不可通约。它是对波普尔图景的重要修正，说明科学家常常并不急于证伪反常，本章「一句必要的限定」即引此标出证伪主义的边界。

6. I. Lakatos (1970).「Falsification and the Methodology of Scientific Research Programmes」. 收于 I. Lakatos, A. Musgrave 编《Criticism and the Growth of Knowledge》, pp. 91-196. Cambridge University Press. [①③]
   拉卡托斯以「研究纲领」调和波普尔与库恩：每个纲领有一个受保护的硬核与一圈可调整的辅助假定，评判标准不是单个反例，而是纲领整体随时间是「进步」（持续做出并兑现新预测）还是「退化」（只忙于事后打补丁）。它把非黑即白的证伪换成对纲领进退的历史判断，是本章界定证伪主义边界时的关键参照。

7. P. Feyerabend (1975).《Against Method: Outline of an Anarchistic Theory of Knowledge》. New Left Books. [①③④]
   费耶阿本德以伽利略等科学史案例力证：并不存在一套普遍有效的科学方法，重大进展往往恰恰来自违反既有规则，故其著名口号是「怎么都行」。它是对统一方法论最激进的反对，本章引它来标明：连「证伪」这样温和的方法论主张，也有人从根本上拒斥。

8. C. G. Hempel (1965).《Aspects of Scientific Explanation and Other Essays in the Philosophy of Science》. Free Press. [②]
   亨佩尔在这部论文集里集大成地阐发科学解释的覆盖律模型，既包括演绎律则式解释，也包括归纳统计式解释，并讨论了确证的逻辑及其悖论。它代表了逻辑经验主义对「理论上被研究过的东西」的系统刻画，为本章关于何为可被检验、可被解释提供了经典背景。

9. W. V. O. Quine (1951).「Two Dogmas of Empiricism」.《The Philosophical Review》, 60(1), 20-43. [②]
   奎因攻击逻辑经验主义的两条教条：分析与综合的截然二分，以及还原论；并提出认识论整体论，主张我们的信念作为一张整体之网共同面对经验，没有哪个陈述能被孤立地证实或否证。结合迪昂的检验整体论（合称 Quine-Duhem 论题），它直接冲击「一个反例干净利落地推翻一个假说」的图景，是本章界定证伪主义边界的核心文献。

10. P. Duhem (1906).《La théorie physique: son objet, sa structure》. Chevalier & Rivière. [②]
   迪昂在此提出检验整体论：物理学中的实验从不检验孤立假说，而是检验「假说连同一整套辅助假定与背景理论」，因此一次失败的预测无法判定究竟错在何处。此即后来与奎因合称的整体论之源头，本章用以说明反例的指向并不像表面那样确定。此处以原始法文版 1906 年为准，第二版 1914 年由 Marcel Rivière 出版，P. P. Wiener 英译《The Aim and Structure of Physical Theory》由 Princeton University Press 1954 年刊行。

11. M. Polanyi (1958).《Personal Knowledge: Towards a Post-Critical Philosophy》. University of Chicago Press. [①④]
   波兰尼提出「默会知识」：我们知道的远多于我们能言说的，科学探究中始终有一层无法形式化、只能在实践与师承中习得的个人判断与技艺。它提醒人们，再严格的方法论也无法消去科学家亲身的、不可言传的判断，呼应本章「历史上科学家的判断」与「如何在无法验证的世界里生活」两个落足点。

12. B. C. van Fraassen (1980).《The Scientific Image》. Clarendon Press. [②④]
   范弗拉森提出「建构经验论」：科学的目标不是宣称理论为真，而只是「经验适当」，即正确地拯救可观察现象；接受一个理论意味着相信它经验适当，而非相信其不可观察部分确实存在。它把「不可证实」转化为一种成熟的科学态度，与本章把「真」替换为「尚未被推翻」的姿态彼此呼应。

13. I. Hacking (1983).《Representing and Intervening: Introductory Topics in the Philosophy of Natural Science》. Cambridge University Press. [②③]
   哈金把哲学注意力从「表征」转向「干预」，主张实在论的最佳辩护不在理论而在实验：当我们能稳定地操纵电子去探测别的东西时，电子就是真实的（「能喷射，便是真」）。它为科学实在论开辟了以实验实践为基础的新进路，也提醒读者科学进展同样依赖动手干预而非只靠理论检验。

14. D. G. Mayo (1996).《Error and the Growth of Experimental Knowledge》. University of Chicago Press. [③]
   梅奥提出「误差统计」哲学：一个假说只有当它通过了「若为假则极可能不通过」的严苛检验时，我们才有理由接受它。这把波普尔的证伪精神落实为可操作的统计检验程序，是证伪主义一个精致的继承者，本章「严苛检验」一说即源于此（属 Science and Its Conceptual Foundations 丛书）。

15. D. G. Mayo (2018).《Statistical Inference as Severe Testing: How to Get Beyond the Statistics Wars》. Cambridge University Press. [③④]
   梅奥在此以「严苛性」为统一原则重构统计推断，试图越过频率派与贝叶斯派长期的「统计之战」，并据此回应复制危机中对显著性检验的批评。它把第 14 项的纲领发展为面向当代统计实践的方法论，对理解如何在不可验证的世界里负责任地使用统计证据尤为切题。

16. L. Laudan (1981).「A Confutation of Convergent Realism」.《Philosophy of Science》, 48(1), 19-49. [①②]
   劳丹列举科学史上一批曾经成功（能预测、能解释）却最终被抛弃的理论，如燃素说、以太说，论证「成功蕴含为真」的推断站不住脚，对收敛实在论构成有力反驳，常被称为「悲观元归纳」。它说明就连经验上很成功的理论也未必接近真理，强化了本章关于科学不以「证实真理」为目标的论点。

17. L. Laudan (1977).《Progress and Its Problems: Towards a Theory of Scientific Growth》. University of California Press. [③]
   劳丹主张以「问题求解能力」而非逼近真理来衡量科学进步：一个研究传统是否进步，取决于它解决的经验问题与概念问题之净增量。它给出了一种绕开真理概念的进步观，为本章「科学如何进展」提供了一个不依赖证实的替代框架。

18. P. Kitcher (1993).《The Advancement of Science: Science without Legend, Objectivity without Illusions》. Oxford University Press. [③]
   基切尔在抛弃科学全知全能的「传说」之后，又拒绝相对主义，转而从科学的社会与认知实践出发重建一种温和而可辩护的客观性与进步观。它示范了如何在承认科学受历史与社会影响的同时，仍守住进步与客观这两个概念，与本章既肯定科学又把边界标清的立场一脉相承。

19. P. K. Stanford (2006).《Exceeding Our Grasp: Science, History, and the Problem of Unconceived Alternatives》. Oxford University Press. [①②③④]
   斯坦福提出「未被设想的替代方案」问题：科学史一再表明，过去的科学家总有一些后来才出现、当时根本想不到的理论选项，故我们没有理由相信今天已穷尽了所有可行解释。他以遗传学等史案归纳出这一「新归纳」，直接呼应本书「无法验证的世界」之框架，提醒读者视野之外总有未及设想的可能。

20. N. Goodman (1955).《Fact, Fiction, and Forecast》. Harvard University Press. [②]
   古德曼提出「归纳的新谜题」：用「绿」与人造谓词「绿蓝」（grue，意为在某时间点前观察为绿、其后为蓝）同样能拟合迄今全部观察，却导出相反预测，可见归纳无法仅凭证据决定，还须依赖哪些谓词「可投射」。它说明归纳的困难不止于休谟式的辩护问题，更在于规律本身的不确定，深化了本章对归纳何以不可靠的理解。初版年份通行作 1955（HUP 一处简介称 1954，存在轻微歧义，此处从广引的 1955）。

21. C. G. Hempel, P. Oppenheim (1948).「Studies in the Logic of Explanation」.《Philosophy of Science》, 15(2), 135-175. [②]
   亨佩尔与奥本海姆在此奠定演绎律则（D-N）解释模型：一个现象得到科学解释，意味着它能从普遍定律加初始条件中逻辑地推演出来。它是二十世纪科学解释理论的起点，界定了「能被解释」在逻辑上意味着什么，为本章关于科学如何刻画规律提供了底层框架。

22. R. Carnap (1936-1937).「Testability and Meaning」.《Philosophy of Science》, 3(4), 419-471; 4(1), 1-40. [②]
   卡尔纳普在此放松严格的可证实原则，改用更宽的「可检验性」与「可确认性」来界定有意义的经验陈述，并以倾向性谓词等技术处理理论词项与观察的联系。它记录了逻辑经验主义从「可证实」向「可检验」的关键退却，正与本章「证实够不着、改用够得着的」这一主线相呼应。原文分两期刊出，第 3 卷第 4 期（1936）与第 4 卷第 1 期（1937）。

23. W. C. Salmon (1984).《Scientific Explanation and the Causal Structure of the World》. Princeton University Press. [②]
   萨蒙主张科学解释的核心不是逻辑推演而是揭示因果机制：解释一个现象，是把它嵌入世界的因果过程与因果相互作用之网。它是对覆盖律模型的重要修正，把「能解释」的标准从可推演转向可追溯的因果结构，为本章理解科学如何刻画世界补上因果这一维度。

24. C. Howson, P. Urbach (1989).《Scientific Reasoning: The Bayesian Approach》. Open Court. [②③]
   豪森与厄巴赫系统主张贝叶斯主义的科学推理观：不作非真即假的二值判决，而把证据看作按贝叶斯定理对信念概率的连续调整，并以此回应归纳与确证的诸多难题。它是本章正文提到的贝叶斯确证论的代表性论著，与证伪、严苛检验形成对照，也预告了全书「标定」一招。

25. E. Sober (2008).《Evidence and Evolution: The Logic Behind the Science》. Cambridge University Press. [②]
   索伯以似然论与统计推断的工具细致分析「证据支持什么」，并讨论何种假说才真正可检验，其中包含对智能设计为何不可检验的剖析。它把抽象的可检验性问题落到具体的科学推断实践（尤以进化论为例），示范了如何严格判断一个主张是否经得起证据的检验。

26. P. Godfrey-Smith (2003).《Theory and Reality: An Introduction to the Philosophy of Science》. University of Chicago Press. [②③]
   戈弗雷-史密斯这部广受好评的科学哲学导论，清晰梳理了从逻辑经验主义、证伪主义、库恩范式到贝叶斯主义与科学实在论之争的整条脉络。它适合作为本章诸多论题的导论性锚点，读者若想在阅读专著之前先建立全局地图，可由此入手。

27. N. Cartwright (1983).《How the Laws of Physics Lie》. Clarendon Press. [②③]
   卡特赖特论证物理学的基本定律之所以普适而优美，恰恰因为它们并不如实描述真实世界，而是描述高度理想化的模型；越基本的定律解释力越强，描述上反而越「说谎」。她转而看重更贴近现象的具体定律与因果能力，提醒读者科学定律之「真」远比通常设想的复杂，深化了本章对理论与世界关系的省思。

28. J. P. A. Ioannidis (2005).「Why Most Published Research Findings Are False」.《PLoS Medicine》, 2(8), e124. [③④]
   约阿尼迪斯用简明的统计建模论证：在效应量小、研究设计灵活、发表偏倚盛行的领域，一个已发表「阳性」结论为假的概率往往高于为真，假阳性可以系统性地多于真阳性。它是复制危机的奠基文献，正是本章「当机器失灵」一节的核心证据，说明科学的自我纠错一旦被削弱会如何空转。

29. Open Science Collaboration (2015).「Estimating the Reproducibility of Psychological Science」.《Science》, 349(6251), aac4716. [③④]
   开放科学合作组织协同上百名研究者，对一百项已发表的心理学研究做了系统性的直接重复，结果能成功重现原效应的不到半数，且重现出的效应普遍弱于原报告。它把复制危机从论证变为大规模实证，是本章「复制危机」一节的实证核心，也凸显了重复与预注册这些招数为何不可或缺。
