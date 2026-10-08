---
id: g9-m07-sql-in-git
grade: 9
hours: 2
prerequisites: [g9-m06-python-in-git]
outcomes:
  - "Explain why we version scripts, not live databases"
  - "Keep schema and queries as .sql files in Git"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 7. SQL under version control

!!! warning "Placement check"
    CDC's Class 10 computer textbook (2025 ed.) teaches **MySQL and databases (Unit 2)**. A Grade 9 syllabus has not been located, so students may not have met MySQL and databases (Unit 2) yet. Teach this module in Grade 10 (after MySQL and databases (Unit 2) is taught), or run it read-only with the provided files: the Git skill is the goal.

## Hook
A database is a living thing: it changes every minute. What exactly would you put in Git?

## Concept (unplugged or visual first)
Two things: the **recipe** (`schema.sql`: `CREATE TABLE`, `INSERT`) and the **questions** (`queries.sql`). Version the recipe; rebuild the database from it any time. A **dump** (`mysqldump`) can export a database to a recipe — but big binary database files do not belong in Git.

## PRIMM lab
Repo: `practice-repos/g09-ward-facts`.
1. Open `schema.sql` and `queries.sql`. **Predict** the result of each query on the data.
2. Run them (MySQL if available; or SQLite for offline: `sqlite3 ward.db < schema.sql`, then `sqlite3 ward.db < queries.sql`). The files use only portable SQL.
3. **Modify:** add a query answering "which wards have fewer than 1,000 people?" on a branch `query-small-wards`.
4. Change the schema (add a column `area_km2`). Commit schema and queries together, in one commit with a message that says why.
5. **Make:** write 3 questions about the dataset in a `QUESTIONS.md`, with the SQL answer for each.

## Parsons practice
Order to change a table safely: *edit schema.sql · rebuild the database · run queries · git add · git commit*.

## Exit ticket
1. Why do we put `.sql` files in Git and not the database file?
2. What does a dump contain?
3. *Misconception:* 'Git can merge two live databases.' True or false?

## Teacher notes
Data is synthetic (invented wards). Do not commit the `.db` file (add `*.db` to `.gitignore`). If MySQL is not installed, SQLite is acceptable for the Git skill; say so to students.
