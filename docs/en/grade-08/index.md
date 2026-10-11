# Grade 8 — Time Machine for My Work

**Big idea:** every file has a history, and you can go back.
**Length:** ≈ 12 periods (calibrate to CDC hours — unverified). **Accounts:** none; everything stays on the school computer (students may be under 13).
**Tools:** paper and cards (Tier 0) · Git + VS Code or GitHub Desktop, and the self-hosted Learn Git Branching visualiser (Tier 1+).
**Hooks:** file management, digital literacy, basic statistics.

## How this chapter is built
Grade 8 is the **foundation** of the whole book. Students meet one mental model — *a commit is a snapshot of the whole project, with a message, that points to its parent* — first on paper, then on a computer. Everything in Grades 9–12 (branches, remotes, pull requests, CI, internals) is built on that picture, so take time here.

```
 M1  why?               (paper)
 M2  snapshots          (paper cards)
 M3  first repo         (GUI)
 M4  read history       (diff)
 M5  undo               (safe undo)
 M6  statistics         (maths link)
 M7  project            (own work)
```

## Modules
| # | Module | Periods | Tiers | Key commands / actions |
|---|---|---|---|---|
| 1 | [The `final_final_v3` problem](m01-final-final/lesson.md) · [teacher guide](m01-final-final/teacher-guide.md) | 1 | 0–3 | — (unplugged) |
| 2 | [Snapshots = commits](m02-snapshots/lesson.md) · [teacher guide](m02-snapshots/teacher-guide.md) | 2 | 0–3 | paper commits |
| 3 | [My first repo](m03-first-repo/lesson.md) · [teacher guide](m03-first-repo/teacher-guide.md) | 2 | 1–3 | `status`, `add`, `commit` |
| 4 | [Reading history and comparing versions](m04-history-diff/lesson.md) · [teacher guide](m04-history-diff/teacher-guide.md) | 2 | 0–3 | `log`, `show`, `diff` |
| 5 | [Undo and restore](m05-undo-restore/lesson.md) · [teacher guide](m05-undo-restore/teacher-guide.md) | 2 | 0–3 | `restore`, `revert` |
| 6 | [Statistics: chart my commits](m06-stats-commits/lesson.md) · [teacher guide](m06-stats-commits/teacher-guide.md) | 1 | 0–3 | `log --format` |
| 7 | [Mini-project: Class Magazine](m07-mini-project/lesson.md) · [teacher guide](m07-mini-project/teacher-guide.md) | 2 | 0–3 | everything |

Printable materials: [cards, Parsons strips and badges](cards.md).

## Chapter outcomes
By the end, a student can:

1. explain why keeping many copies of a file by renaming is risky;
2. explain a commit as a saved snapshot with a message;
3. create a repo, make commits, and read the history;
4. compare two versions and say what changed;
5. restore an earlier version of a file and undo a commit safely;
6. present a bar chart of their own commit counts.

## Free resources used in this chapter
All Grade 8 exercises work **without an account**. The main ones: [Learn Git Branching](https://learngitbranching.js.org/) (self-hosted copy for offline labs), Software Carpentry's [git-novice](https://swcarpentry.github.io/git-novice/) episodes 1, 4 and 5 (CC BY, may be printed), [*Pro Git*](https://git-scm.com/book/en/v2) chapters 1–2 (link only), and the [VS Code Source Control docs](https://code.visualstudio.com/docs/sourcecontrol/overview). The full list with licences is in the [free resource library](../book/resources.md).

## Assessment
- Exit tickets in every lesson.
- **Commit-history rubric:** ≥ 5 meaningful commits, each message says *what and why*, no commit larger than one idea.
- Oral explanation (2 minutes): "show me how you would get yesterday's version back."
- Board-style item bank: `assessments/g08-item-bank.md`.

## Capstone
**Class Magazine:** each student keeps one article's history; the class exhibits the "evolution" of an article. Practice repo: `practice-repos/g08-class-magazine/`.

## Ready for Grade 9?
A student is ready when they can, without help: make three commits with good messages; find who/when/why for a change; and choose between *restore* and *revert*. Students who cannot yet should repeat Modules 3–5 with a buddy at the start of Grade 9 (the [bridge course](../book/after-grade-12.md#bridge-course) also covers this).
