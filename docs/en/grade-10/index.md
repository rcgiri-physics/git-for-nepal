# Grade 10 — Team Workflows

!!! warning "Unpiloted draft"
    Core lessons are written but have not been tried in a classroom. Grade placement of topics is unverified against the CDC syllabus (see `research/decisions.md`).

!!! info "CDC fit (verified)"
    The CDC Class 10 textbook contains Unit 2 Database Management (MySQL) and Unit 4 Programming in Python, so Grade 9 modules 6–7 (Python and SQL under version control) fit naturally here too.

**Big idea:** teams need rules so work does not collide.
**Length:** ≈ 18 periods (to calibrate to CDC hours).
**Accounts:** Accounts for learners 13+ managed with the teacher; LAN server alternative.
**Tools:** Git, a Git host (GitHub, Codeberg/Forgejo, GitLab), HTML/CSS, Python (optional), check scripts.

## How this chapter is built
Grade 9 was two people. Grade 10 is a **team** with a **server** in the middle: work is planned in issues, proposed in pull requests, checked by people (review) and robots (CI), and shipped as releases.

```
 M1  issues                (plan)
 M2  fork/clone/branch     (where copies live)
 M3  pull requests         (propose)
 M4  review                (check)
 M5  PR conflicts          (integrate)
 M6  releases              (version)
 M7  publish               (ship)
 M8  CI                    (robot)
 M9  team project          (all together)
```

## Modules
| # | Module | Periods | Tiers | Key ideas |
|---|---|---|---|---|
| 1 | [Issues as a to-do list](m01-issues/lesson.md) | 1 | 0, 2–3 | issue anatomy, labels, `Closes #N` |
| 2 | [Fork vs clone vs branch](m02-fork-clone-branch/lesson.md) | 1 | 2–3 | `origin`, `upstream` |
| 3 | [Pull requests](m03-pull-requests/lesson.md) | 2 | 1–3 | PR description, `format-patch` |
| 4 | [Code review with a checklist](m04-code-review/lesson.md) | 2 | 0–3 | kind, specific, actionable |
| 5 | [Real merge conflicts](m05-conflicts/lesson.md) | 1 | 1–3 | merge `origin/main` into the branch |
| 6 | [Tags and releases](m06-releases/lesson.md) | 1 | 1–3 | annotated tags, changelog |
| 7 | [Publishing a static website](m07-static-site/lesson.md) | 2 | 1–3 | Pages, LAN server |
| 8 | [Automatic checks (CI) intro — optional](m08-ci-intro/lesson.md) | 1 | 1–3 | exit codes, CI |
| 9 | [Team project](m09-team-project/lesson.md) | 3 | 1–3 | charter, demo, retrospective |

## Chapter outcomes
1. plan team work with issues
2. choose between fork, clone and branch
3. open and review pull requests
4. resolve conflicts on a PR
5. tag a release and write notes
6. publish a static site from a repo
7. run a check script

## Free resources used in this chapter
[GitHub Skills](https://skills.github.com/) courses (Introduction to GitHub, Review pull requests, Resolve merge conflicts, GitHub Pages, Hello GitHub Actions, Release-based workflow — learners 13+), [*Pro Git*](https://git-scm.com/book/en/v2) chapters 2, 5 and 6, [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), [Open Source Guides](https://opensource.guide/), Atlassian's [workflow comparison](https://www.atlassian.com/git/tutorials/comparing-workflows), Learn Git Branching's Remote tab and the Codeberg/Forgejo docs. Full list: [free resource library](../book/resources.md).

## Assessment
Team rubric (individual contribution visible in history), peer-review quality, viva. First-draft item bank: `assessments/g10-item-bank.md` (to be reviewed after Pilot 1).

## Capstone
**Our School Website** (or a Python app) built by teams of 3–4 with issues, PRs and review. Practice repo: `practice-repos/g10-school-website/`.


## Ready for Grade 11?
A student is ready when they can, without help: write a clear issue; open a PR that closes it; give a specific, kind review; and fix a conflicted PR by merging `main` into their branch.
