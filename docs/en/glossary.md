# Glossary

Terms used in this book, alphabetical. The grade column says where a term is first taught (8–12; "VIII" = Part VIII).

*Nepali column: first draft, needs native review (`needs-nepali-review`). Blank = not yet translated; the English term is commonly used.*

| Word | नेपाली | Meaning | Grade |
|---|---|---|---|
| absolute path | पूर्ण मार्ग | a path from the top of the folder tree, e.g. `/c/Users/s07/school` | 9 |
| AI-use policy | | written rules for using AI assistants in a project | 12 |
| amend | | replace the last commit (`git commit --amend`); only before pushing | 11 |
| annotated tag | | a tag that stores tagger, date and message (`git tag -a`) | 10 |
| API key / token | | a secret string that lets a program use a service; never commit it | 12 |
| approve | स्वीकृत गर्नु | a reviewer's decision that a PR may be merged | 10 |
| assignee | | the one person responsible for an issue | 10 |
| attribution (TASL) | श्रेय | credit with Title, Author, Source, Licence | 11 |
| backlog | | the ordered list of work not yet done (issues) | 11 |
| binary file | | a non-text file (image, Word, database); Git cannot show line diffs | 9 |
| bisect | | binary search through history to find the first bad commit | 12 |
| blame / annotate | | show the last commit, author and date for every line of a file | 12 |
| blob | | Git object holding one file's contents | 12 |
| branch | शाखा | a movable label pointing at a commit | 9 |
| branch protection | | host rules that stop direct or force pushes to a branch and require reviews/checks | 12 |
| breaking change | | a change that makes users' old use stop working → MAJOR version | 11 |
| bundle | | a single file containing a repository, for moving it by USB (`git bundle`) | 9 |
| changelog | परिवर्तन सूची | a human-written list of what changed in each version (`CHANGELOG.md`) | 9 |
| check script | | a program that answers pass/fail about the project (exit code 0 = pass) | 10 |
| cherry-pick | | copy one commit onto the current branch | 11 |
| CI (continuous integration) | | running checks automatically on every push or pull request | 10 |
| CD (continuous delivery/deployment) | | publishing automatically after CI passes | 12 |
| claim (an issue) | | comment that you will work on an issue, with a plan | 11 |
| clone | क्लोन | copy a whole repo with its history | 9 |
| closing keyword | | `Closes #N` / `Fixes #N` in a merged commit or PR closes issue N | 10 |
| code of conduct | आचारसंहिता | rules for how people behave in a project | 11 |
| code review | | a teammate reads and comments on a change before it is merged | 10 |
| CODEOWNERS | | a file naming who must review changes to which folders | 12 |
| commit | कमिट / स्न्यापसट | a saved snapshot of the whole project with a message, author, date and parent | 8 |
| commit id / hash | | the unique name of a commit (e.g. `78a873e…`), computed from its content | 8 |
| common ancestor | साझा पुर्खा | the last commit two branches share; merges compare against it | 9 |
| conflict | द्वन्द्व | two changes to the same lines that Git cannot combine alone | 9 |
| conflict markers | | `<<<<<<<`, `=======`, `>>>>>>>` lines showing both sides of a conflict | 9 |
| content-addressed | | stored under a name computed from the content (Git objects) | 12 |
| context line | | an unchanged line shown around changes in a diff | 8 |
| Conventional Commits | | message format `type(scope): summary`, e.g. `fix(menu): …` | 11 |
| CONTRIBUTING file | | a file explaining how to contribute to a project | 11 |
| copyright | प्रतिलिपि अधिकार | the creator's automatic right over their work | 11 |
| detached HEAD | | HEAD points directly at a commit, not at a branch | 9 |
| diff | फरक | the difference between two versions, line by line (`-` removed, `+` added) | 8 |
| dump | | a database exported as SQL statements that recreate it | 9 |
| environment variable | | a setting given to a program from outside its code (used for secrets) | 12 |
| exit code | | a number a program returns: 0 = success, other = failure | 10 |
| fast-forward | | a merge where the branch label simply moves forward; no merge commit | 9 |
| feature flag | | a switch in the code that turns a feature on or off | 12 |
| fetch | | download new commits from a remote without merging | 9 |
| fork | फोर्क | your own copy of someone else's repo on a server | 10 |
| `.git` folder | | the hidden folder where a repository keeps its history | 8 |
| `.gitignore` | | a file listing files Git should not track | 9 |
| Gitflow | | a branching strategy with `main`, `develop`, release and hotfix branches | 12 |
| GitHub flow | | strategy: `main` always releasable, one short branch + PR per change | 12 |
| HEAD | | the pointer to "where you are" — usually the current branch | 8 |
| history / log | इतिहास | the list of commits | 8 |
| host | | a service that stores Git repositories (GitHub, Codeberg, GitLab, Forgejo) | 9 |
| hotfix | | an urgent fix to a released version | 12 |
| increment | | a working, shown piece of progress at the end of an iteration | 11 |
| issue | मुद्दा / काम | a task, bug or idea written down on the server, with a number | 10 |
| kanban board | | a board with columns To do · Doing · Done | 10 |
| label | लेबल | a tag on an issue such as `bug` or `good-first-issue` | 10 |
| licence | इजाजतपत्र | written permission to use, change or share a work | 11 |
| maintainer | | a person who reviews and merges contributions to a project | 11 |
| merge | मिलाउनु | combine the work of two branches | 9 |
| merge commit | | a commit with two parents, joining two lines of work | 9 |
| merge request (MR) | | GitLab's name for a pull request | 10 |
| message | सन्देश | the text of a commit explaining what and why | 8 |
| milestone | | a target (date or version) grouping issues | 10 |
| modified | परिवर्तित | a tracked file that changed since the last commit | 8 |
| object | | a stored item in Git: blob, tree, commit or tag | 12 |
| origin | | the usual name of the remote you cloned from | 9 |
| pager | | a page viewer for long output; Space = next page, q = quit | 8 |
| parent | | the commit that came just before a commit | 8 |
| patch | | a text file containing a diff (`git format-patch`) | 10 |
| path | मार्ग | the address of a file or folder in the tree | 9 |
| plumbing / porcelain | | low-level Git commands / everyday friendly commands | 12 |
| pre-release | | a test version before a release, e.g. `2.0.0-rc.1` | 12 |
| process model | | the order in which a team does the work of building software | 11 |
| prompt | | the text before the cursor in a terminal, showing where you are | 9 |
| public API | | what users of a project rely on; changes to it decide the version bump | 12 |
| pull | ल्याउनु | fetch + merge commits from a remote | 9 |
| pull request (PR) | | a request to merge your branch, with diff, checks and discussion | 10 |
| push | पठाउनु | send commits to a remote | 9 |
| README | | the front page of a repository: what, how to run, who | 9 |
| rebase | | replay a branch's commits on a new base; rewrites history | 11 |
| reference (ref) | | a name pointing at a commit: branch, tag, HEAD, remote branch | 12 |
| reflog | | a local record of where HEAD has been; recovers "lost" commits | 11 |
| release | रिलिज | a tag plus notes (and files) for users | 10 |
| relative path | सापेक्ष मार्ग | a path from where you are now, e.g. `class9/ward-facts` | 9 |
| remote | टाढाको भण्डार | a copy of the repo on another computer or server | 9 |
| repository (repo) | भण्डार | a project folder that remembers its history | 8 |
| reproducible | पुनरुत्पादनीय | anyone can re-run the steps and get the same result | 11 |
| reset | | move the current branch label (`--soft`, mixed, `--hard`); rewrites if pushed | 11 |
| restore | पुनर्स्थापना | bring a file back to a committed version (`git restore`) | 8 |
| retrospective | पुनरावलोकन | a team meeting about what went well and what to change | 10 |
| revert | | undo a commit by adding a new opposite commit | 8 |
| reviewer | समीक्षक | the person checking a pull request | 10 |
| root commit | | the first commit; it has no parent | 9 |
| runner | | the machine that runs CI jobs | 12 |
| schema | | the structure of a database (`CREATE TABLE …`) | 9 |
| secret | गोप्य | a password, key or token; never commit it | 9 |
| semantic versioning (SemVer) | | MAJOR.MINOR.PATCH: break · add · fix | 10 |
| share alike (SA) | | a licence condition: changed versions must use the same licence | 11 |
| signed commit | | a commit with a cryptographic signature proving who made it | 12 |
| snapshot | स्न्यापसट | a complete picture of the project at one moment | 8 |
| spam PR | | a useless pull request made only to collect points | 11 |
| SPDX identifier | | the official short name of a licence, e.g. `MIT`, `CC-BY-4.0` | 11 |
| sprint | | a short fixed period of work in Scrum (1–4 weeks) | 11 |
| squash | | combine several commits into one | 11 |
| staging area (index) | | the "next snapshot" box you are preparing (`git add`) | 8 |
| stash | | a drawer for unfinished, uncommitted work (`git stash`) | 11 |
| static site | | a website made only of files, served as they are | 10 |
| switch | | change to another branch (`git switch`) | 9 |
| tag | ट्याग | a permanent name on one commit, e.g. `v1.0.0` | 9 |
| team charter | | a team's written roles, rules and privacy promises | 10 |
| terminal / shell | टर्मिनल | a window where you type commands | 9 |
| tree | | Git object for a folder: names → blobs and trees | 12 |
| triage | | sorting issues by clarity, size and priority | 11 |
| trunk-based development | | everyone merges small changes into `main` at least daily | 12 |
| unstage | | take a change out of the staging area (`git restore --staged`) | 8 |
| untracked | | a file Git has never been told to track | 8 |
| upstream | | the original repository a fork came from | 10 |
| version | संस्करण | the state of a work at one moment | 8 |
| version control system | संस्करण नियन्त्रण प्रणाली | a program that keeps the history of your files | 8 |
| workflow / pipeline | | a CI configuration: triggers, jobs and steps | 12 |
| working copy | काम गर्ने प्रति | the files you see and edit | 8 |
