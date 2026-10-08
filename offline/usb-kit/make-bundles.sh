#!/usr/bin/env bash
# Build .bundle files of every practice repo for tier-1 (offline) classes.
# Usage: bash make-bundles.sh out-dir   ->  out-dir/g08-class-magazine.bundle, g09-ward-facts.bundle, ...
set -euo pipefail
root="$(cd "$(dirname "$0")/../.." && pwd)"
out="$(mkdir -p "${1:-bundles}" && cd "${1:-bundles}" && pwd)"
tmp="$(mktemp -d)"
# Grade 8 has a scripted 6-commit history.
bash "$root/practice-repos/g08-class-magazine/make-repo.sh" "$tmp/g08-class-magazine" >/dev/null 2>&1
git -C "$tmp/g08-class-magazine" bundle create "$out/g08-class-magazine.bundle" --all >/dev/null 2>&1
# The other practice repos are plain folders: make a one-commit repo from each.
for d in "$root"/practice-repos/g09-* "$root"/practice-repos/g1*; do
  n="$(basename "$d")"
  cp -r "$d" "$tmp/$n"
  git -C "$tmp/$n" init -q -b main
  git -C "$tmp/$n" -c user.name=Teacher -c user.email=teacher@example.invalid add -A
  git -C "$tmp/$n" -c user.name=Teacher -c user.email=teacher@example.invalid commit -q -m "Starter files for $n"
  git -C "$tmp/$n" bundle create "$out/$n.bundle" --all >/dev/null 2>&1
done
rm -rf "$tmp"
ls "$out"
