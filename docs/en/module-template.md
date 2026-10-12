# Module template

Every module lives in `docs/en/grade-NN/mNN-slug/` and has a `lesson.md` (front-matter below). Grade 8 also has a separate `teacher-guide.md`; Grades 9–12 keep their teacher notes at the end of the lesson.

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

## Sections of a lesson (v0.2 "book" structure)

| # | Section | Purpose | Typical time |
|---|---|---|---|
| — | **At a glance** box | time, materials, tiers, prerequisites, outcomes | — |
| 1 | **Hook** | a real problem from the students' own context | 5 min |
| 2 | **Understand it** | the full explanation a student can read alone: analogy → precise idea → text diagram → what Git really does | read 10–15 min (before or after class) |
| 3 | **See it** | a worked example: exact commands *and expected output*, annotated | 5–10 min demo |
| 4 | **Unplugged / concept activity** | paper or visual model first | 15 min |
| 5 | **PRIMM lab** | Predict, Run, Investigate, Modify, Make, with checkpoints | 30–40 min |
| 6 | **Parsons practice** | put jumbled steps in order | 10 min |
| 7 | **Common mistakes** | symptom → cause → fix table | — |
| 8 | **Practise more with free resources** | 3–6 exercises from the [resource library](book/resources.md), each with tier and what to hand in | homework / lab |
| 9 | **Exit ticket** | 3 questions, one checks a misconception | 5 min |
| 10 | **Key points** | 4–6 revision bullets | — |
| 11 | **New words** | terms used, all in the [glossary](glossary.md) | — |
| 12 | **Extension quest** | for fast finishers | — |
| 13 | **Teacher notes** (Grades 9–12) | timing, misconceptions, fallbacks, answer key | — |

## Teacher guide sections (Grade 8)
Timing · materials · common errors · fallback if no internet / no computer · differentiation · evidence to collect · answer key (including the free-resource exercises) · extension quest.

## Rules
- Concept before commands. Commands and code stay in English.
- Diagrams are plain text inside code blocks, so they print on any printer and work offline.
- Free resources are **linked, not copied**, unless their licence allows it (see the library).
- Every external link is opened and checked before it is added.
- Practice data is real-and-open or clearly synthetic; never student PII.
- Pair work (driver/navigator) is the default.
