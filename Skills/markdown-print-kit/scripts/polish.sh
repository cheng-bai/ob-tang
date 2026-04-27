#!/usr/bin/env bash
set -euo pipefail

# polish.sh - 润色 Markdown 文件，使其符合 Obsidian 排版规范
# 用法：bash scripts/polish.sh <input.md> [output.md]

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <input.md> [output.md]"
  echo "  若不指定 output.md，则原地修改"
  exit 1
fi

IN="$1"
OUT="${2:-$IN}"

if [[ ! -f "$IN" ]]; then
  echo "Error: File '$IN' not found."
  exit 1
fi

# 使用 Perl 进行多步转换
perl -e '
use strict;
use warnings;
use utf8;

# 读取整个文件
local $/;
binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
my $content = <STDIN>;

# 1. 转换 :::space 为 Obsidian callout 格式
# :::space type=mc level=A lines=2  ->  > [!blank]- 留白\n> - 类型：选择题\n> - 难度：A\n> - 行数：2
$content =~ s/^:::space\s+type=([a-z]+)\s+level=([ABC])\s+lines=(\d+)\s*\n:::\s*$/
  my ($type, $level, $lines) = ($1, $2, $3);
  my $type_name = $type eq "mc" ? "选择题" : ($type eq "fill" ? "填空题" : "解答题");
  "> [!blank]- 留白\n> - 类型：$type_name\n> - 难度：$level\n> - 行数：$lines\n"/gme;

# 2. 规范化选择题选项格式：将 "A." 开头的行转为列表
# 匹配连续的四行 A./B./C./D.
$content =~ s/^(\s*)A\.\s*(.+?)\n(\s*)B\.\s*(.+?)\n(\s*)C\.\s*(.+?)\n(\s*)D\.\s*(.+?)\n/
  "- A. $2\n- B. $4\n- C. $6\n- D. $8\n"/gme;

# 3. 确保 **题目** 后有一个空行
$content =~ s/(\*\*题目\*\*.+?)\n(?!\n)(?![\-\*\>]|\*\*答案\*\*|<!--)/$1\n\n/g;

# 4. 规范化章节标题：确保 ### 前后有适当空行
$content =~ s/([^\n])\n(### .+)/$1\n\n$2/g;
$content =~ s/(### .+)\n([^\n#])/ $1\n\n$2/g;

# 5. 添加/更新 frontmatter（如果没有）
if ($content !~ /^---\n/) {
  my $title = "";
  if ($content =~ /^#\s+(.+)/m) {
    $title = $1;
  }
  my $date = `date +%Y-%m-%d`;
  chomp $date;
  $content = "---\ntags: [数学/讲义, 打印]\ncreated: $date\nversion: student\n---\n\n$content";
}

print $content;
' < "$IN" > "$OUT"

echo "Polished: $OUT"
