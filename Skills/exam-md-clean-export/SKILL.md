---
name: exam-md-clean-export
description: Use this when processing a Chinese high-school math exam Markdown split/export workflow in latex-maki-math, especially when removing unwanted heading styles like "### 考点：...", regenerating student/teacher/split Markdown, converting Markdown to LaTeX, compiling PDFs, and verifying no stale labels remain.
---

# Exam MD Clean Export

This skill captures the verified workflow:

`source OCR Markdown -> split_md.py -> clean split Markdown -> md2tex.py -> XeLaTeX PDFs -> residue checks`

Default repository:

```text
/Users/tangchengbaiair/Downloads/latex-maki-math
```

## When To Use

Use this skill when the user asks to:

- delete repeated style headings such as `### 考点：棱柱体积公式`;
- adjust generated exam Markdown style in a split exam directory;
- regenerate student, teacher, and topic-split versions;
- export or refresh LaTeX/PDF files after Markdown cleanup;
- verify the final PDFs/TeX no longer contain old labels.

## Default Workflow

1. Locate the target exam directory.

   Prefer a concrete directory named by the user. If absent, inspect directories matching:

   ```bash
   find . -maxdepth 2 -type d -name '*拆分版*' -print
   ```

2. Search before editing.

   ```bash
   rg -n "^###\\s*考点[:：]" <target-dir>
   rg -n "knowledge_points|考点|^\\s*out\\.append\\(f?\"###" <target-dir>/*.py
   ```

3. Fix the generator first.

   If `split_md.py` emits `out.append(f"### {knowledge_points[q_num]}\n\n")`, remove that append and keep the question body append. Do not only patch generated Markdown, because regeneration would reintroduce the heading.

4. Preserve teacher-answer metadata unless the user explicitly asks to remove it.

   - Remove: question-front headings like `### 考点：...`.
   - Keep by default: answer-block metadata like `【考点】：...`, because it belongs to teacher answer information rather than the visual question heading.

5. Regenerate Markdown.

   Run from the target exam directory:

   ```bash
   python3 split_md.py
   ```

6. Regenerate LaTeX/PDF.

   ```bash
   python3 md2tex.py
   ```

   If sandboxing blocks writes or TeX auxiliary cache files, rerun with the required escalation and explain that the command writes generated Markdown, TeX, aux, log, and PDF files.

7. Verify residue.

   ```bash
   rg -n "^###\\s*考点[:：]" .
   rg -n -F "\\kp{" tex
   python3 ../Skills/exam-md-clean-export/scripts/quick_validate.py .
   ```

   A successful cleanup should report no question-front `### 考点` headings and no generated `\kp{...}` labels in TeX.

## Completion Standard

Report these items:

- edited generator file path;
- regenerated Markdown groups;
- regenerated PDF paths or PDF count;
- exact verification result for `### 考点` and `\kp{`;
- whether `【考点】：...` inside teacher answers was kept or removed.

## Common Failure Modes

- Editing only generated Markdown: next `split_md.py` run brings the headings back.
- Forgetting `md2tex.py`: Markdown is clean but the PDFs still show old labels.
- Treating `【考点】：...` and `### 考点：...` as the same thing: they are different surfaces.
- Stopping after a failed sandbox write: rerun the generation command with write permission instead of assuming the script logic failed.
