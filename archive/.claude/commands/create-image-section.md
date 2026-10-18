---
description: Generate the section icon (PNG+SVG) for a given Section, via the authorized image script.
argument-hint: <phase number> <section number>
user-invocable: true
---

# `/create-image-section`

Corresponds to canon command `[CREATE IMAGE: SECTION N]` (C-37). Uses
`.claude/tools/saga_image_creator.py` exclusively.

## Sequence

1. Confirm the Phase/Section numbers and name, and gather a short descriptive prompt (or ask).
2. Run `.claude/tools/saga_image_creator.py section --phase N --section M --name "<name>" --output-root projects/novel-starward-saga [--prompt ...]`.
3. Confirm the output files land at `projects/novel-starward-saga/phase-N/section-M/section-icon.{png,svg}`.
