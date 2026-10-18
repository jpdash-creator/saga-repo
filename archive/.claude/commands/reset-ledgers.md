---
description: Reset all story-memory ledgers to blank/index-only, leaving written prose untouched. Does not invoke `.claude/tools/reset_story.py` (that script has no ledger-only mode and always also deletes prose); ledger-clearing is performed directly per this command's Sequence instead. Destructive to ledger data. Human-invocation only.
user-invocable: true
disable-model-invocation: true
---

# `/reset-ledgers`

Corresponds to canon command `[RESET LEDGERS]` (C-2). Note: `.claude/tools/reset_story.py`
has no CLI flag to run only its ledger-clearing steps — its `main()` unconditionally runs
its prose-clearing step too, deleting all `prose-*.md`/`prose-*.docx` files under
`projects/novel-starward-saga/` (see `/reset-story` for that full, prose-inclusive reset).
This command therefore does NOT invoke that script; it performs the equivalent
ledger-clearing steps directly, leaving prose alone.

## Sequence

1. Confirm explicitly with the user before running (state plainly: all
   `.claude/story-memory/ledger-*/` entity files reset to index-only; prose is not affected).
2. Perform the ledger-clearing steps directly — equivalent to steps 2-5 of
   `.claude/tools/reset_story.py` (clear `session-log/`, clear `ledger-character-side/`,
   clean `ledger-character-hero/`, clean other `ledger-*/` folders) — without invoking that
   script, since running it would also delete prose per its Step 1.
3. Recommend `/force-ledger-audit` afterward if any prose already exists, so ledgers get
   rebuilt from what's actually on the page rather than staying blank while prose is ahead.

## Failure/abort

Do not run without explicit confirmation in the current turn.
