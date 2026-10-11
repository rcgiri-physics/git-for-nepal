---
id: g11-m08-data-project
grade: 11
hours: 3
prerequisites: [g11-m04-first-pr]
outcomes:
  - "Keep a dataset in Git with a changelog"
  - "Document source and licence in DATA.md"
  - "Separate raw and cleaned data and make cleaning reproducible"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 8. Data project: version, clean and document open data

!!! abstract "At a glance"
    **Time:** 3 periods · **Tiers:** 1 (data on USB), 2, 3 · **You need:** `practice-repos/g11-data-thread`, Python; optionally a real open dataset whose licence you have checked

    **Before this:** Modules 1 (licences) and 4 (contributing); Grade 9 Modules 6–7.

    **By the end you can:** set up a data repository that anyone can trust — raw data untouched, cleaning done by a script, every step in history, and source and licence documented.

## Hook (5 min)
Nepal's local-level boundaries were restructured in 2017. If your analysis of ward or municipality data uses an old copy, your answers are wrong — and nobody can tell which copy you used. **Version the data like code.**

## Understand it

### Why version data?
Data changes: new census rounds, corrections, new boundaries, cleaning fixes. Without history you cannot answer *"which data did this chart use?"*, *"who changed this number, and why?"* or *"can I reproduce last year's report?"*. Git answers all three — for data files that are text (CSV, JSON, GeoJSON) and of moderate size.

### The data rules
1. **Raw stays raw.** Put downloaded data in `raw/` and never edit it by hand. It is your evidence.
2. **Clean by script.** A script (`clean.py`) turns `raw/` into `clean/`. Anyone can re-run it and get the same result — the cleaning is **reproducible**.
3. **Document the source.** `DATA.md` records where the data came from, when, under which licence, and what you changed.
4. **Explain each change.** One cleaning step per commit, with a message saying why; a `CHANGELOG.md` entry per version of the dataset.
5. **No personal data.** Ever. Names, phone numbers, citizenship numbers stay out of repositories.

```
 raw/schools.csv  --clean.py-->  clean/schools.csv
   (untouched)      (in Git)       (in Git, or regenerated)
         \                              /
          +---- DATA.md: source, licence, date, changes ----+
```

### `DATA.md`: the data card
This repository uses a short format (see `datasets/README.md`):

```yaml
name: Synthetic school table (teaching data)
source_url: written for this project
licence: CC-BY-4.0
redistribution_ok: yes
attribution_text: Git for Nepal contributors, CC BY 4.0
personal_data: none
changes_made: raw/ is never edited; clean/ is produced by clean.py (strip spaces, Title Case, drop rows without a student count)
```

Add the **date retrieved** and the **version** of the source for real data.

### Licences for data
Module 1 applies: **being able to download data does not mean you may redistribute it.** Check the licence on the source page. OKN's `localboundaries` states CC BY 4.0; Open Data Nepal lists a licence per dataset — read it. If a repository has **no stated licence**, do not copy its data; **link** to it instead.

### Diffs for data
Because CSV is text, `git diff` shows exactly which rows changed. `git diff --stat` counts them. Useful options: `git diff --word-diff` (changes inside a row), and for large tables, compare with a small script instead. Very large files (hundreds of MB) do not belong in plain Git — see *Version control in any project* for Git LFS and DVC.

## See it
```console
$ cat raw/schools.csv
school_id,name,district,students
1,  test primary school ,Testpur,310
2,TEST SECONDARY SCHOOL,Testpur,540
3,Test Basic School,Demoganj,
4,test lower secondary school,Demoganj,225
$ python clean.py
3 rows written (1 dropped)
$ cat clean/schools.csv
school_id,name,district,students
1,Test Primary School,Testpur,310
2,Test Secondary School,Testpur,540
4,Test Lower Secondary School,Demoganj,225
$ git add clean/schools.csv
$ git commit -m "Clean school names and drop row without student count" \
             -m "Row 3 has no student count in the source; dropped rather than guessed."
```

## Unplugged: the data detective (15 min)
Give pairs a printed "raw" table with problems (extra spaces, mixed capitals, a missing value, a duplicate row) and two different "clean" versions made by two invented students — one documented, one not. Which clean version would you trust for a report to the municipality? Why? What would you need to know?

## PRIMM lab (3 periods)
Practice repo: `practice-repos/g11-data-thread` (synthetic starter). **Real data:** choose a dataset from Open Knowledge Nepal `localboundaries` (stated CC BY 4.0) or Open Data Nepal — **verify each licence yourself and record it**; do not copy data whose licence is unclear or missing (e.g. a repo with no stated licence).

1. Fetch the data (Tier 3) or use the teacher's USB copy (Tier 1). Commit it in `raw/` with a message naming the source and date.
2. `raw/` untouched; make `clean/` with a script `clean.py`. **Predict** how many rows the cleaning will change.
3. Run it; check with `git diff --stat` and `git diff` — were you right?
4. Add one cleaning step at a time (e.g. trim spaces → fix capitals → drop empty rows → convert BS dates), **one commit per step**, each message saying why.
5. Fill `DATA.md` (see `datasets/README.md` template). Add a `CHANGELOG.md` entry per dataset version; tag `data-v1.0`.
6. **Investigate:** delete `clean/`, re-run `clean.py`. Is the result identical? (`git status` should show no change — that is reproducibility.)
7. **Make:** open a PR proposing the dataset for the shared `datasets/` folder **only if its licence allows redistribution**.

## Parsons practice
Order: *download raw · commit raw · write cleaning script · commit clean · document in DATA.md*.

## Rubric
| Criterion | 3 | 2 | 1 |
|---|---|---|---|
| Raw data untouched, in `raw/` | yes | edited once, documented | edited |
| Cleaning by script, reproducible | re-run gives identical output | mostly | manual edits |
| One step per commit, messages explain why | yes | mostly | no |
| `DATA.md` complete (source, date, licence, changes, personal data) | all fields | most | missing |
| Licence checked and respected | yes, with evidence | checked | not checked |
| Changelog + tag | both | one | neither |

## Common mistakes
| Mistake | Fix |
|---|---|
| Editing `raw/` "just to fix one typo" | fix it in `clean.py`; raw stays evidence |
| Cleaning by hand in a spreadsheet | write the step in the script |
| Excel changes dates/IDs when saving CSV | edit CSV in a text editor or Python |
| Huge files committed | sample or link; consider Git LFS/DVC |
| Licence "probably fine" | check and record it, or link only |
| Personal data in the dataset | remove it before committing; tell the teacher |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | The Turing Way, [**Version Control**](https://book.the-turing-way.org/reproducible-research/vcs) — read the data versioning part. List two tools for large data. | 3 | 20 min | 2 tools |
| 2 | Software Carpentry [**Open Science**](https://swcarpentry.github.io/git-novice/10-open.html) and [**Citation**](https://swcarpentry.github.io/git-novice/12-citation.html): add a `CITATION.cff` to your data repo. | 1 / 3 | 25 min | `CITATION.cff` |
| 3 | Perez-Riverol et al., [*Ten Simple Rules for Taking Advantage of Git and GitHub*](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004947) — which rules did your project follow? | 3 | 30 min | rule list |
| 4 | Browse [OKN localboundaries](https://github.com/openknowledgenp/localboundaries): find its licence and how its files are organised. | 3 | 15 min | notes |
| 5 | [Citation File Format](https://citation-file-format.github.io/): check your `CITATION.cff` with its description of fields. | 3 | 10 min | corrected file |

## Exit ticket
1. Why keep raw and clean data apart?
2. What goes in `DATA.md`?
3. *Misconception:* "If I can download it, I can redistribute it."

## Key points
- Raw stays raw; clean by script; one step per commit; document in `DATA.md`.
- Reproducible = anyone re-runs the script and gets identical output.
- Check and record every licence; link when redistribution is not allowed.
- Never commit personal data.

## New words
**raw data**, **clean data**, **reproducible**, **data card / DATA.md**, **CITATION.cff** — see the [glossary](../../glossary.md).

---

**Chapter complete.** You have contributed to a real project and versioned real data. In Grade 12 you will look **inside** Git, design **branching strategies**, build **CI pipelines**, handle **security**, **review AI-written code**, hunt bugs with **blame and bisect**, and run a professional **capstone**.

## Teacher notes
- **Teacher checks every licence before class. No personal data. Link-only is always a safe fallback.**
- **Timing:** P1: hook + understand 20, detective 15, lab 1–2. P2: lab 3–5. P3: lab 6–7, peer check with the rubric.
- For Tier 1, prepare the dataset on USB together with its licence page saved as a PDF.
- **Data detective answers:** trust the documented version — it records source, steps and reasons and can be reproduced.
- **Answer key:** Exit 1: raw is evidence; clean can be regenerated and checked against it. 2: name, source, date, licence, redistribution, attribution, personal data, changes made. 3: False.
