---
description: Delete all written Areas in one Chapter only (the named Chapter, default the current one), then re-open it for a fresh draft. Destructive within scope. Human-invocation only.
argument-hint: <chapter reference, default the current Chapter>
user-invocable: true
disable-model-invocation: true
---

# `/reset-chapter`

Corresponds to canon command `[RESET CHAPTER]` (C-22). Scoped deletion — only the named
Chapter's Area files (`chapter-NNN/area-NN.docx` and `area-NN.md`; the current Chapter when
none is named) under `projects/novel-starward-saga/`. The Chapter's spec file **survives** the
reset (Part 38 reset rule), and so do the Novel-Part Spec and the Section Spec above it — they
are the plan the fresh draft is written against, with statuses rolled back per step 3.

## Sequence

1. Scope = the named Chapter (the current Chapter when none is named). First ask the author,
   through `AskUserQuestion` with a Cancel option, to commit or copy `projects/` and
   `story-memory/`; go on only when the author says that is done. These deletions run by hand,
   not through the script, so list, before asking, the files that will be deleted (this
   Chapter's Area files, its archived file pairs under
   `projects/novel-starward-saga/_archive/` and its exported files) with their counts. Then
   confirm through `AskUserQuestion` with a Cancel option which Chapter is being reset and that
   its Area files, its exported files and the archived file pairs of this Chapter will be
   deleted (state that its Chapter Spec survives, with Area statuses rolled back, and that its
   Novel-Part Spec and Section Spec survive too); the confirming answer names the scope in words
   (for example "Reset Chapter 12, 5 Areas, 2 archived pairs"), as
   `guardrails/commands/guardrail-command-law.md` requires.
2. Delete the Chapter's Area files, its exported files (the Chapter files `Chapter NNN - *.docx` and
   `Chapter NNN - *.md` in the Novel-Part folder, and the `phase-N-complete` and `starward-saga-complete` files that
   join its text, which would otherwise keep the discarded text, Part 2 Rule 5.3.5) and the
   archived file pairs of this Chapter under `projects/novel-starward-saga/_archive/`.
3. Invoke **continuity-checker** to run `/force-ledger-audit` afterward, since deleted Areas
   may leave ledger entries referencing content that no longer exists — reconcile rather than
   leave stale. A behavioral drift whose Area was deleted is undone the same way (Part 39 Rule
   39.41.6.1): its Section 12 entry is marked `rolled back`, never deleted, and a Permanent
   drift's prior value returns to Section 11 from the superseded-behaviors table. The calendar
   ledger rolls back with it (Part 41 Area 9, The calendar ledger, resets and rewinds): the
   Chapter's row and its Area rows in `ledger-worlds-calendar/_index.md` are
   removed, the Novel-Part, Section and Phase rollups are recomputed from the rows that remain,
   and the Current Position block is rewritten from the last surviving Area; the Baseline tables
   are not touched. The same reconcile step also performs the Part 38 Rule 7.2.1 rollback in
   full (statuses, name tags, reference stamps): the Chapter's spec file is kept, and its Area
   blocks roll back to match what survives (`WRITTEN` → `PLANNED`, each with a variance note
   recording the reset; the pacing and size target the spec records stay). The `COMPLETED` rollback (Part 38 Rule 9.8.1), the variance note, the built-against stamps and the Coverage-cell refresh are stated once, in `/force-ledger-audit` under "Gate 2 and destructive-command invocations" (Part 38 Rules 1.2.2, 10.1.2 and 11.1.2); this command adds only its scope: the Novel-Part Spec and the Section Spec above the Chapter are not rolled back block by block, and the Section and Novel-Part Coverage cells above this Chapter are refreshed. Specs of other Chapters are not touched.
4. Invoke **area-scorer** — launched together with Step 3, since the two write disjoint
   files — to remove the scores of the deleted Areas from the CDL-2 tracker
   (`.claude/story-memory/cdl2-density-tracking/`). Pass it the references of the deleted
   Areas: their per-Area rows are removed and the Section running aggregate is recomputed.

## Whole-built Chapters

A Chapter built whole by `/create-chapter` (Build mode `whole`; Area rows `WRITTEN(P.S.N.CCC)`) has no Area
files. Its reset deletes the Chapter file pair (`Chapter NNN - <Name>.md` and `.docx` in the Novel-Part
folder), the `phase-N-complete` and `starward-saga-complete` files that join its text, and the archived
copies of that Chapter file pair under `projects/novel-starward-saga/_archive/`; the listing and the
confirming question name the Chapter file pair, for example "Reset Chapter 2, 1 file pair, 1 archived pair".
Step 3 reconciles every row citing the Chapter reference `P.S.N.CCC`; the Chapter Spec survives with its Area
rows rolled back from `WRITTEN(P.S.N.CCC)` to `PLANNED` (variance note recording the reset; pacing, size
targets, Scene Map and stretch stay). Step 4 removes the Chapter's single CDL-2 block. The Chapter is
afterwards written again by `/create-chapter`.

## Failure/abort

Do not run without the confirming answer that names the Chapter in scope; Cancel, or any
other answer, ends the command with nothing changed.

A reset can stop after Step 2 and before Step 3 is done: the author declines the
reconciliation preview, the audit stops at `NEW ENTITY TYPE`, or the run is interrupted. The
Areas are then deleted while the ledgers, spec blocks and scores still show them. This state is
named *deleted, not reconciled*. Re-run `/reset-chapter` with the same Chapter: Step 2 is
skipped for files already deleted, and Step 3 runs again, with Step 4 launched alongside it
as before.
