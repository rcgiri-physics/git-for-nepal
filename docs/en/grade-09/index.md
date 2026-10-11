# Grade 9 — Branch and Share

!!! warning "Unpiloted draft"
    Core lessons are written but have not been tried in a classroom. Grade placement of topics is unverified against the CDC syllabus (see `research/decisions.md`).

!!! info "Grade placement"
    Python and MySQL are confirmed in CDC's **Grade 10** textbook, not Grade 9 (see `alignment/cdc-ncf2076.yml`). Modules 6–7 can move to Grade 10; modules 1–5 and 8 do not depend on them.

**Big idea:** branches let people work in parallel; remotes let work travel.
**Length:** ≈ 16 periods (to calibrate to CDC hours).
**Accounts:** only for learners 13+, managed by the teacher; otherwise a LAN server or bundles on USB.
**Tools:** Git CLI (Git Bash on Windows), Python, SQL (MySQL or SQLite), Forgejo LAN or class organisation.

## How this chapter is built
Grade 8 gave students one line of history on one computer. Grade 9 adds two dimensions: **parallel lines** (branches and merges) and **other computers** (remotes). The terminal arrives first so that every later command can be written down exactly.

```
 M1  terminal             (cd, ls, mkdir)
 M2  CLI cycle            (Grade 8 in commands)
 M3  branches             (labels on commits)
 M4  merge / conflict     (two lines join)
 M5  remotes              (work travels)
 M6  Python               (.gitignore, debugging)
 M7  SQL                  (recipe vs dish)
 M8  pair project         (agreement, changelog, tag)
```

## Modules
| # | Module | Periods | Tiers | Key commands |
|---|---|---|---|---|
| 1 | [Terminal basics bridge](m01-terminal-bridge/lesson.md) | 1 | 1–3 | `pwd`, `ls`, `cd`, `mkdir` |
| 2 | [status/add/commit/log on the CLI](m02-cli-basics/lesson.md) | 2 | 1–3 | `init`, `status`, `add`, `commit`, `diff --staged` |
| 3 | [Branches](m03-branches/lesson.md) | 2 | 0–3 | `branch`, `switch -c`, `log --graph --all` |
| 4 | [Merge and the conflict game](m04-merge/lesson.md) | 2 | 0–3 | `merge`, `merge --abort` |
| 5 | [Remotes](m05-remotes/lesson.md) | 2 | 1–3 | `clone`, `push`, `pull`, `fetch`, `bundle` |
| 6 | [Python under version control](m06-python-in-git/lesson.md) | 2 | 1–3 | `.gitignore`, `log -p` |
| 7 | [SQL under version control](m07-sql-in-git/lesson.md) | 2 | 1–3 | schema/queries, dumps |
| 8 | [Pair project: Ward Facts](m08-pair-project/lesson.md) | 3 | 1–3 | `tag`, `shortlog` |

## Chapter outcomes
1. use the terminal to create and navigate folders
2. run the basic Git cycle on the command line
3. create, switch and merge branches
4. resolve a simple merge conflict
5. clone, push and pull to a shared remote
6. explain why scripts (not live databases) are versioned

## Free resources used in this chapter
Software Carpentry's [Unix Shell](https://swcarpentry.github.io/shell-novice/) and [git-novice](https://swcarpentry.github.io/git-novice/) episodes 2–9 (CC BY), [Learn Git Branching](https://learngitbranching.js.org/) levels `intro2`, `intro3`, `rampup1` and the Remote tab, [*Pro Git*](https://git-scm.com/book/en/v2) chapters 2–3, [Visualizing Git](https://git-school.github.io/visualizing-git/), [Oh My Git!](https://ohmygit.org/), and — for learners 13+ with internet — [GitHub Skills](https://skills.github.com/). Full list: [free resource library](../book/resources.md).

## Assessment
Practical (create → branch → merge → push), Parsons card test, short written questions in board style. First-draft item bank: `assessments/g09-item-bank.md` (to be reviewed after Pilot 1).

## Capstone
**Ward Facts** — pairs maintain a Python script and a SQL file that answer three questions about a small (synthetic) ward dataset. Practice repo: `practice-repos/g09-ward-facts/`.

## Ready for Grade 10?
A student is ready when they can, without help: create a branch, commit on it and merge it; resolve a one-line conflict; and recover from a rejected push by pulling.
