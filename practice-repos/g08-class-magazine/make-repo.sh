#!/usr/bin/env bash
# Build the Grade 8 starter repo with a fixed, reproducible history.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
dest="${1:-my-magazine}"
[ -e "$dest" ] && { echo "$dest already exists"; exit 1; }
mkdir -p "$dest" && cd "$dest" && git init -q -b main
git config user.name "Teacher"
git config user.email "teacher@example.invalid"
commit() { # n message date
  cp "$here/versions/v$1.md" article.md
  git add article.md
  GIT_AUTHOR_DATE="$3T10:00:00" GIT_COMMITTER_DATE="$3T10:00:00" git commit -q -m "$2"
}
commit 1 "Add working title" 2026-10-01
commit 2 "Add better title and opening line" 2026-10-01
commit 3 "Say where the festival is and what happens" 2026-10-02
commit 4 "Add paragraph about food stalls and library fund" 2026-10-05
commit 5 "Add Class Eight momo paragraph (typo left in on purpose)" 2026-10-05
commit 6 "Add closing sentence about the tastiest stall" 2026-10-07
echo "Created $dest with $(git rev-list --count HEAD) commits"
