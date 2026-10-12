---
id: g11-m01-licences
grade: 11
hours: 2
prerequisites: []
outcomes:
  - "Explain what MIT and CC BY allow and require"
  - "Write a correct attribution line"
  - "Tell whether two licences can be combined"
tier_support: [0, 1, 2, 3]
license: CC-BY-4.0
---

# 1. Open-source licences and attribution

!!! abstract "At a glance"
    **Time:** 2 periods · **Tiers:** 0–3 · **You need:** licence and permission cards (Tier 0), this repository's `LICENSE`, `LICENSE-CONTENT.md` and `ATTRIBUTION.md`

    **Before this:** Grades 8–10.

    **By the end you can:** say what common open licences allow and require, credit others' work correctly, choose a licence for your own project, and spot licences that cannot be mixed.

!!! note "Not legal advice"
    This lesson gives general information so you can read licences sensibly. For a real legal question, ask a qualified person.

## Hook (5 min)
You find a great photo of Rara Lake, a poem about Dashain and a Python program that draws charts — all online. Can you use them in your school project? Can you put them on the school website? Can the school *sell* a printed booklet that contains them?

## Understand it

### Copyright is the default
When someone creates a photo, text or program, they automatically own the **copyright**. Nobody else may copy, change or share it **unless the owner gives permission**. A **licence** is that permission, written down. So:

> **No licence = no permission.** "It's on the internet" does not make it free.

### Open licences
An **open licence** gives everyone permission in advance, under some conditions. There are two families:

- **Open-source software licences** — for code: **MIT**, **Apache-2.0**, **GPL-3.0**, BSD, …
- **Creative Commons (CC) licences** — for writing, images, data, lessons: **CC BY**, **CC BY-SA**, **CC BY-NC**, **CC0** …

### What each one says
| Licence | Copy & share | Change | Use commercially | Conditions |
|---|---|---|---|---|
| **CC0** / public domain | ✓ | ✓ | ✓ | none (credit is polite) |
| **MIT** (code) | ✓ | ✓ | ✓ | keep the copyright and licence notice |
| **Apache-2.0** (code) | ✓ | ✓ | ✓ | keep notices, state changes; includes a patent grant |
| **CC BY 4.0** | ✓ | ✓ | ✓ | **credit** the author, link the licence, say if you changed it |
| **CC BY-SA 4.0** | ✓ | ✓ | ✓ | credit **and share alike**: your changed version must use the same licence |
| **GPL-3.0** (code) | ✓ | ✓ | ✓ | share alike for code: if you distribute a changed program, share its source under GPL |
| **CC BY-NC** | ✓ | ✓ | **✗** | credit; **non-commercial only** |
| **CC BY-ND** | ✓ | **✗** | ✓ | credit; **no derivatives** (no changes) |
| "All rights reserved" | ✗ | ✗ | ✗ | ask the owner |

The letters combine: **BY** = attribution, **SA** = share alike, **NC** = non-commercial, **ND** = no derivatives.

### This book's choice
This book is **CC BY 4.0** for content and **MIT** for code (see `LICENSE-CONTENT.md` and `LICENSE`). Why? CC BY lets the CDC, any school or any publisher print and adapt it — even sell printed copies to cover costs — as long as they credit the authors. That is exactly what a national curriculum resource needs.

### Writing an attribution: TASL
A good credit line has **T**itle, **A**uthor, **S**ource (link), **L**icence — and says if you changed it:

> *"Rara Lake at dawn"* by Sita Sharma, from Wikimedia Commons (link), licensed CC BY 4.0. Cropped.

For this book, `ATTRIBUTION.md` gives a ready sentence to copy.

### Mixing licences
When you combine works, every licence's conditions apply at once. Some combinations are **impossible**:

- CC BY-**NC** text cannot go into this CC BY book — CC BY allows commercial use, NC forbids it.
- CC BY-**SA** text cannot go in either — SA would force the whole book to become CC BY-SA.
- MIT code can go into a GPL program (GPL's conditions then apply to the whole), but GPL code cannot go into an MIT project.

That is why this book only **links** to excellent resources like *Pro Git* (CC BY-NC-SA) instead of copying them — see the [resource library](../../book/resources.md).

### Licences in a repository
Put the licence text in a file called **`LICENSE`** at the top of the repo. Hosts detect it and show it on the project page. For files with different licences, projects add notes, or use the **REUSE** standard with **SPDX identifiers** — short official names like `MIT`, `CC-BY-4.0` (this book's lessons say `license: CC-BY-4.0` in their front-matter).

## See it
```console
$ head -3 LICENSE
MIT License

Copyright (c) 2026 The git-for-schools contributors
$ grep -m1 "Attribution 4.0" LICENSE-CONTENT.md
**Creative Commons Attribution 4.0 International (CC BY 4.0)**.
$ grep license: docs/en/grade-11/m01-licences/lesson.md
license: CC-BY-4.0
```

## Unplugged: licence card sort (20 min)
Pairs get **licence cards** (`CC0`, `MIT`, `CC BY 4.0`, `CC BY-SA 4.0`, `CC BY-NC-SA`, `GPL-3.0`, "all rights reserved") and **permission cards** (copy, change, sell, must credit, must share alike, must keep notice). Place permission cards under each licence. Then three **scenarios**: (1) put a CC BY photo on the school website, (2) print a CC BY-NC poem in a booklet sold at the school fair, (3) use an MIT chart library in your Grade 12 project. For each: allowed? what must you do?

## PRIMM lab (40 min)
1. Read this repo's `LICENSE-CONTENT.md` and `ATTRIBUTION.md`. **Predict** what you must write if you reuse Grade 8 Module 1 in your own worksheet. Write it.
2. Write attribution lines (TASL) for three given items: a photo under CC BY, a MIT library, a poem under CC BY-SA — what changes for SA?
3. **Investigate:** why can't a CC BY-NC-SA text be copied into this repo? (Conflicting terms.) Find two resources in the [library](../../book/resources.md) marked "link only" and say why.
4. **Investigate:** on [choosealicense.com](https://choosealicense.com/), compare MIT, Apache-2.0 and GPL-3.0. What is the main difference?
5. **Make:** choose a licence for your own Grade 11 project (code: MIT or GPL; data/writing: CC BY or CC BY-SA). Add the `LICENSE` file, commit with a message explaining the choice.

## Parsons practice (10 min)
Match each licence to what it requires (credit / share alike / no commercial use / keep notice / nothing).

## Common mistakes
| Mistake | Fix |
|---|---|
| "No licence shown, so it's free" | no licence = all rights reserved; ask or find another source |
| Credit without a link or licence name | use TASL |
| Copying NC or SA text into a CC BY project | link to it instead |
| Changing the licence of someone else's work | you can't; only the owner can |
| Inventing a licence ("free for students") | use a standard licence so everyone understands it |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Software Carpentry [**Licensing**](https://swcarpentry.github.io/git-novice/11-licensing.html) — do its exercise "Can I Use Open License?". | 1 / 3 | 20 min | answer |
| 2 | [choosealicense.com](https://choosealicense.com/): choose a licence for three imaginary projects (a game, a dataset, a school notes site). | 3 | 15 min | 3 choices + reasons |
| 3 | Read the human summary of [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Explain "no additional restrictions" in your own words. | 3 | 10 min | 2 sentences |
| 4 | [SPDX licence list](https://spdx.org/licenses/): find the identifiers for five licences in this lesson. | 3 | 10 min | 5 ids |
| 5 | [REUSE](https://reuse.software/): read the three steps. How would they help a project with mixed licences? | 3 | 15 min | summary |

## Exit ticket (5 min)
1. What must you do when reusing CC BY work?
2. What does "share alike" require?
3. *Misconception:* "If it is on the internet, it is free to use." True or false?

## Key points
- Copyright is automatic; a **licence** gives permission. No licence = no permission.
- Code: MIT, Apache-2.0, GPL. Content: CC0, CC BY, CC BY-SA, CC BY-NC, CC BY-ND.
- Credit with **TASL**; say if you changed it.
- Some licences cannot be combined; link instead of copying.
- Put a `LICENSE` file in every repo; use SPDX identifiers.

## New words
**copyright**, **licence**, **open licence**, **attribution (TASL)**, **share alike**, **non-commercial**, **SPDX identifier**, **public domain** — see the [glossary](../../glossary.md).

## Extension quest
Look up your government's open-data portal (or, as an example, OKN's `localboundaries` repository in Nepal). What licence does it use? What would you need to write to use it in a school project?

## Teacher notes
- **Timing:** P1: hook 5, understand 20, card sort 15. P2: lab 30, Parsons 5, exit 5.
- This is general information, not legal advice; avoid giving legal opinions. Link to the official summaries at creativecommons.org and opensource.org.
- **Card-sort answers:** CC0 — copy, change, sell; MIT — copy, change, sell, keep notice; CC BY — copy, change, sell, credit; CC BY-SA — plus share alike; CC BY-NC-SA — copy, change, credit, share alike, **not** sell; GPL-3.0 — copy, change, sell, keep notice, share source alike; all rights reserved — nothing without asking.
- **Scenarios:** (1) yes, with TASL credit; (2) no — selling is commercial; (3) yes, keep the MIT notice.
- **Answer key:** Exit 1: credit (TASL), link the licence, say if changed. 2: derivatives must use the same (or compatible) licence. 3: False. Lab 4: MIT/Apache permissive (Apache adds patents); GPL requires sharing changed source under GPL.
