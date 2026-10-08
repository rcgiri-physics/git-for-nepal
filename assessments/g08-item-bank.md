# Grade 8 item bank (board-style)

Marks in brackets. Answer key at the end.

## Group A — Very short answer (1 mark each)
1. What does a commit store besides the file contents? [1]
2. Name the command that lists the history of a repository. [1]
3. What is a diff? [1]
4. Which command shows what you changed since the last commit? [1]
5. Write one rule of a good commit message. [1]

## Group B — Short answer (2 marks each)
6. Why is naming files `essay_final_v3` a poor way to keep versions? Give two reasons. [2]
7. Explain the difference between *saving a file* and *committing it*. [2]
8. What is the difference between `restore` and `revert`? [2]
9. A student's chart shows 6 commits on Monday and 1 on Tuesday. Calculate the mean commits per day. [2]

## Group C — Long answer (4 marks each)
10. Describe the three places a change passes through (working copy, staging area, history) and name the action that moves it from one to the next. [4]
11. A classmate deleted the middle paragraph of a committed file and has not committed. Describe how to get it back, and what to check first. [4]

## Answer key
1. Message, author, date/time, pointer to parent commit (any one). 2. `git log`. 3. The difference between two versions of a file. 4. `git diff`. 5. Starts with a verb / says what and why / one idea (any one).
6. Any two: no order, no reason recorded, hard to see differences, easy to overwrite. 7. Saving writes the file in the editor; committing stores a snapshot with a message in the history. 8. `restore` discards uncommitted changes or brings back a file's old content; `revert` adds a new commit that undoes a past commit and keeps history. 9. (6 + 1) ÷ 2 = 3.5 commits per day.
10. Edit (working copy) → `add` → staging area → `commit` → history; 1 mark each for the three places, 1 for actions. 11. Check `git diff` (is this really what they want to undo?); `git restore article.md`; the paragraph returns from the last commit; warn that uncommitted work cannot be recovered after restore.
