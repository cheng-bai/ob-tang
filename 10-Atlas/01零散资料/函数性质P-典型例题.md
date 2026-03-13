# 函数性质P-典型例题

## 题目

设函数 $y = f(x)$ 是定义在 $\mathrm{R}$ 上的函数，定义性质 $\mathrm{P}$：若对任意 $x_1, x_2 \in \mathrm{R}$，当 $|x_1| < |x_2|$ 时，$f(x_1) < f(x_2)$，则称函数 $y = f(x)$ 具有"性质 P"。

(1) 判断函数 $f(x) = e^x$ 是否具有"性质 P"；

(2) 若分段函数 
$$f(x) = \begin{cases} ax, & x \leq 0 \\ x + b, & x > 0 \end{cases}$$
具有"性质 P"，求所有满足条件的实数 $a$ 和 $b$；

(3) 已知函数 $y = f(x)$ 的值域为 $[0, 1)$，且在 $[0, +\infty)$ 上是严格增函数，证明：函数 $y = f(x)$ 具有"性质 P"的充要条件是函数 $y = f(x)$ 是偶函数。

---

## 性质 P 的本质

性质 P 的定义：
$$|x_1| < |x_2| \Rightarrow f(x_1) < f(x_2)$$

这意味着：**函数值只与 $|x|$ 有关，且 $|x|$ 越大，$f(x)$ 越大**。

换句话说，$f$ 是 $|x|$ 的严格递增函数。

---

## (1) 判断 $f(x) = e^x$ 是否具有性质 P

### 分析

$e^x$ 在 $\mathrm{R}$ 上单调递增。

对于任意 $|x_1| < |x_2|$：
- 若 $x_1, x_2 \geq 0$，则 $x_1 < x_2 \Rightarrow e^{x_1} < e^{x_2}$ ✓
- 若 $x_1, x_2 \leq 0$，则 $|x_1| < |x_2| \Rightarrow -x_1 > -x_2 \Rightarrow x_1 > x_2$，但 $e^{x_1} < e^{x_2}$（因为指数函数递增）✓
- 若 $x_1 < 0 < x_2$，则 $|x_1| < |x_2|$ 等价于 $-x_1 < x_2$，此时 $e^{x_1} < e^{x_2}$ 同样成立 ✓

### 结论

**$f(x) = e^x$ 具有性质 P**。

---

## (2) 求 $a, b$ 的取值范围

### 分析

函数：
$$f(x) = \begin{cases} ax, & x \leq 0 \\ x + b, & x > 0 \end{cases}$$

#### 条件一：各自区间内严格递增

- 当 $x \leq 0$ 时，$f(x) = ax$ 严格递增 ⇒ **$a > 0$**
- 当 $x > 0$ 时，$f(x) = x + b$ 严格递增 ⇒ 显然成立

#### 条件二：跨区间比较

取 $x_1 < 0 < x_2$，且满足 $|x_1| < |x_2|$。

令 $x_1 = -t$（$t > 0$），$x_2 = s$（$s > 0$），且 $t < s$：

- $f(x_1) = f(-t) = a \cdot (-t) = -at$
- $f(x_2) = f(s) = s + b$

性质 P 要求：$-at < s + b$，即 $b > -at - s$

由于 $t < s$，令 $s = t + \Delta$（$\Delta > 0$），则：
$$b > -a(t + t + \Delta) = -2at - a\Delta$$

取 $t \to 0^+$，$\Delta \to 0^+$，得：
$$b \geq -2a \cdot 0 = 0$$

更严格地，考虑边界情况 $x_1 \to 0^-$，$x_2 \to 0^+$：

令 $x_1 = -\varepsilon$，$x_2 = \varepsilon$（$\varepsilon > 0$ 很小）：
$$|x_1| = \varepsilon = |x_2|$$

此时 $|x_1| = |x_2|$，不满足 $|x_1| < |x_2|$，但我们可以考虑极限情况。

取 $x_1 = -\varepsilon$，$x_2 = 2\varepsilon$（$|x_1| < |x_2|$）：
$$f(-\varepsilon) = -a\varepsilon, \quad f(2\varepsilon) = 2\varepsilon + b$$
$$-a\varepsilon < 2\varepsilon + b \Rightarrow b > -a\varepsilon - 2\varepsilon$$

令 $\varepsilon \to 0^+$，得 $b \geq 0$。

再考虑更一般的情况。设 $x_1 = -x$（$x > 0$），$x_2 = y$（$y > 0$），满足 $x < y$：

$$-ax < y + b \Rightarrow b > -ax - y$$

由于 $x < y$，设 $y = kx$（$k > 1$）：
$$b > -ax - kx = -(a + k)x$$

由于 $0 < \frac{x}{y} < 1$，最大值出现在 $\frac{x}{y} \to 1^-$：

$$b \geq -2y$$

令 $y \to 0^+$，得 $b \geq 0$。

### 答案

$$\boxed{a > 0, \quad b \geq 0}$$

---

## (3) 证明：性质 P ⇔ 偶函数

### 已知条件

- $f(x)$ 的值域为 $[0, 1)$
- $f(x)$ 在 $[0, +\infty)$ 上严格递增

### 证明

#### 必要性（性质 P ⇒ 偶函数）

假设 $f$ 具有性质 P。

对任意 $x \in \mathrm{R}$：
- 取 $x_1 = x$，$x_2 = -x$
- 则 $|x| = |-x|$，不满足 $|x_1| < |x_2|$

但我们可以考虑 $x_1 = x$，$x_2 = -x - \varepsilon$（$\varepsilon > 0$ 足够小）：

当 $|x| > 0$ 时，有 $|x| < |x + \varepsilon|$ 和 $|x| < |x - \varepsilon|$。

取 $x_1 = x - \varepsilon$，$x_2 = -x$：
$$|x - \varepsilon| < |-x| = |x| \Rightarrow f(x - \varepsilon) < f(-x)$$

令 $\varepsilon \to 0^+$，由连续性（严格递增函数必连续）得：
$$f(x) \leq f(-x)$$

同理，取 $x_1 = x$，$x_2 = -x + \varepsilon$ 可得：
$$f(x) \geq f(-x)$$

故 $f(x) = f(-x)$，即 $f$ 是偶函数。

#### 充分性（偶函数 + 严格递增 ⇒ 性质 P）

假设 $f$ 是偶函数，且在 $[0, +\infty)$ 上严格递增。

对任意 $x_1, x_2 \in \mathrm{R}$，若 $|x_1| < |x_2|$：

由于 $f$ 在 $[0, +\infty)$ 递增，且 $|x_1|, |x_2| \in [0, +\infty)$：
$$|x_1| < |x_2| \Rightarrow f(|x_1|) < f(|x_2|)$$

利用偶函数性质：$f(x_1) = f(|x_1|)$，$f(x_2) = f(|x_2|)$，得：
$$f(x_1) < f(x_2)$$

故 $f$ 具有性质 P。

#### 结论

函数 $y = f(x)$ 具有"性质 P"的充要条件是 $y = f(x)$ 是偶函数。

---

## 总结

| 小问 | 答案 |
|------|------|
| (1) | 具有性质 P |
| (2) | $a > 0, b \geq 0$ |
| (3) | 证明见上文 |

---

## 关键知识点

1. **性质 P 的本质**：$f$ 是 $|x|$ 的严格递增函数
2. **单调性分析**：分段函数需同时满足区间内单调和跨区间单调
3. **偶函数判定**：$f(x) = f(-x)$
4. **充要证明**：需分别证明充分性和必要性
