---
id: g8-m05-undo-restore
grade: 8
hours: 2
prerequisites: [g8-m04-history-diff]
outcomes:
  - "Throw away an uncommitted change"
  - "Restore an earlier version of a file"
  - "Undo a bad commit without erasing history"
tier_support: [0, 1, 2, 3]
license: CC-BY-4.0
---

# 5. Undo and restore

## Hook (5 min)
Show a "disaster": a student deleted three paragraphs and saved. *"In your old way, it is gone. Today it comes back in 10 seconds."*

## Unplugged (15 min)
With the Module 2 cards: three situations. For each, pick the right card action:
1. "I made a mess since my last card." → throw the messy sheet away and re-copy the last card (**restore**).
2. "Card c4 was wrong." → make a **new** card c5 that undoes c4 (**revert**). Don't rub out c4!
3. "I need last Tuesday's paragraph." → look at the card c2 and copy that paragraph back.

## PRIMM lab (40 min)
1. **Predict & run:** delete the middle paragraph of `article.md` (do not commit). Predict what Source Control shows. Then **discard changes** for that file (in the tool) or `git restore article.md`.
2. **Predict:** make and commit a bad edit ("Change title to ???"). Predict what `git log` shows if we **revert** it.
3. **Run:** revert the commit (right-click → *Revert*, or `git revert HEAD`). Look at the log: two new things, the bad commit is still there.
4. **Investigate:** why does Git keep the bad commit? (Because history is a record of what really happened.)
5. **Modify:** restore only `article.md` from an older commit: `git restore --source=<id> article.md`, then commit.
6. **Make:** break and repair something on purpose; write a message explaining the repair.

## Safety rule (important)
- `git restore` on **uncommitted** changes cannot be undone — those changes are gone. Check the diff first.
- Committed work is safe; you can always get it back.

## Parsons practice (10 min)
Order: *notice the mistake · look at git log · choose revert · check the log again · write why*.

## Exit ticket (5 min)
1. Which command/tool throws away an uncommitted edit?
2. Does `revert` delete the bad commit? What does it do?
3. *Misconception check:* "Once I commit, I can never fix a mistake." (False.)
