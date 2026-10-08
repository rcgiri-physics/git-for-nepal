# USB kit recipe (tier 1)

Binaries are **not** stored in this repo. Download them once on a connected PC and copy to the USB stick.

| Item | Where from | Note |
|---|---|---|
| Git for Windows (portable) | git-scm.com → "Portable" | check current version; verify the checksum shown on the site |
| VS Code (portable/zip) | code.visualstudio.com | optional; GitHub Desktop is an alternative |
| learnGitBranching build | `bash build-learngitbranching.sh out-dir` (this folder) | **Tested 2026-10-07** (Node 24, commit 287153f, 8.7 MB, loads with no console errors). The script removes the Google Analytics snippet and keeps the MIT licence file as `LICENSE-learnGitBranching.md`. Serve with `python -m http.server -d out-dir 8080` or open `index.html` |
| Practice-repo bundles | `bash make-bundles.sh bundles` (this folder) | **Tested 2026-10-07:** produces one `.bundle` per practice repo (Grade 8 with its 6-commit history); `git clone x.bundle` works |
| Printable cards and handouts | build from `docs/` | `mkdocs build` and print |

## Folder layout on the stick
```
USB/
  git-portable/
  vscode-portable/        (optional)
  learnGitBranching/build/
  bundles/g08-class-magazine.bundle
  print/
```
## Checklist before class
- [ ] `git --version` works on a lab PC
- [ ] a bundle clones: `git clone bundles/g08-class-magazine.bundle test`
- [ ] the visualiser opens without internet
