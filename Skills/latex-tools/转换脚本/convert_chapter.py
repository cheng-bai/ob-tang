#!/usr/bin/env python3
"""
教材 MD 转 LaTeX - 通用转换脚本
支持任意章节转换
"""

import re
import os
import sys
from pathlib import Path


def convert_md_to_latex_ultimate(md_path, template_path, output_path, chapter_num, chapter_title):
    """
    终极完美版本 V3 - 通用版
    """
    
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    
    doc_start = template.find('\\begin{document}')
    preamble = template[:doc_start] if doc_start > 0 else template
    
    # 在导言区末尾添加 solution 环境定义
    solution_env = r"""
% ======================================
%  新增环境定义（题目解答分离）- 优化版
% ======================================

% 解答盒子 - 浅蓝色，更紧凑
\newtcolorbox{solutionBox}[1][]{
    enhanced, colback=ExBg!50, colframe=ExColor!70, 
    boxrule=0.4pt, arc=2pt, left=2.5mm, right=2.5mm, top=1.5mm, bottom=1.5mm,
    fontupper=\small, 
    before skip=0.5em, after skip=0.5em,
    #1
}

% 思路点拨盒子 - 浅黄色，更醒目
\newtcolorbox{hintBox}[1][]{
    enhanced, colback=DefBg!80, colframe=DefColor!70, 
    boxrule=0.4pt, arc=2pt, left=2.5mm, right=2.5mm, top=1.5mm, bottom=1.5mm,
    fontupper=\small\color{DefColor!80!black},
    before skip=0.5em, after skip=0.5em,
    #1
}

% 解答环境
\newenvironment{solution}{\begin{solutionBox}}{\end{solutionBox}}

% 思路点拨环境  
\newenvironment{hint}{\begin{hintBox}\textbf{【思路点拨】}~}{\end{hintBox}}

% 优化 example 环境间距
\tcbset{
    exBox/.append style={
        before skip=0.8em, after skip=0.5em
    }
}

"""
    
    # 在导言区末尾（\begin{document}之前）插入新环境定义
    preamble = preamble.rstrip() + '\n\n' + solution_env + '\n'
    
    lines = content.split('\n')
    
    # 预处理：合并 $$ 包裹的多行公式
    processed_lines = []
    i = 0
    in_display_math = False
    math_buffer = []
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        if stripped == '$$':
            if in_display_math:
                # 结束数学环境
                math_buffer.append(line)
                processed_lines.append('\n'.join(math_buffer))
                math_buffer = []
                in_display_math = False
            else:
                # 开始数学环境
                in_display_math = True
                math_buffer = [line]
            i += 1
        elif in_display_math:
            math_buffer.append(line)
            i += 1
        else:
            processed_lines.append(line)
            i += 1
    
    # 如果有未闭合的数学环境，作为普通行添加
    if math_buffer:
        processed_lines.extend(math_buffer)
    
    lines = processed_lines
    latex_lines = []
    
    # 状态变量
    in_example = False
    in_solution = False
    in_exercise = False
    example_problem = []
    example_solution = []
    exercise_content = []
    current_exercise_title = ""
    skip_first_line = True
    pending_separator = False
    
    def close_example():
        """关闭例题环境，题目和解答分离"""
        nonlocal in_example, in_solution, example_problem, example_solution
        if in_example and example_problem:
            # 过滤掉空行和分隔符
            filtered_problem = [l for l in example_problem if l.strip() and l.strip() != '---']
            if filtered_problem:
                # 例题题目盒子
                latex_lines.append("\\begin{example}")
                latex_lines.append("\\textbf{【题目】}\\par\\vspace{0.3em}")
                formatted_problem = format_content_with_line_breaks(filtered_problem, is_problem=True)
                latex_lines.extend(formatted_problem)
                latex_lines.append("\\end{example}")
                latex_lines.append("")
                
                # 例题解答盒子（如果有解答）
                if example_solution:
                    filtered_solution = [l for l in example_solution if l.strip()]
                    if filtered_solution:
                        # 确保解答以"解"开头
                        first_line = filtered_solution[0]
                        if not first_line.startswith('解') and not first_line.startswith('\\textbf{解'):
                            # 添加解标记
                            if first_line.startswith('证明'):
                                filtered_solution[0] = f"\\textbf{{{first_line[:2]}}} {first_line[2:]}"
                            else:
                                filtered_solution.insert(0, "\\textbf{解}")
                        
                        latex_lines.append("\\begin{solution}")
                        formatted_solution = format_content_with_line_breaks(filtered_solution, is_solution=True)
                        latex_lines.extend(formatted_solution)
                        latex_lines.append("\\end{solution}")
                        latex_lines.append("")
                        
                        # AI 思路点拨
                        latex_lines.append("\\begin{hint}")
                        latex_lines.append(generate_ai_hint(filtered_problem, filtered_solution))
                        latex_lines.append("\\end{hint}")
                        latex_lines.append("")
        
        in_example = False
        in_solution = False
        example_problem = []
        example_solution = []
    
    def close_exercise():
        """关闭练习环境"""
        nonlocal in_exercise, exercise_content, current_exercise_title
        if in_exercise and exercise_content:
            filtered_content = [l for l in exercise_content if l.strip() and l.strip() != '---']
            if filtered_content:
                latex_lines.append(f"\\begin{{exercise}}")
                latex_lines.append(f"\\textbf{{{current_exercise_title}}}\\par\\vspace{{0.5em}}")
                formatted_content = format_exercise_content(filtered_content)
                latex_lines.extend(formatted_content)
                latex_lines.append("\\end{exercise}")
                latex_lines.append("")
        
        in_exercise = False
        exercise_content = []
        current_exercise_title = ""
    
    def format_content_with_line_breaks(content_list, is_problem=False, is_solution=False):
        """格式化内容，确保换行"""
        formatted = []
        for line in content_list:
            stripped = line.strip()
            if not stripped or stripped == '---':
                continue
            
            # 处理题目编号 (1) (2) (3) (4)
            if re.match(r'^[(（][\d一二三四五六七八九十]+[)）]', stripped):
                line = re.sub(r'^([(（][\d一二三四五六七八九十]+[)）])', r'\\par\n\1 ', line)
            # 处理解答步骤编号
            elif is_solution and re.match(r'^解[（(][\d]+[)）]', stripped):
                line = re.sub(r'^(解[（(][\d]+[)）])', r'\\textbf{\1} ', line)
            # 处理选择题选项 A. B. C. D.
            elif re.match(r'^[ABCDabcd][\.．]', stripped):
                line = re.sub(r'^([ABCDabcd])[\.．]', r'\\par\n\\textbf{\1.} ', line)
            
            formatted.append(line)
        return formatted
    
    def format_exercise_content(content_list):
        """格式化习题内容，优化选择题排版"""
        formatted = []
        current_item = []
        item_number = 0
        
        for line in content_list:
            stripped = line.strip()
            if not stripped or stripped == '---':
                continue
            
            # 检查是否是新题目的开始（1. 2. 3. 等）
            new_item_match = re.match(r'^([\d]+)[\.．]\s*(.+)', stripped)
            if new_item_match:
                # 保存之前的题目
                if current_item:
                    formatted.extend(format_single_exercise_item(current_item, item_number))
                    formatted.append("\\par\\vspace{0.8em}")
                
                item_number = int(new_item_match.group(1))
                current_item = [new_item_match.group(2)]
            else:
                # 继续当前题目
                current_item.append(line)
        
        # 保存最后一题
        if current_item:
            formatted.extend(format_single_exercise_item(current_item, item_number))
        
        return formatted
    
    def format_single_exercise_item(item_lines, item_number):
        """格式化单个习题题目，优化选择题"""
        formatted = []
        text = ' '.join(item_lines)
        
        # 检查是否是选择题（包含 A. B. C. D.）
        if re.search(r'[ABCD][\.．]', text):
            # 分离题干和选项
            parts = re.split(r'(?=[ABCD][\.．])', text)
            stem = parts[0].strip()
            options = parts[1:]
            
            formatted.append(f"\\textbf{{{item_number}.}} {stem}")
            formatted.append("\\par\\vspace{0.3em}")
            
            # 使用表格排版选项（每行2个）
            if len(options) >= 4:
                formatted.append("\\begin{center}")
                formatted.append("\\begin{tabular}{@{}p{0.45\\textwidth}p{0.45\\textwidth}@{}}")
                
                for i in range(0, len(options), 2):
                    opt1 = format_option(options[i]) if i < len(options) else ""
                    opt2 = format_option(options[i+1]) if i+1 < len(options) else ""
                    if opt2:
                        formatted.append(f"{opt1} & {opt2} \\\\\\vspace{{0.2em}}")
                    else:
                        formatted.append(f"{opt1} & \\\\\\vspace{{0.2em}}")
                
                formatted.append("\\end{tabular}")
                formatted.append("\\end{center}")
            else:
                # 选项较少，直接列出
                for opt in options:
                    formatted.append(f"\\hspace{{1em}}{format_option(opt)}\\par\\vspace{{0.2em}}")
        else:
            # 非选择题，正常处理
            formatted.append(f"\\textbf{{{item_number}.}} {text}")
        
        return formatted
    
    def format_option(opt_text):
        """格式化单个选项"""
        opt_text = opt_text.strip()
        match = re.match(r'^([ABCD])[\.．]\s*(.+)', opt_text)
        if match:
            return f"\\textbf{{{match.group(1)}.}} {match.group(2)}"
        return opt_text
    
    def generate_ai_hint(problem, solution):
        """生成 AI 思路点拨 - 增强版"""
        problem_text = ' '.join(problem)
        solution_text = ' '.join(solution)
        
        # 等式与不等式
        if '等式' in problem_text and '性质' in problem_text:
            return "本题考查等式的基本性质，关键是掌握等式的传递性、加法性质和乘法性质。"
        elif '不等式' in problem_text and '性质' in problem_text:
            return "本题考查不等式的基本性质，特别注意：两边同乘负数时不等号方向要改变。"
        elif '一元二次' in problem_text or 'ax^2' in problem_text or '判别式' in problem_text:
            return "本题考查一元二次不等式的求解，关键是先求对应方程的根，再结合二次函数图像确定解集。"
        elif '韦达' in problem_text or '根与系数' in problem_text:
            return "本题考查韦达定理的应用，关键是建立根与系数的关系：$x_1+x_2=-b/a$，$x_1x_2=c/a$。"
        elif '分式' in problem_text and '不等式' in problem_text:
            return "本题考查分式不等式的求解，注意：分母不能为零，通常转化为整式不等式求解。"
        elif '绝对值' in problem_text:
            return "本题考查绝对值不等式的求解，关键是根据绝对值的定义进行分类讨论。"
        elif '基本不等式' in problem_text or '均值' in problem_text:
            return "本题考查基本不等式的应用，注意一正二定三相等：各项为正、和或积为定值、等号能取到。"
        elif '比较' in problem_text and '大小' in problem_text:
            return "本题考查实数大小的比较，常用方法：作差法、作商法、中间值法。"
        elif '配方' in problem_text:
            return "本题考查配方法的应用，通过配方可以将代数式化为完全平方形式，便于分析。"
        elif '倒数' in problem_text:
            return "本题考查倒数的性质，注意：同号两数，较大数的倒数反而较小。"
        elif '充要条件' in problem_text or '充分必要' in problem_text:
            return "本题考查充分条件与必要条件的判断，关键是理解推出关系及其逆否命题。"
        # 集合与逻辑
        elif '有限集' in problem_text and '无限集' in problem_text:
            return "本题考查有限集与无限集的判断，关键是看元素个数是否有限。"
        elif '列举法' in problem_text:
            return "本题考查集合的列举法表示，注意元素不重复且不考虑顺序。"
        elif '描述法' in problem_text:
            return "本题考查集合的描述法表示，关键是准确描述元素的共同特征。"
        elif '子集' in problem_text:
            return "本题考查子集的概念，注意空集是任何集合的子集。"
        elif '交集' in problem_text or '并集' in problem_text:
            return "本题考查集合的运算，建议画出文氏图帮助理解。"
        elif '充分条件' in problem_text or '必要条件' in problem_text:
            return "本题考查充分条件与必要条件的判断，关键是理解推出关系。"
        elif '区间' in problem_text:
            return "本题考查区间的表示方法，注意端点是否包含。"
        elif '属于' in problem_text or '∈' in problem_text:
            return "本题考查元素与集合的关系，关键是判断元素是否满足集合的特征性质。"
        else:
            return "本题考查基本概念和方法，注意理解题意，运用相关知识进行推理和计算。"
    
    def process_text(text):
        """处理文本内容"""
        text = re.sub(r'_{3,}', r'\\fillin[2cm]', text)
        if text.startswith('<table>'):
            return convert_html_table_to_latex(text)
        return text
    
    def convert_html_table_to_latex(html_table):
        """转换 HTML 表格"""
        rows = re.findall(r'<tr>(.+?)</tr>', html_table)
        if not rows:
            return "% [表格转换失败]"
        
        latex_rows = []
        max_cols = 0
        
        # 首先计算最大列数
        for row in rows:
            cells = re.findall(r'<td[^>]*>(.+?)</td>', row)
            # 检查是否有 colspan
            colspan_matches = re.findall(r'colspan="(\d+)"', row)
            total_cols = len(cells)
            for cs in colspan_matches:
                total_cols += int(cs) - 1
            max_cols = max(max_cols, total_cols)
        
        for i, row in enumerate(rows):
            cells = re.findall(r'<td[^>]*>(.+?)</td>', row)
            if cells:
                # 处理 colspan（简单处理：用空单元格填充）
                processed_cells = []
                for cell in cells:
                    processed_cells.append(cell)
                    # 检查是否有 colspan
                    cs_match = re.search(r'colspan="(\d+)"', cell)
                    if cs_match:
                        # 添加空单元格
                        for _ in range(int(cs_match.group(1)) - 1):
                            processed_cells.append('')
                
                if i == 0:
                    latex_rows.append(' & '.join(processed_cells) + ' \\\\\\hline')
                else:
                    latex_rows.append(' & '.join(processed_cells) + ' \\\\')
        
        if latex_rows:
            table_code = [
                "\\begin{center}",
                "\\begin{tabular}{" + "|c" * max_cols + "|}",
                "\\hline"
            ]
            table_code.extend(latex_rows)
            table_code.extend([
                "\\hline",
                "\\end{tabular}",
                "\\end{center}"
            ])
            return '\n'.join(table_code)
        
        return "% [表格需要手动转换]"
    
    # 主循环
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        if not stripped:
            i += 1
            continue
        
        if skip_first_line:
            skip_first_line = False
            i += 1
            continue
        
        # 处理分隔符 ---
        if stripped == '---':
            if in_example:
                pending_separator = True
            i += 1
            continue
        
        # 图片
        if stripped.startswith('!['):
            img_match = re.match(r'!\[.*?\]\((.+?)\)', stripped)
            if img_match:
                img_path = img_match.group(1)
                img_filename = Path(img_path).name
                img_relative_path = f"chapter{chapter_num}/{img_filename}"
                latex_lines.append("\\vspace{0.5em}")
                latex_lines.append("\\begin{figure}[htbp]")
                latex_lines.append("\\centering")
                latex_lines.append(f"\\includegraphics[width=0.5\\textwidth]{{{img_relative_path}}}")
                latex_lines.append("\\end{figure}")
                latex_lines.append("\\vspace{0.5em}")
            i += 1
            continue
        
        # 三级标题
        section_match = re.match(r'###\s+(\d+\.\d+)\s+(.+)', stripped)
        if section_match:
            close_example()
            close_exercise()
            latex_lines.append(f"\\section{{{section_match.group(1)} {section_match.group(2)}}}")
            latex_lines.append("")
            i += 1
            continue
        
        # 二级标题
        subsection_match = re.match(r'##\s+(\d+)\s+(.+)', stripped)
        if subsection_match:
            close_example()
            close_exercise()
            subsection_num = subsection_match.group(1)
            subsection_title = subsection_match.group(2)
            
            if '练习' in subsection_title or '习题' in subsection_title:
                latex_lines.append(f"\\subsection*{{{subsection_num} {subsection_title}}}")
                in_exercise = True
                current_exercise_title = f"{subsection_num} {subsection_title}"
            else:
                latex_lines.append(f"\\subsection{{{subsection_num} {subsection_title}}}")
            latex_lines.append("")
            i += 1
            continue
        
        # 特殊标题
        if stripped.startswith('## '):
            close_example()
            close_exercise()
            title = stripped[3:].strip()
            
            if '内容提要' in title:
                latex_lines.append(f"\\section*{{{title}}}")
            elif '复习题' in title:
                latex_lines.append(f"\\section*{{{title}}}")
            elif '拓展与思考' in title:
                latex_lines.append(f"\\subsection*{{{title}}}")
            elif 'A 组' in title or 'B 组' in title:
                latex_lines.append(f"\\subsection*{{{title}}}")
                in_exercise = True
                current_exercise_title = title
            elif '练习' in title or '习题' in title:
                latex_lines.append(f"\\subsection*{{{title}}}")
                in_exercise = True
                current_exercise_title = title
            else:
                latex_lines.append(f"\\subsection*{{{title}}}")
            latex_lines.append("")
            i += 1
            continue
        # 例题 - 改进识别逻辑，排除 "例 X 表明/说明/证明" 等模式
        example_match = re.match(r'[?？]?\s*例\s+(\d+)\s+(.+)', stripped)
        if example_match:
            ex_num = int(example_match.group(1))
            ex_title = example_match.group(2)
            
            # 排除说明性文字（例 X 表明/说明/证明/指出等）
            skip_keywords = ['表明', '说明', '指出', '告诉我们', '可得', '给出']
            # 检查标题中是否包含跳过关键词，且不包含题目关键词
            has_skip_keyword = any(kw in ex_title for kw in skip_keywords)
            has_problem_keyword = bool(re.search(r'[求证计算化简解]|已知|求证|若|设', ex_title))
            
            if has_skip_keyword and not has_problem_keyword:
                # 这是说明性文字，不是例题
                if in_example:
                    close_example()
                latex_lines.append(processed)
                latex_lines.append("")
                i += 1
                continue
            
            # 如果已经在处理例题，先关闭当前的
            if in_example and example_problem:
                close_example()
            
            close_exercise()
            in_example = True
            example_problem.append(f"\\textbf{{例 {ex_num} {ex_title}}}\\par\\vspace{{0.3em}}")
            
            i += 1
            continue
        
        # 解答
        if stripped.startswith('解') and in_example:
            in_solution = True
            pending_separator = False
            if len(stripped) > 1:
                if re.match(r'解[（(]', stripped):
                    example_solution.append(stripped)
                else:
                    example_solution.append(stripped[1:].strip())
            i += 1
            continue
        
        # 处理题目编号 (1) (2) (3) (4) - 如果在例题中且不在解答中，属于题目
        if in_example and not in_solution:
            if re.match(r'^[(（][\d一二三四五六七八九十]+[)）]', stripped):
                example_problem.append(process_text(stripped))
                i += 1
                continue
        
        # 处理普通内容
        processed = process_text(stripped)
        
        if processed in ['Q', '']:
            i += 1
            continue
        
        # 判断是否结束例题
        if in_example:
            if re.match(r'^(###|##)\s+', processed):
                close_example()
                latex_lines.append(processed)
                latex_lines.append("")
            elif re.match(r'^[?？]?\s*例\s+', processed):
                close_example()
                continue
            elif '练习' in processed and re.match(r'^(###|##)\s+', processed):
                close_example()
                latex_lines.append(processed)
                latex_lines.append("")
            elif in_solution:
                example_solution.append(processed)
            else:
                example_problem.append(processed)
        elif in_exercise:
            exercise_content.append(processed)
        else:
            latex_lines.append(processed)
            latex_lines.append("")
        
        i += 1
    
    close_example()
    close_exercise()
    
    # 组合文档
    body = '\n'.join(latex_lines)
    
    latex_doc = preamble
    latex_doc += "\\begin{document}\n\n"
    latex_doc += "\\frontmatter\n\n"
    latex_doc += "\\MakeTitlePage\n\n"
    latex_doc += "\\tableofcontents\n\n"
    latex_doc += "\\mainmatter\n\n"
    latex_doc += f"%==========================================================\n"
    latex_doc += f"\\chapter{{{chapter_title}}}\n"
    latex_doc += f"%==========================================================\n\n"
    latex_doc += body
    latex_doc += "\n\n\\end{document}\n"
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(latex_doc)
    
    return output_path


def convert_chapter(chapter_name, md_file, template_file, output_file, chapter_num, chapter_title):
    """转换单个章节"""
    base_dir = Path("/Users/tangchengbaiair/Downloads/mini-数学资料库")
    
    md_source = base_dir / md_file
    template = base_dir / template_file
    latex_output = base_dir / output_file
    
    # 复制图片
    source_img_dir = base_dir / f"03-上海教材md/{chapter_name}/images"
    target_img_dir = base_dir / f"09-终极版本/必修第一册/chapter{chapter_num}"
    
    if source_img_dir.exists():
        import shutil
        target_img_dir.mkdir(parents=True, exist_ok=True)
        for img in source_img_dir.glob('*'):
            if img.suffix in ['.jpg', '.png', '.jpeg']:
                shutil.copy2(img, target_img_dir / img.name)
        print(f"✓ 图片已复制到 {target_img_dir}")
    
    print("=" * 70)
    print(f"教材 MD 转 LaTeX - {chapter_title}")
    print("=" * 70)
    
    print("\n转换中...")
    result = convert_md_to_latex_ultimate(
        str(md_source),
        str(template),
        str(latex_output),
        chapter_num,
        chapter_title
    )
    print(f"  ✓ LaTeX 已生成: {result}")
    
    # 编译
    print("\n编译 PDF...")
    import subprocess
    
    for run in range(2):
        result_compile = subprocess.run(
            ['xelatex', '-interaction=nonstopmode', str(latex_output)],
            cwd=str(latex_output.parent),
            capture_output=True,
            text=True
        )
    
    if result_compile.returncode == 0:
        print("  ✓ 编译成功!")
        pdf_path = latex_output.with_suffix('.pdf')
        if pdf_path.exists():
            size = pdf_path.stat().st_size / 1024
            print(f"  ✓ PDF: {pdf_path.name} ({size:.1f} KB)")
    else:
        print("  ⚠ 编译有警告")
    
    return result_compile.returncode == 0


def main():
    """主函数 - 转换第2章"""
    success = convert_chapter(
        chapter_name="必修一第2章等式与不等式",
        md_file="03-上海教材md/必修一第2章等式与不等式/必修一第2章等式与不等式-dollar.md",
        template_file="02-讲义输出/必修第一册/第2章-等式与不等式-讲义.tex",
        output_file="09-终极版本/必修第一册/第2章-等式与不等式-讲义.tex",
        chapter_num=2,
        chapter_title="等式与不等式"
    )
    
    if success:
        print("\n" + "=" * 70)
        print("✅ 第2章转换完成!")
        print("=" * 70)
    else:
        print("\n" + "=" * 70)
        print("⚠️ 转换过程中有警告")
        print("=" * 70)


if __name__ == "__main__":
    main()
