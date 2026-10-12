# Git for Schools

**A free, open, offline-first curriculum for teaching Git and version control, Grades 8–12 (ages ~13–18).**
Five chapters, 41 modules, teacher guides, assessments, practice repos and a ~260-page printable book — built to work in classrooms with **no computers, offline computers, a school network, or full internet**.

[**Read online**](https://rcgiri-physics.github.io/git-for-schools/) · [**Download the PDF book**](book/dist/git-for-schools-book.pdf) · [**Teachers start here**](docs/en/teachers/index.md) · [**Contribute**](CONTRIBUTING.md)

> **Status: edition 0.3 — not yet piloted in a classroom.** Grade 8 is a full chapter; Grades 9–12 are complete drafts. Feedback from teachers who try a module is the most useful contribution right now.

## Why this exists
Most Git tutorials assume an adult developer with a laptop and fast internet. School students learn programming but rarely learn *how people work together on code*: history, branches, reviews, releases, open source. This curriculum teaches that from the first idea ("why is `final_FINAL_v3.doc` a bad version system?") to professional workflows — and every lesson has a no-computer fallback, because many schools have few machines and unreliable internet.

It began in **Nepal**, where it was written for schools under exactly those conditions, and it keeps an optional Nepali translation and a mapping to Nepal's national curriculum ([`alignment/`](alignment/)). Nothing in the lessons depends on one country.

## What's inside
| Grade | Chapter | Big idea |
|---|---|---|
| 8 | Time Machine for My Work | every file has a history |
| 9 | Branch and Share | branches work in parallel; remotes let work travel |
| 10 | Team Workflows | teams need rules so work does not collide |
| 11 | Open-Source Contributor | you can improve software others also use |
| 12 | Engineering with Git | professional teams ship safely, repeatedly |

Every module has a lesson, a teacher guide (timing, misconceptions, fallback), exercises and an exit ticket. Each grade ends with a real artefact: a class magazine, a data script, a team website, a merged open-source contribution, a released capstone.

## Four delivery tiers
Every module says which it supports: **0** no computer · **1** offline computers · **2** school LAN (self-hosted Forgejo) · **3** internet. See [`offline/`](offline/README.md).

## The book (PDF)
**Teaching Version Control: A Foundation Book for Grades 8–12** — [`book/dist/git-for-schools-book.pdf`](book/dist/git-for-schools-book.pdf). Adds a teaching guide, a bridge course after Grade 12, a handbook for using version control in any project, a reading list, a free-resource library, a cheat sheet and a troubleshooting guide. Rebuild with `python tools/build_book.py` (needs Chrome, Chromium or Edge).

## Who is it for?
- **Teachers** — [`docs/en/teachers/`](docs/en/teachers/index.md)
- **Students and self-learners** — start at [Grade 8](docs/en/index.md); adults can move through it quickly.
- **Curriculum bodies** — see [`alignment/`](alignment/) for an example mapping (Nepal's CDC) and adapt it.
- **Contributors** — [`CONTRIBUTING.md`](CONTRIBUTING.md). Translations, classroom feedback and new exercises are especially welcome.

## Build the site locally
```bash
pip install -r requirements.txt
mkdocs serve
```

## Licence and credit
Content: **CC BY 4.0** ([`LICENSE-CONTENT.md`](LICENSE-CONTENT.md)) · Code, scripts, templates: **MIT** ([`LICENSE`](LICENSE)) · How to credit: [`ATTRIBUTION.md`](ATTRIBUTION.md) · Cite: [`CITATION.cff`](CITATION.cff)

## How this was made
Drafted with AI assistance; the author curated, verified and adapted every lesson. An originality check against major Git references found no copied text — see [`research/originality-check.md`](research/originality-check.md).
