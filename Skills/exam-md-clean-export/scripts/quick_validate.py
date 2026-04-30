#!/usr/bin/env python3
"""Validate the exam Markdown cleanup/export workflow.

Usage:
    python3 quick_validate.py <exam-split-dir>
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys


FRONT_KP_RE = re.compile(r"^###\s*考点[:：]", re.MULTILINE)
TEX_KP_RE = re.compile(r"\\kp\{")


def scan_file(path: pathlib.Path, pattern: re.Pattern[str]) -> list[int]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []
    return [m.start() for m in pattern.finditer(text)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="Exam split directory to validate")
    args = parser.parse_args()

    root = pathlib.Path(args.target).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        print(f"ERROR target is not a directory: {root}")
        return 2

    md_hits: list[pathlib.Path] = []
    tex_hits: list[pathlib.Path] = []
    pdfs: list[pathlib.Path] = []

    for path in root.rglob("*"):
        if path.is_dir():
            continue
        if path.suffix == ".md" and scan_file(path, FRONT_KP_RE):
            md_hits.append(path)
        elif path.suffix == ".tex" and scan_file(path, TEX_KP_RE):
            tex_hits.append(path)
        elif path.suffix == ".pdf":
            pdfs.append(path)

    print(f"target: {root}")
    print(f"pdf_count: {len(pdfs)}")
    print(f"front_heading_hits: {len(md_hits)}")
    for path in md_hits:
        print(f"  MD {path.relative_to(root)}")
    print(f"tex_kp_hits: {len(tex_hits)}")
    for path in tex_hits:
        print(f"  TEX {path.relative_to(root)}")

    if md_hits or tex_hits:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
