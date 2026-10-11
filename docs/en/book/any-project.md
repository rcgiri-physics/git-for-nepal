# Part VIII. Version control in any project

Grades 8–12 taught version control through school projects. This part is a **practical handbook** for bringing it into *any* project you start or join — an essay, a thesis, a research analysis, a website, an app, a dataset, a design, a hardware build, an organisation's documents. Each section ends with a short checklist you can copy.

## 1. Should this project use version control?

Almost always **yes** if any of these is true:

- it will change over more than a few days;
- more than one person works on it;
- you might want an old version back;
- someone will need to know *why* it looks the way it does;
- it must be reproducible (research, data, reports).

**What to track** — anything a person writes and needs to rebuild the project:

| Track in Git | Don't track (ignore) | Never track |
|---|---|---|
| source code, scripts, notebooks (cleaned) | generated output, caches, builds | passwords, keys, tokens, `.env` |
| text: Markdown, LaTeX, HTML, CSV, JSON, YAML | local databases, logs, temp files | personal data about others |
| configuration and build files | editor/OS files (`.vscode/`, `.DS_Store`) | files you have no licence to share (in public repos) |
| small data you may share | very large data (→ LFS, DVC, or a link) | |
| documentation, licence, changelog | downloaded dependencies (`node_modules/`, `venv/`) | |

**Text beats binary.** Git can diff and merge text line by line. For binary formats (Word, Excel, Photoshop, video) it only knows "changed" — prefer text formats where you can (Markdown instead of Word, CSV instead of Excel), and see §7 for the rest.

## 2. The 10-step adoption playbook

Use these steps for a new project, or to bring an existing one under control.

1. **Make the folder a repository.** `git init my-project` (or *Initialize Repository* in VS Code).
2. **Add a `.gitignore` first** — before the first commit — from [github/gitignore](https://github.com/github/gitignore) for your language or tool, plus `.env`.
3. **Write a `README.md`:** what it is, how to run/build/read it, where data comes from, who to contact.
4. **Choose a licence** and add `LICENSE` (code: MIT/Apache-2.0/GPL; content and data: CC BY/CC BY-SA/CC0). Private project? Still note who owns it.
5. **First commit:** `git add . && git status` (check!) `&& git commit -m "Start project"`.
6. **Set up a remote — and a backup.** A host (GitHub, Codeberg, GitLab, a school/office Forgejo) or at least a bundle on a USB drive: `git bundle create backup.bundle --all`.
7. **Decide the branch rules.** Solo: work on short branches or directly on `main`. Team: branches + PRs, protected `main` (Grade 12 M2).
8. **Decide the review rule.** Team: at least one approval. Solo: review your own diff before every commit (`git diff --staged`).
9. **Automate a check.** Even one script (does it build? are links valid? is the CSV well-formed?) run in CI or a pre-commit hook.
10. **Release and record.** Tag meaningful versions (`v1.0.0`, `submitted-2026-11-30`), keep a `CHANGELOG.md`.

## 3. Where the repository lives: choosing a home

| Option | Good for | Watch out |
|---|---|---|
| **Local only** | private drafts, learning | one disk = one failure away from loss — add backups |
| **USB / external drive** (`git bundle` or a bare repo) | offline schools, backup | drives get lost; keep two |
| **School or office LAN server** (Forgejo, GitLab) | teams without reliable internet; private data stays in the building | someone must maintain and back it up |
| **Public host** (GitHub, Codeberg, GitLab.com) | open-source, portfolios, open data | everything public is public for ever |
| **Private repo on a host** | team work that must not be public | private ≠ secret (no passwords, no unnecessary personal data) |

**Backups: the 3-2-1 rule.** Keep **3** copies, on **2** different kinds of storage, **1** somewhere else. With Git this is easy: your laptop, a host or LAN server, and a bundle on a USB drive.

## 4. A sensible project layout

```
my-project/
├── README.md           what, how to run, contact
├── LICENSE             permission
├── CHANGELOG.md        what changed in each version
├── CONTRIBUTING.md     (teams) how to work together
├── .gitignore          what Git should ignore
├── .gitattributes      line endings, binary files, LFS
├── docs/               longer documentation
├── src/  or  scripts/  code
├── data/raw/           untouched inputs (if small and shareable)
├── data/clean/         produced by scripts
├── tests/  or  check.sh
└── .github/workflows/  (or .forgejo/workflows/) CI
```

Not every project needs every file. Start with README, LICENSE and `.gitignore`.

## 5. Recipes by project type

### 5.1 School assignments and homework
- One repository per subject or per big assignment.
- Commit at the end of every work session with a message that says what you did.
- Submit a **tag** (`submitted`) or the repository link if the teacher accepts it; the history shows your process (and protects you if someone claims you copied).
- **Checklist:** `.gitignore` · commit per session · tag on submission.

### 5.2 Essays, reports, theses and books
- Write in **plain text**: Markdown (convert with Pandoc to Word/PDF), or **LaTeX** (Overleaf has a [Git integration](https://www.overleaf.com/learn/how-to/Git_integration)).
- Put **one sentence per line** (or one paragraph per line): diffs become readable and two people's edits rarely conflict.
- Keep references in a `.bib` file; figures as files in `figures/` with the scripts that make them.
- Tag each version sent to a supervisor (`draft-1-to-supervisor`); their comments become issues.
- **Have to use Word?** Commit the `.docx` anyway (you still get history and backups), and make Git show text diffs with a converter — see *Pro Git* [§8.2 **Git Attributes**](https://git-scm.com/book/en/v2/Customizing-Git-Git-Attributes) ("Diffing Binary Files").
- **Checklist:** text format · line-per-sentence · tag per submission · bibliography in Git.

### 5.3 Research analysis and notebooks
- Separate `data/raw/` (never edited), `data/clean/` (made by scripts), `scripts/` or `notebooks/`, `results/` (usually ignored and regenerated).
- Record the software environment (`requirements.txt`, `environment.yml`).
- **Jupyter notebooks** store outputs inside the file, which makes huge, unreadable diffs: clear outputs before committing (or use a tool such as `nbstripout`), and use [nbdime](https://nbdime.readthedocs.io/) to diff and merge notebooks.
- Add `CITATION.cff` so others can cite your code; archive releases with a DOI service if your field expects it.
- Read: [The Turing Way — Version Control](https://book.the-turing-way.org/reproducible-research/vcs), *Ten Simple Rules for Taking Advantage of Git and GitHub*, *Good Enough Practices in Scientific Computing* (Part IX).
- **Checklist:** raw/clean split · environment file · clean notebooks · CITATION.cff · tag the version used in each paper.

### 5.4 Data projects
- Everything from Grade 11 Module 8: raw stays raw, clean by script, `DATA.md` with source, date, licence and changes, a changelog per data version.
- Validate the data in CI (header, types, row counts, no personal data columns).
- Large data: see §7.
- **Checklist:** DATA.md · licence checked · validation in CI · no personal data.

### 5.5 Websites and documentation sites
- Static sites (Grade 10 M7) or site generators (MkDocs, Hugo, Jekyll): content in Markdown, published by CI from `main`.
- Preview every PR before merging; run a link checker in CI.
- **Checklist:** `check` in CI · PR review · publish from `main` only · credits for images.

### 5.6 Programs and apps (any language)
- `.gitignore` for the language (build folders, virtual environments, `node_modules/`).
- Commit the **lock file** (`package-lock.json`, `poetry.lock`) for apps so builds are repeatable.
- Tests in CI from day one; branch protection when the team grows.
- SemVer releases if others depend on it (Grade 12 M4).
- **Checklist:** language `.gitignore` · lock file · tests in CI · releases.

### 5.7 Mobile apps and games
- Engines (Unity, Godot, Unreal) have ready `.gitignore` templates — use them; never commit the `Library/` or build caches.
- Art, audio and video → **Git LFS** (§7); consider LFS **file locking** so two artists don't edit the same binary at once.
- Keep signing keys and store credentials **out** of the repository.
- **Checklist:** engine `.gitignore` · LFS for assets · locking for binaries · no signing keys.

### 5.8 Design, images and other binary files
- Binary files can't be merged: agree **one owner per file** at a time, or use LFS locking.
- Keep **exports** (PNG, PDF) only if needed; keep the **source** (SVG, `.kra`, `.fig` export) as the tracked file.
- Prefer text-based formats where possible (SVG instead of PNG for diagrams).
- **Checklist:** source files tracked · owner per file · LFS above a few MB.

### 5.9 Spreadsheets
- Keep the **data** as **CSV** (diffable) and the calculations as a script; use the spreadsheet only to view.
- If you must keep `.xlsx`, also export the important sheets to CSV in each commit so changes are visible.
- Beware: spreadsheet programs silently change values when saving CSV (leading zeros in ward codes, dates). Check `git diff` after every save.
- **Checklist:** CSV as truth · formulas → scripts · check diffs for silent changes.

### 5.10 Arduino, Raspberry Pi and hardware
- Track sketches/code, wiring notes, circuit and PCB design files (KiCad files are text), a parts list (`BOM.csv`), photos of the build (LFS if many).
- Tag the version that is flashed onto each device (`device-a-v1.2`).
- **Checklist:** code + schematics + BOM · tag per flashed version · no Wi-Fi passwords in code (use a `secrets.h` that is git-ignored, with a `secrets.example.h`).

### 5.11 Translation and multilingual documentation
- One file per language (`docs/en/…`, `docs/ne/…`) with the same structure — as this book does.
- Mark which English version a translation follows (a commit id or a "last synced" note), so translators can run `git diff <that-id> -- docs/en/page.md` to see what changed since.
- Labels such as `needs-nepali-review`; native-speaker review on every PR.
- **Checklist:** parallel folders · "translated from" marker · reviewer per language.

### 5.12 Organisations: NGOs, offices, municipalities, schools
- Policies, procedures, forms, minutes and open data as **Markdown/CSV in a repository**; proposals for change as **PRs**; discussion in **issues**; approved versions as **tags** (`policy-2083-v2`).
- The history is an audit trail: who changed what, when, who approved it, and why.
- Personal data stays in proper record systems, **not** in Git.
- **Checklist:** text formats · PR for every change · approvals required · tagged official versions · no personal data.

### 5.13 Personal: notes, configuration files, portfolio
- A notes repository (Markdown) synced between devices.
- "Dotfiles" — your tool configurations — in a repository so a new computer is set up in minutes.
- A portfolio repository: `CONTRIBUTIONS.md`, `BADGES.md`, pathway map (Grade 12 M9).

## 6. Bringing an existing project under version control

### A folder full of `final_final` copies
You can turn renamed copies into a real history, oldest first, keeping their dates. Test on a **copy** of the folder:

```bash
#!/usr/bin/env bash
# Turn a folder of renamed copies into a Git history, oldest first.
# Usage: bash import-versions.sh <folder-with-copies> <target-file-name> <new-repo>
set -euo pipefail
src="$1"; target="$2"; repo="$3"
git init -q -b main "$repo"
ls -tr "$src" | while IFS= read -r f; do            # oldest first, by modification time
  when=$(date -r "$src/$f" +%Y-%m-%dT%H:%M:%S)
  cp "$src/$f" "$repo/$target"
  git -C "$repo" add "$target"
  GIT_AUTHOR_DATE="$when" GIT_COMMITTER_DATE="$when" \
    git -C "$repo" commit -q -m "Import old copy: $f"
done
git -C "$repo" log --date=short --format="%h %ad %s"
```

```console
$ bash import-versions.sh old-essays essay.md essay-history
9768672 2026-09-09 Import old copy: essay_final_final.md
21893f4 2026-09-05 Import old copy: essay_final.md
a95e70a 2026-09-01 Import old copy: essay.md
```

Now `git diff` between any two old versions works — the `final_final` problem from Grade 8, solved retroactively.

### A ZIP or shared-drive project
1. Copy the latest version into a new folder; `git init`; add `.gitignore`; commit "Import project as of <date>".
2. Keep the old ZIPs as an archive; don't try to reconstruct every past state unless it matters.
3. From now on, all changes go through commits.

### From another version control system
Subversion, Mercurial and others can be converted with dedicated tools (`git svn`, import tools on hosts). See *Pro Git* chapter 9 (*Git and Other Systems*).

## 7. Large files and binaries

Plain Git keeps every version of every file in every clone. A 200 MB video changed 10 times = 2 GB for everyone.

| Situation | Use |
|---|---|
| a few images, PDFs, small datasets (< a few MB each) | plain Git is fine |
| many or large binaries (art, audio, video, models) | **[Git LFS](https://git-lfs.com/)** — Git stores small pointers; the big files live on an LFS server |
| large datasets and ML models, pipelines | **[DVC](https://dvc.org/doc/start)** alongside Git |
| huge public data | don't copy — link to the source and record the version/date in `DATA.md` |

Git LFS in three commands:

```bash
git lfs install
git lfs track "*.psd" "*.mp4"      # writes rules into .gitattributes
git add .gitattributes
```

Check your host's LFS storage limits; a school Forgejo server can host LFS too.

## 8. Settings for different contexts

| | Solo | Team (school, office) | Open source |
|---|---|---|---|
| Branches | optional; short-lived | branch per issue | fork + branch per PR |
| Review | read your own diff | ≥ 1 approval | maintainers review |
| `main` | yours | protected; no direct pushes | protected; CODEOWNERS |
| CI | a simple check | required checks | required checks, from forks without secrets |
| Communication | commit messages | issues, PRs, charter | issues, PRs, CONTRIBUTING, code of conduct |
| Licence | still useful | agree with the organisation | essential |
| Releases | tags for milestones | tags + changelog | SemVer + changelog + release notes |

## 9. Introducing Git to a team that doesn't use it

1. **Start with a pain point** ("which version did we send to the ministry?"), not with Git itself.
2. **Start small:** one project, one champion, the GUI first (VS Code, GitHub Desktop) — Grade 8's path works for adults too.
3. **Write the conventions** on one page (branch names, messages, review rule) — Grade 11 M6.
4. **Teach the three ideas** that prevent most trouble: commit = snapshot; pull before push; never rewrite shared history.
5. **Make the safe way the easy way:** protected `main`, PR templates, a check in CI.
6. **Hold a short retrospective** after a month and adjust.

## 10. Security and backup checklist

- [ ] `.gitignore` includes `.env`, keys, local databases and generated files.
- [ ] Secrets come from environment variables or the host's secret store; only `*.example` files are committed.
- [ ] A secret scanner runs before commit or in CI.
- [ ] No personal data in the repository — public or private.
- [ ] `main` is protected (no force pushes; PR + review + checks for teams).
- [ ] Dependencies are pinned; alerts for known vulnerabilities are on.
- [ ] 3-2-1 backups exist (e.g. laptop + host/LAN + bundle on USB), and a restore was tested once.
- [ ] Someone other than you knows how to access the repository if you are away.

## 11. Templates

Copy and adapt. (All templates in this book are MIT-licensed.)

### `README.md`
```markdown
# Project name
One sentence: what this is and who it is for.

## How to run / read
1. ...
2. ...

## Data
Source, date retrieved, licence — see DATA.md.

## Contributing
See CONTRIBUTING.md. Questions: open an issue.

## Licence
Code: MIT. Content: CC BY 4.0. See LICENSE.
```

### `CONTRIBUTING.md`
```markdown
# Contributing
- Open or pick an issue first; comment before starting.
- Branch: type/short-topic (feat/, fix/, docs/).
- Commits: imperative summary ≤ 72 chars; body says why.
- Run the checks: `bash check.sh`.
- Open a PR with "Closes #N"; one approval needed; CI must be green.
- No secrets, no personal data. AI-assisted changes: you must be able to explain every line.
```

### Pull request template (`.github/pull_request_template.md` or `.forgejo/pull_request_template.md`)
```markdown
## What
## Why
Closes #
## How to check
## Checklist
- [ ] Checks pass locally
- [ ] Docs / changelog updated
- [ ] No secrets or personal data
```

### `.gitattributes`
```gitattributes
* text=auto
*.sh text eol=lf
*.png binary
*.jpg binary
*.pdf binary
```

### Minimal CI workflow (`.github/workflows/check.yml`; Forgejo: `.forgejo/workflows/check.yml`)
```yaml
name: check
on: [push, pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: bash check.sh
```

### `CHANGELOG.md`
```markdown
# Changelog
## [Unreleased]
## [1.0.0] - 2026-11-30
### Added
- First public version.
```

### `CITATION.cff`
```yaml
cff-version: 1.2.0
message: "If you use this, please cite it as below."
title: "Project name"
authors:
  - family-names: "Surname"
    given-names: "Given"
version: 1.0.0
date-released: 2026-11-30
license: CC-BY-4.0
```

## 12. Is my project well version-controlled? (final checklist)

- [ ] It is a repository with a README, LICENSE and `.gitignore`.
- [ ] Commits are small, with messages that say what and why.
- [ ] There is a remote **and** a backup.
- [ ] Branch, review and message rules are written down (teams).
- [ ] At least one automatic check runs.
- [ ] Versions that matter are tagged; a changelog exists.
- [ ] No secrets or personal data; large files handled with LFS/DVC or links.
- [ ] A new person could start contributing using only the documentation.
