# Appendix A. Command cheat sheet

Commands grouped by the grade where they are taught. `<file>`, `<branch>`, `<id>` are placeholders — replace them, without the `< >`.

## Set up once per computer (teacher, Grade 8–9)
```bash
git config --global user.name "Student 07"            # pseudonym in school
git config --global user.email "s07@example.invalid"
git config --global init.defaultBranch main
git config --global pull.rebase false                 # pull = fetch + merge
git config --global core.editor "code --wait"         # VS Code instead of Vim
```

## Grade 8 — my own history
| I want to… | Command | Button (VS Code) |
|---|---|---|
| make a folder a repository | `git init` | *Initialize Repository* |
| see where my changes are | `git status` | Source Control panel |
| stage a file | `git add <file>` | **+** |
| commit | `git commit -m "Add …"` | ✓ Commit |
| see the history | `git log --oneline` | Timeline / Graph |
| see one commit's change | `git show <id>` | click the commit |
| see my uncommitted changes | `git diff` | click the file |
| throw away uncommitted edits ⚠ | `git restore <file>` | *Discard Changes* |
| bring back an old version | `git restore --source=<id> <file>` | — |
| undo a commit safely | `git revert <id>` | *Revert* |
| dates for statistics | `git log --date=short --format=%ad` | — |

## Grade 9 — branch and share
| I want to… | Command |
|---|---|
| where am I / what's here / move / make folder | `pwd` · `ls` · `cd <path>` · `mkdir <name>` |
| see staged changes | `git diff --staged` |
| list / create+switch / switch branch | `git branch` · `git switch -c <branch>` · `git switch <branch>` |
| draw the graph | `git log --oneline --graph --all` |
| merge a branch into the current one | `git merge <branch>` |
| give up a merge | `git merge --abort` |
| copy a repository | `git clone <url>` |
| send / receive commits | `git push origin <branch>` · `git pull` |
| download without merging | `git fetch` |
| list remotes | `git remote -v` |
| move a repo by USB | `git bundle create x.bundle --all` · `git clone x.bundle` · `git pull x.bundle main` |
| commits with their diffs | `git log -p` |
| tag a version | `git tag v1.0` (push: `git push origin v1.0`) |
| commits per person | `git shortlog -s -n` |

## Grade 10 — team workflows
| I want to… | Command |
|---|---|
| connect the original project of my fork | `git remote add upstream <url>` |
| update my fork | `git fetch upstream` · `git merge upstream/main` · `git push origin main` |
| push a new branch and track it | `git push -u origin <branch>` |
| fix a conflicted PR | `git fetch origin` · `git merge origin/main` · resolve · `git add` · `git commit` · `git push` |
| annotated tag | `git tag -a v1.0.0 -m "…"` |
| what changed since a release | `git log --oneline v1.0.0..main` · `git diff v1.0.0 main --stat` |
| patches without a server | `git format-patch main` · `git am *.patch` |
| close an issue from a commit | message contains `Closes #12` |

## Grade 11 — contributor tools
| I want to… | Command |
|---|---|
| search tracked files | `git grep "word"` |
| park unfinished work | `git stash` · `git stash list` · `git stash pop` |
| fix the last commit (not pushed) | `git commit --amend` |
| undo commits, keep changes staged (not pushed) | `git reset --soft HEAD~1` |
| undo commits and changes ⚠ (not pushed) | `git reset --hard HEAD~1` |
| replay my branch on new main | `git rebase main` (then `git push --force-with-lease` on **your own** branch only) |
| tidy last 3 commits | `git rebase -i HEAD~3` |
| find "lost" commits | `git reflog` |
| copy one commit here | `git cherry-pick <id>` |
| search history | `git log --grep="fix"` · `git log --author="…"` · `git log -S "text"` |

## Grade 12 — engineering
| I want to… | Command |
|---|---|
| inspect objects | `git cat-file -t <id>` · `git cat-file -p <id>` · `git ls-tree HEAD` |
| hash a file | `git hash-object <file>` |
| who last changed each line | `git blame <file>` · `git blame -L 10,20 <file>` |
| find the bad commit | `git bisect start` · `git bisect bad` · `git bisect good <id>` · … · `git bisect reset` |
| automatic bisect | `git bisect run bash check.sh` |
| describe a commit by nearest tag | `git describe --tags` |
| signed commit | `git commit -S -m "…"` |
| large files | `git lfs install` · `git lfs track "*.mp4"` |

## Which undo do I need?
| Situation | Pushed / shared? | Use |
|---|---|---|
| messy edits, not committed | — | `git restore <file>` ⚠ edits lost |
| staged something by mistake | — | `git restore --staged <file>` |
| want an old version of a file | — | `git restore --source=<id> <file>` then commit |
| bad commit | **yes** | `git revert <id>` |
| bad last commit message / forgot a file | no | `git commit --amend` |
| several messy commits | no | `git reset --soft HEAD~N` then commit |
| need to stop for a moment | — | `git stash` |
| lost commits after reset/rebase | — | `git reflog`, then `git reset --hard <id>` or `git branch rescue <id>` |
| secret committed | either | **revoke the secret first**, then see Grade 12 Module 5 |

## Names for commits
| Write | Means |
|---|---|
| `HEAD` | the commit you are on |
| `HEAD~1`, `HEAD~2` | one / two commits before HEAD (first parents) |
| `HEAD^2` | the second parent of a merge commit |
| `main`, `origin/main`, `v1.0` | the commit a branch, remote branch or tag points to |
| `a..b` | commits reachable from `b` but not from `a` ("what's new in b") |
| `<id>:<path>` | a file as it was in a commit (`git show v1.0:README.md`) |

## Reading `git status -s`
| Code | Means |
|---|---|
| `??` | untracked |
| `A ` | new file, staged |
| `M ` | modified, staged |
| ` M` | modified, not staged |
| `MM` | staged, then modified again |
| ` D` | deleted, not staged |
| `UU` | conflict (both modified) |
| `!!` | ignored (with `--ignored`) |

Offline help: `git help <command>` or `git <command> -h`.
