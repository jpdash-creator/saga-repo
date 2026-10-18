# ledger-people-society-faction — Ledger Index

**Ledger Domain:** People, Society — Faction State
**Governed By:** Part 1 Area 5 (Ledger System), Part 22 (Faction Law), Part 23 (Affiliation Law)
**Template:** Part 1 Area 5.5.2 — Faction Domain Ledger Format
**Last Updated:** 2026-05-24
**Index Version:** v1.4
**Total Entries:** 5

> **Purpose:** This folder tracks the canonical state of factions that appear in the novel. For each faction, it records: Faction Type (FT), Faction Power Tier (FPT), active doctrine, key alliance and rivalry positions, resource holdings, internal governance structure, active crises, and major events that have affected the faction. Character affiliation bonds to factions are cross-referenced from character ledger Section 7.

> **When to Create a New Faction File:** When a named faction first appears in prose with enough governance detail to warrant tracking, or when a faction's state changes significantly (FPT shift, doctrine change, alliance shift, major resource event).

> **Update Protocol:** Per Part 1 Area 6, the Pre-Write Ledger Check reads faction state before any prose where faction decisions, doctrines, or power dynamics govern the narrative. Faction-level events (FPT shift, doctrine change, alliance formation or rupture, significant resource change, territorial change) trigger mandatory Post-Write Ledger Update.

> **Cross-Reference:** Character Ledger Section 7 (Relationships and Faction Positions) records each character's affiliation bonds. This ledger records the faction's side of the same relationships. Consistency between these two records is required — [RUN CANON AUDIT] (C-10) checks this consistency.

> **Command Interface:** [STATUS] (C-13) reports active faction positions and tensions from this ledger. [CONSEQUENCE AUDIT] (C-18) is informed by faction rupture CSS events.

> **CS%/TS% Tracking:** CS% (Cultivation Synergy %) and TS% (Technology Synergy %) for each faction are Living Information (L) stored in Faction Ledger Section 2 per Part 31 Area 21.8. Values range 0%–100%. The _index.md registry includes CS%/TS% columns for quick-reference. Synergy Integration Institutes (SII, Part 22 Area 9.3) typically have both CS% and TS% in the 55%–80% range by definition. Updates triggered by FPT shift, Sacred Ground access change, major weapon/vehicle fleet tier change, or CI Technology level change.

---

| File | Faction Name | Faction Type | FPT | CS% | TS% | Status | Ledger Ver. | Last Updated |
|---|---|---|---|---|---|---|---|---|
| azure-sky-kingdom-state.md | Azure Sky Kingdom (Ruling State) | Sovereign Kingdom — Dual-Track | FPT-5 (upper continental kingdom) | 70% | 70% | Active — Windward Pass CPM crisis bilateral response ongoing; formal session in 17 days (Prose 00001) | v1.21 | 2026-05-24 |
| gale-kingdom-state.md | Gale Kingdom (Ruling State) | Sovereign Kingdom — Cultivation-Dominant | FPT-4 to FPT-5 (mid-to-upper continental) | 75% | 45% | Active — Northern Accord co-signatory; bilateral CPM crisis response; session in 17 days (Prose 00001) | v1.12 | 2026-05-24 |
| fallen-moon-sect.md | Fallen Moon Sect | Cultivation Sect — Apex (Space Affinity) | Apex — system-wide | 95% | 10% | Dominant — co-governs Moon of Saha | v1.1 | 2026-04-20 |
| full-moon-sect.md | Full Moon Sect | Cultivation Sect — Apex (Time Affinity) | Apex — system-wide | 95% | 10% | Dominant — co-governs Moon of Saha | v1.1 | 2026-04-20 |
| dark-moon-sect.md | Dark Moon Sect | Cultivation Sect — Apex (Darkness Affinity) | Apex — system-wide | 95% | 10% | Dominant — co-governs Moon of Saha | v1.1 | 2026-04-20 |

---

*ledger-people-society-faction _index — v1.3 (2026-05-10) — Prose 9: azure-sky v1.20 (delegation departed; operation in execution phase), gale-kingdom v1.11 (departure + Varya latency figure closure) — 5 faction entries; Azure Sky (v1.19) and Gale Kingdom (v1.10) updated from Prose 1–8 audit; arc status updated to reflect active bilateral CPM discharge coordination; three Moon Sects remain PENDING (P30-L8 Phase 1 Forbidden Entity).*

---

## Part 28 Area 17 — Lore Section Schema (Faction Domain)

**Added:** 2026-04-19 (formal Canon amendment — schema expansion pass).
**Governing Law:** Part 28 Area 17 (Lore Creation Law). **Audit Hook:** Part 1 Area 8.13 ALCA dimension AL-10 (Lore Completeness Alignment).

**Mandate:** Every faction entity file must carry a dedicated **Section 5 — Lore (Part 28 Area 17)** block populated to the Breadth-and-Depth Standard.

**Required Axes (Minimum Lore Fields per Part 28 Area 17.2 — Faction):**

1. **Faction Name and Known Aliases** — canonical name plus any alternate names used in-world.
2. **Founding Date and Founder** — specific date, era-anchor, or approximate era; named founder or founding council.
3. **Ideological Orientation** — Part 20 category and variant; named doctrinal texts or slogans where applicable.
4. **Membership Size Class** — Part 22 Scale Code.
5. **Resource Class** — treasury, territorial holdings, cultivation/technology assets, named material advantages.
6. **Governance Archetype** — hierarchical / decentralized / cell / consensus / autocratic / hybrid (per Part 22).
7. **Public Face** — what the faction presents to outsiders; official narratives.
8. **Private Reality** — what insiders know that outsiders do not; internal tensions, secret doctrines, hidden costs of membership.
9. **Known Rivals and Allies** — Part 23 affiliation positions; named rivalries with specific origin events; named alliances with specific terms.
10. **Signature Methods** — how the faction characteristically operates (patient infiltration, open warfare, commercial strangulation, ideological conversion, etc.).
11. **Recruitment Practices** — who is admitted, how they are tested, what they must give up to join, named initiation rites.

**Depth Test (Part 28 Area 17.3):** "Can I write a 1800%-immersion scene involving this faction using only what is in the ledger?" If yes, depth is satisfied.

**Silent Overwrite Prohibition (Part 28 Area 17.5):** Once faction lore is recorded, it is fixed under the Establishment Threshold.

---

## Lore Section Compliance Registry

| File | Faction | Lore Status | Last Lore Update |
|---|---|---|---|
| azure-sky-kingdom-state.md | Azure Sky Kingdom (Ruling State) | POPULATED (Stage 4 partial; §7.3 Wardens paragraph rolled back per [RESET CHAPTER: 1]; Prose 1–8 event rows added v1.19; Northern Accord + Windward Protocol + Twin Oath Compact + Lyraen River Compact oaths added §7.5) | 2026-05-10 |
| gale-kingdom-state.md | Gale Kingdom (Ruling State) | POPULATED (Stage 4 partial; Prose 1–8 event rows added v1.10; Northern Accord + Windward Protocol + Lyraen River Compact oaths added §7.5; Gale northern monitoring station added §3) | 2026-05-10 |
| fallen-moon-sect.md | Fallen Moon Sect | PENDING STAGE 4 CONTINUATION | — |
| full-moon-sect.md | Full Moon Sect | PENDING STAGE 4 CONTINUATION | — |
| dark-moon-sect.md | Dark Moon Sect | PENDING STAGE 4 CONTINUATION | — |

*Stage 4 Partial Execution note: 2 of 5 factions populated on 2026-04-19. Remaining 3 factions deferred to continuation session.*

*Lore Compliance Registry v1.1 amendment (2026-04-20): Azure Sky Kingdom's §7.3 Wardens of the Reconciliation paragraph has been rolled back to a pre-prose institutional placeholder per [RESET CHAPTER: 1] — the full seven-standing Chamber-oathed structure, sovereign-only appointment, joint Azure-Gale chest salary, standing watch with Warden Senna naming, and all Prose 4 canonicalisation details have been removed pending re-establishment in authored prose. Azure Sky Kingdom's §7.8 Prose-derived legacy-weight hooks (grey-seal matter; Apprentice's Choice cohort irregularity interlock; Warden institution canonicalisation; Aeries political-debt register exterior rendering) have all been removed. All other §7.1–§7.7 content (founding event, doctrine, governance structure header, military command paired-orders, oath network, economic base, reputation) is preserved as pre-prose institutional canon. Gale Kingdom §7.1–§7.8 lore content is fully preserved — none of it was Prose-derived.*
