# Appendix B. Troubleshooting: "Oops, Git!"

Real situations from classrooms and projects, with **safe** fixes. Before any fix: **stop, run `git status`, and read what Git says** — its hints are usually right. If you are unsure, copy the whole folder (including `.git`) as a backup first.

!!! tip "Two lifelines"
    - **Committed work is almost never lost:** `git reflog` remembers where you have been.
    - **Uncommitted work is fragile:** commit (or `git stash`) before trying anything risky.

## Setup and everyday messages

### 1. `Please tell me who you are`
Git needs a name and email for commits.
```bash
git config --global user.name "Student 07"
git config --global user.email "s07@example.invalid"
```

### 2. `fatal: not a git repository (or any of the parent directories)`
You are not inside a repository. Run `pwd`, then `cd` into the project folder (the one containing `.git`). If you never ran `git init` or `git clone`, do that.

### 3. A black screen with `~` signs (Vim) opened
Git wants a message. Type `:wq` and Enter to save and continue, or `:q!` and Enter to cancel. Avoid it next time: `git commit -m "…"`, or `git config --global core.editor "code --wait"`.

### 4. `git log` "froze" and I can't type
It opened a pager. **Space** = next page, **q** = quit.

### 5. `warning: LF will be replaced by CRLF`
Windows and Linux end lines differently. Harmless. For projects with shell scripts, add a `.gitattributes` with `* text=auto` and `*.sh text eol=lf`.

### 6. `error: pathspec 'Add' did not match any file(s)`
The message was not in quotes: `git commit -m Add README` → `git commit -m "Add README"`.

### 7. I committed in the wrong folder / my whole home folder is a repository
Someone ran `git init` in the wrong place. Find it: `git rev-parse --show-toplevel`. If it is your home folder, remove **only that `.git` folder** (ask the teacher; check the path twice).

## Commits

### 8. Wrong message in the last commit (not pushed)
`git commit --amend -m "Better message"`. Already pushed? Leave it; write a better message next time.

### 9. Forgot a file in the last commit (not pushed)
`git add forgotten.txt && git commit --amend --no-edit`.

### 10. Committed to `main` instead of a new branch (not pushed)
```bash
git branch feature/my-work        # label the commits where they are
git reset --hard origin/main      # move main back to the server's version
git switch feature/my-work        # continue on the branch
```
Check `git status` first: uncommitted changes would be lost by `--hard`.

### 11. I need to undo a commit that is already pushed
`git revert <id>` — adds an opposite commit; safe for everyone.

### 12. I discarded changes with `restore` and want them back
If they were never committed or stashed, Git cannot recover them. Check your editor's undo history or local history (VS Code: *Timeline → Local History*). Lesson: commit often.

### 13. I ran `git reset --hard` and lost commits
```bash
git reflog                       # find the line before the reset
git reset --hard <id-from-reflog>
```

### 14. I deleted a branch with work on it
`git reflog` shows the last commit of that branch; `git branch rescued <id>`.

## Branches

### 15. "My files disappeared!" after switching branches
They belong to the other branch's snapshot. `git switch <other-branch>` and they are back.

### 16. `Your local changes to the following files would be overwritten by checkout`
Git protects uncommitted work. Commit it, `git stash` it, or (if you don't need it) `git restore` it — then switch.

### 17. `You are in 'detached HEAD' state`
You checked out a commit or tag, not a branch. To look around: fine. To return: `git switch main`. To keep work made here: `git switch -c new-branch` **before** leaving.

## Merging and conflicts

### 18. `CONFLICT (content): Merge conflict in …`
Open the file; find `<<<<<<<`, `=======`, `>>>>>>>`; edit to the correct final text; delete all markers; `git add <file>`; `git commit`. To start over: `git merge --abort`. (Rebase: `git rebase --continue` / `--abort`.)

### 19. I committed conflict markers by mistake
Search: `git grep -n "<<<<<<<"`. Fix the files and commit again. Add a check to CI that fails on markers.

### 20. `fatal: You have not concluded your merge (MERGE_HEAD exists)`
A merge is half done. Finish (`git add …` + `git commit`) or `git merge --abort`.

### 21. My PR says "This branch has conflicts"
On your branch: `git fetch origin`, `git merge origin/main`, resolve, test, commit, `git push`.

## Remotes

### 22. `! [rejected] main -> main (fetch first)` / `non-fast-forward`
The remote has commits you don't have. `git pull`, resolve any conflict, `git push`. **Do not** force-push a shared branch.

### 23. `fatal: Need to specify how to reconcile divergent branches`
Choose how `pull` combines work, once: `git config --global pull.rebase false` (merge). Then `git pull` again.

### 24. `Authentication failed` / `Permission denied`
Check the account and URL (`git remote -v`). GitHub does not accept account passwords for HTTPS pushes — use a personal access token, a credential manager, or SSH keys. Pushing to someone else's repository? Push to **your fork** instead.

### 25. `repository not found`
URL typo, private repository, or no access. Copy the URL from the web page again; ask the owner for access.

### 26. I pushed to the wrong branch
Tell your team. If the wrong branch is shared, `git revert` the commits there and push them to the right branch (`git cherry-pick`). Ask the maintainer before any force push.

### 27. My push was rejected after a rebase
Expected: rebase made new commits. On **your own** PR branch only: `git push --force-with-lease`.

## Files and ignoring

### 28. A file is still tracked after adding it to `.gitignore`
`.gitignore` affects only untracked files. `git rm --cached <file>`, commit.

### 29. `.gitignore` doesn't work at all
On Windows it may have been saved as `.gitignore.txt`. Rename it (turn on "show file extensions"). Check patterns with `git check-ignore -v <file>`.

### 30. The repository is huge / clone is slow
Large binaries were committed. For the future: Git LFS or DVC (Part VIII §7). Removing them from history requires rewriting it — a maintainer task with `git filter-repo`, coordinated with everyone who has a clone.

## Security and privacy

### 31. I committed a password, key or token
1. **Revoke/rotate it now** (the service's settings) — assume it is stolen.
2. Remove it from the code; use environment variables and `.gitignore`.
3. Tell the teacher/maintainer; they decide about rewriting history.
See Grade 12 Module 5.

### 32. I committed someone's personal data (names with marks, phone numbers, photos)
Stop pushing; tell the teacher immediately. Remove it in a new commit; the teacher/maintainer decides about history rewriting and who must be informed, following the school's policy.

## CI

### 33. CI is red but it works on my computer
Read the first failing step's log. Common causes: a file you forgot to commit (`git status`), a dependency installed only on your PC, Windows line endings in scripts, upper/lower case in file names (Linux is case-sensitive).

### 34. The workflow never runs
Wrong folder (`.github/workflows/` or `.forgejo/workflows/`), wrong file extension (`.yml`), wrong trigger, YAML indentation error, or (Forgejo) no runner with the label in `runs-on`.

## Still stuck?
- `git help <command>` (works offline).
- Software Carpentry's [git-novice](https://swcarpentry.github.io/git-novice/) episodes and *Pro Git* [§2.4 Undoing Things](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things).
- [Dangit, Git!?](https://dangitgit.com/) for quick rescues; [Git Flight Rules](https://github.com/k88hudson/git-flight-rules) for everything else.
- Ask: describe what you ran, what you expected, and paste the exact message — never paste secrets.
