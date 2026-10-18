# ledger-people-society-affiliation — Ledger Index

**Ledger Domain:** People & Society — Affiliation Agreements and Faction-Pair Relationship State
**Governed By:** Part 1 Area 5 (Ledger System), Part 23 (Affiliation Law)
**Template:** Part 1 Area 5.5.9 — Affiliation Ledger Format
**Last Updated:** 2026-05-24
**Index Version:** v1.3
**Total Entries:** 4 (Named Affiliation Agreements: 3; Faction-Pair Relationship Files: 1)

> **Purpose:** This folder tracks two categories of affiliation entity introduced in prose:
> - **Named Affiliation Agreements** — formal treaties, pacts, compacts, alliances, and accords established by name in prose. One `.md` file per named agreement. Examples: "The Threeford River Compact," "The Azure-Gale Non-Aggression Accord."
> - **Faction-Pair Relationship State** — the current AFF spectrum position (AFF-1 through AFF-14) between any two named factions whose relationship has been canonically established in prose. One `.md` file per faction pair. Example: "azure-sky-kingdom-gale-kingdom.md" tracking the current spectrum position and history.
>
> This ledger is the authoritative source for answering: *"What is the formal relationship between Faction A and Faction B, and what agreements govern it?"* It prevents continuity errors where a character acts as though an alliance exists that was never established, or references a pact the parties do not formally hold.

> **Update Protocol:** Per Part 1 Area 6 (Ledger Audit and Update Law):
> - **New Agreement File Trigger:** Any prose unit that formally names, establishes, or introduces a new affiliation agreement between factions requires a new `[agreement-name].md` file created at Gate 2.
> - **Faction-Pair File Trigger:** Any prose unit that establishes the first formal interaction between two named factions (assigning them an AFF spectrum position) requires a new `[faction-a]–[faction-b].md` file. The file name uses the canonical faction slugs in alphabetical order, separated by an en-dash.
> - **Update Trigger:** Any prose event that changes an existing affiliation spectrum position, violates or terminates an agreement, activates a treaty clause, or changes the public vs. covert layer of an affiliation triggers a mandatory Post-Write Ledger Update to the relevant file(s).

> **Mandatory Update Triggers (per Part 23 Area 10 and Part 1 Area 6):**
> - New formal affiliation agreement introduced by name
> - AFF spectrum position shift between any tracked faction pair
> - Treaty violation or dissolution event
> - Hidden affiliation revealed (covert → public layer transition)
> - New party added to a multi-faction agreement
> - Affiliation-driven CSS-4+ consequence event (triggers Part 27 update simultaneously)

> **CS%/TS% Note:** Affiliation agreements and faction-pair relationship files do not carry personal CS%/TS% values — those are actor properties. However, the file notes whether the agreement involves synergy-capability factions (SII-type, Model C/D practitioners) where Part 31 integration model access is part of the agreement's strategic value.

> **AFF Spectrum Reference (Part 23 Area 2.1):**
> AFF-1 Absolute Alliance → AFF-2 Strategic Alliance → AFF-3 Formal Alliance → AFF-4 Active Partner → AFF-5 Cooperative → AFF-6 Neutral-Positive → AFF-7 True Neutral → AFF-8 Cautious → AFF-9 Rival → AFF-10 Active Rival → AFF-11 Cold War → AFF-12 Proxy War → AFF-13 Open Conflict → AFF-14 Absorption Campaign

---

## Registry A — Named Affiliation Agreements

| File | Agreement Name | Parties | AFF Tier | Status | Established | Last Updated |
|---|---|---|---|---|---|---|
| northern-accord.md | The Northern Accord | Azure Sky Kingdom + Gale Kingdom + Moon Sect (observer, contested, P30-L8) | AFF-3 Formal Alliance | Active | Pre-story (established before Prose 1); First Prose Establishment: Prose 00001 | 2026-05-24 |
| lyraen-river-compact.md | The Lyraen River Compact | Azure Sky + Gale + Southern March kingdoms (Saltmere + Ironshore identified Prose 00001; full party list partially established) | AFF-5 Cooperative | Active | Pre-story (established before Prose 1); Prose 00001: Saltmere + Ironshore identified as candidate signatories | 2026-05-24 |
| — | Southern March Framework | Azure Sky + Border Kingdoms of Southern March + southern neighbors | AFF-6 Neutral-Positive (estimated) | Active | Pre-story | — |

*Note: Southern March Framework is a named continental agreement (nine-suns-continent.md §5.9) but has insufficient canonical detail for a standalone file; a file will be created when the Framework is established with term-level detail in prose.*

---

## Registry B — Faction-Pair Relationship State

| File | Faction A | Faction B | Current AFF Position | Public Layer | Covert Layer | Last Updated |
|---|---|---|---|---|---|---|
| azure-sky-kingdom-gale-kingdom.md | Azure Sky Kingdom | Gale Kingdom | AFF-3 Formal Alliance | Northern Accord; joint Windward patrol; Lyraen customs partner; bilateral CPM crisis response active; Prose 00001 first prose establishment | None established | 2026-05-24 |

---

## Part 28 Area 17 — Lore Section Schema (Affiliation Domain)

**Governing Law:** Part 28 Area 17 (Lore Creation Law). **Audit Hook:** Part 1 Area 8.13 ALCA dimension AL-10 (Lore Completeness Alignment).

**For Named Affiliation Agreements — Required Minimum Lore Fields:**

1. **Agreement Name** — the canonical name established in prose (Negotiable Canon per Part 28 — once named, immutable).
2. **Parties** — all named factions, institutions, or characters who are formal signatories.
3. **AFF Spectrum Position** — the Part 23 AFF-1 through AFF-14 position this agreement represents or establishes.
4. **Terms** — the canonical obligations, permissions, and prohibitions governing each party.
5. **Activation Clauses** — conditions under which the agreement escalates, triggers mutual defense, or terminates.
6. **Violation Profile** — what constitutes a violation, which party holds violation rights, and what CSS consequence class results.
7. **Secrecy Layer** — whether the agreement is public, semi-public, or covert; who knows it exists.
8. **History** — how the agreement came to be; prior relationship state that necessitated it.

**For Faction-Pair Relationship Files — Required Minimum Lore Fields:**

1. **Faction Pair** — canonical names from the faction ledger.
2. **Current AFF Position** — Part 23 spectrum position with date of last change.
3. **Public Layer** — what both factions publicly acknowledge about their relationship.
4. **Covert Layer** — what the relationship actually is beneath the surface, if different.
5. **Multi-Axis Profile** — military / economic / intelligence / political / ideological / cultivation axes (Part 23 Area 2 — each may be at a different position).
6. **Relationship History** — prior AFF positions and the events that shifted them.
7. **Active Agreements** — cross-reference to Registry A files governing this pair.
8. **Trigger Events** — known events that would cause a shift in spectrum position.

**Depth Test:** "Can a scene of diplomatic negotiation, alliance activation, or betrayal between these factions be written from only this ledger file, without inventing facts?" If yes, depth is satisfied.

**Silent Overwrite Prohibition (Part 28 Area 17.5):** Once affiliation lore is recorded, it is fixed under the Establishment Threshold. Spectrum position changes require a new entry in the History field, not replacement of the prior state.

---

## Lore Section Compliance Registry (Affiliation)

| File | Entry Name | Type | Depth-Test Certification | Last Lore Update |
|---|---|---|---|---|
| northern-accord.md | The Northern Accord | Named Affiliation Agreement | PENDING — core terms established; activation clauses and violation profile partially pending (mutual aid thresholds not prose-established) | 2026-05-10 |
| azure-sky-kingdom-gale-kingdom.md | Azure Sky ↔ Gale Kingdom | Faction-Pair Relationship State | PENDING — multi-axis profile established; trigger events characterized; historical depth partially pending | 2026-05-10 |
| lyraen-river-compact.md | The Lyraen River Compact | Named Affiliation Agreement | PENDING — agreement identity and parties established; term details pending authored prose | 2026-05-10 |

---

*ledger-people-society-affiliation _index — v1.2 (2026-05-10) — Prose 9: northern-accord v1.1 (operation in execution phase), azure-sky–gale-kingdom v1.1 (bilateral execution; Aeries recalibration note). v1.1 (2026-05-10) — 4 entries (Named Agreements: 3 [northern-accord.md, lyraen-river-compact.md, Southern March Framework — stub note only]; Faction-Pair: 1 [azure-sky-kingdom-gale-kingdom.md]). v1.1: Populated from Prose 1–8 audit; Northern Accord (AFF-3, Windward Protocol sub-instrument); Azure Sky ↔ Gale faction-pair (multi-axis profile); Lyraen River Compact (stub).*
