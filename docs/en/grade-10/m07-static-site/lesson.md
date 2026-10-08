---
id: g10-m07-static-site
grade: 10
hours: 2
prerequisites: [g10-m06-releases]
outcomes:
  - "Build a small HTML/CSS site in a repo"
  - "Publish it with a static-host feature or open it from disk"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 7. Publishing a static website from the repo

## Hook
Can the school have a web page without buying a server?

## Concept (unplugged or visual first)
A **static site** is just files: `index.html`, `style.css`, images. Hosts like GitHub Pages or Codeberg Pages serve a branch for free. On the LAN, any computer can serve the folder (`python -m http.server`).

## PRIMM lab
Practice repo: `practice-repos/g10-school-website`.
1. Open `index.html` in a browser (tier 1 works offline).
2. **Predict**, then change the headline and the colour in `style.css`; refresh.
3. Add an `about.html` on a branch; link it from the menu; open a PR.
4. Publish: tier 3 → enable Pages for `main`; tier 2 → `python -m http.server 8000` on the server PC.
5. **Make:** add one page that uses an open dataset table (credit the source).

## Parsons practice
Order: *edit HTML · open in browser · commit · push · publish*.

## Exit ticket
1. What makes a site 'static'?
2. Where would you publish with no internet?
3. *Misconception:* 'a website needs a database.' True or false?

## Teacher notes
Credit images and text (CC BY). Never publish student names or photos. Use the check script `check.sh` to validate that every internal link exists.
