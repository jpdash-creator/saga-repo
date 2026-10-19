---
description: Build, revise, show, or complete a per-Chapter story specification (Part 38 Story Specification Law) -- the author-confirmed Rich-schema plan every Area in the Chapter is written against, and the last link of the spec chain (Section Spec, Novel-Part Spec, Chapter Spec).
argument-hint: "[build|revise|show|complete] [chapter reference]"
user-invocable: true
---

# `/chapter-spec`

Corresponds to canon command `[CHAPTER SPEC]` (C-39 — Part 38 Story
Specification Law). One spec file per Chapter at
`.claude/story-memory/phase-section-part-chapter-area-specs/phase-N/section-N/part-N/chapter-NNN-spec.md`
(reference `P.S.P.CCC`, for example `1.2.3.004`), registered in the Chapter Specs table of that
folder's `_index.md`. Governing guardrail: `.claude/guardrails/ledger/guardrail-story-spec-law.md`;
primary skill: `spec-story-specification-law`.

**The spec chain.** A Chapter Spec is the last link of a chain of three specs (Part 38 Area 9).
It is built from its own entry in a **Novel-Part Spec** (`/part-spec`, C-41, reference `P.S.P`),
and that spec is built from a **Section Spec** (`/section-spec`, C-40, reference `P.S`). At a
boundary `/start-story`, `/next-section` and `/next-part` build the missing links top-down, each
through its own `[CONFIRM SPEC]`, and run this build last (Rule 9.2.1); `/next-chapter` builds
the Chapter Spec only and, when a link above it is not in force, stops and names the command
that puts it right. Run alone, `/chapter-spec` builds or revises the Chapter Spec; the only
things it writes above it are a new entry (under "When the Chapter has no entry", through that
entry's own confirm) and variance notes on every spec above it, the Section Spec first (Step 4,
Part 38 Rule 9.4.5). Plan content of a higher spec changes only through that spec's own command
(Rule 9.4.3).

**Modes** (first argument; `build` is the default when omitted; the second argument is the
Chapter reference, and when it is left out the command works on the active Chapter, the one
`/status` names, or Chapter 1.1.1.001 at the start of the story (`story start`), and says which one it took before it asks anything):

- **`build`** — create a new spec for a Chapter that has none, from that Chapter's entry in
  its Novel-Part Spec. For an already-started Chapter this is a retro-fit build (Part 38
  Rule 3.1.2, generalised by Rule 9.8.2): Areas already written are recorded **as-built**
  (status `WRITTEN`, beat/POV/pacing/size as actually delivered, audit notes where the record is
  reconstructed), and only the Chapter's remaining Areas go through forward planning and
  consultation. When a spec for the Chapter already exists (a `DRAFT` saved by `[SKIP SPEC]`,
  or one that survived a reset or a rewind), `build` runs as `revise` on it — never a blind
  rebuild.
- **`revise`** — amend an existing spec (`DRAFT`, `CONFIRMED`, `AMENDED-PENDING-RECONFIRM` or
  `COMPLETED`; a `DRAFT` is taken up again and finished). A spec is retired only through an
  explicit `revise` that marks it `RETIRED`, never silently (Part 38 Rule 7.2.2).
  Substantial amendments (new/changed beats, widening or narrowing a Tier Scope Bracket range beyond
  in-flow readjustment, changed entity debuts, changed Area breakdown, scene anchors, opening or closing
  types, an Area's viewpoint, time skips, an Area's thread) re-run the Step 2
  audit and re-confirm via `[CONFIRM SPEC]`; light amendments (audit-note wording, status
  housekeeping, an Area's pacing or size target, in-flow bracket readjustment, setting or clearing a
  sensory anchor, tone, voice or content entry, a change the author ruled live at a Decision Consultation
  Gate) are written directly once the author signs off (Part 38 Rules 2.3.3 and 3.5.2). A `COMPLETED` spec is revised the same way, at any time: its
  status never refuses a revise (only the chain rule below can). If the revision changes plan
  content that a written Area already follows, whether the Area is redrafted is the author's call
  (`/redraft-area`, `/redraft-chapter`); the spec never forces it. When the revise is confirmed,
  a spec whose every Area block is terminal is `COMPLETED` again and any other is `CONFIRMED`, and
  the completion pieces (final variance summary, Reader now knows line, Chapter digest, New named
  things line) are refreshed for what the revision changed. A revision that departs from the
  Novel-Part Spec entry is shown with the departure question of Step 3.
- **`show`** — read-only render of the spec and its registry row, with the chain beside it (the
  Spec Status of its Novel-Part Spec and Section Spec, and its entry in the Novel-Part Spec). No
  consultation, no audit, no writes.
- **`complete`** — Chapter completion with final variance summary (see below). Normally reached
  through `/next-chapter`'s Plan Mode; invokable standalone. A
  Chapter Spec is completed, never closed, and stays a living record.

There is no quick form of `build`: if the author adds the word `quick`, say it does not exist
and run the full build.

## What a spec is (authority)

Rich schema per Part 38: one **Area block** per Area — the plan of one written unit (an Area is
a complete scene, or one stretch of a scene that continues across consecutive Areas of the
Chapter) and the bible that connects the chapter (want, obstacle and stake, opening and closing
type, scene anchors, **Pacing** (decided here for the Area and carried at writing, never re-asked),
**Area size** (1,600, 1,800 or 2,000 words; asked per Area, a separate field from pacing and not
tied to it), carry-over from the previous Area, thread, planned time skips,
story link and change, setups and payoffs (optional), consequences landing here (optional),
emotional line, world/setting/people, novel elements carried, optional fight line, the optional sensory anchor,
tone or voice and content lines (each `unset` until the author sets it), Behavioral Plan (Part 38 section 2.2a), beat, the Area's single Viewpoint (a change of
viewpoint falls between two Areas),
entities/debuts, CDL-2 emphasis, status
`PLANNED`/`DRAFTED`/`WRITTEN`/`DROPPED`) — plus chapter-level **Tier Scope Bracket ranges** (the
spec is the authoritative backing store for bracket ranges; nothing above Chapter grain is
stored, so there is no "Chapters in Part" row). Settled items, skips, deferrals, name and consultation
statuses and variance notes are not marked in the Area blocks: they are notes in the Audit and Settlement
Notes at the end of the file, each pointing to its Area block.

**Built from the Novel-Part Spec entry.** The Chapter's entry in its Novel-Part Spec (Part 38
Rules 11.3.2 and 11.4.1) pre-fills the Chapter header: the title label, Chapter Purpose,
Calendar Window, Threads Carried In and Out, Protagonist Thread Map, Opening hook and Closing beat. Each
pre-filled line is noted in the Audit and Settlement Notes as taken from the Novel-Part Spec
entry (naming the entry and the header line) as a From note. Items the author settled in the
Section Spec or the Novel-Part Spec are carried in as Inherited notes in the same section, naming the source spec, the answer and the date, and every deferral the
author made to the writing is carried in as an Inherited Deferred note (Deferred to: the Area writing, with the date) pointing to the Chapter item it bears on (Part 38 Rules 9.3.1, 9.5.1 and 9.5.2). An
inherited item never loses its note by being copied. The body of the spec reads as clean plan
text with no inline tag of any kind (the rule of the Audit and Settlement Notes, below).
Copying from a higher spec into this one is allowed because it is noted; copying ledger field
values into any spec stays barred (Part 38 Rule 1.4.2, Rule 9.3.4). The names above Chapter
grain are working labels with no Establishment tag. The Establishment status of the Novel-Part and
Chapter labels the Chapter takes from the entry is a Name note in the Audit and Settlement Notes
(`proposed`, then `locked-at-Gate-1` or `locked-at-Gate-2` with its ref; Part 38 Rule 2.3.1), and so is the
status of each debut's naming consultation (Rule 2.3.4). The template has sections 1 to 7 and the header has no Epigraph line: a title-page epigraph is
never a Chapter field. A Phase's first Area prints the Phase epigraph from Part 30 and, below it,
Section 1's own Epigraph from its Section Spec; the first Area of any other Section prints only
that Section's own Epigraph from its Section Spec (Part 38 Rule 10.3.1).

**Clean body, notes at the end** (Part 38, the Audit and Settlement Notes rule). A Chapter Spec
carries no inline `[SETTLED ...]`, `[OPEN ...]`, `[SKIPPED ...]`, `[FROM ...]` or `[ASKED ...]`
tag and no provenance or audit mark in its body. Every note of the nine kinds of Part 38 Rule 9.10.2
(Settled, Skipped, Open, Deferred, From, Inherited, Name, Variance, Audit)
is collected in one final section, **Audit and Settlement Notes**, at the end of the file, a plain list, never a table, each
note pointing to the plan item it concerns (by Area block and field, or by header line). The
file reads start to finish as plan text. `/next-area` and `/chapter-spec complete` find Open and Deferred
notes in that section.

**Governing after the confirm.** After `[CONFIRM SPEC]` this Chapter header governs the writing
and Gate 1; the Novel-Part Spec entry stays the plan baseline (Part 38 Rule 9.3.2). A **departure**
flows back up the chain only for what the entry fixes: purpose, calendar window,
threads in and out, who is on the page, key events, reveals owed, opening hook, closing beat
(Rule 9.3.3). Splitting, merging, re-shaping or renaming Areas is this spec's own business and
is never a departure. Each departure is also recorded as a variance note in the Audit and
Settlement Notes of every spec above this one, the Section Spec first and then the Novel-Part Spec, written top-down in one step at
the confirm; a note is light and changes no plan content, and the author chooses, per departure,
whether the plan is amended or the original stays the plan baseline (Part 38 Rule 9.4.5; Steps 3 and 4).

A confirmed spec is a valid decision input with settling power: items the author settled
at spec time are **not re-asked** at Area-writing time (DCG Rule 19.4 via Part 38), and that
includes each Area's pacing and size, the Chapter's Build mode, pacing and word budget, each Area's Budget stretch and the Scene Map, which the spec decides for every Chapter. Always still
asked at Area-writing time regardless: the spec's Open and Deferred notes (including every
deferral the author made to the Area writing), newly-surfaced branches, and anything that would
reduce clarity. A spec
never establishes canon facts — names and events in it are proposals until a Gate 1 delivery that is confirmed and
written, or a Gate 2 write. Precedence: Locked Canon > ledger (established) > spec chain (intent) >
session-log; the ledger supersedes the spec. Inside the chain, for what each level must do:
Section Spec > Novel-Part Spec > Chapter Spec, and the lower spec governs its own detail; a
conflict found while building a lower spec is a question to the author, never a silent pick,
and the author's answer is noted as a variance on every spec above (Steps 3 and 4); where the
author amends the plan, the higher spec is changed through its own command (Part 38 Rule 9.4.1).

**What the per-Area agents read.** area-maker, area-scorer, both Gate 1 checker instances and
the outline-planner when it plans a single Area
read this Chapter Spec in full plus the header block and the closing-state block of its
Novel-Part Spec; they do not read the Section Spec (Part 38 Rule 9.9.2). That is why this spec carries
every inherited item, noted with its source. The BUILD agents read the whole chain above this
level in full (see Preconditions).

## Preconditions

- Read `.claude/guardrails/ledger/guardrail-story-spec-law.md` and
  `.claude/guardrails/commands/guardrail-plan-then-auto-execution.md` — this command is
  one of the Plan Mode → Auto Mode in-scope commands (consultation rounds are its Plan
  Mode; default model/effort, mandatory parallelism, and milestone progress reports
  apply end to end).
- `spec-story-specification-law` is the primary skill read (consolidated-first per
  `guardrails/authority/guardrail-consolidated-skill-reading.md`).
- **The chain is in force (Part 38 Rule 9.1.1).** `build` and `revise` run only while this
  Chapter's Novel-Part Spec AND its Section Spec are `CONFIRMED` or `COMPLETED`. The command
  reads both Spec Status lines (and registry rows) top-down, Section Spec first, and stops at
  the first link that is missing or not in force. A parent that does not exist, or is `DRAFT`
  (saved by a `[SKIP SPEC]`), `AMENDED-PENDING-RECONFIRM` or `RETIRED`, refuses the build, and
  the refusal names the command that fixes it: `/section-spec` for the Section Spec, `/part-spec`
  for the Novel-Part Spec (a `DRAFT` or `AMENDED-PENDING-RECONFIRM` parent is brought back to
  `CONFIRMED` by running that command again; a `RETIRED` one is replaced only if the author
  decides so there). A `[SKIP SPEC]` on any level stops the chain at that level. `show` needs no
  chain check. `complete` needs only the Chapter Spec itself to be `CONFIRMED` or `COMPLETED`.
  A retro-fit Chapter build obeys the same rule: the Section and Novel-Part Specs are built
  first (their own retro-fit builds, Part 38 Rule 9.8.2).
- **The Chapter has an entry (Rule 9.1.2).** The Novel-Part Spec must carry an entry for this
  Chapter. If it does not (the story needed one more Chapter than the Novel-Part Spec listed),
  see "When the Chapter has no entry" below. Never build a Chapter Spec on an entry that is not
  there.
- **Reads (Part 38 Rule 9.9.2).** The planner and the checker read the whole Section Spec and the whole
  Novel-Part Spec in full, not only the Chapter's entry; this command reads the same two specs
  to pre-fill the header.
- Spec files are story-memory files written with ordinary Write/Edit — the
  authorized-scripts law (`guardrails/tools/guardrail-authorized-scripts-only.md`) covers
  only novel output files and does not apply to Section, Novel-Part or Chapter Specs.
- **Named items, naming and cost.** Named items are written in italic, naming is never presented
  as a cost, and an item met in the consultation enters no register row until its Gate 2: follow Part 38 Rule 9.9.4 and Part 28 Rules 20.8.2, 20.8.7 and 20.9. Where an option could
  name or leave unnamed, the named version is the `(Recommended)` one. A named item the Chapter Spec
  introduces is an in-world name recorded as a Name note, `proposed`, which becomes `locked-at-Gate-2 (ref)` when its Area is written (Part 38 Rule 1.3.2).
- **Monsters (Part 40).** A monster the Chapter plans is a Kind
  and, where it has a name, an Individual; its name is set in roman and is recorded as a Name note, `proposed` (Part 38 Rule
  1.3.2). If the Chapter plans the beasts that Part 30 plans for Phase 1 (the forest monsters, the airship
  attackers), this Chapter Spec is where their Kind is defined and named ("Define during chapter-spec", Part
  40 Rule 40.7.5.1), inside Part 30's bands, as wild pressure and never an opposing force. **Standing
  exclusion: no sentient monster, and no allusion to one, in any Phase 1 spec item (Law P30-L9), save the one narrow artifact-made exception of Canon Amendment 2026-10-19 (Law P30-L9).** Ask the
  author, never decide, where a plan would bring a Tier C or D monster to a trigger of Part 40 Rule 40.6.2.2.

### When the Chapter has no entry

Stop before any consultation about the Chapter itself and say which Novel-Part Spec lacks the
entry ("Novel-Part Spec 1.2.3 has no entry for Chapter 004"). When the Chapter asked for would
come after the last entry the Novel-Part Spec has, the command does not decide what that means:
it asks the author whether the Novel-Part has finished (the next step is `/next-part`) or the
story needs one more Chapter, because a Novel-Part ends where the story ends it (Part 38 Rule 9.1.2;
Part 38 Rule 1.5.1). If the story needs one more Chapter, offer, through `AskUserQuestion`, to
add the entry as a **light amendment** of that Novel-Part Spec (Rule 11.5.2), or `/part-spec
revise` for a larger change. The entry round asks the Chapter's purpose, its calendar window
(inside the Novel-Part window), its threads in and out, who is on the page (all eight
protagonists accounted for), its key events, its opening hook and its closing beat, and asks the
remaining entry fields (reveals owed, one-line Area outline, linked setup keys) the same way, each
with 2 to 3 concrete options plus `SKIP — let AI decide`, with the entries before and after it
shown so it fits; the author may defer any of them to the Chapter Spec. The continuity-checker
makes a light audit of the new entry and what it touches (its window inside the Novel-Part
window, all eight protagonists accounted for, threads in matching the entry before it). The entry
then goes to the author with its own `[CONFIRM SPEC]` / `[REVISE SPEC]` / `[SKIP SPEC]` prompt,
which names "Novel-Part Spec 1.2.3, new entry for Chapter 1.2.3.004". It is written at that
confirm (Part 38 Rule 9.4.4), top-down in one step: first the variance note on the Section Spec for the
added Chapter (Rule 11.4.3, a light note under Rule 9.4.5), then the entry in the Novel-Part Spec,
each with its registry row (Last Updated; the Novel-Part row's Coverage cell is refreshed, Rule
1.2.2). Only after that confirm does the Chapter build begin, from the new entry; the two prompts
are never open together. If the author declines or skips, no Chapter Spec is built and the
Chapter stays blocked for writing (Part 38 Rule 9.1.1).

## Plan Mode → Auto Mode

For `build` and `revise`, Step 0 (grounding + iterative consultation, ending in the final
sweep and the author's "nothing further to steer" answer) is this command's
**Plan Mode**: every genuine open branch at the Chapter's own level is asked and resolved
(answered, or explicitly skipped, or deferred by the author) across as many `AskUserQuestion` rounds as it takes
(the Exhaustive Clarity Mandate, Rule 38.13). Steps 1–2 then run in **Auto Mode** with no
further discretionary questions — but Auto Mode never waives a mandatory stop: the Step 3
`[CONFIRM SPEC]` token is a hard pause exactly as Gate 1's `[CONFIRM WRITE]` is in
`/next-area`. `show` is read-only and has no Plan Mode boundary; `complete` consults on
unresolved Open and Deferred notes in the Audit and Settlement Notes and asks one confirmation before it writes COMPLETED.

## Parallel orchestration

Per `guardrails/commands/guardrail-plan-then-auto-execution.md` (absolute binding, not a
convenience to weigh):

- **Command start:** launch together (a) **outline-planner** as a background agent at the same
  moment the first consultation round is presented, instructing it to ground on: the
  guardrails (including `ledger/guardrail-story-spec-law.md`), `spec-story-specification-law`,
  the Part 30 / Part 2 / Part 28 consolidated skills, all relevant
  `.claude/story-memory/ledger-*/` entries, the Chapter's existing Areas (retro-fit and
  revise cases), the CDL-2 Section running aggregate and, for every build, the whole Section
  Spec and the whole Novel-Part Spec of the Chapter — and to report open branch
  points it finds, *not* to finalize the spec; (b) for `complete`, **area-scorer** for the
  Chapter-Level aggregate (see `complete`); and (c) one **continuity-checker** background
  pre-read for its grounding reads (Locked Canon, Entity Naming Law, Part 30 locks and Section
  mandates, current bracket state, the two parent specs) that serves the final sweep and the
  Step 2 audit. Author answers are fed back to the planner via `SendMessage`; any new branches
  the planner surfaces feed further consultation rounds.
- **Step 2 ∥ draft:** while outline-planner finalizes the draft spec, the checker's pre-read
  continues; send it the drafted spec via `SendMessage` when it lands.
- **Inside a chain run** (`/start-story`, `/next-section`, `/next-part`, `/next-chapter`) the
  calling command owns the order across levels: consultation runs strictly top-down, so this
  build's consultation begins only after the Novel-Part Spec's `[CONFIRM SPEC]`; the Chapter
  planner, grounded from the start, is told by `SendMessage` that its parent is confirmed and
  finalizes (Part 38 Rule 9.9.3). Only one confirm prompt is open at a time in a chain.

Never parallelized: consultation answers precede the finalized draft; the final sweep precedes
the "nothing further to steer" question; the Step 2 audit precedes presentation; the author's
`[CONFIRM SPEC]` or `[SKIP SPEC]` precedes any file write.

## Sequence (build / revise)

0. **Plan Mode — grounding + iterative consultation.** Launch the outline-planner
   grounding (see above) in parallel with the first `AskUserQuestion` round. Consultation
   is exhaustive-clarity and iterative: multiple rounds — not one — until the done test below is met, covering the
   Chapter's direction (its opening beat and shape inside the Novel-Part entry; the themes were asked at the Section and
   Novel-Part builds and are not asked again), Area breakdown (started from the entry's one-line Area outline), each Area's scene anchors,
   pacing and size (the Area-block consultation below), per-Area beats/POV, each Area's Behavioral Plan
   (any question it needs is asked here, Part 39 Rule 39.46.2.5), entity debuts, outcome
   forks, and bracket-range intent. **Collective and location codes (Part 39 Rule 39.23.1.5):** for each
   collective whose members, or location where two or more named people, appear together in an Area block,
   the planner reads the Collective Behavior Code block in the ledger (Part 39 Area 41.4). `Registered` or
   `None, by the author's ruling` is cited in the block's Behavioral Plan. `Not yet registered`, a stub or
   no ledger entry is recorded as a blocking Open note, the planner proposes a short code from cited ledger
   facts (or recommends none for an incidental crew), and the author confirms, changes or rules none here;
   a new entity is always asked. The confirmed answer is a Settled note. The spec writes no ledger: the
   continuity-checker writes the confirmed block into the entity's ledger file before drafting
   (`/create-chapter` or `/next-area` Step 0). Direction options carry Part 36
   Area 13 thematic previews (`narration-novel-thematic-law`).
   MAJOR-entity names and Hero/Villain address-register gaps route through consultation
   per Part 28 Area 20.4 — never AI-assumed. Never ask about anything already settled by
   the Canon, or by a settled item of the Section Spec or the Novel-Part Spec: those are carried in
   as notes with their source, and are not re-asked (Rule 9.5.1). The carve-outs of Rule 9.5.3 still
   hold: Area pacing and Area size are never settled above the Chapter Spec (they are decided here; the Novel-Part Spec's Chapter pacing and word budget are guides this spec settles in its header); tone, voice, sensory and
   content tags stay at the Area; Part 36 Autonomous Matters are never fixed above the Area; a
   genuinely new branch is asked; and an inherited answer whose clarity has reduced (Part 38 Rule 4.2.4)
   is asked again with the original answer and the source of the change shown. An inherited item the
   author deferred to this spec (a Deferred note in a higher spec naming the Chapter Spec) is asked in
   this build.
   The header values pre-filled from the entry are shown for the author to edit, each as the
   `(Recommended)` option where a question is put (Part 38 Rule 9.6.3); a pre-filled value the author leaves
   alone stays noted as taken from the entry and gains settling power only if the author
   answers it explicitly in this build (Rules 9.3.1 and 4.1.1).
   The planner never leaves an item open on its own, and never defers one: every branch at the
   Chapter's own level is asked. Only the author may defer ("handle it in the writing"; a Chapter
   Spec defers to the Area writing only), and that is recorded as a Deferred note (Deferred to: the
   Area writing, with the date) in the Audit and Settlement Notes.
   A deferral to the Area writing is asked at that Area's Decision Consultation Gate like any
   open note (Part 38 Rule 4.2.2); the drafter never settles it silently. A question the author
   answers with `SKIP — let AI decide` is recorded as a Skipped note (planner chose X, with the date)
   and settles nothing (Rules 9.5.2 and 9.6.4). Scene anchors, Continuation, Pacing and Size target
   may not be left open at `[CONFIRM SPEC]`: a SKIP on one of these four records the planner's pick, never a
   blank, and a deferral of them is not offered (Rule 2.4.2). *Amended 2026-10-07:* the same holds
   for the Build mode, the Chapter pacing, the Chapter size target, each Budget stretch and the
   Scene Map's assignment of every Area block to a scene.
   **Chapter-level consultation: Build mode, Chapter pacing and Chapter word budget (Part 38 Rules
   2.3.8 and 2.3.9, Amended 2026-10-07).** Asked before the Area blocks, in the same style (2 to 3
   concrete options with previews, plus `SKIP — let AI decide`, up to four questions per
   `AskUserQuestion` call): (a) *Build mode* — "How should this Chapter be written?" Options are
   `whole` (`/create-chapter` writes the whole Chapter in one cycle, no Area files; the
   `(Recommended)` default) and `by-area` (`/next-area` writes it one Area at a time and
   `/chapter-builder` condenses it); a SKIP records `whole`. (b) *Chapter pacing* — "How should the
   Chapter as a whole move?" Options are Fast, Medium and Slow with the planner's `(Recommended)`
   pick and its one-line reason, and the guidance stated in the question: fights are usually Fast,
   intrigue, deception, lore and thought are usually Slow, dialogue is usually Medium, and it is
   always the author's call because it depends on the story. The Chapter's value from the
   Novel-Part Spec entry (if set) is shown as the pre-filled `(Recommended)` option. (c) *Chapter word
   budget* — "How many words should the Chapter be written to?" The default offered is the sum of
   the Area size targets (settled in the Area questions below), with a plain chance to **raise**
   it ("raise it" is always an option, the new figure typed under "Other", no reason asked); a
   raised figure is carried into the Area size targets, and the planner asks which Areas take the
   rise. The planner states once, in the question, what the figure means for a `whole` Chapter:
   the Chapter is written at 55 to 60 percent of each Area's target and 0.55 to 0.72 of the Chapter
   total (Rule 2.3.10), and that pacing and size are the author's decision, recorded in the spec.
   Chapter pacing and the Chapter word budget are written to the header block; the Build mode too.
   **Area-block consultation (Part 38 Rules 2.4.1–2.4.11 and 3.2.4).** Everything about how an
   Area is written is captured here, never at writing time. No question asks for a word-count cut. An Area
   is the written unit, a complete scene or
   one stretch of a scene that continues across consecutive Areas; the planner proposes the beat boundary where a scene runs on and the author
   confirms it, under the Area-to-Area carry-over
   rule, Part 2 Rule P2-Area-6 (an Area that continues the previous one opens in motion from the exact state the previous
   Area left, and an Area that continues a scene ends on live tension). For each Area, in chapter
   order, outline-planner proposes and the author settles, up to four questions per `AskUserQuestion`
   call, each option with its Part 36 preview and `SKIP — let AI decide` always offered:
   1. *Anchors* — "What should this Area be built around?" Options are 2 to 3 concrete scene-anchor
      plans built from the entry's one-line Area outline (plus SKIP, four options in all, the tool
      maximum), each stating whether the Area is a complete scene or one stretch of a scene that
      continues in the next Area, and the reason (the depth and immersion the beat needs). The
      The planner proposes the Area's single Viewpoint with the anchors (Part 38 Rule 3.2.4); a change of viewpoint is planned as the next Area's Viewpoint field, never inside one Area. The answer settles the Area's anchors, its beat and its Viewpoint.
   2. *Opening* — "How should this Area open?" Options are the 2 to 3 opening types that fit
      the scene, with SKIP making four options, the tool maximum (the fixed list is continues directly / time jump / cut to another thread /
      flashback, memory, dream or vision / in medias res / quiet opening; a word given through
      "Other" is shown with the nearest listed type for the author to confirm and is kept in the detail, Part 38
      Rule 2.4.3), with the previous Area's opening and closing type shown
      beside them so the variety rule is visible; a repeat of the previous Area's type needs
      the author's reason (`repeat on purpose`). The first Area of the story has no Area
      before it, so only in medias res, quiet opening and flashback, memory, dream or vision
      are offered (Part 38 Rule 2.4.4). When the type is flashback,
      memory, dream or vision, one follow-up question asks the source: the character's own
      mind (Part 26), a cultivation ability the canon gives (such as the Dream affinity, Part 4
      Area 1.3), or a channel Part 24 defines (Part 36 Rule 27.3.1); the answer is kept in the
      detail beside the type. The planner proposes every other detail the type needs (how long
      a time jump, which thread or place a cut goes to, which past moment a flashback or memory
      returns to) and shows them at Step 3 for the author to edit (Part 38 Rule 2.4.3).
   3. *Closing* — "How should this Area end?" Options are the 2 to 3 closing types that fit the
      scene, with SKIP making four options, the tool maximum (the fixed list is cliffhanger / turn or reveal / resolved / quiet landing /
      question left open; a word given through "Other" is shown with the nearest listed type for the author to
      confirm and is kept in the detail, Part 38 Rule 2.4.3). A cliffhanger or an
      open question is followed by "Where is it resolved?" (an Area reference or, only if the
      author chooses to defer it, a Deferred note in the Audit and Settlement Notes), and a cut away
      by "Where does the interrupted thread resume?". An Area that continues a scene into the next
      Area is closed on live tension (a cliffhanger, a turn or reveal, or a question left open).
   4. *Only when the scene has them* — a brief time skip
      inside the Area, a reveal or mystery with a Reader-Reveal Timing deadline, a cut-back
      to an earlier thread, a fight (the optional Fight line, Part 38 Rule 2.4.10, which also carries the Situation line of Part 45 for a fight: the ground, light, postures, people to protect, intent, energy budget and a menu of moves with the situation each fits, never an order of moves), lore the author owns (if the author does not know it yet, the author may defer it, recorded as a Deferred note).
   5. *Pacing* — "How should this Area move?" Options are Fast, Medium and Slow, with SKIP making
      four options, the tool maximum. The planner marks its pick `(Recommended)` and gives a one-line
      reason from the anchor types of the scene (the Part 2 anchor defaults, Part 38 Rule 2.3.3). The answer
      is the Area's Pacing, which is decided here and carried at writing time: no pacing question is
      asked when the Area is written. Fast, Medium and Slow are the vocabulary the spec records,
      not a rule that sets a size.
   6. *Area size* — "How long should this Area run?" Options are 1,600, 1,800 or 2,000 words
      (the planner marks its pick `(Recommended)` from the scene), with SKIP making four options.
      The passing range at writing is 1,280 to 2,400 words (Part 2 Rule P2-Area-7), so the answer is the target the Area is
      written to. It is asked apart from pacing, and neither answer sets the other (Part 2; Part 38
      Rule 2.4.10). In a `whole` Chapter (Build mode, above) the author may instead name a
      raised or custom figure under "Other", with no reason asked, and the Area is written to the
      word band of Rule 2.3.10 and not to the 1,280 to 2,400 range *(Amended 2026-10-07)*.
      Questions 5 and 6 go in the next `AskUserQuestion` call after the first four,
      since the tool takes four questions to a call.
   7. *Budget stretch* (a `whole` Chapter only; Part 38 Rule 2.3.10, Amended 2026-10-07) — "May this
      Area run longer than the usual band?" Options are `none` (`(Recommended)` unless the scene
      plainly needs more room: the Area is written at 55 to 60 percent of its size target) and
      `up to 0.72 of target` (the author gives a one-line reason, typed under "Other" or chosen
      from the planner's proposed reason, for example a fight turn or a reveal that needs room),
      plus SKIP, which records `none`. The planner states the effect in plain words: only an Area
      that names a stretch may pass 60 percent of its target, never beyond 72 percent, and a
      stretch the spec does not name is refused at the audit. A `by-area` Chapter asks no stretch
      and records `none`. Question 7 goes in the call that carries questions 5 and 6.
   Every other field of the block (Serves [Part 30 Section mandate and protagonist arc, by function name; a Part 30 pillar may be cited by its ID], Change, want, obstacle and stake, Carry-over, Thread, emotional line, world,
   setting and people, ledgers expected to change, setups and payoffs, consequences landing here, novel elements) is
   filled by outline-planner from Part 30, the ledgers, the two parent specs and the Area before it, and shown at
   Step 3 for the author to edit. Each Area's in-story time is filled the same way, as a date (or a range)
   with its Phase Day, inside the Chapter's calendar window (itself dates plus Phase Day, Part 41 Area 4) and on
   or after the last day of the Area before it (Part 41 Areas 5 and 6):
   an Area that opens as `flashback, memory, dream or vision` carries the remembered date or the night
   dreamed, a `time jump` carries its new date, and a `cut to another thread` may step back inside the
   Chapter window; an Area that opens in the last dark hour and runs on into a dawn takes that dawn's day, with
   no range (Part 41 Area 2, the one scoped exception to the dawn-to-dawn day).
   The planner never leaves the in-story time open on its own (Rule 9.6.3); only the author
   defers it. No question is asked about the sensory anchor, tone or voice, or content lines: each reads
   `unset` until the author sets it (Part 38 Rules 2.3.5a, 2.3.5b and 2.3.5d and 4.2.5).
   **Scene Map consultation (Part 38 Rule 2.4.12, Amended 2026-10-07).** Asked after the Area
   blocks are settled, as section 5.0 of the spec, one scene at a time in chapter order, in the same
   style (2 to 3 concrete options with previews, plus `SKIP — let AI decide`, up to four questions
   per call). The planner first proposes how the Area blocks group into scenes, starting from the
   anchors and Continuation answers already given (an Area that runs on into the next is one scene
   with it), and asks: (a) *Which Area blocks form the scene* — the grouping, for example 01-02
   as S1; one scene may span several Area blocks. (b) *The POV sequence* — every viewpoint of the
   scene in order and the Area block or beat where each takes over; any number of viewpoints is
   lawful, and a takeover at a beat inside an Area block makes that block a Dual-POV Area, which
   the author confirms (Part 38 Rule 2.4.7). (c) *The scene arc* — for a fight: the opening, the
   exchanges, the turn and the end; for a conversation: the turns and where the reveal lands;
   otherwise the movement of the scene. (d) *Scene pacing and scene word budget* — the pacing with
   the guidance above, and a budget that defaults to the sum of its Area targets (a raise is
   always offered, and a stretch follows Area question 7). (e) *Does a scene cross a Chapter
   seam* — whether the scene runs in from the previous Chapter or out to the next, in which case
   the Chapter reference is recorded and the scene names its `PS` row of the Novel-Part Spec; and
   (f) *The join state at each Area seam of the scene* — the exact state (position, wounds, who
   knows what, whose floor it is). Then one question settles **the visible-break rule** for each
   scene, with the rule stated plainly in the question: a scene break (`---` in the md, a
   centred `*   *   *` in the docx) shows only when the scene changes or when the same scene moves
   to a different viewpoint; when one scene simply continues across Area blocks with the same
   viewpoint there is no visible break and only the hidden Area marker; a scene whose date differs
   from the scene before it carries its own date line directly after its break. The answer is the
   `Visible break before` column (yes or no), and the planner proposes the answer the rule gives
   as `(Recommended)`. Every Area block belongs to exactly one scene of the map before the spec can
   be confirmed. In a `by-area` Chapter the same questions are asked and the Continuation field of
   each Area block agrees with the map.
   **Hero arc cells (a Deferred note from a higher spec).** When this Chapter is the first Chapter in
   which one of the eight protagonists appears (viewpoint or on the page) and a higher spec carries a Deferred note for that
   hero's five arc cells (Stated Want, Underlying Need, Deepest Fear, Belief That Blocks the Need, and the Part 30 Section 1.5
   arc vector cell), they are asked in this build, one hero at a time, each cell with 2 to 3 options built from Part 30's arc line and the Hero Ledger, plus
   `SKIP — let AI decide`. Each answer is a Settled note against the Protagonist Thread Map row of that hero; Gate 2 carries it to the
   hero's ledger fields (Part 17 and Part 37), so the spec holds the answer and the ledger holds the fact. A SKIP records a Skipped note
   and the cell stays open in the ledger as `OPEN-AREA`.
   **Done test (Part 38 Rule 38.13; Rules 9.6.1 to 9.6.5).** The consultation is finished only
   when all four of these hold, in this order. (1) *No unasked branch at the Chapter's own level.*
   A question belongs here when the author's answer first changes this Chapter's plan. A matter
   the answer would change only the writing of the Area itself (drafting craft,
   Part 36 Autonomous Matters) is not a question of this build, and a matter that first changes the
   Novel-Part's or the Section's plan was asked at that level (when this build's own work makes it
   live again, it is put to the author as a question, never a silent pick, Rule 9.4.1). (2) *A final
   sweep* of the whole assembled draft (outline-planner assembles it from the answers; it is not yet
   shown) by outline-planner and continuity-checker, which looks for conflicts with Part 30, the
   ledgers, the Section Spec and the Novel-Part Spec, and lists again every Skipped note and every
   deferral (the inherited ones too) so the author has a last chance to settle them (Rule 9.6.5).
   If the sweep returns anything new, more rounds follow and then a new sweep. (3) *The author's
   explicit "nothing further to steer"*, asked with one `AskUserQuestion` (the options "Nothing further to steer", "Change one of the skipped or deferred items" and "Steer something else", with no SKIP option, the same as in `/section-spec`) after a sweep that returned
   nothing new. (4) Then Steps 1 to 3 and the confirm token. No score, no percentage and no round
   count is kept: the story decides when the author has nothing further to steer.
1. **outline-planner finalizes the Rich-schema spec** from the assembled draft, which comes from the
   Chapter's entry in the Novel-Part Spec and from the answers of Step 0:
   the chapter header lines (title label, Chapter Purpose, Calendar Window inside the entry's window,
   Threads Carried In and Out, Protagonist Thread Map with all eight protagonists accounted for, opening
   hook and closing beat) pre-filled from the entry, plus the Build mode, the Chapter pacing and the Chapter size target
   from the Chapter-level consultation, the Scene Map (section 5.0) from the Scene Map consultation and a Budget stretch line
   in every Area block (Part 38 Rules 2.3.8 to 2.3.10 and 2.4.12, Amended 2026-10-07), with a note in the Audit and Settlement Notes
   naming the entry (From notes); the items settled in the Section Spec or the Novel-Part Spec carried in as
   Inherited notes; every deferral to the Area writing
   copied in as an Inherited Deferred note (Deferred to: the Area writing, with the date); a line that
   the author's answers moved is shown as changed with the entry's original beside it (a
   departure, see Step 3); then one Area block per Area (the entry's one-line Area outline is the
   starting point: it gives descriptors only and never names an Area, so naming, splitting,
   merging and re-shaping the Areas is this spec's own work, Part 38 Rule 11.3.4), each with its pacing and
   size, plus the chapter-level Tier Scope Bracket ranges, the body being clean plan text and the
   Audit and Settlement Notes section at the end of the file reflecting exactly what the author
   settled versus deferred in Step 0, with a Skipped note (planner chose X, with the date) for every
   item the author skipped (Part 38 Rule 2.3.6), each note pointing to the plan item it concerns
   (retro-fit: written Areas recorded as-built). The planner writes the full
   template of Part 38 Rule 2.2.1, sections 1 to 7 in order: the header block (section 1, with the Calendar Window,
   the Opening hook, the Closing beat, the New named things line and the Protagonist Thread Map), the Tier Scope Bracket ranges (section 2), the Standing
   Exclusions block written out in full (section 3, Rule 2.3.7), the P30-L5 crisis-density row (section 4; at Chapter 001 the rolling
   window reads "no earlier Chapter"), the Area blocks (section 5), the Completion Record stub "not yet written" (section 6) and the
   Audit and Settlement Notes (section 7). There is no Epigraph line: the title-page epigraph comes from
   the Section Spec, and for a Phase's first Area also from Part 30 (the Phase line, printed above
   Section 1's own; Part 38 Rule 10.3.1), and no agent ever writes epigraph text.
2. **Light continuity-checker spec audit** — report-only, writes nothing: Locked-Canon
   conflict scan; P30-L8 forbidden entities + P30-L9 (no sentient monster in Phase 1, save the one narrow artifact-made exception of Canon Amendment 2026-10-19 (Law P30-L9)) + no-Sapphire-Line; Entity Naming Law flags
   (`guardrails/quality/guardrail-entity-naming-law.md`); all seven template sections present, including the Standing Exclusions block and the P30-L5 row; the Behavioral Plan (an
   acting character without a tier-compliant registration is a blocking finding; a Tier D character planned to speak is not; one planned to act
   consequentially is flagged to the author, who rules: Part 38 Rule 38.2.2a.1 and Part 39 Rule 39.46.2.3); Part 30 Section-mandate
   coverage; established ledger state (threads in match the prior chapter's close; entities on
   the page exist or are debuts); schema conformance; Tier Scope Bracket range sanity; Area-block connection (Part 38 Rule 3.3.2(f):
   required fields, scene anchors, pacing and size (1,600, 1,800 or 2,000, or the raised or custom figure of a `whole` Chapter) present; Build mode, Chapter pacing, Chapter size target (equal to the sum of the Area targets), every Budget stretch and a Scene Map that assigns every Area block to exactly one scene present (Amended 2026-10-07); every gap between Areas
   accounted for by an opening type; every Area that continues a scene carries the Area-to-Area
   carry-over (opens in motion from the exact state the previous Area left, and ends on live
   tension); no unmarked repeat of an opening type; cliffhangers and
   cut-aways resolved or returned; each Area's single Viewpoint recorded and time skips listed; cross-references
   resolve; every element name in the Part 36 element lookup table; the body free of inline tags and
   every note in the Audit and Settlement Notes well formed and pointing to a plan item); and (g)
   derivation (Rule 3.3.2(g); Rules 9.3.2, 9.3.3 and, for the nesting, 9.3.1): every header field
   agrees with its entry in the Novel-Part Spec or is noted as a departure, every inherited item
   still carries its note, and the Chapter's calendar window sits inside the Novel-Part window, which
   sits inside the Section window. Each window and each
   Area's in-story time also reads as dates plus Phase Day that agree by the conversion of Part 41 Area 4,
   and the Area dates follow the dating rules of Part 41 Area 6 (a mismatch is a finding for the planner to
   correct before `[CONFIRM SPEC]`).
   On any FAIL finding: revise via
   outline-planner and re-audit before presenting — never present a spec with a FAIL
   outstanding. A Chapter that cannot sit inside its Novel-Part's own purpose, closing state, calendar
   window or reveals owed is a conflict with the parent: this command never changes those (a
   substantial change of the Novel-Part Spec, Part 38 Rule 9.4.2); the author is asked, and the change goes through
   `/part-spec revise` (or `/section-spec revise`, where it is the Section Spec's own plan that would
   move).
3. **Present the spec + audit summary** (with the chapter's run of opening and closing
   types laid side by side) **and the departures**: each header line that differs from what the
   Novel-Part entry fixes (purpose, calendar window, threads in and out, who is on the page, key
   events, reveals owed, opening hook, closing beat), with the entry's original beside it, and says
   that a variance note for each will be left on every spec above this Chapter, the Novel-Part Spec
   and the Section Spec (Part 38 Rule 9.4.5). For each departure the author says, with `AskUserQuestion`,
   whether to **amend the plan too** (the Novel-Part entry, with the planner's proposed wording of
   the amended entry shown beside the question) or **leave the original as the plan baseline**; both
   answers are lawful, the notes are left either way, and this question is part of the confirm
   step, not a new round of consultation. Then wait for an explicit `[CONFIRM SPEC]` /
   `[REVISE SPEC]` / `[SKIP SPEC]` — never assume confirmation. The prompt names the artifact and
   its reference ("Chapter Spec 1.2.3.004"), and the `[CONFIRM SPEC]` is not accepted if a parent has gone
   out of force since the build began (Part 38 Rule 9.1.1). `[REVISE SPEC]` loops back
   through Steps 0–2 (consultation and the final sweep scoped to what changed).
4. **On `[CONFIRM SPEC]`:** this command (the orchestrator, never outline-planner) writes with
   ordinary Write/Edit (the authorized-scripts law does not apply to spec files), top-down in one
   write step. First, for each departure, one traced variance note is appended to the Section Spec,
   then the same note to the Novel-Part Spec (a light, appended note that changes no plan content,
   Part 38 Rule 9.4.5; each gives the date, the trigger, what differs and the author's answer for that
   departure), with the registry row of each spec moved to the new Last Updated date. Then the Chapter
   Spec file is written and this Chapter's row in the Chapter Specs table of
   `phase-section-part-chapter-area-specs/_index.md` is updated (Spec File / Ref / Status /
   Spec Ver / Last Updated / Coverage; Coverage reads "Areas written / planned"). With no departure nothing is written above the Chapter. The command changes nothing else
   in the Novel-Part Spec or the Section Spec: where the author said "amend the plan too", the entry
   is changed by the Novel-Part Spec's own command (Part 38 Rule 9.4.3), `/part-spec revise` — a light
   amendment when it touches only that entry, a substantial one when it would move the Novel-Part's
   own purpose, calendar window, reveals owed or closing state (Rule 11.7.2) — and where the
   departure also moves something the Section Spec fixes for this Novel-Part, the Section Spec is
   changed by `/section-spec revise` (Rule 9.4.2). This command offers to run the `/part-spec revise`
   straight after the write, starting from the wording shown at Step 3. The Chapter Spec stands as
   confirmed either way (Part 38 Rule 9.3.2). When
   `/next-chapter`, `/next-part`, `/next-section` or `/next-phase` runs this
   build, the completion of the outgoing specs is written in this same write step, bottom-up (Chapter,
   then Novel-Part, then Section, Rule 9.4.4), and the Coverage cells of the Novel-Part and Section
   rows are refreshed in that step as a completion write (Rule 1.2.2). **On `[SKIP SPEC]`:** it writes the drafted spec the same
   way with Spec Status `DRAFT` (for `revise`, `AMENDED-PENDING-RECONFIRM`, Part 38 Rule 3.5.2),
   sets the registry row Status to `DRAFT`, and notes the skip in the spec's Audit and Settlement Notes
   (Part 38 Rule 3.4.1). Nothing is written to the Novel-Part Spec or the Section Spec, and no
   outgoing spec is completed. A DRAFT spec has no settling power, the chain stops at this level, and
   the Chapter stays blocked for `/next-area` and every other Area-writing command until
   `[CONFIRM SPEC]`.
5. **Log the outcome to `.claude/story-memory/session-log/`** — this command writes the line:
   mode, the artifact and its reference (for example "Chapter Spec 1.2.3.004"), confirmation token,
   any departures and what the author chose for each, and any Open or Deferred notes the author
   deliberately left in the Audit and Settlement Notes.

### `show`

Read the spec file and its registry row and render them for the author, with its chain beside
it (the Spec Status of its Novel-Part Spec and Section Spec, and its entry in the Novel-Part
Spec) — read-only; no consultation, no audit, no writes. For the in-story dates of a Section or the
open setups across all Chapters, use `/timeline` and `/threads`.

### `complete`

Part 38 Rule 3.7.1 and Rule 9.7.2. A Chapter Spec is completed, never closed: it stays a living
record, and `revise` keeps working on it any time. Verify every Area block carries a terminal
status (`WRITTEN`, or `DROPPED` with an audit note); surface any unresolved
Open or Deferred note in the Audit and Settlement Notes, any setup planted with no payoff and any unresolved cliffhanger via
`AskUserQuestion` (resolve it, carry it forward to the next Chapter's spec, or mark it lapsed with a
one-line reason; an item is marked lapsed only on the author's answer). At the start of `complete`, launch **area-scorer** in the background for
the Chapter-Level CDL-2 Aggregate Block of the Chapter being completed
(`narration-content-density-law` section 4.2) and show it with the completion question; it is
information only and never blocks the completion. Then ask the author to confirm with `AskUserQuestion` ("Complete this
Chapter's spec?", with "Complete it (Recommended)" and "Not yet"), saying that completing locks
nothing: `/chapter-spec revise` still works on the spec afterwards. On "Not yet" nothing is
written. On a yes, write the final variance summary (planned vs. as-written, per Part 38), the
Reader now knows line (a short list, by reference code, of what the reader has been shown;
it seeds the next spec's Carry-over) and the Chapter digest (the text `/chapter-summary` prints
for the Chapter, Part 38 Rule 3.7.1) into the spec; complete the Chapter Header Block's New named
things line; set the status to `COMPLETED` (the Gate 2 sync already sets it when the last Area block
is written, Part 38 Rule 3.6.1 item 1, so this step sets it only if it is not yet set) and update the
registry row, then refresh the Coverage cells of its Novel-Part row and Section row, because a
child's completion is a completion write step (Rule 1.2.2; never done at Gate 2); log to
session-log. When a `COMPLETED` spec is revised later, these pieces are refreshed for what the
revision changed.

When `/next-chapter`, `/next-part`, `/next-section` or `/next-phase` runs `complete` ahead of
building the next Chapter's spec, `complete` does everything above except the write: a yes means
"complete it when the new Chapter's spec is confirmed", and the write is made at that
`[CONFIRM SPEC]`, in the same write step as the new spec (at a Novel-Part or Section boundary that step
also carries the completion of the outgoing Novel-Part Spec and Section Spec, bottom-up — Chapter, then
Novel-Part, then Section — which `/next-part` and `/next-section` own, Part 38 Rules 9.4.4 and 9.7.3). A
`[SKIP SPEC]` at any level writes no completion at all, and the command is run again. Run alone,
`complete` writes at once. `/next-chapter` never advances unless the prior Chapter's spec is
`COMPLETED`.

## Failure/abort

`[SKIP SPEC]` defers confirmation and keeps the work: the drafted spec is written with
Spec Status `DRAFT`, the registry row says `DRAFT`, and the skip is noted in the spec's
Audit and Settlement Notes (Part 38 Rule 3.4.1). The skip stops the chain at this level, and the Chapter stays
blocked for `/next-area` until `[CONFIRM SPEC]`. A parent link that is missing, `DRAFT`,
`AMENDED-PENDING-RECONFIRM` or `RETIRED` stops the build before any consultation and names the
command to run (`/section-spec` or `/part-spec`); a Chapter with no entry in its Novel-Part Spec
stops at the entry offer above. Irreconcilable conflicts (author intent vs. Locked
Canon, spec intent vs. an established ledger fact, or the Chapter's plan vs. its Novel-Part Spec or
Section Spec) are escalated via `AskUserQuestion`, never force-written and never silently
reconciled; the author's answer is noted as a variance on every spec above, the Section Spec first
(Step 4), and a change to a higher spec's own plan is made by that spec's own command,
`/part-spec revise` or `/section-spec revise` (Part 38 Rules 9.4.1 to 9.4.3).
`revise` is never refused for a `COMPLETED` spec. When `/redraft-chapter` or `/redraft-area` calls
`revise`, that command has already asked the author (its Step 1): a revise that changes no plan
content (a redraft that executes the existing plan) returns the spec to `CONFIRMED` at once, with one
variance line; a revise that changes plan content reads `AMENDED-PENDING-RECONFIRM` until
`[CONFIRM SPEC]` and `CONFIRMED` afterwards; the Gate 2 sync sets `COMPLETED` when the last Area block
is written again (Part 38 Rule 3.6.1 item 1).
A correction of record (no plan change, no change to any Area text) is written as a light annotation with a
variance note and needs no redraft (Rules 3.5.2 and 6.1.1(a)).
