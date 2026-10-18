---
description: Interrupt an in-progress command sequence cleanly, without writing a partial file or a partial ledger update.
user-invocable: true
---

# `/pause`

Corresponds to canon command `[PAUSE]` (C-34) — the sole mid-execution interrupt.

## Behavior

Stop the current sequence at the next safe boundary (never mid-file-write). If a Gate 1
audit was already shown but not yet confirmed, leave it pending rather than discarding it —
the next `/next-prose`-family invocation should be able to resume from that pending state, or
the user can explicitly abandon it. Do not perform a ledger update for anything not yet
confirmed at Gate 2.
