---
id: g10-m02-fork-clone-branch
grade: 10
hours: 1
prerequisites: [g10-m01-issues]
outcomes:
  - "Distinguish fork, clone and branch"
  - "Choose the right one for a situation"
  - "Set up origin and upstream remotes"
tier_support: [2, 3]
license: CC-BY-4.0
---

# 2. Fork vs clone vs branch

!!! abstract "At a glance"
    **Time:** 1 period · **Tiers:** 2–3 (Tier 0 role-play below) · **You need:** the teacher's `school-website-template` repo on the class server

    **Before this:** Grade 9 Module 5 (remotes), Module 1.

    **By the end you can:** explain the three words, pick the right one for a situation, and keep a fork up to date with `upstream`.

## Hook (5 min)
You want to improve a project you do **not** own — say, a Nepali dictionary app made by strangers. You cannot push to their repository. What are your options?

## Understand it

### Three ways to have "your own" version
| | Where it lives | What it is | Who uses it | Made with |
|---|---|---|---|---|
| **branch** | inside one repository | a label for a line of work | people who can **write** to that repository | `git switch -c` |
| **clone** | **your computer** | a full local copy of a repository | everyone — you need one to work at all | `git clone <url>` |
| **fork** | **your account on the server** | a full server-side copy of someone else's repository, linked to the original | people who **cannot write** to the original | the host's *Fork* button |

They are not alternatives so much as **layers**. A visitor contributing to an open-source project uses all three:

```
   [ original repo ]  owner: the project            <- "upstream"
          |  Fork (on the server)
          v
   [ your fork ]      owner: you                    <- "origin"
          |  git clone
          v
   [ your laptop ]    branch: feature/about-page    <- where you work
```

Changes travel back up this ladder: you **push** your branch to your fork (`origin`), then open a **pull request** from your fork to the original (`upstream`) — Module 3.

### Which do I need?
| Situation | Use |
|---|---|
| I'm in the team and have write access | **clone** the team repo, work on a **branch** |
| I want to contribute to a project where I have no write access | **fork**, then clone your fork, work on a branch |
| I want to try an idea for an hour | a **branch** (cheap, delete later) |
| I want my own long-term variant of a template (our school's site from the template) | **fork** (or *Use this template*, which copies without the link) |

### `origin` and `upstream`
When you clone your fork, Git names it `origin` automatically. Add the original project as a second remote, by convention called **`upstream`**:

```bash
git remote add upstream http://school-server/teacher/school-website-template.git
git remote -v
```

To get new work from the original into your fork:

```bash
git switch main
git fetch upstream
git merge upstream/main      # bring the original's new commits into your main
git push origin main         # update your fork on the server
```

Most hosts also have a **"Sync fork"** button that does the same.

## See it
```console
$ git clone http://school-server/s-12/school-website-template.git site
$ cd site
$ git remote add upstream http://school-server/teacher/school-website-template.git
$ git remote -v
origin    http://school-server/s-12/school-website-template.git (fetch)
origin    http://school-server/s-12/school-website-template.git (push)
upstream  http://school-server/teacher/school-website-template.git (fetch)
upstream  http://school-server/teacher/school-website-template.git (push)
$ git switch -c feature/about-page
Switched to a new branch 'feature/about-page'
```

## Unplugged: owners and visitors (10 min)
A poster on the wall is the **original** repo; only two "owners" may write on it. Visitors **photocopy** the poster (fork), take a copy home (clone), and write their idea on a sticky note on *their* copy (branch). To get the idea onto the original, a visitor brings their copy to an owner and asks (pull request). Meanwhile the owners add something new to the poster: visitors must **sync** their copy (fetch + merge upstream).

## PRIMM lab (25 min)
1. Teacher repo `school-website-template`. **Predict** which of fork/clone/branch you need (a) as the owner of your team repo, (b) as a visitor to the teacher's repo.
2. **Fork** the template into your account/organisation (on a LAN Forgejo server: the *Fork* button at the top right).
3. **Clone your fork.** Run `git remote -v`. Add the original as `upstream`: `git remote add upstream <url>`.
4. Create a branch `feature/about-page`. Commit one small change and push it to **origin**: `git push -u origin feature/about-page`.
5. **Investigate:** the teacher now adds a commit to the original. Fetch it (`git fetch upstream`) and look: `git log --oneline main..upstream/main`. Merge it into your `main` and push.
6. **Make:** draw the three copies (original, fork, local) and the arrows (fork, clone, push, fetch upstream, pull request).

## Parsons practice (5 min)
Order: *fork · clone · branch · commit · push to fork*.

## Common mistakes
| Symptom | Cause | Fix |
|---|---|---|
| `Permission denied` / `403` on push | pushing to the original, not your fork | push to `origin` (your fork) |
| Cloned the original instead of the fork | — | `git remote set-url origin <your-fork-url>`, then add `upstream` |
| Fork is "N commits behind" | the original moved on | fetch + merge upstream, or *Sync fork* |
| `upstream` and `origin` mixed up | — | `git remote -v` — origin = yours, upstream = theirs |
| Forked the same repo many times | — | one fork per project; branches inside it |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | *Pro Git* [§6.2 **Contributing to a Project** (GitHub)](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project): read "Forking Projects" and "The GitHub Flow". List its numbered steps. | 3 | 20 min | step list |
| 2 | *Pro Git* [§5.1 **Distributed Workflows**](https://git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows): which of the three workflows does our class use? | 3 | 15 min | answer + reason |
| 3 | Learn Git Branching **Remote** tab: [`remote2` Remote Branches](https://learngitbranching.js.org/?locale=en_US&level=remote2) and `remote3` Git Fetchin'. | 1 / 3 | 15 min | levels done |
| 4 | Atlassian, [**Comparing workflows**](https://www.atlassian.com/git/tutorials/comparing-workflows) — read the "Forking workflow" part. Draw it. | 3 | 15 min | drawing |

## Exit ticket (5 min)
1. When do you need a fork?
2. What is `upstream`?
3. *Misconception:* "A fork is the same as a branch." True or false?

## Key points
- **Branch** = label inside a repo · **clone** = copy on your computer · **fork** = your copy on the server.
- Team member with write access: clone + branch. Outsider: fork + clone + branch.
- `origin` = your fork; `upstream` = the original. Fetch and merge upstream to stay in sync.

## New words
**fork**, **upstream**, **origin**, **sync fork**, **template repository** — see the [glossary](../../glossary.md).

## Extension quest
Find out what `git push -u` (set upstream tracking) changes: after it, what does `git status` say about your branch?

## Teacher notes
- **Timing:** hook 5 · understand 10 · role-play 10 · lab 15 · exit 5. Prepare the template repo and an extra commit to push during lab step 5.
- Students 13+ only create accounts; teacher-managed organisation preferred. On a LAN Forgejo, create pseudonymous accounts in advance.
- **Typical confusion:** `origin` vs `upstream`; also "tracking branch" vs "remote". Keep the ladder diagram on the board.
- **Fallback Tier 1:** forks need a server. Without one, teach the role-play and simulate `upstream` with a second local repo: `git remote add upstream ../teacher-copy`.
- **Answer key:** Exit 1: when you want to contribute to a repo you cannot write to (or keep your own long-term copy on the server). 2: the remote name for the original project you forked from. 3: False — a fork is a whole server-side repository; a branch is a label inside one. Extension: it records the remote branch so `git status` says "ahead/behind 'origin/feature/about-page'" and plain `git push`/`git pull` work.
