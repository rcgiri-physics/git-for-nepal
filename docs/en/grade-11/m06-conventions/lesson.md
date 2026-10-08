---
id: g11-m06-conventions
grade: 11
hours: 1
prerequisites: [g11-m05-rebase-stash-revert]
outcomes:
  - "Write conventional commit messages"
  - "Name branches consistently"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 6. Commit-message and branching conventions

## Hook
Which message helps someone in two years: 'update' or 'Fix wrong date format in report header (#14)'?

## Concept (unplugged or visual first)
Convention: short imperative first line (≤ 72 chars), blank line, body explaining *why*; reference issue numbers. Branch names: `type/short-topic` (`feat/`, `fix/`, `docs/`).

## PRIMM lab
1. Rewrite 8 bad messages as good ones.
2. **Predict** which message style makes `git log --oneline` readable.
3. Add a `.gitmessage` template to your repo: `git config commit.template .gitmessage`.
4. **Make:** team agreement document `CONVENTIONS.md`.

## Parsons practice
Order the parts of a commit message: *summary · blank line · body (why) · issue reference*.

## Exit ticket
1. What is the ideal length of the first line?
2. What should the body explain?
3. *Misconception:* 'messages are only for me.'

## Teacher notes
Avoid over-formalising for a school: the aim is readability, not a rigid standard.
