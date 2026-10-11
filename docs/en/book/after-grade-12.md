# Part VII. After Grade 12: the foundation, consolidated

You have finished the five chapters. This part helps you **check** that your foundation is solid, **fix** any gaps, and see **what comes next**. It also contains a four-week **bridge course** for anyone who joins late — a student starting at +2 or university, a learner who missed grades, or a teacher preparing to teach.

## 1. The foundation in one page

```
 objects & refs:  commit = snapshot (tree) + parents + message      G12 M1 explains G8 M2
      |
 three places:    working copy -> staging area -> history           G8 M3, G9 M2
      |
 undo:            restore, stash | revert (shared)                  G8 M5, G11 M5
                  reset, rebase (local only) | reflog rescues
      |
 labels:          branches and tags point at commits;               G9 M3, G10 M6
                  HEAD = you are here
      |
 integration:     merge via common ancestor;                        G9 M4, G10 M5
                  conflicts = human decisions
      |
 sharing:         every clone is complete: fetch, pull, push,       G9 M5, G10 M2
                  forks, upstream
      |
 team process:    issue -> branch -> PR -> review -> CI             G10, G12
                  -> merge -> release
      |
 responsibility:  licences, privacy, secrets, AI review, credit     G11 M1, G12 M5-M6
```

## 2. Competency checklist

Tick what you can do **without help**. Each line says where it was taught, so you can go back.

### A. History and snapshots
- [ ] I can explain a commit as a snapshot with a message, author, date and parent(s). *(G8 M2)*
- [ ] I can read `git log`, `git show` and a diff, and answer who/when/what/why for any change. *(G8 M4)*
- [ ] I can explain blobs, trees, commits and refs, and why commit ids change after a rebase. *(G12 M1)*

### B. Undo and safety
- [ ] I can choose between `restore`, `restore --source`, `revert`, `reset`, `commit --amend` and `stash` for a situation. *(G8 M5, G11 M5)*
- [ ] I follow the golden rule: never rewrite history others already have. *(G11 M5)*
- [ ] I can recover "lost" commits with `reflog`. *(G11 M5)*

### C. Branching and integration
- [ ] I can create, switch, merge and delete branches, and read `log --graph`. *(G9 M3–M4)*
- [ ] I can resolve a conflict calmly, test the result, and finish or abort a merge. *(G9 M4, G10 M5)*
- [ ] I can rebase my own branch and explain when not to. *(G11 M5)*
- [ ] I can find the commit that broke something with `bisect`. *(G12 M7)*

### D. Sharing and remotes
- [ ] I can clone, fetch, pull and push, and fix a rejected push. *(G9 M5)*
- [ ] I can fork a project, set `upstream`, and keep my fork in sync. *(G10 M2)*
- [ ] I can move a repository with no network using `git bundle`. *(G9 M5)*

### E. Collaboration and communication
- [ ] I can write clear issues, PR descriptions and full commit messages. *(G10 M1, M3; G11 M6)*
- [ ] I can review a PR with a checklist and write specific, kind, actionable comments. *(G10 M4)*
- [ ] I can contribute to someone else's project following its rules. *(G11 M2–M4)*

### F. Automation and quality
- [ ] I can write `.gitignore`, check scripts and a CI workflow, and fix a red run. *(G9 M6, G10 M8, G12 M3)*
- [ ] I can release with tags, SemVer and a changelog. *(G10 M6, G12 M4)*
- [ ] I can make data cleaning reproducible and documented. *(G11 M8)*

### G. Ethics, licences, privacy, security
- [ ] I can credit sources (TASL) and choose a licence. *(G11 M1)*
- [ ] I keep secrets and personal data out of repositories and know the incident checklist. *(G12 M5)*
- [ ] I never commit code I cannot explain, including AI-generated code. *(G12 M6)*

### H. Beyond code
- [ ] I can bring version control into a non-software project. *(Part VIII)*

**Reading your result:** 20–22 ticks — a strong foundation; go to section 5. 14–19 — fix the gaps with the table below. Fewer than 14 — take the bridge course.

## 3. The foundation test (practical, 60 minutes)

A teacher can use this as a final check, or a learner as a self-test. Do it in a fresh practice repository.

1. Create a repository with a `README.md` and a `.gitignore` that ignores `*.log`; make two commits with good messages.
2. Create a branch `feature/notes`, add `notes.md` in two commits, merge it into `main`. Was it a fast-forward? Why?
3. Create a conflict on purpose between two branches and resolve it so both ideas are kept.
4. Commit a "bad" change and undo it **safely as if it were already pushed**.
5. Make three messy local commits and turn them into one clean commit.
6. Delete a branch with unmerged work, then recover it with `reflog`.
7. Clone your repository into a second folder, commit there, and bring the commit back to the first folder (push/pull between the two, or a bundle).
8. Tag `v1.0.0`; make a backwards-compatible feature; tag the correct next version.
9. Write a check script that fails if `README.md` has no heading, and a CI workflow that runs it.
10. Use `git bisect run` to find the commit where you broke the check on purpose.

*Explain aloud* after each step what Git did. The explanations matter as much as the commands.

## 4. Gaps and fixes

| If you struggle with… | The missing idea is usually… | Go back to |
|---|---|---|
| "My file disappeared after switching" | switching shows the branch's snapshot | G9 M3 (sticky notes) |
| `git status` output | three places | G8 M3, G9 M2 |
| choosing an undo | adding vs rewriting history | G8 M5, G11 M5 |
| conflicts | common ancestor; same lines | G9 M4 |
| rejected pushes | every clone is complete; remote moved | G9 M5 |
| forks vs clones | where each copy lives | G10 M2 |
| detached HEAD | HEAD is a pointer | G9 M3, G12 M1 |
| rebase surprises | rebased commits are new objects | G11 M5, G12 M1 |
| CI fails but works locally | CI starts from a clean machine | G12 M3 |

## 5. Bridge course (4 weeks) { #bridge-course }

For learners who join late or need to rebuild the foundation, and for teachers preparing to teach. About **3 sessions of 60–90 minutes per week**. Each session points to the lessons to use; do the *Understand it*, *See it* and PRIMM parts, and at least one free-resource exercise.

| Week | Session 1 | Session 2 | Session 3 | End-of-week check |
|---|---|---|---|---|
| **1 — My own history** | G8 M1–M2: why version control; snapshots (paper) | G8 M3 + G9 M1–M2: first repo, terminal, CLI cycle | G8 M4–M5: history, diff, restore, revert | foundation test steps 1 and 4 |
| **2 — Parallel and shared** | G9 M3: branches (sticky notes + Learn Git Branching `intro2`) | G9 M4: merge and conflicts | G9 M5: remotes (LAN server or bundles) | steps 2, 3 and 7 |
| **3 — Team work** | G10 M1–M3: issues, forks, PRs | G10 M4–M5: review, PR conflicts | G10 M6, M8: releases, check scripts | a reviewed PR that closes an issue |
| **4 — Professional practice** | G11 M5–M6: stash/reset/rebase/reflog, conventions | G12 M1 + M3: internals, CI | G12 M5 + M7: security, bisect | steps 5, 6, 9 and 10 |

**Fast track for teachers (one weekend):** the [3-hour training outline](../teachers/training-outline.md), then Week 1 and Week 2 of the bridge course on your own laptop, then Learn Git Branching to the end of the Remote tab.

## 6. What comes next

Topics this book does not cover in depth, for university, work and self-study:

| Topic | What it is | Where to start |
|---|---|---|
| Interactive rebase and history editing | reorder, split, squash commits before sharing | *Pro Git* §7.6 Rewriting History |
| Advanced merging | strategies, `rerere`, resolving large conflicts | *Pro Git* §7.8 Advanced Merging |
| Hooks | scripts Git runs on commit, push … | *Pro Git* §8.3 Git Hooks; pre-commit |
| Submodules and subtrees | repositories inside repositories | *Pro Git* §7.11 Submodules |
| Worktrees | several branches checked out at once | `git help worktree` |
| Large files | Git LFS; DVC for data and models | Part VIII §7 |
| Monorepos and scaling | very large repositories, sparse checkout, partial clone | *Software Engineering at Google*, ch. 16 |
| Merge queues and code owners | busy repositories with many PRs | your host's docs |
| GitOps / infrastructure as code | servers and deployments managed by PR | CI/CD docs of your host |
| Running a server | Forgejo/GitLab administration, backups | Forgejo docs; `offline/forgejo-lan/` |
| Maintaining an open-source project | governance, releases, community | *Producing Open Source Software* (Part IX) |

Continue with **Part VIII** to put version control into any project you start, and **Part IX** for books and courses.
