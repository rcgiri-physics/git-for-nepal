#!/usr/bin/env bash
# Build a self-hosted, analytics-free copy of learnGitBranching (MIT) for the USB kit.
# Tested 2026-10-07 with Node 24 and learnGitBranching commit 287153f (v0.8.0). Needs internet once.
set -euo pipefail
out="${1:-learnGitBranching-build}"
commit="${LGB_COMMIT:-287153f}"
work="$(mktemp -d)"
git clone -q https://github.com/pcottle/learnGitBranching "$work/lgb"
git -C "$work/lgb" checkout -q "$commit"
npm install --silent --prefix "$work/yarn" yarn
export PATH="$work/yarn/node_modules/.bin:$PATH"
( cd "$work/lgb" && yarn install --frozen-lockfile >/dev/null && yarn build >/dev/null )
rm -rf "$out" && cp -r "$work/lgb/build" "$out"
cp "$work/lgb/LICENSE.md" "$out/LICENSE-learnGitBranching.md"   # MIT: keep the licence file
# Remove Google Analytics (children's classroom, offline use): the gtag loader and its inline config block.
python - "$out/index.html" <<'PY'
import re, sys
p = sys.argv[1]
t = open(p, encoding="utf-8").read()
t = re.sub(r'\s*<!-- Google tag \(gtag\.js\) -->\s*<script async src="https://www\.googletagmanager\.com[^"]*"></script>\s*<script>.*?</script>', "\n", t, count=1, flags=re.S)
assert "googletagmanager" not in t, "analytics not removed"
open(p, "w", encoding="utf-8").write(t)
PY
rm -rf "$work"
echo "Built $out. Open $out/index.html, or: python -m http.server -d $out 8080"
echo "Note: the app shows two promotional links to external sites; they do nothing offline."
