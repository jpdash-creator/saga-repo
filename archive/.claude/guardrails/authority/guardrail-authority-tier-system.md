# Guardrail: Authority Tier System

**Source:** Part 1 (Governance and Audit Law), Area 1 · Part 34 (Knowledge Graph), Area 1
**Applies to:** all 4 agents, always

## The rule

Authority tiers govern functional *scope*, not importance — a Tier 1 Part is not "less
canon" than Tier 0, it simply has no authority outside its own domain.

- **Tier 0 — Validation Protocol: Part 1.** Part 1 cannot create narrative content, cannot
  alter mechanical systems, and cannot override another Part's domain. Its sole power is to
  return VALID/INVALID rulings, route disputes, and mandate the audit process. If Part 1 is
  ever cited as the *source* of a narrative decision, that citation is invalid — Part 1
  evaluates, it never creates (Foundational Principle F-3).
- **Tier 0 — Meta-Canon Reference, peer to Part 1: Part 34.** Governs canon system
  architecture, the Neuro-Symbolic knowledge graph, and cross-Part relationship data. Not
  subordinate to Part 1, and likewise not a narrative-content author.
- **Tier 0 — Narrative Identity: Part 36.** Added later; governs *how* Tier 1 requirements
  are fulfilled in prose (never *whether* they apply). This is a third, distinct Tier-0
  authority layered on top of the original two — do not conflate its "Tier 0" with Part 1's
  or Part 34's; Part 36 cannot excuse a Part 1–35 technical requirement, only choose among
  compliant ways to render it.
- **Tier 1 — Domain Authority: Parts 2–33, 35, 37.** Each owns exactly one registered domain
  (see `guardrail-domain-ownership.md`). No Tier 1 Part may validate itself, and no Tier 1
  Part outranks another Tier 1 Part.

## Hard rules

- **No Tier Escalation.** A Part inserting language like "this overrides all other Parts" is
  itself invalid — Tier 0/1 assignment is fixed by Part 1 Area 1, not self-declared.
- **No Tier Delegation.** The audit function is indivisible — it cannot be handed off to a
  Tier 1 Part or skipped because "this case is simple."
- **Vertical Separation / Horizontal Equality.** A Tier 1 Part cannot promote itself above
  another Tier 1 Part; disputes between two Tier 1 Parts route through Part 1's audit
  process, never through one Part simply asserting priority over the other.

Note the separate, unrelated use of the word "tier" in Part 28 (Locked Canon "Tier 2
Authorization") — that is a content-flexibility classification, not an Authority Tier. Do
not conflate the two vocabularies.

## Escalation

Any apparent authority conflict is not resolved by an agent's own judgment — escalate via
`/run-canon-audit`.
