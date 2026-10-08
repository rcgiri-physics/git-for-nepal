---
id: g10-m02-fork-clone-branch
grade: 10
hours: 1
prerequisites: [g10-m01-issues]
outcomes:
  - "Distinguish fork, clone and branch"
  - "Choose the right one for a situation"
tier_support: [2, 3]
license: CC-BY-4.0
---

# 2. Fork vs clone vs branch

## Hook
You want to change a project you do not own. What are your options?

## Concept (unplugged or visual first)
Draw a table together:

| | where it lives | who it's for |
|---|---|---|
| **branch** | inside one repo | people who can write to the repo |
| **clone** | your computer | everyone (a local copy) |
| **fork** | your own copy on the server | people who cannot write to the original |

Act it out: students are 'owners' and 'visitors' with a shared poster.

## PRIMM lab
1. Teacher repo `school-website-template`. **Predict** which of fork/clone/branch you need as owner of your team repo vs. as a visitor.
2. Fork the template into your account/organisation (or, on a LAN server, create a copy via the server's fork button).
3. Clone your fork. `git remote -v`. Add the original as `upstream`: `git remote add upstream <url>`.
4. Create a branch `feature/about-page`.
5. **Make:** draw the three copies (original, fork, local) and the arrows (push, pull, pull request).

## Parsons practice
Order: *fork · clone · branch · commit · push to fork*.

## Exit ticket
1. When do you need a fork?
2. What is `upstream`?
3. *Misconception:* 'a fork is the same as a branch.' True or false?

## Teacher notes
Students 13+ only create accounts; teacher-managed organisation preferred. Typical confusion: `origin` vs `upstream`.
