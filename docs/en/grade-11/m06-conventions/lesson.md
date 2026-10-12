---
id: g11-m06-conventions
grade: 11
hours: 1
prerequisites: [g11-m05-rebase-stash-revert]
outcomes:
  - "Write conventional commit messages"
  - "Name branches consistently"
  - "Write a team conventions document"
tier_support: [0, 1, 2, 3]
license: CC-BY-4.0
---

# 6. Commit-message and branching conventions

!!! abstract "At a glance"
    **Time:** 1 period · **Tiers:** 0–3 · **You need:** a list of 8 bad commit messages; your repo

    **Before this:** Grade 8 Module 2 (message rules), Module 5.

    **By the end you can:** write a full commit message (summary, body, references), use Conventional Commits where a project wants them, and agree naming rules with a team.

## Hook (5 min)
Which message helps someone in two years: `update` or `Fix wrong date format in report header (#14)`? Imagine searching 3,000 commits for "when did the report date change?".

## Understand it

### Why conventions?
A **convention** is a shared habit. When everyone writes messages and names branches the same way, the history becomes **searchable, readable and even machine-readable** — tools can build changelogs automatically from it.

### Anatomy of a full commit message
```
Fix wrong date format in report header (#14)          <- summary: imperative, ≤ 72 chars
                                                      <- blank line
The header showed dates as MM/DD/YYYY, but local      <- body: WHY, and what was wrong;
school reports use YYYY-MM-DD.                            wrap at ~72 characters
Switch to ISO format and add a test for 2026-10-01.

Closes #14                                            <- references (issues, co-authors)
```

Rules of thumb (from Grade 8, grown up):

- **Summary:** imperative mood ("Fix", not "Fixed" or "Fixes") — read it as *"If applied, this commit will … fix wrong date format"*.
- **Body:** explain *why* and any trade-offs; the diff already shows *what*.
- **One logical change per commit** — easier to review, revert and bisect (Grade 12).
- Write messages for strangers: the future reader has no memory of today.

Write a multi-line message by running `git commit` without `-m` (an editor opens), or with several `-m` flags: `git commit -m "Summary" -m "Body paragraph"`.

### Conventional Commits
Many projects use the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) format:

```
<type>(<optional scope>): <summary>

feat(gallery): add photo gallery page
fix(menu): correct link to festival page
docs: explain how to run check.sh
refactor(clean): split cleaning into functions
test: add test for empty student count
chore: update .gitignore
feat!: rename data columns          <- "!" marks a breaking change
```

| Type | Means | Version bump (Grade 12) |
|---|---|---|
| `feat` | new feature | MINOR |
| `fix` | bug fix | PATCH |
| `docs`, `style`, `refactor`, `test`, `chore` | no user-visible change | none |
| `!` or `BREAKING CHANGE:` in body | breaks compatibility | MAJOR |

Use it **if the project uses it**. This book's own repository uses plain imperative messages (see `CONTRIBUTING.md`) — follow each project's rules.

### Branch naming
`type/short-topic`, lower-case, hyphens: `feat/photo-gallery`, `fix/menu-link`, `docs/readme-run-steps`. Some teams add the issue number (`fix/14-report-date`) or the author (`sita/report-date`). Pick one style and write it down.

### A conventions document
Put the team's choices in `CONVENTIONS.md` (or `CONTRIBUTING.md`): message format, branch names, review rules, merge or rebase. Optionally add a **commit template** so the editor shows the format every time:

```bash
git config commit.template .gitmessage
```

## See it
```console
$ git log --oneline -6
a3f9c01 fix(menu): correct link to festival page (#21)
77b2e10 feat(gallery): add photo gallery with alt text (#18)
5c1d9e4 docs: explain how to run check.sh
e02a7b3 feat(contact): add office hours (#12)
9d1e4a7 chore: add .gitignore for editor files
1b8c6f2 feat: first version of the school website
$ git log --oneline --grep="^fix"
a3f9c01 fix(menu): correct link to festival page (#21)
```

Searching history becomes easy when messages follow a convention.

## Unplugged: message makeover (15 min)
Pairs rewrite 8 bad messages (with a description of each change) as full messages: summary + body + reference. Then convert each summary to Conventional Commits form. Swap with another pair and check against the rules.

## PRIMM lab (25 min)
1. Rewrite 8 bad messages as good ones (teacher list).
2. **Predict** which message style makes `git log --oneline` readable. Compare `git log --oneline` of your Grade 10 team repo with this book's repo.
3. Add a `.gitmessage` template to your repo: write the format as comment lines (`# type(scope): summary`, `# why:`), then `git config commit.template .gitmessage`. Make a commit without `-m` and see it.
4. **Investigate:** use `git log --grep="fix"` and `git log --author="Student 12"` to search history.
5. **Make:** team agreement document `CONVENTIONS.md` (messages, branches, merge vs rebase, review).

## Parsons practice (5 min)
Order the parts of a commit message: *summary · blank line · body (why) · issue reference*.

## Common mistakes
| Mistake | Fix |
|---|---|
| Summary too long, wraps in `--oneline` | ≤ 72 characters; details in the body |
| Body repeats the diff ("changed line 4") | explain why |
| Past tense / "this commit fixes…" | imperative: "Fix …" |
| Mixing conventions in one project | write `CONVENTIONS.md`; follow it |
| Over-formalising a tiny school repo | readability matters more than rules |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) — read the summary and the examples; answer its FAQ question about a commit that fits more than one type. | 3 | 20 min | answer |
| 2 | *Pro Git* [§5.2 **Contributing to a Project**](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project) — "Commit Guidelines" (the model message). Compare with ours. | 3 | 15 min | 2 differences |
| 3 | Software Carpentry [**Tracking Changes**](https://swcarpentry.github.io/git-novice/04-changes.html) — exercise "Choosing a Commit Message". | 1 / 3 | 10 min | answer |
| 4 | Read the last 30 messages of a big open-source project. Which convention does it use? | 3 | 15 min | evidence |

## Exit ticket (5 min)
1. What is the ideal length of the first line?
2. What should the body explain?
3. *Misconception:* "Messages are only for me."

## Key points
- Full message: imperative summary (≤ 72 chars), blank line, body explaining **why**, references.
- Conventional Commits: `type(scope): summary` — readable and machine-usable.
- Branch names: `type/short-topic`.
- Write the team's conventions down; follow each project's own rules.

## New words
**convention**, **imperative mood**, **commit body**, **Conventional Commits**, **commit template**, **breaking change** — see the [glossary](../../glossary.md).

## Extension quest
Find a tool that builds a changelog from Conventional Commits messages. What would it produce from the *See it* history?

## Teacher notes
- **Timing:** hook 5 · understand 10 · makeover 15 · lab 10 · Parsons + exit 5 (lab steps 3–5 as homework if short).
- **Avoid over-formalising for a school:** the aim is readability, not a rigid standard.
- **Bad messages list:** `update`, `fix bug`, `changes`, `asdf`, `final version`, `did stuff for gallery and fixed menu and readme`, `Fixed the thing Sita said`, `WIP`.
- **Answer key:** Exit 1: about 50, at most 72 characters. 2: why the change was made (and trade-offs). 3: False — they are for every future reader, including tools. Exercise 1: split it into several commits where possible.
