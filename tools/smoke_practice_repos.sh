#!/usr/bin/env bash
# For each practice repo: it has a README, a check script, and the check script passes
# on a pristine copy (clone-equivalent). Fails if any practice repo is broken.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
fail=0
for d in "$root"/practice-repos/*/; do
  name="$(basename "$d")"
  [ -f "$d/README.md" ] || { echo "ERROR: $name lacks README.md"; fail=1; continue; }
  if [ -f "$d/check.sh" ]; then
    tmp="$(mktemp -d)"; cp -r "$d"/. "$tmp"/
    ( cd "$tmp" && bash check.sh ) && echo "ok: $name" || { echo "ERROR: $name check.sh failed"; fail=1; }
    rm -rf "$tmp"
  else
    echo "ERROR: $name lacks check.sh"; fail=1
  fi
done
exit $fail
