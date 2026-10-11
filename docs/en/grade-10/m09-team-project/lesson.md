---
id: g10-m09-team-project
grade: 10
hours: 3
prerequisites: [g10-m08-ci-intro]
outcomes:
  - "Work in a team of 3–4 with issues, PRs and review"
  - "Release and publish a website (or Python app)"
  - "Reflect on the team process in a retrospective"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 9. Team project: Our School Website

!!! abstract "At a glance"
    **Time:** 3 periods over about 3 weeks (+ work between) · **Tiers:** 1–3 · **You need:** a team repository on the class server, the `g10-school-website` starter

    **Before this:** Modules 1–8.

    **By the end you can:** run a small real project as a team — plan with issues, build with branches and PRs, review every change, release, publish, and reflect.

## Hook (5 min)
The principal wants a school website for the festival. You have **3 weeks** and **4 team members**. Last year's team ended up with three "About" pages and a broken menu on the big day. This year you will use everything from this chapter.

## Understand it

### Team charter
Before writing code, write down how you will work. A **team charter** (`CHARTER.md`, committed in week 1) is the Grade 9 working agreement grown up:

```markdown
# Team charter — Team 3
## Roles (rotate each week)
- Lead: keeps the board up to date, runs the weekly demo
- Reviewer: makes sure every PR gets a review within one day
- Tester: runs check.sh and opens every page before a release
- Writer: README, CHANGELOG, release notes
## Rules
- Every change goes through a PR with one approval from someone else.
- Branches: feature/<issue-number>-short-name, e.g. feature/7-gallery
- PRs say "Closes #N".
- We pull main at the start of every session.
- Meetings: Sunday and Wednesday, 10 minutes after class.
## Privacy
- No student names, photos, marks or phone numbers on the site.
```

**Roles** are hats, not jobs: *everyone* writes code and reviews; the role says who is responsible for making sure something happens.

### The team cycle
```
 issue -> branch -> commits -> PR -> CI ✓ -> review -> merge -> (weekly) demo -> (end) release
   ^                                                                      |
   +-------------------- new issues from feedback ------------------------+
```

### Weekly demo
Once a week, each team shows the class (3 minutes): the **board** (what is done, doing, to do), the **graph** (`git log --oneline --graph --all`), and the live site. Others give one compliment and one suggestion — which become new issues.

### Retrospective
At the end, the team answers three questions, honestly and without blame:
1. **What went well?** (keep doing)
2. **What was hard?** (change next time)
3. **What will we try next time?** (one concrete experiment)
Professional teams do this after every project; it is how teams get better.

### Evidence of your contribution
The history is the evidence: commits per person (`git shortlog -s -n`), PRs opened and reviewed, issues closed, review comments written. Every team member must be **visible** in it.

## Plan
| Week | Goals | Evidence |
|---|---|---|
| 1 | charter; ≥ 10 issues with labels and owners; skeleton pages | `CHARTER.md`, board |
| 2 | each member: ≥ 2 PRs merged with review; CI/check passing | PR list |
| 3 | release `v1.0.0`, publish, release notes, retrospective, viva | tag, live URL, `RETRO.md` |

## See it
A healthy team repository at the end of week 2 (summary):

```console
$ git shortlog -s -n
     9  Student 12
     8  Student 07
     7  Student 03
     6  Student 21
$ git log --oneline --merges | head -4
c1d0e9a Merge pull request #14 from team-3/feature/12-contact-hours
9ab33f2 Merge pull request #13 from team-3/feature/9-gallery
5e71b08 Merge pull request #11 from team-3/feature/8-menu-phones
2f4c6d1 Merge pull request #10 from team-3/feature/2-about
```

## Lab (3 periods)
1. **Issues → plan** (≥ 10 issues), charter, board.
2. Each member works on branches; **every change goes through a PR with one review**.
3. **Weekly demo:** show the board and the graph.
4. **Tag v1.0.0 and publish.** Write release notes.
5. **Retrospective:** `RETRO.md` with the three questions.

**Optional enrichment (Django):** teams that finish early may build a Django starter app in Git — Django is not confirmed in the CDC syllabus, so it is never required.
**Alternative project:** a small Python app (for example a quiz or a unit converter) with the same process.

## Parsons practice
Order the team cycle: *issue · branch · commits · PR · review · merge · demo*.

## Rubric
| Criterion | 4 | 3 | 2 | 1 |
|---|---|---|---|---|
| Individual commits (history) | ≥ 8, clear messages | 5–7 | 3–4 | < 3 |
| PRs authored, reviewed by others | ≥ 3 | 2 | 1 | 0 |
| Reviews given (quality of comments) | specific, kind, actionable | mostly | vague | none |
| Issues linked to PRs | all | most | some | none |
| Release | tag + notes + changelog | two of these | one | none |
| Published site works, `check.sh` passes | yes | minor issues | major issues | not published |
| Viva (3 min): explain one design decision and one review | clear | mostly | partly | unclear |

Maximum 28 points; the first three rows are **individual**, the rest are shared by the team.

## Common mistakes
| Problem | Fix |
|---|---|
| One person does everything, others "help" | issues assigned to everyone; rubric rows are individual |
| Huge PR the night before the deadline | small PRs from week 1 |
| PRs wait days for review | reviewer role: review within one day |
| Merged with failing checks | team rule: no merge on ✗ |
| Blame in the retrospective | talk about the process, not people |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Atlassian, [**Comparing workflows**](https://www.atlassian.com/git/tutorials/comparing-workflows): which workflow did your team use? | 3 | 15 min | answer |
| 2 | Open Source Guides, [**How to Contribute**](https://opensource.guide/how-to-contribute/): which habits would have helped your team? | 3 | 20 min | 3 habits |
| 3 | *Pro Git* [§5.3 **Maintaining a Project**](https://git-scm.com/book/en/v2/Distributed-Git-Maintaining-a-Project): read "Generating a Build" and "The Shortlog". Try `git shortlog v1.0.0..main`. | 1 / 3 | 15 min | output |
| 4 | Read another team's `RETRO.md`; write one suggestion for them. | 1 | 10 min | suggestion |

## Exit ticket
1. What did you learn about working in a team?
2. How can the teacher see your contribution?
3. *Check:* who reviewed your PRs?

## Key points
- A **charter** sets roles, rules and privacy before work starts.
- Issue → branch → PR → checks → review → merge; demo weekly; release at the end.
- The history is the evidence of each person's contribution.
- **Retrospectives** turn experience into improvement.

## New words
**team charter**, **role**, **demo**, **retrospective**, **viva** — see the [glossary](../../glossary.md).

---

**Chapter complete.** Your team can now ship a real project together. In Grade 11 you will step outside your class: **licences**, reading and contributing to **real open-source projects**, and safer history tools (**rebase, stash, revert**).

## Teacher notes
- **Rubric:** individual contribution visible in history (≥ 5 commits each); ≥ 2 PRs reviewed; issues linked; v1.0 tagged; viva (3 min) on one design decision. Ties into the school project work (verify with CDC).
- **Timing:** P1 (week 1): charter + issues. P2 (week 2): demo + review clinic. P3 (week 3): release, retrospective, vivas. Between periods teams need lab access — book it in advance.
- **Viva questions:** "Show me a PR you reviewed — what did you ask for and why?", "Why is this branch named like this?", "What would you do if your PR had a conflict now?"
- **Fairness:** read messages and reviews, not only counts; students with fewer but larger, well-reviewed commits can still score well.
- **Fallback Tier 1:** one shared USB "server" bundle per team, and a teacher-run integration session each week.
