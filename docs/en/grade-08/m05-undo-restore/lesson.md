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

!!! abstract "At a glance"
    **Time:** 2 periods · **Tiers:** 0–3 · **You need:** the practice repo (or your own repo from Module 3); Module 2 cards for Tier 0

    **Before this:** Module 4 (reading history and diffs).

    **By the end you can:** throw away a messy uncommitted change; bring back a file from any older commit; undo a bad commit with a new "revert" commit; choose the right undo for a situation.

## Hook (5 min)
Your teacher shows a "disaster": a student deleted three paragraphs of the article and pressed Save. *"In your old way, it is gone. Today it comes back in 10 seconds."* Then the teacher brings it back — in front of you.

## Understand it
Git is a **time machine**, but a careful one. There are three different kinds of "undo", for three different situations. Choosing the right one is the skill.

### Situation 1 — "I made a mess since my last commit"
You edited a file, it went wrong, you have **not committed**. You want the file exactly as it was in the last commit.

→ **Restore** the file: `git restore article.md` (VS Code: right-click the file in Source Control → *Discard Changes*; GitHub Desktop: right-click → *Discard changes*).

```
 history:  c1 - c2 - c3          working copy: c3 + mess
                      \___ restore copies c3's version back ___/
```

!!! danger "The one dangerous undo"
    Restore throws away the uncommitted changes, and **Git cannot bring them back** — they were never in a commit. Always look at the diff first: *am I sure I want to lose all of this?*

### Situation 2 — "I need an old version of one file"
Last Tuesday's version was better. You want *that* version back, but keep the history that came after.

→ **Restore from an older commit**: `git restore --source=<id> article.md`. The old version appears in your working copy as a normal change. Look at it, then **commit** it with a message such as `Bring back Tuesday's opening paragraph`.

### Situation 3 — "My last commit was a mistake"
You committed something wrong. You do *not* rub out the bad commit — remember the khata: you never tear out a page. Instead you add a **new commit that does the opposite**.

→ **Revert**: `git revert <id>` (VS Code / GitHub Desktop: right-click the commit in the history → *Revert*).

```
 before:  c1 - c2 - c3 - BAD
 after:   c1 - c2 - c3 - BAD - "Revert BAD"     <- the article is like c3 again,
                                                   and the record shows what happened
```

Why keep the bad commit? Because history is a **true record**. A teacher or teammate can see the mistake *and* the fix. And if the "bad" commit turns out to be good after all, you can even revert the revert.

### Which undo do I need?
| Situation | Committed yet? | Use | History after |
|---|---|---|---|
| Messy edits I don't want | no | `git restore <file>` / *Discard* | unchanged (edits lost!) |
| Unstage something I added to the box by mistake | staged, not committed | `git restore --staged <file>` | unchanged (edit kept in working copy) |
| Bring back an old version of one file | — | `git restore --source=<id> <file>` then commit | one new commit |
| Undo a whole commit | yes | `git revert <id>` | one new "Revert …" commit |

In Grade 11 you will meet more powerful (and more dangerous) tools such as `git reset`, which *can* rewrite history. In Grade 8 we use only the safe ones above.

### The safety rule
- **Committed work is safe.** You can always get it back.
- **Uncommitted work is fragile.** Commit often — then nothing is ever really lost.

## See it
A bad commit and its revert, with real output:

```console
$ git commit -am "Change title to ???"
[main 28ed605] Change title to ???
 1 file changed, 1 insertion(+), 1 deletion(-)

$ git revert --no-edit HEAD                 <- HEAD = the latest commit
[main 578a17e] Revert "Change title to ???"
 1 file changed, 1 insertion(+), 1 deletion(-)

$ git log --oneline -3
578a17e Revert "Change title to ???"         <- new commit: title is back
28ed605 Change title to ???                  <- the mistake stays in the record
366579e Change title to Dashain Festival at Our School
```

And throwing away a mess (situation 1):

```console
$ git status --short
 M article.md                                <- M = modified, not committed
$ git restore article.md
$ git status
On branch main
nothing to commit, working tree clean        <- back to the last commit
```

## Unplugged (15 min)
With the Module 2 cards, three situations. For each, pick the right card action and say which Git command it matches:

1. "I made a mess on my sheet since my last card." → throw the messy sheet away and re-copy the last card (**restore**).
2. "Card c4 was wrong." → make a **new** card c5 that undoes c4 (**revert**). Don't rub out c4!
3. "I need last Tuesday's paragraph." → look at card c2 and copy that paragraph back onto the sheet, then make a new card (**restore from an old commit**).

Then the teacher reads out 6 quick situations (see the teacher guide); pairs hold up a card saying **RESTORE**, **REVERT** or **OLD VERSION**.

## PRIMM lab (40 min)
1. **Predict & run:** delete the middle paragraph of `article.md` and save (do not commit). Predict what Source Control shows. Look at the diff — it should be all red. Then **discard changes** for that file (in the tool) or `git restore article.md`.
   *Checkpoint:* the paragraph is back; `git status` says clean.
2. **Predict:** make and commit a bad edit (`Change title to ???`). Predict what `git log` shows if we **revert** it: one commit fewer, the same, or one more?
3. **Run:** revert the commit (right-click → *Revert*, or `git revert HEAD`). If an editor opens asking for a message, save and close it. Look at the log: one *new* commit, and the bad commit is still there.
4. **Investigate:** why does Git keep the bad commit? Discuss with your partner, then write one sentence. *(Because history is a record of what really happened.)*
5. **Modify:** restore only `article.md` from an older commit — for example the very first one:
   `git restore --source=d38a483 article.md` (use the id from your own log). Open the file: it is the first version! Run `git status` — it is a *change*, not yet committed. Decide: commit it, or restore again to go back to the latest version (`git restore article.md`).
6. **Make:** break and repair something on purpose (for example add a silly sentence and commit, then revert it). Write a revert message that explains *why* — `git revert` lets you edit the message.

## Parsons practice (10 min)
Order: *notice the mistake · look at git log · choose revert · check the log again · write why*.

## Common mistakes
| Symptom | Cause | Fix |
|---|---|---|
| "I discarded changes and lost an hour's work" | restore on uncommitted work cannot be undone | always check the diff first; commit more often |
| A strange editor (Vim) opens during revert and you can't leave | Git asks for a revert message | type `:wq` and press Enter; or use `git revert --no-edit HEAD`; or set VS Code as the editor (teacher) |
| "Revert deleted my commit" | it did not — look at the log | the bad commit is still there, followed by its opposite |
| `restore --source` "did nothing" | the old version is in the working copy, not committed | look at the file / `git status`; commit if you want to keep it |
| Typed `git reset --hard` from a website | it can destroy work | stop and ask the teacher; we learn reset in Grade 11 |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Software Carpentry [**Exploring History**](https://swcarpentry.github.io/git-novice/05-history.html), second half (restoring old versions with `git restore`/`git checkout`). Do its "Recovering Older Versions of a File" exercise on our article. | 1 / 3 | 20 min | answer to the exercise |
| 2 | [Learn Git Branching, level `rampup4` "Reversing Changes in Git"](https://learngitbranching.js.org/?locale=en_US&level=rampup4) — **only the `git revert` part.** Watch how revert adds a new commit. (Skip `git reset` for now.) | 1 / 3 | 10 min | drawing of the graph after revert |
| 3 | *Pro Git* [§2.4 **Undoing Things**](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things): find the warning box. What does it say about discarded changes? | 3 | 10 min | the warning in your own words |
| 4 | **Undo decision cards (paper):** make 4 cards — one per row of the "Which undo do I need?" table — with a drawing for each. Use them to test a partner. | 0 | 15 min | the 4 cards |
| 5 | **Time-machine challenge:** in your own Module 3 `poem` repo, bring back the 2-line version of the poem, commit it, then revert that commit. Draw the history. | 1 | 15 min | drawing + `git log --oneline` |

## Exit ticket (5 min)
1. Which command/tool throws away an uncommitted edit?
2. Does `revert` delete the bad commit? What does it do?
3. *Misconception check:* "Once I commit, I can never fix a mistake." (False.)

## Key points
- Three undos: **restore** (throw away uncommitted mess), **restore from an old commit** (bring back an old version of a file), **revert** (undo a commit with a new commit).
- `git restore` on uncommitted work **cannot be undone** — check the diff first.
- Revert keeps the bad commit in history; history is a true record.
- Committed work is safe. Commit often.

## New words
**restore**, **discard**, **revert**, **HEAD**, **unstage** — see the [glossary](../../glossary.md).

## Extension quest
After a revert, can you "revert the revert"? What happens to the article? Try it and draw the history.
