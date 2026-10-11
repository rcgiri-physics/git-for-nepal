# Book plan — status

Read [`PLAN.md`](PLAN.md) first. Tick items as they are finished; the next session continues from the first unticked line.

## WP1 Resource library
- [x] `docs/en/book/resources.md`

## WP2 Lessons
- [x] Module template updated
- [x] G8 m01–m07 lessons
- [x] G8 m01–m07 teacher guides
- [x] G8 index
- [x] G9 m01–m08 + index
- [x] G10 m01–m09 + index
- [x] G11 m01–m08 + index
- [x] G12 m01–m09 + index

## WP3 Book chapters
- [x] book/index.md (preface)
- [x] teaching-foundation.md
- [x] after-grade-12.md
- [x] any-project.md
- [x] books.md
- [x] cheatsheet.md
- [x] troubleshooting.md

## WP4 PDF
- [x] book/book.yml manifest
- [x] book/print.css
- [x] tools/build_book.py
- [x] PDF built and visually checked

## WP5 Integrate and check
- [x] index/README/teachers/CHANGELOG/sources updated
- [x] validators + strict build pass
- [x] external link sweep

## Notes for later steps
- after-grade-12.md must have a heading "Bridge course" (anchor #bridge-course, linked from grade-08/index.md)
- glossary.md needs new terms: version, version control system, snapshot, working copy, parent, commit id, .git, untracked, modified, context line, pager, restore, revert, HEAD, unstage, frequency table, --format + all Grade 9–12 terms
- troubleshooting.md is linked from resources.md
- Session 1 ended 2026-10-11 at usage limit. Next: books.md, cheatsheet.md, troubleshooting.md, book/index.md, then WP4 PDF, WP5 (glossary expansion, link sweep, strict build). Known broken links until then: book/books.md, book/troubleshooting.md.
- Session 2 (2026-10-11): plan complete. PDF: 260 pages, 4.9 MB, 79 bookmarks, TOC page numbers. Checks pass: validate_frontmatter, check_links, check_datasets, smoke tests, mkdocs --strict; all real external links 200 (placeholders like school-server excluded).
- Needs humans: classroom pilot, Nepali translation of the expanded text, review of new chapters by a teacher, commit/push (not done — not requested).
