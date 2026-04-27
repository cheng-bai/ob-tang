import os, re, glob

books = [
    ("必修第一册", "沪教版必修第一册2026.pdf_os_*/沪教版必修第一册2026-dollar.md"),
    ("必修第二册", "沪教版必修第二册2026.pdf_os_*/沪教版必修第二册2026-dollar.md"),
    ("必修第三册", "沪教版必修第三册2026.pdf_os_*/沪教版必修第三册2026-dollar.md"),
    ("必修第四册", "沪教版必修第四册2026.pdf_os_*/沪教版必修第四册2026-dollar.md"),
    ("选择性必修第一册", "沪教版选择性必修第一册2026.pdf_os_*/沪教版选择性必修第一册2026-dollar.md"),
    ("选择性必修第二册", "沪教版选择性必修第二册2026.pdf_os_*/沪教版选择性必修第二册2026-dollar.md"),
    ("选择性必修第三册", "沪教版选择性必修第三册2026.pdf_os_*/沪教版选择性必修第三册2026-dollar.md"),
]

chapter_pat = re.compile(r'^(?:#{1,3}\s*)?第\s*([一二三四五六七八九十\d]+)\s*章\s+(.+)$')
# 小节: 1.1 标题 或 ### 1.1 标题
section_pat = re.compile(r'^(?:#{1,3}\s*)?([\d]+\.[\d]+)\s+(.+)$')
# 定义/定理句提取
key_pats = [
    re.compile(r'(.{10,90}(?:定义|定理|公理|推论|性质|公式|法则|恒等式|结论).{0,40})'),
]

def extract(path, book_name):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    chapters = []
    current_chapter = None
    current_section = None
    
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        # 过滤出版信息、图片等
        if line.startswith('![') or '' in line or line.startswith('$$') or line.startswith('普通高中教科书'):
            continue
        m = chapter_pat.match(line)
        if m:
            num = m.group(1)
            title = m.group(2).strip()
            # 过滤目录页可能重复出现的页码
            title = re.sub(r'\s+\d+\s*$', '', title)
            current_chapter = {'num': num, 'title': title, 'sections': []}
            chapters.append(current_chapter)
            current_section = None
            continue
        m = section_pat.match(line)
        if m and current_chapter:
            sec_num = m.group(1)
            sec_title = m.group(2).strip()
            sec_title = re.sub(r'\s+\d+\s*$', '', sec_title)
            if sec_title.isdigit() or '![' in sec_title:
                continue
            current_chapter['sections'].append({'num': sec_num, 'title': sec_title, 'keys': []})
            current_section = current_chapter['sections'][-1]
            continue
        # 关键句提取（每小节最多3条）
        if current_section and len(current_section['keys']) < 3:
            # 简单启发：包含特定关键词且长度适中
            if any(k in line for k in ['定义', '定理', '公理', '推论', '性质', '公式', '法则', '恒等式', '结论']):
                if 15 <= len(line) <= 120 and '![' not in line and not line.startswith('$$'):
                    # 去重
                    if line not in [k['text'] for k in current_section['keys']]:
                        current_section['keys'].append({'text': line, 'type': 'key'})
    return chapters

all_data = {}
for name, pat in books:
    paths = glob.glob(pat)
    if paths:
        all_data[name] = extract(paths[0], name)
    else:
        print(f"未找到: {name}")

# 生成大纲
output_lines = ["# 教材知识点大纲", ""]

order = [
    "必修第一册", "必修第二册", "必修第三册", "必修第四册",
    "选择性必修第一册", "选择性必修第二册", "选择性必修第三册"
]

for book in order:
    if book not in all_data:
        continue
    output_lines.append(f"# {book}")
    output_lines.append("")
    chapters = all_data[book]
    for c in chapters:
        output_lines.append(f"## 第{c['num']}章 {c['title']}")
        output_lines.append("")
        for s in c['sections']:
            output_lines.append(f"- {s['num']} {s['title']}")
            for k in s['keys']:
                output_lines.append(f"  - **{k['text']}**")
        output_lines.append("")

os.makedirs('outputs', exist_ok=True)
with open('outputs/教材知识点大纲.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print("生成完成，共处理以下册数:")
for book in order:
    if book in all_data:
        print(f"  {book}: {len(all_data[book])} 章")
