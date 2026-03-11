---
name: markdown-math-worksheet-pdf
description: Generate polished, printable student worksheet PDFs from Markdown math handouts. Use when the user asks to print/export Markdown to beautiful PDF, improve worksheet layout, add writing space lines, enforce A4 two-sided margins, keep multiple-choice options vertical, or hide answers/analysis for student versions.
---

# Markdown Math Worksheet PDF

Follow this skill to render high-school math Markdown into attractive, printable PDF handouts.

## Execute Workflow

1. Normalize worksheet markers.
Run `scripts/normalize_space_markers.sh` to convert custom `:::space type=... level=... lines=...` blocks into Pandoc fenced div attributes.

2. Render with Pandoc.
Run `scripts/render_student_pdf.sh <input.md> <output.pdf>`.
Use XeLaTeX output by default for robust local rendering.

3. Keep student output clean.
Store answers and analysis inside HTML comments in source markdown so student PDF excludes them.

4. Preserve worksheet readability.
Keep A/B/C option lines vertical and contiguous.
Keep one question block together where possible.

## Choose Defaults

- Paper: A4, two-sided (`inner/outer` mirrored margins).
- Density: medium whitespace.
- Space blocks:
`mc: A=2 B=3 C=3`, `fill: A=2 B=3 C=4`, `solve: A=6 B=8 C=10`.
- Writing area style: horizontal writing lines.

## Read References When Needed

- Read `references/authoring-spec.md` for Markdown authoring rules.
- Read `references/layout-tuning.md` for typography and spacing adjustments.

## Use Assets

- Use `assets/header.tex` for page geometry, heading style, and worksheet visual polish.

## Validate Quickly

- Confirm `pandoc` and `xelatex` exist before rendering.
- If rendering warnings show encoding issues, inspect source for malformed characters first.
