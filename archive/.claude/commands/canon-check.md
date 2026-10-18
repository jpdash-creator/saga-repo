---
description: Check a specific passage or claim against canon without running a full audit -- a targeted, single-question version of /run-canon-audit.
argument-hint: <passage or claim to check>
user-invocable: true
---

# `/canon-check`

Corresponds to canon command `[CANON CHECK: passage]` (C-20).

## Sequence

1. Identify which Part(s)/skill(s) govern the subject of the passage via
   `.claude/canon-manifest/skill-index.json` and `.claude/guardrails/authority/guardrail-domain-ownership.md`.
2. Invoke **continuity-checker** to read those specific skills plus any relevant
   `.claude/story-memory/ledger-*/` entries and verify the passage against them.
3. Report VALID / INVALID with the specific rule cited — never a vague impression. If
   genuinely ambiguous or a true Joint Domain case, say so rather than forcing a verdict.
