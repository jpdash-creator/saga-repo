---
description: Revise an already-written prose unit in place, re-running the full Gate 1/Gate 2 cycle on the revision.
argument-hint: <prose reference>
user-invocable: true
---

# `/revise-prose`

Corresponds to canon command `[REVISE PROSE: ref]` (C-28). A revision is not exempt from the
audit pipeline just because the unit was previously accepted.

## Sequence

1. Invoke **prose-maker** to revise the identified prose unit per the requested change.
2. Invoke **continuity-checker** for a fresh Gate 1 audit of the revision (not a diff-only
   check — the whole unit is re-audited).
3. Confirm via `[CONFIRM WRITE]` / `[REVISE PROSE]` / `[SKIP WRITE]`.
4. On confirm: overwrite the `.docx`/`.md` files via the authorized scripts, run Gate 2, and
   run `/force-ledger-audit` since the revision may change what the ledger should say.

## Failure/abort

A revision that fails Gate 1 is corrected and re-audited exactly like a fresh draft — never
written through on the strength of the original's prior approval.
