---
description: "Write the next Area of the Starward Saga (the written unit) through the full Two-Gate pipeline: pick the next Area from the Chapter Spec, draft, Gate 1 audit, confirm, Gate 2 write, ledger update, score."
user-invocable: true
---

# `/next-area`

Corresponds to canon command `[NEXT AREA]` (C-4).

The Area pipeline's command: the one command that writes one Area (`/create-chapter` is the second
lawful writer and writes one whole Chapter; neither batches Areas). Chapters built by Area are written at
Area level.
An Area is the written unit; it may be a complete scene, or a scene may continue across consecutive
Areas of the Chapter. The command picks the next Area from the Chapter Spec (advancing to the next
Area of the Chapter), and writes exactly that one Area per invocation.

## Preconditions

- Read `.claude/guardrails/_index.md`, `.claude/guardrails/audit/guardrail-audit-gate-law.md`,
  and `.claude/guardrails/commands/guardrail-plan-then-auto-execution.md` (Plan Mode to Auto
  Mode sequencing, default model/effort, mandatory parallelism, milestone progress
  reports; it governs this command's execution shape end to end).
- Pre-Write Ledger Check: confirm the relevant `.claude/story-memory/ledger-*/` entries for
  every entity about to appear are current.
- Read `.claude/guardrails/ledger/guardrail-story-spec-law.md` (Part 38, Story
  Specification Law) and the active Chapter Spec at
  `.claude/story-memory/phase-section-part-chapter-area-specs/phase-N/section-N/part-N/chapter-NNN-spec.md`.
  **The chain must be in force** (Part 38 Rule 9.1.1): the Chapter Spec is `CONFIRMED`, and its
  Novel-Part Spec (`.../section-N/part-N/part-N-spec.md`) and its Section Spec
  (`.../section-N/section-N-spec.md`) are each `CONFIRMED` or `COMPLETED`; none of the three is
  `DRAFT`, `AMENDED-PENDING-RECONFIRM` or `RETIRED`. Read each link's status from its row in the
  registry `_index.md` of that folder. A missing link, or one that is not in force, is a **stop
  condition**: check top-down, name the FIRST missing or unconfirmed link (Section Spec, then
  Novel-Part Spec, then Chapter Spec) with its status, and direct the author to the command that
  fixes it: `/section-spec`, `/part-spec` or `/chapter-spec` (build when none exists, revise when
  it is `DRAFT` or `AMENDED-PENDING-RECONFIRM`); a `RETIRED` link is surfaced as it stands and the
  author rules what takes its place. Never plan the Area ad hoc without the chain. Gate 1 Check
  #18(a) repeats this test at the gate (Step 3).
- **Per-Area read set (Part 38 Rule 9.9.2).** For the one Area this command writes, area-maker,
  area-scorer, both Gate 1 continuity-checker instances and the outline-planner, which plans that
  one Area in Step 1, read the Chapter Spec in full and, of the Novel-Part Spec, its header block
  and its closing-state block only; the Section Spec is not in that set. Nothing is cut down by
  this: the Chapter Spec carries every inherited item, tagged with its source. Pass the
  Novel-Part Spec path with the Chapter Spec path when launching them.
- **Refuse a whole-built Chapter.** If the active Chapter Spec's `Build mode` is `whole` and the Chapter has
  been built whole (its Area rows read `WRITTEN(P.S.N.CCC)`, or the Chapter file pair exists in the
  Novel-Part folder with no Area files), stop before anything else and say: "Chapter P.S.N.CCC was built
  whole by /create-chapter and has no Area files; /next-area writes Areas of Chapters built by Area. To
  change it use /revise-chapter, or /redraft-chapter to write it afresh." A Chapter whose Build mode is
  `whole` and that is not yet built is also not written here by default: name `/create-chapter`; `/next-area`
  runs on it only when the author asks for it and revises the spec to `Build mode: by-area` first
  (`/chapter-spec` revise).
- **Pick the Area to write from the Chapter Spec, not from where the files on disk end.** The next
  Area is the first Area row, in Chapter order, of the active Chapter Spec whose status is
  `PLANNED` or `DRAFTED`; a `DROPPED` row is skipped. When Area files sit after that row on disk (a redraft in progress after
  `/redraft-area` or `/redraft-chapter`), the Position Header Block says "redraft in progress" and
  the row still stands. The Area number, its pacing, its size target and every `is_first_area_of_*` flag
  come from that row, never from the last file written. If no `PLANNED` or `DRAFTED` row is left in
  the Chapter (the last Area was the Chapter's last), direct the author to `/next-chapter`, or to
  `/chapter-spec` (revise) to add an Area. When `/next-chapter`, `/next-part`, `/next-section`,
  `/next-phase` or `/start-story` runs this command, the advance is already made and that
  redirect does not apply.
- Identify the **Area window** (the read set, defined once in Part 2 Rule P2-Area-1): the Area
  under audit, the previous Area of the Chapter as written on disk (the last Area of the previous
  Chapter when this is the Chapter's first), and the earlier Areas of a scene that continues across
  Areas, read in order; the Area's own block in the spec is read with them. An Area row that records no
  scene anchors, no beat or no pacing is a **stop condition**: direct the author to
  `/chapter-spec` (revise). Pass the window's references to outline-planner, area-maker and both
  Gate 1 instances. The span of days an Area covers is called the Area's dates, never its window.
- Read the Current Position block of `.claude/story-memory/ledger-worlds-calendar/_index.md` (the
  Open Chapter and the Open Chapter's recorded window, First to Latest) and the
  row of the Area being written (Part 41 Area 9, The calendar ledger): the story clock and the days
  covered. The block and the one row are read, not the whole file. Pass them with the Area window to
  outline-planner, area-maker and both Gate 1 instances.
- **Area size and pacing** are governed by the Area size rule of `narration-novel-book-structure-law`
  and by the confirmed Chapter Spec. An Area is written to one of three targets, 1,600, 1,800 or
  2,000 words, decided in the Chapter Spec for that Area; the passing range is 1,280 to 2,400
  words. A count outside 1,280 to 2,400 words is a blocking finding: the write waits for the author to
  confirm the Area or send it back. Pacing (Fast, Medium, Slow) is decided in the
  Chapter Spec for every Area and is carried here as recorded; it is a craft matter independent of
  size and tied to no word band, and a pacing difference is shown, never blocking. Read the figures in the rule rather than assuming them. Thematic
  quality (Gate 1 Check #16) is governed primarily by `narration-novel-thematic-law`
  (`.claude/guardrails/quality/guardrail-tier0-narrative-quality.md`).
- **Area-to-Area carry-over.** Every Area knows what came before (Rule P2-Area-2). An Area that
  continues the previous one opens in motion from the exact state the previous Area left (same
  place, moment and register; no second opening and no recap), and an Area that continues a scene
  ends on live tension.

## Plan Mode to Auto Mode

Step 0 below (the Decision Consultation Gate) is this command's **Plan Mode**: every author-facing
question this invocation will ever ask (every open narrative branch, every major-entity name) is
asked and resolved (answered or explicitly `[SKIP]`ped) before Step 1 begins. Pacing and size are
not asked: the Chapter Spec carries them. Once Plan Mode concludes, Steps 1 to 8 run in **Auto
Mode**: no further discretionary questions, straight through to the next mandatory gate. Auto Mode
never waives a required stop; the Gate 1 presentation and its confirmation token (Step 4) remain a
hard pause (`guardrails/commands/guardrail-plan-then-auto-execution.md`). A number crossing a stated
line that is not the size range is not a question at all: it is information in the audit report
(`guardrails/quality/guardrail-threshold-consultation.md`). An Area-window finding that needs the
author (a remedy that changes the page, a cause in an earlier Area), a Check #21 enquiry and a Tier
D consequence flag (Part 19 Rule 19.1.2.4) are the questions Plan Mode cannot pre-empt, because they
are only computable once a draft exists: each is asked mid-Auto-Mode with the Area's full text
printed first.

## Parallel orchestration (speed policy)

The gate order below is law; within it, always run independent work concurrently rather than
serially. This binding is absolute, not a suggestion to weigh against convenience
(`guardrails/commands/guardrail-plan-then-auto-execution.md`).

- **Step 0 and planner grounding:** launch **outline-planner** as a background agent at the same
  moment the `AskUserQuestion` consultation is presented, instructing it to do its grounding reads
  (guardrails, on-disk position, Part 30 and Part 2 consolidated files, ledger entries, **the active
  Chapter Spec**, and the header block and closing-state block of its Novel-Part Spec, which with
  the Chapter Spec make up the per-Area read set) and to report any open branch points it finds, but
  not to finalize a plan. When the author's answers arrive, continue the same agent via
  `SendMessage` to produce the single-Area plan. Any new branches it surfaced feed further
  consultation rounds (Exhaustive Clarity Mandate) before the plan is finalized.
- **Step 2 and Gate 1 pre-read:** while **area-maker** drafts, launch **continuity-checker** in the
  background to complete its Pre-Area Read checkpoint (guardrails, canon-manifest forced read, ledger
  state, the Area window as written), and launch a second **continuity-checker** instance for the
  grounding reads of the Area flow review (the Area window as written, the first and last paragraph
  of the previous Area (the first paragraph of narration, below the date line), for the reported
  patterns only, Part 36, the spec's Area blocks). When the draft lands, send it to both via
  `SendMessage`: the first runs the 23-check Gate 1 audit, the second the Area flow review (Check #16
  dimension 16-J). The forced-read discipline is unchanged: the 23-check instance still performs its
  fresh manifest re-read (the flow-review instance checks no cross-Part edge and makes none); only
  the grounding happens concurrently with drafting. Both instances stay available for the FAIL loop
  (Author ruling, 2026-10-18): the re-audit after fixes of Step 3 goes to the first instance by `SendMessage`,
  which resumes with its first-pass reads, and to the second only when a finding came from the flow review or a
  fix touches a seam; the loop starts no fresh instance and repeats no grounding.
- **Steps 6 and 7:** after the authorized scripts have written the files, launch three parallel
  agents in a single message: (1) **continuity-checker** for the Gate 2 **Post-Write Audit** only,
  with its own independent fresh forced-read (checkpoint 3 of 3), verification against the manifest,
  and the Completeness Indicator (Block A) and Tier Scope Brackets (Block B); this instance is
  read/report-only and writes nothing to disk; (2) a second, separate **continuity-checker**
  instance for the **Post-Write Ledger Update** only
  (`guardrails/ledger/guardrail-ledger-update-law.md`): new entity files, named-item register rows,
  state-record updates, narrative-summary enrichment, Section 10 Canon Events Log rows, the calendar
  rows of `ledger-worlds-calendar/_index.md` (Part 41 Area 9), **plus the active Chapter Spec file and
  its registry row (the mandatory Part 38 as-built sync: the Area row's status flips to `WRITTEN`, and
  the last Area row of the Chapter going `WRITTEN` sets the Chapter Spec's own status to `COMPLETED`,
  Part 38 Rule 3.6.1 item 1; every difference `[CONFIRM WRITE]` accepted is recorded in the file's
  Audit and Settlement Notes, and every item settled at this Area is moved there, Part 38 Rule 38.14;
  the sync writes no Novel-Part Spec and no Section Spec, Part 38 Rule 9.4.3)**; (3) **area-scorer**
  for the CDL-2 score of the Area, the Section aggregate and the report-only Voice and Variety block.
  The split stays 3-way and all three write sets stay disjoint (audit report only /
  `story-memory/ledger-*/` entity files plus the active Chapter Spec file and its registry row / the
  CDL-2 Section aggregate), so there is no conflict running them concurrently. The audit lane cannot
  see the other two lanes' returns, so it shows the Block A ledger-obligation line as "pending
  merge". Once all three return, this command (the orchestrator, not a lane) merges the ledger
  instance's return (the obligation discharge) and the scorer's block into Block A, then presents
  their outputs in canonical order (Completeness Indicator, Tier Scope Brackets, the CDL-2 block, then
  the Voice and Variety block).

Never parallelized, ever: consultation answers precede the finalized plan; the plan precedes
drafting; the Gate 1 audit precedes the confirmation prompt; `[CONFIRM WRITE]` precedes any file
write or ledger update; exactly one Area per invocation throughout.

## Sequence

0. **Decision Consultation Gate** (`narration-novel-creative-flexibility-law` Area 19, Exhaustive
   Clarity Mandate): before any planning or drafting, run the consultation. The Area's pacing and
   size target are not asked; they are read from the Chapter Spec's row and carried (the Gate 1
   Position Header Block shows them as carried from the spec). Ask only:
   - **Narrative-direction branches (Rule 19.3, spec-scoped per Rule 19.4 and Part 38):** (i)
     branches the active Chapter Spec carries as Open or Deferred notes for this Area in its Audit and
     Settlement Notes section (an open in-story time is one: it is the date the Area will carry, Part 41 Area 5;
     never filled silently), and (ii) genuinely new branches not addressed by the spec (direction,
     major-entity naming (per Part 28 Area 20.4; minor entities are AI-named autonomously; naming is
     never presented as a cost, risk or downside of an option and the named version is the
     `(Recommended)` one, Part 28 Rule 20.9), cultivation/technology/combat outcome,
     emotional/relational fork, scope) that outline-planner or this command's own reading of the Canon
     surfaces, plus anything that would reduce clarity, which is always asked. Items the spec's
     Audit and Settlement Notes list as Settled are **not re-asked** (DCG Rule 19.4 via Part 38): the
     author settled them at spec time. A Skipped note settles nothing. The Chapter Spec is the only spec this step reads for them:
     whatever the author settled in the Section Spec or the Novel-Part Spec was carried into it as an
     Inherited note naming its source and is not re-asked either (Part 38 Rule 9.5.1), while a matter
     the author deferred to the writing was carried in as a Deferred note naming the deferral and is
     asked here like any open item; the drafter never settles it silently (Rule 9.5.2). Keep asking in
     further rounds if an answer opens a new branch, until no genuine open branch remains (answered or
     explicitly SKIPped). Never ask about anything already settled by the Canon or by the confirmed
     spec.
   - **Register new collective and location codes before drafting (Part 39 Rule 39.23.1.5).** For every
     collective (a faction, formation, patrol, crew or kingdom-state) whose members appear together in this
     Area, and every location where two or more named people act, read its Collective Behavior Code block
     (Part 39 Area 41.4) in its ledger file. `Registered` or `None, by the author's ruling` needs nothing
     more. `Not yet registered`, an empty stub or no ledger file at all is a blocking item. Who does what:
     the outline-planner proposes a short code built only from facts the ledger already holds, each one
     cited, or recommends none for an incidental crew; the author confirms it, changes it or rules `none`
     through `AskUserQuestion` in this Step 0 (a Chapter Spec Settled note already counts as the author's
     confirmation). A new collective or location is always asked, never decided by the planner or the
     drafter; a `[SKIP]` registers nothing and the item stays blocking. Once the author has confirmed, the
     continuity-checker writes the block into the entity's own ledger file before the area-maker is
     launched (an author-directed ledger write, the only one before Gate 2): the Area 41.4 template as a
     Baseline (B/L) block, `Code Status: Registered YYYY-MM-DD` (or `None, by the author's ruling`). A
     formation with no file gets a new author-directed faction file (Threshold F-1); a location with no file
     of its own goes in the block of the file its index row points to; a location the kingdom-state code
     already covers points to that code and does not restate it. At Gate 2 the checker's ledger instance
     only verifies that the block matches what the author confirmed and brings the Members line up to date;
     it never registers a code that was not confirmed before drafting. The area-maker never invents a code
     inside the prose.
   - A viewpoint change, `⁂` time skip or scene break this Area would need that its row in the Chapter
     Spec does not list is a new branch and is asked. With `[NO CONSULT]` (Part 28 Rule 19.4) the
     spec's plan stands and Check #18 reports any difference.
1. Invoke **outline-planner** to confirm exactly what this Area covers, using the answers from step
   0, **planning the Area against its row and its block in the active Chapter Spec** (the row's beat,
   POV, pacing, size target, entity debuts and CDL-2 emphasis, and the block's Opening and Closing
   type, scene anchors, Carry-over from the previous Area, Thread or storyline, Story link and change,
   Setups and payoffs, Emotional line, World/setting/people, Novel elements carried and Behavioral
   Plan are the plan's baseline; step 0 answers resolve its open items). Divergence from the spec is
   not silently absorbed: it is either consulted (spec revise via `/chapter-spec`) or recorded as a
   variance note in the Audit and Settlement Notes at the Gate 2 as-built sync. **Single-Area
   scope:** this plans exactly one Area, never more; the Area that follows is planned in the *next*
   invocation, never folded into this one. The plan carries the Area's date in its Calendar field: the
   day it begins, and the day it ends if it crosses days, planned inside the Area window from the Area
   block's in-story time and the Current Position block, under the dating rules of Part 41 Area 6. A
   scene that opens in the last dark hour and runs on into a dawn is planned on that dawn's day, with
   no range (Part 41 Area 2, Epoch, year and months: the one scoped exception to the dawn-to-dawn day).
2. Do not launch the area-maker while a collective or location code from Step 0 is confirmed but not yet
   written, or still open. Invoke **area-maker** to draft the Area (one Area only), after it has read the previous Area (and
   the Areas of the same scene, in order); its reading order is fixed in its agent file. The text it
   drafts begins with the Area's date line (Part 41 Area 5, The date line), and it hands over the
   `CALENDAR (this Area)` block with the other hand-off blocks.
3. Invoke **continuity-checker** to run the Gate 1 Post-Draft Audit as two read-only instances
   launched together: the **23** checks on the draft, and the Area flow review (Check #16 dimension
   16-J) over the Area window. The 23 checks include Part 36 Check #16, the Part 28 Area 20 Entity
   Naming Check #17, the Part 38 Spec Conformance Check #18 (stated below) and the Prose Vitality Check
   #19: Part 28 Area 13 / Part 29 Area 4 craft counts (read as information only) plus the Part 36
   Area 17 qualitative dimensions. A **numeric reading**, a computed value crossing a stated line
   other than the size range, is not a FAIL: do not remedy it
   and do not ask about it. Record it in the Post-Draft Audit Report with the number, the line it
   crossed and the margin (`guardrails/quality/guardrail-threshold-consultation.md`); the author sees it
   at the confirmation. **Size is structural and blocks:** a count outside 1,280 to 2,400 words is a
   blocking finding: the write waits for the author to confirm the Area or send it back. On any FAIL: revise via area-maker and re-audit until clean
   (`guardrails/audit/guardrail-audit-gate-law.md` Correction Protocol); never proceed with a FAIL
   outstanding, unless the remedy would change what happens on the page, which is asked, not absorbed.
   **Re-audit after fixes (Author ruling, 2026-10-18).** The first audit of a draft is full (both
   instances). area-maker returns a list of its fixed lines, each paragraph pinned, the old line and the
   new line quoted. When the first audit returned a limited set of FAILs that are each a located, local
   fix, the re-audit goes to the same continuity-checker instance by `SendMessage`, with the first
   report's findings, the list of fixed lines and the revised Area: it re-runs only the checks that
   produced a finding, on the touched lines, reads those lines for any fresh fault, runs the regression
   sweep over the whole Area (the word count against 1,280 to 2,400, contractions, em-dashes, forbidden
   vocabulary, new or changed names, the date line) and returns `FIXES CONFIRMED` or the remaining
   findings. The checker decides, and states why, whether the fixes are local; where the first findings
   were widespread or structural, or a fix changes what happens on the page, adds a plot fact or a
   person, moves the viewpoint or crosses the seam with the Area before or after, the affected checks
   re-run in full (both instances where the flow review is affected). The author may order a full
   re-run at any time. The scope rules are those of the gate law's section "Re-audit after fixes".
   The number of revisions a check has taken is information only and stops nothing by itself. The
   author may stop the loop at any time: print the Position Header and the full text of the draft,
   with the check, its last two findings and the conflict that keeps it from clearing. An agent never
   declares diminishing returns or a structural impossibility itself
   (`guardrails/audit/guardrail-audit-gate-law.md`).
   Check #18 (Spec Conformance, Part 38): the drafted Area is compared with every spec-planned element
   and shown as a plan-versus-written list; a difference on a core item (Part 38 Rule 6.1.1(b): the beat (the Area's purpose); the scene anchors (their order is part of the anchors); the Continuation; the viewpoint (the Dual-POV mark included); every planned time skip; the Behavioral Plan (Rule 6.1.2); the Opening type; the Closing type; the Thread or storyline; and every settled item) blocks unless it traces to an on-record author answer from this invocation; a size outside
   1,280 to 2,400 words also blocks (a count outside 1,280 to 2,400 words is a blocking finding: the
   write waits for the author to confirm the Area or send it back); a pacing difference is listed
   only and never blocks; every other difference is listed, `[CONFIRM WRITE]` accepts the listed ones (the spec is updated at Gate 2) and
   `[REVISE AREA]` rejects them. **18(a), the chain is in force:** the Chapter Spec `CONFIRMED` and its
   Novel-Part Spec and Section Spec each `CONFIRMED` or `COMPLETED`, none of them `DRAFT`,
   `AMENDED-PENDING-RECONFIRM` or `RETIRED`. A missing or unconfirmed link is a FAIL: Critical where no
   chain stands (a link is missing, `DRAFT` or `RETIRED`), Major where a link stands but is
   `AMENDED-PENDING-RECONFIRM` (Part 38 Rules 6.1.3 and 9.1.3); the FAIL names the first missing link
   and its command. No comparison of the Area with the Novel-Part Spec or the Section Spec is added:
   the plan-versus-written list stays against the Chapter Spec, which carries what they settled. The
   check count is 23.
   **Area-window findings.** A break of time, place, point of view or character state in the window
   FAILs and follows the loop above; sameness patterns are not a FAIL: they go into the audit report
   with quoted lines for the author's ruling at Step 4. When the cause of a finding lies in an earlier
   Area, area-maker first repairs it inside the new Area; if that does not solve it, name the earlier
   Area (Reference Code and name) and ask the author via `AskUserQuestion` whether to run
   `/revise-area` on it first. If yes, the pending draft is discarded (this invocation ends as a
   `[SKIP WRITE]`: nothing written or updated) and `/next-area` is run again once the revision is
   written. If no, the author chooses another repair; the finding stays blocking until it is repaired or
   the author rules a canon amendment, and nothing is accepted automatically. Never edit a written Area
   file. Every question about the draft (a Check #21 enquiry, an earlier-Area repair, a spec
   difference) is asked after the Position Header and the full text are printed. After
   `/redraft-area` or `/redraft-chapter`, when the next Area is already written, the review also reads
   the join with that Area's opening. When the cause of a finding there lies in that later Area, the
   new Area is repaired inside itself if that solves it; otherwise the author rules: hold the ending as
   written, or accept the join and run `/revise-area` on the later Area once this one is written
   (recorded as a variance).
   Also blocking: **Check #20 (Behavioral Conformance, Part 39 Area 43)**, elements 20-1 through 20-12
   (20-3 is retired; the recurrence and off-register counts inform only), including that no character
   acts or speaks without a tier-compliant Part 39 registration (a Tier C or Tier D person improvised
   in the prose passes by its Gate 1 identification and its Gate 2 registration, Rule 39.4.3.1 Route 2)
   and that the Layer L29 waiting beat of a present-but-not-acting character is rendered where the
   scene shows the wait (reported per Area; none is added to meet the rule); and **Check #21
   (Behavioral Change Detection, Part 39 Area 44)**, which **blocks by asking rather than failing**: on
   an unmapped trigger, a contradicted Signature, a flagged item not yet ruled, an Area where the prose
   shows a POV character's profile moving (a Section close is reviewed by `/next-section`), or any
   PIS-7 / CSS-8 / age-band / realm crossing (Part 39 Area 44.2) it raises an `AskUserQuestion`
   offering `[KEEP PROFILE]` / `[EVOLVE]` / `[REVISE AREA]` / `[PROVISIONAL]` / `[DEFER]` with a
   reasoned recommendation. A review that finds none of D-1 to D-4 and no unmapped trigger reports
   SILENT and asks nothing. **Check #21 widened (evolution, 2026-10-06; Part 43, Character Evolution Law):** at Gate 1 it detects EVERY behaviour change in the draft for every character (the 36 Layers, the 12 Signatures and the bound properties). For heroes and Tier A side characters, villains and monsters it asks the author with `AskUserQuestion`; for Tier B, C and D side characters, villains and monsters the Gate 1 continuity-checker decides itself and records its decision and reasons, asking nothing. A change to an immutable trait always needs the author's explicit ruling and a recorded reason, for every tier. Gate 2 presents every evolution (all tiers) with its recorded information. A `[REVISE AREA]` send-back goes through `/revise-area`. No new command exists, and evolution is not drift. An open Check #21 enquiry blocks Gate 2 exactly as a FAIL does.
   Also blocking: **Check #22 (Plain Language and Narrative Impact,
   `guardrails/quality/guardrail-plain-language.md`)**: modern slang in the setting (22-3) and
   plainness that flattens an image or a sensory anchor (22-6) FAIL; the heavy-word counts (22-1,
   22-2) go into the audit report as information and are never a FAIL or a question to the author. **Check #22 vocabulary elements (plain vocabulary, 2026-10-06):** the check also blocks a special or invented word with no picture at first use, one word carrying two meanings in an Area, a jargon wall (three or more unexplained special terms in one sentence or speech) and a figure the reader cannot parse at first read; 22-3, 22-6 and these new elements block, while 22-1, 22-2 and 22-7 inform.
   Also blocking: **Check #23 (Battle Plausibility, Part 44, `guardrails/quality/guardrail-battle-plausibility.md`)**, elements 23-1 to 23-6 on every Area whose text holds a fight (N/A for an Area with no fight) and element 23-7 on every Area (gap arithmetic in prose, a FAIL): a hard-rule break FAILs (23-1 anchors and levels; 23-2 a lower side winning a Shut pairing of 3 or more minor steps in a fair contest, or harming a Barred pairing across a Major Realm without Part 3 Rule 17.3.3; 23-3 a side unable to be present or survive at the stated levels; 23-4 an unlawful, unbounded or unpriced offset (a limit break, Part 3 Area 7.5, is priced on the page afterwards), or a gifted fighter not registered in the ledger before the scene; 23-5 a result the levels forbid). A strained-but-lawful mismatch (23-6) is reported to the author as a ruling point at `[CONFIRM WRITE]` and never blocks.
   **The date line (Part 41 Areas 5 and 6).** The checker reads the first line of the Area text under
   Check #11 element 11-2 (the dating rules R1 to R6 of Part 41 Area 6, with the weekday in rule R4)
   and under Check #12 (its form, and the roman form of month and weekday names elsewhere). A failure
   of R1 to R6 or of the form is a FAIL like any other and follows the loop above; a planned step back
   at a `cut to another thread` Area is information. The check count is 23 and Check #11 keeps its
   six elements. The line is not narration: Checks #10, #16, #19 and #22 skip it.
   **Calendar hand-off.** When area-maker's handoff carries its `CALENDAR (this Area)` block, the
   checker's Gate 1 report reconciles it with the line and returns the checked block. Do not print the
   block in chat; the Position Header carries the Calendar line instead (Step 4). On `[CONFIRM WRITE]`,
   pass the checked block unchanged into the prompt of the Step 6 ledger instance, which writes the
   calendar rows; a `[SKIP WRITE]` discards it.
   **Tier D hand-off.** When area-maker's handoff lists a new Tier D person, the checker's Gate 1
   report carries a Tier D block (name, descriptor, code, result). Do not print the block or the code in
   chat; a failure still open when Gate 1 closes appears in the Gate 1 report like any other FAIL (the
   test V1 to V9 and the token at fault), and correction loops are not printed. On `[CONFIRM WRITE]`,
   pass the block unchanged into the prompt of the Step 6 ledger instance, which writes the row; the
   command confirms the row when that instance returns. Pass each Check #21 ruling (character, trigger,
   token) to that instance the same way; a `[SKIP WRITE]` discards them. If area-maker reports that a
   Tier D person acts or decides (Part 19 Rule 19.1.2.4), the command puts the keep-or-promote question
   to the author with the Position Header and full text printed first; on a promote ruling the pending
   draft is discarded as a `[SKIP WRITE]`, `/character-behavior` runs (Part 39 Rule 39.4.3.2a) and
   `/next-area` is run again; on a keep ruling the draft continues.
   **Named items hand-off (Part 28 Rule 20.8.4(e)).** When area-maker's handoff carries a
   `NAMED ITEMS (new in this Area)` block, the checker's Gate 1 report reconciles it with the italic
   names in the draft and returns the checked list (name, Type, home ledger entry or `none`, naming
   checks). Do not print the list in chat; a departure from the named-item form (Check #12) or an item
   the list missed appears in the Gate 1 report like any other finding. On `[CONFIRM WRITE]`, pass the
   checked list unchanged into the prompt of the Step 6 ledger instance, which enters each item as a
   row of `ledger-named-items/_index.md`; a `[SKIP WRITE]` discards it. The same block carries each
   named document and each named agreement, treaty or accord that is new in the Area (Part 28 Rule
   20.8.7), which the instance enters as a row of `ledger-society-information/_index.md`.
   The same route carries the `NAMED MOVES (new in this Area)` block (Part 6 Rule 6.5): the Step 6
   ledger instance enters each Named Move as a row of `ledger-named-moves/_index.md` and in each user's
   character-ledger Named Moves registry, the row and the entry pointing at each other.
   **Monsters hand-off (Part 40).** When area-maker's handoff carries a `MONSTERS (new in this Area)`
   block, the checker's Gate 1 report reconciles it with the monsters in the draft and returns the
   checked list (Kind or name, Kind or Individual, tier, what the Area established, Named Moves used).
   Do not print it in chat. On `[CONFIRM WRITE]`, pass the checked list unchanged into the prompt of the
   Step 6 ledger instance, which enters each Kind and each Tier C and D monster in
   `ledger-character-monster/` (Part 37 Thresholds M-1 and M-2); a `[SKIP WRITE]` discards it. When the
   checker or area-maker reports that a Tier C or D monster has reached a trigger of Part 40 Rule
   40.6.2.2 (it kills or maims a named person, destroys a named place or thing, becomes a recurring
   individual, or is tied to a Named Move), put the question to the author with `AskUserQuestion` before
   the draft continues, as for a Tier D consequence flag; the author rules and nothing promotes on its
   own. A non-sentient monster's hostility never raises the Threshold C-2 villain question, and a
   sentient monster in a Phase 1 draft is a Check #11 FAIL (Law P30-L9).
4. Present the Gate 1 result and wait for an explicit `[CONFIRM WRITE]` / `[REVISE AREA]` /
   `[SKIP WRITE]`; never assume confirmation. **Presentation format:** print, in this order, the
   Position Header Block (the complete five-tier name chain, Phase / Section / Novel-Part / Chapter /
   Area, Part 28 Area 18 Rule 18.3.1, plus Reference Code, the pacing and size target carried from the
   spec, a **Calendar line** (chat only: the date line as written, the Phase Day it stands for, the
   date of the previous Area and the Area window), and a "redraft in progress" line when later Area
   files sit after it on disk), the **full text of the Area, verbatim, its date line first**, never a
   summary, an excerpt, a paraphrase or a file path, the Contextual Earning Declaration, and the
   Post-Draft Audit Report (it names the Triggered Parts and every FAIL and gives one line counting the
   Not Triggered and N/A Parts; the full named-result list, every Part as Triggered, Not Triggered or
   N/A, goes to the session log, which meets the gate law's omission rule) with the Area window
   verdict, any reported flow pattern and its quoted lines, one line on the FAIL loop where it ran (the first
   audit's FAIL checks, the mode of the re-audit and its result; Author ruling, 2026-10-18), and the plan-versus-written list (Part 38
   Rule 6.1.4; a list with a BLOCKS line gets no confirmation prompt), then the confirmation prompt,
   which says that `[CONFIRM WRITE]` accepts the listed differences. The full text is printed at every
   Gate 1 and again after every `[REVISE AREA]`; when a question to the author is about the draft
   (Step 3), the Position Header and full text are printed before the question. No other
   assistant-authored commentary is wrapped around these blocks. Exactly one Area is ever presented at
   once; lines quoted from earlier Areas as evidence are not a presentation of it. `[CONFIRM WRITE]`
   accepts the non-settled spec differences and the sameness patterns the report lists;
   `[REVISE AREA]` rejects them, returns to Step 2, and re-runs the whole of Step 3 (both instances; a first full audit of the revised text, Author ruling, 2026-10-18)
   before the revised text is printed again; `[SKIP WRITE]` discards everything (see Failure/abort).
5. On `[CONFIRM WRITE]`: write the `.docx` and `.md` files as a coupled pair via
   `.claude/tools/area_docx_creator.py` and `.claude/tools/area_md_creator.py`
   (`guardrails/tools/guardrail-authorized-scripts-only.md`; no other write method), passing the
   writer's `is_first_area_of_chapter`, `is_first_area_of_phase` and `is_first_area_of_section`
  parameters (the CLI flags `--first-of-chapter`, `--first-of-phase`, `--first-of-section`) from the
  Area's position. Every
   Area file is written with the **Area Title Block** (the icon, the Area title and the Reference Code).
   For the first Area of a Phase or a Section the file also passes the epigraph lines of its Title Page,
   and which lines they are depends on the Area (Part 38 Rule 10.3.1). For the first Area of a Phase it
   passes TWO: the Phase epigraph, the `Epigraph:` line of that Phase in Part 30
   (`narration-novel-macro-story-law`), as the writers' `--phase-epigraph-file`, and Section 1's own
   Epigraph line from the header block of its Section Spec as `--section-epigraph-file`; the title page
   prints the Phase line first and Section 1's line second. For the first Area of any other Section it
   passes ONE, the Epigraph line of that Section's Section Spec, as `--section-epigraph-file` and no
   Phase line. `unset` means none for that line, and the writers are then called without its flag. The
   writers take the two values as `--phase-epigraph-file` (or `--phase-epigraph`) and
   `--section-epigraph-file` (or `--section-epigraph`), and they refuse a Phase line on any Area that is
   not the first of its Phase. No agent writes epigraph text or takes it from anywhere else. This
   command reads those lines itself, from the files, at this step (Part 30 and the Section Spec are not
   in the per-Area read set, so no agent has read them for it). From Part 30 the value is the text that
   follows `Epigraph: ` on the Phase's own `Epigraph:` line, which holds that text or `unset` alone;
   the label is never part of the value and the note line beneath it is never read; from a Section Spec it is the text of its Epigraph line in the header block. Pass
   `--output-root` as the absolute path of `projects/novel-starward-saga/` under the repo root (the
   folder that holds `.claude/`), never a relative path, so the files land in the same place whatever
   folder the session runs from. Each script prints the absolute path it wrote; the Post-Write Audit
   (Step 6) checks that path against the Area's position: 
   `projects/novel-starward-saga/phase-N/section-N/part-N/chapter-NNN/area-NN.docx` and `area-NN.md`
   (two-digit Area number, resetting per Chapter).
   The call, once per script (`area_md_creator.py` takes the same arguments). First write the confirmed
   Area text to a temporary UTF-8 text file outside `projects/` and `.claude/` and pass it with
   `--text-file`; that file is an input, not a script and not an Area file
   (`guardrails/tools/guardrail-authorized-scripts-only.md`). The file begins with the date line (Part
   41 Area 5): the writers print the Title Block above it. The `.docx` writer styles the date line as a
   centred, smaller italic paragraph and gives the drop cap to the first paragraph of narration after
   it; the `.md` writer keeps the line as typed.

   ```
   python .claude/tools/area_docx_creator.py write --text-file "<temp file>" --output-root "<repo root>/projects/novel-starward-saga" --phase P --section S --part N --chapter C --area A --phase-name "<name>" --section-name "<name>" --novel-part-name "<name>" --chapter-name "<name>" --area-name "<name>" [--first-of-chapter] [--first-of-phase] [--first-of-section] [--phase-epigraph-file "<file holding the text of the Part 30 Phase Epigraph line>"] [--section-epigraph-file "<file holding the Section Spec's Epigraph line>"]
   ```

   Give a `--first-of-*` flag only when it is true, `--phase-epigraph-file` only on the first Area of a
   Phase (with `--first-of-phase`) and `--section-epigraph-file` on the first Area of a Phase or of a
   Section, each only when that line is not `unset`. A writer refuses to replace an Area that is already
   on disk and stops with an error; only `/revise-area` adds `--overwrite` (a redraft moves the old pair to the archive first, so its
   write is a fresh one). If either script fails,
   stop as the Failure/abort section says. When both writers have returned, read the Title Block back
   from the `.docx` just written:
   `python .claude/tools/area_docx_creator.py check --file "<the .docx path the writer printed>" --expect present`
   (every Area file carries the Area Title Block). Hand the printed result to the Step 6 audit lane,
   which holds no shell (`guardrails/audit/guardrail-audit-gate-law.md`, Gate 2); that lane reads the
   `.md` file itself.
6. Invoke **continuity-checker** for the Gate 2 Post-Write Audit (Completeness Indicator and Tier Scope
   Brackets; give it the Step 5 Title Block read-back result) and, as a separate parallel
   continuity-checker instance, the Post-Write Ledger Update
   (`guardrails/ledger/guardrail-ledger-update-law.md`), which also performs the mandatory Part 38 spec
   as-built sync on the active Chapter Spec file (the Area row flips to `WRITTEN`; the last Area row of
   the Chapter going `WRITTEN` sets the Chapter Spec to `COMPLETED`; variance notes for every difference
   `[CONFIRM WRITE]` accepted and every item settled here go to the Audit and Settlement Notes section,
   with its registry row); see the 3-way split in Parallel orchestration above. The audit lane also
   reads the first line of the written `.md` and checks it against the date line confirmed at Gate 1,
   and the ledger instance writes the calendar rows (the Area row, the rollups and
   the Current Position block, which names the Open Chapter and the Open Chapter's recorded window,
   First to Latest) from that line and the checked `CALENDAR (this Area)` block; the as-built
   in-story time of the spec sync mirrors the line.
7. Invoke **area-scorer** (the date line is left out of every reading and of the size) to record the
   CDL-2 density score for this Area, produce the report-only Voice and Variety block, and update the
   Section running aggregate (the Section's tracker,
   `.claude/story-memory/cdl2-density-tracking/phase-N/section-M-aggregate.md`; the scorer creates it at
   the Section's first scored Area), launched together with both Step 6 instances, not after them. A
   density reading below or above its line, measured or forecast, is shown in the Gate 2 presentation as
   information and raises no question and no FAIL
   (`guardrails/quality/guardrail-threshold-consultation.md`), once the first Chapter of the Section has
   closed; until then the running aggregate is provisional, shown without a status mark, and nothing is
   raised to the author on account of it (Part 35 Area 4.1).
8. Log the outcome to `.claude/story-memory/session-log/`.

## Failure/abort

`[SKIP WRITE]` discards everything: no file is written and no ledger or spec update runs, so files,
ledger and spec agree; the draft, its audit, the differences its plan-versus-written list showed and any
name it introduced are dropped, and a name delivered in a discarded draft is not established. Any
irreconcilable Gate 1 conflict is escalated via `AskUserQuestion`, never force-written.

A failed Gate 2 write (Step 5) stops the invocation: remove the file the other script already wrote for
this Area (a plain delete; no script and no Area file is written), run no ledger update and no spec
sync, show the author the error, and wait. The confirmed text is still in the conversation, and the
author re-issues `[CONFIRM WRITE]` to try the write again once the cause is fixed (Part 2 Rules 6.4.5
and 7.4.3). The Area is not counted as written until both files are on disk.
