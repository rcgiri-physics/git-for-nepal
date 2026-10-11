# Part I. Teaching version control as a foundation

This part is for **teachers, teacher trainers and curriculum planners**. It explains *why* the lessons in Parts II–VI are ordered and designed the way they are, so that you can teach them well, adapt them to your school, and judge whether your students have built a real foundation — not just memorised commands.

!!! abstract "In one paragraph"
    Teach **one mental model** early and keep returning to it: *a commit is a snapshot of the whole project, with a message, pointing to its parent; branches and tags are labels on commits; every copy of a repository is complete.* Teach it **on paper before on screen**, **with buttons before commands**, **with safe tools before sharp ones**, **alone, then in pairs, teams and communities**. Assess the **process** (the history) and not only the product. Everything else in this book is built on that.

## 1. What "foundation" means

After five years a student should leave school with three things:

1. **A correct mental model** of how version control works — robust enough that they can reason about a command they have never seen ("this rewrites history, so I must not use it on a shared branch").
2. **Habits** that have become automatic — small commits with clear messages, reading the diff before committing, pulling before pushing, reviewing kindly, never committing secrets or private data.
3. **Judgement** — knowing which tool fits a situation, when to ask, how to work in someone else's project, and how to bring version control into *any* new project (Part VIII).

Commands change; hosts come and go; a solid model, good habits and judgement last a career.

## 2. The concept spine: eight strands over five grades

Each strand starts simply and deepens every year. When you teach a lesson, know which strand it belongs to and what came before.

| Strand | Grade 8 | Grade 9 | Grade 10 | Grade 11 | Grade 12 |
|---|---|---|---|---|---|
| **A. History and snapshots** | commit = snapshot + message + parent; reading `log` and `diff` | CLI cycle; `diff --staged` | history as team evidence | message conventions; reading others' history | objects, hashes, refs |
| **B. Undo and safety** | restore, revert | switching protects work | revert on shared branches | stash, reset, rebase, reflog — the golden rule | secret leaks; history rewriting as incident response |
| **C. Branching and integration** | (one line only) | branch = label; merge; conflicts | conflicts on PRs; merge `main` in | rebase vs merge | strategies; protection; bisect |
| **D. Sharing and remotes** | (one computer) | clone, push, pull, bundles | forks, `upstream` | contributing to other projects | CI/CD, releases as distribution |
| **E. Collaboration and communication** | messages for others | pair agreement | issues, PRs, review, charter | triage, etiquette, conventions | review of AI-assisted work; capstone process |
| **F. Automation and quality** | — | `.gitignore` | check scripts, CI intro | data reproducibility | CI workflows, SemVer, scanners |
| **G. Ethics, licences, privacy, security** | no real names; pseudonyms | no secrets in repos | credit on the public web | licences and attribution | secrets, signing, supply chain, AI policy |
| **H. Version control beyond code** | essays, magazine | data and SQL scripts | websites | open data | pathways; any project (Part VIII) |

**Using the spine:** when a student struggles in Grade 11 with rebase, the problem is often in strand A or C (they do not see branches as labels on commits) — go back to the Grade 9 sticky-note model before going forward.

## 3. Threshold concepts

Some ideas are *thresholds*: once understood, everything after makes sense; until then, students memorise and get stuck. Plan extra time, paper models and repeated checks for these.

| Threshold concept | Introduced | Diagnostic question | If they don't have it |
|---|---|---|---|
| A commit is a **whole snapshot**, not a list of changes | G8 M2 | "If you delete commit 3's card, can you still rebuild commit 4?" (yes — each card is complete) | repeat the paper-commit game |
| Changes move through **three places** (working copy, staging area, history) | G8 M3 | "You saved but `git status` shows *modified*. Where is your change?" | three trays on the desk |
| **Saving ≠ committing** | G8 M3 | "The power went off. Which work is safe?" | demonstrate after a real power cut |
| A **branch is a label**, not a copy | G9 M3 | "How much disk space does a new branch use?" (almost none) | sticky notes on cards |
| Every clone is a **complete, equal copy** | G9 M5 | "The server breaks. What is lost?" (nothing that anyone has pulled) | acting out with card rows |
| Merging compares with a **common ancestor** | G9 M4 | "Why is there no conflict when we edit different lines?" | paper merge game |
| **Adding vs rewriting** history | G8 M5 → G11 M5 | "Your teammate already pulled. Revert or reset?" | card table with a second group |
| **Objects never change; refs move** | G12 M1 | "Why does rebase change commit ids?" | object graph on paper |

## 4. Mental models to teach — and to avoid

| Teach | Avoid | Why |
|---|---|---|
| Commit = photo of the whole project + caption | "Git saves your changes" | leads to "a commit is a diff" and to confusion with Ctrl+S |
| History = chain of commits pointing to parents | history = a list of file versions | branches and merges need the graph |
| Branch = sticky note on a commit | branch = a folder / a copy | makes switching "disappearing files" incomprehensible |
| HEAD = "you are here" pointer | HEAD = "the newest commit" | detached HEAD then makes sense |
| Remote = another full copy with a name | remote = "the cloud" / "GitHub" | Git ≠ GitHub; offline and LAN work become obvious |
| Pull = fetch + merge | pull = download | explains why pull can conflict |
| Conflict = Git asking a human | conflict = error / failure | reduces panic |
| Revert = new opposite commit; reset = move a label | "undo" as one thing | students choose the wrong undo |
| PR = request + discussion pointing at a branch | PR = a copy of the code | updates by pushing to the branch make sense |

## 5. Misconception catalogue

Use these as exit-ticket items, discussion prompts and test distractors. Each lesson's exit ticket already includes one.

| # | Misconception | Correct idea | Addressed in |
|---|---|---|---|
| 1 | Git saves every keystroke | only commits are saved snapshots | G8 M2 |
| 2 | Saving the file puts it in history | only a commit does | G8 M3 |
| 3 | A diff shows the whole file | only changed lines plus context | G8 M4 |
| 4 | Once committed, mistakes can't be fixed | restore / revert | G8 M5 |
| 5 | Revert deletes the bad commit | it adds an opposite commit | G8 M5 |
| 6 | More commits = better work | activity ≠ quality | G8 M6 |
| 7 | The terminal does things by itself | it only runs what you type | G9 M1 |
| 8 | `git add` saves to history | it stages | G9 M2 |
| 9 | A branch is a full copy | it is a label | G9 M3 |
| 10 | After a conflict my work is lost | both sides are kept until you decide | G9 M4 |
| 11 | Git = GitHub | GitHub is one host for Git repositories | G9 M5 |
| 12 | `commit` sends work to the server | only push does | G9 M5 |
| 13 | If code works, history doesn't matter | history explains, debugs, undoes | G9 M6 |
| 14 | Git can merge live databases | version the scripts, not the database | G9 M7 |
| 15 | A fork is a branch | a fork is a whole server-side repository | G10 M2 |
| 16 | A PR is a copy of the code | it points at a branch | G10 M3 |
| 17 | Reviewing is for experts | anyone can spot clarity and checks | G10 M4 |
| 18 | Conflicts mean someone did wrong | conflicts are normal in parallel work | G10 M5 |
| 19 | A tag moves with new commits | tags stay | G10 M6 |
| 20 | A passing check means a perfect page | checks cover only their rules | G10 M8 |
| 21 | If it's online, it's free to use | no licence = no permission | G11 M1 |
| 22 | Rebase and merge give identical history | rebase rewrites into a line | G11 M5 |
| 23 | Messages are only for me | they are for every future reader and tool | G11 M6 |
| 24 | Agile means no planning | planning is frequent and small | G11 M7 |
| 25 | If I can download data, I can redistribute it | check the licence | G11 M8 |
| 26 | Git stores differences | the model stores snapshots | G12 M1 |
| 27 | Gitflow is always professional | choose by context | G12 M2 |
| 28 | Green CI means no bugs | only the written checks passed | G12 M3 |
| 29 | Private repos keep secrets safe | a leaked secret is burned | G12 M5 |
| 30 | If tests pass, the AI change is fine | tests may be weakened or incomplete | G12 M6 |
| 31 | Blame is for punishing people | it finds context and who to ask | G12 M7 |

Research on learners' confusions with Git (e.g. Isomöttönen and Cochez, 2014) found many of the same problems — especially the staging area, branches and remote synchronisation — which is why this book spends paper-model time on exactly those.

## 6. Sequencing principles

These rules decided the order of every lesson.

1. **Concept before commands.** Paper and visual models come first; commands name an idea students already have (Wagner and Thurner, 2025, recommend separating concepts from tool skills).
2. **Low floor → high ceiling: GUI → CLI → internals.** Grade 8 uses buttons (VS Code, GitHub Desktop); Grade 9 the terminal; Grade 12 the plumbing. Every student can pass Grade 8; fast learners always have an extension quest.
3. **Safe tools before sharp tools.** Restore and revert in Grade 8; reset and rebase only in Grade 11, with the golden rule.
4. **Local before remote.** One computer (G8) → two computers (G9) → a server with a team (G10) → strangers' projects (G11) → automation (G12).
5. **Solo → pair → team → community.** Social complexity grows with technical complexity, not before it.
6. **Delay accidental complexity.** SSH keys, credential helpers and configuration details are postponed; pseudonymous HTTP accounts and bundles keep early lessons about ideas.
7. **Real, Nepali, open artefacts.** A class magazine, a ward-facts script, a school website, a contribution, a capstone — each grade ends with something real (the "Nepal data thread").
8. **Spiral back.** Every grade revisits earlier strands at a deeper level (e.g. undo: restore → revert → reset/reflog → incident response).

## 7. Lesson design in practice

### PRIMM with Git
**P**redict → **R**un → **I**nvestigate → **M**odify → **M**ake (Sentance, Waite and Kallia, 2019). For Git, the "program" is a command and the "output" is the repository state:

| Stage | Git example |
|---|---|
| Predict | "Write what `git status` will say after `git add`." |
| Run | run it; compare with the prediction |
| Investigate | "Why is README listed twice?" (staged + modified) |
| Modify | change the scenario: edit after staging, then predict again |
| Make | create your own scenario and challenge a partner |

Insist on *written* predictions; that is where learning happens.

### Parsons problems
Jumbled steps to put in order (Parsons and Haden, 2006). They test understanding of *sequence and dependency* without requiring recall of syntax — ideal for mixed-ability rooms and for Tier 0. Every lesson has a set; printable strips are on the [Grade 8 cards page](../grade-08/cards.md).

### Unplugged models
Cards, string, sticky notes, trays, floor maps and acting out make invisible structures visible. They also make every lesson possible with **no computer at all** (Tier 0).

### Live demonstration ("think aloud")
When you demonstrate on the projector, *type slowly and say your thinking*: "Before I commit, I always check the diff — let me read it… oh, I left a debug line." Make a mistake on purpose and fix it. Students copy habits more than commands.

### Pair programming
**Driver** (keyboard) and **navigator** (reads, predicts, checks), swapping every 10 minutes. It halves the number of computers needed and doubles the talking about ideas.

### Worked examples and fading
Each lesson's *See it* section is a worked example with real output. In later lessons, show less and ask more ("fade" the support).

## 8. Assessment progression

| Grade | Formative | Practical | Summative |
|---|---|---|---|
| 8 | exit tickets; reading the card rows | 3 commits + restore + revert | commit-history rubric (Class Magazine), oral "show me yesterday's version" |
| 9 | predict-the-status worksheets | create → branch → merge → push | pair project rubric; Parsons card test |
| 10 | review-comment quality | PR with review; fix a conflicted PR | team rubric with individual rows; viva |
| 11 | claim comments; licence attributions | merged contribution | `CONTRIBUTIONS.md` portfolio; data project rubric |
| 12 | CI logs, security checklist | bisect a planted bug | capstone (100-point rubric); viva |

### Assess the process: read the history
The repository **is** the evidence. Before marking a product, read `git log` (or the card row): Are commits small and meaningful? Do messages say what and why? Did the student restore, revert, resolve, review? Is there work across several sessions? `git shortlog -s -n` shows contribution, but **read messages and reviews, not only counts** — counts are easy to game and unfair to students who make fewer, larger, well-explained commits.

### Fitting a marks-based exam system
Every grade has a board-style item bank in `assessments/` (definitions, ordering, "what will this command do?", misconception true/false, short explanations). Practical rubrics give marks too, so internal assessment can combine both.

## 9. Running labs in Nepali schools

### Delivery tiers
| Tier | Setting | What to do |
|---|---|---|
| 0 | no computer | cards, string, sticky notes, printed diffs and logs; every lesson has an unplugged path |
| 1 | offline computers | USB kit: portable Git + VS Code, self-hosted Learn Git Branching, practice repos as `.bundle` files, *Pro Git* PDF |
| 2 | school LAN | Forgejo on a Raspberry Pi or old PC; issues, PRs and (with a runner) CI work exactly like GitHub |
| 3 | internet | GitHub / Codeberg / GitLab; GitHub Skills; real open-source contributions (learners 13+) |

### 40 students, 10 computers
- **Pairs at PCs, the rest at paper:** half the class runs the unplugged version while the other half is at computers; swap after 20 minutes.
- **Stations:** PCs for the lab, a table for Parsons strips, a table for the predict worksheet.
- **One projector:** the class predicts aloud; volunteers drive.

### Shared lab PCs
- Set a **pseudonymous identity per PC** (`Student 07`, `s07@example.invalid`) and `init.defaultBranch main`, `pull.rebase false`, and an easy editor (`code --wait`).
- Keep each student's repo on a named USB folder or a per-student folder; back up the whole folder **including `.git`**.

### Power cuts
Teach "commit often" as the defence. A commit is safe on disk even if the PC then loses power. After the power returns, run `git status` with the class — it is a perfect lesson.

### Windows quirks
Use **Git Bash** for the same commands as Linux; ignore `LF will be replaced by CRLF` warnings in Grade 8; in Grade 10–12, add a `.gitattributes` (`* text=auto`, `*.sh text eol=lf`) so scripts run in CI.

## 10. Differentiation and inclusion

- **Language:** explain in Nepali (or the students' home language); keep commands, code and branch names in English. The [glossary](../glossary.md) gives Nepali terms.
- **Colour:** diffs use colour *and* `+`/`-` signs; teach both. Printed materials are black-and-white friendly.
- **Support:** sentence starters for messages, printed step cards with screenshots, pre-filled tables, buddy pairing.
- **Stretch:** every lesson has an extension quest; GitHub Skills and Learn Git Branching levels for fast finishers.
- **Participation:** rotate driver/navigator and team roles so every student types, reviews and presents — including students who are quiet or new to computers.
- **No shame:** badges in each student's own `BADGES.md`, never a public leaderboard.

## 11. Safety, privacy and ethics

- **Under 13:** no online accounts (GitHub's terms require 13+). Grade 8 is entirely local.
- **Pseudonyms** for Git identities; never real emails.
- **No personal data** (names with marks, phone numbers, photos, addresses) in any repository, public or private.
- **Vetted projects only** for under-18 contributions; agree with maintainers in advance.
- **AI use:** a student may use an AI helper only if they can explain every line of the diff they commit; follow school and CDC policy (G12 M6).
- **Fake secrets only** in security lessons.

## 12. Growing as a teacher

You do **not** need to know Git before you start: teach Grade 8 one lesson ahead of your students.

1. Do the [3-hour training outline](../teachers/training-outline.md).
2. Work through Grade 8 yourself on paper and on a PC.
3. Read Software Carpentry's [git-novice](https://swcarpentry.github.io/git-novice/) lesson and the short paper by Blischak, Davenport and Wilson (2016) — see the [reading list](books.md).
4. Play [Learn Git Branching](https://learngitbranching.js.org/) up to the Remote tab.
5. For pedagogy, read Greg Wilson's [*Teaching Tech Together*](https://teachtogether.tech/).
6. Join or start a local community of practice; contribute your improvements to this book (Grade 11 Module 4 shows how).

## 13. A year plan template

Each grade is a "chapter" of 12–20 periods. A typical school-year layout (adjust to CDC hours and your timetable):

| Term | Grade 8 | Grade 9 | Grade 10 | Grade 11 | Grade 12 |
|---|---|---|---|---|---|
| 1 | M1–M3 | M1–M3 | M1–M4 | M1–M3 | M1–M3 |
| 2 | M4–M6 | M4–M6 | M5–M8 | M4–M6 | M4–M7 |
| 3 | M7 project + exhibition | M7–M8 project | M9 team project | M7–M8 data project | M8 capstone, M9 |

## 14. Research base

- Wagner, A. and Thurner, V. (2025). *Rethinking How We Teach Git: Pedagogical Recommendations and Practical Strategies for the Information Systems Curriculum.* Journal of Information Systems Education, 36(1). <https://jise.org/Volume36/n1/JISE2025v36n1pp1-12.html>
- Sentance, S., Waite, J. and Kallia, M. (2019). *Teaching computer programming with PRIMM: a sociocultural perspective.* Computer Science Education, 29(2–3). doi:10.1080/08993408.2019.1608781
- Isomöttönen, V. and Cochez, M. (2014). *Challenges and Confusions in Learning Version Control with Git.* In ICTERI 2014, Communications in Computer and Information Science, Springer. doi:10.1007/978-3-319-13206-8_9
- Parsons, D. and Haden, P. (2006). *Parson's programming puzzles: a fun and effective learning tool for first programming courses.* Proceedings of the 8th Australasian Computing Education Conference.
- Blischak, J. D., Davenport, E. R. and Wilson, G. (2016). *A Quick Introduction to Version Control with Git and GitHub.* PLOS Computational Biology. <https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004668>
- Raspberry Pi Foundation, *PRIMM* quick read (see `research/sources.md`, S8).

The full list of sources used to build this book is in `research/sources.md` in the repository.
