---
id: g9-m04-merge
grade: 9
hours: 2
prerequisites: [g9-m03-branches]
outcomes:
  - "Merge a branch into main"
  - "Recognise and resolve a simple merge conflict"
tier_support: [0, 1, 2, 3]
license: CC-BY-4.0
---

# 4. Merge and the merge-conflict game

## Hook
Two edits to the same line of the poem. Who wins?

## Concept (unplugged or visual first)
**Paper merge-conflict game.** Pairs share a printed 5-line poem. Each edits line 3 differently on their own copy. Then they must combine. Write the rule: *Git can combine changes to different lines, but when both change the same line, a human decides.*
Show conflict markers on paper: `<<<<<<<`, `=======`, `>>>>>>>`.

## PRIMM lab
1. **Predict:** you merge `add-verse` (new lines) into `main`. Will there be a conflict? Run `git switch main`, `git merge add-verse`.
2. **Investigate:** `git log --graph --oneline --all`. Was it a fast-forward or a merge commit?
3. Create a conflict: on `main` and on `fix-spelling` change line 2 of `poem.txt` differently. Merge.
4. Open the file, find the markers, decide the final line, delete the markers, `git add poem.txt`, `git commit`.
5. **Modify:** repeat with a partner changing different lines — no conflict.
6. **Make:** write a team rule for your pair project: who edits which file.

## Parsons practice
Order for resolving a conflict: *merge · open the file · edit and remove markers · git add · git commit*.

## Exit ticket
1. When does a conflict happen?
2. What do the markers mean?
3. *Misconception:* 'after a conflict my work is lost.' True or false?

## Teacher notes
Students panic at conflicts. Normalise: conflicts are Git asking for a human decision. `git merge --abort` returns to before the merge.
