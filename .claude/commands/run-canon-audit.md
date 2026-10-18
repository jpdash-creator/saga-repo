---
description: Run a full canon audit (CCIA + FCIA + ALCA) across all skills, guardrails and story-memory ledgers, and the written Areas of the Chapter or Section you name. The escalation target whenever an agent or command detects an unresolved conflict.
argument-hint: [chapter or section for the FCIA pass]
user-invocable: true
---

# `/run-canon-audit`

Corresponds to canon command `[RUN CANON AUDIT]` (C-10). This is the general escalation
target referenced throughout the guardrails ("escalate via `/run-canon-audit`") — invoke it
whenever a conflict needs full-system verification rather than a narrow single-unit check.

## Preconditions

- See `.claude/guardrails/commands/guardrail-plan-then-auto-execution.md` for this
  command's Plan Mode → Auto Mode execution shape, default agent model/effort, mandatory
  parallelism, and progress-checkpoint relay.

## Plan Mode → Auto Mode

This command has no pre-work consultation step — it launches straight into the three
audits with no author-facing questions, so Plan Mode is trivial/immediate here. Everything
from Step 1 onward runs in Auto Mode; the one mandatory stop this command preserves is the
Failure/abort escalation below, and Auto Mode never waives it — a finding that implies a
structural change is still reported for explicit decision, never auto-applied
(`guardrails/commands/guardrail-plan-then-auto-execution.md`).

## Sequence

1. Launch **three continuity-checker agents in parallel** (single message, three Agent
   calls) — the three audits are independent, read-only over different layers:
   - **CCIA** (`.claude/guardrails/audit/guardrail-ccia.md`) — governance/structure
     integrity across skills, guardrails, and the canon manifest. The Continuity Checker runs
     the CCIA docs-page check (`.claude/docs/index.html` against `commands/` and `agents/`) in
     the CCIA lane.
   - **FCIA** (`audit/guardrail-fcia.md`) — the written Areas of the Chapter or Section the
     author names (the current Section when none is named), read in full from
     `projects/novel-starward-saga/` (never the `_archive` folder).
   - **ALCA Mode B** (`audit/guardrail-alca.md`) — the full AL-1–AL-10 pass: its
     ledger-facing dimensions read `.claude/story-memory/ledger-*/`, its rule-facing
     dimensions (Rule Internal Consistency, Cross-Part Consistency, Version Consistency,
     Canon-Manifest Accuracy) read the 39 consolidated skills and `.claude/canon-manifest/`.
   - **Calibration check** (only when this audit follows a change to an agent file in
     `.claude/agents/` or to Part 28, 29, 36 or 39; when it is not known whether such a change
     happened, it runs) — a fourth continuity-checker agent, launched in the same message,
     runs the checker over each passage in `.claude/story-memory/calibration/`. It treats each
     passage as the Area under audit for the one check its header names, reads nothing but
     that passage and the Part the header names, and reports the passage as CAUGHT or MISSED as
     `.claude/story-memory/calibration/README.md` defines. A MISSED passage means the checker
     no longer sees that fault: it is reported for the author's decision (Failure/abort below)
     and nothing is edited to make it pass. The passages are test material: the FCIA lane never
     reads them, no ledger is updated from them, and a folder with no passages ends this lane
     at once.
   Each agent logs its own timestamped file to `.claude/story-memory/session-log/`
   (distinct files — no write conflict). This three-way parallel launch is a binding
   requirement under `.claude/guardrails/commands/guardrail-plan-then-auto-execution.md` —
   the three audits are never issued one at a time "for simplicity," and the calibration
   check, when it applies, goes in the same message.
2. Once all the agents return, produce a Unified Audit Summary from their reports (the
   calibration check adds one CAUGHT or MISSED line per passage) and log it to
   `.claude/story-memory/session-log/`.

## Failure/abort

Any finding that implies a structural change (new skill, guardrail edit, manifest change,
schema change) is reported for explicit decision, never auto-applied.
