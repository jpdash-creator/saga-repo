# ledger-society-information — Ledger Index

**Ledger Domain:** Information and Secrecy State, and every named document and agreement.
**Governed By:** `guardrails/ledger/guardrail-ledger-update-law.md`, Part 37 (Ledger Schema Law), Part 24 (Information and Secrecy Law)
**Template:** Part 37 Area 3.4 — Schema Template: Information Ledger
**Last Updated:** 2026-10-05
**Index Version:** 10.0
**Total Entries:** 0

> **Purpose:** This folder tracks the canonical information state of the novel — what each named character knows, what intelligence assets are active, what information is classified and at what tier, and what secrecy doctrines are in force for active factions. This is the authoritative record that prevents information continuity errors (a character "knowing" something they were never told, or "forgetting" something they canonically learned).

> **All information is stored here.** This folder holds, besides the intelligence and knowledge states above, one register row for every named document (a map, a letter or message, a charter, a decree or order, a codex, a record or account book) and for every named agreement, treaty or accord.
>
> **Form of these names (the author's style ruling):** "Roman for agreements, treaties and accords; italic for named maps and documents". A named map, letter, charter or other document is set in italic at every mention (the name only, no leading article inside the name, roman inside an italic passage; Part 28 Rule 20.8.2) and its Entity Name cell is written in italic (`*Name*`); it is registered here and not in `ledger-named-items`. An agreement, treaty or accord is set in roman and its Entity Name cell is written in roman. Part 28 Rule 20.8.7 owns the rule; Part 37 Area 3.4 owns the schema.
>
> **Three Types of Information Entries :**
> - **Character Knowledge Files:** A Character Knowledge File is created only for a character whose knowledge differential drives a live secret, concealment or deception. It tracks what they know, what they believe (that may be false), and what they have been deceived about, in the shape of the Part 24 N24-1 knowledge map (knows, believes falsely, suspects, conceals, how learned). Every other character's knowledge stays in the character ledger's events log.
> - **Intelligence Asset Files:** One file per active intelligence operation, classified asset, or structured secrecy doctrine that governs multiple characters.
> - **Information Records (a row, no file):** one registry row per named document and per named agreement, treaty or accord. The row is the record's whole ledger record, with one exception that points elsewhere: an agreement, treaty or accord has its home file in `ledger-people-society-affiliation/` (Part 23; Part 37 Area 3.3), which owns its parties, terms and state, and the row here holds only the name, the Kind, the first Area and the pointer (one owner, Part 37 Area 5). A named knowledge asset keeps its home entry in `ledger-technology-science/` and has its pointer row here. A document that carries actor-level detail (a custodian, an access rule, a classified finding) also earns an Intelligence Asset file.
> - **Record kinds (the `Kind` column):** `Intelligence Asset`; `Character Knowledge`; `Agreement, Treaty or Accord`; `Map`; `Letter or Message`; `Charter, Decree or Order`; `Codex, Record or Account Book`; `Other Document`.
> - **Status of a record:** for a document, `Active`, `Dormant`, `Lost`, `Destroyed` or `Withdrawn`; for an agreement, treaty or accord, the status of its affiliation file, mirrored from it.

> **New Row Trigger for records:** every named document and every named agreement, treaty or accord written into a confirmed and written Area is entered as a row at Gate 2 by the Post-Write Ledger Update, with no significance test. A name that exists only in a spec, or in a draft discarded by `[SKIP WRITE]`, enters nothing. The Area Maker lists them in the same hand-off block as the named items, marked for this ledger. No backfill is required: the agreements that `ledger-people-society-affiliation/` already lists (the agreements in its Registry A) are entered when an Area that writes them is confirmed, or when the author directs it.

> **Update Protocol:** Per `guardrails/ledger/guardrail-ledger-update-law.md`, the Pre-Write Ledger Check reads relevant information state before any prose where character knowledge differentials, intelligence operations, or secrecy enforcement are relevant. Any event written in an Area that constitutes an information revelation to a character who has a Character Knowledge File (a character learning something canonically significant), a secrecy breach, or an intelligence disclosure triggers a mandatory Post-Write Ledger Update routing here; revelations are appended as dated rows.

> **Command Interface:** [CANON CHECK: passage] (C-20) audits passages for Part 24 information violations against this ledger's state. [RUN CANON AUDIT] (C-10) includes information state consistency check against character ledger Canon Events Logs.

> **CS%/TS% Note:** Information entities (intelligence assets, knowledge states, secrecy doctrines) do not carry personal CS%/TS% values — these are properties of actors (characters, factions, civilizations, locations, objects), not of information items. However, this ledger tracks which actors possess integration-model knowledge (Model C/D integration architecture is Tier I Sovereign Secret Category C per Part 24 — its disclosure constitutes a dual-track CS%/TS% intelligence exposure event per Part 31 Cross-Part Dependency Table, row Canon-Part 24, and Part 24 Area 4.1). The Classification column notes when information items are synergy-sensitive (Model C/D knowledge, SII research, Integrated Practitioner capability profiles).

> **Marker Legend:** These markers appear in the entries of this ledger. Open cells otherwise carry `OPEN-AREA` or `OPEN-AUTHOR` (Part 37 Area 5).
> - `[ASKED]`: the author chose this value.
> - `[DERIVED]`: the drafter inferred this value from cited evidence and the author reviewed it in the digest without overriding it (Part 39 Rule 39.3.3.1); it is pending only when the entry also says flagged for author confirmation.
> - `[AUTHOR-PENDING]`: a question about this value has been raised and is not yet answered.
> - `[MARKED SLOT]`: a slot left empty on purpose until the author rules.
> - "flag, do not invent": when a scene needs the value, the prose may establish one small fact at a time under Part 28 Area 17, logged in this ledger and offered to the author as a draft value at the next Section close. A name or a major entity (Part 28 Area 20.4) goes to the author first, through the Decision Consultation Gate.

---

| Entity Name (B) | Classification (B/L) | First Area Appearance (B) | Entity File (L) | Status (L) | Last Updated (L) | Kind (B) |
|---|---|---|---|---|---|---|

---

## Part 28 Area 17 — Lore Section Schema (Information Domain)

**Governing Law:** Part 28 Area 17 (Lore Creation Law). **Audit Hook:** ALCA dimension AL-10 (`guardrails/audit/guardrail-alca.md`) (Lore Completeness Alignment).

**Mandate:** Every named information entity (intelligence asset, classified doctrine, narratively significant secret) must carry a dedicated **Lore (Part 28 Area 17)** section, placed after the template's numbered sections, populated to the Breadth-and-Depth Standard.

**Required Axes (Minimum Lore Fields per Part 28 Area 17.2 — Information Entity):**

1. **Classification Tier** — Part 24 Area 2 five-tier system.
2. **Custodian** — named faction, character, or institution that holds the information; chain of custody if changed.
3. **Access Control** — who may read, who may copy, who may destroy; named gatekeepers.
4. **Decay Rate** — how quickly the information loses strategic value (half-life or event-triggered obsolescence).
5. **Corruption Risk** — probability and vectors for the information being altered, forged, or partially lost.
6. **Known Copies/Versions** — inventory of instances and their locations; named unauthorized copies if any.
7. **Exposure Consequences** — per Part 24 and Part 27, what CSS event would result from public or hostile disclosure.

**Depth Test (Part 28 Area 17.3):** "Can I write a pacing-appropriate immersion scene (Part 28 Area 17.3) in which this information is deployed, withheld, or contested using only what is in the ledger?" If yes, depth is satisfied.

**Character Knowledge Files:** Also apply this schema to per-character knowledge-state files — the minimum lore is what the character knows + how they came to know it + what they still do not know + what they believe that may be false.

**Silent Overwrite Prohibition (Part 28 Area 17.5):** Once information lore is recorded, it is fixed under the Establishment Threshold.

---

## Lore Section Compliance Registry (Information)

| File | Entity/Asset Name | Type | Lore Status | Last Lore Update |
|---|---|---|---|---|

*No entries yet. Schema applies to all future information files from creation.*
