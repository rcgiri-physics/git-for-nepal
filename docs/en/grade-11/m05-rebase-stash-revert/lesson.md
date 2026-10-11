---
id: g11-m05-rebase-stash-revert
grade: 11
hours: 2
prerequisites: [g11-m04-first-pr]
outcomes:
  - "Use stash to park work"
  - "Rebase a feature branch on main"
  - "Choose between revert and reset"
  - "Recover 'lost' commits with reflog"
tier_support: [0, 1, 2, 3]
license: CC-BY-4.0
---

# 5. rebase, stash, revert, reset — when to use each

!!! abstract "At a glance"
    **Time:** 2 periods · **Tiers:** 0 (cards), 1–3 · **You need:** a **throwaway** practice repo (never your real project), commit cards and sticky notes

    **Before this:** Grade 8 Module 5 (restore, revert), Grade 9 Modules 3–4, Module 4.

    **By the end you can:** park unfinished work, replay a branch on a newer `main`, tidy unpushed commits, choose the safe undo for shared history, and rescue commits you thought were lost.

## Hook (5 min)
Your PR is behind `main`, a reviewer asked for a change, you have half-done work in the folder, and your last commit message says `typo fxi`. Which tools fix this safely — and which could destroy a teammate's work?

## Understand it

### The golden rule
> **Never rewrite history that other people already have.**

Some tools **add** to history (safe anywhere). Others **rewrite** it — they replace commits with new ones. Rewriting is fine on commits that exist only on your computer; on shared, pushed branches it causes confusion and lost work.

| Tool | Adds or rewrites? | Use on pushed/shared commits? |
|---|---|---|
| `git revert` | adds a new commit | ✓ yes — the safe undo |
| `git stash` | doesn't touch history | ✓ |
| `git commit --amend` | rewrites the last commit | only if not pushed |
| `git reset` | moves the branch label | only if not pushed |
| `git rebase` | replays commits as new ones | only on your own branch (see below) |

### `stash` — a drawer for unfinished work
You are halfway through a change and must switch branches (a reviewer needs a quick fix). Commit half-done work? No — **stash** it:

```bash
git stash            # put uncommitted changes in a drawer; folder is clean again
git switch other-branch ... (do the urgent thing) ... git switch back
git stash pop        # take the changes out of the drawer
git stash list       # see what is in the drawer
```

Use the drawer for minutes or hours, not weeks — stashes are easy to forget.

### `revert` — undo by adding (Grade 8 revisited)
Creates a new commit that does the opposite of an old one. History stays true and nobody's copy breaks. **The right undo for anything already pushed.**

### `reset` — move the label
`git reset` moves the current branch label to another commit. Three strengths:

| Command | Branch label | Staging area | Working files | Use |
|---|---|---|---|---|
| `git reset --soft HEAD~1` | moves back 1 | keeps the changes **staged** | unchanged | redo the last commit (e.g. combine commits) |
| `git reset HEAD~1` (mixed) | moves back 1 | unstages | unchanged | un-commit, keep edits |
| `git reset --hard HEAD~1` | moves back 1 | reset | **reset — edits lost!** | throw away commits and edits |

```
 before:              c1 -- c2 -- c3 -- c4  [main]
 after reset HEAD~2:  c1 -- c2  [main]
                      (c3, c4 still exist, unlabelled; reflog remembers them)
```

`--hard` is the most dangerous everyday command in Git. Check `git status` and `git diff` first.

Small sibling: **`git commit --amend`** replaces the last commit (fix its message or add a forgotten file). Only before pushing.

### `rebase` — replay your work on a new base
Your branch started from an old `main`; `main` has moved. In Grade 10 you **merged** `main` into your branch. **Rebase** is the other option: it takes your branch's commits and **replays them one by one on top of the new `main`**, as if you had started today:

```
 before:     m1 -- m2 [main]
               \
                B1 -- B2 [feature]

 after git rebase main:
              m1 -- m2 [main] -- B1' -- B2' [feature]
```

`B1'` and `B2'` are **new commits** (new ids) with the same changes. Result: a straight, easy-to-read history and no merge commit. Price: history was rewritten. So:

- ✓ rebase **your own** feature branch that nobody else has built on — even if you pushed it for a PR (then push with `git push --force-with-lease`, which refuses if someone else pushed in the meantime);
- ✗ never rebase `main` or any branch others work on.

If a replayed commit conflicts, Git stops: resolve like a merge, `git add`, then `git rebase --continue` (or `git rebase --abort` to give up).

**Merge or rebase?** Both are fine; teams choose. Merge keeps history exactly as it happened; rebase makes it tidier. Follow the project's CONTRIBUTING rules.

### `reflog` — Git's safety net
Commits "lost" by reset or rebase are not deleted at once. **`git reflog`** lists every place `HEAD` has been recently (usually kept 90 days). Find the id and bring it back:

```bash
git reflog                     # find the commit before the accident
git reset --hard <that-id>     # or: git branch rescue <that-id>
```

Reflog is local — it is your computer's diary, not shared.

### Which tool when?
| Situation | Tool |
|---|---|
| Interrupted with half-done work | `stash` |
| Bad commit already pushed / shared | `revert` |
| Typo in the last commit message, not pushed | `commit --amend` |
| Several messy local commits → one clean commit | `reset --soft HEAD~N` then `commit` (or interactive rebase) |
| My feature branch is behind `main` | `merge main` or `rebase main` (own branch only) |
| "I reset and lost my commits!" | `reflog` |

## See it
Real output from a practice repo:

```console
$ git status --short
 M b.txt                                        <- half-done work
$ git stash
Saved working directory and index state WIP on feature: 4992393 Extend b
$ git log --oneline --graph main feature
* 4992393 (feature) Extend b
* 24ff680 Add b
| * 547b291 (main) Add m on main
|/
* 5ab9aa8 Add a
$ git rebase main
Successfully rebased and updated refs/heads/feature.
$ git log --oneline --graph main feature
* 3ca532b (HEAD -> feature) Extend b             <- new ids: these are new commits
* 181e7ad Add b
* 547b291 (main) Add m on main
* 5ab9aa8 Add a
$ git stash pop                                 <- half-done work is back
$ git reset --hard HEAD~1                       <- oops
HEAD is now at 181e7ad Add b
$ git reflog -3
181e7ad HEAD@{0}: reset: moving to HEAD~1
157ac83 HEAD@{1}: commit: Add b.txt with three lines
181e7ad HEAD@{2}: reset: moving to HEAD~3
$ git reset --hard 157ac83                      <- rescued
```

## Unplugged: the card table (20 min)
Lay the commit cards on the table with a `main` sticky note and a `feature` sticky note.

- **revert:** add a new card that undoes an old one. (Nothing moves.)
- **reset:** move the sticky note back two cards. Where do the skipped cards go? (They lie unlabelled — the reflog remembers them.)
- **rebase:** pick up the `feature` cards, *copy* them onto new cards placed after `main`'s newest card, move the `feature` note; the old cards lie unlabelled.
- **stash:** put the working sheet in a drawer.

Now give a second group a copy of the old `feature` cards *before* the rebase, and ask: what happens when they try to add their next card? (Their history no longer matches — that is why we never rebase shared branches.)

## PRIMM lab (50 min)
Throwaway repo only: `git init practice-undo`, make 3 commits on `main`, branch `feature` with 2 commits, then 1 more commit on `main`.

1. **Predict** what each command does, and write it down: `git stash`, `git rebase main`, `git reset --soft HEAD~1`, `git revert HEAD`.
2. Run each in turn (stash with some uncommitted edits; then rebase `feature` on `main`; then reset; then revert). After each, run `git log --oneline --graph --all` and compare with your prediction.
3. **Investigate:** compare commit ids before and after the rebase. Why are they different?
4. **Investigate:** `git reset --hard HEAD~2`, then use `git reflog` to find and restore the lost commits.
5. **Modify:** squash your last 3 commits into one with a clean message (`git reset --soft HEAD~3 && git commit -m "…"`). Then try the same with `git rebase -i HEAD~3` (change `pick` to `squash` for the last two lines).
6. **Make:** write your own "which tool when" cheat sheet and keep it in your portfolio.

## Parsons practice (5 min)
Match situation → tool: pushed bad commit → revert; unpushed typo commit → reset/amend; branch behind main → rebase or merge; interrupted → stash.

## Common mistakes
| Symptom | Cause | Fix |
|---|---|---|
| `git push` rejected after a rebase | the remote has the old commits | on **your own** PR branch: `git push --force-with-lease`; on shared branches: don't rebase |
| Teammate's history "goes crazy" | someone rewrote a shared branch | agree a recovery with the teacher; protect `main` |
| Edits gone after `reset --hard` | `--hard` resets the working files | committed work → `reflog`; uncommitted edits are truly lost |
| Forgot a stash for weeks | — | `git stash list`; `git stash show -p stash@{0}` |
| Stuck in the middle of a rebase | conflict | resolve, `git add`, `git rebase --continue`, or `git rebase --abort` |
| Interactive rebase opened Vim | — | edit, then `:wq`; or set VS Code as editor |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Learn Git Branching: [`intro4` Rebase Introduction](https://learngitbranching.js.org/?locale=en_US&level=intro4), [`rampup4` Reversing Changes](https://learngitbranching.js.org/?locale=en_US&level=rampup4), `move1` Cherry-pick Intro, `move2` Interactive Rebase Intro. | 1 / 3 | 40 min | levels done |
| 2 | *Pro Git* [§7.7 **Reset Demystified**](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified) — the "three trees" explanation. Redraw its main figure with our three places from Grade 8. | 3 | 30 min | drawing |
| 3 | *Pro Git* [§3.6 **Rebasing**](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) — read "The Perils of Rebasing". Explain the golden rule in your own words. | 3 | 20 min | explanation |
| 4 | *Pro Git* [§7.3 **Stashing and Cleaning**](https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning): try `git stash -u` with an untracked file. | 1 / 3 | 15 min | what `-u` does |
| 5 | [Dangit, Git!?](https://dangitgit.com/) — read three rescues; which ones use reflog, reset or amend? | 3 | 15 min | table |

## Exit ticket (5 min)
1. Why is `reset` risky on a pushed branch?
2. What does `git reflog` do?
3. *Misconception:* "Rebase and merge produce identical history."

## Key points
- **Golden rule:** never rewrite history others already have.
- `stash` parks work · `revert` undoes by adding · `reset` moves the label · `rebase` replays commits on a new base · `amend` fixes the last commit.
- `--hard` throws away working edits — check first.
- `reflog` recovers commits lost by reset or rebase.
- Merge vs rebase: both valid; follow the project's rules.

## New words
**stash**, **reset (soft/mixed/hard)**, **amend**, **rebase**, **interactive rebase**, **squash**, **reflog**, **force-with-lease**, **rewrite history** — see the [glossary](../../glossary.md).

## Extension quest
Use `git cherry-pick <id>` to copy one commit from another branch onto yours. When would that be better than merging the whole branch?

## Teacher notes
- **Timing:** P1: hook 5, understand 20, card table 15. P2: see it 5, lab 30, Parsons + exit 5.
- **Run this lesson on throwaway repos only.** Do not allow `push --force` on shared branches; protect `main` on the class server (Forgejo/GitHub branch protection: block force pushes).
- **Key misconception:** "reset deletes commits." It moves a label; commits remain reachable via reflog until garbage-collected.
- **Fallback Tier 0:** the card table plus the second-group experiment is the whole lesson.
- **Answer key:** Exit 1: others already have those commits; moving the label (and force-pushing) breaks their history and can lose their work. 2: lists where HEAD has been, so you can find and restore "lost" commits. 3: False — rebase creates new commits in a straight line; merge keeps both lines and adds a merge commit. Lab 3: rebased commits are new objects with new parents, so new ids.
