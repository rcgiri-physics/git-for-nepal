---
id: g8-m02-snapshots
grade: 8
hours: 2
prerequisites: [g8-m01-final-final]
outcomes:
  - "Explain a commit as a snapshot with a message"
  - "Draw a history of commits in order, each pointing to its parent"
  - "Write a message that says what and why"
tier_support: [0, 1, 2, 3]
license: CC-BY-4.0
---

# 2. Snapshots = commits

!!! abstract "At a glance"
    **Time:** 2 periods · **Tiers:** 0–3 (unplugged core; computer optional) · **You need:** 8 index cards per pair, string or a pen to draw lines, pens

    **Before this:** Module 1 (why renaming fails).

    **By the end you can:** explain what a commit is; draw a history where each commit points to its parent; write a clear commit message.

## Hook (5 min)
A builder in your town takes a photo after every stage of building a house: foundation, first floor walls, roof, paint. Months later the owner asks, "Where exactly are the water pipes in the wall?" The builder opens the photo from the "walls" stage. Nothing was lost, because every stage was **photographed and labelled**.

A **commit** is a photo of your whole project plus a note.

## Understand it

### A commit is a snapshot
When you **commit**, Git takes a **snapshot**: a complete picture of every file in your project *at that moment*. It also writes down:

| Part of a commit | Example | Answers the question |
|---|---|---|
| a **message** | `Add second verse about the river` | *why / what* |
| the **author** | `Student 07` | *who* |
| the **date and time** | `5 Oct 2026, 10:00` | *when* |
| the **parent** | "the commit before me is c2" | *what came before* |
| a **commit id** | `78a873e` | a unique name for this snapshot |

Do you remember the four things from Module 1 — what, when, who, why? A commit records all four, plus a link to the commit before it.

### Snapshots, not just changes
It is natural to think a commit stores only "the line I changed". It does not: each commit is a **whole picture** of the project. Git is clever about space — if a file did not change, the new snapshot simply *points to* the old copy instead of storing it again — but in your head you should think *"each commit = the complete project at that moment"*. That is why you can jump back to *any* commit and get everything exactly as it was.

### History is a chain
Every commit (except the very first) remembers its **parent**, the commit that came just before it. Following the parents backwards gives you the **history**, oldest to newest:

```
  c1  <---  c2  <---  c3  <---  c4
 "Write    "Add      "Fix      "Add
  title"    verse 1"  spelling" verse 2"
                                  ^
                                 newest
```

The arrows point *backwards* because each commit knows its parent, but a parent does not know its future children. You will see this again in Grade 9 when we learn branches.

### Commit ids
Git names each commit with a long code such as `78a873e8c1…`. It is calculated from the commit's content, so two different commits can never have the same id. People usually use the first 7 characters (`78a873e`). You never need to remember them — you copy them when you need one.

### Writing good messages
The message is the part a future reader (often *you*, three months later) relies on. A good message:

- starts with a **verb** in the present tense: *Add*, *Fix*, *Remove*, *Change*, *Move*;
- says **what** changed and, if it is not obvious, **why** — in one short line (about 50 characters);
- describes **one idea**. If you need the word "and" twice, it was probably two commits.

| Weak message | Why it is weak | Better message |
|---|---|---|
| `stuff` | says nothing | `Add paragraph about food stalls` |
| `fix` | fix what? | `Fix spelling of Bhaktapur` |
| `final` | every commit is "final" for a moment | `Add closing sentence` |
| `changed lots of things and fixed typo and new title` | three ideas in one | three commits: `Fix typo…`, `Change title…`, `Add…` |

### When should you commit?
Commit when you reach a **small, complete step** you might want to return to: a paragraph is finished, a mistake is fixed, a new section is added. Not after every word (too many), and not once at the end of a week (too few — you cannot go back to the middle).

## See it
On a computer, after three commits, the history looks like this (from the practice repo; Module 3 shows you how to make it). Newest is at the top:

```console
$ git log --oneline
b16c8b6 Say where the festival is and what happens
78a873e Add better title and opening line
d38a483 Add working title
```

Each line is one card from today's game: an id, then the message. Your ids will be different — that is normal.

## Unplugged: the paper-commit game (25 min)
**Materials:** index cards, string, pens. Pairs.

1. Each pair writes a 4-line poem about their village or school on a sheet. This sheet is the **working copy** — the thing you are editing.
2. **Make a commit:** copy the *whole sheet* onto an index card. At the top write a short message (*what + why*), e.g. `Add first two lines`. Number it `c1`. Write your pair name as author and today's date.
3. Edit the sheet (add a line). Make card `c2` with its message. On `c2` write **parent: c1**, and connect the cards with string (or draw an arrow from `c2` back to `c1`).
4. Keep going until you have four commits. Lay the cards in a row. This row is the **history** — what `git log` shows.
5. **Swap** cards with another pair. Answer *only from their cards*: What changed between `c2` and `c3`? Why? Who? When?
6. Give the other pair one piece of feedback on their messages.

### Rules of a good message
- Starts with a verb: "Add", "Fix", "Remove".
- Says *what and why* in one line.
- One idea per commit.

## Predict (PRIMM) (10 min)
1. **Predict:** your teacher shows 3 cards with messages `stuff`, `fix`, `final`. Can you tell what changed in each? What would you need to do to find out?
2. **Run:** now look at 3 cards: `Add title`, `Fix spelling of Bhaktapur`, `Add third verse`. Can you tell now?
3. **Investigate:** which set would help a teacher, a partner or *you in three months*? Why?
4. **Modify:** rewrite the three weak messages so that they are useful (look at the cards' contents).

## Parsons practice (10 min)
Put these commits in order to make a sensible history, using the messages as clues:
*Write title · Add first verse · Fix spelling · Add second verse*.
Then draw the parent arrows.

## Common mistakes
| Mistake | Why it is a problem | Fix |
|---|---|---|
| Copying only the changed line onto the card | A commit is the *whole* project; you could not go back to it alone | copy the whole sheet |
| Forgetting the parent | the history cannot be followed | always write "parent: c…" and draw the arrow |
| Rubbing out an old card to fix it | history is changed; the record is no longer true | make a **new** card that fixes it |
| One huge commit at the end | cannot go back to the middle | commit after each small step |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | [Learn Git Branching, level `intro1` "Introduction to Git Commits"](https://learngitbranching.js.org/?locale=en_US&level=intro1). Type `git commit` twice to finish the level. Then type `undo` and try again slowly, watching each new circle appear with an arrow to its parent. | 1 (self-hosted) / 3 | 10 min | a drawing of the final graph |
| 2 | In the same tool type `sandbox`, then `git commit` five times. Draw what you see. Which circle is the newest? Which way do the arrows point, and why? | 1 / 3 | 10 min | drawing + 1 sentence |
| 3 | **Message makeover:** your teacher gives 10 weak messages (see the teacher guide). Rewrite each as a good one-line message. | 0 | 15 min | list of 10 |
| 4 | Read [*Pro Git* §1.3 "What is Git?"](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F), the part about "Snapshots, Not Differences" (teacher may read aloud). Explain the house-photo idea to a family member. | 3 (or read aloud) | 15 min | 3 sentences |

## Exit ticket (5 min)
1. What is a commit?
2. Write a good message for adding a heading to an essay.
3. *Misconception check:* "Git automatically saves every keystroke." True or false? (False — only when you commit.)

## Key points
- A **commit** is a snapshot of the whole project plus a message, author, date, parent and id.
- The **history** is a chain of commits, each pointing back to its parent.
- Good messages start with a verb, say what and why, and describe one idea.
- Commit after each small, complete step.
- Never change an old commit to fix a mistake; add a new one.

## New words
**commit**, **snapshot**, **working copy**, **message**, **parent**, **commit id**, **history / log** — see the [glossary](../../glossary.md).

## Extension quest
Make the cards for a *wrong* edit (for example a line in the wrong place) and add a new commit that fixes it, instead of rubbing out an old card. History is never rewritten here — this prepares Module 5.
