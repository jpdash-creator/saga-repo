---
description: Read-only session initialization -- load all skills, guardrails, the canon manifest, story-memory ledgers, and existing prose output to establish full current state.
user-invocable: true
---

# `/load-canon`

Corresponds to canon command `[LOAD CANON]` (C-35). Read-only session init; makes no
changes. Useful at the start of a session, or any time you want a full-state refresh rather
than trusting conversational memory (`.claude/guardrails/ledger/guardrail-session-log-not-canon.md`).

## Sequence

1. Read `.claude/guardrails/_index.md` and every guardrail file beneath it.
2. Read `.claude/canon-manifest/skill-index.json` (and the other manifest files) in full.
3. Read every `.claude/story-memory/ledger-*/_index.md`.
4. Read the current position and all existing prose under `projects/novel-starward-saga/`.
5. Report a brief summary of current state — do not draft, audit, or plan anything as part
   of this command.
