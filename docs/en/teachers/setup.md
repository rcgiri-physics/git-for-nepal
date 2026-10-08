# Setup guide

## Tier 0 — no computer
Print the unplugged pages of each lesson and the card sets from `docs/assets/cards/`. Nothing to install.

## Tier 1 — offline computers
1. Copy the **USB kit** (`offline/usb-kit/`, see its README) to each lab PC: Git for Windows (portable), VS Code (portable) and the self-hosted learnGitBranching build.
2. Open a terminal and run `git --version`.
3. Set a name and email **that is not the student's real identity**: `git config --global user.name "Student 07"` and `git config --global user.email "s07@example.invalid"`.
4. Copy a practice repo from its `.bundle` file: `git clone g08-class-magazine.bundle my-magazine`.

## Tier 2 — school LAN
Follow `offline/forgejo-lan/` in the repo. A Raspberry Pi-class machine is enough.

## Tier 3 — internet
Teacher creates a **private** class organisation. Students under 13 do not create accounts (GitHub terms). From Grade 9 learners aged 13+ may have accounts managed with the teacher.

## Power cuts
Git saves nothing until you commit. Commit often; a commit is safe on disk even if the PC then loses power.
