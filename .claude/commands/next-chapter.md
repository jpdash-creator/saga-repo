---
description: Advance to the next Chapter within the current Novel-Part (Area numbering resets within it) -- complete the closing Chapter's spec, build the new Chapter Spec from its Novel-Part Spec entry, then write the new Chapter whole with /create-chapter (or its opening Area with /next-area when asked or when the Build mode is by-area).
user-invocable: true
---

# `/next-chapter`

Corresponds to canon command `[NEXT CHAPTER]` (C-6). A new Chapter is the last link of the
**spec chain** (Part 38 Rule 38.9, Area 9): its Chapter Spec is built from its own **entry in the
Novel-Part Spec** of the current Novel-Part (Rule 9.1.2), which stands under the Section Spec. This
command builds that one link; the Section Spec and the Novel-Part Spec above it must already be in
force, and it builds neither of them (the one addition, a missing Chapter entry, is step 0 and has
its own confirm).

## Preconditions

- Read `.claude/guardrails/commands/guardrail-plan-then-auto-execution.md` — it governs this
  command's Plan Mode → Auto Mode shape, default agent model/effort, mandatory parallelism,
  and milestone progress reporting, exactly as it governs the `/next-area` call this
  command delegates to.
- Read `.claude/guardrails/ledger/guardrail-story-spec-law.md` and `spec-story-specification-law`
  (Part 38 Areas 9 and 11): the chain rule (Rule 9.1.1), the entry rule (Rule 9.1.2) and
  Chapter completion (Rule 9.7.2).
- **The chain is in force.** The current Chapter's Novel-Part Spec AND its Section Spec must be
  `CONFIRMED` or `COMPLETED`. Read both, Section Spec first, and stop at the first link that
  is missing, `DRAFT`, `AMENDED-PENDING-RECONFIRM` or `RETIRED`, naming the command that fixes
  it (`/section-spec` or `/part-spec`).

## Plan Mode → Auto Mode

Steps 0 to 3 are this command's **Plan Mode**. It checks the chain and the Chapter's entry (step 0,
with that entry's own confirm when one has to be added), confirms every Area of the current Chapter
is terminal (`WRITTEN`, or `DROPPED` with a variance note), prepares the completion of the current
Chapter's spec with its final variance summary (the `/chapter-spec` **complete** flow: its checks,
its questions and its confirmation, with nothing written yet), and then builds the next Chapter's
spec via the `/chapter-spec` **build** flow — full iterative author consultation, ending in the
final sweep and an explicit `[CONFIRM SPEC]` — before any Area is planned or drafted. The
completion is written on that `[CONFIRM SPEC]`, in the same write step as the new spec (step 3). The
prompt names the artifact and its reference ("Chapter Spec 1.2.3.004"). Once the new Chapter's spec
is confirmed, **Auto Mode** begins: step 4 proceeds straight into `/create-chapter` by default (or
`/next-area` when the author asks or the Build mode is `by-area`), which runs its own
full Plan Mode → Auto Mode cycle (Decision Consultation Gate through Gate 2 confirmation)
independently and in full — this command neither shortens nor restates it (its consultation is
spec-scoped: items the author settled in the Chapter Spec, and the settled items of the Section
Spec and Novel-Part Spec carried into it, are not re-asked, per DCG Rule 19.4 via Part 38; Rules
9.5.1 and 9.5.2). Step 4 depends on step 3's confirmation, so those steps are sequential — the
mandatory-parallelism binding applies inside the delegated `/next-area` call, as documented there.

## Parallel orchestration

Per `guardrails/commands/guardrail-plan-then-auto-execution.md` (absolute binding; Part 38 Rule 9.9.3).
Once step 0 passes, launch together in one message: (a) **outline-planner** for the closure
check and the completion preparation (step 1); (b) **area-scorer** for the Chapter-Level CDL-2
Aggregate Block of the closing Chapter (`narration-content-density-law` section 4.2), shown
before the new spec is built (information only, blocks nothing); (c) the grounding of the
**Chapter Spec build** (outline-planner, reading the whole Section Spec and the whole
Novel-Part Spec, told to report open branch points, *not* to finalize); and (d) one
**continuity-checker** pre-read that serves the final sweep and the light audit. Question
streams stay separate: the questions of the completion flow and the consultation of the build
never share one `AskUserQuestion` call.

## Sequence

0. **Chain and entry check** (reads only, apart from the entry added under (a) below; nothing
   else is launched until it passes). First the chain of Preconditions. Then find the next
   Chapter's **entry in the current Novel-Part Spec** (the next one in its Chapter list after the
   current Chapter; Part 38 Rule 11.3.2). If the entry is there, go on to step 1. If the
   Novel-Part Spec has no further Chapter entry, stop before anything is written and ask the
   author, through `AskUserQuestion`, which way to go: (a) the story needs one more Chapter here,
   so add the entry as a light amendment (the short entry round of `/chapter-spec`, "When the
   Chapter has no entry", Rule 11.5.2: purpose, calendar window, threads, who is on the page, key
   events, hook and closing beat; the entry has its own `[CONFIRM SPEC]` prompt and is written at
   that confirm, before the Chapter build begins, as `/chapter-spec` sets out), (b) this
   Novel-Part has finished, so run `/next-part`, or (c) the Novel-Part's plan needs re-thinking,
   so run `/part-spec revise`. outline-planner marks its pick `(Recommended)` with a one-line
   reason from the Novel-Part Spec's closing state and the closing Chapter's last beat; the
   author's word decides. On (b) or (c) nothing is written and the command stops with the named
   command. On (a), this is the answer to the offer in `/chapter-spec`; it is not asked a second
   time. The entry round and its own confirm come first and finish before anything below is
   launched; the entry is the one thing written before the new Chapter's confirm, and the
   outgoing Chapter's completion and everything else wait for that later confirm. If the author
   declines or skips the entry's confirm, the command stops with no Chapter Spec built.
1. Invoke **outline-planner** to confirm every Area of the current Chapter is terminal (every
   Area row is `WRITTEN`, `WRITTEN(P.S.N.CCC)` for a whole-built Chapter, or `DROPPED` with a variance note) and to prepare the completion of the
   current Chapter's spec with its final variance summary (the `/chapter-spec` **complete** flow:
   its checks, its questions and its one confirmation (on "Not yet" nothing is written, an entry
   already written at step 0(a) staying, and the command stops, as `/next-part` and
   `/next-section` do), and the drafted summary, Reader now knows line, Chapter digest and
   New-named-things line; nothing is written yet). The Chapter Spec is normally `COMPLETED`
   already, set by the Gate 2 sync when its last Area row was written (Part 38 Rule 3.6.1 item 1);
   the completion step sets it if it is not yet set and writes the completion pieces. The
   Chapter-Level CDL-2 Aggregate Block runs through **area-scorer**, as in Parallel orchestration.
2. Build the new Chapter's spec via the `/chapter-spec` **build** flow — full consultation
   through `[CONFIRM SPEC]`, from its entry in the Novel-Part Spec (the entry pre-fills the
   Chapter header; the settled items of the Section Spec and the Novel-Part Spec are carried in
   and not re-asked; the author's deferrals to the writing are carried in and recorded in the
   spec's Audit and Settlement Notes section, as Part 38 sets out), establishing the Chapter's
   title, purpose, Area breakdown and each Area's block (Part 38 section 2.4: its size target
   of 1,600, 1,800 or 2,000 words, its pacing, whether it is a complete scene or continues a scene
   across Areas, opening and closing type, carry-over, thread and the other fields listed there)
   — BEFORE any Area is planned or drafted. A header line that departs from what the entry fixes
   is shown at the confirm step with the question whether to amend the plan too or leave the entry
   as the plan baseline, and with the note that a variance note for it is left on the Section Spec
   and on the Novel-Part Spec either way (Part 38 Rules 9.3.3 and 9.4.5). The Chapter window and each
   Area's in-story time are written as dates plus Phase Day (Part 41 Area 4), and the carry-in
   names the last dated moment of the closing Chapter, read from the calendar ledger's Current
   Position block (Part 41 Area 9). If the new Chapter's spec already exists and is confirmed (a
   spec survives a rewind, a reset or a redraft, Part 38 Rule 7.1.1), do not build it blind: run
   the `/chapter-spec` **revise** flow on it and re-confirm what survives, as `/start-story` does.
3. **On `[CONFIRM SPEC]`, one write step:** the variance note of each departure, written top-down
   (the Section Spec first, then the Novel-Part Spec, each with its registry row; as `/chapter-spec`
   Step 4 sets out, Rule 9.4.5); the new Chapter Spec file and its registry row; the outgoing
   Chapter's completion pieces (and `COMPLETED` if not yet set) with its registry row; and the
   Coverage cells of the Novel-Part and Section rows (Chapters completed / planned), refreshed
   because this is a completion write step (Part 38 Rule 1.2.2; never at Gate 2). An amended Novel-Part
   entry is made by `/part-spec revise`, not by this write step. A Chapter added at step 0(a) was
   written, and noted as variance on the Section Spec (Rule 11.4.3), at its own confirm. The
   outgoing spec's completion pieces are therefore never written without a confirmed successor.
   **On `[SKIP SPEC]`** the new spec is saved as `DRAFT`, nothing is written to the Section Spec,
   the Novel-Part Spec or the outgoing Chapter Spec (its completion pieces are not written; an
   entry written at step 0(a) stays), the chain stops there, and `/next-chapter` is run again.
4. **Proceed to the writer the Chapter Spec's Build mode names.** By default (Build mode `whole`, the
   default for a new spec) run `/create-chapter` for the new Chapter: one whole Chapter in one cycle, with
   its own Plan Mode (Decision Consultation Gate and build-plan confirmation), Gate 1 and Gate 2, as
   documented there; this command neither shortens nor restates it. Run `/next-area` instead only when the
   author asks for it or the spec's Build mode is `by-area`: then run `/next-area` for the new Chapter's
   opening Area (now spec-grounded), with `--first-of-chapter` (the writer's `is_first_area_of_chapter`;
   Chapter Header Block handling per Part 2 Rule 6.3.1/6.3.1a in `narration-novel-book-structure-law`
   Area 6 and `.claude/tools/area_docx_creator.py`). Once the Chapter Spec is confirmed, the only questions
   left to Plan Mode are those of the writer's own Step 0 (`/create-chapter` Step 0, or `/next-area`
   Step 0); pacing, size targets and stretch are carried from the Chapter Spec and are not asked again.
   After a whole-built Chapter, the Chapter Spec is already `COMPLETED` at Gate 2, so this command's
   completion step (step 1) only checks it and writes the pieces still missing.

## Failure/abort

Do not advance a Chapter with an Area that is not terminal, or with open/unresolved Area
content — surface it instead. Never advance with the prior Chapter's spec not `COMPLETED`
(or not completable: an Area row that is neither `WRITTEN` nor `DROPPED` with a variance note)
or the new Chapter's spec unconfirmed (Part 38): `[SKIP SPEC]` at the build gate saves the
drafted spec as `DRAFT` and stops the advance there; the new Chapter stays blocked for
`/next-area` until `[CONFIRM SPEC]`. The outgoing spec's completion pieces are written only on
that confirmation, so after a skip it is left as it was and `/next-chapter` is run again. A
parent link that is missing, `DRAFT`, `AMENDED-PENDING-RECONFIRM` or `RETIRED` stops the command
at step 0 and names `/section-spec` or `/part-spec`; a Novel-Part Spec with no further Chapter
entry stops at the question of step 0 (the author chooses an added entry, which has its own
`[CONFIRM SPEC]` and, if skipped or declined, leaves no Chapter Spec built; `/next-part`; or
`/part-spec revise`). If the build shows that the Novel-Part Spec or the Section Spec needs a
substantial change (the new Chapter cannot sit inside its Novel-Part's purpose, closing state,
calendar window or reveals owed), ask it as a question, never settle it silently; the author's
answer amends the higher spec through `/part-spec revise` or `/section-spec revise` (Part 38 Rule 9.4.2),
with a variance note on every spec above the Chapter as `/chapter-spec` Step 4 sets out, and the
run stops at that level until the revised spec is confirmed.
