# Nepali text status

Decision D4 (confirmed 2026-10-08): all grades in English and Nepali.

- `docs/ne/` holds Nepali drafts: **Grades 8–12 (all modules; Grade 8 as lesson summaries, Grades 9–12 as short summaries with the key commands and exit tickets)**, plus the CDC brief. Full-length Nepali lessons, worksheets and teacher guides are not written.
- They are machine-drafted and **have not been reviewed by a native speaker**; they must be reviewed before use (`needs-nepali-review`).
- The site builds both languages (`mkdocs-static-i18n`, folder structure; the language switcher is in the header). Devanagari rendering was checked on a Windows PC with system fonts in October 2026; **check it on the actual lab PCs** (the CSS lists Noto Sans Devanagari, Nirmala UI and Mangal; no web fonts are loaded so the site works offline). Material has no Nepali UI strings, so menus show English (`overrides/partials/languages/ne.html`).
- Keep command names and code in English; translate the explanation.
- Glossary Nepali terms are in [the glossary](../glossary.md).
