#!/usr/bin/env python3
"""Every folder in datasets/ must have a DATA.md with required fields and redistribution_ok: yes."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent / "datasets"
FIELDS = ["name:", "source_url:", "licence:", "redistribution_ok:", "attribution_text:", "personal_data:"]
errors = []
for d in sorted(p for p in ROOT.iterdir() if p.is_dir()):
    f = d / "DATA.md"
    if not f.exists():
        errors.append(f"{d.name}: missing DATA.md")
        continue
    text = f.read_text(encoding="utf-8")
    for field in FIELDS:
        if field not in text:
            errors.append(f"{d.name}: DATA.md lacks '{field}'")
    if "redistribution_ok: yes" not in text:
        errors.append(f"{d.name}: redistribution_ok must be 'yes'")
    if "personal_data: none" not in text:
        errors.append(f"{d.name}: personal_data must be 'none'")
for e in errors:
    print("ERROR:", e)
print(f"datasets checked, {len(errors)} error(s)")
sys.exit(1 if errors else 0)
