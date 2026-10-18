---
name: ssc-ledger-p37-additional-ledger-types-from-parts-1
description: Covers the seven additional ledger folder types (Travel Route/Gate, Named Distance Measurement, Affiliation Agreement, Information/Intelligence Asset, Technology Scale Reference, Technology Growth Program, Technology Science Framework) defined by earlier Parts but left unpopulated at Part 37 Canon v1.0 initial authoring, and the mandatory flagging protocol C-38 must follow the first time it discovers an entity of one of these types in prose (since no schema template yet exists for them); reach for this when creating or auditing ledger entries for travel routes, named distances, affiliation agreements, intelligence assets, or technology scale/growth/science entities, or when determining the correct ledger folder name for a newly discovered entity of these types. This is canon Part 37 Area 3, domain ledger.
user-invocable: false
---

## Rule Text (Verbatim Source — Authoritative)
## Area 3 — Additional Ledger Types from Parts 1–37 Review

The following additional ledger folder types are defined by existing Parts but not yet populated with entity files at Part 37's initial authoring (Canon v1.0). C-38 must use these folder names when discovering entities of these types in prose.

| Entity Type | Governing Part | Ledger Folder | Creation Threshold |
|---|---|---|---|
| Travel Route / Gate | Part 15 | `ledger-worlds-travel/` | Named travel route described in prose |
| Named Distance Measurement | Part 14 | `ledger-worlds-distance/` | Named canonical distance established in prose |
| Affiliation Agreement | Part 23 | `ledger-people-society-affiliation/` | Named formal affiliation agreement established |
| Information / Intelligence Asset | Part 24 | `ledger-people-society-information/` | Named intelligence asset with actor-level detail |
| Technology Scale Reference | Part 8/35 | `ledger-technology-scale/` | Named technology scale standard established |
| Technology Growth Program | Part 8 | `ledger-technology-growth/` | Named technology research/growth program introduced |
| Technology Science Framework | Part 8 | `ledger-technology-science/` | Named scientific framework introduced in prose |

**Schema templates for these additional types:** Not yet authored at Part 37 v1.0. When C-38 first discovers an entity of one of these types, it must flag `NEW ENTITY TYPE — schema to be authored in Part 37 Area 3` and request user direction per Area 1.6.

> **[Repo layout note]** `ledger-worlds-travel/` above refers to `.claude/story-memory/ledger-worlds-travel/` in the current repo layout (post-.claude/ migration).
> **[Repo layout note]** `ledger-worlds-distance/` above refers to `.claude/story-memory/ledger-worlds-distance/` in the current repo layout (post-.claude/ migration).
> **[Repo layout note]** `ledger-people-society-affiliation/` above refers to `.claude/story-memory/ledger-people-society-affiliation/` in the current repo layout (post-.claude/ migration).
> **[Repo layout note]** `ledger-people-society-information/` above refers to `.claude/story-memory/ledger-people-society-information/` in the current repo layout (post-.claude/ migration).
> **[Repo layout note]** `ledger-technology-scale/` above refers to `.claude/story-memory/ledger-technology-scale/` in the current repo layout (post-.claude/ migration).
> **[Repo layout note]** `ledger-technology-growth/` above refers to `.claude/story-memory/ledger-technology-growth/` in the current repo layout (post-.claude/ migration).
> **[Repo layout note]** `ledger-technology-science/` above refers to `.claude/story-memory/ledger-technology-science/` in the current repo layout (post-.claude/ migration).

---

## Cross-References
| Related Skill | Relation | Source |
|---|---|---|
| ssc-cultivation-p03-cultivation-ladder-realm-hierarchy | SOFT | Inherited Part-level relation only: Area 3 catalogs seven non-character ledger types (travel route/gate, named distance, affiliation agreement, information asset, technology scale/growth/science) and their folder names — none of which involve character cultivation-realm data, so there is no Area-level dependency on this skill. |
| ssc-cultivation-p03-lifespan-mechanics | SOFT | Inherited Part-level relation only: this Area's non-character ledger types (travel, distance, affiliation, information, technology scale/growth/science) have no lifespan-mechanics content. |
| ssc-cultivation-p03-power-density | SOFT | Inherited Part-level relation only: power-density is not referenced by any of the seven non-character ledger types this Area defines. |
| ssc-cultivation-p03-realm-transition | SOFT | Inherited Part-level relation only: realm-transition mechanics are unrelated to the travel/distance/affiliation/information/technology ledger types cataloged here. |
| ssc-cultivation-p03-cultivation-talent | SOFT | Inherited Part-level relation only: cultivation-talent content has no bearing on this Area's non-character ledger-type definitions. |
| ssc-cultivation-p03-growth-speed | SOFT | Inherited Part-level relation only: cultivation growth-speed is unrelated to the folder/threshold definitions this Area provides for travel, distance, affiliation, information, and technology entities. |
| ssc-cultivation-p03-power-comparison | SOFT | Inherited Part-level relation only: power-comparison content is not part of this Area's scope, which is limited to naming and thresholding seven non-character ledger types. |
| ssc-cultivation-p03-damage-tolerance-recovery | SOFT | Inherited Part-level relation only: damage-tolerance-recovery mechanics play no role in the non-character ledger types this Area defines. |
| ssc-cultivation-p03-affinity-cultivation | SOFT | Inherited Part-level relation only: affinity-cultivation is unrelated to the travel/distance/affiliation/information/technology entity types this Area governs. |
| ssc-cultivation-p03-heart-cultivation | SOFT | Inherited Part-level relation only: heart-cultivation content has no connection to this Area's seven non-character ledger-type definitions. |

## Governing Authority
Subordinate to the shared Part 1 (audit law) + Part 34 (knowledge graph) grounding in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.

## Source Provenance
Part 37, Area 3 — "Additional Ledger Types from Parts 1–37 Review" · canon v4.33 · migrated 2026-08-03
