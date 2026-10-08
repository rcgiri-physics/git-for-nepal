---
id: g10-m03-pull-requests
grade: 10
hours: 2
prerequisites: [g10-m02-fork-clone-branch]
outcomes:
  - "Open a pull request with a clear description"
  - "Explain how a PR connects an issue, a branch and a review"
tier_support: [2, 3]
license: CC-BY-4.0
---

# 3. Pull requests

## Hook
In Grade 9 you merged straight into main. In a real team, someone checks first.

## Concept (unplugged or visual first)
A **pull request (PR)** says: 'please merge my branch; here is what and why; please review.' It shows the diff and a place to talk. Role-play on paper: author hands a printed diff to a reviewer who writes comments.

## PRIMM lab
1. Take issue #1 ('Add About page'). Work on `feature/about-page`, make 2–3 commits.
2. Push the branch. Open a PR: title, description ('Closes #1'), what you changed, how to check.
3. **Predict:** what will the reviewer see? Check the PR's 'Files changed' tab.
4. Your partner reviews (next module) — meanwhile, fix any requested change by pushing more commits to the same branch.
5. **Make:** write a PR description template for your team.

## Parsons practice
Order: *create branch · commit · push · open PR · review · merge · delete branch*.

## Exit ticket
1. What does 'Closes #1' do?
2. Why open a PR instead of merging yourself?
3. *Misconception:* 'a PR is a new copy of the code.' True or false?

## Teacher notes
Keep PRs small (one issue). On tier 2 Forgejo the PR flow is the same as on GitHub. Tier 1: simulate with `git format-patch` and a printed diff.
