---
name: manual-and-weapon-style-law
description: Governs manuals, the written or encoded transmission texts (Part 6 Area 7.1 Method L-2, Manual Study) that each hold a group of Named Moves for exactly one weapon type, and the weapon-style disciplines they teach. The eight manual grades (Basic, Intermediate, Advanced, Elite, Signature, Fusion, Catastrophic, Mythic) with their fixed move-type composition, the 5-to-15 move rule, the fixed rounding rule and the 8-grade by N=5..15 composition table; the Known-but-Latent state model (every move in a held manual is Usable, Conditional or Latent for a given character, computed from the Part 6 Access Table, which is not amended) and the general Seal Rule (an effective-realm cap plus a blocked-type list, as the Olympus Suppression Seal binds Hercules and Bison); School Moves versus a personal Signature (Part 6 identity binding amended in scope, purpose kept); the five realm bands (M1, M2, XT, CF, DV) and the per-grade distribution of manuals across them; the four requirement ladders (energy, cultivation, affinity, sovereignty) with per-grade defaults grounded in Parts 3, 4 and 6; acquisition channels, institutions, rarity, access and copy-control; learning and mastery with manuals (Novice start, no skipping); the registry of the 79 weapon types and their relation to the Part 33 technology weapon taxonomy (powder weapons and siege engines stay within the Tier 3 handling sheet in Phase 1); the Manual Ledger (`ledger-manuals/`, CSV files keyed by one ID scheme, queried by ID and not searched, with the exact header line of every file, the characters and kits files, and the read-only query tool); eligibility for Tier C and Tier D characters; naming and registration (manual titles are plain-italic named items, move names are bold-italic Named Moves, the move-naming law of Rule 42.12.2.3 (Canon Amendment 2026-10-08: one or two words, tied to the weapon type and the level and grade of the move, never to a place, setting, tactic or enemy), Gate 2 flow, uniqueness across the whole ledger, the Azorion and Gale registers); narration standards N42-1 through N42-9; the cross-Part dependency table; and the exact amendments Part 42 requires of Parts 6, 12, 17, 18, 19, 28, 33 and 37. Reach for this whenever a manual, a library or academy stock of techniques, a hero's or side character's manual kit, a weapon style, a School Move or a Latent move is planned, named, registered, written or audited. This is canon Part 42, domain cultivation, the single consolidated authority for the whole Part.
user-invocable: false
---

# Manual and Weapon Style Law

**Authority Tier:** 1 (Domain Authority — Cultivation; see `.claude/guardrails/authority/guardrail-authority-tier-system.md`)
**Domain:** Cultivation — Manual and Weapon Style Governance: Founding and Scope (what a manual is and is not, what the Part owns and what stays with Parts 3, 4, 6, 12, 28, 33 and 37), the Eight Grades, Composition and Move Counts (the fixed rounding rule and the composition table), Known but Latent and the Seal Rule, School Moves and Personal Signature, Realm Bands and their Distribution, the Requirement Ladders (energy, cultivation, affinity, sovereignty), Acquisition Channels, Institutions and Copy Control, Learning and Mastery with Manuals, the Weapon-Type Registry and its Relation to Part 33, the Manual Ledger (folders, IDs, exact CSV headers, validation, the query tool), Characters, Kits and Eligibility, Naming and Registration, Narration Standards (N42-1 to N42-9), Boundaries and the Cross-Part Dependency Master Table, and the Amendments Part 42 Requires of Other Parts
**Governing Canon Parts Cross-Reference:** Parts 2, 3, 4, 6, 7, 12, 17, 18, 19, 22, 23, 25, 28, 29, 30, 33, 37, 38, 39, 40, 41

---

## Overview

Part 42 is the Starward Saga Canon's Manual and Weapon Style Law: the one home for the written and encoded texts through which Named Moves are taught, and for the weapon-style disciplines those texts teach. Part 6 says how a move is classified, named, learned and registered. Part 3 and Part 4 say what a body and a soul can do. Part 33 says what a technology weapon is. None of them says what a book of moves is, who may read it, which weapon it teaches, how many moves it holds, which realm it suits, where it is kept, or how a character who holds it but cannot yet use all of it is recorded. Part 42 says all of that, and gives every manual and every manual-borne move one ID in one database-style ledger, so that an agent asks for an ID and reads the answer instead of searching text. This Part is Canon v10.0.

**Design.** A manual teaches one weapon type. Manuals come in eight grades, Basic to Mythic, and each grade has a fixed mix of Part 6 move types and a move count of 5 to 15. A manual is tied to a realm band and carries four requirements (energy, cultivation, affinity, sovereignty). Institutions hold manuals in libraries, colleges, academies, sects, orders, kingdoms and empires; some manuals are found in quests, tombs and vaults. A character may hold a manual of any grade: each move in it is Usable, Conditional or Latent for that character, and the manual is a growth track (Area 3). The Part 6 Access Table is not amended. The Signature, Fusion, Catastrophic and Mythic moves in an institutional manual are School Moves, owned by the school and teachable; a hero's own personal Signature stays identity-bound (Area 4).

**What Part 42 owns and what it points at.** It owns: the definition of a manual; the eight grades, their composition and move counts; the Usable, Conditional and Latent states and the Seal Rule; the School Move rule; the realm bands and the four requirement ladders; the channel, access and copy-control codes; the manual-learning rules; the registry of weapon types; the Manual Ledger and its IDs, headers and checks; the character, kit and eligibility files; and the naming and narration rules for manuals and manual-borne moves. It does not take over Part 6 (what a move is, its Type, Function, access table, energy cost classes, mastery grades, naming patterns, learning methods and the generic register), Part 3 (the ladder, reserves, the power table), Part 4 (the affinity levels, soul and heart), Part 33 (the technology weapon taxonomy, tiers and handling sheet), Part 28 (the Naming Law and the named-item form), Part 37 (the ledger schema system) or Part 17, 18 and 19 (the character ledgers). It points at them. Domain Ownership (`guardrails/authority/guardrail-domain-ownership.md`) forbids any of those Parts from ruling on manuals quietly; this Part is the owner.

**How the Areas run.** Area 1 founds the Part and draws its boundary. Area 2 sets the eight grades, the composition, the move-count rule and the rounding table. Area 3 sets Known but Latent and the Seal Rule. Area 4 sets School Moves and the personal Signature. Area 5 sets the realm bands. Area 6 sets the four requirement ladders. Area 7 sets channels, institutions and copy control. Area 8 sets learning and mastery. Area 9 holds the weapon-type registry and the Part 33 relation. Area 10 is the Manual Ledger: folders, IDs, headers, checks and the query tool. Area 11 is characters, kits and eligibility. Area 12 is naming and registration. Area 13 holds the narration standards. Area 14 draws the boundaries and holds the dependency table. Area 15 states the amendments this Part requires of other Parts.

**One home for each rule.** Where another Part carries a pointer to a rule of this Part, it carries a short pointer by Area number and name, and this Part stands on any difference about manuals. On any difference about realm access, the Part 6 Access Table and Part 3 Area 16.2 stand. On any difference about a hero's realm, affinity or seal, the hero's own ledger stands, and the Manual Ledger mirror is corrected. The numbers in this Part are rules of a reference system that the author set, for the ledger. They are never a pace or a quota for the story (Rule 42.1.3.1).

This file is the single authority for the whole of Part 42.

---

## Area 1 — Founding and Scope

### 1.1 — What a Manual Is

**Rule 42.1.1.1 — Definition.** A **manual** is a written or encoded transmission text that holds a group of Named Moves for exactly one weapon type. Written or encoded means a bound book, a scroll, a carved tablet, a jade slip, a recorded formation or any equivalent record that Part 6 Area 7.1 Method L-2 (Manual Study) reads. Every manual has one `weapon_id` (Area 9), one grade (Area 2), one realm band (Area 5), four requirements (Area 6), one origin and one ID (Area 10), and 5 to 15 moves.

**Rule 42.1.1.2 — A Manual Is a Text, a Move Is the Content.** The manual is the carrier. The Named Moves in it are Part 6 Named Moves, each with its own Type, Function and ID. The manual title is a named item (Area 12). A manual is not itself a Named Move, and a Named Move is not itself a manual.

**Rule 42.1.1.3 — What a Manual Is Not.** A manual is not:
- a source of power, realm or equipment. Reading a manual gives knowledge of form and theory, and nothing else (Rule 42.3.1.2);
- a Part 33 weapon. It teaches a style that uses a weapon (Area 9);
- a Named Relic or Artifact, unless the author registers that one manual as a relic under Part 12, in which case it has a relic entry as well as its manual row;
- a personal Signature. A personal Signature is identity-bound and is registered under its owner (Area 4);
- a named document or agreement of Part 28 Rule 20.8.7. A manual is registered in the Manual Ledger, with a pointer row in `ledger-named-items` (Area 12), and not in `ledger-society-information`;
- a spec, a plan or a count of anything the story must reach (Rule 42.1.3.1).

**Rule 42.1.1.4 — One Weapon Type Per Manual.** A manual holds the moves of one weapon type and no other. A style that spans two weapons (a sword and shield style, a dual-axe style) is two manuals, one per `weapon_id`, or a personal or found manual whose `weapon_id` is the one primary type and whose moves name the second item in their descriptions. This Part does not add a second `weapon_id` column. Where a hero's manual is a paired style (dual axe, sword and shield), the manual takes the primary type and the description of each move says what the off hand does.

### 1.2 — What Part 42 Owns and What Stays Elsewhere

**Rule 42.1.2.1 — What Part 42 Owns.** The definition of a manual (Area 1); the eight grades, composition, move counts and the rounding table (Area 2); the Usable, Conditional and Latent states and the Seal Rule (Area 3); the School Move rule (Area 4); the realm bands and distribution (Area 5); the requirement ladders and their defaults (Area 6); channels, institutions, rarity, access and copy control (Area 7); the manual-learning rules (Area 8); the registry of the 79 weapon types (Area 9); the Manual Ledger, its IDs, headers and checks (Area 10); the characters, kits and eligibility files (Area 11); the naming and registration of manuals and manual-borne moves (Area 12); the narration standards N42-1 to N42-9 (Area 13).

**Rule 42.1.2.2 — What Stays Elsewhere.**

| Matter | Stays with |
|---|---|
| What a Named Move is; its Type and success rates; its Function; the Access Table 4.1; the cost classes of Area 5.3; the mastery grades; the naming patterns of Area 6.2; the five learning methods; Lineage Techniques; the generic register of Rule 6.5 | Part 6. Part 42 reads them and amends only the scope and extension rules of Area 15 |
| The cultivation ladder, reserves, the Move Access Ceiling of Area 16.2, the Depletion States | Part 3 |
| The nine Affinity Levels, the milestones by realm, the 50-type catalog, the Heart and Soul ladders | Part 4 |
| What a technology weapon is, its type, tier, scale class and the Tier 3 Handling Sheet | Part 33 |
| How a name is made, the named-item form, the Rule 20.3 naming method and the Rule 20.8 register duty | Part 28 |
| The layout of a ledger folder, the Baseline and Living (B/L) classification, thresholds | Part 37 |
| The hero, villain and side-character ledgers and their Section 3 | Parts 17, 18 and 19 |
| The institutions themselves (the Nine Halls, the academies, the military orders), their rank ladders and their rules | Parts 22, 23 and the faction entries |
| The forbidden entity of Phase 1 and the Phase 1 narrative ceiling | Part 30 (Law P30-L8; Part 3 Rule 1.7.3) |

**Rule 42.1.2.3 — Locked Canon Untouched.** The Part 6 Access Table (Area 4.1), the Part 3 Move Access Ceiling (Area 16.2), the Part 4 Affinity Level milestones, the Part 30 Phase 1 narrative ceiling and the Part 30 Law P30-L1 are not changed by this Part. Rule 42.3.1.1 states the consequence for access.

### 1.3 — The Principles

**Rule 42.1.3.1 — A Fact of the World, Never a Gate.** The Manual Ledger records what manuals exist and who holds them. Its counts (how many manuals per weapon, how many moves per grade, how many per kingdom) are ledger design set by the author, so that the stock is complete and queryable. They are not a pace for the story. No count, quota, minimum or maximum of manuals, moves or lessons per Area, Chapter, Novel-Part or Section exists in this Part. How a character comes to hold a manual, how long a study takes and when a Latent move becomes Usable is decided by the confirmed spec chain, the heroes' own arcs and Part 30, never by a table here.

**Rule 42.1.3.2 — One ID, Queried and Not Searched.** Every manual and every manual-borne move has one ID (Area 10). An agent that needs a fact about one asks the query tool for the ID, or reads the one CSV file the ID names. An agent does not search text across the ledger. The author's directive of 2026-10-05: "instead of using AI for grepping too much we will use IDs, like a database query."

**Rule 42.1.3.3 — Known Is Not Usable.** A character may know a manual and hold it, while some of its moves cannot yet be executed. The record of that is a per-move state computed from the character's effective realm (Area 3). Holding never changes realm access.

**Rule 42.1.3.4 — Part 6 Stands on Realm Access.** Nothing in this Part widens or narrows the Part 6 Access Table. A manual of any grade gives no access that the Access Table does not give.

**Rule 42.1.3.5 — The Titles Are Items, the Moves Are Named Moves.** A manual title is a named item, set in plain italic. A manual move is a Named Move, set in bold-italic. CSV cells hold plain text. Area 12 holds the form.

**Rule 42.1.3.6 — Baseline, Changed Only by the Author's Word.** The eight grades and their composition, the rounding rule and its table, the move-count ranges, the ID schemes, the exact header lines, the code ladders and the per-grade defaults are Baseline (B). They change only by a formal Canon Amendment on the author's own word (a `[CANON AMENDMENT]`, `guardrails/commands/guardrail-command-law.md`); the Continuity Checker then edits them, logs the amendment and runs ALCA Mode A. The rows of the CSV files are Baseline stock until an Area writes a name, after which their `first_area`, `status` and `notes` cells are Living (L) (Part 37 Area 5).

**Rule 42.1.3.7 — The Phase 1 Prose Ceiling Is Unchanged.** The ledger may use any realm name in any cell. Prose follows Part 3 Rule 1.7.3 and Law P30-L8 whatever band or grade a manual carries (Rule 42.13.1.4). A manual of a high grade may exist in a library of Phase 1 and be held by a Phase 1 character as a Latent growth track without any forbidden realm word appearing on the page.

---

## Area 2 — The Eight Grades, Composition and Move Counts

### 2.1 — The Eight Grades

**Rule 42.2.1.1 — The Grades.** A manual has exactly one grade, written in the ledger as a three-letter code. The grade fixes the mix of Part 6 move types (Part 6 Area 2.2) in the manual. The percentages below are of the manual's moves.

| Grade | Code | Basic | Intermediate | Advanced | Elite | Signature | Fusion | Catastrophic | Mythic |
|---|---|---|---|---|---|---|---|---|---|
| Basic | BAS | 100% | | | | | | | |
| Intermediate | INT | 70% | 30% | | | | | | |
| Advanced | ADV | 50% | 30% | 20% | | | | | |
| Elite | ELI | 40% | 30% | 20% | 10% | | | | |
| Signature | SIG | 30% | 30% | 20% | 10% | 10% | | | |
| Fusion | FUS | 30% | 30% | 20% | 10% | | 10% | | |
| Catastrophic | CAT | | 30% | 30% | 20% | 10% | | 10% | |
| Mythic | MYT | | | 30% | 30% | 20% | | 10% | 10% |

**Rule 42.2.1.2 — What Each Grade Is.**
- **Basic** explains the moves and how to do them so that anyone can learn them. It has few requirements. All of its moves are Basic type.
- **Intermediate** adds Intermediate-type moves to a Basic base. It carries energy-usage requirements and links to other cultivation skills.
- **Advanced** carries higher cultivation, affinity and sovereignty requirements than Intermediate.
- **Elite** carries more requirements again (cultivation, affinity, sovereignty).
- **Signature** adds Signature-type moves. They are School Moves when the manual is institutional (Area 4).
- **Fusion** adds Fusion-type moves in place of Signature-type moves.
- **Catastrophic** has no Basic moves. Its base is Intermediate and Advanced, and it holds Elite, Signature and Catastrophic moves.
- **Mythic** has no Basic or Intermediate moves. Its base is Advanced and Elite, and it holds Signature, Catastrophic and Mythic moves.

**Rule 42.2.1.3 — Grade Is Not Rank of the Reader.** A manual's grade says what its moves are. It does not say who may read it (Areas 6 and 7), and it does not say what a given reader can execute (Area 3).

### 2.2 — The Move-Count Rule

**Rule 42.2.2.1 — 5 to 15.** Every manual holds 5 to 15 moves. A manual with fewer than 5 or more than 15 moves fails the ledger check (Rule 42.10.8.1).

**Rule 42.2.2.2 — Ranges for Generated Manuals.** The workers that fill the Manual Ledger vary the count of each manual within the range for its grade. These ranges are fixed, and the ledger check reads them:

| Grade | BAS | INT | ADV | ELI | SIG | FUS | CAT | MYT |
|---|---|---|---|---|---|---|---|---|
| Moves per manual | 5 to 8 | 6 to 10 | 8 to 12 | 9 to 13 | 10 to 12 | 10 to 14 | 13 to 15 | 12 to 15 |

**Rule 42.2.2.3 — Fixed Counts the Author Set.** A library (institutional) Signature manual has 10 to 12 moves. A personal Catastrophic manual has 14 or 15 moves. A personal Signature manual (the Olympus Signature manuals of Hercules and Bison, the sword-family Signature manuals of the heroes) follows the Signature range. Any other personal manual follows the range for its grade.

**Rule 42.2.2.4 — Moves Are Listed Lowest Type First.** The moves of a manual are numbered `01` upward in the order Basic, Intermediate, Advanced, Elite, Signature, Fusion, Catastrophic, Mythic, and inside one type in the order a student meets them. The `seq` and the suffix of the `move_id` are the same two digits.

### 2.3 — The Rounding Rule and the Composition Table

**Rule 42.2.3.1 — The Rounding Rule (Fixed).** For a manual of N moves and a grade with listed types:
1. Moves per type = the floor of N times the percent.
2. Moves left over after step 1 go, one each, to the types with the largest fractional remainders. A tie goes to the HIGHER move type.
3. Then, if N is at least the number of listed types, every listed type gets at least 1. The move is taken from the type with the largest count, and a tie for the largest is taken from the LOWEST type.

**Rule 42.2.3.2 — The Composition Table.** The result of Rule 42.2.3.1 for the eight grades and N = 5 to 15. B is Basic, I Intermediate, A Advanced, E Elite, S Signature, F Fusion, C Catastrophic, M Mythic; the number is the count of moves of that type. This table is fixed and is the only source of a manual's `composition` cell (Rule 42.2.3.3).

| N | BAS | INT | ADV | ELI | SIG | FUS | CAT | MYT |
|---|---|---|---|---|---|---|---|---|
| 5 | B5 | B3 I2 | B2 I2 A1 | B2 I1 A1 E1 | B1 I1 A1 E1 S1 | B1 I1 A1 E1 F1 | I1 A1 E1 S1 C1 | A1 E1 S1 C1 M1 |
| 6 | B6 | B4 I2 | B3 I2 A1 | B2 I2 A1 E1 | B1 I2 A1 E1 S1 | B1 I2 A1 E1 F1 | I1 A2 E1 S1 C1 | A1 E2 S1 C1 M1 |
| 7 | B7 | B5 I2 | B4 I2 A1 | B3 I2 A1 E1 | B2 I2 A1 E1 S1 | B2 I2 A1 E1 F1 | I2 A2 E1 S1 C1 | A2 E2 S1 C1 M1 |
| 8 | B8 | B6 I2 | B4 I2 A2 | B3 I2 A2 E1 | B2 I2 A2 E1 S1 | B2 I2 A2 E1 F1 | I2 A2 E2 S1 C1 | A2 E2 S2 C1 M1 |
| 9 | B9 | B6 I3 | B4 I3 A2 | B3 I3 A2 E1 | B2 I3 A2 E1 S1 | B2 I3 A2 E1 F1 | I2 A3 E2 S1 C1 | A2 E3 S2 C1 M1 |
| 10 | B10 | B7 I3 | B5 I3 A2 | B4 I3 A2 E1 | B3 I3 A2 E1 S1 | B3 I3 A2 E1 F1 | I3 A3 E2 S1 C1 | A3 E3 S2 C1 M1 |
| 11 | B11 | B8 I3 | B6 I3 A2 | B5 I3 A2 E1 | B3 I4 A2 E1 S1 | B3 I4 A2 E1 F1 | I3 A4 E2 S1 C1 | A3 E4 S2 C1 M1 |
| 12 | B12 | B8 I4 | B6 I4 A2 | B5 I4 A2 E1 | B4 I4 A2 E1 S1 | B4 I4 A2 E1 F1 | I4 A4 E2 S1 C1 | A4 E4 S2 C1 M1 |
| 13 | B13 | B9 I4 | B6 I4 A3 | B5 I4 A3 E1 | B4 I4 A3 E1 S1 | B4 I4 A3 E1 F1 | I4 A4 E3 S1 C1 | A4 E4 S3 C1 M1 |
| 14 | B14 | B10 I4 | B7 I4 A3 | B6 I4 A3 E1 | B4 I4 A3 E1 S2 | B4 I4 A3 E1 F2 | I4 A4 E3 S1 C2 | A4 E4 S3 C1 M2 |
| 15 | B15 | B10 I5 | B7 I5 A3 | B6 I4 A3 E2 | B4 I4 A3 E2 S2 | B4 I4 A3 E2 F2 | I4 A4 E3 S2 C2 | A4 E4 S3 C2 M2 |

**Rule 42.2.3.3 — The `composition` Cell.** A manual's `composition` cell is written exactly as in the table for its grade and its move count (for example `B6 I2`), and the type counts must equal the number of its move rows of each `move_type` (Rule 42.10.8.1, check C-6). A personal or found manual follows the same table. A manual whose moves do not match the table is corrected by changing the moves, never the table.

**Rule 42.2.3.4 — What a Move of Each Type Needs in Its Row.** The move rows obey Part 6, and Part 42 adds only the following guards:
- a **Fusion**-type move names its two streams in its `description` as `streams: <X> + <Y>` (Part 6 Area 10.1, genuine integration), and the pair is one the Part 6 Area 10.2 requirements allow;
- a **Catastrophic**-type move states its scale as the destructive ceiling of its tier, not as a fixed size (Part 6 Type 7, Scale Requirement), and its `form` is INSTANT or CAST (Part 6 Area 5.3 gives it no channeled cost);
- a **Mythic**-type move states in its `description` the one thing it does that no cultivation energy mechanic explains (Part 6 Type 8, What Makes a Move Mythic), and its `form` is INSTANT or CAST; a successful use is a Part 27 consequence event (Part 6 Area 2.2);
- a **Signature**-type move in an institutional manual is a School Move (Area 4), and its `description` is written for the school and never as one person's story;
- a move's `function` obeys Rule 42.10.5.2.

---

## Area 3 — Known but Latent, and the Seal Rule

### 3.1 — The Principle

**Rule 42.3.1.1 — The Access Table Is Not Amended.** Part 6 Area 4.1 (the Access Table) and Part 3 Area 16.2 are unchanged. A manual of any grade can be held by a character of a lower realm. Holding is not using.

**Rule 42.3.1.2 — Known but Latent.** A character who holds a manual has learned its moves in form and theory. For that character each move in the manual is in exactly one of three states:
- **Usable:** the character's effective realm group allows the move's type, which is an Access Table cell of Standard or Possible. The character may execute the move, within the ordinary limits of reserve, injury, mastery and the weapon being in hand;
- **Conditional:** the Access Table cell is Rare. The move is Usable only when the Part 6 condition named for that cell is met and recorded (Rule 42.3.3.3);
- **Latent:** the cell is "—", or the character is under a seal that blocks the move's type (Rule 42.3.4.1). The character knows the form, the principle and the order of the movements. The character cannot execute it. Part 3 Rule 16.2.1 binds execution, and a Latent move is never executed in prose (Rule 42.13.1.3).

**Rule 42.3.1.3 — The Manual Is a Growth Track.** A Latent move is a goal in view, not a lost cause. When the character's effective realm group changes (a breakthrough, the weakening or lifting of a seal), the states are recomputed from the new realm, and moves become Usable without any other act. A move that becomes Usable begins at Novice mastery (Rule 42.8.2.2). The recomputation writes nothing to the move rows: the state is derived and is never stored per move (Rule 42.3.3.4).

**Rule 42.3.1.4 — Usable Is Not Mastery.** Usable means the realm allows the type. It does not say how reliably the character executes it. Reliability is the mastery grade and the success rates of Part 6 Area 2, and Part 6 Rule 4.2.1 still holds: reaching a realm does not guarantee the realm's ceiling in practice.

### 3.2 — The Nine Access Groups

**Rule 42.3.2.1 — The Groups.** Part 6 Area 4.1 names nine realm groups. This Part gives each a code, so that a character's effective realm turns into one group.

| Code | Realm group of the Access Table | Realms it covers |
|---|---|---|
| AG1 | Mortal Tier 1 | Unawakened, Skin, Muscle, Tendon, Bone, Blood, Marrow, Soul (the body stage Soul) |
| AG2 | Mortal Tier 2 Senior to Warrior | Senior, Warrior |
| AG3 | Mortal Tier 2 Champion to Ruler | Champion, Ruler |
| AG4 | Mortal Tier 2 Monarch | Monarch |
| AG5 | Xiantian Demigod to Void God | Demigod, Void God |
| AG6 | Xiantian True God to Absolute God | True God, Absolute God |
| AG7 | Core Formation to Core Assimilation | Core Formation, Core Assimilation |
| AG8 | Core Solidification | Core Solidification |
| AG9 | Divine Realm | Divine Transformation, Sea Formation, Heaven Treading, Divine Ascension, Divine Sea Realm |

**Rule 42.3.2.2 — The Matrix.** The cells of the Part 6 Access Table 4.1, written as codes: S is Standard, P is Possible, R is Rare, a dash is "—". This matrix is a copy for lookup. The Part 6 table stands on any difference, and a difference is a defect of this copy (Rule 42.3.2.3).

| Move type | AG1 | AG2 | AG3 | AG4 | AG5 | AG6 | AG7 | AG8 | AG9 |
|---|---|---|---|---|---|---|---|---|---|
| Basic | S | S | S | S | S | S | S | S | S |
| Intermediate | R | S | S | S | S | S | S | S | S |
| Advanced | - | - | P | P | S | S | S | S | S |
| Elite | - | - | - | R | S | S | S | S | S |
| Signature | R | P | P | P | S | S | S | S | S |
| Fusion | - | - | - | R | P | P | S | S | S |
| Catastrophic | - | - | - | - | P | S | S | S | S |
| Mythic | - | - | - | - | - | R | P | S | S |

**Rule 42.3.2.3 — Re-Derive, Do Not Copy.** The matrix is re-derived from Part 6 Area 4.1 whenever it is used by the query tool or carried into another file. On a difference, Part 6 Area 4.1 stands and the difference is corrected here.

### 3.3 — How the State Is Computed

**Rule 42.3.3.1 — The Four Steps.** For a character, a manual and a move:
1. Read the character's `effective_realm` from `characters.csv` (Area 11) and turn it into an access group (Rule 42.3.2.1).
2. Read the cell for the move's `move_type` and that group in the matrix. S or P gives Usable. R gives Conditional. A dash gives Latent.
3. If the move's type is in the character's `blocked_types`, the state is Latent whatever step 2 gave (Rule 42.3.4.1).
4. If the state is Conditional, it becomes Usable only when the condition code for that cell appears in the `note` of the character's kit row for that manual, as `COND:<code>` (Rule 42.3.3.3). Otherwise it stays Conditional, which prose treats as not available.

**Rule 42.3.3.2 — Unlock Realm of Each Type.** The `unlock_realm` of a move is the lowest realm at which the Access Table first gives its type a Usable cell (S or P). It is a function of the move's type, and each value is checked against the Access Table:

| Move type | Unlock realm (exact Part 3 position) | First Usable cell | Rare exception (Conditional) | Standard from |
|---|---|---|---|---|
| Basic | T1 Unawakened | S at AG1 | none | AG1 |
| Intermediate | Senior L1 Low | S at AG2 | AG1 near-Soul-stage physical specialists (Part 6 Rule 4.2.2) | AG2 |
| Advanced | Champion L1 Low | P at AG3 | none | AG5 |
| Elite | Demigod L1 Low | S at AG5 | AG4 Monarch | AG5 |
| Signature | Senior L1 Low | P at AG2 | AG1 exceptional physical specialists | AG5 |
| Fusion | Demigod L1 Low | P at AG5 | AG4 Monarch Level 9 Peak with an early-awakened soul only (Part 6 Rule 4.2.3) | AG7 |
| Catastrophic | Demigod L1 Low | P at AG5 | none | AG6 |
| Mythic | Core Formation L1 Low | P at AG7 | AG6 Absolute God peak only | AG8 |

**Verification against the Access Table, and the one slip fixed.** Advanced, Elite, Fusion, Catastrophic and Mythic agree with the author's list. Signature was listed as Mortal Tier 2 Warrior; the Access Table cell "Possible" belongs to the whole group Senior to Warrior (AG2), so the first Usable realm is Senior, not Warrior. The `unlock_realm` of a Signature-type move is therefore Senior L1 Low. The Signature manuals of Area 5 start their study at Warrior by their own `min_realm`, which is an admission rule and not an unlock rule (Rule 42.5.3.1).

**Rule 42.3.3.3 — The Condition Codes.** A Conditional move is Usable only when its condition is met. The conditions are those the Part 6 table names, and each has a code:

| Code | Cell | Condition (Part 6) |
|---|---|---|
| C-T1-SPEC | Intermediate at AG1 | a Mortal Tier 1 physical martial arts specialist near the Soul stage (the Marrow or Soul stage), with near-peak physical refinement (Part 6 Rule 4.2.2), and the move is a physical-architecture technique |
| C-T1-EXC | Signature at AG1 | an exceptional physical specialist, recorded as such in the character's own ledger |
| C-M-ELITE | Elite at AG4 | a Monarch whose own ledger records genuine Elite-level technique (Part 6 Area 2.2, Type 4) |
| C-M-FUSION | Fusion at AG4 | a Monarch at Level 9 Peak with an early-awakened soul and both qi circulation and soul (Part 6 Rule 4.2.3; Part 4 Area 2.5) |
| C-AG-MYTHIC | Mythic at AG6 | an Absolute God at the extreme peak of the realm only (Part 6 Rule 4.2.4) |

A condition is met only by the character's own ledger recording it. An agent never invents a condition, and the ledger records it only on the author's word.

**Rule 42.3.3.4 — Derived, Not Stored.** The state of a move for a character is derived by Rule 42.3.3.1. It is never written into a move row, a manual row or a kit row as a second fact. The query tool `usable CHARACTER` computes it (Rule 42.10.9.1). The one thing a kit row may store is the `COND:` token that meets a condition.

**Rule 42.3.3.5 — Live Conditions the Ledger Does Not Store.** Part 3 Area 16.4 sets live conditions that can lower access for a time: dantian or Core damage lowers effective realm by one Move Type for access, an active Qi Deviation of Grade 3 or more removes Advanced and above, and low reserve removes Elite at Depleted and everything but Basic at Critical (Part 3 Area 12.4). The Manual Ledger stores none of these. Prose obeys them, and the Pre-Write Ledger Check states any that apply.

### 3.4 — The Seal Rule

**Rule 42.3.4.1 — The General Seal Rule.** A **seal** is any binding that holds a character's expressed power below the character's true cultivation (Part 3, Part 13 and the character's own ledger name each one). For this Part a seal is two things written in `characters.csv`: an **effective-realm cap**, which is the realm the Manual Ledger reads as the character's `effective_realm`, and a **blocked-type list**, which is the move types the seal blocks outright, written as three-letter grade codes in `blocked_types`. A blocked type is Latent for that character whatever the effective realm gives. A character who is under no seal has `effective_realm` equal to `realm` and `blocked_types` of `none`.

**Rule 42.3.4.2 — The Olympus Suppression Seal.** Hercules and Bison are Demigods by true cultivation (Xiantian Demigod Level 1 Mid) held by the Olympus Suppression Seal at an effective Mortal Tier 2 Champion Level 8 High. The author's ruling: **Signature and Catastrophic are blocked by the seal itself.** Elite is also Latent, because the effective realm (group AG3) gives no Elite access. For them the file reads `effective_realm` of `Champion L8 High` and `blocked_types` of `SIG;CAT`. The result:

| Type | Effective realm AG3 | Seal block | State |
|---|---|---|---|
| Basic | S | none | Usable |
| Intermediate | S | none | Usable |
| Advanced | P | none | Usable |
| Elite | - | none | Latent (effective realm gives no access) |
| Signature | P | blocked | Latent (the seal) |
| Fusion | - | none | Latent (effective realm) |
| Catastrophic | - | blocked | Latent (the seal, and the effective realm) |
| Mythic | - | none | Latent (effective realm) |

**Rule 42.3.4.3 — When the Seal Changes.** As Phase 1 weakens the Seal, the effective cap rises (Part 30 gives the end-states, Ruler Level 7 Low for Hercules and Ruler Level 6 High for Bison). Both stay inside group AG3, so the states do not change while the cap rises inside it. `blocked_types` changes only on an author-set change to the seal itself, recorded in the character's own ledger and then mirrored. `effective_realm` is updated at Gate 2 when the character's own ledger changes it. The true `realm` is unchanged by the seal.

**Rule 42.3.4.4 — The Firmament Lock Is Not a Seal Here.** The Firmament Lock is the outer system ceiling (`ledger-worlds-location/sol-star-system.md` §2). It binds everyone in the system alike, it is not a per-character binding, and the Manual Ledger does not store it. The tighter binding governs, as the character's ledger and Part 3 say, and for Hercules and Bison that is the Seal.

**Rule 42.3.4.5 — The Seal Rule Is General.** Any later binding (a new seal, a suppression, a taboo oath that bars a type) is recorded the same way: an effective-realm cap if one applies, and a blocked-type list if types are barred. This Part adds no other kind of per-character restriction.

### 3.5 — Worked Examples

**Rule 42.3.5.1 — Worked States at the Phase 1 Start.** These are derived, not stored. They show the rule and are re-derived when used (Rule 42.3.3.4).

| Character, effective realm | Group | Manual (grade) | Usable | Latent |
|---|---|---|---|---|
| Varys, Ruler L3 Mid | AG3 | a Signature sword manual (SIG) | Basic, Intermediate, Advanced, Signature | Elite |
| Varys, Ruler L3 Mid | AG3 | his personal Catastrophic manual (CAT) | Intermediate, Advanced, Signature | Elite, Catastrophic |
| Valia, Ruler L1 Mid; Aalia, Ruler L1 Mid; Aeries, Ruler L2 Mid | AG3 | a Signature manual (SIG) | Basic, Intermediate, Advanced, Signature | Elite |
| Hercules and Bison, Champion L8 High under the Seal | AG3 with SIG and CAT blocked | a personal Signature manual (SIG) | Basic, Intermediate, Advanced | Elite, Signature |
| Hercules and Bison, Champion L8 High under the Seal | AG3 with SIG and CAT blocked | a personal Catastrophic manual (CAT) | Intermediate, Advanced | Elite, Signature, Catastrophic |
| Varya and Aegon, T1 Unawakened | AG1 | none held | | |

The Signature cell reads Usable for the four unsealed heroes because Part 6 Area 4.1 gives Signature at AG3 the value Possible, and the author's ruling counts Possible as Usable. Whether a School Signature-type move is executed well is a matter of mastery (Rule 42.3.1.4).

---

## Area 4 — School Moves and Personal Signature

### 4.1 — The School Move

**Rule 42.4.1.1 — Definition.** A **School Move** is a Signature-type, Fusion-type, Catastrophic-type or Mythic-type Named Move that sits inside an institutional manual (a manual of origin Common, Azorion or Gale). It is a Lineage Technique under Part 6 Area 7.2: it belongs to the school or institution that holds the manual, it is teachable by Method L-1 and Method L-2, and it is NOT any character's personal Signature. A manual-borne move of the types Basic, Intermediate, Advanced and Elite is a lineage or school technique too (Rule 42.12.5.2); the School Move rule is named for the four types that Part 6 Area 2.2 and Area 9.1 would otherwise bind to one person's identity.

**Rule 42.4.1.2 — Owned by the School, Taught Under Its Rules.** A School Move is owned by the institution named in the kingdom row of its manual (Rule 42.10.6.1) and is transmitted by that institution's recognized authorities under that institution's own rules (Parts 22 and 23). Teaching it outside the school without authority is the violation Part 6 Area 7.2 and Rule 7.4.4 already describe, and Part 6 Rule 7.4.2 still holds for a stolen manual: the thief learns by Method L-2 and starts at Novice.

**Rule 42.4.1.3 — Type and Rates Are Unchanged.** A School Move keeps the Type it is classified as (Part 6 Area 2), and the base and maximum success rates of that Type apply. A Signature-type School Move therefore has the Signature Type's rates (Part 6 Area 2.2, Type 5). The four depth levels of Part 6 Area 9.2 (Form, Understanding, Integration, Transcendence) describe a personal Signature deepening with its owner's life and do not apply to a School Move, whose progress is the ordinary mastery grades, Novice to Master (Part 6 Area 2.1).

**Rule 42.4.1.4 — The Register Kind.** A School Move is registered in the generic register as `Lineage or school technique` (Part 6 Rule 6.5.3), and in the Manual Ledger by its move ID (Rule 42.12.4.1).

### 4.2 — The Personal Signature

**Rule 42.4.2.1 — Identity Binding Stays.** A hero's own personal Signature, the move that the hero developed through Experiential Discovery (Method L-4) and that expresses who the hero is, stays identity-bound exactly as Part 6 Area 9.1 says. It is registered under the hero's own `Signature Named Moves` (Part 6 Rule 6.5.2) with the kind `Signature Named Move`. It is never a row of any manual, never taught from a manual, and cannot be learned from observation or from a transmission manual. A copy made from sight is Advanced at best (Part 6 Area 9.1).

**Rule 42.4.2.2 — Personal Manuals Carry the Source's Lineage Moves.** A personal manual (a mentor's, a master's or an archive's manual tied to one individual, Area 10.7) holds moves that belong to its source's lineage. A Signature-type or Catastrophic-type move in a personal manual is the source's lineage move, taught to the owner, and is not the owner's personal Signature. What the owner develops for the owner's own is registered separately under Rule 42.4.2.1.

**Rule 42.4.2.3 — Codifying a Founder's Form.** A school may codify a lineage-descended form of a founder's personal Signature only as a new Named Move under a new name (Part 6 Rule 6.4). The new move is a School Move with its own ID. The founder's Signature stays identity-bound, and its registration is unchanged.

### 4.3 — The Purpose That Survives

**Rule 42.4.3.1 — Scope Amended, Purpose Kept.** Part 6 Area 9.1's binding is amended in scope and not in purpose. Its purpose is that a person's own Signature cannot be copied from observation or from a transmission manual, so that a Signature stays the mark of one cultivator. That purpose holds. The scope is now stated as: the binding covers a personal Signature, and a School Move in an institutional manual is a teachable technique of the institution. Area 15 (Amendment 1) gives the exact text for Part 6.

**Rule 42.4.3.2 — What a Reader Does Not Gain.** A hero who studies a School Move gains a school technique. The hero gains no Signature, no depth level and no identity claim from it. A School Move that a hero comes to use as the hero's own mark, over a long practice, does not become a Signature by use. A Type Upgrade (Part 6 Area 9.3) or a new named creation is the route to a personal Signature.

**Rule 42.4.3.3 — Not a Loophole for Heroes.** The hero seeds hold School Moves of Signature type in their institutional manuals (Area 11). This does not give a hero a second personal Signature. Whether a hero has a personal Signature at all, and which, is the hero's own ledger.

---

## Area 5 — Realm Bands and Distribution

### 5.1 — The Five Bands

**Rule 42.5.1.1 — The Bands.** A manual is linked to a realm band. The band is a code in `realm_band`, and it is the band of the manual's `min_realm`.

| Code | Band | Part 3 range |
|---|---|---|
| M1 | Mortal Tier 1 | the eight stages Unawakened to Soul: body only, no qi (Part 3 Rule 1.2.1) |
| M2 | Mortal Tier 2 | Senior Level 1 Low to Monarch Level 9 Peak |
| XT | Xiantian | Demigod Level 1 Low to Absolute God Level 9 Peak. The author wrote "Xiantan"; the canon spelling is Xiantian |
| CF | Core | Core Formation Level 1 Low to Core Solidification Level 9 Peak. The author's list names the Core band; the code is CF (Core Formation is its first realm) |
| DV | Divine | Divine Transformation Level 1 Low to Divine Sea Realm Level 9 Peak. The author wrote "Dive"; the band is the Divine Realm |

**Rule 42.5.1.2 — The Ledger May Use Any Realm Name.** The ledger holds the true band and the true `min_realm` of every manual whatever the saga's Phase. The Phase 1 prose vocabulary is a rule for prose and does not reach the ledger (Rule 42.1.3.7, Rule 42.13.1.4).

### 5.2 — The Distribution Rule

**Rule 42.5.2.1 — The Rule, from the Access Table.** The distribution of a weapon's manuals across the bands follows the Access Table (Rule 42.3.2.2). Within one weapon type:

| Grade | Distribution across bands |
|---|---|
| Basic | About half M1 (body only, no qi use) and half M2. Neither band holds fewer than half of the weapon's Basic manuals rounded down |
| Intermediate | M2, with `min_realm` of Senior or Warrior. At most ONE near-Soul-stage Mortal Tier 1 physical-specialist exception per weapon (Part 6 Rule 4.2.2; the move's condition is C-T1-SPEC) |
| Advanced | The Mortal Tier 2 Champion-to-Ruler band (M2) and Xiantian (XT). Neither band holds fewer than one third of the weapon's Advanced manuals (Common and both kingdoms counted together) |
| Elite | Xiantian (XT) mainly. At most ONE Monarch-gated Rare manual (band M2, `min_realm` Monarch, condition C-M-ELITE) per weapon per kingdom |
| Signature | Per kingdom per weapon, the 6 are: four M2, one XT, one CF (Rule 42.5.2.2) |
| Fusion | XT or CF. The Monarch-gated Rare (C-M-FUSION) is allowed only in a personal manual |
| Catastrophic | XT, CF or DV. No M1 or M2 |
| Mythic | CF or DV. An XT True God to Absolute God manual (condition C-AG-MYTHIC) only in a personal or found manual |

**Rule 42.5.2.2 — The Six Signature Manuals of a Kingdom and a Weapon.** The Signature stock of one weapon in one kingdom is 6 manuals, numbered `001` to `006` for Azorion and `007` to `012` for Gale (Rule 42.10.2.3). Inside each kingdom's six:
- the first four are Mortal Tier 2 (band M2). Their `min_realm` values are non-decreasing in number order, the first is Warrior (any Level), and none is above Ruler Level 1 Mid, so the four spread from Warrior through Ruler and all four are within the reach of a character at Ruler Level 1 Mid. At least three of them have a minimum no higher than Ruler Level 1 Mid (the author's rule), and this Rule makes all four so;
- the fifth is Xiantian (band XT);
- the sixth is Core (band CF).

**Rule 42.5.2.3 — Common Manuals Have a Band Too.** A Common manual (origin Common) is in one band and appears in both kingdoms' stocks. A kingdom manual (origin Azorion or Gale) is in one band and appears in one kingdom's stock.

**Rule 42.5.2.4 — Brackenhold Has Its Own Signature Manuals, Not Six (Canon Amendment 2026-10-08).** The six-Signature pattern of Rule 42.5.2.2 belongs to Azorion and Gale. Brackenhold (Rule 42.10.2.6) holds only the Signature manuals the author names, numbered as extras after the Gale numbers, and each is a Mortal Tier 2 manual. No Brackenhold Signature manual is bound to the four-M2, one-XT, one-CF layout, and check C-11 does not read Brackenhold rows.

### 5.3 — `min_realm`

**Rule 42.5.3.1 — `min_realm` Is an Admission Position.** `min_realm` is the lowest realm at which an institution admits a student to study the manual from its first page (Rule 42.6.1.1). It is an exact Part 3 position and is not the unlock realm of the manual's highest move. A Signature manual with a `min_realm` of Warrior holds Elite and Signature moves that its early students cannot yet use (Latent, Area 3), and that is the manual doing its work as a growth track.

**Rule 42.5.3.2 — The Format.** `min_realm` is written in one of two forms and nothing else:
- Tier 1: `T1 <Stage>`, the stage being one of Unawakened, Skin, Muscle, Tendon, Bone, Blood, Marrow, Soul (for example `T1 Bone`);
- every other realm: `<Realm> L<n> <Sub>`, the realm being a Part 3 realm name, `n` a Level 1 to 9, and `Sub` one of Low, Mid, High, Peak (for example `Warrior L1 Low`, `Demigod L1 Low`). The sub-level words are Low, Mid, High and Peak; `powerlevels.csv` calls the first two Early and Medium, and Early is Low, Medium is Mid (Part 3 Area 1.6).

**Rule 42.5.3.3 — The Windows.** The `min_realm` of a manual lies inside the window for its grade and band. A manual outside its window fails the ledger check (check C-9).

| Grade | Band | Window of `min_realm` |
|---|---|---|
| BAS | M1 | `T1 Unawakened` to `T1 Bone` |
| BAS | M2 | `Senior L1 Low` to `Senior L9 Peak` |
| INT | M2 | `Senior L1 Low` to `Warrior L9 Peak` |
| INT | M1 (exception) | `T1 Marrow` or `T1 Soul` |
| ADV | M2 | `Champion L1 Low` to `Ruler L9 Peak` |
| ADV | XT | `Demigod L1 Low` to `Void God L9 Peak` |
| ELI | XT | `Demigod L1 Low` to `True God L9 Peak` |
| ELI | M2 (Monarch-gated Rare) | `Monarch L1 Low` to `Monarch L9 Peak` |
| SIG | M2 | `Warrior L1 Low` to `Ruler L1 Mid` (non-decreasing in number order) |
| SIG | XT | `Demigod L1 Low` to `Void God L9 Peak` |
| SIG | CF | `Core Formation L1 Low` to `Core Assimilation L9 Peak` |
| FUS | XT | `Demigod L1 Low` to `Absolute God L9 Peak` |
| FUS | CF | `Core Formation L1 Low` to `Core Solidification L9 Peak` |
| CAT | XT | `Demigod L1 Low` to `Absolute God L9 Peak` |
| CAT | CF | `Core Formation L1 Low` to `Core Solidification L9 Peak` |
| CAT | DV | `Divine Transformation L1 Low` to `Divine Sea Realm L9 Peak` |
| MYT | CF | `Core Formation L1 Low` to `Core Solidification L9 Peak` |
| MYT | DV | `Divine Transformation L1 Low` to `Divine Sea Realm L9 Peak` |

**Rule 42.5.3.4 — Never Below the Lowest Move.** `min_realm` is never below the unlock realm (Rule 42.3.3.2) of the manual's lowest-type move, so a student is never admitted to a manual none of whose moves they could yet use. Catastrophic manuals begin at Intermediate (unlock Senior) and Mythic manuals at Advanced (unlock Champion); their windows above are stricter and govern.

**Rule 42.5.3.5 — Why the Windows Are These.** Each window is drawn from the Access Table and Part 3 Area 16.2: Basic is standard at Tier 1; Intermediate is standard from Senior; Advanced is first possible at Champion and standard from Xiantian; Elite is standard from Xiantian with the Monarch exception; Signature is possible from Senior and standard from Xiantian; Fusion, Catastrophic and Mythic begin at Xiantian, Xiantian and Core. A Phase 1 character stands at Ruler Level 9 Low at most in prose, so Xiantian and Core manuals are, in Phase 1, held and not used (Rule 42.1.3.7).

---

## Area 6 — The Requirement Ladders

### 6.1 — The Principle

**Rule 42.6.1.1 — Requirements Are Admission Standards.** The four requirement columns, `energy_req`, `cultivation_req`, `affinity_req` and `sovereignty_req`, state what an institution asks of a student before it admits the student to study the manual by Method L-2 (and, with `min_realm`, what a teacher asks before teaching it). They are the eligibility test of Area 11. They do not decide whether a move in a manual the character already holds is Usable: that is the Access Table and the seal (Area 3). A character who holds a manual by another route (a mentor, an inheritance, a find) holds it under Area 3 whether or not the admission standard was ever met.

**Rule 42.6.1.2 — Closed Code Lists.** Each column takes codes from a closed list below, so that a worker fills a cell by rule and the ledger check reads it. A cell holds one code, except where a ladder says codes join with `+`. No other text stands in a requirement cell.

**Rule 42.6.1.3 — Basic Has Few, Higher Grades Have More.** The defaults of Rule 42.6.6.1 rise with the grade, so that a Basic manual asks little and a Mythic manual asks much. A manual's cell is never below the default of Rule 42.6.6.1 for its grade and band (check C-10).

**Rule 42.6.1.4 — Mortal Tier 1 Has No Qi.** A Mortal Tier 1 manual has `energy_req` NONE, `affinity_req` NONE and `sovereignty_req` NONE: there is no qi reserve (Part 3 Area 12.2), energy use is forbidden before the Second Awakening (Part 3 Rule 1.2.1), and affinity cannot manifest at Tier 1 (Part 4 Area 1.1). A Tier 1 Basic manual therefore demands NONE energy.

### 6.2 — The Energy Ladder (`energy_req`)

**Rule 42.6.2.1 — The Codes.** The energy requirement is the energy-use standard the student must be able to bear. The codes follow the cost classes of Part 6 Area 5.3 and the Reserve Impact shares there, and the reserves of Part 3 Area 12.2.

| Code | Meaning | Anchor |
|---|---|---|
| NONE | no qi, body and stamina only | Mortal Tier 1; Part 3 Area 12.2; Part 6 Rule 5.1 (stamina cost) |
| QI-MIN | own qi circulates; Minimal cost class, Reserve Impact Negligible (under 1%) | the Second Awakening onward; Part 3 Area 1.2.1 |
| QI-LOW | Low cost class, Reserve Impact Minor (1 to 5%) | Part 6 Area 5.3, Intermediate |
| QI-MOD | Moderate cost class, Reserve Impact Noticeable (5 to 15%) | Part 6 Area 5.3, Advanced |
| QI-HIGH | High cost class, Reserve Impact Significant (15 to 30%) | Part 6 Area 5.3, Elite |
| QI-VHI | Very High cost class, Reserve Impact Major (30 to 50%) | Part 6 Area 5.3, Fusion |
| QI-EXT | Extreme cost class, Reserve Impact Depleting (50 to 80%) | Part 6 Area 5.3, Catastrophic |
| QI-REAL | Reality-level cost class, Potentially Lifespan | Part 6 Area 5.3, Mythic |

The ladder runs NONE, QI-MIN, QI-LOW, QI-MOD, QI-HIGH, QI-VHI, QI-EXT, QI-REAL. The Signature type's cost is Variable (Part 6 Area 5.3), so a Signature manual takes the code its band's reserve supports (Rule 42.6.6.1).

### 6.3 — The Cultivation Ladder (`cultivation_req`)

**Rule 42.6.3.1 — What It Is.** The cultivation requirement is the state of body and qi architecture the manual presumes, plus the links to other cultivation skills that the student must already hold. It is not the realm (that is `min_realm`). It is written as one state code, optionally followed by link codes joined with `+`, for example `CIRC+LINK-PRIOR+LINK-STEP`.

**Rule 42.6.3.2 — State Codes.** Exactly one state code leads the cell.

| Code | Meaning | Anchor |
|---|---|---|
| NONE | no state required | Basic, Mortal Tier 1 |
| T1-SKIN, T1-MUSCLE, T1-TENDON, T1-BONE, T1-BLOOD, T1-MARROW, T1-SOUL | the Mortal Tier 1 body stage named, or above (T1-SOUL is the body stage Soul, not a soul rung) | Part 3 Area 1.2.1 |
| CIRC | the student circulates own qi: the Second Awakening is done | Part 3 Area 1.2.1 |
| MER-PART | primary meridians partly active (meridians 3 to 7) | Part 3 Area 16.2, Senior to Warrior |
| MER-FULL | full primary meridian activation | Part 3 Area 16.2, Champion to Ruler |
| MER-NET | complete meridian network, dantian at the mortal-tier maximum | Part 3 Area 16.2, Monarch |
| XT-FIELD | qi extends beyond the body and circulates as a living field | Part 3 Area 12.2, Xiantian |
| CORE-ON | a formed Core | Part 3 Area 1.4 |
| DIVINE | divine energy | Part 3 Area 1.5 |

**Rule 42.6.3.3 — Link Codes.** A link code names a skill the student must already hold. Link codes follow the state code, in this order, joined with `+`.

| Code | Meaning |
|---|---|
| DUAL-STREAM | the student can control two distinct power streams, with Adept mastery of a technique in each (Part 6 Rule 4.2.3 and Requirement F-1 of Area 10.2). A Fusion manual carries it |
| LINK-PRIOR | the student holds a manual of the same weapon type of the next lower grade (for FUS, CAT and MYT, any lower grade of the same weapon), at mastery of Practiced or better as the kit records it (Area 11) |
| LINK-STEP | the student holds a Mobility:Step Named Move of Basic type or higher, at Practiced or better |
| LINK-GUARD | the student holds a Defense:Shield or Defense:Deflect Named Move of Basic type or higher, at Practiced or better |
| LAW-INSIGHT | the student has a recorded deep enlightenment of the principle the Mythic move works on (Part 6 Type 8 and Area 2.2) |

The "links to other cultivation skills" that the author asked of Intermediate and higher are these codes.

### 6.4 — The Affinity Ladder (`affinity_req`)

**Rule 42.6.4.1 — The Codes.** The affinity requirement is a level of Part 4's nine Affinity Levels (Area 1.2 of Part 4), in the exact canon names, that the student holds as current level. Level 1 Null is NONE. Level 8 Sovereignty and Level 9 Origin Convergence belong to the sovereignty ladder (Area 6.5).

| Code | Part 4 level and name | Efficiency (Part 4 Area 1.2) |
|---|---|---|
| NONE | no affinity needed (Level 1, Null, is acceptable) | none |
| A2 | Level 2, Whisper | about 5% |
| A3 | Level 3, Echo | 15% |
| A4 | Level 4, Resonance | 25% |
| A5 | Level 5, Attunement | 35% |
| A6 | Level 6, Harmony | 50% |
| A7 | Level 7, Communion | 70% |

A code with the suffix `W` (A3W and so on) means the affinity must be weapon-aligned: Swords for the sword families (Bladed swords, Hook swords, Butterfly swords) and Strength for the unarmed family, the only two weapon-form types in the closed 50-type catalog of Part 4 Area 1.3. For every other weapon type no weapon-aligned affinity exists in the catalog, so `W` is never used there and the code means an affinity of any type at that level or higher. The Fusion code is `A4+A4` (two affinities, each at Level 4 or higher, Part 4 Area 1.6).

**Rule 42.6.4.2 — The Realm Cap on Affinity.** A requirement must be reachable by a student admitted at `min_realm`, and Part 4 Area 1.4 sets when each level is reachable: Levels 1 to 3 in Mortal Tier 2; Levels 4 and 5 at Xiantian; Level 6 at Core Formation or above; Levels 7 and 8 at Core Solidification or the Divine Realm. The cap by band:

| Band of `min_realm` | Highest affinity code the manual may ask |
|---|---|
| M1 | NONE (affinity cannot manifest) |
| M2 | A3 |
| XT | A5 |
| CF | A6 (A7 only when `min_realm` is Core Solidification) |
| DV | A7 |

A recorded affinity level in a hero's ledger is a ceiling, and the current level follows the milestones (Part 4 Area 1.4). The eligibility test therefore reads the lower of the ledger's level and the realm's cap (Rule 42.11.6.2).

### 6.5 — The Sovereignty Ladder (`sovereignty_req`)

**Rule 42.6.5.1 — What Sovereignty Means Here.** Sovereignty is Level 8 of the Part 4 affinity scale: the cultivator commands the aligned force as a natural authority. Every hero of the first series carries a Sovereignty affinity (for example Sovereignty, Swords) with a ceiling of Level 8, which the ledgers record as a ceiling that the current level follows by realm milestones. Because Level 8 is reached at Core Solidification or in the Divine Realm (Part 4 Area 1.4), a manual below the Core band that asks for sovereignty can ask only for the recorded ceiling, which is a test of the ledger and not of the present level.

**Rule 42.6.5.2 — The Codes.**

| Code | Meaning | Where it may stand |
|---|---|---|
| NONE | no sovereignty needed | any |
| SOV-C | the student's ledger records a Sovereignty affinity (ceiling Level 8) in any force | any band; the default for higher grades below the Core band |
| SOV-CW | the recorded Sovereignty ceiling is in the weapon-aligned force: Swords for the sword families and Strength for the unarmed family (same families as `W`, Rule 42.6.4.1) | only manuals whose `tradition` names that force; never the default |
| SOV-H | the student currently holds Level 8, Sovereignty | only a manual whose `min_realm` is Core Solidification or in the Divine Realm |
| SOV-O | the student currently holds Level 9, Origin Convergence | only a Divine Realm manual; Part 4 places Level 9 at the Divine Sea Realm |

The ladder runs NONE, SOV-C, SOV-CW, SOV-H, SOV-O.

**Rule 42.6.5.3 — The Heroes Meet the Ceiling Tests.** All eight heroes hold a Sovereignty affinity ceiling, so a manual with SOV-C is open to a hero by its ledger. SOV-CW is met by a hero only where the hero's own Sovereignty type is the weapon-aligned force (Varys, Swords; Hercules, Strength). That is why SOV-CW is never the default: the Azorion Signature katana manuals that Valia holds (Sovereignty, Healing) must stay open to her.

### 6.6 — The Per-Grade Defaults

**Rule 42.6.6.1 — The Defaults.** A worker fills the four cells by this table, by grade and band. A cell may rise above the default by one code on the author's word and may never fall below it. Where a cell shows two options, the worker uses the first unless the manual's `tradition` gives a reason for the second.

| Grade and band | `energy_req` | `cultivation_req` | `affinity_req` | `sovereignty_req` |
|---|---|---|---|---|
| BAS, M1 | NONE | NONE, or T1-<stage> up to T1-BONE | NONE | NONE |
| BAS, M2 | QI-MIN | CIRC | NONE | NONE |
| INT, M2 | QI-LOW | CIRC+LINK-PRIOR+LINK-STEP, or CIRC+LINK-PRIOR+LINK-GUARD | NONE | NONE |
| INT, M1 exception | NONE | T1-MARROW+LINK-PRIOR, or T1-SOUL+LINK-PRIOR | NONE | NONE |
| ADV, M2 | QI-MOD | MER-FULL+LINK-PRIOR+LINK-STEP, or MER-FULL+LINK-PRIOR+LINK-GUARD | A2 | NONE; SOV-C for at most one in three of the kingdom-specific manuals |
| ADV, XT | QI-MOD | XT-FIELD+LINK-PRIOR | A3 | NONE; SOV-C for at most one in three of the kingdom-specific manuals |
| ELI, XT | QI-HIGH | XT-FIELD+LINK-PRIOR+LINK-STEP+LINK-GUARD | A4 | SOV-C |
| ELI, M2 Monarch-gated | QI-HIGH | MER-NET+LINK-PRIOR+LINK-STEP+LINK-GUARD | A3 | SOV-C |
| SIG, M2 (min Warrior) | QI-MOD | MER-PART+LINK-PRIOR | A2 | NONE |
| SIG, M2 (min Champion or above) | QI-MOD | MER-FULL+LINK-PRIOR | A3 | SOV-C |
| SIG, XT | QI-HIGH | XT-FIELD+LINK-PRIOR+LINK-STEP | A4 | SOV-C |
| SIG, CF | QI-HIGH | CORE-ON+LINK-PRIOR+LINK-STEP | A5 | SOV-C |
| FUS, XT | QI-VHI | DUAL-STREAM+XT-FIELD+LINK-PRIOR | A4+A4 | NONE |
| FUS, CF | QI-VHI | DUAL-STREAM+CORE-ON+LINK-PRIOR | A4+A4 | SOV-C |
| CAT, XT | QI-EXT | XT-FIELD+LINK-PRIOR+LINK-STEP | A5 | SOV-C |
| CAT, CF | QI-EXT | CORE-ON+LINK-PRIOR+LINK-STEP | A6 | SOV-C |
| CAT, DV | QI-EXT | DIVINE+LINK-PRIOR | A7 | SOV-H |
| MYT, CF | QI-REAL | CORE-ON+LINK-PRIOR+LAW-INSIGHT | A6 | SOV-C |
| MYT, DV | QI-REAL | DIVINE+LINK-PRIOR+LAW-INSIGHT | A7 | SOV-H |

**Rule 42.6.6.2 — A Personal or Found Manual.** A personal or found manual follows the same table by its grade and band. Where the source is a mentor who gives the manual by Method L-1, the admission standard is a record of what the source asked, and the student may hold the manual below it (Rule 42.6.1.1); the cells still record the standard, and the kit records how the student came to hold it.

**Rule 42.6.6.3 — How "Not Below the Default" Is Read.** Check C-10 compares a cell with the default for its grade and band. Energy, affinity and sovereignty are compared by the order of their lists in this Area (Rules 42.6.2.1, 42.6.4.1 and 42.6.5.2). For cultivation, the state code is the default's or a later code in the list of Rule 42.6.3.2, and the link codes include every link code of the default (or of the alternative option the row shows). The affinity cap of Rule 42.6.4.2 still applies, so a cell may rise only as far as the band's cap.

---

## Area 7 — Acquisition Channels, Institutions and Copy Control

### 7.1 — The Channels

**Rule 42.7.1.1 — The Institutional Channels.** Manuals are generally available in libraries, colleges, academies, sects, large organizations, kingdoms and empires. The `channel` cell of a kingdom row (Rule 42.10.6.1) holds one of these codes, the primary channel through which a student reaches the manual there.

| Code | Channel | What it is |
|---|---|---|
| LIB | library | a public, civic, temple or private reading hall that keeps texts for readers |
| COL | college | a place of advanced study or of a craft or science (a college of artificers, a college of law) that teaches weapon styles as part of its craft |
| ACA | academy | a cultivation academy that enrols students and teaches by grade (the foundation, middle and apex academies of the kingdoms) |
| SECT | sect | a sect, clan, lineage or school that teaches its own members |
| ORG | large organization | an order, guild, concord, company, host, fleet or military body |
| KNG | kingdom | the crown's own archive, office or order, holding texts by royal authority |
| EMP | empire | an imperial archive or office; ledger use only (Rule 42.7.1.3) |

**Rule 42.7.1.2 — The Found and Personal Channels.** A manual may also come from a quest, a lost tomb or other mysterious place. These are not institutional stock. They are individual items (Rule 42.7.4.1), and the codes are used in the `source` cell of a personal manual and in the `source` cell of a kit row:

| Code | Channel |
|---|---|
| QST | a quest reward |
| TMB | a lost tomb |
| VLT | a hidden vault |
| RLC | a relic cache |
| MEN | a mentor's or master's own manual, given to one student |

An institutional code (LIB, COL, ACA, SECT, ORG, KNG, EMP) is also valid in a `source` cell, for a personal manual that an institution gave a person, for example an archive. A `source` cell is one code, or one code, a colon and a short plain phrase naming the role (`MEN:mentor of Varys`).

**Rule 42.7.1.3 — The Empire Code Is Ledger Use Only.** The `EMP` channel exists so that the ledger can record a manual that an imperial archive held. It never names or implies the Phase 1 forbidden entity in prose (Part 30 Law P30-L8), and no Phase 1 Area, spec or scene text carries an `EMP` source. The Olympus Archives of the Hercules and Bison seeds are ledger fields under the origin `Olympus` (Rule 42.10.4.1) and follow the rule of their ledgers.

### 7.2 — The Institutions

**Rule 42.7.2.1 — Institutions Are Already in the Ledgers.** The `institution` cell of a kingdom row names an institution that a ledger already holds, or reads `OPEN-AUTHOR` followed by a role word (for example `OPEN-AUTHOR library`). No worker coins a new institution, person, place or relic name. The author names institutions under Part 28 Area 20.4 (MAJOR entities), and an author-named institution is entered here only after the ledger holds it.

**Rule 42.7.2.2 — The Institutions the Ledgers Hold Today.** This list is a convenience copy of what the ledgers name, and the ledgers stand on any difference.

| Kingdom | Institution | Channel | Where it is held |
|---|---|---|---|
| Azure Sky | the Nine Halls (the umbrella institution over the three academies; sole authority over cultivation) | SECT or KNG | `ledger-people-society-faction/nine-halls.md` |
| Azure Sky | Sapphire Ascent Academy (primary foundation school) | ACA | `ledger-worlds-location/azure-sky-kingdom.md` §5 |
| Azure Sky | Lyraen Heights Academy (middle academy) | ACA | same |
| Azure Sky | Windward Reach Academy (apex academy) | ACA | same |
| Azure Sky | Azure Crafters' Concord (weapons, armor, dual-purpose combat implements) | ORG | `ledger-people-society-faction/azure-crafters-concord.md` |
| Azure Sky | the Skysworn (the cultivation-side order of the Azure Sky military) | ORG | `ledger-people-society-faction/azure-sky-military.md` |
| Azure Sky | the Azure Guard (the technology-side order) | ORG | same |
| Gale | Stormbreak Academy (foundation-tier) | ACA | `ledger-people-society-faction/gale-kingdom-state.md` |
| Gale | Aerie Academy (mid-tier) | ACA | same |
| Gale | Long Coast Academy (apex-tier) | ACA | same |
| Gale | the Oath-Voices (a lineage of wind-academy masters holding the oral Founding Oath chain) | SECT | `ledger-worlds-kingdom-state/gale-kingdom.md` |
| Gale | the Stormwing Order, the Windward Host, the Long Coast Fleet, the Wind-Sworn Militia (the four bodies of the Gale military) | ORG | `ledger-people-society-faction/gale-kingdom-military.md` |
| Gale | Aerie Artificers' College | COL | `ledger-worlds-kingdom-state/gale-kingdom.md` |
| Gale | Long Coast Shipwrights' Order | ORG | `ledger-worlds-kingdom-state/gale-kingdom.md` |

The author's brief for this Part named the Nine Halls umbrella over three academies, Sapphire Ascent Academy and the Azure Crafters' Concord for Azure Sky, and the wind academies (unnamed) and the Oath-Voices for Gale. The Gale ledgers now name three academies (Stormbreak, Aerie and Long Coast), and the table above uses them. Whether the Nine Halls contain, are spread across or sit beside the three Azure Sky academies is unestablished in the ledger, so a manual at the umbrella level names the Nine Halls and a manual at one academy names that academy (open for the author).

**Rule 42.7.2.3 — Where Each Grade Sits, by Default.** The default institution type by grade is a guide for workers and never a gate:

| Grade | Usual channels |
|---|---|
| Basic | LIB, ACA (the foundation academies), SECT |
| Intermediate | ACA (foundation and middle), COL, LIB, SECT |
| Advanced | ACA (middle and apex), ORG, SECT |
| Elite | ORG (the military orders), ACA (apex), KNG |
| Signature | ACA (apex), KNG, SECT, ORG |
| Fusion, Catastrophic, Mythic | KNG, SECT, a found channel; no institutional stock yet |

**Rule 42.7.2.4 — The Register Shows in the Name.** A kingdom manual of origin Azorion or Gale takes its title and its moves in that kingdom's register (Rule 42.12.3.1). Its institution is one of that kingdom's institutions.

### 7.3 — Access, Copy Control and Rarity

**Rule 42.7.3.1 — Access Codes.** The `access` cell of a kingdom row says who may read the manual at the institution:

| Code | Who may read it |
|---|---|
| OPEN | anyone who can reach the institution (a public hall) |
| ENROLLED | a student enrolled at the academy or college may borrow or read the institution's copy (this describes the institution's copy, not who may learn the move; anyone can learn, 2026-10-07) |
| MEMBER | a member of the sect, order or organization |
| RANKED | a member who holds the rank or standing the institution sets |
| PERMIT | a person with a written permit from the institution's head or from the crown |
| SEALED | no one with standing access; opened only by the holder's own order or a key |

**Rule 42.7.3.2 — Copy-Control Codes.** The `copy_control` cell says what may be done with the text:

| Code | What it means |
|---|---|
| FREE | copying is allowed and common; copies circulate |
| LENDING | a copy may be borrowed and must be returned; the institution lends under its rules |
| RESTRICTED | read in the hall only; no removal; copying only by the institution |
| SEALED | kept sealed; neither read nor copied without the holder's own authority |

**Rule 42.7.3.3 — Rarity.** Rarity is a plain five-step word that the story may use. It is derived and not stored: it follows the grade and the copy control, and an author override is written in the row's `local_note` as `rarity=<word>`.

| Grade | Default rarity | Usual access (who may borrow or read the institution's copy, not who may learn the move; anyone can learn, 2026-10-07) | Usual copy control |
|---|---|---|---|
| Basic | COMMON | OPEN or ENROLLED | FREE |
| Intermediate | COMMON | ENROLLED or OPEN | FREE or LENDING |
| Advanced | UNCOMMON | ENROLLED or MEMBER | LENDING |
| Elite | SCARCE | MEMBER or RANKED | RESTRICTED |
| Signature | RARE | RANKED or PERMIT | RESTRICTED |
| Fusion, Catastrophic, Mythic | UNIQUE | SEALED or PERMIT | SEALED |

The rarity words are COMMON, UNCOMMON, SCARCE, RARE and UNIQUE. A manual reached by a found channel is UNIQUE by default (Rule 42.7.4.1).

**Rule 42.7.3.4 — A Common Manual Appears in Both Kingdoms.** A Common manual has a row for Azorion and a row for Gale (Rule 42.10.6.2). The two rows may carry different institutions, channels, access and copy control, because the same text is kept differently in each kingdom. The manual itself is one row with one ID.

### 7.4 — Found Manuals

**Rule 42.7.4.1 — A Found Manual Is an Individual Item.** A manual that comes from a quest, a lost tomb, a hidden vault or a relic cache is not stock. It is one thing, found once, with one holder. It is entered as an individual manual: in the holder's `personal/<char>-manuals.csv` with `owner` and `source` set (Rule 42.10.7.1), or, when no holder is yet known, in a `found/` file pair that this Part reserves (Rule 42.10.7.4). Its rarity is UNIQUE.

**Rule 42.7.4.2 — Access Is Not a Question for a Found Manual.** A found manual has no institution, no access code and no copy control. Whoever holds it holds it, and what that holder can do with it is Area 3. If a holder copies it, the copy is not a new row: the copying is a story fact and the author decides whether it is ledgered.

**Rule 42.7.4.3 — A Found Manual Does Not Enter a Kingdom Stock.** A manual enters a kingdom's institutional stock only by an Area that shows an institution taking it in, and only on the author's word. Then it is given a kingdom row of its own (Rule 42.10.6.3).

### 7.5 — Access Is Not Eligibility

**Rule 42.7.5.1 — Two Different Questions.** Access (this Area) asks whether the institution lets a person read the text. Eligibility (Area 11) asks whether the person meets the admission standard (`min_realm` and the four requirements) and has access. A person may be eligible and have no access (a Common manual in a sealed vault), or have access and not be eligible (a public library copy of an Advanced manual read by a Senior). Neither is the Area 3 state of a move.

**Rule 42.7.5.2 — Access Codes Govern Institutional Stock Only (anyone can learn, 2026-10-07).** The access codes govern INSTITUTIONAL STOCK only (the kingdom's, an academy's, a sect's or a company's holdings). They are never a limit on who may learn, practise or train. Anyone can learn from any manual by any route (Part 6 Area 7.1 L-1, L-2, L-3, a found manual, a teacher of any kind, practice). A person with no institution simply reads other stock or learns by other routes.

---

## Area 8 — Learning and Mastery with Manuals

### 8.1 — The Learning Method

**Rule 42.8.1.1 — Manual Study Is Method L-2.** Learning from a manual of this ledger is Part 6 Area 7.1 Method L-2 (Manual Study): slower than Direct Transmission, with errors of interpretation, because the student reads the principle from text or encoding without the teacher's living guidance. A student of a manual typically begins at Novice.

**Rule 42.8.1.2 — A Teacher With the Manual Is Method L-1.** When a living teacher who holds the manual teaches the student from it, with demonstration and correction, the learning is Direct Transmission (Method L-1), and the manual is the teacher's text. The kit records `learned_via` as `L-1` (Rule 42.11.2.2). A teacher's authority to teach a School Move is the institution's (Rule 42.4.1.2).

**Rule 42.8.1.3 — One Weapon Type Per Manual.** A manual teaches the style of its one `weapon_id` (Rule 42.1.1.4). A move needs the weapon of that type, or the tool the style names, in hand. A character who holds a manual of a weapon the character does not wield holds it, and the moves are not performed until the weapon is in hand. That is a scene condition and is never a ledger state (Rule 42.3.3.4).

**Rule 42.8.1.4 — A Personal Signature Is Not Learned From a Manual.** Part 6 Method L-4 (Experiential Discovery) is the source of a personal Signature. No manual teaches one (Rule 42.4.2.1).

**Rule 42.8.1.5 — Theft and Copying.** A stolen manual, or a manual copied against its copy control, is learned by Method L-2 and the thief starts at Novice (Part 6 Rule 7.4.2). The theft itself is a Part 24 operation (Part 6 Rule 7.4.3). A School Move held by a thief is still the school's: using it where the school can recognize it exposes the thief (Part 6 Rule 7.4.4).

### 8.2 — Mastery

**Rule 42.8.2.1 — The Grade of the Manual Does Not Skip Mastery.** A manual's grade says what kind of moves it holds. It does not raise the reader's mastery. A reader of a Mythic manual who can use none of its moves has no mastery in any of them, and a reader of a Basic manual starts at Novice in each move.

**Rule 42.8.2.2 — Novice Is the Start.** A move that a character can use (Usable, or Conditional with its condition met) begins at Novice mastery (Part 6 Area 2.1), whether the manual was studied alone, taught or inherited. A move that becomes Usable by a change of realm (Rule 42.3.1.3) begins at Novice from the moment it becomes Usable. A move that is Latent has no mastery grade, because knowing a form and a theory is not practice.

**Rule 42.8.2.3 — Where Mastery Is Recorded.** The kit row records one `mastery` grade for the manual as a whole, the grade the character holds across its Usable moves, and a departure for one move is written in the row's `note` as `<move_id>=<Grade>` (Rule 42.11.2.2). The grades are Part 6's: Novice, Practiced, Adept, Proficient, Expert, Master. The mastery of a hero's moves in an Area is the hero's own ledger's fact once an Area shows it.

**Rule 42.8.2.4 — Type Rates Still Rule.** The success rates of a move are those of its Type and the mastery grade (Part 6 Area 2), and a Basic move is at 100% from Novice. Reading a manual changes no rate. Part 6 Rule 5.4.3 still holds: a higher mastery lowers energy cost for the same output.

**Rule 42.8.2.5 — Mastery Is Earned in the Story.** How long mastery takes and when a character steps from one grade to the next is the spec chain's and the character's arc, never a table here (Rule 42.1.3.1). Part 6 Rule 4.2.1 holds: a realm does not guarantee the realm's ceiling in practice.

### 8.3 — What a Manual Does Not Give

**Rule 42.8.3.1 — No Power, No Realm, No Breakthrough.** A manual gives no realm, no reserve, no affinity, no soul and no breakthrough. It gives names, forms and principles for one weapon type. Realm and power come from Part 3, and a move's output scales with the user's Heavenly Scale Grade and not with the manual's grade (Part 3 Area 16.3).

**Rule 42.8.3.2 — A Move Does Not Exceed Its Weapon.** A move of a manual that uses a technology weapon of Part 33 (Area 9) is bounded by that weapon's tier and by the user's own output (Rule 42.9.4.4).

---

## Area 9 — The Weapon-Type Registry and the Part 33 Relation

### 9.1 — What a Weapon Type Is

**Rule 42.9.1.1 — A Weapon Type Is a Style Discipline.** A weapon type is the family of forms, grips, distances, tempo and handling that a manual teaches for one kind of weapon. It has a three-letter `weapon_id` that names the files of its manuals (Rule 42.10.1.2). A weapon type is not a weapon: it is the discipline a weapon is used by.

**Rule 42.9.1.2 — The List Is Closed at 79.** The registry holds 79 weapon types. A new type, a rename or a removed type is a Canon Amendment on the author's word, with a new row in `weapons.csv` and the files of Area 10. A worker never adds a type.

**Rule 42.9.1.3 — `weapons.csv` Is the Owner of the Counts.** `weapons.csv` holds, for each type, its code, family, name, a one-line description, its prominence and the manual counts. This Area states the rule that fills the counts, and `weapons.csv` states the result.

### 9.2 — The Registry

**Rule 42.9.2.1 — The 79 Types.** (P is Prominent, S is Standard, N is Niche. The descriptions are in `weapons.csv`.)

| Family | Weapon types (code, name, prominence) |
|---|---|
| Bladed swords (11) | STS Straight sword (P); GRS Greatsword (P); SAB Saber (P); KAT Katana (P); RAP Rapier (S); SHS Short sword (P); SCI Scimitar (S); FAL Falchion (S); JIA Jian (P); DAO Dao (P); EST Estoc (S) |
| Knives and short blades (7) | DAG Dagger (P); KNF Knife (P); STI Stiletto (N); KUK Kukri (N); MAC Machete (N); SIC Sickle (N); SAI Sai (N) |
| Axes (5) | HAX Hand axe (S); BAX Battle axe (P); GAX Greataxe (P); TOM Tomahawk (N); WPK War pick (N) |
| Polearms (9) | SPR Spear (P); PIK Pike (N); LAN Lance (N); HAL Halberd (P); GLV Glaive (S); NAG Naginata (S); TRI Trident (N); GUA Guandao (S); JAV Javelin (N) |
| Blunt and hafted (9) | CLB Club (S); MCE Mace (P); WHM Warhammer (P); MAU Maul (N); MST Morning star (N); QST Quarterstaff (P); BOS Bo staff (S); TON Tonfa (N); BAT Baton (N) |
| Flexible and chained (9) | FLA Flail (N); WHP Whip (S); CHW Chain whip (N); NUN Nunchaku (N); KUS Kusarigama (N); MET Meteor hammer (N); RPD Rope dart (N); BOL Bolas (N); NET Net (N) |
| Ranged and thrown (9) | BOW Bow (P); CRB Crossbow (P); SLG Sling (N); TKN Throwing knife (N); SHU Shuriken (N); CHK Chakram (N); BMR Boomerang (N); BLW Blowgun (N); ATL Atlatl (N) |
| Firearms and gunpowder (6) | PST Pistol (S); MUS Musket (S); RIF Rifle (S); SHG Shotgun (N); CAN Cannon (N); GRN Grenade (S) |
| Siege and heavy (4) | CTP Catapult (N); TRB Trebuchet (N); BAL Ballista (N); RAM Battering ram (N) |
| Unarmed and close aids (5) | HTH Hand to hand combat (P); KND Knuckle-duster (N); CLW Claws (N); GAU Gauntlet (N); GAR Garrote (N) |
| Defensive weapons (2) | SHD Shield (P); BUC Buckler (S) |
| Exotic and special (3) | FAN War fan (S); HKS Hook swords (S); BFS Butterfly swords (S) |

There are 20 Prominent, 19 Standard and 40 Niche types.

### 9.3 — The Counts

**Rule 42.9.3.1 — The Counts per Kingdom.** For each weapon type and each kingdom, the author wants at least 10 to 12 Basic, 8 to 10 Intermediate, 7 to 9 Advanced, 6 to 8 Elite and 6 Signature manuals. The prominence class of a weapon sets the figure inside those ranges:

| Class | Basic | Intermediate | Advanced (per kingdom) | Elite (per kingdom) | Signature (per kingdom) |
|---|---|---|---|---|---|
| Prominent | 12 | 10 | 9 | 8 | 6 |
| Standard | 11 | 9 | 8 | 7 | 6 |
| Niche | 10 | 8 | 7 | 6 | 6 |

**Rule 42.9.3.2 — What Is Common and What Is Kingdom-Specific.** Basic, Intermediate and 50% of Advanced (rounded up) are Common: one manual that appears in both kingdoms' stocks. The rest of Advanced, all of Elite and all of Signature are kingdom-specific, Azorion or Gale. So for a weapon, `adv_common_n` is half of `adv_n` rounded up and `adv_kingdom_n` is `adv_n` less `adv_common_n`, per kingdom. The columns of `weapons.csv` are `basic_n`, `inter_n`, `adv_n` (Advanced per kingdom, Common included), `adv_common_n`, `adv_kingdom_n`, `elite_n` and `sig_n` (both per kingdom).

**Rule 42.9.3.3 — The Number of Generic Manuals.** For one weapon the generic manual rows are: `basic_n` Basic, `inter_n` Intermediate, `adv_common_n` plus 2 times `adv_kingdom_n` Advanced, 2 times `elite_n` Elite and 2 times `sig_n` Signature. The whole registry therefore holds 4,442 generic manuals (a Prominent weapon holds 63, a Standard 58 and a Niche 52). (Canon Amendment 2026-10-08): Brackenhold-origin manuals (Rule 42.10.2.6) are extras on top of these counts; the `weapons.csv` columns do not change, and check C-3 adds the Brackenhold-origin rows of that grade and weapon to the expected count. The Fusion, Catastrophic and Mythic generic folders exist and hold a header row only, because the author's kingdom stocks stop at Signature. Catastrophic manuals exist today only as personal manuals.

### 9.4 — The Relation to Part 33

**Rule 42.9.4.1 — Two Laws, Two Questions.** Part 33 governs what a technology weapon is: its mechanism, tier, scale class, power and the Tier 3 Handling Sheet. Part 42 governs the style discipline taught for the weapon type. A manual teaches how to use, aim, drill, crew or qi-assist a weapon type, within what Part 33 allows the weapon to do. Part 33 Area 18.2 (item 4) already says that cultivation techniques which resemble weapons are Part 6 Named Moves and not Part 33 weapons. The moves of a manual are such Named Moves.

**Rule 42.9.4.2 — Hand Weapons Have No Part 33 Class.** Part 33's taxonomy begins at the Shard-Thrower. The hand-held weapons of the first nine families (blades, knives, axes, polearms, blunt, flexible, unarmed aids, defensive weapons, exotic) are ordinary arms and have no Part 33 sub-type. A hero ledger's field "Primary Weapon Classification (Part 33)" that reads Swords or Blades names a family of the registry (Rule 42.9.4.7), and Part 42 is the finer record. A particular named blade is a named item (Part 28 Rule 20.8) and, when the author makes it a weapon with an entry, a `ledger-technology-weapon` entry (Threshold O-2).

**Rule 42.9.4.3 — The Part 33 Class of Each Missile, Powder and Siege Type.**

| Part 42 weapon types | Part 33 class and tier |
|---|---|
| BOW, SLG, TKN, SHU, CHK, BMR, BLW, JAV | Kinetic Strike, Shard-Thrower (Tier 1): stone, bone or metal propelled by muscle power; slings and bows |
| ATL, CRB, CTP, TRB, BAL | Kinetic Strike, Iron-Lance (Tier 2): crossbow bolt, arrow, early trebuchet stone, spear-thrower |
| PST, MUS, RIF, SHG, CAN | Kinetic Strike, Powder-Shot (Tier 3): gunpowder-propelled solid or fragmenting round |
| GRN | Detonation Burst, Thunder-Charge (Tier 3): gunpowder explosive, grenade |
| RAM | a crew tool and not a projectile weapon: no Part 33 sub-type |
| every other type | hand weapon: no Part 33 sub-type (Rule 42.9.4.2) |

The Bola and the Net are thrown hand weapons of the Flexible family and are read as hand weapons.

**Rule 42.9.4.4 — The Phase 1 Ceiling Is Tier 3.** In Phase 1 no style moves a weapon beyond Tier 3. A manual of a powder weapon or siege engine teaches handling, aim, drill, crew work and qi-assisted use within Part 33's Tier 3 Handling Sheet (Area 2.9), and a move delivers either (a) the weapon's own effect, bounded by the Handling Sheet's range, rate, carry, failure and outcome columns, or (b) the user's own qi through the weapon, bounded by the user's realm output and the move's Type (Part 3 Area 16.3, Part 6 Area 5.4.5). A move never claims a weapon effect above the Handling Sheet. The Handling Sheet rows are the Musket, the Rifle, the Field gun (the Cannon type), the Grenade and the two Mines. The Pistol and the Shotgun have no Handling Sheet row, so a move for either states no range, rate or carry figure, and the missing rows are an open item for the author. Siege engines of Tier 2 (Iron-Lance) have no sheet row either and are written without figures beyond Part 14 Area 5.3.

**Rule 42.9.4.5 — The Technology Gate by Kingdom.** A civilization cannot distribute weapons it cannot construct (Part 33 Area 3.3). Azure Sky is at Technology Tier 3 active, with black-powder muskets, rifles, field guns, grenades and mines in its military profile. Gale is at Tier 2 (upper end), with firearms issued to infantry absent and a few muskets and black-powder cannon on larger cutters imported from Azure Sky (`ledger-worlds-kingdom-state/gale-kingdom.md`). So a Gale-origin manual of a Firearms-family type (PST, MUS, RIF, SHG, CAN, GRN) teaches the handling of an imported or ship-mounted piece and the countering of fire, and never a drilled infantry volley as if Gale issued the weapon. Its `local_note` says so. The author's counts for those six types stand for both kingdoms, and the Gale stock of them is an open item for the author (Area 15, open questions).

**Rule 42.9.4.6 — Qi-Assisted Use.** A cultivator may use a technology weapon alongside cultivation techniques (Part 33 Area 3.2, WU-I-C; Area 6.3). A manual's qi-assisted move is a Named Move whose Type and cost class are Part 6's and whose weapon effect stays inside Rule 42.9.4.4. Part 33 Area 6 governs how cultivation defense meets a weapon.

**Rule 42.9.4.7 — The Hero Weapon Field.** The `primary_weapons` cell of `characters.csv` (Rule 42.11.1.2) lists weapon IDs, and for a hero it is read from the hero's field "Primary Weapon Classification": Swords reads the Bladed swords family; Blades reads the Bladed swords family and the Knives and short blades family; the specific type the hero's seed manual teaches is picked by the drafter and marked DERIVED for the author to override (Rule 42.11.3.2).

---

## Area 10 — The Manual Ledger

### 10.1 — The Folder and Its Files

**Rule 42.10.1.1 — One Folder, Many CSV Files, One Index.** The Manual Ledger is the folder `.claude/story-memory/ledger-manuals/` (the twenty-second ledger folder; Area 15, Amendment 5 gives the Part 37 text). It holds one Markdown file, `_index.md` (the design record and folder map, which carries the canonical headers and points here), one Markdown file of rules, `eligibility-rules.md`, and CSV files keyed by one ID scheme. The ledger is queried by ID like a database (Rule 42.1.3.2). The shortened folder name `ledger-manuals/` is the author's, like `ledger-named-moves/` (Part 37 Area 4).

```
ledger-manuals/
  _index.md                       the design record, the folder map, the canonical headers
  weapons.csv                     the 79 weapon types, their codes and manual counts
  manuals/<grade>/<WPN>.csv       generic manual definitions, one file per grade per weapon
  moves/<grade>/<WPN>.csv         the moves of those manuals, same split
  kingdoms/azorion.csv            Azorion kingdom IDs -> generic manual IDs, institution, channel, access
  kingdoms/gale.csv               Gale kingdom IDs -> generic manual IDs, institution, channel, access
  kingdoms/brackenhold.csv        Brackenhold kingdom IDs -> generic manual IDs (Canon Amendment 2026-10-08)
  personal/<char>-manuals.csv     a person's own manuals (mentor, master, archive, found), one pair per individual
  personal/<char>-moves.csv       the moves of those manuals
  found/                          RESERVED for found manuals with no holder yet (Rule 42.10.7.4)
  characters.csv                  realm snapshot, seal, weapons for every linked character
  character-kits.csv              which manual each linked character holds, from which source
  eligibility-rules.md            the eligibility rule for Tier C and Tier D characters
```

**Rule 42.10.1.2 — An ID Names Its Own File.** `<grade>` is one of `basic, intermediate, advanced, elite, signature, fusion, catastrophic, mythic`. `<WPN>` is the three-letter code in `weapons.csv`. `<char>` is the lowercase three-letter character code (`vrs`, `vla`, `aer`, `aal`, `hrc`, `bsn`, `vry`, `aeg` and the codes of `characters.csv`). So `MAN-ADV-STS-005` is in `manuals/advanced/STS.csv`, its moves `MV-ADV-STS-005-07` are in `moves/advanced/STS.csv`, `AZ-ADV-STS-005` is in `kingdoms/azorion.csv`, and `PER-VRS-01` is in `personal/vrs-manuals.csv` with its moves `PER-VRS-01-07` in `personal/vrs-moves.csv`. A reader that has an ID opens one file.

**Rule 42.10.1.3 — The File Format.** Every CSV is UTF-8 without a byte-order mark, comma separated, header row first, one record per line. A cell that contains a comma is wrapped in double quotes, and a double quote inside a cell is doubled. No cell holds a line break or a tab. Cells hold plain text: no bold, italic, backtick or other mark-up (Rule 42.12.1.2), and no em dash, except the one in the Area form of the `first_area` cell, which copies the named-move register's form. A file ends with one line break and no blank line.

**Rule 42.10.1.4 — The Header-Only Folders.** The `fusion`, `catastrophic` and `mythic` folders of `manuals/` and `moves/` hold, for each weapon, a file with the header row only, because the author's kingdom stocks stop at Signature (Rule 42.9.3.3). A Catastrophic manual exists today only as a personal manual. A generic Fusion, Catastrophic or Mythic row is added only on the author's word, in the number order of Rule 42.10.2.3.

### 10.2 — The ID Schemes

**Rule 42.10.2.1 — The IDs.**

| Thing | ID | Example |
|---|---|---|
| Generic manual | `MAN-{GRD}-{WPN}-{NNN}` | `MAN-ADV-STS-005` |
| Move of a generic manual | `MV-{GRD}-{WPN}-{NNN}-{SS}` | `MV-ADV-STS-005-07` |
| Azorion kingdom manual row | `AZ-{GRD}-{WPN}-{NNN}` | `AZ-ADV-STS-005` |
| Gale kingdom manual row | `GA-{GRD}-{WPN}-{NNN}` | `GA-ADV-STS-005` |
| Brackenhold kingdom manual row (Canon Amendment 2026-10-08) | `BR-{GRD}-{WPN}-{NNN}` | `BR-SIG-HAL-013` |
| Personal manual | `PER-{CHR}-{NN}` | `PER-VRS-01` |
| Move of a personal manual | `PER-{CHR}-{NN}-{SS}` | `PER-VRS-01-07` |
| Found manual (reserved) | `FND-{NNN}` | `FND-001` |
| Move of a found manual (reserved) | `FND-{NNN}-{SS}` | `FND-001-04` |

**Rule 42.10.2.2 — The Parts of an ID.** `{GRD}` is `BAS INT ADV ELI SIG FUS CAT MYT`. `{WPN}` is the three-letter weapon code of Rule 42.9.2.1. `{NNN}` is three digits, `{NN}` two and `{SS}` two (`01` upward in the manual's order, Rule 42.2.2.4). `{CHR}` is a three-letter character code: VRS Varys, VLA Valia, AER Aeries, AAL Aalia, HRC Hercules, BSN Bison, VRY Varya, AEG Aegon. A side character gets a three-letter code in `characters.csv` (Rule 42.11.1.2) that no other character has and that does not read as any code above.

**Rule 42.10.2.3 — `{NNN}` Inside One Grade and Weapon.** Numbers run Common first, then Azorion, then Gale, with no gaps:
- **Basic and Intermediate:** all Common, `001` upward (`basic_n` and `inter_n` of them).
- **Advanced:** Common `001` to `adv_common_n`; then the Azorion ones (`adv_kingdom_n` of them); then the Gale ones (`adv_kingdom_n` of them).
- **Elite:** Azorion `001` to `elite_n`; Gale `elite_n + 1` to `2 x elite_n`.
- **Signature:** Azorion `001` to `006`; Gale `007` to `012`. Inside each kingdom's six: the first four are Mortal Tier 2, the fifth Xiantian, the sixth Core (Rule 42.5.2.2).
- **Brackenhold (Canon Amendment 2026-10-08):** Brackenhold-origin manuals take the numbers after the last Gale number of their grade and weapon, in the order they are added (Rule 42.10.2.6). Today, for the halberd (`HAL`): Intermediate `011` and `012`; Advanced `014`; Signature `013`.

**Rule 42.10.2.4 — Kingdom IDs Point, They Do Not Define.** A kingdom ID (`AZ-`, `GA-` or `BR-`) has the same `{GRD}`, `{WPN}` and `{NNN}` as the generic row it points at, and it adds no manual. A Common manual has an Azorion row and a Gale row; an Azorion manual has an Azorion row; a Gale manual has a Gale row; a Brackenhold manual has a Brackenhold row (Rule 42.10.6.2).

**Rule 42.10.2.5 — IDs Are Permanent.** An ID is never reused, renumbered or changed. A manual that is revised or replaced becomes `Superseded` and its successor takes a new ID (Rule 42.12.7.1). A personal manual `{NN}` is numbered `01` upward for that character in the order the manuals are added.

**Rule 42.10.2.6 — Brackenhold in the Register (Canon Amendment 2026-10-08).** On the author's word of 2026-10-08, Brackenhold joins Azure Sky and Gale in the register, with these and only these changes: (a) the origin `Brackenhold` and the kingdom ID prefix `BR-` exist; (b) the file `kingdoms/brackenhold.csv` exists, with the kingdom header of Rule 42.10.3.1; (c) a Brackenhold-origin manual is a generic `MAN-` row, numbered as an extra after the Gale numbers (Rule 42.10.2.3), up to the Signature grade (no Fusion, Catastrophic or Mythic row), and has one `BR-` row; (d) a Common manual may also carry a `BR-` row, and its absence is not a finding (Rule 42.10.6.2); (e) the `kingdom` cell of a Brackenhold kingdom row reads `Brackenhold`, and the `kingdom` column of `characters.csv` may read `Brackenhold`; (f) the register of a Brackenhold manual is the neutral register until the author supplies one (Rule 42.12.3.1); (g) the Brackenhold Signature manuals are not bound to the Azorion and Gale layout (Rule 42.5.2.4), and Brackenhold rows are counted in check C-3 as extras to `weapons.csv`; (h) the institution cell reads `OPEN-AUTHOR` and a role word until the ledgers hold the institution (Rule 42.7.2.1). Elite and Advanced moves of a Brackenhold manual stay latent for a Warrior and are not shown (Rule 42.13.1.3). Nothing else in this Part changes.

### 10.3 — The Canonical Header Lines

**Rule 42.10.3.1 — The Headers.** These are the canonical header lines, copied by `_index.md`. A header never changes except by Canon Amendment (Rule 42.1.3.6), and check C-1 reads each line exactly.

`weapons.csv`:
```
weapon_id,family,name,description,prominence,basic_n,inter_n,adv_n,adv_common_n,adv_kingdom_n,elite_n,sig_n
```
`manuals/<grade>/<WPN>.csv` (generic manuals):
```
manual_id,grade,weapon_id,origin,title,realm_band,min_realm,energy_req,cultivation_req,affinity_req,sovereignty_req,move_count,composition,tradition,summary,status,first_area,notes
```
`moves/<grade>/<WPN>.csv` (moves of generic manuals) and `personal/<char>-moves.csv` (moves of personal manuals):
```
move_id,manual_id,seq,name,move_type,function,form,cost_class,unlock_realm,description,status,first_area
```
`kingdoms/azorion.csv`, `kingdoms/gale.csv` and `kingdoms/brackenhold.csv`:
```
kingdom_id,manual_id,kingdom,institution,channel,access,copy_control,local_note,status
```
`personal/<char>-manuals.csv` (the manuals header with `owner,source` added before `status`):
```
manual_id,grade,weapon_id,origin,title,realm_band,min_realm,energy_req,cultivation_req,affinity_req,sovereignty_req,move_count,composition,tradition,summary,owner,source,status,first_area,notes
```
`characters.csv`:
```
char_id,name,ledger_file,tier,kingdom,realm,effective_realm,blocked_types,affinity,sovereignty,primary_weapons,snapshot_date
```
`character-kits.csv`:
```
char_id,manual_id,kingdom_manual_id,source,learned_via,mastery,assign_status,note
```
The reserved `found/` files, when created, use the personal manuals header and the moves header.

### 10.4 — The Manual Columns

**Rule 42.10.4.1 — The Columns of a Manual Row.**

| Column | What it holds |
|---|---|
| `manual_id` | the ID of Rule 42.10.2.1 |
| `grade` | `BAS INT ADV ELI SIG FUS CAT MYT` |
| `weapon_id` | a code of `weapons.csv`; the same as the `{WPN}` of the ID and of the file |
| `origin` | `Common`, `Azorion`, `Gale`, `Brackenhold`, `Personal` or `Olympus` (and `Found` for the reserved found files). `Azorion` is the author's label for the Azure Sky tradition (Azorion is that kingdom's capital); the kingdom cell of a kingdom row reads `Azure Sky` (Rule 42.10.6.1). `Olympus` is a ledger-only origin (Rule 42.13.1.4) |
| `title` | the manual's title as plain text, unique across the ledger (Rule 42.12.1.1) |
| `realm_band` | `M1 M2 XT CF DV` (Rule 42.5.1.1) |
| `min_realm` | an exact Part 3 position in the form of Rule 42.5.3.2 |
| `energy_req` | a code of Rule 42.6.2.1 |
| `cultivation_req` | a state code and optional link codes of Rule 42.6.3 |
| `affinity_req` | a code of Rule 42.6.4.1 |
| `sovereignty_req` | a code of Rule 42.6.5.2 |
| `move_count` | an integer, 5 to 15, equal to the number of its move rows |
| `composition` | the cell of the table in Rule 42.2.3.2 for its grade and `move_count` |
| `tradition` | a plain tag of one to five words naming the school of practice, in the register of the origin (Rule 42.12.3.1); Common uses the neutral register |
| `summary` | one sentence, 10 to 30 words, saying what the manual teaches and to whom, with no lore beyond what the ledgers hold |
| `owner` (personal only) | the `char_id` of the one individual the manual is tied to |
| `source` (personal only) | a channel code of Rule 42.7.1.2, or the code, a colon and a short plain phrase |
| `status` | `Active`, `Dormant`, `Lost` or `Superseded` (Rule 42.10.4.2) |
| `first_area` | `Not yet established` until an Area writes the title, then `Area NN — Title (Ref: P.S.N.CCC.AA)` (the form of the named-move register) |
| `notes` | plain text for the ledger: `OPEN-AUTHOR` items, `DERIVED` marks, an author override; empty when none |

**Rule 42.10.4.2 — The Status Values.** `Active`: the manual exists and a copy is held somewhere or is known. `Dormant`: it exists and no one now holds or reads a copy. `Lost`: no copy is known. `Superseded`: a revised or replacing manual has taken its place, under its own ID. The values and their reading follow the named-move register (Part 37 Area 3.9).

**Rule 42.10.4.3 — Baseline and Living.** `manual_id`, `grade`, `weapon_id`, `origin`, `title`, the realm, requirement, count, composition, tradition and summary cells are Baseline (B). `status`, `first_area` and `notes` are Living (L) (Part 37 Area 5).

### 10.5 — The Move Columns

**Rule 42.10.5.1 — The Columns of a Move Row.**

| Column | What it holds |
|---|---|
| `move_id` | the ID of Rule 42.10.2.1; its prefix is the `manual_id` and its suffix is `seq` |
| `manual_id` | the manual that carries the move |
| `seq` | `01` upward, lowest type first (Rule 42.2.2.4) |
| `name` | the move's name as plain text, unique across the ledger (Rule 42.12.2.2) and, for every name made on or after 2026-10-08, in the form of the move-naming law (Rule 42.12.2.3) |
| `move_type` | `Basic`, `Intermediate`, `Advanced`, `Elite`, `Signature`, `Fusion`, `Catastrophic` or `Mythic` |
| `function` | a Part 6 Area 3 function (Rule 42.10.5.2) |
| `form` | `INSTANT`, `CHANNELED` or `CAST` (Rule 42.10.5.5) |
| `cost_class` | a cost class (Rule 42.10.5.4) |
| `unlock_realm` | the unlock realm of the type, the exact string of Rule 42.3.3.2 |
| `description` | one sentence, 8 to 24 words, naming the physical action and what it does, with no invented lore; a Fusion move begins `streams: X + Y;` (Rule 42.2.3.4) |
| `status` | `Active`, `Dormant`, `Lost` or `Superseded`; the move's own, which follows its manual unless an Area says otherwise |
| `first_area` | `Not yet established` until an Area writes the name, then the Area in the form of Rule 42.10.4.1 |

**Rule 42.10.5.2 — The `function` Cell.** `function` is one primary function written `Category:Sub`, optionally followed by `|` and one secondary function in the same form (Part 6 Area 3.1: a move may have a primary function and secondary functions). The categories and subs are Part 6 Area 3's:

| Category | Subs |
|---|---|
| Attack | Strike, Projectile, Area, Penetrating, TrueDamage, Suppression |
| Defense | Shield, Deflect, Absorb, Reflect, Nullify |
| Mobility | Step, Flash, Phase |
| Control | Bind, Seal, Suppress, Disrupt, Confuse |
| Trap | Trap, Formation, Contaminate |
| Support | Heal, Empower, Sense |
| Combination | Sequence, Convergence |

A soul function takes the prefix `Soul-` on the category (Part 6 Area 3.8), for example `Soul-Attack:Penetrating`.

**Rule 42.10.5.3 — Weapon-Style Guards on Function.** A weapon style teaches physical-layer movements. So: Absorb (specific to the Void Root), Flash, Phase, TrueDamage, Heal and every `Soul-` function appear only in moves of type Elite or above, and never in a Common manual; Convergence appears only in a Fusion-type move; Formation and Trap appear only in moves of type Advanced or above. An area-effect move (Attack:Area, Control, Trap) obeys Part 6 Rule 3.10.1 and carries no radius figure in the ledger.

**Rule 42.10.5.4 — The Cost Class.** `cost_class` is a Part 6 Area 5.3 class: `STAMINA`, `MINIMAL`, `LOW`, `MODERATE`, `HIGH`, `VARIABLE`, `VERY-HIGH`, `EXTREME`, `REALITY`. `STAMINA` is the physical cost of a Mortal Tier 1 move with no qi (Part 6 Rule 5.1) and appears only in a Basic move of an M1 manual, or in a Basic move that uses no qi. The default by type, which a worker may move by one step inside the range Part 6 states:

| Move type | Default | Allowed range (Part 6 Area 2.2) |
|---|---|---|
| Basic | MINIMAL | STAMINA, MINIMAL, LOW |
| Intermediate | LOW | LOW, MODERATE |
| Advanced | MODERATE | MODERATE, HIGH |
| Elite | HIGH | HIGH |
| Signature | VARIABLE | VARIABLE |
| Fusion | VERY-HIGH | VERY-HIGH |
| Catastrophic | EXTREME | EXTREME |
| Mythic | REALITY | REALITY |

**Rule 42.10.5.5 — The Form.** `form` is a Part 6 Area 5.2 deployment form. Part 6 Area 5.3 gives some types no cost for a form, and such a move may not take that form: Basic and Intermediate are INSTANT or CHANNELED (no cast accumulation); Advanced, Elite, Signature and Fusion may take any of the three; Catastrophic and Mythic are INSTANT or CAST (no channeled cost).

**Rule 42.10.5.6 — Baseline and Living.** `move_id`, `manual_id`, `seq`, `name`, `move_type`, `function`, `form`, `cost_class`, `unlock_realm` and `description` are Baseline (B). `status` and `first_area` are Living (L).

### 10.6 — The Kingdom Rows

**Rule 42.10.6.1 — The Columns of a Kingdom Row.**

| Column | What it holds |
|---|---|
| `kingdom_id` | `AZ-{GRD}-{WPN}-{NNN}`, `GA-{GRD}-{WPN}-{NNN}` or `BR-{GRD}-{WPN}-{NNN}` |
| `manual_id` | the generic manual the row points at |
| `kingdom` | `Azure Sky` for a row of `azorion.csv`, `Gale` for a row of `gale.csv`, `Brackenhold` for a row of `brackenhold.csv` |
| `institution` | an institution the ledgers hold (Rule 42.7.2.2) or `OPEN-AUTHOR` and a role word |
| `channel` | an institutional channel code of Rule 42.7.1.1 |
| `access` | an access code of Rule 42.7.3.1 |
| `copy_control` | a copy-control code of Rule 42.7.3.2 |
| `local_note` | plain text on how this kingdom keeps the manual; `rarity=<word>` for an author override; the technology note of Rule 42.9.4.5 where it applies |
| `status` | `Active`, `Dormant`, `Lost` or `Superseded`, for this kingdom's copy |

**Rule 42.10.6.2 — Which Rows Exist.** A Common manual has two rows (`AZ-` and `GA-`). An Azorion manual has one row in `azorion.csv`. A Gale manual has one row in `gale.csv`. A Brackenhold manual has one row in `brackenhold.csv`, and a Common manual may also have one there. A kingdom row never points at a manual of the other kingdom's origin.

**Rule 42.10.6.3 — A Later Row.** A found or personal manual that an institution later takes in gets a kingdom row only on the author's word (Rule 42.7.4.3). Its `kingdom_id` is built from the manual it points at, so the manual must have a generic ID: a found manual that enters stock is added as a generic row first.

### 10.7 — Personal and Found Manuals

**Rule 42.10.7.1 — One Personal File Pair per Individual.** A personal manual is tied to ONE individual (`owner`). The individual's manuals are in `personal/<char>-manuals.csv`, and the moves of those manuals in `personal/<char>-moves.csv`. The origin of a personal manual is `Personal`, or `Olympus` where the author sets that origin. Personal manuals have no kingdom row, because they are not stock.

**Rule 42.10.7.2 — What Makes a Manual Personal.** A manual is personal when it is one text tied to one person: a mentor's or master's own manual given to one student (`MEN`), a text from an archive that one person was given or took, a found manual that one person holds. A personal manual follows the grade, composition, band and requirement rules of this Part like any other.

**Rule 42.10.7.3 — The Personal Move Rows.** The moves of a personal manual are written like any other (Rule 42.10.5.1) with IDs `PER-{CHR}-{NN}-{SS}`. Their Signature-type and Catastrophic-type moves are the source's lineage moves, not the owner's personal Signature (Rule 42.4.2.2).

**Rule 42.10.7.4 — The Found Folder Is Reserved.** `found/` is reserved for found manuals that have no holder yet. It is created when the author first writes a found manual, with two files (`found/found-manuals.csv` and `found/found-moves.csv`), the personal manuals header and the moves header, and IDs `FND-{NNN}` and `FND-{NNN}-{SS}`. Until then no `found/` file exists.

### 10.8 — The Ledger Checks

**Rule 42.10.8.1 — The Checks.** The `validate` command (Rule 42.10.9.1) runs these checks over every file. A FAIL is a defect to correct; INFO is reported and does not fail.

| Check | What it reads | Result |
|---|---|---|
| C-1 Headers | the first line of every CSV equals its canonical line (Rule 42.10.3.1) | FAIL |
| C-2 IDs | every ID matches its pattern; each is unique across the ledger; each is in the file its code names (Rule 42.10.1.2); a kingdom ID has the same `{GRD}-{WPN}-{NNN}` as its manual | FAIL |
| C-3 Row counts | for each weapon, the rows of `manuals/<grade>/<WPN>.csv` equal the counts of `weapons.csv` (BAS `basic_n`; INT `inter_n`; ADV `adv_common_n` + 2 x `adv_kingdom_n`; ELI 2 x `elite_n`; SIG 2 x `sig_n`; FUS, CAT, MYT none), plus the Brackenhold-origin rows of that grade and weapon (Rule 42.10.2.6) | FAIL |
| C-4 Numbering | `{NNN}` is contiguous from `001`; the origins run Common, then Azorion, then Gale, then Brackenhold as Rule 42.10.2.3 sets; Signature `001` to `006` is Azorion and `007` to `012` is Gale | FAIL |
| C-5 Kingdom rows | a Common manual has an `AZ-` and a `GA-` row, an Azorion manual an `AZ-` row, a Gale manual a `GA-` row, a Brackenhold manual a `BR-` row (a Common manual's `BR-` row is optional); `kingdom` matches the file; the channel, access and copy-control codes are valid | FAIL |
| C-6 Composition | `move_count` is 5 to 15 and equals the number of move rows; `composition` equals the table cell of Rule 42.2.3.2 for (`grade`, `move_count`); the counts of each `move_type` in the move rows equal the composition | FAIL |
| C-7 Move-count range | `move_count` is inside the range of Rule 42.2.2.2 for the grade; a personal Catastrophic manual has 14 or 15; a Signature manual (library or personal) has 10 to 12 | FAIL |
| C-8 Move rows | `seq` runs `01` to `move_count` with no gap; `move_id` is the `manual_id`, a hyphen and `seq`; moves run lowest type first; every `move_type` is one the grade's composition lists | FAIL |
| C-9 Realm | `realm_band` is valid; `min_realm` has the form of Rule 42.5.3.2; its band equals `realm_band`; it is inside the window of Rule 42.5.3.3; it is not below the unlock of the lowest move (Rule 42.5.3.4) | FAIL |
| C-10 Requirements | every requirement cell is a code of its ladder; each is not below the default of Rule 42.6.6.1 (Rule 42.6.6.3); the affinity code does not pass the band's cap (Rule 42.6.4.2); an M1 manual has NONE in energy, affinity and sovereignty; `W` and SOV-CW appear only in a sword, hook-sword, butterfly-sword or unarmed-family manual; SOV-H and SOV-O stand only where Rule 42.6.5.2 allows | FAIL |
| C-11 Distribution | per weapon: Basic is about half M1 and half M2; at most one Intermediate M1 manual; each of M2 and XT holds at least one third of its Advanced manuals; at most one Monarch-gated Elite per kingdom; per kingdom the six Signature manuals are four M2, one XT, one CF, with the four M2 `min_realm` values non-decreasing and none above `Ruler L1 Mid` (Rules 42.5.2.1 and 42.5.2.2); Brackenhold rows are not read (Rule 42.5.2.4) | FAIL |
| C-12 Move fields | `function` has the form of Rule 42.10.5.2 and obeys Rule 42.10.5.3; `form` obeys Rule 42.10.5.5; `cost_class` is inside the range of Rule 42.10.5.4; `unlock_realm` equals the string for the `move_type` in Rule 42.3.3.2; a Fusion move's description begins `streams:` | FAIL |
| C-13 Names | every move `name` and every manual `title` is unique after the comparison form is taken (lowercase, punctuation removed, spaces collapsed), across every file including personal and found files; no `name` equals a `title`; no `name` or `title` equals an institution of Rule 42.7.2.2 | FAIL |
| C-14 Plain text | no cell holds `*`, a backtick, an underscore used as mark-up, a tab, a line break, or an em dash outside the `first_area` cell | FAIL |
| C-15 References | every `weapon_id` is in `weapons.csv` and equals the `{WPN}` of the ID; every `manual_id` in a move, kingdom or kit row exists; every manual has at least one move row; no orphan row | FAIL |
| C-16 Status and first area | `status` is one of the four values; `first_area` is `Not yet established` or the Area form | FAIL |
| C-17 Institutions | `institution` is in the list of Rule 42.7.2.2 or begins `OPEN-AUTHOR` | FAIL |
| C-18 Personal | a personal ID is `PER-{CHR}-{NN}` with `{CHR}` equal to the `owner` code; `owner` is in `characters.csv`; `source` has a valid code; `origin` is `Personal` or `Olympus` | FAIL |
| C-19 Characters | `char_id` is unique; the realm cells have the form of Rule 42.5.3.2; `blocked_types` is `none` or grade codes; `primary_weapons` codes exist; `ledger_file` exists; `snapshot_date` is a date | FAIL |
| C-20 Kits | `char_id` and `manual_id` exist; a `kingdom_manual_id`, when present, exists and points at the same `manual_id`; `learned_via` is `L-1` or `L-2`; `mastery` is a Part 6 grade; `assign_status` is `ASKED` or `DERIVED`; no Varya or Aegon kit row exists, and no Tier C or Tier D kit row exists unless its `assign_status` is `ASKED` | FAIL |
| C-21 Kit coherence | a kit manual's `weapon_id` is in the character's `primary_weapons` | INFO |
| C-22 Registered rows | where `first_area` is not the default, `ledger-named-moves` and `ledger-named-items` hold the row for it (Rule 42.12.5.1) | INFO |

### 10.9 — The Query Tool

**Rule 42.10.9.1 — `manual_ledger_query.py`.** One authorized script reads the Manual Ledger: `.claude/tools/manual_ledger_query.py`, the fifth authorized script (`guardrails/tools/guardrail-authorized-scripts-only.md`). It is read-only. It never writes, creates or changes any file. Its commands:

| Command | What it returns |
|---|---|
| `manual ID` | the manual row of a generic, kingdom or personal ID, with its kingdom rows (or, from a kingdom ID, the generic row it points at) and the count of its move rows |
| `moves ID` | the move rows of a manual ID, in order, or the one row of a move ID |
| `kit CHARACTER` | the kit rows of a character (by `char_id`), each with its manual title, grade and band |
| `usable CHARACTER` | for each manual in the character's kit and each of its moves, the state Usable, Conditional or Latent, computed by Rule 42.3.3.1 from the character's `effective_realm` and `blocked_types`, with the access group and the cell used, and the condition code for a Conditional move; and, as information, whether the character meets the manual's admission standard (Rule 42.11.6.1) |
| `validate` | runs checks C-1 to C-22 and returns each FAIL and INFO with the file and ID, exiting non-zero on any FAIL |

**Rule 42.10.9.2 — A Sixth Command Is Recommended.** The collision scan of Rule 42.12.6.1 asks whether a name already exists in the ledger. The five commands above read by ID, so a name has no lookup. This Part recommends a sixth read-only command, `name TEXT`, returning every move name and manual title that equals or closely matches the text, in the comparison form of check C-13. It is a recommendation to the author and the tool builder, and the five commands stand without it (Area 15, open questions).

**Rule 42.10.9.3 — Who Reads It.** The Pre-Write Ledger Check reads `kit` and `usable` for any character whose manual or moves the Area draws on, and `manual` or `moves` for any manual the Area names. Gate 1 and Gate 2 run `validate` after any Gate 2 write to the Manual Ledger. No agent searches the CSV text for a fact that an ID or a command returns.

### 10.10 — Writing, Rollback and Housekeeping

**Rule 42.10.10.1 — Who Writes What.** The stock is written once, under the author's directive of 2026-10-05, by the generation workers and the orchestrator. After that, the Post-Write Ledger Update (Gate 2) edits only: the `first_area`, `status` and `notes` cells of the rows an Area first wrote or changed; the `characters.csv` and `character-kits.csv` rows of a character whose ledger changed; and, on the author's word, new rows and the rename pass of Rule 42.12.2.3(g), which replaces a `name` cell and keeps the old name in the manual row's `notes`. A header, a code, a composition or a baseline cell changes only by Canon Amendment (Rule 42.1.3.6).

**Rule 42.10.10.2 — One Row at a Time, Then Validate.** A Gate 2 edit changes one row's cells, and `validate` is run after the pass.

**Rule 42.10.10.3 — Rollback.** When a written Area is archived or deleted (`/rewind-to`, `/redraft-area`, `/redraft-chapter`, `/restore-archive`, `/reset-chapter`, `/reset-phase`) or revised (`/revise-area`), the continuity-checker ledger pass restores `first_area` to `Not yet established` on the rows that Area first wrote, and removes the rows it added to `ledger-named-moves` and `ledger-named-items` for them, as Part 41 Rule 41.9.5.2 does for the calendar rows.

**Rule 42.10.10.4 — Resets.** The reset script (`tools/reset_story.py`, Step 5b, authorized by the author on 2026-10-05) restores every `first_area` cell of the CSV files under `manuals/`, `moves/` and `personal/` to `Not yet established` and touches nothing else in them; it deletes no file and does not read `kingdoms/`, `characters.csv` or `character-kits.csv`. `/reset-story`, `/reset-ledgers` and `/hard-reset` therefore restore those cells themselves, and the ledger pass of Rule 42.10.10.3 only verifies them.

**Rule 42.10.10.5 — No Size Limit.** No row count blocks an Area. The ledger holds about 4,442 generic manuals, their moves and the kingdom rows, and a query reads one file.

---

## Area 11 — Characters, Kits and Eligibility

### 11.1 — `characters.csv`

**Rule 42.11.1.1 — Who Has a Row.** `characters.csv` holds one row for every character linked to a manual: the eight heroes, and each Tier A and Tier B side character. A Tier C or Tier D character has a row only if an Area shows that character holding or using a manual (Rule 42.11.5.3).

**Rule 42.11.1.2 — The Columns.**

| Column | What it holds |
|---|---|
| `char_id` | the three-letter code (Rule 42.10.2.2) |
| `name` | the character's name, plain text |
| `ledger_file` | the path of the character's ledger entry from `story-memory/`, for example `ledger-character-hero/varys.md` |
| `tier` | `Hero`, `A`, `B`, `C` or `D` (Part 17 and Part 19 Depth Spectrum) |
| `kingdom` | `Azure Sky`, `Gale`, `Brackenhold` or `none` |
| `realm` | the character's true realm, an exact Part 3 position (Rule 42.5.3.2) |
| `effective_realm` | the realm the Manual Ledger reads (Rule 42.3.4.1); equal to `realm` when no seal applies |
| `blocked_types` | `none`, or grade codes joined by `;` (for example `SIG;CAT`) |
| `affinity` | each affinity as `<Type>:<ceiling level name>` joined by `;` (for example `Swords:Sovereignty`), the level being the ledger's ceiling in Part 4's exact level names, or `none` |
| `sovereignty` | `none`, `ceiling:<Type>`, `held:<Type>` or `origin:<Type>` (Rule 42.6.5.2) |
| `primary_weapons` | weapon IDs joined by `;`, or `none` (Rule 42.9.4.7) |
| `snapshot_date` | the real date (`YYYY-MM-DD`) on which the row was last synchronized with the ledger |

**Rule 42.11.1.3 — A Mirror, Not an Owner.** The character's own ledger owns every value in the row (Part 37 Area 5, one owner for a fact held in two places). `characters.csv` mirrors realm, effective realm, seal, affinity, sovereignty and weapons so that `usable` can compute without opening a long ledger. On a difference the ledger stands and the row is corrected, as a finding at the next ALCA pass. Gate 2 updates the row, and its `snapshot_date`, whenever the ledger changes a realm, an effective realm, a seal, an affinity or a weapon.

**Rule 42.11.1.4 — The Hero Rows at the Phase 1 Start.** These are the values the hero ledgers hold today, for the pass that writes the file (the weapon cell is DERIVED and the drafter may pick the type):

| `char_id` | `realm` | `effective_realm` | `blocked_types` | `sovereignty` |
|---|---|---|---|---|
| VRS | `Ruler L3 Mid` | `Ruler L3 Mid` | none | `ceiling:Swords` |
| VLA | `Ruler L1 Mid` | `Ruler L1 Mid` | none | `ceiling:Healing` |
| AER | `Ruler L2 Mid` | `Ruler L2 Mid` | none | the ledger's own type |
| AAL | `Ruler L1 Mid` | `Ruler L1 Mid` | none | `ceiling:Space` |
| HRC | `Demigod L1 Mid` | `Champion L8 High` | `SIG;CAT` | `ceiling:Strength` |
| BSN | `Demigod L1 Mid` | `Champion L8 High` | `SIG;CAT` | the ledger's own type |
| VRY | `T1 Unawakened` | `T1 Unawakened` | none | `ceiling:Creation` |
| AEG | `T1 Unawakened` | `T1 Unawakened` | none | the ledger's own type |

### 11.2 — `character-kits.csv`

**Rule 42.11.2.1 — One Row per Character and Manual.** A kit row says that a character holds a manual. It is the Manual Kit that the character's ledger points at (Rule 42.11.4.2).

**Rule 42.11.2.2 — The Columns.**

| Column | What it holds |
|---|---|
| `char_id` | the character |
| `manual_id` | the manual held: a `MAN-` or a `PER-` ID |
| `kingdom_manual_id` | the `AZ-` or `GA-` ID through which the character reached it, or empty for a personal manual |
| `source` | a channel code of Rule 42.7.1.2 or Rule 42.7.1.1, or the code, a colon and a short plain phrase |
| `learned_via` | `L-1` (Direct Transmission, Rule 42.8.1.2) or `L-2` (Manual Study, Rule 42.8.1.1) |
| `mastery` | the manual-level mastery grade across the Usable moves: Novice, Practiced, Adept, Proficient, Expert or Master |
| `assign_status` | `ASKED` (the author chose it) or `DERIVED` (the drafter inferred it and the author has not reviewed it) |
| `note` | plain text joined by `;`: `COND:<code>` for each condition met (Rule 42.3.3.3); `<move_id>=<Grade>` for a move whose mastery differs from the row; any other plain note |

**Rule 42.11.2.3 — Which ID Goes Where.** `manual_id` is always the generic or personal manual. A character who reached a manual through an institution has the kingdom ID in `kingdom_manual_id`, so that the route is on record. A personal manual has no kingdom ID.

### 11.3 — The Hero Seeds

**Rule 42.11.3.1 — The Seeds.** These are the author's seeds. Each hero is linked by ID through `character-kits.csv`. The weapon types are picked by the drafter and marked DERIVED for the author to override (Rule 42.11.3.2).

| Hero | Personal manuals | Institutional manuals |
|---|---|---|
| Varys (VRS) | one personal Catastrophic manual of 15 moves, from his mentor (`PER-VRS-01`, source `MEN`) | four Azorion Signature manuals of the sword family (10 to 12 moves each) |
| Valia (VLA) | none | four Azorion Signature katana manuals (KAT) |
| Aeries (AER) | one personal Catastrophic manual of 14 moves, from his master (`PER-AER-01`, source `MEN`) | three Gale academy Signature greatsword manuals (GRS) |
| Aalia (AAL) | none | four Gale Signature manuals of the short-sword family; her teachers are the Gale academies and not the Azorion library |
| Hercules (HRC) | one personal Catastrophic manual of 15 moves from the Olympus Archives, Xiantian band (`PER-HRC-01`), and three personal Olympus Signature manuals (spear, a blade type, halberd: `PER-HRC-02` to `PER-HRC-04`) | none |
| Bison (BSN) | one personal Catastrophic manual of 14 moves from the Olympus Archives (`PER-BSN-01`), and three personal Olympus Signature manuals (dual-axe and warhammer styles: `PER-BSN-02` to `PER-BSN-04`) | none |
| Varya (VRY) and Aegon (AEG) | none | none (Rule 42.11.7.1) |

For Hercules and Bison every Signature and Catastrophic move is Latent under the seal (Rule 42.3.4.2). The Olympus origin stays in ledger fields and never reaches prose except as the Hercules and Bison ledgers allow (Rule 42.13.1.4).

**Rule 42.11.3.2 — DERIVED Picks.** The hero weapon types (the sword-family types for Varys, the short-sword-family types for Aalia, the blade type for Hercules, the axe types for Bison) are the drafter's inference from the hero ledgers' weapon fields (Rule 42.9.4.7) and are `DERIVED` in `assign_status`. The kit rows of the seeds are `DERIVED` unless the author sets them (`ASKED`).

**Rule 42.11.3.3 — Seeds Meet Their Own Rules.** Each seed must pass the ledger checks: a Signature manual of 10 to 12 moves, a personal Catastrophic manual of 14 or 15 moves, a Xiantian or Core band for the Catastrophic manuals (Rule 42.5.3.3), and a Signature manual with `min_realm` that a hero of Ruler Level 1 Mid or above meets, for the institutional ones.

### 11.4 — Tier A and Tier B Side Characters

**Rule 42.11.4.1 — Concrete Manual IDs, Marked DERIVED.** Each Tier A and Tier B side character gets concrete assigned manual IDs in `character-kits.csv`, chosen to fit the character's ledger (weapon, realm, kingdom, rank, institution and role), marked `DERIVED` for the author's review. The assigner does not go beyond what the character's ledger supports, and the institutional manuals assigned pass the eligibility test (Rule 42.11.6.1) unless the source is `MEN` or a found channel.

**Rule 42.11.4.2 — The Manual Kit Pointer in the Ledger.** A hero, villain or side-character ledger holds, in its Section 3, a Manual Kit pointer line that lists the character's manual IDs and points at the kit. It holds no move block for a manual-borne move (Rule 42.12.4.3). Amendment 4 of Area 15 gives the line.

**Rule 42.11.4.3 — Promotion.** When a Tier C or Tier D character is promoted to Tier A or Tier B (Part 19 Lifecycle), the promotion pass adds the character's `characters.csv` row and kit rows by Rule 42.11.4.1.

### 11.5 — Tier C and Tier D Side Characters

**Rule 42.11.5.1 — Eligibility Only, No Assignment.** A Tier C or Tier D character gets no individual manual assignment. The ledger records the eligibility rule (Rule 42.11.6.1) in `eligibility-rules.md`, and nothing else for them.

**Rule 42.11.5.2 — `eligibility-rules.md`.** The file states, for the people who write the scenes, the one rule: a Tier C or Tier D character may be shown with a manual only if the character is eligible for it, by realm at or above `min_realm`, energy, cultivation, affinity and sovereignty requirements met, access through the kingdom and institution, and the Part 6 learning rules. It restates Rule 42.11.6.1 in plain words and carries no list of characters.

**Rule 42.11.5.3 — When a Scene Shows One.** If a scene shows a Tier C or Tier D character with a manual, the manual is chosen from those the character is eligible for. The Area writes the names in it, and Gate 2 registers the moves by Rule 42.12.5.1. A kit row for such a character is added only if the author asks for it; the kit never lists a Tier C or Tier D character by default (check C-20).

### 11.6 — The Eligibility Test

**Rule 42.11.6.1 — The Test.** A character is eligible to be admitted to a manual by an institution when all of the following hold. The test is a reading of the ledger and of the character's own entry, and it is informational in `usable` (Rule 42.10.9.1):
1. **Realm.** The character's `effective_realm` is at or above the manual's `min_realm` in the Part 3 order (the institution sees the realm the character expresses).
2. **Energy.** The manual's `energy_req` is not above what the character's access group can bear (Rule 42.11.6.3).
3. **Cultivation.** The state code is met by the character's `effective_realm` (T1-<stage> by the Tier 1 stage; CIRC and MER-PART from Senior; MER-FULL from Champion; MER-NET at Monarch; XT-FIELD from Demigod; CORE-ON from Core Formation; DIVINE from Divine Transformation), and each link code is met: LINK-PRIOR, LINK-STEP and LINK-GUARD by the character's kit and Named Moves at Practiced or better; DUAL-STREAM and LAW-INSIGHT only where the character's own ledger records them.
4. **Affinity.** The affinity code's level is not above the lower of the character's ledger ceiling and the realm cap of Rule 42.6.4.2 (Rule 42.11.6.2), and for a `W` code the character holds the weapon-aligned affinity; for `A4+A4` the character holds two affinities that reach Level 4.
5. **Sovereignty.** SOV-C is met when the `sovereignty` cell is not `none`; SOV-CW when it is `ceiling:` the weapon-aligned force; SOV-H when it is `held:`; SOV-O when it is `origin:`.
6. **Access.** This item describes who may borrow or read the INSTITUTION'S copy, not who may learn the move (anyone can learn, 2026-10-07; Rule 42.7.5.2). To read the institution's copy the character can reach the institution (kingdom) and meets its `access` code: enrolment for ENROLLED, membership for MEMBER, rank for RANKED, a permit for PERMIT. A SEALED manual has no standing access. A person who fails this item may still learn the same moves by other routes.
7. **Learning.** The Part 6 Area 7 rules hold: the manual teaches by Method L-1 or L-2, the character starts at Novice, a personal Signature is not on offer (Rule 42.4.2.1), and the jurisdiction does not forbid the move (Part 6 Area 4.3).
8. **Not already held.** The character does not already hold the manual.

**Rule 42.11.6.2 — Reading the Affinity.** A recorded affinity level is a ceiling, and the current level follows the Part 4 milestones (Part 4 Area 1.4). The test reads the lower of the ledger's level and the realm cap: Level 1 in Mortal Tier 1; Level 3 in Mortal Tier 2; Level 5 at Xiantian; Level 6 at Core Formation or Core Assimilation; Level 8 at Core Solidification and in the Divine Realm.

**Rule 42.11.6.3 — The Highest Energy Code a Group Bears.** The highest `energy_req` code that an access group supports is the cost class of the highest type that group can use (a Standard or Possible cell), or, for the groups with only Rare cells, the cost class the condition makes available:

| Group | Highest energy code |
|---|---|
| AG1 | NONE |
| AG2 | QI-MOD |
| AG3 | QI-MOD |
| AG4 | QI-HIGH |
| AG5 | QI-EXT |
| AG6 | QI-EXT |
| AG7 | QI-REAL |
| AG8 | QI-REAL |
| AG9 | QI-REAL |

**Rule 42.11.6.4 — Eligible Does Not Mean Holds.** Passing the test says the character may be admitted. It records nothing and gives nothing. A character holds a manual only when a kit row says so. *Added 2026-10-19 (Part 45, Canon Amendment):* the link codes are eligibility prerequisites to hold a manual and never an ordering rule for a scene; no scene has to show a Basic move or an earlier manual before an Intermediate or higher move for a link code to count as met, and no move has to follow another by type (Part 45 Rule 45.1.1.1).

### 11.7 — Varya and Aegon

**Rule 42.11.7.1 — No Manuals, a Learning-Plan Pointer Only.** Varya and Aegon are eight years old, Mortal Tier 1 and Unawakened. They hold no manuals and have no kit rows. Their ledgers carry a learning-plan pointer only, saying that they will learn from the academies of their kingdom (the foundation academies of Rule 42.7.2.2) and that no manual ID is assigned. Amendment 4 of Area 15 gives the line. Any manual that either child comes to hold is added by an Area that shows it, by Rule 42.11.4.1.

### 11.8 — Keeping the Files Current

**Rule 42.11.8.1 — Gate 2 Keeps Them.** At Gate 2 the Post-Write Ledger Update updates `characters.csv` when a character's ledger changed a realm, an effective realm, a seal, an affinity, a sovereignty or a weapon, and `character-kits.csv` when an Area shows a character gaining or learning a manual, with the `mastery` and `note` cells as the Area shows. A new Tier A or Tier B side character (Part 19, C-38) gets a code and a row.

---

## Area 12 — Naming and Registration

### 12.1 — Manual Titles

**Rule 42.12.1.1 — A Title Is a Named Item.** A manual's title is a named item (Part 28 Rule 20.8.1): a made thing, a text that a character could hold, read or copy, which the story calls by a proper name of its own. It is set in plain italic in the Area text and in every spec file, the name only, at its first use and at every use after, and in roman inside a passage that is already italic (Part 28 Rule 20.8.2). The article is never part of the name: the text writes `the *Title*`, and `The *Title*` at the start of a sentence. A title is never bold-italic, because it is not a Named Move. Its Type in the named-item register is `other item` (Rule 42.12.4.4). A title is unique across the whole ledger (check C-13).

**Rule 42.12.1.2 — CSV Cells Are Plain.** The `title` and `name` cells of the CSV files hold plain text with no mark-up (Rule 42.10.1.3). The italic of a title and the bold-italic of a move name are added by the prose and the specs, never stored.

**Rule 42.12.1.3 — What a Title Is Made Of.** A title names the book. It does not contain a move's name, an institution's name, a person's name or a grade code or ID. A title may use the register of its origin (Rule 42.12.3.1). A Common title uses everyday words (a primer, a drill-book, a handbook, a treatise, a canon, a workbook) with the weapon or a plain quality of the style. A title may not equal a proper name from a widely known published work, and may not carry a contemporary-Earth anachronism.

**Rule 42.12.1.4 — Who Classes a Title MAJOR or MINOR.** The classification of a name as MAJOR or MINOR is Part 28 Rule 20.4's, and this Part adds none. The stock titles are written under the author's directive of 2026-10-05, and an author-set title is immutable (Part 28 Area 3.4 and Rule 20.4).

### 12.2 — Move Names

**Rule 42.12.2.1 — Bold-Italic, Always.** A manual-borne move is a Named Move and keeps its bold-italic form at every mention, inside dialogue and outside it, with no dialogue exception and no roman break (Part 2 Rule 3.2.1; Part 6 Rule 6.5.4). A move name that contains the name of an item takes the move's form and nothing nests (Part 28 Rule 20.8.2(e)).

**Rule 42.12.2.2 — Every Move Name Is Unique.** Every move name is unique across the whole Manual Ledger (every generic, personal and found file) and does not equal or closely echo any Named Move in `ledger-named-moves`, in a hero, villain, side-character or monster ledger, any manual title, any item in `ledger-named-items`, or any institution, person or place the ledgers hold (check C-13 reads the first two; Rule 42.12.6.1 reads the rest).

**Rule 42.12.2.3 — The Move-Naming Law (Canon Amendment 2026-10-08).** *Authority: the author's instruction in chat on 2026-10-08, after the Chapter 003 draft review. This rule replaces the earlier rule "The Patterns", whose last sentence read "A name is two to seven words".* A move name belongs to the move and never to the situation in which the move is called. It is tied to two things only: the weapon type, and the cultivation level and grade of the move. The law governs the name of every manual-borne move (stock, personal and found) and every new Named Move name that an Area, a spec or a ledger pass sets for a move used with a weapon. For a Named Move that has no weapon (a species-innate move, a soul move), parts (a), (c), (d) and (e) apply in the same way and part (b) is read through the move's own substrate and function.

(a) **Length.** A name is one word or two words. At most 5 percent of a manual's moves carry a three-word name, counted in whole moves and rounded down, so a manual of fewer than 20 moves holds none (this is the plain arithmetic of the author's wording, and no manual of the Basic to Signature grades reaches 20 moves). A Catastrophic or Mythic manual may use three words and is still mostly two: more than half of its names have one or two words. A Named Move that is not in a manual takes one or two words, or three if it is a Catastrophic or Mythic move. A name never runs to four words or more, and three or more is never the routine.

(b) **Tied to the weapon and to the level.** A name is specific to its weapon type: it names the grip, the edge, the reach, the tool or the motion that the type has, so that it could not stand for a move of another type. Up to Mortal Tier 2 Senior level (Mortal Tier 1 and Senior) a name is generic and weapon-based. From Mortal Tier 2 Warrior level upward a name is generic, weapon-anchored, cultivation-anchored, or a combination of these. `[DERIVED]` The level is read from the ledger by ID: for a manual-borne move it is the `min_realm` of its manual (Rule 42.5.3.1); for a move outside a manual it is the realm at which its type unlocks (Rule 42.3.3.2). A cultivation-anchored name carries the cultivation of its level in plain words and never a realm name that Part 3 Rule 1.7.3 keeps off the page (Rule 42.13.1.4).

(c) **Never the situation.** A name does not name a place, a setting, a tactic or an enemy. Invented illustrations of what this bars, which establish no name: a place ("Courtyard Thrust"), a setting ("Night March Cut"), a tactic ("Flank Break"), an enemy ("Bandit Breaker").

(d) **The name carries the impact, and the impact rises with the grade.** Basic and Intermediate names are simpler. Advanced and Elite names are more impactful. Signature and Fusion names are highly impactful. Catastrophic and Mythic names carry the highest impact.

(e) **The name fits the function.** A move may attack, heal, scout, defend, control, move its user or serve another function (Part 6 Area 3). The name fits that function and never deceives about it (Rule 42.12.2.4): a defence, a heal, a scouting move, a control move or a movement is not given an attack name.

(f) **Patterns, creator reference and registers.** The Part 6 Rule 6.2 patterns remain as ways to build a name and set no length (the Part 6 Area 6.2 note, Amendment 10 of Area 15). A name built on Creator Reference (Pattern 3) names no person that the ledgers do not hold (Rule 42.7.2.1) and keeps to the length of (a). The registers of Rule 42.12.3.1 stay the source of a name's words and images; a register word that names a place or a setting is not used as the place or setting of a move (c).

(g) **Replacing a name, and the one grandfathered name.** A stock name made before this amendment that does not meet this law stands until the author orders the rename pass, and `validate` does not fail it: no check reads length or situation, and `manual_ledger_query.py` is unchanged by this amendment. When a name is replaced, the old name is kept in the notes. A moves file has no `notes` cell (Rule 42.10.3.1), so the old name is written in the `notes` cell of the move's manual row as `renamed <move_id> from "<old name>" <YYYY-MM-DD>`; the new name passes check C-13 and the collision scan (Rule 42.12.6.1). A name already written in a confirmed Area is never replaced (Rule 42.12.7.1). The one name written in prose that does not meet this law is ***Open Guard Reading Cut*** (`PER-VRS-01-01`, Varys's personal move, written in Chapter 001, which is frozen); it is grandfathered, stays as written and sets no precedent.

(h) **Who reads it.** The Area Maker and the Outline Planner apply this law whenever they name or propose a move. Gate 1 Check #17(b) reads each new move name in a draft against it as the entity-type convention for moves, and a departure blocks like any naming departure. The Naming Checks cell of the register row records the check (Rule 42.12.5.1). A name that breaks the law is not made lawful by the register of its culture or by a spec.

**Rule 42.12.2.4 — What a Name May Not Be.** A name may not equal a proper name from a widely known published work, may not carry a contemporary-Earth anachronism, may not be a name that deceives about the move's function (Part 6 Area 6.2, Invalid Names), may not name a place, a setting, a tactic or an enemy (Rule 42.12.2.3(c)), and may not be so general that it names neither its weapon nor its motion. The generic, weapon-based names that Rule 42.12.2.3(b) asks for at the lower levels do name both, and a name like "Big Strike" names neither (Canon Amendment 2026-10-08).

### 12.3 — The Registers of Culture

**Rule 42.12.3.1 — The Three Registers.** The register of a manual follows its origin. Part 28 Rule 20.3 step 2 (the producing culture's register, from Part 25) is applied by the register below, and the check is recorded in the Naming Checks cell (Rule 42.12.5.1). **Author reading (2026-10-05):** the phrase "no walls" and its negations (for example "Unwalled", "Without a Wall") are the author's own Gale register and are allowed; only an affirmative wall, gate, bastion or fortress word (a Gale name that is a wall) stays banned.

| Origin | Register | What it draws on |
|---|---|---|
| Common | neutral | everyday words for the principle and the action: no kingdom vocabulary, no kingdom's pairing or wind imagery |
| Azorion | the Azure Sky register: dual-track, paired, twin-court, hawk and azure, basin and river | names that come in pairs or carry a twin, the two tracks of the kingdom, the court of two, the hawk and the azure sky, the basin and the river that runs through it |
| Gale | the Gale register: wind-sworn, plateau, oath, bearing, no walls | names built on the wind and on oaths sworn to it, the plateau and its edge, a bearing taken and held, and never a wall, a gate, a bastion or a fortress |
| Brackenhold (Canon Amendment 2026-10-08) | neutral, until the author supplies a Brackenhold register | everyday words, as for Common (Rule 42.10.2.6) |

**Rule 42.12.3.2 — The Author's Lists Are a Source, Not a Fence.** The registers are the author's own words to draw on. A worker does not extend them with an invented culture or invented lore, and does not use a word of one register in the manuals of the other kingdom. A personal manual takes the register of its source's culture where the ledgers set one, and the neutral register where they do not. An Olympus-origin manual takes the neutral register and names nothing of its origin (Rule 42.13.1.4).

### 12.4 — The Registers

**Rule 42.12.4.1 — The Manual Ledger Is the Register of Manual-Borne Moves.** Part 6 Rule 6.5.1 holds one generic register of every Named Move. For a move that a manual of this ledger carries, the register of record is the Manual Ledger, by the move's ID, in its CSV files, from the day the row exists (the move has a name, a Type and a Function). `ledger-named-moves/_index.md` carries a pointer block for the stock and not a row for each of its tens of thousands of moves (Rule 42.12.4.2). A manual-borne move becomes a full row of the generic register when its name is first written in prose (Rule 42.12.5.1).

**Rule 42.12.4.2 — The Pointer Block.** `ledger-named-moves/_index.md` carries one block, in this form, placed under its Purpose notes:

> **Manual-borne moves (Part 42).** The Named Moves that the manuals of `ledger-manuals/` carry are registered in that ledger by ID (`MV-…` and `PER-…`), in its CSV files, and are not listed row by row here. A manual-borne move becomes a full row of this register when its name is first written in prose, at the Gate 2 of that Area (Part 6 Rule 6.5.5), and its First Area Appearance is then also entered in its CSV row. The Pre-Write Ledger Check and the Part 6 Rule 6.2 collision scan read the Manual Ledger by ID and by name. Query: `manual_ledger_query.py`.

**Rule 42.12.4.3 — The User Holds a Pointer, Not a Block.** For a manual-borne move the user's character-ledger entry holds the Manual Kit pointer line (Rule 42.11.4.2) and no move block. The Manual Ledger row owns every value of the move (Part 6 Rule 6.5.6, one owner). The register row's Users cell points at the user's Manual Kit line, or, for a move no single person uses, at the institution's entry. A hero's own personal Signature keeps its move block in the hero's Section 3 as Part 6 Rule 6.5.2 says.

**Rule 42.12.4.4 — The Title Register.** A manual title is registered by its ID in the Manual Ledger, and a pointer row in `ledger-named-items/_index.md` is written when the title is first written in prose (Rule 42.12.5.1). The row's Type is `other item`, its Entity File is the CSV file that holds the manual and the `manual_id`, and it holds no value of the manual (Part 28 Rule 20.8.4; one owner).

### 12.5 — The Gate 2 Flow

**Rule 42.12.5.1 — When an Area First Writes a Manual-Borne Name.** The Area Maker takes every manual title and move name that the Area uses from the ledger by ID, and lists each in the hand-off. After `[CONFIRM WRITE]`, the Post-Write Ledger Update, in the same pass:
1. sets `first_area` in the move's CSV row to the Area (`Area NN — Title (Ref: P.S.N.CCC.AA)`), and in the manual's CSV row too if the title is first written;
2. adds a full row to `ledger-named-moves/_index.md`: Entity Name `***Name***`; Classification `Lineage or school technique`; First Area Appearance the Area; Entity File the move's CSV path and `move_id`; Status `Active`; Last Updated the date; Users a pointer to the user's Manual Kit line, or to the institution's entry; Naming Checks `manual ledger <move_id>; collision scan by ID and by name <date>; register <Common, Azorion or Gale>; move-naming law Rule 42.12.2.3 <date>` (the last clause is added by the Canon Amendment of 2026-10-08);
3. adds a pointer row to `ledger-named-items/_index.md` for a manual title first written (Rule 42.12.4.4);
4. updates `character-kits.csv` and `characters.csv` where the Area shows a character gaining a manual, a mastery grade or a realm change (Rule 42.11.8.1);
5. runs `validate` (Rule 42.10.10.2).

**Rule 42.12.5.2 — The Kind.** Every manual-borne move of every origin and every type is registered as `Lineage or school technique` (Part 6 Rule 6.5.3): the School Moves by Area 4, and the Basic to Elite moves because a manual is an institution's or a source's transmitted text. A hero's own personal Signature stays `Signature Named Move`.

**Rule 42.12.5.3 — A Name in a Spec Enters Nothing.** A manual title or move name that appears only in a spec or in a discarded draft enters no register and sets no `first_area` (Part 38 Rule 1.3.2). The stock rows exist already; what an Area adds is the Area.

**Rule 42.12.5.4 — The Area Does Not Add to the Stock.** An Area that needs a manual or a move that the ledger does not hold does not invent it into the stock. The need goes to the author, and a new personal or found manual is added by the author's word with a new ID (Rule 42.10.7.1). A new name for a hero's own move follows Part 6 Rule 6.5.5 and also passes the collision scan of the Manual Ledger (Rule 42.12.6.1) and the move-naming law (Rule 42.12.2.3).

### 12.6 — Collision Scan and Uniqueness

**Rule 42.12.6.1 — The Scan Reads the Manual Ledger.** The ledger scan of Part 6 Rule 6.2 and Part 28 Rule 20.3 step 1 now includes the Manual Ledger: a new name is compared with every move name and every manual title in it (by ID where the name is already there, and by name through the lookup of Rule 42.10.9.2 where it is new), and with the generic register, the character ledgers and the named-item register. A name that equals or closely echoes one is changed before it is used, never after.

**Rule 42.12.6.2 — What "Closely Echo" Means.** Two names closely echo when they differ only by a swapped, added or dropped small word, a changed number, a changed order of the same words, or a plural. The comparison form of check C-13 (lowercase, punctuation removed, spaces collapsed) is the first test, and a reader's judgment is the second.

**Rule 42.12.6.3 — Distinctiveness in a Scene.** Within one scene and one Chapter, the move names and the manual titles that appear are phonetically and visually distinct from one another (Part 6 Rule 6.2, check 5). A scene that draws several moves from one manual takes care that their names do not blur.

### 12.7 — Stability

**Rule 42.12.7.1 — Names Do Not Change.** A name in the ledger is immutable once written in prose (Part 28 Area 3.4; Part 6 Rule 6.4). A revised manual or a re-worked move is a new row with a new ID, and the old row becomes `Superseded`. The ledger renumbers nothing (Rule 42.10.2.5).

**Rule 42.12.7.2 — A Hero's Variant Is a New Move.** A hero's own variant of a School Move is a new Named Move under a new name (Part 6 Rule 6.4), registered under the hero as a personal move or Signature by Area 4.

---

## Area 13 — Narration Standards

**Rule 42.13.1.1 (N42-1) — The Forms.** A manual's title is plain italic at every mention (`the *Title*`). A move from a manual is bold-italic at every mention, inside dialogue and outside it. The name of the school or institution that holds a manual is roman, as any institution name is. Gate 1 Check #12 reads both forms and Check #17 reads the naming.

**Rule 42.13.1.2 (N42-2) — Ledger Words Stay Out of the Prose.** The prose never carries an ID, a grade code (BAS, INT, ADV, ELI, SIG, FUS, CAT, MYT), a band code (M1, M2, XT, CF, DV), a composition string, an access group, a requirement code, the words Usable, Conditional or Latent as ledger terms, a `min_realm` string in the ledger form, or a count of the moves in a manual as a figure the ledger sets. The prose says in plain words what the manual is, what it asks and what it holds.

**Rule 42.13.1.3 (N42-3) — A Latent Move Is Never Executed.** A character who holds a move that is Latent for that character does not execute it in prose (Part 3 Rule 16.2.1; the one use of Part 3 Area 16.6 and the one bounded case of Part 30 Law P30-L1 stand as written). The prose may show the character knowing it: the stance drilled slowly with no qi in it, the order of the movements spoken or drawn, the breath that does not yet catch. It never shows an effect, an output or a result of the move. A Latent move is felt as a distance to cover and not as a rule that a table sets. Whether a move is Latent is read from `usable CHARACTER` before the Area is drafted (Rule 42.10.9.3).

**Rule 42.13.1.4 (N42-4) — The Realm Vocabulary Stays Where Part 3 Puts It.** Part 3 Rule 1.7.3 and Law P30-L8 govern the words of the page: in Phase 1 prose set in the Sol Star System no character, monster or manual is named above Ruler Level 9 Low, and the forbidden realm names stay off the page unless one of the three exceptions of Rule 1.7.2 holds. A manual of a high band is shown by what it asks (a reserve no reader in the hall has, a state of body no student has reached) and by what its moves do, never by naming its band or its grade. The origin `Olympus` and the origin `EMP` are ledger fields. Hercules and Bison may speak or think the word Olympus and the Seal under the P30-L8 exception, as their ledgers say, and no Phase 1 text names the Empire of Gods or any other name for that origin, or labels a manual by that origin.

**Rule 42.13.1.5 (N42-5) — Learning Is Shown as Practice.** A student begins every move at Novice (Rule 42.8.2.2). The grade of a manual never lets a reader skip the work. Manual Study shows the slowness and the errors of reading a principle without a teacher: a misread diagram, a form held wrong for a season. A teacher who teaches from the manual shows correction and demonstration. No success rate, mastery grade or percentage is stated as a figure in prose (Part 6 Area 11).

**Rule 42.13.1.6 (N42-6) — Weapon Realism.** A style for a powder weapon or a siege engine keeps to the Part 33 Tier 3 Handling Sheet in what it shows: the reload, the smoke and flash, the sound, the carried rounds, the failure (Part 33 Rule 33.7.3, N33-1 to N33-5). A qi-assisted move shows the user's own output through the weapon, and never a weapon effect above Tier 3 in Phase 1 (Rule 42.9.4.4).

**Rule 42.13.1.7 (N42-7) — School and Self Stay Apart.** A School Move taught to many is never described as one person's own Signature, and a hero's personal Signature is never described as written in a manual (Rule 42.4.2.1). A school that codifies a founder's form gives it a new name, and the prose gives the new name (Rule 42.4.2.3).

**Rule 42.13.1.8 (N42-8) — The Manual as an Object.** A manual is an ordinary object in the medium the ledger names or implies (a bound book, a scroll, a carved tablet, a jade slip, a recorded formation). Its copy control shows in how it is kept and read: a restricted text is read in the hall and does not leave it, a lending text is signed for and returned, a sealed text needs a key or an authority. A manual is not a relic unless Part 12 registers it as one. A found manual is one thing, found once, and its finding is a scene and not a transaction.

**Rule 42.13.1.9 (N42-9) — The Ledger's Names, Exactly.** An Area uses the ledger's names for titles, moves and institutions exactly as written, and invents no manual, move, institution or title that the ledger does not hold (Rule 42.12.5.4). The Latent and Usable condition of a character's moves, and the character's mastery, are shown through the body and its results and never through a label.

---

## Area 14 — Boundaries and Cross-Part Table

### 14.1 — Boundaries

**Rule 42.14.1.1 — Part 6 Stands on Moves and Access.** Part 42 classifies no move and sets no access. Every move row obeys Part 6's Type, Function, cost class and form. The Access Table is read, never changed (Rule 42.1.3.4).

**Rule 42.14.1.2 — Part 33 Stands on Technology Weapons.** Part 42 sets no weapon tier, scale class or handling figure. It reads Part 33's, and a style never carries a weapon beyond them (Rule 42.9.4.4).

**Rule 42.14.1.3 — Part 37 Owns the Schema System.** The Manual Ledger's layout is stated here, and its registry entry, template and threshold are Part 37's, written by Amendment 5. Until Part 37 carries them, this Part states them and Part 37 stands on any difference about the schema system.

**Rule 42.14.1.4 — One Script.** The only script this Part names is the read-only query tool (Rule 42.10.9.1). No other script is created for the Manual Ledger. A change to a script is raised to the author first.

**Rule 42.14.1.5 — No Hero Ledger Is Edited Here.** This Part edits no hero, villain or side-character ledger. The Manual Kit pointer and the learning-plan pointer are applied by the amendment pass on the author's permission (Area 15, Amendment 4).

**Rule 42.14.1.6 — Specs Establish No Manual Fact.** A manual, a move, a title or a kit named in a spec is a proposal (Part 38 Rule 1.3.2). A fact is established by the Manual Ledger and, for `first_area`, by the Area that is confirmed and written.

**Rule 42.14.1.7 — No Pace, No Resolution of Open Lore.** The Manual Ledger sets no pace for the story (Rule 42.1.3.1) and resolves no open lore: an institution not yet named stays `OPEN-AUTHOR`, and the Nine Halls question stays open.

### 14.2 — The Cross-Part Dependency Master Table

| Dependency Row | Relationship | Governance Rule |
|----------------|--------------|-----------------|
| Gate audit (FCIA/ALCA) | Audit governance | The audit law in guardrails/audit/guardrail-audit-gate-law.md governs Area content produced under this Part. Gate 1 Check #12 reads the forms of Area 12 and Area 13; Check #17 reads the naming; Gate 2 writes the registers of Rule 42.12.5.1; ALCA reads the Manual Ledger against the generic register and the kits against the character ledgers (Areas 10 to 12). |
| Canon-Part 2 | Part 42 → Part 2 | The bold-italic form of a Named Move (Rule 3.2.1) and the Area file structure stay Part 2's. Titles are plain italic named items (Rules 42.12.1.1, 42.12.2.1). |
| Canon-Part 3 | Part 42 → Part 3 | The ladder, the reserves, the Move Access Ceiling (Area 16.2), the Depletion States, Rule 16.2.1 and Rule 1.7.3 stay Part 3's. The energy and cultivation ladders are grounded in Areas 1, 12, 13 and 16 (Areas 3, 6). |
| Canon-Part 4 | Part 42 → Part 4 | The nine Affinity Levels, the realm milestones and the 50-type catalog stay Part 4's. The affinity and sovereignty ladders use the exact level names (Area 6). |
| Canon-Part 6 | Part 42 ↔ Part 6 | The Access Table, Types, Functions, cost classes, mastery, naming patterns (their length and what a name may name are limited by the move-naming law, Rule 42.12.2.3) and learning methods stay Part 6's and are read, not changed. Part 42 states the scope of Area 9.1 identity binding, the extension of Rule 6.5.1 and the pointers of Area 7.1, and Area 15 gives the exact texts. |
| Canon-Part 7 | Part 42 → Part 7 | A Fusion-type move in a manual meets the Fusion Move Protocol (Part 6 Area 10) and the Part 7 success rates; the `streams:` rule (Rule 42.2.3.4). |
| Canon-Part 12 | Part 42 → Part 12 | A manual is not a relic unless registered as one; a Part 12 relic entry is separate from the manual row (Rule 42.1.1.3). |
| Canon-Parts 17, 18, 19 | Part 42 ↔ Parts 17, 18, 19 | Section 3 of each character ledger carries the Manual Kit pointer line and no move block for a manual-borne move (Amendment 4). The tier of a side character (Part 19 Depth Spectrum) sets whether it has a kit (Area 11). |
| Canon-Parts 22, 23 | Part 42 → Parts 22, 23 | The institutions, their ranks and their transmission rules (Lineage Techniques, affiliation) stay Parts 22 and 23's. The `institution` cell names only what their ledgers hold (Rule 42.7.2.1). |
| Canon-Part 25 | Part 42 → Part 25 | The cultural registers of the two kingdoms come from Part 25; the Azorion and Gale registers are the author's lists (Rule 42.12.3.1). |
| Canon-Part 28 | Part 42 ↔ Part 28 | The Rule 20.3 naming method, the Rule 20.8 named-item form and register, name immutability and the MAJOR and MINOR split stay Part 28's. Manual titles are `other item` named items with a pointer row (Amendment 6). |
| Canon-Part 29 | Part 42 → Part 29 | Realm vocabulary in narration and dialogue follows Part 29 Area 12 and Rule 29.2.1.1d with Part 3 Rule 1.7.3 (Rule 42.13.1.4). |
| Canon-Part 30 | Part 42 → Part 30 | Law P30-L8 (the forbidden entity), Law P30-L1 (the one bounded Catastrophic use), the Phase 1 narrative ceiling and the seal end-states stay Part 30's (Rules 42.3.4.3, 42.13.1.3, 42.13.1.4). |
| Canon-Part 33 | Part 42 ↔ Part 33 | The technology weapon taxonomy, tiers and the Tier 3 Handling Sheet stay Part 33's. A weapon type is a style discipline, and a style never carries a weapon beyond Tier 3 in Phase 1 (Area 9; Amendment 7). |
| Canon-Part 37 | Part 42 → Part 37 | The ledger folder registry, the schema template, the creation threshold and the B/L classification (Area 10; Amendment 5). |
| Canon-Part 38 | Part 42 → Part 38 | A spec establishes no manual fact (Rule 42.14.1.6). |
| Canon-Part 39 | Part 42 → Part 39 | A character's relation to a weapon style may be a behavioral signature of its own (Part 39 owns it); Part 42 records the manuals only. |
| Canon-Part 40 | Part 42 → Part 40 | A monster's innate moves are S-3 species-innate moves (Part 6 Area 12) and are not in manuals (Part 6 Area 12.7, S-3 non-transmission). |
| Canon-Part 41 | Part 42 → Part 41 | `first_area` and the Area form of Rule 42.10.4.1 read the Area reference; no date is stored in the Manual Ledger. |

---

## Area 15 — Amendments Part 42 Requires of Other Parts

This Area lists the exact texts that Part 42 requires another Part to carry. Another agent applies them. Each amendment says what is replaced or inserted, and where. None is applied by this Part.

### 15.1 — The Amendments

**Amendment 1 — Part 6 Area 9.1: the scope of identity binding (purpose kept).**

(a) Insert, after the last paragraph of Area 9.1, a new rule:

> **Rule 9.1.1 — Scope of identity binding (Part 42).** Identity binding applies to a personal Signature: a Signature move that one cultivator developed through Experiential Discovery (Method L-4) and that is registered under that cultivator's `Signature Named Moves`. A personal Signature cannot be learned from observation (Method L-3) or from a transmission manual (Method L-2), and a copy is Advanced at best. A Signature, Fusion, Catastrophic or Mythic type move written into an institutional manual (Part 42) is a School Move: a Lineage Technique under Area 7.2, owned by the school or institution that holds the manual, teachable by Method L-1 and Method L-2, and not any character's personal Signature. A School Move keeps the Type it is classified as (Area 2) and the success rates of that Type; the depth levels of Area 9.2 belong to personal Signatures only. A school may codify a lineage-descended form of a founder's Signature only as a new Named Move under a new name (Rule 6.4); the founder's Signature stays identity-bound. The purpose of the binding is kept: a person's own Signature is never copied from a sight or a book.

(b) In Area 2.2, Type 5 (Signature), under "Identity Binding", replace the first sentence "A Signature move belongs to one cultivator." with: "A personal Signature move belongs to one cultivator (a Signature-type move in an institutional manual is a School Move, Rule 9.1.1)."

(c) In Rule 7.4.2, replace "A Signature move cannot be taken as such, since it is bound to its creator's identity (Area 9.1);" with "A personal Signature move cannot be taken as such, since it is bound to its creator's identity (Area 9.1, Rule 9.1.1);".

**Amendment 2 — Part 6 Area 7.1, Method L-2: the Manual Ledger pointer.** Append to Method L-2 (Manual Study):

> The manuals of the Manual Ledger (Part 42) are read by this method. One manual teaches one weapon type; the student starts at Novice mastery whatever the manual's grade (Part 42 Area 8); a character may hold a manual whose moves the character's realm does not yet allow, and each move is then Usable, Conditional or Latent for that character (Part 42 Area 3, Known but Latent). Area 4.1 is not changed by that.

**Amendment 3 — Part 6 Area 4 (pointer) and Rule 6.5 (the register extension).**

(a) Add, under the Governance boundary note at the head of Area 4, one line:

> Part 42 Area 3 states the per-character state of a move in a held manual (Usable, Conditional, Latent) and the Seal Rule; Table 4.1 is unchanged.

(b) Add to Rule 6.5.1:

> **Rule 6.5.1a — The Manual Ledger is the register of manual-borne moves (Part 42).** A Named Move that a manual of the Manual Ledger (`.claude/story-memory/ledger-manuals/`) carries is registered in the Manual Ledger by its ID, in the CSV files of that ledger, and `ledger-named-moves/_index.md` carries a pointer block for it and not a row for each move. A manual-borne move becomes a full row of the generic register when its name is first written in prose (Rule 6.5.5), and its First Area Appearance is then also entered in its CSV row. The Pre-Write Ledger Check and the Rule 6.2 collision scan read the Manual Ledger by ID and by name. The generic register still holds every Named Move that prose has written.

(c) Add to Rule 6.5.2:

> For a manual-borne move the user's entry holds a Manual Kit pointer (the manual IDs, Part 42 Area 11) in place of a move block. The Manual Ledger row owns every value of the move (Rule 6.5.6). The register row's Users cell points at the user's Manual Kit line, or, for a move no single person uses, at the institution's entry.

(d) Add to Rule 6.5.3, after the list of kinds:

> A manual-borne move is a `Lineage or school technique` (Part 42 Area 12). A personal Signature stays a `Signature Named Move`.

(e) Add to Rule 6.5.5:

> For a manual-borne move the same pass also sets the move's `first_area` in its CSV row (Part 42 Rule 42.12.5.1).

(f) In Area 6.2, "Checks for a New Move Name", after "the ledger scan (the name does not collide with or closely echo a move name already in the ledgers)", add: "the ledgers include the Manual Ledger."

**Amendment 4 — Parts 17, 18 and 19 (and Part 37 Areas 2.1, 2.2, 2.3): the Manual Kit pointer, Section 3 of the character ledgers.** Add to the Section 3 template of the hero, villain and Tier A and Tier B side-character ledgers, after the `Signature Named Moves` subsection (and the `Innate Moves` subsection where there is one), a subsection with this line:

> **Manual Kit (Part 42):** [the manual IDs from `ledger-manuals/character-kits.csv` for this character's `char_id`, separated by semicolons, or "none"]. The Manual Ledger owns the values of every manual-borne move; this line is a pointer. Query: `manual_ledger_query.py kit [char_id]`.

For Varya and Aegon the line reads:

> **Manual Kit (Part 42):** none. **Learning plan:** will learn from the academies of the kingdom (Part 42 Area 7); no manual ID is assigned.

The hero ledgers are frozen. These lines are added only on the author's permission, as the one scoped exception of Part 41 Rule 41.8.1.3 was added for Varya's and Aegon's birthdays.

**Amendment 5 — Part 37: the Manual Ledger, the twenty-second folder.**

(a) Area 4 (Ledger Folder Registry): add the row `| ledger-manuals/ | Area 3.12 | Active |`; change "Total active folders with full schemas: 21", "Total canonical folder count: 21" and every "21 ledger folders" in this Part to 22; add the sentence: "**Manuals.** `ledger-manuals/` is the twenty-second folder: the Manual Ledger of Part 42, a set of CSV files keyed by one ID scheme with an `_index.md` design record, on the schema of Area 3.12, with creation Threshold O-6. It carries the author's shortened name, with `ledger-named-items/`, `ledger-named-moves/` and `ledger-society-information/`."

(b) Area 1.5 (Thresholds): add Threshold O-6: "A manual-borne move or a manual title is entered in the generic register or the named-item register when an Area first writes it and is confirmed and written (Part 42 Rule 42.12.5.1); the Manual Ledger rows exist from the author's directive and need no prose."

(c) Area 3: add Area 3.12, "Schema Template: Manual Ledger", whose body states: file location `ledger-manuals/`; governing Parts 42, 6, 33, 37; the entry types (generic manual, move, kingdom row, personal manual, personal move, character, kit); the folder map, the ID schemes and the eight header lines of Part 42 Rule 42.10.3.1, which are the canonical headers; the B and L marks of Part 42 Rules 42.10.4.3 and 42.10.5.6; and the statement that the Manual Ledger is queried by `manual_ledger_query.py` and checked by Part 42 Rule 42.10.8.1.

(d) Area 7 (dependency table): add the row "Part 42 → Part 37: the Manual Ledger, its folder, template and threshold. HARD. Area 3.12, Area 4, Threshold O-6."

**Amendment 6 — Part 28 Rules 20.8.1, 20.8.4 and 20.8.7 (and Part 12): manual titles.**

(a) Rule 20.8.1, in the Types list, add to the row `other item` the example "a manual title (Part 42)", and add: "A manual title is a named item of Type `other item` registered by ID in the Manual Ledger (`ledger-manuals/`), with a pointer row in `ledger-named-items`; it is italic."

(b) Rule 20.8.4 (the register): add: "A manual title is entered at Gate 2 as a pointer row whose Entity File is the Manual Ledger CSV file that holds the manual and whose cell names the `manual_id` (Part 42 Rule 42.12.4.4)."

(c) Rule 20.8.7 (named documents): add: "A manual of the Manual Ledger (Part 42) is not a named document of this Rule. It is registered in the Manual Ledger and its title is a named item (Rule 20.8.1)."

(d) Part 12, Rule 2.2.3: add: "A manual is a named item and not a Named Relic or Artifact, unless this Part registers that one manual as a relic (Part 42 Rule 42.1.1.3)."

**Amendment 7 — Part 33: the weapon-type pointer.**

(a) Area 18.2 (Explicitly Not Part 33 Domain), add item 10: "**Manual and weapon-style law** → Part 42 (a weapon type is a style discipline taught by manuals; the Part 33 class of each missile, powder and siege type is read from Part 42 Area 9; no style moves a weapon beyond Tier 3 in Phase 1)."

(b) Area 2.9 (Tier 3 Handling Sheet), add after the table: "The sheet binds the Part 42 styles of the Musket, Rifle, Cannon (Field gun) and Grenade; the Pistol and Shotgun have no row (open for the author)."

**Amendment 8 — Part 3 Area 16.2 (pointer).** Add under the table: "Part 42 Area 3 holds the per-character Usable, Conditional and Latent state of a move in a held manual and the Seal Rule; this table is unchanged."

**Amendment 9 — Guardrails.** (a) `guardrails/ledger/guardrail-ledger-update-law.md`: add to the Gate 2 duties the Manual Ledger writes of Rule 42.12.5.1 and Rule 42.11.8.1, and the rollback of Rule 42.10.10.3. (b) `guardrails/ledger/guardrail-ledger-schema-law.md`: carry the twenty-second folder and the pointer to Part 42. (c) `guardrails/tools/guardrail-authorized-scripts-only.md`: the fifth script, `manual_ledger_query.py`, read-only (Rule 42.10.9.1), done by the orchestrator. (d) `guardrails/audit/guardrail-audit-gate-law.md`: the Gate 1 scope reads "Parts 2 to 33 and 35 to 42".

**Amendment 10 — Part 6 Area 6.2: the patterns are illustrations (Canon Amendment 2026-10-08; applied 2026-10-08 with the move-naming law of Rule 42.12.2.3).** (a) At the end of Area 6.2, "Move Naming Conventions", after "Invalid Names", add: "**Length and situation (Part 42 Rule 42.12.2.3).** Patterns 1 to 5 and their examples (which run to three, four and five words) are illustrations of how a name can be built. They are not minimum lengths and not models for a new name. A move name is one or two words (three only as Rule 42.12.2.3 allows), is tied to the weapon type and to the level and grade of the move, and never names a place, a setting, a tactic or an enemy." (b) In Area 6.2, "Checks for a New Move Name", after "distinctiveness (the name is phonetically and visually distinct from the other move names in the same scene and Chapter)", add: "and the move-naming law of Part 42 Rule 42.12.2.3 (length, weapon and level, and nothing situational)".

**Amendment 11 — Part 6 Area 3.7: Revive and Cleanse (Canon Amendment 2026-10-16; applied 2026-10-16 with Area 16).** In Part 6 Area 3.7 (Support Functions), after 3.7.3 Sense, add "**3.7.4 — Revive:** brings a person at the edge of death back within a short window, never the dead after it; each use is a Part 27 consequence event. **3.7.5 — Cleanse:** removes poison, taint, curse, binding, Qi Deviation backlash or soul erosion." The purpose of Area 3.7 (support moves restore, enhance or perceive) is kept. The cultivation axis of Part 42 Area 16 reads them.

### 15.2 — What This Part Applied Itself

This Part's registration was applied with its creation: the four canon-manifest files (`skill-index.json`, `domain-map.json`, `dependency-graph.json`, `ledger-architecture-map.json`); the authority guardrails (`guardrail-authority-tier-system.md`, `guardrail-consolidated-skill-reading.md`, `guardrails/_index.md`); and the counts that enumerate the Parts (forty skills, Parts 2 to 33 and 35 to 42, twenty-two ledger folders) in `guardrail-audit-gate-law.md`, the three agent files that quote the count, and the non-canon reference skill. No text of Parts 3, 6, 12, 17, 18, 19, 28, 33 or 37 was edited. A few other Part skills carry the sentence "Parts 2–27, 30–33, 35, 37–38, 40 and 41" in their Authority Tier line (Parts 2, 8, 9, 30 and 37); this Part leaves them to the amendment pass.

### 15.3 — Findings and Open Questions for the Author

**Findings (conflicts found and how this Part handled them).**
1. **Skill folder name.** The folder is `manual-and-weapon-style-law`, as the brief set. `guardrail-consolidated-skill-reading.md` requires every Part's skill to be named `<group>-<title>` (the domain group first). The conforming name would be `cultivation-manual-and-weapon-style-law`. This Part follows the brief and flags the difference.
2. **Signature unlock realm.** The brief's list put Signature at Mortal Tier 2 Warrior (Possible). The Access Table's "Possible" cell belongs to the group Senior to Warrior, so the first Usable realm is Senior (Rule 42.3.3.2). Fixed. Advanced, Elite, Fusion, Catastrophic and Mythic agree with the table.
3. **Manual titles and Part 28 Rule 20.8.7.** Part 28 sends a named document (a codex, a map) to `ledger-society-information`. The author's ruling makes a manual title a named item with a pointer row in `ledger-named-items`. This Part follows the ruling and asks Part 28 to say so (Amendment 6).
4. **Part 6 Rule 6.5.1 and 6.5.2.** "One generic register" and "a move block in the user's entry" do not fit tens of thousands of manual-borne moves. Extended by Amendment 3, purpose kept.
5. **Part 6 Area 9.1.** The identity binding as worded ("by reading a transmission manual") would make every Signature-type move in a manual impossible. Amended in scope by Amendment 1, purpose kept.
6. **Gale and firearms.** Part 33 Area 3.3 says a civilization cannot distribute weapons it cannot construct, and the Gale ledger records Tier 2, with firearms issued to infantry absent. The author's counts give Gale the same stock for the six Firearms types. Rule 42.9.4.5 limits what a Gale manual of those types teaches. The Gale counts for those six types are an open question.
7. **Part 33 hand weapons.** The hero ledgers' field "Primary Weapon Classification (Part 33)" reads Swords and Blades, but Part 33's taxonomy has no hand-weapon classes. Rule 42.9.4.2 reads the field as a registry family.
8. **Signature minimums.** The brief says at least three of the four Mortal Tier 2 Signature manuals have a minimum no higher than Ruler Level 1 Mid, and the design record says none is above it. This Part follows the design record (all four), which satisfies both.
9. **The Gale academies.** The brief called the Gale wind academies unnamed. The Gale ledgers name three (Stormbreak, Aerie, Long Coast). The table of Rule 42.7.2.2 uses them.
10. **"Azorion".** The author's label is Azorion, which is the capital of the Azure Sky Kingdom. The origin tag stays `Azorion`; the `kingdom` cell reads `Azure Sky`.
11. **Hero ledgers are frozen.** The Manual Kit pointer line needs the author's permission (Amendment 4).
12. **The reset script** restores the CSV `first_area` cells in Step 5b (Rule 42.10.10.4), author-authorized 2026-10-05.

**Open questions for the author.**
- Q1. Rename the folder to `cultivation-manual-and-weapon-style-law` (Finding 1)?
- Q2. Keep the full Gale stock for the six Firearms types, or reduce it (Finding 6)?
- Q3. Add Handling Sheet rows for the Pistol and the Shotgun, and for Tier 2 siege engines (Rule 42.9.4.4)?
- Q4. Are the four requirement ladders and their per-grade defaults right (Area 6)? The energy, cultivation, affinity and sovereignty ladders are `DERIVED` from Parts 3, 4 and 6, and the sovereignty ladder tests the recorded ceiling below the Core band because Level 8 is reached only at Core Solidification.
- Q5. Do the Nine Halls contain, spread across or sit beside the three Azure Sky academies (Rule 42.7.2.2)?
- Q6. Approve the sixth read-only command `name TEXT` for the collision scan (Rule 42.10.9.2)?
- Q7. (Answered 2026-10-05: authorized and done, `reset_story.py` Step 5b.)
- Q8. Approve `A`-prefixed codes, the `W` suffix and the `SOV-C` default (Rules 42.6.4.1, 42.6.5.2)?
- Q9. Approve the `found/` folder and `FND-` IDs as reserved (Rule 42.10.7.4)?
- Q10. Approve `ledger-manuals/` as the twenty-second folder and Threshold O-6 (Amendment 5)?
- Q11. Approve the Manual Kit pointer line in the hero ledgers (Amendment 4)?
- Q12. The personal-file stem is the lowercase character code (`vrs-manuals.csv`), not the character's name (Rule 42.10.1.2). Confirm?

---

## Area 16 — The Cultivation Axis (Canon Amendment 2026-10-16)

*Authority: the author's directive of 2026-10-16, point 8 (chat): cultivation-based moves besides weapon moves, from Warrior and above, a separate axis beside weapons, "same shape as weapons, scaled by affinity prominence", all eight grades, and the full ledger build before any chapter rewrite. The working design is `ledger-manuals/_design-cultivation-axis.md`; where it differs from this Area, this Area stands. Nothing in Areas 1 to 15 changes for the weapon axis.*

### 16.1 — The Axis and the Floor

**Rule 42.16.1.1 — A Second Axis.** The Manual Ledger has a second axis, the **cultivation axis**, in the subfolder `ledger-manuals/cultivation/`. A cultivation manual teaches one **discipline**, not one weapon type, and holds cultivation-based Named Moves (qi, affinity-resonant force, soul force, heart-state). The 79 weapon types, `weapons.csv` and all weapon-axis files, IDs and checks are unchanged.

**Rule 42.16.1.2 — The Floor.** A cultivation-axis move is usable from Mortal Tier 2 Warrior (Warrior Level 1 Low) and above. No cultivation manual has band M1 and no `min_realm` is below `Warrior L1 Low`. The Access Table (Rule 42.3.3.2) still decides which move types a realm may use; the floor is added to it. The one exception in range is Rule 42.16.4.3 (soul types).

**Rule 42.16.1.3 — The Eight Grades.** All eight grades (Basic to Mythic) exist as generic stock for every discipline. Fusion, Catastrophic and Mythic generic manuals are Common-origin and carry no kingdom row unless the author orders one. The composition table, the rounding rule, the move-count ranges, the `move_type`, `form`, `cost_class` and `unlock_realm` values are those of Area 2 and Rule 42.3.3.2, unchanged.

### 16.2 — The Disciplines and Their Prominence

**Rule 42.16.2.1 — The 65 Disciplines.** The registry is `cultivation/affinities.csv` and is closed at 65 `[DERIVED]`: the 50 affinities of Part 4 Area 1.3 (Primordial Element 15, Cosmic Force 8, Life Force 6 with "Soul (as Affinity)", Natural Phenomena 2, Metaphysical/Abstract 11, Healing/Support 4, Transcendent 4), the 11 soul types of Part 4 Area 2.3, and four other categories: Body Path (BDY), Qi Path (QIP, affinity-free qi), Cultivation Heart (HRT) and Formation Casting (FRM, the S-7 substrate). Bloodline-resonance, species-innate, relic-channeled, weapon-bonded and technology-aided moves are not manual material (Part 6 Area 12). A new discipline is a Canon Amendment on the author's word.

**Rule 42.16.2.2 — Prominence.** Each discipline has a class: Prominent, Standard, Niche or Rare (a fourth class the weapon axis does not have). The class sets the counts (Rule 42.16.3.1). The class of each discipline is in the design record `_design-cultivation-axis.md` section 2 and in `affinities.csv`; Healing, Life, Protection, the nine core elements, Swords, Strength, Body Path and Qi Path are Prominent; Death, Chaos, Light, Darkness, Order, Will, Illusion and eight soul types are Standard or Niche as the table says.

### 16.3 — Counts, Files and IDs

**Rule 42.16.3.1 — The Counts per Class.**

| Class | Basic | Intermediate | Advanced (common + per kingdom) | Elite per kingdom | Signature per kingdom | Fusion | Catastrophic | Mythic |
|---|---|---|---|---|---|---|---|---|
| Prominent | 10 | 8 | 7 (4 + 3) | 6 | 5 | 4 | 3 | 2 |
| Standard | 8 | 7 | 6 (3 + 3) | 5 | 4 | 3 | 2 | 1 |
| Niche | 6 | 5 | 4 (2 + 2) | 4 | 3 | 2 | 1 | 1 |
| Rare | 4 | 4 | 4 (2 + 2) | 3 | 2 | 2 | 2 | 2 |

A discipline therefore holds 59, 48, 35 or 30 manuals. The whole axis holds 2,837 manuals and about 28,200 moves.

**Rule 42.16.3.2 — Files and Columns.** `cultivation/affinities.csv` (the registry), `cultivation/manuals/<grade>/<AFF>.csv`, `cultivation/moves/<grade>/<AFF>.csv`, `cultivation/kingdoms/azorion.csv` and `gale.csv`, `cultivation/personal/<chr>-manuals.csv` and `-moves.csv`, `cultivation/kits.csv` and `cultivation/characters-ext.csv`. The columns are those of the weapon files with `weapon_id` replaced by `affinity_id` (manuals, same position) and `affinity_id` inserted after `manual_id` (moves). Exact header lines are in the design record and in `_index.md`; the check C-23 reads them.

**Rule 42.16.3.3 — IDs.** Manual `CMAN-{GRD}-{AFF}-{NNN}`; move `CMV-{GRD}-{AFF}-{NNN}-{SS}`; kingdom rows `CAZ-` and `CGA-`; personal `PCM-{CHR}-{NN}` and `PCM-{CHR}-{NN}-{SS}`. Numbering follows Rule 42.10.2.3: Common, then Azorion, then Gale; Signature and Elite per kingdom.

### 16.4 — Requirements and Eligibility

**Rule 42.16.4.1 — The Discipline Requirement.** The `affinity_req` cell is the discipline-requirement cell. For an affinity discipline it is `A2` to `A7`, never `NONE`, and obeys the band cap of Rule 42.6.4.2. For a soul type it is `SR1` to `SR12` (Part 4 Area 2.2, capped by the rung's realm equivalent). For Heart it is `HL1` to `HL5`. For BDY, QIP and FRM it is `NONE`. The `W` suffix is not used on this axis. `energy_req`, `cultivation_req` and `sovereignty_req` use the ladders and per-grade defaults of Area 6 without the M1 rows.

**Rule 42.16.4.2 — Windows.** BAS: M2, `Warrior L1 Low` to `Warrior L9 Peak`. INT: M2, `Warrior L1 Low` to `Champion L9 Peak`. ADV, ELI, FUS, CAT, MYT: the windows of Rule 42.5.3.3. SIG: the windows of Rule 42.5.3.3, with the layout per kingdom by `sig_n`: 5 = 3 M2, 1 XT, 1 CF; 4 = 2 M2, 1 XT, 1 CF; 3 = 1 M2, 1 XT, 1 CF; 2 = 1 XT, 1 CF.

**Rule 42.16.4.3 — Soul Types `[DERIVED]`.** The soul ladder begins at Demigod (Part 4 Area 2.2), so a soul-type discipline has no M2 band, except one Early Awakening Basic manual per soul type at Monarch (Part 4 Area 2.4). All other soul-type manuals open at Demigod L1 Low or above.

**Rule 42.16.4.4 — Usable.** A cultivation move is Usable for a character when the effective realm is at least `Warrior L1 Low`, the realm allows the move type (Rule 42.3.3.2), and the character holds the discipline's affinity at the level of `affinity_req` (the lower of the ledger ceiling and the realm cap, Rule 42.11.6.2), or the soul rung or heart level; otherwise it is Latent. A character with no affinity holds BDY, QIP and FRM manuals only. The Seal Rule (Area 3.4) applies unchanged.

### 16.5 — The Support Functions

**Rule 42.16.5.1 — Heal, Revive, Sense, Empower, Cleanse.** The function vocabulary of Rule 42.10.5.2 gains `Support:Revive` and `Support:Cleanse` (Part 6 Area 3.7, new 3.7.4 and 3.7.5). **Revive** brings back a person at the edge of death (breath stopped, pulse cut, soul stunned) inside a short window, never the dead after it, and each use is a Part 27 consequence event. Grade floor: Advanced. **Cleanse** removes poison, taint, curse, binding, Qi Deviation backlash or soul erosion. Grade floor: Intermediate. Heal, Empower and Sense are open from Basic. The soul form takes the `Soul-` prefix.

**Rule 42.16.5.2 — Healing Is First-Class.** A healing move is aimed at an ally or the self and its description says who is restored. A healer uses Heal, Revive and Cleanse moves from a healing source: Healing (HEA), Life (LIF) and Healing Soul (SOH) are Primary sources (at least half of their moves are Support, at least 30 percent of the healing ones Heal, Revive or Cleanse); Sense Soul (SOS) is Primary for Sense and Resonate Soul (SOR) for Empower. Secondary disciplines carry at least 15 percent Support moves; the list is the `support_role` column of `affinities.csv`. A healing move is never given an attack name (Rule 42.12.2.3(e)).

### 16.6 — Naming and Fusion

**Rule 42.16.6.1 — The Move-Naming Law Holds.** Rule 42.12.2.3 applies to every cultivation move. Because every manual is Warrior or above, names are affinity-anchored, cultivation-anchored or combined, tied to the discipline and the grade, never to a place, a setting, a tactic or an enemy, and impact rises with the grade. The share of three-word names is read per (grade, discipline) file, at most 5 percent of its moves rounded down, because a cultivation manual of 5 to 15 moves would otherwise allow none `[DERIVED]`; Fusion, Catastrophic and Mythic files may use three words and stay mostly two. Names and manual titles are unique across both axes (check C-31).

**Rule 42.16.6.2 — Fusion.** A Fusion-type move sits in the FUS grade of its primary discipline and begins its description `streams: <X> + <Y>`, the pair allowed by the Fusion Law (Area 2.3 and Area 3).

### 16.7 — The Tool and the Checks

**Rule 42.16.7.1 — Checks C-23 to C-31.** C-23 headers and format of the cultivation files; C-24 row counts and numbering against `affinities.csv`; C-25 the Warrior floor, band and windows; C-26 `affinity_req` form by discipline kind and the band cap; C-27 move rows, composition and move counts; C-28 move fields with the extended function set and the Revive and Cleanse grade floors; C-29 the Support quota by `support_role`; C-30 the Move-Naming Law (FAIL on four or more words and on a three-word share over the cap); C-31 name and title uniqueness across both axes. `manual_ledger_query.py` is extended to read both axes (`--axis weapon|cultivation|both`) and gains `affinity CODE`; it stays read-only, and no script writes ledger content (`guardrails/tools/guardrail-authorized-scripts-only.md`).

**Rule 42.16.7.2 — Ledger Write.** The generation workers write the CSV content by hand, one unit per worker (the design record lists 40 units), in the files they own. Kingdom rows are staged and merged by the orchestrator.

---

## Appendix A — Cross-References (Shared Across All 15 Areas)

The following Cross-References table applies to every Area of Part 42. It is stated once here.

| Related Skill | Relation | Source |
|---|---|---|
| `cultivation-move-taxonomy-law` §Areas 2, 3, 4, 5, 6, 7, 9, 10 | HARD | Part 6: the eight Move Types and rates, the Functions, the Access Table 4.1, the cost classes, the naming patterns, the register of Rule 6.5, the learning methods and Lineage Techniques, Signature identity, the Fusion protocol |
| `cultivation-power-and-lifespan-law` §Areas 1, 12, 13, 16 | HARD | Part 3: the ladder, the reserves, the meridian states, the Move Access Ceiling, Rule 1.7.3 |
| `cultivation-affinity-heart-and-soul-law` §Area 1 | HARD | Part 4: the nine Affinity Levels, the milestones by realm, the 50-type catalog, Fusion affinity pairs |
| `cultivation-fusion-law` | SOFT | Part 7: Fusion success rates and the Fusion architecture a Fusion-type move belongs to |
| `technology-weapon-law` §Areas 2, 3, 6, 18 | HARD | Part 33: the Tier 1 to Tier 3 classes, the Tier 3 Handling Sheet, accessibility by civilization tier, domain ownership |
| `energy-relics-and-artifacts-law` §Area 2 | SOFT | Part 12: a manual is not a relic unless registered |
| `character-hero-law`, `character-villain-law`, `character-side-character-law` | HARD | Parts 17, 18, 19: the character ledgers, Section 3, the Depth Spectrum, promotion |
| `society-faction-law`, `society-affiliation-law` | SOFT | Parts 22, 23: the institutions and their transmission rules |
| `society-culture-and-social-law` | SOFT | Part 25: the cultural registers of the two kingdoms |
| `narration-novel-creative-flexibility-law` §Areas 3, 20 | HARD | Part 28: name immutability, the Rule 20.3 method, the Rule 20.8 named-item form and register, the MAJOR and MINOR split |
| `narration-dialogue-and-social-interaction-law` §Area 12 | SOFT | Part 29: realm vocabulary in narration |
| `narration-novel-macro-story-law` §Area 1 | HARD | Part 30: Law P30-L8, Law P30-L1, the Phase 1 narrative ceiling, the seal end-states |
| `narration-novel-book-structure-law` §Area 3 | SOFT | Part 2: the bold-italic form of a Named Move |
| `ledger-schema-law` §Areas 1, 3, 4, 5 | HARD | Part 37: thresholds, the schema templates, the folder registry, the B/L classification |
| `spec-story-specification-law` §Area 1 | SOFT | Part 38: a spec establishes no fact |
| `character-monster-law` | SOFT | Part 40: monster innate moves are S-3 and are not in manuals |
| `worlds-calendar-law` | SOFT | Part 41: the Area reference form; no date is stored here |

## Appendix B — Governing Authority (Shared Across All 15 Areas)

> Subordinate to the guardrails in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.
