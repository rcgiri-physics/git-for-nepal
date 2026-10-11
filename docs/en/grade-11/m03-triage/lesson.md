---
id: g11-m03-triage
grade: 11
hours: 1
prerequisites: [g11-m02-reading-a-project]
outcomes:
  - "Choose an issue that fits your skills"
  - "Ask a clarifying question politely"
  - "Claim an issue and post a plan"
tier_support: [0, 2, 3]
license: CC-BY-4.0
---

# 3. Triage: finding a good first issue

!!! abstract "At a glance"
    **Time:** 1 period · **Tiers:** 0 (printed issues), 2–3 · **You need:** 10 prepared issues in the curriculum repo (labels `good-first-issue`, `student-friendly`)

    **Before this:** Module 2.

    **By the end you can:** judge an issue's size and clarity, pick one you can finish, ask a good question, and claim it properly.

## Hook (5 min)
A list of 40 issues. Some are one-line typo fixes; some would take a professional a month. Which one can *you* finish in two lessons — and how do you know?

## Understand it

### What triage means
**Triage** (from hospitals: deciding who to treat first) means sorting issues: *is it clear? how big? who should do it? how urgent?* Maintainers triage all the time; as a newcomer you triage to **choose well**.

### Rate an issue
| Question | Signs it's a good first issue |
|---|---|
| **Size** — S / M / L? | **S**: one file, a few lines |
| **Clarity** — do I know what "done" looks like? | clear steps or a "done when" list |
| **Skill** — do I know the tools? | Markdown, text, a small script change |
| **Pointer** — does it say *where*? | names the file or line |
| **Free** — is anyone else working on it? | no assignee, no recent "I'm on it" comment |
| **Alive** — will someone review it? | maintainers replied recently |

Labels like **`good first issue`**, **`good-first-issue`**, **`beginner`**, **`help wanted`** and (in this repo) **`student-friendly`** are set by maintainers to point newcomers to suitable tasks.

### Ask before you start
Always comment before starting work. It avoids two people doing the same thing, and lets the maintainer correct your plan *before* you spend time:

> Hello! I'm a Grade 11 student and would like to work on this. My plan: (1) fix the three spellings in `docs/en/grade-09/m03-branches/lesson.md`, (2) check the glossary for the same words, (3) open a PR that closes this issue. Is that OK?

A good question is **specific** and shows you have read the issue: *"Should the Nepali word go in the glossary table only, or also in the lesson?"* — not *"how do I do this?"*.

Wait for a "go ahead" (or a day or two with no objection, if CONTRIBUTING says so).

### Quality over quantity
Events like **Hacktoberfest** count pull requests, and some people respond by sending many tiny, useless PRs ("spam PRs"). This wastes maintainers' time and harms the project. Our class rule: **one good, useful contribution is worth more than ten trivial ones** — and we contribute only to listed, vetted projects.

## See it
A good claim and a maintainer reply:

```
#23  Fix "Libary" typo and broken link on Grade 10 static-site page   [good-first-issue]

  student-17:  Hi! May I work on this? I'll fix the typo on line 40 and the link
               to cards.md, run check_links.py, and open a PR with "Closes #23".
  maintainer:  Thanks! Go ahead. The link should point to ../../grade-08/cards.md.
               I've assigned it to you.
```

## Unplugged: issue rating (15 min)
Print 10 issues (see teacher notes) on cards. Pairs rate each: **size** S/M/L, **clarity** 1–3, **skill needed**, **predicted time**. Then each pair "claims" one issue by writing a claim comment on a sticky note. The teacher plays maintainer and replies.

## PRIMM lab (20 min)
1. Teacher prepares 10 issues in the curriculum repo (labels `good-first-issue`, `student-friendly`).
2. Rate each on a sheet; **predict** the time to finish.
3. **Investigate:** filter the issue list by label (most hosts: click the label, or search `label:good-first-issue is:open`).
4. Claim one by commenting. Wait for a maintainer's "go ahead".
5. **Make:** write your plan in 3 steps in the issue.

## Parsons practice (5 min)
Order: *read issue · ask question · comment "I'll work on this" · branch · PR*.

## Common mistakes
| Mistake | Fix |
|---|---|
| Starting work on an issue someone already claimed | read the comments first |
| Picking the biggest issue to impress | pick one you can finish; then a bigger one |
| "Can I work on this?" — then silence for weeks | post progress, or say you've stopped so others can take it |
| Vague questions | quote the line you're unsure about |
| Opening a PR with no issue in a project that requires one | check CONTRIBUTING |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Open Source Guides, [**How to Contribute**](https://opensource.guide/how-to-contribute/) — "Finding a project to contribute to" and its checklist. Apply the checklist to one project. | 3 | 20 min | checklist |
| 2 | [First Contributions](https://firstcontributions.github.io/) has a list of projects with beginner-friendly issues. Pick two and rate one issue from each. | 3 | 20 min | ratings |
| 3 | [Hacktoberfest](https://hacktoberfest.com/): read the current rules about quality and spam. Write our class's 3 rules for events. | 3 | 15 min | 3 rules |
| 4 | Write a "good first issue" yourself for this book (a typo, a missing glossary word) — with title, what, why, done-when. | 2 / 3 | 15 min | issue |

## Exit ticket (5 min)
1. What makes an issue "good first"?
2. Why comment before starting?
3. *Misconception:* "Bigger issues are always better."

## Key points
- **Triage** = judge size, clarity, skill, pointer, availability, activity.
- Beginner labels point to suitable issues.
- Comment a specific plan before starting; wait for a go-ahead.
- Quality over quantity; no spam PRs.

## New words
**triage**, **good first issue**, **help wanted**, **claim**, **spam PR** — see the [glossary](../../glossary.md).

## Extension quest
Find an old, unanswered issue in this repo. Can you add useful information to it (steps to reproduce, a file reference) without solving it? That is triage work too.

## Teacher notes
- **Timing:** hook 5 · understand 10 · rating 10 · lab 15 · Parsons + exit 5.
- **Avoid spam:** no one opens PRs for points or events. Hacktoberfest-style events: set rules (quality over quantity, only listed repos).
- **Prepare 10 issues** (mix of sizes): typos in a lesson, a missing glossary word, a broken relative link, a better Nepali-context example, an exercise answer missing from a teacher guide (S); a new Parsons card set (M); a new practice repo (L — to show what *not* to pick first).
- Act as a kind, prompt maintainer during the lab: reply within the lesson.
- **Answer key:** Exit 1: small, clear, says where, labelled, unclaimed, project responsive. 2: avoids duplicate work and gets feedback on the plan. 3: False — finishing a small useful one is better.
