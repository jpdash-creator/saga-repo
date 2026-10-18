---
description: Advance to the next Novel-Part (Chapter numbering resets within it) -- complete the closing Novel-Part's specs, build the new Novel-Part Spec and its first Chapter Spec, then write its opening Area.
user-invocable: true
---

# `/next-part`

Corresponds to canon command `[NEXT PART]` (C-7). "Novel-Part" is Part 2's five-tier structural
unit, distinct from a canon-law "Part" (e.g. Part 3, Part 22) — do not confuse the two when reading
skills/guardrails. For the same reason the spec of a Novel-Part is always called the **Novel-Part
Spec** in rule text; its command is `/part-spec` (C-41).

A new Novel-Part continues the **spec chain** (Part 38 Rule 38.9, Area 9) under the Section Spec
already confirmed for the current Section: this command builds the new Novel-Part's **Novel-Part
Spec** (the `/part-spec` build flow), then the **Chapter Spec** of its first Chapter (the
`/chapter-spec` build flow), each through its own `[CONFIRM SPEC]`, before any Area is planned. It
also completes the closing Novel-Part's specs (its last Chapter and the Novel-Part itself).

## Preconditions

- Read `.claude/guardrails/commands/guardrail-plan-then-auto-execution.md` — it governs this
  command's Plan Mode → Auto Mode shape, default agent model/effort, mandatory parallelism,
  and milestone progress reporting, exactly as it governs the `/next-area` call this
  command delegates to.
- Read `.claude/guardrails/ledger/guardrail-story-spec-law.md` and `spec-story-specification-law`
  (Part 38 Areas 9 and 11): the chain rule (Rule 9.1.1), the clarity mandate that governs both
  builds (Rule 38.13) and completion at the boundary (Rules 9.7.2 and 9.7.3).
- The Section Spec of the current Section must be `CONFIRMED` or `COMPLETED`. If it is not
  (`DRAFT`, `AMENDED-PENDING-RECONFIRM`, `RETIRED` or missing), stop and name `/section-spec`;
  a Novel-Part Spec cannot be built under it (Rule 9.1.1).

## Plan Mode → Auto Mode

Steps 0 to 3 are this command's **Plan Mode**. It confirms the closing Novel-Part's Chapters are
complete, prepares the completion of the closing Novel-Part's specs (nothing is written yet) and
asks whether the Novel-Part has finished, then builds the incoming Novel-Part's Novel-Part Spec
(step 2) and its first Chapter's Chapter Spec (step 3) — full iterative author consultation, each
through an explicit `[CONFIRM SPEC]` — before any Area is planned or drafted. Only ONE confirm
prompt is open at a time; each names the artifact and its reference ("Novel-Part Spec 1.2.3",
"Chapter Spec 1.2.3.001"). Once the new Chapter's spec is confirmed, **Auto Mode** begins: step 4
proceeds straight into `/next-area`, which runs its own full Plan Mode → Auto Mode cycle (Decision
Consultation Gate through Gate 2 confirmation) independently and in full — this command neither
shortens nor restates it. Auto Mode never waives a `[CONFIRM SPEC]`.

## Parallel orchestration

Per `guardrails/commands/guardrail-plan-then-auto-execution.md` (absolute binding; Part 38 Rule 9.9.3).

- **After step 0 passes, launch together in one message:** (a) the completion preparation of the
  closing Novel-Part's last Chapter and of the Novel-Part (outline-planner, step 1) and, through
  the `/chapter-spec` complete flow, area-scorer for the Chapter-Level CDL-2 Aggregate Block
  of the closing Chapter (information only); (b) the grounding of the two builds — one
  outline-planner per level (Novel-Part Spec, Chapter Spec), each reading the whole chain
  above its level (the Section Spec in full for both, the Novel-Part Spec as well for the
  Chapter build) and told to report open branch points, *not* to finalize; (c) one
  continuity-checker pre-read (Locked Canon, Part 30 locks, Entity Naming Law, ledgers, the
  closing specs) that serves the light audit of both new specs.
- **Consultation and confirmation run strictly top-down** — Novel-Part Spec, then Chapter Spec.
  When the Novel-Part Spec is confirmed, tell the Chapter planner so via `SendMessage` and let
  it finalise.
- **Question streams are separate** and never share one `AskUserQuestion` call: the completion
  questions with the finish confirmation (asked first, before any consultation; a "Not yet"
  writes nothing), and then each spec's consultation.
- Step 4 depends on step 3's confirmation, so those steps are sequential; the
  mandatory-parallelism binding applies inside the delegated `/next-area` call, as documented
  there.

## Sequence

0. **Chain check** (reads only; nothing else is launched until it passes). The current Section
   Spec (see Preconditions), the current Novel-Part Spec and the current Chapter Spec must each
   be `CONFIRMED` or `COMPLETED` (Part 38 Rule 9.1.1); a link that is `DRAFT`,
   `AMENDED-PENDING-RECONFIRM`, `RETIRED` or missing stops the command and names the command
   to run (`/section-spec`, `/part-spec` or `/chapter-spec`). Every other Chapter Spec of the
   closing Novel-Part must already be `COMPLETED` and variance-annotated (completed at its own
   `/next-chapter`). The new Novel-Part must have an **entry in the Section Spec's Novel-Part
   plan**. If the Section Spec has no further entry, stop and ask the author through
   `AskUserQuestion` which way to go: the Section has finished (run `/next-section`) or the
   Section Spec needs one more Novel-Part (run `/section-spec revise`, which adds it and runs
   the cascade report of Part 38 Rule 9.4.2); nothing is written. Adding a Novel-Part to a Section Spec
   is a substantial amendment (Rule 9.4.2), so there is no light add here: no Novel-Part Spec is
   built under a Novel-Part the Section Spec does not list.
1. Invoke **outline-planner** to confirm the closing Novel-Part's Chapters are complete (every
   Area row of the last Chapter terminal) and to prepare the completion of
   the two outgoing specs, bottom-up:
   - the last Chapter's completion (the `/chapter-spec` **complete** flow: its checks, its
     questions to the author and its one confirmation, whose yes means "complete it when the
     new Chapter's spec is confirmed", with the drafted final variance summary, Reader now
     knows line, Chapter digest and New-named-things line; nothing is written yet);
   - the Novel-Part's completion (Part 38 Rule 9.7.3 and Rule 11.7.1: the planned-versus-as-written
     variance summary including Chapters added or dropped, the Reader now knows line by
     reference to the last Chapter's line plus Novel-Part additions, the digest, and the
     threads and setups carried on to the next Novel-Part).

   Every unresolved `[OPEN]` item (found in the Audit and Settlement Notes section of each spec),
   every setup planted with no payoff and every unresolved
   cliffhanger or thread is put to the author through `AskUserQuestion`: resolve it, carry it
   on to the new Novel-Part's specs, or mark it lapsed; a setup or thread is marked lapsed only
   on the author's answer (Part 38 Rule 9.7.3). A Chapter entry the story never reached is recorded as
   dropped in the variance summary on the author's answer, never silently. The reports of
   reveals owed and not shown, threads and Part 30 functions at this boundary are information and
   never block (Rule 9.7.4). Then ask the one confirmation, "Has this Novel-Part finished?" (the
   completion flow's question for the Novel-Part, with the facts shown beside it: the closing
   state the Novel-Part Spec planned, the Part 30 functions it carried, any Chapter entry with no
   Chapter Spec, anything still open; a yes also stands for the last Chapter's completion
   confirmation, which is not asked again). On "Not yet" nothing is written and the command
   stops (Rule 9.7.3). The new specs' carry-in reads these completion pieces as drafted here:
   nothing is written until the last confirm (step 3). The consultation of steps 2 and 3
   begins only after that yes.
2. **Novel-Part Spec** — run the `/part-spec` **build** flow for the new Novel-Part (Part 38
   Area 11; clarity to the termination test of Rule 38.13), through `[CONFIRM SPEC]`. It reads
   the whole Section Spec; the Novel-Part's entry in the Section Spec (purpose, calendar window,
   the Part 30 functions it carries, who carries it, opening state, hand-off and its high-level
   Chapter list) pre-fills the draft; settled items of the Section Spec are carried in
   and not re-asked (Rule 9.5.1); every Chapter of the Novel-Part is listed in depth, with the
   direction questions asked at Novel-Part grain. The Novel-Part window and each Chapter window are
   written as dates plus Phase Day (Part 41 Area 4), and the carry-in names the last dated moment of
   the closing Novel-Part, read from the calendar ledger's Current Position block (Part 41 Area 9).
   The file and its registry row (its Coverage
   cell included, Rule 1.2.2) are written at that `[CONFIRM SPEC]` (Rule 9.4.4), and in that same
   step, top-down, the Section Spec first receives a variance note for each departure from what
   its entry fixes (purpose, calendar window, hand-off) and for a changed Chapter list (Rules
   11.4.3 and 9.4.5); the author chooses, per departure, to amend the Section Spec through
   `/section-spec revise` or to keep the original as the plan baseline. If the new Novel-Part's
   Novel-Part Spec already exists — built ahead on request (Part 38 Rule 9.2.2), or surviving a rewind, a
   reset or a redraft (Part 38 Rule 7.1.1; Rule 9.8.1) — do not build it blind: compare its
   built-against stamp with the record
   (Rule 9.2.3) and run the `/part-spec` **revise** flow, re-asking ONLY the items the story has
   moved, each as a clarity-reduction question showing the original answer and the source of the
   change (Part 38 Rule 4.2.4), and re-confirm what survives. The Novel-Part's working name is a
   label here; the name is established in the Chapter Spec header and the delivered files.
3. **Chapter Spec** — run the `/chapter-spec` **build** flow for the new Novel-Part's first
   Chapter (a new Novel-Part's opening Area is also a new Chapter's, so the same obligation
   binds here as in `/next-chapter`; Part 38 Story Specification Law;
   `.claude/guardrails/ledger/guardrail-story-spec-law.md`), from its entry in the confirmed
   Novel-Part Spec (which pre-fills the Chapter header; both upper specs are read in full),
   through `[CONFIRM SPEC]`, establishing the Chapter's title, purpose, Area breakdown and each
   Area's block (Part 38 section 2.4: its size target of 1,600, 1,800 or 2,000 words, its
   pacing, whether it is a complete scene or continues a scene across Areas, opening and closing
   type, carry-over, thread and the other fields listed there) —
   BEFORE any Area is planned or drafted. If the Chapter Spec already exists and is confirmed,
   run `/chapter-spec` **revise** and re-confirm what survives, as `/start-story` does.
   **On this last `[CONFIRM SPEC]`, one write step:** first the variance note of any departure of
   the new Chapter Spec from its entry, written top-down (the Section Spec, then the Novel-Part
   Spec; Part 38 Rule 9.4.5); then the new Chapter Spec file and its registry row; then, bottom-up, the
   completion of the outgoing specs — the last Chapter's completion
   pieces (and `COMPLETED` if not yet set) and the Novel-Part's (`COMPLETED` and its completion
   pieces) — with their registry rows (Status and Last Updated; the Coverage cells of the
   Novel-Part and Section rows, refreshed because this is a completion write step, Rule 1.2.2;
   never at Gate 2). **On `[SKIP SPEC]`** at
   step 2 or step 3 the spec of that level is saved as `DRAFT`, the chain stops there, and
   neither outgoing spec is completed; `/next-part` is run again (Part 38 Rule 9.1.1).
4. Run `/next-area` for the new Novel-Part's opening Area, with
   `--first-of-chapter` (the writer's `is_first_area_of_chapter`) and the new novel_part_name passed through (the working label
   from the Novel-Part Spec header; it stays `proposed` in the Chapter Spec header until Gate 1
   delivers it, Part 38 Rule 3.6.1 item 1). Once the Chapter Spec is confirmed, the only
   questions left to Plan Mode are those of `/next-area` Step 0; the Area's size target and
   pacing are carried from the Chapter Spec and are not asked again.

## Failure/abort

Stop and surface it rather than proceeding if: the Section Spec or any link of the closing
chain is not `CONFIRMED` or `COMPLETED`; the Section Spec has no entry for the next Novel-Part
(the author chooses `/next-section` or `/section-spec revise`; adding a Novel-Part is a
substantial amendment, Part 38 Rule 9.4.2, and there is no light add); any other Chapter Spec of the
closing Novel-Part is not `COMPLETED` or lacks its variance annotations; or the author answers
"Not yet" to "Has this Novel-Part finished?" (nothing written; run again later, and the
question is asked again).

Do not pass the closing Novel-Part's arc threads over silently: every thread left unresolved
is put to the author as above (carried on, resolved, or marked lapsed on the author's
answer), and the report of them is information that never blocks by itself (Part 38 Rule 9.7.4). Under
`[SKIP SPEC]` the drafted spec is saved as `DRAFT`, the chain stops, the new Novel-Part stays
blocked for `/next-area` (Rule 9.1.1), and the outgoing specs are left as they were; run
`/next-part` again and it revises what was confirmed or saved rather than building it blind.
If the Chapter build shows that the Novel-Part Spec confirmed in this run needs a substantial
change, ask it as a question, never settle it silently; the author's answer is noted as a
variance on every spec above the Chapter (Part 38 Rule 9.4.5) and, where the author amends the plan, the
higher spec is changed through its own command (Rule 9.4.2); a substantial change stops the run
at that level until `/part-spec revise` (or `/section-spec revise`, where it is the Section
Spec's own plan that moves) has been confirmed.
