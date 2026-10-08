---
id: g9-m03-branches
grade: 9
hours: 2
prerequisites: [g9-m02-cli-basics]
outcomes:
  - "Explain a branch as a movable label on a commit"
  - "Create, switch and list branches"
tier_support: [0, 1, 2, 3]
license: CC-BY-4.0
---

# 3. Branches

## Hook
Two students want to improve the same poem differently: one adds a verse, one fixes spelling. Do they have to take turns?

## Concept (unplugged or visual first)
**Sticky-note model.** The history is a row of cards. A branch is a sticky note stuck on one card. `main` is one note. Creating a branch = a new note on the same card. Committing = adding a new card and moving *your* note to it. Do it with real sticky notes on Module 2 cards.
Visual tool: the self-hosted learnGitBranching levels 'Introduction Sequence' (tier 1+).

## PRIMM lab
1. In `ward-facts`: **predict** then run `git branch`.
2. `git switch -c add-verse` (older Git: `git checkout -b add-verse`). Predict what `git log --oneline --graph --all` shows.
3. Make a commit on `add-verse`. Switch back: `git switch main`. **Investigate:** where did your new file go? (It is not in the working folder — it is on the other branch.)
4. **Modify:** create a second branch `fix-spelling` from `main` and commit there.
5. **Make:** draw the three labels and the commits with sticky notes; compare with `git log --graph --all`.

## Parsons practice
Order to make a branch with one commit and return: *switch -c · edit · add · commit · switch main*.

## Exit ticket
1. What is a branch?
2. Why did the new file disappear when you switched back to main?
3. *Misconception:* 'a branch is a full copy of the folder.' True or false?

## Teacher notes
The key idea is the pointer. If students ask 'is it a copy?' — no, it is a label, which is why branches are cheap. Always commit or stash before switching; if Git refuses to switch, that protects uncommitted work.
