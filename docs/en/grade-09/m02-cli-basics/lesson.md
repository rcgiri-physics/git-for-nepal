---
id: g9-m02-cli-basics
grade: 9
hours: 2
prerequisites: [g9-m01-terminal-bridge]
outcomes:
  - "Run init/status/add/commit/log in a terminal"
  - "Predict what git status will say before running it"
  - "Use git diff and git diff --staged to check work before committing"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 2. status, add, commit, log on the command line

!!! abstract "At a glance"
    **Time:** 2 periods · **Tiers:** 1–3 · **You need:** Git Bash or a terminal; a pseudonymous `user.name`/`user.email` already set

    **Before this:** Module 1 (terminal), and Grade 8's three places.

    **By the end you can:** create a repository from the terminal, run the full commit cycle, and predict `git status` before you run it.

## Hook (5 min)
In Grade 8 you clicked buttons. Today you type the same actions — and every click now has a name you can write down, share in a chat, and repeat exactly. "Click the plus, then the tick" becomes `git add README.md && git commit -m "Add README"`.

## Understand it

### Same three places, now with names
```
  working copy  --git add-->  staging area  --git commit-->  history
       ^                                                       |
       +------------------ git restore (Grade 8) --------------+
```

| Grade 8 button | Command | What it does |
|---|---|---|
| *Initialize Repository* | `git init` | makes the hidden `.git` folder |
| file list in Source Control | `git status` | where is every change? |
| click a changed file | `git diff` | changes not yet staged |
| **+** (stage) | `git add <file>` | put the change in the box |
| click a staged file | `git diff --staged` | what *will* be committed |
| **✓ Commit** + message | `git commit -m "message"` | take the snapshot |
| History / Timeline | `git log`, `git log --oneline` | read the history |

### The shape of a Git command
```
git  commit  -m  "Add README"
 |     |      |      |
 |     |      |      +-- argument for the option (quotes keep the words together)
 |     |      +--------- option (starts with -)
 |     +---------------- subcommand: what you want Git to do
 +---------------------- the program
```

### Status is your best friend
Run `git status` **before and after every other command** until you can predict its answer. It shows the branch you are on, what is staged ("to be committed"), what is changed but not staged, and what is untracked (new files Git does not know yet). It also prints hints for the next command.

A file's life:

```
 untracked --add--> staged (new file) --commit--> committed (clean)
                                                     |
                     staged (modified) <--add-- modified (edit + save)
```

### `diff` vs `diff --staged`
- `git diff` = working copy compared with the staging area → *"what have I changed but not staged?"*
- `git diff --staged` = staging area compared with the last commit → *"what will my next commit contain?"*

Professionals run `git diff --staged` right before committing. It catches accidents — a debugging line, a password, a file you didn't mean to include.

### Messages on the command line
`-m "…"` gives the message directly. If you forget `-m`, Git opens a text editor to ask for one. If that editor is **Vim** (a black screen with `~` signs), type `:q!` and Enter to quit without committing, then use `-m`. Your teacher can set an easier editor with `git config --global core.editor "code --wait"`.

## See it
Real output from a new repository:

```console
$ git init ward-facts
Initialized empty Git repository in /c/Users/student07/ward-facts/.git/
$ cd ward-facts
$ git status
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
$ echo "# Ward Facts" > README.md          <- creates a file with one line
$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present (use "git add" to track)
$ git add README.md
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
$ git commit -m "Add README"
[main (root-commit) 8b2c8b6] Add README
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
$ git log --oneline
8b2c8b6 Add README
```

`root-commit` means "the first commit — it has no parent".

## Concept warm-up (10 min, unplugged)
On the board, draw the three places as boxes. The teacher reads out commands one by one (`git add notes.md`, edit `notes.md` again, `git commit`…); students move a paper slip for each file between the boxes on their desks, then say what `git status` would print.

## PRIMM lab (50 min)
1. `git init ward-facts` and `cd ward-facts`. **Predict** `git status`, then run it.
2. Create `README.md` with one line (`echo "# Ward Facts" > README.md`, or use VS Code: `code README.md`). **Predict** status ("untracked"). Run.
3. `git add README.md`; predict status ("new file", staged). Run.
4. `git commit -m "Add README"`. Run `git log --oneline`.
5. **Investigate:** change README (add a sentence), run `git diff`. Then `git add README.md` and run `git diff` again — why is it empty now? Run `git diff --staged`.
6. **Investigate:** edit README *again* after staging. Run `git status`. Why is README listed **twice**, as staged and not staged? *(The box holds the first edit; the second edit is only in the working copy.)*
7. **Modify:** make 3 more commits with messages that say *what and why*. Add a second file `notes.md` in one of them.
8. **Make:** draw your history as cards (like Grade 8) and check with `git log --oneline --graph`. Then try `git log --stat` and `git show HEAD`.

## Parsons practice (10 min)
Order: *git init · create a file · git add · git commit · git log*. Second set (harder): *edit file · git diff · git add · git diff --staged · git commit -m "…" · git status*.

## Common mistakes
| Symptom | Cause | Fix |
|---|---|---|
| `fatal: not a git repository` | you are in the wrong folder | `pwd`; `cd` into the repo |
| `Please tell me who you are` | identity not set | `git config --global user.name "Student 07"` and `user.email "s07@example.invalid"` |
| `error: pathspec 'Add' did not match` | message without quotes | `git commit -m "Add README"` |
| Vim opens | forgot `-m` | `:q!` Enter, then use `-m` |
| Committed in your home folder by mistake (the whole home is a repo!) | ran `git init` in `~` | ask the teacher; remove only that `.git` folder carefully |
| `git add .` added files you did not want | `.` means *everything here* | check with `git status` first; `git restore --staged <file>` |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Software Carpentry [**Creating a Repository**](https://swcarpentry.github.io/git-novice/03-create.html) and [**Tracking Changes**](https://swcarpentry.github.io/git-novice/04-changes.html). Do the exercises "Places to Create Git Repositories" and "Choosing a Commit Message". | 1 / 3 | 40 min | answers |
| 2 | *Pro Git* [§2.2 **Recording Changes to the Repository**](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository): read the "short status" part and try `git status -s`. What do `??`, `A` and `M` mean? | 1 / 3 | 15 min | the three codes |
| 3 | [Git Immersion](https://gitimmersion.com/), labs 1–10 (setup through "Changes, not files"). Use a pseudonym in the setup lab. | 3 | 45 min | the history you made |
| 4 | **Predict-the-status worksheet** (teacher guide): 8 situations, write what `git status -s` prints for each. | 0 | 15 min | worksheet |
| 5 | Check your setup: `git config --list --show-origin`. Where is your name stored? (*Pro Git* [§1.6 **First-Time Git Setup**](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).) | 1 | 10 min | file path |

## Exit ticket (5 min)
1. What does `git status` tell you?
2. Difference between `git diff` and `git diff --staged`?
3. *Misconception:* "`git add` saves my file to history." True or false?

## Key points
- `init` → (edit) → `add` → `commit` → `log` is the cycle; `status` between every step.
- A file is untracked → staged → committed → modified → staged …
- `git diff` = not yet staged; `git diff --staged` = what the next commit contains.
- Always use `-m "message"` with quotes; read Git's hints.

## New words
**`git init`**, **root commit**, **option / argument**, **short status**, **`git diff --staged`** — see the [glossary](../../glossary.md).

## Extension quest
Make an **alias**: `git config --global alias.lg "log --oneline --graph --all"`. Now `git lg` draws the graph. (*Pro Git* §2.7 "Git Aliases".)

## Teacher notes
- **Timing:** P1: hook 5, understand 15, see it (live) 10, warm-up 10. P2: lab 35, Parsons 5, exit 5. Lab steps 7–8 can be homework.
- Set `user.name`/`user.email` with pseudonyms first (see [teacher setup](../../teachers/setup.md)). Also set `init.defaultBranch main` and an easy editor.
- **Typical errors:** committing from the wrong folder, forgetting quotes around the message, Vim opening for the message (type `:q!`; teach `-m`).
- **Predict-the-status worksheet** (exercise 4) — situations and answers (`git status -s`): new file not added → `?? a.txt`; new file added → `A  a.txt`; committed file edited → ` M a.txt`; edited and added → `M  a.txt`; added then edited again → `MM a.txt`; nothing changed → (no output); file deleted with `rm` → ` D a.txt`; two new files, one added → `A  a.txt` and `?? b.txt`.
- **Answer key:** Exit 1: which branch, what is staged, modified, untracked. 2: unstaged changes vs staged changes. 3: False — `add` only puts it in the box; `commit` makes history. Lab 5: after `add`, the working copy equals the box, so `git diff` is empty. Exercise 2: `??` untracked, `A` added (new, staged), `M` modified.
