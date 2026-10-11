# The Git for Nepal Book — Plan

> Plan date: 2026-10-11 · Owner: Ram Chandra Giri · Executor: Claude (Opus 5.5) + humans
> Progress is tracked in [`STATUS.md`](STATUS.md). If a work session ends, the next one starts by reading STATUS.md and continuing from the first unchecked item.

## 1. What we are making

One open book, **"Teaching Version Control: A Foundation Book for Grades 8–12"**, that

- a **student** can follow alone, lesson by lesson, from "what is a version?" (Grade 8) to running a team capstone with CI (Grade 12);
- a **teacher** can teach from, with timings, misconceptions, fallbacks for no-computer rooms, answer keys and rubrics;
- a **school, university or project lead** can use after Grade 12 to adopt version control in *any* project (code, writing, data, research, design, hardware).

It is published in two forms from the same Markdown:

1. the **website** (MkDocs, already exists) — every page updated in place;
2. a **printable PDF** (`book/dist/git-for-nepal-book.pdf`) built by `tools/build_book.py`, with cover, table of contents with page numbers, part dividers, and print-friendly styling (works on a B&W printer).

## 2. Principles (do not break these)

| Rule | Why |
|---|---|
| Concept before commands; PRIMM lesson skeleton stays | evidence base in `research/sources.md` (S7, S8) |
| Every lesson must still work at its listed delivery tiers (0–3) | offline-first is a hard requirement |
| Free resources are **linked, never copied** unless their licence is CC BY / MIT / CC0 compatible with our CC BY 4.0 | Pro Git (CC BY-NC-SA), Missing Semester (CC BY-NC-SA), Teaching Tech Together (CC BY-NC) cannot be pasted into a CC BY book |
| Every external link is checked (HTTP 200) on the date it is added; licence recorded in the resource library | trust; avoid dead links in print |
| Under-13 learners (Grade 8) never need an online account; GitHub Skills etc. are marked "13+, internet" | GitHub ToS (S4), privacy rules in SECURITY.md |
| Commands and code stay in English; Nepali full text is a later phase | D4 in the original plan |
| No promises about jobs, admissions or programme acceptance | existing policy in `pathways.md` |
| Front-matter keys stay valid for `tools/validate_frontmatter.py`; `mkdocs build --strict` and `tools/check_links.py` must pass | CI |

## 3. Work packages

### WP1 — Free-resource library (do first; lessons link to it)
- `docs/en/book/resources.md`: catalogue of verified free resources — name, link, what it is good for, grade fit, delivery tier (offline?), age/account needs, licence, "can we copy it?".
  Groups: visual sandboxes (learnGitBranching, Visualizing Git, Oh My Git!), structured courses (Software Carpentry git-novice and shell-novice, GitHub Skills, MIT Missing Semester, The Odin Project, Atlassian tutorials, Git Immersion), reference (Pro Git, git-scm docs, GitHub/GitLab/Codeberg/Forgejo docs, VS Code source control), rescue guides (Oh Shit Git, Git Flight Rules), contribution (First Contributions, Open Source Guides, choosealicense, Hacktoberfest), standards (SemVer, Keep a Changelog, Conventional Commits, REUSE/SPDX, CFF), research and data (Turing Way, PLOS "Ten simple rules"/"Quick introduction", DVC, Git LFS), teaching (Teaching Tech Together, CS Unplugged, Parsons tools).
- Exact exercise mapping per lesson (e.g. *learnGitBranching level `intro2` "Branching in Git"*, *Pro Git §2.2*, *git-novice episode 4*).

### WP2 — Rewrite all 41 lessons (Grades 8–12) with more detail
Every `lesson.md` gets the new structure (also written into `docs/en/module-template.md`):

1. **At a glance** box — time, materials, tiers, outcomes, prerequisites.
2. **Hook** — a real Nepali-context problem (kept and sharpened).
3. **Understand it** — a full explanation in plain English: analogy → precise idea → small diagram (text diagrams so they print), what Git is actually doing, why it matters. This is the "book" part a student can read alone.
4. **See it** — a worked example with exact commands *and the expected output*, annotated.
5. **Unplugged / concept activity** (kept, more detailed steps).
6. **PRIMM lab** — numbered steps for Predict, Run, Investigate, Modify, Make, with checkpoints ("you should now see…").
7. **Parsons practice** (kept).
8. **Common mistakes and how to fix them** — symptom → cause → fix.
9. **Practise more with free resources** — 3–6 exercises using WP1 resources, each with tier, time and what to hand in.
10. **Exit ticket** (kept, one misconception check).
11. **Key points** — 4–6 bullets for revision.
12. **New words** — linked to the glossary.
13. **Extension quest**.
14. **Teacher notes** (Grades 9–12 inline: timing, misconceptions, fallbacks, answer key). Grade 8 keeps its separate `teacher-guide.md`, which is also improved (answer keys for new exercises, differentiation, assessment evidence).

Target length: 1,000–1,800 words per lesson (currently 170–400).

Order: Grade 8 (7 modules + 7 teacher guides) → Grade 9 (8) → Grade 10 (9) → Grade 11 (8) → Grade 12 (9). Grade index pages updated with a chapter map, chapter outcomes, and "practise more" summaries.

### WP3 — New book chapters (`docs/en/book/`)
| File | Content |
|---|---|
| `index.md` | Preface: who the book is for, how to read it (student path, teacher path, self-learner path), how the parts fit, licence and credit |
| `teaching-foundation.md` | **Part I. How to teach version control so it becomes a foundation.** The five-year concept spine (history → snapshot → branch → remote → collaboration → automation → internals); threshold concepts and the misconception catalogue; mental models to teach (and which to avoid); sequencing rules (JISE 2025); PRIMM, Parsons, unplugged, pair work in practice; assessment progression from exit tickets to capstone rubrics; reading `git log` as formative evidence; lab setup and power-cut plans; differentiation and inclusion; running Git in a 40-student, 10-PC room; how to grow as a teacher (training outline, communities) |
| `after-grade-12.md` | **Part VII. The foundation, consolidated.** Competency checklist (what a Grade 12 finisher can do, by strand); self-assessment; gaps-and-fixes; a 4-week bridge course for learners who missed grades or are starting at +2 / university; how the strands connect to university and industry |
| `any-project.md` | **Part VIII. Version control in any project.** Decision guide (what to track, what not); the 10-step adoption playbook (init → .gitignore → README → licence → first commit → remote/backup → branch rules → review → CI → releases); recipes by project type: school assignment, essay/thesis (Markdown/LaTeX/Overleaf), research data and notebooks, website, Python/app, mobile/game, design and binary files (Git LFS), spreadsheets→CSV, Arduino/hardware, documentation/translation, government/NGO data; migrating a `final_final_v3` folder or ZIP history into Git; team adoption in a school or office; solo vs team vs open-source settings; security and backup checklist; templates (README, CONTRIBUTING, PR template, `.gitignore`, CI workflow) |
| `books.md` | **Part IX. Books and reading list.** Free books (Pro Git, Git from the Bottom Up, Producing Open Source Software, Teaching Tech Together, Happy Git with R, The Turing Way) and print books (e.g. *Version Control with Git*, *Building Git*, *Working in Public*, *Forge Your Future with Open Source*, *The Pragmatic Programmer*, *Accelerate*, *The Programmer's Brain*), research papers (PLOS "Ten Simple Rules…", "A Quick Introduction to Version Control with Git and GitHub", "Excuse me, do you have a moment to talk about version control?"), essays and zines; each with level, why read it, and which part of this book it extends |
| `cheatsheet.md` | Appendix A: one-page command cheat sheet by grade, plus a "which undo do I need?" decision table |
| `troubleshooting.md` | Appendix B: "Oops" guide — 25+ real situations (detached HEAD, merge conflict panic, committed a password, pushed to wrong branch, lost work, CRLF warnings, `rejected — fetch first`, …) with safe fixes |

Existing pages reused as appendices: glossary, teacher setup, training outline, pathways, Grade 8 cards, assessment rubrics and item banks, CDC brief, sources/credits.

### WP4 — PDF book build
- `tools/build_book.py` (Python, no new dependencies beyond what CI already has + `markdown`, `pymdown-extensions`, `pypdf`):
  1. reads an ordered manifest (`book/book.yml`) of parts and Markdown files;
  2. strips front-matter, turns it into an "at a glance" line where useful;
  3. renders Markdown with the same extensions as `mkdocs.yml`, rewrites cross-links to in-book anchors;
  4. writes one `book/dist/book.html` with print CSS (`book/print.css`): A4, margins, running header with part/chapter, page numbers, part dividers, avoid page breaks inside tables/code, B&W-safe callouts, Devanagari font fallback;
  5. prints to PDF with headless Chrome/Edge (`--print-to-pdf`), then **second pass**: finds each chapter's page with `pypdf` and fills page numbers into the table of contents.
- Output: `book/dist/git-for-nepal-book.pdf` (committed for download) and linked from the site home page and README.
- Optional later: a CI job that rebuilds the PDF on release.

### WP5 — Integrate and check
- Update `docs/en/index.md`, `README.md`, `docs/en/teachers/index.md`, `module-template.md`, `CHANGELOG.md` (v0.2.0), `research/sources.md` (new sources S19+ with check dates), `ATTRIBUTION.md` if needed.
- Run: `python tools/validate_frontmatter.py`, `python tools/check_links.py`, `mkdocs build --strict`, external link sweep (curl, all `https://` links in `docs/en`), visual check of the PDF (cover, TOC numbers, tables, code blocks, page breaks).
- Nepali pages: unchanged in this pass; `teachers/ne-status.md` notes that the expanded English text is the new source for translation.

## 4. Acceptance criteria
- [ ] 41 lessons follow the new structure; each has ≥ 3 free-resource exercises with tiers and a teacher answer key.
- [ ] 7 Grade 8 teacher guides updated.
- [ ] 7 new book pages written (WP3).
- [ ] Every external link returns HTTP 200 (or is noted as blocking robots, checked manually).
- [ ] `validate_frontmatter.py`, `check_links.py`, `mkdocs build --strict` pass.
- [ ] PDF builds from one command, has cover, TOC with page numbers, all parts, readable in B&W, < 20 MB.

## 5. Out of scope for this pass (needs humans)
Classroom piloting, native-speaker Nepali translation of the expanded text, CDC submission, contacting partner communities, publishing/pushing.
