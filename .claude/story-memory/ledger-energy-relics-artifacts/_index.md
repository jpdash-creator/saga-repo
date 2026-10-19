# ledger-energy-relics-artifacts — Ledger Index

**Ledger Domain:** Energy — Relics and Artifacts
**Governed By:** `guardrails/ledger/guardrail-ledger-update-law.md`, Part 37 (Ledger Schema Law), Part 12 (Energy Relics and Artifacts Law), Part 11 (Energy Substance Law)
**Template:** Part 37 Area 2.8 — Schema Template: Energy-Relics / Artifacts Ledger
**Last Updated:** 2026-10-19
**Index Version:** 10.0
**Total Entries:** 0 — no Named Relics activated in an Area yet; named entities held before any Area noted below

> **Purpose:** This folder tracks named relics, artifacts, and significant energy resource caches that exist as standalone canonical objects beyond individual character ownership — or whose narrative significance warrants a dedicated record independent of any character's personal ledger. Character-owned relics and CPM holdings are also recorded in Character Ledger Section 8; this folder holds the object-level record for Named Relics and formation arrays of narrative significance.

> **Entry Categories:**
> - **Named Relic Files:** Individual files for named relics (Tier 3+ or narratively named) — tracks relic tier, type, current location, Soul Bond status, capabilities, and history.
> - **Formation Array Files:** Named formation arrays of tactical or narrative significance — tracks configuration, location, controlling faction, and operational status.
> - **Energy Resource Cache Files:** Significant CPM deposits or stockpiles that are narrative plot elements — tracks grade, quantity (approximate), location, and controlling faction.

> **Named-item register.** Every named relic, artifact, formation array and energy resource cache here is also a named item (Part 12 Rule 2.2.3; Part 28 Rule 20.8.1). Its name is set in italic, not bold (the author: "Move them to italic and into the named-items register"), and it has a row in `ledger-named-items/_index.md` (Type relic or artifact, formation array, or energy cache) that points at its entry here. This ledger stays the home of every descriptive fact; the register row holds only the name, the Type, the first Area and the pointer, and copies no value.

> **Update Protocol:** Per `guardrails/ledger/guardrail-ledger-update-law.md`, the Pre-Write Ledger Check reads relic/artifact state before any prose where a named relic is deployed or interacted with. Relic acquisition, Soul Bond formation, relic destruction, and transfer between characters trigger mandatory Post-Write Ledger Update to both this ledger and the relevant character's Section 8.

> **Key Events Requiring Immediate Update:**
> - Soul Bond formation (identity event — also triggers [IDEOLOGY AUDIT] C-17)
> - Relic destruction (CSS event — also triggers [CONSEQUENCE AUDIT] C-18)
> - Formation array activation or destruction
> - CS%/TS% update triggers: Soul Bond formation raises CS%; Technology-Relic Hybrid class upgrade raises TS%; relic enhancement or Sacred Ground infusion may raise CS%; structural damage may lower both

> **CS%/TS% Tracking:** CS% (Cultivation Synergy %) and TS% (Technology Synergy %) for relics and artifacts are Base Information (B) at ledger entry creation per Part 31 Area 21.10, with Living Information (L) updates per the triggers above. CS% is governed by relic tier, affinity type, formation array density, Soul Bond status, and cultivation energy function. TS% is governed by Hybrid Class (if applicable), manufactured component density, and CI Technology integration level. The registry table includes CS%/TS% columns for quick reference.

> **Marker Legend:** These markers appear in the entries of this ledger. Open cells otherwise carry `OPEN-AREA` or `OPEN-AUTHOR` (Part 37 Area 5).
> - `[ASKED]`: the author chose this value.
> - `[DERIVED]`: the drafter inferred this value from cited evidence and the author reviewed it in the digest without overriding it (Part 39 Rule 39.3.3.1); it is pending only when the entry also says flagged for author confirmation.
> - `[AUTHOR-PENDING]`: a question about this value has been raised and is not yet answered.
> - `[MARKED SLOT]`: a slot left empty on purpose until the author rules.
> - "flag, do not invent": when a scene needs the value, the prose may establish one small fact at a time under Part 28 Area 17, logged in this ledger and offered to the author as a draft value at the next Section close. A name or a major entity (Part 28 Area 20.4) goes to the author first, through the Decision Consultation Gate.

---

| Entity Name (B) | Classification (B/L) | First Area Appearance (B) | Entity File (L) | Status (L) | Last Updated (L) | Tier | CS% | TS% | Current Location/Holder |
|---|---|---|---|---|---|---|---|---|---|

**Named Entities Before Any Area (pending first Area appearance — no standalone files yet):**
- **The Accord signet** — Azure Sky Kingdom royal regalia held by Valia; declared as named regalia in azure-sky-kingdom-state.md §7.8 ("analogous pending" cross-reference to the Zenith weapon-ledger note); type (artifact/signet regalia), tier, and capabilities not yet established in prose; will receive a standalone file when activated in an Area; it is an artifact, so its home is this ledger (the Zenith oath-blades are the weapon, registered in `ledger-technology-weapon`); its capabilities are OPEN-AREA. *(Naming disambiguation: this is Valia's personal regalia name, unrelated to the name of the kingdom's technology-side military order, the Azure Guard. See azure-sky-kingdom-state.md §7.4/§7.8.)*

---

## Substance Introduction Register (Part 11 Area 14.1)

**Purpose:** Part 11 sets a novel-wide order for introducing energy substances to the reader: Power Crystal first, then Gem, Shard, Core, and Divine Liquid last. This register records which of the five states the reader has already met, so the order can be checked without rereading prose. It records; the order itself is Part 11's.

**Filled by:** the Post-Write Ledger Update, the first time an Area introduces a state to the reader (direct narrative introduction, Part 11 Area 14.1, not an offhand reference). A row set to Y stays Y.

| Substance State (B) | First Area Reference (L) | Introduced Y/N (L) |
|---|---|---|
| Power Crystal | Chapter 005 — The House With No Walls (Ref: 1.1.1.005), Area block 01 | Y |
| Gem | not yet | N |
| Shard | not yet | N |
| Core | not yet | N |
| Divine Liquid | not yet | N |

*Power Crystal was introduced to the reader directly in Chapter 005 (Ref: 1.1.1.005), Area block 01, with its picture in the same clause: "Four wagons of Whistledeep ore stood nose to tail behind her, low-grade Power Crystal, the stone that holds qi, in sacks, bound down the mountain for the Aerie Artificers' College." The cargo is bulk ore of low grade (no grade is stated beyond "low") and the page calls it Power Crystal or ore; in Area block 02 each sack is "dull and heavy and giving off no more pressure than gravel". Gem, Shard, Core and Divine Liquid have not been introduced and stay N (written 2026-10-19 at the Gate 2 of Chapter 005).*

---

## Part 28 Area 17 — Lore Section Schema (Relic/Artifact Domain)

**Governing Law:** Part 28 Area 17 (Lore Creation Law). **Audit Hook:** ALCA dimension AL-10 (`guardrails/audit/guardrail-alca.md`) (Lore Completeness Alignment).

**Mandate:** Every named relic, artifact, formation array, and narratively significant energy resource cache must carry a dedicated **Lore (Part 28 Area 17)** section, placed after the template's numbered sections, populated to the Breadth-and-Depth Standard.

**Required Axes (Minimum Lore Fields per Part 28 Area 17.2 — Relic/Artifact):**

1. **Origin** — who forged, found, or imbued it; under what circumstance; the costs paid by the maker.
2. **Original Owner** — the first known wielder; their fate.
3. **Transfer History** — lineage of ownership; how it moved from hand to hand; named intermediate holders.
4. **Grade** — per Part 12 tier system.
5. **Awakening Condition** — what triggers the relic's active properties (soul bond, blood rite, realm threshold, ambient energy, etc.).
6. **Known Abilities** — what the relic does, within its Part 12 governance; what it refuses to do; what it costs the wielder.

**Depth Test (Part 28 Area 17.3):** "Can I write a pacing-appropriate immersion scene (Part 28 Area 17.3) centered on the deployment of this relic using only what is in the ledger?" If yes, depth is satisfied.

**Silent Overwrite Prohibition (Part 28 Area 17.5):** Once relic lore is recorded, it is fixed under the Establishment Threshold.

---

## Lore Section Compliance Registry (Relic/Artifact)

| File | Entity | Tier | Lore Status | Last Lore Update |
|---|---|---|---|---|

*No entries yet. Schema applies to all future relic/artifact files from creation.*
