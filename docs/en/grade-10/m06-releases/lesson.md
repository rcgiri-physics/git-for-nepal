---
id: g10-m06-releases
grade: 10
hours: 1
prerequisites: [g10-m05-conflicts]
outcomes:
  - "Tag a commit and push the tag"
  - "Write release notes and a changelog entry"
  - "Read a version number as MAJOR.MINOR.PATCH (lightly)"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 6. Tags and releases

!!! abstract "At a glance"
    **Time:** 1 period · **Tiers:** 1–3 · **You need:** your team repository with merged PRs

    **Before this:** Grade 9 Module 8 (first tag), Modules 3–5.

    **By the end you can:** mark a finished version with an annotated tag, publish a release with notes, and keep a changelog.

## Hook (5 min)
The head teacher asks: *"Which version of the website is the finished one we showed at the festival?"* The team is still committing new changes every day. How do you point to *exactly* the version that was shown — today, and in a year?

## Understand it

### Tags: names that never move
A **branch** label moves forward with every commit. A **tag** is a label that **stays on one commit for ever**. It answers "which exact snapshot was version 1.0?".

```
  c1 -- c2 -- c3 -- c4 -- c5   [main]   <- main keeps moving
              ^
           (v1.0)                       <- the tag stays here
```

Two kinds:

| | Lightweight tag | Annotated tag (use this) |
|---|---|---|
| Create | `git tag v1.0` | `git tag -a v1.0 -m "Festival version"` |
| Stores | just the name → commit | name, tagger, date, message |
| Use for | private bookmarks | public versions |

Tags are **not pushed automatically**: `git push origin v1.0` (or `git push --tags` for all).

### Releases
A **release** is a tag plus **release notes** on the hosting server's *Releases* page, often with files to download (a ZIP of the site, a program). Notes are written for **users**, not programmers:

```markdown
## v1.0 — Festival version (2083-07-15)
### Added
- About page with the school's history (#2)
- Contact page with office phone and hours (#3)
### Fixed
- Broken "Festival" link in the menu (#5)
```

### The changelog
`CHANGELOG.md` collects the notes of **every** release, newest first, in the repository itself. The free standard [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) uses the headings *Added, Changed, Deprecated, Removed, Fixed, Security* and keeps an *Unreleased* section at the top for changes not yet released.

Release notes and changelogs are **not** the same as `git log`. The log has every small commit ("Fix typo in about.html"); the changelog says what matters to users.

### Version numbers, lightly
Many projects number versions **MAJOR.MINOR.PATCH** (`1.2.0`):

- **PATCH** (1.2.**1**) — a small fix;
- **MINOR** (1.**3**.0) — something new, nothing broken;
- **MAJOR** (**2**.0.0) — a big change that breaks old ways of using it.

This is called **semantic versioning**; Grade 12 learns its exact rules. For the school site: v1.0.0 at the festival, v1.1.0 when the gallery is added, v1.1.1 for a typo fix.

### Going back to a release
```bash
git switch --detach v1.0     # look at the festival version (read-only "detached HEAD")
git switch main              # come back
git diff v1.0 main           # what changed since the festival?
git log --oneline v1.0..main # which commits came after it?
```

## See it
```console
$ git tag -a v1.0.0 -m "Festival version"
$ git tag
v1.0.0
$ git show v1.0.0 --no-patch
tag v1.0.0
Tagger: Student 12 <s12@example.invalid>
Date:   Thu Oct 29 11:00:00 2026 +0545

Festival version

commit 9d1e4a7 (HEAD -> main, tag: v1.0.0)
...
$ git push origin v1.0.0
To http://school-server/team-3/school-website.git
 * [new tag]         v1.0.0 -> v1.0.0
```

## Unplugged (5 min)
Hold up the class magazine card row from Grade 8. Clip a **paper clip** labelled *v1.0* onto one card, and a **sticky note** *main* onto the newest card. Add two cards: the sticky note moves, the paper clip does not.

## PRIMM lab (30 min)
1. On `main`, when the site is ready, **predict** what `git tag` lists. Then: `git tag -a v1.0.0 -m "First public version"`.
2. `git push origin v1.0.0`. On the server, open *Releases* (or *Tags*) and create a release from the tag with notes using the headings above.
3. **Predict:** what happens to the tag if you commit more? (It stays on the old commit.) Make a commit and check with `git log --oneline --decorate`.
4. **Investigate:** `git log --oneline v1.0.0..main` and `git diff v1.0.0 main --stat`.
5. **Make:** write `CHANGELOG.md` for v1.0.0 in three bullet points, with an empty `## [Unreleased]` section on top. Commit it via a PR.

## Parsons practice (5 min)
Order: *main is ready · tag · push tag · release notes · announce*.

## Common mistakes
| Symptom | Cause | Fix |
|---|---|---|
| Tag not on the server | tags are not pushed by default | `git push origin v1.0.0` |
| Tagged the wrong commit | — | before pushing: `git tag -d v1.0.0`, tag again. After pushing: make a new version (v1.0.1) — don't move public tags |
| Release notes copied from `git log` | too detailed for users | summarise by Added/Changed/Fixed |
| `fatal: tag 'v1.0' already exists` | — | choose the next version number |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | *Pro Git* [§2.6 **Tagging**](https://git-scm.com/book/en/v2/Git-Basics-Tagging): try `git tag -l "v1.*"` and tagging an older commit. | 1 / 3 | 15 min | commands used |
| 2 | [Keep a Changelog](https://keepachangelog.com/en/1.1.0/): read "Guiding principles". Improve your changelog to follow them. | 3 | 15 min | updated changelog |
| 3 | Learn Git Branching [`mixed4` "Git Tags"](https://learngitbranching.js.org/?locale=en_US&level=mixed4). | 1 / 3 | 10 min | level done |
| 4 | GitHub Skills [**Release-based workflow**](https://github.com/skills/release-based-workflow) (13+, account). | 3 | 45 min | completed course |
| 5 | Look at this book's own `CHANGELOG.md` (in the repository). Which headings does it use? | 1 | 5 min | headings |

## Exit ticket (5 min)
1. What does a tag mark?
2. What goes in release notes?
3. *Misconception:* "The tag moves when I commit." True or false?

## Key points
- A **tag** is a permanent name on one commit; use **annotated** tags for versions.
- Push tags explicitly; never move a public tag — release a new version instead.
- A **release** = tag + notes for users; a **changelog** collects them in the repo.
- MAJOR.MINOR.PATCH: break · add · fix (details in Grade 12).

## New words
**tag**, **annotated tag**, **release**, **release notes**, **changelog**, **semantic version** — see the [glossary](../../glossary.md).

## Extension quest
Run `git describe` on a commit after the tag. What do the parts of its output mean? (Learn Git Branching level `mixed5` "Git Describe".)

## Teacher notes
- **Timing:** hook 5 · understand 10 · unplugged 5 · lab 20 · Parsons + exit 5.
- Keep semantic versioning very light here; the full rules come in Grade 12 Module 4.
- If time is short, skip the server *Release* page and do tags + changelog only (works in Tier 1).
- **Answer key:** Exit 1: one exact commit (a version) — permanently. 2: what changed for users: added, changed, fixed (with issue numbers). 3: False. Extension: `v1.0.0-2-g9d1e4a7` = tag, commits since the tag, `g` + short id.
