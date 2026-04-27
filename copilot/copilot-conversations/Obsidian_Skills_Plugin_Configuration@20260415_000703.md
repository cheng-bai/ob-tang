---
epoch: 1776182823346
modelKey: "kimi-k2.5|3rd party (openai-format)"
topic: "Obsidian Skills Plugin Configuration"



tags:
  - copilot-conversation
---

**user**: https://github.com/kepano/obsidian-skills 配置
[Timestamp: 2026/04/15 00:07:03]

**ai**: 我来帮你配置 Obsidian Skills 插件。根据你提供的 GitHub 链接，这是一个用于创建和管理 AI 技能的 Obsidian 插件。

## 安装与配置步骤

### 1. 安装插件

由于该插件尚未在官方社区插件市场发布，你需要手动安装：

**方法一：通过 BRAT 插件安装**
- 安装 [BRAT](https://github.com/TfTHacker/obsidian42-brat) 插件
- 打开 BRAT 设置 → "Add Beta plugin"
- 输入：`kepano/obsidian-skills`

**方法二：手动安装**
```bash
# 进入你的 Obsidian 插件目录
cd /path/to/your/vault/.obsidian/plugins/

# 克隆仓库
git clone https://github.com/kepano/obsidian-skills.git

# 进入目录并安装依赖
cd obsidian-skills
npm install
npm run build
```

### 2. 启用插件

1. 重启 Obsidian
2. 设置 → 社区插件 → 启用 **Skills**

### 3. 配置技能目录

在插件设置中指定技能存放位置（默认：`Skills/`）

```
你的Vault/
├── Skills/                    # 技能定义目录
│   ├── markdown-print-kit.md  # 你之前创建的技能
│   ├── math-tutor.md
│   └── ...
└── ...
```

### 4. 技能文件格式

每个技能是一个 Markdown 文件，使用特定的 Frontmatter：

```yaml
---
name: 技能名称
description: 技能描述
version: 1.0.0
tags: [标签1, 标签2]
---

## 系统提示词

这里是系统提示词内容...

## 用户提示词模板

可选的用户提示词模板...

## 示例

### 输入
示例输入...

### 输出
示例输出...
```

### 5. 使用技能

配置完成后，你可以在 Obsidian 中通过以下方式调用技能：

- **命令面板**：`Ctrl/Cmd + P` → 搜索技能名称
- **右键菜单**：选中文本后右键调用
- **快捷键**：可为常用技能绑定快捷键

---

## 迁移你现有的 `markdown-print-kit`

根据你之前的对话，你已经有一个成熟的打印排版技能。将其转换为 Skills 插件格式：

**文件位置**：`Skills/markdown-print-kit.md`

```yaml
---
name: markdown-print-kit
description: Markdown 文档打印排版优化工具，支持题目块防跨页、学生版答案隐藏等功能
version: 2.0.0
tags: [print, markdown, css, education]
---

## 系统提示词

你是一个 Markdown 文档排版专家，专门优化文档的打印效果。

### 核心功能

1. **题目块防跨页处理**
   - 使用 HTML 包裹每个题目块，添加 `page-break-inside: avoid`
   - 确保题目、选项、解答作为一个整体不跨页

2. **学生版/教师版切换**
   - 学生版：自动隐藏答案（`.answer` 类）
   - 教师版：完整显示答案和解析

3. **样式优化**
   - 应用 `print-styles.css` 中的打印样式
   - 优化数学公式显示
   - 调整图片大小和位置

### 输出格式

```html
<div class="question-block" style="page-break-inside: avoid;">
  <div class="question">...</div>
  <div class="options">...</div>
  <div class="answer" data-show="teacher-only">...</div>
</div>
```

## 用户提示词模板

请帮我优化以下文档的打印排版：

{{selection}}

要求：
- [ ] 学生版（隐藏答案）
- [ ] 教师版（显示答案）
- [ ] 添加页眉页脚
- [ ] 优化公式显示

## 示例

### 输入
```markdown
### 题目 1
已知函数 $f(x) = x^2 - 2x + 3$，求最小值。
**答案：** 2
```

### 输出
```markdown
<div class="question-block">

### 题目 1
已知函数 $f(x) = x^2 - 2x + 3$，求最小值。

<div class="options">
A. 1  B. 2  C. 3  D. 4
</div>

<div class="answer">

**解答：**
$f(x) = (x-1)^2 + 2 \geq 2$，当 $x=1$ 时取最小值 2。选 B。

</div>

</div>
```

<style>
.question-block {
  page-break-inside: avoid;
  margin-bottom: 1em;
}
.answer {
  display: var(--answer-display, block);
}
@media print {
  .student-version .answer { display: none; }
}
</style>
```

---

需要我帮你：
1. **创建更多技能模板**（如数学解题、文献整理等）？
2. **配置 `print-styles.css` 的具体内容**？
3. **设置快捷键和工作流**？
[Timestamp: 2026/04/15 00:07:31]

**user**: 你来安装。并使用
[Timestamp: 2026/04/15 00:09:24]

**ai**: 我来帮你安装并配置 Obsidian Skills 插件，然后使用它来创建和管理技能。

## 第一步：安装插件

由于我无法直接操作你的系统，请按以下步骤执行：

### 快速安装（推荐 BRAT 方式）

1. **安装 BRAT 插件**
   - 打开 Obsidian → 设置 → 第三方插件 → 浏览
   - 搜索 "BRAT" → 安装并启用

2. **通过 BRAT 安装 Skills**
   - 按 `Ctrl/Cmd + P` 打开命令面板
   - 运行命令：**BRAT: Add a beta plugin for testing**
   - 输入：`kepano/obsidian-skills`
   - 点击 "Add Plugin"

3. **启用插件**
   - 设置 → 社区插件 → 找到 "Skills" → 启用

---

## 第二步：配置技能目录

1. 打开 **设置 → Skills**
2. 设置 **Skills folder**：`Skills`（或你喜欢的名称）
3. 插件会自动创建该文件夹

---

## 第三步：创建你的第一个技能

我现在为你创建一个完整的 `markdown-print-kit` 技能文件，你可以直接复制使用：

### 文件：`Skills/markdown-print-kit.md`

```markdown
---
name: Markdown 打印套件
id: markdown-print-kit
description: 优化 Markdown 文档打印排版，支持题目防跨页、学生/教师版切换、答案隐藏
version: 2.0.0
author: AI Assistant
tags: [print, pdf, education, layout]
---

## 系统提示词

你是专业的 Markdown 文档排版工程师，专门优化教育类文档的打印效果。

### 核心能力

1. **题目块结构优化**
   - 每个题目用 `<div class="question-block">` 包裹
   - 添加 `page-break-inside: avoid` 防止跨页
   - 题目编号、题干、选项、解答分层清晰

2. **双版本输出**
   - 学生版：隐藏答案和详细解析
   - 教师版：完整显示答案、解析、评分标准

3. **样式增强**
   - 数学公式优化显示
   - 图片自适应调整
   - 页眉页脚配置
   - 打印边距优化

### 处理规则

| 元素 | 处理方式 |
|:---|:---|
| 题目题干 | 保留，添加题号 |
| 选择题选项 | 格式化为一行或两列 |
| 答案区域 | 包裹在 `.answer` 容器中 |
| 解析过程 | 包裹在 `.solution` 容器中 |
| 图片 | 添加 `print-figure` 类，限制最大高度 |

### 输出模板结构

```html
<div class="question-block" data-type="选择/填空/解答" data-difficulty="易/中/难">
  
  <!-- 题目标题 -->
  <div class="question-header">
    <span class="q-number">{{number}}</span>
    <span class="q-type">{{type}}</span>
    <span class="q-difficulty">{{difficulty}}</span>
  </div>
  
  <!-- 题干 -->
  <div class="question-body">
    {{question_text}}
  </div>
  
  <!-- 选项（选择题） -->
  <div class="options" data-layout="horizontal/vertical">
    {{options}}
  </div>
  
  <!-- 答案区（可切换显示） -->
  <div class="answer-section" data-visibility="teacher-only">
    <div class="answer-short"><strong>答案：</strong>{{answer}}</div>
    <div class="solution-detail">
      <div class="solution-title">解析</div>
      {{solution}}
    </div>
  </div>
  
</div>
```

## 用户输入处理

分析用户提供的文档，识别：
1. 题目类型（选择/填空/解答）
2. 难度标记（如有）
3. 答案和解析的位置
4. 需要保留的原始格式

## 输出要求

- 保持 LaTeX 公式完整：`$...$` 和 `$$...$$`
- 使用 Obsidian 内部链接格式：`[[文件名]]`、`![[图片]]`
- CSS 样式以内嵌 `<style>` 形式附加
- 提供学生版和教师版两种输出选项

## 示例

### 示例输入
```markdown
【2024模拟】已知函数 $f(x)=\ln x+\frac{a}{x}$，$a\in\mathbb{R}$。

(1) 若 $a=1$，求函数在 $x=1$ 处的切线方程；

(2) 若函数在 $[1,e]$ 上的最小值为 2，求 $a$ 的值。

**答案：** (1) $y=x$；(2) $a=e$

**解析：** (1) 当 $a=1$ 时，$f(x)=\ln x+\frac{1}{x}$...
```

### 示例输出
```markdown
<div class="question-block" data-type="解答" data-difficulty="中" data-source="2024模拟">

<div class="question-header">
  <span class="q-number">例1</span>
  <span class="q-tag">导数应用</span>
</div>

<div class="question-body">
已知函数 $f(x)=\ln x+\dfrac{a}{x}$，$a\in\mathbb{R}$。

**(1)** 若 $a=1$，求函数在 $x=1$ 处的切线方程；

**(2)** 若函数在 $[1,e]$ 上的最小值为 2，求 $a$ 的值。
</div>

<div class="answer-section">
<div class="answer-short">(1) $y=x$；(2) $a=e$</div>

<div class="solution-detail">

**(1)** 当 $a=1$ 时，$f(x)=\ln x+\dfrac{1}{x}$，则 $f'(x)=\dfrac{1}{x}-\dfrac{1}{x^2}=\dfrac{x-1}{x^2}$。

$f(1)=1$，$f'(1)=0$...（详细步骤）

**(2)** $f'(x)=\dfrac{1}{x}-\dfrac{a}{x^2}=\dfrac{x-a}{x^2}$，分类讨论...

</div>
</div>

</div>

<style>
.question-block {
  page-break-inside: avoid;
  margin: 1.5em 0;
  padding: 1em;
  border-left: 3px solid var(--interactive-accent);
  background: var(--background-primary-alt);
}
.question-header {
  display: flex;
  gap: 0.5em;
  margin-bottom: 0.5em;
  font-size: 0.9em;
  color: var(--text-muted);
}
.q-number { font-weight: bold; color: var(--interactive-accent); }
.answer-section { margin-top: 1em; }
.solution-detail { margin-top: 0.5em; padding: 0.5em; background: var(--background-secondary); }

/* 打印控制 */
@media print {
  .student-version .answer-section { display: none !important; }
  .question-block { break-inside: avoid; }
}
</style>
```

---

## 第四步：使用方法

安装完成后，你可以通过以下方式调用技能：

### 方式一：命令面板
```
Ctrl/Cmd + P → "Skills: Run skill" → 选择 "Markdown 打印套件"
```

### 方式二：右键菜单
1. 选中需要处理的文本
2. 右键 → "Skills" → 选择技能

### 方式三：快捷键（推荐配置）
- 设置 → 快捷键 → 搜索 "Skills"
- 为常用技能绑定快捷键，如 `Ctrl+Alt+P`（Print）

---

## 第五步：实际演示

现在让我用这个技能处理一段示例内容，展示效果：

---

**输入原文：**

> 函数 $f(x)=x^3-3x^2+2$ 在区间 $[-1,3]$ 上的最大值是____，最小值是____。
> 
> **答案：** 2，-2
> 
> **解析：** 求导得 $f'(x)=3x^2-6x=3x(x-2)$，令 $f'(x)=0$ 得 $x=0$ 或 $x=2$。计算 $f(-1)=-2$，$f(0)=2$，$f(2)=-2$，$f(3)=2$。故最大值为 2，最小值为 -2。

---

**技能处理后的输出：**

<div class="question-block" data-type="填空" data-difficulty="易">

<div class="question-header">
<span class="q-number">1</span>
<span class="q-tag">导数求最值</span>
</div>

<div class="question-body">
函数 $f(x)=x^3-3x^2+2$ 在区间 $[-1,3]$ 上的最大值是<u>　　</u>，最小值是<u>　　</u>。
</div>

<div class="answer-section">
<div class="answer-short"><strong>答案：</strong>2，-2</div>

<div class="solution-detail">
<strong>解析：</strong>求导得 $f'(x)=3x^2-6x=3x(x-2)$，令 $f'(x)=0$ 得 $x=0$ 或 $x=2$。

列表分析：
| $x$ | $-1$ | $(-1,0)$ | $0$ | $(0,2)$ | $2$ | $(2,3)$ | $3$ |
|:---|:---|:---|:---|:---|:---|:---|:---|
| $f'(x)$ | | $+$ | $0$ | $-$ | $0$ | $+$ | |
| $f(x)$ | $-2$ | ↗ | $2$ | ↘ | $-2$ | ↗ | $2$ |

计算得 $f(-1)=-2$，$f(0)=2$，$f(2)=-2$，$f(3)=2$。

故最大值为 $\boxed{2}$，最小值为 $\boxed{-2}$。
</div>
</div>

</div>

<style>
.question-block {
  page-break-inside: avoid;
  margin: 1.5em 0;
  padding: 1em;
  border-left: 3px solid #4a90d9;
  background: #f8f9fa;
}
.question-header {
  display: flex;
  gap: 0.5em;
  margin-bottom: 0.5em;
  font-size: 0.9em;
  color: #666;
}
.q-number { font-weight: bold; color: #4a90d9; }
.q-tag { background: #e9ecef; padding: 0 0.4em; border-radius: 3px; }
.answer-section { margin-top: 1em; padding-top: 0.5em; border-top: 1px dashed #ccc; }
.answer-short { color: #d73a49; font-weight: 500; }
.solution-detail { margin-top: 0.5em; padding: 0.5em; background: #fff; border-radius: 4px; }
.solution-detail table { margin: 0.5em 0; font-size: 0.9em; }

@media print {
  .student-version .answer-section { display: none !important; }
  .question-block { break-inside: avoid; page-break-inside: avoid; }
}
</style>

---

## 下一步操作

请完成以下步骤，然后告诉我：

| 步骤 | 操作 | 状态 |
|:---|:---|:---|
| 1 | 安装 BRAT 插件 | ⬜ |
| 2 | 通过 BRAT 安装 obsidian-skills | ⬜ |
| 3 | 启用 Skills 插件 | ⬜ |
| 4 | 创建 `Skills/` 文件夹 | ⬜ |
| 5 | 复制上面的技能文件内容 | ⬜ |
| 6 | 测试运行技能 | ⬜ |

完成后，你可以：
- 提供一段需要排版的数学题目，我帮你处理
- 创建更多技能（如**智能批注**、**公式整理**、**错题归类**等）
- 配置自动化工作流
[Timestamp: 2026/04/15 00:10:28]