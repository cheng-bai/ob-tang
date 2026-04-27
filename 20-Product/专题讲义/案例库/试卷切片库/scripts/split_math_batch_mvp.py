#!/usr/bin/env python3
from __future__ import annotations

import json
import csv
import re
import shutil
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SourceCase:
    source_md: Path
    district: str
    exam: str
    year: int = 2026
    class_name: str = "26届"

    @property
    def paper_slug(self) -> str:
        return f"{self.year}-{self.class_name}-{self.district}-{self.exam}"

    @property
    def source_pdf(self) -> str:
        return self.source_md.name.replace("-dollar.md", ".pdf")


@dataclass(frozen=True)
class ModuleDef:
    module_dir: str
    module_name: str
    keywords: tuple[str, ...]


SOURCE_CASES = [
    SourceCase(
        source_md=Path(
            "/Users/tangchengbaiair/Downloads/mini-数学资料库/0-一模-二模-模考试卷-md版本/"
            "2026届嘉定区高三下二模数学试卷（解析版）/"
            "2026届嘉定区高三下二模数学试卷（解析版）-dollar.md"
        ),
        district="嘉定",
        exam="二模",
    ),
    SourceCase(
        source_md=Path(
            "/Users/tangchengbaiair/Downloads/mini-数学资料库/0-一模-二模-模考试卷-md版本/"
            "2026届奉贤区高三下二模数学试卷（解析版）/"
            "2026届奉贤区高三下二模数学试卷（解析版）-dollar.md"
        ),
        district="奉贤",
        exam="二模",
    ),
    SourceCase(
        source_md=Path(
            "/Users/tangchengbaiair/Downloads/mini-数学资料库/0-一模-二模-模考试卷-md版本/"
            "2026届崇明区高三下二模数学试卷（解析版）/"
            "2026届崇明区高三下二模数学试卷（解析版）-dollar.md"
        ),
        district="崇明",
        exam="二模",
    ),
    SourceCase(
        source_md=Path(
            "/Users/tangchengbaiair/Downloads/mini-数学资料库/0-一模-二模-模考试卷-md版本/"
            "2026届浦东新区高三下二模数学试卷（解析版）/"
            "2026届浦东新区高三下二模数学试卷（解析版）-dollar.md"
        ),
        district="浦东",
        exam="二模",
    ),
    SourceCase(
        source_md=Path(
            "/Users/tangchengbaiair/Downloads/mini-数学资料库/0-一模-二模-模考试卷-md版本/"
            "2026届金山区高三下二模数学试卷（解析版）/"
            "2026届金山区高三下二模数学试卷（解析版）-dollar.md"
        ),
        district="金山",
        exam="二模",
    ),
    SourceCase(
        source_md=Path(
            "/Users/tangchengbaiair/Downloads/mini-数学资料库/0-一模-二模-模考试卷-md版本/"
            "2026届闵行区高三下二模数学试卷（解析版）/"
            "2026届闵行区高三下二模数学试卷（解析版）-dollar.md"
        ),
        district="闵行",
        exam="二模",
    ),
]

OUTPUT_ROOT = Path(
    "/Users/tangchengbaiair/Downloads/试卷切片库/数学切片样例/2026-26届-六区二模-mvp"
)

MODULES = [
    ModuleDef("01-集合复数与逻辑", "集合复数与逻辑", ("集合", "命题", "充分", "必要", "复数", "虚数")),
    ModuleDef("02-函数与导数", "函数与导数", ("函数", "导数", "单调", "极值", "切线", "对数", "指数", "零点", "幂函数")),
    ModuleDef("03-三角与向量", "三角与向量", ("三角", "正弦", "余弦", "正切", "向量", "角", "终边", "解三角")),
    ModuleDef("04-数列与不等式", "数列与不等式", ("数列", "等差", "等比", "递推", "求和", "不等式", "归纳", "放缩")),
    ModuleDef("05-立体几何与空间向量", "立体几何与空间向量", ("立体", "空间", "线面", "平面", "棱", "锥", "四面体", "体积")),
    ModuleDef("06-解析几何", "解析几何", ("椭圆", "双曲线", "抛物线", "圆锥曲线", "离心率", "轨迹", "焦点", "弦长")),
    ModuleDef("07-概率统计", "概率统计", ("概率", "统计", "随机", "期望", "方差", "分布", "抽样", "回归", "排列", "组合")),
    ModuleDef("08-综合与压轴", "综合与压轴", ("综合", "压轴", "神经网络", "建模")),
]

FALLBACK_MODULE_BY_QNO = {
    1: "01-集合复数与逻辑",
    2: "01-集合复数与逻辑",
    3: "03-三角与向量",
    4: "02-函数与导数",
    5: "07-概率统计",
    6: "04-数列与不等式",
    7: "02-函数与导数",
    8: "03-三角与向量",
    9: "04-数列与不等式",
    10: "07-概率统计",
    11: "02-函数与导数",
    12: "08-综合与压轴",
    13: "07-概率统计",
    14: "02-函数与导数",
    15: "03-三角与向量",
    16: "02-函数与导数",
    17: "01-集合复数与逻辑",
    18: "05-立体几何与空间向量",
    19: "07-概率统计",
    20: "06-解析几何",
    21: "02-函数与导数",
}

MODULE_BY_DIR = {item.module_dir: item for item in MODULES}
QUESTION_RE = re.compile(r"^\s*(\d{1,2})\.\s+\S")
SUBQ_RE = re.compile(r"^\s*[（(](\d+)[)）]")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\((images/[^)]+)\)")


def trim_blank_lines(lines: list[str]) -> list[str]:
    start = 0
    end = len(lines)
    while start < end and not lines[start].strip():
        start += 1
    while end > start and not lines[end - 1].strip():
        end -= 1
    return lines[start:end]


def to_yaml_list(items: list[str], indent: int = 2) -> list[str]:
    return [f"{' ' * indent}- {item}" for item in items]


def qtype_by_qno(qno: int) -> str:
    if qno <= 12:
        return "填空题"
    if qno <= 16:
        return "单选题"
    return "解答题"


def difficulty_by_qno(qno: int) -> int:
    if qno <= 8:
        return 2
    if qno <= 16:
        return 3
    if qno <= 19:
        return 4
    return 5


def answer_type_by_qno(qno: int) -> str:
    if qno <= 16:
        return "结论型"
    if qno == 21:
        return "证明型"
    return "过程型"


def parse_question_blocks(lines: list[str]) -> dict[int, list[str]]:
    starts: dict[int, int] = {}
    expected = 1
    for idx, line in enumerate(lines):
        matched = QUESTION_RE.match(line)
        if not matched:
            continue
        qno = int(matched.group(1))
        if qno == expected and qno <= 21:
            starts[qno] = idx
            expected += 1
            if expected == 22:
                break
    if len(starts) != 21:
        raise ValueError(f"题号识别失败：只识别到 {len(starts)} 题")

    blocks: dict[int, list[str]] = {}
    for qno in range(1, 22):
        start = starts[qno]
        end = starts[qno + 1] if qno < 21 else len(lines)
        blocks[qno] = trim_blank_lines(lines[start:end])
    return blocks


def split_prompt_answer_analysis(block: list[str]) -> tuple[list[str], list[str], list[str]]:
    answer_idx = -1
    analysis_idx = -1
    for idx, line in enumerate(block):
        if answer_idx < 0 and "【答案】" in line:
            answer_idx = idx
            continue
        if analysis_idx < 0 and "【解析】" in line:
            analysis_idx = idx
            break

    if answer_idx < 0:
        return trim_blank_lines(block), ["源文件未识别到答案"], ["源文件未识别到解析"]

    prompt = trim_blank_lines(block[:answer_idx])

    answer_head = block[answer_idx].split("【答案】", 1)[1].strip()
    answer_tail = block[answer_idx + 1 : analysis_idx if analysis_idx >= 0 else len(block)]
    answer = trim_blank_lines(([answer_head] if answer_head else []) + answer_tail)
    answer_images = [line for line in answer if line.strip().startswith("![")]
    if answer_images:
        prompt = trim_blank_lines(prompt + [""] + answer_images)
        answer = [line for line in answer if not line.strip().startswith("![")]
    if not answer:
        answer = ["源文件答案为空"]

    analysis: list[str]
    if analysis_idx >= 0:
        analysis_head = block[analysis_idx].split("【解析】", 1)[1].strip()
        analysis = trim_blank_lines(([analysis_head] if analysis_head else []) + block[analysis_idx + 1 :])
    else:
        analysis = ["源文件未识别到解析"]
    if not analysis:
        analysis = ["源文件解析为空"]

    return prompt, answer, analysis


def classify_module(text: str, qno: int) -> tuple[ModuleDef, int, list[str], bool, str]:
    scores: dict[str, int] = {}
    for module in MODULES:
        score = 0
        for keyword in module.keywords:
            score += text.count(keyword)
        scores[module.module_dir] = score

    ranked = sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))
    best_dir, best_score = ranked[0]
    second_score = ranked[1][1] if len(ranked) > 1 else -1
    best_tie_dirs = [module_dir for module_dir, score in ranked if score == best_score]
    used_fallback = False

    if best_score == 0:
        fallback = FALLBACK_MODULE_BY_QNO.get(qno, "99-未归类待整理")
        used_fallback = True
        if fallback in MODULE_BY_DIR:
            best_dir = fallback
        else:
            best_dir = "99-未归类待整理"
            MODULE_BY_DIR[best_dir] = ModuleDef("99-未归类待整理", "未归类待整理", tuple())

    if len(best_tie_dirs) > 1 and not used_fallback:
        fallback = FALLBACK_MODULE_BY_QNO.get(qno)
        if fallback in best_tie_dirs:
            best_dir = fallback
        else:
            best_dir = sorted(best_tie_dirs)[0]

    def to_candidate(module_dir: str, score: int) -> str:
        module_name = MODULE_BY_DIR[module_dir].module_name if module_dir in MODULE_BY_DIR else module_dir
        return f"{module_dir}:{module_name}:{score}"

    candidate_modules = [to_candidate(module_dir, score) for module_dir, score in ranked[:3]]
    margin_small = second_score >= 0 and (best_score - second_score) <= 1

    review_reasons: list[str] = []
    if used_fallback:
        review_reasons.append("zero_score_fallback")
    if best_score <= 1:
        review_reasons.append("low_confidence")
    if margin_small:
        review_reasons.append("small_margin")
    if len(best_tie_dirs) > 1:
        review_reasons.append("tie_break")

    needs_review = len(review_reasons) > 0 or best_dir == "99-未归类待整理"
    review_reason = ",".join(review_reasons) if review_reasons else "none"
    return MODULE_BY_DIR[best_dir], best_score, candidate_modules, needs_review, review_reason


def normalize_image_refs(
    *,
    lines: list[str],
    qno: int,
    paper_slug: str,
    source_md: Path,
    module_dir: Path,
) -> tuple[list[str], int, list[str]]:
    text = "\n".join(lines)
    rel_to_dest: dict[str, str] = {}
    missing: list[str] = []
    image_counter = 0

    for matched in IMAGE_RE.finditer(text):
        alt, rel = matched.groups()
        if rel in rel_to_dest:
            dest_name = rel_to_dest[rel]
        else:
            src = source_md.parent / rel
            ext = src.suffix.lower() or ".png"
            image_counter += 1
            dest_name = f"{paper_slug}-Q{qno:02d}-fig{image_counter}{ext}"
            rel_to_dest[rel] = dest_name
            dest = module_dir / "images" / dest_name
            dest.parent.mkdir(parents=True, exist_ok=True)
            if src.exists():
                shutil.copy2(src, dest)
            else:
                missing.append(str(src))
        new_alt = alt if alt else f"Q{qno}题图"
        replacement = f"![{new_alt}](images/{dest_name})"
        text = text.replace(matched.group(0), replacement, 1)

    return text.splitlines(), len(rel_to_dest), missing


def extract_subquestion_blocks(lines: list[str]) -> dict[int, list[str]]:
    blocks: dict[int, list[str]] = {}
    current: int | None = None
    for line in lines:
        matched = SUBQ_RE.match(line)
        if matched:
            current = int(matched.group(1))
            blocks[current] = [line]
            continue
        if current is not None:
            blocks[current].append(line)
    return {k: trim_blank_lines(v) for k, v in blocks.items() if trim_blank_lines(v)}


def extract_subanswers(answer_lines: list[str]) -> dict[int, str]:
    text = " ".join(answer_lines).replace("；", ";").replace("，", ",")
    chunks = re.findall(r"[（(](\d+)[)）]\s*([^;]+)", text)
    result: dict[int, str] = {}
    for sub_no_str, sub_answer in chunks:
        result[int(sub_no_str)] = sub_answer.strip(" ;,.")
    return result


def make_frontmatter(
    *,
    title: str,
    function: str,
    module: ModuleDef,
    module_score: int,
    candidate_modules: list[str],
    needs_review: bool,
    review_reason: str,
    case: SourceCase,
    qno: int,
    has_figure: bool,
    subquestion_no: int | None = None,
) -> str:
    qtype = qtype_by_qno(qno)
    difficulty = difficulty_by_qno(qno)
    answer_type = answer_type_by_qno(qno)
    tags = ["试卷切片", "高中数学", case.exam, case.district, module.module_name]
    lines = [
        "---",
        f'title: "{title}"',
        "subject: 高中数学",
        f"module: {module.module_dir}",
        f"module_name: {module.module_name}",
        f"function: {function}",
        f"exam: {case.exam}",
        f"year: {case.year}",
        f"class: {case.class_name}",
        f"district: {case.district}",
        f"question_no: {qno}",
    ]
    if subquestion_no is not None:
        lines.append(f"subquestion_no: {subquestion_no}")
    lines.extend(
        [
            f"question_type: {qtype}",
            f"difficulty: {difficulty}",
            f"answer_type: {answer_type}",
            f"has_figure: {'true' if has_figure else 'false'}",
            f"module_confidence: {module_score}",
            f"needs_review: {'true' if needs_review else 'false'}",
            f'review_reason: "{review_reason}"',
            f'source: "{case.source_md.name}"',
            f'source_pdf: "{case.source_pdf}"',
            "secondary_candidates:",
            *to_yaml_list(candidate_modules),
            "subtopics: []",
            "methods: []",
            "common_mistakes: []",
            "tags:",
            *to_yaml_list(tags),
            "---",
        ]
    )
    return "\n".join(lines)


def write_markdown(path: Path, frontmatter: str, body_lines: list[str]) -> None:
    body = "\n".join(trim_blank_lines(body_lines)).strip()
    content = f"{frontmatter}\n\n{body}\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def process_case(case: SourceCase) -> dict[str, object]:
    lines = case.source_md.read_text().splitlines()
    question_blocks = parse_question_blocks(lines)
    case_output_root = OUTPUT_ROOT / case.paper_slug
    case_output_root.mkdir(parents=True, exist_ok=True)

    stats = {
        "paper_slug": case.paper_slug,
        "source": str(case.source_md),
        "questions": 0,
        "subquestions": 0,
        "files_written": 0,
        "images_copied": 0,
        "missing_images": [],
        "module_counts": {},
        "needs_review_count": 0,
        "review_items": [],
    }

    for qno in range(1, 22):
        prompt_lines, answer_lines, analysis_lines = split_prompt_answer_analysis(question_blocks[qno])
        module_text = "\n".join(prompt_lines + answer_lines + analysis_lines)
        module, module_score, candidate_modules, needs_review, review_reason = classify_module(module_text, qno)

        module_dir = case_output_root / module.module_dir
        stats["module_counts"][module.module_dir] = stats["module_counts"].get(module.module_dir, 0) + 1

        prompt_lines, prompt_img_count, prompt_missing = normalize_image_refs(
            lines=prompt_lines,
            qno=qno,
            paper_slug=case.paper_slug,
            source_md=case.source_md,
            module_dir=module_dir,
        )
        analysis_lines, analysis_img_count, analysis_missing = normalize_image_refs(
            lines=analysis_lines,
            qno=qno,
            paper_slug=case.paper_slug,
            source_md=case.source_md,
            module_dir=module_dir,
        )
        stats["images_copied"] += prompt_img_count + analysis_img_count
        stats["missing_images"].extend(prompt_missing + analysis_missing)

        has_figure = (prompt_img_count + analysis_img_count) > 0
        base = f"{case.paper_slug}-Q{qno:02d}-{module.module_name}"
        title = f"{case.year}{case.district}{case.exam}第{qno}题"

        question_path = module_dir / f"{base}-题目.md"
        answer_path = module_dir / f"{base}-答案.md"
        analysis_path = module_dir / f"{base}-解析.md"

        write_markdown(
            question_path,
            make_frontmatter(
                title=title,
                function="题目",
                module=module,
                module_score=module_score,
                candidate_modules=candidate_modules,
                needs_review=needs_review,
                review_reason=review_reason,
                case=case,
                qno=qno,
                has_figure=has_figure,
            ),
            prompt_lines,
        )
        write_markdown(
            answer_path,
            make_frontmatter(
                title=title,
                function="答案",
                module=module,
                module_score=module_score,
                candidate_modules=candidate_modules,
                needs_review=needs_review,
                review_reason=review_reason,
                case=case,
                qno=qno,
                has_figure=has_figure,
            ),
            ["## 最终答案", "", *answer_lines],
        )
        write_markdown(
            analysis_path,
            make_frontmatter(
                title=title,
                function="解析",
                module=module,
                module_score=module_score,
                candidate_modules=candidate_modules,
                needs_review=needs_review,
                review_reason=review_reason,
                case=case,
                qno=qno,
                has_figure=has_figure,
            ),
            analysis_lines,
        )
        stats["questions"] += 1
        stats["files_written"] += 3

        if needs_review:
            stats["needs_review_count"] += 1
            stats["review_items"].append(
                {
                    "paper_slug": case.paper_slug,
                    "district": case.district,
                    "question_no": qno,
                    "module": module.module_dir,
                    "module_name": module.module_name,
                    "module_confidence": module_score,
                    "review_reason": review_reason,
                    "candidate_modules": candidate_modules,
                    "question_file": str(question_path),
                    "source_md": str(case.source_md),
                    "prompt_preview": prompt_lines[0].strip()[:120] if prompt_lines else "",
                }
            )

        if qno < 17:
            continue

        prompt_sub_blocks = extract_subquestion_blocks(prompt_lines)
        analysis_sub_blocks = extract_subquestion_blocks(analysis_lines)
        sub_answers = extract_subanswers(answer_lines)
        if not prompt_sub_blocks:
            continue

        intro_lines: list[str] = []
        for line in prompt_lines:
            if SUBQ_RE.match(line):
                break
            intro_lines.append(line)
        intro_lines = trim_blank_lines(intro_lines)
        shared_images = [line for line in intro_lines if line.strip().startswith("![")]

        for sub_no, sub_prompt in prompt_sub_blocks.items():
            sub_title = f"{case.year}{case.district}{case.exam}第{qno}题第{sub_no}问"
            sub_base = f"{case.paper_slug}-Q{qno:02d}-{sub_no}问-{module.module_name}"
            sub_analysis = analysis_sub_blocks.get(sub_no, ["源文件未单独标注该小问解析"])
            sub_answer = sub_answers.get(sub_no, "见题目级答案")
            merged_prompt = trim_blank_lines(intro_lines + ([""] + shared_images if shared_images else []) + [""] + sub_prompt)

            write_markdown(
                module_dir / f"{sub_base}-题目.md",
                make_frontmatter(
                    title=sub_title,
                    function="题目",
                    module=module,
                    module_score=module_score,
                    candidate_modules=candidate_modules,
                    needs_review=needs_review,
                    review_reason=review_reason,
                    case=case,
                    qno=qno,
                    has_figure=has_figure,
                    subquestion_no=sub_no,
                ),
                merged_prompt,
            )
            write_markdown(
                module_dir / f"{sub_base}-答案.md",
                make_frontmatter(
                    title=sub_title,
                    function="答案",
                    module=module,
                    module_score=module_score,
                    candidate_modules=candidate_modules,
                    needs_review=needs_review,
                    review_reason=review_reason,
                    case=case,
                    qno=qno,
                    has_figure=has_figure,
                    subquestion_no=sub_no,
                ),
                ["## 最终答案", "", sub_answer],
            )
            write_markdown(
                module_dir / f"{sub_base}-解析.md",
                make_frontmatter(
                    title=sub_title,
                    function="解析",
                    module=module,
                    module_score=module_score,
                    candidate_modules=candidate_modules,
                    needs_review=needs_review,
                    review_reason=review_reason,
                    case=case,
                    qno=qno,
                    has_figure=has_figure,
                    subquestion_no=sub_no,
                ),
                sub_analysis,
            )
            stats["subquestions"] += 1
            stats["files_written"] += 3

    readme_lines = [
        f"# {case.paper_slug} 切片结果",
        "",
        f"- 源文件: `{case.source_md}`",
        f"- 题目数量: {stats['questions']}",
        f"- 小问数量: {stats['subquestions']}",
        f"- 输出文件: {stats['files_written']}",
        f"- 图片拷贝: {stats['images_copied']}",
        f"- 缺失图片: {len(stats['missing_images'])}",
        f"- 待复核题目: {stats['needs_review_count']}",
        "",
        "## 模块分布",
        "",
    ]
    for module_dir in sorted(stats["module_counts"].keys()):
        readme_lines.append(f"- {module_dir}: {stats['module_counts'][module_dir]} 题")
    (case_output_root / "README.md").write_text("\n".join(readme_lines) + "\n")
    return stats


def main() -> None:
    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    all_stats: list[dict[str, object]] = []
    for case in SOURCE_CASES:
        if not case.source_md.exists():
            raise FileNotFoundError(f"源文件不存在: {case.source_md}")
        all_stats.append(process_case(case))

    total_questions = sum(item["questions"] for item in all_stats)
    total_subquestions = sum(item["subquestions"] for item in all_stats)
    total_files = sum(item["files_written"] for item in all_stats)
    total_images = sum(item["images_copied"] for item in all_stats)
    total_missing_images = sum(len(item["missing_images"]) for item in all_stats)
    total_needs_review = sum(item["needs_review_count"] for item in all_stats)
    review_items: list[dict[str, object]] = []
    for item in all_stats:
        review_items.extend(item["review_items"])

    review_csv_path = OUTPUT_ROOT / "needs_review.csv"
    review_md_path = OUTPUT_ROOT / "needs_review.md"

    with review_csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "paper_slug",
                "district",
                "question_no",
                "module",
                "module_name",
                "module_confidence",
                "review_reason",
                "candidate_1",
                "candidate_2",
                "candidate_3",
                "question_file",
                "source_md",
                "prompt_preview",
            ],
        )
        writer.writeheader()
        for item in sorted(review_items, key=lambda x: (x["paper_slug"], x["question_no"])):
            candidates = item.get("candidate_modules", [])
            writer.writerow(
                {
                    "paper_slug": item["paper_slug"],
                    "district": item["district"],
                    "question_no": item["question_no"],
                    "module": item["module"],
                    "module_name": item["module_name"],
                    "module_confidence": item["module_confidence"],
                    "review_reason": item["review_reason"],
                    "candidate_1": candidates[0] if len(candidates) > 0 else "",
                    "candidate_2": candidates[1] if len(candidates) > 1 else "",
                    "candidate_3": candidates[2] if len(candidates) > 2 else "",
                    "question_file": item["question_file"],
                    "source_md": item["source_md"],
                    "prompt_preview": item["prompt_preview"],
                }
            )

    reason_counts: dict[str, int] = {}
    for item in review_items:
        for reason in str(item["review_reason"]).split(","):
            reason = reason.strip()
            if not reason:
                continue
            reason_counts[reason] = reason_counts.get(reason, 0) + 1

    review_lines = [
        "# 待复核清单（自动生成）",
        "",
        f"- 总待复核题目: {len(review_items)}",
        f"- 清单 CSV: `{review_csv_path}`",
        "",
        "## 原因分布",
        "",
    ]
    for reason, count in sorted(reason_counts.items(), key=lambda kv: (-kv[1], kv[0])):
        review_lines.append(f"- {reason}: {count}")

    review_lines.extend(
        [
            "",
            "## 题目明细",
            "",
            "| 试卷 | 题号 | 当前模块 | 置信度 | 复核原因 | 候选模块Top3 | 题目文件 |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for item in sorted(review_items, key=lambda x: (x["paper_slug"], x["question_no"])):
        cands = "<br>".join(item["candidate_modules"])
        review_lines.append(
            f"| {item['paper_slug']} | Q{int(item['question_no']):02d} | "
            f"{item['module_name']} | {item['module_confidence']} | {item['review_reason']} | "
            f"{cands} | {item['question_file']} |"
        )
    review_md_path.write_text("\n".join(review_lines) + "\n")

    summary = {
        "output_root": str(OUTPUT_ROOT),
        "cases": all_stats,
        "total_questions": total_questions,
        "total_subquestions": total_subquestions,
        "total_files_written": total_files,
        "total_images_copied": total_images,
        "total_missing_images": total_missing_images,
        "total_needs_review": total_needs_review,
        "needs_review_csv": str(review_csv_path),
        "needs_review_md": str(review_md_path),
    }
    (OUTPUT_ROOT / "manifest.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")

    report_lines = [
        "# 2026 六区二模数学切片 MVP 报告",
        "",
        f"- 输出目录: `{OUTPUT_ROOT}`",
        f"- 试卷数量: {len(all_stats)}",
        f"- 题目数量: {total_questions}",
        f"- 小问数量: {total_subquestions}",
        f"- 输出文件: {total_files}",
        f"- 图片拷贝: {total_images}",
        f"- 缺失图片: {total_missing_images}",
        f"- 待复核题目: {total_needs_review}",
        f"- 复核清单: `{review_md_path}`",
        "",
        "## 分卷统计",
        "",
    ]
    for item in all_stats:
        report_lines.append(
            f"- {item['paper_slug']}: 题目 {item['questions']}，小问 {item['subquestions']}，"
            f"文件 {item['files_written']}，图片 {item['images_copied']}，缺失图 {len(item['missing_images'])}，"
            f"待复核 {item['needs_review_count']}"
        )
    (OUTPUT_ROOT / "README.md").write_text("\n".join(report_lines) + "\n")


if __name__ == "__main__":
    main()
