---
id: g12-m03-ci
grade: 12
hours: 3
prerequisites: [g12-m02-branching-strategies]
outcomes:
  - "Write a workflow that runs checks on every push and PR"
  - "Read a failing run and fix it"
tier_support: [2, 3]
license: CC-BY-4.0
---

# 3. Automation: CI with GitHub Actions / Forgejo Actions

## Hook
A robot that runs your checks on every PR and refuses a merge if they fail.

## Concept (unplugged or visual first)
A **workflow** file lists triggers (`on: pull_request`) and steps (checkout, install, run check). Same idea on GitHub Actions and Forgejo Actions (syntax is very similar; verify differences in the current docs).

## PRIMM lab
1. Look at `.github/workflows/ci.yml` in this repo. **Predict** what happens on a PR.
2. In your capstone repo add a workflow running `bash check.sh`.
3. Push a broken change. **Investigate** the red run, read the log.
4. Fix; see it turn green. Protect `main` so a red run blocks merging.
5. **Make:** add a data-validation step for a CSV (header and row count).

## Parsons practice
Order: *push · workflow triggers · steps run · pass/fail shown on PR · merge allowed or blocked*.

## Exit ticket
1. What triggers a workflow?
2. Why protect `main`?
3. *Misconception:* 'green CI means no bugs.'

## Teacher notes
Tier 0/1: run `check.sh` by hand; the idea is the same. Pin action versions.
