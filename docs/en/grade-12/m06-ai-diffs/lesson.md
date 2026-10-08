---
id: g12-m06-ai-diffs
grade: 12
hours: 2
prerequisites: [g12-m02-branching-strategies]
outcomes:
  - "Review a diff produced by an AI tool"
  - "Apply the rule: never commit what you cannot explain"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 6. Reviewing AI-assisted changes

## Hook
A tool writes 60 lines for you in 10 seconds. Who is responsible for them?

## Concept (unplugged or visual first)
You are. Git is the safety net: small commits, read the diff, run the tests, write the message in your own words. Typical AI diff problems: invented functions, unrelated edits, deleted tests, copied licence-incompatible code, leaked secrets.

## PRIMM lab
1. Teacher provides 3 diffs 'from an assistant' (one correct, one with an invented function, one that deletes a check).
2. **Predict** the defect type for each before running.
3. Run the checks; mark each line in the review checklist.
4. **Modify:** ask the assistant (or a peer) for a smaller change; commit separately.
5. **Make:** write the class AI-use policy: allowed, must disclose, must explain.

## Parsons practice
Order: *ask for a small change · read the whole diff · run checks · explain it aloud · commit in your own words*.

## Exit ticket
1. What is the golden rule for AI-written code?
2. Name two typical problems in AI diffs.
3. *Misconception:* 'if tests pass, the AI change is fine.'

## Teacher notes
Policy is set by school and CDC guidance; this lesson does not require any specific AI tool. Offline classes can use pre-made diffs.
