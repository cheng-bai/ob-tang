# 2024高联二试几何题完整思维流程分享-dollar
## 前排提醒:

本视频为 up 主 nichijou 的涂山苏苏基于“高中数学经验分享系列”制作的单题讲解视频。up 主的视频全部基于 up 主自己的体系，具有极强的粉丝向特性。在观看视频前，请先阅读 up 主在主页置顶的“粉丝入坑指南”的专栏，并至少观看完 up 主制作的经验分享系列视频，否则对单题讲解视频的内容无法很好地消化。

题目 (2024 全国高中数学联赛二试几何):

如下图, 在凸四边形 ABCD 中, AC 平分 ∠BAD , 点 EF 分别在边 BC, CD 上, 满足 EF //BD。分别延长FA, EA至点P, Q，使得过点A, B, P的圆 ${\omega }_{1}$ 及过点A, D, Q的圆 ${\omega }_{2}$ 均与![bo_d5206bf7aajc73fu47c0_0_656_990_337_310_0.jpg](bo_d5206bf7aajc73fu47c0_0_656_990_337_310_0.jpg)47c0_0_656_990_337_310_0.jpg)

## 读题与画图顺序 (要素关系网) 的分析

拿到一道平面几何题, 最重要的就是先用画图法分析图形结构。先按照题目顺序梳理: 起始背景为四边形 ABCD(系统内有一组等角)，然后画平行线 EF 。接下来是两圆，注意过 $\mathrm{A},\mathrm{B}$ 两点且与 $\mathrm{{AC}}$ 相切的圆是唯一的,因此此处画图顺序应为: 先画出确定的 ${\omega }_{1},{\omega }_{2}$ , 再延长 EA, FA得到 P, Q 。

因此,系统的要素结构梳理为 $\mathrm{{ABCD}} \rightarrow  \left\{  {\begin{array}{l} \mathrm{{EF}} \\  {\omega }_{1},{\omega }_{2} \end{array} \rightarrow  \mathrm{P},\mathrm{Q}}\right.$ 。这表明本题的要素结构是完全顺畅的控制流程(图形可以沿着要素网，一路准确地画下来)，不存在额外添加的牵制条件(例如“若满足……”的额外限制)。

注:在高中竞赛平面几何中，一个常见的现象是:大部分题目的要素结构都可以梳理为纯控制，这类题目的思考方式常常沿着要素网进行分析。而如果一道题目中出现牵制条件，那么这道题通常难度都会较高。

## 消点尝试(要素关系网重构)其一

很多竞赛平面几何都需要重构要素关系网，一个策略是尽量把重要且复杂的要素放到前面。本题的两个圆显然是最重要的核心要素,而且两圆被 $\mathrm{A},\mathrm{B},\mathrm{D}$ 直属控制。因此尝试首先画它们:过 $\mathrm{A}$ 的一条直线与两个切圆 ${\omega }_{1}$ ， ${\omega }_{2}$ ，从 $\mathrm{A}$ 光翼展开一对平分线，生![bo_d5206bf7aajc73fu47c0_1_546_513_572_244_0.jpg](bo_d5206bf7aajc73fu47c0_1_546_513_572_244_0.jpg)47c0_1_546_513_572_244_0.jpg)

小技巧:画图尽量保证要素网简单直接，体现在画图法上，就是画图的难度。若是先画 B，D 再生成圆，这个生成过程较复杂，远没有先画圆再光翼展开生成 B，D 简单。

然后自然就是画 $\mathrm{C} \rightarrow  \mathrm{{EF}}$ 。但是放眼整个要素网, $\mathrm{{EF}}$ 后续还要生成 $\mathrm{P},\mathrm{Q}$ ,直接关系到求证, 非常重要; 而 C 后续就没啥事情了。二者相较, 显然 EF 重要程度更高。能不能颠倒一下要素网, 先画 EF 呢?

平行于 BD 这一条件还得带着。但是接下来只需要让 BE, DF 交出合法的 C 即可。换而言之, 只要 BE, DF 与![bo_d5206bf7aajc73fu47c0_1_866_1339_285_259_0.jpg](bo_d5206bf7aajc73fu47c0_1_866_1339_285_259_0.jpg)7c0_1_866_1339_285_259_0.jpg)

口

${F}_{0}$

隔离出来基础模型。我们设 EF, BD 分别与中轴线交于 S, T 。易见 EF 合法, 当且仅当 $\frac{\mathrm{{ES}}}{\mathrm{{FS}}} = \frac{\mathrm{{BT}}}{\mathrm{{DT}}} = \frac{\mathrm{{AB}}}{\mathrm{{AD}}}$ (最后一条是角平分线定理),而这正好是左右两圆的大小比。

这时注意到左右两圆分别搭配 $\mathrm{{AB}},\mathrm{{AD}}$ ，这两个子系统的“形状”完全一样。如果我们设左右两圆的大小之比为 $\mathrm{k}$ ,则有 $\mathrm{k} = \frac{{\mathrm{R}}_{\text{ 左 }}}{{\mathrm{R}}_{\text{ 右 }}} = \frac{\mathrm{{AB}}}{\mathrm{{AD}}}$ 。此时,只要取一条 $\mathrm{{BD}}$ 的平行线,再在 $\mathrm{S}$ 左右按照 $\mathrm{k}$ 的比例取 $\mathrm{E},\mathrm{F}$ ,那这就是一组合法的 $\mathrm{E},\mathrm{F}$ 。它们再生成 $\mathrm{P},\mathrm{Q}$ 即可。

## 消点尝试(要素关系网重构)其二

目前的要素网已被简化(消去了 C ，信息朝着更加重要的 E, F 集中)。但 EF 直线自身仍然有一个选取的自由度。

直觉感知:这么多自由度就为了给一个平行比例分配，似乎有些过于冗余了。从要素网生成来看，射线EA, FA才是重点。能不能把这个关键信息进一步朝基础要素(ABD系统) 集中?

当有了如上构造的 $\mathrm{E},\mathrm{F}$ 时,设线段 $\mathrm{{EA}},\mathrm{{FA}}$ 与 $\mathrm{{BD}}$ 分别交于 $\mathrm{M},\mathrm{N}$ 。仿照之前的“平行加中轴线”模型推理,可知当且仅当 $\frac{\mathrm{{MT}}}{\mathrm{{NT}}} = \frac{\mathrm{{ES}}}{\mathrm{{FS}}} = \mathrm{k}$ 时,反向从 $\mathrm{{AM}},\mathrm{{AN}}$ 出发,射到一条平行于 $\mathrm{{BD}}$ 的直线上,才能得到合法的一![bo_d5206bf7aajc73fu47c0_2_581_899_529_312_0.jpg](bo_d5206bf7aajc73fu47c0_2_581_899_529_312_0.jpg)47c0_2_581_899_529_312_0.jpg)

因此,信息进一步集中: 直接在 $\mathrm{{BD}}$ 上取一对满足 $\frac{\mathrm{{MT}}}{\mathrm{{NT}}} = \mathrm{k}$ 的 $\mathrm{M},\mathrm{N}$ ,把 $\mathrm{E},\mathrm{F}$ 作为次级要素消去,反而直接让 $\mathrm{{MA}},\mathrm{{NA}}$ 射向圆,生成 $\mathrm{P},\mathrm{Q}$ 。这样,要素网得到进一步简化。注意两侧的大小比为 $\mathrm{k}$ 。在此基础上,已知可直观理解为两点组 $\left( {\mathrm{B},\mathrm{M},\mathrm{T}}\right)$ 与 $\left( {\mathrm{D},\mathrm{N},\mathrm{T}}\right)$ 相似。

$$
\frac{AB}{AD} = k = \frac{t}{N}
$$

$$
\left( {\frac{NT}{ND} = \frac{MT}{MB}}\right) \text{ or }\left( {TN}\ri![bo_d5206bf7aajc73fu47c0_2_426_1546_281_320_0.jpg](bo_d5206bf7aajc73fu47c0_2_426_1546_281_320_0.jpg)7c0_2_426_1546_281_320_0.jpg)

## 解题策略思考

要素网已经得到充分简化。图形在左右大小比 $\mathrm{k}$ 的控制下,对称地分成左右两半。右边的 ADNT 系统会往左边打出一个 $\mathrm{P}$ ，而左边则向右打出 $\mathrm{Q}$ 。这两条线索具有独立性。 但所证则是连结了左右两侧的一个结论。

小经验:面对这样左右交错的要素结构，如果其中一侧的线索可以控制某个东西，另一侧的线索也对称地控制这个对称的东西。而如果能证明左右的控制效果一致, 那么就可以顺利成章地把左右连结起来。

在这个经验的思维指引下, 我们尝试探索可能的求证路径。在联赛中, 证明共圆要么就是角度推导,要么就是圆幂定理 (长度推导) 。这道题的已知几乎全部围绕大小比例 $\mathrm{k}$ 展开, 似乎天生就有 “长度亲和力”。因此我们先试试圆幂定理。如果用相交弦定理, 那还需要连结 PD, BQ, 又需要把左右再打个结。但如果用割线定理, 延长 BP, DQ, 则左右仍是分开的,符合刚才我们讲到的策略。若是延长它们交于 $\mathrm{G}$ ,则自然要算 $\left| \mathrm{{GP}}\right|  \cdot  \left| \mathrm{{GB}}\right|$ 与 $\left| \mathrm{{GQ}}\right|  \cdot  \left| \mathrm{{GD}}\right|$ 。

但准确画图不难注意到:似乎BP，DQ与中轴线三线共点。这时我们恍然大悟:如果真的三线共点,那么用切割线定理立得 $\left| \mathrm{{GP}}\right|  \cdot  \left| \mathrm{{GB}}\right|  = \left| \mathrm{{GQ}}\right|  \cdot  \left| \mathrm{{GD}}\right|  = {\left| \mathrm{{GA}}\right| }^{2}$ ,直接证完了!

一切都在 “明示” 我们证这个。根据刚才分离左右的策略, 我们选取同一法: 让 BP 与中轴线交于 ${\mathrm{G}}_{1}$ ,计算 ${\mathrm{G}}_{1}$ 的位置。利用对称性立刻得到 $\mathrm{{DQ}}$ 与中轴线交点 ${\mathrm{G}}_{2}$ 的位置![bo_d5206bf7aajc73fu47c0_3_498_1253_675_374_0.jpg](bo_d5206bf7aajc73fu47c0_3_498_1253_675_374_0.jpg)7c0_3_498_1253_675_374_0.jpg)

## 完成解题

涉及到计算,而且图还这么简单,我们就大胆交给三角爆算法。设 $\angle \mathrm{{NAT}} = \alpha$ ,再设原始要素 $\angle \mathrm{{BAT}} = \beta$ 。于是图中有三个角都是 $\alpha$ ,这实现了左半侧的完全控制。

由正弦定理得 $\frac{\left| {G}_{1}A\right| }{\sin \alpha } = \frac{\left| AB\right| }{\sin \left( {\beta  - \alpha }\right) } = \frac{\left| AB\right| }{\sin \angle {NAD}}$ ,得 $\left| {{G}_{1}A}\right|  = \frac{\left| {AB}\right| \sin \angle {NAT}}{\sin \angle {NAD}}$ 。同理可得 $\left| {{\mathrm{G}}_{2}\mathrm{\;A}}\right|  = \frac{\left| \mathrm{{AD}}\right| \sin \angle \mathrm{{MAT}}}{\sin \angle \mathrm{{BAM}}}$ 。于是即证 $\frac{\left| \mathrm{{AB}}\right| \sin \angle \mathrm{{NAT}}}{\sin \angle \mathrm{{NAD}}} = \frac{\left| \mathrm{{AD}}\right| \sin \angle \mathrm{{MAT}}}{\sin \angle \mathrm{{BAM}}}$ 。这个式子已经

只和三角形系统有关了, 与圆完全无关了, 作为竞赛题的中间结果已经是简单的不能再简单了。利用好分角引理 $\frac{\sin \angle {NAT}}{\sin \angle {NAD}} = \frac{\left| AD\right| }{\left| AT\right| } \cdot  \frac{\left| TN\right| }{\left| DN\right| }$ 与 $\frac{\sin \angle {MAT}}{\sin \angle {BAM}} = \frac{\left| AB\right| }{\left| AT\right| } \cdot  \frac{\left| TM\right| }{\left| BM\right| }$ 代回上式, 这正好等价于 $\frac{\left| TN\right| }{\left| DN\right| } = \frac{\left| TM\right| }{\left| BM\right| }$ ,也就是 $M, N$ 的选取约束。因此问题得证。

## 综合法解题全流程梳理

利用平行线倒比例推导出 $\frac{\left| TN\right| }{\left| DN\right| } = \frac{\left| TM\right| }{\left| BM\right| }$ ,然后利用分角引理推导出 $\left| {{G}_{1}A}\right|  = \left| {{G}_{2}A}\right|$ ,最后利用切割线定理推导出最终结论。

一共三大步骤, 解题流程很短。但是为何要朝着这个方向思考? 其中的思维历程已经如本视频所展示。