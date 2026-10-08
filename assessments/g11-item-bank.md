# Grade 11 item bank (board-style)

*Draft: not yet reviewed by a teacher.*

1. What must you do when reusing a CC BY work? [2]
2. Why can't CC BY-NC-SA text be copied into a CC BY repo? [2]
3. When is `git revert` better than `git reset`? [3]
4. What does `git stash` do? [2]
5. State the golden rule about rewriting history. [2]
6. Write a good commit message for fixing the date format in a report header (#14). [2]
7. Why keep raw and clean data in separate folders? [2]
8. List four fields of a `DATA.md`. [2]
9. Match: backlog, increment, quality gate to Git artefacts. [3]

Total: 20 marks.

## Answer key
1. Credit the author, link the licence, say if you changed it.
2. Its NonCommercial and ShareAlike terms conflict with CC BY's permissions.
3. When the commit is already pushed/shared: revert adds an undoing commit and keeps history; reset rewrites history.
4. Parks uncommitted changes in a drawer so the working folder is clean; `stash pop` brings them back.
5. Never rewrite history others already have.
6. e.g. 'Fix date format in report header (#14)' with a body explaining why.
7. So the original stays untouched and every cleaning step can be reproduced and reviewed.
8. Name, source URL, retrieved date, licence, redistribution OK, attribution text, personal data, changes made (any four).
9. backlog → issues; increment → tag/release; quality gate → pull-request review.
