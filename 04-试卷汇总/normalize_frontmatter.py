#!/usr/bin/env python3
"""
扫描并规范化试卷汇总目录下所有 .md 文件的 frontmatter
"""

import os
import re
import yaml
from pathlib import Path

BASE_DIR = Path("/Users/tangchengbaiair/Downloads/ob-tang/04-试卷汇总")

# 正则模式用于从文件名提取信息
PATTERNS = {
    'year': r'(20\d{2})',
    'region': r'(?:届|年)([^一二三四五六七八九十]{1,6}?)(?:区|高三|高考|数学|一模|二模|模考|功底考|春考)',
    'exam_type': r'(一模|二模|高考|功底考|春考)',
}

# 地区映射（处理简写和别名）
REGION_MAP = {
    '浦东': '浦东',
    '黄浦': '黄浦',
    '静安': '静安',
    '徐汇': '徐汇',
    '长宁': '长宁',
    '普陀': '普陀',
    '虹口': '虹口',
    '杨浦': '杨浦',
    '宝山': '宝山',
    '闵行': '闵行',
    '嘉定': '嘉定',
    '金山': '金山',
    '松江': '松江',
    '青浦': '青浦',
    '奉贤': '奉贤',
    '崇明': '崇明',
}

# 难度映射
DIFFICULTY_MAP = {
    '一模': '⭐⭐⭐',
    '二模': '⭐⭐⭐',
    '高考': '⭐⭐⭐',
    '功底考': '⭐⭐',
    '春考': '⭐⭐⭐',
}


def extract_info_from_filename(filename):
    """从文件名提取年份、地区、考试类型"""
    info = {'year': None, 'region': None, 'exam_type': None}

    # 提取年份
    year_match = re.search(PATTERNS['year'], filename)
    if year_match:
        info['year'] = year_match.group(1)

    # 提取考试类型
    for exam_type in ['一模', '二模', '高考', '功底考', '春考']:
        if exam_type in filename:
            info['exam_type'] = exam_type
            break

    # 提取地区
    region_match = re.search(PATTERNS['region'], filename)
    if region_match:
        region = region_match.group(1).strip()
        # 映射地区
        for key, value in REGION_MAP.items():
            if key in region:
                info['region'] = value
                break
        if not info['region']:
            info['region'] = region

    return info


def parse_frontmatter(content):
    """解析 frontmatter，返回 (frontmatter_dict, 正文)"""
    if not content.startswith('---'):
        return None, content

    # 找到第二个 ---
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return None, content

    frontmatter_text = match.group(1)
    body = content[match.end():]

    try:
        frontmatter = yaml.safe_load(frontmatter_text) or {}
    except:
        frontmatter = {}

    return frontmatter, body


def build_source(year, region, exam_type):
    """构建来源字段"""
    if not year or not exam_type:
        return None

    # 届数 = 年份最后一位
    if region:
        return f"{year}届{region}{exam_type}"
    else:
        return f"{year}届{exam_type}"


def get_difficulty(exam_type):
    """根据考试类型获取难度"""
    return DIFFICULTY_MAP.get(exam_type, '⭐⭐⭐')


def normalize_frontmatter(frontmatter, filename_info):
    """规范化 frontmatter，返回新的 frontmatter dict 和变更记录"""
    changes = []
    new_fm = dict(frontmatter) if frontmatter else {}

    # 补全年份
    year = filename_info.get('year')
    if year:
        current_year = new_fm.get('年份')
        if not current_year:
            new_fm['年份'] = year
            changes.append(f"添加年份: {year}")
        elif str(current_year) != year:
            new_fm['年份'] = year
            changes.append(f"修正年份: {current_year} → {year}")

    # 补全来源
    source = build_source(
        filename_info.get('year'),
        filename_info.get('region'),
        filename_info.get('exam_type')
    )
    if source:
        current_source = new_fm.get('来源')
        if not current_source:
            new_fm['来源'] = source
            changes.append(f"添加来源: {source}")
        elif current_source != source and '上海模考' in str(current_source):
            new_fm['来源'] = source
            changes.append(f"修正来源: {current_source} → {source}")

    # 补全难度
    exam_type = filename_info.get('exam_type')
    if exam_type:
        difficulty = get_difficulty(exam_type)
        current_difficulty = new_fm.get('难度')
        if not current_difficulty:
            new_fm['难度'] = difficulty
            changes.append(f"添加难度: {difficulty} ({exam_type})")

    # 补全题型
    current_type = new_fm.get('题型')
    if not current_type:
        new_fm['题型'] = '综合'
        changes.append("添加题型: 综合")

    return new_fm, changes


def dump_frontmatter(frontmatter):
    """将 frontmatter 转换为 YAML 字符串"""
    lines = ['---']
    for key, value in frontmatter.items():
        if value is None:
            continue
        # 处理字符串值
        if isinstance(value, str):
            # 如果包含特殊字符，使用引号
            if ':' in value or '"' in value or '\n' in value:
                value = f'"{value.replace("\\", "\\\\").replace('"', '\\"')}"'
            lines.append(f"{key}: {value}")
        else:
            lines.append(f"{key}: {value}")
    lines.append('---\n')
    return '\n'.join(lines)


def process_file(filepath):
    """处理单个文件，返回 (是否修改, 变更列表, 原 frontmatter, 新 frontmatter)"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, [f"读取失败: {e}"], None, None

    # 解析 frontmatter
    frontmatter, body = parse_frontmatter(content)

    # 从文件名提取信息
    filename = filepath.name
    filename_info = extract_info_from_filename(filename)

    # 如果没有提取到任何信息，跳过
    if not any(filename_info.values()):
        return False, ["无法从文件名提取信息，跳过"], None, None

    # 规范化 frontmatter
    new_fm, changes = normalize_frontmatter(frontmatter, filename_info)

    if not changes:
        return False, [], frontmatter, new_fm

    # 构建新内容
    new_content = dump_frontmatter(new_fm) + body

    # 写回文件
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
    except Exception as e:
        return False, [f"写入失败: {e}"], frontmatter, new_fm

    return True, changes, frontmatter, new_fm


def main():
    """主函数"""
    md_files = list(BASE_DIR.rglob('*.md'))

    updated_count = 0
    report_lines = []
    skipped_count = 0

    report_lines.append("=" * 60)
    report_lines.append("试卷 Frontmatter 规范化报告")
    report_lines.append(f"扫描文件数: {len(md_files)}")
    report_lines.append("=" * 60)
    report_lines.append("")

    for filepath in sorted(md_files):
        rel_path = filepath.relative_to(BASE_DIR)
        modified, changes, old_fm, new_fm = process_file(filepath)

        if changes:
            report_lines.append(f"\n📄 {rel_path}")
            if old_fm:
                report_lines.append(f"   原 frontmatter: {old_fm}")
            if new_fm:
                report_lines.append(f"   新 frontmatter: {new_fm}")
            for change in changes:
                report_lines.append(f"   ✓ {change}")

        if modified:
            updated_count += 1
        elif not changes:
            skipped_count += 1

    report_lines.append("\n" + "=" * 60)
    report_lines.append(f"更新文件数: {updated_count}")
    report_lines.append(f"跳过文件数: {skipped_count}")
    report_lines.append("=" * 60)

    report = '\n'.join(report_lines)
    print(report)

    # 保存报告
    report_path = BASE_DIR / 'frontmatter_update_report.txt'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"\n报告已保存至: {report_path}")


if __name__ == '__main__':
    main()
