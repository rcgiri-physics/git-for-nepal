# Grade 12 — Engineering with Git

!!! warning "Unpiloted draft"
    Core lessons are written but have not been tried in a classroom. Grade placement of topics is unverified against the CDC syllabus (see `research/decisions.md`).

!!! info "CDC fit (verified)"
    CDC Grade 12 Unit 7 *Software Development Process* (Waterfall, Agile: Scrum and XP, requirements, Gantt charts, testing) and Unit 8 *Software Project* (group project, at most four members, 10 practical hours; GitHub named among suggested tools) are the natural home for modules 2, 4 and 8. The capstone here is a longer extension of Unit 8.

**Big idea:** professional teams ship safely, repeatedly.
**Length:** ≈ 20 periods (to calibrate to CDC hours).
**Accounts:** Learners 13+; teacher-managed organisations; capstone clients only with written consent.
**Tools:** Git internals tools, CI (GitHub Actions / Forgejo Actions), static analysis/check scripts.

## How this chapter is built
Grade 12 turns habits into **engineering**: first understanding the machine (internals), then the systems professionals build around it — strategies, automation, releases, security, AI review and debugging — all applied in a six-week capstone.

```
 M1  internals              (the machine)
 M2  strategies             (team rules)
 M3  CI                     (robots)
 M4  SemVer                 (promises)
 M5  security               (safety)
 M6  AI diffs               (judgement)
 M7  blame/bisect           (detective work)
 M8  capstone               (all together)
 M9  where next             (beyond school)
```

## Modules
| # | Module | Periods | Tiers | Key ideas |
|---|---|---|---|---|
| 1 | [Git from the inside](m01-internals/lesson.md) | 3 | 0–3 | blob, tree, commit, refs |
| 2 | [Branching strategies](m02-branching-strategies/lesson.md) | 2 | 0–3 | trunk-based, GitHub flow, Gitflow, protection |
| 3 | [CI automation](m03-ci/lesson.md) | 3 | 1–3 | workflows, runners, required checks |
| 4 | [Releases and SemVer](m04-releases/lesson.md) | 2 | 1–3 | MAJOR.MINOR.PATCH, changelog |
| 5 | [Security](m05-security/lesson.md) | 2 | 1–3 | secrets, incident checklist, signing, supply chain |
| 6 | [Reviewing AI-assisted changes](m06-ai-diffs/lesson.md) | 2 | 0–3 | explain every line |
| 7 | [blame and bisect](m07-blame-bisect/lesson.md) | 2 | 0–3 | binary search, `bisect run` |
| 8 | [Team capstone](m08-capstone/lesson.md) | 8 | 1–3 | professional process |
| 9 | [Where Git goes next](m09-where-next/lesson.md) | 3 | 0–3 | pathway map |

## Chapter outcomes
1. describe Git's object model
2. choose and justify a branching strategy
3. write and read CI workflows
4. version releases with SemVer
5. prevent and respond to secret leaks
6. review AI-assisted diffs responsibly
7. locate a bug with bisect

## Free resources used in this chapter
[*Pro Git*](https://git-scm.com/book/en/v2) chapters 7 and 10, [*Git from the Bottom Up*](https://jwiegley.github.io/git-from-the-bottom-up/), MIT [Missing Semester](https://missing.csail.mit.edu/2020/version-control/), [Semantic Versioning](https://semver.org/), GitHub/Forgejo Actions docs, [pre-commit](https://pre-commit.com/), [gitleaks](https://github.com/gitleaks/gitleaks), [OpenSSF Scorecard](https://scorecard.dev/), GitHub Skills (Actions, releases, supply chain) and the PLOS *Ten Simple Rules* paper. Full list: [free resource library](../book/resources.md).

## Assessment
Capstone rubric, CI green, viva on design decisions. First-draft item bank: `assessments/g12-item-bank.md` (to be reviewed after Pilot 1).

## Capstone
A 3–4 person team project for 6+ weeks (CDC's software-project unit caps groups at four). Practice repo: `practice-repos/g12-capstone-starter/`.


## After Grade 12
Continue with [After Grade 12: the foundation, consolidated](../book/after-grade-12.md) and [Version control in any project](../book/any-project.md).
