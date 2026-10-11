# Teacher guide — Module 6 (1 period)

**Goal:** apply Grade 8 statistics to a real data set the students produced themselves, and practise the critical point that activity ≠ quality.

**Timing:** hook 5 · collect 10 · chart 15 · interpret 5 · exit 5. "Understand it" can be read at home before the lesson.
**Materials:** graph paper, rulers, coloured pencils; printed `practice-repos/g08-class-magazine/log-sample.txt` for Tier 0.

## Common errors
- Counting commit lines rather than commits per *date*. Model grouping on the board: circle equal dates, then tally.
- Scale choices that make bars unreadable; ask pairs to justify their scale.
- Reading the chart as a measure of quality. Use exit question 3 to discuss: commits measure activity, not quality.
- `--date=short` missing → long dates that are hard to group. Check the command.
- On Windows `sort | uniq -c` works in Git Bash, not in PowerShell — use Git Bash for the bonus.

## Fallbacks
Tier 0: use the printed `log-sample.txt` (dates are included); Tier 1: LibreOffice Calc optional.

## Cross-curricular link
Tell the mathematics teacher: this lesson practises frequency tables, bar charts, mode and mean with self-generated data. A joint lesson works well.

## Differentiation
- **Support:** give a pre-drawn axis frame.
- **Stretch:** exercises 1 and 3; ask "what would a *histogram* of commit sizes (lines changed, from `git log --stat`) look like?"

## Answer key
Answers depend on the repo. For `log-sample.txt`: 2026-10-01 → 2 commits, 10-02 → 1, 10-05 → 2, 10-07 → 1 (total 6). Busiest days: 10-01 and 10-05 (two modes). Mean over the 4 working days = 6 ÷ 4 = 1.5 commits per day. Exit 3: disagree — messages and content quality matter; many tiny meaningless commits are not better.
**Free-resource 1:** bar chart — authors are categories and we compare counts; a pie works only if parts of a whole matter and there are few authors.
**Free-resource 2:** e.g. `git log --format="%h %s"` → short id and subject.

## Extension quest
Chart "commits per hour of the day" with `--format=%ad --date=format:%H`.
