---
description: Discard and completely redraft an entire Area's worth of prose units (not just one unit -- see /revise-prose for that).
argument-hint: <area reference>
user-invocable: true
---

# `/redraft-area`

Corresponds to canon command `[REDRAFT AREA: ref]` (C-29).

## Sequence

1. Invoke **outline-planner** to re-confirm what the Area should cover (the redraft may be
   happening precisely because the original plan didn't work).
2. Run `/next-prose` repeatedly (one full Gate 1->Gate 2 cycle per unit,
   never batched — `.claude/guardrails/commands/guardrail-deprecated-commands.md`) for every
   Prose unit in the Area — each unit's existing file pair is overwritten in place at Gate 2
   as the redraft progresses (Rule 5.3.2' in `ssc-narration-p02-novel-output-file-structure-law`);
   there is no upfront deletion.
3. Run `/force-ledger-audit` once the Area is fully redrafted.

## Failure/abort

Confirm the redraft scope (exactly this Area, not adjacent ones) before overwriting anything.
