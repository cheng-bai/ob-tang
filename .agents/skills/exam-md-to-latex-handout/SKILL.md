---
name: exam-md-to-latex-handout
description: >
  将已经润色加工过的数学试卷 Markdown 转换为 LaTeX 课堂讲评讲义，
  并同时生成教师版和学生版 PDF。适用于：加工版 MD 转 LaTeX、试卷
  生成教师版/学生版讲义、编译数学讲义 PDF、检查公式与图片渲染、
  记录讲义生成日志。触发词：MD转LaTeX讲义、试卷转讲义、教师版学生版、
  加工版 Markdown 编译、LaTeX 讲义生成。
---

# Exam MD to LaTeX Handout

## 目标

把 `outputs/试卷MD加工/` 中的加工版试卷 Markdown 转成可打印的课堂讲义：

- 教师版：题目、知识点标签、答案与解析。教师版面向老师阅读，应比学生版更紧凑；答案和解析放在同一个讲评盒中，并使用区别于题目蓝色的讲评色。
- 学生版：只保留题目与作答空间，源码中不隐藏教师内容；一道题不要跨页。
- PDF：使用 XeLaTeX 编译，确保公式、图片、目录、跳转可用。

## 当前定稿版式

后续 AI 复用时优先保持以下默认风格，除非用户明确要求改版：

- 教师版使用紧凑布局：`10pt`、正文 `\small`、较窄页边距、较小行距和段距。
- 学生版使用舒展布局：保留较大作答空间，不因压缩页数牺牲书写体验。
- 题目盒使用蓝色主视觉，标题只保留纯数字序号，如 `1`、`2`、`3`；不要写成“第 n 题”，也不要附加题型、分值或难度。
- 教师版答案与解析合并在一个绿色系 `feedbackBox`，盒内用“答案 / 解析”小标题分隔。
- 教学标签用灰底细边 `metaBox`，降低视觉权重，不和题目、讲评争抢注意力。
- 学生版每题使用 `Needspace + samepage`，宁可提前换页，也不要把同一道题拆成两页。
- 图片必须按横竖比自适应，教师版图片上限更保守，避免大图占据过高页面比例。
- 任何公式、OCR、图片、版式修复都优先沉淀回 `pipeline/build/试卷MD转LaTeX讲义.py`，不要只手改生成的 `.tex`。

## 输入要求

优先处理由 `pipeline/build/润色试卷MD.py` 生成的加工版 Markdown。文件应包含：

```markdown
---
title: "试卷标题"
knowledge_points:
  - name: "核心知识点"
    block: "解析几何"
    questions: [20]
    levels: ["压轴题"]
---

#### 第 20 题（解答）

- 核心知识点：
  - ...
- 题意理解：...

##### 题目

##### 答案

##### 解析
```

如果用户给的是原始转换稿，先用加工流程生成加工版 MD，再进入本 Skill。

## 标准命令

在仓库根目录执行：

```bash
python3 pipeline/build/试卷MD转LaTeX讲义.py \
  "outputs/试卷MD加工/试卷名-加工版.md"
```

批量处理 2026 届二模原始 `*-dollar.md` 时，使用：

```bash
python3 pipeline/build/批量处理2026二模试卷.py
```

该命令会自动完成：

- 从 `0-一模-二模-模考试卷-md版本/` 发现 2026 届二模原始试卷 Markdown。
- 复制并润色到 `outputs/试卷MD加工/2026二模批量润色/`，文件名为 `*-AI润色版.md`。
- 在 Markdown frontmatter 与试卷信息中写入加工署名。
- 转换并编译教师版/学生版 PDF 到 `outputs/试卷LaTeX讲义/2026二模批量输出/`。
- 生成 `batch-report.json`，记录页数、编译状态、学生版泄露检查、题框标题检查和 LaTeX 日志检查。

默认输出到：

```text
outputs/试卷LaTeX讲义/试卷标题/
├── 试卷标题-教师版.tex
├── 试卷标题-教师版.pdf
├── 试卷标题-学生版.tex
├── 试卷标题-学生版.pdf
└── images/
```

如需指定输出根目录：

```bash
python3 pipeline/build/试卷MD转LaTeX讲义.py \
  "outputs/试卷MD加工/试卷名-加工版.md" \
  --outdir "outputs/试卷LaTeX讲义"
```

## 编译 PDF

进入生成目录后分别编译：

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error "试卷标题-教师版.tex"
latexmk -xelatex -interaction=nonstopmode -halt-on-error "试卷标题-学生版.tex"
```

如果没有 `latexmk`，可用 `xelatex` 连续编译两次，但优先使用 `latexmk`。

## 必做质检

### 1. LaTeX 日志检查

```bash
rg -n "Missing character|Undefined references|LaTeX Error|Fatal|Emergency stop|Overfull|upper box part" \
  "outputs/试卷LaTeX讲义/试卷标题/"*.log || true
```

目标：无输出。若出现报错，先修复公式、图片路径、表格或过长盒子。

### 2. 学生版泄露检查

学生版不能包含答案、解析、教学标签或隐藏教师内容：

```bash
rg -n "答案|解析：|教学标签|核心知识点|solutionBox|answerBox|feedbackBox|metaBox|teacheronly|studentonly" \
  "outputs/试卷LaTeX讲义/试卷标题/试卷标题-学生版.tex" || true
```

目标：无输出。若有命中，必须修改生成逻辑或重新生成，不要只靠 LaTeX 条件隐藏。

### 3. 学生版分页检查

学生版每道题应作为一个完整单元处理，不能让题框跨页。生成的学生版 `.tex` 应满足：

```bash
rg -n -F '\Needspace' "outputs/试卷LaTeX讲义/试卷标题/试卷标题-学生版.tex" | wc -l
rg -n -F '\begin{samepage}' "outputs/试卷LaTeX讲义/试卷标题/试卷标题-学生版.tex" | wc -l
rg -n -F '\end{samepage}' "outputs/试卷LaTeX讲义/试卷标题/试卷标题-学生版.tex" | wc -l
```

目标：三个数量都应等于题目数。学生版 `questionBox` 不应带 `breakable`；教师版可以保留 `breakable` 以容纳长解析。

### 4. 图片检查

确认图片目录存在并且 PDF 中没有红色缺图提示：

```bash
find "outputs/试卷LaTeX讲义/试卷标题/images" -type f | wc -l
rg -n "图片缺失|includegraphics" "outputs/试卷LaTeX讲义/试卷标题/"*.tex
```

图片不应一律使用同一个固定宽度。转换脚本应读取图片实际尺寸，并按横竖比分档设置 `includegraphics`：

- 宽图：适当加宽，限制高度。
- 方图：收窄到中等宽度，避免撑开题目。
- 竖图：限制宽度，保留可读高度。
- 教师版：图片上限应比学生版更保守，避免一张图占据过高页面比例。

默认仍使用 `keepaspectratio`，不要拉伸变形。

### 5. PDF 基本信息

```bash
pdfinfo "outputs/试卷LaTeX讲义/试卷标题/试卷标题-教师版.pdf" | rg "Pages|Page size"
pdfinfo "outputs/试卷LaTeX讲义/试卷标题/试卷标题-学生版.pdf" | rg "Pages|Page size"
```

## 修复优先级

1. 先修编译失败：LaTeX 语法、未闭合公式、图片路径。
2. 再修数学渲染：弧符号、行列式、OCR 噪声、长公式换行。
3. 再修题目标题：题框标题只显示纯数字序号，如 `1`、`2`、`3`；题型、分值、难度不要放在题框标题里。
4. 再修学生版泄露：学生版源码必须干净。
5. 再修学生版分页：学生版题目用非 `breakable` 题框，并用 `Needspace + samepage` 包住题目和作答区。
6. 再修图片比例：根据图片横竖比调整 `includegraphics` 的宽高上限，保持 `keepaspectratio`。
7. 最后修版面：教师版使用更紧凑字号、页边距、行距和盒子间距；答案与解析放在一个统一的讲评盒里，内部用小标题区分；不要拆成多个强配色盒子。

常见 OCR/公式问题已经在 `pipeline/build/试卷MD转LaTeX讲义.py` 的
`protect_common_math()` 中集中处理。新增修正规则时优先放在那里。

## 日志管理

完成后必须记录：

1. 在 `docs/工作记录/YYYY-MM-DD-单题索引与组卷闭环.md` 或当天工作记录追加一节。
2. 在 `00-索引与配置/任务执行记录.md` 追加任务摘要。
3. 在 `00-索引与配置/加工日志.jsonl` 追加机器可读记录。

日志至少包含：

- 输入 Markdown 路径。
- 输出目录。
- 教师版/学生版 `.tex` 与 `.pdf` 路径。
- 图片数量。
- 教师版/学生版页数。
- 编译命令。
- 日志检查结果。
- 学生版泄露检查结果。
- 做过的人工修复或脚本修复。

## 复用原则

- 不直接改原始转换稿；只处理加工版 MD 或脚本。
- 图片是题目上下文的一部分，不能丢。
- 图片大小要服务题目阅读，不使用“一刀切”大图比例。
- 教师版用于老师浏览，可以用 `10pt`、更小行距和更紧凑盒子；学生版保留更舒展的作答空间。
- 题框标题保持干净，只显示纯数字序号；不要自动加入“第 n 题、填空/选择/解答、分值、难度”。
- 不可靠的难度数值不要写入加工版 Markdown；教师版如需难度评价，应作为经过判断的讲评标签另行设计。
- 学生版不使用“隐藏答案”的策略，要在生成阶段排除答案与解析。
- 学生版不让一道题跨页；宁可增加页数，也不要把同一道题拆在两页。
- 教师版减少颜色层级；答案和解析使用同一个 `feedbackBox`，标签盒使用轻量灰底。
- 知识点总览服务于讲评导航，不把所有零散知识都塞进讲义。
- 每次完成后把可复用修复沉淀回脚本，避免只修单个 `.tex`。
