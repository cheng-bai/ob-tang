#!/usr/bin/env python3
"""
双版本编译器 - 编译学生版和教师版 LaTeX 为 PDF
"""

import subprocess
import sys
from pathlib import Path


class DualCompiler:
    """双版本 PDF 编译器"""
    
    def __init__(self, workdir: str = None):
        self.workdir = workdir or "."
    
    def compile_tex(self, tex_path: str, output_dir: str = None) -> str:
        """编译单个 tex 文件为 PDF"""
        tex_path = Path(tex_path)
        output_dir = Path(output_dir) if output_dir else tex_path.parent
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # 切换到 tex 所在目录编译
        workdir = tex_path.parent
        filename = tex_path.name
        
        print(f"编译：{filename}")
        print(f"工作目录：{workdir}")
        
        # xelatex 编译两遍（确保交叉引用正确）
        for i in range(1, 3):
            print(f"  第 {i} 次编译...")
            result = subprocess.run(
                ['xelatex', '-interaction=nonstopmode', filename],
                cwd=workdir,
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                print(f"  编译出错！")
                print(result.stderr[-500:] if len(result.stderr) > 500 else result.stderr)
                return None
        
        # 移动 PDF 到输出目录
        pdf_name = tex_path.stem + '.pdf'
        pdf_source = workdir / pdf_name
        pdf_target = output_dir / pdf_name
        
        if pdf_source.exists():
            pdf_source.rename(pdf_target)
            print(f"  PDF 已生成：{pdf_target}")
            print(f"  文件大小：{pdf_target.stat().st_size / 1024:.1f} KB")
            return str(pdf_target)
        else:
            print(f"  错误：PDF 文件未生成")
            return None
    
    def compile_dual(self, student_tex: str, teacher_tex: str, output_dir: str) -> tuple:
        """编译双版本"""
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        print("=" * 50)
        print("开始编译学生版...")
        print("=" * 50)
        student_pdf = self.compile_tex(student_tex, output_dir)
        
        print()
        print("=" * 50)
        print("开始编译教师版...")
        print("=" * 50)
        teacher_pdf = self.compile_tex(teacher_tex, output_dir)
        
        return student_pdf, teacher_pdf


def main():
    """命令行入口"""
    if len(sys.argv) < 3:
        print("用法: python dual_compiler.py <学生版.tex> <教师版.tex> [output_dir]")
        sys.exit(1)
    
    student_tex = sys.argv[1]
    teacher_tex = sys.argv[2]
    output_dir = sys.argv[3] if len(sys.argv) > 3 else './outputs'
    
    compiler = DualCompiler()
    compiler.compile_dual(student_tex, teacher_tex, output_dir)


if __name__ == '__main__':
    main()
