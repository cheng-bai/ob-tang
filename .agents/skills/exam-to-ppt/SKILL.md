---
name: exam-to-ppt
description: >
  将数学试卷 Markdown 转换为 LaTeX Beamer 幻灯片（PPT），支持题目智能分页、
  真实图片注入、选择题选项自动排版、教师/学生双模式。适用于：
  (1) 把试卷 Markdown 转成课堂板书 PPT，
  (2) 生成题目讲解幻灯片，
  (3) 处理 exam/试卷/试题库中的 Markdown 文件输出为 PDF，
  (4) 任何需要数学题目 LaTeX Beamer 排版的场景。
  触发词：试卷转PPT、生成题目幻灯片、exam to ppt、beamer 题目、
  课堂板书、数学试卷排版、处理试卷。
---

# Exam to PPT — 试卷题目 → LaTeX Beamer 幻灯片

## 核心能力

将标准格式的试卷 Markdown 文件转换为美观的 LaTeX Beamer 幻灯片 PDF，
支持智能分页、真实图片、动态字号、等间距排版。

## 工作流程

### Step 1: 检查输入文件

确认用户提供的 Markdown 文件存在，格式符合标准试卷格式。

**标准格式要求：**
```markdown
## 一、填空题

1. 题目内容... $公式$ ...

<!-- 图：图片描述（可选）-->

【答案】答案内容
【解析】解析内容

2. 下一题...

## 二、选择题

13. 题目内容
A. 选项1 B. 选项2 C. 选项3 D. 选项4

## 三、解答题

17. 题目内容
(1) 小问1
(2) 小问2
```

**关键规则：**
- 题型用 `## 一、填空题` 等章节标题标识
- 题号用 `数字.` 开头
- 答案用 `【答案】` 标记
- 解析用 `【解析】` 标记
- 图片用 HTML 注释 `<!-- 图：描述 -->` 占位，或用 `<img src="path">` 引用真实图片
- 表格用 HTML `<table>` 标签
- 公式用 `$...$`（行内）或 `$$...$$`（行间）

### Step 2: 图片处理（如有 result.json）

如果用户提供了解析工具生成的 `result.json`（如 marker/pdf2md 输出），
运行图片注入脚本自动提取图片并插入到 Markdown 中：

```bash
python scripts/inject_images.py \
    -r /path/to/result.json \
    -i /path/to/exam.md \
    -o /path/to/exam-with-images.md
```

此脚本会：
1. 从 `result.json` 提取每道题对应的图片路径
2. 将 `<!-- 图：... -->` 占位符替换为 `<img src="images/xxx.jpg">`
3. 把图片复制到输出目录的 `images/` 文件夹

### Step 3: 生成 LaTeX

运行主转换脚本：

```bash
python scripts/md_to_ppt.py \
    -i /path/to/exam-with-images.md \
    -o output.tex
```

**常用参数：**

| 参数 | 说明 | 示例 |
|------|------|------|
| `-i` | 输入 Markdown 文件 | `-i exam.md` |
| `-o` | 输出 LaTeX 文件 | `-o output.tex` |
| `-q` | 题号筛选 | `-q 1,3,5-10,15` |
| `-m` | 模式：`student`/`teacher`/`body-only` | `-m teacher` |
| `-l` | 布局：`auto`/`single`/`compact` | `-l auto` |
| `--answer-area` | 解答题添加答题区域 | `--answer-area` |
| `--max-height` | 单页最大高度(cm) | `--max-height 10.0` |

**模式说明：**
- `student`（默认）：只显示题目，适合课堂练习
- `teacher`：显示题目 + 答案（绿色）+ 解析（蓝色），适合讲解
- `body-only`：显示题目 + 答案，不显示解析

### Step 4: 编译 PDF

使用 `xelatex` 编译：

```bash
xelatex -interaction=nonstopmode output.tex
```

如果图片路径正确且 `images/` 目录存在，编译后 PDF 会直接显示真实图片。

## 输出特点

- **16:9 宽屏比例**，适合投影
- **纯白背景**，无多余装饰线
- **等间距分布**：多题一页时题目均匀分布，不挤在顶部
- **动态字号**：根据内容量自动调整（\small / \footnotesize / \scriptsize）
- **正确换行**：题号与正文用 minipage 分隔，长文本自动换行
- **页码**：右下角显示 `当前页 / 总页数`
- **选择题选项**：自动检测 A/B/C/D 并排版为 4/2/1 栏
- **填空横线**：`___` 自动转换为美观下划线
- **HTML 表格**：自动转换为 LaTeX `tabular`

## 目录结构要求

生成 `.tex` 后，确保图片在正确位置。推荐结构：

```
project/
├── exam.md
├── images/              # 图片目录（与 tex 同级或相对路径正确）
│   ├── image_1.jpg
│   └── ...
└── output.tex
```

如果图片在别处，修改 md 中的 `<img src="...">` 路径为相对 tex 文件的正确路径。

## 常见问题

### Q: 编译报错 "Undefined control sequence"
确保安装了 `ctex`、`tasks`、`graphicx` 等宏包。使用 TeX Live / MacTeX 完整版。

### Q: 图片不显示
检查 `images/` 目录是否和 `.tex` 文件在同一目录，或路径是否正确。

### Q: 某题内容溢出页面
超长题会自动启用 `allowframebreaks` 分页，并缩小字号到 `\scriptsize`。
如需进一步调整，可用 `-q` 单独筛选该题，或降低 `--max-height`。

### Q: 没有 result.json 但有图片
直接在 md 文件中手写 `<img src="path/to/image.jpg">`，parser 会自动识别。

## 脚本文件

- `scripts/md_to_ppt.py` — 主转换脚本
- `scripts/inject_images.py` — 从 result.json 注入图片的辅助脚本
