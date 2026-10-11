---
id: g9-m01-terminal-bridge
grade: 9
hours: 1
prerequisites: []
outcomes:
  - "Move around folders with cd, ls (dir), mkdir"
  - "Explain what a path is"
  - "Read a terminal prompt and recover when lost"
tier_support: [1, 2, 3]
license: CC-BY-4.0
---

# 1. Terminal basics bridge

!!! abstract "At a glance"
    **Time:** 1 period · **Tiers:** 1–3 (Tier 0: the human-terminal game) · **You need:** a lab PC with **Git Bash** (Windows) or a terminal (Linux/macOS); chalk or tape for the floor map

    **Before this:** Grade 8 (or the [bridge course](../../book/after-grade-12.md#bridge-course)).

    **By the end you can:** say where you are (`pwd`), look around (`ls`), move (`cd`), make folders (`mkdir`), and explain absolute and relative paths.

## Hook (5 min)
The teacher asks a student to find `article.md` using only typed words — no mouse. It feels slow at first. Then the teacher types one line that makes 30 folders, one per student, in a second. *Why might a programmer prefer typing?*

## Understand it

### What is the terminal?
The **terminal** (also called the *command line* or *shell*) is a window where you give the computer instructions by typing. Each instruction is a **command**. You type it after the **prompt**, press Enter, and the computer replies with text.

```
student07@LAB-PC MINGW64 ~/school/class9        <- prompt: who @ computer, WHERE
$ ls                                            <- you type a command after the $
ward-facts  magazine  notes.txt                 <- the computer's answer
```

Why learn it when buttons exist?

- **Every Git feature** is available in the terminal; buttons cover only some.
- Commands can be **written down, shared and repeated** exactly ("type this") — clicks cannot.
- Servers, Raspberry Pis and cloud computers usually have **no mouse at all**.
- It works the same on Windows (with Git Bash), Linux and macOS.

### Folders form a tree
Your files live in folders inside folders — a **tree**, drawn upside down:

```
/c/Users/student07            <- your "home" folder (shortcut: ~)
├── school
│   ├── class8
│   │   └── magazine
│   └── class9
│       └── ward-facts        <- we want to be here
└── Downloads
```

A **path** is the address of a folder or file in that tree.

- An **absolute path** starts from the top: `/c/Users/student07/school/class9/ward-facts`. It works from anywhere.
- A **relative path** starts from where you are now. From `school`, the same folder is `class9/ward-facts`.
- Two special names: `.` means "this folder" and `..` means "the folder above". `~` means your home folder.

### Five commands for today
| Command | Means | Example |
|---|---|---|
| `pwd` | **p**rint **w**orking **d**irectory — where am I? | `pwd` → `/c/Users/student07/school` |
| `ls` | **l**i**s**t what is here | `ls` → `class8  class9` |
| `cd <path>` | **c**hange **d**irectory — move | `cd class9`, `cd ..`, `cd ~` |
| `mkdir <name>` | **m**a**k**e **dir**ectory | `mkdir ward-facts` |
| `mkdir -p a/b/c` | make several levels at once | |

Useful extras: `ls -a` shows hidden files (such as `.git`!), `clear` clears the screen, and the **Tab** key completes names for you — type `cd wa` then Tab. The **↑ arrow** brings back the last command.

!!! tip "Windows labs"
    Use **Git Bash** (installed with Git for Windows), not `cmd`. Then every command in this book works the same on Windows and Linux. In `cmd` the equivalent of `ls` is `dir`.

## See it
```console
$ pwd
/c/Users/student07
$ mkdir -p school/class9
$ cd school/class9
$ mkdir ward-facts
$ ls
ward-facts
$ cd ward-facts
$ pwd
/c/Users/student07/school/class9/ward-facts
$ cd ..
$ pwd
/c/Users/student07/school/class9
$ cd
$ pwd
/c/Users/student07                       <- "cd" alone always takes you home
```

## Unplugged: the human terminal (15 min)
Draw a floor map of folders with chalk squares: `home` → `school` → `class9` → `ward-facts`, and a side branch `Downloads`. One student is the **computer** and stands in `home`. The partner is the **user** and writes commands on paper, one at a time: `cd school`, `ls`, `cd class9`, `cd ..`, `pwd`. The computer obeys *exactly* — no guessing. If the command is impossible (`cd ward-facts` from `home`), the computer says `No such file or directory`.
Swap roles. Then the class writes, on the board, the **shortest** command list to go from `Downloads` to `ward-facts` (answer: `cd ../school/class9/ward-facts`).

## PRIMM lab (25 min)
1. **Predict:** what will `pwd` print when you open the terminal? Run it.
2. `ls` (or `dir` on Windows cmd; Git Bash accepts `ls`). Predict, then run. Then `ls -a`: what new names appear?
3. `mkdir ward-facts` then `cd ward-facts`. Check with `pwd`.
4. **Investigate:** what does `cd ..` do? What does `cd` alone do? What does `cd -` do?
5. **Modify:** make `a/b/c` using `mkdir -p`, go into `c`, then return home in **one** command.
6. **Make:** create a folder tree for your pair project (for example `ward-facts/data`, `ward-facts/scripts`, `ward-facts/docs`) and draw it as a tree in your notebook.

## Parsons practice (5 min)
Order: *mkdir ward-facts · cd ward-facts · pwd · ls*. Then: write the commands to go from `ward-facts` back to the folder above.

## Common mistakes
| Symptom | Cause | Fix |
|---|---|---|
| `No such file or directory` | you are not where you think, or a typo | `pwd`, then `ls`; use Tab completion |
| Spaces in names break commands | `cd my folder` is read as two words | avoid spaces; use `my-folder`, or quotes: `cd "my folder"` |
| `ls` "doesn't work" on Windows | you are in `cmd` or PowerShell | open Git Bash |
| Case errors (`Ward-Facts` vs `ward-facts`) | Linux paths are case-sensitive | use lower-case names everywhere |
| Lost in the tree | — | `cd` alone goes home; start again |

## Practise more with free resources
| # | Exercise | Tier | Time | Hand in |
|---|---|---|---|---|
| 1 | Software Carpentry Shell: [**Navigating Files and Directories**](https://swcarpentry.github.io/shell-novice/02-filedir.html) (CC BY — can be printed). Do its exercises on absolute vs relative paths. | 1 / 3 | 30 min | exercise answers |
| 2 | Software Carpentry Shell: [**Working With Files and Directories**](https://swcarpentry.github.io/shell-novice/03-create.html) — only the parts on `mkdir`, `touch`/creating files, and good names. | 1 / 3 | 20 min | 3 naming rules |
| 3 | [explainshell](https://explainshell.com/): paste `ls -la` and `mkdir -p a/b/c`. What does each part mean? | 3 | 10 min | explanations |
| 4 | William Shotts, [**Learning the Shell**](https://linuxcommand.org/lc3_learning_the_shell.php) — first two pages ("What is the shell?", "Navigation"). | 3 | 20 min | 5 new facts |
| 5 | **Speed challenge (paper or PC):** from `home`, reach five folders the teacher names using the fewest commands. | 0 / 1 | 10 min | command lists |

## Exit ticket (5 min)
1. What does `cd ..` do?
2. Which command shows where you are?
3. *Misconception:* "The terminal deletes things by itself." True or false?

## Key points
- The terminal runs typed **commands**; the prompt shows where you are.
- Folders form a **tree**; a **path** is an address in it (absolute from the top, relative from here).
- `pwd` where · `ls` look · `cd` move · `mkdir` make. `..` is up, `~` is home.
- Tab completes, ↑ repeats. Use Git Bash on Windows.

## New words
**terminal / shell**, **command**, **prompt**, **path**, **absolute / relative path**, **home folder** — see the [glossary](../../glossary.md).

## Extension quest
Find out what `ls -l` shows that `ls` does not. What is the date column?

## Teacher notes
- **Timing:** hook 5 · understand + see it 10 · human terminal 15 · lab 10 (steps 1–4; 5–6 as homework) · exit 5. If short of time, run the human terminal for only one pair at the front.
- Use **Git Bash** on Windows labs so students see the same commands as on Linux. Pin it to the taskbar before class.
- **Avoid `rm -r`** in this lesson. If a student asks how to delete, show `rmdir` on an empty folder only.
- **Misconception:** the terminal is scary/dangerous. It only does what you type; most commands (all of today's) only look or create.
- **Fallback Tier 0:** run the human-terminal game for the whole period, including the shortest-path challenge.
- **Answer key:** Exit 1: moves to the folder above. 2: `pwd`. 3: False — it only does what you type. Lab 4: `cd` alone → home; `cd -` → back to the previous folder. Lab 5: `cd ~` or `cd`. Parsons answer as given; then `cd ..`.
