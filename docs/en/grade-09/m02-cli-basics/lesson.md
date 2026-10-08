---
id: g9-m02-cli-basics
grade: 9
hours: 2
prerequisites: [g9-m01-terminal-bridge]
outcomes:
  - "Run init/status/add/commit/log in a terminal"
  - "Predict what git status will say before running it"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 2. status, add, commit, log on the command line

## Hook
In Grade 8 you clicked buttons. Today you type the same actions — and every click now has a name you can write down and share.

## Concept (unplugged or visual first)
Revisit the three places (working copy, staging area, history) with a diagram. Map each Grade 8 button to a command: **+** = `git add`, **Commit** = `git commit`, **History** = `git log`.

## PRIMM lab
1. `git init ward-facts` and `cd ward-facts`. **Predict** `git status`, then run it.
2. Create `README.md` with one line. **Predict** status ("untracked"). Run.
3. `git add README.md`; predict status ("new file", staged). Run.
4. `git commit -m "Add README"`. Run `git log --oneline`.
5. **Investigate:** change README, run `git diff`, then `git add`, `git diff --staged`.
6. **Modify:** make 3 more commits with messages that say *what and why*.
7. **Make:** draw your history as cards (like Grade 8) and check with `git log --oneline --graph`.

## Parsons practice
Order: *git init · create a file · git add · git commit · git log*.

## Exit ticket
1. What does `git status` tell you?
2. Difference between `git diff` and `git diff --staged`?
3. *Misconception:* 'git add saves my file to history.' True or false?

## Teacher notes
Set `user.name`/`user.email` with pseudonyms first (see teacher setup). Typical errors: committing from the wrong folder, forgetting quotes around the message, vim opening for the message (type `:q!`; teach `-m`).
