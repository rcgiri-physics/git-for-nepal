---
id: g10-m04-code-review
grade: 10
hours: 2
prerequisites: [g10-m03-pull-requests]
outcomes:
  - "Review a pull request using a checklist"
  - "Give kind, specific, actionable comments"
  - "Respond to review feedback as an author"
tier_support: [0, 1, 2, 3]
license: CC-BY-4.0
---

# 4. Code review with a checklist

!!! abstract "At a glance"
    **Time:** 2 periods · **Tiers:** 0–3 (printed diffs work everywhere) · **You need:** an open PR from another pair (or a printed diff)

    **Before this:** Module 3.

    **By the end you can:** review a PR systematically, write comments that help, and respond to feedback without taking it personally.

## Hook (5 min)
A reviewer writes *"this is bad"* on your PR. How do you feel? What do you do next? Now imagine the comment said: *"The menu link on line 12 goes to `abuot.html` — should it be `about.html`?"* What changed?

## Understand it

### Why review?
**Code review** means a teammate reads your change *before* it is merged. It:

- **catches mistakes** — broken links, typos, bugs, private data;
- **shares knowledge** — now two people understand the change;
- **keeps quality consistent** — names, style, structure;
- **teaches both sides** — reviewers often learn more than authors.

Big software companies require at least one review for *every* change. Reviewing is a skill you can practise from today — you do not have to be an expert to notice a broken link or an unclear sentence.

### How to review: a routine
1. **Read the description and the issue.** What is this PR *supposed* to do?
2. **Look at the size.** Too big to understand? Ask for it to be split.
3. **Read the diff** (*Files changed*), top to bottom. Note questions.
4. **Run it.** Open the page / run the script on the branch: `git fetch origin && git switch feature/about-page`.
5. **Fill the checklist.**
6. **Write comments** on specific lines, then a summary.
7. **Decide:** *Approve*, *Request changes*, or *Comment* (just questions).

**Checklist**

- [ ] Does it do what the issue asks — no more, no less?
- [ ] Is it small enough to understand?
- [ ] Are names, messages and text clear?
- [ ] Does the page/program still run? Do the checks pass?
- [ ] Nothing private (names, phone numbers, passwords, marks) was added?
- [ ] Would a newcomer understand it?

### Writing helpful comments
A good comment is **specific**, **kind**, **actionable**, and **about the work, not the person**.

| Unhelpful | Helpful |
|---|---|
| "ugly" | "Could we use the school colour `#1a5276` for this heading, like on index.html?" |
| "wrong" | "Line 8 says 2045 BS but the notice board says 2043 BS — which is right?" |
| "you always forget the alt text" | "The image on line 15 needs `alt` text for screen readers, e.g. `alt="School gate"`." |
| "LGTM" on a 900-line PR | "This is too large for me to check carefully — could we split the gallery into its own PR?" |

Useful patterns: **"Could we…?"**, **"What do you think about…?"**, **"I wonder if…"**, and always some **praise**: "Nice — the menu now works on phones."

Label the weight of a comment: **nit:** (tiny, optional), **question:**, **suggestion:**, **must:** (blocks merging).

### Being reviewed
- Thank the reviewer; they spent time on *your* work.
- Answer every comment: fix it (push a commit and reply "Done in `a1b2c3d`") or explain why not.
- Disagree politely and with reasons. If stuck, ask a third person.
- Remember: the review is about the code, not about you.

### AI-written code gets the same review
If any part of a PR was written with an AI helper, it gets the same checklist — and the author must be able to explain every line. "The AI wrote it" is never a reason to approve.

## See it
A review on the *Files changed* tab:

```diff
  <nav>
    <a href="index.html">Home</a>
+   <a href="abuot.html">About</a>
```
> **suggestion:** The link points to `abuot.html`, but the file is `about.html`, so the link will be broken. Could you fix the spelling? `check.sh` should catch this too.

```diff
+ <p>Founded in 2045 BS by local families.</p>
```
> **question:** Is 2045 BS confirmed? The notice board photo in issue #2 says 2043 BS.

> **Summary — Request changes.** Thank you, the page reads well and the menu is consistent. Two things before merging: the link spelling, and the founding year. Everything else looks good.

## Unplugged: rewrite the comments (15 min)
Pairs get 10 unhelpful review comments on cards (see teacher notes). Rewrite each to be specific, kind and actionable. Then the class votes on the best rewrite of each. Finally, review a **printed diff** of a small web page with the checklist.

## PRIMM lab (50 min)
1. Swap PRs with another pair. **Predict** the riskiest line before reading in detail.
2. Read the diff, check out the branch and run the page (or `bash check.sh`). Fill the checklist.
3. Write **2 praise** comments and **2 improvement** comments on specific lines, plus a summary. Choose *Approve* or *Request changes*.
4. **Author:** reply to each comment, push fixes as new commits. **Reviewer:** check the new commits and approve.
5. **Investigate:** read the PR's conversation from top to bottom. Would a newcomer understand *why* the code looks the way it does?
6. **Make:** improve the checklist for your team and commit it to the repo as `REVIEW.md`.

## Parsons practice (10 min)
Match unhelpful comments to kind rewrites: "ugly" → "Could we use the school colour here?".

## Common mistakes
| Problem | Fix |
|---|---|
| Approving without running anything | always open/run the change |
| Only negative comments | add specific praise |
| Comments about the person | talk about the code |
| Reviewing a huge PR | ask for a split |
| Author ignores comments | team rule: every comment gets a reply |
| Arguing in comments for days | meet and talk; write the decision in the PR |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | GitHub Skills [**Review pull requests**](https://github.com/skills/review-pull-requests) (13+, account). | 3 | 45 min | completed course |
| 2 | Open Source Guides, [**How to Contribute**](https://opensource.guide/how-to-contribute/) — the section on communicating. Pick 3 tips that apply to reviews. | 3 | 15 min | 3 tips |
| 3 | Find a merged PR in a well-known open-source project with at least 5 review comments. Classify each comment: praise / question / suggestion / must. | 3 | 20 min | table |
| 4 | **Printed review (Tier 0):** the teacher gives a printed diff with 5 planted problems (broken link, phone number, typo, missing alt text, unclear message). Find them. | 0 | 15 min | list of 5 |

## Exit ticket (5 min)
1. Name three qualities of a good comment.
2. What should a reviewer check before approving?
3. *Misconception:* "Reviewing is only for experts." True or false?

## Key points
- Review catches mistakes, shares knowledge, and teaches both sides.
- Routine: description → size → diff → run → checklist → comments → decision.
- Comments: specific, kind, actionable, about the work; include praise.
- Authors answer every comment; the review is not personal.
- AI-written code gets the same review; the author must explain every line.

## New words
**code review**, **reviewer**, **approve**, **request changes**, **nit**, **LGTM** ("looks good to me") — see the [glossary](../../glossary.md).

## Extension quest
Use the host's **suggestion** feature (on GitHub: the ± icon in a line comment) to propose an exact fix the author can apply with one click.

## Teacher notes
- **Timing:** P1: hook 5, understand 15, rewrite cards 15, see it 5. P2: lab 35, Parsons 5, exit 5.
- **Reviewing teaches more than writing; grade the *quality of review comments*.** Suggested mini-rubric (6 points): specific (2), kind (2), actionable (2).
- Remind students that AI-generated code gets the same review as any other.
- **Unhelpful comment cards:** "ugly", "wrong", "no", "why??", "this is stupid", "fix", "LGTM" (on a huge PR), "you did it again", "I would never do it like this", "?".
- **Printed review planted problems:** `href="galery.html"`, a 10-digit phone number of a "student", "Libary", `<img src="gate.jpg">` with no alt, commit message "stuff".
- **Answer key:** Exit 1: specific, kind, actionable (about the work). 2: the checklist — does what the issue asks, small, clear, runs/checks pass, nothing private. 3: False — anyone can spot unclear text, broken links and missing checks.
