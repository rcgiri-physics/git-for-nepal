#!/usr/bin/env bash
# Build a repo with 12 commits; commit 7 plants a bug that makes check.sh fail (for Module 7: git bisect).
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
dest="${1:-bisect-demo}"
[ -e "$dest" ] && { echo "$dest exists"; exit 1; }
mkdir -p "$dest/data" && cd "$dest" && git init -q -b main
git config user.name Teacher && git config user.email teacher@example.invalid
cp "$here/check.sh" check.sh
printf 'id,name,value\n1,alpha,10\n' > data/sample.csv
git add . && git commit -q -m "Add check script and first row"
for i in $(seq 2 12); do
  if [ "$i" -eq 7 ]; then
    printf '%s,bad row without a value\n' "$i" >> data/sample.csv   # the planted bug
  else
    printf '%s,row%s,%s\n' "$i" "$i" "$((i*10))" >> data/sample.csv
  fi
  git add . && git commit -q -m "Add row $i"
done
echo "Created $dest with $(git rev-list --count HEAD) commits"
