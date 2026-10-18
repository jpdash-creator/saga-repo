# ledger-technology-scale — Ledger Index

**Ledger Domain:** Technology — Named Technology Systems and Institutions
**Governed By:** Part 1 Area 5 (Ledger System), Part 8 (Technology Scale Law)
**Template:** Part 1 Area 5.5.10 — Technology-Scale Ledger Format
**Last Updated:** 2026-05-24
**Index Version:** v1.3
**Total Entries:** 1 (Named Technology Systems: 1; Named Technology Institutions: 0)

> **Purpose:** This folder tracks named technology entities introduced in prose that operate at a defined technology tier (Part 8 Scale Law — Tiers 1–20) and require canonical continuity. Two categories of entity:
> - **Named Technology Systems** — specific technology platforms, devices, networks, and facilities that have been named and characterized in prose. Example: a named orbital weapons platform, a named AI system (S1–S5 classification), a named power generation facility.
> - **Named Technology Institutions** — research institutions, technology corporations, guilds, and academies that are introduced with canonical detail. These are distinct from faction ledger entries (which track organizational governance) — this ledger tracks the *technology identity* of an institution: what domains it operates in, what tier it has achieved, and what its research frontier is.
>
> This ledger prevents continuity errors where a technology system or institution is introduced in one prose unit and then forgotten, incorrectly described, or contradicted in a later unit.

> **Scope Boundary:** This ledger tracks *named technology entities as objects or institutions*. The civilizations and factions that *own* them are tracked in their respective ledgers (`ledger-people-society-civilization`, `ledger-people-society-faction`). This ledger records the technology identity; the organizational identity is elsewhere. The two ledger files cross-reference each other.

> **Update Protocol:** Per Part 1 Area 6:
> - **New Entity File Trigger:** Any prose unit that introduces a named technology system (gives it a proper name, describes its capabilities at tier-level detail, or assigns it a canonical role) requires a new `[system-name].md` file created at Gate 2.
> - **New Institution File Trigger:** Any prose unit that introduces a named technology institution with defined domain scope and tier context requires a new `[institution-name].md` file.
> - **Update Trigger:** Any prose event that changes the technology tier, operational status, ownership, or capability profile of a tracked system or institution triggers a mandatory Post-Write Ledger Update.

> **Mandatory Update Triggers:**
> - Named technology system introduced with tier-level detail
> - Technology tier advancement of a tracked system or institution
> - Named AI system introduced with S-Classification (Part 10)
> - Destruction, capture, or decommission of a tracked system
> - Ownership transfer of a named system
> - New domain added to a tracked institution
> - AI sentience event (S1→S2+ transition) for a tracked AI system

> **CS%/TS% Tracking:** Named technology systems carry TS% values (Technology Synergy %) as Living Information (L). Named AI systems carry both CS% (if the AI has soul-equivalent properties per Part 10 DC-2/DC-3) and TS% values. Technology institutions carry CS%/TS% as organizational properties per Part 31 Area 21.

---

## Registry — Named Technology Entities

| File | Entity Name | Type | Tech Tier | Domain (Part 8 Type) | CS% | TS% | Status | Last Updated |
|---|---|---|---|---|---|---|---|---|
| sapphire-line.md | The Sapphire Line | Named Technology System | Tier 3 | Communication / Signal Relay — dual-track (technology + cultivation-amplified); Part 8 Type cross-ref pending | Inherits Azure Sky CS% 70% (cultivation interface component) | Inherits Azure Sky TS% 70% | Operational — First Prose Appearance: Prose 00001 | 2026-05-24 |

**Described Technology Infrastructure (established in prose but not formally named as proper-noun systems — no standalone ledger file warranted until a proper name is assigned in prose):**
- **Fourth-generation ambient arrays** — bilateral cultivation energy monitoring infrastructure at the Windward Range corridor; Azure Sky northern perimeter arrays (azure-sky-kingdom.md §5.6) and Gale Kingdom northern perimeter monitoring station (gale-kingdom.md Section 3); described in Varys's technical analysis. Tier: consistent with Azure Sky Tier 3 (Azure Sky side) and Gale Tier 2 (Gale side). Will receive a standalone entry if a proper name is assigned in prose.
- **Northern Accord corridor relay infrastructure** — bilateral signal relay network commissioned under the Second Bilateral Infrastructure Accord; 15-minute signal propagation time on the corridor; established in prose (Varya's latency analysis). Will receive a standalone entry if a proper name is assigned in prose.

---

## Part 28 Area 17 — Lore Section Schema (Technology-Scale Domain)

**Governing Law:** Part 28 Area 17 (Lore Creation Law). **Audit Hook:** Part 1 Area 8.13 ALCA dimension AL-10.

**For Named Technology Systems — Required Minimum Lore Fields:**

1. **System Name** — canonical name as established in prose (Negotiable Canon per Part 28 — immutable once named).
2. **Technology Tier** — Part 8 Tier 1–20 classification of the system's construction level.
3. **Domain Type** — Part 8 Type 1–14 classification of the technology domain (Type 4 for AI, Type 8 for military, etc.).
4. **Capability Profile** — what the system can do at its tier; hard capability ceilings per Part 8.
5. **Owner / Operator** — named faction or civilization; cross-reference to faction/civilization ledger.
6. **Location** — Part 13 cosmological hierarchy location where the system operates.
7. **Resource Requirements** — energy class (Part 33 WE-I through WE-VIII for weapons); CPM interface (Part 11 grade) if applicable.
8. **Current Status** — operational / damaged / destroyed / captured / decommissioned.
9. **AI Classification** — for AI systems: S-Classification (S1–S5 per Part 10); DC classification if digital consciousness applies.
10. **CS%/TS%** — synergy percentages per Part 31 Area 21.

**For Named Technology Institutions — Required Minimum Lore Fields:**

1. **Institution Name** — canonical name as established in prose.
2. **Institution Type** — ACR (Academic/Research), STF (Science/Technology), SII (Synergy Integration), or other Part 22 faction type.
3. **Technology Domain Focus** — Part 8 domain type(s) the institution specializes in.
4. **Achieved Tier** — current technology tier in their primary domain(s).
5. **Research Frontier** — what the institution is currently advancing toward.
6. **Membership / Leadership** — named individuals in leadership; total practitioner count by tier category.
7. **Institutional Secrecy** — Part 24 secrecy doctrine governing proprietary research.
8. **Faction Cross-Reference** — faction ledger file if this institution is also tracked as a faction entity.

**Depth Test:** "Can a scene involving this technology system or institution be written from only this ledger file, without inventing capability facts?" If yes, depth is satisfied.

**Silent Overwrite Prohibition (Part 28 Area 17.5):** Once technology lore is recorded, it is fixed. Tier advancement requires a new History entry, not replacement.

---

## Lore Section Compliance Registry

| File | Entity Name | Type | Tier | Depth-Test Certification | Last Lore Update |
|---|---|---|---|---|---|
| sapphire-line.md | The Sapphire Line | Named Technology System | Tier 3 | PENDING — capability profile established; resource requirements partially pending (energy source, CPM grade) | 2026-05-10 |

---

*ledger-technology-scale _index — v1.2 (2026-05-10) — 1 entry (Named Technology Systems: 1 [sapphire-line.md]; Named Technology Institutions: 0); 2 described-but-unnamed technology systems noted (fourth-generation ambient arrays, Northern Accord corridor relay infrastructure). Sapphire Line entry created with full Named Technology System file.*
