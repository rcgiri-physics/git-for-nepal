---
id: g12-m05-security
grade: 12
hours: 2
prerequisites: [g12-m02-branching-strategies]
outcomes:
  - "Keep secrets out of a repo and respond if one leaks"
  - "Explain what signed commits prove"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 5. Security: secrets and safe habits

## Hook
A student commits an API key to a public repo. Within minutes bots have copied it.

## Concept (unplugged or visual first)
Deleting a file in a new commit does **not** remove it from history. Rule: **a leaked secret is a burned secret** — revoke/change it first, then clean up.

## PRIMM lab
1. In a *practice* repo commit a fake `config.py` with `API_KEY = "FAKE-123"`; find it in history with `git log -p -S FAKE-123`.
2. **Predict** whether a new commit that removes it hides it. Check.
3. Add `.env` to `.gitignore` and use environment variables instead.
4. Overview (no setup): signed commits prove *who* made a commit.
5. **Make:** write an incident checklist (revoke → rotate → clean history → tell team).

## Parsons practice
Order the response to a leak: *revoke the key · create a new one · remove from the code · rewrite history if needed · tell the team*.

## Exit ticket
1. Does deleting a file remove it from history?
2. What belongs in `.gitignore`?
3. *Misconception:* 'private repos mean secrets are safe.'

## Teacher notes
Use only fake secrets in class. Never ask students to use real credentials. History rewriting tools (filter-repo) are teacher-demo only.
