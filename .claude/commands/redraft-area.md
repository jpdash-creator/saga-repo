---
description: Discard and completely redraft one Area (a full rewrite from the Chapter Spec's plan; see /revise-area for a targeted in-place revision). Destructive within scope. Human-invocation only.
argument-hint: <area reference>
user-invocable: true
disable-model-invocation: true
---

# `/redraft-area`

Corresponds to canon command `[REDRAFT AREA: ref]` (C-29). One Area is archived whole and
written again, from the Chapter Spec's plan, as a fresh Area.

## Preconditions

- Read `.claude/guardrails/commands/guardrail-plan-then-auto-execution.md` (Plan Mode →
  Auto Mode sequencing, default model/effort, mandatory parallelism, milestone progress
  reports — governs this command's execution shape end to end).
- The spec chain must be in force for the Area's Chapter: its Novel-Part Spec and its Section
  Spec are `CONFIRMED` or `COMPLETED`. Step 1 is a `/chapter-spec` revise flow, which refuses
  to run under a parent spec that is `DRAFT`, `AMENDED-PENDING-RECONFIRM` or `RETIRED`
  (Part 38 Rule 9.1.1).

## Plan Mode → Auto Mode

The scope confirmation in Failure/abort — confirming this is exactly the intended Area, not
an adjacent one — opens this command's own **Plan Mode**, and Step 1's `/chapter-spec`
revise consultation (with its `[CONFIRM SPEC]` gate, scoped to this Area's block, and the
question about the Novel-Part Spec entry that Step 1 describes) completes it: both are
resolved before Step 2 moves anything. Once resolved, Steps 2-4 run in **Auto Mode** with no
further discretionary questions. Auto Mode never waives a mandatory gate: the `/next-area`
cycle launched in Step 3 carries its own nested Plan Mode/Auto Mode (its own Decision
Consultation Gate) and its own Gate 1 `[CONFIRM WRITE]` token, exactly as documented in
`next-area.md` — not duplicated here (`guardrails/commands/guardrail-plan-then-auto-execution.md`).
Pacing is not asked again: the Chapter Spec's pacing value for the Area (as revised in Step 1)
is carried.

Within the `/next-area` cycle, independent steps must still run in parallel per the
guardrail.

## Sequence

1. Re-open the Area's block of the Chapter Spec via the `/chapter-spec` **revise** flow
   (Part 38) — author consultation scoped to this Area's block, through `[CONFIRM SPEC]` — with
   **outline-planner** re-confirming what the Area should cover inside that flow (the redraft
   may be happening precisely because the original plan didn't work). The revised block is
   the redraft plan (its scene anchors, size target of 1,600, 1,800 or 2,000 words, pacing,
   opening and closing type, carry-over and thread); its status is still `WRITTEN` while it
   is agreed, and Step 2 rolls it back. Other Areas' blocks are left untouched. A redraft
   that keeps the plan unchanged needs no amendment (Part 38 Rule 7.3.1) and leaves the spec
   as it is, with one variance line. A spec is a living record, so a `COMPLETED` Chapter Spec is
   revised like any other and nothing extra is asked about it (Part 38 Rule 9.7.1). A substantial
   revision (Part 38 Rule 3.5.2) sets the spec to `AMENDED-PENDING-RECONFIRM` until
   `[CONFIRM SPEC]` and `CONFIRMED` afterwards; a light one (pacing, size target, variance note)
   leaves the status. If the Chapter's
   Novel-Part Spec or Section Spec is not `CONFIRMED` or `COMPLETED`, the revise is refused
   before anything is moved, and the refusal names the command to run (`/part-spec` or
   `/section-spec`).
   **The Novel-Part Spec entry.** The Chapter's entry in its Novel-Part Spec is the plan
   baseline. If the revised block changes something that entry fixes — who is on the page, a
   key event, a reveal owed, a thread in or out, the opening hook when this is the Chapter's
   first Area, or the closing beat when it is the last (Part 38 Rule 9.3.3) — the departure
   is shown at this flow's confirm step, and the author is asked, for each departure, whether
   to amend the plan (the Novel-Part Spec entry is then changed through `/part-spec revise`, a
   light amendment when only that entry changes, Part 38 Rule 11.4.2) or to leave the original
   entry as the plan baseline. Either way the departure is recorded as a variance note on every
   spec above the Chapter Spec, written top-down in one step at this flow's `[CONFIRM SPEC]`:
   the Section Spec first, then the Novel-Part Spec, and the Chapter Spec is updated after them
   (Part 38 Rules 9.4.5 and 11.4.2). Each note is light: it changes no plan content, and the
   plan content of the Novel-Part Spec or the Section Spec changes only through that spec's own
   command. Re-cutting the Area and a different size target or pacing are the Chapter Spec's
   own business and no departure. The question is asked here and not again later.
2. **Go back first, as a rewind to the end of the previous Area does**: move the Area's
   written file pair (`area-NN.docx` and `area-NN.md`), never delete it, to
   `projects/novel-starward-saga/_archive/<date-time>/` keeping its path (Part 2 Rule 5.3.2a; the
   redraft archives first, so its fresh write needs no `--overwrite`, which only `/revise-area`
   passes); invoke **continuity-checker** to run
   `/force-ledger-audit` as the reconciliation pass with the archived Area treated as
   non-canonical (Living fields that only the archived Area established roll back, and so
   does a behavioral drift whose Area is archived, under Part 39 Rule 39.41.6.1: its
   Section 12 entry is marked `rolled back`, never deleted, and a Permanent drift's prior
   value returns to Section 11 from the superseded-behaviors table; the Area's calendar rows
   (its Area row) is removed, the Chapter, Novel-Part, Section and
   Phase rollups and the Current Position block (the Open Chapter and the Open Chapter's recorded
   window, First to Latest) of `ledger-worlds-calendar/_index.md` are
   recomputed from the rows that remain (Part 41 Area 9, The calendar ledger, resets and
   rewinds); the Area's block rolls back to `PLANNED` with a variance note recording the
   redraft, and its pacing value, which the Chapter Spec records, stays as it is; the Chapter Spec, if it is `COMPLETED`, returns to
   `CONFIRMED` with its completion text kept as history, and a `COMPLETED` Novel-Part Spec or
   Section Spec above it returns to `CONFIRMED` with it (statuses only; Part 38 Rules 7.2.1 and
   9.8.1); registry refreshed, including the Coverage cell of every Novel-Part Spec row and
   Section Spec row above the Chapter whose figures changed (Part 38 Rules 10.1.2 and
   11.1.2); rows and entity files whose first appearance is in the archived Area are listed in
   the preview as `/rewind-to` Step 3 sets, and for each entity the preview names the
   surviving Area that cites it; an entity that a surviving Area cites is kept, not removed,
   with its first-appearance field set to `pending redraft`; Part 38 Rule 7.2.1); and invoke
   **area-scorer** to remove the archived Area's score from the CDL-2 tracker and recompute
   the Section running aggregate. The reconciliation shows its preview and waits for
   confirmation (`/force-ledger-audit` Step 5). When later Areas of the Chapter are already
   written they stay canon: their text, rows and ledger effects are not rolled back, only
   what the archived Area alone established is; the redrafted Area must fit what the later
   Areas presuppose, and the Step 3 carry-over reading tests the join. Where the Step 1 revise runs a light
   audit, it treats the Area's own effects as superseded.
   `/restore-archive <date-time>` is the way back for the archived pair: it moves it to its
   path again and brings the ledgers, spec block and score back in line.
3. Run `/next-area` once (one full Gate 1->Gate 2 cycle, never batched —
   `.claude/guardrails/commands/guardrail-deprecated-commands.md`) for the Area the revised
   block plans — it writes a fresh file pair at its Gate 2 (the old pair is in the archive).
   The Area is audited at its close again: Check #21's Area-close enquiry and the Area-level
   score run on it. If a later Area is already written, the Gate 1 also reads the carry-over
   with that Area (the Area-to-Area carry-over rule); the cycle also gives **outline-planner**
   and **area-maker** the later Area's block (its opening type and carry-over) and its text, so
   that a misfit is met while drafting and not after the Area is redrafted. A carry-over
   finding whose cause lies in that later Area follows the route in `next-area.md` Step 3. The
   dates are part of the join: the redrafted Area starts on or after the last day of the Area
   before it, and the later Area, which stays canon, starts on or after the redraft's last
   day (Part 41 Area 6, Dating rules and the check); the redrafted Area writes its calendar
   rows afresh at its Gate 2.
4. Run `/force-ledger-audit` once the Area is redrafted — a plain reconciliation; it performs
   no rollback, because Step 2 did. When the redraft is written and every Area block of the
   Chapter is terminal again, the Gate 2 sync sets the Chapter Spec back to `COMPLETED` (Part
   38 Rule 3.6.1 item 1). The completion content it held (final variance summary,
   Reader-now-knows line, Chapter digest) is kept as history and is refreshed from the
   redrafted text by `/chapter-spec complete` (Part 38 Rule 9.7.2). The Novel-Part Spec and the
   Section Spec are completed again only at their own boundary, on the author's yes (Part 38
   Rule 9.7.3).

## Failure/abort

Confirm the redraft scope (exactly this Area, not an adjacent one) before archiving anything,
through `AskUserQuestion` with a Cancel option; the confirming answer names the scope in words
(for example "Redraft Chapter 12, Area 3, 1 Area archived"), as
`guardrails/commands/guardrail-command-law.md` requires. Cancel, or any other answer, ends the
command with nothing changed.

A redraft can stop inside Step 2, after the move and before the reconciliation is done: the
author declines the reconciliation preview, the audit stops at `NEW ENTITY TYPE`, or the run
is interrupted. The Area is then archived while the ledgers, spec block and score still show
it. This state is named *moved, not reconciled*. Re-run `/redraft-area` with the same Area:
the file move in Step 2 is skipped for files already moved, and the Step 2 reconciliation runs
again.
