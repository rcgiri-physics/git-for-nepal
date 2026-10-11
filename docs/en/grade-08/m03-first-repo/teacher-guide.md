# Teacher guide — Module 3 (2 periods)

**Goal:** students make real commits with a GUI and can say where a change is (working copy, staging area, history).

**Setup (before class, once per PC):** Git and VS Code (or GitHub Desktop) installed from the Tier 1 USB kit. Then run:

```bash
git config --global user.name "Student 07"
git config --global user.email "s07@example.invalid"
git config --global init.defaultBranch main
```

Use a different number per PC; never students' real emails. Copy `g08-class-magazine.bundle` to each PC (see `practice-repos/g08-class-magazine/README.md`) and test one clone yourself.

**Timing:** P1: hook 5, concept "three places" 15, see-it demo 5, lab steps 1–4 (15). P2: lab steps 5–8 (25), Parsons 5, free-resource exercise 1 or 4 (5), exit 5.

## Teaching the three places
Draw the three boxes on the board and keep them there all period. Every time a student asks "where is my change?", point to a box. Physical version: three trays on your desk labelled *working copy*, *box*, *history*; move a paper slip through them as you demonstrate.

## Common errors
| Symptom | Fix |
|---|---|
| "Please tell me who you are" | the `git config` commands above |
| Folder opened one level too high | open the folder that contains `article.md` |
| Commit button greyed out | nothing staged; stage a file first |
| Message empty, commit fails | write a message |
| Confusion: save vs commit | point back to the three-places picture; say "Ctrl+S is not a commit" |
| VS Code asks "stage all changes and commit directly?" | fine to say yes in Grade 8, but explain it skipped the box |
| `LF will be replaced by CRLF` warning | harmless on Windows; ignore |
| `git log` seems stuck | it opened a pager; press **q** |

## Fallbacks
- **One computer:** teacher drives with the projector; pairs sit with the paper cards and predict each result before you click.
- **No computer (Tier 0):** repeat the Module 2 cards with three-places labels: a tray for the working sheet, an envelope for "staged", the card row for history.
- **Power cut mid-lab:** files already committed are safe. Uncommitted edits may be lost if the editor had not saved them. Use it as a teaching moment after power returns: run `git status` and see what survived.

## Differentiation
- **Support:** a printed step card with screenshots of the VS Code Source Control panel; pair a confident driver with an anxious navigator first, then swap.
- **Stretch:** free-resource exercise 4 (new repo from scratch) and lab step 6 (stage only part of a file).

## Evidence to collect
Ask each pair to write `git log --oneline` (or the history list) in their notebook. Look for ≥ 3 new commits with verb-first messages.

## Answer key
- **Exit 1:** the staging area. **2:** because it is only in the working copy until it is staged and committed. **3:** False.
- **Parsons:** edit (then Ctrl+S) → add → commit → status says nothing to commit.
- **Free-resource 2:** Ctrl+Enter in the message box commits (check your VS Code version; it may differ).
- **Free-resource 3:** VS Code shows messages, changed files, author and dates; the game shows only the graph.

## Extension quest
Use `git log --oneline` and match each line to a card from Module 2.
