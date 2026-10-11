---
id: g10-m08-ci-intro
grade: 10
hours: 1
prerequisites: [g10-m07-static-site]
outcomes:
  - "Run a check script and read its result"
  - "Explain what CI does"
  - "Add one new check"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 8. Automatic checks (CI) — intro

!!! abstract "At a glance"
    **Time:** 1 period · **Tiers:** 1 (by hand), 2–3 (automatic) · **You need:** `practice-repos/g10-school-website` with `check.sh`; Git Bash

    **Before this:** Module 7. *Optional module* — skip to Module 9 if time is short.

    **By the end you can:** run a check, read its message and exit code, add a check, and explain how CI runs checks automatically on every push or PR.

## Hook (5 min)
What if a robot could tell you — before a human reviewer even opens your PR — that a link on your page is broken? It never gets tired, never forgets, and checks *every* change.

## Understand it

### A check is a program that says pass or fail
A **check script** looks at the project and answers one question: *is this OK?* It prints messages for humans and ends with an **exit code** for computers: **0 = pass**, anything else = **fail**.

Our `check.sh` checks two rules for every `.html` file: it has a `<title>`, and every internal link points to a file that exists.

```bash
for f in *.html; do
  grep -q "<title>" "$f" || { echo "ERROR: $f has no <title>"; fail=1; }
  ...                                  # for each href: does the file exist?
done
exit $fail                             # 0 if nothing failed
```

### CI = run the checks automatically
**Continuous Integration (CI)** means: every time someone pushes or opens a PR, a server automatically gets the code and runs the checks. The result appears on the PR as a green ✓ or a red ✗.

```
 push / PR  --->  CI server: clone the branch, run check.sh  --->  ✓ pass / ✗ fail on the PR
                                                                     |
                                     reviewers see it; teams can block merging on ✗
```

Why it matters:

- Humans forget to run checks; robots don't.
- Problems are caught **minutes** after they are made, by the person who made them.
- Reviewers can spend their attention on ideas, not broken links.

CI services: GitHub Actions, GitLab CI, Forgejo Actions (on our school server), Woodpecker. They all read a small configuration file in the repository that says *"on push, run these commands"*. This book itself has one: `.github/workflows/ci.yml` checks every lesson, link and practice repo on every PR. Grade 12 Module 3 teaches how to write these files.

### What checks cannot do
A passing check means *"these rules are met"* — not *"the page is good"*. `check.sh` cannot tell you that the text is wrong, the colours are ugly, or the founding year is false. Checks **support** review; they don't replace it.

## See it
```console
$ bash check.sh
g10 ok
$ echo $?
0                                           <- exit code 0 = pass
  (break the Festival link: href="festivl.html")
$ bash check.sh
ERROR: index.html links to missing festivl.html
$ echo $?
1                                           <- non-zero = fail
```

## Unplugged: the robot reviewer (10 min)
One student is the **robot**. They get a written rule card (*"every page must have a title box; every arrow must point to a page that exists"*) and check paper "web pages" drawn by the class, saying only PASS or FAIL + the rule broken. Then discuss: what can the robot **not** notice? (bad writing, wrong facts, unkind words).

## PRIMM lab (30 min)
1. `bash check.sh` in `g10-school-website`. **Predict** the result. Then `echo $?`.
2. Break a link on purpose (`href="aboot.html"`). **Predict** the message. Run again. Read the message and the exit code.
3. Fix it and commit. On Tier 2/3, the platform can run the script automatically (see Grade 12 for workflows) — if your teacher has enabled CI, push and watch the ✓ or ✗ appear on your PR.
4. **Investigate:** delete the `<title>` from one page. Which rule catches it?
5. **Make:** add one more check — for example, *every `<img>` has an `alt` attribute*:
    ```bash
    if grep -o '<img[^>]*>' "$f" | grep -vq 'alt='; then
      echo "ERROR: $f has an image without alt text"; fail=1
    fi
    ```
    Put it inside the loop, test it with a page that breaks the rule, then commit it via a PR.

## Parsons practice (5 min)
Order: *change · run check · read message · fix · commit*.

## Common mistakes
| Symptom | Cause | Fix |
|---|---|---|
| `bash: check.sh: No such file` | wrong folder | `cd` into the site folder |
| `$'\r': command not found` | Windows line endings in the script | save as LF in VS Code (status bar *CRLF → LF*); the repo's `.gitattributes` can enforce it |
| Check passes but the page is broken | the rule doesn't cover it | add a check, *and* review |
| CI is red but works on my PC | different OS, missing file not committed | read the CI log; `git status` for uncommitted files |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | GitHub Skills [**Hello GitHub Actions**](https://github.com/skills/hello-github-actions) (13+, account). | 3 | 45 min | completed course |
| 2 | Read this book's `.github/workflows/ci.yml`. List every check it runs. | 1 | 15 min | list |
| 3 | [Forgejo Actions docs](https://forgejo.org/docs/latest/user/actions/): how is a workflow file for Forgejo similar to GitHub's? | 3 | 15 min | 2 similarities |
| 4 | Software Carpentry Shell: [**Shell Scripts**](https://swcarpentry.github.io/shell-novice/06-script.html) — write a tiny script of your own. | 1 / 3 | 30 min | script |

## Exit ticket (5 min)
1. What does a check script return?
2. Why is a robot reviewer useful?
3. *Misconception:* "If the check passes, the page is perfect." True or false?

## Key points
- A check prints messages and returns an **exit code**: 0 pass, non-zero fail.
- **CI** runs checks automatically on every push/PR and shows ✓/✗.
- Checks catch rule-breaking early; humans still review meaning and quality.

## New words
**check script**, **exit code**, **continuous integration (CI)**, **workflow**, **CI log** — see the [glossary](../../glossary.md).

## Extension quest
Make `check.sh` also check that every page links back to `index.html`.

## Teacher notes
- **Optional unit.** If time is short, skip to the team project.
- **Timing:** hook 5 · understand 10 · robot game 5 · lab 20 · Parsons + exit 5.
- If your Forgejo or GitHub organisation has Actions enabled, add this minimal workflow to the team repos before class so students see real ✓/✗ (GitHub: `.github/workflows/check.yml`; Forgejo: `.forgejo/workflows/check.yml`):
    ```yaml
    on: [push, pull_request]
    jobs:
      check:
        runs-on: ubuntu-latest      # Forgejo: the label of your runner
        steps:
          - uses: actions/checkout@v4
          - run: bash check.sh
    ```
- **Answer key:** Exit 1: pass/fail as an exit code (0 = pass) plus messages. 2: it checks every change automatically and quickly, so humans can focus on meaning. 3: False — it only checks its rules. Lab 4: the `<title>` rule.
