---
description: Reset written prose/output AND all story-memory ledgers by running the full `.claude/tools/reset_story.py` script (it has no prose-only mode); canon skills, guardrails, and canon-manifest structure are untouched. Destructive to prose and ledger data. Human-invocation only.
user-invocable: true
disable-model-invocation: true
---

# `/reset-story`

Corresponds to canon command `[RESET STORY]` (C-21) — runs the full
`.claude/tools/reset_story.py`, which has no flag or mode to run only a subset of its
steps: every invocation clears prose output under `projects/novel-starward-saga/` AND
clears/cleans every `story-memory/ledger-*/` folder (session log, side-character files,
hero ledgers, and all other ledgers) in the same pass. There is no prose-only "portion"
of the script to invoke separately.

## Sequence

1. Confirm explicitly with the user before running (state plainly: all prose under
   `projects/novel-starward-saga/` will be removed, AND all `story-memory/ledger-*/`
   entity files will be reset/cleaned in the same run — canon skills, guardrails, and
   `.claude/canon-manifest/` are the only things left untouched).
2. Run `.claude/tools/reset_story.py` in full.

## Failure/abort

Do not run without explicit confirmation in the current turn.
