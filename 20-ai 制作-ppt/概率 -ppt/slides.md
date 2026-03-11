---
theme: default
title: 第十章 概率
highlighter: shiki
lineNumbers: false
colorSchema: light
fonts:
  sans: 'system-ui'
  mono: 'Fira Code'
layout: cover
background: 'https://images.unsplash.com/photo-1606167668584-78701c57f13d?q=80&w=2070&auto=format&fit=crop'
---

# 第十章 概率

## 高中数学必修课程

<div class="pt-12">
  <span class="px-2 py-1 rounded border bg-opacity-50 bg-white text-gray-800">
    统计与概率系列
  </span>
</div>

---
layout: center
---

# 目录

<div class="grid grid-cols-2 gap-6 mt-8 text-left">
  <div class="bg-blue-50 p-4 rounded-lg">
    <h3 class="font-bold text-lg mb-2">📌 概率基础</h3>
    <ul class="text-sm space-y-1 text-gray-700">
      <li>• 随机事件与概率</li>
      <li>• 概率的性质</li>
      <li>• 古典概型</li>
    </ul>
  </div>
  <div class="bg-green-50 p-4 rounded-lg">
    <h3 class="font-bold text-lg mb-2">📐 概率模型</h3>
    <ul class="text-sm space-y-1 text-gray-700">
      <li>• 几何概型</li>
      <li>• 条件概率</li>
      <li>• 独立事件</li>
    </ul>
  </div>
  <div class="bg-purple-50 p-4 rounded-lg col-span-2">
    <h3 class="font-bold text-lg mb-2">🔢 重要公式</h3>
    <ul class="text-sm space-y-1 text-gray-700">
      <li>• 全概率公式</li>
      <li>• 贝叶斯公式</li>
      <li>• 排列组合应用</li>
    </ul>
  </div>
</div>

---
layout: cover
class: text-white
background: 'https://images.unsplash.com/photo-1518156677180-95a2883c924d?q=80&w=2069&auto=format&fit=crop'
---

# 一、概率的基础概念

---
layout: two-cols
---

# 随机现象

::left::

<div class="space-y-4">

## 什么是随机现象？

<v-clicks>

- 在一定条件下
- 可能出现不同结果
- 事先不能确定

</v-clicks>

## 例子

<v-clicks>

- 掷硬币：正面或反面
- 掷骰子：1,2,3,4,5,6 点
- 抽奖：中奖或不中奖

</v-clicks>

</div>

::right::

<div class="space-y-4">

## 相关概念

<v-clicks>

- **试验**：观察随机现象的过程
- **样本空间**：所有可能结果的集合
- **随机事件**：样本空间的子集

</v-clicks>

</div>

---
layout: center
---

# 样本空间与事件

<div class="bg-white bg-opacity-70 p-6 rounded-lg max-w-3xl mx-auto">

## 掷一枚骰子的样本空间

$$\Omega = \{1, 2, 3, 4, 5, 6\}$$

<v-clicks>

<div class="mt-4 grid grid-cols-3 gap-4">
  <div class="bg-blue-100 p-3 rounded">
    <p class="text-sm font-bold">事件 A：点数为偶数</p>
    <p class="text-xs mt-2">A = {2, 4, 6}</p>
  </div>
  <div class="bg-green-100 p-3 rounded">
    <p class="text-sm font-bold">事件 B：点数大于 4</p>
    <p class="text-xs mt-2">B = {5, 6}</p>
  </div>
  <div class="bg-purple-100 p-3 rounded">
    <p class="text-sm font-bold">事件 C：点数小于 3</p>
    <p class="text-xs mt-2">C = {1, 2}</p>
  </div>
</div>

</v-clicks>

</div>

---
layout: center
---

# 概率的定义

<div class="space-y-6 max-w-4xl mx-auto">

## 古典定义

<v-clicks>

<div class="bg-blue-50 p-6 rounded-lg">
  <p class="text-lg">
    如果样本空间有 <span class="font-bold text-blue-600">n</span> 个等可能的基本事件
  </p>
  <p class="text-lg mt-2">
    事件 A 包含其中 <span class="font-bold text-blue-600">m</span> 个
  </p>
  <p class="text-2xl mt-4 font-bold text-center">
    $$P(A) = \frac{m}{n}$$
  </p>
</div>

<div class="bg-green-50 p-4 rounded">
  <p class="text-sm">
    <strong>性质：</strong> 0 ≤ P(A) ≤ 1，必然事件概率为 1，不可能事件概率为 0
  </p>
</div>

</v-clicks>

</div>

---
layout: two-cols
---

# 概率的性质

::left::

<div class="space-y-4">

## 基本性质

<v-clicks>

1. **非负性**
   $$P(A) \geq 0$$

2. **规范性**
   $$P(\Omega) = 1$$

3. **可加性**
   互斥事件可加

</v-clicks>

</div>

::right::

<div class="space-y-4">

## 重要公式

<v-clicks>

- **对立事件**
  $$P(\bar{A}) = 1 - P(A)$$

- **加法公式**
  $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

</v-clicks>

</div>

---
layout: cover
class: text-white
background: 'https://images.unsplash.com/photo-1509248961158-e54f6934749c?q=80&w=2037&auto=format&fit=crop'
---

# 二、古典概型

---
layout: center
---

# 古典概型的特征

<div class="grid grid-cols-2 gap-8 mt-8">
  <div class="bg-yellow-100 p-6 rounded-lg">
    <h3 class="text-xl font-bold mb-4">🎯 特征 1</h3>
    <p class="text-lg">样本空间的元素个数是<strong class="text-yellow-600">有限的</strong></p>
  </div>
  <div class="bg-orange-100 p-6 rounded-lg">
    <h3 class="text-xl font-bold mb-4">🎲 特征 2</h3>
    <p class="text-lg">每个基本事件发生的可能性<strong class="text-orange-600">相等</strong></p>
  </div>
</div>

<div class="mt-8 bg-white bg-opacity-80 p-6 rounded-lg">
  <h3 class="text-lg font-bold mb-4">计算公式</h3>
  <p class="text-3xl text-center">
    $$P(A) = \frac{\text{事件 A 包含的基本事件数}}{\text{样本空间的基本事件总数}} = \frac{m}{n}$$
  </p>
</div>

---
layout: two-cols
---

# 古典概型例题

::left::

<div class="space-y-4">

## 例题 1：掷硬币

掷两枚均匀的硬币，求：

1. 两枚都是正面的概率
2. 至少有一枚正面的概率

<v-clicks>

<div class="mt-4 bg-blue-50 p-4 rounded text-sm">
  <p><strong>解：</strong></p>
  <p>Ω = {正正，正反，反正，反反}</p>
  <p>n = 4</p>
</div>

</v-clicks>

</div>

::right::

<div class="space-y-4">

## 解答

<v-clicks>

1. **两枚都是正面**
   - A = {正正}
   - m = 1
   - $$P(A) = \frac{1}{4}$$

2. **至少一枚正面**
   - B = {正正，正反，反正}
   - m = 3
   - $$P(B) = \frac{3}{4}$$

</v-clicks>

</div>

---
layout: center
---

# 排列组合在概率中的应用

<div class="space-y-6 max-w-4xl mx-auto">

## 常见模型

<v-clicks>

<div class="grid grid-cols-2 gap-4">
  <div class="bg-purple-100 p-4 rounded">
    <h4 class="font-bold">不放回抽样</h4>
    <p class="text-sm mt-2">用排列 $A_n^m$ 或组合 $C_n^m$</p>
  </div>
  <div class="bg-pink-100 p-4 rounded">
    <h4 class="font-bold">有放回抽样</h4>
    <p class="text-sm mt-2">每次独立，用乘法原理</p>
  </div>
  <div class="bg-blue-100 p-4 rounded">
    <h4 class="font-bold">分组问题</h4>
    <p class="text-sm mt-2">平均分组要除以组数的阶乘</p>
  </div>
  <div class="bg-green-100 p-4 rounded">
    <h4 class="font-bold">至少问题</h4>
    <p class="text-sm mt-2">考虑对立事件</p>
  </div>
</div>

</v-clicks>

</div>

---
layout: center
---

# 经典例题：摸球问题

<div class="bg-white bg-opacity-70 p-6 rounded-lg max-w-3xl mx-auto">

## 题目

袋中有 5 个红球，3 个白球，从中任取 2 个球，求：

<v-clicks>

1. 都是红球的概率
2. 至少有一个白球的概率

<div class="mt-6 text-left space-y-4">

## 解答

1. **都是红球**
   $$P = \frac{C_5^2}{C_8^2} = \frac{10}{28} = \frac{5}{14}$$

2. **至少一个白球**（对立事件：都是红球）
   $$P = 1 - \frac{5}{14} = \frac{9}{14}$$

</div>

</v-clicks>

</div>

---
layout: cover
class: text-white
background: 'https://images.unsplash.com/photo-1509228627152-72ae9ae6848d?q=80&w=2036&auto=format&fit=crop'
---

# 三、几何概型

---
layout: center
---

# 几何概型的概念

<div class="space-y-6 max-w-4xl mx-auto">

## 什么是几何概型？

<v-clicks>

<div class="bg-blue-50 p-6 rounded-lg">
  <p class="text-lg">
    当样本空间是<strong class="text-blue-600">连续的、无限的</strong>区域时
  </p>
  <p class="text-lg mt-2">
    用<strong class="text-blue-600">几何度量</strong>（长度、面积、体积）来计算概率
  </p>
</div>

<div class="bg-green-50 p-6 rounded-lg">
  <h3 class="text-xl font-bold mb-4">计算公式</h3>
  <p class="text-2xl text-center">
    $$P(A) = \frac{\text{构成事件 A 的区域度量}}{\text{全部区域的度量}}$$
  </p>
</div>

</v-clicks>

</div>

---
layout: two-cols
---

# 几何概型例题

::left::

<div class="space-y-4">

## 例题：会面问题

甲乙两人约定在 12:00-13:00 之间会面，先到者等候 15 分钟后即可离去。

求两人能会面的概率。

<v-clicks>

<div class="mt-4 bg-blue-50 p-3 rounded text-xs">
  <p><strong>分析：</strong></p>
  <p>设甲 x 分钟到，乙 y 分钟到</p>
  <p>0 ≤ x ≤ 60, 0 ≤ y ≤ 60</p>
  <p>会面条件：|x - y| ≤ 15</p>
</div>

</v-clicks>

</div>

::right::

<div class="space-y-4">

## 解答

<v-clicks>

<div class="bg-white p-4 rounded">

**样本空间面积**
$$S_{\Omega} = 60 \times 60 = 3600$$

**不能会面的面积**
$$S_{\text{不能}} = 2 \times \frac{1}{2} \times 45 \times 45 = 2025$$

**会面概率**
$$P = 1 - \frac{2025}{3600} = \frac{1575}{3600} = \frac{7}{16}$$

</div>

</v-clicks>

</div>

---
layout: center
---

# 几何概型常见类型

<div class="grid grid-cols-3 gap-4 mt-8">
  <div class="bg-blue-100 p-4 rounded">
    <div class="text-3xl mb-2">📏</div>
    <h4 class="font-bold">长度型</h4>
    <p class="text-xs mt-2">线段上的点</p>
    <p class="text-xs">如：等车时间</p>
  </div>
  <div class="bg-green-100 p-4 rounded">
    <div class="text-3xl mb-2">🔲</div>
    <h4 class="font-bold">面积型</h4>
    <p class="text-xs mt-2">平面区域</p>
    <p class="text-xs">如：会面问题</p>
  </div>
  <div class="bg-purple-100 p-4 rounded">
    <div class="text-3xl mb-2">📦</div>
    <h4 class="font-bold">体积型</h4>
    <p class="text-xs mt-2">空间区域</p>
    <p class="text-xs">如：三维空间</p>
  </div>
</div>

---
layout: cover
class: text-white
background: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=2070&auto=format&fit=crop'
---

# 四、条件概率与独立事件

---
layout: center
---

# 条件概率

<div class="space-y-6 max-w-4xl mx-auto">

## 定义

<v-clicks>

<div class="bg-blue-50 p-6 rounded-lg">
  <p class="text-lg mb-4">
    在事件 A 发生的条件下，事件 B 发生的概率称为条件概率
  </p>
  <p class="text-2xl text-center">
    $$P(B|A) = \frac{P(AB)}{P(A)}, \quad P(A) > 0$$
  </p>
</div>

<div class="bg-green-50 p-4 rounded">
  <h4 class="font-bold mb-2">乘法公式</h4>
  <p class="text-lg">
    $$P(AB) = P(A) \cdot P(B|A)$$
  </p>
</div>

</v-clicks>

</div>

---
layout: two-cols
---

# 条件概率例题

::left::

<div class="space-y-4">

## 例题

一个家庭有两个孩子，已知其中一个是女孩，求另一个也是女孩的概率。

<v-clicks>

<div class="mt-4 bg-blue-50 p-3 rounded text-sm">
  <p><strong>分析：</strong></p>
  <p>Ω = {男男，男女，女男，女女}</p>
  <p>A：至少一个女孩 = {男女，女男，女女}</p>
  <p>B：两个都是女孩 = {女女}</p>
</div>

</v-clicks>

</div>

::right::

<div class="space-y-4">

## 解答

<v-clicks>

<div class="bg-white p-4 rounded">

$$P(A) = \frac{3}{4}$$

$$P(AB) = P(B) = \frac{1}{4}$$

$$P(B|A) = \frac{P(AB)}{P(A)} = \frac{1/4}{3/4} = \frac{1}{3}$$

</div>

<div class="mt-4 text-xs text-gray-600">
  答案：1/3
</div>

</v-clicks>

</div>

---
layout: center
---

# 相互独立事件

<div class="space-y-6 max-w-4xl mx-auto">

## 定义

<v-clicks>

<div class="bg-purple-50 p-6 rounded-lg">
  <p class="text-lg">
    如果事件 A 的发生<strong class="text-purple-600">不影响</strong>事件 B 发生的概率
  </p>
  <p class="text-lg mt-2">
    则称 A 与 B 相互独立
  </p>
</div>

<div class="bg-green-50 p-6 rounded-lg">
  <h3 class="text-xl font-bold mb-4">独立事件的性质</h3>
  <p class="text-2xl text-center">
    $$A, B \text{独立} \iff P(AB) = P(A) \cdot P(B)$$
  </p>
</div>

</v-clicks>

</div>

---
layout: center
---

# 独立重复试验

<div class="bg-white bg-opacity-70 p-6 rounded-lg max-w-3xl mx-auto">

## n 次独立重复试验

<v-clicks>

<div class="space-y-4">

<div class="bg-blue-50 p-4 rounded">
  <h4 class="font-bold">二项分布</h4>
  <p class="text-sm mt-2">
    在 n 次独立重复试验中，事件 A 恰好发生 k 次的概率：
  </p>
  <p class="text-lg mt-2">
    $$P(X=k) = C_n^k p^k (1-p)^{n-k}$$
  </p>
  <p class="text-xs mt-2">其中 p 为每次试验中 A 发生的概率</p>
</div>

<div class="bg-green-50 p-4 rounded">
  <h4 class="font-bold">常见应用</h4>
  <ul class="text-sm mt-2 space-y-1">
    <li>• 射击命中目标</li>
    <li>• 产品合格率检验</li>
    <li>• 投篮命中率</li>
  </ul>
</div>

</div>

</v-clicks>

</div>

---
layout: cover
class: text-white
background: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=2070&auto=format&fit=crop'
---

# 五、全概率公式与贝叶斯公式

---
layout: center
---

# 全概率公式

<div class="space-y-6 max-w-4xl mx-auto">

## 公式内容

<v-clicks>

<div class="bg-blue-50 p-6 rounded-lg">
  <p class="text-sm mb-4">
    设 $B_1, B_2, ..., B_n$ 是样本空间的一个<strong class="text-blue-600">划分</strong>（互斥且并为全集）
  </p>
  <p class="text-lg">
    则对任意事件 A：
  </p>
  <p class="text-2xl mt-4 text-center">
    $$P(A) = \sum_{i=1}^{n} P(B_i) \cdot P(A|B_i)$$
  </p>
</div>

<div class="bg-green-50 p-4 rounded">
  <h4 class="font-bold">思想方法</h4>
  <p class="text-sm mt-2">化整为零，分而治之</p>
</div>

</v-clicks>

</div>

---
layout: two-cols
---

# 全概率公式例题

::left::

<div class="space-y-4">

## 例题：产品检验

某工厂有三条生产线，产量占比分别为：
- 甲线：50%，次品率 2%
- 乙线：30%，次品率 3%
- 丙线：20%，次品率 4%

求任取一件产品是次品的概率。

</div>

::right::

<div class="space-y-4">

## 解答

<v-clicks>

<div class="bg-white p-4 rounded text-sm">

设 A = {取到次品}，$B_i$ = {来自第 i 条线}

$$P(A) = P(B_1)P(A|B_1) + P(B_2)P(A|B_2) + P(B_3)P(A|B_3)$$

$$= 0.5 \times 0.02 + 0.3 \times 0.03 + 0.2 \times 0.04$$

$$= 0.01 + 0.009 + 0.008 = 0.027$$

</div>

<div class="mt-4 text-xs">
  答案：2.7%
</div>

</v-clicks>

</div>

---
layout: center
---

# 贝叶斯公式

<div class="space-y-6 max-w-4xl mx-auto">

## 公式内容

<v-clicks>

<div class="bg-purple-50 p-6 rounded-lg">
  <p class="text-lg mb-4">
    在全概率公式条件下，若 $P(A) > 0$，则：
  </p>
  <p class="text-xl text-center">
    $$P(B_j|A) = \frac{P(B_j) \cdot P(A|B_j)}{\sum_{i=1}^{n} P(B_i) \cdot P(A|B_i)}$$
  </p>
</div>

<div class="bg-green-50 p-4 rounded">
  <h4 class="font-bold">公式含义</h4>
  <p class="text-sm mt-2">
    <strong>由果溯因</strong>：已知结果 A 发生，推断是由哪个原因 $B_j$ 导致的概率
  </p>
</div>

</v-clicks>

</div>

---
layout: two-cols
---

# 贝叶斯公式例题

::left::

<div class="space-y-4">

## 接上题

已知取到的是次品，求它来自甲生产线的概率。

<div class="mt-4 bg-blue-50 p-3 rounded text-xs">
  <p><strong>已知：</strong></p>
  <p>P(甲) = 0.5, P(次 | 甲) = 0.02</p>
  <p>P(次) = 0.027</p>
</div>

</div>

::right::

<div class="space-y-4">

## 解答

<v-clicks>

<div class="bg-white p-4 rounded text-sm">

$$P(\text{甲}|\text{次}) = \frac{P(\text{甲}) \cdot P(\text{次}|\text{甲})}{P(\text{次})}$$

$$= \frac{0.5 \times 0.02}{0.027}$$

$$= \frac{0.01}{0.027} \approx 0.370$$

</div>

<div class="mt-4 text-xs">
  答案：约 37%
</div>

</v-clicks>

</div>

---
layout: center
---

# 贝叶斯公式的应用

<div class="grid grid-cols-2 gap-6 mt-8">
  <div class="bg-blue-100 p-4 rounded">
    <h3 class="font-bold mb-2">🏥 医学诊断</h3>
    <p class="text-xs">
      已知检测结果为阳性，求实际患病的概率
    </p>
  </div>
  <div class="bg-green-100 p-4 rounded">
    <h3 class="font-bold mb-2">📧 垃圾邮件过滤</h3>
    <p class="text-xs">
      已知邮件包含某些关键词，求是垃圾邮件的概率
    </p>
  </div>
  <div class="bg-purple-100 p-4 rounded">
    <h3 class="font-bold mb-2">🔍 故障诊断</h3>
    <p class="text-xs">
      已知设备出现异常，求是某种故障的概率
    </p>
  </div>
  <div class="bg-orange-100 p-4 rounded">
    <h3 class="font-bold mb-2">⚖️ 司法判断</h3>
    <p class="text-xs">
      已知某些证据，求嫌疑人有罪的概率
    </p>
  </div>
</div>

---
layout: cover
class: text-white
background: 'https://images.unsplash.com/photo-1509228627158-e62911f8a77a?q=80&w=2070&auto=format&fit=crop'
---

# 总结与练习

---
layout: center
---

# 知识框架

<div class="grid grid-cols-3 gap-4 mt-8 text-sm">
  <div class="bg-blue-100 p-4 rounded">
    <h4 class="font-bold mb-2">📌 基础概念</h4>
    <ul class="space-y-1 text-xs">
      <li>• 随机事件</li>
      <li>• 样本空间</li>
      <li>• 概率定义</li>
      <li>• 概率性质</li>
    </ul>
  </div>
  <div class="bg-green-100 p-4 rounded">
    <h4 class="font-bold mb-2">📐 概率模型</h4>
    <ul class="space-y-1 text-xs">
      <li>• 古典概型</li>
      <li>• 几何概型</li>
      <li>• 条件概率</li>
      <li>• 独立事件</li>
    </ul>
  </div>
  <div class="bg-purple-100 p-4 rounded">
    <h4 class="font-bold mb-2">🔢 重要公式</h4>
    <ul class="space-y-1 text-xs">
      <li>• 乘法公式</li>
      <li>• 全概率公式</li>
      <li>• 贝叶斯公式</li>
      <li>• 二项分布</li>
    </ul>
  </div>
</div>

---
layout: center
---

# 解题方法总结

<div class="space-y-4 max-w-3xl mx-auto">
  <div class="bg-white bg-opacity-70 p-4 rounded text-left">
    <h4 class="font-bold">1️⃣ 判断概率模型</h4>
    <p class="text-sm text-gray-700">有限等可能 → 古典概型；连续区域 → 几何概型</p>
  </div>
  <div class="bg-white bg-opacity-70 p-4 rounded text-left">
    <h4 class="font-bold">2️⃣ 正确使用排列组合</h4>
    <p class="text-sm text-gray-700">区分有放回/不放回，注意平均分组问题</p>
  </div>
  <div class="bg-white bg-opacity-70 p-4 rounded text-left">
    <h4 class="font-bold">3️⃣ 灵活运用对立事件</h4>
    <p class="text-sm text-gray-700">"至少"问题常考虑对立事件</p>
  </div>
  <div class="bg-white bg-opacity-70 p-4 rounded text-left">
    <h4 class="font-bold">4️⃣ 识别条件概率</h4>
    <p class="text-sm text-gray-700">注意"已知...求..."的表述</p>
  </div>
</div>

---
layout: center
---

# 易错点提醒

<div class="grid grid-cols-2 gap-4 mt-8">
  <div class="bg-red-100 p-4 rounded border-l-4 border-red-500">
    <h4 class="font-bold text-red-700">⚠️ 混淆独立与互斥</h4>
    <p class="text-xs mt-2">独立：P(AB) = P(A)P(B)</p>
    <p class="text-xs">互斥：P(AB) = 0</p>
  </div>
  <div class="bg-red-100 p-4 rounded border-l-4 border-red-500">
    <h4 class="font-bold text-red-700">⚠️ 条件概率颠倒</h4>
    <p class="text-xs mt-2">P(A|B) ≠ P(B|A)</p>
  </div>
  <div class="bg-red-100 p-4 rounded border-l-4 border-red-500">
    <h4 class="font-bold text-red-700">⚠️ 几何度量错误</h4>
    <p class="text-xs mt-2">注意是长度、面积还是体积</p>
  </div>
  <div class="bg-red-100 p-4 rounded border-l-4 border-red-500">
    <h4 class="font-bold text-red-700">⚠️ 重复计数</h4>
    <p class="text-xs mt-2">平均分组要除以组数阶乘</p>
  </div>
</div>

---
layout: center
---

# 课后练习

<div class="space-y-4 max-w-2xl mx-auto">
  <div class="bg-blue-50 p-4 rounded text-left">
    <h4 class="font-bold">基础题</h4>
    <p class="text-sm mt-2">1. 从 1,2,3,4,5 中任取两个数，求和为偶数的概率</p>
    <p class="text-sm mt-2">2. 在区间 [0,10] 内任取一数，求小于 3 的概率</p>
  </div>
  <div class="bg-green-50 p-4 rounded text-left">
    <h4 class="font-bold">提高题</h4>
    <p class="text-sm mt-2">3. 某疾病患病率为 0.1%，检测准确率为 99%，若检测结果为阳性，求实际患病的概率</p>
  </div>
</div>

---
layout: center
class: text-white
background: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=2070&auto=format&fit=crop'
---

# 谢谢！

<div class="mt-12 space-y-4">
  <p class="text-2xl">📚 概率是研究随机现象的数学工具</p>
  <p class="text-gray-200">掌握基本概念，熟练运用公式，多做练习</p>
</div>

<div class="mt-16 flex gap-4 justify-center">
  <span class="px-4 py-2 bg-blue-500 bg-opacity-50 rounded-full text-sm">古典概型</span>
  <span class="px-4 py-2 bg-green-500 bg-opacity-50 rounded-full text-sm">几何概型</span>
  <span class="px-4 py-2 bg-purple-500 bg-opacity-50 rounded-full text-sm">贝叶斯公式</span>
</div>
