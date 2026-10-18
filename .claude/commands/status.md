---
description: Report the current position in the Starward Saga (Phase/Section/Novel-Part/Chapter/Area), the story clock (the date of the last written Area), the spec chain's statuses (Section Spec, Novel-Part Spec, Chapter Spec) with the current Novel-Part's Chapter-list progress, open ledger obligations, and Section density trend.
user-invocable: true
---

# `/status`

Corresponds to canon command `[STATUS]` (C-13). Read-only — makes no changes.

## The active spec in each tier

The specs form a chain of three tiers, the Section Specs, the Novel-Part Specs and the Chapter Specs
(Part 38 Rule 38.9). In each tier the **active** spec is the first one, in story order, whose status
is not `COMPLETED`; a `RETIRED` spec is skipped (Part 38 Rule 9.7.4). Story order is the order of the
Ref numbers, compared number by number (`1.2` comes before `1.10`). So a spec that was built ahead,
or a successor saved as `DRAFT` by a late `[SKIP SPEC]`, is not "current" while an earlier spec in
its tier is still not `COMPLETED`. The status used here is the status of the spec itself (`DRAFT`,
`CONFIRMED`, `AMENDED-PENDING-RECONFIRM`, `COMPLETED`, `RETIRED`). It is not the status of an Area row
(`PLANNED`, `DRAFTED`, `WRITTEN` or `DROPPED`), which is reported separately below.

## Whole-built Chapters

A Chapter built whole by `/create-chapter` (its Chapter Spec's `Build mode` is `whole`; Area rows read
`WRITTEN(P.S.N.CCC)`) has no Area files. For it, report Chapter-level status only: the Chapter file pair
(`Chapter NNN - <Name>.md` and `.docx` in the Novel-Part folder, present or not), the Chapter Spec's status
and coverage, the Chapter's word count against its band (0.55 T to 0.72 T, read from the Chapter Spec and the
`.md`, markers and date lines left out), the open-item count, and the Chapter's single CDL-2 block; list no
Area rows. A Chapter Spec `CONFIRMED` with Build mode `whole` and no Chapter file is "unbuilt, next command
`/create-chapter`" (the Scene Map, pacing and size target fields must be present; if one is missing, name
`/chapter-spec` revise). A whole-built Chapter's incomplete Gate 2 is reported as `incomplete Gate 2 at
P.S.N.CCC` (Chapter file on disk but the spec rows are not `WRITTEN(P.S.N.CCC)`, or no Section 10 row or
calendar row cites the Chapter reference). The Area-position rules below apply to Chapters built by Area.

## Sequence

1. Read `projects/novel-starward-saga/` to see what is written on disk (never report a
   remembered position; the `_archive` folder is never read, listed or counted, Part 2 Rule 5.3.2a).
   The position is the
   next Area, found by the rule `/next-area` uses: the first Area row, in Chapter order, of the
   active Chapter Spec whose status is `PLANNED` or `DRAFTED` (a `DROPPED` row is skipped). If Area files sit after that row on
   disk, report "redraft in progress". A Chapter Spec becomes `COMPLETED` as soon as its last Area
   row is written (Part 38 Rule 3.6.1), so when the last written Area ends its Chapter and no later
   Chapter Spec exists, no Chapter Spec is active: report the position as the end of that Chapter,
   take the Chapter Spec of the last written Area as the Chapter reported on in the steps below, and
   name `/next-chapter` as the next command (it sends the author to `/next-part` or
   `/part-spec revise` when the Novel-Part Spec has no further Chapter entry).
2. Read `.claude/story-memory/ledger-*/_index.md` files for any entity with a pending/stale
   Post-Write Ledger Update obligation, and each character index's "Pending author
   confirmations" table (Part 39 Area 44.2). From `ledger-worlds-calendar/_index.md` read the Current
   Position block only (Part 41 Area 9, The calendar ledger).
3. Read the story-spec registry,
   `.claude/story-memory/phase-section-part-chapter-area-specs/_index.md`, by kind: the Section
   Specs table, the Novel-Part Specs table and the Chapter Specs table, each from its own table (a
   row is never taken from another kind's table). Name the active spec of each tier by the rule
   above. Then read, in one parallel batch and read-only (Part 38), the active Chapter Spec (its
   status, coverage, Area rows and the open items in its Audit and Settlement Notes), the active
   Novel-Part Spec (its Chapter entries and its Audit and Settlement Notes) and the active Section Spec
   (its Novel-Part entries and its Audit and Settlement Notes). Compare the Areas written on disk (Step
   1) with the Chapter Spec rows and the ledgers, and list each written Area whose spec row is not
   `WRITTEN`, or whose ledger rows are missing (no Section 10 row in any ledger entity file
   cites its Reference Code, or no row of the calendar ledger covers its Area), as `incomplete Gate 2 at <ref>` (Part 38 Rule 6.2.1): a pending
   action until reconciled. `/force-ledger-audit` repairs it; run on its own, it performs the
   Rule 3.6.1 spec sync for that Area behind its preview. Only Chapter Specs are compared this way:
   the Gate 2 sync writes the Chapter Spec and its registry row and nothing above them, so a Section
   or Novel-Part row whose stored coverage trails the live count (Step 5) is not an incomplete Gate 2.
4. Read the current Section's tracker file,
   `.claude/story-memory/cdl2-density-tracking/phase-N/section-M-aggregate.md` (it exists once the
   Section's first Area is scored; before that, say so), and quote its running aggregate and its
   Anchor Floor table as stored, showing each category's reading against its range,
   the 4 Anchor Floor categories included. Nothing is recomputed and **area-scorer** is not
   launched; it runs only when the author asks for a rescore. Reported numbers are guide posts
   for the author's information, so name any line currently crossed explicitly with its value and margin
   rather than summarizing it as a status letter
   (`guardrails/quality/guardrail-threshold-consultation.md`).
5. Report: position, **the story clock** (from the Current Position block read in Step 2,
   quoted as stored: the date of the last written Area in the form of the date line, weekday included,
   its Phase Day, and the Open Chapter and the Open Chapter's recorded window (First to Latest); before any Area is written, "story not started: Day One is
   Year 1247, Ilovany, Orvil, Day 1, Phase Day 1" (Phase Day 1 is the third weekday); Part 41 Areas 3, 4 and 9), open ledger obligations, the pending author confirmations (character,
   item, file and section, what it blocks), each `incomplete Gate 2 at <ref>` found in Step 3,
   and these, in this order:
   - **The chain.** Each link of the chain for the position, with its Ref and its status: the
     Section Spec, then the Novel-Part Spec, then the Chapter Spec. The links are found top-down;
     a Novel-Part Spec and a Chapter Spec are found under their parent by Ref (`P.S.P.CCC` sits
     under `P.S.P`, which sits under `P.S`). Where a tier has no active spec (none exists yet, or
     every one is `COMPLETED`), say so: the next spec of that tier is the one still to be made.
   - **The chain flag.** The first link that is missing, or whose status is not `CONFIRMED` or
     `COMPLETED` (that is, `DRAFT`, `AMENDED-PENDING-RECONFIRM` or `RETIRED`), is named as the first
     missing link, in the form "no confirmed Section Spec for 1.2", "no confirmed Novel-Part Spec for
     1.2.3" or "no confirmed Chapter Spec for 1.2.3.004", with its status when it has one. A
     Novel-Part Spec cannot be built or revised unless its Section Spec is in force, and a Chapter
     Spec cannot be built or revised unless its Novel-Part Spec and its Section Spec both are
     (Part 38 Rule 9.1.1). So the flag also names the command that repairs the first missing link:
     `/section-spec`, `/part-spec` or `/chapter-spec` (usually reached through `/start-story`,
     `/next-section`, `/next-part` or `/next-chapter`). Only the first missing link is named. When
     every link is in force, say "chain in force". When the missing link is a Section Spec for a
     Phase 2 Section, add this note: there is no Phase Spec, Part 30 is the Phase-level plan, and
     `/section-spec` refuses a Section that Part 30 has no entry for, so Part 30 has to be expanded
     for Phase 2 before its spec chain can be made (Part 38 Rule 9.1.4).
   - **Chapter-list progress.** For the active Novel-Part Spec, its Chapter entries in order, each
     with its working title and a status worked out from the Chapter Specs table of the registry,
     never read from the Novel-Part Spec (it is not stored there): `no Chapter Spec`, or the status of
     that Chapter Spec's row as it stands. Beside the list, the live count of entries whose Chapter
     Spec is `COMPLETED` out of the entries in the list, and for the active Section Spec the same live
     count of its Novel-Part entries whose Novel-Part Spec is `COMPLETED`. A Chapter Spec in the
     registry under the active Novel-Part with no entry in the list is named. These figures are
     information only: the lists are guides, no target or range is stored, and the length of a list
     is read as information (Part 2 Rules 9.3.1 and 9.13.1).
   - **Stored coverage.** The Coverage cell of each active spec's registry row, quoted as stored and
     always with that row's Last Updated date. The Section and Novel-Part cells are refreshed when that
     spec is confirmed, at any completion write step (a child's included) and at a reset or rewind
     rollback, and never at Gate 2 (Part 38 Rules 1.2.2, 10.1.2 and 11.1.2), so a stored figure can
     be older than the live count above (for example after a Chapter's last Area is written and
     before `/next-chapter` completes it); the live count is the one to read for where the story is now.
   - **The Chapter.** The Chapter Spec's status and coverage (planned vs. written Areas, open-item
     count in its Audit and Settlement Notes) as before, or the flag from the chain step when it is missing or not in
     force.
   - **The Area.** The current Area row's status (`PLANNED`, `DRAFTED`, `WRITTEN` or `DROPPED`), with its pacing
     and size target as the Chapter Spec records them, and the count of Area rows written out of those
     planned in the Chapter (`DROPPED` rows left out); the next command is `/next-area`, or `/next-chapter` when the last Area of the
     Chapter is written.
   - **The Section and the Chapter's record.** The POV count per hero for the current Section (the layout of
     the Section-close POV report, Part 38 Rule 3.7.2; the Section-close figure once the
     Section is closed, that is, once Gate 2 has confirmed its closing Area and the calendar Section row reads `CLOSED`, not when `/section-spec complete` runs; informational, no target, no warning), density trend, and any
     outstanding variance entries in the current Chapter's spec Audit and Settlement Notes (Part 38
     Rule 3.6.1 item 2; variances are recorded there, not in the session log).
   - **Variance notes on the upper specs.** The variance notes appended to the active Novel-Part Spec
     and to the active Section Spec by the flows below them. A departure at any level is noted on
     every spec above it, so a Chapter's departure from what its entry fixed stands on the Novel-Part
     Spec and on the Section Spec, and a Novel-Part's departure stands on the Section Spec; a change
     of the Chapter list is noted the same way (Part 38 Rules 9.4.5 and 11.4.3); a change of the
     Novel-Part list is made by `/section-spec revise` (Rule 9.4.2). Each note is shown as stored:
     its date, the spec it came from, what it records and the
     author's answer (original left as the plan baseline, or plan amended). They are information,
     they are not re-judged here, and they create no check or question.
