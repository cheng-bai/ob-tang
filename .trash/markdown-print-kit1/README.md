# Markdown Print Kit

> 教师使用纯 Markdown 编写讲义，通过 Pandoc 输出 A4 双面可打印 PDF  
> 支持 **Obsidian** 原生排版，一键导出学生版/教师版

## 快速开始

### 1. 安装依赖

```bash
brew install pandoc
brew install --cask wkhtmltopdf  # 可选，渲染效果更好
```

### 2. 编写题目

在 Obsidian 中按以下格式编写：

```markdown
---
tags: [数学/讲义，打印]
version: student
---

# 函数综合题集

## 一、基础题

### 例 1.1（A 组）

**题目** 已知集合 $A = \{x \mid -2 \leq x \leq 3\}$，则（    ）

- A. $\{x \mid 1 < x \leq 3\}$
- B. $\{x \mid 1 \leq x \leq 3\}$
- C. $\{x \mid -2 \leq x \leq 3\}$
- D. $\{x \mid x > -2\}$

> [!blank]- 留白
> - 类型：选择题
> - 难度：A
> - 行数：2

<!-- Answer
**答案** A
**解析** 解析内容...
-->
```

### 3. 导出 PDF

```bash
# 学生版（无答案）
bash scripts/render-student.sh input.md output-student.pdf

# 教师版（含答案）
bash scripts/render-teacher.sh input.md output-teacher.pdf

# 先润色格式
bash scripts/polish.sh input.md
```

---

## 目录结构

```
markdown-print-kit/
├── scripts/
│   ├── polish.sh              # 格式润色
│   ├── render-student.sh      # 导出学生版
│   ├── render-teacher.sh      # 导出教师版
│   └── remove-answers.lua     # 答案过滤
├── templates/
│   ├── worksheet.html         # HTML 模板
│   ├── print.css              # 学生版样式
│   ├── print-teacher.css      # 教师版样式
│   └── obsidian-style.md      # 排版规范
├── examples/
│   └── 函数与集合综合题集.md    # 示例文件
└── README.md
```

---

## 排版规范

### 文档结构

| 层级 | 用途 |
|------|------|
| `#` | 讲义总标题 |
| `##` | 章节/知识点 |
| `###` | 单个题目 |

### 留白块（Callout）

使用 Obsidian 原生 callout 语法：

```markdown
> [!blank]- 留白
> - 类型：选择题 | 填空题 | 解答题
> - 难度：A | B | C
> - 行数：2
```

**推荐行数：**

| 题型 | A 组 | B 组 | C 组 |
|------|------|------|------|
| 选择题 | 2 | 3 | 3 |
| 填空题 | 2 | 3 | 4 |
| 解答题 | 6 | 8 | 10 |

### 答案隐藏

答案放在 HTML 注释中，学生版自动过滤：

```markdown
<!-- Answer
**答案** A
**解析** 详细解析...
-->
```

### 选项格式

```markdown
- A. 选项 A
- B. 选项 B
- C. 选项 C
- D. 选项 D
```

---

## Obsidian 集成

### 方法 1：使用 Templater 插件

创建模板文件，一键插入题目框架：

```markdown
### 例 <% tp.date.now("M.D") %>（A 组）

**题目** 

- A. 
- B. 
- C. 
- D. 

> [!blank]- 留白
> - 类型：选择题
> - 难度：A
> - 行数：2

<!-- Answer
**答案** 
**解析** 
-->
```

### 方法 2：使用 QuickAdd 宏

配置 QuickAdd 宏，选中题目文本后自动添加留白块和答案框。

### 方法 3：命令行调用

在 Obsidian 中安装 **Shell Commands** 插件，添加命令：

```bash
# 导出当前文件为学生版
bash /path/to/markdown-print-kit/scripts/render-student.sh "{{file.path}}" "{{file.path}}.pdf"
```

---

## 样式特点

- ✅ A4 双面打印，左右页边距不同（考虑装订）
- ✅ 题块防跨页，避免题目被切断
- ✅ 留白块自动绘制横线
- ✅ 学生版无答案，教师版答案醒目
- ✅ 支持 LaTeX 数学公式

---

## 常见问题

### Q: 为什么答案还在学生版中？

确保答案使用正确的注释格式：
```markdown
<!-- Answer
内容
-->
```

### Q: 留白块没有横线？

检查是否使用 `> [!blank]` 语法，并确保 CSS 正确加载。

### Q: 公式渲染异常？

确保使用 `$...$`（行内）或 `$$...$$`（独立）格式，Pandoc 会自动处理。

### Q: 想修改字体？

编辑 `templates/print.css`，修改 `font-family`。

---

## 更新日志

- **v2.0** - 支持 Obsidian callout 语法，新增教师版导出
- **v1.0** - 初始版本，支持基础打印功能
