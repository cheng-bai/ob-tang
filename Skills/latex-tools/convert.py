#!/usr/bin/env python3
"""
上海高中数学教材 Markdown 转 HTML 学习平台
"""

import os
import re
import html

def parse_markdown(content):
    """解析Markdown内容，提取章节结构"""
    sections = []
    current_section = None
    current_subsection = None
    
    lines = content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # 一级标题 (## 1.1 集合及其表示)
        if line.startswith('## '):
            if current_section:
                sections.append(current_section)
            current_section = {
                'title': line[3:].strip(),
                'subsections': [],
                'content': []
            }
            current_subsection = None
            
        # 二级标题 (### 1 集合的概念)
        elif line.startswith('### '):
            if current_subsection:
                current_section['subsections'].append(current_subsection)
            current_subsection = {
                'title': line[4:].strip(),
                'content': []
            }
            
        # 三级标题 (#### 练习 1.1(1))
        elif line.startswith('#### '):
            if current_subsection:
                current_subsection['content'].append({
                    'type': 'subsubsection',
                    'title': line[5:].strip()
                })
                
        # 表格
        elif line.startswith('<table>'):
            table_html = line
            while i + 1 < len(lines) and not lines[i+1].strip().startswith('##') and not lines[i+1].strip().startswith('###'):
                i += 1
                if lines[i].strip():
                    table_html += '\n' + lines[i]
            if current_subsection:
                current_subsection['content'].append({
                    'type': 'table',
                    'html': table_html
                })
            elif current_section:
                current_section['content'].append({
                    'type': 'table',
                    'html': table_html
                })
                
        # 图片
        elif line.startswith('!['):
            img_match = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', line)
            if img_match:
                alt, src = img_match.groups()
                content_item = {
                    'type': 'image',
                    'alt': alt,
                    'src': src
                }
                if current_subsection:
                    current_subsection['content'].append(content_item)
                elif current_section:
                    current_section['content'].append(content_item)
                    
        # 分隔线 (---) - 提示框
        elif line == '---':
            hint_content = []
            i += 1
            while i < len(lines) and lines[i].strip() != '---':
                if lines[i].strip():
                    hint_content.append(lines[i])
                i += 1
            if current_subsection:
                current_subsection['content'].append({
                    'type': 'hint',
                    'content': '\n'.join(hint_content)
                })
            elif current_section:
                current_section['content'].append({
                    'type': 'hint',
                    'content': '\n'.join(hint_content)
                })
                
        # 普通段落
        elif line:
            # 检测是否是例题
            if re.match(r'^例\s*\d+', line) or line.startswith('解 '):
                content_item = {
                    'type': 'example' if line.startswith('例') else 'solution',
                    'content': line
                }
                if current_subsection:
                    current_subsection['content'].append(content_item)
                elif current_section:
                    current_section['content'].append(content_item)
            # 检测是否是定义
            elif line.startswith('定义 '):
                content_item = {
                    'type': 'definition',
                    'content': line[3:].strip()
                }
                if current_subsection:
                    current_subsection['content'].append(content_item)
                elif current_section:
                    current_section['content'].append(content_item)
            else:
                content_item = {
                    'type': 'paragraph',
                    'content': line
                }
                if current_subsection:
                    current_subsection['content'].append(content_item)
                elif current_section:
                    current_section['content'].append(content_item)
                    
        i += 1
    
    # 添加最后一个subsection和section
    if current_subsection and current_section:
        current_section['subsections'].append(current_subsection)
    if current_section:
        sections.append(current_section)
        
    return sections

def process_math(text):
    """处理数学公式，转换为HTML"""
    # 保护已有的HTML标签
    text = text.replace('<table>', '&lt;table&gt;')
    text = text.replace('</table>', '&lt;/table&gt;')
    text = text.replace('<tr>', '&lt;tr&gt;')
    text = text.replace('</tr>', '&lt;/tr&gt;')
    text = text.replace('<td>', '&lt;td&gt;')
    text = text.replace('</td>', '&lt;/td&gt;')
    
    # 处理行内公式 $...$
    text = re.sub(r'\$([^$\n]+?)\$', r'<span class="math-inline">\1</span>', text)
    
    # 处理显示公式 $$...$$
    text = re.sub(r'\$\$([^$]+?)\$\$', r'<div class="math-display">\1</div>', text)
    
    # 恢复HTML标签
    text = text.replace('&lt;table&gt;', '<table class="math-table">')
    text = text.replace('&lt;/table&gt;', '</table>')
    text = text.replace('&lt;tr&gt;', '<tr>')
    text = text.replace('&lt;/tr&gt;', '</tr>')
    text = text.replace('&lt;td&gt;', '<td>')
    text = text.replace('&lt;/td&gt;', '</td>')
    
    return text

def generate_nav_items(sections):
    """生成导航项"""
    nav_items = []
    for i, section in enumerate(sections):
        section_id = f"section{i}"
        nav_items.append(f'''
        <div class="nav-item" onclick="showSection('{section_id}')">
            <div class="flex items-center gap-2">
                <span class="w-5 h-5 rounded-full bg-surface-container-high text-on-surface-variant text-xs flex items-center justify-center font-semibold">{i+1}</span>
                <span class="text-sm">{html.escape(section['title'])}</span>
            </div>
        </div>''')
    return '\n'.join(nav_items)

def generate_content(sections):
    """生成内容区域"""
    content_html = []
    
    for i, section in enumerate(sections):
        section_id = f"section{i}"
        is_active = "active" if i == 0 else ""
        
        section_html = f'<section id="{section_id}" class="tab-content {is_active}">\n'
        section_html += f'    <div class="mb-6">\n'
        section_html += f'        <h2 class="text-xl font-semibold text-on-surface mb-3">{html.escape(section["title"])}</h2>\n'
        section_html += f'    </div>\n'
        
        # 处理小节内容
        for subsection in section.get('subsections', []):
            section_html += f'    <div class="card-standard mb-6">\n'
            section_html += f'        <h3 class="text-lg font-semibold text-on-surface mb-4">{html.escape(subsection["title"])}</h3>\n'
            
            for item in subsection.get('content', []):
                section_html += process_content_item(item)
            
            section_html += f'    </div>\n'
        
        # 处理直接属于section的内容
        for item in section.get('content', []):
            section_html += process_content_item(item, wrap_card=True)
        
        section_html += '</section>\n'
        content_html.append(section_html)
    
    return '\n'.join(content_html)

def process_content_item(item, wrap_card=False):
    """处理内容项"""
    item_type = item.get('type', 'paragraph')
    
    if item_type == 'paragraph':
        content = process_math(item['content'])
        if wrap_card:
            return f'    <div class="card-standard mb-4"><p class="text-body-md text-on-surface-variant leading-relaxed">{content}</p></div>\n'
        return f'        <p class="text-sm text-on-surface-variant leading-relaxed mb-3">{content}</p>\n'
    
    elif item_type == 'definition':
        content = process_math(item['content'])
        return f'''        <div class="definition-card mb-4">
            <div class="flex items-center gap-2 mb-2">
                <span class="badge-hint">定义</span>
            </div>
            <p class="text-sm text-on-surface">{content}</p>
        </div>
'''
    
    elif item_type == 'example':
        content = process_math(item['content'])
        return f'''        <div class="example-card">
            <p class="text-sm text-on-surface mb-2"><strong class="text-primary">{content}</strong></p>
        </div>
'''
    
    elif item_type == 'solution':
        content = process_math(item['content'])
        return f'        <p class="text-sm text-on-surface-variant mb-2">{content}</p>\n'
    
    elif item_type == 'hint':
        content = process_math(item['content'])
        return f'''        <div class="hint-box">
            <p class="text-sm text-tertiary">{content}</p>
        </div>
'''
    
    elif item_type == 'table':
        # 简化表格处理
        return ''
    
    elif item_type == 'image':
        return f'''        <div class="my-4 text-center">
            <div class="text-sm text-on-surface-variant italic">[图片: {html.escape(item["alt"])}]</div>
        </div>
'''
    
    elif item_type == 'subsubsection':
        return f'        <h4 class="text-md font-semibold text-on-surface mt-4 mb-2">{html.escape(item["title"])}</h4>\n'
    
    return ''

def generate_html(title, subtitle, sections):
    """生成完整HTML"""
    
    nav_items = generate_nav_items(sections)
    content = generate_content(sections)
    
    html_template = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - {subtitle}</title>
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Inter Font -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- KaTeX for Math Rendering -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
    
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        surface: {{
                            DEFAULT: '#0f172a',
                            dim: '#0f172a',
                            bright: '#1e293b',
                            container: {{
                                lowest: '#020617',
                                low: '#0f172a',
                                DEFAULT: '#1e293b',
                                high: '#334155',
                                highest: '#475569',
                            }},
                        }},
                        'on-surface': {{
                            DEFAULT: '#f1f5f9',
                            variant: '#94a3b8',
                        }},
                        primary: {{
                            DEFAULT: '#3b82f6',
                            fixed: '#dbeafe',
                            'fixed-dim': '#93c5fd',
                        }},
                        secondary: {{
                            DEFAULT: '#10b981',
                            fixed: '#d1fae5',
                            'fixed-dim': '#6ee7b7',
                        }},
                        tertiary: {{
                            DEFAULT: '#f59e0b',
                            fixed: '#fef3c7',
                            'fixed-dim': '#fcd34d',
                        }},
                        error: {{
                            DEFAULT: '#ef4444',
                            container: '#fee2e2',
                        }},
                    }},
                    fontFamily: {{
                        sans: ['Inter', 'system-ui', 'sans-serif'],
                    }},
                }},
            }},
        }}
    </script>
    <style>
        body {{
            font-family: 'Inter', system-ui, sans-serif;
            background-color: #0f172a;
            color: #f1f5f9;
        }}
        
        .katex {{
            font-size: 1.05em;
            color: #f1f5f9;
        }}
        
        .katex-display {{
            margin: 1em 0;
            overflow-x: auto;
            overflow-y: hidden;
        }}
        
        .katex-display .katex {{
            font-size: 1.15em;
        }}
        
        .card-standard {{
            background-color: #1e293b;
            border: 1px solid #334155;
            border-radius: 0.75rem;
            padding: 1.25rem;
        }}
        
        .card-elevated {{
            background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
            border: 1px solid #475569;
            border-radius: 1rem;
            padding: 1.5rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        }}
        
        .btn-primary {{
            background-color: #3b82f6;
            color: #ffffff;
            border-radius: 0.5rem;
            height: 40px;
            padding: 0 1rem;
            font-size: 13px;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
            border: none;
            cursor: pointer;
        }}
        
        .btn-primary:hover {{
            background-color: #60a5fa;
        }}
        
        .btn-ghost {{
            background-color: transparent;
            color: #94a3b8;
            border-radius: 0.5rem;
            padding: 0 1rem;
            height: 40px;
            font-size: 13px;
            font-weight: 500;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
            border: 1px solid #334155;
            cursor: pointer;
        }}
        
        .btn-ghost:hover {{
            background-color: #1e293b;
            color: #f1f5f9;
        }}
        
        .nav-item {{
            padding: 0.625rem 0.875rem;
            border-radius: 0.5rem;
            transition: all 0.2s ease;
            cursor: pointer;
            font-size: 14px;
        }}
        
        .nav-item:hover {{
            background-color: #1e293b;
        }}
        
        .nav-item.active {{
            background-color: #3b82f6;
            color: #ffffff;
        }}
        
        .example-card {{
            background-color: #0f172a;
            border-left: 2px solid #3b82f6;
            padding: 1rem 1.25rem;
            margin: 1rem 0;
            border-radius: 0 0.5rem 0.5rem 0;
        }}
        
        .hint-box {{
            background-color: rgba(245, 158, 11, 0.08);
            border: 1px solid rgba(245, 158, 11, 0.25);
            border-radius: 0.5rem;
            padding: 0.875rem 1rem;
            margin: 0.75rem 0;
        }}
        
        .badge-hint {{
            background-color: #f59e0b;
            color: #78350f;
            border-radius: 9999px;
            padding: 2px 10px;
            font-size: 11px;
            font-weight: 600;
        }}
        
        .definition-card {{
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(16, 185, 129, 0.05) 100%);
            border: 1px solid rgba(59, 130, 246, 0.3);
            border-radius: 0.75rem;
            padding: 1.25rem;
        }}
        
        .progress-bar {{
            height: 3px;
            background-color: #1e293b;
            border-radius: 2px;
            overflow: hidden;
        }}
        
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #3b82f6, #10b981);
            border-radius: 2px;
            transition: width 0.3s ease;
        }}
        
        .tab-content {{
            display: none;
        }}
        
        .tab-content.active {{
            display: block;
            animation: fadeIn 0.3s ease;
        }}
        
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        .math-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
        }}
        
        .math-table th {{
            background-color: #0f172a;
            padding: 0.625rem 0.75rem;
            text-align: left;
            font-weight: 600;
            color: #94a3b8;
            font-size: 12px;
            text-transform: uppercase;
            border-bottom: 1px solid #334155;
        }}
        
        .math-table td {{
            padding: 0.625rem 0.75rem;
            border-bottom: 1px solid #334155;
        }}
        
        .katex .mord, .katex .mbin, .katex .mrel, .katex .mop {{
            color: #f1f5f9;
        }}
    </style>
</head>
<body class="min-h-screen">
    <!-- Header -->
    <header class="bg-surface-dim border-b border-surface-container-high sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-6 py-3 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="w-9 h-9 bg-primary rounded-lg flex items-center justify-center">
                    <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
                    </svg>
                </div>
                <div>
                    <h1 class="text-lg font-semibold text-on-surface">{title}</h1>
                    <p class="text-xs text-on-surface-variant uppercase tracking-wider">{subtitle}</p>
                </div>
            </div>
            <div class="flex items-center gap-3">
                <div class="flex items-center gap-2">
                    <div class="w-24 progress-bar">
                        <div class="progress-fill" style="width: 0%"></div>
                    </div>
                </div>
                <button class="btn-ghost text-sm">保存进度</button>
            </div>
        </div>
    </header>

    <div class="max-w-6xl mx-auto px-6 py-6 flex gap-6">
        <!-- Sidebar Navigation -->
        <aside class="w-56 flex-shrink-0">
            <div class="card-standard sticky top-20">
                <h3 class="text-xs text-on-surface-variant uppercase tracking-wider mb-3 font-semibold">章节导航</h3>
                <nav class="space-y-1">
                    {nav_items}
                </nav>
            </div>
        </aside>

        <!-- Main Content -->
        <main class="flex-1 min-w-0">
            {content}
        </main>
    </div>

    <!-- Footer -->
    <footer class="bg-surface-dim border-t border-surface-container-high mt-12">
        <div class="max-w-6xl mx-auto px-6 py-6">
            <div class="flex items-center justify-between">
                <div>
                    <p class="text-sm text-on-surface-variant">{title} · 上海高中数学</p>
                </div>
                <div class="flex items-center gap-3">
                    <button class="btn-ghost">上一章</button>
                    <button class="btn-primary">下一章</button>
                </div>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener("DOMContentLoaded", function() {{
            renderMathInElement(document.body, {{
                delimiters: [
                    {{left: '$$', right: '$$', display: true}},
                    {{left: '$', right: '$', display: false}}
                ],
                throwOnError: false
            }});
        }});

        function showSection(sectionId) {{
            document.querySelectorAll('.tab-content').forEach(section => {{
                section.classList.remove('active');
            }});
            document.getElementById(sectionId).classList.add('active');
            
            document.querySelectorAll('.nav-item').forEach(item => {{
                item.classList.remove('active');
            }});
            event.currentTarget.classList.add('active');
            
            setTimeout(() => {{
                const section = document.getElementById(sectionId);
                if (section) {{
                    renderMathInElement(section, {{
                        delimiters: [
                            {{left: '$$', right: '$$', display: true}},
                            {{left: '$', right: '$', display: false}}
                        ],
                        throwOnError: false
                    }});
                }}
            }}, 10);
            
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}
    </script>
</body>
</html>'''
    
    return html_template

def convert_chapter(input_path, output_dir, title, subtitle):
    """转换单个章节"""
    print(f"\n正在处理: {title}")
    
    # 读取Markdown文件
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 解析章节结构
    sections = parse_markdown(content)
    print(f"  找到 {len(sections)} 个主要章节")
    
    # 生成HTML
    html_content = generate_html(title, subtitle, sections)
    
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 写入HTML文件
    output_path = os.path.join(output_dir, 'index.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"  ✓ 已生成: {output_path}")
    return True

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 5:
        print("用法: python convert.py <input_file> <output_dir> <title> <subtitle>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_dir = sys.argv[2]
    title = sys.argv[3]
    subtitle = sys.argv[4]
    
    convert_chapter(input_path, output_dir, title, subtitle)
