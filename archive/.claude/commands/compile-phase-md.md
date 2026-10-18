---
description: Assemble an entire Phase's Chapters into a single compiled Markdown file.
user-invocable: true
---

# `/compile-phase-md`

Corresponds to canon command `[COMPILE PHASE MD]` (C-26). Markdown counterpart to
`/compile-phase`: the compiled file is produced by concatenating the per-Chapter
`.md` files — each written via `.claude/tools/prose_md_creator.py`'s
`write_prose_to_per_prose_md()` — for every Chapter in the target Phase, in
Chapter order. `prose_md_creator.py` has no separate phase-compilation function;
the aggregation itself is a plain file-concatenation step.

## Sequence

1. Confirm every Chapter in the target Phase has an up-to-date per-Prose `.md` file.
2. Concatenate the per-Chapter `.md` files for the target Phase, in Chapter order, into a single compiled Markdown file.
3. Report the output path.
