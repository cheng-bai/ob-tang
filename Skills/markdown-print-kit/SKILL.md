# markdown-print-kit

高中数学讲义 Markdown 转 PDF 打印工具包。提供完整的排版规范、转换脚本和样式模板，支持学生版（无答案）和教师版（含答案）双版本输出。

---

## 使用场景

- 将 Obsidian 中的数学讲义 Markdown 文件导出为 PDF
- 生成学生版练习卷（自动隐藏答案）
- 生成教师版参考卷（包含完整答案和解析）
- 统一数学题目的排版格式

---

## 前置依赖

```bash
# 必需
brew install pandoc

# 可选（渲染效果更好）
brew install --cask wkhtmltopdf
```

---

## 核心格式规范

### 1. Frontmatter 设置

```yaml
---
title: 2022-23 高三数学冲刺 - 第 X 讲
tags: [高三冲刺, 知识点, 专题复习]
难度: ⭐⭐⭐⭐
年份: 2022
适用年级: 高三
课时: 2 课时
知识点: [知识点1, 知识点2]
打印版本: 学生版  # 或 教师版
cssclasses: [math-worksheet]
---
```

### 2. 题目块标准格式

```markdown
<div class="question-block" markdown="1">

### 题目 X ⭐⭐⭐

题干内容... $LaTeX公式$

![](图片URL)

<br><br><br>

> [!answer]- 📌 查看答案
> 
> **答案：** 答案内容
> 
> **解析：** 
> 
> 详细解析步骤...

</div>

---
```

### 3. 留白区域（Obsidian Callout）

```markdown
> [!blank] 留白
> - 类型：选择题 | 填空题 | 解答题
> - 难度：A | B | C
> - 行数：2  # 决定留白高度
```

### 4. 答案隐藏（HTML 注释）

```markdown
<!-- Answer
**答案** A
**解析** 详细解析内容...
-->
```

---

## 脚本使用

### 导出学生版（无答案）

```bash
bash scripts/render-student.sh input.md output-student.pdf
```

### 导出教师版（含答案）

```bash
bash scripts/render-teacher.sh input.md output-teacher.pdf
```

### 润色 Markdown 格式

```bash
bash scripts/polish.sh input.md
```

---

## 文件结构

```
markdown-print-kit/
├── SKILL.md                          # 本文件
├── 快速开始.md                        # 快速入门指南
├── 教师写作清单.md                    # 教师编写检查清单
├── examples/                          # 示例文件
│   ├── 函数与集合综合题集.md
│   └── 函数与集合综合题集（打印版）.md
├── scripts/                           # 转换脚本
│   ├── render-student.sh             # 导出学生版
│   ├── render-teacher.sh             # 导出教师版
│   ├── polish.sh                     # 格式润色
│   ├── remove-answers.lua            # 移除答案 filter
│   ├── convert-callouts.lua          # 转换 callout filter
│   ├── normalize-space-markers.sh    # 空间标记规范化
│   └── space-lines.lua               # 行距调整 filter
└── templates/                         # 模板文件
    ├── print.css                     # 打印样式（学生版）
    ├── print-teacher.css             # 打印样式（教师版）
    ├── worksheet.html                # HTML 模板
    ├── obsidian-style.md             # Obsidian 排版规范
    ├── obsidian-template-选择题.md    # 选择题模板
    ├── obsidian-template-填空题.md    # 填空题模板
    └── obsidian-template-解答题.md    # 解答题模板
```

---

## CSS 打印样式

关键规则说明：

```css
@media print {
  /* 隐藏答案区域 */
  .callout[data-callout="answer"] {
    display: none !important;
  }
  
  /* 防止题目跨页 */
  .question-block {
    page-break-inside: avoid;
    break-inside: avoid;
    margin-bottom: 15px;
  }
  
  /* 隐藏教学反思（学生版）*/
  .print-hide-student {
    display: none !important;
  }
  
  /* 优化表格和图片分页 */
  table, img {
    page-break-inside: avoid;
  }
}
```

---

## Obsidian 集成

### 推荐插件

| 插件 | 用途 |
|------|------|
| Templater | 插入题目模板 |
| QuickAdd | 创建快捷命令 |
| Shell Commands | 直接调用导出脚本 |

### Shell Commands 配置示例

```bash
# 导出学生版
bash /path/to/markdown-print-kit/scripts/render-student.sh "{{file.path}}" "{{file.path:dirname}}/{{file.name}}-学生版.pdf"

# 导出教师版
bash /path/to/markdown-print-kit/scripts/render-teacher.sh "{{file.path}}" "{{file.path:dirname}}/{{file.name}}-教师版.pdf"
```

---

## 注意事项

| 问题 | 解决方案 |
|------|----------|
| 题目跨页 | 确保使用 `<div class="question-block" markdown="1">` 包裹 |
| 答案显示 | 学生版打印时答案自动隐藏，无需手动删除 |
| 图片分割 | CSS 已设置 `page-break-inside: avoid` |
| 表格分页 | 表格会自动保持完整 |
| LaTeX 公式 | 使用 `$...$` 格式，确保正确渲染 |

---

## 版本历史

| 版本 | 日期 | 更新内容 |
|------|------|----------|
| 1.0 | 2026-03-11 | 初始版本 |
| 2.0 | 2026-03-11 | 根据实际文档处理流程完善格式规范 |

---

*更新时间：2026-03-11 | 版本：2.0*
