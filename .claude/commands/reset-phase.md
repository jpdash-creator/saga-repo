---
description: Delete all written Areas in a given Phase only, then re-open it for a fresh draft. Destructive within scope. Human-invocation only.
argument-hint: <phase number>
user-invocable: true
disable-model-invocation: true
---

# `/reset-phase`

Corresponds to canon command `[RESET PHASE: N]` (C-23). Scoped deletion — only the named
Phase's Area files (all its Sections/Novel-Parts/Chapters, `chapter-NNN/area-NN.docx` and
`area-NN.md`) under `projects/novel-starward-saga/phase-N/`.

## Sequence

1. First ask the author, through `AskUserQuestion` with a Cancel option, to commit or copy
   `projects/` and `story-memory/`; go on only when the author says that is done. These
   deletions run by hand, not through the script, so list, before asking, the files that will be
   deleted (this Phase's Area files, its archived file pairs under
   `projects/novel-starward-saga/_archive/` and its exported files) with their counts. Then
   confirm through `AskUserQuestion` with a Cancel option which Phase number is being reset and
   that all its Area files, its exported files and their archived file pairs will be deleted; the
   confirming answer names the scope in words (for example "Reset Phase 1, 63 Areas, 9 archived
   pairs"), as `guardrails/commands/guardrail-command-law.md` requires.
2. Delete `projects/novel-starward-saga/phase-N/` Area files, its exported files (every
   Chapter file `Chapter NNN - *.docx` / `.md` in its Novel-Part folders and `phase-N-complete.docx` / `.md`, and
   `starward-saga-complete.docx` / `.md`, which joins this Phase's text; Part 2 Rule 5.3.5) and
   the archived file pairs of this Phase under `projects/novel-starward-saga/_archive/` (phase-icon and section-icon files are never deleted by this command).
3. Invoke **continuity-checker** to run `/force-ledger-audit` afterward to reconcile ledgers
   against the now-shorter written record. A behavioral drift whose Area was deleted is undone
   the same way (Part 39 Rule 39.41.6.1): its Section 12 entry is marked `rolled back`, never
   deleted, and a Permanent drift's prior value returns to Section 11 from the
   superseded-behaviors table. The calendar ledger rolls back with it (Part 41 Area 9, The
   calendar ledger, resets and rewinds): every recorded row of the Phase in
   `ledger-worlds-calendar/_index.md` (its Section, Novel-Part, Chapter and Area rows)
   is removed, the Phase row is recomputed, and the Current Position block is rewritten from the
   last surviving Area, or returned to its starting state when none survives; the Baseline
   tables (epoch, months, weekdays, fixed days, birth years, planned windows) are not touched.
   The same reconcile step also performs the Part 38 Rule 7.2.1 rollback in full (statuses, name
   tags, reference stamps): the Phase's Section Specs, Novel-Part Specs and Chapter Specs all
   **survive** the reset (Part 38 Rule 7.1.1 — only `/hard-reset` deletes a spec), and every
   affected Chapter Spec's Area blocks roll back to match what survives (`WRITTEN` → `PLANNED`,
   each with a variance note recording the reset; the pacing and size target the spec records
   stay). The `COMPLETED` rollback (Part 38 Rule 9.8.1), the variance note, the built-against stamps and the Coverage-cell refresh are stated once, in `/force-ledger-audit` under "Gate 2 and destructive-command invocations" (Part 38 Rules 1.2.2, 10.1.2 and 11.1.2); this command adds only its scope: every Chapter Spec of the Phase whose Area blocks roll back, and every Novel-Part Spec and Section Spec of the Phase, follows it; a spec that is `DRAFT`, `AMENDED-PENDING-RECONFIRM` or `RETIRED` keeps that status.
4. Invoke **area-scorer** — launched together with Step 3, since the two write disjoint
   files — to remove the scores of the deleted Areas from the CDL-2 tracker
   (`.claude/story-memory/cdl2-density-tracking/`). Pass it the references of the deleted
   Areas: their per-Area rows are removed and each Section's running aggregate is recomputed.

## Failure/abort

Do not run without the confirming answer that names the Phase in scope; Cancel, or any
other answer, ends the command with nothing changed.

A reset can stop after Step 2 and before Step 3 is done: the author declines the
reconciliation preview, the audit stops at `NEW ENTITY TYPE`, or the run is interrupted. The
Areas are then deleted while the ledgers, spec blocks and scores still show them. This state is
named *deleted, not reconciled*. Re-run `/reset-phase` with the same Phase number: Step 2 is
skipped for files already deleted, and Step 3 runs again, with Step 4 launched alongside it
as before.
