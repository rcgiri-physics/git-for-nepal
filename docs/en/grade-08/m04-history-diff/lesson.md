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

!!! abstract "At a glance"
    **Time:** 2 periods · **Tiers:** 0–3 (Tier 0 uses printed versions) · **You need:** the practice repo `g08-class-magazine` (6 commits), red and green pens, printed versions for Tier 0

    **Before this:** Module 3 (making commits).

    **By the end you can:** read a history list; open a commit and say what it changed; read a diff line by line; find who, when and why for any change.

## Hook (5 min)
Do you know "spot the difference" puzzles — two pictures that look the same, with seven small changes? A **diff** is a spot-the-difference that the computer solves for you, perfectly, in less than a second, even for a 100-page document.

## Understand it

### History: the list of commits
The **history** (also called the **log**) is the list of every commit, newest first. Each entry shows:

```console
$ git log
commit 711a420055201db8271b5be81c7b6dd2243f5084      <- commit id
Author: Teacher <teacher@example.invalid>             <- who
Date:   Mon Oct 5 10:00:00 2026 +0545                 <- when (+0545 = the time zone, here Nepal)

    Add Class Eight momo paragraph (typo left in on purpose)   <- why / what
```

The short form shows one line per commit:

```console
$ git log --oneline
4ebb164 Add closing sentence about the tastiest stall
711a420 Add Class Eight momo paragraph (typo left in on purpose)
53bf9f6 Add paragraph about food stalls and library fund
b16c8b6 Say where the festival is and what happens
78a873e Add better title and opening line
d38a483 Add working title
```

Reading a history is like reading the contents page of a book: the messages tell the story of how the work grew. This is why good messages matter.

### Diff: what exactly changed
A **diff** compares two versions and shows *only the lines that differ*:

```diff
--- a/article.md                    <- the old version ("a")
+++ b/article.md                    <- the new version ("b")
@@ -1,5 +1,7 @@                     <- where: old lines 1–5, new lines 1–7
 # Our School Festival               <- unchanged line (starts with a space)

-The festival is ... science models.     <- removed line (starts with -)
+The festival is ... science modals.     <- added line (starts with +)

 The best part is the food stalls. ...   <- unchanged
+
+Class Eight made momo and sold forty plates.   <- two new lines
```

The rules are short:

| Line starts with | Colour (usually) | Meaning |
|---|---|---|
| `-` | red | this line was **removed** (or is the old form of a changed line) |
| `+` | green | this line was **added** (or is the new form) |
| a space | normal | unchanged, shown only for context |

Git compares whole **lines**. If you change one word, Git shows the old line with `-` and the new line with `+`. Look carefully at the two lines to find the word — in the example above, *models* became *modals*: a typo was added!

If you cannot see colours (or print in black and white), the `+` and `-` signs carry the same information.

### Three ways to ask "what changed?"
| Question | Command | In VS Code / GitHub Desktop |
|---|---|---|
| What have I changed since my last commit (not yet committed)? | `git diff` | click a file in the Source Control panel |
| What did *this one commit* change? | `git show <id>` | click a commit in the history/timeline |
| What changed between two commits? | `git diff <old-id> <new-id>` | compare in the timeline |

### Detective questions
History lets you answer questions that were impossible with `final_final_v3`:

- *When* did the momo paragraph appear? → find the commit whose diff adds it, read its date.
- *Who* wrote the title? → the author of the commit that added it.
- *Why* was the opening line changed? → read that commit's message.

(In Grade 12 you will learn `git blame`, which answers "who last changed this line?" for every line at once.)

## See it
Find the commit that brought the typo *modals*:

```console
$ git log --oneline
...
711a420 Add Class Eight momo paragraph (typo left in on purpose)
...
$ git show 711a420
commit 711a420055201db8271b5be81c7b6dd2243f5084
Author: Teacher <teacher@example.invalid>
Date:   Mon Oct 5 10:00:00 2026 +0545

    Add Class Eight momo paragraph (typo left in on purpose)

diff --git a/article.md b/article.md
@@ -1,5 +1,7 @@
 # Our School Festival

-The festival is held every year in the school ground. Students sing, dance and show science models.
+The festival is held every year in the school ground. Students sing, dance and show science modals.

 The best part is the food stalls. Each class sells one snack and the money buys books for the library.
+
+Class Eight made momo and sold forty plates.
```

*Who:* Teacher. *When:* 5 October. *What:* the momo paragraph, and — sneakily — the typo. *Why:* the message (it even admits the typo). If you work on a computer where your commit ids are different, use the ones your `git log` shows.

## Unplugged: spot the difference (15 min)
Pairs get two printed versions of the same paragraph (`article.md` at commit 2 and commit 5 — the files `versions/v2.md` and `versions/v5.md` in the practice repo).

1. With a **red pen**, cross out every word that was removed. With a **green pen**, underline every word that was added.
2. Now redo it *Git's way*: write the diff as lines, putting `-` before each old line and `+` before each new line.
3. Compare with another pair. Did you find the same changes? Did anyone find *modals*?
4. Discuss: what is easier — checking word by word, or the line-by-line diff?

## PRIMM lab (40 min)
Repo: `g08-class-magazine` (the starter repo already has 6 commits). Pairs, driver/navigator.

1. **Predict:** look at the list of messages in `git log --oneline` (or the History view in VS Code / GitHub Desktop). Which commit added the paragraph about food stalls? Write the id.
2. **Run & investigate:** open that commit. Red lines = removed, green lines = added. Does it match your prediction?
3. **Investigate more:** for each of the 6 commits, fill this table in your notebook:

    | id | author | date | message | lines added | lines removed |
    |---|---|---|---|---|---|

    *Tip:* `git log --stat` shows how many lines each commit changed.

4. **Investigate:** the typo *modals* was fixed later. Which commit fixed it? Does its message say so? *(It does not! What does this teach about one idea per commit and honest messages?)*
5. **Modify:** make a new edit that changes one word. **Before you commit**, open the diff (`git diff` or click the file) and describe it in your notebook in your own words.
6. **Make:** write a commit message that matches *exactly* what your diff shows. Commit. Swap seats with another pair: can they tell from your message alone what the diff will show? Check with `git show`.

Command-line (optional):

```bash
git log --oneline
git show <commit-id>
git diff
git log --stat
```

`git diff` shows changes you have not committed; `git show` shows what one commit changed.

## Parsons practice (10 min)
Match each description to a command: *list the history* · *what did this commit change?* · *what have I changed since the last commit?* · *how many lines did each commit change?*
Commands: `git show <id>` · `git log --stat` · `git diff` · `git log --oneline`.

## Common mistakes
| Symptom | Cause | Fix |
|---|---|---|
| `git log` fills the screen and you cannot type | it opened a *pager* (a page viewer) | press **space** for the next page, **q** to quit |
| `git diff` shows nothing | there are no uncommitted changes, *or* your changes are already staged | use `git diff --staged` for staged changes, or `git show` for a commit |
| "The diff shows the whole paragraph changed for one word" | Git compares whole lines; a paragraph is one long line | look for the word inside the line; in Grade 9 you can use `git diff --word-diff` |
| Confusing `-` and `+` | — | `-` = old/removed, `+` = new/added; think "minus = taken away" |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Software Carpentry [**Exploring History**](https://swcarpentry.github.io/git-novice/05-history.html): read the first part about `git diff HEAD~1`. In our practice repo, run `git diff HEAD~1` and `git diff HEAD~2`. What does `~1` mean? | 1 / 3 | 15 min | one sentence explanation |
| 2 | *Pro Git* [§2.3 **Viewing the Commit History**](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History): try three options from its table (`--stat`, `--since`, `--author`) on the practice repo. | 1 / 3 | 15 min | the 3 commands and what they showed |
| 3 | **Diff detective (paper):** your teacher prints `versions/v3.md` and `versions/v4.md`. Write the diff by hand with `+` and `-`, then check it on a computer with `git diff b16c8b6 53bf9f6` (ids may differ). | 0 / 1 | 15 min | hand-written diff |
| 4 | In VS Code, open the **Timeline** for `article.md` and click two different commits. Take a screenshot (or draw) of one diff and label the old and new sides. | 1 | 10 min | labelled picture |

## Exit ticket (5 min)
1. What do red and green (or `-` and `+`) lines mean in a diff?
2. Name two pieces of information a commit stores besides the file changes.
3. *Misconception check:* "A diff shows the whole file." (No — only the lines that differ, plus a few lines of context.)

## Key points
- The **history/log** lists commits newest first: id, author, date, message.
- A **diff** shows only changed lines: `-` removed, `+` added, space = context.
- Git compares **lines**, not words.
- `git diff` = my uncommitted changes · `git show <id>` = one commit · `git log --stat` = size of each commit.
- Good messages make history readable; a message that hides a change (like the typo fix) misleads future readers.

## New words
**log**, **diff**, **context line**, **`git show`**, **`git diff`**, **pager** — see the [glossary](../../glossary.md).

## Extension quest
Find the commit where *modals* was misspelled and the commit where it was fixed. Write a better message for the fixing commit — or explain why it should have been two separate commits.
