---
id: g9-m05-remotes
grade: 9
hours: 2
prerequisites: [g9-m04-merge]
outcomes:
  - "Explain a remote as another copy of the repo"
  - "Clone, push and pull using a LAN server, bundle or class organisation"
  - "Recover from a rejected push by pulling first"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 5. Remotes: clone, push, pull

!!! abstract "At a glance"
    **Time:** 2 periods · **Tiers:** 1 (USB bundles), 2 (school Forgejo), 3 (class organisation; learners 13+) · **You need:** a remote URL from the teacher, or a USB stick

    **Before this:** Module 4 (merge).

    **By the end you can:** clone a repository, push your commits, pull your partner's, and fix "rejected — fetch first".

## Hook (5 min)
How do two computers share work without e-mailing files back and forth, and without losing anyone's changes? Today your repository learns to travel.

## Understand it

### Every copy is complete
Git is **distributed**: when you copy a repository, you get **all** of its history, not just the latest files. Your laptop's copy, your partner's copy and the server's copy are equals. A **remote** is simply *another copy of the same repository* that your copy knows about, with a name — usually **`origin`** for the place you cloned from.

```
            [ server: Forgejo / GitHub / Codeberg ]
               origin  (a full copy, with history)
              ^   |                        ^   |
         push |   | pull              push |   | pull
              |   v                        |   v
      [ Sita's laptop ]              [ Hari's laptop ]
       full copy                      full copy
```

### Four verbs
| Command | What travels | When |
|---|---|---|
| `git clone <url>` | the **whole** repository, once | at the start |
| `git push origin main` | your **new commits** → the remote | after you commit |
| `git pull` | the remote's new commits → you (fetch + merge) | before you start work, and when push is rejected |
| `git fetch` | download new commits but **don't merge** yet | when you want to look first |

Nothing moves until you say so. `git commit` never touches the network — it only writes to *your* copy. That is why Git works perfectly offline, and why a power or internet cut can never damage a commit you already made.

### Remote-tracking branches
After a fetch or pull, your repository remembers where the remote's branches were, as **`origin/main`**. `git status` compares: `Your branch is ahead of 'origin/main' by 1 commit` means you have something to push; `behind` means you should pull.

### "Rejected — fetch first"
Sita pushes. Then Hari, who has *not* got Sita's commit, tries to push. The server refuses, because accepting Hari's history would throw Sita's commit away:

```
 ! [rejected]        main -> main (fetch first)
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. ... use 'git pull' before pushing again.
```

The fix is always the same: **pull** (which merges Sita's work into Hari's), resolve any conflict, then **push** again. Never "force" a push to make the error go away — that is how teams lose work.

### Hosts are interchangeable
Git is the tool; **GitHub, GitLab, Codeberg and Forgejo are places that host Git repositories** and add web pages, issues and pull requests. Everything in this lesson works the same on all of them, on a school LAN server, or with a USB stick:

| Tier | Remote | URL looks like |
|---|---|---|
| 1 — offline | a **bundle** file passed on USB | `share.bundle` |
| 2 — school LAN | Forgejo on a Raspberry Pi or old PC | `http://192.168.1.10:3000/class9/ward-facts.git` |
| 3 — internet | a teacher-managed class organisation | `https://github.com/our-class/ward-facts.git` |

## See it
Two people, one server (real output; paths shortened):

```console
sita$ git clone http://school-server/class9/ward-facts.git
Cloning into 'ward-facts'...
sita$ cd ward-facts
sita$ git remote -v
origin  http://school-server/class9/ward-facts.git (fetch)
origin  http://school-server/class9/ward-facts.git (push)
sita$ git commit -qm "Add notes file"     (after adding notes.md)
sita$ git push origin main
To http://school-server/class9/ward-facts.git
   97832b0..129d106  main -> main

hari$ git commit -qm "Add data file"      (Hari has not pulled Sita's commit)
hari$ git push origin main
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'http://school-server/class9/ward-facts.git'
hari$ git pull
Merge made by the 'ort' strategy.
 notes.md | 1 +
hari$ git push origin main
   129d106..dc34351  main -> main
```

Offline with a USB stick (Tier 1):

```console
sita$ git bundle create /e/share.bundle --all     <- E: is the USB stick
hari$ git pull /e/share.bundle main               <- on the other computer
```

## Concept drawing (10 min, unplugged)
Draw two laptops and a server on the board, each with a full row of commit cards. Act it out with three students holding card rows: **clone** (copy the whole row), **push** (add your new card to the server's row — only if the server has nothing you don't have!), **pull** (copy the server's new cards to you). Then act out the rejected push and its fix.

## PRIMM lab (50 min)
**Tier 2 (Forgejo LAN) or Tier 3 (class organisation, students 13+):**

1. The teacher gives each pair a remote URL and pseudonymous logins. Partner A: `git clone <url> ward-facts`.
2. **Predict**, then run `git remote -v`.
3. Commit locally, `git push origin main`. Check the server's web page: is your commit there?
4. Partner B clones (or pulls). Partner A commits and pushes again. Partner B: **predict** what `git pull` changes, then run it. **Investigate** `git log --oneline --graph`.
5. **Modify:** both edit *different* files and commit. Both push — the second push is **rejected**. Read the message aloud. Pull, then push.
6. **Modify:** now both edit the *same line*. Push, get rejected, pull → conflict → resolve (Module 4) → push.

**Tier 1 (no network):**

- Partner A: `git bundle create share.bundle --all`, copy to USB.
- Partner B: `git clone share.bundle ward-facts` the first time, then later `git pull share.bundle main`.
- Swap directions with a new bundle. (Bundles are exactly how this book's practice repos travel to offline schools.)

7. **Make:** write a 3-step teamwork routine on a poster: **pull · work (add, commit) · push**. Add "pull again if push is rejected".

## Parsons practice (10 min)
Order: *pull · edit · add · commit · push*. Second set: *push · rejected · pull · resolve conflict · add · commit · push*.

## Common mistakes
| Symptom | Cause | Fix |
|---|---|---|
| `! [rejected] … (fetch first)` | the remote has commits you don't have | `git pull`, then push |
| `fatal: Need to specify how to reconcile divergent branches` | new Git asks how `pull` should combine | once: `git config --global pull.rebase false` (merge), then pull again |
| `Authentication failed` | wrong login / token | check the class login; on GitHub passwords don't work for push — the teacher sets up a token or uses the LAN server |
| `fatal: repository not found` | URL typo or no access | copy the URL from the web page again |
| Pushed to the wrong branch | typed a different name | ask the teacher; don't force-push |
| Someone suggests `git push --force` | it overwrites others' work | **never** in a shared branch |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Learn Git Branching, **Remote** tab: [`remote1` Clone Intro](https://learngitbranching.js.org/?locale=en_US&level=remote1) to `remote6` Git Pushin'. Watch `o/main` (origin/main) move. | 1 / 3 | 40 min | levels done + one drawing |
| 2 | Software Carpentry [**Remotes in GitHub**](https://swcarpentry.github.io/git-novice/07-github.html) and [**Collaborating**](https://swcarpentry.github.io/git-novice/08-collab.html) — read; do the steps on the class server instead of GitHub. | 2 / 3 | 45 min | your log |
| 3 | *Pro Git* [§2.5 **Working with Remotes**](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes): try `git remote show origin`. What does it tell you? | 2 / 3 | 15 min | output explained |
| 4 | GitHub Skills [**Introduction to GitHub**](https://github.com/skills/introduction-to-github) (13+, with teacher's permission). | 3 | 60 min | completed course |
| 5 | Software Carpentry [**Hosting**](https://swcarpentry.github.io/git-novice/13-hosting.html): list two pros and cons of hosting at school vs on a public service. | 0 (printed) / 3 | 15 min | table |

## Exit ticket (5 min)
1. Does `git commit` send anything over the network?
2. What does `git clone` copy?
3. *Misconception:* "GitHub is Git." True or false?

## Key points
- A **remote** is another full copy of the repository; `origin` is the usual name.
- `clone` once, then **pull · work · push**.
- `commit` is local; only `push`/`pull`/`fetch` use the network.
- A rejected push means "pull first"; never force-push shared work.
- Git ≠ GitHub: hosts are interchangeable; bundles work with no network at all.

## New words
**remote**, **origin**, **clone**, **push**, **pull**, **fetch**, **`origin/main`**, **bundle**, **host** — see the [glossary](../../glossary.md).

## Extension quest
Run `git fetch` then `git log --oneline main..origin/main`. What does this list? (Commits on the remote that you have not merged yet.)

## Teacher notes
- **Timing:** P1: hook 5, understand 15, acting out 10, lab steps 1–3 (10). P2: lab steps 4–7 (35), Parsons 5, exit 5.
- **Privacy:** students under 13 must not create accounts on GitHub; use the LAN server or teacher-managed accounts. Never use real emails.
- **Before class:** create one repo per pair on the server and test a clone + push yourself. Set `git config --global pull.rebase false` on every lab PC to avoid the "divergent branches" message.
- **Auth:** use the server's HTTP with a pseudonymous account; delay SSH keys until Grade 10. GitHub requires a personal access token (not a password) for HTTPS pushes — prepare this or use the LAN server.
- **Typical error:** "rejected, non-fast-forward / fetch first" → pull first.
- **Fallback:** Tier 1 bundles for the whole lab; Tier 0: the acting-out activity with card rows.
- **Answer key:** Exit 1: No. 2: the whole repository with all history (and sets up `origin`). 3: False — GitHub is a website that hosts Git repositories. Extension: commits on the remote not yet in your branch.
