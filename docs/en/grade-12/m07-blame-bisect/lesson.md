---
id: g12-m07-blame-bisect
grade: 12
hours: 2
prerequisites: [g12-m01-internals]
outcomes:
  - "Find who last changed a line and why"
  - "Locate the commit that introduced a bug using bisect"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 7. Debugging history: blame and bisect

## Hook
The page worked last month. Which of 40 commits broke it?

## Concept (unplugged or visual first)
**Binary search** on history: test the middle commit, discard half, repeat. 40 commits need about 6 tests (⌈log₂40⌉).

## PRIMM lab
Practice repo `g12-capstone-starter` has a planted bug.
1. `git blame check.sh` — read the author, date, message.
2. `git bisect start`, `git bisect bad`, `git bisect good <old-commit>`.
3. Run `bash check.sh` at each step, answering `git bisect good/bad`.
4. **Investigate:** which commit is guilty? `git bisect reset`.
5. **Make:** automate with `git bisect run bash check.sh`.

## Parsons practice
Order: *start · mark bad · mark good · test · answer · repeat · reset*.

## Exit ticket
1. How many tests for 64 commits?
2. What does blame show?
3. *Misconception:* 'blame is for punishing people.'

## Teacher notes
Frame `blame` as 'who can I ask?', not 'who is at fault'. Math link: logarithms.
