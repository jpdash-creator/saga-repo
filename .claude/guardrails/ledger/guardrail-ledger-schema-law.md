# Guardrail: Ledger Schema Authority

**Source:** Part 37 (SSC Canon Ledger Schema Law) · full detail: `ledger-schema-law` · Canon v10.0
**Applies to:** Continuity Checker (primary owner of `.claude/story-memory/` writes)

## The rule

Part 37 is the schema authority for every `.claude/story-memory/ledger-*/` file — both the
per-folder `_index.md` registries and the individual entity files. Where any other file
describes a ledger schema differently, **Part 37 governs**.

- **22 active ledger types** have full schema templates in Part 37: ten in Area 2 and
  twelve in Area 3 (Areas 3.1 to 3.12; the eighth and ninth, the named-item register and the
  Named-Move register, are one-table registers with no entity files; the tenth, the monster
  ledger, has entity files; the eleventh, the calendar ledger, is an index-only set of date
  tables with no entity files; the twelfth, the Manual Ledger, is a folder of CSV files with no entity files). If
  prose introduces an entity that fits none of them, flag it (`NEW ENTITY TYPE — Part 37
  schema not yet defined`) and get explicit direction before inventing a schema.
- **Monsters have a ledger, `ledger-character-monster/`** (Part 37 Area 3.10, Thresholds M-1 to M-3;
  defined by Part 40). It holds two kinds of entry, a Kind and an Individual, and an Individual
  points at its Kind and records only what is its own. The folder is arranged by the four tiers of
  depth of record (a full file for Tier A and B, a short entry for Tier C, a row for Tier D); a Kind carries a tier too, and has a full file at its first Named Move, at Section scale or when sentient, whatever its tier.
  **A non-sentient monster's hostility is not qualifying behavior for Threshold C-2** (Part 40
  Rule 40.12.2.1), so the villain-classification question is never put for one; a sentient monster
  raises it once (Threshold M-3), and on a Villain ruling its record moves to
  `ledger-character-villain/` as one canonical file and a pointer row marked migrated stays in the
  monster index. `ledger-character-villain/` is arranged by the same four tiers (Part 18 Area 6.3):
  Tier A and B are reserved until the author maps them, Tier C and D are the side villains.
- **Named items have a register, `ledger-named-items/_index.md`** (Part 37 Area 3.8,
  Threshold O-4; defined by Part 28 Rule 20.8). Every named item written into a confirmed
  and written Area is entered as a row at Gate 2. The row is a pointer and never a copy: where
  the item has a home entry in another ledger, that entry owns every descriptive fact. The register
  has a Types vocabulary of fourteen (apparatus or device, remedy, gear or tool, weapon, system or
  service, material, food, drink, dress or adornment, vessel or vehicle, relic or artifact, formation
  array, energy cache, other item), and anything that is an item gets registered; a Named Relic,
  Named Artifact, formation array and energy cache are items, with their descriptive entries staying
  in `ledger-energy-relics-artifacts`. The article is never
  part of a registered name.
- **The information ledger stores all information, `ledger-society-information/`** (Part 37 Area 3.4;
  Part 28 Rule 20.8.7). Besides intelligence assets and character knowledge, it holds a
  register row for every named document (a map, letter, charter, decree, codex or record, set in
  italic) and every named agreement, treaty or accord (set in roman, with its agreement file in
  `ledger-people-society-affiliation/` as the home entry), entered at Gate 2. A named document is
  never entered in the named-item register.
- **Named Moves have one generic register, `ledger-named-moves/_index.md`** (Part 37
  Area 3.9, Threshold O-5; defined by Part 6 Rule 6.5). Every Named Move is entered as a row at Gate 2,
  and, wherever a person uses it, also in that person's character-ledger entry (the Section 3
  Named Moves registries), the row and the entry each pointing at the other. The entry owns every
  value of the move; the register holds none. A Named Move is not a named item: its form stays
  bold-italic.
- **Manuals have a ledger, `ledger-manuals/`** (Part 37 Area 3.12, Threshold O-6; defined by Part 42, the Manual and
  Weapon Style Law). It is a set of CSV files keyed by one ID scheme, with an `_index.md` design record, and holds no
  entity file. The Manual Ledger owns every value of a manual-borne move; `ledger-named-moves/_index.md` carries a
  pointer block for the stock and a full row only for a move that prose has written, and a manual title is a named item
  whose pointer row sits in `ledger-named-items/_index.md`. Part 42 Rule 42.10.8.1 checks the ledger and
  `manual_ledger_query.py` queries it. A move's `name` cell follows the move-naming law of Part 42 Rule 42.12.2.3
  (Canon Amendment 2026-10-08): one or two words, tied to the weapon type and to the level and grade of the move,
  never to a place, a setting, a tactic or an enemy; the Naming Checks cell of its register row records the check.
  The checks and the script read no length on the weapon axis, and a replaced stock name is kept in the manual row's `notes`.
  **Cultivation axis (Canon Amendment 2026-10-16, Part 42 Area 16):** the Manual Ledger has a second axis,
  `ledger-manuals/cultivation/`, for cultivation-based manuals and moves (65 disciplines: the 50 affinities,
  the 11 soul types, Body Path, Qi Path, Heart and Formation), usable from Warrior and above, all eight
  grades, IDs `CMAN-`/`CMV-`/`CAZ-`/`CGA-`/`PCM-`, columns as the weapon files plus `affinity_id`, checks
  C-23 to C-31 (which do read name length). Heal, Revive, Sense, Empower and Cleanse are first-class Support
  functions. Same Move-Naming Law, same read-only tool, no script writes ledger content.
- **The calendar has a ledger, `ledger-worlds-calendar/_index.md`** (Part 37 Area 3.11,
  Threshold D-1; defined by Part 41, the Calendar Law). It is one index-only file of date tables
  and holds no entity file. Threshold D-1 is met by a dated Area. Its Baseline tables (the epoch,
  the months, the weekdays, the fixed days, the eight heroes' birth years and the planned Phase
  and Section windows, which carry no status column) mirror Part 41, and its recorded tables
  (Phase, Section, Novel-Part, Chapter and Area) and the Current Position row are Living (a
  Section's status is in its recorded Section row, and Gate 2 keeps the Total Entries line
  current; a reset returns it to 0). The ledger dates every Phase, Section, Novel-Part, Chapter
  and Area, and every Area confirmed and written is dated by the date line that opens it: the
  Post-Write Ledger Update writes the Area row, the rollups and the Current Position row at
  Gate 2, and the Pre-Write Ledger Check reads the Current Position row (Open Chapter and the
  Open Chapter's recorded window, First to Latest) and the open Chapter's row. The ledger owns every recorded date, a spec's windows are never copied into it
  (Part 38 Rules 1.3.2 and 1.4.2), and the hero ledgers are frozen, so the birth years live only
  there. Each recorded table sits under an "Events Log" heading, so the existing reset empties it.
- **Entity Creation Thresholds** (Area 1) gate *when* a new ledger file may be created —
  not on first mention, but once the prose has established enough for a real entry. The
  prose comes first and the entry is made at Gate 2: a person the Chapter Spec names is
  registered before drafting, and a person the drafting agent improvises in the prose, Tier C
  or Tier D, is registered at Gate 2 from what the prose established, the gaps marked
  `OPEN-AREA` (Threshold C-1; Part 39 Rule 39.4.3.1). A first
  appearance carrying qualifying antagonistic behaviour requires an explicit
  `AskUserQuestion` before the file is created (Threshold C-2, Villain Classification). A
  Hero Ledger is never created by an agent on its own initiative at all (Threshold C-3):
  C-38 emits only the Hero-candidate flag and waits for explicit user instruction — it does
  not open an `AskUserQuestion` to propose the promotion.
- **Character ledgers are thirteen-section** (Section 13 is described in the next bullet). Section 11 (Behavioral Signature) and
  Section 12 (Behavioral Evolution Log) carry the Part 39 registration. Any reference
  anywhere in the system to the "10-Section Character Ledger Template" is read as the
  thirteen-section template. Section 11 is populated **in full** at registration — a
  partial Section 11 is a registration in progress, not a compliant ledger, and the character
  may not be drafted into an acting appearance until it is complete.
- **Character ledgers also carry Section 13, Current Condition**: the
  emotional, mental, psychological, physical, metaphysical and soul states and every wound with
  how long it lasts, detailed for heroes, villains and Tiers A and B, two lines in the registry
  row for Tiers C and D. It is Living, written after each Area and read before the next.
- **Location, faction and civilization ledgers carry a Collective Behavior Code block**
  (Part 37 Areas 2.4/2.6/2.7, content model at Part 39 Area 41.4). Group conduct is stored
  where the group lives, never duplicated onto each member; a character records only their
  conformance and their named deviation seam.
- **Baseline (B) vs. Living (L) fields**: B fields are locked at creation and may only be
  enriched, never contradicted, without a formal Canon Amendment. **One documented exception
  applies to Part 39 Signatures**: they are Baseline, and they have a second lawful path to
  change besides Canon Amendment — a logged Section 12 drift event with a named trigger
  (Part 39 Area 42). That second path is the entire purpose of the Section 11/12 pairing and
  is not a weakening of the B rule elsewhere. L fields are the ones
  expected to change and are the ones Post-Write Ledger Update (see
  `guardrail-ledger-update-law.md`) actually touches.
- **Canon Amendment procedure.** A formal Canon Amendment of a
  Baseline field is the author's on-record directive: the change, in the author's own words,
  never an agent's inference. The Continuity Checker then edits the Baseline field, appends
  `Amended <date>: <old> to <new>, <reason>` to the file's changelog, and runs ALCA Mode A on
  the entity (`audit/guardrail-alca.md`). `/update-ledger` is the command that carries it out.
- **The Tier D registry is one standard table** (Part 37 Area 2.11, Tier D template): the six standard
  columns plus One-Line Descriptor, Code (Baseline), Pair-Senior and Current Condition (Living). The Code cell is written once, at
  Gate 2, from the code validated at Gate 1, and changes only by Canon Amendment on the author's word.
  Part 19 Rules 19.1.2.3 to 19.1.2.7 are the single source of the Tier D rules.
- **Reference form (Amended 2026-10-07).** A ledger reference to written prose is the Area reference `P.S.N.CCC.AA`
  for an Area-built Chapter and the Chapter reference `P.S.N.CCC` alone for a Chapter built whole by
  `/create-chapter` (it has no Area files and no scene-level code is ever written into a ledger). The same holds for
  every ledger field that names where something happened: First Appearance, Canon Events Log rows, Evolution
  Entries, Named Move rows, calendar rows (a whole-built Chapter gets one row per date segment under its Chapter
  row) and scoring rows. Both forms are valid in the same ledger; a whole-built Chapter is updated in one batch
  (`guardrail-ledger-update-law.md`).
- **A field the template gains.** A field the template defines and the file lacks is added when the
  entity is next touched at Gate 2, written `OPEN-AREA` (`OPEN-AUTHOR` where only the author sets
  it), never an invented fact (Part 37 Area 5).

## Hard rules

- **Ledger beats prose on conflict.** If a ledger file and a written Area disagree, the
  ledger is authoritative until formally reconciled — never silently defer to whichever the
  agent saw most recently.
- **No Duplication Across Ledgers.** An entity gets exactly one canonical ledger file; do not
  create a second record of the same entity in a different folder.
- **A behavioral Signature is never rewritten editorially.** Correcting a Signature outside
  the drift mechanism, or deleting a superseded behavior from Section 12, is a schema
  violation reported via ALCA. Section 12 is append-only: a Check #21 `[DEFER]` is recorded
  by appending a row to its Deferred table (Part 39 Area 41.2), never by editing a counter.
  **One lawful exception: rollback** (Part 39 Rule 39.41.6.1). When
  `/rewind-to`, `/redraft-area`, `/redraft-chapter`, `/reset-chapter` or `/reset-phase`
  archives or deletes the Area that caused a drift, the reconciliation pass undoes that drift:
  the Section 12 entry is marked `rolled back` and is not deleted, and a Permanent drift's
  prior value returns to Section 11 from the superseded-behaviors table. `/hard-reset` and
  `/reset-story` clear Section 12 after the same restore (Rule 39.41.6.2). Nothing else may
  delete or edit a Section 12 entry.
- **Character Role Migration** (villain ↔ side character) is AI-executable; **Hero
  characters cannot be migrated without explicit user instruction** — the Hero Ledger's
  survival-protection status is not something an agent revokes on its own. A sentient monster
  moves to the villain ledger only on the author's answer to the Threshold M-3 question (Part 40
  Rule 40.12.3.1), and a tamed monster that becomes a person-like companion moves to the side
  ledger only on the author's ruling (Part 40 Rule 40.9.3.1).

## Escalation

Schema drift (e.g. a ledger index missing a required section) is reported via ALCA, not
silently rewritten mid-unrelated-task.
