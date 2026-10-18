---
description: Assemble every completed Phase into a single full-novel compiled document.
argument-hint: "[no argument: every completed Phase is joined]"
user-invocable: true
---

# `/compile-novel`

Corresponds to canon command `[COMPILE NOVEL]` (C-27). The largest-scope compile — confirm
this is genuinely intended (most sessions will use `/chapter-builder` or `/compile-phase`
instead) before running.

## Sequence

1. Confirm every Phase to be included has an up-to-date compiled document from `/compile-phase`:
   test each existing `phase-N-complete.docx` by Part 2 Rule 5.3.5 (a per-Area file or Chapter
   file of the Phase newer than it, or files of the Phase moved to the archive since, makes
   it stale). Compile any Phase that has none, recompile any stale one first, and report which were regenerated. Compiling a Phase stops when a Chapter
   file is missing or stale; the remedy is `/chapter-builder` for those Chapters, never a silent build here.
2. Assemble the full novel with the join function of `.claude/tools/area_docx_creator.py`
   (`assemble_novel_docx`), run as `python .claude/tools/area_docx_creator.py assemble --scope novel`
   (add `--overwrite` only after the author has been asked and has confirmed replacing an existing
   `starward-saga-complete.docx`, Part 2 Rule 10.9.3). It joins, in Phase order, the already-compiled Phase-level documents
   produced by `/compile-phase` into `starward-saga-complete.docx` at the root of
   `projects/novel-starward-saga/`. It also builds the novel's contents page (Part 2 Rule 10.8.1) from the
   Chapter names of every Phase (Chapters only, no Area lines); the page follows the title page of the first Phase and replaces
   the contents page of each Phase document. The script stops, naming the Phase, if a Phase file is
   missing or stale.
3. Report the output path, `projects/novel-starward-saga/starward-saga-complete.docx`.
