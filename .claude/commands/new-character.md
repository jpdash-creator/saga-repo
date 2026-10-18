---
description: Build the baseline record of a new hero, villain, Tier A or Tier B character, or a monster Kind or monster Individual, before they first appear. An AskUserQuestion interview that writes Character Ledger Sections 1 to 10 and then points to /character-behavior (characters) or to the Part 40 trait review (monsters).
argument-hint: <name> <role, one of hero | villain | tier-a | tier-b | monster-kind | monster>
user-invocable: true
---

# `/new-character`

Builds the **baseline record** of a character who has no ledger yet: who they are, where they
start, what they believe, what they carry and what they can do. The author is interviewed through
`AskUserQuestion`. The command writes Character Ledger **Sections 1 to 10**, opens the Current
Condition (Part 37 Section 13) as `none recorded at story start`, and then points to
`/character-behavior` for Sections 11 and 12.

Governing authority, by role:

- Villain: `character-villain-law` (Part 18) Area 7.2, Steps 1 to 5 (Rule 18.7.1.2: a villain's
  history is built before the villain appears).
- Hero: `character-hero-law` (Part 17) Area 2.3, the Hero Starting Position.
- Tier A or Tier B: `character-side-character-law` (Part 19) Area 6, the Side Character Profile.
- Monster Kind or monster Individual: `character-monster-law` (Part 40) Areas 2 to 8 and, for
  a sentient monster, Area 11.

Schema authority for what is written: `ledger-schema-law` (Part 37) Areas 1.2 and 2.1 to 2.3, Area 3.10
for a monster, and Area 2.11 for the folder's registry row.

## Why this exists

Part 18 Rule 18.7.1.2 says a villain's history must be built before the villain appears, and Part
17 Area 2.3 requires a hero's Starting Position. Nothing ran those with the author:
`/character-behavior` builds only the behavior record (Sections 11 and 12), `/update-ledger` edits
an entity that already has a ledger, and the Post-Write Ledger Update records only what an Area
has already shown. Without this command the first villain would be created by whoever drafts the
first Area that shows one. This command builds the record first, so the Area is written against
it.

## Modes

| Invocation | Interview | Written |
|---|---|---|
| `/new-character <name> villain` | Part 18 Area 7.2, Steps 1 to 5 | `ledger-character-villain/<name>.md`, Sections 1 to 10 (Part 37 Area 2.2) |
| `/new-character <name> hero` | Part 17 Area 2.3, the Hero Starting Position | `ledger-character-hero/<name>.md`, Sections 1 to 10 (Part 37 Area 2.3) |
| `/new-character <name> tier-a` | Part 19 Area 6.2, the Side Character Profile | `ledger-character-side/<name>.md`, Sections 1 to 10 (Part 37 Area 2.1) |
| `/new-character <name> tier-b` | Part 19 Rule 19.6.1.1, the Side Character Profile, populated as far as the role needs | `ledger-character-side/<name>.md`, Sections 1 to 10 (Part 37 Area 2.1, Ledger Type Tier B) |
| `/new-character <name> monster-kind` | Part 40 Areas 2 to 8: the Kind (class, tier, body, stage band, cultivation varieties, habitat, twelve Baseline traits, distinct abilities, Harvest line) | `ledger-character-monster/<name>-kind.md`, Sections 1 to 10 and the Signature Traits of Section 11 (Part 37 Area 3.10, Kind form), and the Kind Registry row |
| `/new-character <name> monster` | Part 40 Areas 2 to 8 for an Individual (its Kind, exact stage, own history, differences, Threat Role); Part 40 Area 11 as well for a sentient monster | `ledger-character-monster/<name>.md`, Sections 1 to 10 and, for a non-sentient monster, the Signature Traits of Section 11 (Part 37 Area 3.10, Tier A or Tier B Individual), and the Tier A and B registry row |

The monster roles are for a Tier A or Tier B Individual or Kind, for every sentient monster, and for any Kind
that the author builds by hand (Part 40 Rule 40.6.3.1). A Kind carries a tier A to D, and a Kind that has a
Named Move, recurs at Section scale or is sentient has a full file whatever its tier (Part 40 Rule 40.6.1.4). A Tier C or Tier D monster is registered at Gate 2 (or before
drafting, when a Chapter Spec names it), with no interview. A sentient monster is built here only when the
author has opened that class (Part 40 Rule 40.11.4.1); no sentient monster is built for Phase 1 (Law P30-L9),
and where one may live is `OPEN-AUTHOR`. The command creates no Kind for the beasts that Part 30 plans for
Phase 1: that Kind is defined at its Chapter Spec (Part 40 Rule 40.7.5.1).

A villain built here is a Tier A or Tier B villain, which the author maps from the macro story (Part 18 Rule
18.6.3.3); a Tier C or Tier D side villain is an entry or a row in `ledger-character-villain/_index.md`,
not a file built here.

The command is not run for a Tier C or Tier D person. A Tier C person may be registered as an
abbreviated entry when the story needs one (Part 37 Threshold C-1). A Tier D person gets a registry
row with a picked code while the draft is written (Part 19 Rule 19.1.2.7), and no interview.

## Plan Mode / Auto Mode

Per `guardrails/commands/guardrail-plan-then-auto-execution.md`, this command's **Plan Mode** is
the interview: every author-facing question is asked and resolved, and the digest is accepted,
before any file is written. **Auto Mode** is the write and the verification.

## Sequence

1. **Ground**: check the name against every `ledger-character-*/` folder. If it already has a
   ledger, stop and point to `/update-ledger`. Read the Part 37 template for the role, the
   folder's `_index.md`, the entries for this person in the specs of the current chain (the Chapter
   Spec, the Novel-Part Spec and the Section Spec), where such entries exist, and the
   ledgers the answers will touch (home faction, location, civilization). Batch the reads in one
   message.
2. **Ask**: the interview for the role (below), in rounds of up to four questions.
3. **Digest**: present the whole record in plain language, section by section, for override.
   Nothing is written until the digest is accepted.
4. **Write**: Sections 1 to 10 in the Part 37 template, the Current Condition as
   `none recorded at story start`, and the folder's `_index.md` row. Sections 11 and 12 are not
   written here.
5. **Verify**: every section is present; every Baseline (B) field is an author answer, a canon
   value with its source cited, or marked `OPEN-AREA`; the `_index.md` row matches the file.
6. **Point onward**: tell the author to run `/character-behavior <name>` next. Part 39 Rule
   39.4.3.1 requires the registration before the person acts or speaks in an Area (Rule 39.4.3.4
   sets when a villain's registration is due). For a non-sentient monster nothing further is owed: its
   twelve traits and Signature Traits are already written (Part 40 Area 5). For a sentient monster the
   full Part 39 registration is owed, as for a character (Part 40 Rule 40.11.6.1).

## The interview

### Villain (Part 18 Area 7.2)

1. **Ideology first**: Core Ideology (Part 20 Area 1.1), then Operational and Surface Ideology.
2. **History second**: the events (IE, CSS and PIS) that produced the Core Ideology: the original
   wound, the first maladaptive response, the point of no return and the moment of full commitment.
3. **Psychology third**: the Part 18 psychological archetype (Armored, Consumed, Calcified,
   Fractured, Hollow), the PIS state that follows from the history, and the primary coping
   mechanisms.
4. **Power fourth**: realm, technology tier, faction backing and strategic assets, within Parts 3,
   8, 16 and 22.
5. **Function fifth**: the arc type, the thematic weight, and what the villain's defeat (in any of
   the five forms) would mean for the story. Nothing here compares the villain with the hero or
   with any other character.

### Hero (Part 17 Area 2.3)

The Starting Position elements: realm or technology tier at story entry; initial ideology state
(Core, Operational, Surface); initial psychological profile (baseline health and any wound from
before the story); initial consequence profile; initial faction, sect or affiliation position;
initial social class position; and all significant relationships at story entry with type and
weight. Locked Canon fields (Part 30) are copied from Part 30 and never asked.

### Tier A or Tier B (Part 19 Area 6.2)

Identity and primary narrative function; classification (the Part 37 Area 2.1 field list);
ideology (category, stability state, Core, Operational and Surface summary, key IE history);
psychology (PIS state, wounds and their origin events, coping); consequence history and debts;
relationships and faction positions; narrative arc status. A Tier B person gets the same questions,
populated as far as the role needs, for the Tier B file.

### Monster Kind or monster Individual (Part 40 Areas 2 to 8)

Same interview style: rounds of up to four questions, options concrete and quoted from canon, the
recommended option first, free text always open.

- **Kind:** the class (Part 40 Rule 40.2.2.1; a Reserved or `OPEN-AUTHOR` class is not offered for a
  Kind until the author opens it); its depth tier A to D (the name of a Tier A or B Kind is MAJOR: 2 to 3 candidates plus SKIP, Part 28 Rule 20.4(g)); body and size; origin; the stage band (two Part 3
  names, no ladder of its own; inside Part 30's bands for a Phase 1 Kind); affinity type and level, soul rung,
  type and talent, Heart level, Meridian Root and any other cultivation variety (Part 40 Rule 40.3.4.2; the
  Part 3 and Part 4 vocabulary by reference, `OPEN-AREA` where not yet shown); habitat (pointers to the location ledger) and its
  Ambient Energy Class; the twelve Baseline traits, one at a time, each with the Part 39 dimension it reuses;
  distinct abilities (every distinct, memorable ability is named: a body-based one is S-3, a qi-based one S-1;
  regular punches, kicks, bites, charges and the like stay plain description, Part 40 Rule 40.4.1.3; each named
  ability gets its row in `ledger-named-moves` in the same pass); the
  Harvest line (limited by Parts 11 and 12; nothing from a Phase 1 monster); how people treat it. For a
  sentient Kind only, once the class is open: how it speaks (human speech in the common tongue and/or
  mind-voice through the soul-sense channel), its ancient language if any, and the full Part 20 and
  Part 26 profile; its home is `OPEN-AUTHOR` ("It will come in future phases").
- **Individual:** its Kind (a pointer), its name (MAJOR for a Tier A or B Individual: 2 to 3 candidates plus
  SKIP, Part 28 Rule 20.4(g)), the exact stage, its own history, the points where it differs from its Kind,
  its Threat Role, its current state, and its Tier (A or B). A Tier C or D Individual is not built here.
- Nothing compares one monster with another or with a person (Part 40 Rule 40.1.3.4). A non-sentient monster
  is never offered as a villain (Part 40 Rule 40.12.1.1).

## Question construction

- Options are concrete and quoted from canon, with the recommended option first and its reasoning
  in the option description. Free text is always open.
- Story facts default to open. The author may answer "let the first Area decide"; the field is
  then recorded as `OPEN-AREA`, and nothing is invented to fill it.
- Characters are designed standalone. No question asks for, derives or
  records a comparison with another character. A mirror or foil relationship is recorded only on
  the author's own ruling, after each person is designed standalone.
- Never ask what a confirmed spec of the chain (Section, Novel-Part or Chapter Spec) or Part 30
  already fixes; show it as a given.

## Hard rules

- A name that already has a ledger is never rebuilt here: stop and point to `/update-ledger`.
- A Baseline (B) field is never written from a guess.
- No answer changes a Locked Canon fact. A conflict is surfaced to the author, never resolved
  silently (`guardrails/authority/guardrail-locked-vs-negotiable-canon.md`).
- The record is written in full or not at all. A half-built record counts as no record for the
  Pre-Write Ledger Check.
- A Tier D person is excepted throughout (Part 19 Rule 19.1.2.7).

## How the Pre-Write Ledger Check uses it

`guardrails/ledger/guardrail-ledger-update-law.md`: the Pre-Write Ledger Check refuses a first
appearance of a hero, a villain, a Tier A or Tier B person, a Tier A or Tier B monster Individual or Kind or any
sentient monster who has no such record, and points the author here. The Area Maker carries the same stop in its steps before drafting
(`agents/area-maker.md`).

## Related

`/character-behavior` is the next step. `/update-ledger` edits the record afterwards.
`/review-ledger` and `/character-sheet` read the result. The specs list the debut
(`/section-spec`, `/part-spec` and `/chapter-spec`), and `/next-area` runs the Pre-Write Ledger
Check.
