---
id: g12-m08-capstone
grade: 12
hours: 8
prerequisites: [g12-m03-ci, g12-m04-releases, g12-m05-security, g12-m07-blame-bisect]
outcomes:
  - "Deliver a team project with CI, reviews, releases and documentation"
  - "Explain design decisions in a viva"
  - "Run a security and quality review before release"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 8. Team capstone

!!! abstract "At a glance"
    **Time:** 8 periods across 6+ weeks · **Tiers:** 1–3 · **You need:** a team repository with CI on the class server; `practice-repos/g12-capstone-starter`

    **Before this:** Grade 12 Modules 1–7 and everything before.

    **By the end you can:** run a professional-style project from charter to second release, and explain and defend its design and process.

## Hook (5 min)
A client — a local organisation, with written consent — needs a small tool: a validated data repository for their records, a simple web page, a translation of documentation. Your team of 3–4 (CDC's software-project unit allows at most four members) has 6+ weeks. Everything you learned since Grade 8 comes together here.

## Understand it

### What makes a project "professional"?
Not size — **process**. A small project is professional when anyone can see *what* is being built (issues), *why* each change was made (PRs, messages), *that* it works (CI), *which* version is which (releases), *how* to use and contribute (docs), and *that* it is safe (security review, no private data).

### The planning documents (week 1)
| Document | Contents | Built on |
|---|---|---|
| `CHARTER.md` | goal, client, team roles (rotating), meetings, communication | G10 M9 |
| `CONTRIBUTING.md` | branching strategy, review rule, message convention, AI-use policy | G12 M2, G11 M6, G12 M6 |
| **Definition of done** | e.g. *merged via reviewed PR · CI green · docs updated · changelog entry · no secrets* | G10 M1 |
| **Risk list** | what could go wrong and what you'll do (a member ill, power cuts, client unavailable, data licence unclear) | G11 M7 |
| Issues + milestones | ≥ 20 issues, milestones per release | G10 M1 |

### Project options
- **(a) Data repository** with a data card (`DATA.md`, `CITATION.cff`), cleaning scripts, and CI that validates the CSV on every PR — builds directly on Grade 11 Module 8.
- **(b) Web or Python app** — links to the CDC OOP/programming syllabus; tests in CI.
- **(c) Documentation or translation** contribution to a partner project — with the maintainers' consent and their review process.

### Requirements (all options)
≥ 20 issues · PRs with reviews (every member authors and reviews) · CI green on `main` · branch protection on `main` · ≥ 2 tagged releases following SemVer · `README`, `CONTRIBUTING`, `CHANGELOG`, `LICENSE`, `SECURITY.md` · no secrets, no personal data.

### Milestones
| Week | Milestone | Evidence |
|---|---|---|
| 1 | plan: charter, contributing, risks, ≥ 20 issues | documents, board |
| 2 | skeleton + CI + protection | first green run, protection settings |
| 3–4 | features (first release `v0.1.0` at end of week 3) | PRs, tag, release notes |
| 5 | hardening + **security review** (Module 5 checklist, gitleaks, dependency check) + **bug bash** (everyone tries to break it; bisect any regression) | review issue, fixes |
| 6 | release `v1.0.0` + client demo + viva + retrospective | tag, demo, `RETRO.md` |

### The viva
Each member explains, in about 5 minutes: one **design decision** (and an alternative you rejected), one **review** you gave (and what changed because of it), one **problem** you solved with Git (conflict, revert, bisect …), and how the **history** shows your work.

## See it
A capstone repository at release time:

```console
$ git tag --sort=creatordate
v0.1.0
v0.2.0
v1.0.0
$ git log --oneline --merges v0.2.0..v1.0.0 | wc -l
14                                  <- 14 reviewed PRs in the last release
$ git shortlog -s -n v0.1.0..v1.0.0
    23  Student 12
    19  Student 03
    18  Student 21
    16  Student 07
$ ls
CHANGELOG.md  CITATION.cff     DATA.md  README.md  SECURITY.md  clean.py  raw/
CHARTER.md    CONTRIBUTING.md  LICENSE  RETRO.md   check.sh     data/
```

## Weekly cycle
```
 Monday: plan issues for the week (board)
   -> branches -> PRs -> review -> CI -> merge (every day)
 Friday: 5-minute demo to the class/teacher; update risks
```

## Lab
1. Week 1: write the planning documents; open ≥ 20 issues; set milestones.
2. Week 2: build the skeleton from `practice-repos/g12-capstone-starter`; add CI (Module 3); protect `main` (Module 2).
3. Weeks 3–4: features via PRs; release `v0.1.0` (Module 4).
4. Week 5: security review and bug bash; use blame/bisect for any regression (Modules 5, 7).
5. Week 6: release `v1.0.0`; demo; viva; retrospective.

## Parsons practice
Order the weekly cycle: *plan issues · branch · PR · review · CI · merge · demo*.

## Rubric (100 points)
| Area | Points | Look for |
|---|---|---|
| Repository quality | 25 | structure, README/CONTRIBUTING/CHANGELOG/LICENSE, clean history, conventions followed |
| CI and tests | 15 | meaningful checks, green `main`, protection on |
| Review quality | 15 | every member reviews; specific, kind, actionable comments that changed code |
| Release practice | 10 | ≥ 2 SemVer releases with notes |
| Security | 10 | no secrets/PII, `.gitignore`, scanner run, `SECURITY.md`, dependencies pinned |
| Documentation | 10 | a stranger can run and contribute using the docs alone |
| Viva | 15 | individual explanation of a decision, a review and a Git problem |

## Common mistakes
| Problem | Fix |
|---|---|
| Plan written, then ignored | update the board every Monday; issues for all work |
| Everything merged in week 6 | release `v0.1.0` in week 3 — it forces integration early |
| One member is the "Git person" | every member authors and reviews PRs (rubric) |
| CI added at the end | week 2 |
| Client's real personal data used | synthetic or anonymised data only, agreed in writing |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Perez-Riverol et al., [*Ten Simple Rules for Taking Advantage of Git and GitHub*](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004947): score your project against the ten rules. | 3 | 30 min | score sheet |
| 2 | [Open Source Guides](https://opensource.guide/) — "Starting an Open Source Project": which items does your repository still miss? | 3 | 20 min | list |
| 3 | [OpenSSF Scorecard](https://scorecard.dev/) checks: apply them by hand to your repo. | 3 | 30 min | checklist |
| 4 | Software Carpentry [**Citation**](https://swcarpentry.github.io/git-novice/12-citation.html) — make sure your `CITATION.cff` is valid. | 1 / 3 | 15 min | file |

## Exit ticket
1. What was your hardest decision and why?
2. How does the history show each member's work?
3. *Check:* what would you do differently?

## Key points
- Professional = visible process: issues, PRs, reviews, CI, releases, docs, security.
- Plan in week 1, CI in week 2, release early (week 3), harden in week 5, release and reflect in week 6.
- Every member authors, reviews and can explain their work.

## Teacher notes
- **Rubric:** repo quality (25) · CI and tests (15) · review quality (15) · release practice (10) · security (10) · documentation (10) · viva (15). Fits CDC Grade 12 Unit 8 Software Project (10 practical hours); this capstone is a longer extension. CSTA 3B-AP-20 wording unverified.
- **Clients:** written consent; no personal data; the school owns the decision to publish. A teacher-invented "client" is fine.
- **Periods:** use the 8 periods for kick-off, two review clinics, security review, two demos, vivas and retrospective; teams work between periods.
- **Viva prompts:** "Show me the PR you are proudest of." "What did a reviewer change in your work?" "Walk me through how you would find the commit that broke X."
