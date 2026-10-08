# Teacher guide — Module 3 (2 periods)

**Setup (before class):** Git and VS Code (or GitHub Desktop) installed (tier 1 USB kit). Run once per PC:
`git config --global user.name "Student 07"` and `git config --global user.email "s07@example.invalid"` — pseudonymous, never real emails.
**Timing:** P1: hook 5, concept 15, lab steps 1–3 (20). P2: lab steps 4–6 (30), Parsons 5, exit 5.

## Common errors
| Symptom | Fix |
|---|---|
| "Please tell me who you are" | the `git config` commands above |
| Folder opened one level too high | open the folder that contains `article.md` |
| Commit button greyed out | nothing staged; stage a file first |
| Message empty, commit fails | write a message |
| Confusion: save vs commit | point back to the three-places picture |

## Fallbacks
- One computer: teacher drives with the projector; pairs sit at the paper cards and predict each result.
- No computer (tier 0): Module 2 cards repeated with the three-places labels.
- Power cut mid-lab: files already committed are safe. Uncommitted edits may be lost if the editor had not saved them.

## Answer key
Exit 1: the staging area. 2: because it is only in the working copy until committed. 3: False.
Parsons: edit → add → commit → status says nothing to commit.

## Extension quest
Use `git log --oneline` and match each line to a card from Module 2.
