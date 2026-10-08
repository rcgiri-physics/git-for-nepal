---
id: g11-m05-rebase-stash-revert
grade: 11
hours: 2
prerequisites: [g11-m04-first-pr]
outcomes:
  - "Use stash to park work"
  - "Rebase a feature branch on main"
  - "Choose between revert and reset"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 5. rebase, stash, revert, reset — when to use each

## Hook
Your PR is behind main and you have half-done work. What are the safe tools?

## Concept (unplugged or visual first)
Cards on the history line again. **revert** adds a new undoing card (safe for shared history). **reset** moves the sticky note (rewrites; only for commits not yet pushed). **rebase** replays your cards on top of a newer main (rewrites your branch). **stash** puts unfinished work in a drawer.

**Golden rule:** never rewrite history that others already have.

## PRIMM lab
1. Create a messy local history of 3 commits. **Predict** what each of these does: `git stash`, `git rebase main`, `git reset --soft HEAD~1`, `git revert HEAD`.
2. Run each in a practice repo (`git reflog` shows how to find lost commits!).
3. **Investigate:** compare `git log --graph` before and after rebase.
4. **Modify:** squash your last 3 commits into one with a clean message (`git reset --soft HEAD~3 && git commit`).
5. **Make:** write your own 'which tool when' cheat sheet.

## Parsons practice
Match situation → tool: pushed bad commit → revert; unpushed typo commit → reset/amend; branch behind main → rebase or merge; interrupted → stash.

## Exit ticket
1. Why is `reset` risky on a pushed branch?
2. What does `git reflog` do?
3. *Misconception:* 'rebase and merge produce identical history.'

## Teacher notes
Run this lesson on throwaway repos only. Do not allow `push --force` on shared branches; protect `main`.
