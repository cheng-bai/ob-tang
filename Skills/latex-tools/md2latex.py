#!/usr/bin/env python3
"""
整合脚本 - 一键执行 MD 优化 → LaTeX 生成 → PDF 编译
"""

import argparse
import sys
from pathlib import Path

# 添加脚本目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from md_optimizer import MDOptimizer
from md2tex import MD2TeXConverter
from dual_compiler import DualCompiler


def main():
    parser = argparse.ArgumentParser(description='MD 转 LaTeX 双版本 PDF')
    parser.add_argument('input', help='输入 MD 文件路径')
    parser.add_argument('-o', '--output', default='./outputs', help='输出目录')
    parser.add_argument('-s', '--step', choices=['optimize', 'translate', 'compile', 'all'], 
                        default='all', help='执行步骤')
    parser.add_argument('--no-analysis', action='store_true', 
                        help='不调用 math-master-teacher 生成考点分析')
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    output_dir = Path(args.output)
    
    if not input_path.exists():
        print(f"错误：输入文件不存在 {input_path}")
        sys.exit(1)
    
    # 创建工作目录
    work_dir = output_dir / 'work'
    work_dir.mkdir(parents=True, exist_ok=True)
    
    print("=" * 60)
    print(f"输入：{input_path}")
    print(f"输出：{output_dir}")
    print(f"步骤：{args.step}")
    print("=" * 60)
    print()
    
    # Step 1: MD 优化
    if args.step in ['optimize', 'all']:
        print("【Step 1】MD 优化...")
        optimizer = MDOptimizer()
        optimized_md = work_dir / f"{input_path.stem}-optimized.md"
        optimizer.optimize(str(input_path), str(optimized_md))
        print(f"优化完成：{optimized_md}")
        print()
    else:
        optimized_md = work_dir / f"{input_path.stem}-optimized.md"
    
    # Step 2: LaTeX 生成
    if args.step in ['translate', 'all']:
        print("【Step 2】生成 LaTeX...")
        converter = MD2TeXConverter()
        tex_dir = work_dir / 'tex'
        student_tex, teacher_tex = converter.convert(str(optimized_md), str(tex_dir))
        print(f"学生版：{student_tex}")
        print(f"教师版：{teacher_tex}")
        print()
    else:
        tex_dir = work_dir / 'tex'
        student_tex = tex_dir / f"{input_path.stem}-学生版.tex"
        teacher_tex = tex_dir / f"{input_path.stem}-教师版.tex"
    
    # Step 3: 编译 PDF
    if args.step in ['compile', 'all']:
        print("【Step 3】编译 PDF...")
        compiler = DualCompiler()
        pdf_dir = output_dir / 'pdf'
        student_pdf, teacher_pdf = compiler.compile_dual(
            str(student_tex), str(teacher_tex), str(pdf_dir)
        )
        
        print()
        print("=" * 60)
        print("编译完成！")
        print("=" * 60)
        print(f"学生版 PDF：{student_pdf}")
        print(f"教师版 PDF：{teacher_pdf}")
        print()
        print("建议：")
        print("- 学生版用于课堂练习或考试")
        print("- 教师版用于备课和讲评")
        print("=" * 60)


if __name__ == '__main__':
    main()
