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

!!! abstract "At a glance"
    **Time:** 1 period · **Tiers:** 1–3 · **You need:** two PRs (planted by the teacher) that edit the same line of `index.html`

    **Before this:** Grade 9 Module 4 (conflicts), Modules 3–4.

    **By the end you can:** bring `main` into your branch, resolve the conflict locally, and make a blocked PR mergeable again.

## Hook (5 min)
Two PRs change the same menu line. The first is merged. The second now shows a grey box: **"This branch has conflicts that must be resolved."** The merge button is disabled. Whose job is it to fix this — and how?

## Understand it

### Why a PR becomes conflicted
Both PRs started from the same `main`. PR A changed line 12; PR B changed line 12 differently. When A is merged, `main` moves. B's branch is now based on an *old* `main`, and its change collides with A's:

```
            A1 ---- (PR A, merged)
           /      \
  main: m1 -------- m2  <- main now contains A's line 12
           \
            B1        <- PR B also changed line 12: conflict with m2
```

The server cannot ask a human in the middle of a button click, so it refuses. The fix happens on a computer.

### Who fixes it?
The **author of the later PR** (B). They know what their change is meant to do, and they can check that the result works.

### The fix: bring main into your branch
```bash
git switch feature/menu-gallery       # your PR's branch
git fetch origin                      # get the latest main from the server
git merge origin/main                 # bring main into your branch -> CONFLICT
#  ... edit the file, keep the right combination, delete the markers ...
git add index.html
git commit                            # finishes the merge (a merge commit)
git push                              # the PR updates and becomes mergeable
```

This is exactly the Grade 9 conflict, but **on your branch instead of on main**. `main` stays clean; you solve the problem where it belongs. Re-run the page and the checks after resolving — a resolution can be wrong even when the markers are gone!

Many hosts also offer a web conflict editor ("Resolve conflicts" button). It works for small text conflicts, but resolving locally lets you **test** the result.

### Preventing conflicts
Conflicts are a sign of **long-lived branches** and **work that overlaps**. Habits that make them rare:

- **Small PRs, merged quickly** (hours or days, not weeks).
- **Bring `main` into your branch often** (`git fetch && git merge origin/main`), not only at the end.
- **Talk** — "I'm editing the menu today" in the team chat or the issue.
- **Split files** sensibly — a `menu.html` included everywhere instead of the menu copied into every page.

### Rebase? Not yet
You may read online that people use `git rebase` instead of `merge` here. Rebase rewrites your branch's history; it is powerful and easy to misuse. We learn it in Grade 11. In Grade 10 we always **merge** `main` into the branch.

## See it
```console
$ git switch feature/menu-gallery
$ git fetch origin
$ git merge origin/main
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
$ grep -n -A4 "<<<<<<<" index.html
12:<<<<<<< HEAD
13-    <a href="gallery.html">Gallery</a>
14-=======
15-    <a href="about.html">About</a>
16->>>>>>> origin/main
```

Both links are wanted, so the right resolution keeps **both**:

```html
    <a href="about.html">About</a>
    <a href="gallery.html">Gallery</a>
```

```console
$ git add index.html
$ git commit --no-edit
$ bash check.sh            # still passes?
$ git push
```

## Unplugged warm-up (5 min)
Recall the Grade 9 paper game in one minute: two people change line 3 → markers → a human decides. Then ask: *"If one change is already in the class's main folder, who should redo the merge?"*

## PRIMM lab (30 min)
1. Teacher plants two PRs that edit `index.html` line 12 (or each pair creates both: partner A adds an About link, partner B a Gallery link, on separate branches from the same `main`).
2. **Predict:** after PR A is merged, what will PR B's page say? Merge A and look.
3. Author of B: `git switch feature/x`, `git fetch origin`, `git merge origin/main`.
4. Open the file, resolve (here: keep both links in a sensible order), `git add`, `git commit`, run `bash check.sh`, `git push`.
5. **Investigate:** why did the PR become mergeable? Look at the PR's commit list — what new commit appeared?
6. **Modify:** repeat with a *real* disagreement (both change the page title differently). Discuss with your partner before resolving; record the decision in a PR comment.
7. **Make:** write a rule that makes this conflict less likely (e.g. one person per file per day; pull often) and add it to the team's agreement.

## Parsons practice (5 min)
Order: *fetch · merge origin/main into your branch · resolve · add · commit · push*.

## Common mistakes
| Symptom | Cause | Fix |
|---|---|---|
| Resolved by keeping only your line, deleting a teammate's work | rushed | keep both where both are wanted; ask if unsure |
| Merged `main` locally but forgot to push | — | `git push`; the PR updates only after a push |
| Markers left in the file | — | `git grep "<<<<<<<"` before committing; checks may catch it |
| Merged your branch into `main` locally instead | wrong direction | `git merge --abort` (if unfinished); switch to your branch first |
| Used `git push --force` to "make it work" | — | never on shared branches; ask the teacher |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | GitHub Skills [**Resolve merge conflicts**](https://github.com/skills/resolve-merge-conflicts) (13+, account) — it uses the web editor; compare with our local method. | 3 | 45 min | one pro and one con of each method |
| 2 | Software Carpentry [**Conflicts**](https://swcarpentry.github.io/git-novice/09-conflict.html) — exercise "Conflicts on Non-textual Files": what happens with an image? | 1 / 3 | 15 min | answer |
| 3 | *Pro Git* [§3.2 **Basic Merge Conflicts**](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) — try `git mergetool` (or VS Code's merge editor) on your next conflict. | 1 | 20 min | which tool you prefer |
| 4 | Learn Git Branching [`remote7` "Diverged History"](https://learngitbranching.js.org/?locale=en_US&level=remote7) — solve it with merge. | 1 / 3 | 15 min | level done |

## Exit ticket (5 min)
1. Who fixes the conflict — the first or the second PR's author?
2. Name one habit that prevents conflicts.
3. *Misconception:* "Conflicts mean someone did something wrong." True or false?

## Key points
- A PR conflicts when `main` moved and changed the same lines.
- The later PR's author fixes it: fetch, **merge `origin/main` into the branch**, resolve, test, push.
- Test after resolving — no markers ≠ correct.
- Small PRs, frequent merges and talking prevent most conflicts.

## New words
**conflicted PR**, **`origin/main`**, **merge editor / mergetool** — see the [glossary](../../glossary.md).

## Extension quest
Try `git merge --no-commit origin/main` to see the merge result *before* committing it. When could that help?

## Teacher notes
- **Timing:** hook 5 · understand 10 · lab 25 · Parsons + exit 5. Plant the two PRs before class (or have each pair create both in the first 5 minutes of the lab).
- **Rebase is NOT taught here; it comes in Grade 11.** Use merge to bring `main` into the branch.
- VS Code's built-in merge editor shows *Incoming*, *Current* and *Result* panes — fine for students who struggle with raw markers.
- **Fallback Tier 1:** two local branches plus a shared bundle on USB; the "server" is the teacher's laptop.
- **Answer key:** Exit 1: the later (second) PR's author. 2: small PRs, merging main into your branch often, telling the team what you are editing, sensible file structure. 3: False — conflicts are normal when people work in parallel.
