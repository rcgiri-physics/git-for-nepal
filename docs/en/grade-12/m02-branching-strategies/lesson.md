---
id: g12-m02-branching-strategies
grade: 12
hours: 2
prerequisites: [g12-m01-internals]
outcomes:
  - "Compare trunk-based development, feature branches and Gitflow"
  - "Choose a strategy for a project and justify it"
  - "Explain branch protection and feature flags"
tier_support: [0, 1, 2, 3]
license: CC-BY-4.0
---

# 2. Branching strategies

!!! abstract "At a glance"
    **Time:** 2 periods · **Tiers:** 0–3 · **You need:** chart paper, `practice-repos/g12-capstone-starter`

    **Before this:** Grade 10 (PRs), Grade 11 Modules 5–7.

    **By the end you can:** describe the main team branching strategies, match them to project types, and write your capstone's strategy with reasons.

## Hook (5 min)
A team of 3 building a school website and a team of 300 building a banking app should not work the same way. Neither should a library that must keep fixing version 1 while version 2 is being built. How do teams decide how to use branches?

## Understand it

### A strategy answers four questions
1. Which branch holds the **truth** (what we release)?
2. Where does **new work** happen, and for how long?
3. How do we **release**, and how do we **fix** a released version?
4. What **rules** protect the important branches?

### Trunk-based development
Everyone integrates into one branch (**trunk** = `main`) at least daily. Branches are tiny (hours, a day) or don't exist at all. Unfinished features are merged but hidden behind **feature flags** (an `if` that switches a feature on or off). Strong CI is essential.

```
 main: --o--o--o--o--o--o--o--o--o-->   (many small merges per day)
          \/    \/       \/
```

Good for: teams with good tests and CI, web apps deployed often. Fewest conflicts (nothing lives long enough to drift).

### Feature branches + pull requests (GitHub flow)
`main` is always releasable. Each feature or fix gets a short branch and a PR with review and CI; merge, deploy, delete the branch. This is what you did in Grades 10–11.

```
 main: --o-----------o--------o------->
          \         /  \      /
           o--o--o-'    o--o-'          (one branch per issue, days long)
```

Good for: most small and medium teams, school projects, open-source projects (with forks).

### Gitflow
Two long-lived branches — `main` (released versions only, tagged) and `develop` (integration) — plus `feature/*`, `release/*` (stabilising a version) and `hotfix/*` (urgent fix to a released version) branches.

```
 main:    --o-----------------o-------o---->   (v1.0)        (v1.1)   (v1.1.1 hotfix)
             \               /       /|
 develop:     o--o--o--o--o-'--o--o-'-+---->
                \     /
 feature:        o--o
```

Good for: software with planned, versioned releases (installed apps). Costs: more branches, more merges, slower integration. Its own author later said that teams doing continuous delivery should prefer a simpler flow.

### Release branches for long support
Libraries or operating systems that support old versions keep **release branches** (`release/1.x`, `release/2.x`) and **cherry-pick** fixes into them (Grade 11 Module 5 extension).

### Comparison
| | Trunk-based | Feature branches (GitHub flow) | Gitflow |
|---|---|---|---|
| Long-lived branches | `main` only | `main` only | `main` + `develop` |
| Branch lifetime | hours | days | days–weeks |
| Releases | continuous | continuous / tagged | planned versions |
| Conflict risk | lowest | low | higher |
| Needs strong CI | essential | important | helpful |
| Team size | any (with discipline) | small–large | medium–large |

### Rules that protect branches
Hosts let you **protect** important branches: no direct pushes, no force pushes, require a PR with *N* approvals, require CI to pass, require branches to be up to date. A **CODEOWNERS** file names who must review which folders (this book has `.github/CODEOWNERS`). A strategy is only real when these rules enforce it.

## See it
Simulating trunk-based with feature flags in the capstone starter:

```python
# settings.py
SHOW_DENSITY_REPORT = False      # flag: merged to main, but hidden until ready

# report.py
if SHOW_DENSITY_REPORT:
    print_density_report()
```

```console
$ git log --oneline --graph -8
* 4a1e2f0 Turn on density report (flag = True)
* 91b3c77 Add density report behind flag
* 2c8d1a5 Add tests for density calculation
* ...
```

The feature arrived in small, safe merges; switching it on was a one-line change that is easy to revert.

## Unplugged: strategy posters (25 min)
Teams of three each get one strategy and chart paper. Draw its history graph for a 4-week project with two features, one release and one urgent fix to the released version. Present in 2 minutes. The class asks: *Where do conflicts happen? How long does a feature wait? How is the urgent fix made?*

## PRIMM lab (40 min)
1. Given 3 project descriptions — (a) the school website, updated weekly by 4 students; (b) a mobile app released to an app store monthly; (c) a library used by many schools, where version 1 must still get fixes while version 2 is built — **predict** the best strategy for each and write one reason.
2. Simulate one strategy with the practice repo `g12-capstone-starter` for 10 minutes in your team (two features, one release tag, one hotfix).
3. **Investigate:** count branches, merges and conflicts (`git log --oneline --graph --all`, `git log --merges --oneline | wc -l`).
4. **Investigate:** turn on branch protection for `main` on the class server (require PR + 1 approval + CI). Try to push directly — what happens?
5. **Make:** write the strategy for your capstone in `CONTRIBUTING.md`: the four questions answered, plus the protection rules.

## Parsons practice (5 min)
Match strategy to its signature: daily merges → trunk-based; release/hotfix branches → Gitflow; one branch per PR, main always releasable → feature branches; support old versions → release branches.

## Common mistakes
| Mistake | Better |
|---|---|
| Choosing Gitflow because it "looks professional" | choose by release style and team size |
| Feature branches that live for weeks | small PRs; merge `main` in often |
| Feature flags never removed | delete the flag once the feature is on |
| Strategy written but not enforced | branch protection + CODEOWNERS |
| Hotfix made only on `main`, forgotten on `develop` | Gitflow: merge hotfixes into both |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Atlassian, [**Comparing workflows**](https://www.atlassian.com/git/tutorials/comparing-workflows) — read the Gitflow and forking sections. List two costs of Gitflow. | 3 | 20 min | 2 costs |
| 2 | *Pro Git* [§3.4 **Branching Workflows**](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows) — draw the "progressive-stability branching" figure as a graph. | 3 | 15 min | drawing |
| 3 | Learn Git Branching [`move1` Cherry-pick Intro](https://learngitbranching.js.org/?locale=en_US&level=move1) — used for back-porting fixes to release branches. | 1 / 3 | 10 min | level done |
| 4 | GitHub Skills [**Release-based workflow**](https://github.com/skills/release-based-workflow) (13+, account). | 3 | 45 min | completed course |
| 5 | Read this book's `.github/CODEOWNERS` and `CONTRIBUTING.md`. Which strategy does the book use? | 1 | 10 min | answer + evidence |

## Exit ticket (5 min)
1. Which strategy suits a team of three?
2. What is a feature flag?
3. *Misconception:* "Gitflow is always the professional choice."

## Key points
- A strategy answers: where is truth, where is new work, how to release, how to fix, which rules.
- **Trunk-based** (tiny branches + flags + CI) · **feature branches/GitHub flow** (PR per change) · **Gitflow** (develop/release/hotfix) · **release branches** (old versions).
- Choose by team size, release style and CI strength; justify it.
- Enforce with branch protection and CODEOWNERS.

## New words
**trunk-based development**, **feature flag**, **GitHub flow**, **Gitflow**, **release branch**, **hotfix**, **branch protection**, **CODEOWNERS**, **cherry-pick** — see the [glossary](../../glossary.md).

## Extension quest
Design a strategy for a national open-data portal where data files are updated by 10 district offices. Which strategy, and what protection rules?

## Teacher notes
- **Timing:** P1: hook 5, understand 20, posters 15. P2: lab 35, Parsons + exit 5.
- **No single correct answer; grade the reasoning.** Suggested answers: (a) feature branches/GitHub flow; (b) feature branches with release tags, or Gitflow; (c) release branches with cherry-picked fixes.
- Branch protection needs maintainer/admin rights on the class server — set it up yourself if students cannot.
- **Answer key:** Exit 1: feature branches (GitHub flow) or trunk-based — with reasons. 2: a switch in the code that turns a feature on/off, so unfinished work can be merged safely. 3: False — it suits planned versioned releases; it adds overhead elsewhere.
