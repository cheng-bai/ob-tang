#!/usr/bin/env python3
"""
MD → LaTeX 转换器 v4（考试专用）
教师版答案区按【考点】【答案】【解析】标准格式排版
"""

import re
import os
import subprocess
import shutil

SRC_DIR = "/Users/tangchengbaiair/Downloads/latex-maki-math/虹口区高三二模-拆分版"
OUT_TEX_DIR = os.path.join(SRC_DIR, "tex")
IMAGES_SRC = "/Users/tangchengbaiair/Library/Mobile Documents/com~apple~CloudDocs/ipad 中转/公式识别的 pdf 资料/2025-2026学年虹口区高三二模数学试卷及解析.pdf_os_d7obidc91nqc738jp340/images"
os.makedirs(OUT_TEX_DIR, exist_ok=True)
os.makedirs(os.path.join(OUT_TEX_DIR, 'images'), exist_ok=True)

# ========================================
# LaTeX 模板
# ========================================

LATEX_PREAMBLE = r"""\documentclass[11pt,a4paper]{article}
\usepackage[left=2cm,right=2cm,top=2.5cm,bottom=2.5cm]{geometry}
\usepackage{fontspec}
\usepackage{ctex}
\usepackage{amsmath,amssymb,amsfonts,mathtools}
\usepackage[mathbf=sym]{unicode-math}
\setmainfont{STIX Two Text}
\setmathfont{STIX Two Math}
\setsansfont{Arial}
\setmonofont{Courier New}
\setCJKmainfont[BoldFont=Noto Serif CJK SC Bold]{Noto Serif CJK SC}
\setCJKsansfont[BoldFont=Noto Sans CJK SC Bold]{Noto Sans CJK SC}
\setCJKmonofont{Noto Sans CJK SC}
\newCJKfontfamily\examkaishu{FandolKai-Regular}
\usepackage{graphicx}
\usepackage{booktabs,array,multirow,tabularx}
\usepackage{fancyhdr}
\usepackage{needspace}
\usepackage{tikz}
\usepackage{hyperref}
\hypersetup{colorlinks=false}
\usepackage{parskip}
\setlength{\parskip}{0.4em}
\setlength{\parindent}{0em}
\usepackage{xcolor}

% 数学符号
\renewcommand{\ge}{\geqslant}
\renewcommand{\geq}{\geqslant}
\renewcommand{\le}{\leqslant}
\renewcommand{\leq}{\leqslant}

% 知识点标签
\newcommand{\kp}[1]{%
    \par\vspace{0.3em}\noindent%
    {\small\textcolor{gray}{#1}}%
    \par\vspace{0.2em}%
}

% 答案解析区域
\newenvironment{solutionblock}{%
    \par\vspace{0.5em}%
    \noindent\rule{\textwidth}{0.4pt}%
    \vspace{0.5em}%
    \noindent\textbf{【参考答案与解析】}%
    \par\vspace{0.3em}%
    {\small%
}{%
    \par}%
}

% 答案标签
\newcommand{\anslabel}[1]{%
    \par\vspace{0.2em}\noindent%
    \textbf{#1}%
    \ignorespaces%
}

% 页眉页脚
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\examkaishu HEADTITLE_PLACEHOLDER}
\fancyhead[R]{\small\examkaishu 第 \thepage 页}
\fancyfoot[C]{}
\renewcommand{\headrulewidth}{0.4pt}

\begin{document}

{\centering\Large\bfseries TITLE_PLACEHOLDER\par}
\vspace{0.3em}
\hrule
\vspace{0.5em}

"""

LATEX_EPILOGUE = r"\end{document}"

# ========================================
# 转换器核心
# ========================================

def strip_md(text):
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    return text

def convert_math(text):
    """转换文本为 LaTeX（处理特殊字符）"""
    result = []
    i = 0
    n = len(text)

    while i < n:
        # $$ 显示公式
        if text[i:i+2] == '$$':
            end = text.find('$$', i + 2)
            if end != -1:
                result.append('\\[' + text[i+2:end] + '\\]')
                i = end + 2
                continue

        # $ 行内公式
        if text[i] == '$':
            end = text.find('$', i + 1)
            if end != -1:
                result.append('$' + text[i+1:end] + '$')
                i = end + 1
                continue

        # HTML 实体
        if text[i:i+6] == '&amp;':
            result.append('\\&')
            i += 6
            continue
        if text[i:i+5] == '&lt;':
            result.append('<')
            i += 5
            continue
        if text[i:i+5] == '&gt;':
            result.append('>')
            i += 5
            continue
        if text[i:i+6] == '&nbsp;':
            result.append('~')
            i += 6
            continue

        result.append(text[i])
        i += 1

    return ''.join(result)

def convert_line(line, in_answer=False, answer_mode=None):
    """
    转换单行为 LaTeX
    answer_mode: None | 'header' | 'kp' | 'answer' | 'parse' | 'analysis' | 'detail'
    """
    stripped = line.strip()

    if not stripped:
        return ''

    # <br> 留白
    if stripped.startswith('<br>'):
        count = stripped.count('<br>')
        vspace = min(count * 1.2, 15)
        return f'\\vspace{{{vspace}cm}}'

    # 水平线
    if re.match(r'^---+$', stripped):
        if not in_answer:
            return '\\vspace{0.2em}\\hrule\\vspace{0.3em}'
        return ''

    # 标题
    if stripped.startswith('## '):
        sec = strip_md(stripped[3:])
        sec = convert_math(sec)
        return f'\\section*{{{sec}}}'

    if stripped.startswith('# '):
        return ''  # 顶级标题已在模板中设置

    if stripped.startswith('### '):
        kp = strip_md(stripped[4:])
        if kp.startswith('考点：'):
            return f'\\kp{{{convert_math(kp)}}}'
        return f'\\subsection*{{{convert_math(kp)}}}'

    # 图片
    img_match = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', stripped)
    if img_match:
        img_path = img_match.group(2)
        img_name = os.path.basename(img_path)
        src = os.path.join(IMAGES_SRC, img_name)
        if os.path.exists(src):
            dst = os.path.join(OUT_TEX_DIR, 'images', img_name)
            if not os.path.exists(dst):
                shutil.copy2(src, dst)
            return f'\\begin{{center}}\\includegraphics[width=0.45\\textwidth]{{images/{img_name}}}\\end{{center}}'
        return f'% 图片缺失: {img_name}'

    # 粗体 + 数学
    tex = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', stripped)
    tex = convert_math(tex)

    if in_answer:
        return f'{{\\small {tex}}}'
    return tex

def html_table_to_latex(html_lines):
    rows = []
    full_html = '\n'.join(html_lines)
    tr_pattern = re.compile(r'<tr[^>]*>(.*?)</tr>', re.DOTALL)
    td_pattern = re.compile(r'<t[dh][^>]*>(.*?)</t[dh]>', re.DOTALL)

    for tr_match in tr_pattern.finditer(full_html):
        cells = []
        for td_match in td_pattern.finditer(tr_match.group(1)):
            cell = td_match.group(1).strip()
            cell = re.sub(r'<[^>]+>', '', cell)
            cell = convert_math(cell)
            cells.append(cell)
        if cells:
            rows.append(cells)

    if not rows:
        return ''

    num_cols = max(len(r) for r in rows)
    col_spec = '|'.join(['c'] * num_cols)
    col_spec = '|' + col_spec + '|'

    tex = [f'\\begin{{tabular}}{{{col_spec}}}', '\\hline']
    for row in rows:
        while len(row) < num_cols:
            row.append('')
        tex.append(' & '.join(row) + ' \\\\ \\hline')
    tex.append('\\end{tabular}')
    return '\n'.join(tex)

def convert_md_to_tex(md_content):
    """主转换：MD → LaTeX body"""
    lines = md_content.split('\n')
    tex_lines = []
    in_answer = False
    collecting_table = False
    table_lines = []

    for line in lines:
        stripped = line.strip()

        # 检测到新题标题 → 关闭答案解析环境
        if in_answer and (stripped.startswith('## 第') or stripped == '---'):
            tex_lines.append('\\end{solutionblock}')
            in_answer = False
            if stripped == '---':
                tex_lines.append('')
                continue

        if collecting_table:
            table_lines.append(line)
            if '</table>' in stripped:
                latex_table = html_table_to_latex(table_lines)
                if latex_table:
                    tex_lines.append(latex_table)
                collecting_table = False
                table_lines = []
            continue

        if '<table' in stripped:
            collecting_table = True
            table_lines = [line]
            if '</table>' in stripped:
                latex_table = html_table_to_latex(table_lines)
                if latex_table:
                    tex_lines.append(latex_table)
                collecting_table = False
                table_lines = []
            continue

        if not stripped:
            if not in_answer:
                tex_lines.append('')
            continue

        # 答案解析环境开始
        if stripped == '**【参考答案与解析】**' or '【参考答案与解析】' in stripped:
            if not in_answer:
                in_answer = True
                tex_lines.append('\\begin{solutionblock}')
            continue

        # 【考点】
        if stripped.startswith('【考点】：'):
            content = stripped.replace('【考点】：', '').strip()
            tex_lines.append(f'{{\\small \\anslabel{{【考点】：}} {convert_math(content)}}}')
            continue

        # 【答案】
        if stripped.startswith('【答案】'):
            content = stripped.replace('【答案】', '').strip()
            tex_lines.append(f'{{\\small \\anslabel{{【答案】}} {convert_math(content)}}}')
            continue

        # 【解析】
        if stripped == '【解析】' or stripped.startswith('【解析】'):
            tex_lines.append('{\\small \\anslabel{【解析】}}')
            continue

        # 【分析】
        if stripped.startswith('【分析】'):
            content = stripped.replace('【分析】', '').strip()
            tex_lines.append(f'{{\\small \\anslabel{{【分析】}} {convert_math(content)}}}')
            continue

        # 【详解】
        if stripped.startswith('【详解】'):
            content = stripped.replace('【详解】', '').strip()
            tex_lines.append(f'{{\\small \\anslabel{{【详解】}} {convert_math(content)}}}')
            continue

        # 【小问 X 详解】
        if stripped.startswith('【小问'):
            tex_lines.append(f'{{\\small \\textbf{{{convert_math(stripped)}}}}}')
            continue

        # 【点睛】
        if stripped.startswith('【点睛】'):
            content = stripped.replace('【点睛】', '').strip()
            tex_lines.append(f'{{\\small \\anslabel{{【点睛】}} {convert_math(content)}}}')
            continue

        # 普通文本行（在答案解析环境内用小字体）
        if in_answer:
            tex = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', stripped)
            tex = convert_math(tex)
            tex_lines.append(f'{{\\small {tex}}}')
        else:
            tex = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', stripped)
            tex = convert_math(tex)
            tex_lines.append(tex)

    if in_answer:
        tex_lines.append('\\end{solutionblock}')

    return '\n'.join(tex_lines)

def write_tex(body, head_title, title, output_path):
    tex = LATEX_PREAMBLE.replace('HEADTITLE_PLACEHOLDER', head_title)
    tex = tex.replace('TITLE_PLACEHOLDER', title)
    tex += body
    tex += '\n' + LATEX_EPILOGUE

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(tex)

def compile_tex(tex_path):
    work_dir = os.path.dirname(tex_path)
    basename = os.path.splitext(os.path.basename(tex_path))[0]

    print(f"  📝 编译 {basename}...", end=' ', flush=True)

    for _ in range(2):
        cmd = ['xelatex', '-interaction=nonstopmode',
               '-output-directory', work_dir, tex_path]
        subprocess.run(cmd, capture_output=True, text=True, timeout=120)

    pdf_path = os.path.join(work_dir, basename + '.pdf')
    if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 1000:
        size_kb = os.path.getsize(pdf_path) / 1024
        print(f"✅ {size_kb:.0f}KB")
        return pdf_path
    else:
        print("❌")
        return None

def main():
    print("=" * 60)
    print("  MD → LaTeX 转换器 v4")
    print("=" * 60)

    files = [
        ("学生版-2025-2026学年虹口区高三二模数学.md",
         "虹口区高三二模数学（学生版）",
         "2025-2026学年虹口区高三二模数学试卷（学生版）",
         "学生版"),
        ("教师版-2025-2026学年虹口区高三二模数学.md",
         "虹口区高三二模数学（教师版）",
         "2025-2026学年虹口区高三二模数学试卷（教师版）",
         "教师版"),
        ("01-填空题-2025-2026学年虹口区高三二模数学.md",
         "虹口区高三二模·填空题",
         "一、填空题",
         "填空题"),
        ("02-选择题-2025-2026学年虹口区高三二模数学.md",
         "虹口区高三二模·选择题",
         "二、选择题",
         "选择题"),
        ("03-基础解答题-2025-2026学年虹口区高三二模数学.md",
         "虹口区高三二模·基础解答题",
         "三、基础解答题",
         "基础解答题"),
        ("04-解析几何-2025-2026学年虹口区高三二模数学.md",
         "虹口区高三二模·解析几何",
         "四、解析几何",
         "解析几何"),
        ("05-压轴新定义-2025-2026学年虹口区高三二模数学.md",
         "虹口区高三二模·压轴新定义",
         "五、压轴新定义",
         "压轴新定义"),
    ]

    for md_file, head_title, title, label in files:
        md_path = os.path.join(SRC_DIR, md_file)
        if not os.path.exists(md_path):
            print(f"\n⚠️  跳过: {md_file}")
            continue

        print(f"\n📄 {label}")
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        body = convert_md_to_tex(md_content)
        tex_path = os.path.join(OUT_TEX_DIR, f"{label}.tex")
        write_tex(body, head_title, title, tex_path)
        compile_tex(tex_path)

    print("\n" + "=" * 60)
    print("  生成文件:")
    for f in sorted(os.listdir(OUT_TEX_DIR)):
        if f.endswith('.pdf'):
            size = os.path.getsize(os.path.join(OUT_TEX_DIR, f)) / 1024
            print(f"    {f:<25s} {size:>8.0f}KB")
    print("=" * 60)

if __name__ == '__main__':
    main()
