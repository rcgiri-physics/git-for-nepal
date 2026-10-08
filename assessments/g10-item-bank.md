# Grade 10 item bank (board-style)

*Draft: not yet reviewed by a teacher.*

1. Difference between fork, clone and branch (one line each). [3]
2. What are the three parts of a good issue? [3]
3. What does 'Closes #7' in a PR description do? [2]
4. Give three things a reviewer checks. [3]
5. Rewrite 'this is bad' as a good review comment. [2]
6. Who resolves the conflict on a PR and how? [3]
7. What is a tag? Give an example of a semantic version for a first public release. [2]
8. Why is a static site easy to host? [2]
9. What does a CI check script return? [1]

Total: 21 marks.

## Answer key
1. fork = your own server copy of someone else's repo; clone = a local copy; branch = a label inside one repo.
2. Clear verb-first title, what/why, how we know it is done.
3. Links the PR to issue 7 and closes it when merged.
4. Does what the issue asks; small/understandable; runs; no private data; clear messages (any three).
5. Specific, kind, actionable, e.g. 'The heading is hard to read; could we use a darker colour?'
6. The author of the later PR: `git fetch`, merge `origin/main` into their branch, resolve, add, commit, push.
7. A permanent name for a commit; `v1.0.0`.
8. It is just files (HTML/CSS/images), served as they are without a database or server program.
9. Pass (exit 0) or fail (non-zero).
