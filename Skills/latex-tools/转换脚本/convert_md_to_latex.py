#!/usr/bin/env python3
"""
上海教材 MD 转 LaTeX 讲义转换器
严格保留原始教材内容，应用 LaTeX 模板样式
"""

import os
import re
import sys
from pathlib import Path


def read_template_preamble(template_path):
    """读取 LaTeX 模板的导言区（到 \\begin{document} 之前）"""
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    doc_start = content.find('\\begin{document}')
    if doc_start == -1:
        raise ValueError(f"Template {template_path} does not contain \\begin{document}")
    
    return content[:doc_start]


def process_content(text):
    """处理内容中的特殊格式"""
    # 处理填空下划线（3个或更多下划线）
    text = re.sub(r'_{3,}', r'\\fillin[2cm]', text)
    
    # 处理表格标记
    if text.startswith('<table>'):
        return "% [表格需要手动转换为 LaTeX 表格]"
    
    # 跳过水平线
    if text == '---':
        return ""
    
    # 跳过孤立的 "Q"（可能是转换残留）
    if text == 'Q':
        return ""
    
    return text


def md_to_latex_body(md_content, chapter_title):
    """将 MD 内容转换为 LaTeX 正文（严格保留原文）"""
    lines = md_content.split('\n')
    latex_lines = []
    
    in_example = False
    in_exercise = False
    example_content = []
    exercise_content = []
    exercise_title = ""
    skip_first_title = True
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # 跳过空行和图片行
        if not stripped:
            i += 1
            continue
        if stripped.startswith('![') and '](' in stripped:
            i += 1
            continue
        
        # 跳过第一章标题（已经在 \chapter 中）
        if skip_first_title and stripped == chapter_title:
            skip_first_title = False
            i += 1
            continue
        
        # 处理章节标题 ### 1.1 集合初步
        section_match = re.match(r'###\s+(\d+\.\d+)\s+(.+)', stripped)
        if section_match:
            # 关闭之前的环境
            if in_example and example_content:
                latex_lines.append("\\begin{example}")
                latex_lines.extend(example_content)
                latex_lines.append("\\end{example}")
                latex_lines.append("")
                example_content = []
                in_example = False
            if in_exercise and exercise_content:
                latex_lines.append("\\begin{exercise}")
                latex_lines.append(f"\\textbf{{{exercise_title}}}")
                latex_lines.extend(exercise_content)
                latex_lines.append("\\end{exercise}")
                latex_lines.append("")
                exercise_content = []
                in_exercise = False
            
            section_title = section_match.group(2)
            latex_lines.append(f"\\section{{{section_title}}}")
            latex_lines.append("")
            i += 1
            continue
        
        # 处理小节标题 ## 1 集合
        subsection_match = re.match(r'##\s+(\d+)\s+(.+)', stripped)
        if subsection_match:
            # 关闭之前的环境
            if in_example and example_content:
                latex_lines.append("\\begin{example}")
                latex_lines.extend(example_content)
                latex_lines.append("\\end{example}")
                latex_lines.append("")
                example_content = []
                in_example = False
            if in_exercise and exercise_content:
                latex_lines.append("\\begin{exercise}")
                latex_lines.append(f"\\textbf{{{exercise_title}}}")
                latex_lines.extend(exercise_content)
                latex_lines.append("\\end{exercise}")
                latex_lines.append("")
                exercise_content = []
                in_exercise = False
            
            subsection_title = subsection_match.group(2)
            if '练习' in subsection_title or '习题' in subsection_title:
                latex_lines.append(f"\\subsection*{{{subsection_title}}}")
            else:
                latex_lines.append(f"\\subsection{{{subsection_title}}}")
            latex_lines.append("")
            i += 1
            continue
        
        # 处理其他 ## 标题（如练习、习题、A组、B组等）
        if stripped.startswith('## '):
            title = stripped[3:].strip()
            
            # 关闭之前的环境
            if in_example and example_content:
                latex_lines.append("\\begin{example}")
                latex_lines.extend(example_content)
                latex_lines.append("\\end{example}")
                latex_lines.append("")
                example_content = []
                in_example = False
            if in_exercise and exercise_content:
                latex_lines.append("\\begin{exercise}")
                latex_lines.append(f"\\textbf{{{exercise_title}}}")
                latex_lines.extend(exercise_content)
                latex_lines.append("\\end{exercise}")
                latex_lines.append("")
                exercise_content = []
                in_exercise = False
            
            # 特殊标题使用 subsection*
            special_titles = ['练习', '习题', 'A 组', 'B 组', '内容提要', '复习题', '拓展与思考']
            if any(s in title for s in special_titles):
                latex_lines.append(f"\\subsection*{{{title}}}")
            else:
                latex_lines.append(f"\\subsection{{{title}}}")
            latex_lines.append("")
            i += 1
            continue
        
        # 处理例题开始（例 1 ...）
        example_start_match = re.match(r'例\s+(\d+)\s+(.+)', stripped)
        if example_start_match:
            # 关闭之前的 example
            if in_example and example_content:
                latex_lines.append("\\begin{example}")
                latex_lines.extend(example_content)
                latex_lines.append("\\end{example}")
                latex_lines.append("")
                example_content = []
            
            in_example = True
            example_num = example_start_match.group(1)
            example_title_text = example_start_match.group(2)
            example_content.append(f"\\textbf{{例 {example_num} {example_title_text}}}")
            example_content.append("")
            i += 1
            continue
        
        # 处理练习开始（练习 1.1(1) 等）
        exercise_match = re.match(r'(练习\s+\d+\.\d+.*)', stripped)
        if exercise_match:
            # 关闭之前的 example
            if in_example and example_content:
                latex_lines.append("\\begin{example}")
                latex_lines.extend(example_content)
                latex_lines.append("\\end{example}")
                latex_lines.append("")
                example_content = []
                in_example = False
            
            in_exercise = True
            exercise_title = exercise_match.group(1)
            i += 1
            continue
        
        # 处理解（在例题中）
        if stripped.startswith('解') and in_example:
            if len(stripped) > 1:
                example_content.append(f"\\textbf{{解}} {stripped[1:].strip()}")
            else:
                example_content.append("\\textbf{解}")
            i += 1
            continue
        
        # 处理普通内容
        processed = process_content(stripped)
        if not processed:
            i += 1
            continue
        
        if in_example:
            example_content.append(processed)
        elif in_exercise:
            exercise_content.append(processed)
        else:
            latex_lines.append(processed)
        
        i += 1
    
    # 处理未关闭的环境
    if in_example and example_content:
        latex_lines.append("\\begin{example}")
        latex_lines.extend(example_content)
        latex_lines.append("\\end{example}")
    
    if in_exercise and exercise_content:
        latex_lines.append("\\begin{exercise}")
        latex_lines.append(f"\\textbf{{{exercise_title}}}")
        latex_lines.extend(exercise_content)
        latex_lines.append("\\end{exercise}")
    
    return '\n'.join(latex_lines)


def convert_md_to_lecture(md_path, template_path, output_path, chapter_num, chapter_title):
    """将单个 MD 文件转换为 LaTeX 讲义"""
    print(f"  读取: {md_path}")
    
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    print(f"  读取模板: {template_path}")
    preamble = read_template_preamble(template_path)
    
    # 生成正文
    print(f"  转换内容...")
    body = md_to_latex_body(md_content, chapter_title)
    
    # 组合完整文档
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
    
    # 写入输出文件
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(latex_doc)
    
    print(f"  ✓ 已生成: {output_path}")
    return output_path


def get_chapter_info_from_filename(filename):
    """从文件名提取章节信息"""
    # 必修一第1章集合与逻辑-dollar.md -> chapter_num=1, title=集合与逻辑
    match = re.match(r'必修[一二三四]第(\d+)章(.+?)-dollar\.md', filename)
    if match:
        return int(match.group(1)), match.group(2)
    
    # 选修一第1章... 等
    match = re.match(r'选修[一二三]第(\d+)章(.+?)-dollar\.md', filename)
    if match:
        return int(match.group(1)), match.group(2)
    
    return None, None


def main():
    """主函数：批量转换所有教材文件"""
    base_dir = Path("/Users/tangchengbaiair/Downloads/mini-数学资料库")
    md_source_dir = base_dir / "03-上海教材md"
    template_dir = base_dir / "02-讲义输出"
    output_dir = base_dir / "04-讲义输出-v2"
    
    print("=" * 60)
    print("上海教材 MD 转 LaTeX 讲义转换器")
    print("=" * 60)
    
    # 查找所有 MD 文件
    md_files = []
    for item in md_source_dir.iterdir():
        if item.is_dir():
            for md_file in item.glob("*-dollar.md"):
                md_files.append(md_file)
    
    print(f"\n找到 {len(md_files)} 个教材文件")
    print("-" * 60)
    
    # 转换每个文件
    success_count = 0
    failed_files = []
    
    for md_file in sorted(md_files):
        chapter_num, chapter_title = get_chapter_info_from_filename(md_file.name)
        
        if chapter_num is None:
            print(f"\n跳过: {md_file.name} (无法识别章节信息)")
            continue
        
        print(f"\n处理: 第{chapter_num}章 {chapter_title}")
        
        # 确定输出路径
        # 根据文件名判断是必修还是选修
        if '必修一' in md_file.name:
            book_name = "必修第一册"
        elif '必修二' in md_file.name:
            book_name = "必修第二册"
        elif '必修三' in md_file.name:
            book_name = "必修第三册"
        elif '必修四' in md_file.name:
            book_name = "必修第四册"
        elif '选修一' in md_file.name:
            book_name = "选择性必修第一册"
        elif '选修二' in md_file.name:
            book_name = "选择性必修第二册"
        elif '选修三' in md_file.name:
            book_name = "选择性必修第三册"
        else:
            book_name = "其他"
        
        output_path = output_dir / book_name / f"第{chapter_num}章-{chapter_title}-讲义.tex"
        
        # 查找对应的模板
        template_path = template_dir / book_name / f"第{chapter_num}章-{chapter_title}-讲义.tex"
        
        if not template_path.exists():
            # 尝试查找任何可用的模板
            template_candidates = list(template_dir.glob(f"*/第{chapter_num}章-*-讲义.tex"))
            if template_candidates:
                template_path = template_candidates[0]
                print(f"  使用备选模板: {template_path}")
            else:
                print(f"  ✗ 未找到模板，跳过")
                failed_files.append(md_file.name)
                continue
        
        try:
            convert_md_to_lecture(
                str(md_file),
                str(template_path),
                str(output_path),
                chapter_num,
                chapter_title
            )
            success_count += 1
        except Exception as e:
            print(f"  ✗ 转换失败: {e}")
            failed_files.append(md_file.name)
    
    print("\n" + "=" * 60)
    print(f"转换完成: {success_count}/{len(md_files)} 个文件成功")
    if failed_files:
        print(f"失败文件: {', '.join(failed_files)}")
    print(f"输出目录: {output_dir}")
    print("=" * 60)


if __name__ == "__main__":
    main()
