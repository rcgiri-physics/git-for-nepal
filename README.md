# Git for Nepal / नेपालका लागि Git

An open, offline-first curriculum for teaching **Git and version control** in Nepali schools, **Grades 8–12**.
Content is reusable with attribution; it is built only on open-source tools and open data.

Site: https://rcgiri-physics.github.io/git-for-nepal/

> **Status: v0.1 prototype.** Grade 8 is a full chapter. Grades 9–12 are written to outline-plus-core-lessons level and have **not been piloted in a classroom**. The CDC mapping is verified for Grades 10–12 and **unverified for Grades 8–9**; Python and MySQL are Grade 10 in CDC's textbook (see [`research/decisions.md`](research/decisions.md)).

| Grade | Chapter | Big idea |
|---|---|---|
| 8 | Time Machine for My Work | every file has a history |
| 9 | Branch and Share | branches work in parallel; remotes let work travel |
| 10 | Team Workflows | teams need rules so work does not collide |
| 11 | Open-Source Contributor | you can improve software others also use |
| 12 | Engineering with Git | professional teams ship safely, repeatedly |

## Who is this for?
- **Teachers** — start at [`docs/en/teachers/`](docs/en/teachers/index.md). Every module has a teacher guide with timing, misconceptions and a no-computer fallback.
- **Students** — open your grade's chapter in [`docs/en/`](docs/en/index.md).
- **Contributors** — read [`CONTRIBUTING.md`](CONTRIBUTING.md). Your first pull request can be to this repo.
- **Education officials / CDC** — see [`docs/en/cdc-brief.md`](docs/en/cdc-brief.md) and [`alignment/`](alignment/).

## Four delivery tiers
Every module says which tiers it supports: **0** no computer · **1** offline computers · **2** school LAN (Forgejo) · **3** internet. See [`offline/`](offline/README.md).

## Build the site locally
```bash
pip install -r requirements.txt
mkdocs serve
```

## Licence and credit
Content: **CC BY 4.0** ([`LICENSE-CONTENT.md`](LICENSE-CONTENT.md)). Code, scripts, templates: **MIT** ([`LICENSE`](LICENSE)).
How to credit: see [`ATTRIBUTION.md`](ATTRIBUTION.md).
