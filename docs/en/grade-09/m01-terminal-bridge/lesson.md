---
id: g9-m01-terminal-bridge
grade: 9
hours: 1
prerequisites: []
outcomes:
  - "Move around folders with cd, ls (dir), mkdir"
  - "Explain what a path is"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 1. Terminal basics bridge

## Hook
The teacher asks a student to find `article.md` using only typed words, no mouse. Why might a programmer prefer this?

## Concept (unplugged or visual first)
Unplugged: a **human terminal**. One student is the 'computer' standing in a floor-map of folders (chalk squares: `school/` → `class9/` → `ward-facts/`). The partner types commands on paper: `cd class9`, `ls`, `cd ..`. The computer walks accordingly.

## PRIMM lab
1. **Predict:** what will `pwd` print? Run it.
2. `ls` (or `dir` on Windows cmd; Git Bash accepts `ls`). Predict, then run.
3. `mkdir ward-facts` then `cd ward-facts`. Check with `pwd`.
4. **Investigate:** what does `cd ..` do? What does `cd` alone do?
5. **Modify:** make `a/b/c` using `mkdir -p`, then return home.
6. **Make:** create a folder tree for your pair project and draw it.

## Parsons practice
Order: *mkdir ward-facts · cd ward-facts · pwd · ls*. Then: write the commands to go from `ward-facts` back to the folder above.

## Exit ticket
1. What does `cd ..` do?
2. Which command shows where you are?
3. *Misconception:* 'the terminal deletes things by itself.' True or false?

## Teacher notes
Use Git Bash on Windows labs so students see the same commands as on Linux. Avoid `rm -r` in this lesson. **Fallback tier 0:** run the human-terminal game for the whole period.
