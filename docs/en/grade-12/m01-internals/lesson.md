---
id: g12-m01-internals
grade: 12
hours: 3
prerequisites: []
outcomes:
  - "Name Git's four object types"
  - "Explain how a commit points to a tree and a parent"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 1. Git from the inside

## Hook
Git feels like magic. Today we open the box: it is just files in a folder.

## Concept (unplugged or visual first)
Four objects: **blob** (file contents), **tree** (folder), **commit** (snapshot + message + parent), **tag**. Each is named by the hash of its content, so the same content is stored once. A branch is a file containing one hash.

## PRIMM lab
1. `git init demo && cd demo`, `echo hi > a.txt`, `git add a.txt`.
2. **Predict:** what is in `.git/objects` now? Look: `find .git/objects -type f`.
3. `git cat-file -t <hash>` and `git cat-file -p <hash>` on the blob.
4. Commit. Inspect the commit and the tree: `git cat-file -p HEAD`, `git cat-file -p HEAD^{tree}`.
5. **Investigate:** `cat .git/HEAD` and `cat .git/refs/heads/main`.
6. **Make:** draw the object graph for 3 commits and 2 files.

## Parsons practice
Order what `git commit` creates: *blob for each changed file · tree · commit pointing to tree and parent · move branch file*.

## Exit ticket
1. What is a blob?
2. What does a branch file contain?
3. *Misconception:* 'Git stores differences between versions.' True or false? (Conceptually it stores snapshots.)

## Teacher notes
Packfiles compress storage — mention only if asked. Tier 0: draw the object graph on paper from a printed `cat-file` listing.
