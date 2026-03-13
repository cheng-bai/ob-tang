#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <input.md> <output.pdf>"
  exit 1
fi

IN="$1"
OUT="$2"
BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
NORMALIZER="$BASE_DIR/scripts/normalize_space_markers.sh"
SPACE_FILTER="$BASE_DIR/scripts/space_lines.lua"
HEADER="$BASE_DIR/assets/header.tex"
TMP_MD="$(mktemp)"
trap 'rm -f "$TMP_MD"' EXIT

if ! command -v pandoc >/dev/null 2>&1; then
  echo "Error: pandoc not found. Install with: brew install pandoc"
  exit 1
fi

if ! command -v xelatex >/dev/null 2>&1; then
  echo "Error: xelatex not found. Install MacTeX (or BasicTeX)."
  exit 1
fi

bash "$NORMALIZER" "$IN" > "$TMP_MD"

pandoc "$TMP_MD" \
  --standalone \
  --from markdown+raw_html+fenced_divs+bracketed_spans+tex_math_dollars \
  --lua-filter "$SPACE_FILTER" \
  --pdf-engine=xelatex \
  --include-in-header "$HEADER" \
  -V documentclass=article \
  -V classoption=twoside \
  -V papersize=a4 \
  -V fontsize=12pt \
  -V colorlinks=false \
  -o "$OUT"

echo "Generated: $OUT"
