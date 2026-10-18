---
description: Assemble every completed Phase's Markdown file into a single full-novel compiled Markdown file.
argument-hint: "[no argument: every completed Phase is joined]"
user-invocable: true
---

# `/compile-novel-md`

Markdown counterpart to `/compile-novel`. It has no command code. The compiled file is produced by
joining the Phase-level Markdown files `phase-N-complete.md` (themselves made on demand by
`/compile-phase-md`, C-26), in Phase order, into `starward-saga-complete.md` at the root of
`projects/novel-starward-saga/`. `area_md_creator.py` writes only the per-Area `chapter-NNN/area-NN.md`
substrate and has no Phase- or novel-level function, so the join itself is a plain
file-concatenation step, as in `/compile-phase-md`. This is the largest-scope compile: confirm it is
genuinely intended (most sessions will use `/chapter-builder` or `/compile-phase-md` instead)
before running.

## Sequence

1. Confirm every Phase to be included has an up-to-date `phase-N-complete.md` from
   `/compile-phase-md`: test each existing file by Part 2 Rule 5.3.5 (a Chapter file or per-Area
   file of the Phase newer than it, or files of the Phase moved to the archive since, makes it
   stale). Compile any Phase that has none, recompile any stale one first, and report which were regenerated (`/compile-phase-md` stops when a Chapter
   file is missing or stale; the remedy is `/chapter-builder` for those Chapters). Nothing is condensed here. The `_archive` folder is never read.
2. Join the Phase files, in Phase order (numbers sorted as integers), into
   `projects/novel-starward-saga/starward-saga-complete.md`. If that file already exists, replace it
   only after the author has confirmed.
3. Report the output path.
