#!/usr/bin/env python3
"""
MD 转 LaTeX 生成器 - 生成学生版和教师版双版本
"""

import re
import sys
from pathlib import Path
from typing import Tuple, List

# 导入增强版考点分析生成器
try:
    from enhanced_analysis import EnhancedAnalysisGenerator
    HAS_ENHANCED_ANALYSIS = True
except ImportError:
    HAS_ENHANCED_ANALYSIS = False


class MD2TeXConverter:
    """MD 转 LaTeX 转换器"""
    
    def __init__(self):
        self.blank_config = {
            '基础': 0,
            '中档': 3,
            '较难': 8,
            '压轴': 15
        }
        if HAS_ENHANCED_ANALYSIS:
            self.analysis_generator = EnhancedAnalysisGenerator()
        else:
            self.analysis_generator = None
    
    def _auto_difficulty(self, q_num: int) -> Tuple[str, str]:
        """根据题号自动判断难度"""
        if 1 <= q_num <= 6:
            return '基础', 'noblank'
        elif 7 <= q_num <= 16:
            return '中档', 'small'
        elif 17 <= q_num <= 20:
            return '较难', 'full'
        else:
            return '压轴', 'double'
    
    def parse_md(self, content: str) -> List[dict]:
        """解析 MD 为结构化数据"""
        questions = []
        current_q = None
        lines = content.split('\n')
        
        for line in lines:
            # 检测题目开始 - 支持两种格式：
            # 1. ## 【第 N 题】（难度）
            # 2. N. 题目内容（标准试卷格式）
            
            # 格式1：标准格式
            q_match = re.match(r'^##?\s*【第\s*(\d+)\s*题】\s*（([^）]+)）', line)
            if q_match:
                if current_q:
                    questions.append(current_q)
                current_q = {
                    'num': int(q_match.group(1)),
                    'difficulty': q_match.group(2),
                    'content': [],
                    'answer': '',
                    'solution': '',
                    'analysis': '',
                    'tips': '',
                    'image': None
                }
                continue
            
            # 格式2：试卷格式（如 "1. 集合 A = ..."）
            q_match2 = re.match(r'^(\d+)\.\s+(.+)$', line)
            if q_match2 and not line.startswith('##'):  # 避免匹配到标题
                q_num = int(q_match2.group(1))
                # 自动判断难度
                difficulty, _ = self._auto_difficulty(q_num)
                
                if current_q:
                    questions.append(current_q)
                current_q = {
                    'num': q_num,
                    'difficulty': difficulty,
                    'content': [q_match2.group(2)],
                    'answer': '',
                    'solution': '',
                    'analysis': '',
                    'tips': '',
                    'image': None
                }
                continue
            
            if current_q:
                # 检测答案
                if line.startswith('【答案】'):
                    current_q['answer'] = line[4:].strip()
                # 检测解析
                elif line.startswith('【解析】'):
                    current_q['solution'] = line[4:].strip() + '\n'
                elif current_q['solution'] and not line.startswith('【'):
                    current_q['solution'] += line + '\n'
                # 检测考点分析
                elif line.startswith('【考点分析】'):
                    current_q['analysis'] = line[6:].strip()
                # 检测易错点
                elif line.startswith('【易错点】'):
                    current_q['tips'] = line[5:].strip()
                # 检测图片
                elif '<!-- 图：' in line:
                    img_match = re.search(r'<!-- 图：(.+?) -->', line)
                    if img_match:
                        current_q['image'] = img_match.group(1)
                else:
                    current_q['content'].append(line)
        
        if current_q:
            questions.append(current_q)
        
        return questions
    
    def generate_student_version(self, questions: List[dict], title: str) -> str:
        """生成学生版 LaTeX"""
        tex = self._preamble_student()
        tex += f"\\title{{{title}（学生版）}}\n"
        tex += "\\date{}\n"
        tex += "\\begin{document}\n\n"
        tex += "\\maketitle\n\n"
        
        for q in questions:
            tex += self._question_student(q)
        
        tex += "\\end{document}\n"
        return tex
    
    def generate_teacher_version(self, questions: List[dict], title: str) -> str:
        """生成教师版 LaTeX"""
        tex = self._preamble_teacher()
        tex += f"\\title{{{title}（教师版）}}\n"
        tex += "\\date{}\n"
        tex += "\\begin{document}\n\n"
        tex += "\\maketitle\n\n"
        
        for q in questions:
            tex += self._question_teacher(q)
        
        tex += "\\end{document}\n"
        return tex
    
    def _preamble_student(self) -> str:
        """学生版 preamble - 基于 maki 样式"""
        return r'''\documentclass[a4paper,12pt]{ctexart}

% 页面设置
\usepackage[a4paper, left=2.5cm, right=2.5cm, top=2.5cm, bottom=2.5cm]{geometry}
\usepackage{fancyhdr}
\usepackage{amsmath, amssymb, amsthm, mathtools}
\usepackage{mathpazo}
\usepackage[most]{tcolorbox}
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{needspace}

% 字体
\setmainfont{TeX Gyre Pagella}
\setCJKmainfont[
    BoldFont = Noto Serif CJK SC Bold,
    ItalicFont = Noto Serif CJK SC Light
]{Noto Serif CJK SC}
\newCJKfontfamily\kaishu{FandolKai-Regular}

% 颜色定义（maki 原版配色）
\definecolor{LogicColor}{RGB}{200, 80, 110}
\definecolor{LogicBg}{RGB}{255, 240, 245}
\definecolor{DefColor}{RGB}{210, 105, 30}
\definecolor{DefBg}{RGB}{255, 250, 240}
\definecolor{ExColor}{RGB}{70, 130, 180}
\definecolor{ExBg}{RGB}{240, 248, 255}
\definecolor{NoteColor}{RGB}{34, 139, 34}

% 题目环境
\tcbset{
    questionbox/.style={
        enhanced,
        colback=white,
        colframe=LogicColor,
        boxrule=0.5pt,
        sharp corners,
        left=3mm, right=3mm, top=2mm, bottom=2mm,
        before skip=1em, after skip=1em,
        fonttitle=\bfseries\kaishu,
        title={第~\thequestion~题}
    }
}

\newcounter{question}
\newenvironment{question}[1][]{%
    \refstepcounter{question}%
    \begin{tcolorbox}[questionbox, #1]%
}{%
    \end{tcolorbox}%
}

% 留白命令
\newcommand{\blankspace}[1]{%
    \vspace{#1}%
    \par\noindent\textit{（答题区域）}%
    \vspace{0.5cm}%
}

% 防跨页
\newcommand{\questionstart}{\needspace{5cm}}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[C]{\kaishu 学生版 · 请勿提前翻阅答案}
\fancyfoot[C]{\thepage}

'''
    
    def _preamble_teacher(self) -> str:
        """教师版 preamble - 基于 maki 样式，增加分析框"""
        return r'''\documentclass[a4paper,12pt]{ctexart}

% 页面设置
\usepackage[a4paper, left=2.5cm, right=2.5cm, top=2.5cm, bottom=2.5cm]{geometry}
\usepackage{fancyhdr}
\usepackage{amsmath, amssymb, amsthm, mathtools}
\usepackage{mathpazo}
\usepackage[most]{tcolorbox}
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{booktabs}

% 字体
\setmainfont{TeX Gyre Pagella}
\setCJKmainfont[
    BoldFont = Noto Serif CJK SC Bold,
    ItalicFont = Noto Serif CJK SC Light
]{Noto Serif CJK SC}
\newCJKfontfamily\kaishu{FandolKai-Regular}

% 颜色定义（maki 原版配色）
\definecolor{LogicColor}{RGB}{200, 80, 110}
\definecolor{LogicBg}{RGB}{255, 240, 245}
\definecolor{DefColor}{RGB}{210, 105, 30}
\definecolor{DefBg}{RGB}{255, 250, 240}
\definecolor{ExColor}{RGB}{70, 130, 180}
\definecolor{ExBg}{RGB}{240, 248, 255}
\definecolor{NoteColor}{RGB}{34, 139, 34}
\definecolor{NoteBg}{RGB}{240, 255, 240}

% 题目环境
\tcbset{
    questionbox/.style={
        enhanced,
        colback=white,
        colframe=LogicColor,
        boxrule=0.5pt,
        sharp corners,
        left=3mm, right=3mm, top=2mm, bottom=2mm,
        before skip=1em, after skip=1em,
        fonttitle=\bfseries\kaishu,
        title={第~\thequestion~题}
    },
    analysisbox/.style={
        enhanced,
        colback=NoteBg,
        colframe=NoteColor,
        boxrule=0.5pt,
        sharp corners,
        left=3mm, right=3mm, top=2mm, bottom=2mm,
        before skip=0.5em, after skip=0.5em,
        fonttitle=\bfseries\kaishu\color{NoteColor},
        title={考点分析}
    },
    answerbox/.style={
        enhanced,
        colback=DefBg,
        colframe=DefColor,
        boxrule=0.5pt,
        sharp corners,
        left=3mm, right=3mm, top=2mm, bottom=2mm,
        before skip=0.5em, after skip=0.5em,
        fonttitle=\bfseries\kaishu\color{DefColor},
        title={答案与解析}
    }
}

\newcounter{question}
\newenvironment{question}[1][]{%
    \refstepcounter{question}%
    \begin{tcolorbox}[questionbox, #1]%
}{%
    \end{tcolorbox}%
}

\newenvironment{analysis}[1][]{%
    \begin{tcolorbox}[analysisbox, #1]%
}{%
    \end{tcolorbox}%
}

\newenvironment{answer}[1][]{%
    \begin{tcolorbox}[answerbox, #1]%
}{%
    \end{tcolorbox}%
}

% 考点分析框
\newtcolorbox{analysisbox}[1]{%
    enhanced,
    colback=DefBg,
    colframe=DefColor,
    boxrule=0.5pt,
    sharp corners,
    left=3mm, right=3mm, top=2mm, bottom=2mm,
    before skip=0.5em, after skip=0.5em,
    fonttitle=\bfseries\kaishu\color{DefColor},
    title={#1}
}

% 提示框
\newtcolorbox{tipbox}[1]{%
    enhanced,
    colback=NoteBg,
    colframe=NoteColor,
    boxrule=0.5pt,
    sharp corners,
    left=3mm, right=3mm, top=2mm, bottom=2mm,
    before skip=0.5em, after skip=0.5em,
    fonttitle=\bfseries\kaishu\color{NoteColor},
    title={#1}
}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[C]{\kaishu 教师版 · 含完整解析与考点分析}
\fancyfoot[C]{\thepage}

'''
    
    def _question_student(self, q: dict) -> str:
        """生成学生版题目"""
        tex = f"\\questionstart\n"
        tex += f"\\begin{{question}}\n"
        
        # 题目内容
        content = '\n'.join(q['content'])
        content = self._md_to_latex(content)
        tex += content + '\n'
        
        # 图片
        if q['image']:
            tex += f"\\vspace{{0.5cm}}\n"
            tex += f"\\textit{{【图形区域：{q['image']}】}}\n"
            tex += f"\\vspace{{0.5cm}}\n"
        
        # 根据难度添加留白
        difficulty = q['difficulty']
        blank_cm = self.blank_config.get(difficulty, 3)
        
        if blank_cm > 0:
            tex += f"\\blankspace{{{blank_cm}cm}}\n"
        
        tex += "\\end{question}\n\n"
        return tex
    
    def _question_teacher(self, q: dict) -> str:
        """生成教师版题目"""
        tex = f"\\begin{{question}}\n"
        
        # 题目内容
        content = '\n'.join(q['content'])
        content = self._md_to_latex(content)
        tex += content + '\n'
        
        # 图片
        if q['image']:
            tex += f"\\vspace{{0.3cm}}\n"
            tex += f"\\textit{{【图形：{q['image']}】}}\n"
            tex += f"\\vspace{{0.3cm}}\n"
        
        tex += "\\end{question}\n\n"
        
        # 答案与解析框
        tex += "\\begin{answer}\n"
        if q['answer']:
            answer = self._md_to_latex(q['answer'])
            tex += f"\\textbf{{答案：}}{answer}\n\n"
        if q['solution']:
            solution = self._md_to_latex(q['solution'])
            tex += f"\\textbf{{解析：}}{solution}\n"
        tex += "\\end{answer}\n\n"
        
        # 考点分析框 - 使用增强版分析
        if self.analysis_generator:
            # 使用 AI 生成深度考点分析
            try:
                analysis_data = self.analysis_generator.analyze_question(
                    q_num=q['number'],
                    content=q['content'],
                    answer=q['answer'] or '',
                    difficulty=q['difficulty']
                )
                latex_analysis = self.analysis_generator.generate_latex_analysis(analysis_data)
                tex += latex_analysis + '\n\n'
            except Exception as e:
                # 如果 AI 分析失败，回退到基础分析
                print(f"  警告：第{q['number']}题考点分析生成失败，使用基础分析")
                tex += self._generate_basic_analysis(q)
        else:
            tex += self._generate_basic_analysis(q)
        
        return tex
    
    def _generate_basic_analysis(self, q: dict) -> str:
        """生成基础考点分析（回退方案）"""
        tex = "\\begin{analysisbox}{考点分析}\n"
        tex += f"  \\textbf{{难度评级：}}{q['difficulty']}\\par\n"
        if q['analysis']:
            analysis = self._md_to_latex(q['analysis'])
            tex += f"  \\textbf{{核心考点：}}{analysis}\n"
        tex += "\\end{analysisbox}\n\n"
        
        if q['tips']:
            tex += "\\begin{tipbox}{易错警示}\n"
            tips = self._md_to_latex(q['tips'])
            tex += f"  {tips}\n"
            tex += "\\end{tipbox}\n\n"
        
        return tex
    
    def _md_to_latex(self, text: str) -> str:
        """MD 格式转 LaTeX"""
        # 数学公式已经是 $...$ 格式，保持不变
        # 粗体
        text = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', text)
        # 斜体
        text = re.sub(r'\*(.+?)\*', r'\\textit{\1}', text)
        # 换行
        text = text.replace('\n\n', '\n\n\\par\n')
        return text
    
    def convert(self, input_path: str, output_dir: str) -> Tuple[str, str]:
        """执行转换"""
        # 读取优化后的 MD
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 解析题目
        questions = self.parse_md(content)
        
        # 提取标题
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else '数学试卷'
        
        # 生成双版本
        student_tex = self.generate_student_version(questions, title)
        teacher_tex = self.generate_teacher_version(questions, title)
        
        # 保存
        base_name = Path(input_path).stem.replace('-optimized', '')
        student_path = Path(output_dir) / f"{base_name}-学生版.tex"
        teacher_path = Path(output_dir) / f"{base_name}-教师版.tex"
        
        student_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(student_path, 'w', encoding='utf-8') as f:
            f.write(student_tex)
        with open(teacher_path, 'w', encoding='utf-8') as f:
            f.write(teacher_tex)
        
        print(f"学生版已生成：{student_path}")
        print(f"教师版已生成：{teacher_path}")
        
        return str(student_path), str(teacher_path)


def main():
    """命令行入口"""
    if len(sys.argv) < 2:
        print("用法: python md2tex.py <optimized.md> [output_dir]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else './tex'
    
    converter = MD2TeXConverter()
    converter.convert(input_file, output_dir)


if __name__ == '__main__':
    main()
