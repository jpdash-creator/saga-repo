---
description: "Write a whole Chapter of the Starward Saga in one cycle from its confirmed Chapter Spec, with no per-Area files: one draft, one editing pass, Gate 1 audit, confirm, Gate 2 write, one batched ledger update, one CDL-2 score, as-built sync and completion."
argument-hint: "<chapter number> [section number] [part number] [phase number], each left out defaults to the current position"
user-invocable: true
---

# `/create-chapter`

Corresponds to canon command `[CREATE CHAPTER]` (C-42). It builds one **whole Chapter** from its confirmed
Chapter Spec in a single cycle. There are no Area files: the only output is the Chapter file pair in the
Novel-Part folder, written by `.claude/tools/chapter_builder.py` (authorized script 6) in `--mode whole`:

```
projects/novel-starward-saga/phase-P/section-S/part-N/Chapter NNN - <Chapter Name>.md
projects/novel-starward-saga/phase-P/section-S/part-N/Chapter NNN - <Chapter Name>.docx
```

This is a second lawful writer, not an exception. A Chapter is built EITHER by Area (`/next-area`, then
`/chapter-builder`) OR whole (`/create-chapter`), never both. `/next-area` still writes one Area per
invocation; this command writes one whole Chapter per invocation; neither batches Areas. The deprecated
shapes `[WRITE NEXT N AREAS]` and `[WRITE TO END OF CHAPTER]` stay deprecated.

The Chapter Spec's Area blocks stay the plan. Each Area block is written as a stretch of the Chapter at its
own size target and pacing, joined to its neighbours with no seam, and marked in the staged text and the
`.md` by a hidden line `<!-- AREA NN -->`. The `.docx` carries no marker.

## Preconditions

Read these first, in parallel:

- `.claude/guardrails/_index.md`, `.claude/guardrails/audit/guardrail-audit-gate-law.md` and
  `.claude/guardrails/commands/guardrail-plan-then-auto-execution.md` (Plan Mode to Auto Mode, default
  model and effort, mandatory parallelism, milestone progress reports; they govern this command end to end).
- `.claude/guardrails/ledger/guardrail-story-spec-law.md` and the Chapter Spec at
  `.claude/story-memory/phase-section-part-chapter-area-specs/phase-P/section-S/part-N/chapter-NNN-spec.md`.
- `.claude/guardrails/tools/guardrail-authorized-scripts-only.md`.

**Resolve the Chapter.** Defaults come from `/status`: with no argument, the Chapter that `/next-chapter` or
`/start-story` just confirmed, else the first Chapter in story order whose Chapter Spec is `CONFIRMED` and
unbuilt. A named Chapter is taken as named.

**Stop conditions.** Check in this order, name the first failure with its status and the command that fixes
it, write nothing, and stop:

1. **The chain is in force** (Part 38 Rule 9.1.1): the Chapter Spec is `CONFIRMED`, and its Novel-Part Spec
   and its Section Spec are each `CONFIRMED` or `COMPLETED`; none is `DRAFT`, `AMENDED-PENDING-RECONFIRM` or
   `RETIRED`. Read each status from its row in the registry `_index.md`. Check top-down and name the first
   missing or unconfirmed link with `/section-spec`, `/part-spec` or `/chapter-spec`. Never plan the Chapter
   ad hoc without the chain.
2. **The Chapter Spec is complete for a whole build.** Its header block carries `Build mode:` (must read
   `whole`), `Chapter pacing:` (Fast, Medium or Slow) and `Chapter size target (words):`; every Area block
   carries `Pacing (planned)`, `Size target` and its `Budget stretch:` line (none, or up to 0.72 of target
   with a one-line reason); and a `### 5.0 — Scene Map` exists in which every Area block belongs to a scene
   with a POV sequence, a scene arc, a scene pacing, a scene word budget, the visible-break rule and the
   join state at each Area seam. A Chapter Spec that lacks any of these is a **stop condition**: say which
   item is missing and direct the author to `/chapter-spec` (revise). A Build mode of `by-area` is also a
   stop: the Chapter is built with `/next-area`; the author changes the mode only through `/chapter-spec`
   (revise).
3. **The Chapter has no Area files and is not already built whole.** Look in
   `projects/novel-starward-saga/phase-P/section-S/part-N/chapter-NNN/` (never `_archive`) for any
   `area-NN.md` or `area-NN.docx`. If any exist, refuse, list them, and point to `/chapter-builder` (condense
   them into the Chapter file) or `/redraft-chapter` (archive and write afresh). Then look for
   `Chapter NNN - *.md` or `.docx` in the Novel-Part folder with Area rows of the spec already
   `WRITTEN(P.S.N.CCC)`: the Chapter is already built whole; point to `/revise-chapter` or
   `/redraft-chapter`. A Chapter file that exists with no Area files and an unbuilt spec is a stale or
   foreign file: show it and ask the author before going on; nothing is replaced without `--overwrite`.
4. **Dependency preflight.** `python -c "import docx"` succeeds; if not, print
   `pip install -r .claude/tools/requirements.txt` and stop. When the Chapter opens a Phase or a Section, the
   Title Page images exist (`projects/novel-starward-saga/phase-P/phase-icon.png`,
   `.../section-S/section-icon.png`); if one is missing, name `/create-image-phase` or
   `/create-image-section`.

**Read set.** The Chapter Spec in full; of the Novel-Part Spec, its header block and its closing-state block
only; the Section Spec is not read (the Chapter Spec carries every inherited item, tagged with its source;
Part 38 Rule 9.9.2). The one **previous text** is the Chapter file of the previous Chapter as written (its
last scene), or, when the previous Chapter was built by Area, the last Area file of that Chapter; the first
Chapter of the story has none. Read the Current Position block of
`.claude/story-memory/ledger-worlds-calendar/_index.md` (the Open Chapter and its recorded window, First to
Latest) and, for a scene that continues from the previous Chapter, the join state the Scene Map names. Pass
the Chapter Spec path, the Novel-Part Spec path and these references to every agent launched below.

## Word budget, pacing and size, read from the spec

Words, not characters. Each Area block has a size target T(a) in the Chapter Spec. The Chapter is written at
**55% to 60% of each Area block's target**, and the Chapter total target is T, the sum of the Area targets.
The allowed Chapter total is **0.55 T up to 0.72 T** (1.20 times 0.60 T). Only an Area block whose spec names
`Budget stretch: up to 0.72 of target` may exceed 60% of its target, never above 72%; no Area block goes
below 55%. A stretch the spec does not name is refused. Date lines, markers and scene-break marks are not
counted. The old 1,280 to 2,400 passing range of the Area rule is not applied to a whole-built Chapter. The
Chapter's pacing and each Area block's pacing shape the writing (Fast: tight, short beats; Medium: balanced;
Slow: fuller interiority, sensory and world detail) inside the same band; a pacing difference is shown,
never blocking. Read the figures in the Chapter Spec and the script's output rather than assuming them.

## Plan Mode to Auto Mode

Step 0 (the Decision Consultation Gate and the build-plan confirmation) is this command's **Plan Mode**:
every author-facing question this invocation will ever ask is asked and resolved (answered or explicitly
`[SKIP]`ped) before Step 1. Pacing, size and stretch are not asked: the Chapter Spec carries them. After
Plan Mode, Steps 1 to 10 run in **Auto Mode**: no discretionary question, straight through to the next
mandatory gate. Auto Mode never waives a required stop: the Gate 1 presentation and its confirmation token
(Step 6) stay a hard pause. A number crossing a stated line that is not the word band is information in the
audit report, never a question (`guardrails/quality/guardrail-threshold-consultation.md`). Questions that can
only be computed once a draft exists (a flow finding that needs the author, a Check #21 enquiry, a Tier D or
Tier C or D monster consequence flag) are asked mid-Auto-Mode with the Chapter's full text printed first.

## Parallel orchestration (speed policy)

The gate order is law; within it, run independent work concurrently. Absolute binding
(`guardrails/commands/guardrail-plan-then-auto-execution.md`).

- **Grounding (before and during Step 0):** read in parallel, in one batch, the previous text, the ledger
  entries of every entity the Chapter Spec names (character, location, faction, named items, Named Moves,
  monsters), the Current Position block, the skills the Chapter Spec's blocks call for, and the guardrails
  above. Launch **outline-planner** in the background at the moment the `AskUserQuestion` consultation is
  presented, to do its grounding reads and report open branch points, not to finalize a plan.
- **Drafting and editing are single and sequential.** One **area-maker** drafts the whole Chapter in one
  pass (Step 2); one **chapter-editor** then edits the whole draft in one pass (Step 3). Never two
  drafters, never two editors at once.
- **Gate 1 pre-read:** while the chapter-editor works, launch two **continuity-checker** instances in the
  background to do their grounding (guardrails, canon-manifest forced read, ledger state, the previous text,
  the Chapter Spec's blocks and Scene Map). When the edited text and its measure arrive (Step 5), send it to
  both: instance 1 runs the 23-check audit on the whole Chapter, instance 2 runs the flow review (Check #16
  dimension 16-J) over the whole Chapter and its joins. The forced-read discipline is unchanged. Keep both
  instances for the FAIL loop (Author ruling, 2026-10-18): the re-audit after fixes (Step 5, FAIL loop) goes to
  instance 1 by `SendMessage`, which resumes with its first-pass reads, and to instance 2 only when a finding
  came from the flow review or a fix touches a seam; the loop starts no fresh instance and repeats no grounding.
- **Gate 2 (Step 8):** after the script has written the files, launch three agents in one message:
  (1) **continuity-checker** for the Post-Write Audit only (read and report only, writes nothing);
  (2) a separate **continuity-checker** for the single batched Post-Write Ledger Update and the Chapter
  Spec as-built sync and completion; (3) **area-scorer** for the one CDL-2 block of the Chapter and the
  Section aggregate row. Their write sets stay disjoint (audit report only / `story-memory/ledger-*/` plus
  the Chapter Spec file and its registry row / the CDL-2 tracker). Once all three return, this command (the
  orchestrator, not a lane) merges the ledger instance's return and the scorer's block into the audit's
  Completeness Indicator and presents them in canonical order (Completeness Indicator, Tier Scope Brackets,
  the CDL-2 block, the Voice and Variety block).

Never parallelized, ever: consultation answers precede the build plan; the build plan precedes drafting;
drafting precedes editing; editing precedes measuring; the Gate 1 audit precedes the confirmation prompt;
`[CONFIRM WRITE]` precedes any file write or ledger update; one Chapter per invocation.

## Sequence

0. **Decision Consultation Gate** (`narration-novel-creative-flexibility-law` Area 19, Exhaustive Clarity
   Mandate) and the **build-plan confirmation.** Before any drafting, run the consultation across the whole
   Chapter:
   - **Narrative-direction branches (Rule 19.3, spec-scoped per Rule 19.4 and Part 38):** (i) branches the
     Chapter Spec carries as Open or Deferred notes in its Audit and Settlement Notes (an open in-story time
     is one: it is the date the Chapter or scene will carry, Part 41 Area 5; never filled silently), and
     (ii) genuinely new branches the spec does not address (direction, major-entity naming per Part 28 Area
     20.4; minor entities are AI-named autonomously; naming is never presented as a cost, risk or downside of
     an option and the named version is the `(Recommended)` one, Part 28 Rule 20.9; a cultivation,
     technology or combat outcome; an emotional or relational fork; scope) that outline-planner or this
     command's own reading of the Canon surfaces, plus anything that would reduce clarity. Items the spec's
     Audit and Settlement Notes list as Settled or carry as Inherited are not re-asked (DCG Rule 19.4 via
     Part 38; Rule 9.5.1); a Skipped note settles nothing; a Deferred note is asked here (Rule 9.5.2). Keep
     asking in further rounds until no genuine open branch remains (answered or explicitly `[SKIP]`ped).
     With `[NO CONSULT]` (Part 28 Rule 19.4) the spec's plan stands and Check #18 reports any difference.
   - **Register new collective and location codes before drafting (Part 39 Rule 39.23.1.5).** For every
     collective (a faction, formation, patrol, crew or kingdom-state) whose members appear together in the
     Chapter, and every location where two or more named people act, read its Collective Behavior Code
     block (Part 39 Area 41.4) in its ledger file. `Registered` or `None, by the author's ruling` needs
     nothing more. `Not yet registered`, an empty stub or no ledger file at all is a blocking item. Who
     does what: the outline-planner proposes a short code built only from facts the ledger already holds,
     each one cited, or recommends none for an incidental crew; the author confirms it, changes it or
     rules `none` through `AskUserQuestion` in this Step 0 (and in the spec confirm when the Chapter Spec
     already carries it as a Settled note). A new collective or location is always asked, never decided by
     the planner or the drafter; a `[SKIP]` registers nothing and the item stays blocking. Once the author
     has confirmed, the continuity-checker writes the block into the entity's own ledger file before the
     area-maker is launched (an author-directed ledger write, the only one before Gate 2): the Area 41.4
     template as a Baseline (B/L) block, `Code Status: Registered YYYY-MM-DD` (or `None, by the author's
     ruling`). A formation with no file gets a new author-directed faction file (Threshold F-1); a location
     with no file of its own (a court or bridge that is only an index row) goes in the block of the file
     the row points to; a location the kingdom-state code already covers points to that code and does not
     restate it. At Gate 2 the checker's ledger instance only verifies that the block matches what the
     author confirmed and brings the Members line up to date; it never registers a code that was not
     confirmed before drafting. The area-maker never invents a code inside the prose.
   - A viewpoint change, `⁂` time skip or scene break the Chapter would need that the Scene Map does not
     list is a new branch and is asked.
   - **The build plan.** After the branches are resolved, show the author a short build plan and ask,
     through `AskUserQuestion` with a Cancel option, whether to proceed: the Chapter's name chain and
     reference, the scenes in order (Scene ID, the Area blocks it covers, the POV sequence, the visible
     breaks), the date line of each scene, the word budget per Area block (its target, 55% to 60% as a
     figure, and any named stretch up to 72%), the Chapter total band (0.55 T to 0.72 T as figures), and
     the Chapter's pacing with each Area block's pacing. The answer `Proceed` ends Plan Mode; a correction
     that changes the spec goes back to `/chapter-spec` (revise); Cancel ends the command with nothing
     changed.
1. **Plan check.** Continue the outline-planner (via `SendMessage`) to confirm the whole-Chapter plan
   against the Chapter Spec's blocks and Scene Map (the beats, POV, pacing, size targets, entity debuts and
   CDL-2 emphasis per block; Opening and Closing type, scene anchors, carry-over, thread, story link, setups
   and payoffs, emotional line, Behavioral Plan). Divergence from the spec is not absorbed silently: it is
   consulted (`/chapter-spec` revise) or recorded as a variance note at the as-built sync. The plan carries
   each scene's date in a Calendar field (the day it begins, and the day it ends if it crosses days) under
   the dating rules of Part 41 Area 6. The planner plans this one Chapter only and writes no prose.
2. **Draft (one area-maker, Chapter mode).** Do not launch it while a collective or location code from
   Step 0 is confirmed but not yet written, or still open. Invoke **one** area-maker in its Chapter mode. It reads the
   previous text, the Chapter Spec in full and the ledger entries, and drafts the whole Chapter to the staging
   path `.claude/temp/Chapter NNN - <Chapter Name>.md`: the Chapter's date line first, once; the Area blocks
   in spec order, each at its own word budget and pacing, each beginning with the hidden line
   `<!-- AREA NN -->` (NN the two-digit Area block number of the spec); the `---` scene-break rule of the
   Chapter 001 conventions (a `---` line only where the scene changes or the same scene moves to a different
   POV; no visible break where one scene simply continues across Area blocks with the same POV, only the
   hidden marker; a scene whose date differs from the scene before gets its own date line directly after its
   break). It hands over the hand-off blocks (CALENDAR by date segment, NAMED ITEMS, NAMED MOVES, MONSTERS,
   any new Tier D person) with the draft. It has no Bash access and never runs a script.
3. **Edit (one chapter-editor).** Invoke **one** chapter-editor on the staged file. It reads the whole draft,
   the Chapter Spec and the Scene Map and edits only the staged file in `.claude/temp/`, in one pass: the
   seams between Area blocks, voice, repetition, plain language, date lines and the word band. It changes no
   plot fact the spec fixes, never touches the hidden markers' order or number, and returns a short list of
   what it changed. No further editing pass runs unless Gate 1 sends the text back (Step 5).
4. **Measure.** Run
   `python .claude/tools/chapter_builder.py measure --mode whole --spec-file ".claude/story-memory/phase-section-part-chapter-area-specs/phase-P/section-S/part-N/chapter-NNN-spec.md" --text-file ".claude/temp/Chapter NNN - <Chapter Name>.md" --phase P --section S --part N --chapter C`.
   It reports words per Area block (from the markers), each Area block against its 55% to 60% band (up to 72%
   where the spec names a stretch), the Chapter total against 0.55 T to 0.72 T, the marker coverage (every
   Area block of the spec present once, in order) and the structure check. An out-of-band count, a missing
   or duplicated marker or a structure fault is a **blocking finding**: send the figures to the
   chapter-editor (or, when whole Area blocks are missing or far off, to the area-maker) to extend or trim,
   and measure again. Hand the printed result to the Gate 1 instances.
5. **Gate 1: Post-Draft Audit** (`guardrails/audit/guardrail-audit-gate-law.md`, whole-Chapter section).
   Send the measured text to the two **continuity-checker** instances already grounded: the **23 checks** on
   the whole Chapter, and the **flow review** (Check #16 dimension 16-J) across the whole Chapter, every Area
   seam and the join with the previous text. Adaptations for the whole Chapter:
   - **Check #10 (size)** is replaced by the word-band check of Step 4 (per Area block and Chapter total);
     the 1,280 to 2,400 range is not applied.
   - **Check #18 (Spec Conformance, Part 38)** is run per Area block and against the Scene Map: every core
     item (beat, scene anchors in order, Continuation, viewpoint with the Dual-POV mark, every planned time
     skip, the Behavioral Plan, Opening type, Closing type, thread, every settled item) is shown as a
     plan-versus-written list per Area block, plus the scenes, POV sequences and visible breaks against the
     Scene Map; a core difference blocks unless it traces to an on-record author answer from this
     invocation; a pacing difference is listed only; `[CONFIRM WRITE]` accepts the other listed
     differences. **18(a):** the chain is in force as in Preconditions (a missing or unconfirmed link is a
     FAIL: Critical where no chain stands, Major where a link is `AMENDED-PENDING-RECONFIRM`).
   - **Calendar (Check #11 element 11-2, Check #12):** read per date segment: the Chapter's opening date
     line and each later date line (rules R1 to R6 of Part 41 Area 6, the weekday under R4), each against the
     scene before it and the Current Position block. Date lines are not narration; Checks #16, #19 and #22
     skip them, and the date lines, markers and break marks are left out of every count.
   - **Check #23 (Battle Plausibility, Part 44)** runs once for each Area block that holds a fight, against the Engagement Ledger of the Chapter Spec's Fight line, as in `/next-area` Step 3 (an Area block with no fight reads N/A).
   - **Checks #20, #21 and #22** run as in `/next-area` Step 3 (Behavioral Conformance blocks; Behavioral
     Change Detection blocks by asking, with the widened evolution rule of Part 43: the author rules for
     heroes and Tier A side characters, villains and monsters, the checker decides and records its reasons
     for Tiers B, C and D, an immutable always needs the author; Plain Language blocks on 22-3, 22-6 and the
     vocabulary elements). A numeric reading crossing a stated line is information, never a FAIL.
   - **The flow review** FAILs a break of time, place, point of view or character state at any Area seam or
     at the join with the previous text; sameness patterns are reported with quoted lines for the author's
     ruling at Step 6. When the cause lies in an earlier Chapter, the chapter-editor first repairs it inside
     this Chapter; if that does not solve it, name the earlier text (Reference Code and name) and ask the
     author via `AskUserQuestion` whether to run `/revise-area` (an Area-built Chapter) or `/revise-chapter`
     (a whole-built Chapter) on it first; if yes, this invocation ends as a `[SKIP WRITE]`. Never edit a
     written file.
   - **Hand-offs** (CALENDAR by date segment, Tier D, NAMED ITEMS, NAMED MOVES, MONSTERS, Check #21
     rulings): reconciled by the checker as in `/next-area` Step 3 and not printed in chat; on
     `[CONFIRM WRITE]` they are passed unchanged into the single Step 8 ledger instance, and a `[SKIP WRITE]`
     discards them. A Tier D person who acts or decides, and a Tier C or D monster at a trigger of Part 40
     Rule 40.6.2.2, put the keep-or-promote question to the author with the Chapter's Position Header and full
     text printed first; on a promote ruling the pending draft is discarded as a `[SKIP WRITE]`,
     `/character-behavior` runs, and `/create-chapter` is run again.
   - **FAIL loop.** The first Step 5 audit of the staged text is full (both instances). On any FAIL: send the
     findings to the chapter-editor, which returns a list of its fixed lines (each pinned to its Area block, the
     old line and the new line quoted), re-measure, and re-audit until clean (Correction Protocol), the scope of
     each re-audit being set by the gate law's section "Re-audit after fixes" (Author ruling, 2026-10-18). When
     the first audit returned a limited set of FAILs that are each a located, local fix, send the same
     continuity-checker instance, by `SendMessage`, the first report's findings, the list of fixed lines and the
     revised text: it re-runs only the checks that produced a finding, on the touched lines, reads those lines
     for any fresh fault, runs the regression sweep over the whole text (the `measure` figures, markers and
     breaks, contractions, dashes, forbidden vocabulary, new or changed names, date lines) and returns
     `FIXES CONFIRMED` or the remaining findings. The checker decides, and states why, whether the fixes are
     local; where the first findings were widespread or structural, or a fix changes what happens on the page,
     adds a plot fact or a person, moves a viewpoint or crosses an Area seam, the affected checks re-run in
     full, and when the checker names both instances this command re-runs Step 5 in full (both instances) as
     before. The author may order a full re-run at any time. Never proceed with a FAIL outstanding, unless the
     remedy would change what happens on the page, which is asked, not absorbed. A revision count is
     information only. The author may stop the loop at any time: print the Position Header and the full text,
     with the check, its last two findings and the conflict that keeps it from clearing. An agent never
     declares diminishing returns or structural impossibility itself.
6. **Present and confirm.** Wait for an explicit `[CONFIRM WRITE]` / `[REVISE CHAPTER]` / `[SKIP WRITE]`;
   never assume confirmation. Print, in this order: the Position Header Block (the complete five-tier name
   chain Phase / Section / Novel-Part / Chapter, plus the Chapter Reference Code `P.S.N.CCC`, the Chapter
   pacing and size target and each Area block's pacing and target carried from the spec, a Calendar line
   (chat only: each date line as written, its Phase Day, the date of the previous text)); the **full text of
   the Chapter, verbatim, as the reader will see it** (date line first; the hidden markers are shown as the
   lines `Area NN` in a small label above each block here so the author sees the join, never a summary, an
   excerpt or a file path); the **measure figures** (words per Area block against its band, the Chapter
   total against 0.55 T to 0.72 T, any named stretch used); the Contextual Earning Declaration; the
   Post-Draft Audit Report (Triggered Parts and every FAIL, one line counting Not Triggered and N/A Parts;
   the full named-result list goes to the session log) with the flow-review verdict, any reported pattern
   and its quoted lines, one line on the FAIL loop where it ran (the first audit's FAIL checks, the mode of the
   re-audit and its result; Author ruling, 2026-10-18), and the plan-versus-written list per Area block (a list with a BLOCKS line gets no
   confirmation prompt); then the confirmation prompt, which says that `[CONFIRM WRITE]` accepts the listed
   differences. The full text is printed at every Gate 1 and again after every `[REVISE CHAPTER]`; any
   question about the draft is asked after the Position Header and the full text are printed. No other
   assistant commentary is wrapped around these blocks. `[REVISE CHAPTER]` rejects the listed differences,
   returns to Step 3 (the chapter-editor with the author's notes; the area-maker only when whole Area blocks
   must be redrafted), then re-runs Steps 4 and 5 (Step 5 as a first full audit of the revised text; Author ruling, 2026-10-18) before the revised text is printed again. `[SKIP WRITE]`
   discards everything (see Failure/abort).
7. **Write (Gate 2, files).** On `[CONFIRM WRITE]` run the script, and no other write method
   (`guardrails/tools/guardrail-authorized-scripts-only.md`):

   ```
   python .claude/tools/chapter_builder.py write --mode whole --spec-file "<chapter spec path>" --text-file ".claude/temp/Chapter NNN - <Chapter Name>.md" --output-root "<repo root>/projects/novel-starward-saga" --phase P --section S --part N --chapter C --chapter-name "<name>" --phase-name "<name>" --section-name "<name>" --novel-part-name "<name>" [--first-of-phase] [--first-of-section] [--phase-epigraph-file "<file>"] [--section-epigraph-file "<file>"] [--overwrite]
   ```

   `--output-root` is the absolute path of `projects/novel-starward-saga/` under the repo root. Give
   `--first-of-phase` or `--first-of-section` only when true. For the first Chapter of a Phase pass TWO
   epigraph files: the text after `Epigraph: ` on the Phase's own `Epigraph:` line in Part 30
   (`narration-novel-macro-story-law`) as `--phase-epigraph-file`, and Section 1's own Epigraph line from the
   header block of its Section Spec as `--section-epigraph-file`; for the first Chapter of any other Section
   pass ONE, that Section's Epigraph line, as `--section-epigraph-file`. `unset` means none for that line and
   the flag is left out. This command reads those lines itself from the files and passes the text only; no
   agent writes epigraph text. Write the epigraph text to temporary UTF-8 files outside `projects/` and
   `.claude/`. `--overwrite` is given only by `/revise-chapter` and `/redraft-chapter`; here a file already on
   disk is a refusal. The script refuses an out-of-band text, a missing or duplicated marker, a structure
   fault, a Chapter with Area files, and an existing file without `--overwrite`; it writes the `.md` WITH the
   hidden markers and the `.docx` WITHOUT them, the breaks and date lines as the Chapter 001 conventions set.
   If the script fails, stop as Failure/abort says. Read the written `.md` and `.docx` back (python-docx, the
   paragraph list): the Chapter Header Block, the opening date line, the right number of visible breaks, the
   right number of markers in the `.md` (one per Area block) and none in the `.docx`, and no `Area N -`
   title. Hand the read-back result to the Step 8 audit lane, which holds no shell.
8. **Gate 2 (three parallel lanes, one message).**
   - **Post-Write Audit** (continuity-checker, independent fresh forced-read, checkpoint 3 of 3): Completeness
     Indicator (Block A) and Tier Scope Brackets (Block B); checks the printed path against the Chapter's
     position (`.../phase-P/section-S/part-N/Chapter NNN - <Chapter Name>.md` and `.docx`, and no Area file
     exists for it), the opening date line of the written `.md` against the date line confirmed at Gate 1,
     the marker count and order, and the read-back result. Shows the Block A ledger-obligation line as
     "pending merge".
   - **Post-Write Ledger Update, one batched update for the Chapter**
     (`guardrails/ledger/guardrail-ledger-update-law.md`): new entity files; named-item register rows;
     Named Moves (the row in `ledger-named-moves/_index.md` and in each user's character-ledger registry,
     pointing at each other); monsters (Part 40; Part 37 Thresholds M-1 and M-2); Tier D rows; Check #21
     rulings and every Evolution Entry (ADD, CHANGE or RETIRE; Part 43); state-record updates;
     narrative-summary enrichment; Section 10 Canon Events Log rows; current conditions; and the calendar
     rows of `ledger-worlds-calendar/_index.md` (Part 41 Area 9: one row per date segment of the Chapter, the
     rollups and the Current Position block, which names the Open Chapter and its recorded window, First to
     Latest). **Every one of these cites the Chapter reference only, `P.S.N.CCC` (for example `1.1.1.002`);
     no Area-level or scene-level code is written for a whole-built Chapter.** First-appearance fields name
     the Chapter reference. It also performs the **Chapter Spec as-built sync and completion in one pass**
     (Part 38 Rule 3.6.1 and Rule 9.7.2): every Area row set to `WRITTEN(P.S.N.CCC)`; the Signatures-fired
     rows flipped per Area block using the markers in the written `.md`; every difference `[CONFIRM WRITE]`
     accepted recorded as a variance note in the Audit and Settlement Notes, and every item settled here
     moved there (Rule 38.14); the in-story time as built mirroring the date lines; the **Completion
     Record** written (Final Variance Summary, Reader now knows, Chapter digest, New-named-things line); the
     Chapter Spec set to `COMPLETED`; its registry row updated, including the Coverage cell and Last Updated.
     It writes no Novel-Part Spec and no Section Spec (Rule 9.4.3); those complete at their own boundary.
   - **CDL-2 score** (area-scorer): one CDL-2 block for the Chapter (date lines, markers and break marks left
     out of every reading and of the size), the report-only Voice and Variety block, and the Section running
     aggregate row in `.claude/story-memory/cdl2-density-tracking/phase-N/section-M-aggregate.md` (created at
     the Section's first scored Chapter or Area). No per-Area blocks are written. A density reading below or
     above its line is information, raises no question and no FAIL; before the first Chapter of the Section
     has closed the aggregate is provisional and nothing is raised on account of it (Part 35 Area 4.1).
9. **Clean up.** Once Gate 2 has returned, delete the staged file in `.claude/temp/` (an input, not a Chapter
   file) and the temporary epigraph files. A plain delete; never a script.
10. **Log and report.** Write one line to `.claude/story-memory/session-log/` (the Chapter reference, the
    outcome, the word total against its band, the Gate 1 result (with the re-audit mode where the FAIL loop ran; Author ruling, 2026-10-18), the token given, the three Gate 2 lanes'
    results; the full named-result list of the audit goes here). Then report the two output paths, the figures
    (words per Area block, Chapter total, band), the ledger and spec changes in one line each, the CDL-2
    score, and the next command: `/next-chapter`, which now only moves on (the Chapter Spec is already
    `COMPLETED`).

## Failure/abort

`[SKIP WRITE]` discards everything: no file is written and no ledger or spec update runs, so files, ledger
and spec agree; the draft, its edits, its audit, the differences its plan-versus-written list showed and any
name it introduced are dropped (a name delivered in a discarded draft is not established), and the staged
file is deleted. Any irreconcilable Gate 1 conflict is escalated via `AskUserQuestion`, never force-written.
A stop condition in Preconditions writes nothing and names the fix.

A failed Gate 2 write (Step 7) stops the invocation: remove the file the script may have written (a plain
delete of the `.md` or `.docx` of this Chapter only), run no ledger update, no spec sync and no score, show
the author the script's message as it is, and wait. The confirmed text is still in the conversation and the
staged file stays until the write succeeds; the author re-issues `[CONFIRM WRITE]` once the cause is fixed.
The Chapter is not counted as written until both files are on disk.

A Gate 2 lane that fails after the files are written is re-run alone; nothing is written twice, and the
Chapter is not reported complete until the audit, the ledger update with the spec sync, and the score have
all returned. `/force-ledger-audit` repairs an `incomplete Gate 2 at P.S.N.CCC`.

## Rules

- One Chapter per invocation, built whole; never any Area file, never a second Chapter. The Chapter file pair
  in the Novel-Part folder is the only output and is written only by `chapter_builder.py`
  (authorized script 6).
- One area-maker drafts, one chapter-editor edits, in that order and never at once. The area-maker and the
  chapter-editor never run a script and never write outside `.claude/temp/`.
- A Chapter built by Area is never created whole, and a Chapter built whole is never touched by `/next-area`,
  `/revise-area` or `/chapter-builder`. Revision is `/revise-chapter`; a fresh draft is `/redraft-chapter`.
- All ledger, calendar, Events Log, Evolution, Named Move, first-appearance, scoring and spec references of
  the Chapter cite `P.S.N.CCC` only. The hidden `<!-- AREA NN -->` markers are bookkeeping, never citations.
- Gate 1 and Gate 2 are never skipped, never merged and never reordered. `[CONFIRM WRITE]` is the author's
  word in chat; silence is never confirmation.
- Nothing is added that the Chapter Spec and the author's answers do not carry. Plain English, no emojis.
