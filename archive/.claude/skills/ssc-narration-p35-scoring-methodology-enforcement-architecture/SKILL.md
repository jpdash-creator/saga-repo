---
name: ssc-narration-p35-scoring-methodology-enforcement-architecture
description: Covers the CDL-2 (Content Density Law 2) scoring methodology and enforcement pyramid — the four-step Prose-unit scoring protocol against the ten content categories, the word-count-weighted averaging formula used to compute Section-aggregate scores, the four-level enforcement pyramid (Prose Unit / Area / Chapter WARN / Section Hard FAIL and Advisory WARN) governing Universal Anchor Floor categories (COMBAT, CULTIVATION GROWTH, DIALOGUE & SOCIAL, LORE & WORLD-BUILDING), and the CDL-2 Section Override Protocol for documented, user-approved deviations from Locked Guidance targets. Reach for this Area whenever an agent is scoring a just-completed Prose unit for its Completeness Indicator, updating a Section's running CDL-2 aggregate, deciding whether a Chapter or Section close should trigger a WARN or Hard FAIL, or executing/documenting a CDL-2 Section Override. This is canon Part 35 Area 2, domain narration.
user-invocable: false
---

## Rule Text (Verbatim Source — Authoritative)
## Area 2 — Scoring Methodology and Enforcement Architecture

### 2.1 — Prose-Unit Scoring Protocol

At Gate 2, after each Prose unit is written and before the Completeness Indicator is finalized, the AI performs a CDL-2 scoring pass on the Prose unit:

**Step 1 — Identify Primary Content Blocks.** Mentally divide the Prose unit into thematic content blocks by estimated word count. A slow-paced 3000-word Prose unit might have: 1200 words of combat exchange, 700 words of tactical dialogue, 500 words of cultivation description, 300 words of lore rendering, and 300 words of consequence and psychology. A fast-paced 2000-word combat-primary unit might have 1400 words of combat, 300 words of tactical dialogue, and 300 words of consequence.

**Step 2 — Score Each Category.** For each of the ten categories, estimate the percentage of the Prose unit's total word count that is meaningfully engaged in that category. Using the example above: COMBAT ≈ 75% (1,800 + 400 tactical dialogue combat-adjacent = 2,200/4,000 ≈ 55%, but the tactical dialogue also scores DIALOGUE & SOCIAL so COMBAT takes the direct combat words = 1,800/4,000 = 45% — then add pre-combat strategy at 400 = 55%). Scores are approximate and honest, not precise fractions.

**Step 3 — Record Scores in Completeness Indicator.** Every CDL-2 category score is recorded in the Prose unit's Completeness Indicator (format defined in Area 4).

**Step 4 — Update Section Running Totals.** After each Prose unit is scored, the AI updates the running Section aggregate for each category (weighted by Prose unit word count). This running total is visible in the Completeness Indicator's Section-Level CDL-2 Tracker block.

---

### 2.2 — Weighted Averaging for Section Aggregate

Section-aggregate CDL-2 scores are computed as **word-count-weighted averages** across all Prose units completed in the Section. This ensures that a long, combat-heavy Prose unit contributes proportionally more to the COMBAT aggregate than a short non-combat interlude. The weighting formula is:

> **Section Aggregate (Category X) = Σ (Prose_wordcount_i × Score_i) / Σ (Prose_wordcount_i)**

The AI tracks this running weighted average and displays it in the Section-Level CDL-2 Tracker at each Completeness Indicator.

---

### 2.3 — Enforcement Pyramid

**Level 1 — Prose Unit (Record and Display).**
Every Prose unit's CDL-2 scores are recorded in its Completeness Indicator. No enforcement action is taken at the Prose-unit level. The scores are informational and contribute to Area and Section aggregates.

**Level 2 — Area Level (Record and Display).**
At the close of each Area (per Part 2's six-tier hierarchy), the Area-level CDL-2 aggregate is displayed. No enforcement action is taken at the Area level. The aggregate serves as an early-warning signal if the Section trajectory is drifting away from its targets.

**Level 3 — Chapter Level (WARN).**
At the close of each Chapter, if the Chapter-level CDL-2 aggregate for any Universal Anchor Floor category (COMBAT, CULTIVATION GROWTH, DIALOGUE & SOCIAL, LORE & WORLD-BUILDING) is tracking below 20% on a trajectory that would produce a Section-close Hard FAIL, the AI issues a **CDL-2 WARN** in the Completeness Indicator. The WARN identifies which category is at risk, its current trajectory, and the target adjustment required in subsequent prose to bring it within range. WARNs are advisory — they do not block prose authorship, but they must be acknowledged and addressed.

**Level 4 — Section Level (Hard FAIL for Anchor Floors; Advisory WARN for all others).**
At Section-close, the AI performs a full CDL-2 Section Audit:
- **Hard FAIL:** If any of the four Universal Anchor Floor categories (★ COMBAT, ★ CULTIVATION GROWTH, ★ DIALOGUE & SOCIAL, ★ LORE & WORLD-BUILDING) falls below its Section Anchor percentage (see Area 3 Target Table), the Section has FAILED its CDL-2 requirement. A Hard FAIL must be resolved: either through additional Prose content that brings the aggregate within range, or through a documented CDL-2 Section Override with explicit user approval.
- **Advisory WARN:** If any non-Anchor category falls below its Section Low or above its Section High, the AI issues an Advisory WARN. Advisory WARNs are recorded in the SSC Canon event log for the Section and do not block Phase progression, but they are visible for editorial review.

---

### 2.4 — CDL-2 Section Override Protocol

When story necessity requires a Section's actual content distribution to deviate from the Locked Guidance targets in the Area 3 table, a **CDL-2 Section Override** is executed as follows:

1. The AI identifies the deviation and its narrative justification
2. The override is presented to the user with the specific category, the target vs. actual value, and the story reason
3. User approves the override explicitly
4. The override is documented in the SSC Canon event log with: Section identifier, category, original target, override value, user approval reference, and narrative justification
5. No formal Canon Amendment is required — the event log entry is sufficient

CDL-2 Section Overrides that reduce a Universal Anchor Floor below 20% Anchor require a more detailed narrative justification and explicit user approval statement, as they represent a departure from the series' foundational content identity.

---

## Cross-References
| Related Skill | Relation | Source |
|---|---|---|
| (none resolved from the manifest for this Area) | | |

## Governing Authority
Subordinate to the shared Part 1 (audit law) + Part 34 (knowledge graph) grounding in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.

## Source Provenance
Part 35, Area 2 — "Scoring Methodology and Enforcement Architecture" · canon v4.33 · migrated 2026-08-03
