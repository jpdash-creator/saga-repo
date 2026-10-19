---
name: reference-proposal-drafting-tricks
description: Word-count method with no Bash, the unified Part 44 position scale, name-scan glob traps, and fight-plan reads for a consultation proposal under a word limit
metadata:
  type: reference
---

**Word count without Bash.** Grep `output_mode: count` counts matching lines, never matches. To size a file against a word limit, run Grep count with `^(\S+\s+){k}\S+` for k = 0, 10, 20 ... 100, then 120, 140 ... 220 (parallel calls) and add the survival counts: 10 x trapezoid per 10-token step, 20 x per 20-token step. This counts whitespace tokens: table pipes (columns + 1 per row), bullet dashes and `1.` markers inflate it by 200 to 260, so a table-heavy brief reads about 8 percent high. Converting tables to bullet lists is the cheapest cut when a limit is tight. A 3,500-word limit was met at about 3,535 tokens (about 3,470 words).

**Part 44 gaps on one scale.** A realm spans 36 minor steps (4 x 9 Levels). Senior 0 to 35, Warrior 36 to 71, Champion 72 to 107, Ruler 108 to 143; position = realm base + 4 x (Level - 1) + 0, 1, 2 or 3 (Low, Mid, High, Peak); gap = difference. Senior, Warrior, Champion, Ruler and Monarch are all Mortal Tier 2, so a Champion against Warriors is Shut and never Barred; Barred is only across Mortal, Xiantian, Core and Divine. Recompute ranges from the band ends.

**Name scans.** Exclude `archive/**` as well as `**/_archive/**` (a top-level `archive` folder exists), and `.claude/temp/**` once your own draft sits there. Count mode hides which name hit; rerun in content mode with `-o` and the known hits removed. Long-line hits print as "[Omitted long matching line]", so use `-o` with a short alternation. Hits for a pool name may sit in a spec note offering the pool (a pool name partly used is an echo risk; skip it).

**Fight plans for the exiles.** Read both heroes' L25, L27 and L03 lines before planning joy or banter: Hercules's registered grammar (one placed blow, the audited steps, controls without harming) and Bison's (strict proportionality, a held reserve) are author-locked, so an author-ruled exuberance is an Evolution Entry (ADD or CHANGE) at Gate 2, named by cell in a Settled note, never a silent drift. The audited climb gives a natural order for moves across Areas (Basic, then Intermediate, then Advanced, each proven necessary).

**Mid-task rulings.** When the coordinator relays a chat ruling during the build, apply it to the draft, mark it Settled in the hand-off section, remove it from the question list, and re-measure the length.
