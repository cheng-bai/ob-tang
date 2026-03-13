# 过于固定的思维方式：一道高一难题稳定破解思路-dollar
## 题目:

设函数 $f\left( x\right)  = \left| {x + \frac{4}{x} - {ax} - b}\right|$ ,若对任意实数 $a, b$ ,总存在 ${x}_{0} \in  \left\lbrack  {1,3}\right\rbrack$ 使得 $f\left( {x}_{0}\right)  \geq  m$ 成立，则实数 m 的最大值为___。

这是一道典型的封装命题类问题, 不过其约束变元多, 充要替换有一定难度, 导致本题的整体难度比较高, 放在高一年级绝对是一道顶级难度的题目。不过, 如果能较好地掌握我讲过的封装命题处理思维，解决这道题还是不会太依赖灵感和智商的。

所谓 “封装命题”，就是某些自由度被量词(任意，存在)约束，导致该自由度所描述的主要矛盾不再是自身。例如,“任意实数 $\mathrm{x}$ 的平方都是非负的”,这里的 $\mathrm{x}$ 作为一个自由度遍历整个实数, 但是因为前面加了 “任意” 这个量词, 导致这个命题的主要矛盾不再是这个自由度 $\mathrm{X}$ ,而是整个实数轴这个静态对象,于是这个命题就成为了一个静态命题,而不是被动态的 $\mathrm{x}$ 控制的命题了。

关于封装命题类问题的处理方法, 我们在 “高中数学经验分享番外篇” 中有着详细的讲解, 建议在观看过那一期视频后再来学习本题。我们在番外篇中给出了封装命题的统一思维方式, 就是冻结, 遍历, 设问的大致思维路线。当出现 (多个) 被封装的约束变元时, 应当按照它们在要素关系网中出现的顺序，先冻结靠前的，研究靠后出现的约束变元，通过遍历, 设问加充要替换的思维方式去尝试消去约束变元, 在重复上述步骤直至消去所有约束变元。

我们来看本题。题目一共出现了三个约束变元 $\mathrm{a},\mathrm{b},{\mathrm{x}}_{0}$ ,其中 $\mathrm{a},\mathrm{b}$ 是同时出现的,都加的“任意”约束，所以看成 $\forall a,\forall b$ 和 $\forall b,\forall a$ 都可以。但是 ${x}_{0}$ 肯定是最后出现的，于是我们先冻结(随便固定一组)a，b，然后来看这时的命题:存在 ${x}_{0} \in  \left\lbrack  {1,3}\right\rbrack$ 使得 $f\left( {x}_{0}\right)  \geq  m$ 。 这个命题的充要替换是非常基础的，都讲烂了，连遍历和设问都不值得去使用了。其等价于 “ $\mathrm{f}{\left( \mathrm{x}\right) }_{\max } \geq  \mathrm{m}$ ”,当然,要限制定义域为 $\left\lbrack  {1,3}\right\rbrack$ 。于是最后一层封装 ${\mathrm{x}}_{0}$ 就被我们消去了。

我们把思维焦点从 ${\mathrm{x}}_{0}$ 那里离开,继续看剩下的两个约束变元 $\mathrm{a},\mathrm{b}$ 。刚才说到,把它们看成 $\forall a,\forall b$ 和 $\forall b,\forall a$ 都可以,因此下一步的冻结既可以冻结 $\mathrm{a}$ ,也可以冻结 $\mathrm{b}$ ,有两条道路可以选了! 因此，我们需要进行预判与选择。如果我们冻结 $\mathrm{b}$ ,去看 $\mathrm{a}$ ,那么问题就是: 对任意 $\mathrm{a}$ 都有 ${\left| \mathrm{x} + \frac{4}{\mathrm{x}} - \mathrm{a}\mathrm{x} - \mathrm{b}\right| }_{\max } \geq  \mathrm{m}$ 。这是个什么问题呢? 很明显,我们分出两个函数 $\mathrm{g}\left( \mathrm{x}\right)  = \mathrm{x} + \frac{4}{\mathrm{x}}$ 和 $\mathrm{h}\left( \mathrm{x}\right)  = \mathrm{{ax}} + \mathrm{b}$ ,其中 $\mathrm{g}\left( \mathrm{x}\right)$ 是静止的一段对号函数, $\mathrm{h}\left( \mathrm{x}\right)$ (在冻结 $\mathrm{b}$ 活动 $\mathrm{a}$ 时) 是一个过 $\mathrm{y}$ 轴定点 $\left( {0,\mathrm{\;b}}\right)$ 的旋转直线。我们要研究的是过这个定点的旋转和一段对号函数的最大差距,这个元问题好研究吗? $\left| {\mathrm{g}\left( \mathrm{x}\right)  - \mathrm{h}\left( \mathrm{x}\right) }\right|$ 本身作为两个函数的竖直高度差, 这个东西要用 a 带来的旋转去控制, 这本身感觉上就不搭边, 预判的体感肯定不好研究。如果我们冻结 a ，去看 b 呢？刚才说到 g(x) -h(x) 是竖直高度差，正好 b 带来的控制就是竖直移动! 这个感觉是对的, 用操纵竖直移动的主自由度去研究竖直高度差, 比刚才用 a 控制的预判体感要好很多。所以就决定接下来尝试先冻结 a，去研究 b，试着把 b 也消去。

现在的问题是: 任意 $b$ ,都有 ${\left| x + \frac{4}{x} - ax - b\right| }_{\max } \geq  m$ 。这个问题虽然预判上的方向是正确的，但是似乎仍然有些模糊。大致的充要替换方向是有的:冻结 $\mathrm{a}$ ，遍历整个 $\mathrm{b} \in  \mathbb{R}$ ， 那么上面的 ${\left| x + \frac{4}{x} - ax - b\right| }_{\max }$ 就只受 $b$ 控制,相当于一个关于 $b$ 的函数,记为 $\varphi \left( b\right)$ 。我们希望这个 $\varphi \left( b\right)  \geq  m$ 恒成立,也就是希望 $\varphi {\left( b\right) }_{\min } \geq  m$ ,所以关键就是搞清怎么研究 $\varphi {\left( b\right) }_{\min }$ 。

思维仍然模糊的时候, 我们之前说过, 可以尝试思想试验 (参见 “数学的干货” 视频列表)。我们既然冻结了 $\mathrm{a}$ ,那就做个试验,比如我取个 $\mathrm{a} = 1$ (你取别的都行),先尝试研究一个 $\varphi \left( \mathrm{b}\right)  = {\left| \frac{4}{\mathrm{x}} - \mathrm{b}\right| }_{\max }$ 。这就是一段递减函数的上下平移,我们尝试动一动 $\mathrm{b}$ 看看。如果 $\mathrm{b} = {100000}$ ,那么整个反比例函数特别低,绝对值翻上去之后很高, $\varphi \left( \mathrm{b}\right)$ 很大; 而如果 $\mathrm{b} =  - {100000}$ ,同理,反比例函数特别高,绝对值直接去掉也很高, $\varphi \left( \mathrm{b}\right)$ 很大。所以 $\mathrm{b}$ 很大或者很小的时候肯定取不到 $\varphi {\left( \mathrm{b}\right) }_{\min }$ 。继续移动 $\mathrm{b}$ 的滑块,如果移动到 $\mathrm{b} = \frac{4}{3}$ ,减函数段刚好触碰到 $\mathrm{x}$ 轴地面,这时候 $\varphi \left( \mathrm{b}\right)$ 刚好就是这个减函数段本身的高低差 $\left( {4 - \frac{4}{3} = \frac{8}{3}}\right)$ 。继续变大 $\mathrm{b}$ ,减函数段有一部分下沉到 $\mathrm{x}$ 轴以下,这一部分通过绝对值翻到 $\mathrm{x}$ 轴上方。你会发现,此时 $\varphi \left( \mathrm{b}\right)$ 继续变小 (比减函数段本身的高低差 $\frac{8}{3}$ 还要小了)。如果只是下沉下去一点,翻上来一小段,那么 $\varphi \left( \mathrm{b}\right)$ 也就比 $\frac{8}{3}$ 小一点; 如果下沉到正好 $\mathrm{x}$ 轴上方下方各一半,折上去之后 $\varphi \left( \mathrm{b}\right)$ 刚好就是高低差 $\frac{8}{3}$ 的一半,也就是 $\frac{4}{3}$ ; 继续下沉的话, $\mathrm{x}$ 轴下方的部分就很多了,翻上去也会很高,会比 $\frac{4}{3}$ 还高; 再下沉下去的话,整个减函数段就全到 $\mathrm{x}$ 轴下方了, 翻上去之后最大值就不会再小于高低差 $\frac{8}{3}$ 了。

刚才的思想试验能带给我们什么呢? 我们之前说过, 做思想试验的过程本身不是目的, 真正的目的是通过特殊值的试验明白背后的一般规律。刚才 $\varphi \left( \mathrm{b}\right)$ 取最小值是怎么过去的? 首先得有一个高低差,然后需要适度上下平移来把高和低折半,这样才是 $\varphi \left( \mathrm{b}\right)$ 最小值。对于一般的函数, 高低差是什么? 当然是最大值和最小值的差啊! 所以我们就明白了一个事情: $\varphi {\left( \mathrm{b}\right) }_{\min }$ 其实就是把 $\mathrm{y} = \frac{4}{\mathrm{x}} + \mathrm{x} - \mathrm{{ax}}$ 在 $\left\lbrack  {1,3}\right\rbrack$ 上的最大值和最小值拿出来,作差 (就相当于刚才的 $\frac{8}{3}$ )，再除以 2 。b 带来的上下平移不会影响高低差，所以这玩意和 b 本身无关。 这样,我们就得到了一个原命题的充要替换: $y = \frac{4}{x} + x - {ax}$ 的高低差 $\geq  {2m}$ 。预判一下, 高低差就是求最大值和最小值, 对于含参数的对号函数而言并不困难, 因此预判可行。于是现在 b 也被我们消去了。

现在已经消去了两个约束变元,问题变成: 令 $\lambda \left( \mathrm{x}\right)  = \frac{4}{\mathrm{x}} + \mathrm{x} - \mathrm{{ax}},\mathrm{x} \in  \left\lbrack  {1,3}\right\rbrack$ ,对任意 $\mathrm{a}$ , 都有 $\lambda {\left( \mathrm{x}\right) }_{\max } - \lambda {\left( \mathrm{x}\right) }_{\min } \geq  2\mathrm{\;m}$ 。注意这里 $\lambda \left( \mathrm{x}\right)  = \frac{4}{\mathrm{x}} + \left( {1 - \mathrm{a}}\right) \mathrm{x}$ , a 遍历 $\mathbb{R}$ 就相当于 $1 - \mathrm{a}$ 遍历 $\mathbb{R}$ ,所以我们不如直接就当 $\lambda \left( \mathrm{x}\right)  = \frac{4}{\mathrm{x}} + \mathrm{{ax}}$ ,记号还简单。下面只需要求 $\lambda \left( \mathrm{x}\right)$ 在 $\left\lbrack  {1,3}\right\rbrack$ 上的两个最值即可。

当 $\mathrm{a} \leq  0$ 时 $\lambda \left( \mathrm{x}\right)$ 递减; $\mathrm{a} > 0$ 时 $\lambda \left( \mathrm{x}\right)$ 在 $\left( {0,\frac{2}{\sqrt{\mathrm{a}}}}\right)$ 上减, $\left( {\frac{2}{\sqrt{\mathrm{a}}}, + \infty }\right)$ 上增,因此 $\frac{2}{\sqrt{\mathrm{a}}} \geq  3$ , 即 $0 < a \leq  \frac{4}{9}$ 时 $\lambda \left( x\right)$ 也在 $\left\lbrack  {1,3}\right\rbrack$ 上减,这时 $\lambda {\left( x\right) }_{\max } = \lambda \left( 1\right)  = a + 4,\lambda {\left( x\right) }_{\min } = \lambda \left( 3\right)  = {3a} + \frac{4}{3}$ , 于是高低差为 $\frac{8}{3} - 2\mathrm{a}$ 。当 $\frac{2}{\sqrt{\mathrm{a}}} \leq  1$ 即 $\mathrm{a} \geq  4$ 时高低差反过来,是 $2\mathrm{a} - \frac{8}{3}\text{ 。 }\frac{4}{9} < \mathrm{a} < 4$ 时,显然 $\lambda {\left( \mathrm{x}\right) }_{\min } = \lambda \left( \frac{2}{\sqrt{\mathrm{a}}}\right)  = 4\sqrt{\mathrm{a}}$ 。但是最大值要从 $\lambda \left( 1\right)$ 和 $\lambda \left( 3\right)$ 中选,不难看出 $\frac{4}{9} < \mathrm{a} \leq  \frac{4}{3}$ 时 $\lambda \left( 1\right)$ 更大,此时高低差为 $\mathrm{a} + 4 - 4\sqrt{\mathrm{a}} = {\left( \sqrt{\mathrm{a}} - 2\right) }^{2};\frac{4}{3} \leq  \mathrm{a} < 4$ 时 $\lambda \left( 3\right)$ 更大,此时高低差为 $3\mathrm{a} + \frac{4}{3} - 4\sqrt{\mathrm{a}} = 3{\left( \sqrt{\mathrm{a}} - \frac{2}{3}\right) }^{2}$ 。

现在高低差已经被表示成了 $\mathrm{a}$ 的函数 (上面的四段),这个函数恒 $\geq  2\mathrm{\;m}$ ,所以只需要求这个静态函数的最小值,这已经是轻而易举。直接就能判断出它在 $\mathrm{a} \leq  \frac{4}{3}$ 时都递减,在 $\mathrm{a} \geq  \frac{4}{3}$ 时都增,于是高低差函数的最小值在 $\mathrm{a} = \frac{4}{3}$ 时取,代入得到最小值是 $\frac{{16} - 8\sqrt{3}}{3}$ 。因此最后 $2\mathrm{\;m} \leq  \frac{{16} - 8\sqrt{3}}{3}$ ,得到最后 $\mathrm{m}$ 的最大值是 $\frac{8 - 4\sqrt{3}}{3}$ 。

## 总结:

本题综合运用了封装命题的处理思想, 通过不断地依靠冻结来消去靠后的约束变元, 最后回归到问题本身的主要矛盾上去。因为题目的约束变元比较多, 因此消去过程也比较多, 从而增加了题目本身的思维容量。另外, 在消去过程中, 预判, 思想试验, 遍历等思想均得到了综合使用, 最后的计算过程也很考察计算基本功。整体而言, 本题的面向群体是 130 分及以上的同学。本题或许也有更加简易的方法, 但视频中呈现的方法则更容易想到, 更加按部就班, 且稳定性很高, 熟悉本人之前讲过的这些思想, 并且有较好的基本功就能基本稳定解出。希望大家通过本题, 能够加深自己对 “数学的干货” 视频列表中补充思想的理解, 提高自己的思维能力, 体会冻结, 遍历, 设问, 思想试验等思想的科学性和稳定性。

## 整体思路回顾时间规划:

读题,识别出封装命题结构: $1\mathrm{\;{min}}$

消去约束变元 ${x}_{0}$ ，得到等价命题 “对任意 $a, b$ 都有 ${\left| x + \frac{4}{x} - ax - b\right| }_{\max } \geq  m$ ”: 0.5 min

预判下一步消谁,选择消 $\mathrm{b} : {1.5}\mathrm{{min}}$

通过思想试验,明白 $\varphi {\left( \mathrm{b}\right) }_{\min }$ 就是高低差除以 2,从而消去 $\mathrm{b} : {2.5}\mathrm{{min}}$

讨论 $\lambda \left( \mathrm{x}\right)$ 的高低差,并判断其关于 $\mathrm{a}$ 的单调性: ${3.5}\mathrm{\;{min}}$

求出最后的答案: $1\mathrm{\;{min}}$

合计:10min

## 课后练习:

我们在视频中说到, $\varphi {\left( \mathrm{b}\right) }_{\min }$ 就是函数的高低差 (最大值和最小值的差除以 2 )。这一事实比较容易在直观上接受, 但是我们并没有严格写出逻辑证明。请大家尝试给出该命题的严格描述, 并逻辑严谨地给出证明。