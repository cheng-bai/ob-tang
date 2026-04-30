#!/usr/bin/env python3
"""
虹口区高三二模数学试卷 MD 拆分工具 v4
生成：学生版、教师版、题型拆分版
教师版答案区带【考点】标注
"""

import re
import os

SRC_DIR = "/Users/tangchengbaiair/Library/Mobile Documents/com~apple~CloudDocs/ipad 中转/公式识别的 pdf 资料/2025-2026学年虹口区高三二模数学试卷及解析.pdf_os_d7obidc91nqc738jp340"
SRC_MD = os.path.join(SRC_DIR, "2025-2026学年虹口区高三二模数学试卷及解析-dollar.md")
OUT_DIR = "/Users/tangchengbaiair/Downloads/latex-maki-math/虹口区高三二模-拆分版"

with open(SRC_MD, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

# ========== 第一步：分离题目和答案解析 ==========
ref_line_idx = None
for i, line in enumerate(lines):
    if '参考答案及解析' in line:
        ref_line_idx = i
        break

print(f"参考答案起始行: 第 {ref_line_idx + 1} 行")

questions_part = '\n'.join(lines[:ref_line_idx]).strip()
answers_lines = lines[ref_line_idx:]

# 去掉开头的"参考答案及解析:"和后面重复的章节标题
answers_lines_clean = []
for line in answers_lines:
    if '参考答案及解析' in line:
        continue
    if line.strip().startswith('## 二、选择题') or line.strip().startswith('## 三、解答题'):
        continue
    answers_lines_clean.append(line)

answers_part = '\n'.join(answers_lines_clean).strip()

# ========== 第二步：提取题目 ==========
question_pattern = r'^(\d{1,2})[.、]'
question_positions = []

for m in re.finditer(question_pattern, questions_part, re.MULTILINE):
    q_num = int(m.group(1))
    if 1 <= q_num <= 21:
        line_text = questions_part[m.start():m.start()+50]
        if '本试卷' in line_text or '本考试' in line_text:
            continue
        if not any(p[0] == q_num for p in question_positions):
            question_positions.append((q_num, m.start()))

questions = {}
for i, (q_num, start) in enumerate(question_positions):
    end = question_positions[i + 1][1] if i + 1 < len(question_positions) else len(questions_part)
    questions[q_num] = questions_part[start:end].strip()

print(f"提取 {len(questions)} 道题目: {sorted(questions.keys())}")

# ========== 第三步：提取答案解析 ==========
answer_blocks = {}
current_q_num = None
current_answer_lines = []
in_answer = False

for line in answers_part.split('\n'):
    q_match = re.match(r'^(\d{1,2})[.、]', line)
    if q_match:
        q_num = int(q_match.group(1))
        if 1 <= q_num <= 21:
            if current_q_num is not None and current_answer_lines:
                answer_blocks[current_q_num] = '\n'.join(current_answer_lines).strip()
            current_q_num = q_num
            current_answer_lines = []
            if '【答案】' in line:
                in_answer = True
                answer_start = line.find('【答案】')
                current_answer_lines.append(line[answer_start:])
            else:
                in_answer = False
            continue

    if line.strip().startswith('【答案】') or line.strip().startswith('【解析】') or \
       line.strip().startswith('【分析】') or line.strip().startswith('【详解】') or \
       line.strip().startswith('【小问') or line.strip().startswith('【点睛】'):
        in_answer = True

    if in_answer and current_q_num is not None:
        current_answer_lines.append(line)

if current_q_num is not None and current_answer_lines:
    answer_blocks[current_q_num] = '\n'.join(current_answer_lines).strip()

print(f"提取 {len(answer_blocks)} 个答案解析: {sorted(answer_blocks.keys())}")

# ========== 第四步：配置 ==========
medium_hard = {7, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 20, 21}

knowledge_points = {
    1: "考点：集合运算、分式不等式",
    2: "考点：棱柱体积公式",
    3: "考点：二项分布的方差",
    4: "考点：充分必要条件、绝对值不等式",
    5: "考点：独立性检验、假设检验",
    6: "考点：向量数量积、余弦定理",
    7: "考点：二项式定理、排列组合、随机变量期望",
    8: "考点：正四棱台、异面直线所成角、二面角",
    9: "考点：复数运算、复数模的几何意义",
    10: "考点：抛物线定义、余弦定理、基本不等式",
    11: "考点：解三角形、正弦定理、余弦定理、近似计算",
    12: "考点：空间向量、直线与圆的位置关系",
    13: "考点：双曲线的渐近线",
    14: "考点：事件独立性、条件概率",
    15: "考点：等差数列、三角函数性质、数列综合",
    16: "考点：函数性质、集合、逻辑推理",
    17: "考点：圆锥的侧面积、空间向量、线面角、线线垂直",
    18: "考点：正态分布、古典概型、线性回归、数列递推",
    19: "考点：指数函数、不等式求解、函数奇偶性与单调性",
    20: "考点：椭圆离心率、向量平行、直线与椭圆位置关系、圆",
    21: "考点：新定义函数、单射性质、分类讨论、函数方程",
}

def format_answer_block(q_num, raw_answer):
    """
    将原始答案文本格式化为标准教师版格式：
    **【参考答案与解析】**
    【考点】：XXX
    【答案】XXX
    【解析】
    【分析】XXX
    【详解】XXX
    """
    kp = knowledge_points.get(q_num, "").replace("考点：", "")
    
    # 分离各部分
    answer_text = ""
    analysis_text = ""
    detail_text = ""
    
    # 找到第一个【解析】的位置
    parse_idx = raw_answer.find('【解析】')
    if parse_idx != -1:
        answer_part = raw_answer[:parse_idx].strip()
        rest = raw_answer[parse_idx:]
        
        # 提取【分析】
        analysis_idx = rest.find('【分析】')
        if analysis_idx != -1:
            rest_after_analysis = rest[analysis_idx:]
            # 如果还有【详解】，进一步分离
            detail_idx = rest_after_analysis.find('【详解】')
            if detail_idx != -1:
                analysis_text = rest_after_analysis[:detail_idx]
                detail_text = rest_after_analysis[detail_idx:]
            else:
                analysis_text = rest_after_analysis
                detail_text = ""
        else:
            analysis_text = ""
            detail_text = rest
        
        # 提取答案文本（保留【答案】标签）
        answer_text = answer_part.strip()
    else:
        # 没有【解析】部分，整段就是答案
        answer_text = raw_answer.strip()
        analysis_text = ""
        detail_text = ""
    
    # 组装标准格式
    parts = []
    parts.append("**【参考答案与解析】**\n")
    if kp:
        parts.append(f"【考点】：{kp}\n")
    if answer_text:
        parts.append(f"{answer_text}\n")
    if analysis_text or detail_text:
        parts.append("【解析】\n")
    if analysis_text:
        parts.append(f"{analysis_text}\n")
    if detail_text:
        parts.append(f"{detail_text}\n")
    
    return '\n'.join(parts)

# 格式化所有答案块
for q_num in answer_blocks:
    answer_blocks[q_num] = format_answer_block(q_num, answer_blocks[q_num])

# ========== 第五步：生成学生版 ==========
def generate_student_version():
    out = []
    out.append("# 2025-2026学年虹口区高三二模数学试卷（学生版）\n")
    out.append("**考试时间：120分钟  满分：150分**\n---\n")
    out.append("### 考生注意:\n")
    out.append("1. 本试卷共 4 页, 21 道试题, 满分 150 分, 考试时间 120 分钟.\n")
    out.append("2. 作答必须涂 (选择题) 或写 (非选择题) 在答题纸上的相应位置，在试卷上作答一律不得分.\n")
    out.append("---\n\n")

    # 填空题
    out.append("## 一、填空题\n")
    out.append("(本大题共有 12 题，满分 54 分，第 1-6 题每题 4 分，第 7-12 题每题 5 分)\n\n")
    for q_num in range(1, 13):
        if q_num in questions:
            out.append(questions[q_num])
            out.append("\n\n")
            if q_num in medium_hard:
                out.append("\n<br><br><br><br><br>\n\n")

    # 选择题
    out.append("---\n\n## 二、选择题\n")
    out.append("(本大题共有 4 题, 满分 18 分, 第 13-14 题每题 4 分, 第 15-16 题每题 5 分)\n\n")
    for q_num in range(13, 17):
        if q_num in questions:
            out.append(questions[q_num])
            out.append("\n\n")
            if q_num in medium_hard:
                out.append("\n<br><br><br><br><br>\n\n")

    # 解答题
    out.append("---\n\n## 三、解答题\n")
    out.append("(本大题共有 5 题，满分 78 分)\n\n")
    for q_num in range(17, 22):
        if q_num in questions:
            out.append(questions[q_num])
            out.append("\n\n<br><br><br><br><br><br><br><br>\n\n")

    return "\n".join(out)

# ========== 第六步：生成教师版 ==========
def generate_teacher_version():
    out = []
    out.append("# 2025-2026学年虹口区高三二模数学试卷（教师版）\n")
    out.append("**含参考答案及详细解析**\n---\n\n")

    for q_num in range(1, 22):
        if q_num in questions:
            out.append(f"## 第 {q_num} 题\n\n")
            out.append(questions[q_num])
            out.append("\n\n")
            if q_num in answer_blocks:
                out.append(answer_blocks[q_num])
                out.append("\n\n---\n\n")

    return "\n".join(out)

# ========== 第七步：生成题型拆分版 ==========
def generate_split_version():
    sections = {
        "01-填空题": (list(range(1, 13)), "一、填空题", "(本大题共有 12 题，满分 54 分)"),
        "02-选择题": (list(range(13, 17)), "二、选择题", "(本大题共有 4 题, 满分 18 分)"),
        "03-基础解答题": ([17, 18, 19], "三、基础解答题", "(立体几何·概率统计·函数基础)"),
        "04-解析几何": ([20], "四、解析几何", "(椭圆综合)"),
        "05-压轴新定义": ([21], "五、压轴新定义", "(函数性质综合)"),
    }

    results = {}
    for section_name, (q_nums, section_title, section_desc) in sections.items():
        out = []
        out.append(f"# 2025-2026学年虹口区高三二模数学试卷\n## {section_title}\n{section_desc}\n\n")
        out.append("**考试时间：120分钟  满分：150分**\n\n")
        if section_name == "01-填空题":
            out.append("---\n### 考生注意:\n")
            out.append("1. 本试卷共 4 页, 21 道试题, 满分 150 分, 考试时间 120 分钟.\n")
            out.append("2. 作答必须写在答题纸上的相应位置.\n---\n\n")

        for q_num in q_nums:
            if q_num in questions:
                out.append(questions[q_num])
                out.append("\n\n")
                if q_num in medium_hard:
                    h = "<br><br><br><br><br><br><br><br>" if q_num >= 17 else "<br><br><br><br><br>"
                    out.append(f"\n{h}\n\n")
                if q_num in answer_blocks:
                    out.append("---\n")
                    out.append(answer_blocks[q_num])
                    out.append("\n")

        results[section_name] = "\n".join(out)

    return results

# ========== 执行 ==========
print("\n=== 生成学生版 ===")
student_md = generate_student_version()
with open(os.path.join(OUT_DIR, "学生版-2025-2026学年虹口区高三二模数学.md"), 'w', encoding='utf-8') as f:
    f.write(student_md)
print(f"已保存: 学生版 ({len(student_md)} 字符)")

print("\n=== 生成教师版 ===")
teacher_md = generate_teacher_version()
with open(os.path.join(OUT_DIR, "教师版-2025-2026学年虹口区高三二模数学.md"), 'w', encoding='utf-8') as f:
    f.write(teacher_md)
print(f"已保存: 教师版 ({len(teacher_md)} 字符)")

print("\n=== 生成题型拆分版 ===")
split_results = generate_split_version()
for section_name, content in split_results.items():
    path = os.path.join(OUT_DIR, f"{section_name}-2025-2026学年虹口区高三二模数学.md")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"已保存: {section_name} ({len(content)} 字符)")

print("\n✅ 全部生成完成！")
