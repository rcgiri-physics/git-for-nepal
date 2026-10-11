---
id: g12-m06-ai-diffs
grade: 12
hours: 2
prerequisites: [g12-m02-branching-strategies]
outcomes:
  - "Review a diff produced by an AI tool"
  - "Apply the rule: never commit what you cannot explain"
  - "Write and follow an AI-use policy for a repository"
tier_support: [0, 1, 2, 3]
license: CC-BY-4.0
---

# 6. Reviewing AI-assisted changes

!!! abstract "At a glance"
    **Time:** 2 periods · **Tiers:** 0 (printed diffs), 1–3 · **You need:** three prepared diffs "from an assistant" (teacher notes); no AI tool is required

    **Before this:** Grade 10 Module 4 (review), Modules 3 and 5.

    **By the end you can:** review AI-generated changes with a specific checklist, keep AI-assisted work in small explainable commits, and write a class AI-use policy.

## Hook (5 min)
A tool writes 60 lines for you in 10 seconds. They look tidy and confident. The program runs. Who is responsible if the lines delete a check, copy code under an incompatible licence, or send a password to a website? *You are — your name is on the commit.*

## Understand it

### AI assistants change the speed, not the responsibility
AI coding assistants can suggest code, tests, documentation and even whole pull requests. They are useful — and they make mistakes in particular ways, often while sounding very sure. The more code arrives at once, the more important review becomes. Everything in this book still applies, with one rule above all:

> **Never commit a change you cannot explain, line by line, in your own words.**

### Git is the safety net
- **Commit before you ask.** Then any AI change is just a diff against a known good state; `git restore .` or `git revert` undoes it.
- **Ask for small changes.** One function, one fix. Small diffs can be understood.
- **Read the whole diff** (`git diff`), not just the part you asked for.
- **Run the checks and tests** — and read what they *test*.
- **Commit separately**, with a message in your own words that says what and why.
- **Disclose** AI help where the project or school asks (e.g. a line in the PR description).

### Typical problems in AI-generated diffs
| Problem | What it looks like | How to catch it |
|---|---|---|
| **Invented API** ("hallucination") | calls a function or option that does not exist (`df.clean_nepali_dates()`) | run it; search the library docs |
| **Unrelated edits** | reformats 200 lines, renames variables you didn't ask about | `git diff --stat`; ask for a smaller change |
| **Weakened checks** | deletes or loosens a test, a validation or an `if` "to make it pass" | read every `-` line; why was it removed? |
| **Wrong but plausible logic** | off-by-one, wrong rounding, BS/AD date mix-up | test with known answers |
| **Security issues** | hard-coded keys, disabled certificate checks, SQL built from strings | Module 5 checklist; scanners |
| **Licence problems** | long copied passages from code under an incompatible licence | Grade 11 Module 1; ask where it came from |
| **Private data sent away** | you pasted student data or secrets into an online AI tool | never paste private data; use synthetic examples |
| **Outdated practice** | uses deprecated commands or old versions | check current docs |

### The AI-diff review checklist
On top of the Grade 10 checklist:

- [ ] I can explain **every** changed line.
- [ ] The diff contains **only** what I asked for.
- [ ] No test, check or validation was removed or weakened without a reason I agree with.
- [ ] Every function, option and library it uses **exists** (I checked).
- [ ] I tested it with at least one case where I **know the right answer**.
- [ ] No secrets, private data or licence-incompatible copied text.
- [ ] My commit message is in **my own words**.

### Policies
Schools, exam boards, companies and open-source projects set rules for AI use — some forbid it for assessed work, some require disclosure, some allow it freely. A clear **AI-use policy** in a repository (in `CONTRIBUTING.md`) tells everyone the rules. Follow your school's and CDC's guidance; this book does not require any AI tool.

## See it
A diff "from an assistant" that was asked to *"make check.sh also accept empty value fields"*:

```diff
--- a/check.sh
+++ b/check.sh
@@ -3,6 +3,4 @@
 f=data/sample.csv
-[ "$(head -1 "$f" | tr -d '\r')" = "id,name,value" ] || { echo "bad header"; exit 1; }
-tail -n +2 "$f" | tr -d '\r' | awk -F, 'NF!=3 || $1 !~ /^[0-9]+$/ || $3 !~ /^[0-9]+$/ {print "bad row: " $0; bad=1} END {exit bad}'
+tail -n +2 "$f" | awk -F, 'NF<2 {print "bad row: " $0}'
 echo "g12 ok"
```

Review: the header check was **deleted**; the row check no longer **fails** (no `exit`), so CI would stay green on bad data; ID and value validation are gone; `tr -d '\r'` was removed (Windows files will break). The tests still pass — because the checks were weakened. **Request changes.**

## Unplugged: spot the defect (20 min)
Print the three prepared diffs (teacher notes). Teams of three: one reads aloud, one marks each line ✓/?/✗, one fills the AI-diff checklist. Then each team explains the defect *in one sentence a Grade 9 student would understand*.

## PRIMM lab (50 min)
1. Teacher provides 3 diffs "from an assistant" (one correct, one with an invented function, one that deletes a check) — as patch files to apply with `git apply`, or printed.
2. **Predict** the defect type for each before running.
3. Apply each on a branch; run the checks; mark each line in the review checklist.
4. **Investigate:** for the invented function, find the real library documentation and show it does not exist. For the deleted check, show a bad input that now passes.
5. **Modify:** ask the assistant (or a peer playing "assistant") for a *smaller* change; commit it separately with your own message.
6. **Make:** write the class AI-use policy: what is allowed, what must be disclosed, the explain-every-line rule, what must never be pasted into a tool. Add it to your capstone `CONTRIBUTING.md`.

## Parsons practice (5 min)
Order: *ask for a small change · read the whole diff · run checks · explain it aloud · commit in your own words*.

## Common mistakes
| Mistake | Fix |
|---|---|
| Accepting a large change because it "works" | ask for small changes; read all of it |
| Trusting the tool's explanation of its own code | verify against docs and tests |
| Letting AI write the commit message | write it yourself — it shows you understood |
| Pasting real data or secrets into a tool | synthetic examples only |
| "Tests pass, so it's fine" | check whether tests were changed |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | GitHub Skills [**Review pull requests**](https://github.com/skills/review-pull-requests) (13+) — apply the AI-diff checklist to the course PR as well. | 3 | 45 min | review comments |
| 2 | Open Source Guides, [**How to Contribute**](https://opensource.guide/how-to-contribute/) — what does it say about being respectful of maintainers' time? Connect this to large AI-generated PRs. | 3 | 15 min | 3 sentences |
| 3 | Search the CONTRIBUTING file of two large open-source projects for "AI" or "generated". What do their policies say? | 3 | 20 min | comparison |
| 4 | **Paper:** rewrite three AI-written commit messages ("Updated code to improve functionality") in your own words from the diffs. | 0 | 10 min | messages |

## Exit ticket (5 min)
1. What is the golden rule for AI-written code?
2. Name two typical problems in AI diffs.
3. *Misconception:* "If tests pass, the AI change is fine."

## Key points
- You are responsible for every line you commit, whoever or whatever wrote it.
- Commit before asking; ask for small changes; read the whole diff; run and check tests; commit in your own words.
- Watch for invented APIs, unrelated edits, weakened checks, security and licence problems, and private data.
- Follow and write clear AI-use policies; disclose where required.

## New words
**AI assistant**, **hallucination (invented API)**, **AI-use policy**, **disclosure** — see the [glossary](../../glossary.md).

## Extension quest
Use `git log -S "functionName"` to find when a function was introduced, and check whether its first version came with a test.

## Teacher notes
- **Timing:** P1: hook 5, understand 20, spot the defect 15. P2: see it 5, lab 30, Parsons + exit 5.
- Policy is set by school and CDC guidance; this lesson does not require any specific AI tool. Offline classes can use pre-made diffs.
- **The three prepared diffs** (make them on the capstone starter): (1) correct — adds a row-count check with a clear message; (2) invented function — a Python change calling `csv.read_clean()` (no such function in the standard library); (3) deleted check — the *See it* diff.
- **Answer key:** Exit 1: never commit what you cannot explain. 2: any two from the table. 3: False — tests may have been weakened or may not cover the change.
