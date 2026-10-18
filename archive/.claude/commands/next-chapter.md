---
description: Advance to the next Chapter (resetting Area/Prose numbering within it), then write its opening prose unit.
user-invocable: true
---

# `/next-chapter`

Corresponds to canon command `[NEXT CHAPTER]` (C-6).

## Sequence

1. Invoke **outline-planner** to confirm the current Chapter's Areas are all complete and to
   establish the next Chapter's title, purpose, and opening beat.
2. Run `/next-prose` for the new Chapter's opening prose unit, with
   `is_first_prose_of_chapter=true` and `is_first_prose_of_area=true` (a new chapter's
   opening prose is simultaneously Area 1's opening prose) (Chapter Header Block handling
   per Rule 6.3.1/6.3.1a in `ssc-narration-p02-book-creation-law-chapter-document` and
   `.claude/tools/prose_docx_creator.py`).

## Failure/abort

Do not advance a Chapter that has open/unresolved Area content — surface it instead.
