#!/usr/bin/env python3
"""Validate module front-matter and alignment ids.

Checks every docs/<lang>/grade-NN/*/lesson.md:
  - required keys: id, grade, hours, outcomes, tier_support, license
  - id matches folder prefix (e.g. g8-m01-... in folder m01-...)
  - grade matches the grade-NN folder
  - prerequisites refer to existing module ids
  - alignment/*.yml only references existing module ids
Exit code 1 on any error.
"""
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
REQUIRED = ["id", "grade", "hours", "outcomes", "tier_support", "license"]
FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def load_modules():
    mods, errors = {}, []
    for lesson in sorted((ROOT / "docs").glob("*/grade-*/*/lesson.md")):
        rel = lesson.relative_to(ROOT).as_posix()
        m = FM.match(lesson.read_text(encoding="utf-8"))
        if not m:
            errors.append(f"{rel}: missing front-matter")
            continue
        try:
            data = yaml.safe_load(m.group(1))
        except yaml.YAMLError as e:
            errors.append(f"{rel}: bad YAML ({e})")
            continue
        for key in REQUIRED:
            if key not in (data or {}):
                errors.append(f"{rel}: missing key '{key}'")
        if not data or any(k not in data for k in REQUIRED):
            continue
        grade_dir = int(lesson.parent.parent.name.split("-")[1])
        if data["grade"] != grade_dir:
            errors.append(f"{rel}: grade {data['grade']} != folder grade {grade_dir}")
        want = f"g{grade_dir}-{lesson.parent.name.split('-')[0]}-"
        if not str(data["id"]).startswith(want):
            errors.append(f"{rel}: id '{data['id']}' should start with '{want}'")
        if not data["outcomes"]:
            errors.append(f"{rel}: outcomes empty")
        if not set(data["tier_support"]) <= {0, 1, 2, 3} or not data["tier_support"]:
            errors.append(f"{rel}: tier_support must be a non-empty subset of 0-3")
        # same id in en and ne must be identical, so key by (lang, id)
        lang = lesson.relative_to(ROOT / "docs").parts[0]
        key = (lang, data["id"])
        if key in mods:
            errors.append(f"{rel}: duplicate id {data['id']}")
        mods[key] = (rel, data)
    return mods, errors


def main():
    mods, errors = load_modules()
    en_ids = {i for (lang, i) in mods if lang == "en"}
    for (lang, mid), (rel, data) in mods.items():
        for pre in data.get("prerequisites") or []:
            if pre not in {i for (l, i) in mods if l == lang}:
                errors.append(f"{rel}: unknown prerequisite '{pre}'")
    for yml in sorted((ROOT / "alignment").glob("*.yml")):
        data = yaml.safe_load(yml.read_text(encoding="utf-8"))
        refs = []
        for g in (data.get("grades") or {}).values():
            refs += g.get("modules", [])
        for s in data.get("standards") or []:
            refs += s.get("modules", [])
        for r in refs:
            if r not in en_ids:
                errors.append(f"{yml.name}: module '{r}' does not exist in docs/en")
    for e in errors:
        print("ERROR:", e)
    print(f"checked {len(mods)} lesson files, {len(errors)} error(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
