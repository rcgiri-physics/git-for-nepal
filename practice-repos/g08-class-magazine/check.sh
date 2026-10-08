#!/usr/bin/env bash
set -euo pipefail
d="$(mktemp -d)/repo"
bash make-repo.sh "$d" >/dev/null 2>&1
n=$(git -C "$d" rev-list --count HEAD)
[ "$n" -eq 6 ] || { echo "expected 6 commits, got $n"; exit 1; }
git -C "$d" log --date=short --format='%ad %s' | tr -d '\r' | diff - <(tr -d '\r' < log-sample.txt) \
  || { echo "log-sample.txt out of date"; exit 1; }
rm -rf "$(dirname "$d")"
echo "g08 ok"
