---
description: Display an entity's current ledger state in full.
argument-hint: <entity name>
user-invocable: true
---

# `/review-ledger`

Corresponds to canon command `[REVIEW LEDGER: entity]` (C-14). Read-only.

## Sequence

1. Locate the entity's ledger file across `.claude/story-memory/ledger-*/` (use the relevant
   `_index.md` registries, or `.claude/canon-manifest/ledger-architecture-map.json` if the folder
   isn't obvious).
2. Read and display the file in full, noting which fields are Baseline (B) vs Living (L)
   per `.claude/guardrails/ledger/guardrail-ledger-schema-law.md`.
3. Flag anything marked "not yet established" so it's visible as a gap, not silently omitted.
