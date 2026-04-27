#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
讲义内容填充脚本
基于教材Markdown文件提取知识点和例题，填充到讲义模板中
"""

import os
import re
import sqlite3
import sys

# 配置
BASE_DIR = "/Users/tangchengbaiair/Downloads/mini-数学资料库"
TEXTBOOK_DIR = os.path.join(BASE_DIR, "03-上海教材md/2026教材高清精校版 最新版本上海教材 ")
LECTURE_DIR = os.path.join(BASE_DIR, "02-讲义输出")
DB_PATH = os.path.join(BASE_DIR, "00-索引与配置/teaching_index.db")

# 教材映射
TEXTBOOK_MAP = {
    '必修第一册': '沪教版必修第一册2026',
    '必修第二册': '沪教版必修第二册2026',
    '必修第三册': '沪教版必修第三册2026',
    '必修第四册': '沪教版必修第四册2026',
    '选择性必修第一册': '沪教版选择性必修第一册2026',
    '选择性必修第二册': '沪教版选择性必修第二册2026',
    '选择性必修第三册': '沪教版选择性必修第三册2026',
}

def get_chapter_content(book_name, chapter_num):
    """从教材中提取章节内容"""
    textbook_dir = TEXTBOOK_MAP.get(book_name)
    if not textbook_dir:
        return None
    
    # 尝试读取教材文件
    md_file = os.path.join(TEXTBOOK_DIR, textbook_dir, f"{textbook_dir}-dollar-polished.md")
    if not os.path.exists(md_file):
        md_file = os.path.join(TEXTBOOK_DIR, textbook_dir, f"{textbook_dir}-dollar-polished-fixed.md")
    
    if not os.path.exists(md_file):
        return None
    
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取章节内容 (根据章节号)
    chapter_pattern = f"第{chapter_num}章"
    
    # 找到章节开始位置
    chapter_start = content.find(f"# {chapter_pattern}")
    if chapter_start == -1:
        chapter_start = content.find(f"## {chapter_pattern}")
    if chapter_start == -1:
        return None
    
    # 找到下一章或文件结束
    next_chapter = content.find(f"# 第{chapter_num+1}章", chapter_start)
    if next_chapter == -1:
        next_chapter = len(content)
    
    chapter_content = content[chapter_start:next_chapter]
    return chapter_content

def extract_knowledge_points(content):
    """提取知识点"""
    if not content:
        return []
    
    points = []
    
    # 匹配标题作为知识点
    headers = re.findall(r'##+ (.+?)(?:
|$)', content)
    for h in headers[:10]:  # 限制数量
        if '练习' not in h and '习题' not in h and '复习' not in h:
            points.append(h.strip())
    
    return points[:8]  # 最多8个知识点

def extract_examples(content):
    """提取例题"""
    if not content:
        return []
    
    examples = []
    
    # 匹配例题块
    example_blocks = re.findall(r'(?:例题|例)\s*(\d+)\s*[\.、]?(.*?)(?=

|\Z)', content, re.DOTALL)
    
    for num, text in example_blocks[:5]:  # 最多5个例题
        text = text.strip()
        if len(text) > 20:
            examples.append({
                'num': num,
                'content': text[:500]  # 限制长度
            })
    
    return examples

def get_related_slices(book_name, chapter):
    """从数据库获取相关切片"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 根据章节关键词匹配切片
    cursor.execute("SELECT title, tex_path FROM slices WHERE category LIKE ? OR tag LIKE ?", 
                   (f"%{chapter}%", f"%{chapter}%"))
    slices = cursor.fetchall()
    conn.close()
    
    return slices[:3]  # 最多3个

def fill_lecture(lecture_path, book_name, chapter):
    """填充讲义内容"""
    # 获取教材内容
    chapter_num = int(re.search(r'(\d+)', chapter).group(1)) if re.search(r'(\d+)', chapter) else 1
    content = get_chapter_content(book_name, chapter_num)
    
    if not content:
        print(f"  ⚠️ 未找到教材内容: {book_name} {chapter}")
        return False
    
    # 提取知识点和例题
    knowledge_points = extract_knowledge_points(content)
    examples = extract_examples(content)
    related_slices = get_related_slices(book_name, chapter)
    
    # 读取现有讲义
    try:
        with open(lecture_path, 'r', encoding='utf-8') as f:
            lecture = f.read()
    except:
        return False
    
    # 构建填充内容
    knowledge_section = "\subsection{知识要点}
"
    for i, kp in enumerate(knowledge_points, 1):
        knowledge_section += f"\knowledgepoint{{{kp}}}

"
    
    example_section = "\subsection{典型例题}
"
    if examples:
        for ex in examples:
            example_section += f"\example{{{ex['num']}}}
{ex['content']}\

"
    else:
        example_section += "% 例题内容待补充
"
    
    # 替换讲义中的占位符
    lecture = lecture.replace(
        "\subsection{知识要点}
本章主要学习",
        knowledge_section
    )
    
    lecture = lecture.replace(
        "\subsection{典型例题}
% 例题内容待补充",
        example_section
    )
    
    # 添加切片引用
    if related_slices:
        slice_section = "\subsection{相关切片}
"
        for title, path in related_slices:
            slice_section += f"\begin{{itemize}}
\item \textbf{{{title}}}
\end{{itemize}}
"
        
        # 在知识要点后添加
        if "相关切片" not in lecture:
            lecture = lecture.replace(
                "\subsection{课堂练习}",
                slice_section + "
\subsection{课堂练习}"
            )
    
    # 保存
    with open(lecture_path, 'w', encoding='utf-8') as f:
        f.write(lecture)
    
    return True

def main():
    """主函数"""
    print("=" * 60)
    print("讲义内容填充")
    print("=" * 60)
    
    # 获取所有讲义
    lectures = []
    for root, dirs, files in os.walk(LECTURE_DIR):
        for file in files:
            if file.endswith('.tex') and '学生版' in file:
                book = os.path.basename(os.path.dirname(root))
                chapter_match = re.search(r'第(\d+)章', file)
                chapter = f"第{chapter_match.group(1)}章" if chapter_match else "未知"
                lectures.append({
                    'path': os.path.join(root, file),
                    'book': book,
                    'chapter': chapter,
                    'file': file
                })
    
    print(f"\n找到 {len(lectures)} 个学生版讲义")
    
    success = 0
    failed = 0
    
    for lec in lectures:
        print(f"\n处理: {lec['book']} {lec['chapter']}")
        if fill_lecture(lec['path'], lec['book'], lec['chapter']):
            print(f"  ✅ 已填充")
            success += 1
        else:
            print(f"  ❌ 填充失败")
            failed += 1
    
    print(f"\n{'='*60}")
    print(f"完成: 成功 {success}/{len(lectures)}, 失败 {failed}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
