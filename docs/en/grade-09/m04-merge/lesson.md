---
id: g9-m04-merge
grade: 9
hours: 2
prerequisites: [g9-m03-branches]
outcomes:
  - "Merge a branch into main"
  - "Tell a fast-forward merge from a merge commit"
  - "Recognise and resolve a simple merge conflict"
tier_support: [0, 1, 2, 3]
license: CC-BY-4.0
---

# 4. Merge and the merge-conflict game

!!! abstract "At a glance"
    **Time:** 2 periods · **Tiers:** 0–3 · **You need:** a printed 5-line poem per pair, two pen colours; your `ward-facts` repo with branches from Module 3

    **Before this:** Module 3 (branches).

    **By the end you can:** merge a branch, say whether Git did a fast-forward or made a merge commit, and calmly resolve a conflict.

## Hook (5 min)
Two edits to the same line of the poem. Sita wrote *"Rivers flow down to the Terai"*; Hari wrote *"Rivers rush to the plains"*. Who wins? Should a computer decide?

## Understand it

### Merging joins two lines of work
In Module 3 the history split into branches. **Merging** brings the work of one branch *into* another. You always merge **into the branch you are on**:

```bash
git switch main          # go to the branch that should receive the work
git merge add-verse      # bring add-verse's commits into main
```

Git can merge in two ways, depending on the shape of the history.

### Case 1: fast-forward
If `main` has **not moved** since the branch was made, there is nothing to combine. Git simply slides the `main` label forward to the branch's newest commit:

```
 before:  c1 -- c2 [main]                 after:  c1 -- c2 -- c3 [main] [add-verse]
                  \
                   c3 [add-verse]
```

No new commit is made. Git prints `Fast-forward`.

### Case 2: merge commit
If **both** branches have new commits, Git makes a new **merge commit** with **two parents** — it joins the two lines:

```
 before:        c3 [fix-spelling]          after:        c3 -------.
               /                                         /           \
  c1 -- c2 --+                              c1 -- c2 --+             m [main]
               \                                         \           /
                c4 [main]                                 c4 -------'
```

Git compares both branches with their **common ancestor** (`c2`, the last commit they share) and combines the changes automatically — as long as they changed *different* lines.

### Conflicts: when a human must decide
If both branches changed **the same lines** of the same file, Git cannot know which version is right. It stops and marks the file with a **conflict**:

```
Mountains stand tall
<<<<<<< HEAD
Rivers flow down to the Terai          <- the version on the branch you are on (main)
=======
Rivers rush to the plains              <- the version from the branch you are merging
>>>>>>> fix-spelling
The morning is cold
```

| Marker | Means |
|---|---|
| `<<<<<<< HEAD` | start of *your* side (the current branch) |
| `=======` | divider |
| `>>>>>>> fix-spelling` | end of *their* side (the branch being merged) |

**To resolve:** edit the file so it says what it *should* say — keep one side, the other, or write a combination — and **delete all three marker lines**. Then `git add` the file (meaning "resolved") and `git commit` to finish the merge.

!!! tip "A conflict is not an error"
    A conflict is Git politely asking a human for a decision. Nothing is lost: both versions are in the file and in history. If you feel lost, `git merge --abort` puts everything back to before the merge.

### Avoiding conflicts
Conflicts are normal in teams, but you can make them rare: **merge often** (small branches live short lives), **split work by file or section**, and **talk** before two people edit the same paragraph.

## See it
A fast-forward, then a real conflict:

```console
$ git switch main
$ git merge add-verse
Updating c26da4a..f60bbe5
Fast-forward
 poem.txt | 1 +
 1 file changed, 1 insertion(+)

  (now main and fix-spelling both change line 2)

$ git merge fix-spelling
Auto-merging poem.txt
CONFLICT (content): Merge conflict in poem.txt
Automatic merge failed; fix conflicts and then commit the result.
$ git status
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   poem.txt

  (edit poem.txt: keep "Rivers rush down to the Terai", delete the markers)

$ git add poem.txt
$ git commit --no-edit
$ git log --oneline --graph --all
*   97832b0 (HEAD -> main) Merge branch 'fix-spelling'
|\
| * 3d873e6 (fix-spelling) Change line 2 to rush
* | be9221d Name the Terai in line 2
|/
* f60bbe5 (add-verse) Add sixth line about terraces
* c26da4a Add poem
```

The merge commit `97832b0` has two parents — you can see both lines joining in the graph.

## Unplugged: the paper merge-conflict game (20 min)
Pairs share a printed 5-line poem — this is the **common ancestor**.

1. Each partner gets a copy and edits it with their own pen colour: partner A changes lines 1 and 3; partner B changes lines 3 and 5.
2. **Merge:** on a fresh sheet, combine both copies. Lines only one person changed: take that change (Git does this automatically). Line 3, changed by both: write the conflict with markers — `<<<<<<< A`, A's line, `=======`, B's line, `>>>>>>> B`.
3. **Resolve:** the pair discusses and writes the final line 3, crossing out the markers.
4. Write the rule on the board: *Git can combine changes to different lines, but when both change the same line, a human decides.*

## PRIMM lab (40 min)
1. **Predict:** you merge `add-verse` (new lines) into `main`. Will there be a conflict? Will it be a fast-forward? Run `git switch main`, `git merge add-verse`.
2. **Investigate:** `git log --graph --oneline --all`. Was it a fast-forward or a merge commit? How can you tell?
3. **Create a conflict:** make sure you have a `poem.txt` committed on `main`. On `fix-spelling` change line 2 and commit; on `main` change line 2 differently and commit. **Predict**, then `git merge fix-spelling`.
4. Run `git status`. Open the file, find the markers, decide the final line, delete the markers, `git add poem.txt`, `git commit`.
5. **Investigate:** draw the graph. How many parents does the merge commit have? Check with `git log --oneline --graph`.
6. **Modify:** repeat with your partner changing *different* lines — no conflict. Then try `git merge --abort` in the middle of a conflict and check `git status`.
7. **Make:** write a team rule for your pair project: who edits which file, and how often you merge.

## Parsons practice (10 min)
Order for resolving a conflict: *merge · open the file · edit and remove markers · git add · git commit*.

## Common mistakes
| Symptom | Cause | Fix |
|---|---|---|
| Markers `<<<<<<<` left in the file and committed | forgot to delete them | edit the file, remove markers, commit again; search with `git grep "<<<<<<<"` |
| Merged in the wrong direction | ran merge on the wrong branch | check `git status` first; `git merge --abort` if not finished |
| Vim opens for the merge message | merge commit needs a message | `:wq` to accept, or `git commit --no-edit` |
| `fatal: You have not concluded your merge` | a merge is still in progress | finish (`add` + `commit`) or `git merge --abort` |
| "Git deleted my line!" | you chose the other side | it is still in the branch's commit; `git show fix-spelling:poem.txt` |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Learn Git Branching [`intro3` "Merging in Git"](https://learngitbranching.js.org/?locale=en_US&level=intro3). | 1 / 3 | 10 min | goal graph drawing |
| 2 | Software Carpentry [**Conflicts**](https://swcarpentry.github.io/git-novice/09-conflict.html): do the exercise "Solving Conflicts that You Create". | 1 / 3 | 30 min | your resolved file + log |
| 3 | *Pro Git* [§3.2 **Basic Branching and Merging**](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging): find the figures for fast-forward and for the three-way merge. Label the common ancestor. | 3 | 20 min | labelled sketch |
| 4 | GitHub Skills [**Resolve merge conflicts**](https://github.com/skills/resolve-merge-conflicts) (13+, account, internet). | 3 | 45 min | completed course |
| 5 | **Conflict cards (paper):** the teacher hands out 6 pairs of edits; decide for each: no conflict / fast-forward / conflict. | 0 | 10 min | answers |

## Exit ticket (5 min)
1. When does a conflict happen?
2. What do the markers mean?
3. *Misconception:* "After a conflict my work is lost." True or false?

## Key points
- `git merge <branch>` brings that branch's work **into the current branch**.
- **Fast-forward:** the label just moves; **merge commit:** a new commit with two parents.
- Git merges changes to **different lines** automatically; the **same lines** → conflict → a human decides.
- Resolve: edit, remove markers, `git add`, `git commit`. Escape: `git merge --abort`.
- Merge often, split work, talk — fewer conflicts.

## New words
**merge**, **fast-forward**, **merge commit**, **common ancestor**, **conflict**, **conflict markers** — see the [glossary](../../glossary.md).

## Extension quest
After a merge commit, run `git log --first-parent --oneline`. What does it hide? Why might a team like this view?

## Teacher notes
- **Timing:** P1: hook 5, understand 15, paper game 20. P2: see it (live on projector) 5, lab 25, Parsons 5, exit 5.
- **Students panic at conflicts.** Normalise: conflicts are Git asking for a human decision. `git merge --abort` returns to before the merge. Make a conflict *on purpose* in front of the class and resolve it slowly, thinking aloud.
- In VS Code, a conflicted file shows buttons *Accept Current / Accept Incoming / Accept Both* — fine to use, but students must still understand the markers.
- **Conflict cards (exercise 5) answers:** same line both sides → conflict; different lines → merge commit, no conflict; only one side changed → fast-forward; one side adds a line at the end, other edits line 1 → no conflict; both add *different* lines at the end → conflict (same place); one renames the file, other edits it → usually no conflict (Git detects renames).
- **Fallback Tier 0:** the paper game plus exercise 5.
- **Answer key:** Exit 1: when both branches changed the same lines (or one deleted a file the other changed). 2: start of current side / divider / end of incoming side. 3: False — both versions are kept until you decide.
