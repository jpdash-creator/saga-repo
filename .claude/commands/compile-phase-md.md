---
description: Assemble an entire Phase's Chapters into a single compiled Markdown file.
argument-hint: <phase number, default the current Phase>
user-invocable: true
---

# `/compile-phase-md`

Corresponds to canon command `[COMPILE PHASE MD]` (C-26). Markdown counterpart to
`/compile-phase`: the compiled file is produced by concatenating the per-Chapter
Chapter `.md` files (`Chapter NNN - <Chapter Name>.md`) in the Novel-Part folders — themselves made by `/chapter-builder` (C-24)
from the per-Area `.md` files (`chapter-NNN/area-NN.md`), per Part 2 Area 7 — for every Chapter in
the target Phase, in Section, Novel-Part and Chapter order (numbers sorted as integers). It never condenses.
`area_md_creator.py` writes only the per-Area `area-NN.md` substrate and has no chapter- or
phase-level function; the aggregation itself is a plain file-concatenation step.

## Sequence

1. Confirm every Chapter in the target Phase has an up-to-date `Chapter NNN - <Chapter Name>.md`
   in its Novel-Part folder, made by `/chapter-builder` (stale by the test of Part 2 Rule 5.3.5). Do not
   build any on the fly: if a Chapter file is missing or stale, STOP, list those Chapters, and tell the
   author to run `/chapter-builder` for each (it needs the author's confirmation), then run this command again.
2. Concatenate the Chapter `.md` files from the Novel-Part folders for the target Phase, in Section, Novel-Part and Chapter order (numbers sorted
   as integers), into `phase-N/phase-N-complete.md`. If that file already exists, replace it
   only after the author has been asked and has confirmed (Part 2 Rule 10.9.3).
3. Report the output path, `phase-N/phase-N-complete.md`.
