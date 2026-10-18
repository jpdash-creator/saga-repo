---
name: ssc-narration-p36-dcg-thematic-preview-mandate
description: Governs how the Decision Consultation Gate (DCG, Rule 7.1.1(l); Part 28 Area 19) must present scene-direction options during scene-planning, requiring each option to carry a 1-2 sentence narrative preview in Part 36 thematic voice, requiring explicit exposition-risk flagging when an option risks Exposition Dump or Power-System Lecturing, and prohibiting DCG questions that ask the user to settle matters the AI governs autonomously under Part 36; reach for this whenever drafting or reviewing a DCG question set before writing a prose scene, when choosing how to phrase scene-direction options for the user, when a scene direction involves heavy technical/power-system content that must be flagged, or when auditing whether a DCG question improperly asks the user to decide something (like "should this scene have sensory detail?") that Part 36 already settles autonomously; this is canon Part 36 Area 13, domain narration.
user-invocable: false
---

## Rule Text (Verbatim Source — Authoritative)
## Area 13 — DCG Thematic Preview Mandate

### 13.1 — DCG and Part 36

The Decision Consultation Gate (Rule 7.1.1(l); Part 28 Area 19) governs the scene-planning step before every prose unit is drafted. Part 36 adds a thematic requirement to the DCG: the scene-planning consultation must itself be conducted in a way that demonstrates living-scene execution awareness, not only structural planning.

### 13.2 — The Narrative Preview Requirement

For every DCG question that proposes scene-direction options to the user, each option must include a **1–2 sentence narrative preview** written in Part 36 thematic voice. This preview demonstrates what the scene would feel like if that option were chosen — not what plot events would occur (that is structural), but what emotional register and sensory texture the scene would carry.

**Compliant example:**
> Option A — The confrontation happens immediately, before the kingdom's council.
> *Preview: The council chamber fills with the particular silence of high cultivation — that pressurized stillness where everyone present can feel each other's power without acknowledging it. Varys will have to make his case while Aeries's reputation does exactly half the arguing for him, and both of them will know it.*

**Non-compliant example:**
> Option A — The confrontation happens immediately, before the kingdom's council.
> *The scene will involve dialogue between Varys and Aeries with faction members present.*

The narrative preview must use Part 36's living-prose register — sensory, emotionally specific, tonally committed. It must make the user feel what the scene will be like, not only understand what will happen in it.

### 13.3 — Exposition Risk Flagging

When a DCG option carries a high risk of Exposition Dump (Sin 1) or Power-System Lecturing (Sin 5) under Part 36 — because the scene direction requires delivering a large amount of technical information — the DCG must explicitly flag this risk to the user:

> Part 36 exposition risk: This option requires introducing [X technical content]. It will require active character-anchoring to avoid an exposition ceiling violation (Area 3). The AI will handle this in drafting, but be aware that if [X content] cannot be successfully delivered through character experience, an AskUserQuestion escalation may be required during the drafting process.

This flag is informational, not blocking. It ensures the user makes the scene-direction choice with awareness of the delivery challenges inherent in that direction.

### 13.4 — DCG Questions Must Not Ask Part 36 Autonomous Matters

The existing Decision Consultation Gate rule (no question may ask about Canon-settled facts) is reinforced under Part 36: DCG questions that ask the user to settle Part 36 matters that the AI is capable of governing autonomously — such as "should this scene have sensory detail?" or "should the character have an emotional response?" — are violations of the DCG Protocol. Part 36 matters that the AI governs autonomously must be handled in drafting. Only genuine directional choices with multiple valid narrative paths are appropriate DCG questions.

---

## Cross-References
| Related Skill | Relation | Source |
|---|---|---|
| (none resolved from the manifest for this Area) | | |

## Governing Authority
Subordinate to the shared Part 1 (audit law) + Part 34 (knowledge graph) grounding in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.

## Source Provenance
Part 36, Area 13 — "DCG Thematic Preview Mandate" · canon v4.33 · migrated 2026-08-03
