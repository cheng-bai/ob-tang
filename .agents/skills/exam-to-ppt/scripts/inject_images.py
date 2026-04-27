#!/usr/bin/env python3
"""
从 result.json 提取图片，注入到试卷 Markdown 中。

用法:
    python inject_images.py -r ../上海·2026_届崇明区高三数学二模详解.pdf_os_d7ci8valb0pc73bthkm0/result.json \
                            -i ../试卷库/work/崇明二模-optimized.md \
                            -o ../试卷库/work/崇明二模-with-images.md
"""

import argparse
import json
import os
import re
import shutil
import sys


def extract_question_images(result_json_path: str):
    """从 result.json 提取 题号 -> 图片路径列表 映射"""
    with open(result_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    full_md = '\n'.join(p.get('md', '') for p in data['pages'])

    # 匹配题号：数字. 或 ## 数字.
    q_matches = list(re.finditer(r'\n\s*(?:##\s*)?(\d+)\.\s*', full_md))

    question_images = {}
    for i, qm in enumerate(q_matches):
        qnum = int(qm.group(1))
        start = qm.start()
        end = q_matches[i + 1].start() if i + 1 < len(q_matches) else len(full_md)
        segment = full_md[start:end]
        imgs = re.findall(r'<img\s+src=["\'](.*?)["\']', segment)
        if imgs:
            question_images[qnum] = imgs

    return question_images


def inject_images(md_path: str, output_path: str, question_images: dict,
                  images_src_dir: str, images_dst_dir: str):
    """把图片注入到 md 文件中"""

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 确保目标图片目录存在
    os.makedirs(images_dst_dir, exist_ok=True)

    # 逐题处理：找到每道题的范围，替换或插入图片
    lines = content.split('\n')
    result_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]
        result_lines.append(line)

        # 检测题号行
        q_match = re.match(r'(\d+)\.\s*', line.strip())
        if q_match:
            qnum = int(q_match.group(1))

            # 收集本题内容直到下一题/章节/答案
            body_lines = []
            i += 1
            while i < len(lines):
                cur = lines[i].strip()
                if re.match(r'\d+\.\s*', cur) or re.match(r'##\s*', cur):
                    break
                if cur.startswith('【答案】') or cur.startswith('【解析】'):
                    break
                body_lines.append(lines[i])
                i += 1

            # 处理图片
            if qnum in question_images:
                img_paths = question_images[qnum]

                # 复制图片到目标目录
                for src_path in img_paths:
                    # 解析源路径（相对 result.json 所在目录）
                    src_full = os.path.normpath(os.path.join(
                        images_src_dir, src_path))
                    if os.path.exists(src_full):
                        dst_name = os.path.basename(src_path)
                        dst_full = os.path.join(images_dst_dir, dst_name)
                        if not os.path.exists(dst_full):
                            shutil.copy2(src_full, dst_full)
                            print(f'  📷 复制图片: {dst_name}')

                # 在 md 中替换占位符或插入图片
                body_text = '\n'.join(body_lines)

                if '<!-- 图：' in body_text or '<!-- 图:' in body_text:
                    # 替换占位符为第一个图片，同时清理后面可能残留的孤立字母
                    dst_name = os.path.basename(img_paths[0])
                    body_text = re.sub(
                        r'<!--\s*图[：:]\s*.*?\s*-->\s*\n?\s*[A-Da-d]?\s*\n?',
                        f'<img src="images/{dst_name}">\n',
                        body_text
                    )
                    # 如果有更多图片，追加
                    for extra_path in img_paths[1:]:
                        extra_name = os.path.basename(extra_path)
                        body_text += f'\n<img src="images/{extra_name}">'
                else:
                    # 没有占位符，在题干末尾插入图片
                    img_tags = []
                    for src_path in img_paths:
                        dst_name = os.path.basename(src_path)
                        img_tags.append(f'<img src="images/{dst_name}">')
                    body_text += '\n' + '\n'.join(img_tags)

                result_lines.extend(body_text.split('\n'))
                continue  # i 已经指向下一个位置
            else:
                result_lines.extend(body_lines)
                continue

        i += 1

    # 写入输出
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result_lines))

    print(f'\n✅ 注入完成: {output_path}')
    print(f'   图片目录: {images_dst_dir}')


def main():
    parser = argparse.ArgumentParser(description='从 result.json 提取图片注入到试卷 Markdown')
    parser.add_argument('-r', '--result-json', required=True, help='result.json 路径')
    parser.add_argument('-i', '--input', required=True, help='输入的 Markdown 文件')
    parser.add_argument('-o', '--output', required=True, help='输出的 Markdown 文件')
    parser.add_argument('--images-dir', default='images',
                        help='图片复制目标目录（默认: images）')
    args = parser.parse_args()

    if not os.path.exists(args.result_json):
        print(f'错误: 找不到 {args.result_json}')
        sys.exit(1)
    if not os.path.exists(args.input):
        print(f'错误: 找不到 {args.input}')
        sys.exit(1)

    print(f'📖 解析 result.json: {args.result_json}')
    question_images = extract_question_images(args.result_json)
    print(f'   找到 {len(question_images)} 道题目含图片:')
    for qnum in sorted(question_images):
        names = [os.path.basename(p) for p in question_images[qnum]]
        print(f'     题{qnum}: {names}')

    # 图片复制目标目录（相对于输出 md 文件所在目录）
    output_dir = os.path.dirname(os.path.abspath(args.output)) or '.'
    images_dst_dir = os.path.join(output_dir, args.images_dir)

    print(f'\n📝 注入图片到: {args.output}')
    inject_images(args.input, args.output, question_images,
                  os.path.dirname(args.result_json), images_dst_dir)


if __name__ == '__main__':
    main()
