---
description: Report the current position in the Starward Saga (Phase/Section/Novel-Part/Chapter/Area/Prose), open ledger obligations, and Section density trend.
user-invocable: true
---

# `/status`

Corresponds to canon command `[STATUS]` (C-13). Read-only — makes no changes.

## Sequence

1. Read `projects/novel-starward-saga/` to determine the actual current position on disk
   (never report a remembered position).
2. Read `.claude/story-memory/ledger-*/_index.md` files for any entity with a pending/stale
   Post-Write Ledger Update obligation.
3. Invoke **prose-scorer** for the current Section's CDL-2 running aggregate, flagging any
   category at ⚠ WARN or ✗ FAIL, especially the 4 Anchor Floor categories.
4. Report: position, open ledger obligations, density trend, and any outstanding
   Canon Variance entries logged in `.claude/story-memory/session-log/`.
