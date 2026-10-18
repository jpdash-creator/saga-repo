---
description: Reset written Areas/output AND all story-memory ledgers via `.claude/tools/reset_story.py --keep-specs --keep-agent-memory`. Every spec (Section Spec, Novel-Part Spec and Chapter Spec) survives with statuses rolled back (Part 38); agent memory and the canon layer are untouched. Destructive to written Areas and ledger data. Human-invocation only.
user-invocable: true
disable-model-invocation: true
---

# `/reset-story`

Corresponds to canon command `[RESET STORY]` (C-21). It runs the one authorized reset
script with the two flags that define this command's scope:

```
.claude/tools/reset_story.py --keep-specs --keep-agent-memory
```

The written Areas under `projects/novel-starward-saga/` (`chapter-NNN/area-NN.docx` and
`area-NN.md`) are cleared, and every `story-memory/ledger-*/` file is cleaned of its story
record — Canon Events Logs emptied, Area-reference citations and anchor fields stripped,
descriptive content kept. **No ledger entity file is deleted**, side-character files included.
The CDL-2 density tracker (`story-memory/cdl2-density-tracking/`) holds scores for the Areas
being cleared and is not touched by the script, so **area-scorer** returns it to its empty
template (Step 2).

## Scope versus `/hard-reset`

| | `/reset-story` (Command C-21) | `/hard-reset` (Command C-1) |
|---|---|---|
| Written Areas, ledgers, density tracker scores | cleared | cleared |
| Specs (Section Specs, Novel-Part Specs, Chapter Specs) | **survive**, statuses rolled back | all three kinds deleted |
| Session log (`story-memory/session-log/`, `README.md` kept) | deleted | deleted |
| Agent memory | **untouched** | wiped |

Part 38 reset rule: every spec, of all three kinds, **survives** this reset (Rule 7.1.1).
`--keep-specs` is what enforces that, and the script prints a reminder that the status rollback
is owed by this command rather than done for it. Only `[HARD RESET]` deletes specs (Rule 7.1.2).

## Sequence

1. Confirm before running, as `guardrails/commands/guardrail-command-law.md` requires of a
   destructive command. First ask the author, through `AskUserQuestion` with a Cancel option,
   to commit or copy `projects/` and `story-memory/`; go on only when the author says that is
   done. Then run `.claude/tools/reset_story.py --dry-run --keep-specs --keep-agent-memory`,
   which writes nothing and prints every file it would remove or clean (its lines still read
   `deleted:` and `cleaned:`), and show the author its counts: Area files, archived pairs and
   exported files (the paths under `_archive` are archived files, two to a pair; exported files
   are marked) and ledger files. Then state plainly: all Area files under
   `projects/novel-starward-saga/` (the `_archive` folder included) and every exported chapter,
   phase and novel file (the Novel-Part-folder Chapter files `Chapter NNN - *.docx` / `.md`, `phase-N-complete.docx` / `.md`,
   `starward-saga-complete.docx` / `.md`) will be removed; every `story-memory/ledger-*/` file
   will have its story record cleared while keeping its descriptive content; every file in `story-memory/session-log/` (`README.md` kept) will be deleted; and the density
   scores in `story-memory/cdl2-density-tracking/` will be cleared — while canon skills,
   guardrails, `.claude/canon-manifest/`, agent memory, and every spec (Section, Novel-Part and
   Chapter) are left in place, the specs with a post-run status rollback. Ask through
   `AskUserQuestion` with a Cancel option; the confirming answer names the scope in words (for
   example "Reset story: all Areas, all ledger records, the session log, density scores; specs kept").
2. Run `.claude/tools/reset_story.py --keep-specs --keep-agent-memory`. The script does not
   touch the CDL-2 density tracker, so also invoke **area-scorer** (the tracker's sole
   writer), launched together with the Step 3 calls, to return
   `story-memory/cdl2-density-tracking/` to its empty template: every per-Area score,
   aggregate and history row removed, Status OPEN.
3. Resolve the script's REVIEW REQUIRED report: it prints every ledger line where it could
   not separate a descriptive fact from its Area citation, and leaves those lines untouched.
   Invoke **continuity-checker** in parallel, one call per affected file, to resolve them by
   hand — keep the fact, drop the provenance. The same pass clears Section 12 of every
   character ledger (Part 39 Rule 39.41.6.2): each Permanent drift's prior value first returns
   to Section 11 from the superseded-behaviors table, and only then are the log, the Deferred
   table and the superseded-behaviors table emptied to their headers. The same pass returns the
   calendar ledger to its story-start reading (Part 41 Area 9, Resets, rewinds and
   housekeeping): the script has already emptied the recorded tables and the Current Position row
   of `ledger-worlds-calendar/_index.md`, which all sit under "Events Log" headings, and keeps
   its Baseline tables and its Planned windows table (no script change). An empty Current
   Position row is the story-start reading: no Area written, the story clock at Phase Day 1
   (Year 1247, Ilovany, Orvil, Day 1). The script has no `Total Entries` handling and is not
   edited for it, so this pass also sets the `Total Entries` header line of that file (and the
   five row counts it lists) to 0 by hand. The pass confirms the emptied Events Log tables, the 0 on
   that line and that the Baseline tables are intact.
4. Part 38 spec rollback (this flow has no `/force-ledger-audit` step of its own, so it is an
   explicit step): invoke **continuity-checker** to perform the Part 38 Rule 7.2.1 rollback in
   full (statuses, name tags, reference stamps) on every Chapter Spec, to match the now-empty
   written record (`WRITTEN`/`DRAFTED` → `PLANNED`, each Area block with a variance note
   recording the reset; the pacing and size target the spec records stay). The `COMPLETED` rollback (Part 38 Rule 9.8.1), the variance note, the built-against stamps and the Coverage-cell refresh are stated once, in `/force-ledger-audit` under "Gate 2 and destructive-command invocations" (Part 38 Rules 1.2.2, 10.1.2 and 11.1.2); this command adds only its scope: every `COMPLETED` Novel-Part Spec and Section Spec returns to `CONFIRMED`, because every Area is gone, and the Coverage cells of all three registry tables are refreshed. A spec that is `DRAFT`, `AMENDED-PENDING-RECONFIRM` or `RETIRED` keeps that status, and settled answers survive (Rule 7.2.2).

## Failure/abort

Do not run without the confirming answer to the question in step 1 in the current turn;
Cancel, or any other answer, ends the command with nothing changed.
