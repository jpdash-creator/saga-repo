# Guardrail: FCIA — Full Content Integrity Audit

**Source:** this guardrail (the audit layer has no skill file) · Canon v10.0
**Applies to:** Continuity Checker (primary owner); Area Maker (must satisfy it)

## The rule

FCIA audits **narrative prose content** — the actual written Areas and Chapters —
against 16 content dimensions (FC-1–FC-16), and runs on **every accepted Area and
every session end**, not on a sample.

The 16 dimensions: Cultivation, Technology, Synergy, Character Arc, World/Location,
Information/Secrecy, Affiliation/Social, Ideology/Psychology, Consequence, Combat, Ledger
State Consistency, NSA (knowledge-graph) Propagation, Cross-Event Continuity, End-of-Session
state, **FC-15 Contextual Earning Audit** (Part 28 Area 15's Three-Beat Test — has this
moment been narratively earned, not just stated), and **FC-16 Novel Thematic Compliance**
(Part 36's Check #16 — see `.claude/guardrails/quality/guardrail-tier0-narrative-quality.md`).

## Hard rules

- **What fires it.** Every accepted Area and every session end — not just "chapter
  complete," but also things like a new named entity appearing, a ledger-relevant state
  change, or a cross-Part dependency being touched for the first time.
- **An Area Maker output is a draft until FCIA (via Gate 1) has cleared it** — no narrative
  claim is trusted before that.
- **A session ends when a Section closes.** At each Section close, `/next-section` (for a
  Phase's final Section, `/next-phase`) runs FCIA end-of-session and ALCA Mode B together, as
  concurrent agents (they read different layers), and then a Unified Audit Summary after both
  have returned, over the Areas of the closing Section (the Areas written since the previous
  Section closed, found from the written files and the spec, never from the session log) —
  never skip straight to "done" without this chain.
- **Scope.** Each accepted Area gets FCIA in full through Gate 1. The session-end pass covers
  the Areas written in the session (the Areas of the closing Section) plus any earlier Area they cite. The
  FCIA lane of `/run-canon-audit` covers the Chapter or Section the author names.
- **Reader-Reveal Timing Law (RRTL)** is audited as part of FCIA: villain motivation must
  surface by the hero's Arc Phase 4, the hero's core wound by Phase 3, faction agendas one
  Section before climax, and consequences are never concealed indefinitely.

## Escalation

An FCIA FAIL routes back through the Gate 1 Correction Protocol
(`.claude/guardrails/audit/guardrail-audit-gate-law.md`) — it is never waived because a deadline or pacing
preference makes revision inconvenient.
