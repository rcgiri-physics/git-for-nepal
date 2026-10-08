#!/usr/bin/env bash
set -euo pipefail
mkdir -p clean && python clean.py >/dev/null
lines=$(wc -l < clean/schools.csv | tr -d ' ')
[ "$lines" -eq 4 ] || { echo "expected header + 3 rows, got $lines lines"; exit 1; }
grep -q "Test Primary School" clean/schools.csv || { echo "name cleaning failed"; exit 1; }
echo "g11 ok"
