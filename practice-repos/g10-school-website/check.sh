#!/usr/bin/env bash
set -euo pipefail
fail=0
for f in *.html; do
  grep -q "<title>" "$f" || { echo "ERROR: $f has no <title>"; fail=1; }
  for href in $(grep -o 'href="[^"]*"' "$f" | sed 's/href="//;s/"$//'); do
    case "$href" in http*|mailto:*|\#*) continue;; esac
    [ -f "$href" ] || { echo "ERROR: $f links to missing $href"; fail=1; }
  done
done
[ $fail -eq 0 ] && echo "g10 ok"
exit $fail
