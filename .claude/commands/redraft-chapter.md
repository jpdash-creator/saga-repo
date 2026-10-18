---
description: Discard and completely redraft an entire Chapter, Area by Area. Destructive within scope. Human-invocation only.
argument-hint: <chapter reference, default the current Chapter>
user-invocable: true
disable-model-invocation: true
---

# `/redraft-chapter`

Corresponds to canon command `[REDRAFT CHAPTER]` (C-30). Same discipline as `/redraft-area`
but scoped to the whole named Chapter (the current Chapter when none is named).

## Preconditions

- Read `.claude/guardrails/commands/guardrail-plan-then-auto-execution.md` (Plan Mode →
  Auto Mode sequencing, default model/effort, mandatory parallelism, milestone progress
  reports — governs this command's execution shape end to end).
- The spec chain must be in force for the Chapter: its Novel-Part Spec and its Section Spec
  are `CONFIRMED` or `COMPLETED`. Step 1 is a `/chapter-spec` revise flow, which refuses to
  run under a parent spec that is `DRAFT`, `AMENDED-PENDING-RECONFIRM` or `RETIRED`
  (Part 38 Rule 9.1.1).

## Whole-built Chapters

If the Chapter's Build mode after Step 1 is `whole`, the redraft goes through `/create-chapter`, not `/next-area`.
This holds whether the Chapter was built whole (Area rows `WRITTEN(P.S.N.CCC)`, no Area files) or was first written Area by
Area and the author has changed it to `whole` (Amended 2026-10-07, for example Chapter 002): then Step 2 archives the
Chapter's per-Area files, not a file pair, as the Area-built steps below say, and Step 3 is one `/create-chapter` run. The steps below change as follows. Step 1 is
unchanged (the `/chapter-spec` revise flow, which may re-cut the Area blocks and the Scene Map). Step 2
archives the Chapter file pair (`Chapter NNN - <Name>.md` and `.docx` in the Novel-Part folder, a plain move
to `projects/novel-starward-saga/_archive/<YYYY-MM-DD_HHMM>/` keeping its path; there are no Area files) and
runs the same `/force-ledger-audit` reconciliation, in which every row and entity citing the Chapter
reference `P.S.N.CCC` is treated as non-canonical, the Chapter's calendar rows are removed and recomputed,
the Area rows of the Chapter Spec roll back to `PLANNED` with variance notes (a `COMPLETED` spec returns to
`CONFIRMED`, as below), and **area-scorer** removes the Chapter's single CDL-2 block. Step 3 is one run of
`/create-chapter` for the Chapter (its own Plan Mode and its own Gate 1 token), not a series of `/next-area`
cycles; the archive is done first, so its write needs no `--overwrite`. Step 4 is unchanged. The scope
confirmation names the Chapter file pair, for example "Redraft Chapter 2, whole-built, 1 file pair archived".
A Chapter whose Build mode stays `by-area` is redrafted as written below, by `/next-area`.

## Plan Mode → Auto Mode

The scope confirmation in Failure/abort — confirming this is exactly the intended Chapter —
opens this command's own **Plan Mode**, and Step 1's `/chapter-spec` revise consultation
(with its `[CONFIRM SPEC]` gate, and the question about the Novel-Part Spec entry that Step 1
describes) completes it: both are resolved before Step 2 archives anything. Once resolved,
Steps 2-4 run in **Auto Mode** with no further discretionary questions. Auto Mode never waives
a mandatory gate: each `/next-area` cycle launched in Step 3 carries its own nested Plan
Mode/Auto Mode (its own Decision Consultation Gate) and its own Gate 1 `[CONFIRM WRITE]` token,
exactly as documented in `next-area.md` — not duplicated here
(`guardrails/commands/guardrail-plan-then-auto-execution.md`). Pacing is not asked again: the
Chapter Spec's pacing value for each Area (as revised in Step 1) is carried.

Within any single `/next-area` cycle, independent steps must still run in parallel per the
guardrail — but the one-cycle-at-a-time law in Step 3 is untouched: cycles themselves stay
strictly sequential, one Area at a time through the Chapter, never batched. Each cycle starts
by reading the Area before it (the Area just rewritten in this redraft, or the last Area of the
Chapter before); the earlier Area is read, never batched.

## Sequence

1. Scope = the named Chapter (the current Chapter when none is named). Re-open the
   Chapter's spec via the `/chapter-spec` **revise** flow (Part 38) — full author consultation
   through `[CONFIRM SPEC]`, with **outline-planner** re-confirming the Chapter's Area-by-Area
   plan inside that flow (the redraft may be happening precisely because the original spec
   didn't work). Each Area's block is re-opened with it (scene anchors, size target of 1,600,
   1,800 or 2,000 words, pacing, opening and closing type, carry-over, thread), so Areas may be
   re-cut and the number of Areas may differ from the Chapter as first written. The revised
   spec is the redraft plan; its Area blocks are still `WRITTEN` while it is agreed, and Step
   2 rolls them back. A spec is a living record, so a `COMPLETED` Chapter Spec is revised like
   any other and nothing extra is asked about it (Part 38 Rule 9.7.1). A substantial revision
   (Part 38 Rule 3.5.2) sets the spec to `AMENDED-PENDING-RECONFIRM` until `[CONFIRM SPEC]` and
   `CONFIRMED` afterwards, and a light one (pacing, size target, variance note) leaves the status;
   a redraft that keeps the plan unchanged needs
   no amendment (Part 38 Rule 7.3.1) and leaves the spec as it is, with one variance line. If
   the Chapter's Novel-Part Spec or Section Spec is not `CONFIRMED` or `COMPLETED`, the
   revise is refused before anything is archived, and the refusal names the command to run
   (`/part-spec` or `/section-spec`).
   **The Novel-Part Spec entry.** The Chapter's entry in its Novel-Part Spec is the plan
   baseline. If the revised plan departs from what that entry fixes — purpose, calendar window,
   threads in and out, who is on the page, key events, reveals owed, opening hook or closing
   beat (Part 38 Rule 9.3.3) — the departure is shown at this flow's confirm step, and the
   author is asked, for each departure, whether to amend the plan (the Novel-Part Spec entry is
   then changed through `/part-spec revise`, a light amendment when only that entry changes,
   Part 38 Rule 11.4.2) or to leave the original entry as the plan baseline. Either way the
   departure is recorded as a variance note on every spec above the Chapter Spec, written
   top-down in one step at this flow's `[CONFIRM SPEC]`: the Section Spec first, then the
   Novel-Part Spec, and the Chapter Spec is updated after them (Part 38 Rules 9.4.5 and
   11.4.2). Each note is light: it changes no plan content, and the plan content of the
   Novel-Part Spec or the Section Spec changes only through that spec's own command. Re-cutting,
   splitting, merging or renaming Areas, and a different number of Areas, are the Chapter
   Spec's own business and no departure. The question is asked here and not again later.
2. **Go back first, as a rewind to the end of the previous Chapter does**: move the Chapter's
   existing per-Area files (`chapter-NNN/area-NN.docx` and `area-NN.md`), never delete them, to
   `projects/novel-starward-saga/_archive/<date-time>/` keeping their path (Part 2 Rule 5.3.2a; the
   redraft archives first, so its fresh writes need no `--overwrite`, which only `/revise-area`
   passes); invoke **continuity-checker** to run
   `/force-ledger-audit` as the reconciliation pass with the archived Areas treated as
   non-canonical (Living fields that only the archived Areas established roll back, and so
   does a behavioral drift whose Area is archived, under Part 39 Rule 39.41.6.1: its
   Section 12 entry is marked `rolled back`, never deleted, and a Permanent drift's prior
   value returns to Section 11 from the superseded-behaviors table; the Chapter's calendar rows
   (its Chapter row and Area rows) are removed, the Novel-Part, Section and
   Phase rollups and the Current Position block (the Open Chapter and the Open Chapter's recorded
   window, First to Latest) of `ledger-worlds-calendar/_index.md` are
   recomputed from the rows that remain (Part 41 Area 9, The calendar ledger, resets and
   rewinds); the Chapter's Area blocks roll back to `PLANNED` with variance notes recording the
   redraft, and each Area's pacing value, which the Chapter Spec records, stays as it is;
   the Chapter Spec, if it is `COMPLETED`, returns to
   `CONFIRMED` with its completion text kept as history, and a `COMPLETED` Novel-Part Spec or
   Section Spec above it returns to `CONFIRMED` with it (statuses only; Part 38 Rules 7.2.1 and
   9.8.1); registry refreshed, including the Coverage cell of every Novel-Part Spec row and
   Section Spec row above the Chapter whose figures changed (Part 38 Rules 10.1.2 and
   11.1.2); rows and entity files whose first appearance is in the archived Areas are listed in
   the preview as `/rewind-to` Step 3 sets, and for each entity the preview names the
   surviving Area that cites it; an entity that a surviving Area cites is kept, not removed,
   with its first-appearance field set to `pending redraft`; Part 38 Rule 7.2.1); and invoke
   **area-scorer** to remove the archived Areas' scores from the CDL-2 tracker and recompute
   the Section running aggregate. The reconciliation shows its preview and waits for
   confirmation (`/force-ledger-audit` Step 5). When a later Chapter is already written it
   stays canon: its text, rows and ledger effects are not rolled back, only what the archived
   Areas alone established is; the redrafted Chapter must fit what the later Chapter
   presupposes, and the carry-over reading of Step 3 tests the join. Where the Step 1 revise runs a light
   audit, it treats the Chapter's own effects as superseded.
   `/restore-archive <date-time>` is the way back for the archived pairs: it moves them to their
   paths again and brings the ledgers, spec blocks and scores back in line.
3. Rebuild fresh per-Area file pairs under the Chapter folder: run `/next-area` repeatedly,
   one Area at a time, through the Chapter in order. Each Area is written to the size target
   and pacing the re-confirmed spec sets for it, and is audited at its close. If a later
   Chapter is already written, the Gate 1 of the last redrafted Area also reads the carry-over
   with that Chapter's first Area, and so does the Gate 1 of every earlier Area of the
   redraft; each cycle also gives **outline-planner** and **area-maker** the block of that
   Chapter's first Area (its opening type and carry-over) and its text, so that a misfit is met
   while drafting and not after the whole Chapter is redrafted. A carry-over finding whose
   cause lies in that later Area follows the route in `next-area.md` Step 3. The dates are part
   of the join: the redrafted Chapter starts on or after the last day of the Chapter before
   it, and the later Chapter, which stays canon, starts on or after the redraft's last day
   (Part 41 Area 6, Dating rules and the check); each redrafted Area writes its calendar rows
   afresh at its Gate 2.
4. Run `/force-ledger-audit` once the Chapter is fully redrafted — a plain reconciliation; it
   performs no rollback, because Step 2 did. The Gate 2 sync of the redraft's last Area sets
   the Chapter Spec to `COMPLETED` again once every Area block is terminal (Part 38 Rule 3.6.1
   item 1). The completion content it held (final variance summary, Reader-now-knows line,
   Chapter digest) is kept as history while the redraft runs and is refreshed from the
   redrafted text by `/chapter-spec complete` (Part 38 Rule 9.7.2). The Novel-Part Spec and
   the Section Spec are completed again only at their own boundary, on the author's yes (Part
   38 Rule 9.7.3).

## Failure/abort

Confirm the redraft scope (exactly this Chapter) before archiving and rebuilding, through
`AskUserQuestion` with a Cancel option; the confirming answer names the scope in words (for
example "Redraft Chapter 12, 11 Areas archived"), as `guardrails/commands/guardrail-command-law.md`
requires. Cancel, or any other answer, ends the command with nothing changed.

A redraft can stop inside Step 2, after the move and before the reconciliation is done: the
author declines the reconciliation preview, the audit stops at `NEW ENTITY TYPE`, or the run
is interrupted. The Chapter's Areas are then archived while the ledgers, spec blocks and
scores still show them. This state is named *moved, not reconciled*. Re-run
`/redraft-chapter` with the same Chapter: the file move in Step 2 is skipped for files already
moved, and the Step 2 reconciliation runs again.
