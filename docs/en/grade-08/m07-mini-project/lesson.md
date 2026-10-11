---
id: g8-m07-mini-project
grade: 8
hours: 2
prerequisites: [g8-m05-undo-restore, g8-m06-stats-commits]
outcomes:
  - "Keep a real piece of writing under version control for several days"
  - "Present the history of the work and explain key commits"
tier_support: [0, 1, 2, 3]
license: CC-BY-4.0
---

# 7. Mini-project: Class Magazine

!!! abstract "At a glance"
    **Time:** 2 periods + work at home or in free lab time over at least 3 sessions · **Tiers:** 0–3 · **You need:** a repo (Tier 1+) or a stack of commit cards (Tier 0)

    **Before this:** Modules 1–6.

    **By the end you can:** keep a real piece of writing under version control over several days, use restore or revert on purpose, and present how your work grew.

Each student keeps **one article** (a poem, a school news item, a description of a local festival, a recipe from home, a short report on a science model) under version control. At the end the class holds an **exhibition** of the "evolution" of each article: not only the final text, but *how it was made*.

## Why a project?
Everything so far was practice on someone else's article. Now it is your own work, over several days — exactly how real people use version control. You will find out for yourself why small commits and good messages matter, because *you* will be the one reading your history.

## The brief
- Choose a topic from the school or community. **Do not include real names of classmates**, phone numbers or addresses; use roles ("the captain", "our neighbour").
- Make a repo: copy `practice-repos/g08-class-magazine` and replace `article.md` with your own text, or create a new folder and *Initialize Repository* (Tier 1+). Tier 0: a card stack.
- Write the article in at least **5 commits** over at least **3 sessions**.
- Include at least one **restore or revert**, on purpose, with a message that says why.
- Draw the commit-count chart from Module 6.
- Prepare a 2-minute explanation for the exhibition.

## Suggested shape of a good history
```
c1  Add working title and three ideas for the article
c2  Write first paragraph about where the festival happens
c3  Add paragraph about the food
c4  Change opening line after partner's feedback
c5  Revert "Add joke in the conclusion" — it was unkind
c6  Fix spelling of Janakpurdham and Mithila
c7  Add closing sentence
```
Notice: each commit is one idea; the messages tell a story; feedback and the revert are visible.

## Plan
| Stage | Time | What |
|---|---|---|
| Choose and plan | 10 min | topic, 3 bullet ideas, first commit |
| Draft | 1 period + home | first version, commits 2–3 |
| Peer feedback | 10 min | swap with a partner; partner reads your **history first**, then the text, and writes 2 suggestions on paper |
| Improve | 1 period | commits 4–5+, one restore or revert |
| Chart | 10 min | commit chart from Module 6 |
| Exhibition | 20 min | show `git log` (or card stack), one diff, one chart; explain a key commit |

## Peer-feedback questions (for your partner)
1. Reading only the messages, can you tell how the article grew?
2. Is any commit doing two things at once?
3. One thing you liked in the text; one suggestion.

## Exhibition checklist
- [ ] My history (`git log --oneline` printed or written, or my card row).
- [ ] One diff I am proud of — I can explain the red and green lines.
- [ ] My restore or revert, and *why* I did it.
- [ ] My chart, titled and labelled.
- [ ] The final article.

## Rubric (commit-history rubric)
| Criterion | 3 | 2 | 1 |
|---|---|---|---|
| Number of commits | ≥ 5 | 3–4 | 1–2 |
| Messages | each says what + why | most do | vague ("done") |
| One idea per commit | yes | mostly | no |
| Restore/revert used | with explanation | used | not used |
| Oral explanation (2 min) | clear | partly clear | unclear |
| Chart | correct and labelled | minor errors | missing |

Maximum 18 points.

## Common mistakes
| Mistake | Fix |
|---|---|
| All commits in one session, minutes apart | spread work over ≥ 3 sessions |
| Writing everything, then committing once | commit after each paragraph |
| Names, phone numbers or addresses of real people | remove them; use roles |
| Forgetting the restore/revert | plan it: write a sentence you will revert on purpose |
| Messages like "update" | use the Module 2 message rules |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Before you start, play [Learn Git Branching `intro1`](https://learngitbranching.js.org/?locale=en_US&level=intro1) once more and draw the history you *plan* for your article (5–7 circles with messages). Compare it with the real history at the end. | 1 / 3 | 10 min | plan vs real drawing |
| 2 | Write your article in **Markdown** (headings with `#`, *italics* with `*`). Use the [CommonMark 10-minute tutorial](https://commonmark.org/help/tutorial/) (teacher can print the reference card, or use it at home with internet). | 1 / 3 | 15 min | article with ≥ 2 Markdown features |
| 3 | **Badges:** create `BADGES.md` in your repo and record the badges from the [Grade 8 cards page](../cards.md) you earned this chapter — commit it! | 1 | 5 min | `BADGES.md` commit |

## Exit ticket (5 min)
Which commit are you proudest of, and what does its message say?

## Key points
- Version control is most useful on *your own* work over *several days*.
- Small commits + clear messages = a history that tells a story.
- Undo (restore/revert) is a skill, not a failure.
- Private information never goes into a repo.

## Extension quest
Compare two classmates' histories of different topics: whose is more detailed? What makes a history useful to a reader?

---

**Chapter complete.** You can now keep your own work's history. In Grade 9 you will use Git from the **terminal**, learn **branches** (try two ideas at once) and send your work to another computer with **remotes**.
