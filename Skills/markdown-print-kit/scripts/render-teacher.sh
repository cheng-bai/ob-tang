#!/usr/bin/env bash
set -euo pipefail

# render-teacher.sh - 导出教师版 PDF（含答案）
# 用法：bash scripts/render-teacher.sh <input.md> <output.pdf>

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <input.md> <output.pdf>"
  exit 1
fi

IN="$1"
OUT="$2"
BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TEMPLATE="$BASE_DIR/templates/worksheet.html"
CSS="$BASE_DIR/templates/print-teacher.css"
POLISHER="$BASE_DIR/scripts/polish.sh"
CALLOUT="$BASE_DIR/scripts/convert-callouts.lua"
TMP_POLISHED="$(mktemp)"
TMP_MD="$(mktemp)"
trap 'rm -f "$TMP_POLISHED" "$TMP_MD"' EXIT

# 检查 pandoc
if ! command -v pandoc >/dev/null 2>&1; then
  echo "Error: pandoc not found."
  echo "Install: brew install pandoc"
  exit 1
fi

# 步骤 1: 润色 Markdown
bash "$POLISHER" "$IN" > "$TMP_POLISHED"

# 步骤 2: 转换 callout（保留答案）
pandoc "$TMP_POLISHED" \
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

echo "✓ Teacher version generated: $OUT"
