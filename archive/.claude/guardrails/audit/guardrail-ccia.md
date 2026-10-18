# Guardrail: CCIA — Continuous Canon Integrity Audit

**Source:** Part 1 (Governance and Audit Law), Area 8.1–8.11
**Applies to:** Continuity Checker (primary owner)

## The rule

CCIA audits the **governance system itself** — the canon Parts, the skill/guardrail
structure, `.claude/canon-manifest/`, `.claude/story-memory/` architecture — not narrative prose
content (that's FCIA) and not ledger operational correctness (that's ALCA).

- **10 triggers (TR-1–TR-10)** — CCIA runs whenever the canon structure itself changes or is
  suspected to have drifted (new skill added, manifest edited, ledger folder created, etc.),
  not on a fixed schedule alone.
- **7 dimensions** every CCIA pass evaluates: Redundancy/Duplication, Discrepancy/Conflict,
  Ambiguity, Relationship Accuracy / knowledge-graph readiness, Coverage Completeness,
  Ledger Architecture Integrity, and Part 34 manifest currency.
- **5-phase execution**, with updating `.claude/canon-manifest/` (the Part 34 analogue) as
  the **mandatory final phase** of every CCIA cycle — a CCIA pass that doesn't end by
  reconciling the manifest hasn't actually finished.

## Hard rules

- CCIA **cannot** execute a Locked Canon change (Part 28 Tier 2 territory) without explicit
  user authorization.
- CCIA **cannot** delete content without explicit user authorization.
- Every CCIA cycle's findings are logged (see `.claude/story-memory/session-log/`) so structural
  drift is traceable across the life of the project, not just in the moment it's found.

## Escalation

CCIA findings that imply a structural or authority-level fix are reported, not silently
applied — get explicit go-ahead before restructuring skills, guardrails, or the manifest.
