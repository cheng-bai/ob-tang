#!/usr/bin/env python3
"""
MD 优化器 - 将原始 MD 试卷转换为标准化格式
"""

import re
import sys
from pathlib import Path
from typing import Tuple, Optional


class MDOptimizer:
    """MD 优化器"""
    
    def __init__(self):
        self.difficulty_map = {
            'basic': list(range(1, 7)),      # 1-6 基础
            'medium': list(range(7, 19)),     # 7-18 中档
            'hard': [19, 20],                  # 19-20 难题
            'challenge': [21]                   # 21 压轴
        }
    
    def auto_difficulty(self, q_num: int) -> Tuple[str, str]:
        """根据题号自动判断难度"""
        if q_num in self.difficulty_map['basic']:
            return '基础', 'noblank'
        elif q_num in self.difficulty_map['medium']:
            return '中档', 'small'
        elif q_num in self.difficulty_map['hard']:
            return '较难', 'full'
        else:
            return '压轴', 'double'
    
    def normalize_formulas(self, text: str) -> str:
        """标准化数学公式"""
        # 修复常见符号
        replacements = {
            '°': '^\\circ',
            '×': '\\times',
            '÷': '\\div',
            '≤': '\\leqslant',
            '≥': '\\geqslant',
            '≠': '\\neq',
            '∈': '\\in',
            '⊆': '\\subseteq',
            '∩': '\\cap',
            '∪': '\\cup',
            '∅': '\\emptyset',
            '∞': '\\infty',
            '→': '\\to',
            '⇒': '\\Rightarrow',
            '⇔': '\\Leftrightarrow',
            'α': '\\alpha',
            'β': '\\beta',
            'γ': '\\gamma',
            'θ': '\\theta',
            'π': '\\pi',
            'ω': '\\omega',
            'Δ': '\\Delta',
            'Σ': '\\sum',
            '√': '\\sqrt',
            '·': '\\cdot',
        }
        
        for old, new in replacements.items():
            text = text.replace(old, new)
        
        # 确保 $...$ 内是行内公式
        # 修复 $$...$$ 为 \[...\]
        text = re.sub(r'\$\$(.+?)\$\$', r'\\[\1\\]', text, flags=re.DOTALL)
        
        return text
    
    def extract_question_info(self, line: str) -> Optional[dict]:
        """提取题目信息"""
        # 匹配题号
        patterns = [
            r'^##?\s*【第\s*(\d+)\s*题】',
            r'^##?\s*(\d+)\.\s*',
            r'^##?\s*【第\s*(\d+)-(\d+)\s*题】',
        ]
        
        for pattern in patterns:
            match = re.match(pattern, line)
            if match:
                if '-' in pattern:
                    start, end = match.groups()
                    return {'type': 'range', 'start': int(start), 'end': int(end)}
                else:
                    return {'type': 'single', 'num': int(match.group(1))}
        return None
    
    def add_difficulty_tag(self, line: str, q_num: int) -> str:
        """添加难度标签"""
        difficulty, _ = self.auto_difficulty(q_num)
        
        # 如果已经有难度标签，不重复添加
        if '（' in line and '）' in line:
            return line
        
        # 在题号后添加难度
        if '【第' in line and '题】' in line:
            line = line.rstrip() + f'（{difficulty}）\n'
        
        return line
    
    def normalize_structure(self, content: str) -> str:
        """标准化整体结构"""
        lines = content.split('\n')
        result = []
        current_q_num = 0
        
        for line in lines:
            # 提取题号
            q_info = self.extract_question_info(line)
            if q_info:
                if q_info['type'] == 'single':
                    current_q_num = q_info['num']
                    line = self.add_difficulty_tag(line, current_q_num)
                elif q_info['type'] == 'range':
                    # 处理题组
                    pass
            
            # 标准化答案标记
            line = re.sub(r'^[\s]*答案[:：]', '【答案】', line)
            line = re.sub(r'^[\s]*解析[:：]', '【解析】', line)
            line = re.sub(r'^[\s]*考点[:：]', '【考点分析】', line)
            line = re.sub(r'^[\s]*易错[:：]', '【易错点】', line)
            
            # 标准化图片占位
            line = re.sub(r'!\[.*?\]\(.*?\)', self._convert_image, line)
            
            result.append(line)
        
        return '\n'.join(result)
    
    def _convert_image(self, match) -> str:
        """转换图片为占位符"""
        # 提取图片描述（如果有）
        return '<!-- 图：请补充图形描述 -->'
    
    def add_exam_info(self, content: str, filename: str) -> str:
        """添加考试信息头"""
        # 从文件名提取信息
        # 例如：2026届崇明区高三二模数学试卷.md
        year_match = re.search(r'(\d{4})届', filename)
        district_match = re.search(r'([\u4e00-\u9fa5]+区)', filename)
        
        year = year_match.group(1) if year_match else '2026'
        district = district_match.group(1) if district_match else '上海'
        
        header = f"""# {year}届{district}高三二模数学试卷

**考试信息**：{year}年{district}高三下学期二模考试  
**试卷结构**：填空题 1-12 题（54 分），选择题 13-16 题（16 分），解答题 17-21 题（78 分）  
**考试时间**：120 分钟  
**满分**：150 分

---

"""
        
        return header + content
    
    def optimize(self, input_path: str, output_path: Optional[str] = None) -> str:
        """执行优化"""
        # 读取原始 MD
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 标准化公式
        content = self.normalize_formulas(content)
        
        # 标准化结构
        content = self.normalize_structure(content)
        
        # 添加考试信息
        filename = Path(input_path).name
        content = self.add_exam_info(content, filename)
        
        # 保存或返回
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"优化完成：{output_path}")
        
        return content


def main():
    """命令行入口"""
    if len(sys.argv) < 2:
        print("用法: python md_optimizer.py <input.md> [output.md]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    optimizer = MDOptimizer()
    optimizer.optimize(input_file, output_file)


if __name__ == '__main__':
    main()
