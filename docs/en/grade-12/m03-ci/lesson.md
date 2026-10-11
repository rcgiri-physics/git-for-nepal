---
id: g12-m03-ci
grade: 12
hours: 3
prerequisites: [g12-m02-branching-strategies]
outcomes:
  - "Write a workflow that runs checks on every push and PR"
  - "Read a failing run and fix it"
  - "Require green CI before merging"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 3. Automation: CI with GitHub Actions / Forgejo Actions

!!! abstract "At a glance"
    **Time:** 3 periods · **Tiers:** 2 (Forgejo Actions with a runner), 3 (GitHub Actions); Tier 1: run the same steps by hand · **You need:** your capstone repo, `practice-repos/g12-capstone-starter`

    **Before this:** Grade 10 Module 8 (check scripts), Module 2.

    **By the end you can:** write a CI workflow, read its logs, fix a failing run, and make green CI a rule for merging.

## Hook (5 min)
A robot runs your checks on every PR, in a clean computer, in under a minute — and refuses the merge if they fail. This book has one: every lesson you are reading was checked by it.

## Understand it

### From check script to pipeline
In Grade 10 you ran `check.sh` by hand. **CI (Continuous Integration)** runs such checks automatically. A **workflow** (also called a **pipeline**) is a YAML file in the repository describing:

- **triggers** — *when* to run (`on: push`, `on: pull_request`, on a schedule, by hand);
- **jobs** — groups of work, each on a fresh machine (a **runner**);
- **steps** — commands or reusable **actions** (`actions/checkout` gets the code).

```yaml
# .github/workflows/check.yml  (Forgejo: .forgejo/workflows/check.yml)
name: check
on:
  push:
    branches: [main]
  pull_request:
jobs:
  validate:
    runs-on: ubuntu-latest          # Forgejo: the label of your school's runner
    steps:
      - uses: actions/checkout@v4   # pinned version
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: bash check.sh          # exit code 0 = green, otherwise red
      - run: python -m unittest     # more checks = more steps
```

Every push to a PR triggers a run; the PR shows ✓ or ✗ next to each job, with a link to the **log**.

### Why a fresh machine matters
CI starts from a clean computer every time. "Works on my machine" problems — a file you forgot to commit, a library installed only on your PC — fail in CI. That is a feature: CI proves the project builds **from the repository alone**.

### Reading a red run
1. Open the failed job; find the **first** red step.
2. Read the last lines of its log — the error is usually there.
3. Reproduce locally: run the same command on your computer.
4. Fix, commit, push — the PR re-runs automatically.

### CI as a rule
Combine with branch protection (Module 2): *"require status checks to pass before merging"*. Now `main` can only receive changes that passed the checks.

### Good CI habits
- **Fast:** under ~5 minutes, or people stop waiting for it.
- **Pinned:** use fixed versions (`actions/checkout@v4`, `python-version: "3.12"`) so runs are repeatable.
- **Safe:** never print secrets; PRs from forks don't get secrets (Module 5).
- **Meaningful:** a check that always passes is noise; a flaky check that fails randomly teaches people to ignore red.
- **Beyond tests:** linters, link checks, data validation, building the website, building the PDF of a book.

### CD: continuous delivery/deployment
**CD** goes one step further: after CI passes on `main`, automatically publish (deploy the website, upload a release). This book's `.github/workflows/pages.yml` builds and deploys the site on every push to `main`.

## See it
This book's own CI (`.github/workflows/ci.yml`, shortened):

```yaml
on:
  pull_request:
  push:
    branches: [main]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - name: Front-matter and alignment
        run: python tools/validate_frontmatter.py
      - name: Link check (relative links)
        run: python tools/check_links.py
      - name: Build site
        run: mkdocs build --strict
      - name: Practice-repo smoke test
        run: bash tools/smoke_practice_repos.sh
```

A failing data check in the capstone starter:

```console
$ bash check.sh
bad row: 7,bad row without a value
$ echo $?
1
```

In CI this appears as a red ✗ on the step `run: bash check.sh`, with exactly those lines in its log.

## Unplugged: the pipeline relay (15 min)
Students stand in a line as a pipeline: **trigger** (receives a "push" card), **checkout** (copies the paper project), **check 1** (every page has a title), **check 2** (every link exists), **report** (holds up ✓ or ✗). Pass three paper projects through, one with a hidden broken link. Then remove the "checkout" student — what goes wrong? (Checks run on nothing.)

## PRIMM lab (90 min)
1. Look at `.github/workflows/ci.yml` in this repo. **Predict** what happens on a PR: which steps, in which order, and what makes it red.
2. In your capstone repo (start from `practice-repos/g12-capstone-starter`), add a workflow running `bash check.sh` on push and pull request. Push; watch the first run.
3. Push a broken change (e.g. add a row `7,bad row without a value` to `data/sample.csv`) on a branch and open a PR. **Investigate** the red run; read the log; reproduce it locally.
4. Fix; see it turn green. Protect `main` so a red run blocks merging.
5. **Modify:** add a second job or step — e.g. a Python test, or a link check for the README.
6. **Make:** add a data-validation step for a CSV (header and row count), e.g. *"`data/sample.csv` has at least 10 rows"*.

**Tier 1:** run the steps by hand in a fresh clone (`git clone . /tmp/ci-test && cd /tmp/ci-test && bash check.sh`) — this imitates the clean machine.

## Parsons practice (5 min)
Order: *push · workflow triggers · steps run · pass/fail shown on PR · merge allowed or blocked*.

## Common mistakes
| Symptom | Cause | Fix |
|---|---|---|
| Workflow never runs | file in the wrong folder or wrong `on:` | `.github/workflows/*.yml` (GitHub), `.forgejo/workflows/*.yml` (Forgejo); check triggers |
| YAML error | indentation (tabs, wrong spaces) | spaces only; validate in VS Code |
| Passes locally, fails in CI | uncommitted file, missing dependency, Windows vs Linux | commit it; install it in a step; check line endings/paths |
| `Permission denied: ./check.sh` | file not executable in Git | run with `bash check.sh`, or `git update-index --chmod=+x check.sh` |
| Forgejo job stays "waiting" | no runner with that label | ask the admin; match `runs-on` to the runner label |
| Red run ignored and merged | no protection | require status checks |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | GitHub Skills [**Hello GitHub Actions**](https://github.com/skills/hello-github-actions) (13+, account). | 3 | 45 min | completed course |
| 2 | [GitHub Actions docs](https://docs.github.com/en/actions): find "workflow syntax" and explain `on`, `jobs`, `runs-on`, `steps` in your own words. | 3 | 20 min | glossary of 4 terms |
| 3 | [Forgejo Actions docs](https://forgejo.org/docs/latest/user/actions/): what is a runner, and how is one registered? | 3 | 20 min | summary |
| 4 | [pre-commit](https://pre-commit.com/): run checks *before* each commit on your own PC. Compare with CI: why have both? | 1 / 3 | 30 min | answer |
| 5 | Read `tools/smoke_practice_repos.sh` in this repo. What does it test, and why is that useful for a curriculum? | 1 | 15 min | answer |

## Exit ticket (5 min)
1. What triggers a workflow?
2. Why protect `main`?
3. *Misconception:* "Green CI means no bugs."

## Key points
- A **workflow** = triggers + jobs + steps, in YAML in the repo.
- CI runs on a **fresh machine**: it proves the project works from the repo alone.
- Read the first red step's log; reproduce locally; fix; push.
- Require green checks to merge; keep CI fast, pinned and meaningful.
- **CD** publishes automatically after CI passes.

## New words
**workflow / pipeline**, **trigger**, **job**, **step**, **runner**, **action**, **status check**, **continuous delivery (CD)**, **flaky test** — see the [glossary](../../glossary.md).

## Extension quest
Add a `workflow_dispatch:` trigger so the workflow can be run by hand, and a `schedule:` trigger that checks external links once a week.

## Teacher notes
- **Timing:** P1: hook 5, understand 20, relay 15. P2: see it 5, lab 1–3 (35). P3: lab 4–6 (35), Parsons + exit 5.
- **Tier 0/1:** run `check.sh` by hand; the idea is the same. **Pin action versions.**
- Forgejo Actions needs a runner (`forgejo-runner`) registered on the LAN server; test it before class (`offline/forgejo-lan/` is untested on hardware — budget time).
- GitHub Actions minutes are free for public repositories; private repositories have a monthly quota — check the current limits for your organisation.
- **Answer key:** Exit 1: events such as push, pull_request, schedule, manual dispatch. 2: so only reviewed changes with green checks reach it. 3: False — CI only proves the checks you wrote passed.
