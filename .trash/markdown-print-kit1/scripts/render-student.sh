#!/usr/bin/env bash
set -euo pipefail

# render-student.sh - 导出学生版 PDF（无答案）
# 用法：bash scripts/render-student.sh <input.md> <output.pdf>

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <input.md> <output.pdf>"
  exit 1
fi

IN="$1"
OUT="$2"
BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TEMPLATE="$BASE_DIR/templates/worksheet.html"
CSS="$BASE_DIR/templates/print.css"
POLISHER="$BASE_DIR/scripts/polish.sh"
FILTER="$BASE_DIR/scripts/remove-answers.lua"
CALLOUT="$BASE_DIR/scripts/convert-callouts.lua"
TMP_MD="$(mktemp)"
TMP_POLISHED="$(mktemp)"
trap 'rm -f "$TMP_MD" "$TMP_POLISHED"' EXIT

# 检查 pandoc
if ! command -v pandoc >/dev/null 2>&1; then
  echo "Error: pandoc not found."
  echo "Install: brew install pandoc"
  exit 1
fi

# 步骤 1: 润色 Markdown
bash "$POLISHER" "$IN" > "$TMP_POLISHED"

# 步骤 2: 移除答案（学生版）+ 转换 callout
pandoc "$TMP_POLISHED" \
  --lua-filter "$FILTER" \
  --lua-filter "$CALLOUT" \
  -o "$TMP_MD"

# 步骤 3: 选择 PDF 引擎
if command -v wkhtmltopdf >/dev/null 2>&1; then
  echo "Using wkhtmltopdf..."
  pandoc "$TMP_MD" \
    --standalone \
    --from markdown+raw_html+fenced_divs+callouts+bracketed_spans+tex_math_dollars \
    --template "$TEMPLATE" \
    --css "$CSS" \
    -V lang=zh-CN \
    -V geometry:a4paper \
    -V colorlinks=false \
    --pdf-engine=wkhtmltopdf \
    -o "$OUT"
else
  echo "Using xelatex..."
  pandoc "$TMP_MD" \
    --standalone \
    --from markdown+raw_html+fenced_divs+callouts+bracketed_spans+tex_math_dollars \
    --pdf-engine=xelatex \
    -V documentclass=article \
    -V classoption=twoside \
    -V papersize=a4 \
    -V mainfont='Songti SC' \
    -V monofont='Menlo' \
    -V geometry:inner=18mm \
    -V geometry:outer=14mm \
    -V geometry:top=16mm \
    -V geometry:bottom=16mm \
    -V geometry:bindingoffset=2mm \
    -V fontsize=12pt \
    -V colorlinks=false \
    -o "$OUT"
fi

echo "✓ Student version generated: $OUT"
