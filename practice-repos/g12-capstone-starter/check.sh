#!/usr/bin/env bash
# Validate data/sample.csv: header is id,name,value and every row has 3 numeric-id/value fields.
set -euo pipefail
f=data/sample.csv
[ "$(head -1 "$f" | tr -d '\r')" = "id,name,value" ] || { echo "bad header"; exit 1; }
tail -n +2 "$f" | tr -d '\r' | awk -F, 'NF!=3 || $1 !~ /^[0-9]+$/ || $3 !~ /^[0-9]+$/ {print "bad row: " $0; bad=1} END {exit bad}'
echo "g12 ok"
