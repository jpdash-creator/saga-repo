---
name: ssc-ledger-p37-ledger-folder-registry
description: Provides the canonical, complete registry of all Starward Saga ledger folders — their names, their governing schema Area within Part 37, and their current status (Active vs. Defined/schema pending) — with running totals of active vs. pending folders; reach for this whenever an agent needs to enumerate which ledger folders exist, verify a folder name against canon, check whether a given ledger's schema has been finalized or is still pending, or reconcile the ledger directory structure against canon law before creating, renaming, or auditing a ledger folder; this is canon Part 37 Area 4, domain ledger.
user-invocable: false
---

## Rule Text (Verbatim Source — Authoritative)
## Area 4 — Ledger Folder Registry

The following is the canonical complete registry of all ledger folders, their governing schema Areas in this Part, and their current status:

| Folder Name | Schema | Status |
|---|---|---|
| `ledger-character-hero/` | Area 2.3 | Active |
| `ledger-character-villain/` | Area 2.2 | Active |
| `ledger-character-side/` | Area 2.1 | Active |
| `ledger-worlds-location/` | Area 2.4 | Active |
| `ledger-worlds-kingdom-state/` | Area 2.5 | Active |
| `ledger-people-society-faction/` | Area 2.6 | Active |
| `ledger-people-society-civilization/` | Area 2.7 | Active |
| `ledger-energy-relics-artifacts/` | Area 2.8 | Active |
| `ledger-technology-weapon/` | Area 2.9 | Active |
| `ledger-technology-vehicle/` | Area 2.10 | Active |
| `ledger-worlds-travel/` | Area 3 (schema pending) | Defined — schema pending |
| `ledger-worlds-distance/` | Area 3 (schema pending) | Defined — schema pending |
| `ledger-people-society-affiliation/` | Area 3 (schema pending) | Defined — schema pending |
| `ledger-people-society-information/` | Area 3 (schema pending) | Defined — schema pending |
| `ledger-technology-scale/` | Area 3 (schema pending) | Defined — schema pending |
| `ledger-technology-growth/` | Area 3 (schema pending) | Defined — schema pending |
| `ledger-technology-science/` | Area 3 (schema pending) | Defined — schema pending |

**Total active folders with full schemas: 10**
**Total folders with pending schemas: 7**
**Total canonical folder count: 17**

> **[Repo layout note]** `ledger-character-hero/` above refers to `.claude/story-memory/ledger-character-hero/` in the current repo layout (post-.claude/ migration).
> **[Repo layout note]** `ledger-character-villain/` above refers to `.claude/story-memory/ledger-character-villain/` in the current repo layout (post-.claude/ migration).
> **[Repo layout note]** `ledger-character-side/` above refers to `.claude/story-memory/ledger-character-side/` in the current repo layout (post-.claude/ migration).
> **[Repo layout note]** `ledger-worlds-location/` above refers to `.claude/story-memory/ledger-worlds-location/` in the current repo layout (post-.claude/ migration).
> **[Repo layout note]** `ledger-worlds-kingdom-state/` above refers to `.claude/story-memory/ledger-worlds-kingdom-state/` in the current repo layout (post-.claude/ migration).
> **[Repo layout note]** `ledger-people-society-faction/` above refers to `.claude/story-memory/ledger-people-society-faction/` in the current repo layout (post-.claude/ migration).
> **[Repo layout note]** `ledger-people-society-civilization/` above refers to `.claude/story-memory/ledger-people-society-civilization/` in the current repo layout (post-.claude/ migration).
> **[Repo layout note]** `ledger-energy-relics-artifacts/` above refers to `.claude/story-memory/ledger-energy-relics-artifacts/` in the current repo layout (post-.claude/ migration).
> **[Repo layout note]** `ledger-technology-weapon/` above refers to `.claude/story-memory/ledger-technology-weapon/` in the current repo layout (post-.claude/ migration).
> **[Repo layout note]** `ledger-technology-vehicle/` above refers to `.claude/story-memory/ledger-technology-vehicle/` in the current repo layout (post-.claude/ migration).
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
| ssc-cultivation-p03-cultivation-ladder-realm-hierarchy | SOFT | Inherited Part-level relation only: Area 4 is a flat registry of ledger folder names, governing schema Areas, and Active/Defined status — it carries no schema-field content itself, so it has no Area-level dependency on cultivation-realm mechanics (that dependency, if any, belongs to Area 2's schema templates). |
| ssc-cultivation-p03-lifespan-mechanics | SOFT | Inherited Part-level relation only: the folder registry lists names and status, not lifespan-mechanics fields, so there is no genuine dependency here. |
| ssc-cultivation-p03-power-density | SOFT | Inherited Part-level relation only: power-density content is not part of a folder-name/status registry. |
| ssc-cultivation-p03-realm-transition | SOFT | Inherited Part-level relation only: realm-transition mechanics are not tracked by this Area's folder registry. |
| ssc-cultivation-p03-cultivation-talent | SOFT | Inherited Part-level relation only: cultivation-talent content has no place in a folder-name/status registry. |
| ssc-cultivation-p03-growth-speed | SOFT | Inherited Part-level relation only: growth-speed mechanics are unrelated to enumerating folder names and their schema/status. |
| ssc-cultivation-p03-power-comparison | SOFT | Inherited Part-level relation only: power-comparison content plays no role in this Area's registry of folder names and statuses. |
| ssc-cultivation-p03-damage-tolerance-recovery | SOFT | Inherited Part-level relation only: damage-tolerance-recovery mechanics are not reflected in the folder registry. |
| ssc-cultivation-p03-affinity-cultivation | SOFT | Inherited Part-level relation only: affinity-cultivation content is outside the scope of a folder-name/status registry. |
| ssc-cultivation-p03-heart-cultivation | SOFT | Inherited Part-level relation only: heart-cultivation content has no bearing on this Area's registry of folder names and statuses. |

## Governing Authority
Subordinate to the shared Part 1 (audit law) + Part 34 (knowledge graph) grounding in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.

## Source Provenance
Part 37, Area 4 — "Ledger Folder Registry" · canon v4.33 · migrated 2026-08-03
