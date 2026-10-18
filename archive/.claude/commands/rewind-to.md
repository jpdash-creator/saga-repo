---
description: Roll the story back to a specific prior prose reference, discarding everything written after it. Destructive. Human-invocation only.
argument-hint: <prose reference>
user-invocable: true
disable-model-invocation: true
---

# `/rewind-to`

Corresponds to canon command `[REWIND TO: prose-ref]` (C-16).

## Sequence

1. Confirm explicitly with the user the exact target prose reference, and state plainly
   which prose files will be archived as non-canonical (everything after that reference).
2. Archive the prose files after the target reference as non-canonical pending revision
   (Rule 5.3.2' in `ssc-narration-p02-novel-output-file-structure-law`) — do not delete them;
   they are superseded one at a time only as new prose is written forward from the rewind point.
3. Invoke **continuity-checker** to run `/force-ledger-audit`, reconciling every ledger back
   to the state implied by prose up through the target reference only — Living (L) fields
   that were only established by now-archived prose must be rolled back too, not left ahead
   of the actual story.

## Failure/abort

Do not run without an explicit, unambiguous target reference confirmed by the user.
