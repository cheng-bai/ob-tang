"""
数学试卷转 Obsidian Markdown 工具
将解析后的 JSON 试卷转换为 Obsidian 可用的 Markdown 文件格式

使用方法:
    python json_to_obsidian.py

输入:
    同目录下的 *_parsed.json 文件

输出:
    obsidian/ 文件夹，包含:
    - index.md (总索引)
    - questions/ (每道题目独立文件)
    - by_type/ (按题型分类)
    - by_tag/ (按知识点分类)
"""

import json
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any


class ObsidianExporter:
    """将数学试卷导出为 Obsidian Markdown 格式"""

    def __init__(self, json_path: Path):
        self.json_path = json_path
        with open(json_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

        self.output_dir = json_path.parent / "obsidian"
        self.questions_dir = self.output_dir / "questions"
        self.by_type_dir = self.output_dir / "by_type"
        self.by_tag_dir = self.output_dir / "by_tag"

        # 创建目录
        self.output_dir.mkdir(exist_ok=True)
        self.questions_dir.mkdir(exist_ok=True)
        self.by_type_dir.mkdir(exist_ok=True)
        self.by_tag_dir.mkdir(exist_ok=True)

    def clean_filename(self, name: str) -> str:
        """清理文件名，移除非法字符"""
        # 替换 LaTeX 命令为简短描述
        replacements = {
            r'\\left|\\right|\\lvert|\\rvert': '',
            r'\\frac\{(\w+)\{(\w+)\}': r'\1_\2',
            r'\\sin': 'sin',
            r'\\cos': 'cos',
            r'\\tan': 'tan',
            r'\\overrightarrow': 'vec',
            r'\\theta': 'theta',
            r'\\pi': 'pi',
            r'\\alpha': 'alpha',
            r'\\beta': 'beta',
            r'\\omega': 'omega',
            r'\{|\}|\$': '',
            r'\\': '',
            r'\s+': ' ',
        }

        for pattern, repl in replacements.items():
            name = re.sub(pattern, repl, name)

        # 移除其他非法字符
        name = re.sub(r'[<>:"/\\|?*]', '', name)
        name = name.strip()
        return name[:40]  # 限制长度

    def generate_frontmatter(self, question: Dict, exam_info: Dict) -> str:
        """生成 Obsidian frontmatter"""
        tags = question.get('tags', [])
        difficulty = question.get('difficulty', '基础')

        # 转换为 Obsidian 标签格式
        obsidian_tags = '[' + ', '.join([f'"{t}"' for t in tags]) + ']'

        fm = f"""---
title: "第 {question['number']} 题"
exam: "{exam_info['title']}"
subject: "{exam_info['subject']}"
grade: "{exam_info['grade']}"
type: "{question['type']}"
difficulty: "{difficulty}"
tags: {obsidian_tags}
created: {datetime.now().strftime('%Y-%m-%d')}
---

"""
        return fm

    def format_question_markdown(self, question: Dict, exam_info: Dict) -> str:
        """将题目格式化为 Markdown"""
        difficulty = question.get('difficulty', '基础')
        md = self.generate_frontmatter(question, exam_info)

        # 题干
        md += f"## 题目\n\n{question['content']}\n\n"

        # 选择题选项
        if question.get('options'):
            md += "### 选项\n\n"
            for opt_key, opt_val in question['options'].items():
                md += f"- **{opt_key}.** {opt_val}\n"
            md += "\n"

        # 答案
        if question.get('answer'):
            md += f"## 答案\n\n<!-- answer: {question['answer']} -->\n{question['answer']}\n\n"

        # 解析
        if question.get('analysis'):
            md += f"## 解析\n\n{question['analysis']}\n\n"

        # 图片
        if question.get('images'):
            md += "## 图片\n\n"
            for img in question['images']:
                md += f"![{Path(img).stem}]({img})\n"
            md += "\n"

        # 元信息
        md += "---\n\n"
        md += f"> 题号: {question['number']} | 题型: {question['type']} | 难度: {difficulty}\n"

        return md

    def export_questions(self) -> List[str]:
        """导出每道题目为独立文件"""
        exported_files = []

        for q in self.data['questions']:
            # 生成文件名
            filename = f"q{q['number']}_{self.clean_filename(q['content'][:20])}.md"
            filepath = self.questions_dir / filename

            # 写入文件
            content = self.format_question_markdown(q, self.data['exam_info'])
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            exported_files.append(str(filepath.relative_to(self.output_dir)))

        return exported_files

    def export_by_type(self):
        """按题型分类导出"""
        type_groups = {}

        for q in self.data['questions']:
            q_type = q['type']
            if q_type not in type_groups:
                type_groups[q_type] = []
            type_groups[q_type].append(q)

        for q_type, questions in type_groups.items():
            filepath = self.by_type_dir / f"{q_type}.md"

            md = f"""# {q_type}

> 来源: {self.data['exam_info']['title']}
> 总题数: {len(questions)} 题

## 题目列表

"""
            for q in questions:
                filename = f"q{q['number']}_{self.clean_filename(q['content'][:20])}.md"
                md += f"- [[{filename}|第 {q['number']} 题]] "
                md += f"- {q['content'][:50]}..."
                if q.get('tags'):
                    md += f" ({', '.join(q['tags'][:3])})"
                md += "\n"

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(md)

    def export_by_tag(self):
        """按知识点分类导出"""
        tag_groups = {}

        for q in self.data['questions']:
            for tag in q.get('tags', []):
                if tag not in ['基础', '较难', '选择题', '填空题', '解答题']:
                    if tag not in tag_groups:
                        tag_groups[tag] = []
                    tag_groups[tag].append(q)

        for tag, questions in tag_groups.items():
            # 创建以知识点命名的文件夹
            tag_dir = self.by_tag_dir / self.clean_filename(tag)
            tag_dir.mkdir(exist_ok=True)

            # 创建索引文件
            filepath = tag_dir / "index.md"
            md = f"""# {tag}

> 包含 {len(questions)} 道相关题目

## 题目列表

"""
            for q in questions:
                filename = f"q{q['number']}_{self.clean_filename(q['content'][:20])}.md"
                md += f"- [[questions/{filename}|第 {q['number']} 题]] - {q['type']}\n"

            # 创建知识点说明文件
            readme = f"""# {tag}

**相关题目**: {len(questions)} 道

## 题目

"""
            for q in questions:
                filename = f"q{q['number']}_{self.clean_filename(q['content'][:20])}.md"
                readme += f"- [[questions/{filename}|第 {q['number']} 题]]: {q['content'][:60]}...\n"

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(readme)

    def export_index(self, question_files: List[str]):
        """导出总索引页面"""
        exam_info = self.data['exam_info']

        md = f"""# {exam_info['title']}

> 数学 | {exam_info['grade']} | 共 {self.data['total_questions']} 题

## 考试信息

- **科目**: {exam_info['subject']}
- **年级**: {exam_info['grade']}
- **总题数**: {self.data['total_questions']}

## 题型统计

| 题型 | 数量 |
|:---|:---:|
"""

        # 统计各题型数量
        type_counts = {}
        for q in self.data['questions']:
            t = q['type']
            type_counts[t] = type_counts.get(t, 0) + 1

        for t, count in type_counts.items():
            md += f"| {t} | {count} |\n"

        md += """
## 知识点分布

```dataview
TABLE type, difficulty, tags
FROM "obsidian/questions"
SORT number ASC
```

## 解答题 (较难)

"""
        # 列出所有解答题
        for q in self.data['questions']:
            if q['type'] == '解答题':
                filename = f"q{q['number']}_{self.clean_filename(q['content'][:20])}.md"
                md += f"- [[questions/{filename}|第 {q['number']} 题]]: {q['content'][:60]}...\n"

        md += """
## 按题型查看

- [[by_type/选择题|选择题]]
- [[by_type/填空题|填空题]]
- [[by_type/解答题|解答题]]

## 按知识点查看

"""
        # 列出知识点文件夹
        for item in sorted(self.by_tag_dir.iterdir()):
            if item.is_dir():
                md += f"- [[by_tag/{item.name}|{item.name}]]\n"

        md += """
---

*由 math_paper_parser.py 自动生成*
"""

        with open(self.output_dir / "index.md", 'w', encoding='utf-8') as f:
            f.write(md)

    def export_dataview_queries(self):
        """导出常用的 Dataview 查询示例"""
        queries_md = """# Dataview 查询示例

## 按难度筛选

### 基础题
```dataview
TABLE type, number, tags
FROM "obsidian/questions"
WHERE difficulty = "基础"
SORT number ASC
```

### 较难题
```dataview
TABLE type, number, tags
FROM "obsidian/questions"
WHERE difficulty = "较难"
SORT number ASC
```

## 按题型筛选

### 解答题
```dataview
TABLE number, tags, analysis
FROM "obsidian/questions"
WHERE type = "解答题"
SORT number ASC
```

## 按知识点筛选

### 三角函数
```dataview
TABLE number, type
FROM "obsidian/questions"
WHERE contains(tags, "三角函数")
SORT number ASC
```

### 平面向量
```dataview
TABLE number, type
FROM "obsidian/questions"
WHERE contains(tags, "平面向量")
SORT number ASC
```

---

*查询示例文件，仅供参考*
"""

        with open(self.output_dir / "dataview-queries.md", 'w', encoding='utf-8') as f:
            f.write(queries_md)

    def export_student_version(self):
        """导出学生版（隐藏答案和解析）"""
        student_dir = self.output_dir / "student_version"
        student_dir.mkdir(exist_ok=True)

        for q in self.data['questions']:
            filename = f"q{q['number']}_{self.clean_filename(q['content'][:20])}.md"
            filepath = student_dir / filename

            md = f"""# 第 {q['number']} 题 ({q['type']})

**难度**: {q.get('difficulty', '基础')}

## 题目

{q['content']}

"""

            # 选择题选项
            if q.get('options'):
                md += "### 选项\n\n"
                for opt_key, opt_val in q['options'].items():
                    md += f"- **{opt_key}.** {opt_val}\n"
                md += "\n"

            # 答案区域（留空让学生填写）
            if q['type'] == '选择题':
                md += "## 答案\n\n___ \n\n"
            elif q['type'] == '填空题':
                md += "## 答案\n\n___ \n\n"
            else:
                md += "## 解答\n\n\n\n\n"

            # 知识点提示
            tags = [t for t in q.get('tags', []) if t not in ['基础', '较难', '选择题', '填空题', '解答题']]
            if tags:
                md += f"---\n**知识点**: {', '.join(tags)}\n"

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(md)

        # 学生
        index_md = f"""#版索引 学生版 - {self.data['exam_info']['title']}

> 共 {self.data['total_questions']} 题

## 题目列表

"""
        for q in self.data['questions']:
            filename = f"q{q['number']}_{self.clean_filename(q['content'][:20])}.md"
            index_md += f"- [[{filename}|第 {q['number']} 题]] ({q['type']})\n"

        with open(student_dir / "index.md", 'w', encoding='utf-8') as f:
            f.write(index_md)

    def export_all(self):
        """执行完整导出流程"""
        print(f"📄 正在导出: {self.data['exam_info']['title']}")

        # 1. 导出每道题目
        print("  📝 导出题目文件...")
        question_files = self.export_questions()
        print(f"     已导出 {len(question_files)} 道题目")

        # 2. 按题型分类
        print("  📂 按题型分类...")
        self.export_by_type()

        # 3. 按知识点分类
        print("  🏷️ 按知识点分类...")
        self.export_by_tag()

        # 4. 导出总索引
        print("  📋 生成索引页面...")
        self.export_index(question_files)

        # 5. 导出 Dataview 查询示例
        print("  🔍 生成查询示例...")
        self.export_dataview_queries()

        # 6. 导出学生版
        print("  🎓 生成学生版...")
        self.export_student_version()

        print(f"\n✅ 导出完成！")
        print(f"📁 输出目录: {self.output_dir}")
        print(f"""
📂 目录结构:
   ├── index.md              # 总索引
   ├── dataview-queries.md   # 查询示例
   ├── questions/            # 题目文件 (共 {len(question_files)} 个)
   ├── by_type/             # 按题型分类
   │   ├── 选择题.md
   │   ├── 填空题.md
   │   └── 解答题.md
   ├── by_tag/              # 按知识点分类
   └── student_version/     # 学生版 (答案隐藏)
""")


# ====================== 使用方法 ======================
if __name__ == "__main__":
    # 查找 JSON 文件
    script_dir = Path(__file__).parent
    json_files = list(script_dir.glob("*_parsed.json"))

    if not json_files:
        print("❌ 未找到 *_parsed.json 文件")
        print(f"📂 当前目录: {script_dir}")
        print("请先运行 math_paper_parser.py 生成 JSON 文件")
    else:
        # 使用最新的 JSON 文件
        json_file = max(json_files, key=lambda p: p.stat().st_mtime)
        print(f"📂 使用文件: {json_file.name}\n")

        exporter = ObsidianExporter(json_file)
        exporter.export_all()
