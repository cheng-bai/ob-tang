#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <input.md>"
  exit 1
fi

IN="$1"
perl -pe 's/^:::space\s+type=([a-z]+)\s+level=([ABC])\s+lines=(\d+)[ \t]*$/::: {.space data-type="$1" data-level="$2" data-lines="$3"}/' "$IN"
