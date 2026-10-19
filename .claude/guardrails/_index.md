# Guardrails Index

**Canon v10.0 · Last Updated 2026-10-19** (Canon Amendment of 2026-10-19: Situational Combat Mechanics Law, Part 45, read at Gate 1 Check #24, with the invented scene-ordering rule for moves removed; Canon Amendment of 2026-10-17: Battle Plausibility Law, Part 44, read at Gate 1 Check #23; Canon Amendment of 2026-10-16: Cultivation Visibility, Part 29 Rule 29.12.1.3, read at Gate 1 Check #8 element 8-V; Canon Amendments of 2026-10-08: the Move-Naming Law, Part 42 Rule 42.12.2.3; dialogue craft, Part 29 Rules 29.2.1.1c and 29.2.1.7)

This folder is the shared, non-negotiable grounding for all four Starward Saga agents
(Area Maker, Outline Planner, Continuity Checker, Area Scorer). Every agent reads this
index first, then the specific subfolder(s) relevant to what it is about to do. Guardrails
state hard MUST / MUST NOT rules only — the detailed "how" for any given topic lives in the
corresponding `.claude/skills/<group>-<title>` skill, not here. If a
guardrail and a skill ever appear to conflict, the guardrail wins and the conflict must be
escalated by the route set out in the Escalation rule at the foot of this index, never
resolved silently.

Guardrails encode the Tier-0 prose-craft
layer (Parts 28, 29, 36 and 39 and the Plain Language and Narrative Impact guardrail: the
Locked-Canon boundary and naming/narration-craft law, dialogue and voice law, the
narrative-quality mandate, the character behavioral registry, and plain words) and the small
number of Tier-1 Parts that contain absolute, cross-cutting constraints (Part 37's ledger
schema authority, Part 38's spec-chain authority model, and the authorized-scripts law).

## The structure the guardrails govern

- **Five tiers: Phase, Section, Novel-Part, Chapter, Area.** The Area is the written unit. It may be a
  complete scene, or a scene may continue across consecutive Areas of the Chapter. An Area is written to
  one of three targets (1,600, 1,800 or 2,000 words), decided in the Chapter Spec, and passes between
  1,280 and 2,400 words; a count outside that range is a blocking finding: the write waits for the author to confirm the Area or send it back.
  Every Area opens with one italic date line. Every Area is written by one full Gate 1 → confirm → Gate 2 cycle.
  (Amended 2026-10-07: the Area is the written unit of `/next-area`. A Chapter may also be built whole by
  `/create-chapter` (Command C-42, default) from its confirmed Chapter Spec, with no Area files: one Chapter file pair
  in the Novel-Part folder, hidden `<!-- AREA NN -->` markers in the `.md`, each Area block written at 55% to 60% of
  its size target (a named stretch up to 72%), the Chapter total between 0.55 T and 0.72 T, and the Whole-Chapter
  Gate 1 and Gate 2 of `guardrail-audit-gate-law.md`. The Chapter Spec header names `Build mode: whole | by-area`;
  a Chapter is built one way, never both. `/revise-chapter` is Command C-43.)
- **Numbers inform.** Each floor, ceiling, band, budget, counter or projection is a guide post that informs and
  never governs. A crossed line is shown as information in the audit report; it does not fail an Area, block a
  scene, force content or put a question to the author on its own, and the confirmed spec chain and Part 30
  prevail over every counter. The one exception is the Area size range above, which is structural and blocks.
- **The spec chain.** A **Section Spec** (`/section-spec`, Command C-40) is built whenever a Section starts; it
  reads the whole of Part 30 for what that Section is expected to hold and, by asking the author, turns that into
  the Section's Novel-Parts and Chapters at a high level. A **Novel-Part Spec** (`/part-spec`, Command C-41) is
  built whenever a Novel-Part starts and lists every Chapter of it in depth. The **Chapter Spec** (`/chapter-spec`,
  Command C-39) is built from its Novel-Part Spec entry and decides, for every Area, its pacing, its size target
  and its plan. Part 38 (Areas 9 to 11) governs the chain. It is ordered: a Chapter Spec cannot be built or revised
  unless its Novel-Part Spec and its Section Spec are confirmed, and a Novel-Part Spec cannot unless its Section
  Spec is. Gate 1 Check #18(a) asks whether the chain is in force. All three builds keep asking the author until
  nothing is left unasked at their own level, a final sweep finds nothing new and the author says there is nothing
  further to steer; only the author may defer an item (Part 38 Rule 38.13). A spec reads as clean plan text from
  start to finish: every settled item, open item, deferral, ruling, variance and audit note sits in its final
  section, **Audit and Settlement Notes**, each note pointing back to the plan item it concerns. The spec status
  `COMPLETED` marks a finished spec, which stays a living record. The Gate 2 as-built sync writes only the Chapter
  Spec, with its registry row. A Section's title-page epigraph is the Epigraph line of its Section Spec, and the
  Phase epigraph is a line of Part 30 that a Phase's first Area prints above Section 1's own Epigraph line (every
  other Section's first Area prints only that Section's line); no agent ever writes either one. A departure at any
  level is recorded as a variance note on every spec above it, top-down in one step, and the author chooses, for
  each departure, to amend the plan or keep the original as the plan baseline.
- **Named items.** A named item (Part 28 Rule 20.8.1) is a made or used thing with a proper name of its own. Its name
  is set in italic at every mention in the Area text and in every spec file, the name only, and in roman inside a
  passage that is already italic; the same name always takes the same form (Rule 20.8.2). Relics, artifacts,
  formation arrays and energy caches are named items; named documents are italic and agreements, treaties and
  accords are roman, registered in `ledger-society-information/`. Every named item written into a confirmed Area is
  entered at Gate 2 as a row of `ledger-named-items/`, a pointer to its home entry. Naming is never presented as a
  cost (Part 28 Rule 20.9). Every Named Move is entered at Gate 2 in `ledger-named-moves/` and in each user's
  character-ledger Named Moves registry, each pointing at the other; Named Moves keep their bold-italic form.
- **Monsters.** Part 40 (Monster Law, skill `character-monster-law`) governs the beasts of the world; the ledger is
  `ledger-character-monster/`, arranged by depth tiers A to D that mean depth of record and never power. Sentient
  monsters are not in Phase 1 (Law P30-L9; save the one narrow artifact-made exception of Canon Amendment 2026-10-19 (Law P30-L9)). Monster names are set in roman. A monster without a mind is never a villain.
  `ledger-character-villain/` is arranged by the same four tiers (Part 18 Area 6.3).
- **The calendar.** Part 41 (Calendar Law, skill `worlds-calendar-law`) is the one home of the calendar, a Tier 1
  domain authority in the `worlds` group. The saga opens in Year 1247; every Area opens with one italic date line
  (`*Year 1247, <Month>, <Weekday>, Day 27*`) that is not narration, is not counted in any size or word count and is
  never an Area's opening paragraph for any reading. The date line is read at Gate 1 by Check #11 element 11-2 and
  Check #12. The ledger is `ledger-worlds-calendar/` (index-only, `_index.md`); Gate 2 writes its rows, and the
  specs write the Area's dates as dates plus Phase Day.
- **Manuals.** Part 42 (Manual and Weapon Style Law, skill `manual-and-weapon-style-law`) is a Tier 1 domain authority in
  the cultivation group. A manual is a written or encoded transmission text (Part 6 Method L-2) that holds 5 to 15
  Named Moves for exactly one weapon type, in one of eight grades (Basic to Mythic) with a fixed move-type
  composition. Manuals live in `ledger-manuals/`, a set of CSV files keyed by one ID scheme and read by ID with the
  read-only `manual_ledger_query.py`. A character may hold a manual of any grade; each move in it is Usable,
  Conditional or Latent for that character (the Part 6 Access Table is not amended). Signature, Fusion,
  Catastrophic and Mythic moves in an institutional manual are School Moves, not a personal Signature. A manual
  title is a plain-italic named item; a manual move is a bold-italic Named Move. Move names follow the Move-Naming Law
  (Part 42 Rule 42.12.2.3, Canon Amendment 2026-10-08): one or two words, tied to the weapon type and to the level and
  grade of the move, never to a place, a setting, a tactic or an enemy; Gate 1 Check #17(b) reads it.
- **Battle plausibility.** Part 44 (Battle Plausibility Law, skill `cultivation-battle-plausibility-law`, Canon Amendment 2026-10-17) is a Tier 1 domain authority in the cultivation group beside Parts 3 and 5. It checks that a whole engagement (squads, numbers, ground, weapons, wars) makes sense at the levels written: each side is anchored by its strongest few; each pairing is Open (gap 0 to 2 minor steps), Shut (3 or more) or Barred (across a Major Realm); a lower side holds, delays or beats a higher one only through a named, priced, lawful offset (numbers and formation; ground, preparation, ambush, surprise and shielding; technology and weapons; exhaustion and cost; a registered gifted fighter, who fights as if up to 3 minor steps higher, never across a Major Realm, and tides a battle without winning it alone; limit break and striving, a priced burst defined in Part 3 Area 7.5). No math for a group, and no gap arithmetic in narration or dialogue: it lives in the spec and the gate only (Check #23 element 23-7). Every fight Area of a Chapter Spec carries an Engagement Ledger fixed before drafting. Gate 1 Check #23 FAILs a hard-rule break and reports a strained-but-lawful mismatch to the author as a ruling point. Parts 3 and 5 and a hero's Combat Level Advantage are unchanged.
- **Situational combat.** Part 45 (Situational Combat Mechanics Law, skill `cultivation-situational-combat-law`, Canon Amendment 2026-10-19) is a Tier 1 domain authority in the cultivation group beside Parts 3, 5 and 6. There is no order rule for moves: no move of a higher type must follow or be paired with a lower-type move in a scene, and anyone can use any move they have access to, at any point; effort and fatigue are the limit, not sequence. The situation chooses the move: a Situation Frame of fourteen readings (ground, space, posture of both sides, reach and height, size and anatomy, tempo, numbers, people to protect, light and weather, witnesses, hands and weapon, injury and energy, intent and style) and a Move Selection Test; the Seal (Part 42 Rule 42.3.4.2) and the link codes (eligibility only) are unchanged. Gate 1 **Check #24** (24-1 to 24-7 block, 24-8 reports) reads each move against its moment; every Chapter Spec fight carries a Situation line. Applies to future writing only, from Chapter 006.
- **Counts.** 24 Gate 1 checks; Parts 2 to 33 and 35 to 45 audited (each carries a skill, 43 skills in all (Part 45 registered, 2026-10-19));
  22 ledger folders; 19 in-scope orchestrator commands (the 17, plus `/create-chapter` and `/revise-chapter`, 2026-10-07); commands C-1 to C-43 with C-5, C-11 and C-12 vacant.

| File | Source | One-line purpose |
|---|---|---|
| `authority/guardrail-authority-tier-system.md` | This guardrail | Tier 0/1 ranking; Parts 28, 29, 36 and 39 and the plain-language guardrail all sit at Tier 0 (five distinct layers); Part 36 chooses the form for requirements of Parts 28, 29, 39 and the plain-words guardrail, nothing waived; Parts 40 to 42 are Tier 1 |
| `authority/guardrail-domain-ownership.md` | This guardrail | Exactly one Part governs each topic; no silent domain expansion |
| `authority/guardrail-locked-vs-negotiable-canon.md` | Part 28 Area 2 | What may never be improvised vs. what is free creative territory |
| `authority/guardrail-prohibited-creative-acts.md` | Part 28 Area 12 | The 7 absolute creative prohibitions + forbidden realm vocabulary |
| `authority/guardrail-consolidated-skill-reading.md` | One Skill Per Part | Each Part is exactly one skill named `<group>-<title>`, 42 in total, with no layer beneath them; the Part → skill table lives in this guardrail |
| `audit/guardrail-audit-gate-law.md` | This guardrail | The mandatory Two-Gate pipeline (**24**-check Gate 1; every Gate 1 also reviews the Area against the Area before it as one flow) every Area must pass through; Check #18(a) asks that the spec chain is in force; Check #12 reads named-item italics and the date line's form; Check #11 element 11-2 reads the date line against the calendar ledger; Gate 2 writes the Area files as a coupled pair and the calendar rows; the Whole-Chapter Gate 1 section (2026-10-07) runs the 24 checks over a whole-built Chapter, with the word-band check in place of Check #10 |
| `audit/guardrail-ccia.md` | This guardrail | Continuous Canon Integrity Audit — audits the governance system itself |
| `audit/guardrail-fcia.md` | This guardrail | Full Content Integrity Audit — audits narrative prose content |
| `audit/guardrail-alca.md` | This guardrail | Action-Law/Ledger Correctness Audit — audits operational correctness; the date line in each written Area file and the calendar ledger agree both ways, and each rollup row equals the rows beneath it |
| `audit/guardrail-forced-read-discipline.md` | This guardrail | The canon manifest must be physically re-read at 3 fixed checkpoints, never recalled from memory; also states the per-Area spec-read exception to the read-in-full rule |
| `ledger/guardrail-ledger-schema-law.md` | Part 37 | Ledger entity/index schemas are Part 37's authority; ledger beats prose on conflict; 22 ledger types, with Thresholds including M-1 to M-3 for monsters, D-1 for the calendar and O-6 for the Manual Ledger |
| `ledger/guardrail-ledger-update-law.md` | This guardrail | Pre-write ledger check and post-write ledger update are both mandatory, every time; named items, Named Moves, named documents and agreements, monsters and the calendar are entered at Gate 2; dated evolution entries (Part 43) are written at Gate 2 and the hero-ledger edit limit is lifted for them (2026-10-06) |
| `ledger/guardrail-session-log-not-canon.md` | This guardrail | `story-memory/session-log/` is a log only — never a valid decision input; the confirmed spec chain is a valid planning input |
| `ledger/guardrail-story-spec-law.md` | Part 38 | The spec chain, three kinds of spec (Section Spec, Novel-Part Spec, Chapter Spec), each built only while the one above it is confirmed: settling-power planning input, never established canon; ledger supersedes spec; the body reads clean and every settlement, open item, deferral and audit note is in the Audit and Settlement Notes section; Gate 1 Check #18 compares every planned element of the Chapter Spec and blocks on core ones |
| `commands/guardrail-command-law.md` | This guardrail | Bracket-command syntax, Two-Gate binding, confirmation tokens, the `[CANON AMENDMENT]` token; the full text of the Area is printed in chat before every confirmation; the confirmation tokens `[CONFIRM SPEC]` / `[REVISE SPEC]` / `[SKIP SPEC]` serve all three spec commands |
| `commands/guardrail-deprecated-commands.md` | This guardrail | Batch-writing commands are canon-deprecated, never reintroduce them; lists the Canon v10.0 command set (now including `/create-chapter` C-42 and `/revise-chapter` C-43, a new whole-Chapter rule, not a revival) |
| `commands/guardrail-plan-then-auto-execution.md` | This guardrail | Plan Mode → Auto Mode sequencing; Sonnet 5.5/max default model+effort with author-override persistence; mandatory parallel execution; milestone-based (never clock-based) agent progress reporting; in scope: 19 orchestrator commands, the three spec commands and `/create-chapter` and `/revise-chapter` included (the build-plan and staged-text stops are never waived); naming is never presented as a cost of an option |
| `tools/guardrail-authorized-scripts-only.md` | This guardrail | Only the 6 named `.claude/tools/*.py` scripts may ever run (the fifth, `manual_ledger_query.py`, is the read-only Part 42 Manual Ledger lookup and validator; the sixth, `chapter_builder.py`, writes the Chapter files, condensed or, since 2026-10-07, built whole); the date line is ordinary Area text handed to the same scripts |
| `quality/guardrail-tier0-narrative-quality.md` | Part 36 · Parts 28/29 | Novel-feel is Tier 0 authority (Gate 1 Checks #16 + #19; Check #16 spans twelve dimensions, including the Area flow review, Voice and Variety and the named dimension 16-DP); Part 36 chooses the form, nothing is waived; conflicts escalate, never resolve silently; the date line that opens every Area is not narration for Checks #16, #19 and #22 |
| `quality/guardrail-content-density-law.md` | Part 35 | CDL-2 density readings the Area Scorer reports for every Area and at each Section close; information only, never a pass or a fail; the date line is set aside and never scored |
| `quality/guardrail-entity-naming-law.md` | Part 28 Area 20 | Significant entities must be named at introduction; major-entity names author-consulted; Gate 1 Check #17; named items in italic with no leading article, registered at Gate 2 (Rule 20.8); named documents italic and agreements roman (Rule 20.8.7); naming is never weighed as a cost and the named version is the recommended default (Rule 20.9); monster names are roman; a Named Move's name is also read against the Move-Naming Law of Part 42 Rule 42.12.2.3 (Canon Amendment 2026-10-08) |
| `quality/guardrail-threshold-consultation.md` | This guardrail | Numbers are guide posts, not physics; a crossed line is computed and shown as information, never silently fixed, and is never a fail, a block or a question on its own |
| `quality/guardrail-behavioral-authenticity.md` | Part 39 | 36-Layer behavioral registry in Character Ledger §11/§12; no unregistered actor; distinctness is the author's call (overlaps permitted, no comparison derivations); Gate 1 Checks #20 + #21; a sentient monster is registered in full and a non-sentient monster's twelve traits are read in light form; Check #21 widened (2026-10-06) to every behaviour change, author rules heroes and Tier A, agent rules Tier B/C/D, immutables need the author, evolution is not drift, dated evolution entries per Part 43 (Character Evolution Law), no new command |
| `quality/guardrail-battle-plausibility.md` | Part 44 | Battle Plausibility: a whole engagement is checked from the levels (anchors, pairings in the bands Open, Shut and Barred, lawful offsets with a price, registered gifted fighters up to 3 minor steps, the Engagement Ledger in the Chapter Spec); Gate 1 **Check #23** FAILs a hard-rule break (23-1 to 23-5) and gap arithmetic in prose (23-7) and reports strain (23-6) to the author; limit break (offset f, Part 3 Area 7.5); Parts 3 and 5 and the hero's Combat Level Advantage unchanged |
| `quality/guardrail-situational-combat-selection.md` | Part 45 | Situational Combat Selection: no order rule for moves (any Usable move at any point; effort and fatigue are the limit, not sequence); the situation chooses the move (posture, ground and space, reach and anatomy, hands and weapons, light, protection, intent); the Situation line in the Chapter Spec Fight line; Gate 1 **Check #24** FAILs a move impossible or implausible for the posture, ground or body, a fixed ladder or move-name spam, a costly move with no cause or price, wrong-hands geometry and a broken protect or spare intent (24-1 to 24-7) and reports a poor fit (24-8); future writing only, from Chapter 006 |
| `quality/guardrail-plain-language.md` | Plain Language and Narrative Impact | Plain everyday words in narration AND dialogue; contractions are barred in both dialogue and narration (Part 29 Rule 29.2.1.1c, Canon Amendment 2026-10-16), and dialogue is natural and flowing in full connected sentences (Rules 29.2.1.7 and 29.2.1.7a); sentence rhythm deliberately unrestricted; plain words grounded in the world, no modern slang; colloquial register scales by relationship; impact and wonder reached for where the scene earns it and only there; sentence variety is guidance and is never counted; Gate 1 Check #22, with the plain vocabulary standard (2026-10-06): one word one meaning, picture over label, no jargon wall, blocking 22-3, 22-6 and the new vocabulary elements |

## Escalation rule (applies to every guardrail below)

No agent resolves a guardrail conflict on its own judgment. Every conflict — between two
guardrails, between a guardrail and a skill, or between a guardrail and a direct user
request — is surfaced explicitly rather than silently decided. Two routes exist, and which
one applies depends on where the conflict is found:

- **Mid-Area** (found while drafting, auditing, scoring or updating a ledger). The agent
  stops and reports the conflict to the orchestrating command, which asks the author with
  `AskUserQuestion`. No pipeline agent holds `AskUserQuestion` and none can start a slash
  command; an agent never treats that as licence to decide the conflict itself.
- **Between Areas, for structural doubt** (an overlap or gap between Parts, a guardrail and
  a skill that cannot both stand, drift across the written record). The orchestrating
  command runs `/run-canon-audit`. That command asks the author nothing before it runs; a
  finding that implies a structural change is reported for the author's decision, never
  auto-applied.

The standing principle: *a violation that is not detected is not thereby permitted.*
