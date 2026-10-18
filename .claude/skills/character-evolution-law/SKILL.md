---
name: character-evolution-law
description: Governs how every recorded character changes over the story in the Starward Saga, the evolution layer on top of Part 39 and the character Parts. A person can change in everything a person can change (behaviour, fighting style, speech and prosody, morality and ideology, psychology and coping, relationships, routines), so nothing recorded about a character is permanently locked. Eight Areas cover the foundational principles; who rules (the author for heroes and for Tier A side characters, villains and monsters; the Gate 1 continuity-checker for Tier B, C and D, with a recorded reason; the author always for an immutable; Gate 2 presents every evolution); what can evolve (the 36 Behavioral Layers and 12 Signatures of Part 39 and the properties bound from Parts 16 to 20, 26, 27, 29 and 40); the dated Evolution Entry (ADD, CHANGE or RETIRE) and the rule that the current profile is the base profile plus the entries in order; detection inside the existing Gate 1 Check #21, Gate 2 and the send-back through /revise-area, with no new command; reset to a date the author names; the rule that a ruled evolution is not drift; a worked example (Varys, Area 1.1.1.001.04, medium sentences added, rolling default kept); and the cross-Part dependency table. Reach for this whenever a character's behaviour, voice, morals, fighting style or relationships are shown to have changed, a Check #21 question about a profile is raised or ruled, an evolution entry is written to a ledger, or the author asks to reset a character to an earlier date. This is canon Part 43, domain character, the single consolidated authority for the whole Part.
user-invocable: false
---

# Character Evolution Law

**Authority Tier:** 1 (Domain Authority — Character; see `.claude/guardrails/authority/guardrail-authority-tier-system.md`). Part 43 reads Part 39 (Tier 0) and does not override it: Part 39 owns the Layers, the Signatures, the Conditional Drift Map and Check #21; Part 43 owns the rule that a ruled change is an evolution, who rules it, and how it is recorded and reset.
**Domain:** Character — Evolution Governance: Foundational Principles of Evolution, Who Rules, What Can Evolve, the Evolution Entry and the Current Profile, Detection, Gates and Send-Back, Reset and the Drift Distinction, a Worked Example, and the Cross-Part Dependency Table
**Governing Canon Parts Cross-Reference:** Parts 16, 17, 18, 19, 20, 26, 27, 29, 37, 39, 40
**Added:** 2026-10-06 (author-approved policy; Part 43 is the next free Part number, Parts 2 to 42 existing and unchanged)

---

## Overview

Part 43 is the Starward Saga Canon's Character Evolution Law. The author's instruction is that characters are complex beings and can change in everything a person can change: behaviour, fighting style, the psychology of speech, morality, and everything a person feels that is recorded. Nobody is fixed at one date. Before this Part, a registered profile moved only through the Part 39 Conditional Drift Map and a Check #21 `[EVOLVE]` ruling, and hero ledgers were protected from edits that Part 43 now allows for evolution. Part 43 gives that movement one law: a ruled change is an **evolution**, it is written as a **dated Evolution Entry**, the original profile is never overwritten, and a reset to an earlier date always stays possible.

Part 43 adds no command. The author never runs an evolve command. Detection and questions happen inside the audit gates that already exist: the widened Gate 1 Check #21 (Part 39 Area 44) and the Gate 2 ledger update.

Across eight Areas, Part 43 defines: the principles (Area 1); who rules an evolution (Area 2); what can evolve (Area 3); the Evolution Entry and the current-profile rule (Area 4); detection, the two gates and the send-back (Area 5); reset by date and the line between evolution and drift (Area 6); a worked example (Area 7); and the cross-Part dependency table (Area 8). The ledger section that holds the entries is Section 14, Evolution Entries, of the character ledger schema (Part 37 Area 2.1, appended after Section 13, with no section renumbered).

---

## Area 1 — Foundational Principles of Evolution

### 1.1 — The Principles

**Rule 43.1.1.1 — P43-1: A Person Can Change in Everything Recorded.** Nothing recorded about a character is permanently locked. A character who has lived through a nine-year Phase may change in any dimension the canon records for a person (Area 3).

**Rule 43.1.1.2 — P43-2: The Base Profile Is Never Overwritten.** The profile registered when the character was entered is the base profile. It stays in its ledger sections as written. Every change is a dated Evolution Entry (Area 4). The current profile is the base profile plus the entries in order.

**Rule 43.1.1.3 — P43-3: A Reset Always Stays Possible.** Because the base is never overwritten, removing entries back to a date the author names returns the character to the state of that date (Area 6).

**Rule 43.1.1.4 — P43-4: Evolution Is Ruled, Not Assumed.** An evolution has a ruler, a reason and an Area where the story shows it (Area 2, Area 4). A change with none of these is not an evolution. It is unruled drift and stays under the existing drift rules (Area 6).

**Rule 43.1.1.5 — P43-5: Evolution May Add.** An evolution is not always a replacement. It may ADD a new element and leave the old one intact (the worked example, Area 7), CHANGE an element, or RETIRE one (Area 4).

**Rule 43.1.1.6 — P43-6: No New Command.** Detection and questions run inside the existing gates (Area 5). No `/character-evolve` or any other new command exists or may be created for this Part.

---

## Area 2 — Who Rules

### 2.1 — The Ruling Table

**Rule 43.2.1.1 — The Ruler by Character Class.**

| Character | Who rules an evolution | How |
|---|---|---|
| Hero (Part 17) | The author, always | The Gate 1 continuity-checker detects it and asks with `AskUserQuestion` (Part 39 Area 44.4); nothing changes in a ledger until the author rules `[EVOLVE]` |
| Tier A side character (Part 19), Tier A villain (Part 18), Tier A monster (Part 40) | The author | The same question and the same hold |
| Tier B, Tier C and Tier D side character, villain or monster | The Gate 1 continuity-checker | It decides at Gate 1 and records its decision and its reasons. No question is asked |
| Any immutable, any tier | The author, always | See Rule 43.2.1.2 |

**Rule 43.2.1.2 — Immutables Can Evolve, But Only the Author Rules It.** A trait registered as immutable (an `L31-IMMUTABLE` Signature, for example Varya's counting or Valia's held silence) can evolve. A change to an immutable needs the author's explicit ruling and a recorded reason, for every tier. An agent never changes an immutable on its own, even for a Tier B, C or D character; it asks.

**Rule 43.2.1.3 — Gate 2 Presents Every Evolution.** Whoever ruled, Gate 2 presents every evolution of the Area (all tiers) with its recorded information: what changed, the layer or dimension, the Area, who ruled, and the reason. The author sees what the checker ruled on Tier B, C and D characters and may send any of it back through `/revise-area` or ask for a reset (Area 6).

**Rule 43.2.1.4 — The Checker's Own Rulings Are Written Down.** Where the checker rules for a Tier B, C or D character, it writes the ruling as an Evolution Entry with `Ruled by: agent` and the reason. A ruling without a recorded reason is not valid and Gate 2 returns it.

**Rule 43.2.1.5 — Tier B to D Never Reaches an Immutable Silently.** If a Tier B, C or D change touches an immutable or a Signature the checker is unsure of, the checker treats it as an immutable and asks the author. A Tier D person holds no Layer register (Part 39 Area 4); an evolution of a Tier D code is a one-line replacement of the picked code, ruled by the checker, and the entry is still written.

---

## Area 3 — What Can Evolve

### 3.1 — The Evolvable Set

**Rule 43.3.1.1 — Everything Recorded About a Person.** The following can evolve, each under the law that owns it:

| Dimension | Owner | Examples |
|---|---|---|
| The 36 Behavioral Layers and 12 Signatures | Part 39 | A habit, a gesture, a decision style, a Signature |
| Fighting style and combat signature | Parts 17, 18, 19, 40; Part 6 for Named Moves | A new stance, a retired opening, a changed way of finishing |
| Speech and prosody | Part 29 | Sentence length, the working register, a retired phrase |
| Morality and ideology | Parts 20, 18, 19 | A shifted moral line, a changed orientation |
| Psychology and coping | Part 26 | A new coping habit, a retired one |
| Consequence habits and reputation conduct | Part 27 | How a person meets the cost of what they did |
| Relationships and routines | Parts 17, 18, 19, 39 L14 | How a person treats an ally, a daily habit |
| Monster behaviour traits | Part 40 | A changed territory habit |

**Rule 43.3.1.2 — The Owning Law Still Applies.** Evolution does not suspend the law that owns the dimension. A changed fighting style still obeys Part 5 and Part 6; a changed speech register still obeys Part 29; a moral change is still an ideology event under Part 20 where Part 20 says so. Evolution changes the record of the person. It never lets a character pass a Part 3 power barrier, a Part 17 survival rule, or a Phase ceiling.

**Rule 43.3.1.3 — Power, Facts and Events Are Not Evolution.** A realm advance, a wound, a death, an item gained and an event that happened are written by the existing ledger sections (2, 3, 10, 13), not as evolution. Evolution records how the person has changed, not what has happened to them. Where an event causes a change, the event is written in its own section and the change is written as an Evolution Entry that names it.

---

## Area 4 — The Evolution Entry and the Current Profile

### 4.1 — The Entry

**Rule 43.4.1.1 — The Fields of an Entry.** Every evolution is one dated entry in Section 14, Evolution Entries, of the character's ledger (Part 37 Area 2.1). An entry carries: the entry number (Evolution Entry 1, 2, and so on, per character, never reused); the date (the story date of the Area and the date it was ruled); the layer, dimension or code that changes; what it was; what it becomes; the kind of change (ADD, CHANGE or RETIRE); the Area (reference code) where the story shows it; who ruled (author or agent); and the reason.

**Rule 43.4.1.2 — The Three Kinds.** **ADD** puts a new element beside the existing one, which stays. **CHANGE** replaces the value of an element with a new one; the old value stays in the entry. **RETIRE** ends an element without replacing it; the old value stays in the entry.

**Rule 43.4.1.3 — Entries Are Append-Only.** An entry is never edited or deleted. A correction is a new entry that supersedes the earlier one and says so. A reset (Area 6) is the only act that removes entries.

### 4.2 — The Current Profile

**Rule 43.4.2.1 — Current Equals Base Plus Entries.** The current profile of a character is the base profile (Sections 1 to 9 and 11 as registered) plus the Evolution Entries in order. When an agent reads a character's current profile, it reads the base and applies the entries. Where the base and an entry disagree, the later entry governs the current profile and the base stays as the record.

**Rule 43.4.2.2 — Sections 11 and 12 Stay Honest.** Part 39 Section 11 (the registered profile) is the base for Layers and Signatures and is not edited by a Part 43 evolution; Section 12 stays the log of Part 39 drift events. Where a Check #21 `[EVOLVE]` ruling once edited Section 11 and moved the prior value to the Section 12 superseded table (Rule 39.44.4.2), a Part 43 ruling writes an Evolution Entry instead, which keeps the base whole. A Section 12 note may point to the entry.

**Rule 43.4.2.3 — Section Pointers.** The ledger line the evolution touches (for example the working speech register in Section 1) may carry a short pointer, "see Evolution Entry n", so a reader of that line finds the change. The pointer does not replace the line.

### 4.3 — The Hero Ledger Edit Lift

**Rule 43.4.3.1 — Evolution Entries May Be Written Into Hero Ledgers.** The earlier restriction on editing hero ledgers does not apply to Evolution Entries. The ledger update may write them into hero ledgers, and into every character ledger, once the author (or, for Tier B, C and D, the checker) has ruled. Every other hero-ledger protection stays: locked canon blocks, the survival rule, the Section 9 End-State blocks and the rest are unchanged, and an Evolution Entry may not rewrite them.

---

## Area 5 — Detection, Gates and Send-Back

### 5.1 — Detection in Gate 1

**Rule 43.5.1.1 — Check #21 Is Widened, Not Replaced.** Gate 1 Check #21 (Behavioral Change Detection, Part 39 Area 44) detects evolution for every character, not only for those with a full Layer register. Its four detection classes and its five response options stay (Part 39 Area 44.3, 44.4). Part 43 adds what a ruling does (Rule 43.5.2.1) and who rules (Area 2).

**Rule 43.5.1.2 — Heroes and Tier A.** For a hero or a Tier A character, the checker raises the question with `AskUserQuestion`, with its proposed ruling and the reason (Rule 39.44.4.1), opens with one plain sentence on what the Area did and what the profile says, and holds Gate 2 until the author rules.

**Rule 43.5.1.3 — Tier B, C and D.** For a Tier B, C or D character, the checker decides at Gate 1 whether the change is an evolution, records the decision and the reason, and passes it on to Gate 2. No question is asked, except under Rule 43.2.1.2.

### 5.2 — What Each Ruling Does

**Rule 43.5.2.1 — The Options.**

| Token | Effect under Part 43 |
|---|---|
| `[EVOLVE]` | An Evolution Entry is written at Gate 2 after `[CONFIRM WRITE]`. The base is not overwritten. A related Check #20 FAIL on the same line is cleared. The Conditional Drift Map is updated where a trigger was unmapped (Rule 39.44.4.2) |
| `[KEEP PROFILE]` | No entry. The prose is corrected to the current profile |
| `[REVISE AREA]` | The Area goes back through `/revise-area`. Nothing in the ledger changes until the revised Area is confirmed (Rule 43.5.3.1) |
| `[PROVISIONAL]` | A Part 39 Section 12 entry at Provisional grade with a reversion condition. No Evolution Entry, because the change is temporary |
| `[DEFER]` | The question carries to the next boundary review (Part 39 Area 44.4) |

### 5.3 — Gate 2 and Send-Back

**Rule 43.5.3.1 — Send-Back Goes Through the Existing Command.** If the author sends the Area back at Gate 1 (`[REVISE AREA]`), the Area goes through `/revise-area`, and no Evolution Entry is written and no ledger line changes until the revised Area is confirmed. If the revised Area still shows the change, Check #21 raises it again on the revised text.

**Rule 43.5.3.2 — Gate 2 Writes and Presents.** At Gate 2 the ledger update writes each ruled Evolution Entry into Section 14 of the character's ledger and presents every evolution of the Area, all tiers, with what changed, the layer, the Area, who ruled and the reason (Rule 43.2.1.3). A `[SKIP WRITE]` discards the ruling with the draft (Rule 39.44.4.2).

**Rule 43.5.3.3 — Section-Close Rulings.** A ruling made at a `/next-section` boundary review, where no Gate 2 exists, is written at once by a continuity-checker ledger instance, as Rule 39.44.4.2 provides.

---

## Area 6 — Reset and the Drift Distinction

### 6.1 — Reset by Date

**Rule 43.6.1.1 — A Reset Removes Entries Back to a Date.** The author may ask for a reset. The author names a date; every Evolution Entry made after that date for that character is removed from Section 14, and the current profile is the base plus the entries that remain. The removed entries are kept in a one-line note at the head of Section 14 (date of reset, entries removed) so the history of the reset is not lost. A reset is the only act that removes entries, and only the author may order it.

**Rule 43.6.1.2 — A Reset Does Not Rewrite the Prose.** A reset changes the record. Prose already written stands. If the author wants prose changed, that goes through `/revise-area`.

### 6.2 — Evolution Is Not Drift

**Rule 43.6.2.1 — A Ruled Evolution Does Not Count as Drift.** An author-ruled evolution (and a checker-ruled one for Tier B, C and D) does not count against a character's Drift Count (Part 39 Rule 39.35.1.3) and does not trip the drift guardrails. It is recorded as an evolution, in Section 14.

**Rule 43.6.2.2 — Unruled Drift Stays Drift.** A change with no ruling, no reason and no Area is unruled drift. The existing drift rules of Part 39 (Check #20 element 20-2, the Drift Count, the Conditional Drift Map) apply to it unchanged.

---

## Area 7 — Worked Example

### 7.1 — Varys, Area 1.1.1.001.04

**The case.** Varys's registered working speech (Section 1, element 1, the default register, "the working, aloud") is longer, rolling sentences with the verdict arriving last. At Area 1.1.1.001.04, the first Area in which he gives a finding aloud, his one speech ran in medium-length sentences, the reasoning first and the verdict near the end. Check #21 raised the held enquiry.

**The ruling.** On 2026-10-06 the author ruled `[EVOLVE]`: **ADD** medium sentences to his working speech, the rolling default kept intact. Ruled by the author, as Part 17 requires for a hero. No Section 11 value was replaced and no drift was counted (Rule 43.6.2.1).

**The entry.** The Gate 2 agent recorded this ruling in `.claude/story-memory/ledger-character-hero/varys.md` (Section 1, element 1, the ruling bullet, the Section 11.6 note on author-ruled evolutions, and the Section 12 note). Part 43 adopts it as **Varys, Evolution Entry 1**: date 2026-10-06; dimension, Section 1 element 1, the working speech (Part 29 prosody, with Part 39 `B39-L10-TURN-10` and `B39-L15-ANNOUNCE-99` unchanged); kind ADD; from "longer, rolling sentences, verdict last" to "longer, rolling sentences stay the default, and medium sentences are also part of the register"; Area 1.1.1.001.04; ruled by the author; reason, the speech showed the same chain of reasoning and verdict in medium sentences and the author ruled it a real part of the register. The existing ledger text is not edited by Part 43; when `varys.md` is next touched at Gate 2, Section 14 points to that text as Evolution Entry 1 (a pointer, no text lost).

**Reading the current profile.** Base (rolling default) plus Evolution Entry 1 (medium sentences also lawful). A reset to a date before 2026-10-06 returns him to the rolling default alone.

---

## Area 8 — Part 43 Cross-Part Dependency Master Table

The following table applies to every Area of Part 43. It is stated once here.

| Dependency Row | Relationship | Governance Rule |
|---|---|---|
| Gate audit (FCIA/ALCA) | Audit governance | `guardrails/audit/guardrail-audit-gate-law.md` governs Gate 1 and Gate 2. Gate 1 detects and rules (Area 5), Gate 2 writes and presents every evolution (Rule 43.5.3.2). |
| Ledger update | Write governance | `guardrails/ledger/` (the ledger-update guardrail) allows Evolution Entries in hero ledgers (Rule 43.4.3.1); other hero-ledger protections stay. |
| Canon-Part 16 | Part 43 reads Part 16 | Classification and the beings that are characters. |
| Canon-Part 17 | Part 43 reads Part 17 | Heroes: the author rules; the hero protections that stay. |
| Canon-Part 18 | Part 43 reads Part 18 | Villain tiers A to D decide who rules. |
| Canon-Part 19 | Part 43 reads Part 19 | Side character tiers A to D decide who rules. |
| Canon-Part 20 | Part 43 reads Part 20 | Morality and ideology can evolve; Part 20 events still apply. |
| Canon-Part 26 | Part 43 reads Part 26 | Psychology and coping can evolve. |
| Canon-Part 27 | Part 43 reads Part 27 | Consequence conduct can evolve; consequence events stay Part 27's. |
| Canon-Part 29 | Part 43 reads Part 29 | Speech and prosody can evolve under the Part 29 rules. |
| Canon-Part 37 | Part 43 → Part 37 | Section 14, Evolution Entries, is added to the character ledger schema. |
| Canon-Part 39 | Part 43 ↔ Part 39 | Check #21 (Area 44) is widened and points here; the Layers, Signatures, Drift Map and Drift Count stay Part 39's. |
| Canon-Part 40 | Part 43 reads Part 40 | Monster tiers A to D decide who rules; the monster behaviour traits can evolve. |

## Appendix A — Cross-References (Applies to All 8 Areas)

| Related Skill | Relation | Source |
|---|---|---|
| `character-behavioral-synthesis-law` §Areas 4, 41, 42, 44 | HARD | Part 39: registration, Sections 11 and 12, the Drift Map, Check #21 |
| `character-hero-law` §Areas 1, 2 | HARD | Part 17: heroes, growth and the protections that stay |
| `character-villain-law` §Area 6 | HARD | Part 18: villain depth tiers |
| `character-side-character-law` §Area 2 | HARD | Part 19: the Depth Spectrum, Tier A to D |
| `character-monster-law` §Area 6 | HARD | Part 40: monster depth tiers |
| `character-ideology-law`, `character-psychological-law`, `character-consequence-law` | SOFT | Parts 20, 26, 27: the dimensions that can evolve |
| `ledger-schema-law` §Area 2.1 | HARD | Part 37: Section 14, Evolution Entries |

## Appendix B — Governing Authority

> Subordinate to the guardrail grounding in `.claude/guardrails/_index.md` (audit gate law: `guardrails/audit/guardrail-audit-gate-law.md`). Conflicts are never resolved silently — escalate via `/run-canon-audit`.
