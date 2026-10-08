# Grade 12 item bank (board-style)

*Draft: not yet reviewed by a teacher.*

1. Name Git's four object types and what a commit points to. [3]
2. What does a branch file in `.git/refs/heads/` contain? [1]
3. Compare trunk-based development and Gitflow in two lines. [3]
4. What triggers a CI workflow and what does it do? [2]
5. Which version bump: renamed a command; added an option; fixed a typo? [3]
6. A secret was committed to a public repo and then deleted in a new commit. Is it safe? What now? [3]
7. Name two typical defects in AI-generated diffs. [2]
8. About how many tests does `git bisect` need for 64 commits? [2]
9. Give two ways Git is used beyond software development. [2]

Total: 21 marks.

## Answer key
1. blob, tree, commit, tag; a commit points to a tree and its parent commit(s).
2. One commit hash.
3. Trunk-based: tiny branches merged daily into main. Gitflow: long-lived develop/release/hotfix branches, suited to scheduled releases.
4. Events such as push or pull_request; it runs defined steps (checkout, install, test) and reports pass/fail.
5. MAJOR; MINOR; PATCH.
6. No — it is still in history. Revoke and replace it first, then clean history if needed and inform the team.
7. Invented functions, unrelated edits, deleted tests, licence-incompatible code, leaked secrets (any two).
8. 6 (log₂64).
9. Research reproducibility, documentation-as-code, data/ML versioning, translation.
