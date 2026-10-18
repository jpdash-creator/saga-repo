---
name: ssc-society-p21-cct-synthesis-formula
description: Defines how a civilization's five axis values (CA, TA, EA, LA, SA) are combined into a single Composite Civilization Tier (CCT) score from 1 to 20 — the Axis Minimum Rule (hard floor, soft pull, and the SA-0 special case), the four-step Synthesis Formula (weighted average, axis gap penalty, floor check, rounding/banding), worked example synthesis profiles, and the CCT re-assessment cadence (trigger events, multi-generation lag, author reference use). Reach for this Area whenever computing or auditing a civilization's overall CCT tier from its individual axis values, resolving disputes about why a civilization's CCT is capped below its highest axis, determining whether a civilization qualifies for CCT re-assessment after a war, first contact, Sacred Ground event, or territorial shift, or writing/checking narrative claims about a civilization's designation (e.g. Industrial, Solarian, Interstellar, Galactic) against its axis profile. This is canon Part 21, Area 4, domain society.
user-invocable: false
---

## Rule Text (Verbatim Source — Authoritative)
## Area 4 — CCT Synthesis Formula

### 4.1 — The Axis Minimum Rule

The Composite Civilization Tier is bounded from above by the lowest single axis value, subject to a tolerance:

**Rule 4.1.1 — Hard Floor:** No CCT can exceed the lowest axis value by more than 2 tiers. If a civilization's lowest axis is LA-3, its maximum achievable CCT is CCT-5 regardless of all other axis values.

**Rule 4.1.2 — Soft Pull:** If two or more axes are at the minimum value (tied for lowest), the CCT cannot exceed the lowest by more than 1 tier.

**Rule 4.1.3 — SA Special Case:** SA-0 does not hard-cap the CCT. A civilization with SA-0 (pure cultivation or pure technology) may still achieve high CCT, but with a CCT cap of [average of the four non-SA axes], rounded down. SA-0 civilizations cannot exceed CCT-14 under any circumstances — at extreme cosmic scales, the inability to integrate becomes a structural limitation.

### 4.2 — The Synthesis Formula

Let the five axis values be: CA, TA, EA, LA, SA (where SA counts as zero if SA-0).

**Step 1 — Weighted Average:**

> Base = (CA × 0.25) + (TA × 0.25) + (EA × 0.20) + (LA × 0.20) + (SA × 0.10)

**Step 2 — Axis Gap Penalty:**

Identify the range (max axis − min axis). Apply the following penalty to the Base:
- Range 0–2: No penalty.
- Range 3–4: −0.5 to Base.
- Range 5–6: −1.0 to Base.
- Range 7–9: −2.0 to Base.
- Range 10+: −3.0 to Base.

**Step 3 — Synthesis Floor Check:**

The final CCT = floor(Base − Penalty), subject to Rule 4.1.1 (hard floor cap).

**Step 4 — Rounding and Banding:**

Final CCT is rounded down to the nearest integer. CCT is always expressed as a whole number from 1 to 20.

### 4.3 — Example Synthesis Profiles

| Example Civilization | CA | TA | EA | LA | SA | Base | Penalty | CCT | Designation |
|---|---|---|---|---|---|---|---|---|---|
| Pure-cultivation, pre-industrial | 9 | 2 | 6 | 4 | 0 | 5.3→5.1(SA-0 average) | −2.0 (range 7) | 3 | Industrial |
| Balanced stellar civilization | 8 | 8 | 7 | 7 | 6 | 7.4 | −0.5 (range 2) | 6 | Solarian |
| Technology-dominant galactic entity | 4 | 11 | 10 | 10 | 3 | 7.7 | −2.0 (range 8) | 5 | Multi-World |
| Full synergy stellar civilization | 9 | 9 | 8 | 7 | 8 | 8.3 | 0 (range 2) | 8 | Interstellar |
| Galaxy-spanning balanced tier | 12 | 11 | 11 | 12 | 9 | 11.2 | 0 (range 1) | 11 | Galactic |

### 4.4 — CCT Assessment Cadence

CCT is not a fixed value — civilizations change. For narrative purposes:

**Rule 4.4.1 — Assessment Trigger Events:** CCT re-assessment is triggered by any of: major war outcome, first contact with a new civilization, Sacred Ground formation or destruction, technology tier breakthrough, mass cultivation advancement event, territorial conquest or loss exceeding 25% of LA basis.

**Rule 4.4.2 — CCT Lag:** Civilizational tier change does not happen overnight. A CCT advancement requires the new axis threshold to have been sustained for no less than two generations (Part 9 timing referenced). An individual breakthrough does not advance the civilization's CA — the distribution must change.

**Rule 4.4.3 — Author Reference Use:** For narrative purposes, authors assign CCT at the time of first depiction and note any significant axis changes within a book's timeline.

---

## Cross-References
| Related Skill | Relation | Source |
|---|---|---|
| ssc-worlds-p13-foundational-principles-location-law | HARD | Part 34 Area 5: Civilization spatial scope uses Part 13 location hierarchy |
| ssc-worlds-p13-cosmological-architecture | HARD | Part 34 Area 5: Civilization spatial scope uses Part 13 location hierarchy |
| ssc-worlds-p13-village-classification-system | HARD | Part 34 Area 5: Civilization spatial scope uses Part 13 location hierarchy |
| ssc-worlds-p13-town-classification-system | HARD | Part 34 Area 5: Civilization spatial scope uses Part 13 location hierarchy |
| ssc-worlds-p13-city-classification-system | HARD | Part 34 Area 5: Civilization spatial scope uses Part 13 location hierarchy |
| ssc-worlds-p13-capital-classification-system | HARD | Part 34 Area 5: Civilization spatial scope uses Part 13 location hierarchy |
| ssc-worlds-p13-kingdom-classification-system | HARD | Part 34 Area 5: Civilization spatial scope uses Part 13 location hierarchy |
| ssc-worlds-p13-empire-classification-system | HARD | Part 34 Area 5: Civilization spatial scope uses Part 13 location hierarchy |
| ssc-worlds-p13-sacred-ground-governance | HARD | Part 34 Area 5: Civilization spatial scope uses Part 13 location hierarchy |
| ssc-worlds-p13-energy-formation-zone-governance | HARD | Part 34 Area 5: Civilization spatial scope uses Part 13 location hierarchy |

## Governing Authority
Subordinate to the shared Part 1 (audit law) + Part 34 (knowledge graph) grounding in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.

## Source Provenance
Part 21, Area 4 — "CCT Synthesis Formula" · canon v4.33 · migrated 2026-08-03
