---
id: g12-m04-releases
grade: 12
hours: 2
prerequisites: [g12-m03-ci]
outcomes:
  - "Apply MAJOR.MINOR.PATCH correctly"
  - "Produce a changelog and release"
  - "Explain pre-releases and why public versions never change"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 4. Releases and semantic versioning

!!! abstract "At a glance"
    **Time:** 2 periods · **Tiers:** 1–3 · **You need:** your capstone repo with CI from Module 3

    **Before this:** Grade 10 Module 6, Grade 11 Module 6 (Conventional Commits).

    **By the end you can:** choose the correct next version number, write a changelog, tag and publish a release, and explain the promises a version number makes.

## Hook (5 min)
You updated a library from 1.9 to 2.0 and your program broke. Annoying — but the author *warned* you: the **2** means "something changed that may break your code". A version number is a promise. Today you learn to make that promise correctly.

## Understand it

### Semantic Versioning (SemVer)
A version is **MAJOR.MINOR.PATCH**, e.g. `2.4.1`. The project first defines its **public API** — what users rely on (commands, options, function names, file formats, column names in a dataset). Then:

| Change | Bump | Example |
|---|---|---|
| **incompatible** change to the public API (users must change their code/use) | **MAJOR** — `2.4.1 → 3.0.0` | rename a command; remove a column |
| new, **backwards-compatible** functionality | **MINOR** — `2.4.1 → 2.5.0` | add an option; add a column |
| backwards-compatible **bug fix** | **PATCH** — `2.4.1 → 2.4.2` | fix a wrong total |

Rules worth remembering (from semver.org):

- When MINOR goes up, PATCH resets to 0; when MAJOR goes up, both reset (`1.9.3 → 2.0.0`).
- A released version **must never change** — fix it with a new version.
- **`0.y.z`** is initial development: anything may change; `1.0.0` defines the stable public API.
- **Pre-releases** have a hyphen: `2.0.0-alpha.1`, `2.0.0-rc.1` — they come *before* `2.0.0`.
- **Build metadata** has a plus: `1.0.0+20261011` — ignored when comparing versions.

### From commits to versions
With Conventional Commits (Grade 11): any `feat!` / `BREAKING CHANGE` → MAJOR; else any `feat` → MINOR; else `fix` → PATCH. Tools can then compute the next version and write the changelog automatically.

### The release routine
1. All PRs for the release merged; CI green on `main`.
2. Decide the version from the changes since the last tag: `git log --oneline v0.2.1..main`.
3. Move the *Unreleased* changelog entries under the new version and date.
4. Commit: `Release v0.3.0`. Tag: `git tag -a v0.3.0 -m "v0.3.0"`. Push commit and tag.
5. Create the release on the host with notes (and files to download, if any).
6. Announce it.

Many teams let CI do steps 4–5 when a tag is pushed.

### Other versioning schemes
**CalVer** uses dates (`2026.10`, Ubuntu's `24.04`) — good for things released on a schedule. Data releases often use dates too (`census-2021-v2`). SemVer is best when users depend on an API. Choose one and document it.

## See it
```console
$ git log --oneline v0.2.1..main
9f3a2c1 feat(report): add density per ward
41be0d7 fix(clean): keep leading zeros in ward codes
c07d5e2 docs: explain how to run the report
$ # a feat and a fix, no breaking change -> MINOR: v0.2.1 -> v0.3.0
$ git tag -a v0.3.0 -m "v0.3.0"
$ git push origin main v0.3.0
```

```markdown
## [0.3.0] - 2026-11-20
### Added
- Population density per ward in the report (#31).
### Fixed
- Ward codes such as `007` lost their leading zeros (#29).
```

## Unplugged: bump or not? (15 min)
Cards with 10 change descriptions (teacher notes). Teams hold up **MAJOR / MINOR / PATCH / none**. Discuss the disagreements — most come from not agreeing what the public API is.

## PRIMM lab (50 min)
1. Given 10 change descriptions, **predict** the version bump for each; compare with another team and with the rules on [semver.org](https://semver.org/).
2. In the capstone repo tag `v0.1.0`, then add a feature (`v0.2.0`) and a fix (`v0.2.1`) — each through a PR with green CI.
3. Write `CHANGELOG.md` entries (Keep a Changelog format, *Unreleased* on top).
4. **Investigate:** `git describe --tags` on a commit after `v0.2.1`. What does it say?
5. **Make:** generate release notes with `git log v0.1.0..v0.2.1 --oneline`, then rewrite them for users. Publish the release on the host.

## Parsons practice (5 min)
Match change → bump: renamed a command (major), new option (minor), typo fix (patch), README improvement (none).

## Common mistakes
| Mistake | Fix |
|---|---|
| Re-tagging a published version to "fix" it | release a new PATCH |
| Bumping MAJOR for a big but compatible feature | size doesn't matter; compatibility does |
| Breaking change hidden in a PATCH | users' programs break unexpectedly — MAJOR |
| Changelog = raw `git log` | write for users: Added/Changed/Fixed |
| No public API defined | write in the README what users can rely on |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | [Semantic Versioning 2.0.0](https://semver.org/) — read the specification items 1–11 and the FAQ "What do I do if I accidentally release a backwards incompatible change as a minor version?". | 3 | 30 min | answer |
| 2 | [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) — apply all its principles to your capstone changelog. | 3 | 15 min | changelog |
| 3 | Learn Git Branching [`mixed5` "Git Describe"](https://learngitbranching.js.org/?locale=en_US&level=mixed5). | 1 / 3 | 10 min | level done |
| 4 | GitHub Skills [**Release-based workflow**](https://github.com/skills/release-based-workflow) (13+, account). | 3 | 45 min | completed course |
| 5 | Look at the release history of a tool you use (Git itself, Python, VS Code). Which scheme does it use? Find one MAJOR release and what broke. | 3 | 20 min | notes |

## Exit ticket (5 min)
1. When do you bump MAJOR?
2. Where does the changelog live?
3. *Misconception:* "The version number is just a date."

## Key points
- **MAJOR** breaks the public API · **MINOR** adds compatibly · **PATCH** fixes compatibly.
- Published versions never change; `0.x` is unstable; pre-releases use `-alpha`, `-rc`.
- Conventional Commits can compute the bump.
- Routine: merge → decide version → changelog → tag → release → announce.

## New words
**semantic versioning (SemVer)**, **public API**, **breaking change**, **pre-release**, **release candidate (rc)**, **CalVer** — see the [glossary](../../glossary.md).

## Extension quest
Add a workflow that runs when a tag `v*` is pushed and creates a release automatically.

## Teacher notes
- **Timing:** P1: hook 5, understand 20, cards 15. P2: lab 35, Parsons + exit 5.
- Link to semver.org for the exact rules.
- **10 change cards and answers:** rename `--input` to `--file` (MAJOR) · add `--quiet` option (MINOR) · fix wrong average (PATCH) · README typo (none) · remove a CSV column (MAJOR) · add a CSV column at the end (MINOR — unless users read columns by position: discuss!) · speed up the script, same output (PATCH) · change default output folder (MAJOR) · add Nepali translation of messages (MINOR) · update CI only (none).
- **Answer key:** Exit 1: when a change is incompatible with the public API. 2: `CHANGELOG.md` in the repository (and summarised in release notes). 3: False under SemVer — each part has a meaning (CalVer does use dates).
