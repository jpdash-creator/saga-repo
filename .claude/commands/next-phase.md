---
description: Advance to the next Phase of the series. Rare -- Phase 1 alone is 8 Sections; only invoke once Phase 1 is genuinely complete.
user-invocable: true
disable-model-invocation: true
---

# `/next-phase`

Corresponds to canon command `[NEXT PHASE]` (C-9). The total phase count for the series is
explicitly undetermined ("TBD") per canon — this is a major, rare transition, not a
routine navigation step, hence explicit-invocation-only.

**Note.** The Phase 2 spec chain (Section Spec, Novel-Part Spec, Chapter Spec) waits until Part 30 is expanded for Phase 2: no Phase Spec exists, `/section-spec` refuses a Section that Part 30 has no entry for, and Step 4's Chapter Spec build below is refused by the chain rule (Part 38 Rules 9.1.1 and 9.1.4) until the incoming Section Spec and Novel-Part Spec exist. This command closes Section 8 itself: it runs the Section-close reviews and asks the three completion confirmations once each, in the order Chapter, then Novel-Part, then Section (Part 38 Rule 9.7.3). A completion the author already made with `/part-spec complete` or `/section-spec complete` is not asked again.

## Sequence

1. Confirm all 8 Sections of the current Phase are complete and audited clean. The chain check
   (reads only, as `/next-chapter`, `/next-part` and `/next-section` do): the closing Section's
   Section Spec, its current Novel-Part Spec and its current Chapter Spec are each `CONFIRMED` or
   `COMPLETED`, and the incoming Phase's Section 1 Section Spec and first Novel-Part Spec exist
   (Step 5 reads Section 1's Epigraph from that Section Spec); a missing or `DRAFT` link stops the
   command and names the command to run. Then run the Section-close reviews of the Phase's final
   Section by reference to `/next-section` steps 2 (CDL-2 running aggregate), 2a (Check #21
   Section-close behavior review, POV report, Owed Beats line and chain report), 2b (session-end
   FCIA + ALCA Mode B audit chain) and 2c (independent reader pass), launched together as
   `/next-section` launches them; if the audit chain has not run since its last Area, it runs now.
   A Check #21 question or an audit FAIL the author has not ruled on blocks Step 4, exactly as in
   `/next-section`.
   Calendar (Part 41 Area 9): the author decided that every
   Area row stays in the calendar ledger's index with its Current Position block, and that this is
   revisited at the end of Phase 1. When the closing Phase is Phase 1, put that housekeeping question to
   the author through `AskUserQuestion` before Step 2; nothing is moved or archived without the answer.
2. Invoke **outline-planner** to establish the new Phase's premise and arc framework, with its calendar
   windows written as dates plus Phase Day (Part 41 Area 4) and its carry-in naming the last dated moment
   of the closing Phase, read from the calendar ledger's Current Position block (Phase 1 closes at Phase
   Day 3285; Part 41 Area 4).
3. Check the two images the new Phase's Title Page needs (Part 2 Rule 6.3.1b): the Phase icon
   `projects/novel-starward-saga/phase-N/phase-icon.png` and the icon of its first Section,
   `projects/novel-starward-saga/phase-N/section-1/section-icon.png`. Run `/create-image-phase N` and
   `/create-image-section N 1` for whichever is missing, and go on only when both exist.
4. Prepare the completion of the outgoing specs bottom-up, each asked once, in the order Chapter,
   then Novel-Part, then Section (the `/chapter-spec`, `/part-spec` and `/section-spec`
   **complete** flows: their checks, their questions and the author's confirmation, and the
   drafted summaries; nothing is written yet; one already `COMPLETED` is skipped). The Chapter
   questions come first, then the Novel-Part's, then "Has this Section finished?". Then build the incoming Chapter's spec via the
   `/chapter-spec` **build** flow — full consultation through `[CONFIRM SPEC]`,
   establishing the Chapter's title, purpose, Area breakdown and each Area's block
   (Part 38 section 2.4: its size target of 1,600, 1,800 or 2,000 words, its pacing, whether it is
   a complete scene or continues a scene across Areas, opening and closing type, carry-over, thread
   and the other fields listed there) — BEFORE
   any Area is planned or drafted. On `[CONFIRM SPEC]`, write the outgoing Chapter's, Novel-Part's and
   Section's completions (what `complete` writes) in the same write step as the new spec file and its
   registry row, and refresh the Coverage cells of the Novel-Part and Section rows as a completion
   write step (Part 38 Rule 1.2.2); under `[SKIP SPEC]` it is not written. If the incoming Chapter's spec already exists and is confirmed (a spec survives a rewind, a reset or a
   redraft, Part 38 Rule 7.1.1), do not build it blind: run the `/chapter-spec` **revise** flow on it and
   re-confirm what survives, as `/start-story` Step 4 does; the outgoing completions are then
   written at that `[CONFIRM SPEC]`, in the same write step. A Phase advance opens a new Chapter as surely as
   `/next-chapter` does, so the same obligation binds here (Part 38 Story Specification
   Law; `.claude/guardrails/ledger/guardrail-story-spec-law.md`).
5. Run `/next-area` for the new Phase's opening Area, with `--first-of-phase`,
   `--first-of-section` and `--first-of-chapter` (the writers' `is_first_area_of_*` parameters). Its Title Page carries two
   epigraph lines: the new Phase's epigraph, the `Epigraph:` line of that Phase in Part 30, and
   below it Section 1's own Epigraph, the Epigraph line in the header block of the new Phase's
   Section 1 Section Spec; this command reads each from its file and passes the text only (`unset`
   meaning none for that line), as `/next-area` Step 5 sets (Part 38 Rule 10.3.1). The Area's size
   target and pacing are carried from the Chapter Spec and are not asked again. The new Section 1's CDL-2
   tracker does not exist yet: area-scorer creates it from its template at the first scored Area.

## Failure/abort

Never advance a Phase with an incomplete or unaudited prior Section — surface it instead.
