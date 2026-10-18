---
description: Advance to the next Phase of the series. Rare -- Phase 1 alone is 8 Sections; only invoke once Phase 1 is genuinely complete.
user-invocable: true
disable-model-invocation: true
---

# `/next-phase`

Corresponds to canon command `[NEXT PHASE]` (C-9). The total phase count for the series is
explicitly undetermined ("TBD") per canon — this is a major, rare transition, not a
routine navigation step, hence explicit-invocation-only.

## Sequence

1. Confirm all 8 Sections of the current Phase are complete and audited clean (session-end
   FCIA + ALCA Mode B already run for the Phase's final Section).
2. Invoke **outline-planner** to establish the new Phase's premise and arc framework.
3. Invoke `/create-image-phase` for the new Phase's icon.
4. Run `/next-prose` for the new Phase's opening prose unit, with `is_first_prose_of_phase=true`,
   `is_first_prose_of_section=true`, `is_first_prose_of_chapter=true`, and
   `is_first_prose_of_area=true`.

## Failure/abort

Never advance a Phase with an incomplete or unaudited prior Section — surface it instead.
