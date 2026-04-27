#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
from dataclasses import dataclass
from pathlib import Path


@dataclass
class QuestionMeta:
    module_dir: str
    module_name: str
    question_type: str
    difficulty: int
    subtopics: list[str]
    methods: list[str]
    answer_type: str
    answer_summary: str
    common_mistakes: list[str]


SOURCE = Path(
    "/Users/tangchengbaiair/Downloads/mini-数学资料库/试卷 latex 化/"
    "上海·2026_届浦东新区高三数学二模详解.pdf_os_d7ci9eilb0pc739j7m8g/"
    "上海·2026_届浦东新区高三数学二模详解-dollar.md"
)
SOURCE_IMAGE_DIR = SOURCE.parent / "images"
OUTPUT_ROOT = Path(
    "/Users/tangchengbaiair/Downloads/试卷切片库/数学切片样例/2026-26届-浦东-二模"
)

COMMON = {
    "subject": "高中数学",
    "exam": "二模",
    "year": 2026,
    "class": "26届",
    "district": "浦东",
    "source": SOURCE.name,
    "source_pdf": "上海·2026_届浦东新区高三数学二模详解.pdf",
}

QUESTION_STARTS = {
    1: 7,
    2: 11,
    3: 15,
    4: 23,
    5: 27,
    6: 31,
    7: 35,
    8: 37,
    9: 49,
    10: 71,
    11: 95,
    12: 113,
    13: 131,
    14: 143,
    15: 151,
    16: 167,
    17: 193,
    18: 247,
    19: 287,
    20: 325,
    21: 399,
}

META: dict[int, QuestionMeta] = {
    1: QuestionMeta("01-集合复数与逻辑", "集合复数与逻辑", "填空题", 1, ["集合补集"], ["集合运算"], "结论型", "(0,2)", []),
    2: QuestionMeta("01-集合复数与逻辑", "集合复数与逻辑", "填空题", 1, ["复数运算"], ["分母有理化"], "结论型", "z = 1 + i", []),
    3: QuestionMeta("02-函数与导数", "函数与导数", "填空题", 2, ["分段函数", "函数值"], ["分类讨论"], "结论型", "a = -8", ["注意分段条件"]),
    4: QuestionMeta("03-三角与向量", "三角与向量", "填空题", 1, ["解三角形", "余弦定理"], ["余弦定理"], "结论型", "c = 3", []),
    5: QuestionMeta("07-概率统计", "概率统计", "填空题", 2, ["正态分布"], ["对称性"], "结论型", "成绩不低于 120 分的人数约占 12.5%", []),
    6: QuestionMeta("02-函数与导数", "函数与导数", "填空题", 2, ["导数几何意义", "切线斜率"], ["求导"], "结论型", "切线斜率 k = 1/6", ["注意 OCR 原文把正号误识别成负号"]),
    7: QuestionMeta("07-概率统计", "概率统计", "填空题", 1, ["排列组合"], ["分类计数原理"], "结论型", "共有 108 种不同的面试方法", []),
    8: QuestionMeta("07-概率统计", "概率统计", "填空题", 2, ["古典概型"], ["分类计数"], "结论型", "概率为 1/23", ["注意 OCR 原文把正号误识别成负号"]),
    9: QuestionMeta("04-数列与不等式", "数列与不等式", "填空题", 2, ["数列求和"], ["裂项转化", "等比数列求和"], "结论型", "最小正整数 n = 11", []),
    10: QuestionMeta("06-解析几何", "解析几何", "填空题", 4, ["圆", "直线与圆位置关系"], ["对称变换", "距离公式"], "结论型", "m ∈ ((√3 - 1)/2, √2 - 1)", ["注意 OCR 原文多出负号"]),
    11: QuestionMeta("05-立体几何与空间向量", "立体几何与空间向量", "填空题", 3, ["空间轨迹", "向量数量积"], ["建系", "轨迹方程"], "结论型", "轨迹长度为 2√2π 米", []),
    12: QuestionMeta("08-综合与压轴", "综合与压轴", "填空题", 4, ["集合", "组合计数"], ["补集配对", "整体求和"], "结论型", "总和为 1013 × 2^2025", []),
    13: QuestionMeta("07-概率统计", "概率统计", "选择题", 1, ["回归分析"], ["统计概念辨析"], "选择题", "选 D", []),
    14: QuestionMeta("02-函数与导数", "函数与导数", "选择题", 2, ["对数函数性质"], ["构造", "基本不等式"], "选择题", "选 C", []),
    15: QuestionMeta("05-立体几何与空间向量", "立体几何与空间向量", "选择题", 3, ["空间向量", "共面判定"], ["线性表示"], "选择题", "选 B", []),
    16: QuestionMeta("02-函数与导数", "函数与导数", "选择题", 4, ["函数新定义", "函数性质"], ["定义推理", "分类讨论"], "选择题", "选 D", []),
    17: QuestionMeta("05-立体几何与空间向量", "立体几何与空间向量", "解答题", 4, ["面面垂直", "线面垂直", "几何体体积"], ["几何推理", "投影", "分割求体积"], "过程型", "(1) AB ⟂ 平面 PAD；(2) 体积为 2√3/3", []),
    18: QuestionMeta("03-三角与向量", "三角与向量", "解答题", 4, ["三角函数", "函数恒成立"], ["三角恒等变形", "导数/单调性"], "过程型", "(1) φ = π/2；(2) a ∈ (-∞, 5π/12 - √3/2]", []),
    19: QuestionMeta("07-概率统计", "概率统计", "解答题", 3, ["统计估计", "超几何分布", "二项分布"], ["分层抽样", "分布列", "比值法"], "过程型", "(1) 平均数 6.7；(2) P(X=1)=3/10, P(X=2)=6/10, P(X=3)=1/10, E(X)=9/5, D(X)=9/25；(3) k=5 时概率最大", []),
    20: QuestionMeta("06-解析几何", "解析几何", "解答题", 5, ["双曲线", "直线与圆锥曲线"], ["待定系数", "向量关系", "韦达定理"], "过程型", "(1) e = √5；(2) M=(2,3) 或 (5/4, 3√3/4)；(3) 倾斜角 ∈ (arctan(√2/2), arctan(√10/2))", []),
    21: QuestionMeta("02-函数与导数", "函数与导数", "解答题", 5, ["函数新定义", "Lipschitz 条件", "单调性"], ["定义证明", "极值分析", "反证法"], "证明型", "(1) f(x)=x²-x 属于 Ω，且 M(f,[0,1])=1/4；(2) f(1)=±1，f(x)=x 或 -x；(3) 结论成立", []),
}

SUBQUESTION_ANSWER_SUMMARY = {
    (17, 1): "AB ⟂ 平面 PAD",
    (17, 2): "多面体 PQABCD 的体积为 2√3/3",
    (18, 1): "φ = π/2",
    (18, 2): "a ∈ (-∞, 5π/12 - √3/2]",
    (19, 1): "平均甜度偏好分数为 6.7",
    (19, 2): "P(X=1)=3/10, P(X=2)=6/10, P(X=3)=1/10, E(X)=9/5, D(X)=9/25",
    (19, 3): "k = 5 时 P_k 最大",
    (20, 1): "双曲线离心率 e = √5",
    (20, 2): "M=(2,3) 或 (5/4, 3√3/4)",
    (20, 3): "倾斜角 ∈ (arctan(√2/2), arctan(√10/2))",
    (21, 1): "f(x)=x²-x 属于 Ω，且 M(f,[0,1])=1/4",
    (21, 2): "f(1)=±1，且 f(x)=x 或 -x",
    (21, 3): "结论成立",
}


def cleanup_question_line(qno: int, line: str) -> str:
    line = re.sub(r"\s+", " ", line).strip()
    fixes = {
        1: r"1. 已知全集 $U=\left(0,+\infty\right)$，集合 $A=[2,+\infty)$，则 $\bar{A}=$ ______.",
        2: r"2. 已知复数 $z$ 满足 $(1+\mathrm{i})z=2\mathrm{i}$，则 $z=$ ______.",
        3: r"3. 已知 $f(x)=\begin{cases}\sqrt[3]{x}, & x<0, \\ x+1, & x\ge 0. \end{cases}$ 若 $f(a)=-2$，则实数 $a$ 的值为 ______.",
        4: r"4. 在 $\triangle ABC$ 中，若 $a=7, b=8, \cos C=\frac{13}{14}$，则 $c=$ ______.",
        5: r"5. 某校高中三年级 600 名学生参加了区质量检测，已知数学检测成绩 $X$ 服从正态分布 $N(100,\sigma^2)$（试卷满分为 150 分）。统计结果显示，数学检测成绩介于 80 分到 120 分之间的人数为 450 名，则此次检测中成绩不低于 120 分的学生人数约为总人数的 ______（精确到 0.1%）。",
        6: r"6. 已知直线 $l$ 是曲线 $y=\frac{3}{x+1}+\ln x$ 在 $x=2$ 处的切线，则 $l$ 的斜率为 ______.",
        7: r"7. 从 4 名男生、3 名女生中选取 3 人，依次进行面试，其中恰好有 1 名女生，则有 ______ 种不同的面试方法。",
        8: r"8. 一个家庭有两个孩子，生肖均为十二生肖之一（等可能），已知其中一个孩子属马，则另一个孩子也属马的概率为 ______.",
        9: r"9. 已知数列 $\{a_n\}$ 的通项公式是 $a_n=2^{n-1}+1$，$S_n$ 为数列 $\{a_n\}$ 的前 $n$ 项和，则使不等式 $S_n>2026$ 成立的最小正整数 $n$ 的值为 ______.",
        10: r"10. 已知圆 $O$ 是圆心在原点的单位圆，弦 $AB$ 平行于 $x$ 轴，并将圆分为两段弧。将其中一段劣弧 $\overset{\frown}{AB}$ 沿弦 $AB$ 翻折后恰好经过圆心。若直线 $y=x+m$ 与翻折后得到的两段弧有四个不同的交点，则实数 $m$ 的取值范围为 ______.",
        11: r"11. 某光影科技实验室为长方体空间，底面是边长为 4 米的正方形，高为 3 米。为营造动态光影效果，在底面一个顶点处安装射灯 $A$，在与该顶点相对的侧棱上、距底面 1 米处安装射灯 $I$，两盏射灯的光束方向始终相互垂直，且它们的交汇点 $G$ 始终落在实验室天花板上，则交汇点 $G$ 形成的轨迹长度为 ______ 米。",
        12: r"12. 已知集合 $M$ 的元素均为正整数，定义集合 $M$ 的“变项和”为：将 $M$ 中每个元素 $m$ 都乘以 $(-1)^m$ 后再求和。若集合 $A=\{n\mid 1\le n\le 2026, n\in \mathbf{N}\}$，则集合 $A$ 的所有非空子集的“变项和”的总和为 ______.",
        13: r"13. 某校学生会体育部长依据本校高三男生的身高（单位：cm）与体重（单位：kg）的抽样数据，运用电子办公软件求出了“体重” $y$ 关于“身高” $x$ 的回归方程，则该回归方程（ ）",
        14: r"14. 已知实数 $a,b,c$ 满足 $a>b>1>c$，则下列结论一定正确的是（ ）",
        15: r"15. 已知 $\overrightarrow{e_1}$、$\overrightarrow{e_2}$ 与 $\overrightarrow{e_3}$ 是不共面的向量，则以下向量组中一定不共面的是（ ）",
        16: r"16. 定义在 $\mathbf{R}$ 上的非常值函数 $y=f(x)$，若存在一个非零常数 $T$，使得对任意 $x\in\mathbf{R}$，都有 $f(x+T)=T\cdot f(x)$ 成立，那么称函数 $y=f(x)$ 为 $T$ 函数。则下列说法正确的是（ ）",
    }
    return fixes.get(qno, line)


def load_lines() -> list[str]:
    return SOURCE.read_text().splitlines()


def get_question_block(lines: list[str], qno: int) -> list[str]:
    start = QUESTION_STARTS[qno] - 1
    next_start = QUESTION_STARTS.get(qno + 1, len(lines) + 1) - 1
    return lines[start:next_start]


def split_block(qno: int, block: list[str]) -> tuple[list[str], list[str]]:
    if qno <= 12:
        prompt = [cleanup_question_line(qno, block[0])]
        i = 1
        while i < len(block):
            line = block[i]
            if line.strip().startswith("!["):
                prompt.extend(["", line])
                i += 1
                continue
            if line.strip() == "":
                i += 1
                continue
            break
        solution = [line for line in block[i:] if line.strip() != ""]
        return prompt, solution

    if 13 <= qno <= 16:
        prompt: list[str] = [cleanup_question_line(qno, block[0])]
        i = 1
        while i < len(block):
            line = block[i]
            stripped = line.strip()
            if stripped.startswith("![") or re.match(r"^[ABCD]\.", stripped):
                if stripped:
                    prompt.append(stripped if stripped.startswith("![") else line)
                i += 1
                continue
            if stripped == "":
                i += 1
                continue
            break
        solution = [line for line in block[i:] if line.strip() != ""]
        return prompt, solution

    prompt: list[str] = [block[0]]
    seen_subquestions = set()
    i = 1
    for i in range(1, len(block)):
        stripped = block[i].strip()
        if re.match(r"^\((\d)\)", stripped):
            num = int(re.match(r"^\((\d)\)", stripped).group(1))
            if num in seen_subquestions:
                break
            seen_subquestions.add(num)
            prompt.append(block[i])
            continue
        if stripped.startswith("![") or stripped == "" or (seen_subquestions and not prompt[-1].startswith("![")):
            prompt.append(block[i])
            continue
        prompt.append(block[i])
    else:
        i = len(block)
    solution = [line for line in block[i:] if line.strip() != ""]
    prompt = trim_blank_lines(prompt)
    return prompt, solution


def trim_blank_lines(lines: list[str]) -> list[str]:
    start = 0
    end = len(lines)
    while start < end and not lines[start].strip():
        start += 1
    while end > start and not lines[end - 1].strip():
        end -= 1
    return lines[start:end]


def to_yaml_list(items: list[str], indent: int = 0) -> list[str]:
    prefix = " " * indent
    return [f"{prefix}- {item}" for item in items]


def make_frontmatter(
    *,
    title: str,
    function: str,
    meta: QuestionMeta,
    qno: int,
    has_figure: bool,
    subquestion_no: int | None = None,
    extra_tags: list[str] | None = None,
) -> str:
    tags = ["试卷切片", "高中数学", "二模", "浦东", meta.module_name]
    if extra_tags:
        tags.extend(extra_tags)
    lines = [
        "---",
        f'title: "{title}"',
        f"subject: {COMMON['subject']}",
        f"module: {meta.module_dir}",
        f"module_name: {meta.module_name}",
        f"function: {function}",
        f"exam: {COMMON['exam']}",
        f"year: {COMMON['year']}",
        f"class: {COMMON['class']}",
        f"district: {COMMON['district']}",
        f"question_no: {qno}",
    ]
    if subquestion_no is not None:
        lines.append(f"subquestion_no: {subquestion_no}")
    lines.extend(
        [
            f"question_type: {meta.question_type}",
            f"difficulty: {meta.difficulty}",
            f"answer_type: {meta.answer_type}",
            f"has_figure: {'true' if has_figure else 'false'}",
            f'source: "{COMMON["source"]}"',
            f'source_pdf: "{COMMON["source_pdf"]}"',
        ]
    )
    if meta.subtopics:
        lines.extend(["subtopics:", *to_yaml_list(meta.subtopics, 2)])
    else:
        lines.append("subtopics: []")
    if meta.methods:
        lines.extend(["methods:", *to_yaml_list(meta.methods, 2)])
    else:
        lines.append("methods: []")
    if meta.common_mistakes:
        lines.extend(["common_mistakes:", *to_yaml_list(meta.common_mistakes, 2)])
    else:
        lines.append("common_mistakes: []")
    lines.extend(["tags:", *to_yaml_list(tags, 2), "---"])
    return "\n".join(lines)


def write_markdown(path: Path, frontmatter: str, body_lines: list[str]) -> None:
    body = "\n".join(trim_blank_lines(body_lines)).strip()
    content = frontmatter + "\n\n" + body + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def normalize_image_refs(text: str, qno: int, module_dir: Path) -> str:
    images = re.findall(r"!\[([^\]]*)\]\((images/[^)]+)\)", text)
    for idx, (alt, rel) in enumerate(images, start=1):
        src = SOURCE.parent / rel
        ext = src.suffix.lower()
        dest_name = f"2026-26届-浦东-二模-Q{qno:02d}-fig{idx}{ext}"
        dest = module_dir / "images" / dest_name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        replacement = f"![{alt or f'Q{qno}题图'}](images/{dest_name})"
        text = text.replace(f"![{alt}]({rel})", replacement, 1)
    return text


def build_answer_body(qno: int, meta: QuestionMeta) -> list[str]:
    return [
        "## 最终答案",
        "",
        meta.answer_summary,
    ]


def extract_subquestion_blocks(lines: list[str]) -> dict[int, list[str]]:
    blocks: dict[int, list[str]] = {}
    current = None
    for line in lines:
        match = re.match(r"^\((\d)\)", line.strip())
        if match:
            current = int(match.group(1))
            blocks[current] = [line]
            continue
        if current is not None:
            blocks[current].append(line)
    return {k: trim_blank_lines(v) for k, v in blocks.items()}


def write_question_files(qno: int, prompt_lines: list[str], solution_lines: list[str]) -> None:
    meta = META[qno]
    module_dir = OUTPUT_ROOT / meta.module_dir
    has_figure = any("![" in line for line in prompt_lines + solution_lines)

    prompt_text = normalize_image_refs("\n".join(prompt_lines), qno, module_dir)
    solution_text = normalize_image_refs("\n".join(solution_lines), qno, module_dir)
    prompt_lines = prompt_text.splitlines()
    solution_lines = solution_text.splitlines()

    base = f"2026-26届-浦东-二模-Q{qno:02d}-{meta.module_name}"
    title = f"2026浦东二模第{qno}题"

    question_path = module_dir / f"{base}-题目.md"
    answer_path = module_dir / f"{base}-答案.md"
    analysis_path = module_dir / f"{base}-解析.md"

    write_markdown(
        question_path,
        make_frontmatter(title=title, function="题目", meta=meta, qno=qno, has_figure=has_figure),
        prompt_lines,
    )
    write_markdown(
        answer_path,
        make_frontmatter(title=title, function="答案", meta=meta, qno=qno, has_figure=has_figure),
        build_answer_body(qno, meta),
    )
    analysis_body = solution_lines or ["源文件未提供展开解析，仅保留答案结论。"]
    write_markdown(
        analysis_path,
        make_frontmatter(title=title, function="解析", meta=meta, qno=qno, has_figure=has_figure),
        analysis_body,
    )

    if qno >= 17:
        intro = []
        shared_media = [line for line in prompt_lines if line.strip().startswith("![")]
        question_blocks = extract_subquestion_blocks(prompt_lines)
        analysis_blocks = extract_subquestion_blocks(solution_lines)
        for line in prompt_lines:
            if re.match(r"^\((\d)\)", line.strip()):
                break
            intro.append(line)
        for sub_no, q_lines in question_blocks.items():
            sub_title = f"2026浦东二模第{qno}题第{sub_no}问"
            suffix = f"2026-26届-浦东-二模-Q{qno:02d}-{sub_no}问-{meta.module_name}"
            sub_question = intro + ([""] + shared_media if shared_media else []) + [""] + q_lines
            sub_analysis = analysis_blocks.get(sub_no, ["源文件未提供该小问单独解析。"])
            sub_answer_summary = SUBQUESTION_ANSWER_SUMMARY.get((qno, sub_no), "见解析")
            sub_has_figure = any("![" in line for line in sub_question + sub_analysis)
            sub_meta = QuestionMeta(
                module_dir=meta.module_dir,
                module_name=meta.module_name,
                question_type=meta.question_type,
                difficulty=meta.difficulty,
                subtopics=meta.subtopics,
                methods=meta.methods,
                answer_type=meta.answer_type,
                answer_summary=sub_answer_summary,
                common_mistakes=meta.common_mistakes,
            )
            write_markdown(
                module_dir / f"{suffix}-题目.md",
                make_frontmatter(
                    title=sub_title,
                    function="题目",
                    meta=sub_meta,
                    qno=qno,
                    has_figure=sub_has_figure,
                    subquestion_no=sub_no,
                ),
                sub_question,
            )
            write_markdown(
                module_dir / f"{suffix}-答案.md",
                make_frontmatter(
                    title=sub_title,
                    function="答案",
                    meta=sub_meta,
                    qno=qno,
                    has_figure=sub_has_figure,
                    subquestion_no=sub_no,
                ),
                ["## 最终答案", "", sub_answer_summary],
            )
            write_markdown(
                module_dir / f"{suffix}-解析.md",
                make_frontmatter(
                    title=sub_title,
                    function="解析",
                    meta=sub_meta,
                    qno=qno,
                    has_figure=sub_has_figure,
                    subquestion_no=sub_no,
                ),
                sub_analysis,
            )


def main() -> None:
    lines = load_lines()
    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    for qno in range(1, 22):
        block = get_question_block(lines, qno)
        prompt, solution = split_block(qno, block)
        write_question_files(qno, prompt, solution)

    manifest = OUTPUT_ROOT / "README.md"
    manifest.write_text(
        "# 浦东 2026 届二模数学试切样例\n\n"
        f"- 源文件：`{SOURCE}`\n"
        "- 处理方式：按题号切分，17-21 题额外切出小问层。\n"
        "- 注意：源文件存在少量 OCR 噪声，本次样例只做了题干最小清洗；解析部分仍保留原始提取内容。\n"
    )


if __name__ == "__main__":
    main()
