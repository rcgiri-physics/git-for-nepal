---
id: g10-m05-conflicts
grade: 10
hours: 1
prerequisites: [g10-m04-code-review]
outcomes:
  - "Resolve a conflict between two pull requests"
  - "Prevent conflicts with small, frequent integration"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 5. Real merge conflicts, resolved in pairs

## Hook
Two PRs change the same menu line. The second one cannot be merged.

## Concept (unplugged or visual first)
Remember the Grade 9 conflict game. Now the conflict appears on a *PR*: the platform says 'this branch has conflicts'. The author of the later PR fixes it.

## PRIMM lab
1. Teacher plants two PRs that edit `index.html` line 12.
2. Merge the first. For the second: `git switch feature/x`, `git fetch origin`, `git merge origin/main`.
3. Open the file, resolve, `git add`, `git commit`, `git push`.
4. **Investigate:** why did the PR become mergeable?
5. **Make:** write a rule that makes this conflict less likely (e.g. one person per file per day; pull often).

## Parsons practice
Order: *fetch · merge origin/main into your branch · resolve · add · commit · push*.

## Exit ticket
1. Who fixes the conflict — the first or the second PR's author?
2. Name one habit that prevents conflicts.
3. *Misconception:* 'conflicts mean someone did something wrong.' True or false?

## Teacher notes
Rebase is NOT taught here; it comes in Grade 11. Use merge to bring `main` into the branch.
