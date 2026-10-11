---
id: g9-m08-pair-project
grade: 9
hours: 3
prerequisites: [g9-m07-sql-in-git]
outcomes:
  - "Work in a pair using branches and a remote"
  - "Deliver a repo with a script, SQL and README that answer 3 questions"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 8. Pair project: Ward Facts

!!! abstract "At a glance"
    **Time:** 3 periods (+ homework) · **Tiers:** 1 (bundles), 2, 3 · **You need:** the shared remote for your pair (or USB bundles), the `g09-ward-facts` starter

    **Before this:** Modules 1–7.

    **By the end you can:** plan and deliver a small project with a partner, using branches, merges, a remote, a changelog and a tag.

## Hook (5 min)
The class will present to a visiting official (or the head teacher): *"What do the ward numbers tell us?"* Each pair answers three questions — and must be able to show **how** they got the answers, step by step, from their history.

## Understand it

### Working as a pair
Two people, one repository, two computers. The project only goes well if you agree how to work **before** you start. A **working agreement** is a short written list of rules, kept in the repo as `AGREEMENT.md`:

```markdown
# Our working agreement
- Branch names: `name/topic`, e.g. `sita/q2-density`.
- Sita owns `facts.py`; Hari owns `queries.sql`; we both edit README (talk first!).
- We pull at the start of every session and push at the end.
- Before merging into main, the partner reads the diff (`git log -p main..sita/q2-density`).
- Messages: verb first, say what and why.
```

### The pair routine
```
 start of session:  git switch main  ->  git pull
 work:              git switch -c sita/q1   ->  edit  ->  add  ->  commit (repeat)
 share:             git switch main  ->  git pull  ->  git merge sita/q1  ->  git push
```

Each partner works on their **own branch**, so they never block each other; `main` always holds the combined, working version.

### Finishing like professionals: changelog and tag
- A **`CHANGELOG.md`** lists, for humans, what changed in each version: *Added 3 questions; Fixed population total*.
- A **tag** is a permanent name for one commit — like a branch label that never moves. `git tag v1.0` marks "this is the version we presented". Push it with `git push origin v1.0`. (Grade 10 Module 6 and Grade 12 Module 4 go deeper into releases.)

### What the teacher looks at
The history is the evidence. `git log --oneline --graph --all` shows the branches and merges; `git shortlog -s -n` counts commits per author; the messages show your thinking.

## See it
A healthy pair history at the end:

```console
$ git log --oneline --graph --all
*   f7202da (HEAD -> main, tag: v1.0, origin/main) Merge branch 'hari/q3-small-wards'
|| * b4f828b (hari/q3-small-wards) Add query for wards under 1,000 people
* | 5b19654 (sita/q2-density) Print population density per ward
* | 96501d4 Add area_km2 column to schema
|/
* 0acfbde Add working agreement
* 6ca96e1 Start from ward-facts starter
$ git shortlog -s -n
     3  Hari
     3  Sita
```

Sita's branch was merged first as a **fast-forward** (main had not moved), so it looks like a straight line; Hari's branch then needed a **merge commit**.

## Plan (3 periods)
| Stage | When | What |
|---|---|---|
| Agree | P1, 15 min | write and commit `AGREEMENT.md`; choose the 3 questions |
| Build | P1–P2 + home | each partner answers questions on their own branch; merge via the remote |
| Conflict | P2 | resolve at least one conflict honestly (the README is a good place) |
| Review | P2, 15 min | partner reads each branch's diff before merge; swap with another pair and write 2 comments on paper |
| Release | P3, 15 min | `CHANGELOG.md` entry, `git tag v1.0`, push the tag |
| Present | P3 | show the graph, a diff, and the answers (3 min per pair) |

### Question ideas
1. Which ward has the most households? 2. What is the average household size (`population / households`) per ward? 3. Which wards are above the average population? 4. What is the population density (if you added `area_km2`)? 5. What share of the total population lives in the largest ward?

## PRIMM lab
**Brief:** pairs maintain a Python script + SQL file answering 3 questions about the small ward dataset.

1. **Predict:** before cloning, draw the graph you *expect* at the end (two branches, two merges, a tag).
2. Clone the starter. Commit `AGREEMENT.md`. Each partner creates a branch.
3. Each partner answers questions in their files; commit small steps; merge via the shared remote.
4. Resolve at least one conflict honestly (the README is a good place — both add a "Results" section).
5. Add a `CHANGELOG.md` entry and tag the result `v1.0` (`git tag v1.0`, `git push origin v1.0`).
6. **Investigate:** compare your final graph with your prediction.
7. Present: show the graph, a diff, and the answers.

## Parsons practice
Order the pair routine: *pull · switch to your branch · work · commit · switch main · pull · merge · push*.

## Rubric
| Criterion | 3 | 2 | 1 |
|---|---|---|---|
| Commits | ≥ 8 per pair, each partner ≥ 3 | 5–7 / one partner < 3 | < 5 |
| Branches | each partner used a branch, merged into main | one branch | none |
| Conflict | resolved, markers gone, message explains | resolved | not attempted |
| README | explains what, how to run, data source | partly | missing |
| Messages | what + why | mostly | vague |
| Changelog + tag | both | one | neither |
| Answers | 3 correct, explained | 2 | ≤ 1 |

Maximum 21 points.

## Common mistakes
| Problem | Fix |
|---|---|
| One partner does everything | the agreement assigns files; `git shortlog -s -n` shows it |
| Working directly on `main`, overwriting each other | use your own branch; merge only after pulling |
| Never pulling → huge conflicts at the end | pull every session |
| Tag created but not on the server | `git push origin v1.0` (tags are not pushed by default) |
| Conflict "resolved" by deleting the partner's work | talk first; keep both ideas where possible |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Software Carpentry [**Collaborating**](https://swcarpentry.github.io/git-novice/08-collab.html): compare its workflow with your agreement; add one rule you like. | 1 / 3 | 20 min | new rule |
| 2 | *Pro Git* [§2.6 **Tagging**](https://git-scm.com/book/en/v2/Git-Basics-Tagging): what is the difference between a lightweight and an annotated tag? Make an annotated `v1.1` (`git tag -a v1.1 -m "…"`). | 1 / 3 | 15 min | difference + tag |
| 3 | [Keep a Changelog](https://keepachangelog.com/en/1.1.0/): rewrite your `CHANGELOG.md` using its headings (*Added, Changed, Fixed*). | 3 | 15 min | changelog |
| 4 | Learn Git Branching [`remote5` "Faking Teamwork"](https://learngitbranching.js.org/?locale=en_US&level=remote5) and `remote7` "Diverged History" (use the merge solution, not rebase). | 1 / 3 | 20 min | levels done |

## Exit ticket
1. Which commit are you most proud of?
2. What did your pair agreement say?
3. *Check:* how can the teacher see who did what?

## Key points
- Agree how to work first: owners, branches, when to pull and push, review.
- Each partner on their own branch; `main` is the combined, working version.
- Pull at the start, push at the end, merge often.
- Finish with a changelog and a tag; the history is your evidence.

## New words
**working agreement**, **tag**, **changelog**, **`git shortlog`** — see the [glossary](../../glossary.md).

---

**Chapter complete.** You can now branch, merge and share. In Grade 10 you will work in **teams** with **issues**, **pull requests** and **code review**, publish a website, and meet **automated checks (CI)**.

## Teacher notes
- **Timing:** P1: hook + agreement 15, build 25. P2: build/conflict 25, review 15. P3: release 15, presentations 25.
- **Rubric:** ≥ 8 commits per pair; each partner ≥ 3; branch used and merged; ≥ 1 conflict resolved; README explains how to run; messages say what and why. **Peer review:** swap repos and write two comments on paper.
- **Fairness:** use `git shortlog -s -n` but don't mark only by counts; read the messages. One partner may legitimately have fewer, larger commits.
- **Tier 1 version:** each pair passes a bundle on USB at the end of each session (`git bundle create pair.bundle --all`; partner `git pull pair.bundle main`).
- **Answer key for question ideas (synthetic data):** Q1 Test Ward Four (480 households); Q2 sizes ≈ 4.82, 4.68, 4.83, 4.81, 4.57; Q3 average 1242 → Test Ward Two (1450) and Test Ward Four (2310); Q5 2310 / 6210 ≈ 37.2 %.
