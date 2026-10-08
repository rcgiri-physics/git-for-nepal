---
id: g8-m02-snapshots
grade: 8
hours: 2
prerequisites: [g8-m01-final-final]
outcomes:
  - "Explain a commit as a snapshot with a message"
  - "Draw a history of commits in order"
  - "Write a message that says what and why"
tier_support: [0, 1, 2, 3]
license: CC-BY-4.0
---

# 2. Snapshots = commits

## Hook (5 min)
A photographer takes a photo after every step of building a wall. Nothing is lost: you can look at any photo. A **commit** is a photo of your whole project plus a note.

## Unplugged: the paper-commit game (25 min)
**Materials:** index cards, string, pens.

1. Each pair writes a 4-line poem about their village or school on a sheet (the *working copy*).
2. To make a **commit**: copy the whole sheet onto an index card. At the top write a short message (*what + why*), e.g. "Add first two lines". Number it `c1`.
3. Edit the sheet (add a line). Make card `c2` with its message. On `c2` write "parent: c1" and connect the cards with string.
4. After four commits, lay the cards in a row. This row is the **history** (`git log`).
5. **Swap** with another pair. Answer from their cards only: *what changed between c2 and c3? why?*

### Rules of a good message
- Starts with a verb: "Add", "Fix", "Remove".
- Says *what and why* in one line.
- One idea per commit.

## Predict (PRIMM) (10 min)
Show 3 cards with messages "stuff", "fix", "final". Predict: can you tell what changed? Now show "Add title", "Fix spelling of Bhaktapur", "Add third verse". Compare.

## Parsons practice (10 min)
Put these in order to make a history: *Write title · Add first verse · Fix spelling · Add second verse*, using the messages on the cards as clues.

## Exit ticket (5 min)
1. What is a commit?
2. Write a good message for adding a heading to an essay.
3. *Misconception check:* "Git automatically saves every keystroke." True or false? (False — only when you commit.)
