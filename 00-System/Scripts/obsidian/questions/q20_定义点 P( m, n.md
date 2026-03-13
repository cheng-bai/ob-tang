---
title: "第 20 题"
exam: "2024-2025 年七宝中学高一下期中"
subject: "数学"
grade: "高一"
type: "解答题"
difficulty: "较难"
tags: ["解答题", "平面向量", "向量线性运算", "向量数量积", "解三角形", "三角形性质", "不等式与最值", "参数讨论", "较难"]
created: 2026-02-18
---
# q20_定义点 P( m, n

## 题目

定义点 $P\left( {m, n}\right)$ ,若函数满足 $f\left( x\right)  = m\sin x + n\cos x$ ,则称函数 $y = f\left( x\right)$ 为点 $P$ 的 “ $m - n$ 伴生函数”，点 $P\left( {m, n}\right)$ 为函数 $y = f\left( x\right)$ 的 “源点”.
(1)已知点 $P\left( {\sqrt{3},1}\right)$ 为函数 $g\left( x\right)  = \sin \left( {x + \varphi }\right)  - \cos \left( {\frac{4\pi }{3} - x}\right) \left( {\left| \varphi \right|  < \frac{\pi }{2}}\right)$ 的 “源点”，求实数 $\varphi$ 的值.
(2)已知点 $A\left( {m, n}\right)$ 满足 $m = 3, n \in  (0,\sqrt{3}\rbrack$ . 若点 $A\left( {m, n}\right)$ 的 “ $m - n$ 伴生函数” $y = h\left( x\right)$ 在 $x = a$ 时取得最大值,当点 $A$ 运动时,求 $\tan {2a}$ 的取值范围;
(3)已知点 $A$ 的 “ 0-1 伴生函数” $y = F\left( x\right)$ 满足 $F\left( t\right)  = \frac{\sqrt{2}}{2}$ . 若 $\bigtriangleup {ABC}$ 中， ${AB} = \sqrt{2}$ ， $\cos C = F\left( t\right)$ ,点 $O$ 为该三角形的外心,求 $\overrightarrow{OC} \cdot  \overrightarrow{AB} + \overrightarrow{CA} \cdot  \overrightarrow{CB}$ 的最大值.

## 解析

(1) 由题意得 $\sqrt{3}\sin x + \cos x = \sin \left( {x + \varphi }\right)  - \cos \left( {\frac{4\pi }{3} - x}\right)$ ,
令 $x = 0$ ,得 $1 = \sin \varphi  + \frac{1}{2}$ ,所以 $\sin \varphi  = \frac{1}{2}$ ,
因为 $\left| \varphi \right|  < \frac{\pi }{2}$ ,所以 $\varphi  = \frac{\pi }{6}$ ;
(2) $h\left( x\right)  = 3\sin x + n\cos x = \sqrt{9 + {n}^{2}}\sin \left( {x + \varphi }\right)$ ，其中 $\tan \varphi  = \frac{n}{3}$ ，
当 $x + \varphi  = \frac{\pi }{2} + {2k\pi }\left( {k \in  Z}\right)$ ,即 $a =  - \varphi  + \frac{\pi }{2} + {2k\pi }\left( {k \in  Z}\right)$ 时, $h\left( x\right)$ 取最大值,
故 $\tan a = \tan \left( {-\varphi  + \frac{\pi }{2} + {2k\pi }}\right)  = \frac{1}{\tan \varphi } = \frac{3}{n}$ ,
则 $\tan {2a} = \frac{2\tan a}{1 - {\tan }^{2}a} = \frac{2}{\frac{n}{3} - \frac{3}{n}}$ ,
令 $\frac{n}{3} = t \in  \left( {0,\frac{\sqrt{3}}{3}}\right\rbrack$ ,所以 $\tan {2a} = \frac{2}{t - \frac{1}{t}}$ ,
因为 $y = t - \frac{1}{t}$ 严格增,所以 $t - \frac{1}{t} \in  \left( {-\infty , - \frac{2}{\sqrt{3}}}\right)$ ,
所以 $\tan {2a}$ 的取值范围为 $\left( {-\sqrt{3},0}\right)$ ;
(3) 由题意得, $F\left( x\right)  = \cos x$ ,则 $\cos t = \frac{\sqrt{2}}{2}$ ,
在三角形 ${ABC}$ 中, ${AB} = \sqrt{2},\cos C = F\left( t\right)  = \cos t = \frac{\sqrt{2}}{2}$ ,因此 $C = \frac{\pi }{4}$ ,
设三角形 ${ABC}$ 外接圆半径为 $R$ ,由正弦定理得 $\frac{AB}{\sin C} = {2R} = 2$ ,故 $R = 1$ ,
所以 $\left| \overrightarrow{OA}\right|  = \left| \overrightarrow{OB}\right|  = \left| \overrightarrow{OC}\right|  = 1$ ,
$\overrightarrow{OC} \cdot  \overrightarrow{AB} + \overrightarrow{CA} \cdot  \overrightarrow{CB} = \overrightarrow{OC} \cdot  \left( {\overrightarrow{OB} - \overrightarrow{OA}}\right)  + \left( {\overrightarrow{OA} - \overrightarrow{OC}}\right)  \cdot  \left( {\overrightarrow{OB} - \overrightarrow{OC}}\right)$
$=  - 2\overrightarrow{OC} \cdot  \overrightarrow{OA} + \overrightarrow{OA} \cdot  \overrightarrow{OB} + {\overrightarrow{OC}}^{2} =  - 2\cos \angle {AOC} + \cos \angle {AOB} + 1$ ,
$C = \frac{\pi }{4},\angle {AOB} = {2C} = \frac{\pi }{2},\cos \angle {AOB} = \cos \frac{\pi }{2} = 0,$
代入得 $\overrightarrow{OC} \cdot  \overrightarrow{AB} + \overrightarrow{CA} \cdot  \overrightarrow{CB} = 1 - 2\cos \angle {AOC}$ ,
所以当 $\angle {AOC} = \pi$ 时, $\overrightarrow{OC} \cdot  \overrightarrow{AB} + \overrightarrow{CA} \cdot  \overrightarrow{CB}$ 取得最大值 3 .

---

> 题号: 20 | 题型: 解答题 | 难度: 较难
