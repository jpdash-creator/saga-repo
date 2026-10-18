---
description: Assemble an entire Phase's Chapters into a single compiled .docx.
argument-hint: <phase number, default the current Phase>
user-invocable: true
---

# `/compile-phase`

Corresponds to canon command `[COMPILE PHASE]` (C-25).

## Sequence

1. Confirm every Chapter in the target Phase has an up-to-date Chapter file made by `/chapter-builder`
   in its Novel-Part folder: test each existing `Chapter NNN - <Chapter Name>.docx` by Part 2 Rule 5.3.5
   (a per-Area file of the Chapter newer than it, or files of the Chapter moved to the archive since,
   makes it stale). This command never condenses and does not build Chapter files on the fly: if any
   Chapter has no Chapter file or a stale one, STOP, list those Chapters, and tell the author to run
   `/chapter-builder` for each (it needs the author's confirmation), then run this command again.
2. Assemble the target Phase's compiled `.docx` with the join function of
   `.claude/tools/area_docx_creator.py` (`assemble_phase_docx`), run as
   `python .claude/tools/area_docx_creator.py assemble --scope phase --phase N` (add `--overwrite` only after
   the author has been asked and has confirmed replacing an existing `phase-N-complete.docx`, Part 2 Rule 10.9.3). It joins the Chapter
   documents (`Chapter NNN - <Chapter Name>.docx`) already produced by `/chapter-builder` in the Novel-Part folders, in Section, Novel-Part and Chapter order (numbers sorted
   as integers), each Chapter starting a new page under its own running head, into
   `phase-N/phase-N-complete.docx`. The Phase title page (Part 2 Rule 6.3.1b) and phase icon already open the
   Phase's first Chapter file, so the join starts with them. It then adds the contents page (Part 2 Rule 10.8.1), built from the
   Chapter names of the joined Chapter documents (it lists Chapters, no Area lines), and nothing else before the first Chapter.
   The script
   stops, naming the Chapter, if a Chapter file is missing or stale.
3. Report the output path, `phase-N/phase-N-complete.docx`.
