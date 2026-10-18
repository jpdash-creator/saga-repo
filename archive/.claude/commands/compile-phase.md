---
description: Assemble an entire Phase's Chapters into a single compiled .docx.
user-invocable: true
---

# `/compile-phase`

Corresponds to canon command `[COMPILE PHASE]` (C-25).

## Sequence

1. Confirm every Chapter in the target Phase has already been exported via `/export-chapter`
   (or export any that haven't been yet).
2. Assemble the target Phase's compiled `.docx` by concatenating the per-Chapter aggregate
   documents already produced via `/export-chapter`, prefixed with the Phase title page
   (Rule 10.5.14) and phase icon. (Note: `.claude/tools/prose_docx_creator.py` currently
   provides only the per-Prose Gate-2 writer `write_prose_to_per_prose_docx()` and its
   metadata wrapper — it has no phase-level compilation/assembly function, so this
   concatenation step is performed directly rather than via a named script function.)
3. Report the output path.
