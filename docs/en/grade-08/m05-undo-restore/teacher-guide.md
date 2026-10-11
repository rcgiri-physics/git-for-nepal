# Teacher guide — Module 5 (2 periods)

**Goal:** students choose the right, *safe* undo for a situation, and trust that committed work cannot be lost.

**Timing:** P1: hook 5 (live demo), "Understand it" with the decision table 10, unplugged 15, lab 1 (10). P2: lab 2–6 (30), Parsons 5, exit 5.
**Before class:** on the projector PC, make the "disaster" ready: delete three paragraphs of `article.md`, save, *don't commit*. Practise `git restore article.md` once. Also set VS Code as Git's editor so revert does not open Vim: `git config --global core.editor "code --wait"` (or teach `--no-edit`).

## Quick-fire situations (unplugged, round 2)
Read out; pairs hold up RESTORE / REVERT / OLD VERSION:
1. "I typed rubbish into my poem 5 minutes ago and haven't committed." → RESTORE
2. "Yesterday I committed a paragraph that is wrong." → REVERT
3. "I want the title I had on Monday." → OLD VERSION
4. "I committed a joke about my friend by mistake." → REVERT (and discuss: it is still in history! In Grade 12 we learn that secrets/private data need special handling — so never commit them.)
5. "I deleted a file but didn't commit." → RESTORE
6. "The new ending is worse than last week's." → OLD VERSION

## Common errors
- Students run `restore` on work they wanted to keep. Teach "look at the diff first" as a habit; model it aloud every time.
- `revert` opens an editor asking for a message: in Vim type `:wq` + Enter; better, use `git revert --no-edit HEAD` or set VS Code as the editor (above).
- **"Revert" vs "reset":** do not teach `reset` in Grade 8. If asked: "it can rewrite history; we learn it in Grade 11."
- `restore --source` leaves a change that is not yet committed; students think nothing happened. Ask them to run `git status`.
- Revert of an older commit (not the latest) can produce a conflict. Keep to reverting `HEAD` in Grade 8.

## Fallbacks
Tier 0: do the card version only and ask pairs to explain each choice. Power cuts: committed work survives — demonstrate it after the power returns.

## Differentiation
- **Support:** give the "Which undo do I need?" table as a printed card to keep on the desk.
- **Stretch:** free-resource exercise 5, and "revert the revert".

## Evidence to collect
The history drawing after lab step 6 (bad commit + revert) and the revert message (should say *why*).

## Answer key
- **Exit 1:** `git restore <file>` / "Discard changes". **2:** no — it adds a new commit that undoes the changes. **3:** false.
- **Parsons:** notice → log → revert → log again → write why.
- **Lab 2 prediction:** one *more* commit.
- **Free-resource 3:** discarded local changes are gone for good; Git cannot recover them because they were never committed.
- **Free-resource 2:** after `git revert`, a new commit (C2') appears after the commit being reverted.

## Extension quest
After a revert, can you "revert the revert"? What happens to the article? (It returns to the "bad" version, and the history shows all three steps.)
