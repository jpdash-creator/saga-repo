---
description: Discard and completely redraft an entire Chapter's worth of prose units.
user-invocable: true
---

# `/redraft-chapter`

Corresponds to canon command `[REDRAFT CHAPTER]` (C-30). Same discipline as `/redraft-area`
but scoped to the whole current Chapter.

## Sequence

1. Invoke **outline-planner** to re-confirm the Chapter's Area-by-Area plan.
2. Archive the Chapter's existing per-Prose subtree with a timestamp (Rule 5.3.2' in
   `ssc-narration-p02-novel-output-file-structure-law`) — the prior prose is preserved, not deleted.
3. Rebuild fresh per-Prose file pairs under the Chapter folder: run `/next-prose` repeatedly,
   one unit at a time, through every Area of the Chapter.
4. Run `/force-ledger-audit` once the Chapter is fully redrafted.

## Failure/abort

Confirm the redraft scope (exactly this Chapter) before archiving and rebuilding.
