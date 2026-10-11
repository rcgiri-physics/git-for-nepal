---
id: g10-m03-pull-requests
grade: 10
hours: 2
prerequisites: [g10-m02-fork-clone-branch]
outcomes:
  - "Open a pull request with a clear description"
  - "Explain how a PR connects an issue, a branch and a review"
  - "Update a pull request by pushing more commits"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 3. Pull requests

!!! abstract "At a glance"
    **Time:** 2 periods · **Tiers:** 2–3 (Tier 1 version with patches below) · **You need:** your team repo with issues from Module 1

    **Before this:** Modules 1–2.

    **By the end you can:** turn an issue into a branch, the branch into a pull request with a clear description, and update the PR after feedback.

## Hook (5 min)
In Grade 9 you merged straight into `main`. Imagine the whole school website team does that — on exhibition morning, someone's half-finished page breaks the menu for everyone. In a real team, **someone checks first**.

## Understand it

### What a pull request is
A **pull request (PR)** — GitLab calls it a *merge request (MR)* — is a request on the server that says:

> *"Please merge my branch `feature/about-page` into `main`. Here is what I changed and why. Please review it."*

It is **not** a copy of the code. It is a page that points at two branches and shows:

- **Conversation** — the description and everyone's comments;
- **Commits** — the commits on the branch;
- **Files changed** — the diff between the branch and `main`;
- **Checks** — automatic tests, if the team has them (Module 8).

```
 issue #2 "Write About page"
     |  (you create a branch for it)
     v
 branch feature/about-page:  c1 -- c2 -- c3      --push-->  server
     |
     v
 pull request #7: feature/about-page -> main      "Closes #2"
     |   reviewer reads the diff, comments, approves
     v
 merged into main  ->  issue #2 closes  ->  branch deleted
```

### The PR workflow
1. Pick an issue; create a branch named after it (`feature/about-page`, `fix/menu-link`).
2. Commit in small steps; push the branch.
3. Open the PR. Write a description (template below).
4. A teammate **reviews** (Module 4). You fix things by pushing **more commits to the same branch** — the PR updates itself.
5. When approved (and checks pass), someone **merges**. The branch is deleted.

### A good PR description
```markdown
## What
Adds about.html with the school's history and a menu link.

## Why
Closes #2 — parents asked for basic information about the school.

## How to check
1. Open about.html in a browser; the menu link "About" works.
2. Run `bash check.sh` — all links OK.

## Notes for the reviewer
I was not sure about the founding year; I wrote 2045 BS from the school notice board.
```

### Keep PRs small
A PR that changes 20 lines gets a careful review in 5 minutes. A PR that changes 2,000 lines gets "looks good" and hides bugs. **One issue → one branch → one small PR.**

### Who merges?
Teams decide. Common rules: *the author never merges their own PR without one approval*; *the reviewer merges*; *main is protected* — the server refuses direct pushes to `main` (Grade 12 covers branch protection).

## See it
```console
$ git switch main && git pull
$ git switch -c feature/about-page
$ git add about.html index.html
$ git commit -m "Add About page and menu link (closes #2)"
$ git push -u origin feature/about-page
...
remote: Create a new pull request for 'feature/about-page':
remote:   http://school-server/team-3/school-website/compare/main...feature/about-page
```

Most hosts print a link to open the PR right after you push a new branch.

## Unplugged: paper pull requests (15 min)
Pairs. The **author** writes a printed (or hand-written) diff of a small web page change on a sheet, with a PR description at the top. The **reviewer** writes comments in the margin using sticky notes, and either *approves* (✓) or *requests changes*. The author makes a second sheet (a new commit) answering the comments. Only then does the teacher (the "maintainer") staple it into the class's `main` folder.

## PRIMM lab (50 min)
1. Take issue #1 or #2 (e.g. *Add About page*). Create `feature/about-page` and make 2–3 small commits.
2. Push the branch. Open a PR: title, description using the template above (`Closes #N`), what you changed, how to check.
3. **Predict:** what will the reviewer see on the *Files changed* tab? Check it. Is anything there you didn't mean to include?
4. Your partner reviews (Module 4 goes deeper). Meanwhile, **fix a requested change** by pushing one more commit to the same branch. **Investigate:** how did the PR page change?
5. The reviewer approves and merges. **Investigate:** did the issue close? Delete the branch (button on the PR, then `git switch main && git pull && git branch -d feature/about-page` locally).
6. **Make:** write a PR description template for your team and commit it (`.github/pull_request_template.md` on GitHub, `.forgejo/pull_request_template.md` or `.gitea/pull_request_template.md` on Forgejo).

### Tier 1 version (no server): patches
```bash
git format-patch main          # writes 0001-Add-About-page.patch, one file per commit
# copy the .patch files to USB; the reviewer reads them (they are plain text diffs)
git am 0001-*.patch            # the maintainer applies them on their computer
```
This is how the Linux kernel still works today — by email!

## Parsons practice (10 min)
Order: *create branch · commit · push · open PR · review · merge · delete branch*.

## Common mistakes
| Symptom | Cause | Fix |
|---|---|---|
| PR shows dozens of unrelated changes | branched from an old or wrong branch | branch from an up-to-date `main` |
| Opened a new PR for every fix | — | push more commits to the **same** branch |
| Issue did not close | keyword missing, or PR not merged into the default branch | `Closes #N` in the description; merge into `main` |
| PR description says "pls merge" | no what/why/how to check | use the template |
| Merged your own PR with no review | — | team rule: one approval first |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | GitHub Skills [**Introduction to GitHub**](https://github.com/skills/introduction-to-github) (13+, account) — it ends with opening and merging a PR. | 3 | 60 min | completed course |
| 2 | GitHub Docs, [**Hello World**](https://docs.github.com/en/get-started/start-your-journey/hello-world): compare its steps with ours. Which step do we do on the command line instead of the website? | 3 | 15 min | answer |
| 3 | *Pro Git* [§5.2 **Contributing to a Project**](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project): read "Commit Guidelines". Write down three rules and check your PR against them. | 3 | 20 min | 3 rules + self-check |
| 4 | Look at closed PRs in this book's own repository (or any open-source project). Find one with a great description. What makes it great? | 3 | 15 min | link + reasons |

## Exit ticket (5 min)
1. What does `Closes #1` do?
2. Why open a PR instead of merging yourself?
3. *Misconception:* "A PR is a new copy of the code." True or false?

## Key points
- A **PR** asks to merge one branch into another, with description, commits, diff and discussion.
- Issue → branch → small commits → push → PR → review → merge → delete branch.
- Update a PR by pushing more commits to its branch.
- Good descriptions say what, why (`Closes #N`), and how to check.
- Small PRs get good reviews.

## New words
**pull request (PR)**, **merge request (MR)**, **review**, **approve**, **request changes**, **patch** — see the [glossary](../../glossary.md).

## Extension quest
Open a **draft** PR early ("work in progress") to get feedback before you finish. When is that useful?

## Teacher notes
- **Timing:** P1: hook 5, understand 15, paper PRs 15, lab 1–2 (5). P2: lab 3–6 (35), Parsons 5, exit 5.
- Keep PRs small (one issue). On Tier 2 Forgejo the PR flow is the same as on GitHub. Tier 1: simulate with `git format-patch` and a printed diff.
- **Before class:** make sure each team has issues from Module 1 and that `main` is protected (or at least agreed as "no direct pushes").
- **Answer key:** Exit 1: links the PR to issue #1 and closes the issue when the PR is merged into the default branch. 2: so someone reviews it first — catches mistakes, shares knowledge, protects `main`. 3: False — it points at a branch; no code is copied.
