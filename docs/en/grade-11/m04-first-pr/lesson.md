---
id: g11-m04-first-pr
grade: 11
hours: 2
prerequisites: [g11-m03-triage]
outcomes:
  - "Fork, branch, change, push and open a pull request to an open project"
  - "Run a project's checks before opening the PR"
  - "Respond to review comments"
tier_support: [2, 3]
license: CC-BY-4.0
---

# 4. Your first PR — to this curriculum

!!! abstract "At a glance"
    **Time:** 2 periods (+ waiting for review) · **Tiers:** 2 (class copy on the LAN), 3 (the public repository; learners 13+) · **You need:** the issue you claimed in Module 3, Python with `pip install -r requirements.txt`

    **Before this:** Modules 1–3; Grade 10 Modules 2–4.

    **By the end you can:** contribute a change to a real project from fork to merge, following its rules, and handle review gracefully.

## Hook (5 min)
You will improve the very lessons you are learning from. When your PR is merged, your work becomes part of a book that other students in Nepal will read — with your name in the history.

## Understand it

### The open-source contribution path
You did all of these steps in Grade 10 inside your class. The difference now: **you are a visitor** to someone else's project, so you follow *their* rules.

```
  1 fork (server)  ->  2 clone (your PC)  ->  3 branch  ->  4 change
  ->  5 run checks  ->  6 commit  ->  7 push to your fork
  ->  8 open PR to upstream  ->  9 respond to review  ->  10 merged!
```

This is the same model used by the well-known [First Contributions](https://github.com/firstcontributions/first-contributions) practice repository.

### Follow the project's rules
For this book, `CONTRIBUTING.md` says:

- branch name `type/short-description` — e.g. `fix/typo-g9-m03`;
- run `python tools/validate_frontmatter.py` and `mkdocs build --strict` before opening the PR;
- use the PR template (what and why; checklist);
- no student names, photos, marks; no text copied from NC/SA sources;
- commit messages: imperative, short first line.

Other projects have other rules — always read theirs (Module 2).

### Keep your first PR small
A first PR should be small enough that a maintainer can review it in five minutes: a typo, a broken link, a missing glossary word, a clearer example. Small PRs are merged quickly, and you learn the whole process without getting stuck on a big change.

### Review is a conversation
Maintainers may ask for changes. That is normal and good — it is free mentoring from an experienced person. Answer every comment; push fixes to the **same branch**; say thank you. If your PR is closed without merging, ask politely why: maybe the change was already made, or does not fit the project. **A closed PR is not a failure** — you still learned the whole process, and the conversation is public evidence of your work.

### Staying in sync
While you wait, `main` upstream may move. If your PR shows a conflict, update your branch exactly as in Grade 10 Module 5:

```bash
git fetch upstream
git merge upstream/main     # on your PR branch
git push
```

## See it
```console
$ git clone https://github.com/<you>/git-for-nepal.git
$ cd git-for-nepal
$ git remote add upstream https://github.com/rcgiri-physics/git-for-nepal.git
$ git switch -c fix/typo-g9-m03
  (edit docs/en/grade-09/m03-branches/lesson.md)
$ python tools/validate_frontmatter.py
checked 41 lesson files, 0 error(s)
$ python tools/check_links.py
links checked in ... files, 0 broken
$ git commit -am "Fix spelling of 'separately' in Grade 9 branches lesson"
$ git push -u origin fix/typo-g9-m03
  (open the PR: base rcgiri-physics/git-for-nepal:main  <-  compare <you>:fix/typo-g9-m03)
```

## Unplugged rehearsal (10 min)
Before touching a computer, each student writes on paper: the issue number, the branch name, the exact file and line, the commit message, and the PR description (What and why · Type · Checklist). A partner checks it against `CONTRIBUTING.md`.

## PRIMM lab (60 min)
1. **Fork** this repo (Tier 3) or the class copy on the LAN (Tier 2).
2. **Clone** your fork; add `upstream`; `git switch -c fix/...` (use the issue's topic).
3. Make **one** change. **Predict:** will the checks pass? Run `python tools/validate_frontmatter.py` and `python tools/check_links.py` (and `mkdocs build --strict` if installed).
4. **Commit** with a clear message; **push**; open a PR using the template, with `Closes #N`.
5. **Investigate:** read the review comments; reply to each; push fixes. Watch the CI checks on the PR.
6. **Make:** after the merge, record it in your `CONTRIBUTIONS.md` portfolio (link, what you changed, what you learned) and add yourself to the contributors list if the project has one.

## Parsons practice (5 min)
Order: *fork · clone · branch · change · check · commit · push · PR · respond to review*.

## Common mistakes
| Symptom | Cause | Fix |
|---|---|---|
| PR opened against your own fork's main | wrong base repository | base = upstream `main`, compare = your branch |
| PR includes unrelated files | committed with `-a` after other edits, or old branch | branch from up-to-date upstream main; review *Files changed* |
| CI fails on your PR | a check you didn't run | read the CI log, fix, push |
| No reply for a week | maintainers are busy (often volunteers) | one polite reminder comment; be patient |
| Arguing with a reviewer | — | ask questions, give reasons, accept the project's decision |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Do the [First Contributions](https://firstcontributions.github.io/) tutorial (13+, account) — the safe practice PR. Its Nepali README is in the repo's translations folder. | 3 | 45 min | PR link |
| 2 | *Pro Git* [§6.2 **Contributing to a Project**](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project): read "Advanced Pull Requests" — keeping a PR up to date. | 3 | 20 min | summary |
| 3 | Open Source Guides, [**How to Contribute**](https://opensource.guide/how-to-contribute/) — "What happens after you submit a contribution". | 3 | 15 min | 3 possible outcomes |
| 4 | Review a classmate's PR to this repo using the Grade 10 checklist. | 2 / 3 | 20 min | review comments |

## Exit ticket (5 min)
1. What did the review change in your PR?
2. Why keep the first PR small?
3. *Misconception:* "If my PR is closed, I failed."

## Key points
- Fork → clone → branch → change → **run checks** → commit → push → PR → review → merge.
- Follow the project's CONTRIBUTING rules exactly.
- Small first PRs; answer every review comment; be patient and polite.
- A closed PR is still learning and evidence.

## New words
**contribution**, **base / compare branch**, **contributor**, **portfolio** — see the [glossary](../../glossary.md).

## Extension quest
Make a second contribution that is a little bigger: add an exercise answer to a teacher guide, or improve a Nepali summary (`needs-nepali-review`).

## Teacher notes
- **Timing:** P1: hook 5, understand 15, rehearsal 10, lab 1–2 (10). P2: lab 3–6 (35), Parsons + exit 5. Reviews arrive between lessons — check them at the start of Module 5.
- **Maintainers must respond kindly within a week;** add a `student-friendly` label. Agree this with the repository maintainers *before* the lesson.
- CSTA 3B-AP-20 (version control in a group project) is the international precedent for this module — verify wording before citing.
- **Tier 2:** set up a class copy of this repository on the LAN Forgejo with yourself as maintainer; merge good PRs there and forward the best ones upstream yourself.
- **Answer key:** Exit 2: easy to review and merge quickly; you learn the process without getting stuck. Exit 3: False.
