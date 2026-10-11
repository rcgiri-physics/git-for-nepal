---
id: g12-m05-security
grade: 12
hours: 2
prerequisites: [g12-m02-branching-strategies]
outcomes:
  - "Keep secrets out of a repo and respond if one leaks"
  - "Explain what signed commits prove"
  - "Name supply-chain risks and basic defences"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 5. Security: secrets and safe habits

!!! abstract "At a glance"
    **Time:** 2 periods · **Tiers:** 1–3 · **You need:** a *throwaway* practice repo; **fake** secrets only

    **Before this:** Grade 9 Module 6 (`.gitignore`), Grade 12 Modules 1 and 3.

    **By the end you can:** keep secrets and private data out of repositories, find a leaked secret in history, respond correctly to a leak, and explain signing and supply-chain basics.

!!! danger "Classroom rule"
    Use only **fake** secrets like `FAKE-123`. Never type a real password, token or key into a practice repository, chat or AI tool.

## Hook (5 min)
A student commits an API key to a public repository. Within minutes, automated bots that scan public repositories have copied it, and someone starts using it — on the student's bill. The student deletes the file and commits again. *Is the key safe now?*

## Understand it

### History remembers everything
From Module 1: every commit stores a full snapshot, and old objects never change. **Deleting a file in a new commit does not remove it from history** — anyone with a clone can run `git log -p` or `git show <old-commit>:config.py` and read it. And every clone, fork and backup has a copy.

> **A leaked secret is a burned secret.** Revoke it and make a new one — *first*. Cleaning history comes after, and never fully un-leaks it.

### What counts as a secret or private data?
Passwords, API keys and tokens, SSH private keys, database connection strings, `.env` files, certificates — and in schools: **students' names with marks, phone numbers, addresses, photos, citizenship or exam numbers**. Private data in a repo is a privacy breach, even in a "private" repository (people leave teams; repos get made public; laptops get lost).

### Keeping secrets out
1. **Configuration from the environment.** The code reads `os.environ["API_KEY"]`; the value lives in a `.env` file on your PC (or in the CI's secret store), never in Git.
2. **`.gitignore`** `.env`, `*.pem`, `*.key`, local databases. Commit an **example** file without real values: `.env.example` with `API_KEY=put-your-key-here`.
3. **Check before committing:** `git diff --staged`, always.
4. **Scanners:** tools like **gitleaks** scan commits and history for things that look like secrets; run them in a **pre-commit hook** and in CI. Many hosts also scan pushes ("push protection").
5. **CI secrets:** stored in the host's settings (*Secrets*), injected at run time, masked in logs, and **not given to PRs from forks**.

### Responding to a leak — the incident checklist
1. **Revoke / rotate** the secret immediately (the service's dashboard) and create a new one.
2. **Remove** it from the code; switch to environment variables.
3. **Check** whether it was used (the service's logs).
4. **Rewrite history if needed** (e.g. `git filter-repo`), force-push, and ask everyone to re-clone — a **teacher/maintainer** task, because it rewrites shared history (Grade 11's golden rule — this is the rare justified exception).
5. **Tell the team** what happened and what changed, without blame; add a scanner so it doesn't happen again.

For private data about people: also inform whoever is responsible (the teacher, the school), following the school's policy.

### Signed commits: proving who
Anyone can type any `user.name` and `user.email` (you did: "Student 07"!). Git cannot tell whether a commit really came from the person named. **Signing** a commit (with a GPG or SSH key: `git commit -S`) adds a cryptographic signature; hosts then show **Verified**. A signature proves *who made the commit and that it was not changed* — not that the code is good.

### Supply chain: trusting what you depend on
Your project depends on other people's code (libraries, actions, Docker images). Attackers sometimes publish look-alike packages (`requets` instead of `requests`) or take over abandoned ones. Defences:

- add dependencies deliberately; check name, maintainers, activity and licence;
- **pin versions** (`requirements.txt` with exact versions; `actions/checkout@v4` or a full commit hash);
- let a tool alert you about known vulnerabilities (Dependabot, Renovate, `pip-audit`);
- check your project's health with **OpenSSF Scorecard**;
- protect `main` and require review (Module 2) — the best defence against a single bad change.

## See it
```console
$ git log --oneline
b71c0e2 Remove API key from config        <- "fixed"?
4d9a113 Add config with API key
$ git log -p -S "FAKE-123" --oneline       <- search every diff for the string
b71c0e2 Remove API key from config
-API_KEY = "FAKE-123"
4d9a113 Add config with API key
+API_KEY = "FAKE-123"
$ git show 4d9a113:config.py               <- still readable from history
API_KEY = "FAKE-123"
```

The safe version:

```python
# config.py — committed
import os
API_KEY = os.environ.get("API_KEY")        # value comes from the environment
```

```gitignore
# .gitignore
.env
```

```bash
# .env.example — committed, no real values
API_KEY=put-your-key-here
```

## Unplugged: where is the secret? (15 min)
Hand out printed "repository snapshots": a commit history with diffs, a `.gitignore`, a CI log, a screenshot of a README. Teams find all the leaks (a key in an old diff, a phone number in test data, a token printed in a CI log, a password in a README example) and write the incident checklist for each.

## PRIMM lab (50 min)
1. In a *practice* repo commit a fake `config.py` with `API_KEY = "FAKE-123"`; find it in history with `git log -p -S FAKE-123`.
2. **Predict** whether a new commit that removes it hides it. Remove it, commit, then check with `git show <old-id>:config.py`.
3. Switch to the safe version: environment variable, `.env` in `.gitignore`, `.env.example` committed. Run the program with `API_KEY=FAKE-456 python app.py`.
4. **Investigate (Tier 1+ with the tool installed):** run `gitleaks detect` (or `gitleaks git`, depending on version) on the practice repo. Does it find `FAKE-123`? Read its output.
5. Overview (no setup needed): signed commits prove *who* made a commit. On the host, find a commit marked *Verified* and look at what it shows.
6. **Make:** write an incident checklist for your capstone (revoke → rotate → remove → check use → clean history → tell team) and add it to `SECURITY.md`.

## Parsons practice (5 min)
Order the response to a leak: *revoke the key · create a new one · remove from the code · rewrite history if needed · tell the team*.

## Common mistakes
| Mistake | Fix |
|---|---|
| Deleting the file and thinking it's gone | it is in history: revoke first |
| Cleaning history before revoking | attackers already have it — revoke first |
| "It's a private repo, so it's fine" | private ≠ secret; people and settings change |
| Secrets printed in CI logs (`echo $TOKEN`) | never print; hosts mask known secrets, not derived ones |
| Real student data used as "test data" | use synthetic data |
| Installing a package because a blog said so | check it first; pin versions |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | GitHub Skills [**Secure your repository's supply chain**](https://github.com/skills/secure-repository-supply-chain) (13+, account). | 3 | 60 min | completed course |
| 2 | [gitleaks](https://github.com/gitleaks/gitleaks) README: how would you run it as a pre-commit hook? | 3 | 20 min | config snippet |
| 3 | *Pro Git* [§7.4 **Signing Your Work**](https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work): what is the difference between signing a tag and signing a commit? | 3 | 20 min | answer |
| 4 | [OpenSSF Scorecard](https://scorecard.dev/): look up the checks it runs. Which three would matter most for your capstone? | 3 | 20 min | 3 checks + reasons |
| 5 | [pre-commit](https://pre-commit.com/): set up one hook that blocks committing files named `.env`. | 1 / 3 | 30 min | `.pre-commit-config.yaml` |

## Exit ticket (5 min)
1. Does deleting a file remove it from history?
2. What belongs in `.gitignore`?
3. *Misconception:* "Private repos mean secrets are safe."

## Key points
- History keeps every committed byte; **a leaked secret is a burned secret** — revoke first.
- Secrets live in the environment or CI secret stores; commit only `.env.example`.
- Scan with tools (pre-commit, CI, host push protection); always read `git diff --staged`.
- Signed commits prove who and integrity, not quality.
- Supply chain: choose dependencies carefully, pin versions, get alerts, require review.

## New words
**secret**, **API key / token**, **environment variable**, **revoke / rotate**, **secret scanning**, **signed commit**, **supply chain**, **dependency pinning** — see the [glossary](../../glossary.md).

## Extension quest
Find out what `git filter-repo --replace-text` does, and why a maintainer must coordinate with everyone who has a clone before using it.

## Teacher notes
- **Timing:** P1: hook 5, understand 25, unplugged 10. P2: see it 5, lab 30, Parsons + exit 5.
- **Use only fake secrets in class. Never ask students to use real credentials.** History rewriting tools (filter-repo) are teacher-demo only.
- `gitleaks` command names changed between versions — check `gitleaks --help` on the lab build before class.
- Connect to the school's own data-protection rules for student records.
- **Answer key:** Exit 1: No — it stays in earlier commits and in every clone. 2: `.env`, keys, local databases, generated files — anything secret or regenerable. 3: False.
