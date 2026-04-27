# LaTeX 命令速查表

本讲义中可用的 LaTeX 命令和环境汇总。

---

## 环境（盒子）

### 定理类（粉色盒子）

| 环境 | 用途 | 示例 |
|------|------|------|
| `theorem` | 定理 | `\begin{theorem}[极限唯一性]` |
| `lemma` | 引理 | `\begin{lemma}[Fermat引理]` |
| `proposition` | 命题 | `\begin{proposition}[单调性判定]` |
| `corollary` | 推论 | `\begin{corollary}` |
| `property` | 性质 | `\begin{property}[导数性质]` |

```latex
\begin{theorem}[极限唯一性]
若 $\lim_{x \to x_0} f(x)$ 存在，则该极限值唯一。
\end{theorem}

\begin{proof}
假设存在两个不同的极限值...
\end{proof}
```

### 定义类（橙色盒子）

| 环境 | 用途 | 示例 |
|------|------|------|
| `definition` | 定义 | `\begin{definition}[导数]` |
| `axiom` | 公理 | `\begin{axiom}[牛顿-莱布尼兹公式]` |

```latex
\begin{definition}[函数]
设 $A, B$ 是两个非空数集...称 $f: A \to B$ 是一个函数。
\end{definition}
```

### 例题类（蓝色盒子）

| 环境 | 用途 | 备注 |
|------|------|------|
| `example` | 普通例题 | 单页显示 |
| `longexample` | 跨页长例题 | 可自动分页 |
| `exercise` | 练习题 | 同 example 样式 |
| `realexam` | 真题 | 标注考试年份 |
| `longrealexam` | 跨页真题 | 可自动分页 |

```latex
\begin{example}[定义域优先]
求函数 $f(x)=\frac{\sqrt{2x+1}}{x-3}$ 的定义域。
\end{example}

\textbf{解.} 由 $2x+1\ge 0$ 得...

\begin{realexam}[2019 数学一]
设 $f(x)$ 在 $[0, +\infty)$ 上有连续的导数...
\end{realexam}
```

### 注与证明

| 环境 | 用途 | 示例 |
|------|------|------|
| `note` | 注释/说明 | `\begin{note}` |
| `proof` | 证明 | `\begin{proof}`（自动添加证毕符号） |

```latex
\begin{note}
定义域是研究函数的一切前提。
\end{note}

\begin{proof}
假设 $\lim_{x \to x_0} f(x) = A$ 且 $\lim_{x \to x_0} f(x) = B$...
\end{proof}
```

---

## 辅助命令

### 方法提示与易错提醒

```latex
\method{研究单调性时，定义域必须先分区间处理。}
\pitfall{"在定义域上单调"与"在某个区间上单调"不是一回事。}
```

### 填空与选择

```latex
\fillin[3cm]          % 填空横线，默认 3cm 宽
\fillin               % 使用默认宽度
\selectbracket        % 选择题括号 (    )
```

使用示例：

```latex
\begin{exercise}
该校的女生共有 \fillin 人。
\end{exercise}

\begin{exercise}
下列关于可微性的叙述，正确的是 \selectbracket
\begin{enumerate}
    \item[A.] 偏导数存在 $\Longrightarrow$ 可微
    \item[B.] 可微 $\Longrightarrow$ 偏导数连续
    \item[C.] 可微 $\Longrightarrow$ 连续
\end{enumerate}
\end{exercise}
```

### 常用数学符号

```latex
\R      % 实数集 $\mathbb{R}$
\Z      % 整数集 $\mathbb{Z}$
\N      % 自然数集 $\mathbb{N}$
\Q      % 有理数集 $\mathbb{Q}$
\C      % 复数集 $\mathbb{C}$
\sep    % 分隔符 ·
```

### 优化后的数学符号

```latex
\ge     % ≥（自动替换 \geq）
\le     % ≤（自动替换 \leq）
\lim    % 自动 displaystyle
\sum    % 自动 displaystyle
\int    % 自动 displaystyle
\iint   % 自动 displaystyle
\iiint  % 自动 displaystyle
\oint   % 自动 displaystyle
\dfrac  % 自动优化间距
```

---

## 标签与引用

### 标签命名规范

```latex
% 定义: def:章节缩写-概念名
\begin{definition}[函数] \label{def:func-def}
...
\end{definition}

% 定理: thm:章节缩写-定理名
\begin{theorem}[极限唯一性] \label{thm:limit-unique}
...
\end{theorem}

% 例题: ex:章节缩写-序号
\begin{example} \label{ex:func-01}
...
\end{example}

% 公式: eq:章节缩写-描述
\begin{equation} \label{eq:derivative-def}
...
\end{equation}
```

### 引用方式

```latex
\ref{thm:limit-unique}       % 引用定理编号，如 "1.3"
\eqref{eq:derivative-def}    % 引用公式编号，如 "(2.5)"
```

---

## TikZ 绘图

### 基本设置

```latex
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
```

### 函数图像

```latex
\begin{center}
\begin{tikzpicture}
\begin{axis}[
    width=10cm, height=6cm,
    axis lines=middle,
    xlabel={$x$}, ylabel={$y$},
    samples=100, domain=-2:4,
    ymin=-1.5, ymax=4,
    xtick={-1,0,...,3}, ytick={-1,0,...,3},
    grid=major, grid style={dashed, gray!30},
    legend pos=north west
]
    \addplot[thick, color=LogicColor]{x^2*exp(-x)};
    \addlegendentry{$y = x^2 e^{-x}$}
\end{axis}
\end{tikzpicture}
\captionof{figure}{函数图像}
\end{center}
```

### 向量图（三维）

```latex
\begin{tikzpicture}[tdplot_main_coords, scale=1.2]
    % 坐标轴
    \draw[-{Stealth}, thick] (0,0,0) -- (3.5,0,0) node[anchor=north east]{$x$};
    \draw[-{Stealth}, thick] (0,0,0) -- (0,3.5,0) node[anchor=north west]{$y$};
    \draw[-{Stealth}, thick] (0,0,0) -- (0,0,3.5) node[anchor=south]{$z$};
    % 向量
    \draw[-{Stealth}, very thick, color=LogicColor] (0,0,0) -- (2,1,2) 
        node[midway, above left]{\boldsymbol{a}};
\end{tikzpicture}
```

---

## 章节结构

```latex
\chapter{章节名称}

\section{知识框架}
% 本章知识结构概述

\section{核心概念}
% 定义、定理、性质

\section{典型例题}
% 分类例题详解

\section{方法总结}
% 解题方法、技巧归纳

\section{易错点分析}
% 常见错误、注意事项

\section{本章练习}
% 练习题

\section*{本章小结}
\addcontentsline{toc}{section}{本章小结}
% 要点回顾
```

---

## 常用列表

### 有序列表

```latex
\begin{enumerate}
    \item 定义域是研究函数的一切前提；
    \item 单调性常与最值、不等式、图像结合考查；
    \item 奇偶性先看定义域，再看代数关系。
\end{enumerate}
```

### 带字母选项的有序列表

```latex
\begin{enumerate}
    \item[A.] 选项 A
    \item[B.] 选项 B
    \item[C.] 选项 C
\end{enumerate}
```

### 无序列表

```latex
\begin{itemize}
    \item 第一点
    \item 第二点
    \item 第三点
\end{itemize}
```

---

## 表格

```latex
\begin{center}
\begin{tabular}{|c|c|c|c|}
\hline
列1 & 列2 & 列3 & 列4 \\
\hline
数据1 & 数据2 & 数据3 & 数据4 \\
\hline
\end{tabular}
\end{center}
```

或使用 `booktabs` 宏包的无框线表格：

```latex
\begin{center}
\begin{tabular}{cccc}
\toprule
列1 & 列2 & 列3 & 列4 \\
\midrule
数据1 & 数据2 & 数据3 & 数据4 \\
\bottomrule
\end{tabular}
\end{center}
```

---

## 更多参考

- [CTeX 文档](https://ctex.org/)
- [tcolorbox 手册](https://mirror.ctan.org/macros/latex/contrib/tcolorbox/tcolorbox.pdf)
- [pgfplots 手册](https://mirror.ctan.org/graphics/pgf/contrib/pgfplots/doc/pgfplots.pdf)
