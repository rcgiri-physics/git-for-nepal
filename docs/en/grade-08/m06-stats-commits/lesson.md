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

!!! abstract "At a glance"
    **Time:** 1 period · **Tiers:** 0–3 · **You need:** the practice repo or the printed `log-sample.txt`, graph paper, ruler; optional LibreOffice Calc

    **Before this:** Module 4 (reading history).

    **By the end you can:** turn a repository's history into a frequency table; draw and label a bar chart; find the mode and mean; say what the chart does and does not tell you.

Your repo's history is **data**. Today you will make a frequency table and a bar chart of it. This links to your mathematics lessons on statistics (frequency table, bar chart, mode, mean).

## Hook (5 min)
*"Which day did we work hardest on the magazine? Let's let the history answer."*

## Understand it

### History is a data set
Every commit has a date and time. A list of dates is raw data, just like a list of marks or temperatures. When you **group** it (how many commits on each day?), you get a **frequency table**, and from that a **bar chart**.

Software teams do exactly this. Websites like GitHub draw a "contribution graph" from commit dates, and team leaders look at commit activity to see whether a project is alive. Now you know how it is made.

### Getting the data out of Git
`git log` can print just the parts you ask for with `--format`:

| You type | Git prints for each commit |
|---|---|
| `git log --date=short --format=%ad` | the date (`%ad` = author date) |
| `git log --format=%an` | the author's name |
| `git log --date=short --format="%ad %s"` | date and message (`%s` = subject) |

### What the chart can and cannot tell you
A commit chart measures **activity**, not **quality**. Ten tiny commits saying "fix" are not better work than two thoughtful commits. A good statistician always says what the data *does not* show.

## See it
On the practice repo:

```console
$ git log --date=short --format=%ad
2026-10-07
2026-10-05
2026-10-05
2026-10-02
2026-10-01
2026-10-01
```

Grouped into a frequency table:

| Date | Tally | Frequency |
|---|---|---|
| 2026-10-01 | \|\| | 2 |
| 2026-10-02 | \| | 1 |
| 2026-10-05 | \|\| | 2 |
| 2026-10-07 | \| | 1 |
| **Total** | | **6** |

And as a bar chart (text version):

```
commits
  2 |  ##        ##
  1 |  ##   ##   ##   ##
    +----------------------
       1 Oct 2 Oct 5 Oct 7 Oct
```

There are two modes (1 Oct and 5 Oct). The mean over the 4 working days is 6 ÷ 4 = **1.5 commits per day**.

*Bonus:* a computer can count for you — `git log --date=short --format=%ad | sort | uniq -c` prints each date with its count. You will learn how pipes (`|`) work in Grade 9.

## Collect (10 min)
**Tier 1+:** in your repo (the practice repo, or your own article repo), run

```bash
git log --date=short --format=%ad
```

Each line is the date of one commit. **Tier 0:** use the printed `log-sample.txt` from the practice repo, or the dates on your Module 2 cards.

Make a **tally table** in your notebook with columns *Date · Tally · Frequency*, as in the example above.

## Chart (15 min)
Draw a bar chart on graph paper:

1. **x-axis:** dates (in order — even days with zero commits, if you want to show gaps).
2. **y-axis:** number of commits; choose a scale that fits the paper (1 square = 1 commit).
3. Draw one bar per date. Bars do not touch.
4. Give the chart a **title**, and label **both axes**.

Optional on computer: type the table into LibreOffice Calc, select it, and *Insert → Chart → Column*.

## Interpret (5 min)
- Which day has the most commits? That is the **mode**.
- What is the **mean** number of commits per working day? (total commits ÷ number of days with commits)
- Was it better to commit a little every day or a lot on one day? Why might one be safer? (Think about Module 5 and power cuts.)

## Common mistakes
| Mistake | Fix |
|---|---|
| Counting *lines of output* as days | group the same dates first, then count |
| Dates out of order on the x-axis | sort them oldest → newest |
| Scale too big or too small | choose so the tallest bar uses most of the paper |
| Reading the chart as "who worked best" | commits measure activity, not quality |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Chart **commits per author** instead: `git log --format=%an` on a repo with several authors (your teacher can make one, or use the class Module 7 repos later). Which chart type fits better, bar or pie? Why? | 1 | 15 min | chart + reason |
| 2 | *Pro Git* [§2.3 **Viewing the Commit History**](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History) has a table of `--format` codes. Pick two more codes (for example `%h` and `%s`) and print a custom history. | 1 / 3 | 10 min | your command + output |
| 3 | **Hours of the day:** `git log --date=format:%H --format=%ad` prints the hour of each commit. Make a frequency table for your own repo. When do you work most? | 1 | 15 min | table + one sentence |
| 4 | **Paper version:** using the dates on all the class's Module 2 cards, build one class frequency table and chart on chart paper for the wall. | 0 | 20 min | wall chart |

## Exit ticket (5 min)
1. What is the frequency of commits on the busiest day in your chart?
2. Calculate the mean commits per day for your repo.
3. *Check:* "More commits always means better work." Agree or disagree and explain.

## Key points
- A repository's history is a **data set**: dates, authors, messages.
- `git log --format=…` extracts exactly the data you want.
- Frequency table → bar chart → mode and mean.
- Commit counts measure **activity, not quality**.

## New words
**frequency table**, **mode**, **mean**, **`--format`** — see the [glossary](../../glossary.md).

## Extension quest
Chart "commits per hour of the day" with `--format=%ad --date=format:%H`. Then compare with a classmate: who works in the morning, who in the evening?
