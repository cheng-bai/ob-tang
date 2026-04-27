#!/usr/bin/env python3
"""
规范化 2026 年试卷文件的 frontmatter
"""

import os
import re
from pathlib import Path

def extract_info_from_filename(filename):
    """从文件名提取地区、考试类型信息"""
    # 匹配模式: 2026届{地区}{...}{考试类型}...
    pattern = r'2026届([^\d]{2,4})(?:高三[上下]学期)?([^\/\\]*(?:一模|二模|高考|期末|期中|月考))'
    match = re.search(pattern, filename)

    district = None
    exam_type = None

    if match:
        district_raw = match.group(1)
        exam_type_raw = match.group(2)

        # 标准化地区名
        district_map = {
            '浦东': '浦东',
            '浦东新区': '浦东',
            '黄浦': '黄浦',
            '闵行': '闵行',
            '嘉定': '嘉定',
            '金山': '金山区',
            '金山区': '金山区',
            '奉贤': '奉贤区',
            '奉贤区': '奉贤区',
            '崇明': '崇明区',
            '崇明区': '崇明区',
            '杨浦': '杨浦',
            '静安': '静安',
            '长宁': '长宁',
            '普陀': '普陀',
            '虹口': '虹口',
            '宝山': '宝山',
            '松江': '松江',
            '青浦': '青浦',
        }

        for key, value in district_map.items():
            if key in district_raw or district_raw in key:
                district = value
                break

        # 标准化考试类型
        exam_type_keywords = ['一模', '二模', '高考', '期末', '期中', '月考']
        for keyword in exam_type_keywords:
            if keyword in exam_type_raw:
                exam_type = keyword
                break

    return district, exam_type

def get_difficulty(exam_type):
    """根据考试类型返回难度"""
    if exam_type in ['一模', '二模', '高考']:
        return '⭐⭐⭐'
    elif exam_type == '期末':
        return '⭐⭐'
    else:
        return '⭐⭐⭐'  # 默认

def normalize_file(filepath):
    """规范化单个文件的 frontmatter"""
    filename = os.path.basename(filepath)

    # 提取信息
    district, exam_type = extract_info_from_filename(filename)

    if not district or not exam_type:
        return None, f"无法从文件名提取信息: {filename}"

    # 构建规范化值
    year = '2026'
    source = f"2026届{district}{exam_type}"
    difficulty = get_difficulty(exam_type)
    question_type = '综合'

    # 读取文件内容
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 提取或构建 frontmatter
    frontmatter_pattern = r'^---\n(.*?)\n---\n'
    match = re.match(frontmatter_pattern, content, re.DOTALL)

    new_frontmatter = f"""---
title: {filename.replace('.md', '')}
来源: {source}
年份: {year}
难度: {difficulty}
题型: {question_type}
---"""

    if match:
        # 替换现有 frontmatter
        new_content = re.sub(frontmatter_pattern, new_frontmatter + '\n', content, count=1)
    else:
        # 添加新 frontmatter
        new_content = new_frontmatter + '\n' + content

    # 写回文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return {
        'file': filename,
        '年份': year,
        '地区': district,
        '考试类型': exam_type,
        '组合来源': source,
        '题型': question_type,
        '难度': difficulty
    }, None

def main():
    base_dir = Path("/Users/tangchengbaiair/Downloads/ob-tang/04-试卷汇总")

    # 查找所有 2026 md 文件
    files = list(base_dir.glob("*2026*.md"))

    results = []
    errors = []

    print(f"找到 {len(files)} 个 2026 年试卷文件\n")

    for filepath in files:
        result, error = normalize_file(filepath)
        if result:
            results.append(result)
        else:
            errors.append(error)

    # 输出结果表
    print("=" * 100)
    print("规范化结果表")
    print("=" * 100)
    print(f"{'文件名':<40} {'年份':<6} {'地区':<8} {'考试类型':<8} {'组合来源':<20} {'题型':<6} {'难度':<10}")
    print("-" * 100)

    for r in results:
        print(f"{r['file']:<40} {r['年份']:<6} {r['地区']:<8} {r['考试类型']:<8} {r['组合来源']:<20} {r['题型']:<6} {r['难度']:<10}")

    print("-" * 100)
    print(f"总计: 成功更新 {len(results)} 个文件")

    if errors:
        print("\n错误信息:")
        for e in errors:
            print(f"  - {e}")

if __name__ == "__main__":
    main()
