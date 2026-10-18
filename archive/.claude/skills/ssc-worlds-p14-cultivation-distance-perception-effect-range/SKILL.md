---
name: ssc-worlds-p14-cultivation-distance-perception-effect-range
description: Defines the canonical distance mechanics for cultivator perception and technique effect propagation — the Soul Sense Active Range table by Realm/Heavenly Scale Grade (4.1), environmental and active-suppression modifiers with the full stacking priority and floor/cap rules (4.2), and the Cultivation Technique Effect Propagation Distance table plus special technique classes for Soul Attacks, Formation Attacks, and Space-Folding (4.3). Reach for this Area whenever an agent is writing or auditing a scene involving a cultivator sensing/detecting entities or terrain at range, calculating soul sense range under environmental or suppression conditions (including stacking multiple modifiers), determining how far a technique or area-effect attack can reach given a cultivator's realm, resolving soul-attack range (perception-gated) or formation-attack range (array-tier-gated), or converting weapon/engagement ranges in combat scenes (Part 5/Part 34 Area 5) into canonical CMS distance units. This is canon Part 14, Area 4, domain worlds.
user-invocable: false
---

## Rule Text (Verbatim Source — Authoritative)
## Area 4 — Cultivation Distance Perception and Effect Range

### 4.1 — Soul Sense Active Range by Realm

Soul sense range (Part 3, Area 14; Part 4, Area 2) defines the maximum distance at which a cultivator can actively extend their perception to detect entities, formations, energy anomalies, and spatial features. These are the canonical maximums under standard conditions (ambient energy Class 2–3, no active suppression, unobstructed terrain).

| Realm Stage | Heavenly Scale Grade | Maximum Active Soul Sense Range (Standard) | Maximum Passive Awareness Range | Notes |
|---|---|---|---|---|
| Mortal Tier 1 (all stages) | Grade 0 | None — no soul sense | Touch-range physical | No soul sense; perception is biological only |
| Mortal Tier 2: Senior | Grade 1 | ~5–10 m | ~20 m | Faint qi-sense only; detects cultivation energy at close range |
| Mortal Tier 2: Warrior | Grade 2 | ~50 m | ~100 m | Detects active techniques and aura at combat range |
| Mortal Tier 2: Champion | Grade 3 | ~200 m | ~500 m | Can distinguish active cultivation from passive in range |
| Mortal Tier 2: Ruler | Grade 4 | ~500 m | ~1 km | Detects formation array edges at range |
| Mortal Tier 2: Monarch | Grade 5 | ~1–2 km | ~5 km | Senses terrain energy patterns; full battlefield awareness |
| Xiantian: Demigod | Grade 6 | ~5–10 km | ~20 km | Detects Sacred Ground fringe energy at this range |
| Xiantian: Void God | Grade 7 | ~20–30 km | ~50 km | Formation arrays in range are readable in rough architecture |
| Xiantian: True God | Grade 8 | ~50–80 km | ~100 km | Detects spiritual entities at extreme range |
| Xiantian: Absolute God | Grade 9 | ~100–150 km | ~200 km | Continental perimeter awareness beginning |
| Core Formation: Core Formation | Grade 10 | ~200–300 km | ~500 km | Detects planetary-scale energy currents |
| Core Formation: Core Assimilation | Grade 11 | ~500–800 km | ~1,000–1,500 km | Full Kingdom-scale soul sense coverage |
| Core Formation: Core Solidification | Grade 12 | ~1,000–1,500 km | ~2,000 km | Reads terrain cultivation energy at regional scale |
| Divine: Divine Transformation | Grade 13 | ~5,000–10,000 km | ~15,000 km | Continental-scale soul sense; reads formation arrays at distance |
| Divine: Sea Formation | Grade 14 | ~20,000–30,000 km | ~50,000 km | Planetary-scale awareness; perceives orbital structures at limits |
| Divine: Heaven Treading | Grade 15 | ~50,000–100,000 km | ~150,000 km | Near-full planet surface awareness possible; detects life patterns |
| Divine: Divine Ascension | Grade 16 | ~100,000–200,000 km | Full planet surface | Near-full planetary soul sense coverage |
| Divine: Divine Sea Realm | Grade 17 | Full planet surface | ~0.001–0.01 AU (several hundred thousand km) | True planetary soul sense; orbital awareness at limit |

---

### 4.2 — Soul Sense Range Modifiers

**Environmental Modifiers:**
| Ambient Energy Class | Soul Sense Range Modifier |
|---|---|
| Class 0 (Absolute Void) | −80% (devastating suppression; survival itself is the concern) |
| Class 1 (Minimal) | −20% |
| Class 2 (Low) | Standard (0% modifier) |
| Class 3 (Moderate) | +10% |
| Class 4 (High) | +20% |
| Class 5 (Intense) | +35% |
| Class 6 (Extreme) | +50% |
| Class 7 (Sacred Ground) | +70%; qualitative improvement in resolution at all ranges |

**Active Suppression and Interference:**
| Condition | Soul Sense Range Modifier |
|---|---|
| Suppression formation active (Part 12 Tier 2+) | −50% within the formation |
| Void Zone proximity (within 1 km) | −60% |
| Active combat energy saturation (battlefield) | −20% (noise masking) |
| Competing high-realm soul sense (within range) | Variable; contested by Part 5 rules if in combat |
| Dimensional boundary present | −40% beyond the boundary |
| FTL space / hyperspace equivalent | Soul sense non-functional — dimensional substrate inaccessible |

**Soul Sense Modifier Stacking Rules (Rule 4.2.1):**
Multiple soul sense modifiers from different categories stack according to the following priority and floor rules:

1. **Hard suppression modifiers first:** The "Soul sense non-functional" condition (FTL space) is absolute — no other modifier interacts with it. If FTL applies, the result is always non-functional regardless of enhancements.

2. **Category stacking:** Modifiers from different categories (Environmental, Active Suppression/Interference, and enhancements) stack additively. A cultivator in a Class 6 Extreme environment (+50%) inside an active suppression formation (−50%) has 0% net modification from standard (the two effects cancel).

3. **Maximum suppression floor:** Stacked suppression modifiers cannot reduce soul sense range below **5% of the cultivator's standard range at their realm** — soul sense retains minimal residual function at this floor. This floor is the "bare existence sense" that all but completely suppressed soul cultivators retain. The only exceptions are hard suppression (FTL space) and artificially constructed absolute suppression formations at Tier 4+ specifically designed to eliminate all soul sense — those are below-floor exceptions that must be explicitly designated.

4. **Enhancement cap:** Stacked enhancement modifiers from multiple simultaneous positive sources (e.g., Sacred Ground + high ambient energy zone + exceptional personal soul rung) are capped at **+100% above standard** — effective doubling of baseline range. Higher soul rungs already incorporate advanced range; stacked environmental bonuses cannot multiply a cultivator's range indefinitely.

5. **Competing high-realm soul sense resolution:** When two soul sense fields overlap in contested space (Part 5 combat), the higher soul rung cultivator projects normally; the lower-rung cultivator experiences a −15% to −40% interference penalty scaled to the soul rung gap (≤2 rung gap: −15%; 3–5 rung gap: −25%; >5 rung gap: −40%). This is not a mutual modifier — only the lower-rung cultivator's effective range is reduced.

6. **Example stacking:** A Xiantian cultivator (standard range ~80 km at True God) in a battlefield with active combat saturation (−20%), near a Void Zone (−60%), and inside a Tier 2 suppression formation (−50%) would calculate: 80 km × (1 − 0.20 − 0.60 − 0.50) = 80 km × (−0.30) → floor applies → 80 km × 0.05 = 4 km residual soul sense. The cultivator is severely limited but not blind.

---

### 4.3 — Cultivation Technique Effect Propagation Distance

Cultivation techniques project their effects at distances governed by the technique type, the cultivator's realm, and the technique's Grade. This Area establishes the maximum distance at which a technique's output reaches a target — governed jointly with Part 6 (Move Taxonomy Law) for technique classification and Part 3 (Area 20) for Grade-based footprint.

**General Principle — Technique Range Scales with Realm:**
| Realm | Maximum Direct Technique Projection Range | Maximum Area-Effect Radius |
|---|---|---|
| Mortal Tier 1 | Touch / melee range only (meters) | None |
| Mortal Tier 2: Senior–Warrior | ~10–50 m | ~10 m |
| Mortal Tier 2: Champion–Ruler | ~100–500 m | ~50 m |
| Mortal Tier 2: Monarch | ~1–2 km | ~200 m |
| Xiantian: Demigod–Void God | ~5–30 km | ~1–5 km |
| Xiantian: True–Absolute God | ~50–150 km | ~5–20 km |
| Core Formation | ~100–1,000 km | ~100–500 km |
| Divine Transformation–Sea Formation | ~5,000 km – ~20,000 km | ~1,000–5,000 km |
| Heaven Treading–Divine Ascension | ~30,000–80,000 km | ~10,000–30,000 km |
| Divine Sea Realm | Full planet scale | ~50,000–100,000 km |

**Special Technique Classes:**
- **Soul Attacks (Part 4):** Range equals the attacker's soul sense active range — soul attacks travel the soul dimension and are range-gated by perception, not by physical projection
- **Formation Attacks (Part 12 arrays):** Range governed by the array's Tier; Tier 1 = km scale; Tier 2 = hundreds of km; Tier 3 = thousands of km; Tier 4 = planetary/orbital scale
- **Space-Folding and Spatial Techniques:** Not subject to standard range — governed by Part 15 (Travel Law) for fold mechanics; Part 14 governs the canonical distance the fold bridges

---

## Cross-References
| Related Skill | Relation | Source |
|---|---|---|
| ssc-cultivation-p05-foundational-principles-governing-mandate | HARD | Part 34 Area 5: Weapon ranges in combat use Part 14 CMS units |
| ssc-cultivation-p05-governance-areas-overview | HARD | Part 34 Area 5: Weapon ranges in combat use Part 14 CMS units |
| ssc-cultivation-p05-immutable-principles | HARD | Part 34 Area 5: Weapon ranges in combat use Part 14 CMS units |
| ssc-cultivation-p05-combat-initiation-legitimacy | HARD | Part 34 Area 5: Weapon ranges in combat use Part 14 CMS units |
| ssc-cultivation-p05-escalation-tier-classification-system | HARD | Part 34 Area 5: Weapon ranges in combat use Part 14 CMS units |
| ssc-cultivation-p05-engagement-recognition-mutuality-law | HARD | Part 34 Area 5: Weapon ranges in combat use Part 14 CMS units |
| ssc-cultivation-p05-intensity-containment-boundaries | HARD | Part 34 Area 5: Weapon ranges in combat use Part 14 CMS units |
| ssc-cultivation-p05-third-party-proxy-combat-rules | HARD | Part 34 Area 5: Weapon ranges in combat use Part 14 CMS units |
| ssc-cultivation-p05-battlefield-spatial-cosmological-constraints | HARD | Part 34 Area 5: Weapon ranges in combat use Part 14 CMS units |
| ssc-cultivation-p05-multi-faction-chaos-stabilization | HARD | Part 34 Area 5: Weapon ranges in combat use Part 14 CMS units |

## Governing Authority
Subordinate to the shared Part 1 (audit law) + Part 34 (knowledge graph) grounding in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.

## Source Provenance
Part 14, Area 4 — "Cultivation Distance Perception and Effect Range" · canon v4.33 · migrated 2026-08-03
