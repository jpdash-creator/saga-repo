---
description: Assemble every completed Phase into a single full-novel compiled document.
user-invocable: true
---

# `/compile-novel`

Corresponds to canon command `[COMPILE NOVEL]` (C-27). The largest-scope compile — confirm
this is genuinely intended (most sessions will use `/export-chapter` or `/compile-phase`
instead) before running.

## Sequence

1. Confirm every Phase to be included is fully compiled via `/compile-phase`.
2. Assemble the full novel by concatenating, in order, the already-compiled Phase-level
   documents produced by `/compile-phase` (there is no separate full-novel assembly
   function in `.claude/tools/prose_docx_creator.py`; its only public interfaces are the
   per-Prose Gate-2 writer `write_prose_to_per_prose_docx()` and its metadata-dict wrapper).
3. Report the output path.
