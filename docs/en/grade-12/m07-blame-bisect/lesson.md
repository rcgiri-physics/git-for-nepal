---
id: g12-m07-blame-bisect
grade: 12
hours: 2
prerequisites: [g12-m01-internals]
outcomes:
  - "Find who last changed a line and why"
  - "Locate the commit that introduced a bug using bisect"
  - "Automate bisect with a test script"
tier_support: [0, 1, 2, 3]
license: CC-BY-4.0
---

# 7. Debugging history: blame and bisect

!!! abstract "At a glance"
    **Time:** 2 periods · **Tiers:** 0 (numbered-card binary search), 1–3 · **You need:** `practice-repos/g12-capstone-starter/make-bisect-demo.sh`

    **Before this:** Module 1; Grade 9 Module 6 (`git log -p`).

    **By the end you can:** use `git blame` to find the commit and reason behind any line, and `git bisect` to find the commit that introduced a bug among hundreds — by hand or automatically.

## Hook (5 min)
The data check worked last month. Now it fails. There are 40 commits in between, by four people. Reading all 40 diffs takes an hour. Can Git find the guilty commit in six steps?

## Understand it

### `git blame`: who can I ask?
`git blame <file>` shows, for **every line**, the commit that last changed it, the author and the date:

```console
$ git blame data/sample.csv
^a346ca2 (Teacher 2026-10-11 01:09:37 +0545  1) id,name,value
^a346ca2 (Teacher 2026-10-11 01:09:37 +0545  2) 1,alpha,10
77330af1 (Teacher 2026-10-11 01:09:37 +0545  3) 2,row2,20
...
47496f8b (Teacher 2026-10-11 01:09:38 +0545  8) 7,bad row without a value
```

(`^` marks lines from the very first commit.) Then `git show 47496f8` gives the full commit: its message, its whole diff, and often an issue number — **the reason** for the line.

The name is unfortunate: blame is for finding **context and the person to ask**, not for finding fault. Good teams talk about "annotate" (VS Code and many hosts show the same information as *annotations* or "blame view").

Useful options: `git blame -L 10,20 file` (only some lines), `git blame -w` (ignore whitespace changes), and `git log -L 10,20:file` (the full history of those lines).

### `git bisect`: binary search through history
If you know one commit where things were **good** and one where they are **bad**, the first bad commit is somewhere between. **Bisect** tests the commit in the **middle**: if it is bad, the culprit is in the first half; if good, in the second half. Each test halves the remaining commits.

```
 good                                      bad
  c1  c2  c3  c4  c5  c6  c7  c8  c9  c10 c11 c12
                      ^ test c6: good  -> culprit in c7..c12
                                  ^ test c9: bad  -> culprit in c7..c9
                          ^ test c8: bad -> c7..c8
                      ^ test c7: bad -> first bad commit = c7
```

For *n* commits you need about **⌈log₂ n⌉** tests: 12 commits → 4, 40 → 6, 1,000 → 10, 1,000,000 → 20. That is the power of logarithms (Grade 11–12 mathematics) applied to debugging.

The commands:

```bash
git bisect start
git bisect bad                 # the current commit is bad
git bisect good <old-id>       # this old commit was good
#   Git checks out a middle commit. Test it, then say:
git bisect good                # or: git bisect bad
#   ... repeat until Git prints "<id> is the first bad commit"
git bisect reset               # return to where you started
```

### Automatic bisect
If a script can decide good/bad by its **exit code** (0 = good, 1–127 = bad, 125 = "can't test, skip"), Git can do the whole search alone:

```bash
git bisect run bash check.sh
```

This is why **small commits** and **automatic checks** (Module 3) matter: bisect points to one small commit you can understand at once. A giant commit "Update everything" is found just as fast, but tells you little.

## See it
Real output on the 12-commit demo repository (row 7 is the planted bug):

```console
$ git bisect start
$ git bisect bad
$ git bisect good a346ca2
Bisecting: 5 revisions left to test after this (roughly 3 steps)
[35e5fc0...] Add row 6
$ git bisect run bash check.sh
running 'bash' 'check.sh'
g12 ok
Bisecting: 2 revisions left to test after this (roughly 2 steps)
[7148b98...] Add row 9
running 'bash' 'check.sh'
bad row: 7,bad row without a value
Bisecting: 0 revisions left to test after this (roughly 1 step)
[a1c604e...] Add row 8
running 'bash' 'check.sh'
bad row: 7,bad row without a value
Bisecting: 0 revisions left to test after this (roughly 0 steps)
[47496f8...] Add row 7
running 'bash' 'check.sh'
bad row: 7,bad row without a value
47496f8b253518e56e84a38519fa910f3c90e509 is the first bad commit
commit 47496f8b253518e56e84a38519fa910f3c90e509
    Add row 7
 data/sample.csv | 1 +
$ git bisect reset
```

Four tests found the culprit among 11 candidates.

## Unplugged: guess the number (15 min)
One student thinks of a commit number from 1 to 64 (written secretly: "the first bad commit"). The class may only ask "is commit *k* good or bad?" (answer: good if *k* is before the secret number). Count questions. Compare a strategy that tests commits in order (1, 2, 3 …) with one that always tests the middle. Then: how many questions for 1,000 commits?

## PRIMM lab (50 min)
Build the practice repo: `bash practice-repos/g12-capstone-starter/make-bisect-demo.sh bisect-demo && cd bisect-demo`. It has 12 commits and a planted bug.

1. `bash check.sh` — it fails. `git blame data/sample.csv` — read the author, date and commit of the bad line. `git show` that commit.
2. **Predict:** how many tests will bisect need for 12 commits?
3. `git bisect start`, `git bisect bad`, `git bisect good <first-commit>` (find it with `git log --oneline | tail -1`).
4. Run `bash check.sh` at each step, answering `git bisect good` / `git bisect bad`. Count the steps.
5. **Investigate:** which commit is guilty? Does it match blame? Why might blame and bisect give *different* answers in a real project? (Blame shows the last change to a line; a bug can come from a change to *another* line or file.) `git bisect reset`.
6. **Make:** automate with `git bisect run bash check.sh`. Then write a tiny test script for a different bug in your capstone and bisect with it.

## Parsons practice (5 min)
Order: *start · mark bad · mark good · test · answer · repeat · reset*.

## Common mistakes
| Problem | Fix |
|---|---|
| Forgot `git bisect reset`; now in detached HEAD | `git bisect reset` |
| Marked a commit wrongly | `git bisect log` to see answers; `git bisect replay` after editing, or start again |
| A middle commit can't be tested (doesn't build) | `git bisect skip` (or exit code 125 in a script) |
| The test script is not in old commits | keep the script *outside* the repo, or copy it in before running |
| Using blame to shame | use it to find context and who to ask |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | *Pro Git* [§7.10 **Debugging with Git**](https://git-scm.com/book/en/v2/Git-Tools-Debugging-with-Git): try `git blame -C` and `git bisect run`. | 1 / 3 | 25 min | outputs |
| 2 | *Pro Git* [§7.5 **Searching**](https://git-scm.com/book/en/v2/Git-Tools-Searching): `git log -S` ("pickaxe") and `git log -L`. Find when `bad row` text first appeared in `check.sh`. | 1 / 3 | 15 min | commit id |
| 3 | VS Code: open a file and turn on the blame/annotation view (Timeline or the Source Control *Blame* setting, depending on your version). Compare with `git blame`. | 1 | 10 min | screenshot or notes |
| 4 | **Maths link:** complete a table of *n* vs ⌈log₂ n⌉ for n = 8, 50, 100, 1,000, 1,000,000. | 0 | 10 min | table |

## Exit ticket (5 min)
1. How many tests for 64 commits?
2. What does blame show?
3. *Misconception:* "Blame is for punishing people."

## Key points
- `git blame` → for every line: last commit, author, date; then `git show` for the reason.
- `git bisect` → binary search between a good and a bad commit; ⌈log₂ n⌉ tests.
- `git bisect run <script>` automates it using exit codes (0 good, 125 skip, other bad).
- Small commits and automatic checks make both tools powerful.

## New words
**blame / annotate**, **bisect**, **binary search**, **first bad commit**, **pickaxe (`log -S`)** — see the [glossary](../../glossary.md).

## Extension quest
Use `git bisect` with the terms `old`/`new` instead of `good`/`bad` (`git bisect start --term-old=without --term-new=with`) to find when a *feature* (not a bug) first appeared.

## Teacher notes
- **Timing:** P1: hook 5, understand 20, guess-the-number 15. P2: lab 35, Parsons + exit 5.
- **Frame `blame` as "who can I ask?", not "who is at fault".** Math link: logarithms.
- Build the demo repo on each PC before class, or bundle it.
- **Answer key:** Exit 1: 6 (log₂ 64 = 6). 2: for each line, the last commit, its author and date. 3: False — it finds context and the person to ask. Lab 2: about 4 (⌈log₂ 11⌉). Exercise 4: 3, 6, 7, 10, 20.
