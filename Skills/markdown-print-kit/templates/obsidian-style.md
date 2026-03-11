# Obsidian 数学题集排版规范

## 文档结构

```markdown
---
tags: [数学/讲义, 打印]
created: 2026-03-11
version: student  # 或 teacher
---

# 讲义标题

## 章节名称

### 例 1.1（A 组・来源）

**题目** 题干内容...

- A. 选项 A
- B. 选项 B
- C. 选项 C
- D. 选项 D

> [!blank] 留白
> - 类型：选择题
> - 难度：A
> - 行数：2

<!-- Answer
**答案** A
**解析** 解析内容...
-->
```

## 核心规范

### 1. 题目标签

使用 `> [!blank]` callout 语法表示留白区域（Obsidian 原生支持）：

```markdown
> [!blank]- 留白
> - 类型：选择题 | 填空题 | 解答题
> - 难度：A | B | C
> - 行数：2
```

### 2. 答案隐藏

使用 HTML 注释包裹答案，渲染时自动过滤：

```markdown
<!-- Answer
**答案** A
**解析** 详细解析...
-->
```

### 3. 选项格式

选择题选项使用无序列表，便于 Obsidian 渲染：

```markdown
- A. 选项内容
- B. 选项内容
- C. 选项内容
- D. 选项内容
```

### 4. 公式书写

- 行内公式：`$E = mc^2$`
- 独立公式：`$$\int_0^1 f(x)dx$$`

### 5. 章节层级

| 层级 | 用途 |
|------|------|
| `#` | 讲义总标题 |
| `##` | 章节/知识点 |
| `###` | 单个题目 |

## 快速命令

```bash
# 导出学生版（无答案）
bash scripts/render-student.sh input.md output-student.pdf

# 导出教师版（含答案）
bash scripts/render-teacher.sh input.md output-teacher.pdf

# 润色 Markdown 格式
bash scripts/polish.sh input.md
```
