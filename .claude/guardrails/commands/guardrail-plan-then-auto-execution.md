# Guardrail: Plan-Then-Auto Execution

**Source:** this guardrail (the command layer has no skill file) · Canon v10.0
**Applies to:** the 19 orchestrator commands (the 17 below plus `create-chapter` and `revise-chapter`; `next-area`, `start-story`,
`force-ledger-audit`, `run-canon-audit`, `load-canon`, `section-spec`, `part-spec`, `chapter-spec`,
`next-chapter`, `next-part`, `next-section`, `redraft-area`, `redraft-chapter`,
`revise-area`, `update-ledger`, `character-behavior`, `new-character`) and the 4 pipeline
agents (Area Maker, Outline Planner, Continuity
Checker, Area Scorer). Read-only/reporting commands (`status`, `review-ledger`,
`character-sheet`, `canon-check`, `area-history`, `preview-chapter`, `chapter-summary`,
`find`, `timeline`, `threads`, `compile-*`, `ideology-audit`,
`consequence-audit`, `create-image-*`, and `pause`, which is an interrupt outside the
pipeline rather than a report) and the
`disable-model-invocation: true` human-invocation-only commands (`hard-reset`, `reset-*`,
`rewind-to`, `restore-archive`, `next-phase`) are out of scope — the former run no multi-agent pipeline
needing consultation or progress-polling, the latter are human-triggered only. `chapter-builder` is likewise
outside the 17 (it is a Chapter-level command that writes no Area), but it is not read-only: it writes the Chapter
files, and it carries a mandatory author confirmation before it writes, which Auto Mode never waives.
`create-chapter` and `revise-chapter` (Amended 2026-10-07) are in scope as orchestrator commands (the 17 become 19),
each with two mandatory author stops that Auto Mode never waives: the build-plan confirmation (scenes, POV order,
word budget per Area block and for the Chapter, any stretch) and the staged-text confirmation (`[CONFIRM WRITE]` /
`[REVISE CHAPTER]` / `[SKIP WRITE]`). That second
group is not uniformly destructive: `next-phase` sits in it because no agent may decide on
its own initiative that a Phase advance is warranted, not because it erases anything
(`.claude/guardrails/commands/guardrail-command-law.md`, which owns the classification). `redraft-area` and
`redraft-chapter` carry the same flag but are in scope, as listed above.

## The rule

- **Plan Mode.** Every in-scope command's pre-work consultation step — the Decision
  Consultation Gate (`narration-novel-creative-flexibility-law` Area 19) where one exists, or the
  equivalent author-facing confirmation step for commands without a full consultation gate
  (e.g. `update-ledger`'s correction confirmation) — is that command's **Plan Mode** phase.
  All author-facing questions the command will ever ask are asked and resolved (answered or
  explicitly `[SKIP]`ped) before Plan Mode ends — for `/next-area` that includes every open branch of the Area, with the pacing taken from the Chapter
  Spec. This does not add a new step; it names and
  formalizes the existing pre-work question round as a distinct, bounded phase. For
  `/section-spec`, `/part-spec` and `/chapter-spec` the whole iterative consultation is the Plan
  Mode phase (every round, the final sweep and the author's "nothing further to steer", Part 38
  Rule 38.13), and the `[CONFIRM SPEC]` prompt that ends it is a hard pause that Auto Mode never
  waives. Where a command builds more than one level of
  the spec chain (`/start-story`, `/next-section`, `/next-part`), the consultations of all those
  levels together are that command's Plan Mode phase, and they run strictly top-down, Section
  Spec, then Novel-Part Spec, then Chapter Spec, one confirm prompt open at a time.
- **Auto Mode.** Once Plan Mode concludes, the command executes the rest of its sequence
  without pausing to ask further *discretionary* questions. Auto Mode governs only whether
  the AI stops to ask something it could reasonably decide or infer — it never waives a
  mandatory gate. The Two-Gate Audit Pipeline's confirmation tokens
  (`.claude/guardrails/audit/guardrail-audit-gate-law.md`) and the destructive-command confirmation
  (`.claude/guardrails/commands/guardrail-command-law.md`) remain required stops inside Auto Mode exactly as
  before.
- **`/create-chapter` and `/revise-chapter` (Amended 2026-10-07).** Plan Mode for these commands is Step 0
  (Decision Consultation for open or deferred spec notes and genuinely new branches) plus the short build plan,
  shown to the author and confirmed. After it, Auto Mode runs draft, edit, measure and Gate 1, and then stops at the
  staged-text confirmation; neither the build-plan confirmation nor the staged-text confirmation is ever waived.
  Parallel steps: the pre-draft grounding reads (ledger entries, skills, guardrails, the previous Chapter) are
  issued together; Gate 1's two checker instances run together; Gate 2's three lanes (post-write audit, the
  Chapter's batched ledger update, the CDL-2 score) run together. Drafting (one `area-maker`) and editing (one
  `chapter-editor`) are single and sequential, because the edit consumes the draft. The Tier D, monster and Check
  #21 questions are legitimate mid-Auto-Mode stops, asked with the staged Chapter text printed first.
- **Default model and effort.** All 4 pipeline agents run at `model: claude-sonnet-5-5`
  (Claude Sonnet 5.5) and `effort: max` by default, pinned in each agent's frontmatter.
  **Author override persistence:** if the author
  explicitly names a different model or effort for a task in conversation, that instruction
  is authoritative for that agent from that point forward — every subsequent invocation of
  that agent in the session must carry the override, not silently revert to the frontmatter
  default on the next call. The override stands until the author changes or rescinds it.
- **Mandatory parallel execution.** Whenever an in-scope command has two or more steps with
  no dependency on each other, they must be launched together — in a single message, as
  concurrent background agents — never issued one at a time "for simplicity." This is the
  existing "Parallel orchestration (speed policy)" pattern already documented in
  `next-area.md` and `start-story.md`; this guardrail extends the same binding requirement
  to all in-scope commands (17, and 19 with `create-chapter` and `revise-chapter`), not just those two. This is read at its widest: fan-out is the default shape of any multi-item step,
  independent reads and greps are issued together rather than in sequence, and a step is run
  serially only where a genuine data dependency forces it. Serialising independent work is a
  violation of this guardrail, not a stylistic choice.
- **No artificial delay, anywhere.** Nothing in this system may wait on a clock.
  There is no checkpoint interval, no polling loop, no pause "to let a step settle," and no
  sleep between agent launches. An agent starts the instant its inputs exist and reports the
  instant it has a result. Where a set of files must be read, they are read in one batch;
  where a set of files must be written and the write-sets are disjoint, they are written by
  concurrent agents rather than in sequence. The only legitimate reason for step B to begin
  after step A is that B consumes A's output.
- **Milestone progress reporting.** While doing substantive work (drafting, auditing,
  scoring, planning), each of the 4 agents reports to `"main"` via `SendMessage` **on
  completing a real unit of work** — a drafted beat, a completed check, a scored category, a
  resolved planning branch. A report is a short factual line appropriate to that agent's task
  (e.g. "beat 4 of 8 drafted, ~1,300 of ~1,800 target words" for Area Maker; "check 11 of 22
  complete, 0 FAIL so far" for Continuity Checker). The orchestrating command relays each one
  to the author as it arrives, rather than staying silent until the agent's final result.
  Reporting is **event-driven, never clock-driven**: no agent pauses, interrupts, or paces its work in order
  to emit one, and no interval is owed.

## Hard rules

- Plan Mode never shortens or skips the Decision Consultation Gate's Exhaustive Clarity
  Mandate — asking exhaustively, then proceeding autonomously, are sequential
  requirements, not alternatives to trade off against each other.
- Auto Mode never overrides a mandatory confirmation token — those are Tier-0 locked under
  `.claude/guardrails/audit/guardrail-audit-gate-law.md` and `.claude/guardrails/commands/guardrail-command-law.md`, not a
  discretionary question this policy has authority to absorb.
- A number crossing a stated line is not a stop. Counters inform only
  (`.claude/guardrails/quality/guardrail-threshold-consultation.md`): the reading goes into the audit report and
  Auto Mode carries on. A flow finding that needs the author (a remedy that would change
  what happens on the page, a cause in an earlier Area), a Check #21 enquiry and a Tier D
  consequence flag (Part 19 Rule 19.1.2.4) are the questions Plan Mode cannot pre-empt, because
  they are only computable after drafting: each is a legitimate mid-Auto-Mode stop, asked with
  the Area's full text printed first.
- The default model/effort choice is an execution-performance decision, not a canon-content
  one — it never overrides a Locked Canon constraint or an agent's own documented
  task-specific reasoning (e.g. Outline Planner's `max` effort is independently justified
  by its ambiguity-resolution work, not only by this default).
- A progress report is informational only. It never substitutes for, delays, or pads the
  agent's actual final handoff, and it must never report a fabricated percentage with no
  real basis — "grounding reads in progress, no draft started yet" is a valid report. Silence
  between milestones is not a violation; there is no interval to hit and no work may ever be
  paused, chunked, or slowed to produce one.
- The parallel-execution mandate never overrides a real data dependency. Fanning out steps
  that must run in order, to appear fast, is as much a violation as needlessly serialising
  independent ones. The spec chain has one such dependency: the Novel-Part Spec is built from the
  confirmed Section Spec and the Chapter Spec from the confirmed Novel-Part Spec, so their
  consultation and confirmation run top-down, while all the grounding work that needs no
  confirmed parent (planner grounding for every level the command will build, the closing
  reviews that already run together, one continuity-checker pre-read) is launched together at the
  start of the command. The question streams of two
  different levels, or of a spec consultation and an unrelated closing question, are never mixed in
  one `AskUserQuestion` call.

- **Naming is not a cost** (Part 28 Rule 20.9, which owns this rule
  in full). In Plan Mode and in every plan, option set or recommendation of an in-scope command or agent,
  naming a person, thing, place, move or any other entity is never presented as a cost, risk or downside of
  an option, and the ledger work a name creates is never weighed against an option. Where an option could
  name or leave unnamed, the named version is the recommended one. The consultation for MAJOR entity names
  and the Gate 2 ledger obligation are unchanged.

## Escalation

If applying this policy would conflict with a Tier-0 rule elsewhere (a progress checkpoint
tempting an agent to summarize before a check is actually complete, an Auto Mode step
skipping a gate it shouldn't), the Tier-0 rule wins and the conflict is surfaced via
`AskUserQuestion` through the orchestrating command, never silently smoothed over.
