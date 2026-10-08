---
id: g9-m05-remotes
grade: 9
hours: 2
prerequisites: [g9-m04-merge]
outcomes:
  - "Explain a remote as another copy of the repo"
  - "Clone, push and pull using a LAN server, bundle or class organisation"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 5. Remotes: clone, push, pull

## Hook
How do two computers share work without e-mailing files back and forth?

## Concept (unplugged or visual first)
Draw two computers, each with its own full history, and a third 'server' computer. Arrows: **clone** copies everything once; **push** sends new commits; **pull** brings new commits. Nothing moves until you say so.
**Tier 1 (offline):** pass work by `git bundle` on USB.

## PRIMM lab
**Tier 2 (Forgejo LAN) or tier 3 (class organisation, students 13+):**
1. Teacher gives each pair a remote URL. `git clone <url> ward-facts`.
2. **Predict** then run `git remote -v`.
3. Commit locally, `git push origin main`. Check on the server's web page.
4. Partner `git pull`. Predict what changes. **Investigate** `git log`.
5. **Modify:** both edit different files, push in turn. What if both push at the same time? (The second must `pull` first.)
**Tier 1:** `git bundle create share.bundle --all`, pass the USB, partner runs `git pull share.bundle main`.
6. **Make:** write a 3-step teamwork routine on a poster: pull · work · push.

## Parsons practice
Order: *pull · edit · add · commit · push*.

## Exit ticket
1. Does `git commit` send anything over the network?
2. What does `git clone` copy?
3. *Misconception:* 'GitHub is Git.' True or false?

## Teacher notes
Students under 13 must not create accounts on GitHub; use the LAN server or teacher-managed accounts. Never use real emails. Typical error: 'rejected, non-fast-forward' → pull first. Auth: use the server's HTTP with pseudonymous account; delay SSH keys until Grade 10.
