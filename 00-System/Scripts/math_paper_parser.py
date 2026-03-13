"""
数学试卷解析器 (MathPaperParser)
用于解析 Markdown 格式的数学试卷，提取题目、答案、解析和知识点标签

使用方法:
    python math_paper_parser.py

输入:
    与脚本同目录下的 .md 文件 (如 2024-2025年上海市七宝中学高一下期中教师版.md)

输出:
    同名 JSON 文件 (如 2024-2025年上海市七宝中学高一下期中_parsed.json)
"""

import re
import json
from pathlib import Path
from typing import List, Dict, Any


class MathPaperParser:
    """数学试卷 Markdown 解析器"""

    def __init__(self):
        # 答案提取正则
        self.answer_pattern = re.compile(r'【答案】\s*(.+?)(?=\n【解析】|\n##|\Z)', re.DOTALL)
        # 解析提取正则
        self.analysis_pattern = re.compile(r'【解析】\s*(.+?)(?=\n\d+\.|\n##|\Z)', re.DOTALL)
        # 图片提取正则
        self.image_pattern = re.compile(r'!\[.*?\]\((.*?)\)')

        # 高一数学下学期核心知识点映射（可继续扩展）
        self.tag_map = {
            r'sin a|cos θ|tan θ|终边|象限角': ['三角函数', '任意角三角函数'],
            r'扇形|弧长|圆心角|弧度': ['三角函数', '扇形面积与弧长'],
            r'定义域|ln|tan x': ['函数', '函数定义域'],
            r'向量|overrightarrow|数量积|共线': ['平面向量', '向量线性运算', '向量数量积'],
            r'三角形|正弦定理|余弦定理|AB=BC': ['解三角形', '三角形性质'],
            r'对称|周期|单调|极大值|极小值': ['函数性质', '三角函数图象与性质'],
            r'f\(x\) =|g\(x\) =': ['函数', '函数解析式'],
            r'取值范围|最大值|最小值|当且仅当': ['不等式与最值', '参数讨论'],
        }

    def clean_text(self, text: str) -> str:
        """清理文本空白"""
        if not text:
            return ""
        text = re.sub(r'\n+', '\n', text.strip())
        return text.strip()

    def get_tags(self, content: str, q_type: str) -> List[str]:
        """
        根据题目内容自动提取知识点标签

        Args:
            content: 题目完整内容
            q_type: 题目类型（选择题、填空题、解答题）

        Returns:
            知识点标签列表
        """
        tags = [q_type]
        content_lower = content.lower()

        # 关键词匹配
        for keyword, tag_list in self.tag_map.items():
            if re.search(keyword, content_lower, re.IGNORECASE):
                tags.extend(tag_list)

        # 难度粗判
        if (len(content) > 300
            or '当且仅当' in content
            or '取值范围' in content
            or '最大值' in content
            or '最小值' in content):
            tags.append('较难')
        else:
            tags.append('基础')

        # 去重
        return list(dict.fromkeys(tags))

    def parse_paper(self, md_content: str, exam_title: str = "") -> Dict[str, Any]:
        """
        解析试卷 Markdown 内容

        Args:
            md_content: Markdown 文件内容
            exam_title: 考试标题（可选）

        Returns:
            解析后的 JSON 结构
        """
        questions: List[Dict] = []

        # 1. 分大题型 (一、选择题 二、填空题 三、解答题)
        sections = re.split(r'##\s*[一二三]、(.+?)\n', md_content)
        current_type = ""
        i = 0

        while i < len(sections):
            if i % 2 == 1:  # 题型标题行
                current_type = sections[i].strip()
            else:
                if current_type and i < len(sections):
                    section_text = sections[i]

                    # 2. 提取每道小题
                    q_matches = re.finditer(
                        r'^(\d+)\.\s*(.+?)(?=^\d+\.|\Z)',
                        section_text,
                        re.DOTALL | re.MULTILINE
                    )

                    for match in q_matches:
                        q_num = int(match.group(1))
                        full_q = match.group(2).strip()

                        # 提取答案、解析
                        answer_match = self.answer_pattern.search(full_q)
                        analysis_match = self.analysis_pattern.search(full_q)

                        answer = self.clean_text(answer_match.group(1)) if answer_match else ""
                        analysis = self.clean_text(analysis_match.group(1)) if analysis_match else ""

                        # 题干（去掉答案和解析部分）
                        content = full_q
                        if answer_match:
                            content = content.replace(answer_match.group(0), "")
                        if analysis_match:
                            content = content.replace(analysis_match.group(0), "")
                        content = self.clean_text(content)

                        # 提取图片
                        images = self.image_pattern.findall(full_q)

                        # 选择题选项提取
                        options = None
                        if current_type == '选择题':
                            opt_matches = re.findall(
                                r'([A-D])\.\s*(.+?)(?=\n[A-D]\.|【解析】|\Z)',
                                full_q,
                                re.DOTALL
                            )
                            if opt_matches:
                                options = {m[0]: self.clean_text(m[1]) for m in opt_matches}

                        # 生成标签
                        tags = self.get_tags(full_q, current_type)

                        # 构建题目对象
                        question = {
                            "number": q_num,
                            "type": current_type,
                            "content": content,           # 题干（保留LaTeX）
                            "options": options,           # 选择题选项
                            "answer": answer,             # 答案
                            "analysis": analysis,         # 解析
                            "images": images,             # 图片路径列表
                            "tags": tags,                 # 知识点标签
                            "difficulty": "较难" if "较难" in tags else "基础"
                        }
                        questions.append(question)
            i += 1

        return {
            "exam_info": {
                "title": exam_title or "2024-2025 年七宝中学高一下期中",
                "subject": "数学",
                "grade": "高一"
            },
            "total_questions": len(questions),
            "questions": questions
        }


# ====================== 使用方法 ======================
if __name__ == "__main__":
    parser = MathPaperParser()

    # 把你的MD文件路径改这里（和脚本放同一文件夹即可）
    file_path = Path("2024-2025年上海市七宝中学高一下期中教师版.md")

    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            md_text = f.read()

        result = parser.parse_paper(md_text, "2024-2025 年七宝中学高一下期中")

        # 保存 JSON
        output_path = file_path.with_name(file_path.stem + "_parsed.json")
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        print(f"🎉 解析完成！共 {result['total_questions']} 道题")
        print(f"📁 JSON 已保存至: {output_path}")

        # 预览前3道题
        for q in result['questions'][:3]:
            print(f"\n第 {q['number']} 题 [{q['type']}]  →  Tags: {', '.join(q['tags'])}")
            print("题干:", q['content'][:80] + "..." if len(q['content']) > 80 else q['content'])
    else:
        print("❌ 文件不存在，请检查路径！")
        print(f"📂 当前目录: {Path.cwd()}")
        print("📋 目录中的 .md 文件:")
        for f in Path(".").glob("*.md"):
            print(f"  - {f.name}")
