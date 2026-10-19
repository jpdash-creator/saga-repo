---
description: Build, revise, show, or complete a Section Spec (Part 38 Story Specification Law) -- the author-confirmed plan that turns what Part 30 expects of one Section into its Novel-Parts and, at a high level, their Chapters; the first spec in the chain, made before any Novel-Part Spec or Chapter Spec in that Section.
argument-hint: "[build|revise|show|complete] [Section reference, e.g. 1.2]"
user-invocable: true
---

# `/section-spec`

Corresponds to canon command `[SECTION SPEC]` (C-40 — Part 38 Story
Specification Law Area 10). One spec
file per Section at
`.claude/story-memory/phase-section-part-chapter-area-specs/phase-N/section-N/section-N-spec.md`,
reference `P.S` (Phase, Section; for example `1.2`), registered in the Section Specs table of
that folder's `_index.md`. Governing guardrail:
`.claude/guardrails/ledger/guardrail-story-spec-law.md`; primary skill:
`spec-story-specification-law` (Areas 9 and 10, master Rules 38.9 to 38.14); the source it
plans from: `narration-novel-macro-story-law` (Part 30), which this command reads **whole**
every time it builds or revises.

**Where it sits.** The Section Spec is the top of the **spec chain** (Part 38 Rule 38.9):
Section Spec (this command, C-40, reference `P.S`) → Novel-Part Spec (`/part-spec`, C-41,
reference `P.S.P`) → Chapter Spec (`/chapter-spec`, C-39, reference `P.S.P.CCC`). "Novel-Part
Spec" is the formal name of the middle one; in `/part-spec` "Part" means a Novel-Part, never a
canon-law Part such as Part 30. A Novel-Part Spec cannot be built or revised unless its Section
Spec is `CONFIRMED` or `COMPLETED`, and a Chapter Spec needs both (Rule 9.1.1). The Section Spec
has no spec above it: Part 30 is its source. There is no Phase Spec: Part 30 is the Phase-level
plan (Rule 9.1.4).

**Modes** (first argument; `build` is the default when omitted; the second argument is the
Section reference, and when it is left out the command takes the Section the story is in, from
the last written Area and the registry, or Section 1 of Phase 1 at the start of the story, and
says which one it took before it asks anything):

- **`build`** — create the Section Spec for a Section that has none. A reference that names a
  later Section than the one the story is in is an **ahead-build** (Part 38 Rules 9.2.2 and 9.2.3,
  below). For a Section that already has written Chapters this is a **retro-fit** (Rule 9.8.2):
  statuses are taken from the record, every Novel-Part and Chapter already written is entered as
  it was written, anything the record does not show is asked of the author (who may defer it),
  and the Audit and Settlement Notes say "as-built reconstructed". If a Section Spec already exists for the
  reference, do not build over it: run `revise`.
- **`revise`** — change an existing Section Spec. A change to a Novel-Part's purpose, to its
  closing state or hand-off, to its calendar window or to the reveals it owes, to the Section's
  own hand-off or calendar window, or to the set or
  the order of the Novel-Parts (adding, removing or reordering one)
  is **substantial** (Part 38 Rules 9.4.2 and 10.6.2): it re-runs the audit and the final sweep and needs
  a fresh `[CONFIRM SPEC]`. Adding, splitting, merging or dropping a Chapter in a Novel-Part's
  guide list, moving or dropping a suggested thread, setup or payoff, setting or clearing the Section's own Epigraph or a thread-return note, a typo, a variance note, an audit
  note and status housekeeping are **light**: they are written once the author signs off (Rule
  9.4.2). When Novel-Part Specs or Chapter Specs already exist under the spec, `revise` runs the
  cascade report (below).
- **`show`** — read-only render of the spec and its registry row. No consultation, no audit,
  no writes.
- **`complete`** — mark the Section Spec `COMPLETED` once its Section has finished (see below).
  Normally reached through `/next-section`; invokable alone.

There is no short or quick form of this command: every build is
the full consultation.

## What a Section Spec is (authority)

A Section Spec is the author-confirmed, high-level plan of one Section. It says what Part 30
expects of the Section, how the Section will meet that as an ordered set of Novel-Parts, and, for
each Novel-Part, a short list of its Chapters (Part 38 Rules 10.1.1 and 10.2.1). It holds thirteen
blocks, numbered 0 to 12:

0. **Header block** — the name chain through the Section (the Phase and Section names are Locked
   under Part 30 and tagged `locked`); the **Epigraph** for the Section's title page (text and
   source; it reads `unset` until the author gives one and is never written by an agent).
   Every Section Spec carries its own Epigraph line, the first Section of a Phase (Section 1)
   included; the author alone settles each line. The Phase epigraph is a line of Part 30 (it
   reads `unset` until the author gives the text), and a Phase's first Area prints it first and
   Section 1's own Epigraph second, where the first Area of every other Section prints only that
   Section's own Epigraph (Rule 10.3.1); the **Section calendar window** (the anchor length, which
   cites Part 30 §1.3.2a and never copies it, or a chosen length inside the plus or minus two
   months that §1.3.2a allows), written as dates plus Phase Day
   (Part 41 Area 4, Phase Day conversion and Section windows, cited and never copied); and the **carry-in**
   from the previous Section (threads in, a reference to that Section's Reader-now-knows line and the last
   dated moment of the story so far, read from the calendar ledger's Current Position block, Part 41 Area 9).
1. **What Part 30 expects** — citations only, by function name and section heading, with each
   item marked Locked or Negotiable (Rules 10.3.2 and 10.4.2).
2. **Section arc as planned** — how this Section meets the Part 30 arc, and the order of the
   escalations inside it.
3. **Novel-Part plan** — one entry per Novel-Part: a working label, its purpose (by function
   name), its thematic movement, its place or places, its calendar window (inside the Section
   window, as dates plus Phase Day), which Part 30 functions it carries, who carries it (all eight protagonists accounted
   for, no counts), its opening state, its closing state and hand-off, and a high-level list of
   its Chapters (a working title and one line each; a guide, which the Novel-Part Spec may add
   to, split, merge or drop); its **pacing** and **word budget** (Fast, Medium or Slow, and a
   word figure, each a guide and either may read `unset`; Part 38 Rule 10.3.9, Amended 2026-10-07);
   and, after the entries, the **Scene Map across Novel-Parts** (a table of the scenes that run
   across a Novel-Part seam, scene IDs `SS1`, `SS2`, ...; an empty table says none).
4. **Threads, setups and payoffs** — a linked guide, keyed to a Part 30 Setups-table row or a
   short thread name: which Novel-Part plants and which pays. Optional per-thread note on how
   long a thread may stay off the page, default `unset`.
5. **Protagonist arc map** across the Section — all eight.
6. **Progression plan** — cultivation, technology and named-move beats against the Part 30
   §1.3.2 map.
7. **Opposition and pressure** — villain and faction pressure, and reveal timing.
8. **Knowledge, reveals and consequence carry-over.**
9. **Section close hand-off** — what the next Section inherits (for Section 8, the Phase
   Transition items).
10. **Standing exclusions** — by reference to the Chapter Spec template, section 3.
11. **Completion record** — the final variance summary, Reader now knows, Section digest and the
    threads carried to the next Section, written at completion.
12. **Audit and Settlement Notes** — the last section of the file, a plain list of the nine kinds
    of Part 38 Rule 9.10.2 (Settled, Skipped, Open, Deferred, From, Inherited, Name, Variance, Audit),
    each pointing back to the plan item it concerns (by block and field or heading). Nothing of the kind is written
    anywhere else in the file.

The header lines are: Governing Law, Spec Status, Spec Version | Confirmed, Last Updated, Light
Continuity Audit and the **built-against stamp** (the last completed Chapter and Section
reference and the ledger state the spec was built against).

**Clean body, notes at the end** (Part 38, the Audit and Settlement Notes rule). The body of the
spec (blocks 0 to 11) reads as plain plan text from start to finish. It carries no inline
`[SETTLED ...]`, `[OPEN ...]`, `[SKIPPED ...]` or `[ASKED ...]` tag and no provenance, ruling,
date-of-answer or audit mark, and no word such as settled, held, directive or as drafted. Where a plan item is settled, skipped or deferred, the plan text
states the plan itself (for example "its kingdom is not set") and block 12 holds the note, a plain list line
that begins with the plan item (block and field or heading) and then names the kind and the answer with its date:
Settled (the answer), Skipped (what the planner chose), or Deferred (to the Novel-Part Spec, the Chapter Spec or the Area writing). The notes are a list, never a table
(Part 38 Rule 9.10.2). A tag found in the body is a schema finding.

What the spec holds and does not hold:

- **Status.** The spec status is one of `DRAFT`, `CONFIRMED`, `AMENDED-PENDING-RECONFIRM`,
  `COMPLETED`, `RETIRED`.
- **Part 30 by citation only.** The file names Part 30's functions, rows and sections; it never
  copies their text (Rules 2.3.2 and 10.3.2). Part 30 stays the only source of Locked Canon.
- **Guides, not blocks.** The Novel-Part plan and the Chapter lists are the plan; no number or
  range of Novel-Parts or Chapters is stored, and the length of a list is read as information
  only (Part 2 Area 9). Setups, payoffs and threads
  here are a guide and a suggestion, linked by shared keys to the Novel-Part Spec and the Chapter
  Spec below. The story may plant elsewhere, pay earlier or later, or drop one, and an unmet
  suggestion creates no check, gate or question (Rule 9.5.4).
- **Names are working labels.** Novel-Part labels and Chapter titles here are plan labels. No
  Establishment tag (`proposed` or `locked-at-Gate-1`) is stored in a Section Spec;
  establishment is recorded in the Chapter Spec header and in the delivered files (Part 38 Rules 10.3.3
  and 10.3.8).
- **Never here:** tone, voice, pacing, sensory tags or content tags (pacing is decided for each
  Area in the Chapter Spec; Part 36 Autonomous Matters are never fixed above Area); any number
  or range of Novel-Parts or Chapters; Area names, Area sizes or anything inside a scene.
- **Authority.** The spec is intent. It never establishes a canon fact (Rule 1.3.2) and never
  restates ledger content (Rule 1.4.2); spec-to-spec derivation is allowed and always tagged
  (Rule 9.3.4). Order of authority: Locked Canon > ledger > Section Spec > Novel-Part Spec >
  Chapter Spec for what a level must do, and the lower spec governs its own detail (Part 38 Rule 9.4.1);
  a conflict found in a lower build is a question for the author, never a silent pick. Session-log
  is never an input.
- **Settling power downward.** A confirmed Section Spec's Settled notes (block 12) are
  not asked again when a Novel-Part Spec or a Chapter Spec is built under it; they are carried
  into the lower spec's own Audit and Settlement Notes as Inherited notes naming the Section Spec, the answer and the date, pointing to the Chapter Spec item they bear on (Part 38 Rule 9.5.1), so the
  Area-time gate reads only the Chapter Spec. The carve-outs stand (Rule 9.5.3): pacing is never
  settled above Area; tone, voice, sensory and content tags stay with the Area;
  Part 36 Autonomous Matters are never fixed above Area; a genuinely new branch or a
  reduced-clarity item is asked again at any level with the old answer shown (Rule 4.2.4); and a
  settled item in an upper spec never makes a name or fact canon.
- **Who reads it.** Builders of a Novel-Part Spec and of a Chapter Spec read this spec in full.
  Area-time agents (the area-maker, the scorer, both Gate 1 checkers and the outline-planner
  when it plans a single Area) do not read it (Part 38 Rule 9.9.2): the Chapter Spec carries every
  inherited item with its source note. The Epigraph is read from this spec's header block by the
  command that opens the Section's first Area (`/next-section`, `/next-area`), and by a redraft
  of that Area; for a Phase's first Area (opened by `/start-story` for Phase 1) the command
  passes the Part 30 Phase epigraph line as well, as the first of two lines, with this spec's
  Epigraph (Section 1's own) as the second. The writers take the two lines as
  `--phase-epigraph-file` and `--section-epigraph-file`, and `unset` means none for either.

## Preconditions

- Read `.claude/guardrails/ledger/guardrail-story-spec-law.md` and
  `.claude/guardrails/commands/guardrail-plan-then-auto-execution.md` — this command is one of
  the Plan Mode → Auto Mode in-scope commands (the consultation rounds are its Plan Mode;
  default model/effort, mandatory parallelism and milestone progress reports apply end to end).
- **Read the whole of `.claude/skills/narration-novel-macro-story-law/SKILL.md` — every time**
  (every `build`, `revise` and `complete`), in full and from the file, not from memory, not from
  an earlier read in the session and not from a summary (consolidated-first, per
  `guardrails/authority/guardrail-consolidated-skill-reading.md`; Part 38 Rule 10.4.2). The
  outline-planner and the continuity-checker read it whole as well. `show` needs only the spec.
- `spec-story-specification-law` is the primary skill read, Areas 9 and 10 in particular.
  Grounding also reads Part 2 (the Section and Novel-Part tiers, `narration-novel-book-structure-law`),
  Part 28 (naming, consultation and MAJOR entities, `narration-novel-creative-flexibility-law`),
  Part 36 (previews and setups, `narration-novel-thematic-law`) and the ledgers.
- **Part 30 must have an entry for this Section.** If it has none, the command refuses and says
  Part 30 must be expanded first (Rule 9.1.4). Phase 1 has exactly eight Sections, locked by
  Part 30. Phase 2 has no Section entries yet, so its spec chain waits until Part 30 is expanded
  for Phase 2; no Phase Spec is created.
- **No parent spec is needed.** The Section Spec is built from Part 30, the ledgers and the
  previous Section's record. A Section that already has a Section Spec is not rebuilt blind:
  `revise` it. A `RETIRED` Section Spec is brought back only if the author says so, and that goes
  through `revise`.
- Spec files are story-memory files written with ordinary Write/Edit — the authorized-scripts
  law (`guardrails/tools/guardrail-authorized-scripts-only.md`) covers only novel output files
  and does not apply to them. No script is created in the repository for this work.
- **Named items, naming and cost.** Named items are written in italic, naming is never presented
  as a cost, and an item met in the consultation enters no register row: follow Part 38 Rule 9.9.4 and Part 28 Rules 20.8.2, 20.8.7 and 20.9. Where an option could
  name or leave unnamed, the named version is the `(Recommended)` one.
- **Monsters (Part 40).** A monster name met in the consultation is
  set in roman and enters no ledger entry before its first Area (Part 38 Rule 1.3.2). The Phase 1 monsters Part 30
  plans (out of the forest beside the border village; on the airship voyage) are wild pressure and not an
  opposing force, and their Kind is defined and named at the Chapter Spec that plans them. **Standing
  exclusion: no sentient monster, and no allusion to one, in any Phase 1 Section Spec item (Law P30-L9), save the one narrow artifact-made exception of Canon Amendment 2026-10-19 (Law P30-L9).**

## Plan Mode → Auto Mode

For `build` and `revise`, Steps 0 and 1 are this command's **Plan Mode**: grounding, then as many
`AskUserQuestion` rounds as it takes, then the final sweep and the author's explicit "nothing
further to steer" answer (Part 38 Rules 9.6.1 and 9.6.5). Steps 2 and 3 run in **Auto Mode** with no
further discretionary questions. Auto Mode never waives a mandatory stop: the "nothing further to
steer" answer of Step 1 and the Step 3 `[CONFIRM SPEC]` token are hard pauses, exactly as Gate 1's
`[CONFIRM WRITE]` is in `/next-area`. A finding that only the author can rule on is asked as a
question, never settled by the planner (Rule 9.4.1); it is the one legitimate stop inside Auto
Mode, and it sends the command back to Step 0. `show` is read-only and has no Plan Mode
boundary; `complete` asks its questions first and one confirmation before it writes `COMPLETED`.

## Parallel orchestration

Per `guardrails/commands/guardrail-plan-then-auto-execution.md` (absolute binding, not a
convenience to weigh) and Part 38 Rule 9.9.3:

- **Step 0 ∥ planner grounding:** launch **outline-planner** as a background agent at the same
  moment the first consultation round is presented, instructing it to ground on the guardrails
  (including `ledger/guardrail-story-spec-law.md`), `spec-story-specification-law`, **the whole
  Part 30 SKILL.md**, the Part 2 / Part 28 / Part 36 consolidated skills, all relevant
  `.claude/story-memory/ledger-*/` entries, the previous Section's Spec (its hand-off block and,
  if it is complete, its completion record; when `/next-section` is building this spec, the
  closing Section's completion pieces are only drafted at that moment and are written at the last
  confirm of the chain, Rule 9.4.4, so they are read as drafted), the Section's existing Areas
  and specs (retro-fit and revise cases) and the CDL-2 Section running aggregate — and to report
  the open branch points it finds, *not* to finalize the spec. Author answers are fed back by `SendMessage`; any
  new branch the planner surfaces feeds further rounds.
- **∥ one continuity-checker pre-read** at the same moment, serving the audit and the sweep:
  Locked Canon, Entity Naming Law, the whole Part 30, the previous Section's Spec and the ledger
  state. The drafted spec is sent to it by `SendMessage` when it lands.
- **Inside a boundary command** (`/start-story`, `/next-section`): at command start launch
  together the planner grounding for every level the command will build (Section, Novel-Part,
  Chapter), the closing-unit reviews that already run concurrently (the area-scorer aggregate,
  the Section-close continuity review, the FCIA and ALCA chain in `/next-section`), and one
  continuity-checker pre-read that serves all the audits. Consultation and confirmation then run
  **strictly top-down**: this Section Spec first, then the Novel-Part Spec, then the Chapter
  Spec, with only one confirm prompt open at a time. When this spec is confirmed, the lower
  planners are told by `SendMessage` that their parent is confirmed and what it settled, and they
  finalise. In `/next-section` the Section-close ledger writes of its steps 2a and 2b land
  **before** this command's audit, because the audit's carry-in item reads the ledgers; and the
  two questions of its step 2c and this command's consultation are separate question streams,
  never mixed in one `AskUserQuestion` call.

Never parallelized: consultation answers precede the draft; the sweep precedes the "nothing
further" question; the audit precedes presentation; the author's `[CONFIRM SPEC]` or
`[SKIP SPEC]` precedes any spec-file write (the one-line Part 30 Phase epigraph edit of topic
12 rests on the author's own explicit yes and is not a spec file); a Novel-Part Spec is never
presented before its Section Spec is confirmed.

## Sequence (build / revise)

0. **Plan Mode — target, Part 30 read, grounding and consultation.** Settle which Section this is
   and say so. Check that Part 30 has an entry for it (refuse if not), that no Section Spec
   already exists (point to `revise` if one does), and, for an ahead-build, record the
   built-against stamp. Read the whole Part 30 SKILL.md. Launch the planner grounding and the
   checker pre-read (above) in parallel with the first `AskUserQuestion` round, and print the
   **Part 30 read-back** in chat before that round (next section). Consultation is exhaustive and
   goes on for as many rounds as it takes until no unasked branch is left at this spec's own
   level (Rule 9.6.1; see Consultation below). A new collective or location the plan introduces is not
   registered at this level: it is noted as owing a code under Part 39 Rule 39.23.1.5, to be asked and
   registered at the Chapter Spec build. In a **boundary build** (run by `/next-section` or
   `/start-story`), a stamp already on a Section Spec built ahead is compared with reality
   (the last completed Chapter and Section and the ledger state) and only the affected items are
   re-asked, each as a clarity-reduction question showing the original answer and the source of
   the change (Part 38 Rules 9.2.3 and 4.2.4).
1. **Final sweep, cascade report, then "nothing further to steer".** outline-planner assembles
   the whole draft, and the planner **and** the continuity-checker sweep it: conflicts with
   Part 30, the ledgers and the previous Section's record; any branch at Section grain still
   unasked; and a **re-listing of every SKIP and every deferral**, so the author has a last
   chance to settle each (Rule 9.6.5). For a `revise` with children, the checker also produces
   the cascade report and the author rules on each affected item (below). If the sweep returns
   anything new, go back to Step 0 for more rounds and then sweep again. When it returns nothing
   new, ask the author whether there is anything further to steer: one `AskUserQuestion` with the
   options "Nothing further to steer", "Change one of the skipped or deferred items" and "Steer
   something else" (the same three options, with no SKIP, in `/part-spec` and `/chapter-spec`). This question is not a branch question, so it carries no SKIP option. Only an
   explicit "nothing further to steer" ends Plan Mode; anything the author adds sends the command
   back to Step 0. There is no score, no percentage and no round count: the test is the sweep
   and the author's answer.
2. **outline-planner finalises the draft** from the settled answers: every block of the template
   (Part 38 Rule 10.2.1), the body as clean plan text and block 12 (Audit and Settlement Notes) holding
   the Settled, Skipped (planner chose X, with the date) and Deferred (by the author to
   ...) notes exactly as the author left them, each pointing to its plan item (Rule 2.3.6 and
   Rule 9.5.2); the Epigraph exactly as the author gave it, or `unset` (the same on Section 1,
   which carries its own line like every Section); the built-against stamp. The
   planner never leaves an item open on its own (Part 38 Rule 9.6.3); a plain Open note
   (a question raised and not yet answered) can appear only in a retro-fit, for a field the record cannot show,
   until the author has answered or deferred it. Then the **light continuity-checker audit** (report-only, writes nothing;
   scope in Rule 10.5.1):
   - Locked Canon: the Section-close cultivation band of §1.3.2 stays reachable and nobody is
     shown above their band before the Section closes; the Section window holds Part 30 §1.3.2a
     (the anchor, or a length inside the plus or minus two months with the nine-year total
     still met and the §1.3.2 bands still reachable; its dates and its Phase Day span agree by the
     conversion of Part 41 Area 4, a mismatch being a finding for the planner to correct); the Part 30 Law P30-L8 forbidden entities
     and Law P30-L9 (no sentient monster, and no allusion to one, save the one narrow artifact-made exception of Canon Amendment 2026-10-19 (Law P30-L9))
     and the author-removed Sapphire Line and other removed concepts are clean (a conflict
     **blocks**);
   - every Major Narrative Function Part 30 lists for this Section is carried by some Novel-Part
     or has been deferred by the author (a function neither carried nor deferred **blocks** until
     the author rules);
   - the Part 30 setups rows that touch this Section are shown assigned or unassigned
     (information only; an unmet suggestion creates no check, Rule 9.5.4), and every OPEN-AUTHOR
     row due in or planted by this Section has been raised and answered, skipped or deferred by
     the author (Rule 10.4.3; a row that was none of these **blocks**);
   - the ensemble is carried (P30-7): all eight protagonists accounted for, stated without
     counts (a protagonist with no line **blocks**);
   - Reader-Reveal Timing holds for the reveals planned in blocks 7 and 8 (a reveal planned later
     than the latest Novel-Part it is allowed in **blocks**);
   - the Novel-Part windows sit inside the Section window (a window outside it **blocks**), and
     the carry-in matches the previous Section's hand-off and the ledgers, using the stamp for a
     spec built ahead (a contradiction **blocks**);
   - Novel-Part labels pass Part 28 Rules 18.4.1 to 18.4.3 as **advice only**;
   - standing exclusions are clean, by reference (a hit **blocks**);
   - schema conformance: every block present, every field a value or an author deferral, the
     body free of inline tags (a tag in the body **blocks**), every note in block 12 well formed
     and pointing to a plan item, every Deferred note in block 12 an author deferral and every Open note a build-time question, and nothing the
     Section Spec never holds (Part 38 Rule 10.3.8) is in it (a blank required field **blocks**).
   On a blocking finding (Rule 10.5.1: every finding marked **blocks** above; the setups-row
   assignment and the Novel-Part label advice are information only and never block), revise
   through outline-planner and re-audit before presenting; if the finding needs an author answer,
   ask it (Step 0) and sweep again. Never present a spec with a blocking finding outstanding.
3. **Present the spec + audit summary** and wait for an explicit `[CONFIRM SPEC]` /
   `[REVISE SPEC]` / `[SKIP SPEC]` — never assume confirmation. The prompt names the artifact and
   its reference ("Section Spec 1.2"). The presentation shows the whole spec in block order (the
   Part 30 expectations as the citations that will be stored), each Novel-Part entry with its
   Chapter list, the audit summary, every SKIP and deferral, and, for a `revise`, the cascade
   report with the author's rulings. `[REVISE SPEC]` loops back through Steps 0 to 2
   (consultation scoped to what changed, then a new sweep and a new "nothing further" answer).
4. **On `[CONFIRM SPEC]`:** this command (the orchestrator, never outline-planner) writes the
   spec file with ordinary Write/Edit at once (Part 38 Rule 9.4.4) — status `CONFIRMED`, the version, the
   confirmation date, the audit result and the built-against stamp, with the notes of the build
   written into block 12 at the end of the file — and updates the Section
   Specs row of `phase-section-part-chapter-area-specs/_index.md` (Spec File / Ref / Status
   / Spec Ver / Last Updated / Coverage, which for this kind reads "Novel-Parts completed /
   planned; Chapters completed / planned", for example `0/3 Novel-Parts; 0/14 Chapters`, the
   "planned" figures being the lists as they stand, read as information only; the Coverage cell
   is refreshed at this spec's own confirm, at any completion write step, a child's included, and
   at a reset or rewind rollback, and never at Gate 2; Part 38 Rules 1.2.2 and 10.1.2). For a `revise`
   with children it also writes each ruling of the cascade report (below). **In a boundary
   chain** the completion writes for the outgoing specs (Chapter, then Novel-Part, then Section,
   bottom-up) are not made here: the boundary command makes them in one write step at the last
   confirm of the chain, the new Chapter Spec's (Rule 9.4.4).
   **On `[SKIP SPEC]`:** it writes the drafted spec the same way with Spec Status `DRAFT` (for a
   substantial `revise`, `AMENDED-PENDING-RECONFIRM`, Part 38 Rule 3.5.2), sets the registry row Status to
   match, and notes the skip in the spec's Audit and Settlement Notes (Rule 3.4.1). A DRAFT spec has no settling
   power. **A `[SKIP SPEC]` stops the chain at this level:** no Novel-Part Spec or Chapter Spec in
   this Section can be built or revised until `[CONFIRM SPEC]`, and each refusal names
   `/section-spec`. No outgoing spec is completed, and the boundary command that was running can
   be run again.
5. **Log the outcome to `.claude/story-memory/session-log/`** — this command writes the line:
   mode, "Section Spec" and its reference, the confirmation token, and the author deferrals
   (and any Open notes in the Audit and Settlement Notes) left in the spec.

## The Part 30 read-back (Step 0)

After reading the whole Part 30 SKILL.md, the command prints in chat, in plain words,
**what Part 30 expects of this Section**, so the author sees what is fixed before anything is
asked (Rule 10.4.2). It is shown in chat only: the file stores citations, never this text. Each
item is marked **Locked** (read, never asked) or **Negotiable** (the open space the questions
fill), using Part 30's own markers and the Locked and Negotiable split of Part 28 Area 2
(`guardrails/authority/guardrail-locked-vs-negotiable-canon.md`):

- where and when: the location anchor and the Section duration with the plus or minus two months
  of room (§1.3.2a) — Locked, the room inside it Negotiable;
- the thematic focus — Locked;
- the Section arc in a few lines — the ingredients Locked, their order and the events Negotiable;
- each Major Narrative Function, by name — Locked that it is met somewhere in the Section, where
  and how Negotiable; Part 30 floors such as "at least one" are shown as information, not gates;
- the arc line for each of the eight protagonists — Locked, the events Negotiable;
- the Section-close cultivation band for all eight (§1.3.2) — Locked, the path to it Negotiable;
- the technology and political-scale lines for this Section — Locked;
- the Locked events that fall in this Section (for example the awakening boundaries or the
  Apprentice's Choice, where Part 30 places them), with the staging inside them Negotiable;
- the standing exclusions of P30-L8 and P30-L9 (no sentient monster in Phase 1, save the one narrow artifact-made exception of Canon Amendment 2026-10-19 (Law P30-L9)) — Locked;
- the Part 30 Setups-table rows that touch this Section, each marked OPEN-AUTHOR (only the author
  sets it) or OPEN-AREA (Part 30 lets the first Area that needs it set it), with the open
  point named.

The read-back adds nothing to canon and invents nothing: where Part 30 is silent, it says so.

## Consultation (Step 0)

**How questions are put** (Part 38 Rule 38.13 and Rules 3.2.2, 3.2.3 and 9.6.4; Part 28 Rule 19.4;
Part 36 Area 13). Every question is asked through `AskUserQuestion` in plain everyday words (the
plain-language guardrail, `guardrails/quality/guardrail-plain-language.md`), with 2 to 3 concrete
options built from Part 30, the ledgers and the story so far, plus `SKIP — let AI decide`, four
options in all, up to four questions in one call. Options that point the story in a direction
each carry a one- or two-sentence preview in the Part 36 thematic voice (emotional register and
sensory texture, not plot events), with exposition risk flagged. An option never compares one
character with another. The author can always answer in their own words through "Other". An
answer is recorded as a Settled note (the answer and its date) in block 12, the Audit and
Settlement Notes, pointing to the plan item it concerns, while the body states the plan plainly.
A SKIP is recorded as a Skipped note (planner chose X, with the date) and settles nothing
(Part 38 Rule 4.1.2). A MAJOR entity's name,
aim or leader, a Hero or Villain address-register gap and lore the author owns are never settled
by a SKIP (Part 28 Area 20.4): they stay asked until the author answers or defers them.

**The planner never leaves an item open on its own** (Rule 9.6.3): every field of the template is
put to the author. Only the **author** may defer an item, by saying it can be handled in a lower
spec or in the writing (typed under "Other", or taken from a deferral option where the planner
offers one because the matter plainly belongs lower down; the planner never picks it). It is then
recorded as a Deferred note in block 12 (Deferred to: the Novel-Part Spec, the Chapter
Spec or the Area writing, with the date, pointing to its plan item), and a spec may be confirmed with
such deferrals. A deferral to the Novel-Part Spec is asked in that build; a deferral to a Chapter
Spec or to the Area writing is copied into the Audit and Settlement Notes of the Chapter Spec of the
Chapter it bears on as an Inherited Deferred note, so that Chapter's build, or the Area-time gate, asks the author, and the
drafter never settles it silently (Part 38 Rule 9.5.2).

**The grain test** (Rule 9.6.2). A question belongs in this build only if the author's answer is
the first thing that changes **this spec's own plan**: the set and order of Novel-Parts, a
Novel-Part's movement, purpose, window, carriers, hand-off, the Chapter lists as a guide, the
Section's calendar window, arc, progression plan, pressure, reveals and hand-off. Anything that
only changes the inside of a Novel-Part or a Chapter is that spec's question and is **not asked
here**. A Part 30 row marked OPEN-AREA is asked only if the answer changes this Section's plan
(for example which of the Section's threshold events comes first); otherwise Part 30 has already
left it to Area writing and the spec notes it as such. Anything Part 30 or the ledgers already settle is
not asked.

**Never asked in this build:** anything Locked (the read-back shows it); any number or range of
Novel-Parts or Chapters; tone, voice, sensory or content tags and every Part 36
Autonomous Matter (the pacing and word budget of each Novel-Part are asked, topic 14, and are
the only pacing this build asks); Area names, Area sizes (1,600, 1,800 or 2,000 words) and Area pacing, scene anchors, opening or
closing types and Behavioral Plans (the Chapter Spec's); the inside of a Chapter (the Novel-Part Spec's); and
Establishment tags.

**Topics, in order** (several rounds each, as the story needs; each topic is asked only where
Part 30 and the record leave a real branch):

1. **The shape and the Novel-Parts** (blocks 2 and 3): how the Section moves from start to finish,
   then the set and order of its Novel-Parts, each with a working label. Options are 2 to 3 whole
   shapes with previews. No question asks how many.
2. **The thematic movement of each Novel-Part**, in order: how its theme moves from where the
   Novel-Part opens to where it closes, and the place or places it stays in.
3. **Function carriage** (block 3, cited in block 1): which Novel-Part carries each Major Narrative
   Function by name, and which functions are a single event and which a run of scenes spread over
   several Novel-Parts. Every function must be carried by some Novel-Part.
4. **The high-level Chapter list of each Novel-Part**: a working title and one line each, offered
   as a candidate list from the movement and the functions it carries, which the author keeps,
   reshapes or replaces. It is a guide; the Novel-Part Spec decides the real Chapter set.
5. **Calendar windows** (blocks 0 and 3): the Section window (the anchor, offered first, or a
   chosen length inside the room §1.3.2a allows, with the effect on the other Sections shown),
   then each Novel-Part's window nested inside it. Each window is shown as dates plus Phase Day,
   converted by Part 41 Area 4; the planner states the
   conversion and the author never has to work out a date.
6. **Who carries what** (blocks 3 and 5): for each Novel-Part, who carries it and where each
   protagonist off the page stands, so all eight are accounted for, and each protagonist's arc
   across the Section where Part 30 leaves the landing open.
7. **The progression plan** (block 6): cultivation, technology and named-move beats against the
   §1.3.2 map. The Section-close band is Locked and is read, not asked; the path inside it, and
   which adult or which Level boundary where Part 30 leaves it Negotiable, is asked.
8. **Opposition and pressure** (block 7): how villain and faction pressure shows across the
   Section and when the reader first sees it (Reader-Reveal Timing).
9. **Knowledge, reveals and consequence carry-over** (block 8): what the reader learns and when,
   and which events must cast a shadow into later Sections (the Part 30 consequence principle).
10. **Threads, setups and payoffs** (block 4): for each Part 30 Setups-table row that touches the
    Section and each thread the Section carries, where it is planted and where it pays, by
    Novel-Part, as a guide only. **Every OPEN-AUTHOR row due in or planted by this Section is
    raised here**, one by one (Rule 10.4.3), and the author may answer "let the first Area that
    needs it decide", which is a deferral to the Area writing. One question asks whether the author wants any thread
    to carry a thread-return note; "no figure, leave it unset" is offered first.
11. **The Section close hand-off** (block 9): what the next Section inherits. For Section 8, the
    Phase Transition items, including what the event is where Part 30 leaves it to the author.
12. **The Epigraph** (block 0). For every Section, Section 1 of a Phase included: the text and
    its source for this Section's title page. No agent writes or suggests one. A SKIP here records
    a Skipped note in block 12 (planner chose unset, with the date). For Section 1 of a Phase the
    build asks that question as well as a second one: the
    Phase epigraph is a line of Part 30, so one plain question tells the author what that line
    reads now (`unset`, or the author's own text) and offers to give or change it now (the text
    is typed under "Other"; a SKIP records a Skipped note, planner chose leave it as it is).
    Section 1's own Epigraph, if the author gives it, prints below the Phase epigraph on the Phase's
    first title page; each line is the author's and each is asked once.
    Where the author types a text, the command repeats it back once and asks "Write this line
    into Part 30's Phase epigraph line?"; only on the author's yes does it make that one-line
    edit in Part 30, as an author-directed edit of the author's own words (the author may equally
    edit Part 30 by hand). That edit is not a spec-file write and does not wait for a confirm
    token. Nothing else in Part 30 is touched, and no agent ever writes or suggests epigraph text.
13. **Carry-in** (block 0): read from the previous Section's hand-off and the ledgers, shown, and
    asked only where they leave a branch. When the previous Section has no spec, carry-in is read
    from Part 30 and the ledgers and the stamp says so.
14. **Pacing, word budget and scenes across Novel-Parts** (block 3; Part 38 Rule 10.3.9,
    Amended 2026-10-07). Three questions for each Novel-Part, in the Novel-Part order, put in the
    same AskUserQuestion style as the topics above (2 to 3 concrete options built from the
    Novel-Part's movement, plus `SKIP — let AI decide`, each option with its thematic preview):
    (a) **Pacing**: Fast, Medium or Slow for the Novel-Part, with the planner's guidance stated
    in the question: fights are usually Fast, intrigue, deception, lore and thought are usually
    Slow, dialogue is usually Medium, and it is always the author's call because it depends on
    the story; the planner offers its recommendation and the reason from the Novel-Part's
    movement. (b) **Word budget**: a figure for the Novel-Part offered from the Chapter list as a
    guide, with a plain chance to **raise** it ("raise it" is always one of the options, the new
    figure typed under "Other"); `unset` is offered first where the author has no figure. (c)
    **Scenes that run across Novel-Parts**: whether any scene starts in one Novel-Part and
    carries on into the next (a fight, a conversation, a journey), and for each one that does,
    the Novel-Parts it covers, the viewpoints in order and where each takes over, the movement
    of the scene (its arc), its pacing, its word budget and the exact state at each Novel-Part
    seam (position, wounds, who knows what, whose floor it is). "No scene runs across a
    Novel-Part" is offered first and, when chosen, leaves the Scene Map table empty. Answers are
    Settled notes in block 12; a SKIP records the planner's choice and settles nothing, and
    `unset` is a lawful answer for (a) and (b). The author never has to work out a rule: the
    planner states the visible-break rule once with the question (a scene break shows only when
    the scene changes or the same scene moves to a different viewpoint; a scene that simply
    runs on with the same viewpoint shows none).

**Example round** (illustration only; every name is a placeholder and it establishes nothing,
Part 38 Rule 1.3.2):

```
Q1  "How should this Section move from start to finish?"
    A  Widening circles — "Each movement steps one ring further from the quiet centre, and
       the mood tightens from warm familiarity toward a held breath."
    B  One long approach, then the break — "A steady build in one place; the air thickens
       scene by scene, and the turn lands hard when it comes."
    SKIP — let AI decide
Q2  "Which Novel-Part should carry the function called Function A?"
    A  The first Novel-Part, as the opening movement — "Settled early, it lends everything
       after it a lived-in warmth."
    B  The second and third together, as a run of scenes — "It builds slowly, a little more
       felt each time it returns."
    SKIP — let AI decide
Q3  "Part 30 leaves Open Row A to you. What do you want to do with it?"
    A  I will set it now (type it under Other)
    B  Hold it for the Novel-Part Spec where it first shows
    C  Let the first Area that needs it decide
    SKIP — let AI decide (if the row names a MAJOR entity, a SKIP settles nothing and the row
           stays asked)
Q4  "Do you want an Epigraph on this Section's title page?" (every Section, Section 1 included)
    A  Yes, I will give the text and its source (type them under Other)
    B  Leave it unset for now
    SKIP — records "planner chose unset"; no agent writes an Epigraph
```

## Ahead-built Sections and the stamp (Part 38 Rules 9.2.2 and 9.2.3)

The Section Spec is normally built at the boundary: by `/start-story` for Section 1 and by
`/next-section` for each later Section (Rule 9.2.1). The author may also run `/section-spec build`
for a later Section ahead of time, since the only thing it needs is a Part 30 entry. An
ahead-built spec records its **built-against stamp**: the last completed Chapter and Section
reference and the ledger state it was built against. When the boundary command reaches that
Section it compares the stamp with reality and re-asks **only** the items the story has since
moved, each as a clarity-reduction question showing the original answer and the source of the
change (Part 38 Rule 4.2.4). If nothing the spec relies on has moved, it stands as it is. Answers that
change go through `revise` (re-audit, sweep and a new `[CONFIRM SPEC]` when the change is
substantial). The light audit's carry-in item reads the stamp.

## Cascade report (`revise` with children)

When a change to this spec is made after Novel-Part Specs or Chapter Specs exist under it, the
continuity-checker reports every Novel-Part Spec, Chapter entry and Chapter Spec the change no
longer fits, grouped by Novel-Part Spec. For each one the author picks: **keep it** (a variance
is noted on it), **amend it** (the author runs `/part-spec revise` or `/chapter-spec revise` on it
once this spec is confirmed, so it is revised against the confirmed parent), or **mark it
`AMENDED-PENDING-RECONFIRM`**. Nothing flips automatically (Part 38 Rule 9.4.2). The rulings are asked at
Step 1 and written, with the spec, at `[CONFIRM SPEC]`. Written Areas are never touched by a spec
amendment; a correction there goes through `/revise-area` or a redraft. A `COMPLETED` spec stays
a living record: `revise` works any time, and its completion pieces (variance summary,
Reader-now-knows line, digest) are refreshed when it is revised (Rule 10.6.2). A revision that
changes plan content for Areas already written leaves it to the author whether to redraft. After
the re-confirm the spec takes the status its record supports: `COMPLETED` if every Novel-Part
Spec under it is still `COMPLETED` and the author's completion yes still stands, otherwise `CONFIRMED`. Variance notes that lower flows have
appended to the Audit and Settlement Notes of this spec (a Novel-Part Spec's departure from this spec's entry or change of Chapter
list, and a Chapter Spec's departure, which is noted on its Novel-Part Spec and on this spec both,
written top-down, Part 38 Rule 9.4.5) are shown at every `revise` and `show`; they never change this
spec's plan, and folding one into the plan is a `revise`. **Retiring** a
Section Spec is always an explicit `revise` outcome (`RETIRED`), never silent (Rule 7.2.2), and is
refused while any Novel-Part Spec or Chapter Spec under it is not `RETIRED` until the author has
ruled on each of them (Rule 9.8.3). A Novel-Part that already has a spec or written Areas keeps its
number; a change of order that would move one is put to the author as a question.

### `show`

Read the spec file and its registry row and render them for the author: the blocks in order, each
Novel-Part entry with the status of its own spec (from the registry), the author deferrals and
SKIPs, the built-against stamp and the variance notes. Read-only; no consultation, no audit, no
writes. For the in-story dates and the open setups across the story, use `/timeline` and
`/threads`; for the chain's statuses, `/status`. If no Section Spec exists for the reference, say
so and name `/section-spec build`.

### `complete`

A Section Spec is `COMPLETED` when its Section has finished and all its Areas are written; it is
**not closed**, and stays a living record (Part 38 Rule 9.7.1). The boundary command `/next-section` asks
the author, as part of its checks, **"Has this Section finished?"**; a yes completes the spec, a no
stops the command (Rule 9.7.3). Run alone, `complete` does the same:

1. Verify every Novel-Part Spec of the Section is `COMPLETED` (the last one may be completing in
   this same write step, bottom-up) or `RETIRED` with an audit note. For any Novel-Part the
   plan lists that has no spec, ask whether it is dropped (a variance note) or not finished yet.
   A Novel-Part Spec that is neither stops the command and names `/part-spec complete`.
2. Report, as information that never blocks (Part 38 Rule 9.7.4): each Part 30 Major Narrative Function not
   yet met, listed beside the Novel-Part that planned it or with a note that none did; reveals
   owed and not delivered; threads and setups still open. Then surface, by `AskUserQuestion`,
   every unpaid setup, open thread and unresolved Open or Deferred note in the Audit and Settlement Notes: each is resolved, carried
   forward to the next Section's spec, or marked lapsed. **An item is marked lapsed only on the
   author's answer.**
3. Ask the author to confirm with `AskUserQuestion` ("Has this Section finished?", with "Yes, mark
   it completed" and "Not yet"). On "Not yet" nothing is written.
4. On a yes, write the completion content into the spec: the **final variance summary** (planned
   against as written, including Novel-Parts and Chapters added or dropped), the **Reader now
   knows** line (by reference to the last Novel-Part's line plus the Section-level additions,
   copying no list), the **Section digest** (the Section in a few lines, by reference to each
   Novel-Part's digest) and the threads and setups carried to the next Section; set the status to
   `COMPLETED`; update the registry row (Status and the Coverage cell, Part 38 Rules 1.2.2 and 10.1.2); log
   to session-log. `complete` only completes the spec: it never sets the calendar Section row to
   `CLOSED`, which happens when Gate 2 confirms the Section's closing Area (Part 41 Area 9, The
   calendar ledger). For Section 8 the hand-off is the Phase Transition;
   no Phase Spec exists to receive it.

When `/next-section` runs `complete` ahead of building the next Section's chain, `complete` does
everything above except the write: a yes means "complete it when the new Chapter Spec is
confirmed", and the write is made at that last `[CONFIRM SPEC]` of the chain, bottom-up with the
outgoing Chapter and Novel-Part Specs, in one write step (Part 38 Rule 9.4.4). A `[SKIP SPEC]` anywhere in
the chain writes no completion. `/next-section` does not advance on a "Not yet" (Rule 9.7.3).

**At the end of Phase 1** `/next-section` is not run for Section 8, and `/next-phase` does not
complete it (Rule 9.1.4). The author runs `/part-spec complete` for Section 8's last Novel-Part and
then `/section-spec complete` for Section 8; each writes at once, and the `/next-phase` note says so.

## Failure/abort

- **No Part 30 entry.** If Part 30 has no entry for the requested Section, nothing is built: the
  command says Part 30 must be expanded for that Phase first. There is no Phase Spec, and Phase 2
  waits until Part 30 is expanded for it.
- **A spec already exists.** `build` over an existing Section Spec is refused and points to
  `revise`; the chain is never rebuilt blind (revise it, top-down).
- **This spec not in force.** While this spec is `DRAFT`, `AMENDED-PENDING-RECONFIRM` or
  `RETIRED`, every Novel-Part Spec and Chapter Spec build or revise in this Section is refused, and
  each refusal names `/section-spec` (Part 38 Rule 9.1.1). Specs already built under it keep the status
  they have; nothing flips automatically (Rule 9.4.2).
- **`[SKIP SPEC]`** defers confirmation and keeps the work: the draft is written as `DRAFT`, the
  registry row says `DRAFT`, the skip is noted in the Audit and Settlement Notes, and the chain stops here until
  `[CONFIRM SPEC]`. The command can be run again.
- **Built ahead and the story moved.** The built-against stamp is compared with reality at the
  boundary; only what the move touched is re-asked (Part 38 Rule 9.2.3).
- **Conflicts.** Irreconcilable conflicts (author intent against Locked Canon or Part 30, or
  against an established ledger fact) are put to the author through `AskUserQuestion`, never
  force-written and never silently reconciled.
- **Resets and rewinds.** The spec survives every reset, rewind and redraft; `/hard-reset` deletes
  it with the other two kinds. When written Areas are removed, a `COMPLETED` Section Spec returns
  to `CONFIRMED` as soon as any Novel-Part Spec under it is no longer `COMPLETED`, and its
  completion text is kept as history (Part 38 Rule 9.8.1); the reset command's reconciliation pass makes
  that change, not this command, and refreshes the registry row's Status and Coverage with it
  (Rules 1.2.2 and 10.1.2).
- **A correction of record** (no plan change, no change to any Area text) is written as a light annotation
  with a variance note and needs no re-confirm.
