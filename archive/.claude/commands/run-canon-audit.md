---
description: Run a full canon audit (CCIA + FCIA + ALCA) across all skills, guardrails, story-memory ledgers, and written prose. The escalation target whenever an agent or command detects an unresolved conflict.
user-invocable: true
---

# `/run-canon-audit`

Corresponds to canon command `[RUN CANON AUDIT]` (C-10). This is the general escalation
target referenced throughout the guardrails ("escalate via `/run-canon-audit`") — invoke it
whenever a conflict needs full-system verification rather than a narrow single-unit check.

## Sequence

1. Invoke **continuity-checker** to run CCIA (`.claude/guardrails/audit/guardrail-ccia.md`) —
   governance/structure integrity across skills, guardrails, and the canon manifest.
2. Invoke **continuity-checker** to run FCIA (`audit/guardrail-fcia.md`) across all written
   prose in `projects/novel-starward-saga/`.
3. Invoke **continuity-checker** to run ALCA Mode B (`audit/guardrail-alca.md`) across all
   `.claude/story-memory/ledger-*/` folders.
4. Produce a Unified Audit Summary and log it to `.claude/story-memory/session-log/`.

## Failure/abort

Any finding that implies a structural change (new skill, guardrail edit, manifest change,
schema change) is reported for explicit decision, never auto-applied.
