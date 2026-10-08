# Decision log

Status key: ✅ decided or verified · 🟡 provisional · ❓ open

| # | Decision | Value used in this repo | Status | Note |
|---|---|---|---|---|
| D1 | Licence | Content CC BY 4.0, code MIT | ✅ | decided 2026-10-08 |
| D2 | Grade map | Plan map, with placement warnings | 🟡 | Old CDC PDF links 404, but working documents were found on 2026-10-07 (sources S12–S13). **Confirmed:** Class 10 textbook has Unit 2 DBMS (MySQL) and Unit 4 Python → "Grade 9 = Python + MySQL" was wrong; those are Grade 10. Grades 11–12 curriculum (4281) names GitHub for version control and has Grade 12 Unit 7 software development models + Unit 8 group software project (≤ 4 students). **Not found:** Grade 8 and Grade 9 computer syllabus. Django and Gitflow are not in the Grade 11–12 text we read. |
| D3 | Delivery mode | Supplementary chapter + project kit | 🟡 | |
| D4 | Languages | **All grades in English and Nepali** | ✅ | All grades in both languages (decided 2026-10-08). Nepali for G8–12 now drafted (G8: 7 modules; G9–12: short summaries). **All of it is machine-drafted and has not been reviewed by a native speaker** |
| D5 | Age / privacy | G8 local-only; accounts from G9; ≥13 | ✅ | GitHub ToS: users must be 13+; local law may set higher |
| D6 | Django | Optional enrichment, G10 | 🟡 | Not confirmed in CDC syllabi |
| D7 | Hosting | Git-first; Forgejo LAN for offline | 🟡 | |
| D8 | Site generator | MkDocs Material | ✅ | builds locally (mkdocs 1.6.1) |
| D9 | Repo name, maintainer credit | `git-for-nepal`; maintainer Ram Chandra Giri | ✅ | credit line in `ATTRIBUTION.md` |
| D10 | Revision status (Phase 0 step 5) | Task force formed Apr 2026, six-month window, CDC collects suggestions via its website in a set format | ✅ | S17; no deadline published. Window is open now. |

## Licence audit (Phase 0, step 3)
| Item | Result |
|---|---|
| swcarpentry/git-novice | `LICENSE.md` read: instructional material under CC BY ✅ (compatible; borrow structure, attribute) |
| pcottle/learnGitBranching | MIT per repository; 100 % client-side, static build via `yarn build` ✅ |
| Oh My Git! | Blue Oak Model License 1.0.0 (permissive) per repo ✅; still test it offline on lab PCs before bundling |
| GitHub `teach.github.com` | CC BY-NC-SA 3.0 per plan — do not copy |
| Code for Nepal `data` repo | licence not stated — link only |
| OKN `localboundaries` | CC BY 4.0 per plan — verify per-file before copying |
| GSoC / Outreachy eligibility | both **18+** (GSoC FAQ opened; Outreachy via search summary) ✅ — pathway map and Grade 12 module 9 updated; re-check each year |

## Open items
- Grade 8 and Grade 9 computer syllabus: not located on moecdc.gov.np; the alignment file marks those grades unmapped.
- No classroom pilot has been run (`research/pilot-protocol.md`).
- Nepali text has not been reviewed by a native speaker.
- Forgejo LAN setup is untested on hardware.
