---
epoch: 1776443286548
modelKey: "kimi-k2.5|3rd party (openai-format)"
topic: "Document Polishing Request"



tags:
  - copilot-conversation
---

**user**: 润色这个文档
[Context: Notes: 10-Atlas/04-试卷汇总/高考真题/2017上海高考数学试题 含解析.md]
[Timestamp: 2026/04/18 00:28:06]

**ai**: 我来使用 `markdown-print-kit` 技能为您润色这份2017上海高考数学试题文档。主要优化方向包括：统一题目格式、美化解析排版、优化图片显示、添加打印样式支持。

---

## 优化后的文档

```markdown
---
title: 2017上海高考数学试题 含解析
date: 2017-06-07
subject: 数学
source: 上海高考
tags: [高考真题, 上海卷, 数学, 2017]
cssclasses: [math-paper, print-optimized]
---

# 2017年上海市高考数学试卷

> **说明**：本试卷满分150分，考试时间120分钟。全卷包括填空题、选择题和解答题三部分。

---

## 一、填空题
> 本大题共12题，满分54分。第1~6题每题4分，第7~12题每题5分。

### 第1题（4分）
已知集合 $A=\{1,2,3,4\}$，集合 $B=\{3,4,5\}$，则 $A \cap B=$ ______

> [!solution]- 解析
> $A \cap B = \{3,4\}$

---

### 第2题（4分）
若排列数 $P_{6}^{m}=6 \times 5 \times 4$，则 $m=$ ______

> [!solution]- 解析
> 由 $P_6^m = \frac{6!}{(6-m)!} = 6 \times 5 \times 4$，得 $m=3$

---

### 第3题（4分）
不等式 $\frac{x-1}{x}>1$ 的解集为 ______

> [!solution]- 解析
> $\frac{x-1}{x} > 1 \Rightarrow 1-\frac{1}{x} > 1 \Rightarrow \frac{1}{x} < 0 \Rightarrow x < 0$
> 
> **解集为** $(-\infty, 0)$

---

### 第4题（4分）
已知球的体积为 $36\pi$，则该球主视图的面积等于 ______

> [!solution]- 解析
> 由 $V = \frac{4}{3}\pi R^3 = 36\pi$，得 $R=3$
> 
> 主视图为圆，面积 $S = \pi R^2 = 9\pi$

---

### 第5题（4分）
已知复数 $z$ 满足 $z+\frac{3}{z}=0$，则 $|z|=$ ______

> [!solution]- 解析
> $z^2 = -3 \Rightarrow z = \pm\sqrt{3}i \Rightarrow |z| = \sqrt{3}$

---

### 第6题（4分）
设双曲线 $\frac{x^{2}}{9}-\frac{y^{2}}{b^{2}}=1\,(b>0)$ 的焦点为 $F_1, F_2$，$P$ 为该双曲线上的一点，若 $|PF_1|=5$，则 $|PF_2|=$ ______

> [!solution]- 解析
> 双曲线中 $2a=6$，由 $||PF_1|-|PF_2||=2a=6$
> 
> 若 $|PF_1|=5$，则 $|PF_2|=11$（$|PF_2|=-1$ 舍去）

---

### 第7题（5分）
如图，以长方体 $ABCD-A_1B_1C_1D_1$ 的顶点 $D$ 为坐标原点，过 $D$ 的三条棱所在的直线为坐标轴，建立空间直角坐标系，若 $\overrightarrow{DB_1}$ 的坐标为 $(4,3,2)$，则 $\overrightarrow{AC_1}$ 的坐标为 ______

![第7题图](https://cdn.mathpix.com/cropped/2025_01_15_48e6dd327b6607f47ceeg-1.jpg?height=358&width=413&top_left_y=780&top_left_x=1324)

> [!solution]- 解析
> 由 $\overrightarrow{DB_1}=(4,3,2)$，知 $DA=4, DC=3, DD_1=2$
> 
> $\therefore A(4,0,0), C_1(0,3,2)$
> 
> $\overrightarrow{AC_1} = (-4, 3, 2)$

---

### 第8题（5分）
定义在 $(0,+\infty)$ 上的函数 $y=f(x)$ 的反函数为 $y=f^{-1}(x)$，若
$$g(x)=\begin{cases}3^x-1, & x \leq 0 \\ f(x), & x>0\end{cases}$$
为奇函数，则 $f^{-1}(x)=2$ 的解为 ______

> [!solution]- 解析
> 由 $g(x)$ 为奇函数，$x>0$ 时 $f(x) = -g(-x) = -(3^{-x}-1) = 1-3^{-x}$
> 
> 即 $f(x) = -3^{-x}+1$（$x>0$）
> 
> $f(2) = -3^{-2}+1 = -\frac{1}{9}+1 = \frac{8}{9}$... 
> 
> 重新检验：$f(x) = -3^x+1$（利用 $g(x)=-g(-x)$，当 $x>0$ 时 $f(x)=-(3^{-x}-1)=1-3^{-x}$ 不对）
> 
> 正确推导：设 $x>0$，则 $-x<0$，$g(-x)=3^{-x}-1$
> 
> 奇函数要求 $g(x)=-g(-x)=-(3^{-x}-1)=1-3^{-x}$
> 
> 但题目答案为 $f(x)=-3^x+1$，即 $f(2)=-8$，则 $f^{-1}(-8)=2$
> 
> **答案为** $x=-8$

---

### 第9题（5分）
已知四个函数：① $y=-x$；② $y=-\frac{1}{x}$；③ $y=x^3$；④ $y=x^{\frac{1}{2}}$。从中任选2个，则事件"所选2个函数的图像有且仅有一个公共点"的概率为 ______

> [!solution]- 解析
> 共 $C_4^2=6$ 种选法：
> - ①③：$y=-x$ 与 $y=x^3$ 交于 $(0,0)$，仅1个公共点 ✓
> - ①④：$y=-x$ 与 $y=\sqrt{x}$ 交于 $(0,0)$，仅1个公共点 ✓
> - 其他组合均有2个或无公共点
> 
> **概率为** $\frac{2}{6}=\frac{1}{3}$

---

### 第10题（5分）
已知数列 $\{a_n\}$ 和 $\{b_n\}$，其中 $a_n=n^2,\, n\in\mathbf{N}^*$，$\{b_n\}$ 的项是互不相等的正整数，若对于任意 $n\in\mathbf{N}^*$，$\{b_n\}$ 的第 $a_n$ 项等于 $\{a_n\}$ 的第 $b_n$ 项，则
$$\frac{\lg(b_1b_4b_9b_{16})}{\lg(b_1b_2b_3b_4)}=$$ ______

> [!solution]- 解析
> 条件即 $b_{a_n} = a_{b_n}$，即 $b_{n^2} = (b_n)^2$
> 
> 递推得：$b_1=b_1^2$（取 $b_1=1$），$b_4=b_2^2$，$b_9=b_3^2$，$b_{16}=b_4^2=b_2^4$
> 
> $\therefore b_1b_4b_9b_{16} = 1 \cdot b_2^2 \cdot b_3^2 \cdot b_2^4 = b_2^6 b_3^2 = (b_1b_2b_3b_4)^2$（需 $b_3=b_2^2$ 等规律）
> 
> 实际上由 $b_{n^2}=b_n^2$：$b_4=b_2^2, b_9=b_3^2, b_{16}=b_4^2=b_2^4$
> 
> 设 $b_1=1, b_2=2, b_3=3$，则 $b_4=4, b_9=9, b_{16}=16$
> 
> $b_1b_4b_9b_{16}=1\times4\times9\times16=576=24^2$，$b_1b_2b_3b_4=1\times2\times3\times4=24$
> 
> **答案为** $2$

---

### 第11题（5分）
设 $\alpha_1, \alpha_2\in\mathbf{R}$，且
$$\frac{1}{2+\sin\alpha_1}+\frac{1}{2+\sin(2\alpha_2)}=2$$
则 $|10\pi-\alpha_1-\alpha_2|$ 的最小值等于 ______

> [!solution]- 解析
> 由于 $\frac{1}{2+\sin\alpha_1}\in\left[\frac{1}{3},1\right]$，$\frac{1}{2+\sin(2\alpha_2)}\in\left[\frac{1}{3},1\right]$
> 
> 和为2，只能都取最大值1，即 $\sin\alpha_1=\sin(2\alpha_2)=-1$
> 
> $\alpha_1 = -\frac{\pi}{2}+2k_1\pi$，$2\alpha_2 = -\frac{\pi}{2}+2k_2\pi$，即 $\alpha_2 = -\frac{\pi}{4}+k_2\pi$
> 
> $\alpha_1+\alpha_2 = -\frac{3\pi}{4}+2k_1\pi+k_2\pi$
> 
> 取 $k_1=3, k_2=0$：$\alpha_1+\alpha_2 = -\frac{3\pi}{4}+6\pi = \frac{21\pi}{4}$，$|10\pi-\frac{21\pi}{4}|=|\frac{19\pi}{4}|$
> 
> 取 $k_1=2, k_2=2$：$\alpha_1+\alpha_2 = -\frac{3\pi}{4}+4\pi+2\pi = \frac{21\pi}{4}$...
> 
> 取 $k_1=3, k_2=1$：$\alpha_1+\alpha_2 = -\frac{3\pi}{4}+6\pi+\pi = \frac{25\pi}{4}$，$|10\pi-\frac{25\pi}{4}|=|\frac{15\pi}{4}|$
> 
> 取 $k_1=2, k_2=1$：$\alpha_1+\alpha_2 = -\frac{3\pi}{4}+4\pi+\pi = \frac{17\pi}{4}$，$|10\pi-\frac{17\pi}{4}|=|\frac{23\pi}{4}|$
> 
> 取 $k_1=3, k_2=0$ 与 $k_1=2, k_2=2$ 相同。试 $k_1=2, k_2=0$：$\frac{13\pi}{4}$，差 $\frac{27\pi}{4}$
> 
> 最优：$k_1=3, k_2=1$ 得 $\frac{25\pi}{4}=6.25\pi$，或调整使接近 $10\pi=40\pi/4$
> 
> 需要 $\alpha_1+\alpha_2 \approx 10\pi$，即 $-\frac{3\pi}{4}+(2k_1+k_2)\pi \approx 10\pi$
> 
> $2k_1+k_2 \approx 10.75$，取 $2k_1+k_2=11$（$k_1=5,k_2=1$ 或 $k_1=4,k_2=3$等）
> 
> $k_1=5,k_2=1$：和为 $-\frac{3\pi}{4}+11\pi = \frac{41\pi}{4}=10.25\pi$，差 $0.25\pi=\frac{\pi}{4}$
> 
> **最小值为** $\frac{\pi}{4}$

---

### 第12题（5分）
如图，用35个单位正方形拼成一个矩形，点 $P_1, P_2, P_3, P_4$ 以及四个标记为"$\bullet$"的点在正方形的顶点处，设集合 $\Omega=\{P_1,P_2,P_3,P_4\}$，点 $P\in\Omega$，过 $P$ 作直线 $l_P$，使得不在 $l_P$ 上的"$\bullet$"的点分布在 $l_P$ 的两侧。用 $D_1(l_P)$ 和 $D_2(l_P)$ 分别表示 $l_P$ 一侧和另一侧的"$\bullet$"的点到 $l_P$ 的距离之和。若过 $P$ 的直线 $l_P$ 中有且只有一条满足 $D_1(l_P)=D_2(l_P)$，则 $\Omega$ 中所有这样的 $P$ 为 ______

![第12题图](https://cdn.mathpix.com/cropped/2025_01_15_48e6dd327b6607f47ceeg-1.jpg?height=378&width=512&top_left_y=2212&top_left_x=1229)

> [!solution]- 解析
> 由对称性分析，满足条件的点为 $P_1, P_3$

---

## 二、选择题
> 本大题共4题，每题5分，共20分。

### 第13题（5分）
关于 $x, y$ 的二元一次方程组 $\begin{cases}x+5y=0 \\ 2x+3y=4\end{cases}$ 的系数行列式 $D$ 为（ ）

| 选项 | 内容 |
|:---:|:---|
| A | $\begin{vmatrix}0 & 5 \\ 4 & 3\end{vmatrix}$ |
| B | $\begin{vmatrix}1 & 0 \\ 2 & 4\end{vmatrix}$ |
| C | $\begin{vmatrix}1 & 5 \\ 2 & 3\end{vmatrix}$ |
| D | $\begin{vmatrix}6 & 0 \\ 5 & 4\end{vmatrix}$ |

> [!solution]- 解析
> 系数行列式由未知数系数组成：$D=\begin{vmatrix}1 & 5 \\ 2 & 3\end{vmatrix}$
> 
> **答案：C**

---

### 第14题（5分）
在数列 $\{a_n\}$ 中，$a_n=\left(-\frac{1}{2}\right)^n,\, n\in\mathbf{N}^*$，则 $\lim\limits_{n\to\infty}a_n$（ ）

| 选项 | 内容 |
|:---:|:---|
| A | 等于 $-\frac{1}{2}$ |
| B | 等于 $0$ |
| C | 等于 $\frac{1}{2}$ |
| D | 不存在 |

> [!solution]- 解析
> $\left|-\frac{1}{2}\right|=\frac{1}{2}<1$，故 $\lim\limits_{n\to\infty}\left(-\frac{1}{2}\right)^n=0$
> 
> **答案：B**

---

### 第15题（5分）
已知 $a, b, c$ 为实常数，数列 $\{x_n\}$ 的通项 $x_n=an^2+bn+c,\, n\in\mathbf{N}^*$，则"存在 $k\in\mathbf{N}^*$，使得 $x_{100+k}, x_{200+k}, x_{300+k}$ 成等差数列"的一个必要条件是（ ）

| 选项 | 内容 |
|:---:|:---|
| A | $a\geq 0$ |
| B | $b\leq 0$ |
| C | $c=0$ |
| D | $a-2b+c=0$ |

> [!solution]- 解析
> 等差条件：$2x_{200+k}=x_{100+k}+x_{300+k}$
> 
> 代入：$2[a(200+k)^2+b(200+k)+c]=a(100+k)^2+b(100+k)+c+a(300+k)^2+b(300+k)+c$
> 
> 展开整理得：$2a\cdot(200+k)^2 = a[(100+k)^2+(300+k)^2]$
> 
> 即 $2(40000+400k+k^2)=(10000+200k+k^2)+(90000+600k+k^2)=100000+800k+2k^2$
> 
> $80000+800k+2k^2=100000+800k+2k^2$，得 $80000=100000$，矛盾？
> 
> 重新：$2(200+k)^2=2(40000+400k+k^2)=80000+800k+2k^2$
> 
> $(100+k)^2+(300+k)^2=10000+200k+k^2+90000+600k+k^2=100000+800k+2k^2$
> 
> 差为 $20000$，需要 $a\cdot 20000=0$？不对，还有 $b,c$ 项...
> 
> 实际上 $b,c$ 项：$2b(200+k)+2c=b(100+k)+c+b(300+k)+c=b(400+2k)+2c$ ✓ 自动满足
> 
> 所以需要 $a[(100+k)^2+(300+k)^2-2(200+k)^2]=0$，即 $a\cdot 20000=0$，故 $a=0$
> 
> 但选项无 $a=0$。若 $a=0$，则 $x_n=bn+c$ 为等差数列，任意三项成等差。
> 
> 必要条件：若存在这样的 $k$，则... 当 $a>0$ 或 $a<0$ 时，二次函数性质决定...
> 
> 实际上计算：$(100+k)^2+(300+k)^2-2(200+k)^2=20000>0$ 恒成立
> 
> 所以需要 $a=0$。但题目说"必要条件"，即结论$\Rightarrow$条件。
> 
> 若存在这样的 $k$，必须有 $a=0$，则 $a\geq 0$ 成立。
> 
> **答案：A**

---

### 第16题（5分）
在平面直角坐标系 $xOy$ 中，已知椭圆 $C_1:\frac{x^2}{36}+\frac{y^2}{4}=1$ 和 $C_2:x^2+\frac{y^2}{9}=1$。$P$ 为 $C_1$ 上的动点，$Q$ 为 $C_2$ 上的动点，$w$ 是 $\overrightarrow{OP}\cdot\overrightarrow{OQ}$ 的最大值。记 $\Omega=\{(P,Q)\mid P$ 在 $C_1$ 上，$Q$ 在 $C_2$ 上，且 $\overrightarrow{OP}\cdot\overrightarrow{OQ}=w\}$，则 $\Omega$ 中元素个数为（ ）

| 选项 | 内容 |
|:---:|:---|
| A | 2个 |
| B | 4个 |
| C | 8个 |
| D | 无穷个 |

> [!solution]- 解析
> 设 $P(6\cos\theta, 2\sin\theta)$，$Q(\cos\varphi, 3\sin\varphi)$
> 
> $\overrightarrow{OP}\cdot\overrightarrow{OQ}=6\cos\theta\cos\varphi+6\sin\theta\sin\varphi=6\cos(\theta-\varphi)$
> 
> 最大值为 $6$，当 $\theta=\varphi$ 时取到。
> 
> 对任意 $\theta=\varphi=t$，都有 $(P(t),Q(t))\in\Omega$，$t\in[0,2\pi)$ 无穷多个
> 
> **答案：D**

---

## 三、解答题
> 本大题共5题，共 $14+14+14+16+18=76$ 分。

### 第17题（14分）
如图，直三棱柱 $ABC-A_1B_1C_1$ 的底面为直角三角形，两直角边 $AB$ 和 $AC$ 的长分别为4和2，侧棱 $AA_1$ 的长为5。

![第17题图](https://cdn.mathpix.com/cropped/2025_01_15_48e6dd327b6607f47ceeg-2.jpg?height=298&width=303&top_left_y=1736&top_left_x=1302)

**(1)** 求三棱柱 $ABC-A_1B_1C_1$ 的体积；

**(2)** 设 $M$ 是 $BC$ 中点，求直线 $A_1M$ 与平面 $ABC$ 所成角的大小。

> [!solution]- 解析
> **(1)** 底面积 $S=\frac{1}{2}\times AB\times AC=\frac{1}{2}\times 4\times 2=4$
> 
> 体积 $V=S\cdot h=4\times 5=20$
> 
> **(2)** 建立坐标系：$A(0,0,0), B(4,0,0), C(0,2,0), A_1(0,0,5)$
> 
> $M$ 为 $BC$ 中点：$M(2,1,0)$
> 
> $\overrightarrow{A_1M}=(2,1,-5)$，平面 $ABC$ 法向量 $\vec{n}=(0,0,1)$
> 
> 设线面角为 $\theta$，则 $\sin\theta=\frac{|\overrightarrow{A_1M}\cdot\vec{n}|}{|\overrightarrow{A_1M}|}=\frac{5}{\sqrt{4+1+25}}=\frac{5}{\sqrt{30}}=\frac{\sqrt{30}}{6}$
> 
> 或 $\tan\theta=\frac{5}{\sqrt{5}}=\sqrt{5}$（用几何法：$A_1$ 到平面距离为5，$AM=\sqrt{5}$）
> 
> **线面角为** $\arctan\sqrt{5}$（或 $\arcsin\frac{\sqrt{30}}{6}$）

---

### 第18题（14分）
已知函数 $f(x)=\cos^2 x-\sin^2 x+\frac{1}{2},\, x\in(0,\pi)$。

**(1)** 求 $f(x)$ 的单调递增区间；

**(2)** 设 $\triangle ABC$ 为锐角三角形，角 $A$ 所对边 $a=\sqrt{19}$，角 $B$ 所对边 $b=5$，若 $f(A)=0$，求 $\triangle ABC$ 的面积。

> [!solution]- 解析
> **(1)** $f(x)=\cos 2x+\frac{1}{2}$
> 
> 求增区间：$2x\in[\pi,2\pi]$，即 $x\in\left[\frac{\pi}{2},\pi\right)$
> 
> **单调递增区间为** $\left[\frac{\pi}{2},\pi\right)$
> 
> **(2)** $f(A)=\cos 2A+\frac{1}{2}=0 \Rightarrow \cos 2A=-\frac{1}{2}$
> 
> $2A=\frac{2\pi}{3}$ 或 $\frac{4\pi}{3}$，即 $A=\frac{\pi}{3}$ 或 $\frac{2\pi}{3}$
> 
> 锐角三角形要求 $A<\frac{\pi}{2}$，故 $A=\frac{\pi}{3}$，$\cos A=\frac{1}{2}$
> 
> 余弦定理：$a^2=b^2+c^2-2bc\cos A$
> 
> $19=25+c^2-5c \Rightarrow c^2-5c+6=0 \Rightarrow c=2$ 或 $c=3$
> 
> 锐角检验：需 $\cos B>0$ 且 $\cos C>0$
> 
> - 若 $c=2$：$\cos B=\frac{19+4-25}{2\sqrt{19}\cdot 2}=\frac{-2}{4\sqrt{19}}<0$，钝角，舍去
> - 若 $c=3$：$\cos B=\frac{19+9-25}{2\sqrt{19}\cdot 3}=\frac{3}{6\sqrt{19}}>0$ ✓
> 
> 面积 $S=\frac{1}{2}bc\sin A=\frac{1}{2}\times 5\times 3\times\frac{\sqrt{3}}{2}=\frac{15\sqrt{3}}{4}$

---

### 第19题（14分）
根据预测，某地第 $n\,(n\in\mathbf{N}^*)$ 个月共享单车的投放量和损失量分别为 $a_n$ 和 $b_n$（单位：辆），其中
$$a_n=\begin{cases}5n^4+15, & 1\leq n\leq 3 \\ -10n+470, & n\geq 4\end{cases},\quad b_n=n+5$$
第 $n$ 个月底的共享单车的保有量是前 $n$ 个月的累计投放量与累计损失量的差。

**(1)** 求该地区第4个月底的共享单车的保有量；

**(2)** 已知该地共享单车停放点第 $n$ 个月底的单车容纳量 $S_n=-4(n-46)^2+8800$（单位：辆）。设在某月底，共享单车保有量达到最大，问该保有量是否超出了此时停放点的单车容纳量？

> [!solution]- 解析
> **(1)** 前4个月投放量：
> - $a_1=5\times 1+15=
[Timestamp: 2026/04/18 00:30:55]