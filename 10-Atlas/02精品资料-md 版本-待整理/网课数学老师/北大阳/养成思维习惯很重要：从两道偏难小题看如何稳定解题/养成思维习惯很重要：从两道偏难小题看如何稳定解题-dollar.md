## 习题课:要素关系建构与元问题预判练习

## 题目一:

已知平面向量 $\overrightarrow{a},\overrightarrow{b},\overrightarrow{c}$ 满足 $\left| \overrightarrow{a}\right|  = 2,\left| \overrightarrow{b}\right|  = 3,\left| \overrightarrow{c}\right|  = 1$ ，且 $\left( {\overrightarrow{a} - \overrightarrow{c}}\right)  \cdot  \left( {\overrightarrow{b} - \overrightarrow{c}}\right)  =  - 4$ ，则 $\left| {\overrightarrow{a} - \overrightarrow{b}}\right|$ 的取值范围是___。

## 题目二:

已知椭圆 $C : \frac{{x}^{2}}{{a}^{2}} + \frac{{y}^{2}}{{b}^{2}} = 1\left( {a > b > 0}\right)$ 的左右焦点分别为 ${F}_{1},{F}_{2}$ ,离心率为 $e$ 。点 $P$ 在椭圆 $\mathrm{C}$ 上,连接 ${\mathrm{{PF}}}_{1}$ 并延长交 $\mathrm{C}$ 与点 $\mathrm{Q}$ ,连接 ${\mathrm{{QF}}}_{2}$ 。若存在 $\mathrm{P}$ 点使得 $\left| \mathrm{{PQ}}\right|  = \left| {\mathrm{{QF}}}_{2}\right|$ 成立,则 ${\mathrm{e}}^{2}$ 的取值范围是___。

这两道题目都需要构建一个顺畅的要素关系网。我们之间讲要素关系的时候就说过, 构建出好的要素关系网是顺利做题的基础, 因为这直接决定我们后续要算什么, 调用什么元问题, 计算体感如何。而构建好的要素网, 最好的办法就是利用画图法, 带着工程师的意识去操作。画图法就是考虑将题干描述的几何图像画出来, 思考如何画能更加顺畅(多控制，少牵制)，更容易画准确。这样的画图方法给出的要素生成关系就是易于列式的。后续再根据要素网里具体的控制关系，调用相应的元问题去计算即可。

要素关系网是一个抽象的观念，它只描述这个系统里谁“能够”控制谁，而不关心具体怎么控制。具体到怎么算则是需要把元问题展开，把具体已知的数据代进去计算的。因此， 建立要素网的过程只是描述这个系统本身的结构罢了。这也传达出一个要点: 建立要素网应该关注的是题目中的要素结构, 理清题干中的系统的结构是做题的第一步。我经常说 “控制是更根本的”, 控制这个理念本身才是最核心的, 大家做题需要先去关注题干中的系统的结构，不然的话做题只是在到处乱碰，没有目标性，没有踏实感。

既然控制的理念才是最根本的, 我们在做更难的题目的时候, 尤其是想冲击 130 以上的高分的时候, 就需要让思维更加灵活, 在动笔算之前要重点关注题目中的控制关系, 去理顺它的结构。要素关系的语言就是说, 系统的起始的主自由度手握操纵杆, 去控制其他要素, 效果是控制出题目中的重要事物, 例如所求, 例如牵制中的重要参量, 例如多级计算中的中间量。这个控制关系本身是做题的基本, 我们需要先从题目中准确识别这个事物。

我们先看题目一。我们先不必关心已知给的数字怎么参与计算, 而先关注基础的要素关系。显然基础要素就是 $\overrightarrow{\mathrm{a}},\overrightarrow{\mathrm{b}},\overrightarrow{\mathrm{c}}$ ,牵制涉及到 $\left( {\overrightarrow{\mathrm{a}} - \overrightarrow{\mathrm{c}}}\right)  \cdot  \left( {\overrightarrow{\mathrm{b}} - \overrightarrow{\mathrm{c}}}\right)$ ,是由三个向量的信息就能直接控制的参数; 但是所求涉及到 $\left| {\overrightarrow{a} - \overrightarrow{b}}\right|$ ,只是由 $\overrightarrow{a},\overrightarrow{b}$ 的信息控制。从这里就能感觉到,这个题要研究的系统的核心肯定是 $\overrightarrow{a},\overrightarrow{b}$ 构成的, $\overrightarrow{c}$ 至多是陪衬,所以如果要选取主自由度的话,它一定需要反应 $\overrightarrow{a},\overrightarrow{b}$ 的信息。再来看基础要素给出的信息,三个模长都是确定的,所以 $\overrightarrow{a},\overrightarrow{b}$ 系统只剩一个自由度了,所求 $\left| {\overrightarrow{a} - \overrightarrow{b}}\right|$ 显然具备彻底控制死 $\overrightarrow{a},\overrightarrow{b}$ 的效果,因此题目的研究对象就明朗了: $\overrightarrow{a},\overrightarrow{b}$ 这个单自由度系统的主自由度的取值情况是什么? 我强调过很多次, 所求具体是谁并不重要, 关键是要素关系, 动静与控制的观念下问题本质是什么。

现在已经明确题目要研究的就是 $\overrightarrow{\mathrm{a},\mathrm{\;b}}$ 单自由度系统,那我们首先把一个控制杆交给它。 那这个 $\overrightarrow{\mathrm{c}}$ 是干嘛的? 我们来看题: 首先 $\overrightarrow{\mathrm{c}}$ 的模确定,所以至少 $\overrightarrow{\mathrm{c}}$ 目前只有一个自由度控制着。而另一个牵制: $\left( {\overrightarrow{a} - \overrightarrow{c}}\right)  \cdot  \left( {\overrightarrow{b} - \overrightarrow{c}}\right)  =  - 4$ ,显然,如果 $\overrightarrow{a},\overrightarrow{b}$ 的控制杆停下,那么这时候这个牵制就能把 $\overrightarrow{c}$ 彻底静止化。所以我们把要素关系抽象出来: $\overrightarrow{a},\overrightarrow{b}$ 手握一个控制杆， $\overrightarrow{c}$ 是

一个单自由度的东西,有一个和此控制杆相关的牵制能够定死 $\overrightarrow{\mathrm{c}}$ ,求控制杆的活动范围。

上面这个关系网是一个纯抽象的东西, 不含任何计算, 这就是我们需要的东西。解题第一步完成, 我们就可以根据这个关系网去调用元问题, 开展计算。首先, 我们来依据要素结构来识别问题类型。一个控制杆, 一个单自由度参数, 一个控制杆之下的牵制定死单自由度参数, 问控制杆的范围, 这是什么类型的问题? 从脑海里调用元问题, 识别出这是方程有解类问题,就和什么 ${\mathrm{x}}^{2} = \mathrm{a}$ 有解,求 $\mathrm{a}$ 范围这种问题一样。再进一步调用元问题的处理方法:那就是先假定控制杆静止，列出方程，充要替换出有解的条件，再解冻控制杆， 求解有解条件的不等式 (大家看好了, 元问题就是这么用的)。于是开始按照上面的蓝图展开操作。先让控制杆静止,也就是让 $\overrightarrow{a},\overrightarrow{b}$ 系统作为一个静止系统,相当于张开一个确定的三角形, 主自由度因为方程还没列, 所以先不急于选, 看看方程怎么列方便再考虑选取。 方程是 $\left( {\overrightarrow{a} - \overrightarrow{c}}\right)  \cdot  \left( {\overrightarrow{b} - \overrightarrow{c}}\right)  =  - 4$ ,对应元问题: 向量等式变方程,自然是建系。怎么建系? 开始预判, $\overrightarrow{c}$ 肯定是设 $\left( {x, y}\right)$ ,附带约束 $\left| \overrightarrow{c}\right|  = 1$ ,于是选起点为原点就可以。而牵制方程需要 $\overrightarrow{a},\overrightarrow{b}$ 坐标,而且有了坐标,直接点乘,不含根号,式子形式肯定不坏,所以选好坐标系即可。选好原点的话,肯定靠位置无关把 $\overrightarrow{\mathrm{a}}$ 或者 $\overrightarrow{\mathrm{b}}$ 先静止,那另一个就是绕原点转了,主自由度给一个夹角即可,比如设 $\overrightarrow{\mathrm{b}} = \left( {3,0}\right)$ ,再设 $\overrightarrow{\mathrm{a}} = \left( {2\cos \theta ,2\sin \theta }\right)$ ,则 $\theta$ 就是操纵杆,或者不会参数方程的话设 $\overrightarrow{a} = \left( {{x}_{0},{y}_{0}}\right)$ ,附带约束 ${x}_{0}^{2} + {y}_{0}^{2} = 4$ ,则 $\left( {{x}_{0},{y}_{0}}\right)$ 就是操纵杆。我们就选大家容易想到的第二种设法。

先假定 $\left( {{x}_{0},{y}_{0}}\right)$ 静止，于是算出 $\overrightarrow{a} - \overrightarrow{c} = \left( {3 - x, - y}\right) ,\overrightarrow{b} - \overrightarrow{c} = \left( {{x}_{0} - x,{y}_{0} - y}\right)$ ，再点乘得 $\left( {3 - x}\right) \left( {{x}_{0} - x}\right)  - y\left( {{y}_{0} - y}\right)  =  - 4$ ,展开得 ${x}^{2} + {y}^{2} - \left( {{x}_{0} + 3}\right) x - {y}_{0}y + 3{x}_{0} + 4 = 0$ 。而 $\left( {x, y}\right)$ 自带约束 ${x}^{2} + {y}^{2} = 1$ ,所以方程全都列完了,问题充要替换成这个方程组有解。

其实大家应该已经看出来了，这就是两个圆，要它们相交。不过把两个方程隔离出来， 单独看的话,很明显要先把第一个方程变成 $- \left( {{x}_{0} + 3}\right) x - {y}_{0}y + 3{x}_{0} + 5 = 0$ ,这样和第二个方程组合起来,得到的方程组与原方程组等价,而且是直线与 ${x}^{2} + {y}^{2} = 1$ 的联立,非常简单。这时候直线和圆有交点这种元问题就非常基础: $\frac{\left| 3{x}_{0} + 5\right| }{\sqrt{{\left( {x}_{0} + 3\right) }^{2} + {y}_{0}^{2}}} \leq  1$ 。隔离的思维习惯非常普遍, 大家一定要养成。

充要替换已经结束了,这个式子只与原始的控制杆 $\left( {{\mathrm{x}}_{0},{\mathrm{y}}_{0}}\right)$ 有关了,配上 ${\mathrm{x}}_{0}^{2} + {\mathrm{y}}_{0}^{2} = 4$ 的约束。所以直接完成最后的求解即可。把现在的信息全放在一起(一等式一不等式一所求),不难看出把 ${y}_{0}$ 消去即可: $\frac{\left| 3{x}_{0} + 5\right| }{\sqrt{{\left( {x}_{0} + 3\right) }^{2} + 4 - {x}_{0}^{2}}} \leq  1$ ,解这个不等式得到 $- 2 \leq  {x}_{0} \leq   - \frac{2}{3}$ 。 最后 ${\left| \overrightarrow{\mathrm{a}} - \overrightarrow{\mathrm{b}}\right| }^{2} = {\left( {\mathrm{x}}_{0} - 3\right) }^{2} + {\mathrm{y}}_{0}^{2} = {13} - 6{\mathrm{x}}_{0} \in  \left\lbrack  {{17},{25}}\right\rbrack$ ,那答案自然就是 $\left\lbrack  {\sqrt{17},5}\right\rbrack$ 。

可以看到, 整个题目的思考过程就是先建立抽象的要素关系, 根据要素关系识别问题类型, 调用相应的元问题处理方法, 然后顺着关系网, 对每一步的计算做预判, 确认计算可行性, 然后按部就班完成计算即可。在要素关系建立, 元问题预判都做好的前提下, 完成整个题目就是砍瓜切菜。

我们再来看题目二。首先是背景的椭圆C,然后上面一个单自由度动点 $\mathrm{P}$ (不过它在后文来看是被封装了)，P 严格控制 Q 。这时题目给了牵制 $\left| \mathrm{{PQ}}\right|  = \left| {\mathrm{{QF}}}_{2}\right|$ ，一个方程肯定可以求解,所以 $\mathrm{P}$ 是可以被求出来的。背景椭圆在大小无关下只有 $\mathrm{e}$ 这一个自由度。而问的就是“存在 $\mathrm{P}$ ”，即方程有解。看上去和上一题的单自由度系统的一个方程有解是一回事。

下面尝试去调用元问题,并进行预判。需要转化的方程是 $\left| \mathrm{{PQ}}\right|  = \left| {\mathrm{{QF}}}_{2}\right|$ ,调用元问题: 等腰如何充要替换成式子? 显然有两条路,一个是直接算边长,一个是取底边 ${\mathrm{{PF}}}_{2}$ 中点 $\mathrm{N}$ , 式子变成 $\mathrm{{QN}} \bot  {\mathrm{{PF}}}_{2}$ 。先假设椭圆静止,预判第一条路: 如果把主自由度分给 $\mathrm{P}$ ,那么算 $\left| \mathrm{{PQ}}\right|$ 需要有 $\mathrm{{PQ}}$ 的斜率 (这个容易),也需要 $\mathrm{Q}$ 坐标 (这个元问题是已知一交点求另一交点,需要用解点法); 还需要 $\left| {\mathrm{{QF}}}_{2}\right|$ ,这个得用 $\mathrm{Q}$ 坐标。不过如果把主自由度给 $\mathrm{Q},\left| {\mathrm{{QF}}}_{2}\right|$ 的计算就容易一些。如果是第二条路,把主自由度给 $\mathrm{P}$ ,那么只需要通过解点算 $\mathrm{Q}$ 的坐标即可, 比较便利。从预判来看, 第二条路更加舒适, 不过, 既然涉及到解点, 而且还是带着参数的解点, 计算量肯定不小。平时练习处理过含参数解点这一元问题的同学应该会对自己的处理时间有一个了解, 这个计算量已经达到了偏难大题的水平。

如果考场上预判到这里, 而且想不到别的方法的话, 已经可以跳过了。我们重新思考, 这个方法不好, 能不能换一个? 换方法等价于换要素网, 所以重新审视要素关系网。这个要素网显然不符合画图法的标准,等腰三角形根本画不准确,只能瞎点一个 P 来作为示意图,那有没有办法画准确呢? 尝试画一下就明白了。我先画满足 $\left| \mathrm{{PQ}}\right|  = \left| {\mathrm{{QF}}}_{2}\right|$ 的等腰三角形 ${\mathrm{{PQF}}}_{2}$ ,就可以了。那椭圆怎么办呢? 如果先画了 ${\mathrm{{PQF}}}_{2}$ ,那么画椭圆就是画 ${\mathrm{F}}_{1}$ ,这只需要在 $\mathrm{{PQ}}$ 上找满足 $\left| {\mathrm{{PF}}}_{2}\right|  + \left| {\mathrm{{PF}}}_{1}\right|  = \left| {\mathrm{{QF}}}_{2}\right|  + \left| {\mathrm{{QF}}}_{1}\right|$ 的 ${\mathrm{F}}_{1}$ 即可,这个量一下长度就行了,很简单。这样的话整个图像都画出来了, 而且控制很顺畅, 是一个好的关系网!

这时候我们梳理关系网,起始是等腰三角形 ${\mathrm{{PQF}}}_{2}$ ,大小无关的话只有一个自由度, 然后它控制 ${\mathrm{F}}_{1}$ ,进而控制椭圆,控制离心率。那么这个问题就被重构成了已知等腰三角形, 求离心率的取值范围，和一开始的方程有解问题差别很大。有点怪，那么这个时候就思考一下, 这个重构是充要替换吗? 从逻辑上理解一下, 原题是考虑所有的椭圆, 使得存在等腰能按题干放进去，求对应的哪些离心率符合条件；新题是考虑所有的等腰三角形，问控制出来的椭圆的离心率能遍历到哪些值。对于原题的范围, 那样的椭圆肯定能放进合适的等腰三角形 ${\mathrm{{PQF}}}_{2}$ ,所以原题的范围对新题都合适; 反之,新题中给一个等腰三角形,控制出来的椭圆显然也符合原题。所以这两个问题确实是等价的。(大家注意，刚才的这个分析在考场上需要去做, 这样才确保你的思维严谨)

刚才做的这个题目重构, 实际上就是以要素关系网为灵魂的。这里的做题逻辑是: 我先通过画图法认识到了一个新的构建要素关系网的办法，然后对于这个新要素网，我不知道它是不是和原题等价, 所以我做了一点逻辑分析, 发现确实是等价的。动静视角和要素关系网让我们具备了重构题目的能力, 而充要替换的逻辑让我们能够相信自己的判断, 踏实地向前走。

现在可以开始算了。首先大小无关，不妨设 $\mathrm{{PQ}} = 1$ 。下面分配一个主自由度给 ${\mathrm{{PQF}}}_{2}$ 。 分配谁呢? 可以分配给 $\angle {\mathrm{{PQF}}}_{2}$ ,也可以分配给 $\left| {\mathrm{{PF}}}_{2}\right|$ 。我们来做一下计算预判。求的是离心率,也就是椭圆的 $\mathrm{a}$ 和 $\mathrm{c}$ 。而 $\mathrm{a} = \frac{\left| {\mathrm{{PF}}}_{2}\right|  + \left| \mathrm{{PQ}}\right|  + \left| {\mathrm{{QF}}}_{2}\right| }{4} = \frac{2 + \left| {\mathrm{{PF}}}_{2}\right| }{4},\mathrm{c} = \frac{\left| {\mathrm{F}}_{1}{\mathrm{\;F}}_{2}\right| }{2}$ ,所以不管主自由度分配给谁, a 都好控制,分配给角的话稍微麻烦点。但是 $\mathrm{c}$ 则是需要控制 $\left| {{\mathrm{F}}_{1}{\mathrm{\;F}}_{2}}\right|$ , 这个相当于等腰三角形腰上取一个定点 ${\mathrm{F}}_{1}$ 再算距离,隔离出这个元问题,根据要素关系思考一下,就能看出处理方法肯定就是先控制 $\left| {\mathrm{{QF}}}_{1}\right|$ ,然后放在 $\Delta {\mathrm{{QF}}}_{1}{\mathrm{\;F}}_{2}$ 里用余弦定理。所以如果主自由度分配给 $\angle {\mathrm{{PQF}}}_{2}$ 的话,则需要先表示 $\left| {\mathrm{{QF}}}_{1}\right|$ ,这肯定需要 $\left| {\mathrm{{PF}}}_{2}\right|$ 参与,但 $\left| {\mathrm{{PF}}}_{2}\right|$ 也需要 $\angle {\mathrm{{PQF}}}_{2}$ 来控制,这个控制肯定带根号,于是恐怕会出现根号相加的式子; 但是如果主自由度直接分配给 $\left| {\mathrm{{PF}}}_{2}\right|$ 的话,则 $\left| {\mathrm{{QF}}}_{1}\right|$ 很好控制,接下来只需要控制好 $\cos \angle {\mathrm{{PQF}}}_{2}$ , 而这个放在等腰三角形里用余弦定理即可,不带根号,更好一些。所以主自由度给 $\left| {\mathrm{{PF}}}_{2}\right|$ 更优,把它设为 $\mathrm{x} \in  \left( {0,2}\right)$ 。

此时 $\mathrm{a} = \frac{2 + \mathrm{x}}{4}$ ,于是 $\left| {\mathrm{{QF}}}_{1}\right|  = 2\mathrm{a} - \left| {\mathrm{{QF}}}_{2}\right|  = \frac{\mathrm{x}}{2}$ 。又有 $\cos \angle {\mathrm{{PQF}}}_{2} = \frac{1 + 1 - {\mathrm{x}}^{2}}{2 \cdot  1 \cdot  1} = 1 - \frac{{\mathrm{x}}^{2}}{2}$ , 因此 ${\left| {F}_{1}{F}_{2}\right| }^{2} = 1 + \frac{{x}^{2}}{4} - 2 \cdot  1 \cdot  \frac{x}{2} \cdot  \left( {1 - \frac{{x}^{2}}{2}}\right)  = \frac{{x}^{3}}{2} + \frac{{x}^{2}}{4} - x + 1 = \frac{\left( {x + 2}\right) \left( {2{x}^{2} - {3x} + 2}\right) }{4}$ ,因此离心率 ${\mathrm{e}}^{2} = \frac{{\mathrm{c}}^{2}}{{\mathrm{a}}^{2}} = \frac{{\left| {\mathrm{F}}_{1}{\mathrm{\;F}}_{2}\right| }^{2}}{4{\mathrm{a}}^{2}} = \frac{2{\mathrm{x}}^{2} - 3\mathrm{x} + 2}{\mathrm{x} + 2}$ ,定义域 $\mathrm{x} \in  \left( {0,2}\right)$ 。最后求范围就不多说了,非常基础的函数求范围问题,注意一个基本技巧是把 $\mathrm{x} + 2$ 换成 $\mathrm{y}$ ,这样求解更简单,大家自己去求一下即可,最后答案是 $\lbrack 8\sqrt{2} - {11},1)$ 。注意,如果没看出可以因式分解约分的话, 也没关系,大不了求导,时间会多花一些。不过换完 $\mathrm{y}$ 之后分子一定能够直接提出一个 $\mathrm{y}$ 来, 也能够约分约掉。

## 总结:

本次习题课讲解的两道题都体现了要素网, 元问题, 预判, 这三者结合的重要性。要素网体现了题目的结构, 是做题的第一步, 元问题的理解 (基础知识的熟练以及与要素网的匹配)是正确预判与正确解题的基本要求。这也是我们平时一直以来讲解的重点。希望大家多多体会, 多多实践, 只有养成思维习惯才能发挥出这些思维方式的威力。多去思考问题背后的要素关系, 多去用结构的眼光看问题, 学知识和复习知识的时候都用结构, 控制的眼光去看待，以元问题的形式学习，下笔之前多去预判，这样才能慢慢养成思维习惯， 提高自己做题的稳定性与踏实感。

## 时间规划:

题目一:

识别出问题的要素结构, 认识到是方程有解问题: 1min

选取参数的设法,并大致预判计算可行性: $1\mathrm{\;{min}}$

充要替换出 $\frac{\left| 3{x}_{0} + 5\right| }{\sqrt{{\left( {x}_{0} + 3\right) }^{2} + {y}_{0}^{2}}} \leq  1 : 2\mathrm{\;{min}}$

完成最后的计算: $2\mathrm{\;{min}}$

总时间:6min

题目二:

识别出问题的要素结构, 认识到是方程有解问题: 1min

选取参数的设法,并预判计算可行性 (发现计算量过大): $1\mathrm{\;{min}}$

更改方法, 用画图法构建新的要素网: 2min

选取参数的设法, 并预判计算可行性: 1.5min

完成最后的计算: ${3.5}\mathrm{\;{min}}$

总时间: $9\mathrm{\;{min}}$

## 课后练习:

1. 用参数方程的设法 $\overrightarrow{\mathrm{a}} = \left( {2\cos \theta ,2\sin \theta }\right)$ 重新完成题目一的全部计算。

2. 尝试用原始的要素关系网，利用解点的思路完成题目二的计算，并与视频中给出的解法进行计算量上的对比。(一共四条可能的道路, 试着分别预判一下, 算完后和你的预判对照一下，看看符不符合)