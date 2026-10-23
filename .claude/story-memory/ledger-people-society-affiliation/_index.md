# ledger-people-society-affiliation — Ledger Index

**Ledger Domain:** People & Society — Affiliation Agreements, Faction-Pair Relationship Rows and Combined-Force Files
**Governed By:** Part 37 (Ledger Schema Law), Part 23 (Affiliation Law)
**Template:** Part 37 Area 3.3 — Schema Template: Affiliation Agreement Ledger
**Last Updated:** 2026-10-23
**Index Version:** 10.0
**Total Entries:** 5 (Named Affiliation Agreements: 4; Registry B pair rows: 1; Combined-Force Files: 0 — the Northern Accord Expeditionary Wing is listed in Registry C by cross-reference to its faction ledger)

> **Purpose:** This folder tracks three categories of affiliation entity introduced in prose:
> - **Named Affiliation Agreements** — formal treaties, pacts, compacts, alliances, and accords established by name in prose. One `.md` file per named agreement. Examples: "The Threeford River Compact," "The Azure-Gale Non-Aggression Accord."
> - **Faction-Pair Relationship State** — the current AFF spectrum position (AFF-1 through AFF-14) between any two named factions whose relationship has been canonically established in prose. One row per faction pair in Registry B; no file.
> - **Combined-Force Files** — one `.md` file per combined operation, exercise or station of the armed forces of two or more named factions, listed in Registry C. Example: `combined-windward-range-patrol.md`.
>
> This ledger is the authoritative source for answering: *"What is the formal relationship between Faction A and Faction B, and what agreements govern it?"* It prevents continuity errors where a character acts as though an alliance exists that was never established, or references a pact the parties do not formally hold.

> **Update Protocol:** Per `guardrails/ledger/guardrail-ledger-update-law.md`:
> - **New Agreement File Trigger:** Any Area that formally names, establishes, or introduces a new affiliation agreement between factions requires a new `[agreement-name].md` file created at Gate 2.
> - **Pair Row Trigger:** Any Area that establishes the first formal interaction between two named factions (assigning them an AFF spectrum position) adds one row to Registry B. No file is created for a pair of factions.
> - **Combined-Force File Trigger:** Any Area in which the armed forces of two or more named factions carry out a combined operation, a combined exercise or a combined station requires a new `combined-[activity-slug].md` file created at Gate 2 and listed in Registry C. The file name is lower case with plain ASCII hyphens, and the slug is the in-world name of the operation, exercise or station (for example `combined-windward-range-patrol.md`); the two nations are named inside the file, not in the file name. "Combined" means forces of different nations; "joint" means different branches of one nation. Two factions that work together in none of these ways have a Registry B row and no file.
> - **Update Trigger:** Any event written in an Area that changes an existing affiliation spectrum position, violates or terminates an agreement, activates a treaty clause, or changes the public vs. covert layer of an affiliation triggers a mandatory Post-Write Ledger Update to the relevant file(s).

> **Mandatory Update Triggers (per Part 23 Area 10 and `guardrails/ledger/guardrail-ledger-update-law.md`):**
> - New formal affiliation agreement introduced by name
> - AFF spectrum position shift between any tracked faction pair
> - Structural Tie formed or changed between a tracked faction pair (Part 23 Area 9.3)
> - Treaty violation or dissolution event
> - Hidden affiliation revealed (covert → public layer transition)
> - New party added to a multi-faction agreement
> - Affiliation-driven CSS-4+ consequence event (triggers Part 27 update simultaneously)
> - A combined operation, exercise or station begins, changes its command arrangement, or ends

> **CS%/TS% Note:** Affiliation agreements, pair rows and combined-force files do not carry personal CS%/TS% values — those are actor properties. However, the file notes whether the agreement involves synergy-capability factions (SII-type, Model C/D practitioners) where Part 31 integration model access is part of the agreement's strategic value.

> **AFF Spectrum Reference (Part 23 Area 2.1):**
> AFF-1 Absolute Alliance → AFF-2 Full Alliance → AFF-3 Strategic Partnership → AFF-4 Trade Alliance → AFF-5 Cooperation Compact → AFF-6 Non-Aggression Pact → AFF-7 Cautious Neutrality → AFF-8 Competitive Rivalry → AFF-9 Cold War → AFF-10 Embargo & Isolation → AFF-11 Proxy Warfare → AFF-12 Open Conflict → AFF-13 Elimination Campaign → AFF-14 Absorption Campaign

> **Marker Legend:** These markers appear in the entries of this ledger. Open cells otherwise carry `OPEN-AREA` or `OPEN-AUTHOR` (Part 37 Area 5).
> - `[ASKED]`: the author chose this value.
> - `[DERIVED]`: the drafter inferred this value from cited evidence and the author reviewed it in the digest without overriding it (Part 39 Rule 39.3.3.1); it is pending only when the entry also says flagged for author confirmation.
> - `[AUTHOR-PENDING]`: a question about this value has been raised and is not yet answered.
> - `[MARKED SLOT]`: a slot left empty on purpose until the author rules.
> - "flag, do not invent": when a scene needs the value, the prose may establish one small fact at a time under Part 28 Area 17, logged in this ledger and offered to the author as a draft value at the next Section close. A name or a major entity (Part 28 Area 20.4) goes to the author first, through the Decision Consultation Gate.

---

## Registry A — Named Affiliation Agreements

| Entity Name (B) | Classification (B/L) | First Area Appearance (B) | Entity File (L) | Status (L) | Last Updated (L) | Parties | Established |
|---|---|---|---|---|---|---|---|
| The Northern Accord | AFF-3 Strategic Partnership | Not yet established | northern-accord.md | Active | 2026-09-29 | Azure Sky Kingdom + Gale Kingdom + the Three Moon Sects (Fallen, Full, Dark) as a bloc of observers (contested, P30-L8) | Pre-story |
| The Lyraen River Compact | AFF-5 Cooperation Compact (multi-party, not preferential) | Not yet established | lyraen-river-compact.md | Active | 2026-09-29 | Azure Sky + Gale + Southern March kingdoms (Saltmere + Ironshore identified as candidate signatories via kingdom-lore cross-reference; full party list partially established) | Pre-story |
| Southern March Framework | AFF-6 Non-Aggression Pact (estimated) | Not yet established | — | Active | — | Azure Sky + Border Kingdoms of Southern March + southern neighbors | Pre-story |
| Second Bilateral Infrastructure Accord | Not yet established | Not yet established | — | Historical (pre-story); present force not established | — | Azure Sky + Gale | Pre-story |

*Note: Southern March Framework is a named continental agreement (nine-suns-continent.md §5.9) but has insufficient canonical detail for a standalone file; a file will be created when the Framework is established with term-level detail in prose.*

*Note: The Second Bilateral Infrastructure Accord is a pre-story treaty that commissioned the Northern Accord corridor infrastructure and the Windward Protocol relay stations (named in northern-accord.md Section 6 and gale-kingdom-state.md); its terms are not established beyond that, so it has no file. The name implies a first accord, but no ledger names or establishes one.*

---

## Registry B — Faction-Pair Relationship State

| Faction A | Faction B | Current AFF Position | Axis Positions (Mil / Eco / Intel / Pol / Ideo / Cult) | Public Layer | Covert Layer | Structural Tie | Combined-Force File(s) | Last Updated |
|---|---|---|---|---|---|---|---|---|
| Azure Sky Kingdom | Gale Kingdom | AFF-3 Strategic Partnership | AFF-3 / AFF-4 / AFF-5 / AFF-3 / AFF-6 / AFF-5 | Northern Accord; combined Windward patrol; Lyraen customs partner | None established | none (sovereign co-signatories) | The Northern Accord Expeditionary Wing (Registry C) | 2026-09-29 |

---

## Registry C — Combined-Force Files

| File | Activity Name | Kind | Contributing Nations | Contributing Forces | Command Arrangement | Status | Governing Agreement | First Area Appearance | Last Updated |
|---|---|---|---|---|---|---|---|---|---|
| `ledger-people-society-faction/northern-accord-expeditionary-wing.md` (faction ledger; no second file) | The Northern Accord Expeditionary Wing, patrolling the Windward Range passes | Combined Station | Azure Sky Kingdom + Gale Kingdom | One standing company, both kingdoms counted together: 144 at establishment; 112 until 1247.3.24 / PD 83, and **94 now** (the 112 less eighteen dead, nine of each kingdom; Gate 2 of 2026-10-23, Chapter 009) | Paired command (two posts, held for the duty by Corin Vale and Gunnar Stavik by the author's ruling of 2026-10-22, otherwise empty; as first entered, both not yet established) | Active | The Northern Accord, Provision 1 and the Windward Protocol | Chapter 009 — The Pass Holds (Ref: 1.1.1.009) | 2026-10-23 |

*A combined-force file is created only for a combined operation, exercise or station. An activity whose record already lives in a faction ledger is listed here by cross-reference and is not copied.*

---

## Part 28 Area 17 — Lore Section Schema (Affiliation Domain)

**Governing Law:** Part 28 Area 17 (Lore Creation Law). **Audit Hook:** ALCA dimension AL-10 (`guardrails/audit/guardrail-alca.md`) (Lore Completeness Alignment).

**For Named Affiliation Agreements — Required Minimum Lore Fields:**

1. **Agreement Name** — the canonical name established in prose (Negotiable Canon per Part 28 — once named, immutable).
2. **Parties** — all named factions, institutions, or characters who are formal signatories.
3. **AFF Spectrum Position** — the Part 23 AFF-1 through AFF-14 position this agreement represents or establishes.
4. **Terms** — the canonical obligations, permissions, and prohibitions governing each party.
5. **Activation Clauses** — conditions under which the agreement escalates, triggers mutual defense, or terminates.
6. **Violation Profile** — what constitutes a violation, which party holds violation rights, and what CSS consequence class results.
7. **Secrecy Layer** — whether the agreement is public, semi-public, or covert; who knows it exists.
8. **History** — how the agreement came to be; prior relationship state that necessitated it.

**For Registry B Rows (Faction-Pair Relationship State) — Required Minimum Fields:**

1. **Faction A and Faction B** — canonical names from the faction ledger.
2. **Current AFF Position** — Part 23 spectrum position with date of last change.
3. **Axis Positions** — the six axes of Part 23 Area 2.3, each an AFF code.
4. **Public Layer** — what both factions publicly acknowledge.
5. **Covert Layer** — what the relationship is beneath the surface, if different.
6. **Structural Tie** — the rank tie between the pair, if any (none, vassal, protectorate, tributary, branch, puppet or subsidiary; Part 23 Area 9.3); where a tie is concealed, the public tie and the hidden tie are recorded separately.
7. **Active Agreements** — Registry A names governing the pair.
8. **Combined-Force File(s)** — Registry C entries, or none.

**For Combined-Force Files — Required Minimum Lore Fields** (B = baseline, L = living):

1. **Activity Name (B)** — the canonical name established in prose.
2. **Kind (B)** — Combined Operation, Combined Exercise or Combined Station.
3. **Contributing Nations (B)** — canonical faction names.
4. **Contributing Forces (B)** — the named force each nation supplies (cross-reference to its military ledger) and the rung it supplies, named from the shared ladder (squad, platoon, company and so on; `reference-military-organization-and-rank` R3).
5. **Strength (L)** — nominal establishment and current strength, per nation and total (R1.2).
6. **Command Arrangement (B)** — lead-nation command, parallel command, integrated command, or paired command (two commanders of equal standing), with the named command posts. A post is recorded by appointment; "not yet established" is a valid entry and implies no officer (R2.4).
7. **Mission or Purpose (B)** — operation: the mission and its end state. Exercise: the training aim and scenario. Station: why the post is held.
8. **Area (B)** — where it operates, by ledger location cross-reference, with distances in metric.
9. **Period (L)** — start, end or "standing"; length of a posting or rotation.
10. **Governing Agreement (B)** — the Registry A instrument and clause that authorises it.
11. **Rules of Engagement and Status of Forces (B)** — who may order force, and whose law and discipline bind a soldier of the other nation; only what prose has established.
12. **Sustainment and Liaison (B)** — who supplies, pays and houses each contingent; liaison officers; signals and language arrangements.
13. **Outcome (L)** — operation: result and losses. Exercise: findings. Station: relief or rotation record.
14. **Effect on the Pair Row (L)** — any change to the Registry B row.
15. **Events Log (L)**.

Fields record each force on its own terms. No field compares one nation's force with the other's.

**Depth Test:** "Can a scene of diplomatic negotiation, alliance activation, or betrayal between these factions (for an agreement file), or a scene of a combined patrol, exercise or posting between these forces (for a combined-force file), be written from only this ledger file, without inventing facts?" If yes, depth is satisfied.

**Silent Overwrite Prohibition (Part 28 Area 17.5):** Once affiliation lore is recorded, it is fixed under the Establishment Threshold. Spectrum position changes require a new entry in the History field, not replacement of the prior state.

---

## Lore Section Compliance Registry (Affiliation)

| File | Entry Name | Type | Depth-Test Certification | Last Lore Update |
|---|---|---|---|---|
| northern-accord.md | The Northern Accord | Named Affiliation Agreement | PENDING — core terms established; activation clauses and violation profile partially pending (mutual aid thresholds not yet established in an Area) | 2026-08-25 |
| lyraen-river-compact.md | The Lyraen River Compact | Named Affiliation Agreement | PENDING — agreement identity and parties established; term details pending authored prose | 2026-05-10 |

---

