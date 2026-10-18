---
description: Interrupt an in-progress command sequence cleanly, without writing a partial file or a partial ledger update.
user-invocable: true
---

# `/pause`

Corresponds to canon command `[PAUSE]` (C-34). The sole mid-execution interrupt.

## Behavior

Stop the current sequence at the next safe boundary (never mid-file-write). If a Gate 1
audit was already shown but not yet confirmed, leave it pending rather than discarding it.
A pending draft is held only in this conversation (no file holds it), so it survives only
inside the same conversation, where the author can still confirm it or abandon it. A new
session starts again at `/next-area` Step 0; answers given before Gate 2 are held only in the
conversation and are asked again in a new session, because the Chapter Spec records them at the
Gate 2 as-built sync. Running `/next-area` again abandons the pending draft.
If the two Area files are already written, finish the Step 6 and 7 lanes before stopping, or leave
the Area to be repaired by `/force-ledger-audit` (`/status` lists it as `incomplete Gate 2`).
Do not perform a ledger update for anything not yet confirmed at Gate 2.
