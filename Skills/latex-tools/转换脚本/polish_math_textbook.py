#!/usr/bin/env python3
"""
沪教版数学必修第三册 Markdown 润色脚本 - 修正标题层级
"""

import re

def polish_markdown(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    result = []

    prev_line_empty = False
    in_toc = False  # 是否在目录区域
    past_toc = False  # 是否已过目录区域
    seen_chapters = set()  # 用于检测重复的章标题

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # 检测目录开始和结束
        if stripped in ['## 目 录', '目 录']:
            in_toc = True
            result.append('# 目录')
            prev_line_empty = False
            i += 1
            continue

        # 检测目录结束（遇到第一个图片或空行后的章标题）
        if in_toc and stripped.startswith('!['):
            in_toc = False
            past_toc = True

        # 1. 删除无意义的行
        if re.search(r'细目标题|MONE|SHE|TAND|BART|牛肉鸡', stripped):
            i += 1
            continue

        # 2. 跳过纯空标题
        if re.match(r'^#{1,6}\s*$', stripped):
            i += 1
            continue

        # 3. 规范数学公式标记
        line = re.sub(r'\$\s+\$', '$ $', line)

        # 4. 处理章节标题（无 # 标记的）
        # 只匹配 "第 X 章 标题" 格式，且标题应该在教材章节范围内
        chapter_match = re.match(r'^(第\s*(10|11|12|13)\s*章)\s*(.+)$', stripped)
        if chapter_match and not stripped.startswith('#'):
            chapter_num = chapter_match.group(2)
            chapter_title = chapter_match.group(3).strip()
            chapter_key = f"{chapter_num}:{chapter_title}"

            if in_toc:
                # 在目录中，保持为普通文本（缩进）
                result.append(f"- {chapter_match.group(1)} {chapter_title}")
            else:
                # 检查是否重复
                if chapter_key in seen_chapters:
                    i += 1
                    continue
                seen_chapters.add(chapter_key)
                result.append(f"# {chapter_match.group(1)} {chapter_title}")
            prev_line_empty = False
            i += 1
            continue

        # 5. 处理小节标题（如 "10.1 平面及其基本性质"）
        # 原格式：### 10.1 基本性质 → 改为二级标题 ## 10.1 基本性质
        section_match = re.match(r'^###\s+(\d+\.\d+)\s*(.*)$', stripped)
        if section_match:
            section_num = section_match.group(1)
            section_title = section_match.group(2).strip()
            result.append(f"## {section_num} {section_title}")
            prev_line_empty = False
            i += 1
            continue

        # 6. 处理小节内的子标题（如 "## 1 空间的点"）
        # 改为三级标题 ### 1 空间的点
        subsection_match = re.match(r'^##\s+(\d+)\s+(.+)$', stripped)
        if subsection_match:
            subsection_num = subsection_match.group(1)
            subsection_title = subsection_match.group(2).strip()
            result.append(f"### {subsection_num} {subsection_title}")
            prev_line_empty = False
            i += 1
            continue

        # 7. 处理 "## 练习 X.X(X)" - 改为四级标题
        exercise_match = re.match(r'^##\s+(练习)\s+(\d+\.\d+\(\d+\))$', stripped)
        if exercise_match:
            result.append(f"#### {exercise_match.group(1)} {exercise_match.group(2)}")
            prev_line_empty = False
            i += 1
            continue

        # 8. 处理 "## 习题 X.X" - 改为四级标题
        problem_match = re.match(r'^##\s+(习题)\s+(\d+\.\d+)$', stripped)
        if problem_match:
            result.append(f"#### {problem_match.group(1)} {problem_match.group(2)}")
            prev_line_empty = False
            i += 1
            continue

        # 9. 处理 "## A 组" / "## B 组" - 改为五级标题
        group_match = re.match(r'^##\s+([AB])\s+组$', stripped)
        if group_match:
            result.append(f"##### {group_match.group(1)} 组")
            prev_line_empty = False
            i += 1
            continue

        # 10. 处理 "## * 10.5 异面直线间的距离" - 星号小节
        star_section_match = re.match(r'^##\s+\*\s+(\d+\.\d+)\s+(.+)$', stripped)
        if star_section_match:
            result.append(f"## *{star_section_match.group(1)} {star_section_match.group(2)}")
            prev_line_empty = False
            i += 1
            continue

        # 11. 处理特殊标题
        if stripped == '## 前言' or stripped == '前言':
            result.append('# 前言')
            prev_line_empty = False
            i += 1
            continue

        # "内容提要" 作为二级标题（在章下）
        if stripped == '内容提要' or stripped == '## 内容提要':
            result.append('## 内容提要')
            prev_line_empty = False
            i += 1
            continue

        # "复习题" 作为二级标题
        if stripped == '复习题' or stripped == '## 复习题':
            result.append('## 复习题')
            prev_line_empty = False
            i += 1
            continue

        if stripped == '附录' or stripped == '## 附录':
            result.append('# 附录')
            prev_line_empty = False
            i += 1
            continue

        # 12. 删除孤立的章节副标题
        if stripped in ['空间直线', '空间直线与平面', '简单几何体', '概率初步', '统计']:
            next_idx = i + 1
            while next_idx < len(lines) and lines[next_idx].strip() == '':
                next_idx += 1
            if next_idx < len(lines):
                next_line = lines[next_idx].strip()
                if next_line.startswith('#') or re.match(r'^第\s*\d+\s*章', next_line):
                    i += 1
                    continue

        # 13. 处理其他 ## 开头的行
        if stripped.startswith('## ') and not stripped.startswith('###'):
            content_text = stripped[3:].strip()
            # 如果是数字开头，作为三级标题
            if re.match(r'^\d+\s+', content_text):
                result.append(f"### {content_text}")
            else:
                # 其他情况，作为普通段落处理
                result.append(content_text)
            prev_line_empty = False
            i += 1
            continue

        # 14. 删除多余空行
        if stripped == '':
            if prev_line_empty:
                i += 1
                continue
            prev_line_empty = True
        else:
            prev_line_empty = False

        result.append(line)
        i += 1

    # 后处理
    text = '\n'.join(result)

    # 删除连续3个或更多的换行符
    text = re.sub(r'\n{4,}', '\n\n\n', text)

    # 删除行尾多余空格
    lines = text.split('\n')
    lines = [line.rstrip() for line in lines]
    text = '\n'.join(lines)

    # 确保文件末尾有换行符
    text = text.rstrip() + '\n'

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"润色完成！输出文件：{output_file}")

if __name__ == '__main__':
    input_file = '/Users/tangchengbaiair/Downloads/mini-数学资料库/03-上海教材md/2026教材高清精校版 最新版本上海教材 /沪教版必修第三册2026/沪教版必修第三册2026-dollar.md'
    output_file = '/Users/tangchengbaiair/Downloads/mini-数学资料库/03-上海教材md/2026教材高清精校版 最新版本上海教材 /沪教版必修第三册2026/沪教版必修第三册2026-polished.md'
    polish_markdown(input_file, output_file)
