---
name: ssc-ledger-p37-schema-templates
description: Defines the exact Markdown schema templates for every ledger type in the Starward Saga canon system — Side Character, Villain, Hero, Location, Kingdom-State, Faction, Civilization, Energy-Relics/Artifacts, Technology-Weapon, and Technology-Vehicle ledgers — including file locations, governing canon parts, section structures, and B/L (Baseline/Living) update annotations; reach for this whenever creating a new ledger file, auditing an existing ledger's structure for compliance, or determining which fields and sections a given ledger type must contain; this is canon Part 37 Area 2, domain ledger.
user-invocable: false
---

## Rule Text (Verbatim Source — Authoritative)
## Area 2 — Schema Templates

### 2.1 — Schema Template: Side Character Ledger

**File location:** `ledger-character-side/[name].md`
**Governing Canon Parts:** Parts 1 (Area 5.4), 3, 4, 5, 6 (Area 12), 7, 8, 16, 17, 19, 20, 21, 22, 23, 26, 27, 31
**Ledger Type:** Side Character

> **[Repo layout note]** `ledger-character-side/[name].md` above refers to `.claude/story-memory/ledger-character-side/[name].md` in the current repo layout (post-.claude/ migration).

---

```markdown
# [NAME] — Side Character Ledger

**Governing Canon Parts:** [list]
**Ledger Type:** Side Character — Tier [A / B / C] (Part 19)
**First Prose Appearance:** [Prose NNNNN — Title (Ref: P.S.P.C.A.NNNNN)]
**Last Updated:** [YYYY-MM-DD]
**Ledger Version:** v1.0

---

## Section 1 — Identity Baseline (B)

**Full Name:** [full name as established in prose]
**Aliases / Titles / Epithets:** [or "not yet established"]
**Age at Story Start:** [or "not yet established"]
**Gender:** [or "not yet established"]
**Species:** [Human / other]
**Cultural Origin (CPT per Part 25):** [kingdom/region/system — or "not yet established"]
**Physical Description:** [from prose — or "not yet established"]
**Voice Register (per Part 29):** [not yet established]

---

## Section 2 — Classification (B/L)

**Cultivation Realm (Part 3):** [realm + level — or "not yet established"]
**CC-Class (Part 16):** [or "not yet established"]
**Technology Tier (Part 8):** [or "not yet established"]
**Soul Talent (Part 4):** [or "not yet established"]
**Affinity Type(s) (Part 4):** [or "not yet established"]
**Combat Level Advantage (Part 3/5):** [or "not yet established"]
**Cultivation Affinity % (CA):** [or "not yet established"]
**Technology Affinity % (TA):** [or "not yet established"]
**CS% (Part 31 Area 21):** [or "not yet established"]
**TS% (Part 31 Area 21):** [or "not yet established"]

*[L — Updated at every breakthrough, classification change, or CS%/TS%-triggering event]*

---

## Section 3 — Power and Capability Snapshot (B/L)

**Signature Named Moves (Part 6):**
- [Move name] — [substrate, combat function, mastery grade — or "none observed"]

**Innate Moves (Part 6 Area 12):**
- [(none registered) or (species-innate move details)]

**Known Weapon Systems:** [or "not yet established"]
**Effective Combat Range:** [or "not yet established"]

*[L — Updated at every significant power change or Named Move event]*

---

## Section 4 — Ideology Profile (B/L)

**Primary Ideology Category (Part 20):** [or "not yet established"]
**Moral Orientation:** [or "not yet established"]
**Core Belief:** [what they would die for — from prose evidence — or "not yet established"]
**Operational Belief:** [how they act day-to-day — or "not yet established"]

*[L — Updated at every IE-3+ event or IS-state change]*

---

## Section 5 — Psychological Profile (B/L)

**PIS Level (Part 26):** [or "not yet established"]
**Active Psychological Wounds:** [or "not yet established"]
**Psychological Archetype (Part 18 — villains only):** N/A — Side Character classification
**Heart Orientation (Part 4):** [or "not yet established"]

*[L — Updated at every PIS-3+ change or new wound event]*

---

## Section 6 — Consequence Arc (B/L)

**Active CSS Events (Part 27):** [or "none established at story start"]
**CSS Debt Summary:** [or "none established"]
**Accumulated Consequence Weight:** [Baseline]

*[L — Updated after every CSS-3+ event]*

---

## Section 7 — Relationships and Faction Positions (B/L)

**Faction Affiliation (Part 22):** [or "not yet established"]
**Affiliation Bonds (Part 23):** [or "not yet established"]
**Allies:** [or "not yet established"]
**Antagonists:** [or "not yet established"]

*[L — Updated at every significant relationship change or faction event]*

---

## Section 8 — Resources and Possessions (B/L)

**Named Relics (Part 12):** [or "none yet established"]
**Named Weapons (Part 33):** [or "none yet established"]
**Named Vehicles (Part 32):** [or "none yet established"]
**CPM Holdings (Part 11):** [or "not yet established"]

*[L — Updated when resources are gained, lost, or significantly altered]*

---

## Section 9 — Narrative Role and Arc Status (B/L)

**Side Character Tier (Part 19):** Tier [A / B / C]
**Narrative Function:** [from prose — or "not yet established"]
**Arc Trajectory:** [from prose evidence — or "not yet established"]
**Survival Status:** Active

*[L — Updated at every arc phase transition or status change]*

---

## Section 10 — Canon Events Log (L)

| Prose Reference | Event Summary | Parts Triggered | Sections Updated |
|---|---|---|---|
| [P.S.P.C.A.NNNNN — Title] | [event summary] | [Parts] | [sections] |
```

---

### 2.2 — Schema Template: Villain Ledger

**File location:** `ledger-character-villain/[name].md`
**Governing Canon Parts:** Parts 1 (Area 5.4), 3, 4, 5, 6 (Area 12), 7, 8, 16, 17, 18, 20, 21, 22, 23, 26, 27, 31

> **[Repo layout note]** `ledger-character-villain/[name].md` above refers to `.claude/story-memory/ledger-character-villain/[name].md` in the current repo layout (post-.claude/ migration).

---

The Villain Ledger schema follows the identical 10-Section structure as the Side Character schema (Area 2.1) with the following modifications:

- **Section 1 Ledger Type header:** `Villain — [Arc / Series / Faction-Villain type]`
- **Section 5 Psychological Archetype (Part 18):** Active field — must be populated from prose evidence with one of: Armored / Consumed / Calcified / Fractured / Hollow per Part 18
- **Section 9:** Replaces "Side Character Tier" with `**Villain Arc Type (Part 18):**` and `**Villain Narrative Tier:**` [Arc Villain / Series Villain / Faction Villain / Thematic Villain]
- **All narrative summary paragraphs (3b):** AI-authored in full from prose evidence; no user instruction required

---

### 2.3 — Schema Template: Hero Ledger

**File location:** `ledger-character-hero/[name].md`
**Governing Canon Parts:** Parts 1 (Area 5.4), 3, 4, 5, 6 (Area 12), 7, 8, 16, 17, 20, 21, 22, 23, 26, 27, 30, 31
**Special rule:** Hero ledger files are user-designated; C-38 never auto-creates them. See Part 37 Area 1.2 Threshold C-3.

> **[Repo layout note]** `ledger-character-hero/[name].md` above refers to `.claude/story-memory/ledger-character-hero/[name].md` in the current repo layout (post-.claude/ migration).

---

The Hero Ledger schema follows the identical 10-Section structure as the Side Character schema (Area 2.1) with the following modifications:

- **Section 1 Ledger Type header:** `Hero — Co-Equal Protagonist` (or as designated)
- **Section 2:** Includes Phase 1 End-State Power Level and Phase 1 End-State Age blocks (Locked Canon per Part 30 Section 1.3.1)
- **Section 9:** Replaces "Side Character Tier" with `**Hero Arc Phase (Part 17):**` and `**Hero Arc Archetype:**`; adds `**PHASE 1 END-STATE POWER LEVEL (Locked Canon):**` block and `**PHASE 1 END-STATE AGE (Locked Canon):**` block

---

### 2.4 — Schema Template: Location Ledger

**File location:** `ledger-worlds-location/[name].md`
**Governing Canon Parts:** Parts 13, 14, 15, 21, 22, 25, 31
**Creation threshold:** Threshold L-1 (Area 1.3)

> **[Repo layout note]** `ledger-worlds-location/[name].md` above refers to `.claude/story-memory/ledger-worlds-location/[name].md` in the current repo layout (post-.claude/ migration).

---

```markdown
# [NAME] — Location Ledger

**Governing Canon Parts:** [list]
**Location Tier (Part 13):** [Sub-World location / World / Star System / Cluster / Quadrant / Galaxy]
**First Prose Appearance:** [Prose NNNNN — Title (Ref: P.S.P.C.A.NNNNN)]
**Last Updated:** [YYYY-MM-DD]
**Ledger Version:** v1.0

---

## Section 1 — Identity and Classification (B)

**Full Name:** [canonical name]
**Common Name / Aliases:** [or "not yet established"]
**Location Tier (Part 13):** [tier classification]
**Cosmological Area (Part 13):** [area classification]
**Part 13 Character:** [cultivation-dominant / technology-dominant / mixed / other]
**Sacred Ground Status (Part 13 Area 14):** [Yes/No — Grade if Yes — or "not yet established"]
**Containing World:** [or "not yet established"]
**Containing Star System:** [or "not yet established"]
**Physical Description:** [from prose]
**Cultural Association (Part 25):** [or "not yet established"]

---

## Section 2 — Spatial Data (B/L)

**Distance from Key Reference Points (Part 14 CMS):** [or "not yet established"]
**Travel Time from Key Points (Part 15):** [or "not yet established"]
**Ambient Energy Class (Part 11):** [Class 1–7 — or "not yet established"]
**Dominant Affinity Presence (Part 4):** [or "not yet established"]
**Cultivation Synergy % (CS%) (Part 31 Area 21):** [or "not yet established"]
**Technology Synergy % (TS%) (Part 31 Area 21):** [or "not yet established"]

*[L — CS%/TS% updated as location's civilizational balance shifts]*

---

## Section 3 — Faction/Civilization Control (B/L)

**Controlling Faction(s):** [or "not yet established"]
**Contested Status:** [or "not yet established"]
**Known Characters Present:** [or "not yet established"]

*[L — Updated at every control change, character arrival/departure, or battle event]*

---

## Section 4 — Events Log (L)

| Prose Reference | Event Summary | Parts Triggered | Sections Updated |
|---|---|---|---|
| [ref] | [summary] | [Parts] | [sections] |

---

## Section 5 — Lore (Part 28 Area 17)

**Schema:** Part 28 Area 17.2 — [Location Domain tier]
**Depth Standard:** [Breadth-and-Depth per Part 28 Area 17.3]
**Audit Hook:** Part 1 Area 8.13 ALCA dimension AL-10

[Lore subsections populated from prose evidence — geographic, historical, cultural, architectural, sensory signature — as established]
```

---

### 2.5 — Schema Template: Kingdom-State Ledger

**File location:** `ledger-worlds-kingdom-state/[name].md` (or kingdom-state equivalent folder)
**Governing Canon Parts:** Parts 13, 14, 15, 16, 21, 22, 25, 30, 31
**Creation threshold:** Threshold L-2 (Area 1.3)

> **[Repo layout note]** `ledger-worlds-kingdom-state/[name].md` above refers to `.claude/story-memory/ledger-worlds-kingdom-state/[name].md` in the current repo layout (post-.claude/ migration).

---

```markdown
# [NAME] — Kingdom-State Ledger

**Governing Canon Parts:** [list]
**State Type:** [Kingdom / Empire / Sect-Territory / City-State / other]
**First Prose Appearance:** [Prose NNNNN — Title (Ref: P.S.P.C.A.NNNNN)]
**Last Updated:** [YYYY-MM-DD]
**Ledger Version:** v1.0

---

## Section 1 — Identity and Founding (B)

**Full Name:** [canonical name]
**Common Name / Aliases:** [or "not yet established"]
**State Type:** [type classification]
**Governing Philosophy:** [cultivation-dominant / technology-dominant / balanced / other]
**Founding Event:** [or "not yet established"]
**Founder:** [or "not yet established"]
**Founding Oath / Charter:** [or "not yet established"]
**Current Rulers:** [or "not yet established"]
**Territorial Extent:** [from prose — or "not yet established"]
**Capital / Seat of Power:** [or "not yet established"]

---

## Section 2 — Classification (B/L)

**Kingdom Classification (Part 16):** [K-1 through K-5 — or "not yet established"]
**Cultivation Synergy % (CS%) (Part 31):** [or "not yet established"]
**Technology Synergy % (TS%) (Part 31):** [or "not yet established"]
**Dominant Affinity Type (Part 4):** [or "not yet established"]
**Technology Tier Average (Part 8):** [or "not yet established"]
**Firmament Lock ceiling (if applicable):** [or "inherits from containing Sol Star System"]

*[L — CS%/TS% updated as kingdom's civilizational balance shifts]*

---

## Section 3 — Military and Political Power (B/L)

**Military Organization:** [or "not yet established"]
**Cultivation Force Tier:** [or "not yet established"]
**Technology Force Tier:** [or "not yet established"]
**Active Conflicts:** [or "none at story start"]
**Political Posture:** [or "not yet established"]

*[L — Updated at every military event, political crisis, or alliance shift]*

---

## Section 4 — Diplomatic Architecture (B/L)

**Active Treaties:** [treaty name — parties — domain — or "none yet established"]
**Hostile Relationships:** [or "none yet established"]
**Neutral Relationships:** [or "not yet established"]
**Key Diplomatic Events:** [or "none yet established"]

*[L — Updated at every treaty event, alliance shift, or diplomatic crisis]*

---

## Section 5 — Internal Institutions (B/L)

**Cultivation Academies:** [names — or "not yet established"]
**Technology Guilds:** [names — or "not yet established"]
**Information Services (Part 24):** [or "not yet established"]
**Law Enforcement / Internal Security:** [or "not yet established"]

*[L — Updated when institutions are introduced or significantly changed]*

---

## Section 6 — Economy and Resources (B/L)

**Primary Exports:** [or "not yet established"]
**Key Infrastructure:** [or "not yet established"]
**CPM Resource Grade (Part 11):** [or "not yet established"]

*[L — Updated when significant economic events occur]*

---

## Section 7 — Notable Characters (B/L)

**Ruling Characters:** [name — role — cross-ref to character ledger]
**Key NPCs:** [or "not yet established"]

*[L — Updated when characters arrive, depart, die, or change role]*

---

## Section 8 — Events Log (L)

| Prose Reference | Event Summary | Parts Triggered | Sections Updated |
|---|---|---|---|
| [ref] | [summary] | [Parts] | [sections] |

---

## Section 9 — Lore (Part 28 Area 17)

**Schema:** Part 28 Area 17.2 — Kingdom/State tier
**Depth Standard:** Part 28 Area 17.3 — Breadth-and-Depth
**Audit Hook:** Part 1 Area 8.13 ALCA dimension AL-10

[Lore subsections populated from prose evidence — geographic, cultural, architectural, sensory, historical — as established]
```

---

### 2.6 — Schema Template: Faction Ledger

**File location:** `ledger-people-society-faction/[name].md`
**Governing Canon Parts:** Parts 16, 22, 23, 24, 25, 31
**Creation threshold:** Threshold F-1 (Area 1.4)

> **[Repo layout note]** `ledger-people-society-faction/[name].md` above refers to `.claude/story-memory/ledger-people-society-faction/[name].md` in the current repo layout (post-.claude/ migration).

---

```markdown
# [NAME] — Faction Ledger

**Governing Canon Parts:** [list]
**Faction Type:** [Sect / Guild / Military Unit / Political Bloc / Alliance / other]
**First Prose Appearance:** [Prose NNNNN — Title (Ref: P.S.P.C.A.NNNNN)]
**Last Updated:** [YYYY-MM-DD]
**Ledger Version:** v1.0

---

## Section 1 — Identity (B)

**Full Name:** [canonical name]
**Common Name / Aliases:** [or "not yet established"]
**Faction Type (Part 22):** [type classification]
**Founding / Origin:** [or "not yet established"]
**Leadership:** [or "not yet established"]
**Membership Size (approximate):** [or "not yet established"]
**Territory or Base of Operations:** [or "not yet established"]
**Primary Purpose / Mission:** [from prose]

---

## Section 2 — Classification (B/L)

**Faction Tier (Part 22):** [or "not yet established"]
**Cultivation Orientation:** [or "not yet established"]
**Technology Orientation:** [or "not yet established"]
**CS% (Part 31):** [or "not yet established"]
**TS% (Part 31):** [or "not yet established"]

*[L — CS%/TS% updated as faction's orientation shifts]*

---

## Section 3 — Key Members (B/L)

**Leadership Characters:** [cross-ref to character ledger — or "not yet established"]
**Named Members:** [cross-ref to character ledger — or "not yet established"]

*[L — Updated when members join, leave, die, or change role]*

---

## Section 4 — Relationships (B/L)

**Allied Factions:** [or "not yet established"]
**Hostile Factions:** [or "not yet established"]
**Relationship to Hero Group:** [or "not yet established"]

*[L — Updated at every significant faction relationship event]*

---

## Section 5 — Events Log (L)

| Prose Reference | Event Summary | Parts Triggered | Sections Updated |
|---|---|---|---|
| [ref] | [summary] | [Parts] | [sections] |
```

---

### 2.7 — Schema Template: Civilization Ledger

**File location:** `ledger-people-society-civilization/[name].md`
**Governing Canon Parts:** Parts 21, 22, 25, 31
**Creation threshold:** Threshold V-1 (Area 1.4)

> **[Repo layout note]** `ledger-people-society-civilization/[name].md` above refers to `.claude/story-memory/ledger-people-society-civilization/[name].md` in the current repo layout (post-.claude/ migration).

---

```markdown
# [NAME] — Civilization Ledger

**Governing Canon Parts:** [list]
**Civilization Type:** [Human Cultural Group / Species-Civilization / Hybrid-Civilization / other]
**First Prose Appearance:** [Prose NNNNN — Title (Ref: P.S.P.C.A.NNNNN)]
**Last Updated:** [YYYY-MM-DD]
**Ledger Version:** v1.0

---

## Section 1 — Identity (B)

**Full Name:** [canonical name]
**Common Name / Aliases:** [or "not yet established"]
**Civilization Type (Part 21):** [type]
**Geographic Range:** [or "not yet established"]
**Primary Language / Script:** [or "not yet established"]
**Dominant Worldview:** [cultivation-dominant / technology-dominant / pluralist / other]
**Historical Origin:** [or "not yet established"]

---

## Section 2 — Classification (B/L)

**CS% (Part 31):** [civilization-aggregate — or "not yet established"]
**TS% (Part 31):** [civilization-aggregate — or "not yet established"]

*[L — Updated as civilizational balance shifts across prose]*

---

## Section 3 — Cultural Architecture (B/L)

**Core Cultural Values:** [from prose — or "not yet established"]
**Religious / Philosophical Tradition:** [or "not yet established"]
**Governing Political Form:** [or "not yet established"]
**Primary Institutions:** [or "not yet established"]

*[L — Updated when significant cultural events are established in prose]*

---

## Section 4 — Events Log (L)

| Prose Reference | Event Summary | Parts Triggered | Sections Updated |
|---|---|---|---|
| [ref] | [summary] | [Parts] | [sections] |
```

---

### 2.8 — Schema Template: Energy-Relics / Artifacts Ledger

**File location:** `ledger-energy-relics-artifacts/[name].md`
**Governing Canon Parts:** Parts 11, 12, 31
**Creation threshold:** Threshold O-1 (Area 1.5)

> **[Repo layout note]** `ledger-energy-relics-artifacts/[name].md` above refers to `.claude/story-memory/ledger-energy-relics-artifacts/[name].md` in the current repo layout (post-.claude/ migration).

---

```markdown
# [NAME] — Relic / Artifact Ledger

**Governing Canon Parts:** [list]
**Object Type:** [Named Relic / Artifact / Formation Array / Energy Resource Cache]
**First Prose Appearance:** [Prose NNNNN — Title (Ref: P.S.P.C.A.NNNNN)]
**Last Updated:** [YYYY-MM-DD]
**Ledger Version:** v1.0

---

## Section 1 — Identity (B)

**Full Name:** [canonical name]
**Common Name / Aliases:** [or "not yet established"]
**Object Type (Part 12):** [type]
**Physical Description:** [from prose — or "not yet established"]
**Current Holder / Location:** [from prose — or "not yet established"]
**Origin / Forge History:** [or "not yet established"]

---

## Section 2 — Classification (B/L)

**Relic Grade (Part 12):** [or "not yet established"]
**CPM Class (Part 11):** [or "not yet established"]
**Soul Bond Status (Part 12 Area 11):** [or "not yet established"]
**CS% (Part 31):** [or "not yet established"]
**TS% (Part 31):** [or "not yet established"]

*[L — Updated when relic state changes]*

---

## Section 3 — Capabilities (B/L)

**Observed Capabilities (from prose):** [or "not yet established"]
**Limitations:** [or "not yet established"]
**Interaction with Firmament Lock:** [or "not yet established — standard suppression ceiling applies unless noted"]

*[L — Updated each time the relic is used and new capabilities are shown]*

---

## Section 4 — Chain of Custody (L)

| Prose Reference | Holder | Transfer Event | Parts Triggered |
|---|---|---|---|
| [ref] | [holder] | [event] | [Parts] |

---

## Section 5 — Events Log (L)

| Prose Reference | Event Summary | Parts Triggered | Sections Updated |
|---|---|---|---|
| [ref] | [summary] | [Parts] | [sections] |
```

---

### 2.9 — Schema Template: Technology-Weapon Ledger

**File location:** `ledger-technology-weapon/[name].md`
**Governing Canon Parts:** Parts 8, 31, 33
**Creation threshold:** Threshold O-2 (Area 1.5)

> **[Repo layout note]** `ledger-technology-weapon/[name].md` above refers to `.claude/story-memory/ledger-technology-weapon/[name].md` in the current repo layout (post-.claude/ migration).

---

```markdown
# [NAME] — Technology Weapon Ledger

**Governing Canon Parts:** [list]
**Weapon Type:** [Sword / Ranged / Siege / Hybrid / other — Part 33]
**First Prose Appearance:** [Prose NNNNN — Title (Ref: P.S.P.C.A.NNNNN)]
**Last Updated:** [YYYY-MM-DD]
**Ledger Version:** v1.0

---

## Section 1 — Identity (B)

**Full Name:** [canonical name]
**Common Name / Aliases:** [or "not yet established"]
**Weapon Type (Part 33):** [type]
**Physical Description:** [from prose — or "not yet established"]
**Current Wielder / Location:** [from prose — or "not yet established"]
**Technology Integration Level (Part 8):** [or "not yet established"]
**Cultivation Integration:** [or "not yet established"]

---

## Section 2 — Classification (B/L)

**Weapon Grade (Part 33):** [or "not yet established"]
**CS% (Part 31):** [or "not yet established"]
**TS% (Part 31):** [or "not yet established"]
**Authorization Level Required (Part 33 Area 11):** [or "not yet established"]

*[L — Updated when weapon's state or classification changes]*

---

## Section 3 — Capabilities and Combat Profile (B/L)

**Observed Capabilities (from prose):** [or "not yet established"]
**Named Techniques / Modes:** [or "not yet established"]
**Known Limitations:** [or "not yet established"]

*[L — Updated each time the weapon is used in combat]*

---

## Section 4 — Events Log (L)

| Prose Reference | Event Summary | Parts Triggered | Sections Updated |
|---|---|---|---|
| [ref] | [summary] | [Parts] | [sections] |
```

---

### 2.10 — Schema Template: Technology-Vehicle Ledger

**File location:** `ledger-technology-vehicle/[name].md`
**Governing Canon Parts:** Parts 8, 14, 15, 31, 32
**Creation threshold:** Threshold O-3 (Area 1.5)

> **[Repo layout note]** `ledger-technology-vehicle/[name].md` above refers to `.claude/story-memory/ledger-technology-vehicle/[name].md` in the current repo layout (post-.claude/ migration).

---

```markdown
# [NAME] — Technology Vehicle Ledger

**Governing Canon Parts:** [list]
**Vehicle Type:** [Aerial / Ground / Aquatic / Space / Hybrid — Part 32]
**First Prose Appearance:** [Prose NNNNN — Title (Ref: P.S.P.C.A.NNNNN)]
**Last Updated:** [YYYY-MM-DD]
**Ledger Version:** v1.0

---

## Section 1 — Identity (B)

**Full Name:** [canonical name]
**Common Name / Aliases:** [or "not yet established"]
**Vehicle Type (Part 32):** [type]
**Physical Description:** [from prose — or "not yet established"]
**Current Operator / Location:** [from prose — or "not yet established"]
**Technology Tier (Part 8):** [or "not yet established"]
**Cultivation Integration:** [or "not yet established"]

---

## Section 2 — Classification (B/L)

**Vehicle Grade (Part 32):** [or "not yet established"]
**CS% (Part 31):** [or "not yet established"]
**TS% (Part 31):** [or "not yet established"]
**Travel Range and Capacity (Part 14/15):** [or "not yet established"]

*[L — Updated when vehicle's state or classification changes]*

---

## Section 3 — Capabilities (B/L)

**Observed Capabilities (from prose):** [or "not yet established"]
**Armament / Defense Systems:** [or "not yet established"]
**Known Limitations:** [or "not yet established"]

*[L — Updated each time the vehicle is used and new capabilities are shown]*

---

## Section 4 — Events Log (L)

| Prose Reference | Event Summary | Parts Triggered | Sections Updated |
|---|---|---|---|
| [ref] | [summary] | [Parts] | [sections] |
```

## Cross-References
| Related Skill | Relation | Source |
|---|---|---|
| ssc-cultivation-p03-cultivation-ladder-realm-hierarchy | HARD | Part 34 Area 5: Character schema templates include Cultivation Realm field (Part 3 definitions) |
| ssc-cultivation-p03-lifespan-mechanics | HARD | Part 34 Area 5: Character schema templates include Cultivation Realm field (Part 3 definitions) |
| ssc-cultivation-p03-power-density | HARD | Part 34 Area 5: Character schema templates include Cultivation Realm field (Part 3 definitions) |
| ssc-cultivation-p03-realm-transition | HARD | Part 34 Area 5: Character schema templates include Cultivation Realm field (Part 3 definitions) |
| ssc-cultivation-p03-cultivation-talent | HARD | Part 34 Area 5: Character schema templates include Cultivation Realm field (Part 3 definitions) |
| ssc-cultivation-p03-growth-speed | HARD | Part 34 Area 5: Character schema templates include Cultivation Realm field (Part 3 definitions) |
| ssc-cultivation-p03-power-comparison | HARD | Part 34 Area 5: Character schema templates include Cultivation Realm field (Part 3 definitions) |
| ssc-cultivation-p03-damage-tolerance-recovery | HARD | Part 34 Area 5: Character schema templates include Cultivation Realm field (Part 3 definitions) |
| ssc-cultivation-p03-affinity-cultivation | HARD | Part 34 Area 5: Character schema templates include Cultivation Realm field (Part 3 definitions) |
| ssc-cultivation-p03-heart-cultivation | HARD | Part 34 Area 5: Character schema templates include Cultivation Realm field (Part 3 definitions) |

## Governing Authority
Subordinate to the shared Part 1 (audit law) + Part 34 (knowledge graph) grounding in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.

## Source Provenance
Part 37, Area 2 — "Schema Templates" · canon v4.33 · migrated 2026-08-03
