---
description: "Revise one whole-built Chapter in place (a targeted change request): chapter-editor edits the written Chapter text, Gate 1 re-runs, the author confirms, the old pair is archived and the new pair is written with --overwrite."
argument-hint: "<chapter reference> <the change requested>"
user-invocable: true
---

# `/revise-chapter`

Corresponds to canon command `[REVISE CHAPTER]` (C-43). A targeted, in-place revision of one Chapter that was
built whole by `/create-chapter` (its Area rows read `WRITTEN(P.S.N.CCC)` and it has no Area files). It takes
**one change request**. It is not exempt from the audit pipeline because the Chapter was accepted before. To
discard and write the Chapter afresh, use `/redraft-chapter`. A Chapter built by Area is revised with
`/revise-area` (one Area) and is never touched by this command.

## Preconditions

- Read `.claude/guardrails/commands/guardrail-plan-then-auto-execution.md`,
  `.claude/guardrails/audit/guardrail-audit-gate-law.md`,
  `.claude/guardrails/tools/guardrail-authorized-scripts-only.md` and
  `.claude/guardrails/ledger/guardrail-story-spec-law.md`.
- **The Chapter must be whole-built.** The Chapter Spec's Build mode is `whole`, its Area rows read
  `WRITTEN(P.S.N.CCC)`, the Chapter file pair `Chapter NNN - <Name>.md` and `.docx` exists in the Novel-Part
  folder, and the Chapter folder holds no `area-NN` file. A Chapter with Area files is refused: name them and
  point to `/revise-area` (one Area) or `/redraft-chapter`. A Chapter that is not yet written is refused:
  point to `/create-chapter`.
- **The chain is in force** for the Chapter (Part 38 Rule 9.1.1): the Chapter Spec is `CONFIRMED` or
  `COMPLETED`, and its Novel-Part Spec and Section Spec each `CONFIRMED` or `COMPLETED` (status only, read
  from the registry `_index.md`). A `COMPLETED` Chapter Spec counts as in force for Check #18, and the Gate 2
  sync on it is a correction of record (Rules 6.1.1(a) and 9.7.1) that leaves its status as it is. A link
  that is missing, `DRAFT`, `AMENDED-PENDING-RECONFIRM` or `RETIRED` stops the command before Step 1: name
  the first missing link and `/section-spec`, `/part-spec` or `/chapter-spec`.
- **The change request.** One request, stated by the author with the command or asked for first. It must be
  clear enough to act on; an unclear request is asked, not guessed. A request that would break the Chapter
  Spec's plan (a change of beat, scene, viewpoint, ending or a settled item) is not absorbed: it goes to
  `/chapter-spec` (revise) first, and a request that spans more than one Chapter or more than one change is
  split by the author into separate invocations.
- Locate the Chapter's neighbours and name them: the Chapter before and the Chapter after, as written (a
  Chapter file, or the last or first Area file when a neighbour was built by Area). Where a scene runs across
  the Chapter's edge (the Scene Map's `Runs in from / out to`), say so plainly before anything is revised,
  because a revision can change how the scene joins at either edge.
- Read the Chapter Spec in full, the written Chapter `.md` (with its hidden markers), the calendar ledger's
  rows of the Chapter and its neighbours, and the ledger entries the request touches.

## Plan Mode to Auto Mode

The short check below, with the Chapter reference and the change request, is this command's **Plan Mode**,
concluded before Step 1: it asks only about open branches the requested change creates (a new name, a change
of scope), never pacing, size or stretch (the revised Chapter keeps the pacing, size targets and any named
stretch recorded in the Chapter Spec). Steps 1 to 6 then run in **Auto Mode**; Step 3's token is the
mandatory Gate 1 confirmation and is never waived.

Parallel orchestration (absolute binding): the Gate 1 grounding of the two **continuity-checker** instances
runs in the background while the chapter-editor edits; Gate 1's two instances run in parallel on the edited
text; the affected Gate 2 lanes in Step 5 run in parallel in one message. Editing is single: one
**chapter-editor**, one pass per round.

## Sequence

0. **Collective and location codes.** If the change request brings in a collective whose members appear
   together, or a location where two or more named people act, that is not in the written Chapter and whose
   Collective Behavior Code block reads `Not yet registered` or is missing, stop: it follows the step
   "Register new collective and location codes before drafting" of `/create-chapter` Step 0 (the
   outline-planner proposes, the author confirms through `AskUserQuestion`, the continuity-checker writes
   the block) before the chapter-editor starts. The editor never invents a code (Part 39 Rule 39.23.1.5).
1. **Edit (chapter-editor).** Invoke **one** chapter-editor on a staged copy of the written Chapter text
   (`.claude/temp/Chapter NNN - <Chapter Name>.md`, made by copying the written `.md` with its hidden
   markers), with the change request, the Chapter Spec, the neighbours' references and the calendar rows. It
   edits only the staged file, in one pass, and changes only what the request needs plus the seams that the
   change disturbs. It keeps every hidden `<!-- AREA NN -->` marker, in order and once each; it keeps the
   Chapter's date line first; the revised text stays inside the word band (each Area block 55% to 60% of its
   target, up to 72% only where the spec names a stretch; the Chapter total 0.55 T to 0.72 T). Where the
   request moves a scene in time, the new date must still meet the Chapter before and the Chapter after
   (Part 41 Area 6). Measure after the edit:
   `python .claude/tools/chapter_builder.py measure --mode whole --spec-file "<chapter spec path>" --text-file ".claude/temp/Chapter NNN - <Chapter Name>.md" --phase P --section S --part N --chapter C`.
   An out-of-band count or a marker fault is a blocking finding: back to the chapter-editor, measure again.
2. **Gate 1 on the whole revised Chapter** (not a diff-only check). **continuity-checker** runs as two
   read-only instances in parallel: the full **23 checks** adapted to the whole Chapter as `/create-chapter`
   Step 5 sets out (word-band check in place of Check #10; Check #18 per Area block and against the Scene
   Map; calendar by date segment; Checks #20, #21, #22 and, for each fight Area block, #23), and the **flow review** (Check #16 dimension 16-J)
   over the whole Chapter read with its two neighbours in order, so both edges are the **neighbour check**
   under the Area-to-Area carry-over rule. A break of time, place, point of view or character state at an
   edge or a seam FAILs. The instance also lists every fact the old text established that a later Chapter or
   Area cites, naming it; a revision that removes or changes one is put to the author as a question, after
   the Position Header and the full text are printed. A revision that alters a character's rendered conduct
   re-opens Check #21 (heroes and Tier A: the author rules each evolution; Tier B, C and D: the checker
   decides and records its reasons; an immutable always needs the author; evolution is not drift, Part 43).
   The Pre-Write Ledger Check and Check #14 read Living fields as they stood after the Chapter before this
   one, rebuilt from the Canon Events Log, whose rows cite Chapter references. If the cause of a finding lies
   in a neighbour, the revised Chapter is repaired first when that solves it; otherwise name the neighbour
   (Reference Code and name) and ask the author whether to run `/revise-chapter` or `/revise-area` on it
   first; if yes the pending revision is discarded as a `[SKIP WRITE]`. This first audit of the
   revised Chapter is full. On any FAIL: back to the chapter-editor (which returns its list of fixed lines,
   each pinned to its Area block, the old line and the new line quoted), re-measure, and re-audit until clean
   as `/create-chapter` Step 5 sets out for its FAIL loop (Author ruling, 2026-10-18): fixes only, plus the
   regression sweep, after a limited set of local fixes, and this step in full (both instances) where that
   rule calls for it. The author may stop the loop at any time and may order a full re-run.
3. **Present and confirm.** Print the Position Header Block (marked as a revision of the Chapter's Reference
   Code `P.S.N.CCC`, pacing and size carried from the spec), the **full text of the revised Chapter,
   verbatim** (never a summary, excerpt or file path; hidden markers shown as small `Area NN` labels), the
   measure figures against the band, the Contextual Earning Declaration, and the Post-Draft Audit Report with
   the neighbour-check result, one line on the FAIL loop where it ran (the first audit's FAIL checks, the mode
   of the re-audit and its result; Author ruling, 2026-10-18) and the plan-versus-written list; then wait for `[CONFIRM WRITE]` /
   `[REVISE CHAPTER]` / `[SKIP WRITE]`. The prompt says that `[CONFIRM WRITE]` replaces the written Chapter
   and that the previous pair will be kept in the archive. A question to the author about the revision is
   asked after the Position Header and the full text are printed. `[REVISE CHAPTER]` returns to Step 1 with
   the author's notes and re-runs Step 2 in full (a first full audit of the newly revised text; Author ruling, 2026-10-18); `[SKIP WRITE]` discards the revision and leaves the written
   Chapter, the ledger and the spec as they were.
4. **Archive and write.** On `[CONFIRM WRITE]`: first move the old `Chapter NNN - <Name>.md` and `.docx`
   pair, never deleting it, to `projects/novel-starward-saga/_archive/<YYYY-MM-DD_HHMM>/` keeping its path
   (a plain file move, as in a rewind; Part 2 Rule 5.3.2a), then write the revised pair at the same path with
   the script, with `--overwrite` (this command and `/redraft-chapter` are the only ones that pass it):
   `python .claude/tools/chapter_builder.py write --mode whole --spec-file "<chapter spec path>" --text-file ".claude/temp/Chapter NNN - <Chapter Name>.md" --output-root "<repo root>/projects/novel-starward-saga" --phase P --section S --part N --chapter C --chapter-name "<name>" --phase-name "<name>" --section-name "<name>" --novel-part-name "<name>" [--first-of-phase] [--first-of-section] [--phase-epigraph-file "<file>"] [--section-epigraph-file "<file>"] --overwrite`
   with the same `--first-of-*` flags and epigraph lines as the file being replaced, read by this command
   from Part 30 and the Section Spec as `/create-chapter` Step 7 sets out. Read the written pair back (the
   header block, the opening date line, the visible breaks, one marker per Area block in the `.md` and none
   in the `.docx`). If the script fails, stop as Failure/abort says.
5. **Affected Gate 2 lanes, in parallel (one message).** Launch only the lanes the revision touches, and
   always the audit:
   - **continuity-checker, Post-Write Audit only** (Completeness Indicator and Tier Scope Brackets; gets the
     read-back result; writes nothing).
   - **continuity-checker, ledger reconciliation** (`/force-ledger-audit` for what the revision changed, one
     batched update citing the Chapter reference only, `P.S.N.CCC`): entities, named items, Named Moves,
     monsters, Tier D rows, Check #21 rulings and Evolution Entries, Events Log rows, current conditions,
     and the calendar rows of the Chapter (recomputed where a date line changed, left as they are where not;
     the rollups and the Current Position block recomputed accordingly). It also carries the mandatory Part 38
     as-built sync on the Chapter Spec: Area rows stay `WRITTEN(P.S.N.CCC)`, the spec's status stays as it is
     (a `COMPLETED` Chapter Spec stays `COMPLETED`), the Signatures-fired rows are re-flipped per Area block
     from the markers, the variance and settlement notes record every accepted difference, and the
     Completion Record (Final Variance Summary, Reader now knows, Chapter digest) is refreshed from the
     revised text. Skip this lane only when the audit shows the revision changed nothing a ledger or the spec
     records; say so in the report.
   - **area-scorer:** re-score the Chapter (one CDL-2 block, replacing the prior contribution rather than
     adding to it, with the Voice and Variety block) and recompute the Section running aggregate.
6. **Clean up, log, report.** Delete the staged file in `.claude/temp/` (a plain delete). Write one line to
   `.claude/story-memory/session-log/` (the Chapter reference, the change requested in a few words, the
   outcome, the lanes run). Report the output paths, the word figures against the band, the archive folder,
   and what each lane changed.

## Failure/abort

A revision that fails Gate 1 is corrected and re-audited exactly like a fresh draft (the re-audit after the first full audit follows the gate law's section "Re-audit after fixes", Author ruling, 2026-10-18), never written through on
the strength of the original's prior approval. `[SKIP WRITE]` discards the revision: nothing is archived,
written or updated, and the staged file is deleted. An irreconcilable Gate 1 conflict is escalated through
`AskUserQuestion`.

A failed write (Step 4) stops the invocation: if the old pair was already moved to the archive and the new
write failed, move the old pair back to its path (a plain move) so the written Chapter stands as it was, run
no lane, show the author the script's message as it is, and wait. The staged text stays until the write
succeeds; the author re-issues `[CONFIRM WRITE]` once the cause is fixed.

## Rules

- Whole-built Chapters only; one change request and one Chapter per invocation; no Area file is ever
  written. The pair is written only by `chapter_builder.py` (authorized script 6) with `--overwrite`; the old
  pair is archived by a plain move first and never deleted.
- One chapter-editor edits; the area-maker is not used unless the author's request requires whole Area blocks
  to be redrafted, in which case the author is told and `/redraft-chapter` is the command.
- Every ledger, calendar, Events Log, Evolution, scoring and spec reference cites `P.S.N.CCC` only.
- `/revise-area` and `/next-area` refuse a whole-built Chapter; `/rewind-to` on one rewinds to the Chapter.
- Plain English, no emojis.
