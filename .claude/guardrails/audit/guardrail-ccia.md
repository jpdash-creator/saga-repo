# Guardrail: CCIA — Continuous Canon Integrity Audit

**Source:** this guardrail (the audit layer has no skill file) · Canon v10.0
**Applies to:** Continuity Checker (primary owner)

## The rule

CCIA audits the **governance system itself** — the canon Parts, the skill/guardrail
structure, `.claude/canon-manifest/`, `.claude/story-memory/` architecture — not narrative prose
content (that's FCIA) and not ledger operational correctness (that's ALCA).

- **What fires it.** CCIA runs whenever the canon structure itself changes or is
  suspected to have drifted (new skill added, manifest edited, ledger folder created, etc.),
  not on a fixed schedule alone.
- **7 dimensions** every CCIA pass evaluates: Redundancy/Duplication, Discrepancy/Conflict,
  Ambiguity, Relationship Accuracy / knowledge-graph readiness, Coverage Completeness,
  Ledger Architecture Integrity, and canon-manifest currency.
- **Docs page check.** Every CCIA pass also checks that the counts and cards in
  `.claude/docs/index.html` match `.claude/commands/` and `.claude/agents/`. The Continuity
  Checker makes this check, in the CCIA lane of `/run-canon-audit`. The page is maintained by hand and no script keeps it current, so a mismatch is a finding like any other.
- **Steps.** A CCIA cycle evaluates each of the seven dimensions and makes the docs page
  check, logs its findings (Hard rules below), reports any finding that implies a
  structural fix instead of applying it (Escalation below), and ends by updating
  `.claude/canon-manifest/`.
  That last step is **mandatory** — a CCIA pass that doesn't end by reconciling the
  manifest hasn't actually finished.

## Hard rules

- CCIA **cannot** execute a Locked Canon change (Canon Amendment territory) without explicit
  user authorization.
- CCIA **cannot** delete content without explicit user authorization.
- Every CCIA cycle's findings are logged (see `.claude/story-memory/session-log/`) so structural
  drift is traceable across the life of the project, not just in the moment it's found.

## Escalation

CCIA findings that imply a structural or authority-level fix are reported, not silently
applied — get explicit go-ahead before restructuring skills, guardrails, or the manifest.
