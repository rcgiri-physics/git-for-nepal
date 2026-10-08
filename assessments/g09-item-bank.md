# Grade 9 item bank (board-style)

*Draft: not yet reviewed by a teacher.*

1. Draw the history after: commit A, commit B on `main`, then `git switch -c fix` and commit C. Where do `main` and `fix` point? [3]
2. What is the difference between `git add` and `git commit`? [2]
3. Explain why branches are cheap (not a full copy of the folder). [2]
4. When does a merge conflict occur? What do `<<<<<<<`, `=======` and `>>>>>>>` mark? [3]
5. List the steps to resolve a conflict. [3]
6. What do `clone`, `push` and `pull` do? [3]
7. Why is `GitHub` not the same as `Git`? [2]
8. Why do we put `.sql` scripts in Git instead of the database file? [2]
9. Write a `.gitignore` entry list for a Python project with a SQLite file. [2]

Total: 22 marks.

## Answer key
1. `main` → B; `fix` → C; C's parent is B.
2. `add` puts changes in the staging area; `commit` stores a snapshot with a message.
3. A branch is just a label (pointer) to a commit.
4. Both branches changed the same lines; the markers show the two versions: yours above `=======`, the other branch below it.
5. Open the file; choose the final text and remove markers; `git add`; `git commit`.
6. clone copies a remote repo with history; push sends local commits; pull brings remote commits.
7. Git is the version-control tool; GitHub is one hosting service for Git repos (others: Codeberg, GitLab, Forgejo).
8. Scripts are small text files, diffable and mergeable; a live database changes constantly and its binary files are not mergeable. *Placement note: SQL is in the Grade 10 CDC textbook.*
9. `__pycache__/`, `*.pyc`, `*.db`.
