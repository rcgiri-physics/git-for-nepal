# Datasets

**Rule:** a dataset enters this folder only if its licence allows redistribution and it is documented here and in its own `DATA.md`. `tools/check_datasets.py` enforces this in CI.

| Dataset | Folder | Source | Licence | Used in |
|---|---|---|---|---|
| *(none yet)* | | | | |

## Link-only (do not copy)
| Dataset | Why link-only |
|---|---|
| Code for Nepal `data` repo (<https://github.com/CodeforNepal/data>) | no licence stated — ask maintainers before copying |
| Open Data Nepal (<https://opendatanepal.com/>) | licences vary per dataset — check each |
| OKN `localboundaries` (<https://github.com/openknowledgenp/localboundaries>) | stated CC BY 4.0; verify per file, then may copy with attribution |

## Until real datasets are vetted
Grade 8–9 labs use **synthetic teaching data** written for this project (`practice-repos/*/data/`, licensed CC BY 4.0 with the content). It is clearly fake (invented ward names/numbers) and contains no real person.

## `DATA.md` template
```
name:
source_url:
retrieved: YYYY-MM-DD
licence:            # exact name + link
redistribution_ok:  # yes
attribution_text:
personal_data:      # none
changes_made:
```
