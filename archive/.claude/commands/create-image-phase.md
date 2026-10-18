---
description: Generate the phase icon (PNG+SVG) for a given Phase, via the authorized image script.
argument-hint: <phase number>
user-invocable: true
---

# `/create-image-phase`

Corresponds to canon command `[CREATE IMAGE: PHASE N]` (C-36). Uses
`.claude/tools/saga_image_creator.py` exclusively
(`.claude/guardrails/tools/guardrail-authorized-scripts-only.md`).

## Sequence

1. Confirm the Phase name/number and gather a short descriptive prompt from context (or ask).
2. Run `.claude/tools/saga_image_creator.py phase --phase N --name "<name>" --output-root projects/novel-starward-saga [--prompt ...]`.
3. Confirm the output files land at `projects/novel-starward-saga/phase-N/phase-icon.{png,svg}`.
