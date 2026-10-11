---
id: g8-m03-first-repo
grade: 8
hours: 2
prerequisites: [g8-m02-snapshots]
outcomes:
  - "Create a repository and make commits with a tool (VS Code or GitHub Desktop)"
  - "Tell the difference between a changed file and a committed file"
  - "Read git status in plain words"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 3. My first repo

!!! abstract "At a glance"
    **Time:** 2 periods · **Tiers:** 1–3 (Tier 0 version below) · **You need:** a lab PC with Git and VS Code (or GitHub Desktop) from the USB kit; the practice repo `g08-class-magazine`; your Module 2 cards

    **Before this:** Module 2 (commit = snapshot + message + parent).

    **By the end you can:** open a repository, change a file, stage it, commit it with a good message, and explain what `git status` is telling you.

!!! note "No computer?"
    Tier 0: the teacher does the steps on one computer while pairs run the *same* steps on their paper cards. The "three places" picture below works on paper.

## Hook (5 min)
In Module 2 you made commit cards by hand: copy the whole sheet, write a message, link the parent. It was slow. Today the computer makes the cards for you — in one click, perfectly, with the date, author and parent filled in automatically.

## Understand it

### A repository is a folder with a memory
A **repository** (**repo** for short) is an ordinary folder that Git is watching. It looks like any folder: you see your files (`article.md`, pictures, notes). The difference is a hidden sub-folder called **`.git`**. That is where Git keeps every commit — the whole history. If you delete `.git`, the folder forgets its history and becomes an ordinary folder again. So: **never touch `.git` by hand.**

You make a folder into a repository once, with **`git init`** (or "Initialize Repository" in VS Code). Or you get a ready-made one, as we do today, by **cloning** the practice repo.

### Three places
Your work moves through three places on its way into history:

```
  my files              the "next snapshot" box        the history
  (working copy)  --->  (staging area)          --->   (commits)
       edit                  add / stage                 commit
```

- **Working copy** — the files you see and edit. Saving in your editor (Ctrl+S) only changes this.
- **Staging area** — a box where you put the changes you want in your *next* snapshot. "Add" or "stage" = *choose what goes in the photo*.
- **History** — the commits. "Commit" = *take the photo and write the message*.

Why a box in the middle? Imagine you fixed a spelling mistake *and* started a new paragraph that is only half done. You can stage only the spelling fix, commit it with the message `Fix spelling of Pokhara`, and leave the half paragraph for later. Each commit stays **one idea**.

### Saving is not committing
This is the most important sentence of the lesson:

> **Ctrl+S saves the file. Only a commit puts it into history.**

If you edit and save but do not commit, Git knows the file *changed* but has no snapshot of it. If you then make a mess, there is nothing to go back to.

### Reading `git status`
`git status` answers "where are my changes right now?". In plain words:

| Git says | It means |
|---|---|
| `nothing to commit, working tree clean` | every change is safely in a commit |
| `Changes not staged for commit: modified: article.md` | you changed and saved the file, but it is *not* in the box yet |
| `Changes to be committed: modified: article.md` | the change is in the box; the next commit will include it |
| `Untracked files: my-notes.md` | a new file Git has never seen; add it if you want it in history |

In VS Code the same information appears in the **Source Control** panel: **M** = modified, **U** = untracked, **A** = added (staged new file). GitHub Desktop shows a list of changed files with ticks.

### Who am I?
Every commit records an author. Before the first commit on a computer, Git needs a name and an email. In school we use a **pseudonym**, never your real email:

```bash
git config --global user.name "Student 07"
git config --global user.email "s07@example.invalid"
```

Your teacher may already have done this on the lab PCs.

## See it
Here is the whole cycle on the command line, with the real output (your commit id will be different). The teacher can show this on the projector while students use the buttons in VS Code.

```console
$ git status
On branch main
nothing to commit, working tree clean          <- everything is committed

  (edit article.md: change the title, press Ctrl+S)

$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   article.md                 <- changed, not in the box

$ git add article.md                           <- put it in the box

$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   article.md                 <- in the box, ready

$ git commit -m "Change title to Dashain Festival at Our School"
[main 366579e] Change title to Dashain Festival at Our School
 1 file changed, 1 insertion(+), 1 deletion(-)

$ git log --oneline -2
366579e Change title to Dashain Festival at Our School
4ebb164 Add closing sentence about the tastiest stall
```

Notice that `git status` even tells you which command to use next — read its hints.

## PRIMM lab (40 min) — pairs, driver/navigator
Use the practice repo `practice-repos/g08-class-magazine`. Copy it from the USB kit, or make your own copy with:

```bash
git clone g08-class-magazine.bundle my-magazine
```

The **driver** uses the mouse and keyboard; the **navigator** reads the steps, predicts, and writes in the notebook. Swap roles every 10 minutes.

**Predict** — before every step, the navigator writes what they think will happen.

1. Open the folder `my-magazine` in VS Code (*File → Open Folder*) and open the **Source Control** panel (the branch-shaped icon on the left), or open it in GitHub Desktop.
   *Checkpoint:* the panel shows no changes. That matches `nothing to commit`.
2. **Predict & run:** change the title in `article.md` and save. What shows up in the panel? *(It is listed with an **M** — modified.)*
3. **Investigate:** click the file name. A **diff** opens: the old line on the left/red, the new line on the right/green. Module 4 explains this fully.
4. **Stage** the file (the **+** button next to it). Predict: where does it move? *(To "Staged Changes".)* Write a message in the box — `Change title to …` — and press **Commit** (✓).
   *Checkpoint:* the panel is empty again; your commit is in history.
5. **Modify:** add a sentence, stage, commit with a good message. Repeat until you have **3 new commits**. Each one = one idea.
6. **Investigate:** make two changes at once (fix a word in paragraph 1, add a line at the end). Stage only… can you? *(In VS Code, open the diff, select the lines, right-click → "Stage Selected Ranges". It is fine if this is hard — the idea matters more than the click.)*
7. **Make:** create a new file `my-notes.md` with two lines about your article idea. Predict what the panel shows *(**U** — untracked)*. Stage and commit it.
8. Open the history (VS Code: *Timeline* at the bottom of the Explorer, or the *Graph* in Source Control; GitHub Desktop: *History* tab). Count your commits. Compare with your Module 2 cards: what did the computer fill in for you?

Optional command-line peek (teacher demonstrates on the projector): repeat steps 2–4 with `git status`, `git add article.md`, `git commit -m "…"`.

## Parsons practice (10 min)
Order the steps: *edit the file · git add article.md · git commit -m "…" · git status says 'nothing to commit'*. Then add where **Ctrl+S** goes.

## Common mistakes
| Symptom | Cause | Fix |
|---|---|---|
| `Please tell me who you are` | no name/email set on this PC | run the two `git config` lines above |
| Panel says "no repository" | folder opened one level too high or too low | open the folder that contains `article.md` (and the hidden `.git`) |
| Commit button greyed out / "no changes added to commit" | nothing staged | stage a file first (+) |
| Commit fails with an empty message | message box empty | write a message |
| "I saved it, why isn't it in history?" | saving ≠ committing | stage and commit |
| A strange `LF will be replaced by CRLF` warning | Windows and Linux use different line endings | harmless; ignore it in Grade 8 |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Software Carpentry [**Tracking Changes**](https://swcarpentry.github.io/git-novice/04-changes.html) — read the diagram of the staging area (the "git add → git commit" picture). Redraw it with our three places and labels in Nepali and English. | 0 (printed, CC BY) / 3 | 15 min | drawing |
| 2 | VS Code docs, [**Source Control overview**](https://code.visualstudio.com/docs/sourcecontrol/overview): find the section on committing. Which keyboard shortcut commits? Try it in the lab. | 1 / 3 | 10 min | the shortcut |
| 3 | [Learn Git Branching `intro1`](https://learngitbranching.js.org/?locale=en_US&level=intro1) again, then in `sandbox` make 4 commits. Compare: what does the real VS Code history show that the game does not? *(messages, files, dates)* | 1 / 3 | 10 min | 2 differences |
| 4 | **Repo from scratch:** make a new empty folder `poem`, initialise it (VS Code: *Initialize Repository*), write a 4-line poem in `poem.md` over 4 commits — exactly like the Module 2 cards. | 1 | 20 min | `git log --oneline` written in notebook |
| 5 | (Teacher or 13+ at home with internet) Read GitHub's [**Hello World**](https://docs.github.com/en/get-started/start-your-journey/hello-world) page *without* doing it — just spot the words *repository*, *commit* and *branch*. We do the online version in Grade 9. | 3 | 10 min | 3 words found |

## Exit ticket (5 min)
1. What is the "box for the next snapshot" called?
2. Why can a file be changed but not yet committed?
3. *Misconception check:* "If I saved the file in my editor, it is in Git's history." True or false? (False.)

## Key points
- A **repository** is a folder whose history lives in a hidden `.git` folder.
- Work flows **working copy → staging area → history** (edit → add → commit).
- **Saving is not committing.** Only a commit makes a snapshot.
- `git status` (or the Source Control panel) tells you where every change is.
- Commits need an author; in school use a pseudonym.

## New words
**repository (repo)**, **`.git` folder**, **working copy**, **staging area**, **stage / add**, **untracked**, **modified**, **`git status`** — see the [glossary](../../glossary.md).

## Extension quest
Use `git log --oneline` and match each line to a card from Module 2. Then run `git log` (without `--oneline`) and find the author and date of the oldest commit. Press **q** to leave the list.
