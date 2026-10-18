---
description: Force a full ledger audit and update across all story-memory folders -- reconciles every ledger against all accepted prose written so far.
user-invocable: true
---

# `/force-ledger-audit`

Corresponds to canon command `[FORCE LEDGER AUDIT AND UPDATE]` (C-38) — mandatory at every
Gate 2, also invokable standalone for a full reconciliation pass.

## Sequence

1. Invoke **continuity-checker** to read every `.claude/story-memory/ledger-*/` folder and
   every written prose file under `projects/novel-starward-saga/`.
2. For each entity: verify Baseline (B) fields are unmodified and Living (L) fields reflect
   the latest accepted prose (`.claude/guardrails/ledger/guardrail-ledger-schema-law.md`).
3. Regenerate each folder's `_index.md` registry from its entity files, then regenerate the
   root ledger index.
4. If prose introduced an entity type with no existing ledger folder, flag
   `NEW ENTITY TYPE — Part 37 schema not yet defined` and stop for explicit direction
   (`.claude/guardrails/ledger/guardrail-ledger-schema-law.md`) rather than inventing a folder.
5. Preview all proposed changes and require explicit confirmation before writing them.

## Failure/abort

Never write ledger changes without the preview+confirm step above.
