# Eligibility Rules for Tier C and Tier D Characters (Part 42 Areas 11.5 and 11.6)

**Last Updated:** 2026-10-05
**Governed By:** Part 42 Rules 42.11.5.1 to 42.11.5.3, 42.11.6.1 to 42.11.6.4, Part 6 Area 7 (learning), Part 19 (Depth Spectrum).
**Status:** `[DERIVED]` plain-language restatement. Part 42 stands on any difference.

> **What this file is.** The one rule for people who write scenes. It lists no character and assigns no manual. A Tier C or Tier D character has no kit row, and the kit never lists one by default (check C-20). Tier A and Tier B side characters and the heroes are linked by ID in `character-kits.csv` instead.

## The rule in one paragraph

A Tier C or Tier D character may be shown holding or using a manual only if the character is **eligible** for that manual. Eligible means all eight tests below pass for that character and that manual. Eligible does not mean the character holds it (Rule 42.11.6.4): the scene decides which one manual, among those the character is eligible for, is shown. If a scene shows one, the Area writes the manual's name and moves, and Gate 2 registers the moves by Rule 42.12.5.1. A kit row for a Tier C or Tier D character is added only if the author asks for it (Rule 42.11.5.3). A scene that shows a manual the character is not eligible for is a finding at Gate 1 (eligibility is the informational test for institutional stock; it never limits who may learn, practise or train (anyone can learn, 2026-10-07)).

## What the scene writer needs before choosing a manual

1. The character's **realm** as the ledger or the Tier D registry code gives it (for the seven Soldiers of the Ninth the code reads `RLM-SENIOR-5-LOW`). A character whose realm is not recorded is **not eligible for any manual above Basic**, and a drafting agent stops and asks the author before showing one.
2. The character's **kingdom and institution** (Azure Sky or Gale; a soldier's order or company, a Wing, a sect, an academy), if any. The institution decides only which institutional stock the character may borrow or read; it never limits who may learn, practise or train (anyone can learn, 2026-10-07).
3. The character's **affinity and sovereignty**, if the ledger or code records any. A Tier D code such as `AFN-NONE` means none is recorded, and none is invented.

## The eight tests (Rule 42.11.6.1, in plain words)

| Test | Plain reading |
|---|---|
| E1 Realm | The character's effective realm is at or above the manual's `min_realm`. The institution sees the realm the character shows. |
| E2 Energy | The manual's `energy_req` is not higher than the character's access group can bear (Rule 42.11.6.3: groups of Mortal Tier 1 bear NONE; Senior to Ruler bear up to QI-MOD; Monarch bears QI-HIGH; Xiantian bears QI-EXT; Core and Divine bear QI-REAL). |
| E3 Cultivation | The realm meets the manual's state code (a Senior or higher character meets CIRC; MER-FULL needs Champion or higher), and each link code is met by moves the character already holds at Practiced or better: LINK-PRIOR needs an earlier manual of the same weapon, LINK-STEP and LINK-GUARD need a step or guard move from the kit. A Tier C or Tier D character has no kit, so LINK codes count as met only if the scene or the author has shown the earlier manual. |
| E4 Affinity | The affinity code (A2, A3 and so on) is not above the lower of the ledger's recorded ceiling and the realm cap (Level 1 in Mortal Tier 1; Level 3 in Mortal Tier 2; Level 5 at Xiantian). An unrecorded affinity meets only codes that read NONE. |
| E5 Sovereignty | SOV-C and the other sovereignty codes need a sovereignty that the ledger records. A character with none recorded meets only codes that read NONE. |
| E6 Access | Describes who may borrow or read the INSTITUTION'S copy, not who may learn the move (anyone can learn, 2026-10-07). The character can reach the institution that holds the manual and meets its access code: enrolment for ENROLLED, membership for MEMBER, rank for RANKED, a permit for PERMIT, nothing for OPEN. A SEALED manual has no standing access. A character who fails E6 may still learn the same moves by other routes (Rule 42.7.5.2). |
| E7 Learning | The manual teaches by Method L-1 or L-2, the character starts at Novice, a personal Signature is never on offer, and the jurisdiction does not forbid the move. |
| E8 Not already held | The character does not already hold the manual. |

## Kingdom access

A manual is reached through a kingdom row (`kingdoms/azorion.csv` for Azure Sky, `kingdoms/gale.csv` for Gale). A Common manual has a row in both kingdoms. An Azorion manual has an Azure Sky row only, and a Gale manual has a Gale row only. The kingdom of the character decides which row applies, and a character cannot use the other kingdom's row without a scene that shows how the manual crossed the border. A Brackenhold character reads `kingdoms/brackenhold.csv` (Canon Amendment 2026-10-08; Part 42 Rule 42.10.2.6): the four Brackenhold halberd manuals have a `BR-` row, and a Common manual may have one. The six firearm weapon types (PST MUS RIF SHG CAN GRN) have no Gale Advanced, Elite or Signature stock (Part 33 Area 3.3; ledger ruling 10 in `_index.md`).

## Worked examples

These use unnamed, invented roles to show the test. They are not assignments and bind no character.

**Example 1: a Senior-realm soldier of an Azure Sky order.** The soldier is Senior Level 5 Low, in the Azure Sky army, no affinity recorded. The Basic saber manual `MAN-BAS-SAB-012` needs Senior L1 Mid and CIRC, so E1 and E3 pass. Its Azure Sky row `AZ-BAS-SAB-012` is the Skysworn, MEMBER, so E6 passes for a soldier of that order and fails for a soldier of another order. Energy NONE to QI-MIN, E2 passes. Affinity and sovereignty read NONE, E4 and E5 pass. The soldier is eligible. A scene may show the soldier at saber drill.

**Example 2: the same soldier and an Advanced manual.** `MAN-ADV-STS-006` needs Champion L4 Mid. A Senior L5 Low soldier fails E1. Its affinity code is A2 and the soldier has none recorded, so E4 fails as well. The scene may not show it. Two failures are reported, not one.

**Example 3: a clerk or runner with a recorded Ruler realm but no martial role.** The realm would pass E1 for most Basic and Intermediate manuals. E6 fails for any institution's restricted copy: no order, academy enrolment or permit is recorded. A Tier C or D character with no institution reads OPEN institutional stock (the library rows) and may learn the same moves by other routes (Part 6 Area 7.1 L-1, L-2, L-3, a found manual, a teacher of any kind, practice) (anyone can learn, 2026-10-07). A scene may show a library text, and the Area states the reading is self-taught (Method L-2, Novice).

**Example 4: realm unrecorded.** The registry row gives no realm. E1 cannot be read, so the character is not eligible for anything above a Tier 1 Basic manual with `min_realm` T1 Unawakened, and the drafting agent stops and flags the realm to the author before showing any manual that needs more.

**Example 5: a Gale soldier.** A Gale soldier at Warrior realm is eligible to borrow or read the institution's copy of a Gale-row manual through the institution named in its row (the Wind-Sworn Militia, the Windward Host, an academy), and may learn the same moves by other routes (anyone can learn, 2026-10-07). For a firearm type the Gale stock stops at Common Basic and Common Intermediate, so a scene cannot show a Gale soldier with a Gale Advanced rifle manual.

**Example 6: a Signature manual.** A Signature manual is a School Move manual (Part 6 Area 7.2). A Warrior L1 Low character passes E1 for `MAN-SIG-STS-001`, but E6 needs RANKED standing to borrow or read the Windward Reach Academy's copy, E4 needs A2, and E7 forbids a personal Signature. An unranked Tier C or D character is not eligible for the academy's copy and may learn the moves by other routes (anyone can learn, 2026-10-07).

**Example 7: already held.** A character shown in one scene with a manual is not eligible for the same manual again (E8), so a later scene may show the character with a different manual or the same one only as the manual already held.

## Move names

A scene writes each move under the name the Manual Ledger holds, exactly as written (Rule 42.13.1.9). A name that a scene would coin for a move of its own follows the Move-Naming Law of Rule 42.12.2.3 (Canon Amendment 2026-10-08): one or two words, tied to the weapon type and to the level and grade of the move, never a place, a setting, a tactic or an enemy.

## What stays out of this file

No kit rows, no individual manual IDs for any character, no weapon pick for any character. If the author later asks for a Tier C or Tier D kit, the row goes into `character-kits.csv` by Rule 42.11.4.1, and a promotion to Tier A or Tier B adds the `characters.csv` row and kit rows (Rule 42.11.4.3).
