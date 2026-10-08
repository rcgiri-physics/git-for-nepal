# g08-class-magazine (practice repo, Grade 8)

A small article with a ready-made history of **6 commits** on invented dates. The text is synthetic (written for this project, CC BY 4.0): an invented school, no real people.

## For the teacher: build the starter repo
```bash
bash make-repo.sh my-magazine        # creates ./my-magazine with 6 commits
git -C my-magazine bundle create ../g08-class-magazine.bundle --all   # for the USB kit
```
Students then run `git clone g08-class-magazine.bundle my-magazine` (tier 1).

## Files
| File | Purpose |
|---|---|
| `make-repo.sh` | builds the 6-commit starter repo |
| `versions/v1..v6.md` | the article at each commit |
| `log-sample.txt` | printed history for tier-0 classes (Modules 4 and 6) |
| `check.sh` | smoke test used by CI |
