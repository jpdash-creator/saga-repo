---
description: Advance to the next Novel-Part (resetting Chapter numbering within it), then write its opening prose unit.
user-invocable: true
---

# `/next-part`

Corresponds to canon command `[NEXT PART]` (C-7). "Novel-Part" is Part 2's six-tier
structural unit, distinct from a canon-law "Part" (e.g. Part 3, Part 22) — do not confuse
the two when reading skills/guardrails.

## Sequence

1. Invoke **outline-planner** to confirm the current Novel-Part's Chapters are complete and
   to establish the next Novel-Part's arc contribution (per `ssc-narration-p30-*`'s macro
   story arc).
2. Run `/next-prose` for the new Novel-Part's opening prose unit, with
   `is_first_prose_of_chapter=true`, `is_first_prose_of_area=true`, and the new
   novel_part_name passed through.

## Failure/abort

Do not advance if the current Novel-Part's arc threads are left unresolved without cause —
surface it.
