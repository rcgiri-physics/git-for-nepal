# Free resource library

Every lesson in this book has a **"Practise more with free resources"** section. This page is the full catalogue those exercises come from. Every link was opened and returned a working page on **11 October 2026**; licences were read from each project's own licence file where one exists.

!!! warning "Link, don't copy"
    This book is CC BY 4.0. Many excellent resources are **NonCommercial (NC)** or **ShareAlike (SA)**. You may *use* them freely in class and send students to them, but their text must **not be pasted into this book or into printed copies of it**. The "Copy into our book?" column says which ones are safe to adapt with credit.

## How to read the tables

- **Grades** — where the resource fits best in this book.
- **Tier** — the delivery tiers from the [Teacher hub](../teachers/index.md): 0 no computer · 1 offline computers · 2 school LAN · 3 internet.
- **Account** — whether a learner must sign up. Learners under 13 (most of Grade 8) must never need an account.

## 1. Visual sandboxes (see the commit graph move)

| Resource | Good for | Grades | Tier | Account | Licence · Copy into our book? |
|---|---|---|---|---|---|
| [Learn Git Branching](https://learngitbranching.js.org/) ([source](https://github.com/pcottle/learnGitBranching)) | Commits, branches, merge, rebase, remotes as an animated graph; levels with goals; a free "sandbox" | 8–12 | 1 (self-hosted, see `offline/usb-kit/`) or 3 | none | MIT · yes |
| [Visualizing Git](https://git-school.github.io/visualizing-git/) ([source](https://github.com/git-school/visualizing-git)) | Type real commands, watch the graph; good for teacher demos on a projector | 9–12 | 3 (or saved copy) | none | MIT · yes |
| [Oh My Git!](https://ohmygit.org/) ([source](https://github.com/git-learning-game/oh-my-git)) | Card game on top of *real* Git repositories; Windows/Linux/macOS download | 9–10 | 1 after download | none | Blue Oak Model 1.0.0 (permissive) · yes for code; check art |

### Learn Git Branching level map
Levels are opened with `?level=<id>` (online: `https://learngitbranching.js.org/?locale=en_US&level=intro1`). The same ids work in the self-hosted copy.

| Level id | Name (Main / Remote tab) | Used in |
|---|---|---|
| `intro1` | Introduction to Git Commits | G8 M2, G8 M3 |
| `intro2` | Branching in Git | G9 M3 |
| `intro3` | Merging in Git | G9 M4 |
| `intro4` | Rebase Introduction | G11 M5 |
| `rampup1` – `rampup4` | Detach yo' HEAD · Relative Refs (^) · Relative Refs #2 (~) · Reversing Changes in Git | G9 M3 (`rampup1`), G11 M5 (`rampup4`), G12 M1 |
| `move1`, `move2` | Cherry-pick Intro · Interactive Rebase Intro | G11 M5, G12 M2 |
| `mixed4`, `mixed5` | Git Tags · Git Describe | G10 M6, G12 M4 |
| `remote1` – `remote8` | Clone Intro · Remote Branches · Git Fetchin' · Git Pullin' · Faking Teamwork · Git Pushin' · Diverged History · Locked Main | G9 M5, G10 M2–M3 |

Type `levels` inside the app to see the full list, and `sandbox` to leave a level and experiment freely.

## 2. Structured free courses

| Resource | Good for | Grades | Tier | Account | Licence · Copy? |
|---|---|---|---|---|---|
| [Software Carpentry: Version Control with Git](https://swcarpentry.github.io/git-novice/) | 13 short episodes with exercises and solutions; written for adults but very clear | 9–12, teachers | 1 (download the site) / 3 | none (GitHub episode needs one) | CC BY 4.0 · **yes, with credit** |
| [Software Carpentry: The Unix Shell](https://swcarpentry.github.io/shell-novice/) | Terminal basics (`cd`, `ls`, files, pipes, scripts) | 9 | 1 / 3 | none | CC BY 4.0 · **yes, with credit** |
| [GitHub Skills](https://skills.github.com/) | Self-checking courses that run inside a GitHub repo: [Introduction to GitHub](https://github.com/skills/introduction-to-github), [Communicate using Markdown](https://github.com/skills/communicate-using-markdown), [GitHub Pages](https://github.com/skills/github-pages), [Review pull requests](https://github.com/skills/review-pull-requests), [Resolve merge conflicts](https://github.com/skills/resolve-merge-conflicts), [Hello GitHub Actions](https://github.com/skills/hello-github-actions), [Release-based workflow](https://github.com/skills/release-based-workflow), [Secure your repository's supply chain](https://github.com/skills/secure-repository-supply-chain) | 9–12 (13+) | 3 | **GitHub, 13+** | MIT · yes for course text |
| [MIT "Missing Semester": Version Control](https://missing.csail.mit.edu/2020/version-control/) and [Shell Tools](https://missing.csail.mit.edu/2020/shell-tools/) | University-level lecture + exercises; explains the data model (blobs, trees, commits) beautifully | 11–12, teachers | 3 (videos) | none | CC BY-NC-SA 4.0 · **link only** |
| [The Odin Project: Git Basics](https://www.theodinproject.com/lessons/foundations-git-basics) | Self-paced web-developer track with a Git lesson and project | 10–12 | 3 | optional | open curriculum · link only |
| [Atlassian Git tutorials](https://www.atlassian.com/git/tutorials) and [workflow comparison](https://www.atlassian.com/git/tutorials/comparing-workflows) | Clear diagrams of workflows (feature branch, Gitflow, forking) | 10–12 | 3 | none | Atlassian site terms · link only |
| [Git Immersion](https://gitimmersion.com/) | Step-by-step labs, one command at a time | 9–10 | 3 | none | free online · link only |
| [W3Schools Git tutorial](https://www.w3schools.com/git/) | Short pages with "try it" exercises; good for revision | 9–10 | 3 | none (optional) | site terms · link only |
| [CS50 Web, Lecture 1: Git](https://cs50.harvard.edu/web/2020/weeks/1/) | Free university lecture video + notes | 11–12 | 3 | none | Harvard CS50 terms · link only |

### Software Carpentry episode map
| Episode | Topic | Used in |
|---|---|---|
| [1 Automated Version Control](https://swcarpentry.github.io/git-novice/01-basics.html) | why version control | G8 M1 |
| [2 Setting Up Git](https://swcarpentry.github.io/git-novice/02-setup.html) | `git config` | G8 M3, G9 M2 |
| [3 Creating a Repository](https://swcarpentry.github.io/git-novice/03-create.html) | `git init` | G8 M3, G9 M2 |
| [4 Tracking Changes](https://swcarpentry.github.io/git-novice/04-changes.html) | add, commit, staging area | G8 M3, G9 M2 |
| [5 Exploring History](https://swcarpentry.github.io/git-novice/05-history.html) | `log`, `diff`, `restore` | G8 M4, G8 M5 |
| [6 Ignoring Things](https://swcarpentry.github.io/git-novice/06-ignore.html) | `.gitignore` | G9 M6 |
| [7 Remotes in GitHub](https://swcarpentry.github.io/git-novice/07-github.html) | push, pull | G9 M5 |
| [8 Collaborating](https://swcarpentry.github.io/git-novice/08-collab.html) | two people, one repo | G9 M8, G10 M2 |
| [9 Conflicts](https://swcarpentry.github.io/git-novice/09-conflict.html) | merge conflicts | G9 M4, G10 M5 |
| [10 Open Science](https://swcarpentry.github.io/git-novice/10-open.html) | research with Git | G11 M8 |
| [11 Licensing](https://swcarpentry.github.io/git-novice/11-licensing.html) | choosing a licence | G11 M1 |
| [12 Citation](https://swcarpentry.github.io/git-novice/12-citation.html) | `CITATION.cff` | G11 M8, G12 M4 |
| [13 Hosting](https://swcarpentry.github.io/git-novice/13-hosting.html) | where to host | G9 M5, G12 M9 |

## 3. Reference books and documentation

| Resource | Good for | Grades | Tier | Licence · Copy? |
|---|---|---|---|---|
| [*Pro Git*, 2nd ed.](https://git-scm.com/book/en/v2) (Chacon & Straub) | The standard free Git book; downloadable as PDF/EPUB for offline labs | 9–12, teachers | 1 (PDF on USB) / 3 | CC BY-NC-SA 3.0 · **link only** |
| [Git reference manual](https://git-scm.com/docs) and [cheat sheet](https://git-scm.com/cheat-sheet) | Exact meaning of every command and option (also offline: `git help <command>`) | 9–12 | 1 / 3 | GPL-2.0 docs · link only |
| [*Git from the Bottom Up*](https://jwiegley.github.io/git-from-the-bottom-up/) (Wiegley) | Internals explained from blobs upward | 12 | 3 | CC BY 4.0 · yes, with credit |
| [*Think Like (a) Git*](https://think-like-a-git.net/) | Graph thinking: "Git is a graph, branches are labels" | 11–12 | 3 | free online · link only |
| [GitHub Docs](https://docs.github.com/en/get-started/start-your-journey/hello-world) | Accounts, pull requests, Actions, Pages | 9–12 | 3 | CC BY 4.0 ([licence](https://github.com/github/docs/blob/main/LICENSE)) · yes, with credit |
| [GitHub Desktop docs](https://docs.github.com/en/desktop) | GUI path for Grade 8–9 | 8–9 | 1 / 3 | CC BY 4.0 · yes |
| [VS Code: Source Control](https://code.visualstudio.com/docs/sourcecontrol/overview) | Commit, diff and branch from inside the editor | 8–10 | 1 / 3 | CC BY 3.0 US · yes, with credit |
| [Codeberg docs](https://docs.codeberg.org/), [Forgejo docs](https://forgejo.org/docs/latest/), [GitLab Git docs](https://docs.gitlab.com/topics/git/) | Same ideas on non-GitHub hosts (Forgejo = our school-LAN server) | 9–12 | 2 / 3 | various open licences · link |
| [Markdown Guide](https://www.markdownguide.org/) and [CommonMark 10-minute tutorial](https://commonmark.org/help/tutorial/) | Writing READMEs and documentation | 9–10 | 3 | open · link |

## 4. Rescue guides ("I broke it!")

| Resource | Good for | Grades | Licence · Copy? |
|---|---|---|---|
| [Oh Shit, Git!?](https://ohshitgit.com/) and its polite twin [Dangit, Git!?](https://dangitgit.com/) | Short fixes for the most common mistakes. **Use the "Dangit" version with school students.** | 10–12 | no stated licence · link only |
| [Git Flight Rules](https://github.com/k88hudson/git-flight-rules) | Huge "what to do when…" manual | 11–12, teachers | CC BY-SA 4.0 · link only (SA) |
| [Julia Evans: confusing Git terminology](https://jvns.ca/blog/2023/11/01/confusing-git-terminology/) | Why words like *HEAD*, *origin* and *reset* confuse people | 11–12, teachers | blog · link only |
| [explainshell](https://explainshell.com/) | Paste a shell command, see what every part means | 9–12 | open source · link |

Our own rescue guide is [Appendix B: Troubleshooting](troubleshooting.md).

## 5. Open-source contribution and project hygiene

| Resource | Good for | Grades | Account | Licence · Copy? |
|---|---|---|---|---|
| [First Contributions](https://firstcontributions.github.io/) ([repo](https://github.com/firstcontributions/first-contributions)) | A safe practice repo for the first fork → PR, in many languages (including Nepali) | 11 (13+) | GitHub | MIT · yes |
| [Open Source Guides](https://opensource.guide/) — esp. [How to Contribute](https://opensource.guide/how-to-contribute/) | Etiquette, finding issues, being a good contributor | 11–12 | none | CC BY 4.0 · yes, with credit |
| [choosealicense.com](https://choosealicense.com/) | Picking a licence in plain words | 11 | none | MIT · yes |
| [SPDX licence list](https://spdx.org/licenses/), [REUSE](https://reuse.software/), [Creative Commons BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Exact licence identifiers; marking every file's licence | 11–12 | none | open · link |
| [Semantic Versioning](https://semver.org/) | MAJOR.MINOR.PATCH rules | 10, 12 | none | CC BY 3.0 · yes, with credit |
| [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) | Changelog format | 10–12 | none | MIT · yes |
| [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) | `feat:`, `fix:` message convention | 11–12 | none | MIT (site repo) · yes |
| [Citation File Format](https://citation-file-format.github.io/) | `CITATION.cff` so others can cite your work | 11–12 | none | open · link |
| [github/gitignore](https://github.com/github/gitignore) | Ready-made `.gitignore` templates for Python, Node, Java, LaTeX… | 9–12 | none | CC0 · yes |
| [Hacktoberfest](https://hacktoberfest.com/) | October contribution event (check the current year's age rules) | 11–12 | yes | event · link |

## 6. Automation, quality and security

| Resource | Good for | Grades | Tier | Licence |
|---|---|---|---|---|
| [GitHub Actions docs](https://docs.github.com/en/actions) | CI workflows | 10–12 | 3 | CC BY 4.0 |
| [Forgejo Actions](https://forgejo.org/docs/latest/user/actions/) | CI on a school LAN server | 10–12 | 2 | open |
| [pre-commit](https://pre-commit.com/) | Run checks before every commit | 12 | 1 after install | MIT |
| [gitleaks](https://github.com/gitleaks/gitleaks) | Find passwords and keys committed by mistake | 12 | 1 after install | MIT |
| [OpenSSF Scorecard](https://scorecard.dev/) | Security health score of an open-source project | 12 | 3 | Apache-2.0 |
| [Git LFS](https://git-lfs.com/) | Large binary files (images, video, models) | 12, any project | 1 / 3 | MIT |

## 7. Research, data and writing

| Resource | Good for | Grades | Licence · Copy? |
|---|---|---|---|
| [The Turing Way: Version Control](https://book.the-turing-way.org/reproducible-research/vcs) | Version control for research and data, with clear illustrations | 11–12, after school | CC BY 4.0 · yes, with credit |
| Blischak, Davenport & Wilson (2016), [*A Quick Introduction to Version Control with Git and GitHub*](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004668), PLOS Comp. Biol. | Short paper; ideal first reading for science teachers | teachers, 12 | CC BY 4.0 · yes, with credit |
| Perez-Riverol et al. (2016), [*Ten Simple Rules for Taking Advantage of Git and GitHub*](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004947) | Practical rules for projects | 12, after school | CC BY 4.0 · yes, with credit |
| [Happy Git and GitHub for the useR](https://happygitwithr.com/) (Bryan) | Git for data analysis (R users, but most chapters are general) | after school | CC BY-NC 4.0 · link only |
| [Our Coding Club: Git for reproducible research](https://ourcodingclub.github.io/tutorials/git/) | Step-by-step tutorial for scientists | 11–12 | see site · link only |
| [DVC: Get started](https://dvc.org/doc/start) | Versioning large datasets and ML models next to Git | after school | Apache-2.0 docs |
| [Overleaf Git integration](https://www.overleaf.com/learn/how-to/Git_integration) | Version-controlled LaTeX papers and theses | after school | site terms |
| [nbdime](https://nbdime.readthedocs.io/) | Readable diffs of Jupyter notebooks | 11–12 | BSD |
| [Open Data Nepal](https://opendatanepal.com/), [OKN localboundaries](https://github.com/openknowledgenp/localboundaries) | Nepali open data for the data thread (check each dataset's licence) | 9–12 | per dataset |

## 8. For teachers: pedagogy

| Resource | Good for | Licence |
|---|---|---|
| Wilson, [*Teaching Tech Together*](https://teachtogether.tech/) | How people learn programming; lesson design; live coding | CC BY-NC 4.0 · link only |
| [CS Unplugged](https://csunplugged.org/en/) | Computing without computers; ideas for Tier 0 | open licence (check per activity) · link only |
| [Parsons problem tool](https://parsons.problemsolving.io/) | Make drag-and-drop Parsons puzzles | open source |
| [Wizard Zines comics](https://wizardzines.com/comics/) | Hand-drawn one-page explanations (several on Git) — good poster inspiration | free to view · link only |
| [GitHub Education](https://docs.github.com/en/education) and [GitHub Classroom](https://classroom.github.com/) | Free teacher accounts, assignment repos with autograding | service terms |

## 9. Offline packing list (Tier 1 USB kit)

Put these on the school USB stick alongside the kit in `offline/usb-kit/`:

1. Git for Windows (portable) and VS Code (portable).
2. The self-hosted **Learn Git Branching** build (`build-learngitbranching.sh`).
3. **Pro Git** PDF (download from the book page; NC licence allows sharing for non-commercial school use — do not sell copies).
4. A saved copy of the **Software Carpentry** git-novice and shell-novice sites (CC BY 4.0).
5. **Oh My Git!** installers for the lab's operating systems.
6. This book's PDF and the practice-repo `.bundle` files.

*Check before every school year: links change, courses move, and age rules for events and programmes are updated.*
