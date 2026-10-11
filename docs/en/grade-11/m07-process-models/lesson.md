---
id: g11-m07-process-models
grade: 11
hours: 2
prerequisites: [g11-m06-conventions]
outcomes:
  - "Relate waterfall, iterative and agile ideas to branches, PRs and releases"
  - "Map process-model terms to Git artefacts"
tier_support: [0, 1, 2, 3]
license: CC-BY-4.0
---

# 7. Software process models and Git workflows

!!! abstract "At a glance"
    **Time:** 2 periods · **Tiers:** 0–3 · **You need:** this book's repository history (or your Grade 10 team repo), chart paper

    **Before this:** Grade 10 (issues, PRs, releases), Module 6.

    **By the end you can:** describe waterfall, iterative and agile (Scrum, XP) models, and point to where each idea lives in a Git repository.

## Hook (5 min)
Your syllabus has "software process models" — usually learned as diagrams for the exam. But you have already *lived* one: the Grade 10 team project had a backlog, weekly demos and a retrospective. Git workflows are the daily practice of process models.

## Understand it

### What is a process model?
A **software process model** describes the order in which a team does the work of building software: understand requirements, design, build, test, release, maintain. Different models arrange these steps differently.

### Waterfall
Each phase finishes before the next starts, like water falling down steps:

```
 requirements -> design -> implementation -> testing -> deployment -> maintenance
 (months)        (months)   (months)          (months)   (one big release)
```

Good when requirements are fixed and well understood (e.g. building to a government specification), and changes are expensive. Risk: you discover problems very late, and the customer sees the product only at the end.

**In Git:** long-lived branches, few big merges, one major release tag at the end; changelogs with huge entries.

### Iterative and incremental
Build a small working version, then improve it in repeated cycles. Each cycle produces an **increment** — something that works and can be shown.

```
 v0.1 -> feedback -> v0.2 -> feedback -> v0.3 -> ... -> v1.0
```

**In Git:** frequent tags (`v0.1.0`, `v0.2.0` …), short branches, regular merges into `main`.

### Agile: Scrum and XP
**Agile** is a family of iterative approaches that value working software, collaboration and responding to change (from the *Agile Manifesto*, 2001).

- **Scrum** organises work into **sprints** (1–4 weeks). The **product backlog** lists everything wanted; at **sprint planning** the team picks items; a short **daily stand-up** checks progress; the **sprint review** demonstrates the increment; the **retrospective** improves the process. Roles: product owner, Scrum master, developers.
- **XP (Extreme Programming)** focuses on engineering practices: **pair programming**, **test-driven development**, **continuous integration**, **small releases**, collective code ownership.

Agile does **not** mean "no planning" — it means planning *often*, in small pieces.

### Mapping process ideas to Git
| Process idea | Git / host artefact |
|---|---|
| requirement, user story | **issue** |
| product backlog | open issues, ordered on a **board** |
| sprint / iteration | **milestone** with a due date |
| increment | merged PRs + a **release tag** |
| quality gate / review | **pull request review** + **CI** checks |
| continuous integration (XP) | merge to `main` often; CI on every push |
| pair programming (XP) | driver/navigator; `Co-authored-by:` trailer in messages |
| sprint review / demo | weekly demo of the board and graph (Grade 10) |
| retrospective | `RETRO.md` |
| maintenance | issues labelled `bug`, PATCH releases |
| Gantt chart / schedule | milestones and due dates (some hosts draw roadmaps) |

### Reading a model from history
A repository's history shows which model a team really follows: many small merged PRs and frequent tags → iterative/agile; long silences then one giant merge → waterfall-like. You will analyse this book's own history in the lab.

## See it
```console
$ git log --oneline --merges | wc -l              # how many PR merges?
$ git tag --sort=creatordate                      # how often are releases made?
$ git log --format="%ad" --date=format:%Y-%m | sort | uniq -c   # commits per month
```

A team that commits every week and tags every month is working iteratively, whatever its documents say.

## Unplugged: two timelines (20 min)
On chart paper draw two timelines of the same 8-week school website project. **Waterfall:** blocks for requirements (2 weeks), design (2), build (2), test (1), release (1). **Agile:** four 2-week sprints, each ending with a demo star and a small release. Mark with a red dot: *"the head teacher changes her mind about the menu in week 5."* Which timeline copes better? Where is the first moment the head teacher sees something working?

## PRIMM lab (50 min)
1. Sort the project's real history (this book's repo, or your Grade 10 team repo: last 20 commits and PRs) onto a timeline. Which model does it resemble? Use the commands in *See it*.
2. **Predict** which model needs more branching; then count branches and merges in the graph (`git log --oneline --graph --all | head -40`).
3. **Investigate:** map each artefact in your Grade 10 team repo to the table above (which issues were "backlog", which tag was the "increment", where the "retrospective" is).
4. **Modify:** re-plan your Grade 10 project as two Scrum sprints: which issues go in sprint 1? Make two milestones on the server and assign issues.
5. **Make:** a one-page comparison table (waterfall vs iterative vs Scrum vs XP) with examples from your Grade 10 team project.

## Parsons practice (5 min)
Match term to Git artefact: backlog → issues; increment → tag; review → PR; sprint → milestone; CI → automatic checks.

## Common mistakes
| Misunderstanding | Better |
|---|---|
| "Agile means no planning or documents" | planning is frequent and light; documents are kept useful |
| "Waterfall is always bad" | fits fixed, well-understood, regulated work |
| "Using GitHub makes us agile" | tools don't decide the model; habits do |
| "Scrum = daily meetings" | sprints, backlog, review and retrospective matter as much |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Atlassian, [**Comparing workflows**](https://www.atlassian.com/git/tutorials/comparing-workflows): match each Git workflow to the process model it suits best. | 3 | 20 min | table |
| 2 | *Pro Git* [§3.4 **Branching Workflows**](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows): "long-running branches" vs "topic branches" — which model uses which? | 3 | 15 min | answer |
| 3 | [**Open Source Guides**](https://opensource.guide/) — pick one guide and say how open-source projects plan work without a manager. | 3 | 20 min | 5 lines |
| 4 | **Paper:** draw the Scrum cycle and label each part with a Git artefact. | 0 | 15 min | diagram |

## Exit ticket (5 min)
1. Which model uses small frequent releases?
2. What Git feature represents an increment?
3. *Misconception:* "Agile means no planning."

## Key points
- **Waterfall:** phases in sequence, one big release. **Iterative:** repeated cycles, increments. **Agile (Scrum, XP):** short sprints, frequent feedback, engineering practices.
- Git artefacts embody process ideas: issues = backlog, milestones = sprints, tags = increments, PR review + CI = quality gates.
- History shows the model a team *really* follows.

## New words
**process model**, **waterfall**, **iterative**, **increment**, **agile**, **Scrum**, **sprint**, **backlog**, **XP**, **stand-up** — see the [glossary](../../glossary.md).

## Extension quest
Add a `Co-authored-by: Name <email>` trailer to a commit made in pair programming. How does the host display it?

## Teacher notes
- **Timing:** P1: hook 5, understand 25, two timelines 10. P2: lab 35, Parsons + exit 5.
- CDC's Grade 12 syllabus has Unit 7 *Software Development Process* (Waterfall, Agile with Scrum and XP, requirements, Gantt charts, testing). This lesson is a Git-flavoured preview and may be moved to Grade 12. Keep it conceptual; no syllabus text is quoted here.
- Exam link: students can use the mapping table as concrete examples in written answers.
- **Answer key:** Exit 1: iterative/agile. 2: a release tag (with its merged PRs). 3: False — planning happens every sprint.
