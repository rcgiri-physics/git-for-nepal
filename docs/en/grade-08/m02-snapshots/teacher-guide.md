# Teacher guide — Module 2 (2 periods)

**Goal:** a firm mental model — *commit = whole snapshot + message + parent*. Everything later in the book builds on this picture.

**Timing:** Period 1: hook 5, "Understand it" (teacher explains with the board drawing) 10, paper commits 25. Period 2: swap activity 10, predict 10, Parsons 10, free-resource exercise 1 or 3 (5–10), exit 5.
**Materials:** 8 index cards per pair, string or lines drawn with pen, pens. Optional: one computer + projector for Learn Git Branching.

## Board drawing (copy this exactly)
```
  c1  <---  c2  <---  c3  <---  c4
```
Point at the arrows: "each commit remembers the one before it." Write a message under each card.

## Common errors
- **"A commit is a copy of only the changed line."** Correct it: in the game each card holds the *whole* sheet. Git stores a snapshot of the project and cleverly shares unchanged parts.
- **Vague messages** ("done", "ok"). Use the swap activity to show why they hurt: the other pair cannot answer the questions.
- **Forgetting the parent.** Insist on the string or arrow.
- **Rubbing out a card.** Say: "a khata never tears out a page." Make a new card.

## Fallbacks
Fully unplugged. With no cards, use half sheets of paper. With one computer, run free-resource exercise 1 on the projector and let pairs call out the commands.

## Differentiation
- **Support:** give sentence starters for messages: *Add…*, *Fix…*, *Remove…*, *Change … to …*.
- **Stretch:** "If a commit stores the whole project, why doesn't the disk fill up?" (Unchanged files are shared, not copied — Grade 12 internals.)

## Evidence to collect
The card rows: check that each card has a message starting with a verb, a parent, and the whole text.

## Message makeover set (free-resource exercise 3)
Give these ten weak messages with a short description of the change; students rewrite them:
`update` (added a date to the notice) · `asdf` (new paragraph about the library) · `final` (closing sentence) · `fix` (spelling of *Janakpur*) · `changes` (moved the title to the top) · `ok now` (removed a repeated line) · `done!!` (added the author's role) · `new` (added a second verse) · `edit 3` (changed "big" to "huge") · `misc` (fixed two typos in paragraph 2).

Sample answers: `Add date to the notice`, `Add paragraph about the library`, `Add closing sentence`, `Fix spelling of Janakpur`, `Move title to the top`, `Remove repeated line`, `Add author's role`, `Add second verse`, `Change "big" to "huge" in line 3`, `Fix two typos in paragraph 2`.

## Answer key
- **Parsons:** Write title → Add first verse → Fix spelling → Add second verse (any order consistent with the card messages is fine if the student justifies it). Arrows point from each card back to the one before.
- **Exit 1:** a saved snapshot of the whole project with a message (and author, date, parent). **2:** e.g. `Add heading to the essay`. **3:** False.
- **Free-resource 1–2:** circles = commits; the newest is the one the `main*` label points at; arrows point to the parent because a commit records where it came from.
- **Free-resource 4:** Git stores snapshots of the whole project, not lists of differences.

## Extension quest
Make the cards for a *wrong* edit and add a new commit that fixes it, instead of rubbing out an old card. (History is never rewritten here — prepares Module 5.)
