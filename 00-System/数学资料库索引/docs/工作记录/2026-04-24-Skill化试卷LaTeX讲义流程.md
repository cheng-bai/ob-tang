# 2026-04-24 试卷 LaTeX 讲义流程 Skill 化记录

## 背景

用户要求把“加工版试卷 Markdown 转教师版/学生版 LaTeX 讲义并编译 PDF”的流程沉淀成 Skills，方便后续其他 AI 复用。

## 新增 Skill

```text
.agents/skills/exam-md-to-latex-handout/SKILL.md
```

Skill 名称：

```text
exam-md-to-latex-handout
```

适用场景：

- 加工版 Markdown 转 LaTeX 课堂讲评讲义。
- 同时生成教师版和学生版。
- 编译数学讲义 PDF。
- 检查公式、图片、目录跳转与学生版答案泄露。
- 记录讲义生成日志。

## 固化的执行流程

标准入口：

```bash
python3 pipeline/build/试卷MD转LaTeX讲义.py \
  "outputs/试卷MD加工/试卷名-加工版.md"
```

编译入口：

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error "试卷标题-教师版.tex"
latexmk -xelatex -interaction=nonstopmode -halt-on-error "试卷标题-学生版.tex"
```

## 固化的质量检查

Skill 中要求每次生成后至少检查：

- LaTeX fatal/error。
- Missing character。
- Undefined references。
- Overfull 与 tcolorbox 溢出。
- 学生版源码是否泄露答案、解析、教学标签。
- 图片目录是否存在，PDF 是否有缺图提示。
- 教师版与学生版 PDF 页数和纸张大小。

## 设计取舍

- 没有复制一份转换脚本到 Skill 目录，避免 `pipeline/build/试卷MD转LaTeX讲义.py` 与 Skill 脚本产生维护分叉。
- Skill 负责告诉 AI 如何调用、如何检查、如何回写日志；稳定转换逻辑仍保留在 pipeline 中。
- 学生版明确要求源码级净化，不允许只用 LaTeX 条件隐藏答案。
- 新增公式/OCR 修复时，优先沉淀回 `protect_common_math()`。

## 验证

```text
Skill frontmatter: 通过
必要引用路径: 通过
入口脚本存在: 通过
日志路径存在: 通过
```

## 追加记录：学生版题目不跨页

### 背景

用户要求 LaTeX 输出学生版时，不要让一道题目跨越一页。

### 已调整

修改：

```text
pipeline/build/试卷MD转LaTeX讲义.py
.agents/skills/exam-md-to-latex-handout/SKILL.md
```

调整策略：

- `guidebase` 默认不再设置 `breakable`。
- 教师版题框、答案框、解析框显式保留 `breakable`，适配长解析。
- 学生版题框不带 `breakable`。
- 学生版每题前加入 `\Needspace{...}`，空间不足时提前换页。
- 学生版每题使用 `samepage` 包住题框和作答区，避免同一题拆页。

### 重新生成与验证

样例：

```text
outputs/试卷MD加工/2026届浦东新区高三下二模数学试卷-加工版.md
```

结果：

```text
教师版 PDF: 22 页，A4
学生版 PDF: 15 页，A4
学生版 Needspace 数量: 21
学生版 begin{samepage} 数量: 21
学生版 end{samepage} 数量: 21
学生版 questionBox breakable: 0
教师版 questionBox breakable: 1
LaTeX fatal/error/missing character/undefined reference/overfull/tcolorbox overfull: 0
```

## 追加记录：题框标题改为纯数字序号

### 背景

用户进一步指出：题框标题不要显示“第几题”，而是只显示序号。

### 已调整

修改：

```text
pipeline/build/试卷MD转LaTeX讲义.py
.agents/skills/exam-md-to-latex-handout/SKILL.md
```

调整策略：

- LaTeX 题框标题由“第 n 题”改为纯数字序号。
- 生成效果为 `1`、`2`、`3`，不显示“第”“题”。
- Skill 同步更新，后续复用时默认采用纯序号。
- 题型、分值、难度继续不进入题框标题。

### 重新生成与验证

```text
教师版 PDF: 17 页，A4
学生版 PDF: 15 页，A4
教师版题框标题: 21 个，异常标题 0 个
学生版题框标题: 21 个，异常标题 0 个
学生版答案解析泄露: 0
LaTeX fatal/error/missing character/undefined reference/overfull/tcolorbox overfull: 0
```

## 追加记录：教师版紧凑化与讲评盒换色

### 背景

用户反馈教师版是给老师看的，可以更紧凑一些，答案与解析盒也希望换成不同于题目蓝色的颜色；同时大图不应占据过高页面比例。

### 已调整

修改：

```text
pipeline/build/试卷MD转LaTeX讲义.py
.agents/skills/exam-md-to-latex-handout/SKILL.md
```

调整策略：

- 教师版文档从 `11pt` 改为 `10pt`。
- 教师版页边距收紧为 `left/right=1.55cm`，`top=1.75cm`，`bottom=1.85cm`。
- 教师版正文启用 `\small`。
- 教师版行距从 `1.26` 调整为 `1.14`。
- 教师版段距从 `0.45em` 调整为 `0.28em`。
- 教师版盒子内边距和上下间距同步缩小。
- `feedbackBox` 从蓝色改为绿色系，和题目蓝色形成区分。
- 教师版图片尺寸上限进一步收缩，例如宽图上限为 `width=0.66\linewidth,height=0.18\textheight`。

### 重新生成与验证

```text
教师版 PDF: 17 页，A4
学生版 PDF: 15 页，A4
教师版 10pt: true
教师版绿色 feedbackBox: true
教师版正文 small: true
教师版图片压缩参数: true
学生版 Needspace/samepage 数量: 21/21
学生版 feedbackBox: 0
LaTeX fatal/error/missing character/undefined reference/overfull/tcolorbox overfull: 0
```

## 阶段总结：Skill 进化定稿

### 本阶段形成的稳定判断

这轮从“能生成 LaTeX”推进到了“有教师版/学生版差异化版式”的阶段。

稳定下来的原则：

- 教师版不是学生版加答案，而是老师快速浏览与讲评用材料。
- 学生版核心是留白、题目完整、不泄露答案。
- 教师版核心是紧凑、信息密度高、颜色层级少。
- 答案与解析属于同一讲评信息，应放在一个统一盒子里，而不是拆成多个强配色盒子。
- 图片是题目上下文，但不能压过题目本身；教师版尤其要控制图片占比。
- Skill 应记录审美和取舍，不只记录命令。

### 已写入 Skill 的进化点

```text
.agents/skills/exam-md-to-latex-handout/SKILL.md
```

新增“当前定稿版式”：

- 教师版默认 `10pt`、正文 `\small`、紧凑页边距、紧凑行距和段距。
- 学生版默认保留较大作答空间。
- 题目盒使用蓝色主视觉。
- 教师版答案与解析统一放入绿色系 `feedbackBox`。
- 教学标签使用灰底细边 `metaBox`。
- 学生版每题使用 `Needspace + samepage`，不让同题跨页。
- 图片按横竖比自适应，教师版图片上限更保守。
- 可复用修复必须沉淀回 pipeline 脚本。

### 当前样例状态

```text
输入: outputs/试卷MD加工/2026届浦东新区高三下二模数学试卷-加工版.md
输出目录: outputs/试卷LaTeX讲义/2026届浦东新区高三下二模数学试卷
教师版 PDF: 17 页，A4
学生版 PDF: 15 页，A4
编译: latexmk -xelatex 通过
LaTeX fatal/error/missing character/undefined reference/overfull/tcolorbox overfull: 0
学生版答案解析泄露: 0
学生版题目完整单元: 21/21
```

### 后续可继续进化

- 为不同用途增加样式参数：`teacher_compact`、`teacher_readable`、`student_practice`。
- 增加批处理命令，把一批加工版 MD 批量生成双版本 PDF。
- 增加 PDF 截图抽检，对图片过大、空白过多、题目跨页做视觉级检查。
- 将“题号 -> 核心知识点 -> 讲评用途”进一步做成教师版前置索引表。

## 追加记录：题框标题简化

### 背景

用户反馈每道题最前面的“第几题、题型、几分、难度”组合不美观，且难度标注不够可靠。要求先改 Markdown，再转换成 LaTeX；题框标题只保留题目序号。

### 已调整

修改：

```text
outputs/试卷MD加工/2026届浦东新区高三下二模数学试卷-加工版.md
pipeline/build/润色试卷MD.py
pipeline/build/试卷MD转LaTeX讲义.py
.agents/skills/exam-md-to-latex-handout/SKILL.md
```

调整策略：

- 当前浦东加工版 Markdown 删除每题 `难度` 与 `分值` 行。
- 润色源头脚本不再生成 `难度` 与 `分值` 行，避免后续试卷继续污染。
- LaTeX 题框标题从 `第 n 题｜题型｜分值｜难度` 继续收敛为纯数字序号。
- Skill 中补充规则：题框标题只保留纯数字序号，不自动加入“第 n 题”、题型、分值或难度。
- 不可靠的难度数值不写入加工版 Markdown；后续如需难度评价，应另做经过判断的教师版讲评标签。

### 重新生成与验证

```text
加工版 Markdown 难度/分值字段: 0
润色源头脚本难度/分值输出: 0
教师版题框标题: 21
教师版异常标题（含题型/分值/难度）: 0
学生版题框标题: 21
学生版异常标题（含题型/分值/难度）: 0
教师版 PDF: 17 页，A4
学生版 PDF: 15 页，A4
LaTeX fatal/error/missing character/undefined reference/overfull/tcolorbox overfull: 0
```

说明：学生版页数从 13 页增加到 15 页，是为了保证题目整体不跨页而产生的正常结果。

## 追加记录：图片比例自适应

### 背景

用户要求 LaTeX 输出时注意图片大小，调整成更合适的比例。

### 已调整

修改：

```text
pipeline/build/试卷MD转LaTeX讲义.py
.agents/skills/exam-md-to-latex-handout/SKILL.md
```

调整策略：

- 新增 `image_dimensions()`，读取 PNG/JPEG 的实际宽高。
- 新增 `image_latex_options()`，按图片横竖比分档生成 `includegraphics` 参数。
- 宽图使用较大宽度但限制高度。
- 方图收窄到中等宽度，避免挤占题面。
- 竖图限制宽度，保留可读高度。
- 所有图片继续使用 `keepaspectratio`，不拉伸变形。

### 重新生成与验证

```text
教师版 PDF: 22 页，A4
学生版 PDF: 15 页，A4
学生版图片数: 3
教师版图片数: 7
学生版 Needspace/samepage 数量: 21/21/21
LaTeX fatal/error/missing character/undefined reference/overfull/tcolorbox overfull: 0
```

样例中实际生成的图片参数包含：

```text
方图: width=0.54\linewidth,height=0.28\textheight,keepaspectratio
宽图: width=0.76\linewidth,height=0.24\textheight,keepaspectratio
```

## 追加记录：教师版答案解析盒合并

### 背景

用户反馈教师版中教学标签、答案、解析分别使用三个配色和三个彩色盒子，视觉上显得杂乱。

### 已调整

修改：

```text
pipeline/build/试卷MD转LaTeX讲义.py
.agents/skills/exam-md-to-latex-handout/SKILL.md
```

调整策略：

- 删除独立的 `answerBox` 和 `solutionBox`。
- 新增统一的 `feedbackBox`，标题为“答案与解析”。
- 在同一个盒子内部用轻量小标题区分“答案”和“解析”。
- `feedbackBox` 使用主蓝色弱底色，避免新增绿色/红色视觉层级。
- `metaBox` 改为轻量灰底细边，降低“教学标签”的视觉权重。

### 重新生成与验证

```text
教师版 PDF: 22 页，A4
学生版 PDF: 15 页，A4
教师版 answerBox: 0
教师版 solutionBox: 0
教师版 GuideBrick: 0
教师版 feedbackBox: 已启用
学生版 feedbackBox/answerBox/solutionBox: 0
学生版 Needspace/samepage 数量: 21/21/21
LaTeX fatal/error/missing character/undefined reference/overfull/tcolorbox overfull: 0
```
