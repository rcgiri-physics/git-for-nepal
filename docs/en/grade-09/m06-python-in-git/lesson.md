---
id: g9-m06-python-in-git
grade: 9
hours: 2
prerequisites: [g9-m05-remotes]
outcomes:
  - ".gitignore a Python project"
  - "Commit a script and its README"
  - "Use git diff and git log -p to explain and debug a script change"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 6. Python scripts under version control

!!! warning "Placement check"
    CDC's Class 10 computer textbook (2025 ed.) teaches **Python (Unit 4)**. A Grade 9 syllabus has not been located, so students may not have met Python yet. Teach this module in Grade 10 (after Python is taught), or run it read-only with the provided files: the Git skill is the goal.

!!! abstract "At a glance"
    **Time:** 2 periods · **Tiers:** 1–3 · **You need:** Python 3, a terminal, a copy of `practice-repos/g09-ward-facts`

    **Before this:** Modules 2–5.

    **By the end you can:** decide which files belong in a repository, write a `.gitignore`, write a useful README, and use history to find the commit that broke a program.

## Hook (5 min)
Your program worked yesterday and breaks today. You changed "only a little". Can history tell you exactly what changed — and when it broke?

## Understand it

### What belongs in a repository?
A repository should contain everything a person needs to **rebuild and understand** the project, and nothing that the computer can **regenerate** or that must stay **secret**.

| Kind of file | Example | In Git? | Why |
|---|---|---|---|
| source code | `facts.py` | **yes** | it is the work |
| documentation | `README.md`, `DATA.md` | **yes** | people need it |
| small input data you are allowed to share | `data/wards.csv` | **yes** | the script needs it |
| generated / cache files | `__pycache__/`, `*.pyc` | no | Python recreates them |
| output you can recreate | `result.txt`, `chart.png` | usually no | run the script again |
| local databases | `ward.db` | no | rebuild from `.sql` (Module 7) |
| editor settings | `.vscode/`, `.idea/` | usually no | personal |
| **secrets** | passwords, API keys, `.env` | **never** | anyone with the repo can read them — for ever |

### `.gitignore`
A file named **`.gitignore`** in the top folder lists patterns of files Git should not track. Ignored files do not appear in `git status` and `git add .` skips them.

```gitignore
# Python cache files
__pycache__/
*.pyc

# local database built from schema.sql
*.db

# secrets — never commit
.env
```

Pattern rules: `*` matches any characters; a name ending with `/` means a folder; `#` starts a comment. `.gitignore` itself **is** committed, so the whole team ignores the same files. Ready-made templates for every language exist in [github/gitignore](https://github.com/github/gitignore) (CC0 — copy freely).

!!! warning "`.gitignore` does not un-track"
    If a file was already committed, adding it to `.gitignore` does not remove it from history. Remove it from tracking with `git rm --cached <file>` and commit — and if it was a secret, treat it as leaked (Grade 12, Module 5).

### A README that helps
Every repository needs a `README.md` that answers: **What is this? How do I run it? Where does the data come from? Who made it, and under what licence?** A stranger (or you next year) should be able to run the project using only the README.

### History as a debugging tool
When a program breaks, ask *what changed since it last worked?*

- `git diff` — what have I changed since my last commit?
- `git log -p` — every commit **with its diff**; scroll to find a suspicious change (`q` quits).
- `git log -p facts.py` — the same, only for one file.
- `git show <id>` — one commit's change.
- `git restore --source=<good-id> facts.py` — bring back the last working version (Grade 8, Module 5).

This is why **small commits** matter for code: if each commit changes one thing, the commit that broke the program is short and easy to read. (In Grade 12 you will learn `git bisect`, which finds the bad commit automatically.)

## See it
```console
$ python facts.py
Largest ward: Test Ward Four (2310 people)
$ git status --short --ignored
!! __pycache__/                     <- !! = ignored, thanks to .gitignore
$ git log -p -1 facts.py
commit 4f1e2d7 ...
    Rename variable top to biggest
diff --git a/facts.py b/facts.py
@@ -17,5 +17,5 @@
 if __name__ == "__main__":
     wards = load()
-    top = largest_ward(wards)
+    biggest = largest_ward(wards)
     print(f"Largest ward: {top['ward_name']} ({top['population']} people)")
```

The diff shows the bug at once: the variable was renamed on one line but not on the next, so `top` no longer exists. (Your ids will differ.)

## Concept sort (10 min, unplugged)
Print 12 file names on slips (`facts.py`, `__pycache__/facts.cpython-312.pyc`, `README.md`, `.env`, `ward.db`, `data/wards.csv`, `chart.png`, `.vscode/settings.json`, `schema.sql`, `passwords.txt`, `DATA.md`, `notes-for-me.txt`). Pairs sort them into **commit**, **ignore**, **never**. Discuss the hard ones (`chart.png`, `notes-for-me.txt`).

## PRIMM lab (50 min)
Repo: `practice-repos/g09-ward-facts` — copy the folder, then `git init` it and commit everything (`git add . && git commit -m "Start from ward-facts starter"`), or clone the bundle your teacher gives you.

1. **Predict:** read `facts.py`. What will it print? Run `python facts.py`.
2. **Investigate:** open `.gitignore`. Run `git status --short --ignored`. Which file is ignored, and why did it appear only *after* running Python?
3. **Investigate:** temporarily rename `.gitignore` to `gitignore.txt`. What does `git status` show now? Rename it back.
4. **Modify:** change the question the script answers (for example, the ward with the *smallest* population: use `min`). Run, then `git diff`. Commit with a message that says *why*.
5. **Break it on purpose:** rename a variable on one line only (as in *See it*), commit with an innocent message. Run the script — error! Use `git log -p` to find which commit broke it. Fix it with a **new** commit whose message names the bad commit.
6. **Make:** on a branch `add-average`, add a function `average_population(wards)` and print it. Merge the branch into `main` (Module 4). Update the README with one line: *how to run*.

## Parsons practice (10 min)
Order: *edit facts.py · run python · git diff · git add · git commit*. Second set: *program fails · git log -p · find bad commit · fix · commit "Fix … introduced in …"*.

## Common mistakes
| Symptom | Cause | Fix |
|---|---|---|
| `__pycache__` shows as untracked | no `.gitignore` | add the patterns above |
| File still tracked after adding to `.gitignore` | it was committed before | `git rm --cached <file>`, commit |
| `.gitignore` "doesn't work" | saved as `.gitignore.txt` by Windows Notepad | rename; turn on "show file extensions" |
| `python` not found | Python not installed / not on PATH | try `python3` or `py`; ask the teacher |
| Committed a password | — | tell the teacher; change the password; see Grade 12 Module 5 |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Software Carpentry [**Ignoring Things**](https://swcarpentry.github.io/git-novice/06-ignore.html): do the exercises "Ignoring Nested Files" and "Including Specific Files". | 1 / 3 | 25 min | answers |
| 2 | Open the [Python template in github/gitignore](https://github.com/github/gitignore). Find three patterns we did not use and explain what they ignore. | 3 | 15 min | 3 patterns |
| 3 | *Pro Git* [§2.2 **Recording Changes**](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository), section "Ignoring Files": write the five glob-pattern rules in your own words. | 3 | 15 min | rules |
| 4 | GitHub Skills [**Communicate using Markdown**](https://github.com/skills/communicate-using-markdown) (13+, account) — then improve your README. | 3 | 40 min | improved README |
| 5 | **Debug race (Tier 1):** the teacher gives a repo with 10 commits where one broke the script. Find it with `git log -p` faster than the other pairs. | 1 | 15 min | bad commit id |

## Exit ticket (5 min)
1. Why do we ignore `__pycache__/`?
2. How can `git log -p` help debugging?
3. *Misconception:* "If the code works, the history does not matter."

## Key points
- Commit **source, docs and small shareable data**; ignore **generated files**; **never** commit secrets.
- `.gitignore` is itself committed; it does not remove already-tracked files.
- A README says what, how to run, where data comes from, who and licence.
- `git log -p` and small commits turn history into a debugging tool.

## New words
**`.gitignore`**, **pattern / glob**, **generated file**, **secret**, **README**, **`git log -p`** — see the [glossary](../../glossary.md).

## Extension quest
Write a `requirements.txt` (even if empty) and a "How to run" section that a Grade 8 student could follow. Ask one to try it.

## Teacher notes
- **Timing:** P1: hook 5, understand 15, concept sort 10, lab 1–3 (10). P2: lab 4–6 (35), Parsons 5, exit 5.
- Hours depend on CDC placement of Python (unverified). If students have not met Python, use only the provided scripts (read/run/modify) — the Git skill is the goal.
- **Debug race setup (exercise 5):** make 10 small commits to `facts.py`; in commit 6 introduce a typo (`ward_nmae`). Bundle it (`git bundle create debug.bundle --all`).
- **Concept sort answers:** commit — `facts.py`, `README.md`, `data/wards.csv`, `schema.sql`, `DATA.md`; ignore — `__pycache__/…`, `ward.db`, `chart.png` (if regenerated), `.vscode/…`, `notes-for-me.txt` (personal); never — `.env`, `passwords.txt`.
- **Answer key:** Exit 1: Python regenerates them; they are not source. 2: it shows each commit's changes, so you can spot when a bug appeared. 3: False — history lets you understand, debug and undo. Lab 2: `__pycache__/` appears after Python runs because Python creates it then.
