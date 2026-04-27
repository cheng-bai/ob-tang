# 10-工具脚本

这个目录现在只保留“仍可能继续复用”的工具脚本。

## 当前状态

- `pipeline/` 是正式优先入口
- `scripts/` 放兼容入口或少量补充脚本
- `10-工具脚本/` 保留实验性但仍可能有参考价值的工具
- 明显历史版、调试版、一次性检查版已迁到 `99-归档备份/10-工具脚本-历史版本/`

## 建议优先顺序

1. `pipeline/`
2. `scripts/`
3. `10-工具脚本/`
4. `99-归档备份/`

## 当前保留在本目录的脚本

### 根目录脚本

- `analysis_generator.py`
- `dual_compiler.py`
- `enhanced_analysis.py`
- `fill_lectures.py`
- `fix_latex_symbols.py`
- `md2latex.py`
- `md2tex.py`
- `md_optimizer.py`
- `optimization_report.py`
- `smart_exam_generator.py`

### 子目录脚本

- `大纲提取/extract_outline.py`
- `转换脚本/convert_chapter.py`
- `转换脚本/convert_md_to_latex.py`
- `转换脚本/polish_math_textbook.py`

## 已迁移到归档的内容

### 历史版本

- `extract_outline_final.py`
- `extract_outline_v2.py`
- `extract_outline_v3.py`
- `extract_outline_v4.py`
- `extract_outline_v5.py`
- `convert_final.py`
- `convert_lecture_v2.py`
- `convert_lecture_v3.py`
- `convert_perfect.py`
- `convert_ultimate.py`
- `convert_ultimate_v2.py`
- `convert_ultimate_v3.py`

### 一次性检查与调试

- `check_beauty.py`
- `check_chapter2.py`
- `check_latex_quality.py`
- `debug_example.py`
- `debug_full.py`

### 重复旧入口

- 原 `10-工具脚本/generate_lecture.py` 已归档
- 兼容入口保留在 `scripts/generate_lecture.py`

## 维护约定

- 不再继续新增 `*_v2.py`、`*_v3.py`、`*_final.py`、`*_ultimate.py`
- 新的正式脚本直接放进 `pipeline/`
- 只有明确需要保留的实验工具才放进这里
