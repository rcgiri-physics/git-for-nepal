# Grade 12 — Engineering with Git

!!! warning "Unpiloted draft"
    Core lessons are written but have not been tried in a classroom. Grade placement of topics is unverified against the CDC syllabus (see `research/decisions.md`).

!!! info "CDC fit (verified)"
    CDC Grade 12 Unit 7 *Software Development Process* (Waterfall, Agile: Scrum and XP, requirements, Gantt charts, testing) and Unit 8 *Software Project* (group project, at most four members, 10 practical hours; GitHub named among suggested tools) are the natural home for modules 2, 4 and 8. The capstone here is a longer extension of Unit 8.

**Big idea:** professional teams ship safely, repeatedly.
**Length:** ≈ 20 periods (to calibrate to CDC hours).
**Accounts:** Learners 13+; teacher-managed organisations; capstone clients only with written consent.
**Tools:** Git internals tools, CI (GitHub Actions / Forgejo Actions), static analysis/check scripts.

## Modules
| # | Module | Periods |
|---|---|---|
| 1 | [Git from the inside](m01-internals/lesson.md) | 3 |
| 2 | [Branching strategies](m02-branching-strategies/lesson.md) | 2 |
| 3 | [CI automation](m03-ci/lesson.md) | 3 |
| 4 | [Releases and SemVer](m04-releases/lesson.md) | 2 |
| 5 | [Security](m05-security/lesson.md) | 2 |
| 6 | [Reviewing AI-assisted changes](m06-ai-diffs/lesson.md) | 2 |
| 7 | [blame and bisect](m07-blame-bisect/lesson.md) | 2 |
| 8 | [Team capstone](m08-capstone/lesson.md) | 8 |
| 9 | [Where Git goes next](m09-where-next/lesson.md) | 3 |

## Chapter outcomes
1. describe Git's object model
2. choose and justify a branching strategy
3. write and read CI workflows
4. version releases with SemVer
5. prevent and respond to secret leaks
6. review AI-assisted diffs responsibly
7. locate a bug with bisect

## Assessment
Capstone rubric, CI green, viva on design decisions. First-draft item bank: `assessments/g12-item-bank.md` (to be reviewed after Pilot 1).

## Capstone
A 3–4 person team project for 6+ weeks (CDC's software-project unit caps groups at four). Practice repo: `practice-repos/g12-capstone-starter/`.

