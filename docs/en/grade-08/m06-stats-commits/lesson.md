---
id: g8-m06-stats-commits
grade: 8
hours: 1
prerequisites: [g8-m04-history-diff]
outcomes:
  - "Collect data from a repository history (commits per day)"
  - "Draw a bar chart of that data and say what it shows"
tier_support: [0, 1, 2, 3]
license: CC-BY-4.0
---

# 6. Statistics: chart my commits

Your repo's history is **data**. Today you will make a frequency table and a bar chart of it. This links to your statistics lessons (frequency table, bar chart, mean).

## Hook (5 min)
*"Which day did we work hardest on the magazine? Let's let the history answer."*

## Collect (10 min)
Tier 1+: run
```bash
git log --date=short --format=%ad
```
Each line is the date of a commit. (Tier 0: use the printed log from the practice repo, or your Module 2 cards.)

Make a **tally table** in your notebook:

| Date | Tally | Frequency |
|---|---|---|
| 2026-10-01 | \|\|\| | 3 |
| … | | |

## Chart (15 min)
Draw a bar chart on graph paper: date on the x-axis, number of commits on the y-axis. Title it, label the axes, choose a scale.

Optional on computer: paste the table into LibreOffice Calc and insert a bar chart.

## Interpret (5 min)
- Which day has the most commits? That is the **mode**.
- What is the mean number of commits per working day?
- Was it better to commit a little every day or a lot on one day? Why might one be safer?

## Exit ticket (5 min)
1. What is the frequency of commits on the busiest day in your chart?
2. Calculate the mean commits per day for your repo.
3. *Check:* "More commits always means better work." Agree or disagree and explain.
