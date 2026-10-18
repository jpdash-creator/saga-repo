---
name: ssc-narration-p36-part-36-conflict-resolution-protocol
description: Governs how to resolve apparent conflicts between technical accuracy requirements (Parts 1–35, what must be true) and the Part 36 Living Scene Standard (how that truth must feel in prose); trigger this whenever a cultivation/technology/lore fact from another Part seems to force exposition, info-dumping, or scene-stopping delivery — the agent must first exhaust Reframe Mandate options (character-felt delivery, dialogue-embedding, action-anchoring, inference-through-observation) and, only if truly irresolvable, escalate via AskUserQuestion with the four required elements before any prose unit passes the Decision Consultation Gate, since no required technical fact may ever be silently omitted or silently downgraded to "resolve" the conflict; this is canon Part 36 Area 14, domain narration.
user-invocable: false
---

## Rule Text (Verbatim Source — Authoritative)
## Area 14 — Part 36 Conflict Resolution Protocol

### 14.1 — Part 36 Is Primary for Narrative Shape

When a technical accuracy requirement from Parts 1–35 can be fulfilled in multiple narrative forms, Part 36 determines which form is used. Part 36 is the governing authority over how technical requirements are rendered in prose. Parts 1–35 govern what must be true; Part 36 governs how that truth must feel.

### 14.2 — The Reframe Mandate

When a technical requirement appears to conflict with the Living Scene Standard, the AI's first response is always the **Reframe Mandate**: find a way to deliver the required technical content within a living-scene form. The technical content need not be omitted — it must be restructured so that its delivery serves the scene rather than stopping it.

Reframe options include: character-felt delivery, dialogue-embedding, action-anchoring, and inference-through-observation (Area 3.2). The AI must attempt all available reframe options before declaring a reframe impossible.

### 14.3 — Escalation Protocol (Even Minimal Variance)

When the AI cannot find a reframe that satisfies both the technical accuracy requirement and the Part 36 Living Scene Standard — when the two requirements are genuinely incompatible in the specific scene context — the AI must **escalate to the user via `AskUserQuestion`** before proceeding. This escalation fires **even for minimal variance.** A prose unit must not proceed past the Decision Consultation Gate if a genuine Part 36 conflict has been identified and not resolved.

The escalation question must:

**(a)** Name the specific technical requirement (citing the governing Part and rule)
**(b)** Name the specific Part 36 principle in conflict (citing the Area and the sin or law at risk)
**(c)** Present the available resolution options — at minimum: "deliver technically accurate at expense of scene pace," "defer technical explanation to a later prose unit," "embed in dialogue at cost of slightly reduced technical granularity"
**(d)** Include an explicit **SKIP — let AI decide** option

No silent resolution of a Part 36 conflict is permitted. The Canon Variance Process (Part 1 Area 3.3.2) is the backstop for irresolvable conflicts that require formal Canon amendment.

### 14.4 — Part 36 Does Not Permit Technical Inaccuracy

The Reframe Mandate and the Conflict Escalation Protocol do not authorize the AI to resolve a Part 36 conflict by sacrificing technical accuracy. A cultivation fact that must be correct per Part 3 remains correct; Part 36 governs how that correct fact is delivered, not whether it is present. Omitting a required technical fact to avoid an exposition violation is not a Part 36 compliance — it is a different category of Canon violation. All required technical content must be present; Part 36 governs how.

---

## Cross-References
| Related Skill | Relation | Source |
|---|---|---|
| (none resolved from the manifest for this Area) | | |

## Governing Authority
Subordinate to the shared Part 1 (audit law) + Part 34 (knowledge graph) grounding in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.

## Source Provenance
Part 36, Area 14 — "Part 36 Conflict Resolution Protocol" · canon v4.33 · migrated 2026-08-03
