---
id: g11-m08-data-project
grade: 11
hours: 3
prerequisites: [g11-m04-first-pr]
outcomes:
  - "Keep a dataset in Git with a changelog"
  - "Document source and licence in DATA.md"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 8. Data project: version, clean and document open data

## Hook
A table of ward boundaries changed in 2017. If your analysis uses an old copy, your answers are wrong. Version the data like code.

## Concept (unplugged or visual first)
Data rules: keep **raw** (never edited) and **clean** (derived) files separately; record the source, licence and date retrieved in `DATA.md`; explain each cleaning step in a commit message and `CHANGELOG`.

## PRIMM lab
Practice repo: `practice-repos/g11-data-thread` (synthetic starter). **Real data:** choose a dataset from Open Knowledge Nepal `localboundaries` (stated CC BY 4.0) or Open Data Nepal — **verify each licence yourself and record it**; do not copy data whose licence is unclear or missing (e.g. a repo with no stated licence).
1. Fetch the data (tier 3) or use the teacher's USB copy (tier 1).
2. `raw/` untouched; make `clean/` with a script `clean.py`.
3. **Predict** how many rows change; check with `git diff --stat`.
4. Fill `DATA.md` (see `datasets/README.md` template). Add a `CHANGELOG.md` entry per cleaning step.
5. **Make:** open a PR proposing the dataset for the shared `datasets/` folder only if its licence allows redistribution.

## Parsons practice
Order: *download raw · commit raw · write cleaning script · commit clean · document in DATA.md*.

## Exit ticket
1. Why keep raw and clean data apart?
2. What goes in DATA.md?
3. *Misconception:* 'if I can download it, I can redistribute it.'

## Teacher notes
Teacher checks every licence before class. No personal data. Link-only is always a safe fallback.
