## 给中学生的数学科普 time——第三期

主讲:にちじょうの涂山苏苏

## 事前声明:

本次内容主要为映射的基础知识, 属于大学数学的入门衔接知识, 与高考没有任何关系。本讲内容面向对数学有兴趣的观众, 前置知识为集合论, 看过上一期集合的科普视频的话, 本期内容会更好理解, 不过即使只有高中的集合知识储备, 同样可以观看。为了方便高中生理解，内容中的部分定义和表述进行了直观化的简化处理，因此可能部分地方不够严谨，感兴趣的同学可以自行查阅大学数学中映射的相关内容。

另外, 本次内容相对难度会稍微大一点, 因为涉及到的逻辑推理比较多, 相信也能够提高部分想要数学拔尖的同学的逻辑分析能力和处理信息的能力。本讲最后设置了一些比较有挑战性的思考题, 偏向新信息处理和数学探究, 提供给对数学有兴趣的同志们。

集合论是当今数学的基本，有了集合论，我们才能在各式各样的空间中建立丰富多彩的数学分支。集合的基本思想就是把具有相同的某种性质的对象放在一起来研究, 同时, 用集合的语言来描述空间也是十分自然, 合理的。当我们在数学中谈到 “空间” 一词时, 无一例外, 都是具备了某些结构或性质的集合。例如二维欧式空间 ${\mathrm{R}}^{2} = \{ \left( {\mathrm{x},\mathrm{y}}\right)  \mid  \mathrm{x},\mathrm{y} \in  \mathrm{R}\}$ ,就是我们通常认知的平面世界的数学语言刻画, 在上面定义距离, 直线等结构, 引入平行, 垂直, 夹角等概念, 就是我们熟悉的平面几何。

不过, 数学可不止于此。光是在各个集合上面 “闭门造车”, 各研究各的, 可不会让数学家们满意。数学的美感很大程度上来源于不同事物之间千丝万缕的联系。比如, 圆和椭圆看上去形状差不多, 都是个圈, 但是直线和圆就不一样, 因此, 从结构上来看, 圆和椭圆可以归为一类, 直线可以归为一类, 这两种“空间”的结构就完全不同。

因此，研究不同集合之间的关系，是数学中十分重要且基本的内容。而不同集合要建立关系，搭上钩，映射就是一个十分自然的概念了。

## 一、从对应关系到映射

实际上, 对应关系在现实世界中也广泛存在。例如, 每一位中华人民共和国公民，我们可以把他(她)对应到一个数字(最多加点字母)串，也就是身份证号, 人与数字串之间就建立了一个对应。对于超市里的每一瓶饮料, 我们可以把它对应到一个日期, 也就是生产日期......

在数学中，对应关系更为普遍。我们从初中就开始接触函数，实际上函数就是一种数与数之间的对应关系: 对定义域 (一个数集) 内的每一个元素 (数), 我们都可以把它对应到它的函数值, 函数值的集合称为值域, 这也是一个对应关系; 再比如对于 ${\mathrm{R}}^{2}$ 里的每一个点 $\left( {\mathrm{x},\mathrm{y}}\right)$ ,我们可以把它对应到它的横坐标 $\mathrm{x}$ ; 对于每一个三角形,我们可以把它对应到它的面积; 对于每个实数 $\mathrm{x} \in  \mathrm{R}$ ,我们可以把它对应到自己,不过这时候作为复数 $\mathrm{x} \in  \mathrm{C}$ ,这就成了实数集对应到复数集……

对应关系是如此的简单, 以至于我们上面很多例子就像废话一般简单; 对应关系又如此广泛, 以至于在数学中随处可见, 甚至你都察觉不到它的存在!

数学家为了抽象并严格地刻画这种普遍存在的对应关系, 以深刻揭示不同事物之间的联系，建立了映射的概念:

定义:对于非空集合 $A, B$ ，若存在 $A$ 到 $B$ 的某种对应关系 $f : A \rightarrow  B$ ，使得对于 $\forall x \in  A$ ,都存在唯一的 $y \in  B$ ,使得在该对应关系下 $x$ 被对应到 $y$ (映射的确定性和唯一性),记为 $f\left( x\right)  = y$ ,则称 $f$ 是 ${A\text{ 到 }B\text{ 的 }\text{ 一 }\text{ 个 }\text{ 映 }\text{ 射 }}\left( {map}\right) , y$ 称为 $x$ 在 $f$ 下的像, $x$ 称为 $y$ 的一个原像。

注意 A 中任何元素的像都是唯一的, 但是 B 中元素的原像却不一定唯一, 例如考虑 $\mathrm{f} : {\mathrm{R}}^{2} \rightarrow  \mathrm{R},\mathrm{f}\left( \left( {\mathrm{x},\mathrm{y}}\right) \right)  = \mathrm{x}$ ,就是刚才说的取横坐标,任何 $\mathrm{x}$ 的原像都是一条竖直直线; $\mathrm{B}$ 中元素的原像还可能是 $\varnothing$ ,例如考虑 $\mathrm{f} : \mathrm{R} \rightarrow  {\mathrm{R}}^{2},\mathrm{f}\left( \mathrm{x}\right)  = \left( {\mathrm{x},0}\right)$ , 相当于实数对应到平面中的数轴上, 这时候横轴以外的点没有原像。

因此, 我们谈论原像时, 通常谈论的是原像构成的集合。我们再引入如下的定义:

定义: 对于非空集合 $\mathrm{A},\mathrm{B}$ 以及一个给定的 $\mathrm{f} : \mathrm{A} \rightarrow  \mathrm{B}$ ,考虑 $\mathrm{A}$ 的任意子集 $\mathrm{C}$ ,我们称集合 $\{ f\left( x\right)  \mid  x \in  C\}$ 为 $C$ 的像集，记为 $f\left( C\right)$ ; 考虑 $B$ 的任意子集 $D$ ，我们称集合 $\{ x \in  A \mid  f\left( x\right)  \in  D\}$ 为 $D$ 的原像集，记为 ${f}^{-1}\left( D\right)$ 。

有了映射,我们可以看到,函数实际上是一类特殊的映射,它的 $A, B$ 都是数集, $\mathrm{A}$ 称之为定义域, $\mathrm{f}\left( \mathrm{A}\right)$ 称之为值域 (我们在高中的值域实际上就是像集)。数列也是特殊的映射, 它的定义域是正整数集, 值域也是数集, 因此数列可以看作一种特殊的函数。

下面我们来介绍两种大学数学里比较常见的基本的简单的映射:

含入映射: 考虑非空集合 $\mathrm{B},\mathrm{A}$ 是 $\mathrm{B}$ 的非空子集,于是我们可以非常自然地定义一个 $f : A \rightarrow  B$ ,它把自己映成自己: $f\left( x\right)  = x,\forall x \in  A$ ,我们把 $f$ 称之为 $A$ 到 $B$ 的含入映射，通常习惯用小写字母 $i$ 表示含入映射；如果 $A = B$ ，则称 $f$ 是恒同映射,记为 $f = {\mathrm{{id}}}_{A}$ 或简记为id。

限制映射: 若有映射 $\mathrm{f} : \mathrm{A} \rightarrow  \mathrm{B}$ ,那么我们考虑一个 $\mathrm{A}$ 的非空子集 $\mathrm{C}$ ,那么如果只考虑 $\mathrm{f}$ 作用在 $\mathrm{C}$ 的元素上面,这时 $\mathrm{f}$ 就可以看作是 $\mathrm{C} \rightarrow  \mathrm{B}$ 的映射,不过这时定义映射的集合变了,因此这是一个新的映射,我们将其称为 $\mathrm{f}$ 在 $\mathrm{C}$ 上的限制, 记作 ${\left. \mathrm{f}\right| }_{\mathrm{C}}$ ,显然 ${\left. \mathrm{f}\right| }_{\mathrm{C}}\left( \mathrm{x}\right)  = \mathrm{f}\left( \mathrm{x}\right) ,\forall \mathrm{x} \in  \mathrm{C}$ 。

## 二、单射，满射与双射

下面, 我们来介绍三种最为重要的映射分类。

像我们刚才提到的, 一位公民对应到一个身份证号, 这个映射必须要保证的, 最为关键的特点是: 两个人不能有相同的身份证号, 不然的话一个身份证号出来俩人，那不乱套了。因此，不存在多对一是这类映射的一个基本要求。

定义:对于映射 $\mathrm{f} : \mathrm{A} \rightarrow  \mathrm{B}$ ,若 $\mathrm{f}\left( \mathrm{x}\right)  = \mathrm{f}\left( \mathrm{y}\right)  \Rightarrow  \mathrm{x} = \mathrm{y},\forall \mathrm{x},\mathrm{y} \in  \mathrm{A}$ ,即 $\mathrm{B}$ 中每个元素的原像集至多只有一个元素,则称 $\mathrm{f}$ 是单射。

对于映射 $\mathrm{f} : \mathrm{A} \rightarrow  \mathrm{B}$ ,我们知道 $\mathrm{B}$ 的某些元素可能没有原像,这些元素对于问题的研究没有意义。比如每个函数都可以看成定义域到 $\mathrm{R}$ 的映射,但是我们真正关心的是函数的值域。因此, 我们有下面的概念。

定义:对于映射 $\mathrm{f} : \mathrm{A} \rightarrow  \mathrm{B}$ ，若 $\forall \mathrm{y} \in  \mathrm{B},{\mathrm{f}}^{-1}\left( {\{ \mathrm{y}\} }\right)  \neq  \varnothing$ ，即 $\mathrm{B}$ 中每个元素的原像集都非空，则称 $\mathrm{f}$ 是满射(相当于 $\mathrm{f}$ 把 $\mathrm{B}$ 映满)。

不难看出，对任意一个映射，如果我们只考虑像集，去掉没有原像的元素， 那么这个映射都可以看作是满射。

单射和满射能够引出一个重要的概念一一双射。

定义:既单又满的映射称为双射。

双射是一类很重要的映射, 因为它相当于在两个集合之间建立了一一对应: 映满, 并且一对一 (大家可以想一想为什么它就是一一对应了)。因此, 从集合本身的角度来看，这两个集合就是 “一样” 的了。A集合上面有什么东西，我们也可以顺着这个一一对应给搬到 B 映射上去, 这样的话, 在抽象意义下就可以把两个集合等同起来。如果不同的集合上还有不同的数学结构, 那么我们还会希望这个双射有一定的条件, 使得两个集合上的数学结构能够建立某种联系。

单射, 满射和双射是三种重要的集合分类。我们不难看出, 我们常见的一些对应关系里都闪烁着它们的影子。比如含入映射就是一类十分简单的单射; 我们刚才提到的投影就是 ${\mathrm{R}}^{2}$ 到 $\mathrm{R}$ 的投影(取横坐标)就是满射；双射也十分常见,例如, $\mathrm{y} = \tan \mathrm{x}$ 可以看作 $\left( {-\frac{\pi }{2},\frac{\pi }{2}}\right)$ 到 $\mathrm{R}$ 的一个双射 (确实既单又满),并且这个映射还是光滑的。

## 三、映射的性质

下面我们讲点略微枯燥的东西——集合运算和映射之间的性质。这一部分主要是逻辑推理为主, 比较适合各位高中的同志们练习逻辑推理。

定理: 考虑集合 $\mathrm{X},\mathrm{Y}$ 与映射 $\mathrm{f} : \mathrm{X} \rightarrow  \mathrm{Y},{\mathrm{A}}_{1},{\mathrm{\;A}}_{2} \subseteq  \mathrm{X},{\mathrm{B}}_{1},{\mathrm{\;B}}_{2} \subseteq  \mathrm{Y}$ ,则:

(1) ${\mathrm{f}}^{-1}\left( {{\mathrm{\;B}}_{1} \cup  {\mathrm{B}}_{2}}\right)  = {\mathrm{f}}^{-1}\left( {\mathrm{\;B}}_{1}\right)  \cup  {\mathrm{f}}^{-1}\left( {\mathrm{\;B}}_{2}\right)$

(2) ${f}^{-1}\left( {{B}_{1} \cap  {B}_{2}}\right)  = {f}^{-1}\left( {B}_{1}\right)  \cap  {f}^{-1}\left( {B}_{2}\right)$

(3)我们把对应集合在 $X, Y$ 中的补集用右上角标 $c$ 来表示，例如 $A$ 在 $X$ 中的补集是 ${A}_{1}^{c}$ ,则 ${f}^{-1}\left( {B}_{1}^{c}\right)  = {\left( {f}^{-1}\left( {B}_{1}\right) \right) }^{c}$

(4) $f\left( {{A}_{1} \cup  {A}_{2}}\right)  = f\left( {A}_{1}\right)  \cup  f\left( {A}_{2}\right)$

我们只讲一下(1)(4)，其它留作练习。注意证明时需要判定集合相等， 数学上一般判定两个集合 $A, B$ 相等采用证明 $x \in  A \Leftrightarrow  x \in  B$ 的方式。

例如如下证明:

$\mathrm{x} \in  {\mathrm{f}}^{-1}\left( {{\mathrm{\;B}}_{1} \cup  {\mathrm{B}}_{2}}\right) \; y \in  f\left( {{A}_{1} \cup  {A}_{2}}\right)$

$\Leftrightarrow  f\left( x\right)  \in  {B}_{1} \cup  {B}_{2} \; \Leftrightarrow  \exists x \in  {A}_{1} \cup  {A}_{2}, f\left( x\right)  = y$

(1): $\Leftrightarrow  \mathrm{f}\left( \mathrm{x}\right)  \in  {\mathrm{B}}_{1}$ 或 $\mathrm{f}\left( \mathrm{x}\right)  \in  {\mathrm{B}}_{2}$ (4): $\Leftrightarrow  \exists \mathrm{x} \in  {\mathrm{A}}_{1},\mathrm{f}\left( \mathrm{x}\right)  = \mathrm{y}$ 或 $\exists \mathrm{x} \in  {\mathrm{A}}_{2},\mathrm{f}\left( \mathrm{x}\right)  = \mathrm{y}$

$\Leftrightarrow  \mathrm{x} \in  {\mathrm{f}}^{-1}\left( {\mathrm{\;B}}_{1}\right)$ 或 $\mathrm{x} \in  {\mathrm{f}}^{-1}\left( {\mathrm{\;B}}_{2}\right) \; \Leftrightarrow  \mathrm{y} \in  \mathrm{f}\left( {\mathrm{A}}_{1}\right)$ 或 $\mathrm{y} \in  \mathrm{f}\left( {\mathrm{A}}_{2}\right)$

$\Leftrightarrow  \mathrm{x} \in  {\mathrm{f}}^{-1}\left( {\mathrm{\;B}}_{1}\right)  \cup  {\mathrm{f}}^{-1}\left( {\mathrm{\;B}}_{2}\right) \; \Leftrightarrow  \mathrm{y} \in  \mathrm{f}\left( {\mathrm{A}}_{1}\right)  \cup  \mathrm{f}\left( {\mathrm{A}}_{2}\right)$

可以看到, 上面的证明就是在进行等价变形 (也就是我们以前讲过的充要替换)。对问题进行等价变形, 不断向目标靠拢, 是数学的基本方法之一。

我们还有必要介绍一下映射的复合。这相当于复合函数的推广。

定义: 设 $\mathrm{f} : \mathrm{X} \rightarrow  \mathrm{Y}$ 和 $\mathrm{g} : \mathrm{Y} \rightarrow  \mathrm{Z}$ 都是映射, $\mathrm{f},\mathrm{g}$ 的复合是 $\mathrm{X} \rightarrow  \mathrm{Z}$ 的映射,记为 $\mathrm{g} \circ  \mathrm{f} : \mathrm{A} \rightarrow  \mathrm{B},\mathrm{g} \circ  \mathrm{f}\left( \mathrm{x}\right)  = \mathrm{g}\left( {\mathrm{f}\left( \mathrm{x}\right) }\right)$ 。

不难看出,映射的复合有 “结合律”,如果再加一个映射 $\mathrm{h} : \mathrm{Z} \rightarrow  \mathrm{W}$ ,那么显然 $\mathrm{g} \circ  \mathrm{f}$ 可以和 $\mathrm{h}$ 继续复合,同时 $\mathrm{f}$ 也可以和 $\mathrm{h} \circ  \mathrm{g}$ 复合,并且这两种不同的连续的复合是一样的,也就是 $\mathrm{h} \circ  \left( {\mathrm{g} \circ  \mathrm{f}}\right)  = \left( {\mathrm{h} \circ  \mathrm{g}}\right)  \circ  \mathrm{f}$ ,因此一般简写成 $\mathrm{h} \circ  \mathrm{g} \circ  \mathrm{f}$ 。

定理: 若 $\mathrm{B} \subseteq  \mathrm{Z}$ ,则 ${\left( \mathrm{g} \circ  \mathrm{f}\right) }^{-1}\left( \mathrm{\;B}\right)  = {\mathrm{f}}^{-1}\left( {{\mathrm{\;g}}^{-1}\left( \mathrm{\;B}\right) }\right)$

证明方法和刚才一样,写等价就行: $\begin{array}{l} x \in  {\left( g \circ  f\right) }^{-1}\left( B\right) \\   \Leftrightarrow  g\left( {f\left( x\right) }\right)  \in  B \\   \Leftrightarrow  f\left( x\right)  \in  {g}^{-1}\left( B\right) \\   \Leftrightarrow  x \in  {f}^{-1}\left( {{g}^{-1}\left( B\right) }\right)  \end{array}$ 。

## 四、形形色色的映射

下面，为大家简单介绍几种大学数学中十分重要的映射。

## 向量函数与多元函数:

对于 $\mathrm{A} \subseteq  \mathrm{R}$ (常见的如 $\mathrm{R}$ ,区间等),则 $\mathrm{A}$ 到 ${\mathrm{R}}^{2}$ 的映射被称为向量函数 (还可以定义到更高维)。比如我们考察一个在平面内运动的质点, 其运动的时间 $\mathrm{t} \in  \left\lbrack  {0,1}\right\rbrack$ ,那么该质点的速度就相当于时间 $\mathrm{t}$ 的函数,但是因为速度是矢量, 单纯一个数字作为像是不够用的,因此我们把向量作为像 (取坐标相当于 ${\mathrm{R}}^{2}$ 中的点), 这样就产生了向量函数。向量函数的是函数的一种推广, 使用映射来定义十分严谨且方便。

函数是一个数决定另一个数, 但是有时候这还不够用。比如我们考虑等高线地形图, 每一个点都对应一个海拔, 但是平面为 2 个自由度, 无法用我们高中学习的函数来表示，因此这里的海拔实际上相当于两个变量的函数，即映射: $\mathrm{f} : \mathrm{A} \subseteq  {\mathrm{R}}^{2} \rightarrow  \mathrm{R}$ ,这个时候如果 $\left( {\mathrm{x},\mathrm{y}}\right)$ 对应到 $\mathrm{z}$ ,一般习惯写 $\mathrm{f}\left( {\mathrm{x},\mathrm{y}}\right)  = \mathrm{z}$ 。类似可定义更高维的多元函数,例如描述三维空间的电场强度就需要三元函数。

## 线性映射:

我们常见的向量空间,如一维的 ${\mathrm{R}}^{1}$ ,二维的 ${\mathrm{R}}^{2}$ ,三维的 ${\mathrm{R}}^{3}$ ,它都可以看成是以原点为起点的向量构成的空间 (不过二维是平面向量, 三维是空间向量罢了)。在不同的向量空间之间, 可以建立映射, 不过太过于随意的映射我们不太喜欢, 我们喜欢具有比较好的性质的那种。其中, 性质最好的一类就是线性映射, 也就是保持向量加法和数乘的映射。

考虑两个向量空间之间的映射 $\mathrm{f}$ ,如果对 “定义域” 内的任意 $\overrightarrow{\mathrm{x}},\overrightarrow{\mathrm{y}}(\overrightarrow{\mathrm{x}},\overrightarrow{\mathrm{y}}$ 都是向量), $f\left( \overrightarrow{x}\right)  + f\left( \overrightarrow{y}\right)  = f\left( {\overrightarrow{x} + \overrightarrow{y}}\right)$ ; 且对任意 $k \in  R, f\left( {k\overrightarrow{x}}\right)  = {kf}\left( \overrightarrow{x}\right)$ (这里的加法和数乘都对应向量的加法和数乘),那么我们称 $\mathrm{f}$ 是线性映射。

线性映射只考虑保证向量加法和数乘的一致性, 也就是向量线性运算的一致性。实际上, “线性” 二字的核心也在于加法和数乘。

我们首先考察一下 $\mathrm{R} \rightarrow  \mathrm{R}$ 的线性映射 (实数也可以看作一条线上的向量)。 这时候为了简略,我们就不写箭头了。注意到这个时候,对 $\forall \mathrm{x} \in  \mathrm{R}$ ,我们结合第二个性质可以得到 $f\left( x\right)  = f\left( {x \cdot  1}\right)  = {xf}\left( 1\right) , f\left( 1\right)$ 对于 $f$ 而言是一个定值,所以 $\mathrm{f}$ 一定是正比例函数或者恒为 0 的函数。检验第一条性质发现也对,所以 $\mathrm{R}$ 到它自身的线性映射, 其实结构非常简单。

下面,我们看一下 ${\mathrm{R}}^{2} \rightarrow  {\mathrm{R}}^{2}$ 的线性映射。这相当于把一个平面向量映成一个平面向量。这个时候单纯只用第二个性质就不行了, 因为方向变多了, 但是第二个性质只是说在同一条直线上的共线向量的事情。我们想起平面向量基本定理, 它是说找一组基底就可以唯一的表示任何一个向量。比如我们找单位正交基底 $\overrightarrow{{\mathrm{e}}_{1}} = \left( {1,0}\right) ,\overrightarrow{{\mathrm{e}}_{2}} = \left( {0,1}\right)$ ,那么 $\left( {\mathrm{x},\mathrm{y}}\right)$ 就是 $\mathrm{x}\overrightarrow{{\mathrm{e}}_{1}} + \mathrm{y}\overrightarrow{{\mathrm{e}}_{2}}$ 。我们把两条性质全用上, 得到 $f\left( {x, y}\right)  = f\left( {x\overrightarrow{{e}_{1}} + y\overrightarrow{{e}_{2}}}\right)  = {xf}\left( \overrightarrow{{e}_{1}}\right)  + {yf}\left( \overrightarrow{{e}_{2}}\right)$ 。

注意 $\mathrm{f}\left( \overrightarrow{{\mathrm{e}}_{1}}\right) ,\mathrm{f}\left( \overrightarrow{{\mathrm{e}}_{2}}\right)$ 也都是平面向量,设它们分别是 $\left( {\mathrm{a},\mathrm{b}}\right) ,\left( {\mathrm{c},\mathrm{d}}\right)$ ,那么代回去就得到 $f\left( {x, y}\right)  = \left( {{ax} + {cy},{bx} + {dy}}\right)$ ,因此可以看到, $f\left( {x, y}\right)$ 的两个分量都分别是它横, 纵坐标的线性组合。

${\mathrm{R}}^{2} \rightarrow  {\mathrm{R}}^{2}$ 的线性映射加上平移就是我们熟悉的二维仿射变换,仿射变换不仅是几何学的一种重要观点, 也对大家的高中数学有一定的价值, 可以帮助大家更好的从几何角度来理解圆锥曲线中的一些现象。我们下一期科普系列视频会开始为大家科普仿射几何。

另外, 可以看到, 线性映射的定义中, 只涉及加法和数乘。也就是说, 不仅仅是平面向量, 空间向量这些真正的向量, 只要可以定义加法和数乘的运算 (比如复数, 函数, 多项式等等), 那么就可以类似的定义线性映射。我们在下面的部分会稍微看到一点这样的想法。

## 泛函与算子:

我们在高中接触到的主要的映射就是函数。实际上, 映射只是两个集合的对应, 因此其中蕴含着无限可能。比如, 我们可以把函数也视为元素, 把函数放在一起作为集合，定义这个集合上的映射。

定义:设集合 $\mathrm{L}$ 是定义在 $\mathrm{R}$ 上的某些函数(比如连续函数，可导函数等)构成的集合，则 $\mathrm{L}$ 到 $\mathrm{R}$ 的映射称为泛函。

举个例子: 假设 $\mathrm{L}$ 是定义在 $\mathrm{R}$ 上的所有的函数的集合,我们定义 $\varphi  : \mathrm{L} \rightarrow  \mathrm{R}$ , 满足 $\varphi \left( \mathrm{f}\right)  = \mathrm{f}\left( 1\right) ,\forall \mathrm{f} \in  \mathrm{L}$ ,注意这里 $\mathrm{f}$ 本体是函数, $\varphi$ 作用在函数上面。

再比如,假设 $\mathrm{L}$ 是定义在 $\mathrm{R}$ 上的所有可导函数的集合,我们定义 $\varphi  : \mathrm{L} \rightarrow  \mathrm{R}$ , 满足 $\varphi \left( \mathrm{f}\right)  = {\mathrm{f}}^{\prime }\left( 0\right) ,\forall \mathrm{f} \in  \mathrm{L}$ ,这同样是个泛函。

事实上,上面定义的两个泛函都可以看成前面的 “线性映射” 。我们显然可以在 $\mathrm{L}$ 上面定义加法和数乘: $\mathrm{f} + \mathrm{g}$ 就是满足 $\left( {\mathrm{f} + \mathrm{g}}\right) \left( \mathrm{x}\right)  = \mathrm{f}\left( \mathrm{x}\right)  + \mathrm{g}\left( \mathrm{x}\right)$ 的; kf 就是满足 $\left( {kf}\right) \left( x\right)  = {kf}\left( x\right)$ 的。这样的话, $L$ 上面也有加法和数乘,那么,从抽象的意义上来讲, 在线性运算这个角度就可以看成抽象的 “向量” 了。那么前面定义的这两个泛函就可以看成 $\mathrm{L}$ 这个向量空间到 $\mathrm{R}$ 的 “线性映射” 了。由此, 我们可以看到数学是研究结构的, 只要定义是合理的, 就能在各种事物之间找到千丝万缕的联系。

算子则是另一类定义在函数上的映射, 只不过它的像集也是函数构成的集合。比较易于理解的是导算子。我们设 D 是所有定义在 R 上的可导函数构成的集合, $\mathrm{L}$ 是所有定义在 $\mathrm{R}$ 上的函数构成的集合,我们定义映射 $\varphi  : \mathrm{D} \rightarrow  \mathrm{L}$ ,满足 $\varphi \left( \mathrm{f}\right)  = {\mathrm{f}}^{\prime },\forall \mathrm{f} \in  \mathrm{D}$ ,也就是把可导函数映成它的导函数。

不难写出导算子的性质:首先，按照刚才的理解，导算子是线性映射；其次,导算子对乘法也有要求: $\varphi \left( \mathrm{{fg}}\right)  = \mathrm{f}\varphi \left( \mathrm{g}\right)  + \mathrm{g}\varphi \left( \mathrm{f}\right) ,\forall \mathrm{f},\mathrm{g} \in  \mathrm{D}$ 。

## 五、总结

映射是对应关系这一概念的精确数学描述。对应关系广泛存在于日常生活和数学研究中, 因此定义, 研究映射是十分必要的事情。函数的概念严格来讲需要先从映射的概念出发才能讲, 但是现在新高考删去了这部分内容, 那么我就给大家补充回来, 这样才符合数学概念的严谨, 完善。

映射以及与其相关的数学内容相当丰富, 它和集合相辅相成, 互相需要彼此, 很多近现代的数学概念也需要通过集合与映射的语言进行阐述。本讲的主要内容只是做了相当粗浅的介绍, 如果还有兴趣的话, 在学有余力的前提下, 可以来自学一下大学的数学, 在我们前面讲的集合与映射的基础上, 了解一些数学分支的基本内容。

本次为大家准备了一些富有挑战性的思考题, 提供给对数学有兴趣的同学进行思考, 琢磨。注意!! 这些题高考一定不会出现, 只是把一些大学的内容简化后给大家来锻炼脑子的。

## 思考题

注意:思考题内部分问题可能涉及到上一期关于集合的科普视频的内容，如果没看过或者忘了的话, 把相关的问题跳过就可以。

1. 映射的性质

(1)请仿照视频中的证明思路，完成把我们视频中第三大部分中，定理的(2) 和 (3) 的证明。

(2)我们在上一期关于集合的科普中提到，并集和交集可以连续并、交无穷多个集合，并且采用指标集的形式来书写。请把视频中第三大部分中，定理的(1)(2)(4)尝试推广到无穷个集合的形式(采用指标集的记法)。

(3)考虑映射 $f : A \rightarrow  B, A,{A}_{2} \subseteq  A$ ,请证明 $f\left( {{A}_{1} \cap  {A}_{2}}\right)  \subseteq  f\left( {A}_{1}\right)  \cap  f\left( {A}_{2}\right)$ ，且当 $\mathrm{f}$ 是单射时这两个集合相等。你能试着举出一个让上面这两个集合不相等 (也就是说, 左边是右边的真子集) 的例子吗?

2. 单射，满射与双射

(1)证明:对于非空集合 $A, B$ ，存在 $A \rightarrow  B$ 的单射等价于存在 $B \rightarrow  A$ 的满射。 (提示: 每一个方向的证明都试着借助已知来构造所证需要的映射)

(2)对于映射 $f : A \rightarrow  B$ ,若存在 $g : B \rightarrow  A$ ,满足 $g \circ  f = {\operatorname{id}}_{A}, f \circ  g = {\operatorname{id}}_{B}$ ,则称 $\mathrm{g}$ 是 $\mathrm{f}$ 的逆映射。证明: $\mathrm{f}$ 是双射当且仅当 $\mathrm{f}$ 存在逆映射。(提示: 正向证明必要性不难,反向证明充分性可以从两个条件分别推出 $\mathrm{f}$ 既单又满)

(3)证明:若 $\mathrm{f}$ 存在逆映射，则逆映射唯一。(提示:结合 $\mathrm{g} \circ  \mathrm{f} = \mathrm{{id}}{}_{\mathrm{A}}$ 以及 $\mathrm{f}$ 的双射性来证明)

3. 线性函数与对偶空间我们考虑 ${\mathrm{R}}^{2} \rightarrow  \mathrm{R}$ 的线性映射 $\mathrm{f}$ ,也就是满足 $\mathrm{f}\left( {\overrightarrow{\mathrm{x}} + \overrightarrow{\mathrm{y}}}\right)  = \mathrm{f}\left( \overrightarrow{\mathrm{x}}\right)  + \mathrm{f}\left( \overrightarrow{\mathrm{y}}\right) ,\forall \overrightarrow{\mathrm{x}},\overrightarrow{\mathrm{y}} \in  {\mathrm{R}}^{2}$ , 且 $\mathrm{f}\left( {\mathrm{k}\overrightarrow{\mathrm{x}}}\right)  = \mathrm{{kf}}\left( \overrightarrow{\mathrm{x}}\right) ,\forall \overrightarrow{\mathrm{x}} \in  {\mathrm{R}}^{2},\mathrm{k} \in  \mathrm{R}$ 的映射,我们把这样的映射称为 ${\mathrm{R}}^{2}$ 上的线性函数。 全体 ${\mathrm{R}}^{2}$ 上的线性函数构成的集合定义为 ${\left( {\mathrm{R}}^{2}\right) }^{ * }$ ,该集合称为 ${\mathrm{R}}^{2}$ 的对偶空间。

(1)定义 ${\mathrm{R}}^{2}$ 中的单位正交基底 $\overrightarrow{{\mathrm{e}}_{1}} = \left( {1,0}\right) ,\overrightarrow{{\mathrm{e}}_{2}} = \left( {0,1}\right)$ 。对于某个 $\mathrm{f} \in  {\left( {\mathrm{R}}^{2}\right) }^{ * }$ ，我们设 $f\left( \overrightarrow{{e}_{1}}\right)  = a, f\left( \overrightarrow{{e}_{2}}\right)  = b$ ,仿照视频内的推理思路,求 $f\left( {x, y}\right)$ ,其中 $x, y \in  R$ 。

(2)证明:对于 $\forall \left( {a, b}\right)  \in  {R}^{2}$ ，存在唯一的 $f \in  {\left( {R}^{2}\right) }^{ * }$ ，使得 $f\left( \overrightarrow{{e}_{1}}\right)  = a, f\left( \overrightarrow{{e}_{2}}\right)  = b$ 。 (提示: 你需要依据 $\mathrm{a},\mathrm{b}$ ,像 (1) 那样写出 $\mathrm{f}$ 的表达式,并验证 $\mathrm{f} \in  {\left( {\mathrm{R}}^{2}\right) }^{ * }$ )

(3)我们构造一个 ${\mathrm{R}}^{2} \rightarrow  {\left( {\mathrm{R}}^{2}\right) }^{ * }$ 的映射 $\varphi$ ,对 $\forall \left( {\mathrm{a},\mathrm{b}}\right)  \in  {\mathrm{R}}^{2},\varphi \left( {\mathrm{a},\mathrm{b}}\right)$ 是( 2 )中的那个唯一的 $\mathrm{f}$ 。证明: $\varphi$ 是双射,且如果在 ${\left( {\mathrm{R}}^{2}\right) }^{ * }$ 上引入加法和数乘的话, $\varphi$ 是线性映射。(提示:注意不同集合的元素的相等的判定不同，如果要判定两个线性函数 $\mathrm{f},\mathrm{g}$ 相同的话,需要确保 $\mathrm{f}\left( \overrightarrow{\mathrm{x}}\right)  = \mathrm{g}\left( \overrightarrow{\mathrm{x}}\right) ,\forall \overrightarrow{\mathrm{x}} \in  {\mathrm{R}}^{2}$ )

4. 简谐振动的解——二阶线性齐次 ode 问题

考虑光滑水平轴上的小球, 在弹簧牵引下做左右来回运动。相当于在一维坐标系 $\mathrm{R}$ 上运动的小球,根据胡克定律,小球受到弹簧拉力和小球的位移成正比, 且拉力始终指向坐标原点,我们假设小球在 $t$ 时刻所在的坐标 (位移) 为 $x\left( t\right)$ , 因此小球的加速度 (矢量) $a\left( t\right)  = {x}^{\prime \prime }\left( t\right)$ ，则 ${ma}\left( t\right)  =  - {kx}\left( t\right)$ ，其中 $m$ 为小球质量， $\mathrm{k}$ 为劲度系数。假设比例恰好为 1,则 ${\mathrm{x}}^{\prime \prime }\left( \mathrm{t}\right)  + \mathrm{x}\left( \mathrm{t}\right)  = 0$ 。

考虑函数 $\mathrm{x}\left( \mathrm{t}\right)$ ,满足 ${\mathrm{x}}^{\prime \prime }\left( \mathrm{t}\right)  + \mathrm{x}\left( \mathrm{t}\right)  = 0$ ,这样的含有导数的方程被称为常微分方程 (ordinary differential equation, 简称 ode) 。我们把所有满足这个方程的函数 $\mathrm{x}\left( \mathrm{t}\right)$ 构成的集合记为 $\mathrm{H}$ (也就是所有的简谐振动的可能解) 。现在设 $\mathrm{x}\left( 0\right)  = {\mathrm{x}}_{0}$ , ${\mathrm{x}}^{\prime }\left( 0\right)  = {\mathrm{v}}_{0}$ ,也就是给定初始位置与初始速度,在数学上相当于给定函数 $\mathrm{x}\left( \mathrm{t}\right)$ 在 $\mathrm{t} = 0$ 的函数值和导数值。我们要研究简谐振动的解,就要研究 $\mathrm{H}$ 的结构。

(1)证明:对 ${\forall }_{{X}_{1}}\left( t\right) ,{x}_{2}\left( t\right)  \in  H,{x}_{1}\left( t\right)  + {x}_{2}\left( t\right)  \in  H$ ，且 $\forall k \in  R, k{x}_{1}\left( t\right)  \in  H$ ，也就是说, $\mathrm{H}$ 关于加法和数乘封闭,于是不难看出 $\mathrm{H}$ 构成一个类似于向量空间的东西(在内部可以做加法，数乘)。

(2)假设弹簧足够长(只考虑数学问题)，物理学的直观告诉我们，当我们给定 ${\mathrm{x}}_{0},{\mathrm{v}}_{0} \in  \mathrm{R}$ 后, $\mathrm{x}\left( \mathrm{t}\right)$ 存在且唯一,即: $\forall \left( {{\mathrm{x}}_{0},{\mathrm{v}}_{0}}\right)  \in  {\mathrm{R}}^{2}$ ,存在唯一的 $\mathrm{x}\left( \mathrm{t}\right)  \in  \mathrm{H}$ , 满足 $\mathrm{x}\left( 0\right)  = {\mathrm{x}}_{0},{\mathrm{x}}^{\prime }\left( 0\right)  = {\mathrm{v}}_{0}$ (这其实是 ode 解的存在唯一性定理,这里直观理解一下就行)。因此我们可以构造一个映射 $\varphi  : {\mathrm{R}}^{2} \rightarrow  \mathrm{H}$ ， $\varphi$ 把 $\left( {{\mathrm{x}}_{0},{\mathrm{v}}_{0}}\right)$ 映成刚才叙述的那个 $\mathrm{x}\left( \mathrm{t}\right)  \in  \mathrm{H}$ 。简要论述这个 $\varphi$ 是双射。(提示:从单射， 满射和双射的定义出发直接论述即可, 其中满射的论述需要结合一下刚才的 ode 解的存在唯一性定理)

(3)证明 $\varphi$ 是线性映射。(因为(1)保证了 $\mathrm{H}$ 对加法和数乘的封闭性，这里对于 $\varphi$ 映过去的对象就可以在 $\mathrm{H}$ 内自由地进行加法和数乘)

(4)由于 $\varphi$ 是双射，同时保持了 ${\mathrm{R}}^{2}$ 上的加法，数乘运算的一致性，因此 $\varphi$ 相当于把 ${\mathrm{R}}^{2}$ 上的线性运算完全复制到了 $\mathrm{H}$ 上; 换而言之, $\mathrm{H}$ 上的加法和数乘运算,在抽象的向量空间的意义下,和 ${\mathrm{R}}^{2}$ 是完全一样的,因此我们可以把它在抽象意义下当成就是 ${\mathrm{R}}^{2}$ 。因此,在 $\mathrm{H}$ 上可以直接用 “平面向量基本定理”,令 ${x}_{1}\left( t\right)  = \varphi \left( {1,0}\right) ,{x}_{2}\left( t\right)  = \varphi \left( {0,1}\right)$ ,请简要论述: $\forall x\left( t\right)  \in  H,\exists a, b \in  R$ , 使得 $x\left( t\right)  = a{x}_{1}\left( t\right)  + b{x}_{2}\left( t\right)$ ,并结合 $\varphi$ 的 “复制功能”,写出这里的 $a, b$ 分别是 $\mathrm{x}\left( \mathrm{t}\right)$ 的什么。(这里的 $\varphi$ 实际上被称为同构，代表了 ${\mathrm{R}}^{2}$ 和 $\mathrm{H}$ 在线性运算结构上的一致性)

(5)验证 ${x}_{1}\left( t\right)  = \cos t,{x}_{2}\left( t\right)  = \sin t$ 是符合上一问定义的(代入常微分方程验证即可)，因此由于 $\varphi$ 是双射，我们可以确信 $\operatorname{cost},\operatorname{sint}$ 就是 ${\mathrm{R}}^{2}$ 中 ${\overrightarrow{\mathrm{e}}}_{1},{\overrightarrow{\mathrm{e}}}_{2}$ 复制过来的,据此写出所有 ${x}^{\prime \prime }\left( t\right)  + x\left( t\right)  = 0$ 的解的函数的一般形式。