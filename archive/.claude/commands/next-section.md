---
description: Advance to the next Section (one of Phase 1's 8 locked Sections), then write its opening prose unit including title-page handling.
user-invocable: true
---

# `/next-section`

Corresponds to canon command `[NEXT SECTION]` (C-8). Phase 1 has exactly 8 Sections, locked
per Part 30 — confirm which Section is next against `ssc-narration-p30-phase-1-narrative-arc-map`
rather than assuming.

## Sequence

1. Invoke **outline-planner** to confirm the current Section's Novel-Parts/Chapters are
   complete, and to establish the next Section's thematic contribution.
2. Invoke **prose-scorer** to finalize the closing Section's CDL-2 running aggregate before
   moving on (a Section shouldn't close with an unresolved Anchor Floor warning unaddressed).
3. Run `/next-prose` for the new Section's opening prose unit, with
   `is_first_prose_of_section=true` (Section title-page/epigraph per Part 1 Rule 10.5.14),
   `is_first_prose_of_chapter=true`, and `is_first_prose_of_area=true` — a new Section's
   opening prose is simultaneously its first Chapter's and first Area's opening prose.

## Failure/abort

If the 8-Section lock would be exceeded, or the closing Section has an unresolved Anchor
Floor failure, stop and surface it rather than proceeding.
