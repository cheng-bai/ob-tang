#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Append an AI work summary entry to daily worklog.
Usage:
  log_ai_work.py --task "..." --purpose "..." --actions "..." --files "..." --result "..." --todo "..." --base "/path/to/memory"
"""
import argparse
from datetime import datetime
from pathlib import Path

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--task", required=True, help="Short task title")
    p.add_argument("--purpose", default="", help="Purpose/goal")
    p.add_argument("--actions", default="", help="What was done (ops/commands)")
    p.add_argument("--files", default="", help="Changed/created file paths")
    p.add_argument("--result", default="", help="Key results")
    p.add_argument("--todo", default="", help="Remaining items/risks")
    p.add_argument("--base", required=True, help="Base memory path")
    args = p.parse_args()

    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M")

    base = Path(args.base)
    log_dir = base / "ai-worklog"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / f"{date_str}.md"

    entry = [
        f"## {time_str} {args.task}",
        f"- 目的：{args.purpose}",
        f"- 做了什么：{args.actions}",
        f"- 变更清单：{args.files}",
        f"- 关键结果：{args.result}",
        f"- 待办/风险：{args.todo}",
        "",
    ]

    with open(log_file, "a", encoding="utf-8") as f:
        f.write("\n".join(entry))

if __name__ == "__main__":
    main()
