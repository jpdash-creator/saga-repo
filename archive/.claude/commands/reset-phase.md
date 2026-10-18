---
description: Delete all prose in a given Phase only, then re-open it for a fresh draft. Destructive within scope. Human-invocation only.
argument-hint: <phase number>
user-invocable: true
disable-model-invocation: true
---

# `/reset-phase`

Corresponds to canon command `[RESET PHASE: N]` (C-23). Scoped deletion — only the named
Phase's prose files (all its Sections/Novel-Parts/Chapters) under
`projects/novel-starward-saga/phase-N/`.

## Sequence

1. Confirm explicitly with the user which Phase number is being reset and that all its
   prose files will be deleted.
2. Delete `projects/novel-starward-saga/phase-N/` prose content (icons may be kept or
   regenerated per user preference — ask).
3. Invoke **continuity-checker** to run `/force-ledger-audit` afterward to reconcile ledgers
   against the now-shorter prose record.

## Failure/abort

Do not run without explicit confirmation of which Phase number is in scope.
