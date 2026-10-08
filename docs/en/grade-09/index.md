# Grade 9 — Branch and Share

!!! warning "Unpiloted draft"
    Core lessons are written but have not been tried in a classroom. Grade placement of topics is unverified against the CDC syllabus (see `research/decisions.md`).

!!! info "Grade placement"
    Python and MySQL are confirmed in CDC's **Grade 10** textbook, not Grade 9 (see `alignment/cdc-ncf2076.yml`). Modules 6–7 can move to Grade 10; modules 1–5 and 8 do not depend on them.

**Big idea:** branches let people work in parallel; remotes let work travel.
**Length:** ≈ 16 periods (to calibrate to CDC hours).
**Accounts:** Accounts only for learners 13+, managed by the teacher; otherwise a LAN server or bundles on USB.
**Tools:** Git CLI, terminal, Python, SQL (MySQL or SQLite), Forgejo LAN or class organisation.

## Modules
| # | Module | Periods |
|---|---|---|
| 1 | [Terminal basics bridge](m01-terminal-bridge/lesson.md) | 1 |
| 2 | [status/add/commit/log on the CLI](m02-cli-basics/lesson.md) | 2 |
| 3 | [Branches](m03-branches/lesson.md) | 2 |
| 4 | [Merge and the conflict game](m04-merge/lesson.md) | 2 |
| 5 | [Remotes](m05-remotes/lesson.md) | 2 |
| 6 | [Python under version control](m06-python-in-git/lesson.md) | 2 |
| 7 | [SQL under version control](m07-sql-in-git/lesson.md) | 2 |
| 8 | [Pair project: Ward Facts](m08-pair-project/lesson.md) | 3 |

## Chapter outcomes
1. use the terminal to create and navigate folders
2. run the basic Git cycle on the command line
3. create, switch and merge branches
4. resolve a simple merge conflict
5. clone, push and pull to a shared remote
6. explain why scripts (not live databases) are versioned

## Assessment
Practical (create → branch → merge → push), Parsons card test, short written questions in board style. First-draft item bank: `assessments/g09-item-bank.md` (to be reviewed after Pilot 1).

## Capstone
**Ward Facts** — pairs maintain a Python script and a SQL file that answer three questions about a small (synthetic) ward dataset. Practice repo: `practice-repos/g09-ward-facts/`.

