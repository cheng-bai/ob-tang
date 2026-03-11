---
theme: default
title: 游戏背后的数学博弈论
highlighter: shiki
lineNumbers: false
colorSchema: light
fonts:
  sans: 'system-ui'
  mono: 'Fira Code'
layout: cover
background: 'https://images.unsplash.com/photo-1611996997974-2fc12f8394ca?q=80&w=2070&auto=format&fit=crop'
---

# 如何用数学在游戏中必胜？

## 游戏背后的数学博弈论

<div class="pt-12">
  <span class="px-2 py-1 rounded border bg-opacity-50 bg-white text-gray-800">
    组合博弈论入门
  </span>
</div>

<div class="abs-br m-6 flex gap-2">
  <span class="text-sm opacity-75">清华姚班 AI 博士</span>
</div>

---
layout: center
---

# 从一个思想实验开始

<div class="grid grid-cols-2 gap-8 mt-8">
  <div class="bg-blue-100 p-6 rounded-lg">
    <h3 class="text-xl font-bold mb-4">🎮 围棋之神</h3>
    <p class="text-gray-700">两个 AI 对着空白棋盘沉思</p>
    <p class="text-gray-700 mt-2">"你怎么不落子呀？"</p>
    <p class="text-red-600 mt-4 font-bold">黑棋投子认负</p>
  </div>
  <div class="bg-green-100 p-6 rounded-lg">
    <h3 class="text-xl font-bold mb-4">♟️ 象棋之神</h3>
    <p class="text-gray-700">红棋稍作沉思</p>
    <p class="text-gray-700 mt-2">"要不咱们合了吧？"</p>
    <p class="text-blue-600 mt-4 font-bold">双方和棋</p>
  </div>
</div>

---
layout: center
---

# 策梅洛定理 (Zermelo's Theorem)

<div class="text-left space-y-6">

**任何双人有限确定完美信息零和游戏，必居其一：**

<v-clicks>

1. **先手有必胜策略**
2. **后手有必胜策略**  
3. **双方都有策略保证平局**

</v-clicks>

</div>

<div class="mt-12 p-4 bg-yellow-100 rounded-lg">
  <p class="text-sm">1913 年，德国数学家恩斯特·策梅洛提出</p>
</div>

---
layout: two-cols
---

# 游戏类型对比

::left::

<div class="space-y-4">

## ✅ 满足策梅洛定理

- 围棋
- 中国象棋
- 国际象棋
- 井字棋
- 五子棋

</div>

::right::

<div class="space-y-4">

## ❌ 不满足条件

- 有随机因素（骰子）
- 非完美信息（扑克）
- 无限游戏
- 多人游戏

</div>

---
layout: center
---

# 为什么还要下棋？

<div class="grid grid-cols-2 gap-8 mt-8">
  <div>
    <h3 class="text-xl font-bold mb-4">🔢 组合爆炸</h3>
    <div class="bg-gray-100 p-4 rounded text-sm space-y-2">
      <p>井字棋：<span class="text-green-600 font-mono">~几千种</span></p>
      <p>国际象棋：<span class="text-yellow-600 font-mono">10¹²⁰</span></p>
      <p>围棋：<span class="text-red-600 font-mono">10³⁰⁰+</span></p>
    </div>
    <p class="text-xs text-gray-500 mt-2">超过宇宙原子总数！</p>
  </div>
  <div>
    <h3 class="text-xl font-bold mb-4">🧠 有限理性</h3>
    <p class="text-gray-700 text-sm">
      即使存在必胜策略，人类也无法记忆和应用
    </p>
    <p class="text-gray-700 text-sm mt-4">
      比拼的是计算深度和局面判断
    </p>
  </div>
</div>

---
layout: cover
class: text-white
background: 'https://images.unsplash.com/photo-1596495578065-6e0763fa1178?q=80&w=2070&auto=format&fit=crop'
---

# 逆向归纳法

## 从终局反推每个局面的胜负

---
layout: center
---

# 案例 1：拿糖果游戏

<div class="bg-amber-100 p-6 rounded-lg max-w-2xl mx-auto">
  <h3 class="text-lg font-bold mb-4">🍬 游戏规则</h3>
  <ul class="text-left space-y-2 text-gray-700">
    <li>• 50 个糖果</li>
    <li>• A 和 B 轮流拿</li>
    <li>• 每次拿 1-3 个，不能不拿</li>
    <li>• <span class="text-red-600 font-bold">拿走最后一个糖果的人获胜</span></li>
  </ul>
</div>

<div class="mt-8 text-lg">
  <p>谁可以保证必胜？</p>
</div>

---
layout: two-cols
---

# 关键洞察

::left::

<div class="space-y-4">

## 互补策略

不管对方拿几个，你总可以拿一个**互补的数量**，使得：

$$\text{两人这轮共拿 4 个}$$

<v-clicks>

- 先手先拿 **2 个** → 剩 48 个（4 的倍数）
- 对方拿 1，你拿 3
- 对方拿 2，你拿 2
- 对方拿 3，你拿 1

</v-clicks>

</div>

::right::

<div class="space-y-4">

## 为什么是 4？

从终局逆向分析：

<v-clicks>

- **0 个**：先手必败（已输）
- **1-3 个**：先手必胜（一次拿完）
- **4 个**：先手必败（无论怎么拿都留给对方 1-3 个）
- **5-7 个**：先手必胜（可以留给对方 4 个）
- **8 个**：先手必败

</v-clicks>

</div>

---
layout: center
---

# 逆向归纳的过程

<div class="grid grid-cols-6 gap-2 mt-8">
  <div class="bg-red-500 text-white p-3 rounded text-center font-bold">0<br>必败</div>
  <div class="bg-green-500 text-white p-3 rounded text-center font-bold">1<br>必胜</div>
  <div class="bg-green-500 text-white p-3 rounded text-center font-bold">2<br>必胜</div>
  <div class="bg-green-500 text-white p-3 rounded text-center font-bold">3<br>必胜</div>
  <div class="bg-red-500 text-white p-3 rounded text-center font-bold">4<br>必败</div>
  <div class="bg-green-500 text-white p-3 rounded text-center font-bold">5<br>必胜</div>
</div>

<div class="grid grid-cols-6 gap-2 mt-2">
  <div class="bg-green-500 text-white p-3 rounded text-center font-bold">6<br>必胜</div>
  <div class="bg-green-500 text-white p-3 rounded text-center font-bold">7<br>必胜</div>
  <div class="bg-red-500 text-white p-3 rounded text-center font-bold">8<br>必败</div>
  <div class="bg-green-500 text-white p-3 rounded text-center font-bold">9<br>必胜</div>
  <div class="bg-green-500 text-white p-3 rounded text-center font-bold">10<br>必胜</div>
  <div class="bg-green-500 text-white p-3 rounded text-center font-bold">11<br>必胜</div>
</div>

<div class="mt-6 p-4 bg-blue-100 rounded">
  <p class="font-bold">规律浮现：4 的倍数 = 先手必败</p>
</div>

---
layout: center
---

# 一般规律

<div class="text-2xl space-y-4">

如果每次可以拿 **1 到 k** 个糖果：

<v-clicks>

<div class="mt-8 p-6 bg-purple-100 rounded-lg">
  <p>关键控制点 = <span class="text-purple-600 font-bold">(k+1) 的倍数</span></p>
</div>

<div class="mt-4 text-gray-600 text-lg">
  <p>50 个糖果，每次 1-4 个？</p>
  <p class="mt-2">→ 控制 <span class="font-bold text-green-600">5 的倍数</span></p>
</div>

</v-clicks>

</div>

---
layout: cover
class: text-white
background: 'https://images.unsplash.com/photo-1533227297462-09e47577523c?q=80&w=2070&auto=format&fit=crop'
---

# 案例 2：两堆糖果

## 模仿策略的力量

---
layout: center
---

# 新游戏规则

<div class="bg-pink-100 p-6 rounded-lg max-w-3xl mx-auto">
  <h3 class="text-lg font-bold mb-4">🍬🍬 两堆糖果</h3>
  <ul class="text-left space-y-2 text-gray-700">
    <li>• 两堆糖果，每堆 100 个</li>
    <li>• 每次从<strong>同一堆</strong>拿任意多个</li>
    <li>• 不能不拿</li>
    <li>• <span class="text-red-600 font-bold">拿走最后一个糖果的人获胜</span></li>
  </ul>
</div>

---
layout: center
---

# 二维局面分析

<div class="relative">
  <div class="grid grid-cols-6 gap-1 mt-4">
    <div v-for="i in 36" :key="i" class="w-12 h-12 rounded border flex items-center justify-center text-xs"
      :class="i % 7 === 0 ? 'bg-red-500 text-white' : 'bg-green-100'">
      {{ Math.floor((i-1)/6) }},{{ (i-1)%6 }}
    </div>
  </div>
  
  <div class="mt-6 p-4 bg-blue-100 rounded">
    <p class="font-bold">关键洞察：对角线 = 必败</p>
    <p class="text-sm mt-2">两堆数量相同时，先手必败</p>
  </div>
</div>

---
layout: two-cols
---

# 必胜策略

::left::

<div class="space-y-4">

## 模仿策略

<v-clicks>

1. 对方在一堆拿多少
2. 你在另一堆拿**相同数量**
3. 始终保持两堆相等
4. 最终必胜

</v-clicks>

</div>

::right::

<div class="space-y-4">

## 为什么有效？

<v-clicks>

- 对称性游戏
- 后手可以镜像先手操作
- 先手永远面对对称局面
- 直到最后 (0,0) 先手输

</v-clicks>

</div>

---
layout: center
---

# 策略窃取 (Strategy Stealing)

<div class="grid grid-cols-2 gap-8 mt-8">
  <div class="bg-purple-100 p-6 rounded-lg">
    <h3 class="text-xl font-bold mb-4">🍫 毒巧克力游戏</h3>
    <p class="text-sm text-gray-700">
      M×N 巧克力，左下角有毒<br>
      选 (x,y) 吃掉右上方所有<br>
      吃到最后一块的输
    </p>
    <p class="mt-4 font-bold text-purple-600">结论：先手必胜</p>
  </div>
  <div class="bg-indigo-100 p-6 rounded-lg">
    <h3 class="text-xl font-bold mb-4">⬛ 六贯棋 (Hex)</h3>
    <p class="text-sm text-gray-700">
      黑棋连左右，白棋连上下<br>
      不可能平局
    </p>
    <p class="mt-4 font-bold text-indigo-600">结论：先手必胜</p>
  </div>
</div>

---
layout: center
---

# 策略窃取的证明思路

<div class="space-y-4 text-left max-w-3xl mx-auto">

<v-clicks>

1. **假设**后手有必胜策略
2. 先手随便走一步，然后**假装自己是后手**
3. 如果必胜策略要求走那一步，就再随便走一步
4. 先手相当于**偷了后手的策略**还多一个子
5. 多一个子只可能更好，不可能更差
6. **矛盾**！所以假设错误

</v-clicks>

</div>

<div class="mt-8 p-4 bg-red-100 rounded">
  <p class="font-bold">结论：先手必胜（但不告诉我们具体怎么走）</p>
</div>

---
layout: center
---

# 策略窃取的局限

<div class="grid grid-cols-2 gap-8 mt-8">
  <div class="bg-green-100 p-6 rounded-lg">
    <h3 class="text-xl font-bold mb-4">✅ 适用</h3>
    <ul class="text-left space-y-2 text-sm">
      <li>• 六贯棋</li>
      <li>• 毒巧克力</li>
      <li>• 无禁手五子棋</li>
    </ul>
    <p class="text-xs mt-4 text-gray-600">多一个子总是有利的</p>
  </div>
  <div class="bg-red-100 p-6 rounded-lg">
    <h3 class="text-xl font-bold mb-4">❌ 不适用</h3>
    <ul class="text-left space-y-2 text-sm">
      <li>• 中国象棋</li>
      <li>• 国际象棋</li>
      <li>• 围棋</li>
    </ul>
    <p class="text-xs mt-4 text-gray-600">存在"谁先动谁输"的局面</p>
  </div>
</div>

---
layout: cover
class: text-white
background: 'https://images.unsplash.com/photo-1580582932707-520aed937b7b?q=80&w=2069&auto=format&fit=crop'
---

# 人类如何思考？

## α-β剪枝与局面评估

---
layout: center
---

# 井字棋的 α-β剪枝

<div class="grid grid-cols-3 gap-4 mt-8">
  <div class="bg-gray-100 p-4 rounded">
    <h4 class="font-bold text-sm mb-2">当前局面</h4>
    <div class="text-2xl font-mono">X O _<br/>_ X _<br/>O _ _</div>
  </div>
  <div class="bg-gray-100 p-4 rounded">
    <h4 class="font-bold text-sm mb-2">分析 4 种走法</h4>
    <p class="text-xs text-gray-600">利用对称性减少计算</p>
  </div>
  <div class="bg-gray-100 p-4 rounded">
    <h4 class="font-bold text-sm mb-2">剪枝</h4>
    <p class="text-xs text-gray-600">找到必胜就走，不用分析其他</p>
  </div>
</div>

---
layout: two-cols
---

# 人类下棋的方法

::left::

<div class="space-y-4">

## 搜索树

- 计算能覆盖的深度
- 每一步的最优选择
- 考虑对方的应对

</div>

::right::

<div class="space-y-4">

## 局面评估

- 象棋：子力价值
- 围棋：实地/外势
- 不精确但快速的判断

</div>

---
layout: center
---

# 什么是"神之一手"？

<div class="bg-gradient-to-r from-yellow-100 to-orange-100 p-8 rounded-lg max-w-3xl mx-auto">
  <p class="text-lg leading-relaxed">
    一个看似必败的局面，<br>
    其实存在一步能够倒向胜利的<strong class="text-orange-600">妙招</strong>
  </p>
  <p class="text-sm text-gray-600 mt-6">
    它不仅是一步棋，更包含了所有后续局面的逆向推导结果
  </p>
</div>

<div class="mt-8 grid grid-cols-3 gap-4">
  <div class="text-center">
    <div class="text-3xl mb-2">🎯</div>
    <p class="text-xs">走出后必胜</p>
  </div>
  <div class="text-center">
    <div class="text-3xl mb-2">🔗</div>
    <p class="text-xs">后续手段连贯</p>
  </div>
  <div class="text-center">
    <div class="text-3xl mb-2">✨</div>
    <p class="text-xs">化腐朽为神奇</p>
  </div>
</div>

---
layout: center
class: text-white
background: 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop'
---

# 总结

<div class="grid grid-cols-2 gap-8 mt-12 text-left">
  <div class="bg-black bg-opacity-50 p-6 rounded-lg">
    <h3 class="text-xl font-bold mb-4">🎓 核心概念</h3>
    <ul class="space-y-2 text-sm">
      <li>• 策梅洛定理</li>
      <li>• 逆向归纳法</li>
      <li>• 策略窃取</li>
      <li>• α-β剪枝</li>
    </ul>
  </div>
  <div class="bg-black bg-opacity-50 p-6 rounded-lg">
    <h3 class="text-xl font-bold mb-4">💡 关键洞察</h3>
    <ul class="space-y-2 text-sm">
      <li>• 游戏开局胜负已分</li>
      <li>• 组合爆炸让人类比拼有意义</li>
      <li>• 有限理性是人类的局限</li>
    </ul>
  </div>
</div>

---
layout: center
---

# 谢谢！

<div class="mt-12 space-y-4">
  <p class="text-2xl">🎮 数学 + 游戏 = 博弈论</p>
  <p class="text-gray-600">组合爆炸 × 有限理性 = 人类下棋的意义</p>
</div>

<div class="mt-16 flex gap-4 justify-center">
  <span class="px-4 py-2 bg-blue-100 rounded-full text-sm">点赞</span>
  <span class="px-4 py-2 bg-pink-100 rounded-full text-sm">收藏</span>
  <span class="px-4 py-2 bg-purple-100 rounded-full text-sm">关注</span>
</div>
