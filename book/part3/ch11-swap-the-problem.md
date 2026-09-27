# 第 11 章　换一个能处理的问题

> **论点**：不必执着于验证真正的对象。可以将它替换为一个既可检验、又可求解的代理（代理替换，proxy substitution）；也可以不再要求非此即彼的判决，转而依据经过校准的概率行动（校准，calibration）。

前两章的对策，追求的仍是关于对象的真相：或者削减关于它的不确定性，或者借助他人的判断去逼近它。本章讨论的两种对策，即代理替换与校准，则放弃了这一追求。它们不再追问「真正的对象是否正确」，而是改为回答另一个问题：前者更换验证的对象，后者改变判决的形式。

## 代理替换：更换验证的对象

第一种对策的一般形式是：不再以那个无法测量的真实目标为验证对象，而是代之以一个可以检验、且足以满足需要的代理，进而对这个代理加以验证和优化。换言之，接受检验的已不是原来的对象，而是它的替身。

这一对策的种种形态，在前面几乎每一章中都已出现。数学家以等价陈述代替待证的定理（第 7 章）；软件工程师以测试代替正确性，以基准测试代替能力；组织以 KPI 代替自身的健康状况，以 GDP 代替福祉（第 8 章）；机器学习以奖励模型代替人的真实偏好（即第 5 章讨论的 RLHF）。心理学中也有与之对应的现象。卡尼曼与弗雷德里克在 2002 年<sup class="cite"><a href="#ref-32">32</a></sup>提出了「属性替换」（attribute substitution）的概念：人在作直觉判断时，往往不自觉地以一个易于评估的属性，顶替那个难以评估的目标属性。在方法论层面，这一对策亦有其原型：波利亚建议解题者先转向一个相关而较易的问题<sup class="cite"><a href="#ref-30">30</a></sup>，西蒙则提出了满意化（satisficing）<sup class="cite"><a href="#ref-31">31</a></sup>。

这一对策的要害在于，它可能以两种方向相反的方式失效。第 7 章与第 8 章的讨论在此交汇，这条线索也贯穿全书。不妨用两个维度来刻画一个代理：一是「忠实」，即代理是否确实指向原来的目标；二是「更易」，即代理是否确实比原问题更易处理。以二者为坐标轴，可得下图：

![代理替换的两种相反失效方式：忠实 × 更易](../figures/f07-proxy-2x2.svg)

数学家的失败落在左上角：等价改写在忠实性上无可挑剔，却丝毫没有降低求解的难度，只是让同一个困难换了一副面目。组织的失败落在右下角：指标易于测量，然而一旦被当作目标加以优化，它与真实目标之间的对应便会断裂。

优化何以导致断裂？原因在于，代理与真实目标之间的相关，只在现状所对应的分布上成立；而优化的压力会把系统推离这一分布，推向二者分道扬镳的极端。社会科学对这一机制早有表述。古德哈特 1975 年<sup class="cite"><a href="#ref-1">1</a></sup>提出的定律指出，一个指标一旦成为目标，便会失效；坎贝尔 1979 年<sup class="cite"><a href="#ref-3">3</a></sup>的定律表达了同样的观察；卢卡斯 1976 年<sup class="cite"><a href="#ref-6">6</a></sup>在经济学中提出的孪生命题则是：一种结构关系一旦被当作政策目标，便会瓦解。三者描述的是同一个机制。埃斯佩兰与索德尔提出的反应性（reactivity）概念<sup class="cite"><a href="#ref-7">7</a></sup>又推进了一步：指标不仅会失真，还会反过来重塑被测量的对象。

同一机制在机器学习中再度上演，而且表现得格外清晰。阿莫迪等人 2016 年<sup class="cite"><a href="#ref-10">10</a></sup>将奖励黑客（reward hacking，即智能体借奖励设定中的缺陷取得高分，却并未完成预期的任务）列为一个具体的研究问题。此后的工作从经验与理论两个方向加深了对它的认识。潘等人 2022 年<sup class="cite"><a href="#ref-12">12</a></sup>的实证研究发现，能力更强的智能体更善于利用代理奖励的漏洞，真实回报甚至会出现骤降式的相变；斯卡尔塞等人 2022 年<sup class="cite"><a href="#ref-13">13</a></sup>证明，非平凡的奖励几乎不可能做到「无漏洞可钻」；高等人 2023 年<sup class="cite"><a href="#ref-14">14</a></sup>则为这种过度优化（overoptimization）测得了定量的缩放定律（scaling law）。由此可见，一个好的代理必须同时避开上述两种失效：既要忠实，又要更易。能够兼顾二者的代理少之又少；找到这样一个代理，便是这门技艺的全部。

## 校准：改变判决的形式

第二种对策的一般形式是：验证的对象不变，改变的是判决的形式。它不再要求「真」或「假」的二值裁决，而是给出一个经过校准的概率，依据这一概率行动，并承担一个有界的风险。

所谓校准，是指声称的把握与实际发生的频率相符：声称有几成把握的事情，就应当确有几成发生。用形式语言表述，即

$$\Pr\big(Y=1 \mid \hat p=p\big)=p,$$

也就是说，凡是声称有 70% 把握的事情，长期来看应当有七成成真。这一要求弱于「判定对错」，却是可以达到、也可以检验的。

![校准的可靠性图：声称的把握应当与实际发生的频率一致](../figures/f11-calibration.svg)

<figure class="uvw-viz" data-static="f11-calibration" role="group" aria-label="校准可靠性交互图">
<div class="uvw-live" hidden>
<div class="uvw-plot">
<svg viewBox="0 0 480 360" preserveAspectRatio="xMidYMid meet" aria-hidden="true">
<g class="uvw-axes" fill="none" stroke="currentColor" stroke-width="1.2" opacity="0.35">
<line x1="90" y1="300" x2="350" y2="300"></line>
<line x1="90" y1="300" x2="90" y2="40"></line>
</g>
<path class="uvw-gap-fill" stroke="none" opacity="0.14"></path>
<line class="uvw-diag" x1="90" y1="300" x2="350" y2="40" stroke="currentColor" stroke-width="1.3" stroke-dasharray="5 5" opacity="0.5"></line>
<path class="uvw-curve" fill="none" stroke-width="2.8"></path>
<line class="uvw-mark-v" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity="0.45"></line>
<line class="uvw-mark-h" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity="0.45"></line>
<circle class="uvw-dot" r="5"></circle>
<text class="uvw-tick" x="90" y="316" text-anchor="middle">0</text>
<text class="uvw-tick" x="350" y="316" text-anchor="middle">100%</text>
<text class="uvw-tick" x="84" y="44" text-anchor="end">100%</text>
<text class="uvw-diag-lab" x="356" y="44">完美校准</text>
<text class="uvw-xlab" x="220" y="344" text-anchor="middle">声称的把握 →</text>
<text class="uvw-ylab" x="34" y="170" text-anchor="middle" transform="rotate(-90 34 170)">实际发生频率 →</text>
</svg>
</div>
<div class="uvw-controls">
<label>过度自信
<input class="uvw-s-over" type="range" min="-100" max="100" value="60" step="1">
</label>
<label>温度校准
<input class="uvw-s-temp" type="range" min="0" max="100" value="0" step="1">
</label>
<div class="uvw-readout">
<span class="uvw-chip">声称 <b class="uvw-v-stated">70</b>%</span>
<span class="uvw-chip uvw-chip-obs">实际 <b class="uvw-v-obs">–</b>%</span>
<span class="uvw-chip uvw-chip-ece">校准误差 <b class="uvw-v-ece">–</b></span>
<span class="uvw-chip">Brier <b class="uvw-v-brier">–</b></span>
</div>
<p class="uvw-note"></p>
</div>
</div>
</figure>
<style>
.uvw-viz{margin:1.6em 0;padding:0}
.uvw-viz .uvw-live{border:1px solid var(--line,#e5e7eb);border-radius:10px;padding:14px 16px 18px;background:var(--paper,#fff)}
.uvw-viz svg{width:100%;height:auto;color:var(--ink,#1a1a1a);display:block}
.uvw-viz .uvw-tick,.uvw-viz .uvw-xlab,.uvw-viz .uvw-ylab,.uvw-viz .uvw-diag-lab{fill:var(--muted,#6b7280);font-size:12px}
.uvw-viz .uvw-xlab,.uvw-viz .uvw-ylab{font-size:13px}
.uvw-viz .uvw-controls{margin-top:10px}
.uvw-viz .uvw-controls label{display:flex;align-items:center;gap:10px;font-size:14px;color:var(--muted,#6b7280);margin-top:6px}
.uvw-viz .uvw-s-over,.uvw-viz .uvw-s-temp{flex:1;accent-color:#6366f1}
.uvw-viz .uvw-readout{display:flex;flex-wrap:wrap;gap:8px 14px;margin-top:12px;font-size:14px}
.uvw-viz .uvw-chip b{font-variant-numeric:tabular-nums}
.uvw-viz .uvw-chip-obs b{color:#6366f1}
.uvw-viz .uvw-chip-ece b{color:#d97706}
.uvw-viz .uvw-note{margin:12px 0 0;font-size:13.5px;color:var(--muted,#6b7280);min-height:3.6em;line-height:1.6}
@media (prefers-reduced-motion: no-preference){
.uvw-viz .uvw-curve,.uvw-viz .uvw-gap-fill,.uvw-viz .uvw-dot{transition:d .18s ease,cx .18s ease,cy .18s ease}
}
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
 var sOver=root.querySelector('.uvw-s-over'),sTemp=root.querySelector('.uvw-s-temp');
 var curve=root.querySelector('.uvw-curve'),fill=root.querySelector('.uvw-gap-fill');
 var mv=root.querySelector('.uvw-mark-v'),mh=root.querySelector('.uvw-mark-h'),dot=root.querySelector('.uvw-dot');
 var vObs=root.querySelector('.uvw-v-obs'),vEce=root.querySelector('.uvw-v-ece'),vBrier=root.querySelector('.uvw-v-brier');
 var note=root.querySelector('.uvw-note');
 var X0=90,X1=350,Y0=300,Y1=40;
 var AMBER='#d97706',GREEN='#10b981',PURPLE='#a855f7';
 function sx(x){return X0+(X1-X0)*x;}
 function sy(y){return Y0+(Y1-Y0)*y;}
 function gammaEff(){
  var raw=Math.pow(4,(+sOver.value)/100);
  var t=(+sTemp.value)/100;
  return Math.pow(raw,1-t);
 }
 function curveD(g){var d='M'+sx(0).toFixed(1)+','+sy(0).toFixed(1);for(var i=1;i<=100;i++){var x=i/100;d+='L'+sx(x).toFixed(1)+','+sy(Math.pow(x,g)).toFixed(1);}return d;}
 function fillD(g){var d='M'+sx(0).toFixed(1)+','+sy(0).toFixed(1);for(var i=1;i<=100;i++){var x=i/100;d+='L'+sx(x).toFixed(1)+','+sy(Math.pow(x,g)).toFixed(1);}for(var j=100;j>=0;j--){var xx=j/100;d+='L'+sx(xx).toFixed(1)+','+sy(xx).toFixed(1);}return d+'Z';}
 function metrics(g){var ece=0,brier=0,n=50;for(var i=0;i<n;i++){var x=(i+0.5)/n;var y=Math.pow(x,g);ece+=Math.abs(x-y);brier+=(x-y)*(x-y);}return{ece:ece/n,brier:brier/n};}
 function upd(){
  var g=gammaEff();
  var col=Math.abs(g-1)<0.06?GREEN:(g>1?AMBER:PURPLE);
  curve.setAttribute('d',curveD(g));curve.style.stroke=col;
  fill.setAttribute('d',fillD(g));fill.style.fill=col;
  var xs=0.70,ys=Math.pow(xs,g);
  dot.setAttribute('cx',sx(xs));dot.setAttribute('cy',sy(ys));dot.style.fill=col;
  mv.setAttribute('x1',sx(xs));mv.setAttribute('x2',sx(xs));mv.setAttribute('y1',Y0);mv.setAttribute('y2',sy(ys));
  mh.setAttribute('x1',X0);mh.setAttribute('x2',sx(xs));mh.setAttribute('y1',sy(ys));mh.setAttribute('y2',sy(ys));
  var m=metrics(g),obs=Math.round(ys*100);
  vObs.textContent=obs;vEce.textContent=(m.ece*100).toFixed(1)+'%';vBrier.textContent=m.brier.toFixed(3);
  if(Math.abs(g-1)<0.06){
   note.textContent='曲线贴合对角线：声称七成把握的事件，长期来看约有七成发生。赔率已经定准，但是否下注仍未决定。校准为风险定价，却不替人决定是否行动。';
  }else if(g>1){
   note.textContent='曲线位于对角线下方，表明过度自信：声称七成，实际只有 '+obs+'% 发生。调节温度校准，可将其压回对角线。';
  }else{
   note.textContent='曲线位于对角线上方，表明信心不足：声称七成，实际有 '+obs+'% 发生。调节温度校准，可将其拉回对角线。';
  }
 }
 sOver.addEventListener('input',upd);sTemp.addEventListener('input',upd);upd();
})();
</script>

这一对策在各领域中的形态同样整齐。数论中的概率素性检验便是一例：第 7 章已经看到，它给出的结论是某数「以 $1-\varepsilon$ 的概率为素数」。在机器学习中，与之对应的是共形预测（conformal prediction，沃夫克、伽默曼与谢弗 2005<sup class="cite"><a href="#ref-26">26</a></sup>）。这种方法不给出单点的判断，而是给出一个带有覆盖保证的预测集，

$$\Pr\big(Y\in C(X)\big)\ge 1-\alpha.$$

在气象学与预测科学中，校准已发展为一整套成熟的理论。布莱尔在 1950 年<sup class="cite"><a href="#ref-15">15</a></sup>提出了评价概率预报的评分；此后，墨菲在 1973 年<sup class="cite"><a href="#ref-17">17</a></sup>将这一评分分解为可靠性、分辨率与不确定性三个部分，德格鲁特与芬伯格在 1983 年<sup class="cite"><a href="#ref-18">18</a></sup>对此作了系统的处理；格奈廷等人在 2007 年<sup class="cite"><a href="#ref-24">24</a></sup>提出了现代的框架，其要旨可以概括为「受制于校准，越锐越好」，即先要求预测是校准的，再在此前提下使它尽可能锐利，也就是尽可能集中、明确。

天气预报是校准做得最好的领域之一。一个成熟的预报系统宣称「明天降雨概率 70%」，若把它作出这一预报的日子全部汇总，其中确有约七成下了雨。声称的把握与实际的频率严丝合缝，堪称校准的范本。此外，预测理论中还有一项深刻的设计，称为严格适当评分规则（strictly proper scoring rule）：通过精心构造评分函数，让如实报告（报出自己真正相信的概率）恰好成为期望得分最高的选择，

$$p=\arg\max_{q}\ \mathbb{E}_{Y\sim p}\big[S(q,Y)\big].$$

于是，讲真话不再依赖报告者的自觉，而是由评分规则的数学结构强制保证（萨维奇 1971<sup class="cite"><a href="#ref-16">16</a></sup>、格奈廷与拉夫特里 2007<sup class="cite"><a href="#ref-23">23</a></sup>）。关于校准能否实现，理论上既有肯定的结果，也有否定的结果。达维德 1982 年<sup class="cite"><a href="#ref-19">19</a></sup>证明，贝叶斯主体能够渐近地自我校准；福斯特与沃赫拉 1998 年<sup class="cite"><a href="#ref-22">22</a></sup>证明，对任意序列都存在渐近校准的策略。然而，奥克斯 1985 年<sup class="cite"><a href="#ref-20">20</a></sup>的结果「自我校准的先验不存在」，为这一对策标出了极限。在实践中，现代神经网络常常失准（miscalibration，郭等人 2017<sup class="cite"><a href="#ref-25">25</a></sup>），因此需要重新校准。至于第 6 章所述「允许、询问、阻止」的分级信任，则是校准落实到行动层面的形态。

校准的失效也有两种。较浅的一种是失准：声称的把握与实际不符，例如声称有 90% 把握的事情只有六成成真，那么建立在这一数字之上的决策都会随之偏离。较深的一种更为隐蔽，也更为重要：校准给出赔率，却不回答是否应当接受这场赌局。一个完美校准的「70%」，对于「70% 是否足以下注」这一问题不置一词。答案取决于赌注的大小，也取决于行动者看重什么；这是一个价值问题，而不是验证问题。将二者混为一谈，是依据校准行动时最常见的误区。人们以为概率已经替自己作出了决定，而它所做的只是标出赔率；是否下注，仍须行动者自己拿出一套价值判断。

## 两种对策的关联

将两种对策并置，便能看清它们的共同之处。代理替换更换的是验证的对象，转向一个不同的、可以检验的替代目标；校准改变的是判决的形式，以概率取代真或假。二者都不直接回答原来的问题，而是将它转换为一个可以处理的问题。换言之，它们改变的是我们对「答案」的要求：前者改变度量的内容，后者改变判决的形态，并为残余的风险标定价格。

尽管如此，这两种对策仍然致力于把事情做对，只是降低了「对」的标准。最后两种对策则更进一步：它们不再寄望于做对，而是转向管控出错的后果。既然错误无法杜绝，就应当缩小它的代价，并确保它一旦发生便能被发现。这是第 12 章的主题。

---

## 参考文献

> 落足点：① 历史上科学家的判断　② 理论上被研究过的东西　③ 科学如何进展　④ 如何在无法验证的世界里生活。本节经网络逐条核实。

### 代理替换：从古德哈特定律到非预期后果

1. C. A. E. Goodhart (1975).「Problems of Monetary Management: The U.K. Experience」.《Papers in Monetary Economics》, Vol. I. Reserve Bank of Australia. [②]
   这是古德哈特定律的原始出处，源于 1975 年悉尼的一次货币经济学会议。古德哈特在讨论英国货币管理经验时指出，一个统计规律一旦被用作调控目标，原先观察到的稳定关系往往就会失效。本章用它作为代理失真的标杆：指标与真目标的相关只在现状分布上成立，一被当成目标去优化便会断裂。

2. R. K. Merton (1936).「The Unanticipated Consequences of Purposive Social Action」.《American Sociological Review》, 1(6), 894-904. doi:[10.2307/2084615](https://doi.org/10.2307/2084615) [②]
   默顿系统讨论了有目的的社会行动为何会产生行动者未曾预料的后果，并梳理了知识不足、利益迫切、价值约束等若干来源。它是代理替换之副作用在社会学里的早期源头，提醒读者：优化一个代理时，真正吃紧的常是那些没有进入度量视野的后果。

3. D. T. Campbell (1979).「Assessing the Impact of Planned Social Change」.《Evaluation and Program Planning》, 2(1), 67-90. doi:[10.1016/0149-7189(79)90048-x](https://doi.org/10.1016/0149-7189%2879%2990048-x) [②④]
   坎贝尔定律的来源：一个量化的社会指标越是被用于社会决策，它就越容易遭到扭曲，也越容易反过来扭曲它本要监测的社会过程。它与古德哈特定律并列，是代理失真的另一块经典基石，读者可借此看清指标被赋以高利害后的腐化路径。

4. S. Kerr (1975).「On the Folly of Rewarding A, While Hoping for B」.《Academy of Management Journal》, 18(4), 769-783. doi:[10.2307/255378](https://doi.org/10.2307/255378) [②④]
   科尔考察了组织里普遍存在的激励错配：管理者奖励的行为 A，往往并非他们真正期望的行为 B，于是激励系统稳定地产出了与初衷相悖的结果。它是激励与代理错配的管理学经典，正对应本章「优化代理、真目标却烂掉」那一格的现实样貌。

5. M. Strathern (1997).「'Improving ratings': audit in the British University system」.《European Review》, 5(3), 305-321. doi:[10.1002/(sici)1234-981x(199707)5:3&lt;305::aid-euro184&gt;3.0.co;2-4](https://doi.org/10.1002/%28sici%291234-981x%28199707%295:3%3C305::aid-euro184%3E3.0.co;2-4) [②④]
   斯特拉森借英国大学审计制度的观察，给出了那句广为流传的表述：当一个度量成为目标，它便不再是好的度量。本章关于代理一旦被当作目标即失真的论证，常以此为简洁的口径，读者可读到这一表述的原始语境。

6. R. E. Lucas (1976).「Econometric Policy Evaluation: A Critique」.《Carnegie-Rochester Conference Series on Public Policy》, 1, 19-46. doi:[10.1016/s0167-2231(76)80003-6](https://doi.org/10.1016/s0167-2231%2876%2980003-6) [②③]
   卢卡斯批判指出，计量模型中估计出的参数关系依赖于既有政策环境，一旦据此改变政策，主体的预期与行为会随之调整，原有的结构关系便不再成立。它是古德哈特定律的经济学孪生命题，本章用它说明优化压力为何会把系统推离代理与真目标相符的那个分布。

7. W. N. Espeland & M. Sauder (2007).「Rankings and Reactivity: How Public Measures Recreate Social Worlds」.《American Journal of Sociology》, 113(1), 1-40. doi:[10.1086/517897](https://doi.org/10.1086/517897) [②④]
   埃斯佩兰与索德尔提出「反应性」框架：公开的排名与量化指标不只是测量，它们还会改变被测者的行为乃至自我认知，从而重塑它本要描述的社会现实。本章借它把代理失真推进一层，指标不仅会失真，还会反过来重造被测对象。

8. D. Manheim & S. Garrabrant (2018).「Categorizing Variants of Goodhart's Law」. [arXiv:1803.04585](https://arxiv.org/abs/1803.04585). [②]
   两位作者尝试把笼统的「古德哈特定律」拆成几类不同机制（如回归型、极值型、因果型、对抗型），各自的失效方式与对策并不相同。它为本章「代理替换的失效不止一种」提供了细化的分类，便于读者分辨自己面对的是哪一种失真。

9. J. Z. Muller (2018).《The Tyranny of Metrics》. Princeton University Press. doi:[10.23943/9781400889433](https://doi.org/10.23943/9781400889433) [④]
   穆勒以大量医疗、教育、警务、商业等领域的案例，批评了把一切都化为可量化指标并据以问责的风气，指出这种度量崇拜常带来表面达标而实质受损的后果。它是面向一般读者的通俗综述，适合读者在生活与工作中识别代理替换的代价。

### 代理失真在机器学习中的复现：奖励黑客与过度优化

10. D. Amodei, C. Olah, J. Steinhardt, P. Christiano, J. Schulman & D. Mané (2016).「Concrete Problems in AI Safety」. [arXiv:1606.06565](https://arxiv.org/abs/1606.06565). [②]
   这篇影响广泛的综述把 AI 安全拆成若干具体可研究的问题，其中包括奖励黑客（reward hacking）与可扩展监督等。它把社会科学里早已熟知的代理目标失真，清晰地译入了机器学习语境，是本章「同一机制在机器学习里重演」一段的起点。

11. P. F. Christiano, J. Leike, T. B. Brown, M. Martic, S. Legg & D. Amodei (2017).「Deep Reinforcement Learning from Human Preferences」.《Advances in Neural Information Processing Systems》, 30 (NeurIPS 2017). [arXiv:1706.03741](https://arxiv.org/abs/1706.03741) [②④]
   作者用人类对成对轨迹的偏好比较来训练一个奖励模型，再用它驱动强化学习，从而绕开难以手写的目标函数。这是 RLHF 的奠基工作，也正是本章所说「用奖励模型代人的真实偏好」的代理替换样板，读者可由此理解为何这种代理既好用又危险。

12. A. Pan, K. Bhatia & J. Steinhardt (2022).「The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models」. ICLR 2022. [arXiv:2201.03544](https://arxiv.org/abs/2201.03544) [②]
   作者系统考察了奖励设定不当的后果，并给出一个值得警惕的经验现象：能力更强的智能体往往更善于钻代理奖励的空子，真实回报甚至会随能力提升而出现骤降式的相变。本章用它说明代理失真不是线性恶化，而可能在某处突然翻盘。

13. J. Skalse, N. H. R. Howe, D. Krasheninnikov & D. Krueger (2022).「Defining and Characterizing Reward Hacking」.《Advances in Neural Information Processing Systems》, 35 (NeurIPS 2022). doi:[10.52202/068431-0687](https://doi.org/10.52202/068431-0687) [②]
   这篇论文给出奖励黑客的一个形式化定义，并证明在非平凡的情形下，几乎不存在「不可钻空」的代理奖励。它为本章「好代理罕见」提供了理论支撑：忠实又稳健的代理之所以稀少，是有结构性原因的，而非工程上偶然没做好。

14. L. Gao, J. Schulman & J. Hilton (2023).「Scaling Laws for Reward Model Overoptimization」.《Proceedings of the 40th International Conference on Machine Learning》(PMLR 202), 10835-10866. [arXiv:2210.10760](https://arxiv.org/abs/2210.10760) [②]
   作者对奖励模型的过度优化做了定量刻画，给出真实表现随对代理奖励优化程度变化的缩放定律式规律：优化超过某点后，代理得分仍升而真实表现转跌。它把古德哈特式失真从定性观察推进到可测量的曲线，是本章过度优化论证最实证的一块。

### 校准：把二值判决换成概率，并以严格适当评分约束之

15. G. W. Brier (1950).「Verification of Forecasts Expressed in Terms of Probability」.《Monthly Weather Review》, 78(1), 1-3. doi:[10.1175/1520-0493(1950)078&lt;0001:vofeit&gt;2.0.co;2](https://doi.org/10.1175/1520-0493%281950%29078%3C0001:vofeit%3E2.0.co;2) [②]
   布莱尔提出了一个用于评价概率预报的评分（即后来的 Brier 评分），把「报了多大把握、最终是否发生」纳入可计算的考核。它是校准与严格适当评分体系的起点，本章关于「概率可检验」的论证由此发端。

16. L. J. Savage (1971).「Elicitation of Personal Probabilities and Expectations」.《Journal of the American Statistical Association》, 66(336), 783-801. doi:[10.1080/01621459.1971.10482346](https://doi.org/10.1080/01621459.1971.10482346) [②]
   萨维奇研究如何设计评分与激励，使人愿意如实报出自己的主观概率与期望。它为「适当评分规则诱出真实概率」奠定了理论基础，对应本章那句关键设计：讲真话不再靠自觉，而被评分规则的数学结构所强制。

17. A. H. Murphy (1973).「A New Vector Partition of the Probability Score」.《Journal of Applied Meteorology》, 12(4), 595-600. doi:[10.1175/1520-0450(1973)012&lt;0595:anvpot&gt;2.0.co;2](https://doi.org/10.1175/1520-0450%281973%29012%3C0595:anvpot%3E2.0.co;2) [②]
   墨菲把 Brier 评分分解为可靠性、分辨率与不确定性三个分量，让人能分别看清预报哪里失准、哪里有区分力。这一分解是校准概念的量化骨架，本章谈「校准」与「锐度」的区分，正建立在这种拆解之上。

18. M. H. DeGroot & S. E. Fienberg (1983).「The Comparison and Evaluation of Forecasters」.《Journal of the Royal Statistical Society: Series D (The Statistician)》, 32(1-2), 12-22. doi:[10.2307/2987588](https://doi.org/10.2307/2987588) [②]
   德格鲁特与芬伯格对预测者的比较与评价做了系统处理，明确区分了校准（calibration）与精炼/锐度（refinement），并给出据此排序预测者的框架。它是本章校准论证的核心理论来源，读者可在此看到校准作为可检验认识对象的严格表述。

19. A. P. Dawid (1982).「The Well-Calibrated Bayesian」.《Journal of the American Statistical Association》, 77(379), 605-610. doi:[10.1080/01621459.1982.10477856](https://doi.org/10.1080/01621459.1982.10477856) [②]
   达维德证明，一个连贯的贝叶斯主体在自己的主观信念下会渐近地自我校准，即长期看其概率断言与实际频率相符。本章用它说明校准并非外加的苛求，而可以是理性更新的内在产物。

20. D. Oakes (1985).「Self-Calibrating Priors Do Not Exist」.《Journal of the American Statistical Association》, 80(390), 339-342. doi:[10.1080/01621459.1985.10478117](https://doi.org/10.1080/01621459.1985.10478117) [②]
   奥克斯指出，不存在一个先验能保证对所有数据序列都自我校准，从而给达维德式的乐观结果划出了边界。它与 Dawid (1982) 及 Foster-Vohra 的可达性结果形成反向制衡，是本章「校准有其极限」一笔的依据。

21. M. J. Schervish (1989).「A General Method for Comparing Probability Assessors」.《The Annals of Statistics》, 17(4), 1856-1879. doi:[10.1214/aos/1176347398](https://doi.org/10.1214/aos/1176347398) [②]
   舍尔维什给出比较概率评估者的一般方法，把各种适当评分规则纳入统一的比较框架，作为其中的特例。它对校准理论起到集成与整理的作用，便于读者把零散的评分规则放进同一张图里看。

22. D. P. Foster & R. V. Vohra (1998).「Asymptotic Calibration」.《Biometrika》, 85(2), 379-390. doi:[10.1093/biomet/85.2.379](https://doi.org/10.1093/biomet/85.2.379) [②]
   福斯特与沃赫拉证明，即便面对任意（甚至对抗性）的结果序列，也存在一种预测策略能渐近达到校准。这是校准可达性的关键定理，本章据此说明校准是一个比真假判决更弱、却切实可达的认识目标。

23. T. Gneiting & A. E. Raftery (2007).「Strictly Proper Scoring Rules, Prediction, and Estimation」.《Journal of the American Statistical Association》, 102(477), 359-378. doi:[10.1198/016214506000001437](https://doi.org/10.1198/016214506000001437) [②]
   这是严格适当评分规则的权威综述：系统整理了哪些评分函数能使如实报告恰好成为期望得分最优之策，并把它们与预测、估计联系起来。它是本章校准论证的理论支柱，读者要理解「讲真话被数学结构强制」可读此篇。

24. T. Gneiting, F. Balabdaoui & A. E. Raftery (2007).「Probabilistic Forecasts, Calibration and Sharpness」.《Journal of the Royal Statistical Society: Series B (Statistical Methodology)》, 69(2), 243-268. doi:[10.1111/j.1467-9868.2007.00587.x](https://doi.org/10.1111/j.1467-9868.2007.00587.x) [②]
   作者提出概率预测的现代框架，把目标概括为「受制于校准，越锐越好」：先要求预测校准，再在校准的前提下尽量提高锐度。本章关于如何评判一个概率预测好坏的标准，直接采用这一框架。

25. C. Guo, G. Pleiss, Y. Sun & K. Q. Weinberger (2017).「On Calibration of Modern Neural Networks」.《Proceedings of the 34th International Conference on Machine Learning》(PMLR 70), 1321-1330. [arXiv:1706.04599](https://arxiv.org/abs/1706.04599) [②]
   作者发现现代深度神经网络虽然往往更准，却常常失准，置信度系统性地偏离真实正确率，并提出温度缩放等简单的重新校准方法。它是校准问题在机器学习侧的代表作，正对应本章「现代神经网络恰恰常常失准，于是需要重新校准」。

26. V. Vovk, A. Gammerman & G. Shafer (2005).《Algorithmic Learning in a Random World》. Springer. doi:[10.1007/b106715](https://doi.org/10.1007/b106715) [②]
   这是共形预测（conformal prediction）的奠基专著：它不给出单点判断，而构造带有覆盖保证的预测集，使真值落入集合的概率有可控的下界。本章用它作为校准思想在机器学习中的一种实现，给读者一个「带自身可靠性保证的预测」的范例。

### 判断、预测与替换动作的方法论根

27. P. E. Tetlock (2005).《Expert Political Judgment: How Good Is It? How Can We Know?》. Princeton University Press. [Google Books](https://books.google.com/books?id=NAeCzQEACAAJ) [①②]
   泰特洛克对专家政治预测做了长达多年的大规模追踪，发现众多专家的长期预测准确度并不出色，且常逊于简单的外推基准。它是把专家判断放到可检验框架里加以考核的代表作，对本章「按校准的概率行动、而非迷信权威断言」给出经验支撑。

28. P. E. Tetlock & D. Gardner (2015).《Superforecasting: The Art and Science of Prediction》. Crown. [Google Books](https://books.google.com/books?id=hC_qBQAAQBAJ) [①④]
   本书把 IARPA 预测锦标赛的研究成果通俗化，刻画了表现突出的「超级预测者」如何拆解问题、给出概率、并随证据不断微调。它偏向实践，讲的正是如何在无法验证的世界里做出可被校准检验的判断，适合读者据以训练自己的预测习惯。

29. G. E. P. Box (1976).「Science and Statistics」.《Journal of the American Statistical Association》, 71(356), 791-799. doi:[10.1080/01621459.1976.10480949](https://doi.org/10.1080/01621459.1976.10480949) [②③]
   这是「所有模型都是错的，但有些有用」一语的出处。博克斯主张统计建模是科学探究的迭代过程，不应追求绝对正确而应追求有用与可改进。它正服务于本章的一组败法对照：忠实却不易处理，还是可处理但只是近似。

30. G. Pólya (1945).《How to Solve It: A New Aspect of Mathematical Method》. Princeton University Press. doi:[10.1515/9781400828678](https://doi.org/10.1515/9781400828678) [②④]
   波利亚总结了一套解题启发法，其中一条便是先转向一个相关而更易的问题，再借它逼近原题。这正是本章标题这一替换动作的方法论原型，读者可把代理替换看作把这条古老的解题术推广到无法直接验证的场景。

31. H. A. Simon (1956).「Rational Choice and the Structure of the Environment」.《Psychological Review》, 63(2), 129-138. doi:[10.1037/h0042769](https://doi.org/10.1037/h0042769) [②④]
   西蒙提出有限理性与满意化：在能力与信息有限时，主体并不求最优，而是搜到一个「足够好」的方案即停。它为「用足够好的代理取代难以企及的最优」提供了理论根据，是本章替换动作在决策科学里的根。

32. D. Kahneman & S. Frederick (2002).「Representativeness Revisited: Attribute Substitution in Intuitive Judgment」. 收入 T. Gilovich, D. Griffin & D. Kahneman (编)《Heuristics and Biases: The Psychology of Intuitive Judgment》, 49-81. Cambridge University Press. doi:[10.1017/cbo9780511808098.004](https://doi.org/10.1017/cbo9780511808098.004) [②]
   卡尼曼与弗雷德里克提出「属性替换」：当目标属性难以评估时，人会不自觉地用一个更易评估的属性顶替它来作答。这正是本章代理替换机制的心理学孪生，说明换问题这一对策不只是工程策略，也是人类直觉的默认运作方式。
