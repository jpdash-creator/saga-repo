---
description: Read-only session initialization -- load the guardrails, the canon manifest, the story-memory ledger indexes, the story-spec registry, the active Section Spec, Novel-Part Spec and Chapter Spec (each in full), and the current position with its current Area window and last Chapter (all other written Areas are listed by file name) to establish full current state.
user-invocable: true
---

# `/load-canon`

Corresponds to canon command `[LOAD CANON]` (C-35). Read-only session init; makes no
changes. Useful at the start of a session, or any time you want a full-state refresh rather
than trusting conversational memory (`.claude/guardrails/ledger/guardrail-session-log-not-canon.md`).
See also `.claude/guardrails/commands/guardrail-plan-then-auto-execution.md` for this
command's Plan Mode → Auto Mode execution shape and mandatory parallelism.

## Plan Mode → Auto Mode

This command is pure read-only session init — it asks no author-facing questions and
requires no confirmation token at any point, so there is no consultation step to name as a
Plan Mode boundary here; Plan Mode is trivial/immediate and the whole command runs in Auto
Mode by default (`guardrails/commands/guardrail-plan-then-auto-execution.md`).

## Parallel orchestration

Steps 1–4 have no dependency between them except one: the registry read in step 3 names the
active specs, and the three spec files are read only after it. So run it in two waves. In the
first wave, run concurrently everything else that has no dependency: batch independent
Read calls as parallel tool calls, and/or fan the four layers (guardrails / manifest /
ledger indexes + story-spec registry / position, Area window and last Chapter) out to parallel read-only agents.
As soon as the registry has returned, the second wave reads the active Section Spec, the active
Novel-Part Spec and the active Chapter Spec in one parallel batch, while the other layers are still
being read. Merge everything into the single step 5 summary once all return. This concurrency is a binding
requirement under `.claude/guardrails/commands/guardrail-plan-then-auto-execution.md` —
these layers are never read one at a time "for simplicity." (This command invokes no
area-maker, outline-planner, continuity-checker, or area-scorer instance, so the
guardrail's model/effort-default and progress-checkpoint provisions have nothing to attach
to here.)

## Sequence

1. Read `.claude/guardrails/_index.md` and every guardrail file beneath it.
2. Read `.claude/canon-manifest/skill-index.json` (and the other manifest files) in full.
   Skill reads during this init are consolidated-first: each Part has exactly one skill,
   named `<group>-<title>`, and that is the read.
3. Read every `.claude/story-memory/ledger-*/_index.md`. Read the story-spec registry
   (`.claude/story-memory/phase-section-part-chapter-area-specs/_index.md`) before any spec
   file, by kind from its three tables (Section Specs, Novel-Part Specs, Chapter Specs). The
   registry names the **active** spec of each tier: the first spec in story order, by Ref number
   compared number by number, whose status is not `COMPLETED`, with a `RETIRED` spec skipped
   (Part 38 Rule 9.7.4). Then, in one parallel batch, read the **active Section Spec, the active
   Novel-Part Spec and the active Chapter Spec, each in full** (Part 38 — spec state is part of
   full current state). This is the build read-set rule (Part 38 Rule 9.9.2): the chain above the
   level being worked is read in full, not an excerpt of it. The shorter read set of per-Area agents
   (the Chapter Spec in full, with only the Novel-Part Spec's header block and closing-state block,
   and no Section Spec) does not apply to this command, which is a full-state refresh and not a
   per-Area agent. A tier with no active spec (none exists yet, or every one is `COMPLETED`) has no
   file to load: say so, and read nothing in its place.
4. Find the position as `/status` does (the first `PLANNED` or `DRAFTED` row of the active Chapter
   Spec; a `DROPPED` row is skipped). Under `projects/novel-starward-saga/` (the `_archive` folder is
   never read, listed or counted, Part 2 Rule 5.3.2a), read in full the Area window (the previous
   written Area and the earlier Areas of a scene that continues across Areas, defined once in Part 2
   Rule P2-Area-1) and the Areas of the last completed Chapter. The active specs are read in step 3.
   The other written Areas are listed by file name and not read.
5. Report a brief summary of current state — do not draft, audit, or plan anything as part
   of this command. The summary adds the chain: the Ref and status of the active Section Spec,
   Novel-Part Spec and Chapter Spec, and the first missing link, which is the first link, top-down,
   that is missing or whose status is not `CONFIRMED` or `COMPLETED`, named with the command that
   repairs it (`/section-spec`, `/part-spec` or `/chapter-spec`; Part 38 Rule 9.1.1), or "chain in
   force" when no link is missing. The chain's parents are found by Ref (`P.S.P.CCC` sits under
   `P.S.P`, which sits under `P.S`). `/status` gives the full report of the chain and the
   Chapter-list progress.
