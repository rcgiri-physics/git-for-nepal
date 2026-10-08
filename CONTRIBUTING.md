# Contributing

Thank you! Ways to help: **new module**, **translation**, **dataset**, **correction**, **pilot feedback**, **adapting for another country**.

## Quick start (first pull request)
1. Open an issue using a template in `.github/ISSUE_TEMPLATE/`, or pick one labelled `good-first-issue`.
2. Fork the repo (or create a branch if you are a collaborator).
3. Make a small change on a branch named `type/short-description`, e.g. `fix/typo-g8-m02`.
4. Run the checks locally: `python tools/validate_frontmatter.py` and `mkdocs build --strict`.
5. Open a pull request using the template. Explain what and why.

## Rules
- Every module follows the template in `docs/en/module-template.md` and has valid front-matter (`tools/validate_frontmatter.py` enforces this).
- Never add student names, photos, or real marks anywhere.
- Never add a dataset without a documented licence that allows redistribution (`datasets/README.md`).
- Do not copy text from CC BY-NC-SA material. Link instead.
- Commands and code stay in English; explanations are translated.
- Each new module needs **two approvals**, including one teacher.

## Commit messages
Imperative, short first line (≤ 72 chars): `Add Grade 9 branch lesson`. Add a body explaining *why* when it is not obvious.

## Labels
`good-first-issue` · `student-friendly` · `needs-nepali-review` · `needs-teacher-review` · `dataset-licence-check` · `cdc-alignment`
