---
id: g12-m02-branching-strategies
grade: 12
hours: 2
prerequisites: [g12-m01-internals]
outcomes:
  - "Compare trunk-based development, feature branches and Gitflow"
  - "Choose a strategy for a project and justify it"
tier_support: [0, 1, 2, 3]
license: CC-BY-4.0
---

# 2. Branching strategies

## Hook
A team of 3 and a team of 300 should not work the same way.

## Concept (unplugged or visual first)
Poster activity: draw each strategy's history graph: **trunk-based** (tiny branches, merge daily, feature flags), **feature branches** (one branch per feature, PR), **Gitflow** (develop, release, hotfix branches).

## PRIMM lab
1. Given 3 project descriptions (school website; mobile app with monthly releases; library with old versions supported), **predict** the best strategy for each.
2. Simulate each with the practice repo `g12-capstone-starter` for 10 minutes.
3. **Investigate:** count conflicts and branches.
4. **Make:** write the strategy for your capstone in `CONTRIBUTING.md`.

## Parsons practice
Match strategy to its signature: daily merges → trunk-based; release/hotfix branches → Gitflow.

## Exit ticket
1. Which strategy suits a team of three?
2. What is a feature flag?
3. *Misconception:* 'Gitflow is always the professional choice.'

## Teacher notes
No single correct answer; grade the reasoning.
