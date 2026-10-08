# Module template

Every module lives in `docs/en/grade-NN/mNN-slug/` and has `lesson.md` (front-matter below) and `teacher-guide.md`.

```yaml
---
id: g9-m03-branches        # gN-mNN-slug, must match the folder
grade: 9
hours: 2
prerequisites: [ g9-m02-cli-basics ]
outcomes: [ "Create and switch branches", "Explain a branch as a movable label" ]
tier_support: [0, 1, 2, 3]  # which delivery tiers the module works in
license: CC-BY-4.0
---
```

## Sections of a lesson
1. **Hook (5 min)** — a real problem in a Nepali context.
2. **Unplugged / concept (15 min)** — paper or visual model first.
3. **PRIMM lab (40 min)** — Predict, Run, Investigate, Modify, Make.
4. **Parsons practice (10 min)** — put jumbled steps in order.
5. **Exit ticket (5 min)** — 3 questions, one checks a misconception.

## Teacher guide sections
Timing · common errors · fallback if no internet / no computer · answer key · extension quest.

## Rules
- Concept before commands. Commands and code stay in English.
- Practice data is real-and-open or clearly synthetic; never student PII.
- Pair work (driver/navigator) is the default.
