---
description: Reset all story-memory ledgers, leaving written Areas untouched, via `.claude/tools/reset_story.py --ledgers-only --keep-specs --keep-agent-memory`. Destructive to ledger data. Human-invocation only.
user-invocable: true
disable-model-invocation: true
---

# `/reset-ledgers`

Corresponds to canon command `[RESET LEDGERS]` (Command C-2). It runs the one authorized reset script
with the three flags that define this command's scope:

```
.claude/tools/reset_story.py --ledgers-only --keep-specs --keep-agent-memory
```

`--ledgers-only` skips the Area-file pass entirely, so written Areas (`area-NN.docx` and
`area-NN.md`) are never at risk. Every `story-memory/ledger-*/` file has its story record
cleared — Canon Events Logs emptied, Area-reference citations and anchor fields stripped,
descriptive content kept — and **no ledger entity file is deleted**, side-character files
included.

This command never re-implements the script's ledger pass by hand: hand-reimplementing an
authorized script's logic is exactly the drift `guardrails/tools/guardrail-authorized-scripts-only.md`
exists to prevent, so the script's ledger-only flag does the work.

## Sequence

1. Confirm before running, as `guardrails/commands/guardrail-command-law.md` requires of a
   destructive command. First run `.claude/tools/reset_story.py --dry-run --ledgers-only
   --keep-specs --keep-agent-memory`, which writes nothing and prints every ledger file it would
   clean (its lines still read `cleaned:`), and show the author its count of ledger files.
   Then state plainly: every `.claude/story-memory/ledger-*/` file will have its story record
   cleared while keeping its descriptive content; every file in `.claude/story-memory/session-log/` (`README.md` kept) will be deleted; the written Areas are not affected. Ask
   through `AskUserQuestion` with a Cancel option; the confirming answer names the scope in
   words (for example "Reset ledgers: all ledger records and the session log; written Areas untouched").
2. Run `.claude/tools/reset_story.py --ledgers-only --keep-specs --keep-agent-memory`.
3. Resolve the script's REVIEW REQUIRED report: it prints every ledger line where it could
   not separate a descriptive fact from its Area citation, and leaves those lines untouched.
   Invoke **continuity-checker** in parallel, one call per affected file, to resolve them.
   A flagged Section 12 row is left as it is: its Area is still on disk, so no drift is
   rolled back here (Part 39 Rule 39.41.6.1). The same pass confirms the calendar ledger's
   story-start reading (Part 41 Area 9, Resets, rewinds and housekeeping): the script has already
   emptied the recorded tables and the Current Position row of `ledger-worlds-calendar/_index.md`,
   which all sit under "Events Log" headings, and keeps its Baseline tables and its Planned
   windows table (no script change); an empty Current Position row means no Area is recorded and
   the story clock stands at Phase Day 1. The script has no `Total Entries` handling and is not
   edited for it, so this pass also sets the `Total Entries` header line of that file (and the
   five row counts it lists) to 0 by hand.
4. Recommend `/force-ledger-audit` afterward if Areas already exist, so the ledgers get rebuilt
   from what is actually on the page rather than staying blank while the text is ahead; for the
   calendar ledger that rebuild reads the first line of each written `.md`.

Part 38 note: `phase-section-part-chapter-area-specs/` is not a `ledger-*` folder, and
`--keep-specs` keeps it untouched regardless. No spec status rollback is needed here — the
written Areas are untouched, so spec statuses still match the written record.

## Failure/abort

Do not run without the confirming answer to the question in step 1 in the current turn;
Cancel, or any other answer, ends the command with nothing changed.
