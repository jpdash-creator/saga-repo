---
description: Delete all prose in the current Chapter only, then re-open it for a fresh draft. Destructive within scope. Human-invocation only.
user-invocable: true
disable-model-invocation: true
---

# `/reset-chapter`

Corresponds to canon command `[RESET CHAPTER]` (C-22). Scoped deletion — only the current
Chapter's prose files under `projects/novel-starward-saga/`.

## Sequence

1. Confirm explicitly with the user which Chapter is being reset and that its prose files
   will be deleted.
2. Delete the Chapter's prose files.
3. Invoke **continuity-checker** to run `/force-ledger-audit` afterward, since deleted prose
   may leave ledger entries referencing content that no longer exists — reconcile rather
   than leave stale.

## Failure/abort

Do not run without explicit confirmation of which Chapter is in scope.
