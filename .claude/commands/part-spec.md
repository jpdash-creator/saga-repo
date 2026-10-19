---
description: Build, revise, show, or complete a Novel-Part Spec (Part 38 Story Specification Law) -- the author-confirmed plan that lists every Chapter of one Novel-Part in depth, made after its Section Spec and before any Chapter Spec in that Novel-Part.
argument-hint: "[build|revise|show|complete] [Novel-Part reference, e.g. 1.2.3]"
user-invocable: true
---

# `/part-spec`

Corresponds to canon command `[PART SPEC]` (C-41 — Part 38 Story
Specification Law Area 11). One spec
file per Novel-Part at
`.claude/story-memory/phase-section-part-chapter-area-specs/phase-N/section-N/part-N/part-N-spec.md`,
reference `P.S.P` (for example `1.2.3`), registered in the Novel-Part Specs table of that
folder's `_index.md`. Governing guardrail:
`.claude/guardrails/ledger/guardrail-story-spec-law.md`; primary skill:
`spec-story-specification-law` (Areas 9 and 11).

**The name.** The formal name of the thing this command builds is the **Novel-Part Spec**. In
the command name, "Part" means a Novel-Part (the third tier of Part 2's five-tier structure), never
a canon-law Part such as Part 38. Rule text and the registry always say "Novel-Part Spec"; the
short form "Part Spec" appears only in the command name `/part-spec` and the code `[PART SPEC]`.
Its two neighbours are the **Section Spec** (`/section-spec`, C-40, reference `P.S`) above it and
the **Chapter Spec** (`/chapter-spec`, C-39, reference `P.S.P.CCC`) below it; the three together
are the **spec chain** (Part 38 Rule 38.9).

**Where it sits.** A Novel-Part Spec cannot exist without a Section Spec that is `CONFIRMED` (or
`COMPLETED`), and no Chapter Spec in the Novel-Part can be built or revised without a Novel-Part
Spec that is `CONFIRMED` (or `COMPLETED`) (Part 38 Rule 9.1.1). The Novel-Part plan lives here
and in no Chapter Spec (Rule 38.11 and Area 11; Rule 11.1.1).

**Modes** (first argument; `build` is the default when omitted; the second argument is the
Novel-Part reference, and when it is left out the command takes the Novel-Part the story is in, from
the last written Area and the registry, or Novel-Part 1.1.1 at the start of the story (`story start`), and says which one it took before it asks anything):

- **`build`** — create the Novel-Part Spec for a Novel-Part that has none. A reference that names a
  later Novel-Part than the one the story is in is an **ahead-build** (Rules 9.2.2 and 9.2.3, below).
  For a Novel-Part that already has written Chapters this is a **retro-fit** (Rule 9.8.2): statuses
  are taken from the record, every Chapter entry already written is recorded as it was written,
  anything the record does not show is asked or left as the author directs, and the Audit and Settlement
  Notes say "as-built reconstructed". If a Novel-Part Spec already exists for the reference, do not build
  over it: run `revise`.
- **`revise`** — change an existing Novel-Part Spec. A change to the Novel-Part's purpose, its
  closing state or hand-off, its calendar window or the reveals it owes is **substantial**: it re-runs
  the audit and the final sweep and needs a fresh `[CONFIRM SPEC]`. Adding, splitting, merging or
  dropping a Chapter entry, a change inside one entry that leaves the Novel-Part's purpose, calendar
  window, reveals owed and closing state as they were, an audit note, status housekeeping and the
  wording of a working label are **light**: they are written once the author signs off (Part 38 Rules 9.4.2
  and 11.7.2). When Chapter Specs already exist under the spec, `revise` runs the cascade report
  (below).
- **`show`** — read-only render of the spec and its registry row. No consultation, no audit, no
  writes.
- **`complete`** — mark the Novel-Part Spec `COMPLETED` once its Novel-Part has finished (see
  below). Normally reached through `/next-part`; invokable alone.

There is no short or quick form of this command: every build is the
full consultation.

## What a Novel-Part Spec is (authority)

A Novel-Part Spec is the plan of one Novel-Part. It sits between the Section Spec's short entry for
the Novel-Part and the Chapter Specs, and it lists **every Chapter of the Novel-Part in depth**, so
that the story line across the Chapters is decided before any one Chapter is planned scene by scene
(Part 38 Rules 11.1.1 and 11.2.1). It holds twelve blocks, numbered 0 to 11:

0. **Header block** — the name chain through the Novel-Part (the Phase and Section names are Locked
   under Part 30 and tagged `locked`; the Novel-Part name is a working label), the Section Spec
   reference, the purpose (Part 30 functions by name only), the Novel-Part's calendar window (inside
   the Section's window, as dates plus Phase Day: Part 41 Area 4,
   Phase Day conversion and Section windows, cited and never copied; a window that opens in the last dark hour
   and runs on into a dawn starts on that dawn's date, Part 41 Area 2, the one scoped exception)
   and the carry-in from the previous
   Novel-Part (naming the last dated moment of the story so far, read from the calendar ledger's Current
   Position block, Part 41 Area 9).
1. **Thematic movement** — filled from the Section Spec's entry for this Novel-Part, then refined
   (the derivation is noted in block 11, not in the body).
2. **Chapter entries** — one for every Chapter, with its working title, purpose (by function name),
   calendar window, threads in and out, **who is on the page**, key events, reveals and payoffs owed,
   opening hook, closing beat, **Chapter pacing** and **Chapter word budget** (each a guide that
   may read `unset`; Part 38 Rule 11.3.7, Amended 2026-10-07), a **one-line Area outline**, linked
   setup keys and a status that is worked out from the Chapter Spec and the registry and is never
   stored (Part 38 Rules 11.3.2 to 11.3.5); after the entries, a **Scene Map across Chapters**
   (a table of the scenes that run across a Chapter seam, scene IDs `PS1`, `PS2`, ...; an empty
   table says none).
3. **Threads, setups and payoffs** at Novel-Part grain.
4. **Protagonist arc line** through the Novel-Part, all eight protagonists.
5. **Progression beats** against the Part 30 map.
6. **Opposition, pressure and reveal timing.**
7. **Cut and cliffhanger plan across Chapters.**
8. **Closing state and hand-off** to the next Novel-Part.
9. **Standing exclusions** (by reference to the Chapter Spec template, section 3).
10. **Completion record** — the final variance summary, Reader now knows, digest and the threads
    carried to the next Novel-Part, written at completion.
11. **Audit and Settlement Notes** — the last section of the file, a plain list of the nine kinds
    of Part 38 Rule 9.10.2 (Settled, Skipped, Open, Deferred, From, Inherited, Name, Variance, Audit),
    each pointing back to the plan item it concerns (by block, Chapter entry and field). Nothing of
    the kind is written anywhere else in the file.

The header lines are: Governing Law, Spec Status, Spec Version | Confirmed, Last Updated, Light
Continuity Audit and the **built-against stamp** (the last completed Chapter reference, or `story start`, and
the ledger state the spec was built against).

**Clean body, notes at the end** (Part 38, the Audit and Settlement Notes rule). The body
(blocks 0 to 10) reads as plain plan text from start to finish. It carries no inline
`[SETTLED ...]`, `[OPEN ...]`, `[SKIPPED ...]`, `[FROM ...]` or `[ASKED ...]` tag and
no provenance, ruling or audit mark. Each settled, skipped, deferred or derived item is a plain list line
in block 11 beginning with the plan item it concerns, then the kind (Settled with the answer and date; Skipped with what the planner chose; Deferred with the level it was deferred to; From with the Section Spec entry it was taken from; Inherited with the source spec, answer and date),
never a table (Part 38 Rule 9.10.2). A tag found in the body is a schema finding.

What the spec holds and does not hold:

- **Status.** The spec status is one of `DRAFT`, `CONFIRMED`, `AMENDED-PENDING-RECONFIRM`,
  `COMPLETED`, `RETIRED`.
- **Guides, not blocks.** The Chapter list is the plan, and no expected Chapter range is stored: the
  list's length is read as information only (Part 2 Area 9). Setups, payoffs and threads here are a guide and a suggestion, linked by shared keys
  (a Part 30 Setups-table row number, or a short thread name) to the Section Spec above and the
  Chapter Spec below. The story may plant elsewhere, pay earlier or later, or drop one, and an unmet
  suggestion creates no check, gate or question (Rule 9.5.4).
- **Names are working labels.** Chapter titles here are labels. No Establishment tag
  (`proposed` or `locked-at-Gate-1`) is stored in a Novel-Part Spec; establishment is recorded in the
  Chapter Spec header and in the delivered files. Areas are never named here, only described (Rule
  11.3.4).
- **Never here:** tone, voice, sensory tags or content tags; Area names (the pacing and word budget
  of each Chapter are asked, topic 6, and are the only pacing and size this build asks); Area pacing, size
  (1,600, 1,800 or 2,000 words) and opening and closing types (these belong to the Chapter Spec); and the
  Epigraph, which lives in the Section Spec, and in Part 30 too for a Phase's opening title page,
  which prints both (Rule 10.3.1). Questions about any of these are never asked in this build.
- **Authority.** The spec is intent. It never establishes a canon fact (Rule 1.3.2) and never
  restates ledger content (Rule 1.4.2); spec-to-spec derivation from the Section Spec is allowed and
  is always noted in block 11 as a From note (Rule 9.3.4). Order of authority: Locked Canon > ledger > Section Spec >
  Novel-Part Spec > Chapter Spec for what a level must do, and the lower spec governs its own detail
  (Part 38 Rule 9.4.1); session-log is never an input.
- **Settling power downward.** A confirmed Novel-Part Spec's Settled notes (block 11) are
  not asked again when a Chapter Spec is built under it; they are carried into the Chapter Spec's
  own Audit and Settlement Notes as Inherited notes naming the Novel-Part Spec, the answer and the date,
  pointing to the item they bear on (Rule 9.5.1), so the Area-time gate reads
  only the Chapter Spec. The carve-outs stand (Part 38 Rule 9.5.3): Area pacing is never settled above the Chapter Spec (a Chapter pacing and word budget here are guides the Chapter Spec settles in its own header, Rule 11.3.7), tone,
  voice, sensory and content tags stay with the Area, Part 36 Autonomous Matters are never
  fixed above Area, a genuinely new branch or a reduced-clarity item is asked again at any level
  with the stale answer shown (Rule 4.2.4), and a settled item in an upper spec never makes a name or
  fact canon.
- **After a Chapter Spec is confirmed**, the Chapter header governs the writing and Gate 1; the
  Chapter's entry here stays the plan baseline. A Chapter departs upward only on what the entry
  fixes (Part 38 Rules 9.3.2 and 9.3.3), and the departure is noted as a variance in the Audit and Settlement Notes here **and in those of the
  Section Spec above this one**, written top-down in one step, Section Spec first (Rules 9.4.5 and 11.4.2).
  The note is light and appended: this spec's plan changes only through its own `revise`, and the
  author chooses for each departure whether to amend the entry or keep it as the plan baseline.
- **Who reads it.** Builders of a Chapter Spec read this spec in full. Area-time agents (the area
  maker, the scorer, both Gate 1 checkers and the outline-planner when it plans a single Area) read
  only its header block (0) and its closing-state block (8), because the Chapter Spec carries every
  inherited item with its source note (Part 38 Rule 9.9.2).

## Preconditions

- Read `.claude/guardrails/ledger/guardrail-story-spec-law.md` and
  `.claude/guardrails/commands/guardrail-plan-then-auto-execution.md` — this command is one of the
  Plan Mode → Auto Mode in-scope commands (the consultation rounds are its Plan Mode; default
  model/effort, mandatory parallelism and milestone progress reports apply end to end).
- `spec-story-specification-law` is the primary skill read (consolidated-first per
  `guardrails/authority/guardrail-consolidated-skill-reading.md`), Areas 9 and 11 in particular.
- **The chain.** The Section Spec of this Novel-Part's Section must exist and be `CONFIRMED` or
  `COMPLETED`. A Section Spec that is `DRAFT` (saved by `[SKIP SPEC]`), `AMENDED-PENDING-RECONFIRM`
  or `RETIRED`, or that does not exist, refuses this build, and the refusal names the command to run:
  `/section-spec` (Part 38 Rule 9.1.1). There is no Phase Spec: Part 30 is the Phase-level plan, and
  `/section-spec` refuses a Section that Part 30 has no entry for, so no Novel-Part Spec can be built
  for a Phase that Part 30 does not yet cover (Rule 9.1.4).
- **The entry.** The Section Spec must have an entry for this Novel-Part (block 3 of the Section Spec).
  If it has none, because the story needs a Novel-Part the Section Spec did not plan, stop and direct
  the author to `/section-spec revise` to add it first. Adding a Novel-Part to a Section Spec is a
  substantial amendment (Rules 9.4.2 and 10.6.2), so there is no light add here; nothing is built
  under a Novel-Part the Section Spec does not know.
- **Read the whole Section Spec in full**, not only this Novel-Part's entry (Part 38 Rule 9.9.2). The entry
  pre-fills the draft. Part 30 is read through the Section Spec's citations and, where a question
  needs it, from `narration-novel-macro-story-law` itself.
- Spec files are story-memory files written with ordinary Write/Edit — the authorized-scripts law
  (`guardrails/tools/guardrail-authorized-scripts-only.md`) covers only novel output files and does
  not apply to them. No script is created in the repository for this work.
- **Named items, naming and cost.** Named items are written in italic, naming is never presented
  as a cost, and an item met in the consultation enters no register row: follow Part 38 Rule 9.9.4 and Part 28 Rules 20.8.2, 20.8.7 and 20.9. Where an option could
  name or leave unnamed, the named version is the `(Recommended)` one.
- **Monsters (Part 40).** A monster name met in the consultation is
  set in roman and enters no ledger entry before its first Area (Part 38 Rule 1.3.2). The Kind of the beasts that
  Part 30 plans for Phase 1 is defined and named at the Chapter Spec, not here ("Define during
  chapter-spec", Part 40 Rule 40.7.5.1). **Standing exclusion: no sentient monster, and no allusion to one,
  in any Phase 1 Chapter entry (Law P30-L9), save the one narrow artifact-made exception of Canon Amendment 2026-10-19 (Law P30-L9).** A plan that would bring a Tier C or D monster to a trigger of
  Part 40 Rule 40.6.2.2 is put to the author, never decided.

## Plan Mode → Auto Mode

For `build` and `revise`, Steps 0 and 1 are this command's **Plan Mode**: grounding, then as many
`AskUserQuestion` rounds as it takes, then the final sweep and the author's explicit "nothing further
to steer" answer (Part 38 Rules 9.6.1 and 9.6.5). Steps 2 to 3 run in **Auto Mode** with no further
discretionary questions. Auto Mode never waives a mandatory stop: the Step 3 `[CONFIRM SPEC]` token is
a hard pause exactly as Gate 1's `[CONFIRM WRITE]` is in `/next-area`. A finding that only the author can rule
on is asked as a question, never settled by the planner (Rule 9.4.1); it is the one legitimate stop inside
Auto Mode. `show` is read-only and has no Plan Mode boundary; `complete` asks its questions first and
one confirmation before it writes `COMPLETED`.

## Parallel orchestration

Per `guardrails/commands/guardrail-plan-then-auto-execution.md` (absolute binding, not a convenience
to weigh) and Part 38 Rule 9.9.3:

- **Step 0 ∥ planner grounding:** launch **outline-planner** as a background agent at the same moment
  the first consultation round is presented, instructing it to ground on the guardrails (including
  `ledger/guardrail-story-spec-law.md`), `spec-story-specification-law`, **the whole Section Spec**, the
  Part 30 / Part 2 / Part 28 consolidated skills, all relevant `.claude/story-memory/ledger-*/` entries,
  the previous Novel-Part Spec (its closing-state block and, if it is complete, its completion
  record; when a boundary command, `/next-part` or `/next-section`, is building this spec, the closing
  unit's completion pieces are only drafted at that moment and are written at the last confirm of the
  chain, Rule 9.4.4, so they are read as drafted), the Novel-Part's existing Areas and Chapter Specs
  (retro-fit and revise cases), and the CDL-2 Section running aggregate. It reports the open branch
  points it finds and does *not* finalize the spec. Author answers are fed back by `SendMessage`; any new branch the planner surfaces feeds
  further rounds.
- **∥ one continuity-checker pre-read** at the same moment, serving the sweep and the audit: Locked
  Canon, Entity Naming Law, Part 30 locks and Section mandates, the Section Spec's duties for this
  Novel-Part, the ledger state. The drafted spec is sent to it by `SendMessage` when it lands.
- **Inside a boundary command** (`/start-story`, `/next-section`, `/next-part`): at
  command start launch together the planner grounding for every level the command will build, the
  closing-unit reviews that already run concurrently, and one continuity-checker pre-read for all the
  audits. Consultation and confirmation then run **strictly top-down** (Section Spec, then this
  Novel-Part Spec, then the Chapter Spec), only one confirm prompt open at a time. When this spec is
  confirmed, the Chapter planner is told by `SendMessage` that its parent is confirmed, and it
  finalises.

Never parallelized: consultation answers precede the finalized draft; the sweep precedes the "nothing
further" question; the audit precedes presentation; the author's `[CONFIRM SPEC]` or `[SKIP SPEC]`
precedes any file write; a Chapter Spec is never presented before its Novel-Part Spec is confirmed.

## Sequence (build / revise)

0. **Plan Mode — chain check, grounding and consultation.** Check the precondition chain and say
   which Novel-Part this is. Launch the planner grounding in parallel with the first `AskUserQuestion`
   round. Read the Section Spec's entry for this Novel-Part and use it as the pre-filled draft: each
   pre-filled value is shown as the `(Recommended)` option, and the derivation is noted in block 11
   (not in the body); anything the author settled in the Section Spec is carried as an Inherited note in
   block 11 (source spec, answer and date) and is **not** asked again (Part 38 Rule 9.5.1).
   Consultation is exhaustive and goes on for as many
   rounds as it takes until no unasked branch is left at this spec's own level (Rule 9.6.1; see
   Consultation below). A new collective or location an entry introduces is not registered at this level:
   the planner notes it in the entry as owing a code under Part 39 Rule 39.23.1.5, to be asked and
   registered at the Chapter Spec build. The built-against stamp is taken now (the last completed Chapter
   and the ledger state), and it matters most for an **ahead-build**. When a boundary command
   (`/next-part` or a peer) reaches a Novel-Part whose spec was built ahead, it does not rebuild it: it
   runs `revise` on it, compares the stamp with reality, and re-asks only the affected items, each as a
   clarity-reduction question that shows the original answer and the source of the change (Part 38 Rules 9.2.3
   and 4.2.4).
1. **Final sweep, then "nothing further to steer".** outline-planner assembles the whole draft and
   the planner **and** the continuity-checker sweep it: conflicts with Part 30, the ledgers and the
   Section Spec; any branch at this level still unasked; and a **re-listing of every SKIP and every
   deferral**, so the author has a last chance to settle each (Rule 9.6.5). If the sweep returns
   anything new, go back to Step 0 for more rounds and then sweep again. When it returns nothing new,
   ask the author whether there is anything further to steer: one `AskUserQuestion` with the options "Nothing further to steer", "Change one of the skipped or deferred items" and "Steer something else", with no SKIP option (the same three options as in `/section-spec`). Only an explicit "nothing further"
   ends Plan Mode; anything the author adds sends the command back to Step 0. There is no score, no
   percentage and no round count: the test is the sweep and the author's answer.
2. **outline-planner finalises the draft** from the settled answers: every block of the template,
   every Chapter entry in order as clean plan text, with the Settled, Skipped (planner chose X),
   From, Inherited and Deferred (by the author to ...) notes written
   exactly as the author left them in block 11, each pointing to its plan item (Part 38 Rules 2.3.6 and 9.5.2). The planner never leaves an item open
   on its own (Rule 9.6.3). Then the **light continuity-checker audit** (report-only, writes nothing;
   scope in Rule 11.6.1):
   - the Novel-Part window sits inside the Section window (Part 30 §1.3.2a) and each Chapter window
     sits inside the Novel-Part window (the nesting that Part 30 Check 11-2 reads); each window's dates
     and Phase Day span agree by the conversion of Part 41 Area 4, and the carry-in names the last dated
     moment (a mismatch is a finding for the planner to correct);
   - every duty the Section Spec gives this Novel-Part (Major Narrative Functions carried, Locked events
     placed, reveals owed, items deferred to this spec) is covered by some Chapter entry, and every
     item the Section Spec settled is carried in as a note (a Part 30 setups row assigned to this
     Novel-Part and not carried is shown as information only and never blocks, Rules 11.6.1 and 9.5.4);
   - all eight protagonists are accounted for in each Chapter entry (viewpoint, on the page, or off the
     page with where they stand), stated without counts;
   - the threads coming in match the previous Novel-Part's close (the carry-in item, extended to this
     level, using the stamp for a spec built ahead);
   - the Chapter labels pass Part 28 Rules 18.4.1 to 18.4.3 as **advice only**;
   - standing exclusions are clean (P30-L8 forbidden entities; P30-L9, no sentient monster (save the one narrow artifact-made exception of Canon Amendment 2026-10-19 (Law P30-L9)) and no allusion to
     one in Phase 1; the author-removed Sapphire Line);
   - the one-line Area outlines hold descriptors only: no opening or closing types, Area pacing, Area sizes
     or Area names;
   - each Chapter entry carries a Chapter pacing and a Chapter word budget (a value or `unset`), and
     the Scene Map across Chapters stands in the block, each row's Chapters being entries of this
     spec (Rule 11.3.7);
   - schema conformance: every block present, every field a value or an author deferral, the body
     free of inline tags (a tag in the body blocks), every note in block 11 well formed and pointing
     to a plan item, and no Establishment tag, no count or range of Chapters and no
     stored status appears;
   - parent conformance: nothing contradicts a Locked Canon item or a settled item of the Section
     Spec, and for the last Novel-Part of a Section block 8 agrees with the Section Spec's hand-off;
     where this draft otherwise departs from the Section Spec's entry, each departure is listed.
   On a blocking finding (Part 38 Rule 11.6.1: every item above except the label advice and an unmet setups
   assignment, which are information only), revise through
   outline-planner and re-audit before presenting; never present a spec with a blocking finding
   outstanding. The advice-only label item and an unmet setups assignment are reported and block nothing.
3. **Present the spec + audit summary** and wait for an explicit `[CONFIRM SPEC]` / `[REVISE SPEC]` /
   `[SKIP SPEC]` — never assume confirmation. The prompt names the artifact and its reference
   ("Novel-Part Spec 1.2.3"). The presentation shows each Chapter entry in order; the Chapters' openings
   and closings side by side (block 7); the protagonist lines; the audit summary; every SKIP and
   deferral; and two lists kept for the Section Spec: (a) every **departure from the Section Spec's
   entry** (purpose, calendar window, hand-off or closing state, reveals owed) and (b)
   every **change of Chapter list** against the Section Spec's guide list (Chapters added, split, merged
   or dropped). When either list has entries, the author is also asked, before the token prompt and
   **for each item on the lists**, whether to **leave the Section Spec's original as the plan
   baseline** or to **amend the Section Spec to match**. Both answers are lawful, a variance note for
   each item is left on the Section Spec either way, and this spec governs the Chapters either way
   (Part 38 Rules 9.4.5 and 11.4.3; Step 4 says what is written and what the amend answer leads to).
   `[REVISE SPEC]` loops back through Steps 0 to 2 (consultation scoped to what changed, then a new
   sweep).
4. **On `[CONFIRM SPEC]`:** this command (the orchestrator, never outline-planner) writes top-down in
   one step (Rule 9.4.5), with ordinary Write/Edit and at once (Rule 9.4.4). First it **always appends
   to the Section Spec**, the only spec above this one, one variance note for each departure and each
   Chapter-list change on the two lists of Step 3, giving the author's answer for each (original left
   as the plan baseline, or plan amended); each note is a light amendment: a lower flow may append
   variance notes to a spec it derives from, but never changes that spec's plan content (Part 38 Rules 9.4.3,
   9.4.5 and 11.4.3). It moves the Section Spec row's Last Updated date. Then it writes this spec file —
   status `CONFIRMED`, the version, the confirmation date, the audit result and the built-against stamp
   — and updates the Novel-Part Specs row of the registry `_index.md` (Spec File / Ref / Status / Spec
   Ver / Last Updated / Coverage, which for this kind reads "Chapters completed / planned"; the
   coverage cell is refreshed at this spec's own confirm, at any completion write step, a child's
   included, and at a reset or rewind rollback, and never at Gate 2; Part 38 Rules 1.2.2 and 11.1.2). With no
   departure and no Chapter-list change nothing is written to the Section Spec.
   **Where at Step 3 the author chose, for any item, to amend the Section Spec to match,** the Section
   Spec's own entry or Chapter list changes only through `/section-spec revise` (Rule 9.4.2), and
   this command changes nothing else in the Section Spec: it offers to run `/section-spec revise`
   straight after the write, starting from what was shown at Step 3, and where that change is
   substantial (a purpose, window, hand-off or reveals-owed change, Part 38 Rule 3.5.2) the audit and the
   confirm are taken in that same run. This spec is **never saved as `DRAFT` because of that
   answer**: it is written `CONFIRMED` as above and governs the Chapters either way (Rule 11.4.3),
   whereas a `DRAFT` would block every Chapter build under it.
   **In a boundary chain** the completion writes for the outgoing specs (Chapter, then Novel-Part,
   then Section, bottom-up) are not made here; the boundary command makes them in one write step at
   the last confirm of the chain, the new Chapter Spec's (Part 38 Rule 9.4.4).
   **On `[SKIP SPEC]`:** it writes the drafted spec the same way with Spec Status `DRAFT` (for a
   substantial `revise`, `AMENDED-PENDING-RECONFIRM`, Rule 3.5.2), sets the registry row Status to match,
   notes the skip in the spec's Audit and Settlement Notes (Rule 3.4.1) and appends nothing upward. A DRAFT spec has
   no settling power. **A `[SKIP SPEC]` stops the chain at this level:** no Chapter Spec in this
   Novel-Part can be built or revised until `[CONFIRM SPEC]`, no outgoing spec is completed, and the
   boundary command that was running can be run again.
5. **Log the outcome to `.claude/story-memory/session-log/`** — this command writes the line: mode,
   "Novel-Part Spec" and its reference, the confirmation token, the author deferrals and Open notes
   in the Audit and Settlement Notes left in the spec, and the variance notes appended to the Section Spec (listed first, as they were
   written first).

## Consultation (Step 0)

**How questions are put** (Part 38 Rules 38.13, 3.2.2, 3.2.3 and 9.6.4; Part 28 Rule 19.4; Part 36
Area 13). Every question is asked through `AskUserQuestion` in plain everyday words, with 2 to 3
concrete options built from the Section Spec's entry, Part 30, the ledgers and the story so far, plus
`SKIP — let AI decide`, four options in all, up to four questions in one call. Options that point the
story in a direction each carry a one- or two-sentence preview in the Part 36 thematic voice, with
exposition risk flagged. The author can always answer in their own words through "Other". An answer is
recorded as a Settled note (answer and date) in block 11, the Audit and Settlement Notes, pointing to
the plan item it concerns, while the body states the plan plainly. A SKIP is recorded as a Skipped
note (planner chose X, with the date) and settles nothing (Rule 4.1.2). **The planner never leaves an item open on its own:** every field of
every entry is put to the author. Only the author may defer an item, by saying it can be handled in
the Chapter Spec or in the writing; it is then recorded as a Deferred note in block 11 (Deferred to: the
Chapter Spec or the Area writing, with the date), and a spec may be confirmed with such
deferrals. A deferral is copied into the Audit and Settlement Notes of the Chapter Spec of the
Chapter it bears on, so that Chapter's build, or the Area-time gate, asks the author; the drafter
never settles it silently (Part 38 Rule 9.5.2). A deferral the Section Spec made *to this Novel-Part Spec*
(a Deferred note in the Section Spec's Audit and Settlement Notes naming the Novel-Part Spec) is asked
here.

**The grain test** (Rule 9.6.2). A question belongs in this build only if the author's answer is the
first thing that changes **this spec's own plan**: the set and order of Chapters, a Chapter's purpose,
window, who is on the page, key events, reveals, hook or closing beat, or the Novel-Part's hand-off.
Anything that only changes a Chapter's inside (Area pacing, Area size, Area budget stretch, opening and closing types,
tone, voice, sensory and content tags) is the Chapter Spec's question and is not
asked here. Anything Part 30 or the ledgers already settle is not asked. Anything the Section Spec
settled is not asked again unless it is a new branch or its clarity has dropped, in which case it is
shown with the original answer and the source of the change (Rule 4.2.4).

**Topics, in order** (several rounds each, as the story needs):

1. **The Novel-Part's frame:** its purpose (the Part 30 functions it carries, named, never copied), its
   thematic movement (direction options with previews), its place or places, its calendar window
   inside the Section window (Part 30 §1.3.2a; dates plus Phase Day, Part 41 Area 4), its opening state and the carry-in from the
   previous Novel-Part (what the reader knows, where each protagonist stands, which threads arrive). When
   the previous Novel-Part has no spec yet, the carry-in is read from the Section Spec's closing
   state for it, marked as planned and covered by the built-against stamp. For the first Novel-Part of the story the carry-in is `story start`; for the first of a later Section it is the previous Section's last Novel-Part.
2. **The Chapter set and order**, starting from the Section Spec's guide list: keep it, add a Chapter,
   split one, merge two, or drop one, each shown with what it does to the story line, then the order,
   then a working label for each Chapter.
3. **Each Chapter in turn, every field of its entry** (Part 38 Rules 11.3.2 and 11.3.3): its purpose (by function
   name); its calendar window, inside the Novel-Part window (dates plus Phase Day); threads in and out; **who is on the page** —
   a compact line naming the viewpoint, who is on the page, and, for each protagonist off the page,
   where that protagonist stands, so all eight are accounted for; key events; reveals and payoffs
   owed; the opening hook; the closing beat; a one-line Area outline of descriptors only (the scenes in
   a word or two each, never named, never sized, never typed, Part 38 Rule 11.3.4); and the setup keys the
   Chapter carries. The questions for one Chapter are grouped up to four to a call.
4. **Across the Chapters:** the cut and cliffhanger plan (how Chapters end and open so that
   neighbouring ones differ, and where each cliffhanger or cut-away is answered or returned to, planned
   at Chapter grain); threads, setups and payoffs at this grain (a guide: planted in Chapter Y, paid in
   Chapter W, by shared key); the protagonist arc line for all eight through the Novel-Part; the progression beats
   (cultivation, technology, named moves) against the Part 30 map, as a guide with nobody shown above their
   Section band earlier; opposition, pressure and reveal timing; and the Novel-Part's closing state and
   hand-off.
5. **Departures from the Section Spec.** Where an answer differs from the Section Spec's entry, the
   difference is asked about as a question and carried to the Step 3 lists. It is never a silent pick
   (Part 38 Rule 9.4.1).

6. **Pacing, word budget and scenes across Chapters** (block 2; Part 38 Rule 11.3.7, Amended
   2026-10-07). Three questions for each Chapter of the Novel-Part, in the Chapter order, put in the
   same AskUserQuestion style as the topics above (2 to 3 concrete options built from the Chapter's
   key events and closing beat, plus `SKIP — let AI decide`, each option with its thematic
   preview): (a) **Pacing**: Fast, Medium or Slow for the Chapter, with the guidance stated in the
   question: fights are usually Fast, intrigue, deception, lore and thought are usually Slow,
   dialogue is usually Medium, and it is always the author's call because it depends on the story;
   the planner offers its recommendation and the reason from the Chapter's key events. (b) **Word
   budget**: a figure for the Chapter, offered as a guide from its key events, with a plain chance
   to **raise** it ("raise it" is always an option, the new figure typed under "Other"); `unset` is
   offered first where the author has no figure; the Chapter Spec settles the Chapter size target
   and the Area targets that add up to it. (c) **Scenes that run across Chapters**: whether any
   scene starts in one Chapter and carries on into the next, and for each one that does, the
   Chapters it covers, the viewpoints in order and where each takes over, the movement of the scene
   (its arc), its pacing, its word budget and the exact state at each Chapter seam (position,
   wounds, who knows what, whose floor it is). "No scene runs across a Chapter" is offered first
   and, when chosen, leaves the Scene Map table empty. The planner states the visible-break rule
   once with the question: a scene break shows only when the scene changes or the same scene moves
   to a different viewpoint; a scene that simply runs on with the same viewpoint shows none. Answers
   are Settled notes in block 11; a SKIP records the planner's choice and settles nothing; `unset`
   is a lawful answer for (a) and (b).

No question asks how many Chapters the Novel-Part should have, how long it should be in Chapters, or what any
Chapter's count should be: the Chapter list is the plan, the story decides where the Novel-Part
ends (Rule 1.5.1), and no range is stored. MAJOR-entity names and Hero or Villain address-register
gaps still route through consultation per Part 28 Area 20.4 when a Chapter entry would force one.

## Adding a Chapter entry later (Rule 11.5.2)

A Chapter the story needs that has no entry here is added by a **light amendment**: a short entry round
(purpose, calendar window, threads in and out, who is on the page, key events, hook, closing beat, Chapter pacing and Chapter word budget),
asked in the same question shape, with the new entry shown to the author. There are two ways in:

- **From `/chapter-spec` or `/next-chapter`** (Part 38 Rule 9.1.2): the Chapter build stops, offers to add the
  entry and runs the short round (see "When the Chapter has no entry" in `/chapter-spec`). The entry
  then goes to the author with its own `[CONFIRM SPEC]` / `[REVISE SPEC]` / `[SKIP SPEC]` prompt, which
  names "Novel-Part Spec 1.2.3, new entry for Chapter 1.2.3.004", and is written at that confirm with
  this spec's registry row. Only after that confirm does the Chapter build begin, and the two prompts
  are never open together. Under `[SKIP SPEC]`, or if the author declines, this spec is left as it was
  and no Chapter Spec is built.
- **From `/part-spec revise`**: the same short round, and the entry is written on the author's
  sign-off, with a variance line.

Either way, because the Chapter list is also a guide in the Section Spec, the addition is noted as a
variance on the Section Spec (Part 38 Rule 11.4.3), written first and the entry second, top-down (Rule 9.4.5).

## `revise`, `show` and `complete` in detail

### Cascade report (`revise` with children)

When a change to this spec is made after Chapter Specs exist under it, the continuity-checker reports
every Chapter entry and every Chapter Spec the change no longer fits. For each one the author picks:
**keep it** (a variance is noted), **amend it**, or **mark it `AMENDED-PENDING-RECONFIRM`**. Nothing
flips automatically (Part 38 Rule 9.4.2). Written Areas are never touched by a spec amendment; a correction there
goes through `/revise-area` or a redraft. A `COMPLETED` spec stays a living record: `revise` works any
time, and its completion pieces (variance summary, Reader-now-knows line, digest) are refreshed when
it is revised (Rule 11.7.2). A revision that changes plan content for Areas already written leaves it to
the author whether to redraft. After the re-confirm, the spec takes the status its record supports:
`COMPLETED` if every Chapter Spec under it is still `COMPLETED` and the author's completion yes still stands, otherwise `CONFIRMED`.
**Retiring** a Novel-Part Spec is always an explicit `revise` outcome (`RETIRED`), never silent
(Part 38 Rule 7.2.2), and is refused while any Chapter Spec under it is not `RETIRED` until the author has
ruled on each of them (Rule 9.8.3).

### `show`

Read the spec file and its registry row and render them for the author: the blocks in order, each
Chapter entry with its derived status (no spec, `DRAFT`, `CONFIRMED` or `COMPLETED`, read from the
Chapter Specs and the registry), the author deferrals and SKIPs, and the variance notes. Read-only; no
consultation, no audit, no writes. For the in-story dates and the open setups across the story, use
`/timeline` and `/threads`; for the chain's statuses, `/status`.

### `complete`

A Novel-Part Spec is `COMPLETED` when its Novel-Part has finished and all its Areas are written; it is
**not closed**, and stays a living record. `/next-part` asks the author, as part of its checks,
**"Has this Novel-Part finished?"**; a yes completes the spec, a no stops the command (Part 38 Rule 9.7.3).
`/next-section` asks one question, "Has this Section finished?", and its yes also stands for the
Section's last Novel-Part and its last Chapter, so this question is not asked a second time there.
Run alone, `complete` asks "Has this Novel-Part finished?" itself and does the same:

1. Verify every Chapter entry has a Chapter Spec that is `COMPLETED` (the last Chapter may be completing
   in this same write step, bottom-up, Chapter first: when the last Chapter's completion pieces are
   not yet written, `complete` first puts the `/chapter-spec` complete questions for it and writes its
   pieces in this step), is `RETIRED` with a variance note, or was
   never written and is recorded as dropped, with a variance note, on the author's yes.
2. Surface, by `AskUserQuestion`, every unresolved Open or Deferred note in the Audit and Settlement Notes, every setup planted and not paid,
   every unresolved cliffhanger and every reveal owed and not delivered: each is resolved, carried
   forward to the next Novel-Part Spec, or marked lapsed. **An item is marked lapsed only on the author's
   answer.** The report on unmet reveals, threads and Part 30 functions is information and never blocks
   (Rule 9.7.4).
3. Ask the author to confirm with `AskUserQuestion` ("Has this Novel-Part finished?", with "Yes, mark
   it completed" and "Not yet"). On "Not yet" nothing is written.
4. On a yes, write the completion content into the spec: the **final variance summary** (planned against
   as written, including Chapters added or dropped), the **Reader now knows** line (by reference to the
   last Chapter's line plus the Novel-Part-level additions, copying no list), the **digest**, and the
   threads and setups carried to the next Novel-Part; set the status to `COMPLETED`; update the registry
   row (Status and the coverage cell "Chapters completed / planned") and, because a child's completion
   refreshes its parent's coverage, the coverage cell of the Section Spec's row (Part 38 Rules 1.2.2 and
   11.1.2); log to session-log.

When `/next-part` or `/next-section` runs `complete` ahead of building the next spec, `complete` does
everything above except the write: a yes means "complete it when the new Chapter Spec is confirmed",
and the write is made at that `[CONFIRM SPEC]`, bottom-up with the outgoing Chapter Spec (and the
Section Spec when a Section ends), in one write step. A `[SKIP SPEC]` anywhere in the chain writes no
completion.

**At the end of Phase 1** no boundary command completes Section 8's last Novel-Part Spec: `/next-phase`
does not (Part 38 Rule 9.1.4). The author runs `/part-spec complete` for it, which takes the last Chapter's
completion questions first and writes that Chapter's pieces in the same bottom-up step, and then
`/section-spec complete` for Section 8, so the author still runs two commands; each writes at once,
and the `/next-phase` note says so.

## Failure/abort

- **Parent not in force.** A missing, `DRAFT`, `AMENDED-PENDING-RECONFIRM` or `RETIRED` Section Spec
  refuses the build and names `/section-spec`. A Section Spec with no entry for this Novel-Part sends
  the author to `/section-spec revise`. No Phase Spec exists, and Phase 2 waits until Part 30 is
  expanded for it.
- **`[SKIP SPEC]`** defers confirmation and keeps the work: the draft is written as `DRAFT`, the
  registry row says `DRAFT`, the skip is noted in the Audit and Settlement Notes, and the chain stops here until
  `[CONFIRM SPEC]`. The command can be run again.
- **Built ahead and the story moved.** The built-against stamp is compared with reality at the boundary;
  only what the move touched is re-asked (Part 38 Rule 9.2.3).
- **Conflicts.** Irreconcilable conflicts (author intent against Locked Canon, or against an established
  ledger fact, or a Chapter entry against what the Section Spec fixes) are put to the author through
  `AskUserQuestion`, never force-written and never silently reconciled.
- **Resets and rewinds.** The spec survives every reset, rewind and redraft; `/hard-reset` deletes it
  with the other two kinds. When written Areas are removed, a `COMPLETED` Novel-Part Spec returns to
  `CONFIRMED` as soon as any Chapter Spec under it is no longer `COMPLETED`, and its completion text is
  kept as history (Part 38 Rule 9.8.1); the reset command's reconciliation pass makes that change, not this
  command, and refreshes the registry row's Status and Coverage with it (Rules 1.2.2 and 11.1.2).
- **A correction of record** (no plan change, no change to any Area text) is written as a light annotation with a
  variance note and needs no re-confirm.
