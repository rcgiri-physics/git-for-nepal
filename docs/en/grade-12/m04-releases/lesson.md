---
id: g12-m04-releases
grade: 12
hours: 2
prerequisites: [g12-m03-ci]
outcomes:
  - "Apply MAJOR.MINOR.PATCH correctly"
  - "Produce a changelog and release"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 4. Releases and semantic versioning

## Hook
Version 2.0 broke my program. Why did the author number it that way?

## Concept (unplugged or visual first)
SemVer: **MAJOR** = breaking change, **MINOR** = new feature, backwards-compatible, **PATCH** = bug fix. Changelog = human summary.

## PRIMM lab
1. Given 10 change descriptions, **predict** the version bump for each; compare.
2. In the capstone repo tag `v0.1.0`, then add a feature (`v0.2.0`) and a fix (`v0.2.1`).
3. Write `CHANGELOG.md` entries. **Make:** generate release notes with `git log v0.1.0..v0.2.1 --oneline`.

## Parsons practice
Match change → bump: renamed a command (major), new option (minor), typo fix (patch).

## Exit ticket
1. When do you bump MAJOR?
2. Where does the changelog live?
3. *Misconception:* 'the version number is just a date.'

## Teacher notes
Link to semver.org for the exact rules.
