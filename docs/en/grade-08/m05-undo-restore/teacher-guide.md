# Teacher guide — Module 5 (2 periods)

**Timing:** P1: hook 5, unplugged 15, lab 1–2 (20). P2: lab 3–6 (30), Parsons 5, exit 5.

## Common errors
- Students run `restore` on work they wanted to keep. Teach "look at the diff first" as a habit; model it.
- `revert` opens an editor asking for a message: in the default editor save and close, or use `git revert --no-edit HEAD`.
- "Revert" vs "reset": **do not teach `reset` in Grade 8.** If asked: "it can rewrite history; we learn it in Grade 11."

## Fallbacks
Tier 0: do the card version only and ask pairs to explain each choice. Power cuts: committed work survives.

## Answer key
Exit 1: `git restore <file>` / "Discard changes". 2: no — it adds a new commit that undoes the changes. 3: false.
Parsons: notice → log → revert → log again → write why.

## Extension quest
After a revert, can you "revert the revert"? What happens to the article? (It returns.)
