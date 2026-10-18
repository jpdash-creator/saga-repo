# Guardrail: Authority Tier System

**Source:** this guardrail · Canon v10.0
**Applies to:** all 4 agents, always

## The rule

Authority tiers govern functional *scope*, not importance — a Tier 1 Part is not "less
canon" than Tier 0, it simply has no authority outside its own domain.

- **Tier 0 — Narrative Identity: Part 36.** Governs *how* other Parts'
  technical requirements are fulfilled in prose (never *whether* they apply). Part 36
  cannot excuse a technical requirement of another Part, only choose among compliant ways
  to render it. That choice names the requirements of Parts 28, 29 and 39 and of
  `.claude/guardrails/quality/guardrail-plain-language.md` beside
  Parts 2–35 (Part 36 Area 14.1; Parts 37 and 38 govern ledgers and specs, not prose form,
  and are outside this choice): Part 36 chooses the form, nothing is waived, and a
  requirement that can be met in only one way still comes to the author.
- **Tier 0 — Narration-Craft Law: Part 28.** Whole-Part Tier 0 — narrative flexibility,
  naming, and narration-craft law. Like Part 36, its Tier 0 governs *how* prose is rendered:
  it cannot excuse a technical requirement of another Part, and its Tier 0 is craft-layer
  scope.
- **Tier 0 — Dialogue and Voice Law: Part 29.** Whole-Part Tier 0 — dialogue and
  voice law. Like Part 36, its Tier 0 governs *how* prose is rendered: it cannot excuse a
  technical requirement of another Part.
- **Tier 0 — Character Behavioral Law: Part 39.** The specification,
  registry and governed evolution of character behavior across 36 Layers.
  Like Parts 28, 29 and 36, its Tier 0 is **craft-layer scope**: it governs *how* a character
  is rendered as a person and cannot excuse a technical requirement of another Part.
  Part 39 is the executable form of Part 28 Area 6's Behavioral
  Authenticity Law, not a replacement for it: Part 28 keeps the freedom principle and the
  Prohibition on Robotic Behavior, Part 39 owns the registry and the audit. Enforced at Gate 1
  Checks #20 and #21 (their counted elements inform only).
- **Tier 0 — Plain Language and Narrative Impact: the guardrail
  `.claude/guardrails/quality/guardrail-plain-language.md`.** Plain everyday words in narration and dialogue, and impact and wonder where the
  scene earns them. It is the fifth Tier 0 layer and has no Part number. Like Parts 28, 29, 36
  and 39, its Tier 0 is **craft-layer scope**: it governs *which words* a sentence is built from
  and cannot excuse a technical requirement of another Part. Enforced at blocking Gate 1 Check #22.
  (plain vocabulary, 2026-10-06) The layer also covers clarity and one meaning per word. Check #22
  elements 22-3, 22-6 and the new 22-8 to 22-11 block; 22-1, 22-2, 22-4, 22-5 and 22-7 inform.
- **Tier 1 — Domain Authority: Parts 2–27, 30–33, 35, 37–38 and 40 to 44** (Part 40 is Monster Law; Part 41 is Calendar Law, a Tier 1 domain authority like Parts 13 to 15; Part 42 is Manual and Weapon Style Law, a Tier 1 domain authority in the cultivation group beside Part 6; Part 43 is Character Evolution Law; Part 44 is Battle Plausibility Law, a Tier 1 domain authority in the cultivation group beside Parts 3 and 5, enforced at Gate 1 Check #23). Each owns exactly one registered domain
  (see `.claude/guardrails/authority/guardrail-domain-ownership.md`). No Tier 1 Part may validate itself, and no Tier 1
  Part outranks another Tier 1 Part.

## Hard rules

- **No Tier Escalation.** A Part inserting language like "this overrides all other Parts" is
  itself invalid — Tier 0/1 assignment is fixed by this guardrail, not self-declared.
- **No Tier Delegation.** The audit function is indivisible — it cannot be handed off to a
  Tier 1 Part or skipped because "this case is simple."
- **Vertical Separation / Horizontal Equality.** A Tier 1 Part cannot promote itself above
  another Tier 1 Part; disputes between two Tier 1 Parts route through the audit
  process (`.claude/guardrails/audit/guardrail-audit-gate-law.md`), never through one Part simply asserting priority over the other.
- **Counters inform; the confirmed spec chain and Part 30 prevail.** A confirmed spec chain
  (Section Spec, Novel-Part Spec and Chapter Spec, Part 38) and
  Part 30 (Novel Macro Story Law) prevail over every counter, floor,
  ceiling, budget, count and threshold in the Canon. At Gate 1 and Gate 2 such a figure is
  information: it is shown in the report and it never forces content, never fails an Area,
  never blocks a scene and never puts a question to the author on its own. This changes no
  tier and moves no Part: Part 30 and Part 38 stay Tier 1 domain authorities, Part 28 stays
  the Tier 0 narration-craft layer. Locked
  Canon facts, ledger facts, content limits and the style bans (the em-dash, contractions in
  narration and in dialogue, Canon Amendment 2026-10-16, and the like) are not
  counters and are unchanged.

Note the separate, unrelated use of the word "tier" in Part 28 (Locked Canon "Tier 2
Authorization") — that is a content-flexibility classification internal to Part 28's own
domain, not an Authority Tier. With Part 28 itself at Authority Tier 0 the collision risk is real: "Part 28 is Tier 0" refers to the authority
table above, while "Tier 1/Tier 2 flexibility" and "Tier 2 Authorization" remain Part 28's
internal content vocabulary. Do not conflate the two vocabularies.

## Escalation

Any apparent authority conflict is not resolved by an agent's own judgment. Mid-Area, the
agent stops and reports it to the orchestrating command, which asks the author; structural
doubt between Areas goes to `/run-canon-audit`. The route is set out in the Escalation rule
of `.claude/guardrails/_index.md`.
