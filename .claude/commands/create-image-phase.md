---
description: Generate the phase icon (PNG+SVG) for a given Phase, via the authorized image script.
argument-hint: <phase number>
user-invocable: true
---

# `/create-image-phase`

Corresponds to canon command `[CREATE IMAGE: PHASE N]` (C-36). Uses
`.claude/tools/saga_image_creator.py` exclusively
(`.claude/guardrails/tools/guardrail-authorized-scripts-only.md`).

## Modes

The command always names the mode with `--mode`. The script's own default is `openai`, which fails
without a key.

- `svg`: the script draws the icon itself. It needs no key and sends nothing to an outside service.
  It writes both `phase-icon.svg` and `phase-icon.png`. The PNG needs the `cairosvg` library; without
  it the script stops with an error and writes nothing.
- `openai`: used only when `OPENAI_API_KEY` is set. The prompt is sent to an outside service. It writes
  the PNG only (`phase-icon.png`), with no SVG.

## Sequence

1. Confirm the Phase name/number and gather a short descriptive prompt from context (or ask).
2. Before anything is run, ask the author (`AskUserQuestion`) to confirm the mode and what it will use:
   for `openai` the prompt, shown in full; for `svg` the name and the drawing settings (`--svg-param`
   colours and shape, or the script's defaults). Nothing is generated before the answer, and the script
   is always given the confirmed prompt and mode (`--prompt`, `--mode`).
3. If `projects/novel-starward-saga/phase-N/phase-icon.png` or `phase-icon.svg` already exists, say so
   and ask before replacing it.
4. Run `.claude/tools/saga_image_creator.py phase --phase N --name "<name>" --mode <svg|openai>
   --prompt "<confirmed prompt>" [--svg-param KEY=VALUE ...]`. Do not pass `--output-root`: the
   script's default is the repo's `projects/novel-starward-saga`, anchored to the script's own
   location, so the images land there whatever folder the session runs from.
   If the script exits with an error, report its message and stop: it has written nothing.
5. Confirm the output files land at `projects/novel-starward-saga/phase-N/phase-icon.{png,svg}`
   (`phase-icon.png` alone in `openai` mode) and that the PNG is over 1 KB (1,024 bytes). A PNG of 1 KB
   or less is a failed run: say so, and do not report the icon as made.
