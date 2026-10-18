---
name: ssc-narration-p28-lore-creation-law
description: Governs the mandatory creation, breadth-and-depth standard, recording protocol, and consistency/enrichment rules for lore attached to every named entity introduced in Starward Saga prose — worlds/locations, factions, civilizations, affiliation agreements, information entities, travel routes, spatial landmarks, technology systems, research programs, scientific frameworks, systems (sects/academies/guilds), characters, cultures/festivals, relics, weapons, and vehicles; reach for this whenever prose is about to introduce or reference a named entity for the first time, when populating or auditing a ledger entity file's Lore Section, when deciding how much backstory an entity's ledger entry needs before a scene can safely draw on it, or when reconciling a contradiction between new prose and previously established ledger lore. This is canon Part 28 Area 17, domain narration.
user-invocable: false
---

## Rule Text (Verbatim Source — Authoritative)
## Area 17 — Lore Creation Law

### 17.1 — The Lore Mandate

Every entity introduced in prose, or referenced by proper name in prose as a named entity, must have lore recorded in its governing ledger before or within the same Gate-2 sequence as the prose that introduces it. Lore is not optional decoration — it is the texture that turns governed categories into inhabited instances. A governed category (a faction type, a location tier, a cultural paradigm, a character classification) tells the reader *what kind of thing* an entity is. Lore tells the reader *who this particular thing is*: where it came from, what shaped it, whom it has harmed or helped, what it remembers, what it fears, what it still owes.

Without lore, Negotiable Canon (Area 2) collapses into naming alone — a faction has a name but no history, a festival has a name but no origin, a kingdom has a name but no weight. With lore, every named entity becomes a fixed point around which future prose may gather depth. The Lore Mandate closes the gap between the Naming Freedom Law (Area 3) and the Contextual Earning Law (Area 15): the author is free to invent names (Area 3), but every named invention must be anchored in recorded lore (Area 17) so the Three-Beat Test (Area 15.4) has substance to draw from when the prose earns its delivery.

**The Mandate:** A prose unit that introduces or references a named entity without triggering a corresponding ledger lore capture is a Part 28 Area 17 violation, audited under Part 1 Area 8.13 ALCA Mode A dimension AL-10 (Lore Completeness Alignment). The violation is a Post-Prose Audit failure; the prose unit does not pass audit until the lore capture is complete.

**Scope of "Named Entity":** A named entity is any entity given a proper noun in prose — a city, a kingdom, a faction, a festival, a weapon, a relic, a vehicle, a character (named, not merely referenced by role), a cultural tradition, an information artifact, a governance body. Unnamed background references (a road, a merchant, a crowd) are not named entities and do not trigger the Mandate. Once a name is given — once "the merchant" becomes "Merchant Olara" — the Mandate activates for that entity.

### 17.2 — Entity Categories and Minimum Lore Fields

For each entity category, the following are the minimum lore axes that must be populated in the governing ledger. All axes listed are mandatory for a lore entry to be considered complete under this Area. Additional axes beyond these are encouraged — the minimum is the floor, not the ceiling.

**World / Star System / Continent / Kingdom / City / Village / Sub-Location (governed by Part 13):**
- Geographic extent (area, population-bearing region, borders or territorial limits)
- Founding history (when established, by whom, under what circumstance)
- Ruling authority (current governing body, succession mechanism, known historical ruling lineages)
- Dominant culture (governing Part 25 CPT, dominant linguistic/aesthetic register)
- Cultivation profile (Part 3 power distribution, sects present, highest-known realm)
- Technology profile (Part 8 TA tier, domain specializations, signature technologies)
- Ambient energy class (per Part 13 Area 2.3)
- Notable landmarks (named sites, named districts, named infrastructure)
- Diplomatic posture (Part 23 affiliation positions with neighboring entities)
- Population estimate (order of magnitude, composition)
- Economy primary drivers (what the location produces, trades, imports)
- Distinctive architectural/sensory signature (what a visitor first notices — materials, colors, sounds, smells, skyline)

**Faction (governed by Part 22):**
- Faction name and any known aliases
- Founding date and founder (or approximate era if precise date is unknown)
- Ideological orientation (Part 20 category and variant)
- Membership size class (Part 22 Scale Code)
- Resource class (treasury, territorial holdings, cultivation/technology assets)
- Governance archetype (hierarchical / decentralized / cell / consensus / autocratic — per Part 22)
- Public face (what the faction presents to outsiders)
- Private reality (what insiders know that outsiders do not)
- Known rivals and allies (Part 23 affiliation positions)
- Signature methods (how the faction characteristically operates — patient infiltration, open warfare, commercial strangulation, ideological conversion)
- Recruitment practices (who is admitted, how they are tested, what they must give up to join)

**Civilization (governed by Part 21):**
- CCT tier and civilization type (CS / TS / BP / ES / LS / CP per Part 21 Area 6)
- Dominant language(s) and writing system(s)
- Calendar system (epochs, year-reckoning, festival calendar anchors)
- Religious/philosophical framework (if any — pantheon, cosmology, ethical system)
- Kinship structure (family/clan/lineage organization, inheritance rules)
- Economic paradigm (subsistence, redistributive, mercantile, tributary, post-scarcity, per CCT context)
- Technology stance (Part 8 TA posture — promotion, restriction, monopoly, openness)
- Cultivation stance (Part 3/4 posture — meritocratic, aristocratic, forbidden, mandatory)

**Affiliation Agreement / Faction-Pair Relationship State (governed by Part 23 → `ledger-people-society-affiliation`):**
Two sub-types tracked in separate files:
*Named Affiliation Agreements* — formal treaties, pacts, compacts, accords:
- Agreement name (canonical name as established in prose)
- Parties (all named signatories)
- AFF spectrum position (Part 23 AFF-1 through AFF-14)
- Core obligations, permissions, prohibitions, and activation clauses
- Secrecy layer (public / semi-public / covert)
- Violation profile and CSS consequence class
- Current status (active / suspended / violated / dissolved)
*Faction-Pair Relationship State* — AFF spectrum tracking between named faction pairs:
- Current AFF position per axis (military / economic / intelligence / political / ideological / cultivation)
- Public layer vs. covert layer distinction
- Relationship history (prior positions and triggering events)
- Active agreements cross-references

> **[Repo layout note]** `ledger-people-society-affiliation` above refers to `.claude/story-memory/ledger-people-society-affiliation` in the current repo layout (post-.claude/ migration).

**Information Entity (governed by Part 24 → `ledger-people-society-information`):**
- Classification tier (Part 24 Area 2 five-tier system — Tier I Sovereign through Tier V Common)
- Custodian (faction, character, or institution that holds the information; chain of custody)
- Access control (who may read, who may copy, who may destroy)
- Decay rate (how quickly the information loses strategic value; event-triggered obsolescence)
- Corruption risk (probability of the information being altered, forged, or partially lost)
- Known copies/versions (inventory of instances and their locations; unauthorized copies if any)
- Exposure consequences (CSS event class if disclosed)

> **[Repo layout note]** `ledger-people-society-information` above refers to `.claude/story-memory/ledger-people-society-information` in the current repo layout (post-.claude/ migration).

**Travel Route / Gate Network / Infrastructure (governed by Part 15 → `ledger-worlds-travel`):**
*Named Travel Routes:*
- Start and end points (Part 13 location hierarchy)
- Paradigm band (Part 15 ST/OS/IS/GT/CT-Band) and tier range
- Standard travel time and CMS distance (Part 14)
- Hazards and faction control
*Named Gate Networks (Formation Teleportation Arrays, star gates):*
- Node locations, gate type, range, throughput, activation energy, controller
*Named Infrastructure (waypoints, stations, hubs):*
- Location, type, canonical function, faction control, capacity

> **[Repo layout note]** `ledger-worlds-travel` above refers to `.claude/story-memory/ledger-worlds-travel` in the current repo layout (post-.claude/ migration).

**Spatial Landmark / Distance Measurement (governed by Part 14 → `ledger-worlds-distance`):**
*Named Spatial Landmarks:*
- CMS scale and precise location relative to named reference points
- Navigation function and visibility profile (soul sense range / tech sensor range)
- Type (formation array marker / natural feature / constructed waypoint / stellar body)
*Canonical Distance Measurements* (tracked in `_index.md` Registry B directly, no separate file needed unless complex):
- CMS value between named location pair, journey time at standard speed, establishing prose reference

> **[Repo layout note]** `ledger-worlds-distance` above refers to `.claude/story-memory/ledger-worlds-distance` in the current repo layout (post-.claude/ migration).

**Technology System / Technology Institution (governed by Part 8 → `ledger-technology-scale`):**
*Named Technology Systems:*
- Technology tier (Part 8 Tier 1–20) and domain type (Part 8 Type 1–14)
- Capability profile within tier; hard ceilings
- Owner/operator; location; AI classification if applicable (Part 10 S1–S5)
- CS%/TS% values; current status
*Named Technology Institutions:*
- Institution type (ACR / STF / SII per Part 22), domain focus, achieved tier
- Research frontier, secrecy status, leadership

> **[Repo layout note]** `ledger-technology-scale` above refers to `.claude/story-memory/ledger-technology-scale` in the current repo layout (post-.claude/ migration).

**Research Program / Discovery Event (governed by Part 9 → `ledger-technology-growth`):**
*Named Research Programs:*
- Technology domain and current/target tier
- Growth mechanism (Part 9 — Systematic / Accident / Cultivation-Assisted / Transfer)
- Prerequisite status (Category I scientific / II resource / III institutional)
- Current status and secrecy classification
*Named Discovery Events:*
- Domain, knowledge layer achieved (Part 10 L1–L4), tier impact
- Discoverer; paradigm-shift event status; diffusion state

> **[Repo layout note]** `ledger-technology-growth` above refers to `.claude/story-memory/ledger-technology-growth` in the current repo layout (post-.claude/ migration).

**Scientific Framework / Paradigm-Shift Event / Knowledge Asset (governed by Part 10 → `ledger-technology-science`):**
*Named Scientific Frameworks:*
- Domain (Part 8 Type 1–14); knowledge layer (Part 10 L1–L4)
- Core claims; predictive scope; limitations; current paradigm status
- Civilization of origin; diffusion (who operates within this framework)
*Named Paradigm-Shift Events:*
- Prior paradigm, triggering anomaly, shift event, new paradigm
- Civilization impact; historical date
*Named Knowledge Assets:*
- Classification tier (Part 24); content; custodian; strategic value; known copies

> **[Repo layout note]** `ledger-technology-science` above refers to `.claude/story-memory/ledger-technology-science` in the current repo layout (post-.claude/ migration).

**System** (cultivation sect, academy, guild, political system — cross-governed by Part 22 and Part 25; technology institutions use `ledger-technology-scale`):
- Founding charter (the written or oral constitution of the system)
- Governing body (who makes the rules, how they are selected)
- Membership criteria (who may join, what they must demonstrate)
- Advancement path (how members rise, what milestones mark progression)
- Known branches (sub-systems, regional chapters, affiliated but independent bodies)

> **[Repo layout note]** `ledger-technology-scale` above refers to `.claude/story-memory/ledger-technology-scale` in the current repo layout (post-.claude/ migration).

**Character (governed by Part 16):**
- All lore fields enumerated in the hero/villain/side-character ledger schemas (Parts 17/18/19)
- The three-tier lore-depth spectrum established by Part 19 (Tier A / B / C side character profiles) governs the required depth for non-hero characters
- Heroes (Part 17) require maximum depth; villains (Part 18) require comprehensibility-sufficient depth; side characters (Part 19) follow the Tier A/B/C schema

**Culture / Festival (governed by Part 25):**
- Origin myth (the narrative the culture tells about why the practice exists)
- Calendar position (date or astronomical anchor)
- Ritual components (sequence of events, participants, objects, sounds, foods, garments)
- Regional variation (how the practice differs across the culture's geographic spread)
- Political significance (what the ritual performs socially — legitimization, reconciliation, mourning, bonding)
- Lore-integration with major factions/kingdoms (how the ritual intersects with the governance structures that participate in or host it)

**Relic / Artifact (governed by Part 12):**
- Origin (who forged, found, or imbued it; under what circumstance)
- Original owner (the first known wielder)
- Transfer history (lineage of ownership; how it moved from hand to hand)
- Grade (per Part 12 tier system)
- Awakening condition (what triggers the relic's active properties)
- Known abilities (what the relic does, within its Part 12 governance)

**Weapon (governed by Part 33):**
- Smith (who made it; under what conditions)
- Commission story (why it was made; for whom; what the making cost)
- Transfer history (ownership lineage)
- Named-move affinity (what Part 6 Named Moves the weapon is shaped for, if any)
- Grade (per Part 33 classification)
- Distinguishing marks (physical features that identify this particular weapon)

**Vehicle (governed by Part 32):**
- Designer (who engineered it)
- Commission date (when built)
- Operator lineage (who has piloted/owned it)
- Distinguishing features (physical and functional signature)
- Known missions (events it has participated in)

### 17.3 — The Breadth-and-Depth Standard

Lore for all named entities must be created with extreme breadth and depth. This Sub-Area operationalizes that standard.

**Breadth:** Every axis listed in 17.2 for the entity's category must be present in the ledger entry — not just the axes that the current scene touches. A kingdom's lore entry must include its economy even if the current scene is about its court politics. A faction's lore entry must include its recruitment practices even if the current scene is about its military operations. Absence of an axis is a completeness failure, audited under AL-10. The breadth standard is what prevents lore from being written only to the scene's immediate need and then becoming contradictory when a later scene draws from an unaddressed axis.

**Depth:** Each axis must carry enough content to seed at least one future prose scene without contradiction. A one-line placeholder ("founded long ago by a great warrior") fails depth. A depth-compliant entry gives: specific names, specific dates or era-anchors, specific founding events, specific named successors or known figures, specific signature cultural or political features, and at least one ongoing tension or open question that future prose can resolve. Depth is measured not by word count but by generativity — a depth-compliant entry is a scene-seed; a depth-insufficient entry is a label.

**Proportionality Exception:** The breadth-and-depth standard applies at full strength to entities of narrative significance — locations the heroes visit, factions the heroes interact with, characters who speak, cultural events that frame the story. For strictly background entities that are named but not narratively active (a neighboring kingdom referenced once, a historical faction mentioned in passing), the minimum is satisfied by populating the axes to the depth required for internal consistency of the reference, not to full scene-seed generativity. Background entities may be promoted to full breadth-and-depth at any later point if a future scene activates them.

**The Depth Test:** For any lore entry, apply the scene-seed question: "Can I write a pacing-appropriate immersion scene (3500%–5000%; all ten Depth Pillars satisfied) in this location / about this faction / featuring this character / rendering this festival using only what is in the ledger?" If the answer is yes, depth is satisfied. If the answer is no, the ledger entry must be expanded.

### 17.4 — Lore Recording Protocol

**Ledger Schema Integration:** Every ledger folder's `_index.md` shall include a dedicated **Lore Section** specification whose structure matches the entity category's axes per 17.2. The ledger schema update shall be applied to existing ledger schemas and entity files as a priority update.

**First-Appearance Capture:** First-appearance prose of a named entity triggers lore capture in the same Gate-2 sequence as the prose's ledger state update. The Gate-2 sequence executes: (a) per-Prose `.docx` write; (b) per-Prose `.md` write; (c) ledger state update for affected entities; (d) ledger lore update for named entities introduced or first-named in this Prose — this step creates the entity's ledger file if it doesn't exist (Rule 5.3.4a) and populates it with minimum lore fields per this Area; (e) Post-Prose Audit. Gate 2 is not complete until step (d) has been performed for every named entity in the Prose that lacks prior lore.

**Narrative Summary Paragraph Mandate (aligns with Part 1 Area 6.3 Step 3b):**
Every ledger section that is touched by a prose unit must be enriched with a **narrative summary paragraph** — not just field values. This paragraph synthesizes what the section now knows about the entity in coherent, prose-quality language. The paragraph is updated cumulatively with each new prose contribution:
- The first time a section is populated, the paragraph captures everything the introducing prose established about that aspect of the entity.
- Each subsequent prose unit that adds to the entity's characterization extends or revises the paragraph to incorporate the new information.
- The paragraph is written in third person, present tense, as a description of the entity's current canonical state — not as a log of what happened.

**What "narrative summary paragraph" means in practice:**
- **Character Section 5 (Psychology):** "Varys presents as composed and strategically cautious, but the prose has established a buried guilt response when his kingdom's vulnerability is mentioned directly — his jaw tightens, his left hand closes. He does not acknowledge this response consciously. His PIS baseline is 2 (Mild Operational Stress) with a latent spike to PIS-4 when sovereignty is threatened."
- **Location Section 2 (Character):** "Azure Sky Kingdom is a mid-range cultivator civilization built on the Lyraen River's eastern bank, with architecture that mixes grey river-stone with carved azure-veined marble. The smell of the river and of river-market commerce dominates the lower districts. The royal district sits elevated, visible from 30 km."
- These are not lists. They are short scene-seed paragraphs that any author could use to write the next scene involving this entity without inventing facts.

**Pre-Prose Lore Read (extends Rule 7.1.1(i)):** The Pre-Prose Read Mandate (Rule 7.1.1(i)) is extended to include reading the Lore Section of every ledger entity file referenced by name in prior Prose within the same Chapter. This ensures continuity of lore voice and prevents contradiction.

**Audit Hook:** No prose unit may pass Post-Prose Audit if any of its named entities lacks the minimum lore fields specified by 17.2. The audit hook is the new Part 1 Area 8.13 ALCA Mode A dimension AL-10 (Lore Completeness Alignment).

### 17.5 — Lore Consistency and Retroactive Enrichment

**Establishment:** Once lore is recorded in a ledger, it is fixed under the same Establishment Threshold as Area 2.3 (Negotiable Canon Establishment Rule). The lore becomes a reference point that future prose and future ledger updates may neither contradict nor silently overwrite.

**Retroactive Enrichment:** Later prose may enrich established lore — deepen the founding story, add named subordinates, extend the cultural calendar, reveal previously unknown branches — per the Retroactive Enrichment Rule (Area 2.4 / Area 11.2). Enrichment must be consistent with all prior established lore on that entity.

**Contradiction Handling:** A contradiction between new prose and established ledger lore is a CCIA violation. The prose may not overwrite the ledger lore unilaterally. Resolution pathway: (a) identify the contradiction during the Post-Prose Audit; (b) determine whether the new prose or the existing ledger lore is the correct canonical state; (c) if the existing lore is correct, the prose is revised; (d) if the new prose is correct and the existing lore is wrong, a formal Canon amendment is made to update the lore (the ledger lore does not change via prose fiat — it changes via formal amendment).

**Silent Overwrite Prohibition:** Editing ledger lore without a corresponding formal amendment or Post-Prose Audit finding is prohibited. This preserves the audit trail of how lore has evolved and prevents the ledger from silently diverging from the prose that established its content.

### 17.6 — Lore Delivery in Prose (Alignment with Contextual Earning Law)

The Lore Creation Law (Area 17) governs lore's **existence** in the ledger. The Contextual Earning Law (Area 15) governs lore's **delivery** in the prose. The two Areas are complementary, not redundant.

**Storage vs. Rendering:** The ledger stores the full lore to the Breadth-and-Depth Standard (17.3). The prose earns whatever fragment of it the scene requires through the Three-Beat Test (Area 15.4). A festival's full ritual calendar lives in the ledger; the scene renders only the fragment that the Three-Beat Test makes load-bearing. A kingdom's full economic profile lives in the ledger; the scene renders only the aspect the current beat activates. A faction's full recruitment protocol lives in the ledger; the scene shows only the moment of recruitment that the current character is living through.

**The Author's Workflow:** (1) Before writing the scene, read the ledger lore for every named entity that will appear. (2) During writing, select the fragments of that lore that the scene's Three-Beat Test can earn. (3) Render those fragments through the preferred delivery mechanisms of Area 15.5 (sensed impression, rendered use, comparative behavior, consequential naming, earned exposition). (4) Leave the rest of the lore in the ledger, where it waits to be earned by a future scene.

**Immersion Preservation:** A scene that dumps ledger lore — that renders the full founding history of a kingdom when the scene's Three-Beat Test earns only the fact that the current king is the founder's grandson — is a Contextual Earning Law violation (Area 15), not a Lore Creation Law success. The two Areas together require: *lore exists in full, but is delivered in fragments that the scene earns*. Lore completeness is the precondition for earned delivery; earned delivery is the precondition for immersion; immersion is the terminal value.

**No Conflict With Breadth-and-Depth:** Writing full lore to the ledger does not pressure the prose to render it. The ledger is a reservoir. The prose is a draw. A deep reservoir makes for rich, non-repetitive draws over many scenes. A shallow reservoir forces the prose to invent, which returns the author to the contradiction-risk that Area 17 exists to prevent.

---

## Cross-References
| Related Skill | Relation | Source |
|---|---|---|
| ssc-cultivation-p03-cultivation-ladder-realm-hierarchy | HARD | Part 34 Area 5: Cultivation realm names are Locked Canon under Part 28 |
| ssc-cultivation-p03-lifespan-mechanics | HARD | Part 34 Area 5: Cultivation realm names are Locked Canon under Part 28 |
| ssc-cultivation-p03-power-density | HARD | Part 34 Area 5: Cultivation realm names are Locked Canon under Part 28 |
| ssc-cultivation-p03-realm-transition | HARD | Part 34 Area 5: Cultivation realm names are Locked Canon under Part 28 |
| ssc-cultivation-p03-cultivation-talent | HARD | Part 34 Area 5: Cultivation realm names are Locked Canon under Part 28 |
| ssc-cultivation-p03-growth-speed | HARD | Part 34 Area 5: Cultivation realm names are Locked Canon under Part 28 |
| ssc-cultivation-p03-power-comparison | HARD | Part 34 Area 5: Cultivation realm names are Locked Canon under Part 28 |
| ssc-cultivation-p03-damage-tolerance-recovery | HARD | Part 34 Area 5: Cultivation realm names are Locked Canon under Part 28 |
| ssc-cultivation-p03-affinity-cultivation | HARD | Part 34 Area 5: Cultivation realm names are Locked Canon under Part 28 |
| ssc-cultivation-p03-heart-cultivation | HARD | Part 34 Area 5: Cultivation realm names are Locked Canon under Part 28 |

## Governing Authority
Subordinate to the shared Part 1 (audit law) + Part 34 (knowledge graph) grounding in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.

## Source Provenance
Part 28, Area 17 — "Lore Creation Law" · canon v4.33 · migrated 2026-08-03
