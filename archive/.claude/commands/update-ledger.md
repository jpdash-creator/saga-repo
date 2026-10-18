---
description: Manually update a specific entity's ledger entry outside the normal post-write flow (e.g. to correct or enrich a field directly).
argument-hint: <entity name>
user-invocable: true
---

# `/update-ledger`

Corresponds to canon command `[UPDATE LEDGER: entity]` (C-15).

## Sequence

1. Invoke **continuity-checker** to read the entity's current ledger file.
2. Confirm the proposed change: enrichment of a blank/Living field is fine; contradicting an
   existing Baseline (B) field requires a formal Canon Amendment, not a routine update
   (`.claude/guardrails/ledger/guardrail-ledger-schema-law.md`) — stop and ask if that's what's
   being requested.
3. Apply the change, update `Last Updated` / `Ledger Version`, and regenerate the folder's
   `_index.md` entry for this file.

## Failure/abort

Never silently contradict a Baseline field — surface it as an amendment decision instead.
