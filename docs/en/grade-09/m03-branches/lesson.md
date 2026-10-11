---
id: g9-m03-branches
grade: 9
hours: 2
prerequisites: [g9-m02-cli-basics]
outcomes:
  - "Explain a branch as a movable label on a commit"
  - "Create, switch and list branches"
  - "Explain HEAD as 'the branch I am on now'"
tier_support: [0, 1, 2, 3]
license: CC-BY-4.0
---

# 3. Branches

!!! abstract "At a glance"
    **Time:** 2 periods · **Tiers:** 0–3 · **You need:** Module 2 cards from Grade 8 (or new ones) and sticky notes; a terminal; Learn Git Branching (self-hosted or online)

    **Before this:** Module 2.

    **By the end you can:** explain what a branch really is, create one, switch between branches, and read a branch graph.

## Hook (5 min)
Two students want to improve the same poem differently: Sita adds a verse, Hari fixes spelling. Do they have to take turns? What if Sita's verse turns out badly — can we throw it away without losing Hari's fixes?

## Understand it

### A branch is a label, not a copy
In Grade 8 the history was one straight line of commits. A **branch** is simply a **name stuck on one commit** — like a sticky note. The default branch is usually called `main`.

```
  c1 <-- c2 <-- c3
                ^
              [main]
```

When you make a new commit on a branch, the commit is added *after* the one the label points to, and **the label moves forward** to the new commit:

```
  c1 <-- c2 <-- c3 <-- c4
                       ^
                     [main]        <- the label moved
```

Creating a new branch makes a **new label on the same commit** — nothing is copied:

```
  c1 <-- c2 <-- c3
                ^
         [main] [add-verse]
```

Now commit on `add-verse`, and only *that* label moves:

```
  c1 <-- c2 <-- c3 <-- c4
                ^      ^
             [main]  [add-verse]
```

Switch back to `main` and commit there (Hari's spelling fix): the history **splits**. Two lines of work grow side by side from `c3`:

```
                    c4   [add-verse]
                   /
  c1 <-- c2 <-- c3
                   \
                    c5   [main]
```

Because a branch is only a label (Git stores it as a tiny file containing a commit id), branches are **cheap**: you can make one for every idea, experiment or task, and delete it later.

### HEAD: "you are here"
How does Git know which label to move when you commit? It keeps one more special pointer, **`HEAD`**, which points at the branch you are on. In `git log` you see it as `HEAD -> main`. **Switching** branches moves HEAD and changes the files in your folder to match that branch's latest commit.

### Switching changes your files
This surprises everyone the first time: if `add-verse` has a file `poem.md` that `main` does not have, then after `git switch main` the file **disappears from the folder**. It is not deleted — it lives in the `add-verse` commits. Switch back and it returns. Your working folder always shows *the snapshot of the branch you are on*.

That is also why Git **refuses to switch** if you have uncommitted changes that would be overwritten — it protects your work. Commit first (or use `git stash`, Grade 11).

### Commands
| Task | Command | Older form (still works) |
|---|---|---|
| list branches (`*` = current) | `git branch` | |
| create a branch here | `git branch <name>` | |
| create and switch to it | `git switch -c <name>` | `git checkout -b <name>` |
| switch to a branch | `git switch <name>` | `git checkout <name>` |
| see all branches as a graph | `git log --oneline --graph --all` | |
| delete a merged branch | `git branch -d <name>` | |

Good branch names are short, lower-case, with hyphens, and say what the work is: `add-verse`, `fix-spelling`, `ward-7-data`.

## See it
```console
$ git branch
* main
$ git switch -c add-verse
Switched to a new branch 'add-verse'
$ echo "verse" > poem.md
$ git add poem.md
$ git commit -qm "Add first verse"
$ git switch main
Switched to branch 'main'
$ ls
README.md                                  <- poem.md is not here: it lives on add-verse
$ git switch -c fix-spelling
Switched to a new branch 'fix-spelling'
$ echo "fixed" >> README.md
$ git commit -qam "Fix spelling in README"
$ git log --oneline --graph --all
* 3e7c90e (add-verse) Add first verse
| * e73e388 (HEAD -> fix-spelling) Fix spelling in README
|/
* 5e7cc8a (main) Describe the project in README
* 8b2c8b6 Add README
```

Read the graph from the bottom: two commits on `main`, then the history splits into `add-verse` and `fix-spelling`. HEAD is on `fix-spelling`.

## Unplugged: the sticky-note model (15 min)
The history is a row of cards (from Grade 8, or new ones). A branch is a **sticky note** stuck on one card.

1. Put a note `main` on the newest card. Put a small coin or a note `HEAD` on the `main` note.
2. **Create a branch:** write a new note `add-verse` and stick it on the *same* card.
3. **Switch:** move the HEAD coin to `add-verse`.
4. **Commit:** add a new card after the current one, connect it to its parent, and move *only the note HEAD is on*.
5. Switch back to `main` (move the coin) and commit there: the cards now fork into two rows.
6. Ask: *when we switched, which card's sheet should be on the desk as the working copy?*

## PRIMM lab (40 min)
Visual first: open [Learn Git Branching level `intro2` "Branching in Git"](https://learngitbranching.js.org/?locale=en_US&level=intro2) (self-hosted in the lab). Complete it, then continue in your own repo.

1. In `ward-facts`: **predict** then run `git branch`.
2. `git switch -c add-verse` (older Git: `git checkout -b add-verse`). Predict what `git log --oneline --graph --all` shows. Run it.
3. Make a commit on `add-verse` that adds a new file. Switch back: `git switch main`. **Investigate:** where did your new file go? (It is not in the working folder — it is on the other branch.) Switch again and check.
4. **Investigate:** edit `README.md` without committing, then try to switch. What happens? Read Git's message. Commit (or undo the edit) and switch.
5. **Modify:** create a second branch `fix-spelling` from `main` and commit there.
6. **Make:** draw the three labels, HEAD and the commits with sticky notes; compare with `git log --graph --all`. They should match exactly.

## Parsons practice (10 min)
Order to make a branch with one commit and return: *switch -c · edit · add · commit · switch main*.

## Common mistakes
| Symptom | Cause | Fix |
|---|---|---|
| "My file vanished!" | you switched to a branch that does not have it | switch back; it is in the other branch's commits |
| `error: Your local changes … would be overwritten by checkout` | uncommitted changes conflict with the target branch | commit them, or undo them, then switch |
| Commit went to the wrong branch | forgot to switch first | check the prompt/`git status` before committing; in Grade 11 you learn to move commits |
| `git switch` not recognised | very old Git | use `git checkout <name>`; update Git if possible |
| `You are in 'detached HEAD' state` | switched to a commit id, not a branch | `git switch main`; detached HEAD is explained in Grade 12 |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Learn Git Branching [`intro2`](https://learngitbranching.js.org/?locale=en_US&level=intro2) and [`rampup1` "Detach yo' HEAD"](https://learngitbranching.js.org/?locale=en_US&level=rampup1). | 1 / 3 | 20 min | drawing of each goal graph |
| 2 | [Visualizing Git](https://git-school.github.io/visualizing-git/): type `git commit`, `git branch idea`, `git checkout idea`, `git commit`. Watch the labels move. | 3 | 10 min | screenshot or drawing |
| 3 | *Pro Git* [§3.1 **Branches in a Nutshell**](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell): look at the figures with `HEAD` and `testing`. Redraw one with our sticky notes. | 3 | 20 min | redrawn figure |
| 4 | **Oh My Git!** ([download](https://ohmygit.org/), Tier 1 after download): play the levels about branches. | 1 | 30 min | levels completed |
| 5 | **Paper quiz:** the teacher draws 4 graphs; for each, write which branch HEAD is on and which files would be in the folder. | 0 | 10 min | answers |

## Exit ticket (5 min)
1. What is a branch?
2. Why did the new file disappear when you switched back to main?
3. *Misconception:* "A branch is a full copy of the folder." True or false?

## Key points
- A **branch** is a movable **label** on a commit; committing moves the label you are on.
- **HEAD** marks the branch you are on.
- **Switching** changes the files in your folder to that branch's snapshot.
- Branches are cheap: one per idea or task.
- Git refuses to switch rather than lose uncommitted work.

## New words
**branch**, **`main`**, **HEAD**, **switch**, **graph**, **detached HEAD** — see the [glossary](../../glossary.md).

## Extension quest
Run `cat .git/HEAD` and `cat .git/refs/heads/main`. What do the files contain? (You have just seen that a branch really is a tiny file with a commit id. Grade 12 goes deeper.)

## Teacher notes
- **Timing:** P1: hook 5, understand with board diagrams 15, sticky notes 15, LGB `intro2` 5. P2: lab 30, Parsons 5, exit 5.
- **The key idea is the pointer.** If students ask "is it a copy?" — no, it is a label, which is why branches are cheap. Always commit before switching; if Git refuses to switch, that protects uncommitted work.
- **Common misconception:** "the branch is the commits after the split." Branch = label on one commit; the commits belong to the graph.
- **Fallback Tier 0:** sticky notes for the whole lab; exercise 5 as the practical.
- **Answer key:** Exit 1: a movable label pointing at a commit. 2: the file exists only in the commits of the other branch; the folder shows the current branch's snapshot. 3: False. Lab 4: Git refuses (or carries the change if there is no conflict — both are possible; discuss why). Extension: `ref: refs/heads/main` and a 40-character commit id.
