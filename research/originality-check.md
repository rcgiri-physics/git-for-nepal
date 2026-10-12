# Originality check — 2026-10-12

## Method
- **Automated overlap scan** of all 160 Markdown files (~92,000 words in `docs/` and `book/`; code blocks and inline code excluded) against:
  - *Pro Git* 2nd ed. (`progit/progit2`, CC BY-NC-SA 3.0)
  - Official Git documentation (`git/git` → `Documentation/`)
  - GitHub Docs (`github/docs` → get-started, repositories, pull-requests)
- Flagged any run of **7+ identical consecutive words**. Detector verified by planting a known Pro Git sentence (caught).
- **Web spot-check** of distinctive definition sentences (Grades 8, 9, 11) for exact-phrase matches on Atlassian, freeCodeCamp and other tutorial sites.

## Result
- **10+ word runs:** none.
- **7-word runs:** 5, all generic phrasing or GitHub UI setting names — no rewrite needed:
  - "require branches to be up to date" / "require status checks to pass before merging" (G12 m02, m03) — names of GitHub branch-protection settings; quoting them is correct.
  - "when you want to contribute to a project where" (G10 m02), "on the command line instead of the" (G10 m03) — common phrases.
- **Web spot-check:** no exact-phrase matches found.
- **Assets:** no third-party images, fonts or datasets; practice-repo data is synthetic and project-authored (see `datasets/README.md`).

## Limits
Automated comparison covered only openly downloadable sources. Paid courses, books other than *Pro Git*, and paraphrase (same ideas, different words) are not detected by word-run matching; ideas and standard explanations are not copyrightable, but sources the lessons follow should still be credited in `research/sources.md`.
