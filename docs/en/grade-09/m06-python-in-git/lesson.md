---
id: g9-m06-python-in-git
grade: 9
hours: 2
prerequisites: [g9-m05-remotes]
outcomes:
  - ".gitignore a Python project"
  - "Commit a script and its README"
  - "Use git diff to explain a script change"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 6. Python scripts under version control

!!! warning "Placement check"
    CDC's Class 10 computer textbook (2025 ed.) teaches **Python (Unit 4)**. A Grade 9 syllabus has not been located, so students may not have met Python (Unit 4) yet. Teach this module in Grade 10 (after Python (Unit 4) is taught), or run it read-only with the provided files: the Git skill is the goal.

## Hook
Your program worked yesterday and breaks today. Can history tell you what changed?

## Concept (unplugged or visual first)
Which files belong in Git? **Source files** (`facts.py`, README) yes; **generated files** (`__pycache__/`, output) no; **secrets** never. Introduce `.gitignore` as 'the list of things Git should ignore'.

## PRIMM lab
Repo: `practice-repos/g09-ward-facts` (copy it).
1. Run `python facts.py`. **Predict** its output from reading the code.
2. `git status` — what is untracked? Add a `.gitignore` containing `__pycache__/` and `*.pyc`.
3. **Modify:** change the question the script answers (e.g. the ward with the largest population). Run, then `git diff`.
4. Commit with a message that says *why*.
5. **Break it on purpose** (typo), commit, find which commit broke it with `git log -p`, fix it with a new commit.
6. **Make:** add a function `average_population` on a branch `add-average`, merge it.

## Parsons practice
Order: *edit facts.py · run python · git diff · git add · git commit*.

## Exit ticket
1. Why do we ignore `__pycache__/`?
2. How can `git log -p` help debugging?
3. *Misconception:* 'if the code works, the history does not matter.'

## Teacher notes
Hours depend on CDC placement of Python (unverified). If students have not met Python, use only the provided scripts (read/run/modify) — the Git skill is the goal.
