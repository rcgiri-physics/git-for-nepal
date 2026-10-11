---
id: g12-m01-internals
grade: 12
hours: 3
prerequisites: []
outcomes:
  - "Name Git's four object types"
  - "Explain how a commit points to a tree and a parent"
  - "Explain why identical content is stored once and why history cannot be changed silently"
tier_support: [0, 1, 2, 3]
license: CC-BY-4.0
---

# 1. Git from the inside

!!! abstract "At a glance"
    **Time:** 3 periods · **Tiers:** 0 (paper object graph from printed output), 1–3 · **You need:** a terminal, an empty practice folder

    **Before this:** Grades 8–11 (you have used every command; now you see how they work).

    **By the end you can:** inspect Git's objects with plumbing commands, draw the object graph of a small repository, and explain branches, HEAD and tags as references.

## Hook (5 min)
Git feels like magic: it brings back last year's file in a second, knows exactly what changed, and two computers can compare histories without sending everything. Today we open the box. Inside there is no magic — just small files in a folder, named by fingerprints.

## Understand it

### Content-addressed storage
Git stores everything as **objects** in `.git/objects/`. Each object is named by a **hash** — a 40-character fingerprint (SHA-1; newer Git can use SHA-256) calculated from the object's **content**:

```
 "hi\n"  --SHA-1-->  45b983be36b73c0788dc9cbcb76cbb80fc7bb057
```

Three consequences explain much of Git's behaviour:

1. **Same content → same name → stored once.** Ten identical files cost the space of one.
2. **Different content → different name.** Change one letter and the hash changes completely.
3. **Integrity.** If anyone changes an old object, its hash no longer matches its name. And because each commit includes its parent's hash, changing *any* old commit changes every commit after it. History cannot be altered silently — this is why rebase creates *new* commit ids (Grade 11).

### The four object types
| Object | Stores | Like |
|---|---|---|
| **blob** | the contents of one file (no name, no date) | the text on a page |
| **tree** | a folder: list of names → blobs and sub-trees, with file modes | a table of contents |
| **commit** | one tree (the snapshot) + parent commit(s) + author, committer, dates + message | a dated, signed photo with a caption |
| **tag** (annotated) | a pointer to a commit + tagger, date, message | a label with a note |

```
 commit e303976 ----------> tree 0d8a474 ----> blob 45b983b  ("hi\n")   named a.txt
   parent: (none)
   "Add a.txt"

 commit 7c1f... ----------> tree bee4886 --+--> blob 45b983b   named a.txt
   parent: e303976                          +--> blob 45b983b   named b.txt  <- stored once!
   "Add b.txt with same content"
```

So Grade 8's model was exactly right: **a commit is a whole snapshot** (a tree), and unchanged files are *shared* (the same blob), not copied.

### References: branches, HEAD, tags
Objects never change. The things that *move* are **references** — small text files holding a hash:

- a **branch** = `.git/refs/heads/main`, containing one commit hash;
- **HEAD** = `.git/HEAD`, usually `ref: refs/heads/main` (a pointer to a branch); if it holds a commit hash directly, you are in **detached HEAD**;
- a **tag** = `.git/refs/tags/v1.0`;
- **remote-tracking** branches = `.git/refs/remotes/origin/main`.

Committing = write new blobs/trees + a commit object, then update the branch file to the new hash. That is all.

### Porcelain and plumbing
Commands you have used (`add`, `commit`, `log`) are **porcelain** — the friendly surface. Underneath are **plumbing** commands that read and write objects directly:

| Plumbing | Does |
|---|---|
| `git hash-object <file>` | compute a file's blob hash |
| `git cat-file -t <hash>` | object type |
| `git cat-file -p <hash>` | pretty-print an object |
| `git ls-tree HEAD` | list a tree |
| `git rev-parse HEAD` | resolve a name to a hash |
| `git count-objects -v` | how many objects are stored |

### Packfiles
Loose objects are compressed (zlib). Later, Git packs many objects into **packfiles** and stores similar versions as **deltas** to save space (`git gc`). This is a storage optimisation; the *model* is still snapshots.

## See it
Real output (the blob and tree hashes will be identical on your computer — they depend only on content):

```console
$ git init -q demo && cd demo
$ echo hi > a.txt
$ git add a.txt
$ find .git/objects -type f
.git/objects/45/b983be36b73c0788dc9cbcb76cbb80fc7bb057    <- the blob, created by "add"!
$ git cat-file -t 45b983b
blob
$ git cat-file -p 45b983b
hi
$ git commit -qm "Add a.txt"
$ git cat-file -p HEAD
tree 0d8a474fc67971fb3dd7616e26323d3066442555
author Student 07 <s07@example.invalid> 1791692100 +0545
committer Student 07 <s07@example.invalid> 1791692100 +0545

Add a.txt
$ git cat-file -p HEAD^{tree}
100644 blob 45b983be36b73c0788dc9cbcb76cbb80fc7bb057    a.txt
$ cat .git/HEAD
ref: refs/heads/main
$ cat .git/refs/heads/main
e303976a5221b14438483e6b15d11056b060a188
$ echo hi > b.txt && git add b.txt && git commit -qm "Add b.txt with same content"
$ git cat-file -p HEAD^{tree}
100644 blob 45b983be36b73c0788dc9cbcb76cbb80fc7bb057    a.txt
100644 blob 45b983be36b73c0788dc9cbcb76cbb80fc7bb057    b.txt     <- same blob
```

The number `1791692100` is the time in seconds since 1 January 1970 (Unix time); `+0545` is Nepal's time zone.

## Unplugged: build the object graph (20 min)
Give pairs a printed version of the *See it* output. Using three colours of cards (blob, tree, commit) and arrows, build the object graph. Then add a third commit on paper that changes `a.txt` to "hello": which cards are new? Which are reused? (New blob, new tree, new commit; `b.txt`'s blob is reused.) Finally, place sticky notes for `main` and `HEAD`.

## PRIMM lab (80 min)
1. `git init demo && cd demo`, `echo hi > a.txt`, `git add a.txt`.
2. **Predict:** what is in `.git/objects` now? Look: `find .git/objects -type f`. (Surprise: `add` already wrote the blob.)
3. `git cat-file -t <hash>` and `git cat-file -p <hash>` on the blob. Compare with `git hash-object a.txt`.
4. Commit. Inspect the commit and the tree: `git cat-file -p HEAD`, `git cat-file -p HEAD^{tree}`.
5. **Investigate:** `cat .git/HEAD` and `cat .git/refs/heads/main`. Create a branch and look in `.git/refs/heads/` again. Create an annotated tag and inspect it with `git cat-file -p v0.1`.
6. **Investigate:** add `b.txt` with the same content and commit. How many *new* objects appeared (`git count-objects -v`)? Why?
7. **Investigate:** `git switch --detach HEAD~1` and `cat .git/HEAD`. What changed? Return with `git switch main`.
8. **Make:** draw the object graph for 3 commits and 2 files (one changed, one not), with refs.

## Parsons practice (10 min)
Order what `git commit` creates: *blob for each changed file · tree · commit pointing to tree and parent · move branch file*.

## Common mistakes
| Misunderstanding | Correction |
|---|---|
| "Git stores differences" | the model stores snapshots; deltas are only a packing optimisation |
| "A branch contains its commits" | a branch is a file with one hash; commits are reached by following parents |
| "Deleting a branch deletes the commits" | commits remain until unreachable *and* garbage-collected (reflog helps) |
| Editing files in `.git` by hand | never in real repos; only read them |
| "The blob knows its file name" | names live in trees |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | *Pro Git* [§10.2 **Git Objects**](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects) — build a commit **only with plumbing** (`hash-object -w`, `update-index`, `write-tree`, `commit-tree`). | 1 / 3 | 45 min | your commit's `cat-file -p` |
| 2 | *Pro Git* [§10.3 **Git References**](https://git-scm.com/book/en/v2/Git-Internals-Git-References): create a branch with `git update-ref`. | 1 / 3 | 15 min | command + result |
| 3 | [*Git from the Bottom Up*](https://jwiegley.github.io/git-from-the-bottom-up/) (CC BY): read "Repository: Directory content tracking" and "Introducing the blob". | 3 | 30 min | summary |
| 4 | MIT Missing Semester, [**Version Control (Git)**](https://missing.csail.mit.edu/2020/version-control/) — watch/read "Data model"; write its pseudocode for a commit in your notebook. | 3 | 40 min | pseudocode |
| 5 | *Pro Git* [§10.1 **Plumbing and Porcelain**](https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain) and [§10.4 **Packfiles**](https://git-scm.com/book/en/v2/Git-Internals-Packfiles): run `git gc` on a repo and look in `.git/objects/pack`. | 1 / 3 | 20 min | what you found |

## Exit ticket (5 min)
1. What is a blob?
2. What does a branch file contain?
3. *Misconception:* "Git stores differences between versions." True or false? (Conceptually it stores snapshots.)

## Key points
- Objects are named by the **hash of their content**: identical content stored once; any change is detectable.
- **blob** (contents) · **tree** (folder) · **commit** (tree + parents + metadata + message) · **tag**.
- **References** (branches, HEAD, tags, remote branches) are small files holding hashes; only they move.
- Porcelain commands are built on plumbing commands you can run yourself.

## New words
**object**, **hash / SHA-1**, **blob**, **tree**, **content-addressed**, **reference (ref)**, **plumbing / porcelain**, **packfile**, **detached HEAD** — see the [glossary](../../glossary.md).

## Extension quest
Explain, using objects, why `git clone` of a repo with 10 years of history can still be fast, and what `git clone --depth 1` changes.

## Teacher notes
- **Timing:** P1: hook 5, understand 25, unplugged 10. P2: see it (live) 10, lab 1–5 (30). P3: lab 6–8 (30), Parsons 5, exit 5.
- Packfiles compress storage — mention only if asked. Tier 0: draw the object graph on paper from a printed `cat-file` listing.
- On Windows, if `core.autocrlf` is on, a file created by Git Bash with LF is still stored with LF, so the `hi` blob hash matches; if students create the file in Notepad, the hash differs (CRLF) — a nice demonstration that the hash depends on every byte.
- **Answer key:** Exit 1: an object holding one file's contents (no name). 2: one commit hash (40 hex characters). 3: False. Lab 6: two new objects (the tree and the commit); the blob is reused. Lab 7: HEAD holds a commit hash instead of `ref: refs/heads/main`.
