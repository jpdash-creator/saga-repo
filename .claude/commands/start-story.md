---
description: Begin the Starward Saga from a clean state -- build the spec chain, then write Chapter 1 of Phase 1, Section 1, Novel-Part 1 whole with /create-chapter (or its Area 1 with /next-area when asked or when the Build mode is by-area).
user-invocable: true
---

# `/start-story`

Corresponds to canon command `[START STORY]` (C-3). Use only when `projects/novel-starward-saga/`
has no written Area (a true fresh start) or immediately after `/hard-reset`.

Before any Area is written it builds the whole spec chain for the opening of the story, top-down: the
Section Spec of Section 1, the Novel-Part Spec (`/part-spec`) of Novel-Part 1 and the Chapter Spec of
Chapter 1 (Part 38 Areas 9 to 11). Each is built through its own command flow and confirmed with its
own `[CONFIRM SPEC]`. No spec of the chain is assumed to exist until it is built or revised here.
After the Chapter Spec is confirmed the story proceeds to `/create-chapter` by default; `/next-area` runs
only on request or when the spec's Build mode is `by-area` (step 5).

## Preconditions

Read `.claude/guardrails/commands/guardrail-plan-then-auto-execution.md` alongside the
guardrail index (step 2 below); it governs this command's Plan Mode to Auto Mode shape,
default model/effort, mandatory parallelism, and milestone progress reports exactly as
it governs `/next-area`.

## Sequence

0. **Dependency preflight.** Run `python -c "import docx"`. If it fails, stop and print the install line
   `pip install -r .claude/tools/requirements.txt`; the consultation does not begin until the import succeeds.
0a. **Icon preflight.** Area 1 is the first Area of Phase 1 and of Section 1, so its Word file opens
   with the Title Page, which holds both images (Part 2 Rule 6.3.1b). Check, under the repo root
   (the folder that holds `.claude/`), that `projects/novel-starward-saga/phase-1/phase-icon.png` and
   `projects/novel-starward-saga/phase-1/section-1/section-icon.png` exist. If one is missing, stop
   and run `/create-image-phase 1` or `/create-image-section 1 1` first; the consultation does not
   begin until both exist.
1. Confirm `projects/novel-starward-saga/phase-1/` has no `area-NN.docx` or `area-NN.md` file anywhere under it; if it does,
   stop and ask whether the intent was `/next-area` instead.
2. Read `.claude/guardrails/_index.md` in full, plus the consolidated primary reads that
   establish how a story opens: `narration-novel-book-structure-law` (five-tier structure),
   `narration-novel-macro-story-law` (macro arc / Phase 1 framework; read whole, because the
   Section Spec build reads the whole Part 30 file every time, Part 38 Rule 10.4.2), and
   `narration-novel-creative-flexibility-law` (creative flexibility); and
   `.claude/guardrails/ledger/guardrail-story-spec-law.md` with `spec-story-specification-law`
   (Part 38, Areas 9 to 11: the spec chain).
3. **Plan Mode: the order of the questions.** The author is asked for the Section Spec first,
   then the Novel-Part Spec, then the Chapter Spec, in that order (Part 38 Rule 9.1.1). There is no
   separate up-front narrative-direction round: the direction questions are asked inside the three
   builds, each at the level where the author's answer first changes that level's own plan (Part 38
   Rule 9.6.2): themes and the direction of the Section and of the Novel-Part in the Section Spec and
   the Novel-Part Spec, the opening beat of the book in the Chapter Spec. Nothing is left unasked (Part
   38 Rule 38.13). Do not under-consult in any of them just because this is the first invocation of the
   session: the opening of the entire novel typically has real, high-consequence open branches (which
   thread or character opens the book, what the opening beat is). Area 1's pacing and size target are
   not asked here or at writing time: the Chapter Spec decides them for every Area, in step 4c. Steps
   3 and 4 together are this command's Plan Mode boundary: every author-facing question is asked and
   resolved across them before Auto Mode begins at step 5. Each of the three builds is a Plan Mode of
   its own inside that boundary, and the `[CONFIRM SPEC]` token of each is a hard stop.
4. **The spec chain build (Part 38 Areas 9 to 11), top-down.** Build the chain for Phase 1,
   Section 1, Novel-Part 1, Chapter 1 before any Area is written, in this order, each through its own
   command flow and its own `[CONFIRM SPEC]` / `[REVISE SPEC]` / `[SKIP SPEC]` (the three tokens
   are shared by all three spec kinds). The build below starts only after the one above it is
   `CONFIRMED` (Part 38 Rule 9.1.1), and only one confirm prompt is open at a time; each prompt,
   session-log line and registry row names the artifact and its reference.
   - **(4a) Section Spec 1.1**: the `/section-spec` **build** flow for Phase 1, Section 1
      (file `.claude/story-memory/phase-section-part-chapter-area-specs/phase-1/section-1/section-1-spec.md`).
      It reads the whole Part 30 SKILL.md, prints in chat what Part 30 expects of the Section
      (Locked and Negotiable marked), and expands those expectations into the Section's
      Novel-Parts and Chapters at high level through its consultation. Section 1's Section Spec
      carries its own Epigraph line, asked in this build as in any Section's, in addition to the Phase
      epigraph, which is a line of Part 30: the title page of Area 1 prints both (Part 38 Rule 10.3.1).
      It surfaces every Part 30 `OPEN-AUTHOR` row due in or planted by the Section (Rule 10.4.3).

      **Both epigraph lines are asked once, inside this build.** Section 1's own Epigraph is a line
      of the Section Spec and is asked in `/section-spec` topic 12 like any Section's. The Phase
      epigraph is the `Epigraph:` line of Phase 1 in Part 30 (`narration-novel-macro-story-law`),
      and it reads `unset` until the author gives the text. `/section-spec` asks that question in
      the same topic 12 (what the line reads now, and whether to give or change it, with a
      repeat-back before the one-line Part 30 edit); `/start-story` asks nothing of its own, so the
      author is never asked twice. No agent ever writes or suggests either text. The writers get
      both lines in step 6.
   - **(4b) Novel-Part Spec 1.1.1**: the `/part-spec` **build** flow for Novel-Part 1 of
      Section 1 (file `.../phase-1/section-1/part-1/part-1-spec.md`). It reads the whole Section
      Spec, is pre-filled from the Section Spec's entry for Novel-Part 1 and lists every Chapter
      of the Novel-Part in depth (Part 38 Area 11).
   - **(4c) Chapter Spec 1.1.1.001**: the `/chapter-spec` **build** flow for Chapter 1 (file
      `.../part-1/chapter-001-spec.md`). It reads the Section Spec and the Novel-Part Spec and is
      built from the Novel-Part Spec's entry for Chapter 1 (Part 38 Rule 9.3.1); its Area-block
      consultation is included: the scene anchors, pacing, size target (1,600, 1,800 or 2,000 words)
      and opening and closing type of every Area of Chapter 1 are settled here, not at writing time.

   Every window in the chain is written as dates plus Phase Day, converted by Part 41 Area 4 (Phase Day
   conversion and Section windows). The story opens on Day One: Phase Day 1 is Year 1247, Ilovany,
   Orvil, Day 1, the first day of spring (the third weekday), and the three builds plan from it.

   Every build runs its own command's clarity mandate in full (Part 38 Rule 38.13): no unasked
   branch at that spec's own level, the final sweep by outline-planner and continuity-checker,
   the author's explicit "nothing further to steer" answer, then the confirm token. Calling a
   command from here never shortens its build, and no shortened form of a build exists.
   What the author settles in a spec settles on that spec's own `[CONFIRM SPEC]` (Rule 4.1.1) and
   is not re-asked in the builds below it: it is carried into the Chapter Spec's Audit and
   Settlement Notes as an Inherited note naming its source spec (Part 38 Rule 9.5.1); an answer the
   author skipped is recorded there as a Skipped note, with the planner's choice, and settles nothing; a
   matter the author chose to leave to the writing is carried into the Chapter Spec as a Deferred note
   naming the deferral and is asked at the Area's own consultation (Rule 9.5.2).

   **A link that already exists is revised, never rebuilt blind.** If any link of the chain
   already exists (for example specs that survived `/reset-story` with statuses rolled back, a
   `DRAFT` left by an earlier `[SKIP SPEC]`, or a Section Spec or Novel-Part Spec built ahead with
   `/section-spec build` or `/part-spec build`), that link is taken through its command's
   **revise** flow, top-down, and what survives is re-confirmed with its own `[CONFIRM SPEC]`
   (consultation scoped to what changed). A link built ahead carries a built-against stamp, which
   is checked against the ledgers as they stand and only the items it affects are re-asked, with
   the original answer shown (Part 38 Rule 9.2.3, Rule 4.2.4). `/hard-reset` deletes every spec of all
   three kinds (Part 38 Rule 7.1.2), so after one there is nothing to revise and the whole chain
   is a fresh build.

   **A `[SKIP SPEC]` at any level stops the chain at that level** (Rule 9.1.1): the drafted spec
   is saved as `DRAFT` by its own command, nothing below it is built, no Area is planned or
   drafted, and `/start-story` can be run again; it then takes the saved `DRAFT` through the
   revise path above. No Area is planned or drafted until all three specs are confirmed.
5. **Auto Mode begins; choose the writer by Build mode.** After `[CONFIRM SPEC]` of Chapter 1's spec,
   proceed by default to `/create-chapter` for Chapter 1 (Build mode `whole`, the default for a new spec):
   it writes the whole Chapter in one cycle, with its own Plan Mode, Gate 1 and Gate 2, and its Chapter file
   is the first Chapter of Phase 1 and of Section 1, so it receives the same two epigraph lines as step 6
   describes, read from their files and passed as `--phase-epigraph-file` and `--section-epigraph-file` to
   `chapter_builder.py`. In that case steps 5 (the per-Area plan) and 6 below do not run; `/create-chapter`'s
   own sequence replaces them. Proceed to the Area path below (`/next-area`) only when the author asks for it
   or the Chapter Spec's Build mode is `by-area`. The Area path follows.

   **Area path.** Invoke **outline-planner** to plan Area 1 (the opening Area of Chapter 1),
   using the confirmed Chapter Spec, which carries everything the chain settled, with its Area 1
   row and block from step 4 (scene anchors, pacing, size target, opening type). This is a per-Area
   plan, so the planner reads the Chapter Spec in full and, of the Novel-Part Spec, its header block
   and its closing-state block only; the Section Spec is not in that read set (Part 38 Rule 9.9.2).
   **Single-Area scope applies**: this plans exactly one Area
   (`phase-1/section-1/part-1/chapter-001/area-01`); the Area that follows is planned after
   reading it, in its own `/next-area` cycle, never planned or drafted together with Area 1.
6. Proceed exactly as `/next-area` from step 0 onward (the consultation, then draft -> Gate 1 ->
   confirm -> Gate 2 -> ledger update -> score) for that single Area, including the Gate 1 presentation
   of `/next-area` Step 4, in the order it sets (the Position Header Block with the full
   five-tier name chain first, the full text of the Area printed verbatim in chat, then the
   audit report and the prompt; no extra wrapper commentary; one Area presented at a
   time). Auto Mode never waives Gate 1's confirmation token; that stop
   remains mandatory. Area 1 is the first Area of Phase 1 and of Section 1, so when it is written
   the writers receive TWO epigraph lines: as `--phase-epigraph-file`,
   the Phase epigraph, the text of the `Epigraph:` line of Phase 1 in Part 30 as it stands after step 4a,
   and as `--section-epigraph-file`, Section 1's own Epigraph line from the header block of its
   Section Spec as confirmed in step 4a. This command reads both from their files at this step and
   passes the text only, as `/next-area` Step 5 sets out; the title page prints the Phase line
   first and Section 1's line second. Chapter 1's spec is not a source. `unset` means none for
   that line, and the writers are then called without its flag.
   Every Area file carries the Area Title Block, so the Title Block read-back of `/next-area` Step 5
   runs with `--expect present` and its printed result goes to the Post-Write Audit instance.
   **Area 1 carries Day One's date** (Part 41 Areas 4 and 5): its text begins with
   `*Year 1247, Ilovany, Orvil, Day 1*`, Phase Day 1 (the third weekday; Part 41 Area 3; the same date
   holds where Area 1 opens in the last dark hour and runs on into Day One's dawn, Part 41 Area 2, the
   one scoped exception to the dawn-to-dawn day), unless the confirmed Chapter Spec plans Area 1 as a
   `flashback, memory, dream or vision`, when the line carries the remembered date or the night
   dreamed instead (Part 41 Area 5). The line sits directly under the Title Page and Title Block (the
   `.docx` writer sets it as a centred, smaller italic line and gives the drop cap to the first
   paragraph of narration after it), and Gate 1 reads it against the Chapter Spec's in-story time for
   Area 1 as `/next-area` Step 3 sets out. The Gate 2 ledger instance writes the first calendar rows
   (the Phase, Section, Novel-Part, Chapter and Area rows and the Current Position block, which names the Open Chapter and the Open Chapter's recorded window, First to Latest), as
   `/next-area` Step 6 sets out.

## Parallel orchestration

Apply `/next-area`'s **Parallel orchestration (speed policy)** throughout, as an absolute
binding rather than a convenience; see
`guardrails/commands/guardrail-plan-then-auto-execution.md`:

- **At the end of step 2, before the first question is put,** launch together as background
  agents: one **outline-planner** grounding for each of the three levels this command builds
  (one planner per level, never one agent building two levels), and one **continuity-checker**
  pre-read (Locked Canon, Entity Naming Law, Part 30 locks and Section mandates, current ledger
  state) that serves the light audits of all three builds. The step 2 consolidated reads are
  batched as parallel tool calls. The Section planner grounds on the whole Part 30 SKILL.md; the
  two lower planners ground on everything that does not depend on their parent's answers.
- **Consultation and confirmation run strictly top-down** (Section Spec, then Novel-Part Spec,
  then Chapter Spec), never in parallel and never interleaved. Each lower planner is told by
  `SendMessage` that its parent is confirmed, reads that parent spec in full, and then
  finalizes; the author's answers are fed to each planner the same way, any new branch it
  surfaces feeds further rounds, and each planner carries through its own build rather than being
  re-grounded from scratch.
- The Gate 1 continuity-checker instances' Pre-Area Read and grounding (two instances, as
  `next-area.md` defines them) run in the background while area-maker drafts; and after the
  file writes, Gate 2 runs as the same 3-way parallel split defined in `next-area.md`
  (Post-Write Audit as one continuity-checker instance, Post-Write Ledger Update as a second
  separate continuity-checker instance, and area-scorer, all three launched together, not
  staged). The gate order itself is never reordered or skipped.

## Failure/abort

If written Areas already exist, do not overwrite silently; escalate via `AskUserQuestion`.

`[SKIP SPEC]` at any of the three levels stops the chain there as step 4 says: the spec is saved
`DRAFT`, nothing below it is built, and nothing is planned or drafted until the chain is confirmed.
If Part 30 has no Section entry for Section 1, `/section-spec` refuses and says Part 30 must be
expanded first; a conflict between author intent and Locked Canon, or between a spec and an
established ledger fact, is escalated via `AskUserQuestion`, never force-written.
