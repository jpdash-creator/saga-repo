---
description: Full wipe -- clears all written Areas, deletes every spec (Section Specs, Novel-Part Specs and Chapter Specs), empties every ledger's event log while keeping its description, and wipes agent memory. Ledger entity files are never deleted. Destructive. Human-invocation only.
user-invocable: true
disable-model-invocation: true
---

# `/hard-reset`

Corresponds to canon command `[HARD RESET]` (Command C-1), executed via the sole authorized
`reset_story.py` (`.claude/guardrails/tools/guardrail-authorized-scripts-only.md`). This is
the most destructive command in the system — it may only be triggered by an explicit human
`/hard-reset` invocation, never inferred or auto-run by any agent.

## What it does and does not destroy

The governing idea is that **the ledger keeps describing the world; it stops recording the
story.** Everything that says what an entity *is* survives. Everything that records which
Area established it does not.

| Destroyed | Kept |
|---|---|
| All Area files (`chapter-NNN/area-NN.docx` and `area-NN.md`) under `projects/novel-starward-saga/` (the `_archive` folder included) | Phase and Section icon files, and the folders holding them |
| Every exported file that holds that text: the Chapter files `Chapter NNN - <Chapter Name>.docx` / `.md` in the Novel-Part folders, `phase-N-complete.docx` / `.md`, `starward-saga-complete.docx` / `.md` (Part 2 Rule 5.3.5) | Nothing; `/chapter-builder` and `/compile-phase` make them again from new Areas |
| Every spec file of all three kinds: `section-N-spec.md`, `part-N-spec.md` (the Novel-Part Spec) and `chapter-NNN-spec.md` (Part 38 Rule 7.1.2) | The specs `_index.md`, emptied to its three registry tables' headers |
| Every Canon Events Log row in every ledger, and every Section 12 (Behavioral Evolution Log) entry in every character ledger | The Canon Events Log heading and table header; the Section 12 headers; Section 11 as registered |
| Every Area-reference citation and anchor field in every ledger | Every descriptive value those citations annotated |
| Every recorded row of the calendar ledger `ledger-worlds-calendar/_index.md` (its Phase, Section, Novel-Part, Chapter and Area tables and its Current Position row, which all sit under "Events Log" headings, and its `Total Entries` header line, set to 0 by the ledger pass) | The Baseline tables (epoch, months, weekdays and formula, fixed days, birth years) and the Planned windows table; an empty Current Position row is the story-start reading (Part 41 Area 9) |
| Every file in `.claude/story-memory/session-log/` is deleted | `README.md` of that folder |
| All `.claude/agent-memory/` note files | Each agent's `MEMORY.md`, emptied to its header |
| Every score in the CDL-2 density tracker (`.claude/story-memory/cdl2-density-tracking/`: per-Area rows, aggregate, history) | The tracker file, returned to its empty template with Status OPEN |

**No ledger entity file is ever deleted** — including side-character files, which exist only
because the story created them. They keep their descriptive content and lose their provenance,
exactly like every other ledger file.

## Sequence

1. **Confirm before running anything**, as `guardrails/commands/guardrail-command-law.md`
   requires of a destructive command. First ask the author, through `AskUserQuestion` with a
   Cancel option, to commit or copy `projects/` and `story-memory/`; go on only when the
   author says that is done. Then run `.claude/tools/reset_story.py --dry-run`, which writes
   nothing and prints every file it would remove or clean (its lines still read `deleted:` and
   `cleaned:`), and show the author the counts it implies: Area files, archived pairs and
   exported files (the paths under `_archive` are archived files, two to a pair; exported files
   are marked), specs (the `section-N-spec.md`, `part-N-spec.md` and `chapter-NNN-spec.md` files
   inside the `phase-N` folders that the script's spec step lists, counted by kind: the dry run
   prints only the top-level `phase-N` folders, so count the spec files yourself) and ledger
   files. Then state plainly what will be erased, using the table above and those counts, and ask
   through `AskUserQuestion` with a Cancel option; the confirming answer names the scope in words
   (for example "Hard reset: all Areas, every Section, Novel-Part and Chapter spec, every ledger
   log, the session log, all agent memory"). Do not proceed on an inferred or implied yes.
2. Run `.claude/tools/reset_story.py`. Its steps cover every row of that table except the
   last, apart from the Section 12 entries, which Step 3 clears. The script's spec step sweeps the
   whole specs folder except `_index.md`, so Section Specs and Novel-Part Specs go with the
   Chapter Specs, and it empties every table in `_index.md`, which leaves the three registry
   tables with headers only. It never touches `.claude/skills/`, `guardrails/`,
   `canon-manifest/`, `agents/`, `commands/`, `docs/`, or `tools/`. The last row of the table,
   the CDL-2 density tracker, is not touched by the script either: invoke **area-scorer** (the
   tracker's sole writer), launched together with the Step 3 calls, to return
   `story-memory/cdl2-density-tracking/` to its empty template, with every per-Area score,
   aggregate and history row removed and Status OPEN.
3. **Resolve the script's REVIEW REQUIRED report.** The cleaner deliberately refuses to
   touch any line where it cannot separate a descriptive fact from its Area citation, and
   prints those lines instead. Invoke **continuity-checker** — in parallel, one call per
   affected ledger file — to resolve them by hand: keep the fact, drop the provenance,
   delete blocks that are purely bookkeeping of what was written. A regex must never be allowed
   to mangle a descriptive sentence, which is why this step exists rather than a more
   aggressive script. The same pass clears Section 12 of every character ledger (Part 39 Rule
   39.41.6.2): each Permanent drift's prior value first returns to Section 11 from the
   superseded-behaviors table, and only then are the log, the Deferred table and the
   superseded-behaviors table emptied to their headers. The same pass confirms the calendar
   ledger's story-start reading (Part 41 Area 9): the script has already emptied the recorded
   tables and the Current Position row of `ledger-worlds-calendar/_index.md` (no script change),
   and an empty Current Position row means no Area is recorded and the story clock stands at
   Phase Day 1, Year 1247, Ilovany, Orvil, Day 1. The script has no `Total Entries` handling and
   is not edited for it, so this pass also sets the `Total Entries` header line of that file (and
   the five row counts it lists) to 0 by hand.
4. **Verify.** Re-grep the ledger tree for Area references (the pattern is five dot-separated
   numeric groups, Phase.Section.Novel-Part.Chapter.Area). The expected count is zero. Report
   the count.
5. **Stop.** The command ends at a verified clean baseline. It does **not** chain into
   `/start-story` — that is a separate, explicit author invocation (rebuilding the spec chain,
   which is Section Spec 1.1, then Novel-Part Spec 1.1.1, then Chapter Spec 1.1.1.001, and
   drafting Area 1 is creative work the author should choose to begin, not a side effect of a
   wipe). Because every spec is gone, the next `/start-story` is a fresh build of all three.

## Failure/abort

Do not run without an explicit, unambiguous human confirmation in the current turn (the
confirming answer to the question in step 1); Cancel, or any other answer, ends the command
with nothing changed. If the script reports a directory it could not remove (Windows and
OneDrive both hold directory handles briefly), that is not a failure — the files inside are
gone; note it and continue.
