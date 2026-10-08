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

!!! note "No computer?"
    Tier 0: the teacher does the steps on one computer while pairs run the *same* steps on their paper cards. The "three places" picture below works on paper.

## Hook (5 min)
In Module 2 you made cards by hand. Today the computer makes the cards for you.

## Concept: three places (15 min)
Draw on the board and have students copy it:

```
 my files          the "next snapshot" box          the history
 (working copy) -> (staging area)               ->  (commits)
     edit             add                            commit
```
- **edit**: change a file.
- **add**: put the change into the box for the next snapshot ("add" = *choose what goes in the photo*).
- **commit**: take the photo and write the message.

## PRIMM lab (40 min) — pairs, driver/navigator
Use the practice repo `practice-repos/g08-class-magazine` (copy it from the USB kit, or `git clone g08-class-magazine.bundle my-magazine`).

**Predict** — before every step, the navigator writes what they think will happen.

1. Open the folder in VS Code and open the **Source Control** panel (or GitHub Desktop).
2. **Predict & run:** change the title in `article.md`. What shows up in the panel? (It is listed as *modified*.)
3. **Investigate:** click the file to see the lines that changed.
4. Stage the file (the **+** button), write a message ("Change title to …"), and commit.
5. **Modify:** add a sentence, stage, commit with a good message. Repeat until you have 3 commits.
6. **Make:** create a new file `my-notes.md`, commit it with a message.

Optional command-line peek (teacher demonstrates on the projector):
```bash
git status
git add article.md
git commit -m "Change title to the school name"
```

## Parsons practice (10 min)
Order the steps: *edit the file · git add article.md · git commit -m "…" · git status says 'nothing to commit'*.

## Exit ticket (5 min)
1. What is the "box for the next snapshot" called?
2. Why can a file be changed but not yet committed?
3. *Misconception check:* "If I saved the file in my editor, it is in Git's history." True or false? (False.)
