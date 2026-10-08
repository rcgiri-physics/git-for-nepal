---
id: g10-m08-ci-intro
grade: 10
hours: 1
prerequisites: [g10-m07-static-site]
outcomes:
  - "Explain a CI check as a robot reviewer"
  - "Run a given check script locally"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 8. Automatic checks (CI) — intro

## Hook
What if a robot could tell you before the review that a link on your page is broken?

## Concept (unplugged or visual first)
A **check script** is a small program that returns pass/fail. **CI** runs it automatically on every push or PR. We start with running the script by hand.

## PRIMM lab
1. `bash check.sh` in `g10-school-website`. **Predict** the result.
2. Break a link on purpose (`href="aboot.html"`). Run again. Read the message.
3. Fix it and commit. On tier 2/3 the platform can run the script automatically (see Grade 12 for workflows).
4. **Make:** add one more check (e.g. every page has a `<title>`).

## Parsons practice
Order: *change · run check · read message · fix · commit*.

## Exit ticket
1. What does a check script return?
2. Why is a robot reviewer useful?
3. *Misconception:* 'if the check passes, the page is perfect.' True or false?

## Teacher notes
Optional unit. If time is short, skip to the team project.
