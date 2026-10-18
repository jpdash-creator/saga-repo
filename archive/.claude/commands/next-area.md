---
description: Advance to the next narrative Area within the current Chapter, then write its opening prose unit.
user-invocable: true
---

# `/next-area`

Corresponds to canon command `[NEXT AREA]` (C-5). An "Area" here is the narrative
structural unit from Part 2's six-tier hierarchy (Phase -> Section -> Novel-Part -> Chapter
-> **Area** -> Prose) — distinct from a canon-law "Area" (the `ssc-*` skill unit). Do not
confuse the two.

## Sequence

1. Invoke **outline-planner** to confirm the current Chapter is ready to advance to its next
   Area (all planned beats for the current Area covered) and to establish what the new
   Area covers.
2. Run `/next-prose` for the Area's opening prose unit, with `is_first_prose_of_area=true`
   passed through to the write step (title/divider handling in
   `.claude/tools/prose_docx_creator.py` / `prose_md_creator.py`).

## Failure/abort

If the current Area's beats aren't actually finished, surface that rather than advancing
early.
