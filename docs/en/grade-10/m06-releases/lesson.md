---
id: g10-m06-releases
grade: 10
hours: 1
prerequisites: [g10-m05-conflicts]
outcomes:
  - "Tag a version and write release notes"
  - "Explain why a version number is a promise"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 6. Tags and releases

## Hook
A shopkeeper asks 'which version of the website is the finished one?'

## Concept (unplugged or visual first)
A **tag** is a permanent name on a commit (`v1.0`). A **release** is a tag + notes saying what changed. Version numbers like 1.2.0: *major.minor.patch* — we'll learn the rules fully in Grade 12.

## PRIMM lab
1. On `main`, when the site is ready: `git tag -a v1.0 -m "First public version"`.
2. `git push origin v1.0`. On the server, create a release with notes.
3. **Predict:** what happens to the tag if you commit more? (It stays on the old commit.)
4. **Make:** write `CHANGELOG.md` for v1.0 in three bullet points.

## Parsons practice
Order: *main is ready · tag · push tag · release notes · announce*.

## Exit ticket
1. What does a tag mark?
2. What goes in release notes?
3. *Misconception:* 'the tag moves when I commit.' True or false?

## Teacher notes
Keep semantic versioning very light here.
