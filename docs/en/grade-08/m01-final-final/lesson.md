---
id: g8-m01-final-final
grade: 8
hours: 1
prerequisites: []
outcomes:
  - "Describe the problem with keeping versions by renaming files"
  - "Say what a 'version history' should record: what, when, who, why"
  - "Explain in one sentence what a version control system does"
tier_support: [0, 1, 2, 3]
license: CC-BY-4.0
---

# 1. The `final_final_v3` problem

!!! abstract "At a glance"
    **Time:** 1 period (40 min) · **Tiers:** 0–3 (fully unplugged) · **You need:** a printed paragraph per group, blank A4 sheets, pens

    **Before this:** nothing — this is the first lesson of the whole book.

    **By the end you can:** explain why renaming files is a poor way to keep versions; list what a good history must record; say what a version control system is.

## Hook (5 min)
Your teacher shows this folder on the board. It is a real kind of folder; most people have one.

```
essay.doc
essay_new.doc
essay_final.doc
essay_final_final.doc
essay_final_v3_REAL.doc
essay_final_v3_REAL_sir_checked.doc
```

Answer without opening any file:

- Which one should I hand in?
- Which one did Sir correct?
- What changed between `essay_new` and `essay_final`, and *why*?

You cannot answer. That is the problem this whole book solves.

## Understand it

### What is a "version"?
A **version** is the state of your work at one moment. When you write an essay, you make many versions: the first rough draft, the draft after a friend's comments, the draft after the teacher's corrections. Every version is a little different from the one before.

Keeping versions is useful. You might:

- want an **old paragraph back** that you deleted last week;
- need to **show your teacher what changed** after their comments;
- want to know **who** changed something in a group project, and **why**;
- want to **try a risky idea** without losing the work that already works.

### The renaming method and why it fails
Most people keep versions by saving a copy under a new name: `essay_final.doc`, `essay_final_final.doc`, and so on. This feels safe, but it breaks in at least six ways:

| Problem | What happens |
|---|---|
| **No order** | Is `final_v3` newer than `final_final`? Names do not say. You guess from the "date modified", which changes if you just open and save. |
| **No reason** | Nothing records *why* a copy was made. "REAL" is not a reason. |
| **No difference** | To see what changed, you must open two files side by side and read every line. |
| **Easy to overwrite** | One wrong "Save" over the wrong copy and a version is gone for ever. |
| **No "who"** | In a group, you cannot tell who wrote which part. |
| **Wasted space and confusion** | Six full copies of the same essay. Multiply by every subject and every student. |

When two people work on the same file, it becomes worse: Sita has `report_sita.doc`, Ram has `report_ram_edited.doc`, and someone must combine them by hand, line by line.

### What a good history records
Think of a careful shopkeeper's **khata** (account book). Every line records *when* something happened, *what* happened, *who* did it, and often *why* ("credit to Hari dai until Friday"). Nobody tears out old pages; mistakes are corrected with a new line. Because the old lines stay, the shopkeeper can always answer "how did we get here?".

A good history of your work needs the same four things:

1. **What** changed — exactly which words or lines.
2. **When** — the date and time.
3. **Who** — the person who made the change.
4. **Why** — a short message in plain words.

…and one power that a khata does not have: **go back** — bring back any earlier version in seconds.

### Version control systems
A **version control system** is a program that keeps this history for you. Instead of copies with strange names, you keep **one** folder. Whenever you reach a good point, you tell the program "remember this, and here is why". Later it can show you the whole history, the exact difference between any two moments, and give you back any old version.

The version control system used by almost every software team, many writers and many scientists in the world is called **Git**. It is free and open source, works without the internet, and runs on old computers too. Over the next five years you will learn it step by step: first as a time machine for your own work (Grade 8), then for sharing work (Grade 9), for teams (Grade 10), for open-source projects (Grade 11) and for professional engineering (Grade 12).

```
  Without version control              With version control (Git)
  -----------------------              --------------------------
  essay.doc                            essay.doc   <- one file
  essay_new.doc                          history:
  essay_final.doc                          5 Oct  Fix spelling after Sir's comments   (Sita)
  essay_final_final.doc                    3 Oct  Add conclusion                      (Sita)
  essay_final_v3_REAL.doc                  1 Oct  First draft of introduction         (Sita)
```

## Unplugged: the folder game (15 min)
**Groups of 4.** Each group gets a printed paragraph (6 lines, for example a short school notice).

1. **Round 1–4 (2 min each):** the group makes one edit (change a word, add a line, remove a line). After each edit, copy the *whole* paragraph onto a **new** sheet and give it a file name the way people usually do (`notice_new`, `notice_final`, …). Never change an old sheet.
2. Put all sheets in a pile and shuffle them.
3. The teacher secretly asks one group at a time: *"Go back to the version before the third edit."* Time how long it takes.
4. Then: *"What changed in the second edit, and why did you make it?"*

**Discuss as a class:**

- How long did it take to find the right sheet? Did anyone pick the wrong one?
- Could you tell *what* changed without reading both sheets word by word?
- Did any sheet say *why* the edit was made? *When*? *Who* made it?
- What would you add to each sheet to make the game easy? (Students usually invent: a number, a date, a name and a reason — exactly what Git records.)

## Think (PRIMM — Predict) (10 min)
1. **Predict:** 30 students each keep 6 copies of 5 assignments. How many files is that? *(30 × 5 × 6 = 900.)*
2. **Predict:** two people both edit `report_final.doc` on different computers and both save. What happens when they bring their files together? *(Two different files that must be combined by hand; one person's work is easily lost.)*
3. **Investigate:** look at your own computer, phone or Google Drive at home. Do you have a `final_final`? (Describe it tomorrow — don't bring the file.)

## Key idea (5 min)
A good history records **what** changed, **when**, **who** changed it and **why**, and it lets you **go back**. File names cannot do that. A version control system such as **Git** does.

## Common mistakes
| What students say | Better thinking |
|---|---|
| "I just press Ctrl+Z." | Undo disappears when you close the file or the power goes; a history must survive for months. |
| "I keep everything in Google Drive, so it's safe." | Drive keeps *copies*; it does not say why something changed, and in a group it cannot combine two people's edits line by line. |
| "Version control is only for programmers." | Writers, scientists, lawyers, designers and governments use it; you will use it for an essay first. |
| "A longer, more careful file name fixes it." | Names cannot show differences or reasons, and can still be confused. |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Read the short page **"About Version Control"** in the free book [*Pro Git*, §1.1](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) (teacher can read it aloud or print one page for class use). Find the three kinds of version control it describes and draw a picture of one. | 0 (printed) / 3 | 15 min | drawing + 2 sentences |
| 2 | Look at the Jorge Cham comic "FINAL.doc" in Software Carpentry's [**Automated Version Control**](https://swcarpentry.github.io/git-novice/01-basics.html) episode. Write your own Nepali-context version of the comic in 4 boxes. | 3 (or teacher shows it on one screen) | 20 min | 4-box comic |
| 3 | Open [Learn Git Branching](https://learngitbranching.js.org/?locale=en_US&level=intro1) (self-hosted copy in the lab, Tier 1). Don't type anything yet — just watch the demo of the first level. What do you think the circles are? | 1 / 3 | 5 min | one guess, written down |
| 4 | **Family interview:** ask an adult how they keep old versions of important papers (land records, shop accounts, letters). What do they record? Compare with *what, when, who, why*. | 0 | homework | 5 lines |

## Exit ticket (5 min)
1. Name one problem with `final_final_v3`.
2. What four things should a history record?
3. *Misconception check:* "A bigger file name like `essay_final_v3_REAL` is a good version system." True or false? Why?

## Key points
- Renaming copies gives no order, no reason, no difference, no "who", and is easy to overwrite.
- A good history records **what, when, who, why**, and lets you go back.
- A **version control system** keeps that history for you in one folder.
- **Git** is the most widely used, free and open-source version control system, and works offline.

## New words
**version**, **history**, **version control system**, **Git** — see the [glossary](../../glossary.md).

## Extension quest
Design a better "khata" for your essay on paper: a table with columns you think a history needs. Keep it — in Module 2 you will compare it with what Git really stores.
