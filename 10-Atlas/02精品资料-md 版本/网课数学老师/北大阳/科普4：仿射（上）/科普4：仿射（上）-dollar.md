# 科普4：仿射（上）-dollar
## 给中学生的数学科普 time——第四期

主讲:にちじょうの涂山苏苏

事前声明:

本次内容主要为仿射几何的基础知识, 属于大学数学的知识, 但是作为一种几何思想, 对高中的几何问题也有一定的帮助。本讲内容的前置知识为平面向量的线性运算, 建议高中几何知识学完的同学再来观看。为了方便高中生理解, 内容中的部分定义和表述进行了简化的简化处理, 因此可能部分地方不够严谨, 感兴趣的同学可以自行查阅大学数学中仿射几何的相关内容。

仿射几何是一种优美的几何观点, 主要数学原理就是向量的线性运算, 同时可以作为一种二级结论而简化部分高中问题。本讲主要讲解仿射坐标系和坐标变换, 下一讲会涉及仿射变换。希望大家通过本讲，感受几何学的魅力，同时提高自己的数学思维与解题能力。

大家从小学到高中学习的几何学，都涉及到什么内容呢?

角度, 平行, 垂直, 全等, 长度, 夹角, 面积......内容相当丰富呢。

不过, 大家认知中的几何, 大都是把大量的概念, 定理堆砌起来, 碰到题目就尝试往上套。今天我给大家讲解的仿射几何，更多的则是一种观念性的东西，通过捕捉问题中存在的仿射结构，来解决一大类具有内在联系的问题。

仿射几何, 其实就是研究只与向量的线性运算有关的几何性质, 在这种观念下，很多的几何问题被统一起来。研究仿射几何主要有两大工具:仿射坐标系与仿射变换。当然, 真正在解决实际问题时, 更多的几何性质也会被考虑进来, 但是敏锐地捕捉到问题中只与仿射几何相关的部分, 然后利用相关内容简化问题, 也是仿射几何的应用之一。

## 一、与线性运算相关的坐标系

我们先来回顾一下向量的线性运算。其实内容是很简单的, 向量的线性运算就是加法和数乘。其中,减法是加法的逆,可以解释为加法: $\overrightarrow{a} - \overrightarrow{b} = \overrightarrow{a} + \left( {-\overrightarrow{b}}\right)$ 。 向量的线性运算其实相当于在平面 ${\mathrm{R}}^{2} = \{ \left( {\mathrm{x},\mathrm{y}}\right)  \mid  \mathrm{x},\mathrm{y} \in  \mathrm{R}\}$ 上定义了一种保持我们通常认知的加法和倍乘(各个分量分别进行加法和倍乘)，并且整体保持了交换律, 结合律, 分配律这些代数定律。事实上, 我们甚至可以把向量线性运算的几何定义直接理解为 ${\mathrm{R}}^{2}$ 上数学运算的几何解释。

与线性运算相关的一个重要的观念是平面向量基本定理, 它揭示了平面上线性运算的结构一一基表示。任取两个非 0 的,不共线的向量 $\overrightarrow{\alpha },\overrightarrow{\beta }$ ,那么平面上任意一个向量都可以被它们唯一的决定。也就是: $\forall \overrightarrow{\gamma } \in  {\mathrm{R}}^{2}$ ,存在唯一的一组 $x, y \in  R$ ,使得 $\overrightarrow{\gamma } = x\overrightarrow{\alpha } + y\overrightarrow{\beta }$ 。

事实上, 从自由度的角度也易于理解: 平面本身为 2 个自由度, 因此, 想要确定平面上的一个点需要对应两个参数。这里的 x, y 正好扮演了这样的角色。

以上都是大家在高中接触过的内容。下面我们来思考一个问题: 如何用参数来表示点? 这其实就是坐标系的含义。我们的平面直角坐标系就是用 2 个参数 (两条轴上的投影数值) 来表示平面上的所有点; 另外还有极坐标系, 也是选择了两个参数(极径和极角)来表示点······保持好？个自由度的前提下，只要你能找到合适的两个数来对应点，就可以称之为坐标系。

那么, 刚才提到的平面向量基本定理, 不就是恰好满足这个条件?

因此, 我们自然就有这样的一种定义坐标系的方法:

定义 (仿射坐标系) : 在平面上取定一个坐标原点 $\mathrm{O}$ ,以及 2 个非零,不共线的向量 $\overrightarrow{\alpha },\overrightarrow{\beta }$ ,则 $\forall \mathrm{P} \in  {\mathrm{R}}^{2}$ ,存在唯一的 $\left( {\mathrm{x},\mathrm{y}}\right)  \in  {\mathrm{R}}^{2}$ ,使得 $\overrightarrow{\mathrm{{OP}}} = \mathrm{x}\overrightarrow{\alpha } + \mathrm{y}\overrightarrow{\beta }$ ,我们称 $\{ \mathrm{O} : \overrightarrow{\alpha },\overrightarrow{\beta }\}$ 为一个仿射坐标系, $\left( {\mathrm{x},\mathrm{y}}\right)$ 称为 $\mathrm{P}$ 在该坐标系下的坐标。

从这个定义可以看出, 我们平时使用的平面直角坐标系其实是仿射坐标系的一种特殊情况: 若取定两个垂直的单位向量 $\overrightarrow{{\mathrm{e}}_{1}},\overrightarrow{{\mathrm{e}}_{2}}$ ,以及任意一个坐标原点 $\mathrm{O}$ (选取可依据具体题目),那么 $\left\{  {\mathrm{O} : \overrightarrow{{\mathrm{e}}_{1}},\overrightarrow{{\mathrm{e}}_{2}}}\right\}$ 就是我们熟悉的平面直角坐标系。

这个仿射坐标系, 有什么用呢? 我们可以看到, 仿射坐标系有相当多, 是一个庞大的集合，比原本的直角坐标系广泛很多。但是它们看上去又都差不多: 都是基于平面向量线性运算的理论定义出来的; 都是取线性分解的系数作为确定某个点的参数依据。这意味着不同的仿射坐标系应当是具有共性的。那么， 如何去寻找, 思考这样的共性?

## 二、线性运算的本质与仿射性质

这就不得不考虑这个理论建立的基础: 平面向量线性运算了。所有的仿射坐标系都是只使用线性运算来确立坐标的, 因此, 如果某些几何性质只与线性运算牵扯到的东西相关，那么自然，在任何一个仿射坐标系中，都应当是类似的 (这体现了一种深刻的思想: 理论的建立基础决定了理论的适用范围)。我们从简单的例子入手，来探索这样的问题。

例:已知 $\Delta \mathrm{{ABC}}$ , $\mathrm{D}$ 为 $\mathrm{{BC}}$ 的中点,试考虑如何定量描述 $\mathrm{D}$ 的位置?

从传统的自由度的角度来看, $\Delta \mathrm{{ABC}}$ 有 3 个自由度, $\mathrm{D}$ 也没有减少自由度, 因此想要实际定下 D 的位置是不太行的。但是, 题目中的所有已知都只与线性运算的性质相关。

什么叫做只与线性运算的性质相关? 我们回顾线性运算的全部内容: 加法, 数乘。加法是在干什么? 是对一些相对位置进行联系,比如 $\overrightarrow{\mathrm{{AB}}} + \overrightarrow{\mathrm{{BC}}} = \overrightarrow{\mathrm{{AC}}}$ ,就是表示了这些点之间的基本位置的行走顺序。

但是, 向量加法的理论组成还有一个重要的部分: 向量相等的判定: 向量相等判定为长度和方向一致, 这里的 “方向一致” 的本质是平行关系, 而 “长度一致” 本质是同向线段的比例为 1 。因此, 向量在考虑加法的时候, 实际上是在考虑方向, 以及同向长度比例意义下的一种位置的计算。

数乘则更为简单:进行数乘得到的向量方向保持平行，长度的比例按照给定的倍率进行变化，这与刚才提到的加法在内在之中“不谋而合”。因此，把加法和数乘综合起来, 就是: 对平行关系和平行意义下的长度比例 (定比分) 进行的 “相对位置” 层面的运算。

这实际上就是线性运算刻画的全部内容。如果问题的描述只与最基本的几何位置(点，线，相交)，平行关系，以及共线的线段比例(定比分)相关， 与其它几何性质一律无关，那么这整个问题自然都可以用线性运算来描述。

幸运的是，我们刚刚建立了仿射坐标系的理论。仿射坐标系就是原原本本的对线性运算的性质进行了定量刻画一一坐标。这里的坐标只涉及到了线性运算的内容, 只与线性运算有关, 但是作为一个定量的工具, 它刻画了整个平面中所有要素与选取的基底 $\overrightarrow{\alpha },\overrightarrow{\beta }$ 的相对位置。

像我们刚才谈到的例子,如果我们取 $\overrightarrow{\mathrm{{AB}}} = \overrightarrow{\alpha },\overrightarrow{\mathrm{{AC}}} = \overrightarrow{\beta }$ ,那么由于我们熟悉的 $\overrightarrow{\mathrm{{AD}}} = \frac{1}{2}\left( {\overrightarrow{\mathrm{{AB}}} + \overrightarrow{\mathrm{{AC}}}}\right)$ ,因此 $\mathrm{D}$ 的坐标就是 $\left( {\frac{1}{2},\frac{1}{2}}\right)$ 。这里我们并没有关心 $\bigtriangleup \mathrm{{ABC}}$ 到底长什么样, 它的边长, 角度等, 我们都不知道, 但是我们使用一个定量的坐标 $\left( {\frac{1}{2},\frac{1}{2}}\right)$ 就表示了 $\mathrm{D}$ 点。这其实是一种思维上的进步,这意味着,我们有希望把解析几何搬到这种啥也不知道, 只知道那些与线性运算相关的最基本的几何关系的情境下去。

实际上, 这就是仿射几何的基本思想。我们把只与线性运算相关的几何性质称之为仿射性质。像刚才提到的, 仿射性质就是只与基本几何位置关系(点， 线, 相交等), 平行 (共线), 以及平行线段的长度比例 (定比分), 这些内容相关, 并被这些内容决定的几何性质。如果一个问题全部都是由仿射性质构成, 那么这个问题就可以使用纯粹的仿射几何的方法解决, 也就是: 线性运算, 仿射坐标系等工具。

我们再看一个例子。这是前段时间一个粉丝发给我的, 算是一个正常的高考难度小题。

例:已知 $\bigtriangleup \mathrm{{ABC}}$ 中, $\mathrm{D}$ 为 $\mathrm{{BC}}$ 的中点,若 $4\overrightarrow{\mathrm{{DE}}} + \overrightarrow{\mathrm{{AD}}} = \overrightarrow{0}$ ,则 $\overrightarrow{\mathrm{{CE}}} = \mathrm{m}\overrightarrow{\mathrm{{AD}}} + \mathrm{n}\overrightarrow{\mathrm{{BE}}}$ , 求 mn 的值为( )

这道题我们画出图一看, 就发现整个问题牵扯到的完全是仿射性质。因此, 具体的关于系统内的线段具体长度, 某个具体角度, 等非仿射性质是应该可以不考虑的, 那么, 在仿射眼光下, 这个问题的自由度是多少呢?

不难看出,如果我们画出图,并考虑仿射坐标系 $\{ \mathrm{A} : \overrightarrow{\mathrm{{AB}}},\overrightarrow{\mathrm{{AC}}}\}$ ,也就是假定 $\overrightarrow{\mathrm{{AB}}},\overrightarrow{\mathrm{{AC}}}$ 静止,那么整个系统的后续要素完全被它们控制(相当于整个系统的全部要素都被基地死死地控制住，没有其他自由度)。因此，在仿射眼光下，这个系统应当是静止的！！

于是, 我们自然可以使用纯粹的解析几何方式来进行求解了! (当然, 你使用传统的线性运算的书写方式来求解也没有问题, 但是, 在仿射眼光下, 把问题变成静止的解析几何, 算坐标的问题, 自然是非常舒适, 踏实的)

建立了坐标系 $\left\{  {\mathrm{A} : \overrightarrow{\mathrm{{AB}}},\overrightarrow{\mathrm{{AC}}}}\right\}$ 之后,我们自然可以画一下图,坐标就是线性分解的分量, 因此, 我们在平面直角坐标系中的, 关于线性运算的, 向量坐标运算公式, 可以直接迁移过来。也就是, 加减法和数乘的坐标运算公式!

不难写出坐标 $\mathrm{B}\left( {1,0}\right) ,\mathrm{C}\left( {0,1}\right)$ ,进而 $\mathrm{D}\left( {\frac{1}{2},\frac{1}{2}}\right)$ ,也就是 $\overrightarrow{\mathrm{{AD}}} = \left( {\frac{1}{2},\frac{1}{2}}\right)$ 。

然后是 $\mathrm{E}$ 。你可以先分析出 $\overrightarrow{\mathrm{{ED}}} = \frac{1}{4}\overrightarrow{\mathrm{{AD}}}$ ,从而 $\overrightarrow{\mathrm{{AE}}} = \frac{3}{4}\overrightarrow{\mathrm{{AD}}} = \left( {\frac{3}{8},\frac{3}{8}}\right)$ ,这就是得到的 $\mathrm{E}\left( {\frac{3}{8},\frac{3}{8}}\right)$ ; 也可以直接暴力转化条件,设 $\mathrm{E}\left( {\mathrm{x},\mathrm{y}}\right)$ ,直接照抄题目中的已知条件得到 $4\left( {\mathrm{x} - \frac{1}{2},\mathrm{y} - \frac{1}{2}}\right)  + \left( {\frac{1}{2},\frac{1}{2}}\right)  = \left( {0,0}\right)$ ,直接求出 $\mathrm{E}\left( {\mathrm{x},\mathrm{y}}\right)  = \left( {\frac{3}{8},\frac{3}{8}}\right)$ 。

剩下的就没有任何难度,直接照抄已知就行。 $\overrightarrow{\mathrm{{CE}}} = \left( {\frac{3}{8},\frac{3}{8}}\right)  - \left( {0,1}\right)  = \left( {\frac{3}{8}, - \frac{5}{8}}\right)$ , $\overrightarrow{\mathrm{{BE}}} = \left( {\frac{3}{8},\frac{3}{8}}\right)  - \left( {1,0}\right)  = \left( {-\frac{5}{8},\frac{3}{8}}\right)$ ,从而写出 $\left( {\frac{3}{8}, - \frac{5}{8}}\right)  = \mathrm{m}\left( {\frac{1}{2},\frac{1}{2}}\right)  + \mathrm{n}\left( {-\frac{5}{8},\frac{3}{8}}\right)$ ,这就是个二元一次方程组了,直接求解就是 $\mathrm{m} =  - \frac{1}{2},\mathrm{n} =  - 1$ ,那最后自然 $\mathrm{{mn}} = \frac{1}{2}$ 。

从此可以看出, 在仿射坐标系中进行的计算, 其实就有点类似于直接把线性运算的过程变成了坐标运算的形式。但是, 在数学意义上, 二者具有本质的差异:仿射坐标系的引入，实际上是抽出了线性运算的本质，利用基表示的原理, 构建了坐标系这一种强力的定量神器, 让运算变成机械化的过程。在仿射的眼光下，原本不静止的一些形状也能够视作静止的事物，从而将线性运算涉及到的几何性质呈现在我们眼前, 这是一种几何的观念与视角, 高于我们平时机械学习几何知识点。

## 三、有趣的坐标变换

仿射坐标系本身是不考虑像长度, 角度这些东西的, 只考虑一些带有 “相对位置” 色彩的玩意 (根本在于线性运算) 。在欣赏过仿射坐标系本身之后, 我们就要来看不同的仿射坐标系之间的 “联系” 了(寻找不同事物之间的联系也是数学的乐趣之一)。

最容易想到的, 对象之间的 “联系”, 一个是在不同的仿射坐标系中观测同一个点的坐标差异, 另一个则是在不同的仿射坐标系中观测坐标相同的两个点的差异。前者是我们今天要看的坐标变换, 后者则是下一期科普视频将要讲到的仿射变换。

我们下面来考虑这样一个问题: 假设平面上已经有了两个仿射坐标系, 那么对于同一个点 $\mathrm{P},\mathrm{P}$ 在这两个坐标系下将会有两个坐标,这俩坐标之间是怎样的关系? 例:考虑一般的平面直角坐标系 $\left\{  {\mathrm{O} : \overrightarrow{{\mathrm{e}}_{1}},\overrightarrow{{\mathrm{e}}_{2}}}\right\}$ ,也就是一组正交单位向量产生的仿射坐标系; 再考虑仿射坐标系 $\left\{  {\mathrm{O} : \overrightarrow{\alpha },\overrightarrow{\beta }}\right\}$ ,其中 $\overrightarrow{\alpha } = \left( {\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2}}\right) ,\overrightarrow{\beta } = \left( {-\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2}}\right)$ , 这里的坐标是在平面直角坐标系下的坐标。也就是说: 新的仿射坐标系相当于原本的坐标系把基底旋转了 ${45}^{ \circ  }$ 。

我们考虑平面上任意一点 $\mathrm{P}$ ,设它在第一个坐标系中的坐标是 $\left( {\mathrm{x},\mathrm{y}}\right)$ ,第二个坐标系中的坐标是 $\left( {{\mathrm{x}}^{\prime },{\mathrm{y}}^{\prime }}\right)$ 。那么 $\left( {\mathrm{x},\mathrm{y}}\right)$ 和 $\left( {{\mathrm{x}}^{\prime },{\mathrm{y}}^{\prime }}\right)$ 有着怎样的关系呢? (这个问题是明确的, 对于每一个不同的仿射坐标系, 我们都可以单独用它来研究平面, 但是用不同的仿射坐标系来研究同一个平面, 会碰撞出怎样的火花? )

实际上, 我们可以看到, 这个问题仍然只和仿射坐标系本身的 “相对位置” 相关, 不涉及线性运算以外的几何性质。因此, 仍然可以用线性运算来解决!

解决方法其实很简单,就是直接翻译仿射坐标系与坐标的定义。P 不是说在 $\{ \mathrm{O} : \overrightarrow{\alpha },\overrightarrow{\beta }\}$ 里的坐标是 $\left( {{\mathrm{x}}^{\prime },{\mathrm{y}}^{\prime }}\right)$ 吗? 那我直接抄定义, $\overrightarrow{\mathrm{{OP}}} = {\mathrm{x}}^{\prime }\overrightarrow{\alpha } + {\mathrm{y}}^{\prime }\overrightarrow{\beta }$ 。

这样,立马就可以搬到 $\left\{  {\mathrm{O} : \overrightarrow{{\mathrm{e}}_{1}},\overrightarrow{{\mathrm{e}}_{2}}}\right\}$ 里去了。 $\overrightarrow{\alpha } = \left( {\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2}}\right) ,\overrightarrow{\beta } = \left( {-\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2}}\right)$ , 所以自然地, $\overrightarrow{\mathrm{{OP}}}$ 在平面直角坐标系 $\left\{  {\mathrm{O} : \overrightarrow{{\mathrm{e}}_{1}},\overrightarrow{{\mathrm{e}}_{2}}}\right\}$ 的坐标就是 (用 $\overrightarrow{\mathrm{{OP}}} = {\mathrm{x}}^{\prime }\overrightarrow{\alpha } + {\mathrm{y}}^{\prime }\overrightarrow{\beta }$ 写)

$$
\overrightarrow{\mathrm{{OP}}} = {\mathrm{x}}^{\prime }\left( {\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2}}\right)  + {\mathrm{y}}^{\prime }\left( {-\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2}}\right)  = \left( {\frac{\sqrt{2}}{2}{\mathrm{x}}^{\prime } - \frac{\sqrt{2}}{2}{\mathrm{y}}^{\prime },\frac{\sqrt{2}}{2}{\mathrm{x}}^{\prime } + \frac{\sqrt{2}}{2}{\mathrm{y}}^{\prime }}\right) \text{ 。 }
$$

这样的话,再结合 $\left\{  {\mathrm{O} : {\overrightarrow{\mathrm{e}}}_{1},{\overrightarrow{\mathrm{e}}}_{2}}\right\}$ 中原始的坐标 $\overrightarrow{\mathrm{{OP}}} = \left( {\mathrm{x},\mathrm{y}}\right)$ ,我们就得到了如下的表达式:

$$
\left\{  \begin{array}{l} x = \frac{\sqrt{2}}{2}{x}^{\prime } - \frac{\sqrt{2}}{2}{y}^{\prime } \\  y = \frac{\sqrt{2}}{2}{x}^{\prime } + \frac{\sqrt{2}}{2}{y}^{\prime } \end{array}\right.
$$

这就是两个坐标系之间，同一个点的坐标变换公式。

从式子的形式可以看出，不同仿射坐标系的坐标变换公式也是线性的，都是些一次的东西加加减减(实际上，如果坐标原点选取不同，可能还要加上点常数项)，和线性运算的“精神内核”一致。

有了这个变换公式, 我们能干什么呢? 马上就能做一个非常美妙的事情。 考虑 $\left\{  {\mathrm{O} : \overrightarrow{{\mathrm{e}}_{1}},\overrightarrow{{\mathrm{e}}_{2}}}\right\}$ 中的反比例函数 $\mathrm{x}\mathrm{y} = 1$ ，这相当于给出了一个图形的方程，相当于这个图形上,坐标 $\left( {\mathrm{x},\mathrm{y}}\right)$ 满足 $\mathrm{{xy}} = 1$ 的点构成的集合 (就是一个图形) 。那么, 如果在 $\left\{  {\mathrm{O} : \overrightarrow{\alpha },\overrightarrow{\beta }}\right\}$ 下观测同样的图形,那么这个图形上的点坐标就是 $\left( {{\mathrm{x}}^{\prime },{\mathrm{y}}^{\prime }}\right)$ ,如果在新坐标系下观测,我们是希望得到 ${\mathrm{x}}^{\prime },{\mathrm{y}}^{\prime }$ 之间满足的方程的。

这在有了坐标变换公式的前提下,已经易如反掌。 $\mathrm{{xy}} = 1$ (旧坐标系) 就等价于 $\left( {\frac{\sqrt{2}}{2}{\mathrm{x}}^{\prime } - \frac{\sqrt{2}}{2}{\mathrm{y}}^{\prime }}\right) \left( {\frac{\sqrt{2}}{2}{\mathrm{x}}^{\prime } + \frac{\sqrt{2}}{2}{\mathrm{y}}^{\prime }}\right)  = 1$ ,整理一下就得到 ${\mathrm{x}}^{\prime 2} - {\mathrm{y}}^{\prime 2} = 2$ 。

这也就是说,新坐标系 (相当于转了 ${45}^{ \circ  }$ 的平面直角坐标系) 中,原本的反比例函数图像的方程是 ${\mathrm{x}}^{\prime 2} - {\mathrm{y}}^{\prime 2} = 2$ ,正是我们在高中学习的双曲线! 因此,这也证实了初中的反比例函数的图像, 就是几何中的双曲线!

从这里, 我们足以看出, 在不同的仿射坐标系中观测同一个事物, 得到的形式可能并不相同。但是, 我们利用仿射坐标系本身, 就可以导出不同观测结果之间的联系来 (也就是坐标变换公式) 。只要有了这个根本的, 基底 (万恶之源)之间的联系，就可以依据它来研究其它一切的联系！

四、仿射坐标系中的直线

最后, 我们利用仿射坐标系, 来研究一类和 “线性” 紧密相关的几何对象 ——直线，看看它的方程长什么样子。

众所周知,在最一般的平面直角坐标系 $\left\{  {\mathrm{O} : \overrightarrow{{\mathrm{e}}_{1}},\overrightarrow{{\mathrm{e}}_{2}}}\right\}$ 中,直线方程的一般形式为 $\mathrm{{Ax}} + \mathrm{{By}} + \mathrm{C} = 0$ ，其中 $\mathrm{A},\mathrm{B}$ 不同时为 0 。那么，既然直线本身就是 “线性” 的代名词，它的形式，直觉上来看，在一般的仿射坐标系中应该会具有这样的一致性。

我们使用和刚才一致的思路来推导仿射坐标系中的直线方程。不过这次, 为了让结论更加具有普遍性, 我们直接对一般的仿射坐标系来操作, 也就是, 带着字母!

我们随便搞一个仿射坐标系 $\{ \mathrm{O} : \overrightarrow{\alpha },\overrightarrow{\beta }\}$ ,以及一条平面直线1。不过,为了能够好好的来计算直线方程, 我们可以把这套东西先放进一个比较标准的体系里面去, 也就是——标准的平面直角坐标系。

取定一个标准的平面直角坐标系 $\left\{  {\mathrm{O} : \overrightarrow{{\mathrm{e}}_{1}},\overrightarrow{{\mathrm{e}}_{2}}}\right\}$ (取在哪都行,不过为了方便, 还是让二者原点重合吧)。这样的话, $\left\{  {\mathrm{O} : \overrightarrow{\alpha },\overrightarrow{\beta }}\right\}$ 的位置就可以描述了,假设在标准直角坐标下, $\overrightarrow{\alpha } = \left( {\mathrm{a},\mathrm{b}}\right) ,\overrightarrow{\beta } = \left( {\mathrm{c},\mathrm{d}}\right) ,1$ 的方程为 $\mathrm{{Ax}} + \mathrm{{By}} + \mathrm{C} = 0$ 。我们仿照刚才算双曲线的方法,计算 1 在 $\left\{  {\mathrm{O} : \overrightarrow{\alpha },\overrightarrow{\beta }}\right\}$ 内的方程。

先得重算一下坐标变换公式吧(毕竟现在是字母形式了)。考虑同一个点 $\mathrm{P}$ ,在 $\left\{  {\mathrm{O} : \overrightarrow{{\mathrm{e}}_{1}},\overrightarrow{{\mathrm{e}}_{2}}}\right\}$ 的坐标为 $\left( {\mathrm{x},\mathrm{y}}\right)$ ,在 $\{ \mathrm{O} : \overrightarrow{\alpha },\overrightarrow{\beta }\}$ 中的坐标是 $\left( {{\mathrm{x}}^{\prime },{\mathrm{y}}^{\prime }}\right)$ ,于是按照坐标定义, $\overrightarrow{\mathrm{{OP}}} = {\mathrm{{xe}}}_{1} + {\mathrm{{ye}}}_{2} = {\mathrm{x}}^{\prime }\overrightarrow{\alpha } + {\mathrm{y}}^{\prime }\overrightarrow{\beta }$ 。另外, $\overrightarrow{\alpha } = {\mathrm{{ae}}}_{1} + {\mathrm{{be}}}_{2},\overrightarrow{\beta } = {\mathrm{{ce}}}_{1} + {\mathrm{{de}}}_{2}$ ,因此, 整理得到 $\overrightarrow{\mathrm{{OP}}} = \left( {{\mathrm{{ax}}}^{\prime } + {\mathrm{{cy}}}^{\prime }}\right) \overrightarrow{{\mathrm{e}}_{1}} + \left( {{\mathrm{{bx}}}^{\prime } + {\mathrm{{dy}}}^{\prime }}\right) \overrightarrow{{\mathrm{e}}_{2}}$ 。从而,得到如下坐标转换公式:

$$
\left\{  \begin{array}{l} x = a{x}^{\prime } + c{y}^{\prime } \\  y = b{x}^{\prime } + d{y}^{\prime } \end{array}\right.
$$

这里有一点需要注意的东西,就是最开始指派 $\mathrm{a},\mathrm{b},\mathrm{c},\mathrm{d}$ 时,不能乱指派,需要保证 $\overrightarrow{\alpha },\overrightarrow{\beta }$ 全部非 0 且不同向,实际上,做到这一点只需要 $\mathrm{{ad}} - \mathrm{{bc}} \neq  0$ 。

下面，激动人心的时候到了！把坐标像之前算双曲线那样，直接换进去。 我们得到 $A\left( {a{x}^{\prime } + c{y}^{\prime }}\right)  + B\left( {b{x}^{\prime } + d{y}^{\prime }}\right)  + C = 0$ ,这就是说,如果 $P\left( {x, y}\right)$ 作为直角坐标系的点在这个直线上,那么换到 $\left\{  {\mathrm{O} : \overrightarrow{\alpha },\overrightarrow{\beta }}\right\}$ 里,坐标变成 $\left( {{\mathrm{x}}^{\prime },{\mathrm{y}}^{\prime }}\right)$ ,那么 ${\mathrm{x}}^{\prime },{\mathrm{y}}^{\prime }$ 需要满足的方程式就是这个, 整理得到:

$$
\left( {\mathrm{{Aa}} + \mathrm{{Bb}}}\right) {\mathrm{x}}^{\prime } + \left( {\mathrm{{Ac}} + \mathrm{{Bd}}}\right) {\mathrm{y}}^{\prime } + \mathrm{C} = 0
$$

这就是新的仿射坐标系中的直线方程(不需记忆，高考也不考这种问题)。

这个推导具有一般性, 因此是普适的。从中可以看出, 任意一条直线, 我们写出它在直角坐标内的方程 (用 Ax + By + C = 0 的形式的话), 再写出仿射坐标系的基底的位置(直角坐标)，就可以得到直线在任意仿射坐标系内的方程了。这个形式和原本的直线方程形式是一致的,都是 $\mathrm{x},\mathrm{y}$ 的一次组合配上个常数的形式, 这也符合我们最初的数学直觉和预期。

注意这里,实际上两个一次项系数 $\mathrm{{Aa}} + \mathrm{{Bb}},\mathrm{{Ac}} + \mathrm{{Bd}}$ 同样不可能全为 0,因为我们预先要求过 $\mathrm{{ad}} - \mathrm{{bc}} \neq  0$ ，本身 $\mathrm{A},\mathrm{B}$ 也不全为 0,这时候是可以证明无法让 $\left\{  \begin{array}{l} \mathrm{{Aa}} + \mathrm{{Bb}} = 0 \\  \mathrm{{Ac}} + \mathrm{{Bd}} = 0 \end{array}\right.$ 同时成立的,大家可以考虑一下这是为什么 (注意这可以看成纯代数问题, 也可以看成解析几何问题) 。另外, 如果任意给一个新坐标系内的直线方程 $\alpha \mathrm{x} + \beta \mathrm{y} + \gamma  = 0$ ,我们可以反向求出原坐标系内的直线方程。因此,一般的仿射坐标系中的直线方程一般式, 其要求和平面直角坐标系中的一般式一致。

既然仿射坐标系中的直线方程形式和我们熟悉的直角坐标中是类似的, 那我们紧接着就会想: 坐标本质是基向量线性表示的系数, 那么, 如果改写回这个形式 (也就是不用仿射坐标系的语言, 直接用向量线性运算的语言, 这样就是纯种的高中问题了)，这个事情会变成什么样子呢? 例: (等和线问题) 考虑 $\Delta \mathrm{{ABC}}$ ,如果平面内点 $\mathrm{D}$ 满足 $\overrightarrow{\mathrm{{AD}}} = \lambda \overrightarrow{\mathrm{{AB}}} + \mu \overrightarrow{\mathrm{{AC}}}$ ,且满足 $\lambda  + \mu  = 1$ ,那么 $\mathrm{D}$ 的位置有怎样的限制呢?

实际上,这是我们高中熟悉的一个基本模型。 $\lambda  + \mu  = 1$ 就等价于 $\mathrm{D}$ 在直线 $\mathrm{{BC}}$ 上。这也符合自由度的观点: 如果 $\Delta \mathrm{{ABC}}$ 视为静态,那么 $\mathrm{D}$ 存在两个自由度, 添加上牵制关系 $\lambda  + \mu  = 1$ 后, $\mathrm{D}$ 被一个自由度控制,表现在平面内就是: $\mathrm{D}$ 的运动轨迹(允许的位置构成的集合)是一条线。

现在,我们在仿射几何的眼光下看这个问题。建立仿射坐标系 $\left\{  {\mathrm{A} : \overline{\mathrm{{AB}}},\overline{\mathrm{{AC}}}}\right\}$ , 那么把条件翻译一下就是 $\mathrm{D}\left( {\lambda ,\mu }\right)$ ,那么 $\lambda  + \mu  = 1$ 就可以看作仿射坐标系下的一个东西的方程了! 刚才讲过了, 这东西就代表一条直线!

那么, 如何去定位这个直线呢? 仿射坐标系因为基底之间位置的不确定性, 因此我们没法单纯从这个直线方程出发, 考虑斜率, 倾斜角, 距离这些玩意, 但幸运的是，两点确定一条直线，我们随便找俩点不就得了？

$\lambda  + \mu  = 1\cdots \cdots$ 找 (1,0) 和 (0,1) 不就得了? 那这俩点还真就刚好对应 B, C , 所以这条线就得是 BC 了。这就是这个模型的仿射解释。

我们再考虑一个进阶点的问题: 把 “ $\lambda  + \mu  = 1$ ” 改成 “ $\lambda  + \mu$ 是定值”,这时候 D 的位置又如何? (这就是大家熟悉的高中二级结论一一等和线了)

一样啊, 假如这个定值是 $\mathrm{t}$ (视为静止参数), 那么 D 的轨迹方程不就变成了 $\lambda  + \mu  = \mathrm{t}$ 了吗? 还是直线啊,为了确定这条直线,只需要确定 $\left( {\mathrm{t},0}\right) ,\left( {0,\mathrm{t}}\right)$ 的位置,这不就是 $\mathrm{t}\overrightarrow{\mathrm{{AB}}},\mathrm{t}\overrightarrow{\mathrm{{AC}}}$ 吗? 如果 $\mathrm{t} \neq  0$ ,无非就是把 $\overrightarrow{\mathrm{{AB}}},\overrightarrow{\mathrm{{AC}}}$ 拉伸或收缩同样的倍率 (记拉伸完的点是 ${\mathrm{B}}^{\prime },{\mathrm{C}}^{\prime }$ ),那么因为是同样倍率,所以 ${\mathrm{B}}^{\prime }{\mathrm{C}}^{\prime }//\mathrm{{BC}}$ ,所以, 这时候 $\mathrm{D}$ 所在的直线就是一条平行于 $\mathrm{{BC}}$ 的直线了,具体平行后的 ${\mathrm{B}}^{\prime }{\mathrm{C}}^{\prime }$ 跑哪去了,这取决于 $\mathrm{t}$ ,也就是 $\lambda  + \mu$ 到底是多少。

当然, $\mathrm{t} = 0$ 时,我们随便取一组点,比如 $\left( {1, - 1}\right) ,\left( {0,0}\right)$ ,画画图就可以看到, 这条直线是过原点的平行于 $\mathrm{{BC}}$ 的直线,道理也是一样的。

这就是等和线的仿射解释: “ $\lambda  + \mu$ 是定值” 就代表了, $\mathrm{D}$ 被限制在某一条平行于 $\mathrm{{BC}}$ 的直线上,直线的位置取决于定值的大小,直线经过坐标轴时的拉伸倍率就是定值的大小( $\mathrm{t\overrightarrow{AB}, t\overrightarrow{AC}}$ )。

我们又立刻想到:除了等和线的 $\lambda  + \mu$ 以外，还是有很多其他样子的直线方程啊。那么，其他那些呢？

例(瞎写的):考虑 $\bigtriangleup  \mathrm{{ABC}}$ ，如果平面内点 $\mathrm{D}$ 满足 $\overrightarrow{\mathrm{{AD}}} = \lambda \overrightarrow{\mathrm{{AB}}} + \mu \overrightarrow{\mathrm{{AC}}}$ ，且满足 $\lambda  - {2\mu } = 1$ ,那么 $\mathrm{D}$ 的位置有怎样的限制呢?

比如随便写一个上面的例子, 我们随手一画三角形, 然后画出仿射坐标系 $\left\{  {\mathrm{A} : \overrightarrow{\mathrm{{AB}}},\overrightarrow{\mathrm{{AC}}}}\right\}$ 。直线 $\lambda  - {2\mu } = 1$ 经过 $\left( {1,0}\right) ,\left( {0, - \frac{1}{2}}\right)$ ，其中 $\left( {1,0}\right)$ 就是 $\mathrm{B},\left( {0, - \frac{1}{2}}\right)$ 代表了 $- \frac{1}{2}\overrightarrow{\mathrm{{AC}}}$ ,也就是: 延长 $\mathrm{{CA}}$ 到 $\mathrm{E}$ ,使得 $\mathrm{{AE}} = \frac{1}{2}\mathrm{{CA}}$ ,然后直线 $\mathrm{{BE}}$ 就是 $\mathrm{D}$ 的轨迹了。类似的, 我们还可以画更多其它的直线......

## 五、总结

本讲的主要内容是仿射坐标系与坐标变换, 是仿射几何的基础内容。仿射几何只关注与线性运算相关的性质, 也就是: 基本几何位置关系 (点, 线, 相交), 平行关系, 共线向量的长度比例。建立在这些几何性质之上的仿射几何, 通过反映这些仿射性质之间的关联, 体现了仿射几何学独特视角的美感与协调。

仿射坐标系是仿射几何强有力的工具, 可以把仿射几何问题定量化, 通过线性运算的核心一一基的线性表示, 引入坐标运算来程序化问题。不同的仿射坐标系之间的关联也是充分诠释了“线性”一词，坐标变换建立了不同仿射坐标系之间的联系，让我们得以在不同仿射视点下观测同一对象的不同展现形式。

本次为大家准备了一些思考题, 提供给对数学有兴趣的同学进行思考。由于本讲内容相对比较贴近高考，因此如果完整听完了本讲内容，是比较推荐对这些问题进行一些体验的。欢迎大家在评论区讨论这些问题。

## 思考题

1. (三角形的重心) 考虑 $\Delta \mathrm{{ABC}}$ , D, E, F 分别是 $\mathrm{{AB}},\mathrm{{BC}},\mathrm{{CA}}$ 的中点。我们建立仿射坐标系 $\left\{  {\mathrm{A} : \overrightarrow{\mathrm{{AB}}},\overrightarrow{\mathrm{{AC}}}}\right\}$ (题中的方程和坐标都在这个坐标系之下讨论)

(1)写出 A, B, C, D, E, F 的坐标,并据此求出直线 AE, BF, CD 的方程(提示: 既然直线方程形式跟直角坐标系差不多, 那么给定两点求直线该怎么做呢)

(2)通过彼此联立，证明 $\mathrm{{AE}},\mathrm{{BF}},\mathrm{{CD}}$ 经过同一点，并写出这个点的坐标

2. (坐标变换) 在传统的平面直角坐标系 $\left\{  {\mathrm{O} : \overrightarrow{{\mathrm{e}}_{1}},\overrightarrow{{\mathrm{e}}_{2}}}\right\}$ 中,我们考虑新的仿射坐标系 $\left\{  {\mathrm{O} : \overrightarrow{{\alpha }_{1}},\overrightarrow{{\beta }_{1}}}\right\}$ ,其中 $\overrightarrow{{\alpha }_{1}} = \left( {\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2}}\right) ,\overrightarrow{{\beta }_{1}} = \left( {-\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2}}\right)$ ; 再考虑另一个仿射坐标系 $\left\{  {\mathrm{O} : \overrightarrow{{\alpha }_{2}},\overrightarrow{{\beta }_{2}}}\right\}$ ,其中 $\overrightarrow{{\alpha }_{2}} = \left( {0,1}\right) ,\overrightarrow{{\beta }_{2}} = \left( {-1,0}\right)$ 。上面的坐标都是 $\left\{  {\mathrm{O} : \overrightarrow{{\mathrm{e}}_{1}},\overrightarrow{{\mathrm{e}}_{2}}}\right\}$ 里的坐标。

(1)如果一个点 $\mathrm{P}$ 在 $\left\{  {\mathrm{O} : \overrightarrow{{\alpha }_{1}},\overrightarrow{{\beta }_{1}}}\right\}$ 内的坐标是 $\left( {{\mathrm{x}}_{1},{\mathrm{y}}_{1}}\right)$ ,在 $\left\{  {\mathrm{O} : \overrightarrow{{\alpha }_{2}},\overrightarrow{{\beta }_{2}}}\right\}$ 内的坐标是 $\left( {{\mathrm{x}}_{2},{\mathrm{y}}_{2}}\right)$ ,求这两个坐标之间的关系,也就是: 求 $\left\{  {\mathrm{O} : \overrightarrow{{\alpha }_{1}},\overrightarrow{{\beta }_{1}}}\right\}$ 和 $\left\{  {\mathrm{O} : \overrightarrow{{\alpha }_{2}},\overrightarrow{{\beta }_{2}}}\right\}$ 之间的坐标变换公式,要求用 ${x}_{2},{y}_{2}$ 的式子分别去表示 ${x}_{1},{y}_{1}$ 。(提示:可以仿照视频里的推导思路,把坐标都统一到 $\left\{  {\mathrm{O} : \overrightarrow{{\mathrm{e}}_{1}},\overrightarrow{{\mathrm{e}}_{2}}}\right\}$ 里)

(2)对比视频第三部分中作为例子的那个坐标变换公式，你发现了(1)中的变换公式和那个例子的变换公式有什么关系? 你能否从几何角度(可以自已画画图看看这些基底的位置关系)给一个理解呢?

3. (旋转了的曲线) 考虑平面直角坐标系 $\left\{  {\mathrm{O} : \overrightarrow{{\mathrm{e}}_{1}},\overrightarrow{{\mathrm{e}}_{2}}}\right\}$ ,其中有一条曲线 $\Gamma$ 的方程为 ${x}^{2} + {y}^{2} - {xy} = 3$ ,这个曲线表示的图形是什么呢?

(1)考虑一个新的仿射坐标系 $\left\{  {\mathrm{O} : \overrightarrow{\alpha },\overrightarrow{\beta }}\right\}$ ，其中 $\overrightarrow{\alpha } = \left( {\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2}}\right)$ ， $\overrightarrow{\beta } = \left( {-\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2}}\right)$ ， 这里的基底坐标是 $\left\{  {\mathrm{O} : \overrightarrow{{\mathrm{e}}_{1}},\overrightarrow{{\mathrm{e}}_{2}}}\right\}$ 里的坐标。我们在视频第三部分中,作为例子推导了这两个坐标系之间的坐标变换公式,并计算了双曲线 ${xy} = 1$ 的新坐标系中的方程。请仿照那个例子,计算 $\Gamma$ 在 $\{ \mathrm{O} : \overrightarrow{\alpha },\overrightarrow{\beta }\}$ 中的新方程 (用 $\left( {{\mathrm{x}}^{\prime },{\mathrm{y}}^{\prime }}\right)$ 即可)；由于 $\{ \mathrm{O} : \overrightarrow{\alpha },\overrightarrow{\beta }\}$ 也是一个标准直角坐标系(只是转了45°)，因此放在这个新系内观测也是一样的,据此,可以得出 $\Gamma$ 是什么图形?

(2)把 $\{ \mathrm{O} : \overrightarrow{\alpha },\overrightarrow{\beta }\}$ 的基底画到直角坐标系 $\left\{  {\mathrm{O} : \overrightarrow{{\mathrm{e}}_{1}},\overrightarrow{{\mathrm{e}}_{2}}}\right\}$ 内，并尝试画出 $\Gamma$ 的图像。

4. (数量积) 仿射几何重点讨论仿射性质, 但是像长度, 角度等这些性质, 单纯靠仿射几何是无法研究的, 这些性质通常称为度量性质。但是, 如果知道了仿射坐标系基底间的度量性质(长度，角度等)，那么这个问题就可以研究了。

(1)我们取一个标准的平面直角坐标系 $\left\{  {\mathrm{O} : \overrightarrow{{\mathrm{e}}_{1}},\overrightarrow{{\mathrm{e}}_{2}}}\right\}$ ,再取一个一般的仿射坐标系 $\{ \mathrm{O} : \overrightarrow{\alpha },\overrightarrow{\beta }\}$ ,其中 $\overrightarrow{\alpha } = \left( {\mathrm{a},\mathrm{b}}\right) ,\overrightarrow{\beta } = \left( {\mathrm{c},\mathrm{d}}\right)$ ,这两个坐标是在 $\left\{  {\mathrm{O} : \overrightarrow{{\mathrm{e}}_{1}},\overrightarrow{{\mathrm{e}}_{2}}}\right\}$ 中的直角坐标。我们知道,在 $\left\{  {\mathrm{O} : \overrightarrow{{\mathrm{e}}_{1}},\overrightarrow{{\mathrm{e}}_{2}}}\right\}$ 中,坐标为 $\left( {{\mathrm{x}}_{1},{\mathrm{y}}_{1}}\right) ,\left( {{\mathrm{x}}_{2},{\mathrm{y}}_{2}}\right)$ 的两个向量的数量积为 ${\mathrm{x}}_{1}{\mathrm{x}}_{2} + {\mathrm{y}}_{1}{\mathrm{y}}_{2}$ ; 现在,请尝试推导: 如果两个向量在 $\left\{  {\mathrm{O} : \overrightarrow{\alpha },\overrightarrow{\beta }}\right\}$ 中的坐标分别是 $\left( {{x}_{1},{y}_{1}}\right) ,\left( {{x}_{2},{y}_{2}}\right)$ ,那么它们的数量积是多少? (提示: 把这两个向量在 $\left\{  {\mathrm{O} : \overrightarrow{{\mathrm{e}}_{1}},\overrightarrow{{\mathrm{e}}_{2}}}\right\}$ 中的坐标算出来然后求数量积,最后的结果请用含 ${\mathrm{x}}_{1},{\mathrm{y}}_{1},{\mathrm{x}}_{2},{\mathrm{y}}_{2}$ 和 $a, b, c, d$ 的式子表示)

(2)上一问的式子看上去有点丑，让我们重新整理一下:设 $\left| \overrightarrow{\alpha }\right|  = m,\left| \overrightarrow{\beta }\right|  = n$ ，以及 $\overrightarrow{\alpha } \cdot  \overrightarrow{\beta } = p$ ,请将上一问的结果整理成用 ${x}_{1}{x}_{2},{y}_{1}{y}_{2},{x}_{1}{y}_{2} + {x}_{2}{y}_{1}$ ,以及 $m, n, p$ 表示的形式,并将它和 $\left\{  {\mathrm{O} : \overrightarrow{{\mathrm{e}}_{1}},\overrightarrow{{\mathrm{e}}_{2}}}\right\}$ 中的标准的数量积计算公式进行比较。

(3)借助上一问的结果思考，如果我们希望数量积公式里只有 ${x}_{1}{x}_{2},{y}_{1}{y}_{2}$ 这两项， 在选取 $\{ \mathrm{O} : \overrightarrow{\alpha },\overrightarrow{\beta }\}$ 时有什么要求? 如果进一步希望这两项的系数相同呢? 如果再希望这两项的系数都为 1 (也就是和标准直角坐标的公式一样)呢?