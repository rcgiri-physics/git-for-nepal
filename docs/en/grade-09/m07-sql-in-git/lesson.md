---
id: g9-m07-sql-in-git
grade: 9
hours: 2
prerequisites: [g9-m06-python-in-git]
outcomes:
  - "Explain why we version scripts, not live databases"
  - "Keep schema and queries as .sql files in Git"
  - "Rebuild a database from versioned scripts"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 7. SQL under version control

!!! warning "Placement check"
    CDC's Class 10 computer textbook (2025 ed.) teaches **MySQL and databases (Unit 2)**. A Grade 9 syllabus has not been located, so students may not have met databases yet. Teach this module in Grade 10 (after Unit 2), or run it read-only with the provided files: the Git skill is the goal.

!!! abstract "At a glance"
    **Time:** 2 periods · **Tiers:** 1–3 · **You need:** `practice-repos/g09-ward-facts`; MySQL **or** SQLite (or Python's built-in `sqlite3` module)

    **Before this:** Module 6.

    **By the end you can:** explain the difference between a database and the scripts that build it, keep both schema and queries in Git, and rebuild the database from them at any time.

## Hook (5 min)
A database is a living thing: in a real ward office, records change every minute. What exactly would you put in Git — the whole database file, every minute? What happens when two people change it?

## Understand it

### Recipe vs. dish
Think of a database as a **dish** and the SQL scripts as the **recipe**. You cannot keep a history of a dish — it changes as people eat it — but you can keep a history of the recipe, and cook the dish again whenever you want.

| | Database file (`ward.db`, MySQL data folder) | SQL scripts (`schema.sql`, `queries.sql`) |
|---|---|---|
| What it is | the live data, in a binary format | plain text instructions |
| Readable diff? | no (binary) | **yes** — line by line |
| Merge two people's changes? | no | **yes**, like any text file |
| Size | can be huge | small |
| In Git? | **no** (add `*.db` to `.gitignore`) | **yes** |

So we version:

- **`schema.sql`** — the structure: `CREATE TABLE …` (and, for small teaching data, `INSERT …`).
- **`queries.sql`** — the questions we ask: `SELECT …`.
- later, **migrations** — numbered scripts that change the structure step by step (`001_create_wards.sql`, `002_add_area.sql`). This is how professional teams evolve databases; you will meet it again in Grade 12.

### Dumps
A **dump** is a database exported *as a recipe*: `mysqldump wards_db > dump.sql` (MySQL) or `sqlite3 ward.db .dump > dump.sql` writes SQL statements that recreate the tables and data. Dumps of small, shareable data can be committed; dumps containing **personal data must never be** — a ward database with names and phone numbers is private.

### Rebuild any time
Because the recipe is in Git, anyone can rebuild the exact database from any commit:

```bash
git switch main
sqlite3 ward.db < schema.sql       # cook the dish
sqlite3 ward.db < queries.sql      # ask the questions
```

Checkout an old commit and you can even rebuild **last month's** database — very useful for "the report used to say 6,210, why does it say 6,500 now?".

### Changing a table safely
When the structure changes, change **schema and queries together** in one commit, so every commit in history is consistent (the queries in commit X work with the schema in commit X).

## See it
```console
$ cat queries.sql
-- Q1: total population
SELECT SUM(population) AS total_population FROM wards;
-- Q2: the largest ward
SELECT ward_name, population FROM wards ORDER BY population DESC LIMIT 1;
$ sqlite3 ward.db < schema.sql
$ sqlite3 ward.db < queries.sql
6210
Test Ward Four|2310
$ git status --short
                                     <- nothing! ward.db is ignored by .gitignore
$ git diff                           (after adding a column in schema.sql)
-  households INTEGER NOT NULL
+  households INTEGER NOT NULL,
+  area_km2 REAL
```

No SQLite program? Python has one built in:

```bash
python -c "import sqlite3; c=sqlite3.connect('ward.db'); c.executescript(open('schema.sql').read())"
```

## Unplugged: recipe or dish? (10 min)
Pairs get cards: *a photo of the school register*, *the instructions for drawing the register's columns*, *the list of questions the head teacher asks every month*, *the filled-in register for October*, *a printed copy of all students' phone numbers*. Sort into **recipe (version it)**, **dish (rebuild it)**, **private (never share)**.

## PRIMM lab (50 min)
Repo: `practice-repos/g09-ward-facts` (your copy from Module 6).

1. Open `schema.sql` and `queries.sql`. **Predict** the result of each query on the data (add up the populations by hand!).
2. Run them (MySQL if available; or SQLite for offline: `sqlite3 ward.db < schema.sql`, then `sqlite3 ward.db < queries.sql`). The files use only portable SQL. Were you right?
3. **Investigate:** run `git status`. Why does `ward.db` not appear?
4. **Modify:** on a branch `query-small-wards`, add a query answering "which wards have fewer than 1,000 people?". Rebuild, run, commit, merge into `main`.
5. **Modify:** change the schema — add a column `area_km2 REAL` and give each `INSERT` a value (invent them; it is synthetic data). Add a query for population density (`population / area_km2`). Commit schema **and** queries together in one commit with a message that says why.
6. **Investigate:** `git log -p schema.sql` — read the history of the table's structure.
7. **Make:** write 3 questions about the dataset in a `QUESTIONS.md`, with the SQL answer for each.

## Parsons practice (10 min)
Order to change a table safely: *edit schema.sql · rebuild the database · run queries · git add · git commit*.

## Common mistakes
| Symptom | Cause | Fix |
|---|---|---|
| `ward.db` committed | missing `*.db` in `.gitignore` | `git rm --cached ward.db`, add the pattern, commit |
| `table wards already exists` | ran the schema twice without `DROP TABLE` | our schema starts with `DROP TABLE IF EXISTS`; keep it |
| A query works in MySQL but not SQLite | non-portable SQL | stick to standard `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY` |
| Old queries break after a schema change | schema and queries committed separately | commit them together |
| Real names or phone numbers in `INSERT` lines | private data | remove; use synthetic data; tell the teacher |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Software Carpentry [**Exploring History**](https://swcarpentry.github.io/git-novice/05-history.html) — use `git diff HEAD~1 schema.sql` and `git restore --source=HEAD~1 schema.sql` on your schema. | 1 / 3 | 15 min | commands used |
| 2 | **Rebuild last week:** use `git log` to find the first commit, then `git switch --detach <id>`, rebuild the database and run the queries. Compare the answers with today's. Return with `git switch main`. | 1 | 20 min | old vs new results |
| 3 | Make a dump: `sqlite3 ward.db .dump > dump.sql`. Compare `dump.sql` with `schema.sql` using `git diff --no-index schema.sql dump.sql`. | 1 | 15 min | 2 differences |
| 4 | Open data: look at the [Open Data Nepal](https://opendatanepal.com/) catalogue and find one small dataset whose licence allows sharing. Write a `DATA.md` for it (source, licence, date) — do not download yet. | 3 | 20 min | `DATA.md` draft |

## Exit ticket (5 min)
1. Why do we put `.sql` files in Git and not the database file?
2. What does a dump contain?
3. *Misconception:* "Git can merge two live databases." True or false?

## Key points
- Version the **recipe** (schema, queries, migrations), not the **dish** (the database file).
- SQL scripts are text: readable diffs, mergeable, small.
- Rebuild the database from any commit; change schema and queries **together**.
- Dumps are recipes too — but never commit personal data.

## New words
**schema**, **query**, **dump**, **migration**, **binary file** — see the [glossary](../../glossary.md).

## Extension quest
Split `schema.sql` into numbered migrations (`001_create_wards.sql`, `002_add_area.sql`) and write a one-line script that runs them in order.

## Teacher notes
- **Timing:** P1: hook 5, understand 15, sort 10, lab 1–3 (10). P2: lab 4–7 (35), Parsons 5, exit 5.
- Data is synthetic (invented wards). Do not commit the `.db` file (`*.db` is already in the starter's `.gitignore`). If MySQL is not installed, SQLite (or Python's `sqlite3`) is acceptable for the Git skill; say so to students.
- `git switch --detach` (exercise 2) gives a "detached HEAD" message — reassure students and make sure they return with `git switch main`.
- **Sort answers:** recipe — column instructions, monthly questions; dish — filled-in October register (rebuilt each month); private — phone numbers (and the photo of the register if it shows names).
- **Answer key:** Lab 1–2: 6210; Test Ward Four, 2310. Lab 4: Test Ward One (820), Test Ward Three (990), Test Ward Five (640). Exit 1: text scripts diff and merge; the database file is binary, large and changes constantly. 2: SQL statements that recreate the tables and data. 3: False.
