# Grade 11 — Open-Source Contributor

!!! warning "Unpiloted draft"
    Core lessons are written but have not been tried in a classroom. Grade placement of topics is unverified against the CDC syllabus (see `research/decisions.md`).

!!! info "CDC fit (verified)"
    The CDC Grade 11–12 curriculum lists, for Unit 4 Web Development, a group web-app activity "using GitHub for version control". Modules 4–6 and 8 support that activity directly.

**Big idea:** you can improve software and knowledge that others also use.
**Length:** ≈ 20 periods (to calibrate to CDC hours).
**Accounts:** Learners 13+ with teacher oversight; contribute only to vetted projects.
**Tools:** Git, GitHub/Codeberg/Forgejo, the curriculum repo itself, partner projects with consent.

## How this chapter is built
Grades 8–10 happened inside the classroom. Grade 11 steps **outside**: other people's projects, other people's rules, and real open data. It also adds the "sharp tools" (rebase, reset, reflog) once students have the judgement to use them safely.

```
 M1  licences                (may I?)
 M2  read a project          (how do they work?)
 M3  triage                  (what can I do?)
 M4  first PR                (contribute)
 M5  rebase/stash/reset      (sharp tools, safely)
 M6  conventions             (shared habits)
 M7  process models          (why teams work so)
 M8  data project            (real data)
```

## Modules
| # | Module | Periods | Tiers | Key ideas |
|---|---|---|---|---|
| 1 | [Licences and attribution](m01-licences/lesson.md) | 2 | 0–3 | CC BY, MIT, GPL, TASL credit |
| 2 | [Reading a project](m02-reading-a-project/lesson.md) | 1 | 1–3 | README, CONTRIBUTING, `git grep` |
| 3 | [Triage: a good first issue](m03-triage/lesson.md) | 1 | 0, 2–3 | size, clarity, claiming |
| 4 | [Your first PR](m04-first-pr/lesson.md) | 2 | 2–3 | fork → PR → review |
| 5 | [rebase, stash, revert, reset](m05-rebase-stash-revert/lesson.md) | 2 | 0–3 | golden rule, reflog |
| 6 | [Commit and branch conventions](m06-conventions/lesson.md) | 1 | 0–3 | message body, Conventional Commits |
| 7 | [Process models and Git workflows](m07-process-models/lesson.md) | 2 | 0–3 | waterfall, Scrum, XP |
| 8 | [Data project](m08-data-project/lesson.md) | 3 | 1–3 | raw/clean, DATA.md |

## Chapter outcomes
1. explain common open licences and credit sources correctly
2. find an appropriate first issue
3. open a pull request to an open project
4. use stash, rebase, revert and reset with care
5. write clear conventional messages
6. version and document a dataset

## Free resources used in this chapter
[First Contributions](https://firstcontributions.github.io/), [Open Source Guides](https://opensource.guide/), [choosealicense.com](https://choosealicense.com/), [Creative Commons](https://creativecommons.org/licenses/by/4.0/), [SPDX](https://spdx.org/licenses/), [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), [*Pro Git*](https://git-scm.com/book/en/v2) chapters 3, 5–7, Learn Git Branching's rebase and cherry-pick levels, [The Turing Way](https://book.the-turing-way.org/reproducible-research/vcs) and Software Carpentry's licensing, open-science and citation episodes. Full list: [free resource library](../book/resources.md).

## Assessment
Portfolio (`CONTRIBUTIONS.md`), reflection, viva on a PR the student reviewed. First-draft item bank: `assessments/g11-item-bank.md` (to be reviewed after Pilot 1).

## Capstone
A merged contribution and a `CONTRIBUTIONS.md` portfolio. Contribution targets: this curriculum repo first; **3–5 partner projects are still to be agreed with maintainers' consent** (FOSS Nepal, NOSK, Open Knowledge Nepal, Code for Nepal are candidates — not yet contacted).


## Ready for Grade 12?
A student is ready when they can, without help: credit a CC BY source correctly; open a PR to a project that follows its CONTRIBUTING rules; choose revert vs reset by asking "is it pushed?"; and recover a commit with `reflog`.
