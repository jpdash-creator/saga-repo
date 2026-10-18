---
description: Roll the story back to the end of a specific prior Area, Chapter or Section, archiving everything written after it as non-canonical. Destructive. Human-invocation only.
argument-hint: <area reference | chapter reference | section reference>
user-invocable: true
disable-model-invocation: true
---

# `/rewind-to`

Corresponds to canon command `[REWIND TO: ref]` (C-16).

## Sequence

1. Resolve the level first, then confirm. The target is an Area reference
   (`Phase.Section.Novel-Part.Chapter.Area`), a Chapter reference or a Section reference. An Area
   target keeps that Area whole and archives every Area written after it; a Chapter or Section
   target means the last Area of that Chapter or Section. If the target Area sits inside a
   scene that continues into the next Area (the Area-to-Area carry-over rule), warn that the
   scene would be left open at that Area, and that it must be continued with `/next-area` or
   written afresh before the story moves on. Then confirm through `AskUserQuestion` with a
   Cancel option the final target reference, stating plainly which Area files will be archived
   as non-canonical (everything after that reference); the confirming answer names the scope in
   words (for example "Rewind to Chapter 12, Area 3; 5 Areas archived", or "Rewind to the end
   of Chapter 11: Chapter 11, Area 4; 5 Areas archived"), as
   `guardrails/commands/guardrail-command-law.md` requires.
2. Archive the Area files after the target reference as non-canonical pending revision: move
   them, never delete them, to `projects/novel-starward-saga/_archive/<date-time>/`, keeping
   their path below `projects/novel-starward-saga/` (Part 2 Rule 5.3.2a in
   `narration-novel-book-structure-law` Area 5; each Area is a coupled `area-NN.docx` and
   `area-NN.md` pair). New text written forward creates fresh file pairs at those positions.
   `/restore-archive <date-time>` is the way back: it moves the pairs to their paths again and
   brings the ledgers, spec blocks and scores back in line.
3. Invoke **continuity-checker** to run `/force-ledger-audit`, reconciling every ledger back
   to the state implied by the Areas up through the target reference only — Living (L) fields
   that were only established by now-archived Areas must be rolled back too, not left ahead
   of the actual story. A behavioral drift whose Area is now archived is undone the same way
   (Part 39 Rule 39.41.6.1): its Section 12 entry is marked `rolled back` and never deleted,
   and a Permanent drift's prior value returns to Section 11 from the superseded-behaviors
   table. The calendar ledger rolls back the same way (Part 41 Area 9, The calendar ledger,
   resets and rewinds): the Area rows of the archived Areas are removed, the
   Chapter, Novel-Part, Section and Phase rows are recomputed from the rows that remain, and
   the Current Position block is rewritten from the last surviving Area, its date and its Phase
   Day; the Baseline tables (epoch, months, weekdays, fixed days, birth years, planned windows)
   are not touched. The same reconcile step also performs the Part 38 spec rollback: every spec,
   of all three kinds (Section Spec, Novel-Part Spec and Chapter Spec), **survives** the rewind,
   and every Area block of a Chapter Spec after the target reference rolls back to match the
   surviving record (`WRITTEN` → `PLANNED`, each with a variance note recording the rewind);
   blocks at or before the reference keep their statuses, and the pacing and size target the
   spec records stay (a Chapter's status is re-derived from its blocks; Part 38 Rules 2.4.9 and
   7.2.1). The `COMPLETED` rollback (Part 38 Rule 9.8.1), the variance note, the built-against stamps and the Coverage-cell refresh are stated once, in `/force-ledger-audit` under "Gate 2 and destructive-command invocations" (Part 38 Rules 1.2.2, 10.1.2 and 11.1.2); this command adds only its scope: a Chapter Spec none of whose blocks roll back keeps its status, a rewind to a Chapter or Section reference needs no special case, and a spec that ends at or before the target keeps its status.. Invoke
   **area-scorer** to remove the scores of the archived Areas from the CDL-2 tracker (per-Area
   rows) and recompute the Section running aggregate. Ledger rows and entity files whose first
   appearance is in archived Areas are listed in the reconciliation preview for removal or an
   `archived` note in their Status field, the form being the author's to choose at the preview;
   none is removed without the author's confirmation. A spec reference stamp that cites an
   archived Area reverts to its unstamped form (Part 38 Rule 7.2.1).

## Whole-built Chapters

A Chapter built whole by `/create-chapter` (Build mode `whole`; Area rows `WRITTEN(P.S.N.CCC)`) has no Area
files and cannot be rewound to an Area: an Area reference inside it is refused with "Chapter P.S.N.CCC was
built whole; rewind to the Chapter (keep it whole) or to the Chapter before it". The unit is the Chapter
file pair (`Chapter NNN - <Name>.md` and `.docx` in the Novel-Part folder). Rewinding **to** a whole-built
Chapter keeps it whole and archives every later Chapter file pair and Area file; rewinding to an earlier
point archives the Chapter file pair of each whole-built Chapter after the target, by the same plain move to
`projects/novel-starward-saga/_archive/<date-time>/` keeping its path. In Step 3 the reconciliation treats
every row citing an archived Chapter reference as non-canonical, the Chapter Spec's Area rows of an
archived whole-built Chapter roll back from `WRITTEN(P.S.N.CCC)` to `PLANNED` with a variance note, and
area-scorer removes that Chapter's single CDL-2 block. The confirming answer names the scope in words, for
example "Rewind to the end of Chapter 2; Chapter 3 (whole-built, 1 file pair) archived".

## Failure/abort

Do not run without an explicit, unambiguous target reference confirmed by the user through
that question; Cancel, or any other answer, ends the command with nothing changed.

A rewind can stop after Step 2 and before Step 3 is done: the author declines the
reconciliation preview, the audit stops at `NEW ENTITY TYPE`, or the run is interrupted. The
Areas are then archived while the ledgers, spec blocks and scores still show them. This state
is named *moved, not reconciled*. Re-run `/rewind-to` with the same target reference: Step 2 is
skipped for files already moved, and Step 3 runs again.
