---
id: g10-m01-issues
grade: 10
hours: 1
prerequisites: []
outcomes:
  - "Write a clear issue with a title, description and acceptance check"
  - "Assign and label issues in a team"
  - "Link a commit or pull request to an issue"
tier_support: [0, 2, 3]
license: CC-BY-4.0
---

# 1. Issues as a to-do list

!!! abstract "At a glance"
    **Time:** 1 period · **Tiers:** 0 (paper kanban wall), 2 (Forgejo), 3 (GitHub/Codeberg/GitLab) · **You need:** a team repository on the class server, or sticky notes and a wall

    **Before this:** Grade 9 (branches, remotes).

    **By the end you can:** write an issue that anyone can act on, label and assign it, plan with a board, and close it from a commit.

## Hook (5 min)
A team of four building the school website says *"we'll just remember what to do"*. Two weeks later, three people have each made an "About us" page, and nobody made the contact page. What went wrong?

## Understand it

### An issue is a written task
An **issue** (called a *ticket* or *work item* on some platforms) is a task, bug report, question or idea written down **where the whole team can see it** — on the Issues page of the repository's host. Each issue gets a number (`#1`, `#2`, …), a discussion thread, and a status: **open** or **closed**.

Issues turn "we should…" into a shared, numbered, checkable list. They are also history: a year later, you can read *why* a feature was built.

### Anatomy of a good issue
```
Title:   Add contact page with the school's phone and address        <- verb first, specific

What:    The website has no way to contact the school.
Why:     Parents asked the head teacher for the office number.        <- reason
Done when:                                                            <- acceptance check
  - [ ] contact.html exists and is linked from the menu
  - [ ] it shows the office phone, address and hours (no personal numbers)
  - [ ] check.sh passes
Labels:  feature        Assignee: @student-12
```

| Weak issue | Problem | Better |
|---|---|---|
| `fix it` | fix what? | `Fix broken link to festival.html in the menu` |
| `website bad` | no action, not kind | `Increase text size on phones — hard to read` |
| `do the stuff for Friday` | many tasks in one | split into 3 issues, one each |

A good issue is **one task**, small enough for one person in a few days, with a **"done when"** check so everyone agrees when it is finished.

### Labels, assignees, milestones, boards
- **Labels** group issues: `bug` (something is wrong), `feature` (something new), `docs` (writing), `good first issue` (easy start for newcomers — Grade 11!).
- **Assignee** — the *one* person responsible. Several people can help, but one person owns it.
- **Milestone** — a target date or version (`v1.0 — exhibition day`).
- **Board** (kanban) — columns *To do · Doing · Done*; each issue is a card that moves right.

### Linking work to issues
When you fix an issue, mention its number. Most hosts (GitHub, GitLab, Forgejo/Codeberg) understand **closing keywords**: a commit message or pull request description containing `Closes #3` or `Fixes #3` will automatically close issue #3 when merged into the main branch. Just `#3` (without the keyword) creates a link without closing.

```bash
git commit -m "Add contact page (closes #3)"
```

## See it
A team board at the start of the project:

```
| To do                              | Doing                         | Done                 |
|------------------------------------|-------------------------------|----------------------|
| #4 Add photo gallery      feature  | #2 Write About page  @s-07    | #1 Set up repo       |
| #5 Fix menu on phones     bug      | #3 Add contact page  @s-12    |                      |
| #6 Write README for site  docs     |                               |                      |
```

Every card has a number, a label and — once someone starts — exactly one owner.

## Unplugged: the kanban wall (15 min)
Draw three columns on the board or a wall: **To do · Doing · Done**. Each team writes the tasks of the School Website project on sticky notes, one task per note, using the "anatomy" above (title + done-when on the back). Rules: a person can have at most **two** notes in *Doing*; a note moves to *Done* only when its done-when check is ticked by someone else.

## PRIMM lab (25 min)
1. In your team's repo (LAN server or hosting platform), open the **Issues** page.
2. **Predict:** which of these is a good issue — `fix it`, `Add contact form to the school website`, `website bad`? Why?
3. Write **5 issues** for the School Website project, each with *what, why, done when*. **Modify** them after a neighbour team's feedback.
4. **Label** (`bug`, `feature`, `docs`) and **assign** each issue to one person. Create a milestone `v1.0`.
5. **Investigate:** comment on another team member's issue with a question. Who gets notified?
6. **Make:** put them on a board (the host's project board, or the wall); agree the first three to do. Make one commit with `closes #N` in the message and push — watch the issue close.

## Parsons practice (5 min)
Order the life of an issue: *open · discuss · assign · work on a branch · close with a commit message that mentions it*.

## Common mistakes
| Problem | Fix |
|---|---|
| One issue holds a whole week's work | split it; one task each |
| Nobody assigned → nobody does it | exactly one assignee |
| Issue closed but the work is not finished | use "done when" checks; close only when ticked |
| `closes #3` in a commit on a branch didn't close it | it closes only when merged into the default branch |
| Personal data (phone numbers, marks) in an issue | issues are visible to everyone in the repo; edit it out |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | GitHub Docs: [**Hello World**](https://docs.github.com/en/get-started/start-your-journey/hello-world) — read the steps; then compare with your class server: where is the Issues tab? | 3 | 15 min | 2 differences |
| 2 | Open any large open-source repository's issue list (for example [First Contributions](https://github.com/firstcontributions/first-contributions)). Find one issue that is clearly written and one that is not. What makes the difference? | 3 | 20 min | two examples, explained |
| 3 | [Codeberg docs](https://docs.codeberg.org/) — find the page about issue labels / project boards. | 3 | 10 min | link + summary |
| 4 | **Paper sort:** the teacher gives 10 issues; mark each *good / fix it* and rewrite the weak ones. | 0 | 15 min | rewritten issues |

## Exit ticket (5 min)
1. What three parts make a good issue?
2. Who should an issue be assigned to?
3. *Misconception:* "Issues are only for bugs." True or false?

## Key points
- An **issue** is a numbered, visible task with a discussion and a status.
- Good issue: verb-first title, what + why, **done when** checks; one task.
- Labels group, one assignee owns, milestones set targets, boards show flow.
- `Closes #N` in a merged commit or PR closes the issue automatically.

## New words
**issue**, **label**, **assignee**, **milestone**, **kanban board**, **closing keyword** — see the [glossary](../../glossary.md).

## Extension quest
Add an **issue template** to your repo (`.github/ISSUE_TEMPLATE/bug.md` on GitHub, `.forgejo/issue_template/…` or `.gitea/issue_template/…` on Forgejo) so every new bug report asks *what happened / what should happen / steps*. This book's own repository has templates in `.github/ISSUE_TEMPLATE/` — look at them.

## Teacher notes
- **Timing:** hook 5 · understand 10 · kanban wall 15 (or lab) · lab 20 · exit 5. With a short period, do the wall *or* the online lab.
- **Tier 0/1** teams use a paper kanban wall for the whole chapter. Keep titles in English or Nepali but code names in English.
- **Rubric for issues:** clear verb-first title, why, done-check, one task, one assignee.
- **Paper sort set:** include `help`, `Make site better`, `Add festival dates for 2083 BS to festival.html`, `ERROR!!!`, `Fix the about page and gallery and menu`, `Replace "Libary" with "Library" on index.html`, etc.
- **Answer key:** Exit 1: title, what/why, done-when. 2: one person who owns the task. 3: False — features, docs, questions and ideas too.
