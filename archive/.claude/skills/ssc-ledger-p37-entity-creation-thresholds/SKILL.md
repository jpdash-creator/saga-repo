---
name: ssc-ledger-p37-entity-creation-thresholds
description: Defines the minimum prose-evidence thresholds that must be met before C-38 [FORCE LEDGER AUDIT AND UPDATE] creates a new ledger file for a discovered entity — covering character entities (side character, villain classification question, hero manual-only flag), world/location entities (location, kingdom-state), people/society entities (faction, civilization), object entities (relic/artifact, weapon, vehicle), and the escalation procedure for entity types not covered by the ten established ledger schemas; reach for this whenever an agent is deciding whether a newly-named character, place, faction, civilization, relic, weapon, or vehicle mentioned in prose has met the bar for ledger-file creation, whether a villain-classification question should fire, or how to handle an entity type with no existing schema. This is canon Part 37 Area 1, domain ledger.
user-invocable: false
---

## Rule Text (Verbatim Source — Authoritative)
## Area 1 — Entity Creation Thresholds

### 1.1 — Purpose

The entity creation thresholds define the minimum prose evidence required for C-38 [FORCE LEDGER AUDIT AND UPDATE] to trigger the creation of a new ledger file for a discovered entity. The thresholds are designed to prevent both premature ledger creation (for entities that are merely mentioned in passing) and late creation (for entities that have been canonically established but lack ledger coverage).

### 1.2 — Character Entity Thresholds

**Threshold C-1 — Side Character Ledger Creation.**
A new `ledger-character-side/[name].md` file must be created when: a named character appears in any prose unit with any combination of the following — direct action, spoken dialogue, physical description, or narrative attention from the POV character. A character who is named and present in the scene, even without dialogue, meets this threshold. A character mentioned by name but not present in any prose scene does NOT meet this threshold and is not ledger-eligible until they appear directly.

> **[Repo layout note]** `ledger-character-side/[name].md` above refers to `.claude/story-memory/ledger-character-side/[name].md` in the current repo layout (post-.claude/ migration).

**Threshold C-2 — Villain Classification.**
When a newly-introduced named character's first prose appearance contains any of the following qualifying behaviors — violence, deception, coercion, cruelty, faction-opposition to hero interests, cultivation suppression, or betrayal — C-38 must fire an `AskUserQuestion` before creating their ledger file, asking whether the character should be classified as Villain (ledger-character-villain/) rather than Side Character. This question fires once per character, only at first prose appearance, only when qualifying behavior is present. If the user confirms Villain classification, the file is created in `ledger-character-villain/` instead.

> **[Repo layout note]** `ledger-character-villain/` above refers to `.claude/story-memory/ledger-character-villain/` in the current repo layout (post-.claude/ migration).

**Threshold C-3 — Hero Ledger (Manual Only).**
Hero ledger files (`ledger-character-hero/[name].md`) are never auto-created by C-38. Hero status is user-designated. C-38 may flag a Side Character as a potential Hero candidate for user consideration if their prose weight across multiple units clearly warrants it, but it does not act unilaterally. The flag text is: `⚠ Hero designation consideration: [name] has appeared in [N] prose units with significant protagonist-level narrative weight. User may wish to promote to Hero ledger via explicit instruction.`

> **[Repo layout note]** `ledger-character-hero/[name].md` above refers to `.claude/story-memory/ledger-character-hero/[name].md` in the current repo layout (post-.claude/ migration).

### 1.3 — World and Location Entity Thresholds

**Threshold L-1 — Location Ledger Creation.**
A new `ledger-worlds-location/[name].md` file must be created when: a named place receives any physical, sensory, or spatial description in any prose unit. A location mentioned by name but not described does NOT meet this threshold. A location named and described (even in one sentence) meets this threshold.

> **[Repo layout note]** `ledger-worlds-location/[name].md` above refers to `.claude/story-memory/ledger-worlds-location/[name].md` in the current repo layout (post-.claude/ migration).

**Threshold L-2 — Kingdom-State Ledger Creation.**
A new `ledger-worlds-kingdom-state/[name].md` file (or equivalent kingdom-state folder) must be created when: any named kingdom, empire, polity, city-state, sect-territory, or governing entity is mentioned by name in any prose unit. Mention by name alone (without physical description) is sufficient for kingdom-state threshold — kingdoms are politically significant even when not physically described.

> **[Repo layout note]** `ledger-worlds-kingdom-state/[name].md` above refers to `.claude/story-memory/ledger-worlds-kingdom-state/[name].md` in the current repo layout (post-.claude/ migration).

### 1.4 — People and Society Entity Thresholds

**Threshold F-1 — Faction Ledger Creation.**
A new `ledger-people-society-faction/[name].md` file must be created when: any named organization, sect, guild, alliance, military unit, political bloc, or formal association is mentioned by name and its existence is confirmed (not merely speculated about) in prose.

> **[Repo layout note]** `ledger-people-society-faction/[name].md` above refers to `.claude/story-memory/ledger-people-society-faction/[name].md` in the current repo layout (post-.claude/ migration).

**Threshold V-1 — Civilization Ledger Creation.**
A new `ledger-people-society-civilization/[name].md` file must be created when: a named civilization, cultural identity, or species-group is described with any cultural, historical, or civilizational characteristic in prose.

> **[Repo layout note]** `ledger-people-society-civilization/[name].md` above refers to `.claude/story-memory/ledger-people-society-civilization/[name].md` in the current repo layout (post-.claude/ migration).

### 1.5 — Object Entity Thresholds

**Threshold O-1 — Relic/Artifact Ledger Creation.**
A new `ledger-energy-relics-artifacts/[name].md` file must be created when: a named relic, artifact, or formation array is described in active use or detailed characterization in any prose unit. Passive mention by name without description does not meet this threshold.

> **[Repo layout note]** `ledger-energy-relics-artifacts/[name].md` above refers to `.claude/story-memory/ledger-energy-relics-artifacts/[name].md` in the current repo layout (post-.claude/ migration).

**Threshold O-2 — Weapon Ledger Creation.**
A new `ledger-technology-weapon/[name].md` file must be created when: a named weapon is described in active use in any prose unit. A weapon referenced by name but not used in the prose does not meet this threshold.

> **[Repo layout note]** `ledger-technology-weapon/[name].md` above refers to `.claude/story-memory/ledger-technology-weapon/[name].md` in the current repo layout (post-.claude/ migration).

**Threshold O-3 — Vehicle Ledger Creation.**
A new `ledger-technology-vehicle/[name].md` file must be created when: a named vehicle is described in active use or detailed physical characterization in any prose unit.

> **[Repo layout note]** `ledger-technology-vehicle/[name].md` above refers to `.claude/story-memory/ledger-technology-vehicle/[name].md` in the current repo layout (post-.claude/ migration).

### 1.6 — New Entity Type Discovery

When C-38 identifies a named entity that does not fit any of the ten established ledger types (Side Character, Villain, Hero, Location, Kingdom-State, Faction, Civilization, Relic/Artifact, Weapon, Vehicle), C-38 must:
1. Cross-reference Parts 1–37 to identify the governing Part for this entity type
2. Determine the correct ledger folder name using the `ledger-[domain]-[type]/` convention
3. Flag the new entity type in the C-38 preview as `NEW ENTITY TYPE — requires Part 37 schema definition before file creation`
4. Request user direction before creating any file for this entity type
5. Once user confirms, add the schema to Part 37 Area 2 or later and create the ledger folder with `_index.md`

---

## Cross-References
| Related Skill | Relation | Source |
|---|---|---|
| ssc-cultivation-p03-cultivation-ladder-realm-hierarchy | SOFT | Inherited Part-level relation only: Area 1 governs prose-evidence thresholds for *when* to create a ledger file (dialogue, action, description, mention), not the cultivation-realm data those files later store — that field-level dependency belongs to Area 2's schema templates (ssc-ledger-p37-schema-templates), not to this Area. |
| ssc-cultivation-p03-lifespan-mechanics | SOFT | Inherited Part-level relation only: Area 1's thresholds are about prose-evidence sufficiency for ledger creation, not lifespan mechanics; no Area-level dependency exists here. |
| ssc-cultivation-p03-power-density | SOFT | Inherited Part-level relation only: Area 1 does not consume or reference power-density mechanics — it only defines the evidentiary bar for creating a character/entity ledger file. |
| ssc-cultivation-p03-realm-transition | SOFT | Inherited Part-level relation only: realm-transition mechanics play no role in deciding whether an entity has met the ledger-creation threshold. |
| ssc-cultivation-p03-cultivation-talent | SOFT | Inherited Part-level relation only: cultivation-talent content is unrelated to the prose-evidence thresholds this Area defines for ledger-file creation. |
| ssc-cultivation-p03-growth-speed | SOFT | Inherited Part-level relation only: growth-speed mechanics are not referenced by or relevant to Area 1's entity-creation thresholds. |
| ssc-cultivation-p03-power-comparison | SOFT | Inherited Part-level relation only: power-comparison content has no bearing on when Area 1 says a ledger file should be created. |
| ssc-cultivation-p03-damage-tolerance-recovery | SOFT | Inherited Part-level relation only: damage-tolerance-recovery mechanics are outside the scope of Area 1's creation-threshold rules. |
| ssc-cultivation-p03-affinity-cultivation | SOFT | Inherited Part-level relation only: affinity-cultivation content does not factor into the prose-evidence thresholds this Area sets for ledger creation. |
| ssc-cultivation-p03-heart-cultivation | SOFT | Inherited Part-level relation only: heart-cultivation content is not part of what Area 1's entity-creation thresholds test for. |

## Governing Authority
Subordinate to the shared Part 1 (audit law) + Part 34 (knowledge graph) grounding in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.

## Source Provenance
Part 37, Area 1 — "Entity Creation Thresholds" · canon v4.33 · migrated 2026-08-03
