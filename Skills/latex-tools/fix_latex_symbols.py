#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数学符号修复脚本
修复沪教版选择性必修第一册教材中的LaTeX数学符号问题
"""

import re
import sys

def fix_latex_issues(input_file, output_file=None):
    """修复LaTeX数学符号问题"""
    
    if not output_file:
        output_file = input_file.replace('.md', '-fixed.md')
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    fixes = []
    
    # 修复1: \lbrack 和 \rbrack → \left[ 和 \right]
    content, count = re.subn(r'\\left\\lbrack', r'\\left[', content)
    if count > 0:
        fixes.append(f"修复 \left\lbrack → \left[ : {count} 处")
    
    content, count = re.subn(r'\\right\\rbrack', r'\\right]', content)
    if count > 0:
        fixes.append(f"修复 \right\rbrack → \right] : {count} 处")
    
    content, count = re.subn(r'\\lbrack', r'[', content)
    if count > 0:
        fixes.append(f"修复 \lbrack → [ : {count} 处")
    
    content, count = re.subn(r'\\rbrack', r']', content)
    if count > 0:
        fixes.append(f"修复 \rbrack → ] : {count} 处")
    
    # 修复2: \text{ ⏜ } → \frown (圆弧符号)
    content, count = re.subn(r'\\text\s*{\s*⏜\s*}', r'\\frown', content)
    if count > 0:
        fixes.append(f"修复 \text{{⏜}} → \frown : {count} 处")
    
    # 修复3: \text{ ⏝ } → \smile (下弧)
    content, count = re.subn(r'\\text\s*{\s*⏝\s*}', r'\\smile', content)
    if count > 0:
        fixes.append(f"修复 \text{{⏝}} → \smile : {count} 处")
    
    # 修复4: 数学模式中的中文顿号
    content, count = re.subn(r'\\text\s*{\s*、\s*}', r',', content)
    if count > 0:
        fixes.append(f"修复 \text{{、}} → , : {count} 处")
    
    # 修复5: \text{ 或 } → \text{ 或 }
    content, count = re.subn(r'\\text\s*{\s*或\s*}', r'\\text{ 或 }', content)
    if count > 0:
        fixes.append(f"修复 \text{{或}} 格式 : {count} 处")
    
    # 修复6: \text{ 且 } → \text{ 且 }
    content, count = re.subn(r'\\text\s*{\s*且\s*}', r'\\text{ 且 }', content)
    if count > 0:
        fixes.append(f"修复 \text{{且}} 格式 : {count} 处")
    
    # 修复7: \text{ 与 } → \text{ 与 }
    content, count = re.subn(r'\\text\s*{\s*与\s*}', r'\\text{ 与 }', content)
    if count > 0:
        fixes.append(f"修复 \text{{与}} 格式 : {count} 处")
    
    # 保存修复后的文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # 输出修复报告
    print(f"✅ 修复完成: {output_file}")
    print(f"
修复内容:")
    for fix in fixes:
        print(f"  • {fix}")
    
    if not fixes:
        print("  (无需修复)")
    
    # 统计
    print(f"
统计:")
    print(f"  原始文件大小: {len(original_content)} 字符")
    print(f"  修复后大小: {len(content)} 字符")
    print(f"  变化: {len(content) - len(original_content)} 字符")

if __name__ == '__main__':
    input_file = "/Users/tangchengbaiair/Downloads/mini-数学资料库/03-上海教材md/2026教材高清精校版 最新版本上海教材 /沪教版选择性必修第一册2026/沪教版选择性必修第一册2026-dollar-polished.md"
    fix_latex_issues(input_file)
