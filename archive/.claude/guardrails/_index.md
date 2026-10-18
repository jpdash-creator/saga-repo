# Guardrails Index

This folder is the shared, non-negotiable grounding for all four Starward Saga agents
(Prose Maker, Outline Planner, Continuity Checker, Prose Scorer). Every agent reads this
index first, then the specific subfolder(s) relevant to what it is about to do. Guardrails
state hard MUST / MUST NOT rules only — the detailed "how" for any given topic lives in the
corresponding `.claude/skills/ssc-*` skill, not here. If a guardrail and a skill ever appear
to conflict, the guardrail wins and the conflict must be escalated via `/run-canon-audit`,
never resolved silently.

Guardrails encode Part 1 (Governance and Audit Law) and Part 34 (Knowledge Graph) — the two
Tier-0 canon authorities that ground every agent — plus the small number of other Parts that
contain absolute, cross-cutting constraints (Part 28's Locked-Canon boundary, Part 35's
density floors, Part 36's Tier-0 narrative-quality mandate, and Rule 10.5.13's authorized-
scripts law).

| File | Source | One-line purpose |
|---|---|---|
| `authority/guardrail-authority-tier-system.md` | Part 1 Area 1 | Tier 0/1 ranking; Parts 1, 34, and 36 all sit at Tier 0 (three distinct layers) |
| `authority/guardrail-domain-ownership.md` | Part 1 Area 2; Part 34 Area 4 | Exactly one Part governs each topic; no silent domain expansion |
| `authority/guardrail-locked-vs-negotiable-canon.md` | Part 28 Area 2 | What may never be improvised vs. what is free creative territory |
| `authority/guardrail-prohibited-creative-acts.md` | Part 28 Area 12 | The 7 absolute creative prohibitions + forbidden realm vocabulary |
| `audit/guardrail-audit-gate-law.md` | Part 1 Areas 4, 7, 9, 10 | The mandatory Two-Gate pipeline every prose unit must pass through |
| `audit/guardrail-ccia.md` | Part 1 Area 8.1–8.11 | Continuous Canon Integrity Audit — audits the governance system itself |
| `audit/guardrail-fcia.md` | Part 1 Area 8.12 | Full Content Integrity Audit — audits narrative prose content |
| `audit/guardrail-alca.md` | Part 1 Area 8.13 | Action-Law/Ledger Correctness Audit — audits operational correctness |
| `audit/guardrail-forced-read-discipline.md` | Part 34 Rule 1.1.6 | Part 34 must be physically re-read at 3 fixed checkpoints, never recalled from memory |
| `ledger/guardrail-ledger-schema-law.md` | Part 37 | Ledger entity/index schemas are Part 37's authority; ledger beats prose on conflict |
| `ledger/guardrail-ledger-update-law.md` | Part 1 Areas 5, 6 | Pre-write ledger check and post-write ledger update are both mandatory, every time |
| `ledger/guardrail-session-log-not-canon.md` | Rule F-5 | `story-memory/session-log/` is a log only — never a valid decision input |
| `commands/guardrail-command-law.md` | Part 1 Area 7 | Bracket-command syntax, Two-Gate binding, confirmation tokens |
| `commands/guardrail-deprecated-commands.md` | Part 1 Area 7 | 2 commands are canon-deprecated — never reintroduce them |
| `tools/guardrail-authorized-scripts-only.md` | Rule 10.5.13 | Only the 4 named `.claude/tools/*.py` scripts may ever run |
| `quality/guardrail-tier0-narrative-quality.md` | Part 36 | Novel-feel is Tier 0 authority; conflicts escalate, never resolve silently |
| `quality/guardrail-content-density-law.md` | Part 35 | CDL-2 density floors the Prose Scorer enforces on every prose unit |

## Escalation rule (applies to every guardrail below)

No agent resolves a guardrail conflict on its own judgment. Every conflict — between two
guardrails, between a guardrail and a skill, or between a guardrail and a direct user
request — is surfaced explicitly (via `AskUserQuestion` or `/run-canon-audit`) rather than
silently decided. This mirrors Part 1's own Foundational Principle F-4: *"A violation that
is not detected is not thereby permitted."*
