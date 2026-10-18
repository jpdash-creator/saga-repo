---
description: Revise one already-written Area in place (a targeted revision of its text), re-running the full Gate 1/Gate 2 cycle on the revision.
argument-hint: <area reference>
user-invocable: true
---

# `/revise-area`

Corresponds to canon command `[REVISE AREA: ref]` (C-28). A targeted, in-place revision of one
written Area. A revision is not exempt from the audit pipeline just because the Area was
previously accepted. To discard and write an Area afresh, use `/redraft-area`.

## Preconditions

- Read `.claude/guardrails/commands/guardrail-plan-then-auto-execution.md` (Plan Mode →
  Auto Mode sequencing, default model/effort, mandatory parallelism, milestone progress
  reports — governs this command's execution shape end to end).
- Read `.claude/guardrails/ledger/guardrail-story-spec-law.md` and the Area's block in the
  spec of the Area's own Chapter under
  `.claude/story-memory/phase-section-part-chapter-area-specs/` — not the active Chapter's
  spec when the Area belongs to an earlier Chapter. That spec may be `COMPLETED`: Part 38
  Rule 6.1.1(a) counts a `COMPLETED` spec as in force for Check #18, and the Gate 2 sync on it is
  a correction of record (Rules 6.1.1(a) and 9.7.1) that leaves its status as it is. The
  revision is made in knowledge of what the spec says this Area covers (its size target,
  pacing, opening and closing type, Behavioral Plan and thread).
- The spec chain must be in force for the Area's own Chapter (Part 38 Rule 9.1.1; Gate 1
  Check #18(a)): the Chapter Spec is `CONFIRMED` or `COMPLETED`, and so are its Novel-Part Spec
  and its Section Spec, each read from `.claude/story-memory/phase-section-part-chapter-area-specs/`
  (status only; the Area's own Chapter Spec carries every inherited item). If a link is
  missing, `DRAFT`, `AMENDED-PENDING-RECONFIRM` or `RETIRED`, stop before Step 1 and name the
  first missing link and the command that mends it (`/section-spec`, `/part-spec` or
  `/chapter-spec`). Nothing is revised and nothing is written.
- **Refuse a whole-built Chapter.** If the Area's Chapter was built whole (its Chapter Spec's `Build mode`
  is `whole` and its Area rows read `WRITTEN(P.S.N.CCC)`, with no `area-NN` files), stop before Step 1 and
  say: "Chapter P.S.N.CCC was built whole by /create-chapter and has no Area files; use /revise-chapter to
  change it." Nothing is revised and nothing is written.
- Locate the Area in its Chapter and read its neighbours: name the Area before and the Area
  after it. Where the scene continues across consecutive Areas, say so plainly before anything is
  revised, because a revision can change how the scene carries over at either edge of the Area.

## Plan Mode → Auto Mode

This command runs its own single Gate 1/Gate 2 cycle directly rather than invoking
`/next-area` — its Decision Consultation Gate (Part 28 Area 19) is a short check: it asks only about
open branches the requested change creates (a new name, a change of scope) and never the
pacing question, because the revised Area keeps the pacing and size target recorded in the
Chapter Spec. That check, with the Area reference and the requested change the command is
invoked with, is this command's **Plan Mode**, concluded before Step 1 begins. Steps 1-4 then
run in **Auto Mode** with no further discretionary questions, but Auto Mode never waives a
mandatory gate: Step 3's `[CONFIRM WRITE]` / `[REVISE AREA]` / `[SKIP WRITE]` token is the same
mandatory Gate 1 confirmation `/next-area` requires at its own confirmation step — not duplicated
here (`guardrails/commands/guardrail-plan-then-auto-execution.md`).

## Sequence

1. Invoke **area-maker** to revise the identified Area per the requested change. Where the
   revision touches a numeric reading other than size, the requested change governs the remedy, and
   the number yields to keeping the scene alive (`guardrails/quality/guardrail-threshold-consultation.md`).
   The revised Area stays inside the size range (1,280 to 2,400 words; the
   spec sets the target at 1,600, 1,800 or 2,000): a count outside 1,280 to 2,400 words is a
   blocking finding: the write waits for the author to confirm the Area or send it back. Pass area-maker the references of the Area
   before and the Area after the revised Area and the spec's Area block; it reads both
   neighbours from the written files before revising. The revised text keeps its date line as
   its first line (Part 41 Area 5); the line changes only if the requested change moves the
   scene in time, and then the new date must still meet the Area before it and the Area after it
   (Part 41 Area 6). Pass area-maker the calendar ledger's row of the Area with its neighbours.
2. Invoke **continuity-checker** for a fresh Gate 1 audit of the revision (not a diff-only
   check — the whole Area is re-audited through the full 23-check sequence, including Check #18
   (Spec Conformance, Part 38; stated below), the Prose Vitality Check #19, Behavioral Conformance
   Check #20, Behavioral Change Detection Check #21 and Plain Language and Narrative Impact
   Check #22 and, where the Area holds a fight, Battle Plausibility Check #23, Part 44). This first audit of the revision is always full; a FAIL it returns is fixed and re-audited under the gate law's section "Re-audit after fixes" (Author ruling, 2026-10-18), as `/next-area` Step 3 sets out. A revision that alters a character's rendered conduct re-opens Check #21: the
   profile may have to move with the text, or the text back to the profile. (2026-10-06) A send-back at Check #21 `[REVISE AREA]` arrives here; nothing in a ledger changes until the revised Area is confirmed, and no new command exists. Heroes and Tier A characters: the author rules each evolution; Tier B, C and D: the continuity-checker decides and records its reasons; an immutable trait always needs the author's ruling. Evolution is not drift (Part 43). **Check #22 vocabulary elements (plain vocabulary, 2026-10-06):** the check also blocks a special or invented word with no picture at first use, one word carrying two meanings in an Area, a jargon wall (three or more unexplained special terms in one sentence or speech) and a figure the reader cannot parse at first read; 22-3, 22-6 and these new elements block, while 22-1, 22-2 and 22-7 inform.
   Check #18 (Spec Conformance, Part 38): the drafted Area is compared with every spec-planned
   element and shown as a plan-versus-written list; a difference on a core item (Part 38 Rule 6.1.1(b): the beat (the Area's purpose); the scene anchors (their order is part of the anchors); the Continuation; the viewpoint (the Dual-POV mark included); every planned time skip; the Behavioral Plan (Rule 6.1.2); the Opening type; the Closing type; the Thread or storyline; and every settled item) blocks unless it traces to an on-record author
   answer from this invocation; a size outside 1,280 to 2,400 words also blocks (a count outside
   1,280 to 2,400 words is a blocking finding: the write waits for the author to confirm the Area or
   send it back); a pacing difference is listed only and never blocks; every other difference is listed, `[CONFIRM WRITE]` accepts the
   listed ones (the spec is updated at Gate 2) and `[REVISE AREA]` rejects them. An Area whose
   spec chain is not in force (a Chapter Spec, Novel-Part Spec or Section Spec that is missing,
   `DRAFT`, `RETIRED` or `AMENDED-PENDING-RECONFIRM`) fails Check #18(a) (Part 38 Rule 6.1.1(a)). A
   missing or unconfirmed link is a FAIL: Critical where no chain stands (a link is missing,
   `DRAFT` or `RETIRED`), Major where a link stands but is `AMENDED-PENDING-RECONFIRM` (Part 38
   Rules 6.1.3 and 9.1.3). Check #18 compares the Area with its own Chapter Spec only; it adds
   no comparison with the Novel-Part Spec or the Section Spec.
   The Area flow review (Check #16 dimension 16-J) runs as a second instance over the revised
   Area read with its neighbours in order (the Area before and the Area after, from the
   written files); the two edges at the revised Area are the **neighbour check**, so both
   carry-overs are audited under the Area-to-Area carry-over rule. A break of time, place,
   point of view or character state at either edge FAILs (the dates are part of it: the date
   line is read under Check #11 element 11-2 (the dating rules, the weekday included) and
   Check #12 (its form), against both neighbours' lines, so a revised end day that no longer
   meets the next Area's start day FAILs under Part 41 Area 6); sameness is reported with
   quoted lines. If the cause lies in a neighbour, the revised Area is repaired first when
   that solves it; otherwise the neighbour is named (Reference Code and name) and the author
   is asked whether to run `/revise-area` on it first. If the author declines, the author
   chooses another repair, the finding stays blocking until it is repaired or the author
   rules a canon amendment, and nothing is accepted automatically. If the author agrees, the
   pending revision is discarded (this invocation ends as a `[SKIP WRITE]`: nothing written
   or updated) and `/revise-area` runs on the neighbour first, then on this Area again.
   Check #21's Area-close enquiry runs again, because every Area is audited at its close.
   When later Areas are already written, the ledgers hold facts the old text did not
   establish. The Pre-Write Ledger Check (Step 1) and the character ledger state
   verification (Check #14) therefore read Living fields as they stood after the Area
   before the revised one, rebuilt from the Canon Events Log, whose rows carry Area
   references. The 23-check instance also lists every fact the old text established that a
   later Area cites, naming that Area; a revision that removes or changes one of them is
   put to the author as a question, after the Position Header and the full text are printed.
3. Present and confirm: print the Position Header Block (marked as a revision of the Area's
   Reference Code, its pacing declared as the value recorded in the Chapter Spec), the **full
   text of the revised Area, verbatim** — never a summary, an excerpt or a file path — the
   Contextual Earning Declaration, and the Post-Draft Audit Report with the neighbour-check
   result, the word count against the passing range, one line on the FAIL loop where it ran (the first audit's
   FAIL checks, the mode of the re-audit and its result; Author ruling, 2026-10-18) and the plan-versus-written list, then
   wait for `[CONFIRM WRITE]` / `[REVISE AREA]` / `[SKIP WRITE]`. The confirmation prompt says
   that `[CONFIRM WRITE]` replaces the written text and that the previous text will be kept in
   the archive. A question to the author about the revision is asked after the Position
   Header and the full text are printed. `[REVISE AREA]` returns to Step 1, re-runs Step 2 in
   full (both instances; a first full audit of the newly revised text, Author ruling, 2026-10-18) and prints the text again; `[SKIP WRITE]` discards the revision and
   leaves the written Area, the ledger and the spec as they were.
4. On confirm: first move the old `area-NN.docx` / `area-NN.md` pair, never deleting it, to
   `projects/novel-starward-saga/_archive/<date-time>/` keeping its path (a plain move, as in a
   rewind; Part 2 Rule 5.3.2a), then write the revised
   `.docx`/`.md` files at the same path
   (`projects/novel-starward-saga/phase-N/section-N/part-N/chapter-NNN/area-NN.(docx|md)`)
   via the authorized scripts (`area_docx_creator.py` and `area_md_creator.py`; the call printed in
   `/next-area`'s Gate 2 write step with `--overwrite` added; this is the one command that passes
   it) with the same `--first-of-*` flags as the files being replaced (a revised first Area of a
   Phase or a Section also passes the same epigraph lines as `/next-area` sets, Part 38 Rule
   10.3.1; this command reads those lines itself, from Part 30 and from the Section Spec, and
   passes only the epigraph text: for the first Area of a Phase, TWO lines, the Phase
   epigraph, the `Epigraph:` line of that Phase in Part 30, its text after the label (`--phase-epigraph-file`), and
   the Epigraph line of that Phase's Section 1 in its Section Spec (`--section-epigraph-file`);
   for the first Area of any other Section, the Epigraph line of that Section's Section Spec
   (`--section-epigraph-file`) alone; `unset` meaning none for that line, so that its Title
   Page keeps its epigraph lines). Every Area file carries the Area Title Block; read it back
   from the `.docx` as `/next-area` sets (`--expect present`). Then launch in
   parallel: **continuity-checker** for the Gate 2 Post-Write Audit only (Completeness
   Indicator + Tier Scope Brackets, no ledger writes; give it the read-back result),
   `/force-ledger-audit` for the ledger reconciliation this revision may require, and
   **area-scorer** to re-score the overwritten Area (with its Voice and Variety block) and
   recompute the Section CDL-2 running aggregate (the revision replaces the Area's prior
   contribution rather than adding to it, so the aggregate `/status` reports stays live; same
   3-way split as `next-area.md` — audit reporting, ledger writes, and scoring are independent,
   so they are never staged one after the other). The reconciliation-side instance also carries
   the mandatory Part 38 as-built sync on the Area's spec block (Part 38 Rule 3.6.1 — every Gate 2,
   this same instance): run the Rule 3.6.1 sync on the Area's block (the block's status stays
   `WRITTEN` and the spec's own status stays as it is — a `COMPLETED` Chapter Spec stays
   `COMPLETED`; the pacing and size target stay as recorded in the block; the Signatures fired
   record of the revised Area replaces the old one). It is an ordinary Edit, named here
   explicitly because the spec folder is outside the ledger reconciliation's own scope. If the
   revised text introduces a new Tier D person, pass the Tier D block unchanged into the
   prompt of the reconciliation-side instance (which writes the row), as `/next-area` sets,
   and pass it each Check #21 ruling (character, trigger, token) the same way. Pass it the
   checked NAMED ITEMS list the same way (Part 28 Rule 20.8.4(e)): the instance enters as a
   row of `ledger-named-items/_index.md` any item the revised text introduces, and keeps the
   row of an item whose first Area this is in line with the revised text. A named document or a
   named agreement, treaty or accord the revised text introduces is entered the same way in
   `ledger-society-information/_index.md` (Part 28 Rule 20.8.7). The same goes for the
   `NAMED MOVES (new in this Area)` block and `ledger-named-moves/_index.md` (Part 6 Rule 6.5),
   and for the checked `MONSTERS (new in this Area)` list and `ledger-character-monster/`
   (Part 40; Part 37 Thresholds M-1 and M-2). The same instance corrects the calendar rows of
   the revised Area from the first line of the rewritten `.md` and the checked
   `CALENDAR (this Area)` block (Part 41 Area 9): the revision replaces the Area's dating, so
   the Area row, the rollups and the Current Position block (the Open Chapter and the Open Chapter's
   recorded window, First to Latest) are recomputed
   where the line changed and left as they are where it did not. The written text file begins
   with the date line, as `/next-area` sets out.

## Failure/abort

A revision that fails Gate 1 is corrected and re-audited exactly like a fresh draft (the re-audit after the first full audit follows the gate law's section "Re-audit after fixes", Author ruling, 2026-10-18) — never
written through on the strength of the original's prior approval.
