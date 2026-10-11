# Teacher guide — Module 4 (2 periods)

**Goal:** students read history and diffs fluently and use them to answer who / when / what / why.

**Timing:** P1: hook 5, "Understand it" with the annotated diff on the board 10, unplugged 15, lab 1–2 (10). P2: lab 3–6 (25), Parsons 5, free-resource exercise 3 (5), exit 5.
**Materials:** printed `versions/v2.md` and `versions/v5.md` (one pair each), red and green pens; for Tier 0 also `log-sample.txt` and `versions/v3.md`, `versions/v4.md`.

## Facts about the practice repo you need
| Commit (message) | What its diff does |
|---|---|
| 1 `Add working title` | creates `article.md` with a title |
| 2 `Add better title and opening line` | new title + first sentence (3 lines added, 1 removed) |
| 3 `Say where the festival is and what happens` | changes the opening sentence |
| 4 `Add paragraph about food stalls and library fund` | adds 2 lines |
| 5 `Add Class Eight momo paragraph (typo left in on purpose)` | adds momo line **and** changes *models* → *modals* |
| 6 `Add closing sentence about the tastiest stall` | extends the momo line **and silently fixes** *modals* → *models* |

Commit ids depend on the time zone of the PC that built the repo, so read them from your own `git log`.

## Common errors
- `git log` opens a pager and the student is stuck: press **q** to quit.
- Colour-blind students: also teach the `+` and `-` signs at the start of lines; the unplugged activity can use "circle" and "underline" instead of colours.
- Mixing up `git diff` (uncommitted) and `git show` (a commit). Keep the three-question table on the board.
- "`git diff` shows nothing" after staging: use `git diff --staged`.
- A changed word shows as a whole changed line — expected; Git compares lines.

## Fallbacks
- **Tier 0:** print the two versions of `article.md` (commit 2 and commit 5) and the log from the practice repo; run the whole lesson on paper. The lab table (step 3) can be filled from the printed table above.
- **One computer:** project it; pairs answer on paper and call out predictions.

## Differentiation
- **Support:** give the lab table with ids and messages already filled; students add authors, dates, sizes.
- **Stretch:** `git log --since=2026-10-03`, `git log -p` (every diff), `git diff --word-diff`.

## Evidence to collect
The completed lab table and the hand-written diff (exercise 3).

## Answer key
- **Lab 1:** commit 4, `Add paragraph about food stalls and library fund`.
- **Lab 4:** commit 6 fixed the typo; its message does not mention it → messages should describe every change, or the fix should have been its own commit.
- **Exit 1:** red/`-` removed, green/`+` added. **2:** author, date/time, message, parent commit (any two). **3:** false.
- **Parsons:** `git log --oneline` list history · `git show <id>` commit changes · `git diff` uncommitted changes · `git log --stat` lines changed per commit.
- **Free-resource 1:** `HEAD~1` means "one commit before the latest"; `HEAD~2` two before.
- **Free-resource 3:** v3 → v4 adds a blank line and the food-stalls sentence (2 lines with `+`).

## Extension quest
Find the commit where a word was misspelled and when it was fixed (commits 5 and 6).
