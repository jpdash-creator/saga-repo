# Guardrail: The Two-Gate Audit Pipeline

**Source:** this guardrail (the audit layer has no skill file) · Canon v10.0
**Applies to:** all 4 agents — this is the backbone every `/next-area`-style command runs through; `/create-chapter` and `/revise-chapter` run the Whole-Chapter Gate 1 section (Amended 2026-10-07)
**Re-audit scope:** the Re-Audit step of the Correction Protocol is scoped by the section "Re-audit after fixes" below; the first Gate 1 audit of a draft stays full and the loop's purpose is unchanged (Author ruling, 2026-10-18)

## The rule

Every narrative output is validated against the complete applicable canon before it is
accepted. No prose is written to disk, and no ledger is updated, outside this sequence:

1. **Pre-Write Ledger Check** — read current state from
   `.claude/story-memory/ledger-*/` before drafting anything, and read the active Chapter's
   confirmed spec chain alongside the ledgers (Part 38, `.claude/guardrails/ledger/guardrail-story-spec-law.md`).
   For the per-Area agents (the drafting agent, the scorer, both Gate 1 checker
   instances and the Outline Planner when it plans one Area; the per-Area read set, Part 38 Rule 9.9.2) the chain read is the Chapter Spec in full plus the header block and the closing-state block of its
   Novel-Part Spec; the Section Spec is not in that set, because the Chapter Spec carries every
   inherited item with its source recorded in its Audit and Settlement Notes. Nothing is cut down by this: those reads are simply not
   mandatory for a per-Area agent. The chain must be in force before drafting (Check #18(a) below;
   Part 38 Rule 9.1.1). The specs supply the Area's planned slot, the
   ledgers supply established state, and on conflict the ledger supersedes the spec.
2. **Draft** — Area Maker writes the Area (never the file yet).
3. **Gate 1 — Post-Draft Audit** (Area 9): a 23-check mandatory sequence, numbered 1 to 23 in the order given, run before any
   `[CONFIRM WRITE]` offer, performed by the Continuity Checker:
   #1 Parts checked (all applicable Parts, currently 2–33 and 35–44 (Part 44 registered, 2026-10-17)) · #2 Ledgers checked (all folders) · #3 no em-dashes · #4 no contractions anywhere in the Area body, in narration or in direct speech (any contraction FAILs; Canon Amendment 2026-10-16 reversed the dialogue allowance of 2026-10-08, Part 29 Rule 29.2.1.1c), and the Flowing Dialogue Standard as an explicit pass/fail item of the same check (Canon Amendment 2026-10-16, Part 29 Rule 29.2.1.7a: full grammatical sentences, speakers answer and build on the previous line, turns usually two to four connected sentences, no chain of clipped fragments, no statement-comma-clipped-jab pattern; a chain of clipped fragments, the comma-jab pattern or a non-answering exchange FAILs, quoted in the report; the count stays 22) ·
   #5 dialogue format `*"..."*` (a named item's name set in roman inside the speech is the one lawful break, Part 28 Rule 20.8.2(c); the channel forms of Part 29 Rule 29.14.3.3 are not speech aloud and are read there, so their plain-type forms are not flagged here) · #6 filter language (advisory) · #7 Named Moves (CDL2-L6 reading, information only) ·
   #8 cultivation realm accuracy, which also reads Cultivation Visibility (element 8-V, Part 29 Rule 29.12.1.3, Canon Amendment 2026-10-16): every named person in the text has their level made known by sensing, speech, a short identification or an event; every combatant's level is known before or at the first blow and each cross-level moment is narrated; a sealed character shows current and true level where the viewpoint knows; a level shown again when changed; woven in, never a stat dump; a named person with no level shown, or a fight with an unknown combatant level, FAILs Major, the count is 23 · #9 deep POV maintained (per-segment in a spec-designated Dual-POV Area, Part 2 Rule 4.3.1) · #10 Area size (1,280 to 2,400 words, Part 2; a count outside the range is a blocking finding, reported with its word count: the write waits for the author to confirm the Area or send it back) · #11 Part 30
   Phase-1-framework compliance (**Check #11**, six elements 11-1 through 11-6: Section-close cultivation band, date and age (element 11-2 also reads the Area's date line against the Current Position block and the Area's row of `ledger-worlds-calendar/_index.md` and against the Chapter Spec's dates for the Area: a date never runs backward without a lawful cause, an Area that continues a scene starts on the day and moment the Area before it ended, an Area starts on or after the last day of the Area before it save at a flashback, memory, dream or vision, and each Area, Chapter, Novel-Part and Section sits inside the dates of the level above it, the month is in the calendar's table and the Day is inside that month's length, the weekday is the one the calendar's formula gives for that Year, Month and Day (a wrong weekday FAILs like a wrong day number), a range runs in order with each end checked on its own, a scene that opens in the last dark hour and runs on into a dawn is read as that dawn's day with no range (Part 41 Area 2, the one scoped exception to the dawn-to-dawn day), the protagonists' ages agree with Part 30, and a festival scene falls on its festival's fixed day; a planned step back at a `cut to another thread` Area is reported as information; Part 41, Area 6, Dating rules and the check), the forbidden-entity scan (Law P30-L8 and Law P30-L9, no sentient monster in Phase 1), Section major functions, the P30-L5 ten-Chapter window and the progression-axis beat per Area; the first three read Locked Canon facts and a contradiction FAILs (the Section 5 and Section 6 cells for Hercules and Bison in element 11-1 are guide posts, reported as information), the last three are floors reported as information, never a FAIL; defined in Part 30 Area 2) · #12 bold-italic formatting (Named Moves and cultivation levels) and named-item italics (a named item, which includes a Named Relic, Artifact, formation array and energy cache, not in italic, in italic inside an italic span, in bold, with its leading article inside the name or the italic, or in a form other than its registered one FAILs; a named document not in italic, or an agreement, treaty or accord not in roman, FAILs the same way; a registered item name italicised for emphasis is reported at the same check; Part 28 Rule 20.8.2, 20.8.5 and 20.8.7) and the italic form of the date line (one paragraph, wholly italic, the first line of the Area text directly under the Area Title Block, written `*Year 1247, <Month>, <Weekday>, Day 27*` or in its range form with the weekday at both ends, commas as set and no full stop) and the roman form of a month or weekday name written anywhere else in the text (neither is a named item); a line that is missing, misplaced, not wholly italic or in any other form FAILs (Part 41, Area 5, The date line) · #13 canon-manifest dependency-map
   consultation · #14 character ledger state verification · #15 ledger obligation scan · Novel
   Thematic Compliance (Part 36 Check #16, twelve dimensions: 16-A to 16-I, plus 16-J Area flow review, 16-K Voice and Variety and the named dimension 16-DP, Depth Pillars and quota-filler test, reported for the author's ruling) · Entity Naming (Part 28
   Area 20, Check #17, which also reads each new Named Move name against the Move-Naming Law of Part 42 Rule 42.12.2.3, Canon Amendment 2026-10-08) · Spec Conformance (Part 38, Check #18: the drafted Area is compared with every spec-planned element and shown as a plan-versus-written
   list; a difference on a core item (Part 38 Rule 6.1.1(b): the beat (the Area's purpose); the scene anchors (their order is part of the anchors); the Continuation; the viewpoint (the Dual-POV mark included); every planned time skip; the Behavioral Plan (Rule 6.1.2); the Opening type; the Closing type; the Thread or storyline; and every settled item) blocks unless it traces to an on-record author answer from
   this invocation; pacing is a listed difference, shown and never blocking (Part 38 Rules 6.1.1(d), 6.1.3); size is structural and blocks: a count outside 1,280 to 2,400 words is a blocking finding: the write waits for the author to confirm the Area or send it back (Part 38 Rule 6.1.4); every other difference is listed, `[CONFIRM WRITE]` accepts the listed
   ones (the spec is updated at Gate 2) and `[REVISE AREA]` rejects them; **18(a), the chain is in force:
   no Area is drafted against a plan the author has not
   confirmed, at every level of the plan:** the Chapter's Chapter Spec is CONFIRMED (or COMPLETED,
   when an older Area is revised) AND its Novel-Part Spec AND its Section Spec are each CONFIRMED or
   COMPLETED, and none of the three is DRAFT, AMENDED-PENDING-RECONFIRM or RETIRED. A missing or unconfirmed
   link is a FAIL: Critical where no chain stands (a link is missing, DRAFT or RETIRED), Major where a link
   stands but is AMENDED-PENDING-RECONFIRM (Part 38 Rules 6.1.3 and 9.1.3), and the FAIL names the first missing link and the
   command that fixes it (`/section-spec`, `/part-spec` or `/chapter-spec`). The check reads each link's
   status from its registry row; it adds no comparison of the Area with the Section Spec or the
   Novel-Part Spec, whose plan the Chapter Spec already carries, and the plan-versus-written list is
   still made against the Chapter Spec alone. The count is 23) · Prose Vitality (P28/P29/P36,
   Check #19 — countable closer-variety, single-statement, voice-signature,
   epigram-budget, and friction-floor rules (Part 28 Area 13 / Part 29 Area 4) plus the
   qualitative vitality dimensions 16-G/16-H/16-I; counted over the Area under audit and read as information only, so a count never produces a FAIL; defined in Part 36 Area 17) · Behavioral
   Conformance (Part 39, **Check #20** — eleven live elements (20-3 is retired) 20-1 through
   20-12: registration completeness, signature conformance, the signature
   recurrence, contradiction and cost presence, the L29 waiting beat, off-register
   count, collective-code conformance, demonstrated-not-named, provenance integrity,
   age-band anchors, and boundary integrity; the count elements are listed once, in Part 39 Area 43.3, are information only and never produce a FAIL; element 20-2 also reads a non-sentient monster's recorded traits in light form, Part 40 Rule 40.5.4.1; defined in Part 39 Area 43) · Behavioral Change
   Detection (Part 39, **Check #21** — **blocks by asking, not by failing**:
   fires as Part 39 Area 44.2 sets out: on an unmapped trigger (or a mapped one that breaks
   L34-END), a contradicted Signature, a flagged item the author has not yet ruled, an Area
   in which the prose shows a POV character's profile moving, a Section close for the characters
   whose profiles the prose shows moving, and automatically at PIS-7, CSS-8, an age-band crossing or
   a realm crossing, and a boundary review that finds none of D-1 to D-4 reports SILENT
   and asks nothing; the author rules `[KEEP PROFILE]` / `[EVOLVE]` / `[REVISE AREA]` /
   `[PROVISIONAL]` / `[DEFER]`; defined in Part 39 Area 44. **Check #21 widened (evolution, 2026-10-06; Part 43, Character Evolution Law):** at Gate 1 it detects EVERY behaviour change in the draft for every character (the 36 Layers, the 12 Signatures and the bound properties). For heroes and Tier A side characters, villains and monsters it asks the author with `AskUserQuestion`; for Tier B, C and D side characters, villains and monsters the Gate 1 continuity-checker decides itself and records its decision and reasons, asking nothing. A change to an immutable trait always needs the author's explicit ruling and a recorded reason, for every tier. Gate 2 presents every evolution (all tiers) with its recorded information. A `[REVISE AREA]` send-back goes through `/revise-area`. No new command exists, and evolution is not drift.) · Plain Language and Narrative Impact (**Check #22** — seven elements 22-1 through 22-7: heavy-word instances in narration and in dialogue, each flagged with its plain alternative and both reported as information rather than silently rewritten; setting-grounding against modern slang; colloquial calibration by relationship; impact and wonder reached for where the scene earns it and never strained for where it does not; plainness-without-flattening, so no Depth Pillar, image or sensory anchor is lost while simplifying vocabulary; and the crutch-word watchlist, listed for every Area as information. **Check #22 vocabulary elements (plain vocabulary, 2026-10-06):** the check also blocks a special or invented word with no picture at first use, one word carrying two meanings in an Area, a jargon wall (three or more unexplained special terms in one sentence or speech) and a figure the reader cannot parse at first read; 22-3, 22-6 and these new elements block, while 22-1, 22-2 and 22-7 inform. **Sentence length is deliberately NOT an element** — that absence is the author's ruling, not an oversight, and no pass may add it without a fresh directive; defined in `.claude/guardrails/quality/guardrail-plain-language.md`). Battle Plausibility (**Check #23**, Part 44, Canon Amendment 2026-10-17: elements 23-1 through 23-6 run on every Area whose text holds a fight and read N/A for an Area with no fight, and element 23-7 reads every Area; seven elements 23-1 through 23-7; the checker builds an engagement ledger from the draft and the ledgers (each side's anchors, every pairing that meets with its gap in minor steps and its band Open, Shut or Barred, the offset that explains any held gap, its price, the outcome) and compares it with the Engagement Ledger of the Chapter Spec. **Blocking (FAIL):** 23-1 anchors and levels, 23-2 pairings (the 3-Level Rule; a Major Realm crossing with no lawful offset under Part 3 Rule 17.3.3), 23-3 presence and survival (a side unable to be present or survive at the stated levels), 23-4 offsets (unlawful, unbounded, unpriced, a limit break not priced on the page afterwards or past its reach or hard cap, or a gifted fighter not registered in the ledger before the scene), 23-5 outcome (a result the levels forbid), 23-7 no gap arithmetic in prose (narration or dialogue that states minor steps, percentages, multipliers, "N levels above" or a computed gap; level strings and sensed comparison in words are lawful, Part 44 Area 5.3). **Reported, never a FAIL:** 23-6 strain, a lawful but strained mismatch, listed for the author as a ruling point at `[CONFIRM WRITE]`. Not retroactive: Chapters 1 and 2 hold no fight. Defined in `.claude/guardrails/quality/guardrail-battle-plausibility.md` and Part 44). **A Gate 1 skipped entirely,
   or delivered with any single check FAILing, is a Critical Violation of this law** — Gate 2
   is blocked until a clean re-audit (the re-audit of the Hard rules, in full or after fixes; Author ruling, 2026-10-18). Check #21 is not satisfied by an unanswered question:
   an open Check #21 enquiry blocks Gate 2 exactly as a FAIL does.
   **Area flow review.** An Area is the written unit: it may be a complete scene, or a scene may
   continue across consecutive Areas of the Chapter. Every Gate 1 audits the new Area with the 23 checks
   and also reviews it against the Area before it as one flow. The review is
   dimension **16-J (Area flow review)** of Check #16; the count is 23.
   - **Area window.** The Area window is the read set defined once in Part 2 Rule P2-Area-1: the draft, the Area before it, read in full from its written `.md` file (for the first Area of a Chapter, the last Area
     of the previous Chapter; the first Area of the novel has none), and, where the scene under audit continues a scene begun earlier, the earlier Areas of that scene, read
     in order. The checker also reads the Area block of the active Chapter Spec. For the two reported patterns that compare with earlier Areas (openings and closers;
     register) the checker also reads the first paragraph and the last
     paragraph of each earlier Area of the Chapter (and of the previous
     Area when it lies in the previous Chapter), with the tone tags the spec gives them; these reads support a
     reported pattern and never block. The checker also searches the written Areas of the Section, files already on disk, for item (l) of 16-J
     Read 2 below.
     When a later Area is already written (after `/redraft-area` or `/redraft-chapter`), the review
     also reads the carry-over into that Area's opening.
     `[SKIP WRITE]` discards everything, so every earlier Area read is on disk.
     Never read, list or count files under `_archive`; read each file by its exact
     path (Part 2 Rule 5.3.2a).
     For a revised Area (`/revise-area`) the read set is the Area as written with the
     revised text in place of the old, with the Area before it and the Area after it when written (the read set of Rule P2-Area-1 with the following Area added for a revision): ceilings are counted on it, floors and
     whole-scene properties are read on it, and the neighbour check is the carry-over reading of 16-J at both ends.
   - **Two read-only instances, launched together.** One runs Checks 1 to 23 with 16-J
     excepted (the window reads and counts of Part 36 Area 2.4, the rest on the draft); the other runs 16-J on the window. The 23-check instance re-reads
     `.claude/canon-manifest/*.json` fresh at this checkpoint (the targeted read of
     `.claude/guardrails/audit/guardrail-forced-read-discipline.md`); the flow-review instance checks no cross-Part
     edge and makes no manifest re-read. Their results are merged into
     one named-result list; the flow review is not a second full-canon pass. This is the shape of the first audit and of a full re-run; a re-audit after local fixes runs as the section "Re-audit after fixes" sets out (Author ruling, 2026-10-18).
   - **Continuity findings block.** A break of time, place, point of view or character state
     inside the Area, or at the carry-over from the Area before it, is a FAIL, unless the
     spec's Area block plans it (a catalogued viewpoint change, ⁂ time skip, or planned cut
     between Areas) or the author ruled it in this invocation (Part 38 Rule 6.1.1(b)). An
     unplanned gap is a FAIL. An Area that continues the previous Area's scene opens in motion from the exact state the previous Area left (same place, moment, register, no second opening and no recap); a second opening or a recap is a continuity finding.
   - **Sameness is reported, not failed.** The patterns of 16-J Read 2 (repeated openings,
     closers and carry-over shapes; cadence; explanation clustering or one sense leading every
     Area; worn figures and repeated callbacks; one register throughout; the shape of a fight
     against the fight before it, read from the spec's Fight lines; a search
     of the Section's written Areas for each quoted figure and repeated three-word phrase, with
     each hit's reference code; and the new names met) appear in the audit
     report with the lines that show the pattern, quoted. The author rules: `[CONFIRM WRITE]`
     accepts the pattern, `[REVISE AREA]` rejects it, or the author ends the invocation
     with `[SKIP WRITE]`, revises the spec's opening or closing type through `/chapter-spec`
     and runs `/next-area` again. No agent revises a sameness pattern on
     its own.
   - **Ceilings run, floors close.** A ceiling (a run, a rate, a budget) is checked on every
     pass against the window. A floor or a whole-scene property is read on the Area under audit and, for a scene that continues across Areas, again on that scene's Areas read in order (Part 36 Area 2.4); neither reading fails an Area.
   - **Counts.** Where a Part counts over the Area (Part 36 for Check #19, Part 39 for
     the Area-level elements of Check #20), the report states the Area (by reference)
     and the counting method, and a crossed line is shown as information under
     `.claude/guardrails/quality/guardrail-threshold-consultation.md`.
   - **Report.** The flow verdict, every continuity finding (16-J Read 1) and every reported
     pattern (16-J Read 2, the Area Flow REPORT block of Part 36 Area 16.3) name the Areas read by
     Reference Code, are pinned to an Area reference and its carry-over, and sit inside the
     Post-Draft Audit Report beside the plan-versus-written list of Check #18.
   - **Area status.** At its Gate 2 the ledger lane's spec sync writes the Area's row `WRITTEN` (Part 38 Rule 3.6.1),
     the scorer lane adds the Area-level CDL-2 block and the Area-level Voice and Variety block,
     and Block B's Tier Scope Bracket lines carry the Area emission (Part 2 Rule
     9.10.3). Check #21's enquiry (run by the 23-check instance) runs for every POV character whose profile the prose shows moving in the Area (Part 39 Area 44.2).
   **Calendar.** Every Area opens with its
   date line (Part 41, Area 5, The date line), and every Gate 1 reads it, under Check #11 element 11-2 for the
   dates and the weekday and under Check #12 for the italic form, as set out in the two checks above and in Part 41
   Area 6 (Dating rules and the check). A failure of either reading is a FAIL like any other under those checks; the one
   thing that is information only is a date that steps back at a planned `cut to another thread` Area. The count
   of checks is 23 and the six elements of Check #11 stay six. The Position Header Block carries a **Calendar
   line**, in chat only: the date line as written, the Phase Day it stands for and the date of the Area before it. At Gate 2 the audit lane also reads the first line of the written `.md` and checks it
   against the date line confirmed at Gate 1; a difference is reported as a Post-Write Audit finding that blocks
   nothing already confirmed. The date line is not narration: it is not counted in the Area size (Check #10) and it
   is never the Area's opening or closing paragraph for any reading of Checks #16, #19 and #22 or of the Area
   Scorer (Part 2 and `.claude/guardrails/quality/guardrail-tier0-narrative-quality.md`).
4. **Inter-Gate Confirmation** — `[CONFIRM WRITE]` / `[REVISE AREA]` / `[SKIP WRITE]`,
   required on every single Area, every time. No exceptions for "obviously fine" Areas.
   The full text of the Area has been printed in chat before the prompt appears
   (`.claude/guardrails/commands/guardrail-command-law.md`, Gate 1 Chat Delivery format). `[CONFIRM WRITE]`
   also accepts the non-settled spec differences and the sameness patterns the audit report
   lists; a plan-versus-written list with a BLOCKS line gets no
   confirmation prompt (Part 38
   Rule 6.1.4). `[REVISE AREA]` rejects the listed differences, returns to drafting, re-runs
   Gate 1 in full (both instances; a first full audit of the revised text, Author ruling, 2026-10-18) and prints the revised text in full again; `[SKIP WRITE]`
   discards everything — the draft, its audit, the listed differences and any name it
   introduced — and nothing is written or updated, so files, ledger and spec agree.
5. **Gate 2 — Post-Write Audit** (Area 10): file creation only via the authorized
   `.claude/tools/area_docx_creator.py` / `area_md_creator.py` scripts (see
   `.claude/guardrails/tools/guardrail-authorized-scripts-only.md`), written as a coupled pair, `chapter-NNN/area-NN.docx` and
   `chapter-NNN/area-NN.md`. The file check confirms the path: each
   writer prints the absolute path it wrote, and that path must lie under the repo's
   `projects/novel-starward-saga/` at the Area's position (`phase-N/section-N/part-N/chapter-NNN/area-NN`); a file written anywhere else is a Post-Write Audit FAIL. It also reads the Area Title Block
   as present in the file of every Area (Part 2 Rules 6.3.2a and 6.6.1) — in the `.docx` by the
   script's own read-back, `python .claude/tools/area_docx_creator.py check --file <path> --expect present`,
   which the orchestrating command runs and whose printed result it hands to
   the audit lane (that lane holds no shell), and in the `.md` by reading the file for its `## Area` heading and
   `*Reference:` line; an Area Title Block missing from either file is a Post-Write Audit FAIL, repaired by the orchestrating command deleting the
   wrong file or files (a plain delete, as the failed-write rule of `/next-area` does), re-running the
   writer script for each with the correct flags and without `--overwrite` (only `/revise-area` passes it)
   over the same text, and re-running the audit lane;
   the ledger lane's writes stand, because the text is unchanged. The audit, ledger and
   scorer lanes run together and none waits for another. Two mandatory blocks follow every
   write: Block A (Completeness Indicator: carry-forward checks, ledger-obligation
   discharge, tier hierarchy counts, and the CDL-2 block that follows, which is the
   area-scorer's, with the Area-level CDL-2 block) and Block B
   (Tier Scope Brackets). The audit lane cannot see the other two lanes' returns, so it
   shows the ledger-obligation line as "pending merge"; after all three lanes return, the
   orchestrating command merges the ledger instance's return (the obligation discharge)
   and the scorer's block into Block A.
6. **Post-Write Ledger Update** (command `/force-ledger-audit`) —
   mandatory, not optional, every time prose changes canon state; this includes writing every
   executed behavioral drift to Character Ledger Section 12 and editing Section 11 where the
   drift is Permanent (Part 39 Areas 41–42), and entering each named item the Area wrote as a row of
   `ledger-named-items/_index.md` (Part 28 Rule 20.8.4), and each named document and each named agreement, treaty or accord as a row of `ledger-society-information/_index.md` (Part 28 Rule 20.8.7), and entering each monster Kind the Area first described and each Tier C and Tier D monster it introduced or changed in `ledger-character-monster/` (Part 37 Thresholds M-1 and M-2; Part 40 Area 7), and writing the calendar rows of `ledger-worlds-calendar/_index.md` for the Area just written (its Area row, the rollups up the Chapter, Novel-Part, Section and Phase rows, and the Current Position block; Part 37 Threshold D-1; Part 41, Area 9, The calendar ledger), which `[SKIP WRITE]` never writes; the same Continuity
   Checker instance also performs the mandatory Part 38 spec as-built sync on the active
   Chapter Spec file — status flips (the Area's row going `WRITTEN`), variance notes (including every difference `[CONFIRM WRITE]`
   accepted) and settlement notes, written in the Audit and Settlement Notes section, and the Area's
   pacing and size carried as the spec records them (Part 38 Rule 3.6.1),
   with the spec's registry row (`.claude/guardrails/ledger/guardrail-story-spec-law.md`). The sync's write set is the ledger files plus the active Chapter
   Spec and its registry row, and the Gate 2 split is three-way. It writes no Novel-Part
   Spec and no Section Spec: their statuses are derived or are written by the spec flows and the
   boundary commands (Part 38 Rule 9.4.3), and variance reaches an upper spec only through those flows
   (Part 38 Rule 9.4.5), never at Gate 2. For the same reason the Coverage cell of a Section or Novel-Part
   registry row is not touched at Gate 2: it is refreshed only at that spec's own confirm, at a completion
   write step and at a reset or rewind rollback (Part 38 Rules 1.2.2, 10.1.2 and 11.1.2). The one addition is the Chapter Spec's own status: the sync
   sets it to COMPLETED when the last Area row is written (Part 38 Rule 3.6.1 item 1), the Chapter
   Spec's registry row following.

## Hard rules

- **Full-Canon Named-Result Check.** Every audit pass evaluates all applicable Parts
  (currently 2–33 and 35–44 (Part 44 registered, 2026-10-17)) by name — Triggered / Not Triggered / N/A. Silent omission of any Part is itself a POST-AUDIT
  FAIL. (Author ruling, 2026-10-18) The pass that names every Part is the first full audit of a draft and any full re-run; a re-audit after fixes names the checks it re-ran and carries the others from the first full audit (section "Re-audit after fixes").
- **One-Area-Per-Invocation.** For `/next-area` and `/revise-area` (the Area pipeline), never batch multiple Areas through a single Gate
  1→Gate 2 pass. The Area before the new one is read, never batched: it is read
  for the flow review, but only the new Area is planned, drafted, presented, confirmed and
  written. (Amended 2026-10-07: this binds the Area pipeline only. `/create-chapter` and `/revise-chapter` are
  the lawful whole-Chapter writer and reviser, a new rule and not an exception; they run the Whole-Chapter Gate 1
  and Gate 2 set out in the section below, write no Area file, and never batch Areas through the Area pipeline.
  A Chapter is built either by Area or whole, never both.)
- **Pre-Area Read Mandate.** All governing Parts + all relevant ledgers + the Area before the one being written
  (in full, plus the earlier Areas of a continued scene) must be
  (re-)read before drafting; older Areas and Chapters reach the writer through the ledgers, and a fact from an
  older Area is checked by opening that Area by search (Part 28 Area 4.6) — no
  exception on grounds of session
  boundary (this is the files-only discipline; see `.claude/guardrails/ledger/guardrail-session-log-not-canon.md`).
- **Correction Protocol** on any FAIL: Acknowledge → Prioritize → Revise → Re-Audit → Iterate.
  Termination only on Clean Audit or Irreconcilable Conflict — never on "close enough." The scope of the Re-Audit step is set by the section "Re-audit after fixes" below (Author ruling, 2026-10-18): after a limited set of local fixes it is the fixes plus a regression sweep, otherwise the whole Gate 1 again; a clean re-audit of either kind is a Clean Audit.
  Four rules on that loop (the first two from `.claude/guardrails/quality/guardrail-threshold-consultation.md`):
  - **A numeric reading is information, not a FAIL.** Check #19's countable elements, Check
    #16's countable dimensions (the exposition ceiling, the three-consecutive-mode rule), and
    Check #20's count elements (the single list in Part 39 Area 43.3) are guide posts: a crossing is reported with the value and the line it crossed, and
    nothing is revised, blocked or asked because of it. The Area size limit (Check #10) is the
    one word-count limit, it is structural and it follows Part 2: a count outside 1,280 to 2,400 words is a blocking finding: the write waits for the author to confirm the Area or send it back. It is reported with its word count and the counting method; pacing stays a craft matter independent of size.
    Non-numeric FAILs — Check #17 entity naming and the Check #16 dimensions that can FAIL (16-G, 16-I, 16-J Read 1 and a content-limit breach under 16-D); the craft findings of 16-A, 16-C, 16-D, 16-E, 16-F, 16-H, 16-K and 16-DP are reported for the author's ruling and enter no loop — keep the
    loop above, except where the remedy would change what happens on the page rather than how a
    line is worded, which is brought to the author.
  - **Diminishing Returns and Structural Impossibility are not an agent's to declare.** Either
    is brought to the author instead of terminating the loop. No agent rules a canon
    requirement unsatisfiable on its own judgment.
  - **Two audits of unchanged text that return different verdicts stop the loop.**
    If two audits of text that has not changed between them return
    different verdicts on one dimension, the orchestrating command prints both verdicts, each
    with the lines it quoted, and asks the author to rule. No further automatic revision is
    made until the author has ruled.
  - **The loop revises the new Area only. The first Gate 1 audit runs both instances in full, and so does any re-run that the section "Re-audit after fixes" calls for; a re-audit after local fixes is scoped by that section (Author ruling, 2026-10-18).**
    When the cause of a flow finding lies in an earlier
    Area, the new Area first repairs it if that solves it. If it does not, the earlier
    Area is named (Reference Code and name) and the author is asked, with the Position
    Header and full text of the new Area printed first, whether to run `/revise-area` on it
    first. If the author agrees, the pending draft is discarded (this invocation ends as a
    `[SKIP WRITE]`: nothing written or updated) and `/next-area` is run again once the
    revision is written. If the author declines, the author chooses another repair; the
    finding stays blocking until it is repaired or the author rules a canon amendment, and
    nothing is accepted automatically. When the cause of a carry-over finding lies in a later Area
    already written (after `/redraft-area` or `/redraft-chapter`), the new Area is repaired
    inside itself if that solves it; otherwise the author rules: hold the Area as
    written, or accept the carry-over and run `/revise-area` on the later Area once this one is
    written (recorded as a variance). No agent edits a written Area file: a
    forbidden-vocabulary hit found in one is named at once and corrected through
    `/revise-area` (Part 2 Rule 5.3.2a).

## Re-audit after fixes (Author ruling, 2026-10-18)

This section sets the scope of the Re-Audit step of the Correction Protocol, in the Area pipeline and in the
Whole-Chapter Gate 1 alike. The author ruled in chat on 2026-10-18: "If we ran a full audit after fixes, just run the
ones that were fixed. A full audit takes a lot of time. ... if there were a few fails in the first full Gate 1 audit,
next time it runs only the fixes." The purpose of the loop does not change: no FAIL stands unfixed, a fix must not
create a new fault, and the author may stop the loop at any time. The earlier practice, the whole Gate 1 again (both
instances) after every fix pass, stays the rule wherever this section calls for it.

1. **The first Gate 1 audit of a draft is always full:** the 23 checks and the flow review, both instances. A text the
   author sends back with `[REVISE AREA]` or `[REVISE CHAPTER]`, and a revision made by `/revise-area` or
   `/revise-chapter`, gets a first full audit of the revised text (a revision is never audited by its diff alone). The
   rest of this section governs the loop that follows a first full audit that returned FAILs.
2. **The continuity-checker decides the scope of each re-audit and states its reason in its report.** It decides by
   judgement and not by a count: no number of findings, lines or percentage is a threshold, and "a few" in the author's
   ruling is judged, not counted. In doubt, it runs the affected checks in full.
3. **Fixes only (the re-audit after local fixes).** When the first full audit returned a limited set of FAIL findings
   and each remedy is a located, local fix (a word, a line, a clause, a name, or a beat the confirmed Chapter Spec
   already plans and the draft left out), the re-audit runs only the four items below and reports `FIXES CONFIRMED` or
   the remaining findings. It is cumulative: it covers every line changed since the last full audit, not only the
   latest fix pass.
   - (a) The checks that produced a finding, on the lines and passages the fixes touched (a cut counts: the lines
     either side are read).
   - (b) The touched lines, and only those, read for the line-level faults a rewrite can newly bring (a form or format,
     a name, a plain-vocabulary slip, a level line, a speech line, a line of a character's conduct), each check named
     with its reason, so that a fix does not create a new fault. This is a read of the fixed lines and never a re-run
     of a whole check. A restored beat, or any added passage, is read as new text: under every check that reads a passage, with its two edges read for carry-over.
   - (c) The mechanical regression sweep of the whole text, for the cheap deterministic items: the size (an Area against
     1,280 to 2,400 words; a whole Chapter by the script `measure`, per Area block and in total, reconciled with the
     checker's own count); the hidden markers (each present once, in order) and the break rule; contractions (Check #4);
     em-dashes (Check #3); forbidden vocabulary (`.claude/guardrails/authority/guardrail-prohibited-creative-acts.md`)
     and the modern-slang words that Check #22 element 22-3 names; a name scan for every name new or changed since the
     first audit (Check #17, with the register and collision scan, the Move-Naming Law for a Named Move and the item
     form of Check #12); and every date line (Check #11 element 11-2, rules R1 to R6 of Part 41 Area 6, and the form
     under Check #12).
   - (d) A fresh reconciliation of every hand-off block (CALENDAR, TIER D, NAMED ITEMS, NAMED MOVES, MONSTERS,
     BEHAVIOUR CHANGES, STRANGER PASS) that a fixed line touches, so that the blocks passed to Gate 2 match the final
     text.
4. **The affected checks in full.** The re-audit instead runs each affected check over the whole text, as in a first
   audit (and the flow review too where a seam, a viewpoint or the order of events is touched), when: the first audit's
   findings were widespread or structural (where they reach most checks or most of the text, the whole Gate 1 runs
   again, both instances, as before this ruling); a fix changes what happens on the page, adds a plot fact or a person,
   moves a viewpoint, or crosses an Area seam (restoring a beat the confirmed spec plans is a local fix under item 3, read as new text, and does not by itself count here); the sweep or the touched-line read finds a new fault that is more than a
   one-word slip; or the author orders a full re-run, which the author may do at any time. A beat or fact the Chapter
   Spec does not carry is not a fix: it is brought to the author (the Correction Protocol's first rule), and after the
   author's answer it takes this full re-run.
5. **Inputs.** The orchestrating command gives the checker the first report's findings (check and element, Area or Area
   block, quoted line, severity), the fixer's list of fixed lines (each pinned to its Area or Area block, the old line
   and the new line quoted) and the revised text. A changed line that is not on the list is a touched line too, and an
   Area block whose word figure moved with no listed fix is read in full.
6. **What stays.** The re-audit is a Gate 1 pass: the 23-check instance re-reads `.claude/canon-manifest/*.json` fresh
   from disk (the targeted read of `.claude/guardrails/audit/guardrail-forced-read-discipline.md`), and the Parts,
   ledgers and spec block behind each check it runs are read in full (an instance resumed by `SendMessage` holds them
   from its first pass). Two instances launched together are the shape of the first audit and of a full re-run; a
   re-audit of local fixes may run in one instance, the 23-check instance, which carries the sweep, with the flow-review
   instance joining only when a finding came from the flow review or a fix touches the flow or a seam. The third rule
   of the Correction Protocol stands: a re-audit that disagrees with the first full audit about text the fixes did not
   touch is two audits of unchanged text with different verdicts, and the orchestrating command prints both and asks the
   author. The Full-Canon Named-Result Check is met for the draft by its first full audit; a re-audit names the checks
   it re-ran and carries every other check's result for the untouched text.
7. **What the author sees.** The Post-Draft Audit Report carries one line on the loop (the checks that FAILed in the
   first audit, the mode of the re-audit and why, its result), so that the author can order a full re-run before
   `[CONFIRM WRITE]`. Reported patterns, ruling points (23-6) and Check #21 enquiries stand from the first full audit (a
   quoted line a fix changed is re-quoted from the revised text or dropped); information counts are those of the first
   full audit and are labelled so. Revisions inside the loop are not printed
   (`.claude/guardrails/commands/guardrail-command-law.md`).
8. **Reading this section with the rest.** A clean re-audit is `FIXES CONFIRMED` with no finding left, or a clean full
   re-run. Wherever another guardrail, command, agent file or skill says a FAIL is "re-audited" or that the audit is
   "re-run clean", the re-run is the one this section sets; none of them is weakened beyond that.

## Whole-Chapter Gate 1 (Amended 2026-10-07)

This section governs `/create-chapter` (Command C-42) and `/revise-chapter` (Command C-43) for a Chapter whose
Build mode is `whole`. Everything in the sections above stands for the Area pipeline; this section says what
changes when the audited unit is the whole Chapter text. The two-gate shape is the same, run once for the Chapter.

1. **Order.** Step 0 Decision Consultation and the confirmed build plan; the draft (one `area-maker` in Chapter
   mode); the edit (one `chapter-editor`, on the staged file in `.claude/temp/` only); the measure (script
   `measure`); Gate 1 by the `continuity-checker`; the staged text printed in full with its figures and audit;
   the author's `[CONFIRM WRITE]` / `[REVISE CHAPTER]` / `[SKIP WRITE]`; Gate 2.
2. **The 23 checks run over the whole Chapter.** The count is 23 and every check keeps its definition above,
   read on the whole Chapter text with these adaptations:
   - **Check #10 is replaced by the word-band check.** The 1,280 to 2,400 range is not applied to a whole-built
     Chapter. Words are counted, not characters; date lines, hidden markers and scene-break marks are not counted.
     Each Area block is written at 55% to 60% of its size target in the Chapter Spec; only an Area block whose
     `Budget stretch:` names it in the spec may exceed 60%, and never above 72%; no Area block goes below 55%.
     The Chapter total must fall between 0.55 T and 0.72 T, where T is the sum of the size targets. A count outside
     a band, a stretch not named in the spec, a missing or duplicated `<!-- AREA NN -->` marker or markers out of
     order is a blocking finding, reported with its word count and the counting method; the write waits for the
     author to confirm the Chapter or send it back. Pacing stays a craft matter inside the band.
   - **Check #18, Spec Conformance, is read per Area block and against the Scene Map.** The plan-versus-written
     list is made for each Area block of the Chapter Spec (the same core items as above: the beat, the scene
     anchors in order, the Continuation, the viewpoint and Dual-POV mark, every planned time skip, the Behavioral
     Plan, the Opening and Closing types, the Thread, every settled item) and for each Scene of the Chapter Spec's
     `5.0 Scene Map` (the Area blocks it spans, its POV sequence, its arc, its scene pacing, its word budget, its
     visible-break rule and the join state at each Area seam). The core-item rules above apply to each; a
     difference on a core item blocks unless it traces to an on-record author answer from this invocation. 18(a),
     the chain is in force, applies unchanged. The Chapter Spec must carry pacing, size target and scene assignment
     at the Chapter, every Area block and the Scene Map; a Chapter Spec missing any of them FAILs 18(a) Major and the
     command stops.
   - **Check #11 element 11-2 and the calendar are read by date segment.** The Chapter prints one date line at
     its top; a scene whose date differs from the scene before it carries its own date line directly after its
     break. Each date segment is read as a date line was read per Area above: no backward date without a lawful
     cause, a scene continued from the segment before starts where it ended, weekday by the calendar's formula,
     every segment inside the Chapter's, Novel-Part's and Section's windows. A same-date scene repeats no date line.
   - **Check #12 date-line form** is read on every date line of the Chapter; the first is the first line of the
     Chapter text.
   - **Check #9 deep POV** is read per POV segment; a POV shift is lawful where the Scene Map plans it and carries
     the visible break of Part 2.
   - **Checks #19, #20, #22** are counted over the whole Chapter and read as before; Check #20's recurrence
     elements read the Behavioral Plan Signatures per Area block.
   - **Check #23 battle plausibility** (Part 44) is read once for each Area block that holds a fight, against that block's
     Engagement Ledger in the Chapter Spec; an Area block with no fight reads N/A.
3. **Flow review across the whole Chapter (16-J).** Done once, by the second read-only instance, over the whole
   Chapter text as one flow and with the previous Chapter's last passage (the read set of Part 2 Rule P2-Area-1
   with the Chapter as the unit). It covers: every seam between consecutive Area blocks, read as the carry-over
   reading of Read 1 (a scene that continues across a seam opens in motion from the exact state the join state of
   the Scene Map names, with no second opening and no recap, and with no visible break); every POV shift (it must
   be planned in the Scene Map, carry a visible break, and hand over the exact state); and the Read 2 patterns
   (repeated openings and closers across Area blocks, cadence, explanation clustering, worn figures, one register,
   fight shape against earlier fights, a search of the Section's written text for each quoted figure and repeated
   three-word phrase, new names) reported with their lines quoted and the Area block number (never an Area file).
   Continuity findings block exactly as above; sameness is reported, not failed.
4. **Two read-only instances, launched together** (parallel), as for the Area pipeline: one runs Checks 1 to 23 with
   16-J excepted, the other runs 16-J. Results merge into one named-result list. The 23-check instance re-reads
   `.claude/canon-manifest/*.json` fresh. This is the shape of the first audit and of a full re-run; a re-audit after local fixes follows the section "Re-audit after fixes" (Author ruling, 2026-10-18).
5. **Tier D, monster and Check #21 triggers.** A Tier D or monster flag (Tier C or D monster, genuine consequence
   arriving for a Tier D character) and every Check #21 enquiry that asks the author are asked with
   `AskUserQuestion`, with the Position Header Block (the Chapter chain and Chapter reference `P.S.N.CCC`) and the
   full staged Chapter text printed first and the question after them. Tier B, C and D evolution is decided by the
   Gate 1 checker with its reasons recorded, as above.
6. **FAIL loop.** On any FAIL the orchestrating command sends the findings to the `chapter-editor`, which edits
   the staged file in `.claude/temp/` in one pass; the script `measure` re-runs; the re-audit runs as the section "Re-audit after fixes" sets out (Author ruling, 2026-10-18): both Gate 1 instances re-run in
   full where that section calls for a full re-run, and otherwise only the fixes and the regression sweep run. The Correction Protocol and its four rules apply unchanged, with these differences: the loop revises the
   staged Chapter only; where the remedy would change what happens on the page rather than how a line is worded it
   is brought to the author; the author may stop the loop at any time (`[SKIP WRITE]`). A cause that lies in an
   earlier written Chapter is named by reference and the author is asked, with the staged text printed first,
   whether to revise that Chapter (`/revise-chapter` for a whole-built one, `/revise-area` for an Area-built one).
7. **Inter-Gate Confirmation.** The staged Chapter text is printed in full in chat, with its Position Header, the
   word figures per Area block and the Chapter total against the bands, and the Post-Draft Audit Report, before the
   prompt. `[CONFIRM WRITE]` writes; `[REVISE CHAPTER]` (the gate token, not the command) rejects the listed
   differences and returns to the editing loop with the author's note (Gate 1 then runs as a first full audit of the revised text; Author ruling, 2026-10-18); `[SKIP WRITE]` discards everything and
   nothing is written or updated. A plan-versus-written list with a BLOCKS line gets no confirmation prompt.
8. **Gate 2.** The script `.claude/tools/chapter_builder.py --mode whole` writes the `.md` (with the hidden
   markers) and the `.docx` (without) into the Novel-Part folder, and refuses an out-of-band count, a missing or
   duplicated marker, a Chapter that has Area files, and an existing file without `--overwrite`. Then three lanes
   run in parallel: the post-write audit (file path under `projects/novel-starward-saga/`, the date line, the
   markers in the `.md`, none in the `.docx`), the ledger update (one batched update for the Chapter, citing the
   Chapter reference only, see `guardrail-ledger-update-law.md`) and the Chapter-level CDL-2 score (one block per
   Chapter plus the Section aggregate row). The same continuity-checker instance does the Chapter Spec as-built
   sync and completion in one pass: every Area row `WRITTEN(P.S.N.CCC)`, the Signatures-fired rows flipped per Area
   block, variances and settlements, the Completion Record, the Chapter Spec `COMPLETED` and the registry row.
   The command writes the session-log line.
9. **Revision (`/revise-chapter`).** One change request for a whole-built Chapter: the `chapter-editor` edits the
   written Chapter text in a staged copy, Gate 1 re-runs in full on it (as a first full audit of the revised text; any FAIL it returns follows the loop above, Author ruling, 2026-10-18), the author confirms, the old pair is
   archived by a plain file move into `projects/novel-starward-saga/_archive/<YYYY-MM-DD_HHMM>/` and the pair is
   replaced through the script with `--overwrite`; the affected Gate 2 lanes re-run.

## Escalation

A conflict discovered mid-audit is never resolved silently — surface it and, where the
canon itself calls for it (e.g. a new antagonistic character crossing into villain
territory), stop and ask via `AskUserQuestion`, through the orchestrating command, before proceeding.
