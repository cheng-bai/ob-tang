#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
试卷题目 → LaTeX Beamer PPT 转换器 (v2 — 等间距 / 正确换行 / 真实图片 / 更小字号)

直接读取试卷库标准格式 Markdown，智能分页生成课堂板书幻灯片。

用法示例:
    python md_to_ppt.py -i 崇明二模-optimized.md -q 1,3,5,10-12,15-17 -m student -o output.tex
"""

import re
import os
import sys
import argparse
from dataclasses import dataclass, field
from typing import List, Optional, Tuple


# ============================================================
# 数据模型
# ============================================================

@dataclass
class Question:
    """单道题目"""
    num: int                          # 题号
    qtype: str                        # 题型: 填空题/单选题/多选题/解答题
    body: str                         # 题干内容（已清理）
    options: List[str] = field(default_factory=list)  # 选择题选项
    answer: Optional[str] = None      # 答案
    parsing: Optional[str] = None     # 解析
    has_image: bool = False           # 是否包含图片占位
    image_desc: Optional[str] = None  # 图片描述（占位符用文字）
    image_path: Optional[str] = None  # 真实图片文件路径（img src）
    raw_lines: List[str] = field(default_factory=list)  # 原始行（调试用）

    def estimate_height(self) -> float:
        """估算题目在幻灯片上的空间占用（单位：cm）"""
        # 基础文本高度
        lines = self.body.count('\n') + 1
        height = lines * 0.45

        # 行内公式额外空间
        inline_formulas = len(re.findall(r'(?<!\$)\$(?!\$)[^$]+(?<!\$)\$(?!\$)', self.body))
        height += inline_formulas * 0.2

        # 行间公式额外空间
        display_formulas = len(re.findall(r'\$\$[\s\S]*?\$\$', self.body))
        height += display_formulas * 0.8

        # 图片占位（真实图片和占位框占相同空间）
        if self.has_image or self.image_path:
            height += 2.5

        # 选项
        if self.options:
            height += max(len(self.options) * 0.4, 1.0)

        # 小问标记 (1) (2) 等
        sub_questions = len(re.findall(r'\n\s*\(\d+\)', '\n' + self.body))
        height += sub_questions * 0.3

        # 答案和解析
        if self.answer:
            height += 0.6 + self.answer.count('\n') * 0.4
        if self.parsing:
            height += 0.6 + self.parsing.count('\n') * 0.35

        return height


@dataclass
class Frame:
    """一页幻灯片"""
    questions: List[Question] = field(default_factory=list)

    def total_height(self) -> float:
        # 题目之间需要间隔（在vfill排版中，此间隔仅用于字号判断）
        total = sum(q.estimate_height() for q in self.questions)
        total += (len(self.questions) - 1) * 0.8
        return total


# ============================================================
# 解析器
# ============================================================

class ExamParser:
    """解析试卷库标准格式 Markdown"""

    TYPE_MAP = {
        '填空': '填空题',
        '选择': '单选题',
        '单选': '单选题',
        '多选': '多选题',
        '解答': '解答题',
    }

    def __init__(self, content: str):
        self.content = content
        self.questions: List[Question] = []

    def parse(self) -> List[Question]:
        lines = self.content.split('\n')
        i = 0
        current_type = '未知'

        while i < len(lines):
            line = lines[i].strip()

            if not line:
                i += 1
                continue

            if i == 0 and not line.startswith('#') and not line.startswith('##'):
                i += 1
                continue

            # 识别题型章节: ## 一、填空题 或 三、解答题
            type_match = re.match(r'(?:##\s*)?[一二三四五六七八九十]+、\s*(.+)', line)
            if type_match and not re.match(r'(?:##\s*)?\d+\.', line):
                current_type = self._normalize_type(type_match.group(1))
                i += 1
                continue

            # 识别题目: 支持 1. xxx 或 ## 18. xxx
            q_match = re.match(r'(?:##\s*)?(\d+)\.\s*(.*)', line)
            if q_match:
                q_num = int(q_match.group(1))
                q_content = q_match.group(2)

                i += 1
                body_lines = [q_content] if q_content else []
                answer_lines = []
                parsing_lines = []
                state = 'body'

                while i < len(lines):
                    cur = lines[i].rstrip()

                    if re.match(r'(?:##\s*)?\d+\.\s*', cur):
                        break
                    if re.match(r'(?:##\s*)?[一二三四五六七八九十]+、\s*', cur):
                        break

                    if cur.startswith('【答案】'):
                        state = 'answer'
                        answer_lines.append(cur.replace('【答案】', '').strip())
                        i += 1
                        continue

                    if cur.startswith('【解析】'):
                        state = 'parsing'
                        parsing_lines.append(cur.replace('【解析】', '').strip())
                        i += 1
                        continue

                    if not cur:
                        i += 1
                        continue

                    if state == 'body':
                        body_lines.append(cur)
                    elif state == 'answer':
                        answer_lines.append(cur)
                    elif state == 'parsing':
                        parsing_lines.append(cur)

                    i += 1

                body = '\n'.join(body_lines).strip()
                answer = '\n'.join(answer_lines).strip() if answer_lines else None
                parsing = '\n'.join(parsing_lines).strip() if parsing_lines else None

                # --- 处理真实图片: <img src="..."> ---
                image_path = None
                img_match = re.search(r'<img\s+src=["\'](.*?)["\']', body)
                if img_match:
                    image_path = img_match.group(1).strip()
                    # 去掉图片标签本身
                    body = re.sub(r'<img\s+src=["\'].*?["\']\s*/?>', '', body).strip()
                    # 去掉可能残留的 <br>
                    body = re.sub(r'<br\s*/?>', '', body).strip()

                # --- 处理 Markdown 图片: ![desc](path) ---
                md_img_match = re.search(r'!\[.*?\]\((.*?)\)', body)
                if md_img_match and not image_path:
                    image_path = md_img_match.group(1).strip()
                    body = re.sub(r'!\[.*?\]\(.*?\)', '', body).strip()

                # --- 处理图片占位符 <!-- 图：描述 --> ---
                has_image = False
                image_desc = None
                placeholder_match = re.search(r'<!--\s*图[：:]\s*(.*?)\s*-->', body)
                if placeholder_match:
                    has_image = True
                    image_desc = placeholder_match.group(1).strip()
                    body = re.sub(r'<!--\s*图[：:]\s*.*?\s*-->', '', body).strip()
                    body = re.sub(r'\n\s*[A-Da-d]\s*\n', '\n', '\n' + body + '\n')
                    body = body.strip()

                # 提取选择题选项
                body, options = self._extract_options(body)

                q = Question(
                    num=q_num,
                    qtype=current_type,
                    body=body,
                    options=options,
                    answer=answer,
                    parsing=parsing,
                    has_image=has_image,
                    image_desc=image_desc,
                    image_path=image_path,
                )
                self.questions.append(q)
                continue

            i += 1

        return self.questions

    def _normalize_type(self, raw: str) -> str:
        raw = raw.strip()
        for key, val in self.TYPE_MAP.items():
            if key in raw:
                return val
        return raw

    def _extract_options(self, body: str) -> Tuple[str, List[str]]:
        options = []

        pattern_single_line = re.compile(
            r'^(.*?)\s*'
            r'A\.\s*(.+?)\s+'
            r'B\.\s*(.+?)\s+'
            r'C\.\s*(.+?)\s+'
            r'D\.\s*(.+?)$',
            re.DOTALL
        )

        m = pattern_single_line.match(body)
        if m:
            body_part = m.group(1).strip()
            options = [m.group(2).strip(), m.group(3).strip(),
                       m.group(4).strip(), m.group(5).strip()]
            return body_part, options

        pattern_multi = re.compile(
            r'(.*?)\s*\n'
            r'A\.\s*(.+?)\s*\n'
            r'B\.\s*(.+?)\s*\n'
            r'C\.\s*(.+?)(?:\s*\n|\s+|$)'
            r'D\.\s*(.+?)$',
            re.DOTALL
        )

        m = pattern_multi.match(body)
        if m:
            body_part = m.group(1).strip()
            options = [m.group(2).strip(), m.group(3).strip(),
                       m.group(4).strip(), m.group(5).strip()]
            return body_part, options

        if re.search(r'\bA\.\s', body) and re.search(r'\bB\.\s', body):
            opt_pattern = re.compile(
                r'^(.*?)\s*\n?\s*'
                r'A\.\s*(.+?)\s*\n?\s*'
                r'B\.\s*(.+?)\s*\n?\s*'
                r'C\.\s*(.+?)\s*\n?\s*'
                r'D\.\s*(.+?)$',
                re.DOTALL
            )
            m = opt_pattern.match(body)
            if m:
                body_part = m.group(1).strip()
                options = [m.group(2).strip(), m.group(3).strip(),
                           m.group(4).strip(), m.group(5).strip()]
                return body_part, options

        return body, options


# ============================================================
# 布局引擎
# ============================================================

class LayoutEngine:
    def __init__(self, max_height: float = 10.0):
        self.max_height = max_height

    def layout(self, questions: List[Question], mode: str = 'auto') -> List[Frame]:
        if mode == 'single':
            return [Frame([q]) for q in questions]
        if mode == 'compact':
            return self._greedy_layout(questions, allow_split=False)
        return self._greedy_layout(questions, allow_split=True)

    def _greedy_layout(self, questions: List[Question], allow_split: bool = True) -> List[Frame]:
        frames = []
        current_frame = Frame()
        current_height = 0.0

        for q in questions:
            q_height = q.estimate_height()

            if allow_split and q_height >= self.max_height * 0.65:
                if current_frame.questions:
                    frames.append(current_frame)
                    current_frame = Frame()
                    current_height = 0.0
                frames.append(Frame([q]))
                continue

            added_height = q_height
            if current_frame.questions:
                added_height += 0.8

            if current_height + added_height <= self.max_height:
                current_frame.questions.append(q)
                current_height += added_height
            else:
                if current_frame.questions:
                    frames.append(current_frame)
                current_frame = Frame([q])
                current_height = q_height

        if current_frame.questions:
            frames.append(current_frame)

        return frames


# ============================================================
# LaTeX 生成器
# ============================================================

class LatexGenerator:
    """生成 LaTeX Beamer 代码（v2 — 借鉴 SimplePlus 简洁风格）"""

    TEMPLATE = r'''\documentclass[aspectratio=169]{beamer}

\usepackage[utf8]{inputenc}
\usepackage{ctex}
\usepackage{amsmath, amsfonts, amssymb}

% === 参考 SimplePlus 的简洁风格 ===
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{headline}{}
\setbeamertemplate{frametitle}{}
\usebackgroundtemplate{}

% === 页脚：右下角显示页码（SimplePlus风格）===
\setbeamertemplate{footline}{%
    \hfill
    \usebeamercolor[fg]{page number in head/foot}%
    \usebeamerfont{page number in head/foot}%
    \insertframenumber\,\,/\,\inserttotalframenumber%
    \kern1.5em\vspace{0.6em}%
}

% === 页面边距（更宽，类似 SimplePlus）===
\setbeamersize{text margin left=2em, text margin right=2em}

% === 柔和配色（SimplePlus 灵感）===
\definecolor{DarkBlue}{RGB}{13, 38, 89}
\definecolor{MediumBlue}{RGB}{70, 130, 180}
\definecolor{AnswerColor}{RGB}{34, 139, 34}
\definecolor{HintColor}{RGB}{70, 130, 180}
\definecolor{MutedBlack}{RGB}{51, 51, 51}

\setbeamercolor{normal text}{fg=MutedBlack}

% === 表格与选项 ===
\usepackage{array}
\usepackage{tasks}
\settasks{
    label=\Alph*.,
    label-format=\bfseries,
    label-width=1.2em,
    item-indent=1.8em,
    column-sep=1.2em
}

% === 图片支持 ===
\usepackage{graphicx}

% === 填空横线 ===
\newcommand{\blankline}{\underline{\hspace{1.5cm}}}

% === 图片占位框（灰色虚线框）===
\newcommand{\imageplaceholder}[1]{%
    \vspace{0.2cm}
    \begin{center}
    \fbox{\parbox{0.6\textwidth}{\centering\vspace{1cm}\textcolor{gray}{\small [图：#1]}\vspace{1cm}}}
    \end{center}
}

% === 真实图片（限制最大高度，防止溢出）===
\newcommand{\questionimage}[1]{%
    \vspace{0.2cm}
    \begin{center}
    \includegraphics[width=0.65\textwidth,height=0.45\textheight,keepaspectratio]{#1}
    \end{center}
}

% === 答题区域 ===
\newcommand{\answerarea}[1][2.5cm]{%
    \vspace{0.2cm}
    \noindent\hfill\fbox{\parbox{0.94\textwidth}{\vspace{#1}}}\hfill
}

\begin{document}

<<CONTENT>>

\end{document}
'''

    BG_PLACEHOLDER = r'''% 背景占位（纯白，无横线）'''

    def __init__(self, template_style: str = 'standard', max_height: float = 10.0):
        self.template_style = template_style
        self.max_height = max_height

    def generate(self, frames: List[Frame], mode: str = 'student',
                 answer_area: bool = True, warn_overflow: bool = True) -> str:
        latex = self.TEMPLATE.replace('<<BACKGROUND>>', self.BG_PLACEHOLDER)

        content = []
        for frame in frames:
            frame_tex = self._render_frame(frame, mode, answer_area, warn_overflow)
            content.append(frame_tex)

        final = latex.replace('<<CONTENT>>', '\n\n'.join(content))
        return final

    def _render_frame(self, frame: Frame, mode: str, answer_area: bool, warn_overflow: bool = True) -> str:
        frame_height = frame.total_height()
        frame_opt = '[t]'
        if frame_height > self.max_height * 1.2:
            frame_opt = '[t,allowframebreaks]'
            if warn_overflow:
                q_nums = [q.num for q in frame.questions]
                print(f'   ⚠️  第 {q_nums} 题内容较长 ({frame_height:.1f}cm)，已启用自动分页')

        parts = [f'\\begin{{frame}}{frame_opt}']

        # === 字号选择（整体缩小一档） ===
        if frame_height > 14:
            parts.append('\\scriptsize')
        elif frame_height > 10:
            parts.append('\\footnotesize')
        elif frame_height > 6:
            parts.append('\\small')
        # else: 默认 \normalsize

        # === 等间距：顶部 vfill ===
        parts.append('\\vfill')

        for i, q in enumerate(frame.questions):
            if i > 0:
                parts.append('\\vfill')  # 题间弹性间距

            # 构建题目内容（在 minipage 内）
            body_parts = []

            # 题干
            body_tex = self._escape_latex(q.body)
            body_parts.append(body_tex)

            # 图片（真实图片优先）
            if q.image_path:
                # 去掉路径开头的 ./ 以便 xelatex 查找
                img_path = q.image_path.lstrip('./')
                body_parts.append(f'\\questionimage{{{img_path}}}')
            elif q.has_image and q.image_desc:
                body_parts.append(f'\\imageplaceholder{{{self._escape_latex(q.image_desc)}}}')

            # 选择题选项
            if q.options:
                body_parts.append(self._render_options(q.options))

            # 解答题答题区域
            if answer_area and mode == 'student' and q.qtype == '解答题':
                height = min(max(q.estimate_height() * 0.6, 2.5), 5)
                body_parts.append(f'\\answerarea[{height}cm]')

            # 答案和解析
            if mode in ('teacher', 'body-only'):
                if q.answer:
                    ans_tex = self._escape_latex(q.answer)
                    body_parts.append(f'\\vspace{{0.2cm}}')
                    body_parts.append(f'{{\\textcolor{{AnswerColor}}{{\\textbf{{【答案】}}{ans_tex}}}}}')

                if mode == 'teacher' and q.parsing:
                    par_tex = self._escape_latex(q.parsing)
                    body_parts.append(f'\\vspace{{0.2cm}}')
                    body_parts.append(f'{{\\textcolor{{HintColor}}{{\\textbf{{【解析】}}{par_tex}}}}}')

            # 直接内联：题号 + minipage 内容（避免宏参数嵌套问题）
            question_content = '\n'.join(body_parts)
            parts.append('\\noindent')
            parts.append(f'\\makebox[1.6em][l]{{\\textbf{{{q.num}.}}}}%')
            parts.append('\\begin{minipage}[t]{\\dimexpr\\linewidth-1.6em\\relax}')
            parts.append(question_content)
            parts.append('\\end{minipage}%')
            parts.append('\\par')

        # === 等间距：底部 vfill ===
        parts.append('\\vfill')
        parts.append('\\end{frame}')
        return '\n'.join(parts)

    def _render_options(self, options: List[str]) -> str:
        if not options:
            return ''

        total_len = sum(len(opt) for opt in options)
        labels = ['A', 'B', 'C', 'D', 'E', 'F']

        if total_len < 60 and len(options) <= 4:
            cols = 4
        elif total_len < 120:
            cols = 2
        else:
            cols = 1

        parts = ['\\vspace{0.15cm}', f'\\begin{{tasks}}({cols})']
        for opt in options:
            opt_tex = self._escape_latex(opt)
            parts.append(f'    \\task {opt_tex}')
        parts.append('\\end{tasks}')
        return '\n'.join(parts)

    def _escape_latex(self, text: str) -> str:
        if not text:
            return ''

        # 清理填空题答案: ___答案___ -> ___
        text = re.sub(r'___\s*[^_\n]+\s*___', r'___', text)

        # 保护 HTML 表格块
        tables = []
        def save_table(match):
            tables.append(match.group(0))
            return f"HTMLTABLE{len(tables)-1}"

        text = re.sub(r'<table>.*?</table>', save_table, text, flags=re.DOTALL)

        # 按 $ 分割，对非公式部分转义
        result = []
        i = 0
        while i < len(text):
            if text[i:i+2] == '$$':
                end = text.find('$$', i+2)
                if end != -1:
                    result.append(text[i:end+2])
                    i = end + 2
                    continue

            if text[i] == '$':
                end = i + 1
                while end < len(text):
                    if text[end] == '$':
                        break
                    end += 1
                if end < len(text):
                    result.append(text[i:end+1])
                    i = end + 1
                    continue

            plain_start = i
            while i < len(text):
                if text[i] == '$':
                    break
                if text[i:i+2] == '$$':
                    break
                i += 1
            plain = text[plain_start:i]
            result.append(self._escape_plain_text(plain))

        result_str = ''.join(result)

        # 还原 HTML 表格为 LaTeX
        for idx, table_html in enumerate(tables):
            latex_table = self._html_table_to_latex(table_html)
            result_str = result_str.replace(f"HTMLTABLE{idx}", latex_table)

        # 连续下划线替换为填空横线
        result_str = re.sub(r'(?:\\_){3,}', r'\\blankline ', result_str)

        return result_str

    def _escape_plain_text(self, text: str) -> str:
        replacements = [
            ('\\', '\\textbackslash{}'),
            ('&', '\\&'),
            ('%', '\\%'),
            ('#', '\\#'),
            ('_', '\\_'),
            ('{', '\\{'),
            ('}', '\\}'),
            ('~', '\\textasciitilde{}'),
            ('^', '\\textasciicircum{}'),
            ('①', '\\textcircled{1}'),
            ('②', '\\textcircled{2}'),
            ('③', '\\textcircled{3}'),
            ('④', '\\textcircled{4}'),
            ('⑤', '\\textcircled{5}'),
            ('⑥', '\\textcircled{6}'),
            ('⑦', '\\textcircled{7}'),
            ('⑧', '\\textcircled{8}'),
            ('⑨', '\\textcircled{9}'),
            ('⑩', '\\textcircled{10}'),
        ]
        for old, new in replacements:
            text = text.replace(old, new)
        return text

    def _html_table_to_latex(self, table_html: str) -> str:
        rows = re.findall(r'<tr>(.*?)</tr>', table_html, re.DOTALL)
        if not rows:
            return '[表格]'

        latex_rows = []
        ncol = 0
        for row in rows:
            cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.DOTALL)
            ncol = max(ncol, len(cells))
            clean_cells = []
            for cell in cells:
                cell = re.sub(r'<[^>]+>', '', cell)
                cell = cell.strip()
                clean_cells.append(cell)
            latex_rows.append(' & '.join(clean_cells))

        if not latex_rows:
            return '[表格]'

        latex = '\\begin{center}\n\\small\n'
        latex += '\\begin{tabular}{' + 'c' * ncol + '}\n'
        latex += '\\hline\n'
        latex += ' \\\\ \n'.join(latex_rows)
        latex += ' \\\\ \n\\hline\n'
        latex += '\\end{tabular}\n\\end{center}'
        return latex


# ============================================================
# 工具函数
# ============================================================

def parse_question_numbers(spec: str) -> Optional[List[int]]:
    if not spec or spec.lower() == 'all':
        return None

    result = set()
    parts = spec.split(',')
    for part in parts:
        part = part.strip()
        if '-' in part:
            start, end = part.split('-')
            result.update(range(int(start), int(end) + 1))
        else:
            result.add(int(part))

    return sorted(result)


def filter_questions(questions: List[Question],
                     numbers: Optional[List[int]] = None,
                     qtypes: Optional[List[str]] = None) -> List[Question]:
    result = questions

    if numbers is not None:
        result = [q for q in result if q.num in numbers]

    if qtypes is not None:
        normalized_types = [t.strip() for t in qtypes]
        result = [q for q in result if q.qtype in normalized_types]

    return result


# ============================================================
# 主程序
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description='试卷题目 → LaTeX Beamer PPT 转换器',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  # 生成完整试卷的 PPT（学生版，纯题目）
  python md_to_ppt.py -i 崇明二模-optimized.md -o output.tex

  # 只选第 3、5、10-12、15-17 题
  python md_to_ppt.py -i 崇明二模-optimized.md -q 3,5,10-12,15-17 -o output.tex

  # 教师版（带答案和解析），横线稿纸背景
  python md_to_ppt.py -i 崇明二模-optimized.md -m teacher -t lined -o output.tex

  # 只选填空题，解答题带答题区域
  python md_to_ppt.py -i 崇明二模-optimized.md --type 填空题 --answer-area -o output.tex
        '''
    )

    parser.add_argument('-i', '--input', required=True, help='输入的 Markdown 试卷文件')
    parser.add_argument('-o', '--output', default='output.tex', help='输出的 LaTeX 文件（默认: output.tex）')
    parser.add_argument('-q', '--questions', default='all',
                        help='题号筛选，如 1,3,5-10,15（默认: all）')
    parser.add_argument('--type', default=None,
                        help='题型筛选，如 填空题,单选题,解答题')
    parser.add_argument('-m', '--mode', default='student',
                        choices=['student', 'teacher', 'body-only'],
                        help='输出模式: student=纯题目, teacher=带答案解析, body-only=题干+答案（默认: student）')
    parser.add_argument('-l', '--layout', default='auto',
                        choices=['auto', 'single', 'compact'],
                        help='布局模式: auto=智能分页, single=每题一页, compact=紧凑（默认: auto）')
    parser.add_argument('-t', '--template', default='standard',
                        choices=['standard', 'lined'],
                        help='模板风格: standard=标准投影, lined=横线稿纸（默认: standard）')
    parser.add_argument('--answer-area', action='store_true',
                        help='解答题下方添加答题区域（仅 student 模式有效）')
    parser.add_argument('--max-height', type=float, default=10.0,
                        help='单页最大高度（cm，默认: 10.0）')

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f'错误: 找不到输入文件 {args.input}')
        sys.exit(1)

    with open(args.input, 'r', encoding='utf-8') as f:
        md_content = f.read()

    print(f'📖 正在解析: {args.input}')

    exam_parser = ExamParser(md_content)
    questions = exam_parser.parse()
    print(f'✅ 解析完成: 共 {len(questions)} 道题目')

    if not questions:
        print('⚠️ 未解析到任何题目，请检查文件格式')
        sys.exit(1)

    type_counts = {}
    for q in questions:
        type_counts[q.qtype] = type_counts.get(q.qtype, 0) + 1
    print(f'   题型分布: {type_counts}')

    # 统计图片
    img_count = sum(1 for q in questions if q.image_path)
    ph_count = sum(1 for q in questions if q.has_image)
    if img_count:
        print(f'   📷 检测到 {img_count} 道题目含真实图片')
    if ph_count:
        print(f'   🖼️  {ph_count} 道题目含图片占位符')

    numbers = parse_question_numbers(args.questions)
    qtypes = [t.strip() for t in args.type.split(',')] if args.type else None
    filtered = filter_questions(questions, numbers, qtypes)

    if numbers:
        print(f'🔢 题号筛选: {args.questions} -> 选中 {len(filtered)} 题')
    if qtypes:
        print(f'🏷️  题型筛选: {args.type} -> 选中 {len(filtered)} 题')

    if not filtered:
        print('⚠️ 筛选后没有题目，请检查参数')
        sys.exit(1)

    layout_engine = LayoutEngine(max_height=args.max_height)
    frames = layout_engine.layout(filtered, mode=args.layout)
    print(f'📄 分页完成: 共 {len(frames)} 页幻灯片')

    for i, frame in enumerate(frames, 1):
        nums = [q.num for q in frame.questions]
        height = frame.total_height()
        print(f'   第{i:2d}页: 题号 {nums} (占用 {height:.1f}cm)')

    latex_gen = LatexGenerator(template_style=args.template, max_height=args.max_height)
    latex_code = latex_gen.generate(
        frames,
        mode=args.mode,
        answer_area=args.answer_area
    )

    output_path = args.output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(latex_code)

    print(f'\n🎉 生成成功: {output_path}')
    print(f'   题目数: {len(filtered)} | 页数: {len(frames)} | 模式: {args.mode} | 模板: {args.template}')
    print(f'\n下一步: 使用 xelatex 编译')
    print(f'   xelatex -interaction=nonstopmode {output_path}')


if __name__ == '__main__':
    main()
