#!/usr/bin/env python3
"""Check that relative Markdown links in docs/ and top-level *.md resolve to files.
External (http) links are not fetched here; run a separate link checker online."""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
errors = 0
files = list((ROOT / "docs").rglob("*.md")) + list(ROOT.glob("*.md"))
for f in files:
    in_code = False
    for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip().startswith("```"):
            in_code = not in_code
        if in_code:
            continue
        for target in LINK.findall(line):
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            path = target.split("#")[0]
            if not path:
                continue
            if not (f.parent / path).resolve().exists():
                print(f"ERROR: {f.relative_to(ROOT)}:{n}: broken link {target}")
                errors += 1
print(f"links checked in {len(files)} files, {errors} broken")
sys.exit(1 if errors else 0)
