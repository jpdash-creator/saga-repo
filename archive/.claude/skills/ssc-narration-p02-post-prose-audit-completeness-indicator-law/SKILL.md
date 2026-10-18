---
name: ssc-narration-p02-post-prose-audit-completeness-indicator-law
description: Governs the Post-Prose Audit Completeness Indicator — the mandatory two-component block (Narrative Position Block + CDL-2 Ten-Category Block) emitted immediately after every accepted Prose unit and before the next user prompt; use this when a prose-producing command (C-1, C-3, C-4, C-5, C-6, C-7, C-8, C-9, C-28, C-29, C-30) has just accepted a Prose unit into canon, when formatting or filling in the ASCII completeness-indicator block, when deciding whether N/M values carry canon authority, or when handling a [SKIP WRITE] divergence flag; this is canon Part 2 Area 8, domain narration.
user-invocable: false
---

## Rule Text (Verbatim Source — Authoritative)
## Area 8 — Post-Prose Audit Completeness Indicator Law (Canon v2.3)

### 8.1 — Purpose and Mandate

**Rule 8.1.1 — Purpose.**
The Post-Prose Audit Completeness Indicator is a two-component block emitted after every accepted Prose unit:

**Component 1 — Narrative Position Block (governed by Part 2 Area 8):** A tentative, advisory block reporting the system's current best estimate of where that Prose sits within the Phase 1 structural envelope defined by Part 30 (Macro Story Law) and the six-tier hierarchy of Part 2 Area 1. It is not a canon decision, not an enforcement mechanism, and not a commitment to a specific total Prose/Area/Chapter/Part/Section/Phase count — it is a navigation aid so the user can track progress toward Phase 1 end-state Locked Canon (Part 30 Section 1.3.1) without manually auditing the narrative position.

**Component 2 — CDL-2 Ten-Category Block (governed by Part 35 Area 4):** The mandatory content density scoring block showing the Prose unit's CDL-2 scores across all ten content categories (Combat, Named Moves, Cultivation Growth, Technology, Lore & World-Building, Dialogue & Social, Information & Intrigue, Consequence & Psychology, Travel & Discovery, Political & Faction), the running Section aggregate, and ON TRACK / WARN / FAIL status per category against the active Section targets from Part 35 Area 3. This block is enforced (not advisory) for the four Universal Anchor Floors (Combat, Cultivation Growth, Dialogue & Social, Lore & World-Building) at Section close. Part 35 Area 4 governs the CDL-2 block format; Part 2 Area 8 governs the narrative position block. Both blocks are emitted as a single post-Prose output per Part 1 Rule 7.1.1(j).

**Rule 8.1.2 — Mandate.**
Every prose-producing command (C-1, C-3, C-4, C-5, C-6, C-7, C-8, C-9, C-28, C-29, C-30) that accepts a Prose unit into canon must emit the Post-Prose Audit Completeness Indicator block immediately after the Post-Write Ledger Update and before the next user prompt. This is required by Part 1 Rule 7.1.1(j) and operationalized here.

### 8.2 — Canonical Block Format

**Rule 8.2.1 — Block Format.**
The indicator is emitted as the following ASCII block, with numeric estimates filled in per the current narrative position and the governing Phase 1 End-State Locked Canon. Each "~M" value is tentative — the system's current best estimate, subject to revision as the story develops. The "N" values are exact counts of accepted canon content.

```
┌─────────────────────────────────────────────────────────────┐
│ POST-PROSE COMPLETENESS INDICATOR (tentative, advisory)     │
├─────────────────────────────────────────────────────────────┤
│ Prose in Area A of Chapter C of Part P:        N of ~M      │
│ Areas in Chapter C of Part P:                  N of ~M      │
│ Chapters in Part P of Section S:               N of ~M      │
│ Parts in Section S of Phase Φ:                 N of ~M      │
│ Sections in Phase Φ:                           N of ~M      │
└─────────────────────────────────────────────────────────────┘
```

**Rule 8.2.2 — Tentativeness Marker.**
The `~` prefix on M is a mandatory tentativeness marker. It signals that M is an estimate and may shift as the story develops. N values carry no `~` because they are exact counts.

**Rule 8.2.3 — Phase 1 Envelope Source.**
M estimates at the Section and Part levels are anchored to Part 30 Section 1.3.1 (Phase 1 End-State Locked Canon) and Part 30's Phase 1 arc map (8 Sections). M estimates at the Chapter, Area, and Prose levels are drawn from current narrative-plan estimates maintained by the system and revised as the story progresses; they have no Locked Canon anchor and are labeled tentative to reflect this.

### 8.3 — Governing Constraints

**Rule 8.3.1 — Advisory Only.**
The Completeness Indicator is advisory. It does not constrain narrative structure. A Chapter may end before N reaches ~M, or continue after N exceeds ~M. The indicator tracks; it does not govern.

**Rule 8.3.2 — No Canon Authority.**
M estimates are not Locked Canon. They may not be cited as a rule basis for audit findings, consequence rulings, or structural decisions. The governing structure law remains Part 2 Area 1 (six-tier hierarchy) and Part 30 (Macro Story Law).

**Rule 8.3.3 — Skip Write Behavior.**
On `[SKIP WRITE]`, the Completeness Indicator is still emitted (the Prose is canon-accepted per Part 1 Rule 7.1.1's chat-accepted-counts rule), but a divergence flag is appended noting that the per-Prose `.docx`/`.md` file pair was not written at this position.

---

## Cross-References
| Related Skill | Relation | Source |
|---|---|---|
| ssc-cultivation-p03-cultivation-ladder-realm-hierarchy | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 8 governs solely the ASCII Post-Prose Completeness Indicator block (Narrative Position + CDL-2 blocks) and has no prose-content or scene-setting rule that depends on cultivation-realm mechanics |
| ssc-cultivation-p03-lifespan-mechanics | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 8 governs solely the ASCII Post-Prose Completeness Indicator block and has no rule tied to lifespan mechanics |
| ssc-cultivation-p03-power-density | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 8 governs solely the ASCII Post-Prose Completeness Indicator block and has no rule tied to power-density mechanics |
| ssc-cultivation-p03-realm-transition | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 8 governs solely the ASCII Post-Prose Completeness Indicator block and has no rule tied to realm-transition mechanics |
| ssc-cultivation-p03-cultivation-talent | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 8 governs solely the ASCII Post-Prose Completeness Indicator block and has no rule tied to cultivation-talent mechanics |
| ssc-cultivation-p03-growth-speed | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 8 governs solely the ASCII Post-Prose Completeness Indicator block and has no rule tied to growth-speed mechanics |
| ssc-cultivation-p03-power-comparison | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 8 governs solely the ASCII Post-Prose Completeness Indicator block and has no rule tied to power-comparison mechanics |
| ssc-cultivation-p03-damage-tolerance-recovery | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 8 governs solely the ASCII Post-Prose Completeness Indicator block and has no rule tied to damage-tolerance/recovery mechanics |
| ssc-cultivation-p03-affinity-cultivation | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 8 governs solely the ASCII Post-Prose Completeness Indicator block and has no rule tied to affinity-cultivation mechanics |
| ssc-cultivation-p03-heart-cultivation | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 8 governs solely the ASCII Post-Prose Completeness Indicator block and has no rule tied to heart-cultivation mechanics |

## Governing Authority
Subordinate to the shared Part 1 (audit law) + Part 34 (knowledge graph) grounding in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.

## Source Provenance
Part 2, Area 8 — "Post-Prose Audit Completeness Indicator Law (Canon v2.3)" · canon v4.33 · migrated 2026-08-03
