---
id: g8-m04-history-diff
grade: 8
hours: 2
prerequisites: [g8-m03-first-repo]
outcomes:
  - "Read the history of a repository"
  - "Use a diff to say what changed between two versions"
  - "Find who/when/why from a commit"
tier_support: [0, 1, 2, 3]
license: CC-BY-4.0
---

# 4. Reading history and comparing versions

## Hook (5 min)
Spot the difference puzzles! A **diff** is a spot-the-difference that the computer solves for you.

## Unplugged: spot the difference (15 min)
Give pairs two printed versions of the same paragraph (the practice repo's `article.md` at commit 2 and commit 5). Mark with a **red pen** each removed word and a **green pen** each added word. Compare with another pair.

## PRIMM lab (40 min)
Repo: `g08-class-magazine` (the starter repo already has 6 commits).

1. **Predict:** look at the list of messages in `git log --oneline` (or the History view in VS Code / GitHub Desktop). Which commit added the third paragraph?
2. **Run & investigate:** open that commit. Red lines = removed, green lines = added. Does it match your prediction?
3. **Investigate more:** in `git log` find the author, date and message of each commit.
4. **Modify:** make a new edit that changes one word; before you commit, open the diff and describe it in your notebook.
5. **Make:** write a message that matches exactly what the diff shows.

Command-line (optional):
```bash
git log --oneline
git show <commit-id>
git diff
```
`git diff` shows changes you have not committed; `git show` shows what one commit changed.

## Parsons practice (10 min)
Match each description to a command: *list the history* · *what did this commit change?* · *what have I changed since the last commit?*

## Exit ticket (5 min)
1. What do red and green lines mean in a diff?
2. Name two pieces of information a commit stores besides the file changes.
3. *Misconception check:* "A diff shows the whole file." (No — only the lines that differ.)
