---
description: Advance to the next Section (one of Phase 1's 8 locked Sections) -- complete the closing Section's specs, build the new Section's spec chain (Section Spec, first Novel-Part Spec, first Chapter Spec), then write its opening Area including title-page handling.
user-invocable: true
---

# `/next-section`

Corresponds to canon command `[NEXT SECTION]` (C-8). Phase 1 has exactly 8 Sections, locked
per Part 30 — confirm which Section is next against `narration-novel-macro-story-law`
(Area 2 — Phase 1 Narrative Arc Map) rather than assuming.

A new Section opens a new **spec chain** (Part 38 Rule 38.9, Area 9): the **Section Spec**
(`/section-spec`, C-40), then the **Novel-Part Spec** of the Section's first Novel-Part
(`/part-spec`, C-41; "Novel-Part Spec" is the formal name, so it is never read as the spec of a
canon "Part"), then the **Chapter Spec** of that Novel-Part's first Chapter (`/chapter-spec`,
C-39). This command builds all three, in that order, each through its own `[CONFIRM SPEC]`; no
Area is planned until all three are confirmed. It also completes the specs of the closing Section
(its last Chapter, its last Novel-Part and the Section itself).

## Preconditions

- Read `.claude/guardrails/commands/guardrail-plan-then-auto-execution.md` — it governs this
  command's Plan Mode → Auto Mode shape, default agent model/effort, mandatory parallelism,
  and milestone progress reporting, exactly as it governs the `/next-area` call this
  command delegates to.
- Read `.claude/guardrails/ledger/guardrail-story-spec-law.md` and `spec-story-specification-law`
  (Part 38 Areas 9 to 11): the chain rule (Rule 9.1.1), the clarity mandate that governs all
  three builds (Rule 38.13) and completion at the boundary (Rules 9.7.2 and 9.7.3).
- The Section Spec build reads the **whole** of `narration-novel-macro-story-law` every time
  (Rule 10.4.2); this command never shortens that read. Part 30 must hold an entry for the
  new Section. If it does not (`/section-spec` refuses, Rule 9.1.4), stop and say Part 30
  must be expanded first; nothing is started.

## Plan Mode → Auto Mode

Steps 0 to 5 are this command's **Plan Mode**: the questions and the finish confirmation of the
completion preparation (step 1), the two questions of the independent reader pass (step 2c),
the Check #21 questions of the Section-close review (step 2a), any ruling on a FAIL of the audit
chain (step 2b) and the three spec builds (steps 3 to 5, top-down, each through its own
`[CONFIRM SPEC]`). Apart from those, this command has no separate author-facing consultation
gate of its own. The reviews do not depend on each other's output, so the mandatory-parallelism
binding means they are launched together as concurrent background agents in a single message,
not issued one after the other (see below).

Once the finish confirmation is a yes, every Check #21 question and audit-chain FAIL is ruled
and the Chapter Spec of step 5 is confirmed, **Auto Mode** begins: step 6 proceeds straight
into `/next-area`, which runs its own full Plan Mode → Auto Mode cycle (Decision Consultation
Gate through Gate 2 confirmation) independently and in full — this command neither shortens
nor restates it. Auto Mode never waives a `[CONFIRM SPEC]`: each of the three is a hard pause,
and only ONE confirm prompt is open at a time. Each prompt names the artifact and its
reference: "Section Spec 1.2", "Novel-Part Spec 1.2.1", "Chapter Spec 1.2.1.001".

## Parallel orchestration

Per `guardrails/commands/guardrail-plan-then-auto-execution.md` (absolute binding; Part 38 Rule 9.9.3).

- **At command start, once step 0 passes, launch together in one message:** (a) the
  completion preparation of the closing Section's last Chapter, last Novel-Part and the
  Section (outline-planner, step 1); (b) the grounding of the three builds — one
  outline-planner per level (Section Spec, Novel-Part Spec, Chapter Spec), each reading the
  whole chain above its level and told to report open branch points, *not* to finalize;
  (c) area-scorer for the closing Section's CDL-2 running aggregate (step 2) and, through the
  `/chapter-spec` complete flow, the Chapter-Level CDL-2 Aggregate Block of the closing Chapter;
  (d) continuity-checker for the Section-close review (step 2a) and, as a separate instance,
  one pre-read (Locked Canon, Part 30 locks, Entity Naming Law, ledgers, the closing Section's
  specs) that serves the light audit of all three new specs. The session-end audit chain (step
  2b) is launched the moment its inputs exist (steps 2 and 2a done), not later.
- **Consultation and confirmation run strictly top-down** — Section Spec, then Novel-Part Spec,
  then Chapter Spec — because each consumes its parent's confirmed answers. When a parent is
  confirmed, tell the next planner so via `SendMessage` and let it finalise.
- **Question streams are separate** and never share one `AskUserQuestion` call: the completion
  questions and finish confirmation, the two questions of step 2c, the Check #21 questions, any
  audit-chain FAIL ruling, and each spec's consultation. The streams may take turns between calls.
- **Ordering that cannot be parallelised:** the finish confirmation comes first of the
  author-facing questions that change anything (a "Not yet" writes no spec and no ledger); the
  Check #21 ledger writes of step 2a and the report of step 2b are in BEFORE the Section Spec's
  light audit runs (its carry-in item reads the ledgers, Part 38 Rule 10.5.1); and each new spec's file
  is written only at its own `[CONFIRM SPEC]`.

## Sequence

0. **Icon check.** The new Section's first Area opens with the Title Page, which holds the Phase image
   and the Section image (Part 2 Rule 6.3.1b). Check that
   `projects/novel-starward-saga/phase-N/phase-icon.png` and
   `projects/novel-starward-saga/phase-N/section-M/section-icon.png` exist, N being the Phase and M the
   new Section. If one is missing, stop and run `/create-image-phase N` or `/create-image-section N M`
   first; nothing else in this command starts until both exist. Then the **chain check** (reads
   only): the closing Section's Section Spec, its current Novel-Part Spec and its current Chapter
   Spec must each be `CONFIRMED` or `COMPLETED` (Part 38 Rule 9.1.1); a link that is `DRAFT`,
   `AMENDED-PENDING-RECONFIRM`, `RETIRED` or missing stops the command and names the command to
   run (`/section-spec`, `/part-spec` or `/chapter-spec`). Part 30's 8-Section lock and its entry
   for the new Section are checked here too.
1. Invoke **outline-planner** to confirm the closing Section's Novel-Parts/Chapters are
   complete and to prepare the completion of the three outgoing specs, bottom-up. Every
   Chapter Spec and every Novel-Part Spec of the closing Section other than the last of each
   must already be `COMPLETED` and variance-annotated (completed at their own `/next-chapter`
   and `/next-part`); every Area row of the last Chapter must be terminal (`WRITTEN`, or
   `DROPPED` with a variance note). The three completions are:
   - the last Chapter's completion (the `/chapter-spec` **complete** flow: its checks and its
     questions to the author, with the drafted final variance summary, Reader now knows line,
     Chapter digest and New-named-things line; nothing is written yet);
   - the last Novel-Part's completion (Part 38 Rule 9.7.3 and Rule 11.7.1: the planned-versus-as-written
     variance summary including Chapters added or dropped, the Reader now knows line by
     reference to the last Chapter's line plus Novel-Part additions, the digest, and the
     threads and setups carried on to the next unit);
   - the Section's completion (Rule 10.6.1: the same pieces at Section grain, including
     Novel-Parts added or dropped and the Part 30 functions the Section carried).

   Every unresolved `[OPEN]` item (found in the Audit and Settlement Notes section of each spec),
   every setup planted with no payoff and every unresolved
   cliffhanger or thread is put to the author at the right level through `AskUserQuestion`:
   resolve it, carry it on to the new Section's specs, or mark it lapsed; a setup or thread
   is marked lapsed only on the author's answer (Part 38 Rule 9.7.3). An entry or a Novel-Part the
   story never reached is recorded as dropped in the variance summary on the author's
   answer, never silently. The reports of reveals owed and not shown, threads and Part 30
   functions at this boundary are information and never block (Rule 9.7.4). Then ask the one
   confirmation, "Has this Section finished?" (the completion flow's question for the Section;
   a yes also stands for the last Novel-Part's and the last Chapter's completion
   confirmations, which are not asked again). On "Not yet" no spec and no ledger is written,
   the reviews already launched are set aside, and the command stops (Part 38 Rule 9.7.3). The new specs'
   carry-in reads the completion pieces as drafted here:
   nothing is written until the last confirm (step 5). Section-open is the natural point to look
   at the CDL-2 readings: the new Section's Chapter Specs may carry CDL-2 emphasis where the
   author wants it, and the Anchor Floor lines are information only.
2. Launched together with step 1, invoke **area-scorer** to finalize the closing
   Section's CDL-2 running aggregate (its tracker,
   `.claude/story-memory/cdl2-density-tracking/phase-N/section-M-aggregate.md`) before moving
   on (the readings are shown with it as information; an Anchor Floor reading never holds the
   Section open). The new Section's tracker does not exist yet: the scorer creates it at that
   Section's first scored Area (step 6), from the headings of the closing Section's tracker file.
2a. Launched together with steps 1 and 2, invoke **continuity-checker** for the Section-close
   review of the closing Section: Check #21's Section-close behavior review (Part 39 Area 44.2:
   the characters whose profiles the Areas show moving, with the deferred questions
   presented together) and the Section-close POV report (Part 38 Rule 3.7.2: the written
   Areas by viewpoint, per protagonist; informational, computed from the
   Areas written and never stored), together with the threads off the page past the stretch
   the author set and the setups still open (Rule 3.7.2), the Owed Beats line (Part 39
   Rule 39.41.5.2; report-only) and the spec chain's Section-level report (reveals owed and not
   shown, and the Part 30 Major Narrative Functions the Section carried, read against the
   Section Spec; information only, Rule 9.7.4). The POV report, the Owed Beats line and the
   chain report are shown to the author. Each Check #21 question goes to the author through
   `AskUserQuestion` with the checker's recommended ruling (Part 39 Rule 39.44.4.1), once the
   finish confirmation of step 1 is a yes; a review that finds none of D-1 to
   D-4 and no unmapped trigger reports SILENT and asks nothing. An open question blocks step 6
   exactly as it blocks a Gate 2. No Gate 2 exists here, so each ruling is written at once by
   a continuity-checker ledger instance (Part 39 Rule 39.44.4.2), and those writes land before
   the Section Spec's light audit (step 3).
2b. Once steps 2 and 2a are done (the ledger writes of 2a are in), invoke
   **continuity-checker** for the session-end audit chain on the closing Section; it waits for
   no spec step. The close of a Section is the session end (`audit/guardrail-fcia.md`), so this
   step runs FCIA end-of-session and ALCA Mode B (`audit/guardrail-alca.md`) together, as
   concurrent continuity-checker agents (they read different layers), then a Unified Audit
   Summary after both, logged to `.claude/story-memory/session-log/`, over the Areas of the
   closing Section (the Areas written since the previous Section closed, found from the
   written files and the spec chain, never from the session log). The chain reports and
   changes nothing: no agent edits a written Area file, and a finding that needs an Area
   corrected goes to the author, who may run `/revise-area` on it. Its report is in before the
   Section Spec's light audit runs (step 3), so a ruling that bears on the carry-in lands in the
   Section Spec before it is confirmed. A FAIL the author has not ruled on blocks step 6, as an
   open Check #21 question does.
2c. Independent reader pass on the closing Section (area-scorer charter, Section close). Once
   the finish confirmation of step 1 is a yes, ask the author through `AskUserQuestion` which
   model the pass runs on (the author names it) and which three Areas of the closing Section
   it reads (its own call, apart from every other question stream). When the answers arrive,
   invoke **area-scorer** on that model through the model override of
   `guardrails/commands/guardrail-plan-then-auto-execution.md`; this model applies to this one
   pass only and does not carry to later calls; the pass does not wait for
   steps 1, 2, 2a or 2b. Report-only: its report is shown to the author, and it changes
   nothing and blocks nothing.
3. **Section Spec** — run the `/section-spec` **build** flow for the new Section (Part 38
   Area 10; clarity to the termination test of Rule 38.13), through `[CONFIRM SPEC]`, once the
   finish confirmation of step 1 is a yes. It reads the whole of Part 30, prints what Part 30
   expects of this Section in chat, asks the Part 30 `OPEN-AUTHOR` rows due in or planted by
   it, asks the Section's own Epigraph (the line for its title page; never written by an agent) and
   expands the Section into its Novel-Parts and, at high level, their Chapters, with the
   themes, direction and opening questions asked at Section grain. Its light audit runs after
   the Check #21 ledger writes of step 2a and the report of step 2b are in. The file and its
   registry row are written at that `[CONFIRM SPEC]` (Part 38 Rule 9.4.4). Its Section window and each
   Novel-Part window are written as dates plus Phase Day (Part 41 Area 4, Phase Day conversion and
   Section windows), and its carry-in names the last dated moment of the closing Section, read from
   the calendar ledger's Current Position block (Part 41 Area 9). If the new Section's
   Section Spec already exists — built ahead on request (Rule 9.2.2), or surviving a rewind, a
   reset or a redraft (Part 38 Rule 7.1.1; Rule 9.8.1) — do not build it blind: compare its
   built-against stamp with the record (Rule 9.2.3) and run the `/section-spec` **revise**
   flow, re-asking ONLY the items the story has moved, each as a clarity-reduction question
   showing the original answer and the source of the change (Part 38 Rule 4.2.4), and
   re-confirm what survives.
4. **Novel-Part Spec** — run the `/part-spec` **build** flow for the Section's first Novel-Part
   (Part 38 Area 11), from that Novel-Part's entry in the confirmed Section Spec (which
   pre-fills the draft; the Section Spec is read in full), through `[CONFIRM SPEC]`: every
   Chapter of the Novel-Part listed in depth, with direction questions asked at Novel-Part
   grain. Settled items of the Section Spec are carried in and not re-asked (Rule
   9.5.1). The file and its registry row are written at that `[CONFIRM SPEC]`; every departure
   from the Section Spec's entry, and every changed Chapter list, is noted as variance on the
   Section Spec whatever the author's answer (original left as the plan baseline, or plan
   amended; Part 38 Rules 9.4.5 and 11.4.3), written first, top-down, in the same write step. Where the
   author chose to amend the Section Spec, that change is made only by `/section-spec revise`
   (Rule 9.4.2), which `/part-spec` offers to run straight after the write; the Novel-Part Spec is
   still written `CONFIRMED`, never `DRAFT` because of that answer, so the chain goes on. The same
   already-exists rule applies as in step 3 (`/part-spec` **revise**, stamp re-check).
5. **Chapter Spec** — run the `/chapter-spec` **build** flow for that Novel-Part's first
   Chapter (a new Section's opening Area is also a new Chapter's), from its entry in the
   confirmed Novel-Part Spec (which pre-fills the Chapter header; the Section Spec and the
   Novel-Part Spec are both read in full), through `[CONFIRM SPEC]`, establishing the
   Chapter's title, purpose, Area breakdown and each Area's block (Part 38 section 2.4: its
   size target of 1,600, 1,800 or 2,000 words, its pacing, whether it is a complete scene or
   continues a scene across Areas, opening and closing type, carry-over, thread and the other
   fields listed there) — BEFORE any Area is planned or drafted. If
   the Chapter Spec already exists and is confirmed, run `/chapter-spec` **revise** and
   re-confirm what survives, as `/start-story` does. **On this last `[CONFIRM SPEC]`, one write
   step, bottom-up:** the new Chapter Spec file and its registry row, then the completion of
   the outgoing specs — the last Chapter's completion pieces (and `COMPLETED` if not yet set),
   the last Novel-Part's (`COMPLETED` and its completion pieces) and the Section's
   (`COMPLETED` and its completion pieces) — with their registry rows (Status and Last
   Updated; the Coverage of the Novel-Part and Section rows is refreshed at this completion
   write step, as at a spec's own confirm and at a reset or rewind rollback, and never at
   Gate 2; Part 38 Rules 1.2.2, 10.1.2 and 11.1.2). The calendar ledger's Section row is not touched here: its Status
   became `CLOSED` when Gate 2 confirmed the Section's closing Area (Part 41 Area 9, The calendar
   ledger), and `/section-spec` **complete** never sets it. The variance notes the builds append to a higher
   spec (Rule 9.4.5) are written in their own build's write step, top-down: the Section Spec
   first, then the Novel-Part Spec, then the lower spec itself. **On `[SKIP SPEC]` at any of
   steps 3 to 5** the spec of that level is saved as `DRAFT`, the chain stops there, and none of
   the outgoing specs is completed; `/next-section` is run again (Rule 9.1.1).
6. Run `/next-area` for the new Section's opening Area, with
   `--first-of-section` (the writer's `is_first_area_of_section`; Section title page and epigraph per Part 2 Rules 6.3.1b
   and 7.2.1a; the writers' `--section-epigraph-file` argument is the Epigraph line of the new
   Section's own Section Spec, Part 38 Rule 10.3.1, and `unset` means none; only a Phase's first
   Area also prints the Part 30 Phase epigraph, above Section 1's own line, which is not this
   command's case) and `--first-of-chapter` — a new Section's opening Area is
   simultaneously its first Chapter's opening Area. Once the Chapter Spec is confirmed, the only
   questions left to Plan Mode are those of `/next-area` Step 0; the Area's size target and
   pacing are carried from the Chapter Spec and are not asked again.

## Failure/abort

Stop and surface it rather than proceeding if: the 8-Section lock would be exceeded (that
is `/next-phase`, not this command; `/next-phase` runs the Section-close reviews and the
completions of Section 8 itself); Part 30 holds no entry for the next Section (expand
Part 30 first); a spec of the closing Section's chain is not `CONFIRMED` or `COMPLETED`; any of
the closing Section's other Chapter Specs or Novel-Part Specs is not `COMPLETED` or is
missing its variance annotations; the author answers "Not yet" to "Has this Section
finished?" (nothing written; run again later, and the question is asked again); a Check #21
question from the Section-close review is still open; or the audit chain of step 2b reports a
FAIL the author has not ruled on. Under `[SKIP SPEC]` at any of the three confirm gates the
drafted spec is saved as `DRAFT`, the chain stops there, the new Section stays blocked for
`/next-area` (Part 38 Rule 9.1.1), and the outgoing specs are left as they were; run `/next-section`
again and it revises what was confirmed or saved rather than building it blind. If a lower
build shows that a spec confirmed earlier in this run needs a substantial change (a conflict
with the Section Spec found while building a Novel-Part Spec, for example), ask it as a
question, never settle it silently; a departure is noted as variance on every spec above it,
top-down, whatever the author's answer (Part 38 Rule 9.4.5), and a change to a higher spec's plan is
made only by that spec's own revise flow (Rule 9.4.2), so a substantial change stops the run at
that level until `/section-spec revise` or `/part-spec revise` has been confirmed. An Anchor
Floor reading below its line is shown with the Section-close report as information (the value,
the line and the margin); it does not stop the advance and raises no question
(`guardrails/quality/guardrail-threshold-consultation.md`).
