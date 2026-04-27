---
epoch: 1776264429000
modelKey: "kimi-k2.5|3rd party (openai-format)"
topic: "Obsidian Skills Introduction"



tags:
  - copilot-conversation
---

**user**: 你好使用obsidian-skills
[Timestamp: 2026/04/15 22:47:09]

**ai**: 你好！我看到你想使用 `obsidian-skills` 技能。根据之前的对话记录，我们已经创建并完善了 `markdown-print-kit` 这个技能，它专门用于优化 Obsidian 文档的打印排版，特别是针对数学题目和教育类文档。

## markdown-print-kit 技能概览

这个技能主要包含以下功能：

### 1. 文档 Frontmatter 模板
```yaml
---
title: 文档标题
date: 2026-04-15
tags: [数学, 高三, 冲刺]
cssclasses:
  - print-optimized
  - math-document
print_options:
  show_answer: false  # 学生版设为 false，教师版设为 true
  page_break: true    # 题目间是否分页
---
```

### 2. 题目块格式
```markdown
> [!question] 题目 1
> 已知函数 $f(x) = \ln x - ax + \frac{1}{x}$...
> 
> > [!blank] 解答
> > 详细解答内容...
```

### 3. 打印优化 CSS 类
- `.no-break` - 防止内容跨页断裂
- `.question-block` - 题目块样式
- `.answer-hidden` / `.answer-visible` - 控制答案显示/隐藏

---

**你想用这个技能做什么？** 例如：
- 格式化新的数学文档？
- 调整现有文档的打印样式？
- 修改技能配置（如答案显示设置）？
- 应用到其他类型的文档？

请告诉我具体需求，我可以直接帮你处理！
[Timestamp: 2026/04/15 22:47:18]

**user**: Canvas Skills
[Timestamp: 2026/04/15 22:47:40]

**ai**: 你好！你想创建或使用 **Canvas Skills** —— 针对 Obsidian Canvas 的专用技能。

根据我们之前 `markdown-print-kit` 的经验，我可以帮你设计一个系统化的 Canvas 技能框架。请告诉我你的具体需求：

---

## 可能的 Canvas Skills 方向

| 技能类型 | 用途 | 典型场景 |
|---------|------|---------|
| **canvas-layout-kit** | 自动排版与美化 | 知识图谱、项目看板 |
| **canvas-mindmap** | 思维导图生成 | 头脑风暴、大纲转换 |
| **canvas-presentation** | 演示模式优化 | 幻灯片展示、教学课件 |
| **canvas-workflow** | 流程图/工作流 | 项目管理、算法流程 |
| **canvas-study-notes** | 学习笔记可视化 | 概念关联、复习卡片 |

---

## 请提供以下信息

1. **主要用途** —— 你想用 Canvas 做什么？
2. **内容来源** —— 从 Markdown 笔记生成？还是从零创建？
3. **自动化程度** —— 需要一键生成，还是手动调整为主？
4. **输出格式** —— 仅 Canvas 文件，还是需要导出（图片/PDF/网页）？

---

例如：
> "我想把 [[高三数学错题本]] 里的题目自动转换成 Canvas 卡片，按知识点分类排列"

或者：
> "我需要做一个项目进度看板，能从 [[任务清单]] 自动同步状态"

请描述你的场景，我来设计对应的技能方案！
[Timestamp: 2026/04/15 22:47:54]

**user**: 帮我画一幅高中所有知识点的框架图高中数学
[Context: Notes: 未命名.canvas]
[Timestamp: 2026/04/15 22:55:40]

**ai**: 我来帮你创建一幅**高中数学知识点框架图**的 Canvas 技能方案。这是一个 `.canvas` 文件，可以用 Obsidian 直接打开和编辑。

---

## 方案：canvas-math-framework 技能

### 核心结构（分层展开）

```
高中数学（根节点）
├── 预备知识
│   ├── 集合与逻辑
│   ├── 不等式
│   └── 函数概念
├── 函数与导数
│   ├── 基本初等函数
│   ├── 三角函数
│   ├── 函数性质与应用
│   └── 导数及其应用
├── 数列
│   ├── 等差数列
│   ├── 等比数列
│   └── 数列求和与递推
├── 立体几何
│   ├── 空间几何体
│   ├── 点线面位置关系
│   └── 空间向量与计算
├── 解析几何
│   ├── 直线与圆
│   ├── 椭圆
│   ├── 双曲线
│   └── 抛物线
├── 概率与统计
│   ├── 计数原理
│   ├── 概率
│   ├── 统计
│   └── 成对数据分析
└── 选考内容
    ├── 坐标系与参数方程
    └── 不等式选讲
```

---

### 生成的 Canvas 文件

由于当前文件解析出错，我直接为你生成标准的 `.canvas` JSON 结构。你可以：

**方法一：直接复制到文件**
1. 创建新文件 `高中数学知识框架.canvas`
2. 粘贴以下内容：

```json
{
	"nodes": [
		{"id": "root", "type": "text", "text": "## 高中数学\n**核心知识框架**", "x": 0, "y": 0, "width": 200, "height": 100, "color": "1"},
		{"id": "prep", "type": "text", "text": "### 预备知识\n- 集合与常用逻辑用语\n- 一元二次函数、方程和不等式\n- 函数的概念与性质", "x": -400, "y": 200, "width": 220, "height": 120, "color": "4"},
		{"id": "func", "type": "text", "text": "### 函数与导数\n- 指数函数与对数函数\n- 三角函数\n- 函数的应用\n- **导数及其应用** ⭐", "x": -150, "y": 200, "width": 220, "height": 140, "color": "2"},
		{"id": "seq", "type": "text", "text": "### 数列\n- 等差数列\n- 等比数列\n- 数列求和方法\n- 递推数列", "x": 100, "y": 200, "width": 200, "height": 120, "color": "4"},
		{"id": "solid", "type": "text", "text": "### 立体几何\n- 空间几何体结构\n- 点、直线、平面的位置关系\n- **空间向量与立体几何** ⭐", "x": 350, "y": 200, "width": 220, "height": 120, "color": "3"},
		{"id": "anal", "type": "text", "text": "### 解析几何\n- 直线与圆的方程\n- **椭圆** ⭐\n- **双曲线** ⭐\n- **抛物线** ⭐", "x": -300, "y": 400, "width": 200, "height": 140, "color": "5"},
		{"id": "prob", "type": "text", "text": "### 概率与统计\n- 计数原理\n- 随机变量及其分布\n- 统计与成对数据分析\n- **正态分布、回归分析**", "x": 0, "y": 400, "width": 220, "height": 140, "color": "6"},
		{"id": "elect", "type": "text", "text": "### 选考内容\n- 坐标系与参数方程\n- 不等式选讲", "x": 300, "y": 400, "width": 180, "height": 100, "color": "4"}
	],
	"edges": [
		{"id": "e1", "fromNode": "root", "fromSide": "bottom", "toNode": "prep", "toSide": "top"},
		{"id": "e2", "fromNode": "root", "fromSide": "bottom", "toNode": "func", "toSide": "top"},
		{"id": "e3", "fromNode": "root", "fromSide": "bottom", "toNode": "seq", "toSide": "top"},
		{"id": "e4", "fromNode": "root", "fromSide": "bottom", "toNode": "solid", "toSide": "top"},
		{"id": "e5", "fromNode": "func", "fromSide": "bottom", "toNode": "anal", "toSide": "top"},
		{"id": "e6", "fromNode": "func", "fromSide": "bottom", "toNode": "prob", "toSide": "top"},
		{"id": "e7", "fromNode": "seq", "fromSide": "bottom", "toNode": "prob", "toSide": "top"},
		{"id": "e8", "fromNode": "solid", "fromSide": "bottom", "toNode": "elect", "toSide": "top"}
	]
}
```

---

### 视觉效果说明

| 颜色代码 | 含义 | 使用模块 |
|---------|------|---------|
| 🟡 `1` (黄) | 核心根节点 | 高中数学总纲 |
| 🔴 `2` (红) | 重难点模块 | 函数与导数 |
| 🟢 `3` (绿) | 几何模块 | 立体几何 |
| 🔵 `4` (蓝) | 基础模块 | 预备知识、数列、选考 |
| 🟣 `5` (紫) | 解析几何 | 圆锥曲线 |
| 🟠 `6` (橙) | 应用模块 | 概率统计 |

---

### 进阶扩展建议

如果你想进一步细化，可以：

1. **展开具体考点** —— 如"导数"下展开：切线问题、单调性、极值最值、零点问题、不等式证明
2. **添加链接** —— 每个节点链接到对应笔记 `[[导数应用]]`
3. **标记考频** —— 用 ⭐ 表示高频考点，用 📌 表示易错点
4. **分层显示** —— 高一/高二/高三用不同颜色区分

---

需要我：
- **展开某个模块的详细知识点**？
- **生成带链接的完整版本**（链接到你的现有笔记）？
- **添加更多层级**（如每个知识点下的具体题型）？
- **导出为其他格式**（Markdown 大纲 / PDF 图片 / HTML）？
[Timestamp: 2026/04/15 22:56:19]