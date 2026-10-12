---
id: g10-m07-static-site
grade: 10
hours: 2
prerequisites: [g10-m06-releases]
outcomes:
  - "Explain what a static site is"
  - "Change a static site through a pull request"
  - "Publish a site from a repository (Pages host or LAN)"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 7. Publishing a static website from the repo

!!! abstract "At a glance"
    **Time:** 2 periods · **Tiers:** 1 (open in browser), 2 (serve on LAN), 3 (Pages host) · **You need:** `practice-repos/g10-school-website`, a browser, your team repo

    **Before this:** Modules 3–6.

    **By the end you can:** edit HTML/CSS in a repo, preview it, review it through a PR, and publish it — for free — from the repository.

## Hook (5 min)
Can the school have a web page without buying a server or paying a company every month? Yes — if the site is **static**, the repository itself can be the website.

## Understand it

### Static vs dynamic sites
| | Static site | Dynamic site |
|---|---|---|
| Made of | files: `index.html`, `style.css`, images | a program + a database (e.g. PHP/Python + MySQL) |
| The server | just sends the files | runs code for every visitor |
| Examples | school notice pages, documentation, portfolios, **this book's website** | online shops, exam-result search, social media |
| Cost & safety | free hosting, very little can break or be hacked | needs a real server and maintenance |

For a school's information site, static is usually enough — and every page lives in Git, with full history and review.

### Repository → website
```
 your repo (main branch)            Pages host                    visitors
 index.html, style.css ...  --->  copies the files  --->  https://our-school.codeberg.page/
       ^                          after each push
       |  PRs with review
```

Free "Pages" services publish a branch as a website: **GitHub Pages**, **Codeberg Pages**, **GitLab Pages**. Forgejo can do the same with Actions. With no internet, any computer on the school LAN can serve the folder:

```bash
python -m http.server 8000      # then other PCs open http://<this-PC's-IP>:8000
```

Every change goes through a branch and a PR, so the live site only changes after review — and if something breaks, `git revert` brings the old page back.

### Site generators (a glimpse)
Writing every page in HTML gets repetitive. **Static site generators** turn Markdown into HTML pages with a shared menu and style. This book uses **MkDocs**: each lesson is a `.md` file in Git; one command (`mkdocs build`) makes the website, and the GitHub workflow `.github/workflows/pages.yml` publishes it automatically on every push to `main`. Others: Jekyll, Hugo, Eleventy.

### Credit and privacy on the public web
- Credit every image and text you did not create: *"Photo: Name, CC BY 4.0"*. Use only what you are allowed to.
- **Never publish students' names, photos, marks or phone numbers.** A public site is public for ever (and copied by search engines).
- Contact details: the school office only.

## See it
```console
$ cd school-website
$ bash check.sh
g10 ok
$ git switch -c feature/about-page
  (create about.html, add <a href="about.html">About</a> to the menu)
$ bash check.sh
g10 ok
$ git add about.html index.html festival.html
$ git commit -m "Add About page and link it from every menu (closes #2)"
$ git push -u origin feature/about-page
  (open PR -> review -> merge -> the Pages host republishes main)
```

## Unplugged (10 min)
Draw the journey of a page change on the board: *edit → commit → push → PR → review → merge → Pages publishes → visitor sees it*. Students act as each step holding a printed page; ask "where could a mistake be caught?" (review, check script, preview).

## PRIMM lab (60 min)
Practice repo: `practice-repos/g10-school-website` (copy it into your team repo if you don't have one).

1. Open `index.html` in a browser (Tier 1 works offline).
2. **Predict**, then change the headline and the colour in `style.css`; refresh. Run `git diff` — which file did the colour change touch?
3. On a branch, add an `about.html`; link it from the menu of **every** page; run `bash check.sh`; open a PR; get it reviewed and merged.
4. **Publish:**
    - **Tier 3:** enable Pages for `main` (GitHub: *Settings → Pages → Deploy from a branch → main / root*; Codeberg: push to a repository named `pages`, or a `pages` branch — follow Codeberg's docs).
    - **Tier 2:** on the server PC, `python -m http.server 8000` in the site folder; classmates open `http://<IP>:8000`.
    - **Tier 1:** open the files directly in the browser.
5. **Investigate:** make a small change, merge it, and time how long until the live site updates.
6. **Make:** add one page that shows a small open-data table (for example 5 rows from a census or open-data table from your country you are allowed to use) and **credit the source** at the bottom.

## Parsons practice (5 min)
Order: *edit HTML · open in browser · commit · push · publish*.

## Common mistakes
| Symptom | Cause | Fix |
|---|---|---|
| Page works on my PC, broken online | links with `C:\Users\…` paths or wrong case (`About.html` vs `about.html`) | relative links, lower-case names; `check.sh` |
| Changes not visible online | Pages not enabled, wrong branch, or browser cache | check settings; wait a minute; Ctrl+F5 |
| Images missing | image not committed, or in `.gitignore` | `git status`; add the image |
| Site shows the README instead | no `index.html` in the published folder | add `index.html` at the root |
| Personal photo or phone number published | — | remove, commit, and ask the teacher about removing it from history (Grade 12 M5) |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | GitHub Skills [**GitHub Pages**](https://github.com/skills/github-pages) (13+, account). | 3 | 45 min | your published page URL |
| 2 | [Codeberg docs](https://docs.codeberg.org/) — find the *Codeberg Pages* section and list its steps. | 3 | 15 min | steps |
| 3 | [Markdown Guide](https://www.markdownguide.org/): rewrite your About page in Markdown (as this book's lessons are). | 1 / 3 | 20 min | `about.md` |
| 4 | Look at this book's `mkdocs.yml` and one lesson `.md` file. How does MkDocs know the page title? | 1 | 10 min | answer |
| 5 | The Odin Project, [**Git Basics**](https://www.theodinproject.com/lessons/foundations-git-basics) — its project of putting a page on GitHub. | 3 | 60 min | URL |

## Exit ticket (5 min)
1. What makes a site "static"?
2. Where would you publish with no internet?
3. *Misconception:* "A website needs a database." True or false?

## Key points
- A **static site** is only files; a host sends them as they are.
- **Pages** services publish a branch for free; a LAN PC can serve it with `python -m http.server`.
- Every change goes branch → PR → review → merge → publish; revert fixes a broken live page.
- Credit sources; never publish private data.

## New words
**static site**, **dynamic site**, **Pages**, **site generator**, **relative link** — see the [glossary](../../glossary.md).

## Extension quest
Add a `404.html` page ("page not found") and a simple CSS rule that makes the menu readable on phones (`@media (max-width: 600px) { … }`).

## Teacher notes
- **Timing:** P1: hook 5, understand 15, unplugged 10, lab 1–2 (10). P2: lab 3–6 (35), Parsons 5, exit 5.
- **Credit images and text (CC BY). Never publish student names or photos.** Use the check script `check.sh` to validate that every internal link exists.
- Pages settings change over time — check the host's current docs before class.
- If the school has no internet, the LAN server is the "live" site for the exhibition.
- **Answer key:** Exit 1: it is only files sent unchanged; no program runs per visitor. 2: on the school LAN (`python -m http.server`, or the Forgejo server). 3: False — static sites need none. Exercise 4: from the first `#` heading in the file (or the `title` in front-matter/nav).
