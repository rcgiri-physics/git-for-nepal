---
id: g11-m02-reading-a-project
grade: 11
hours: 1
prerequisites: [g11-m01-licences]
outcomes:
  - "Find how to run, how to contribute and what is being worked on in an unfamiliar repo"
  - "Use git log, git grep and the file tree to orient yourself"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 2. Reading a project: README, CONTRIBUTING, issues

!!! abstract "At a glance"
    **Time:** 1 period · **Tiers:** 1 (clone from bundle), 2–3 · **You need:** a clone of this book's repository (or a teacher-vetted partner project); the treasure-hunt worksheet

    **Before this:** Module 1.

    **By the end you can:** open an unfamiliar repository and, in 30 minutes, know what it is, how to run it, how to contribute, and what is being worked on.

## Hook (5 min)
You join a new club. Before you speak at the first meeting, you read the notice board: rules, who is in charge, what is planned. A repository's notice board is its **README**, **CONTRIBUTING** file, **licence** and **issues**.

## Understand it

### The standard files
Most healthy open-source projects have the same set of files at the top level. Learn to look for them first:

| File | Answers | In this book's repo |
|---|---|---|
| `README.md` | What is it? How do I run/build it? | yes |
| `CONTRIBUTING.md` | How do I help? Branch names, checks, review rules | yes |
| `LICENSE` | What may I do with it? (Module 1) | `LICENSE`, `LICENSE-CONTENT.md` |
| `CODE_OF_CONDUCT.md` | How must people behave? | yes |
| `GOVERNANCE.md` | Who decides? How? | yes |
| `SECURITY.md` | How to report a security or privacy problem privately | yes |
| `CHANGELOG.md` | What changed in each version? | yes |
| `CITATION.cff` | How to cite it in research | yes |
| `.github/` | issue/PR templates, CI workflows, code owners | yes |

### A reading strategy (30 minutes)
1. **README** — one sentence: what is this project for?
2. **LICENSE** — may I contribute and reuse?
3. **CONTRIBUTING** — the rules for a first contribution; checks to run.
4. **Folder tree** — where do the main things live? (`ls`, or the server's file view)
5. **Recent history** — `git log --oneline -15`: how do maintainers write messages? What is active?
6. **Issues** — labels such as `good-first-issue`; what is being discussed?
7. **Pull requests** — how are they reviewed? How long do they wait?
8. **Run it** — follow the README's build steps. If they fail, *that* might be your first contribution (improving the README)!

### Git commands for orientation
| Question | Command |
|---|---|
| What are the top-level folders? | `ls` / `git ls-files \| head` |
| What changed recently? | `git log --oneline -15` |
| Who works on what? | `git shortlog -s -n` |
| Where is a word or function used? | `git grep "word"` |
| What is the history of one file? | `git log --oneline -- path/to/file` |
| How big is the project? | `git ls-files \| wc -l` |

`git grep` searches only tracked files and is much faster than searching the folder by hand.

### Is this project healthy?
Signs of a welcoming project: a clear README and CONTRIBUTING, recent commits, issues that get replies, labels for beginners, a code of conduct. Warning signs: no licence, no activity for years, unanswered issues, rude comments. Contribute where you will be welcome.

## See it
Orienting in this book's repository:

```console
$ git clone https://github.com/rcgiri-physics/git-for-nepal.git
$ cd git-for-nepal
$ ls
ATTRIBUTION.md      CONTRIBUTING.md  README.md     alignment/    offline/
CHANGELOG.md        GOVERNANCE.md    ROADMAP.md    assessments/  practice-repos/
CODE_OF_CONDUCT.md  LICENSE          SECURITY.md   docs/         research/  tools/ ...
$ grep -n "good-first-issue" CONTRIBUTING.md
6:1. Open an issue using a template in `.github/ISSUE_TEMPLATE/`, or pick one labelled `good-first-issue`.
$ git grep -l "PRIMM" -- docs/en | head -3
docs/en/grade-08/m01-final-final/lesson.md
docs/en/grade-08/m02-snapshots/lesson.md
docs/en/grade-08/m03-first-repo/lesson.md
```

## Unplugged: the notice-board hunt (10 min, Tier 0 option)
Print `README.md`, `CONTRIBUTING.md` and the first page of `git log --oneline` of this repository. Pin them on the wall like a notice board. Teams race to answer the worksheet questions using only the printouts.

## PRIMM lab (30 min)
1. Open this repo (on the server, or your clone). Answer the 8 questions on the worksheet:
    1. What is the project for, in one sentence?
    2. How do I build the website locally?
    3. Which licence covers the lessons, and which covers the code?
    4. What label marks easy tasks?
    5. Which two checks must pass before a PR?
    6. Who must approve a new module?
    7. Which label asks for a Nepali reviewer?
    8. What was the last thing changed, and by whom?
2. **Predict** where a typo fix should go (branch? issue first?). Check `CONTRIBUTING.md`.
3. Read `git log` for how maintainers write messages. Copy two good examples.
4. **Investigate:** use `git grep` to find every lesson that mentions `bisect`.
5. **Make:** write a 5-line "how to contribute" summary in your own words.

## Parsons practice (5 min)
Order the first steps on a new project: *read README · read CONTRIBUTING · check issues · build/run · ask*.

## Common mistakes
| Mistake | Fix |
|---|---|
| Starting to change code before reading CONTRIBUTING | read it first; it may require an issue first |
| Ignoring the licence | Module 1: check you may contribute and reuse |
| Choosing an inactive project | check recent commits and issue replies |
| Getting lost in a big project | follow the 30-minute strategy; ask in the issue |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Open Source Guides, [**How to Contribute**](https://opensource.guide/how-to-contribute/) — section "Orienting yourself to a new project". Compare its checklist with ours. | 3 | 20 min | 2 differences |
| 2 | Apply the 30-minute strategy to [First Contributions](https://github.com/firstcontributions/first-contributions). Find its Nepali README. | 3 | 30 min | answers |
| 3 | *Pro Git* [§7.5 **Searching**](https://git-scm.com/book/en/v2/Git-Tools-Searching): try `git grep -n` and `git log -S "word"`. | 1 / 3 | 15 min | commands + output |
| 4 | Pick a Nepali open project (e.g. [OKN localboundaries](https://github.com/openknowledgenp/localboundaries)). Answer worksheet questions 1, 3 and 8 for it. | 3 | 20 min | answers |

## Exit ticket (5 min)
1. Which file tells you how to contribute?
2. Where do you look for easy tasks?
3. *Misconception:* "Just send a PR without reading anything."

## Key points
- Read the standard files first: README, LICENSE, CONTRIBUTING, CODE_OF_CONDUCT.
- Follow a strategy: purpose → licence → rules → tree → history → issues → PRs → run.
- `git log`, `git shortlog`, `git grep` orient you fast.
- Choose healthy, welcoming projects.

## New words
**CONTRIBUTING file**, **code of conduct**, **governance**, **`git grep`**, **maintainer** — see the [glossary](../../glossary.md).

## Extension quest
Draw a map of this repository's folders (like Grade 9 Module 1's tree) with one line describing each folder.

## Teacher notes
- **Timing:** hook 5 · understand 10 · lab 30 · Parsons + exit 5. Use the notice-board hunt if computers are limited.
- **Students under 18 should only contribute to projects the teacher has vetted** (this repo and consented partners).
- **Worksheet answers (this repo):** 1 open offline-first Git curriculum for Nepali schools, Grades 8–12; 2 `pip install -r requirements.txt` then `mkdocs serve`; 3 CC BY 4.0 / MIT; 4 `good-first-issue` (and `student-friendly`); 5 `validate_frontmatter.py` and `mkdocs build --strict`; 6 two approvals including one teacher; 7 `needs-nepali-review`; 8 read from `git log -1`.
- **Answer key:** Exit 1: `CONTRIBUTING.md`. 2: issues labelled `good-first-issue` / `student-friendly`. 3: False — read the rules first.
