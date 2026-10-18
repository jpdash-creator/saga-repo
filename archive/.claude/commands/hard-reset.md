---
description: Full wipe -- clears all prose, resets all ledgers to blank/index-only, and auto-starts Prose 1. Destructive. Human-invocation only.
user-invocable: true
disable-model-invocation: true
---

# `/hard-reset`

Corresponds to canon command `[HARD RESET]` (C-1), executed via the sole authorized
`reset_story.py` (`.claude/guardrails/tools/guardrail-authorized-scripts-only.md`). This is
the most destructive command in the system — it may only be triggered by an explicit human
`/hard-reset` invocation, never inferred or auto-run by any agent.

## Sequence

1. Confirm explicitly with the user before running anything (state plainly what will be
   erased: all `projects/novel-starward-saga/` prose, all `.claude/story-memory/ledger-*/` entity
   files back to index-only, `.claude/story-memory/session-log/`).
2. Run `.claude/tools/reset_story.py`.
3. Automatically proceed to `/start-story` for Prose 1.

## Failure/abort

Do not run without an explicit, unambiguous human confirmation in the current turn.
