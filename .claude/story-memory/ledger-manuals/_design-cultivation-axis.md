# Design: the Cultivation Axis of the Manual Ledger (Canon Amendment 2026-10-16)

**Status:** DESIGN ONLY. No manual or move row exists yet. Authority: author directive 2026-10-16 point 8 (cultivation-based moves from Warrior and above, a separate axis beside weapons, "same shape as weapons, scaled by affinity prominence", all eight grades, full ledger build before any chapter rewrite). The law text is Part 42 Area 16 (`skills/manual-and-weapon-style-law/SKILL.md`), Part 37 Area 3.12 (`skills/ledger-schema-law/SKILL.md`) and `guardrails/ledger/guardrail-ledger-schema-law.md`. Where this file and Part 42 Area 16 differ, Part 42 stands.
**Markers:** `[ASKED]` the author said it. `[DERIVED]` the drafter inferred it; the author may override. Items marked OPEN are listed at the end.

## 1. What the axis is

A cultivation manual teaches one **discipline**: an affinity, a soul type, or another cultivation category. Its moves are cultivation-based (qi, affinity-resonant force, soul force, heart-state), not weapon-based. `[ASKED]` The weapon axis is untouched: weapons.csv, manuals/, moves/, kingdoms/, personal/, characters.csv and character-kits.csv keep their headers and counts.

**Eligibility floor `[ASKED]`:** a cultivation-axis move is usable from Mortal Tier 2 Warrior (Warrior L1 Low) and above. No cultivation manual has an M1 band, and no `min_realm` is below `Warrior L1 Low`. The Part 6 Access Table still decides which move types a realm may use (an Elite move is still Latent for a Warrior); the floor is added on top of it.

## 2. The disciplines (65)

Source: Part 4 Area 1.3 (50 affinities in seven domains, the "Soul (as Affinity)" entry included), Part 4 Area 2.3 (11 soul types), Fusion Law Area 3.1 (cultivation paths: qi, body, soul), Part 4 Area 3 (Cultivation Heart), Part 6 Area 12 (S-7 formation-mediated), Part 6 Area 3.9 (Trap:Formation). `[DERIVED]` for the four "other" disciplines.

Left out on purpose (not transmissible by manual, Part 6 Area 12): Bloodline-Resonance S-2 and Species-Innate S-3 (non-transmissible), Relic-Channeled S-4 and Weapon-Bonded S-5 (belong to the relic or the weapon axis), Technology-Aided S-6 (Part 31). Fusion moves are not a discipline: they sit in the `FUS` grade of the primary affinity and name both streams (section 7).

Prominence classes `[DERIVED]`: **Prominent** (common in the world and the story), **Standard**, **Niche**, **Rare** (a fourth class the weapon axis does not have; used for Transcendent, taboo and abstract disciplines).

| Code | Discipline | Domain | Class | Req kind |
|---|---|---|---|---|
| EAR | Earth | Primordial | Prominent | A |
| FIR | Fire | Primordial | Prominent | A |
| WAT | Water | Primordial | Prominent | A |
| WND | Wind | Primordial | Prominent | A |
| THN | Thunder/Lightning | Primordial | Prominent | A |
| MTL | Metal | Primordial | Prominent | A |
| WOD | Wood/Nature | Primordial | Prominent | A |
| SWD | Swords (affinity) | Primordial | Prominent | A |
| STR | Strength | Primordial | Prominent | A |
| ICE | Ice/Frost | Primordial | Standard | A |
| PSN | Poison | Primordial | Standard | A |
| SND | Sand/Dust | Primordial | Standard | A |
| SVB | Sound/Vibration | Primordial | Standard | A |
| CRY | Crystal | Primordial | Niche | A |
| MGM | Magma/Lava | Primordial | Niche | A |
| LGT | Light | Cosmic | Standard | A |
| DRK | Darkness | Cosmic | Standard | A |
| SUN | Sun | Cosmic | Standard | A |
| SPC | Space | Cosmic | Standard | A |
| GRV | Gravity | Cosmic | Niche | A |
| CEL | Celestial/Star | Cosmic | Niche | A |
| MOO | Moon | Cosmic | Niche | A |
| TIM | Time | Cosmic | Rare | A |
| LIF | Life | Life Force | Prominent | A |
| DTH | Death | Life Force | Standard | A |
| BLD | Blood | Life Force | Standard | A |
| BON | Bone | Life Force | Niche | A |
| SLA | Soul (as Affinity) | Life Force | Niche | A |
| RNC | Reincarnation | Life Force | Rare | A |
| STM | Storm | Natural Phenomena | Standard | A |
| MST | Mist/Fog | Natural Phenomena | Niche | A |
| ILL | Illusion | Metaphysical | Standard | A |
| WIL | Will | Metaphysical | Standard | A |
| CHS | Chaos | Metaphysical | Standard | A |
| ORD | Order | Metaphysical | Standard | A |
| DRM | Dream | Metaphysical | Niche | A |
| MEM | Memory | Metaphysical | Niche | A |
| TAO | Tao | Metaphysical | Rare | A |
| FAT | Fate | Metaphysical | Rare | A |
| KRM | Karma | Metaphysical | Rare | A |
| TRU | Truth | Metaphysical | Rare | A |
| VOD | Void/Nothingness | Metaphysical | Rare | A |
| HEA | Healing | Healing/Support | Prominent | A |
| PRT | Protection | Healing/Support | Prominent | A |
| SEA | Sealing | Healing/Support | Standard | A |
| BND | Binding | Healing/Support | Standard | A |
| CRE | Creation | Transcendent | Rare | A |
| DST | Destruction | Transcendent | Rare | A |
| INF | Infinity | Transcendent | Rare | A |
| BAL | Balance/Harmony | Transcendent | Rare | A |
| SOW | Weapon Soul | Soul type | Standard | SR |
| SOD | Defense Soul | Soul type | Standard | SR |
| SOS | Sense Soul | Soul type | Standard | SR |
| SOH | Healing Soul | Soul type | Standard | SR |
| SOT | Trap Soul | Soul type | Niche | SR |
| SOC | Convert Soul | Soul type | Niche | SR |
| SOP | Phantom Soul | Soul type | Niche | SR |
| SOB | Bind Soul | Soul type | Niche | SR |
| SOR | Resonate Soul | Soul type | Niche | SR |
| SON | Nullify Soul | Soul type | Niche | SR |
| SOV | Devour Soul (taboo, Part 4 Area 2.3) | Soul type | Rare | SR |
| BDY | Body Path | Path | Prominent | NONE |
| QIP | Qi Path (affinity-free qi) | Path | Prominent | NONE |
| HRT | Cultivation Heart | Heart | Standard | HL |
| FRM | Formation Casting (S-7) | Formation | Niche | NONE |

Totals: 14 Prominent, 22 Standard, 17 Niche, 12 Rare = 65. Domain tally: 15 + 8 + 6 + 2 + 11 + 4 + 4 = 50 affinities; 11 soul types; 4 others.

Healing, Death and Chaos (the author's named examples) are HEA Prominent, DTH Standard, CHS Standard. `[DERIVED]`

## 3. Folder layout `[ASKED]` (inside `ledger-manuals/`, new subfolder so weapon file stems never collide)

```
ledger-manuals/cultivation/
  affinities.csv                         the 65 disciplines, class, counts (the weapons.csv analogue)
  manuals/<grade>/<AFF>.csv              e.g. manuals/basic/HEA.csv
  moves/<grade>/<AFF>.csv                e.g. moves/basic/HEA.csv
  kingdoms/azorion.csv, gale.csv         kingdom rows (Brackenhold: none unless the author orders)
  personal/<chr>-manuals.csv, -moves.csv a person's own cultivation manuals (one pair per individual)
  kits.csv                               who holds which cultivation manual
  characters-ext.csv                     soul rung, soul types, heart level, healer flag per character
```
`<grade>` is the same eight folders. `<AFF>` is the code of section 2.

## 4. IDs `[DERIVED]`

| Thing | ID | Example |
|---|---|---|
| Cultivation manual | `CMAN-{GRD}-{AFF}-{NNN}` | `CMAN-BAS-HEA-003` |
| Cultivation move | `CMV-{GRD}-{AFF}-{NNN}-{SS}` | `CMV-BAS-HEA-003-02` |
| Azorion row | `CAZ-{GRD}-{AFF}-{NNN}` | `CAZ-ADV-FIR-005` |
| Gale row | `CGA-{GRD}-{AFF}-{NNN}` | `CGA-ADV-FIR-005` |
| Personal manual / move | `PCM-{CHR}-{NN}` / `PCM-{CHR}-{NN}-{SS}` | `PCM-VLA-01-04` |

`{GRD}` as before (`BAS INT ADV ELI SIG FUS CAT MYT`). The `C` prefix keeps the cultivation IDs distinct from the weapon IDs, so one ID names its own file and axis at a glance. Numbering inside one grade and discipline: Common first, then Azorion, then Gale (Basic, Intermediate, Fusion, Catastrophic, Mythic are all Common). Signature: Azorion `001..sig_n`, Gale `sig_n+1..2*sig_n`. Elite: Azorion `1..elite_n`, Gale after. Advanced: Common, then Azorion, then Gale, as for weapons.

## 5. Schema `[ASKED]`: identical to weapons, plus `affinity_id`

- `affinities.csv`: `affinity_id,domain,name,description,prominence,basic_n,inter_n,adv_n,adv_common_n,adv_kingdom_n,elite_n,sig_n,fus_n,cat_n,myt_n,req_kind,support_role`
- `manuals/<grade>/<AFF>.csv`: the weapon manuals header with `weapon_id` replaced by `affinity_id` in the same position: `manual_id,grade,affinity_id,origin,title,realm_band,min_realm,energy_req,cultivation_req,affinity_req,sovereignty_req,move_count,composition,tradition,summary,status,first_area,notes`
- `moves/<grade>/<AFF>.csv`: the weapon moves header with `affinity_id` inserted after `manual_id`: `move_id,manual_id,affinity_id,seq,name,move_type,function,form,cost_class,unlock_realm,description,status,first_area`
- `kingdoms/*.csv`, `personal/*`: the weapon headers with the same substitution.
- `kits.csv`: `char_id,manual_id,kingdom_manual_id,source,learned_via,mastery,assign_status,note`
- `characters-ext.csv`: `char_id,soul_rung,soul_types,heart_level,healer`
- Everything else (grades, composition table, move-count ranges, rounding rule, `move_type` set, `form`, `cost_class`, `unlock_realm`, status, `first_area`) is the weapon axis unchanged. Part 42 Rules 42.2.2.2 and 42.2.3.2 apply to this axis verbatim.

### Requirement cells (eligibility)

`affinity_req` is the discipline-requirement cell, read by `req_kind`:
- **A** (affinities): `A2..A7`, never `NONE` (the manual teaches that affinity). Capped by band: M2 up to A3, XT up to A5, CF up to A6 (A7 at Core Solidification), DV up to A7 (Part 4 Area 1.4, Rule 42.6.4.2). A recorded level is a ceiling; the eligibility test reads the lower of ceiling and realm cap (Rule 42.11.6.2). A weapon-aligned `W` suffix is not used on this axis.
- **SR** (soul types): `SR1..SR12` (Soul Wisp to Eternal Soul, Part 4 Area 2.2; the rung's realm equivalent is the cap).
- **HL** (Heart): `HL1..HL5` (Ember to Sovereign, Part 4 Area 3.3).
- **NONE** (BDY, QIP, FRM): no discipline gate; the energy and cultivation cells still apply.

`energy_req`, `cultivation_req`, `sovereignty_req`: the ladders and per-grade defaults of Part 42 Area 6, with the M1 rows removed. `cultivation_req` starts at `CIRC` or `MER-PART` (Warrior reads the circulation and partial-meridian states).

### `min_realm` windows `[DERIVED]`

| Grade | Band | Window |
|---|---|---|
| BAS | M2 | Warrior L1 Low to Warrior L9 Peak |
| INT | M2 | Warrior L1 Low to Champion L9 Peak |
| ADV | M2 / XT | Champion L1 Low to Ruler L9 Peak / Demigod L1 Low to Void God L9 Peak |
| ELI | XT (and one Monarch-gated M2 Rare per discipline per kingdom) | as the weapon axis |
| SIG | M2 / XT / CF | Warrior L1 Low to Ruler L1 Mid / Demigod to Void God / Core Formation to Core Assimilation |
| FUS | XT / CF | as the weapon axis |
| CAT | XT / CF / DV | as the weapon axis |
| MYT | CF / DV | as the weapon axis |

Signature layout per kingdom by `sig_n`: 5 = 3 M2, 1 XT, 1 CF; 4 = 2 M2, 1 XT, 1 CF; 3 = 1 M2, 1 XT, 1 CF; 2 = 1 XT, 1 CF (the M2 minimums non-decreasing in number order).

**Soul-type disciplines (SR kind)** `[DERIVED, OPEN-1]`: Part 4 Area 2.2 puts Soul Rung 1 at Demigod. So SOW SOD SOS SOH SOT SOC SOP SOB SON SOR SOV start in the XT band (Demigod L1 Low): Basic and Intermediate in XT from Demigod, Advanced XT, Signature XT and CF, and no M2 band, except one **Early Awakening** Basic manual per soul type at Monarch L1 Low to Monarch L9 Peak (Part 4 Area 2.4; Access Table "early-awakened soul, Monarch"). This is the one place the Warrior floor of section 1 is not reachable, because the soul ladder starts higher. The author may instead rule that soul types open at Warrior.
**Heart (HL)**: Ember Heart is not realm-gated in Part 4 Area 3.2, so HRT may open at Warrior; the HL cap by realm is read from Part 4 Area 3.4 at generation.

## 6. Counts per class, same shape as weapons `[DERIVED]`

Weapon shape: Basic, Intermediate, Common plus kingdom Advanced, Elite and Signature per kingdom. Cultivation adds the three high grades, which the author asked for ("all eight grades for affinities"); they are Common-origin (no kingdom stock) with no kingdom row unless the author orders one.

| Class | BAS | INT | ADV (common + per kingdom) | ELI per kingdom | SIG per kingdom | FUS | CAT | MYT | Manuals | Moves (est.) |
|---|---|---|---|---|---|---|---|---|---|---|
| Prominent | 10 | 8 | 7 (4 + 3) | 6 | 5 | 4 | 3 | 2 | 59 | 588 |
| Standard | 8 | 7 | 6 (3 + 3) | 5 | 4 | 3 | 2 | 1 | 48 | 474 |
| Niche | 6 | 5 | 4 (2 + 2) | 4 | 3 | 2 | 1 | 1 | 35 | 345 |
| Rare | 4 | 4 | 4 (2 + 2) | 3 | 2 | 2 | 2 | 2 | 30 | 307 |

Manuals per discipline = BAS + INT + adv_common + 2*adv_kingdom + 2*ELI + 2*SIG + FUS + CAT + MYT. Move counts use the Part 42 ranges (Basic 5-8, Intermediate 6-10, Advanced 8-12, Elite 9-13, Signature 10-12, Fusion 10-14, Catastrophic 13-15, Mythic 12-15), so the move figures are estimates.

**Totals:** 14 x 59 + 22 x 48 + 17 x 35 + 12 x 30 = **2,837 manuals** and about **28,200 moves** (the weapon axis holds 4,442 manuals and about 40,000 moves).

## 7. Functions, healing and the Support family `[ASKED, wording DERIVED]`

Part 6 Area 3.7 has Support:Heal, Support:Empower, Support:Sense. This amendment adds two, so the first-class set is **Heal, Revive, Sense, Empower, Cleanse**:
- **Support:Revive**: bring back a person at the edge of death (stopped breath, cut-off pulse, a stunned or collapsed soul) inside a short window; never returns the dead after that window, and every use is a Part 27 consequence event (CSS). Grade floor Advanced; Catastrophic and Mythic reach the widest windows.
- **Support:Cleanse**: remove poison, taint, curse, a binding, Qi Deviation backlash or soul erosion. Grade floor Intermediate.
- Heal from Basic; Empower and Sense from Basic (soul-form with the `Soul-` prefix, e.g. `Soul-Support:Heal`).
A healing move is aimed at an ally or the self; the description says who is restored. A healer uses a Heal, Revive or Cleanse move from a healing source: HEA, LIF, SOH (primary), or the secondary sources below. A healing move is never given an attack name (Rule 42.12.2.3(e)).

`support_role` in `affinities.csv`:
- **Primary** (at least half of the discipline's moves are Support; at least 30 percent Heal, Revive or Cleanse for the healing ones): HEA, LIF, SOH; Sense: SOS; Empower: SOR.
- **Secondary** (at least 15 percent Support moves in the discipline): PRT, WAT, WOD, SUN, LGT, BLD, RNC, DTH (Cleanse only), TIM (restore), CRE, BAL, WIL (Empower), ORD (Empower), STR (Empower), HRT (Empower), SPC and TRU (Sense), WND and SVB (Sense), QIP, BDY (Heal of the body).
- **Minor** (no quota): all others. A non-healing discipline may still carry a thematic Support move where one fits.

## 8. Move-Naming Law on this axis (Rule 42.12.2.3 applies unchanged, plus the notes below)

One or two words; three words only up to about 5 percent. Because every cultivation manual is Warrior or above, names are affinity-anchored, cultivation-anchored or combined (never the weapon-based Senior-and-below register). The name is tied to the **affinity (or soul type, path) and to the grade**, never to a situation, place, tactic or enemy. Impact rises with the grade (Basic and Intermediate simplest; Advanced and Elite more impactful; Signature and Fusion highly impactful; Catastrophic and Mythic the highest). The name fits the function (a heal is not named like an attack).
- **Share of three-word names** `[DERIVED]`: read per (grade, discipline) file, not per manual, because a cultivation manual holds 5 to 15 moves and per-manual rounding down would leave Basic to Signature with no three-word name at all. At most 5 percent of the moves of one (grade, discipline) file, rounded down, carry three words; Fusion, Catastrophic and Mythic files may use three but stay mostly two.
- Uniqueness is across both axes (about 68,000 names in all). Each worker works in one discipline vocabulary (the discipline's own force words) and runs `find-name` before reporting.
- A manual title is unique across both axes.

## 9. Fusion moves

A Fusion-type move sits in the FUS grade of the primary affinity file and starts its description `streams: <X> + <Y>`, X being the file's discipline and Y a partner from the Fusion Law Area 2.3 pairing table (or a path or soul pairing under Fusion Law Area 3). Pairs must be ones the Fusion Law allows; the validator reads `streams:` form only, the pair table is read by the worker.

## 10. Kits, characters and usability

`kits.csv` links characters to cultivation manuals as the weapon kit file does. `characters-ext.csv` records soul rung, soul types, heart level and a `healer` flag. A move is **Usable** for a character when the effective realm is at or above Warrior L1 Low, the realm allows the move type (Access Table), and the character holds the discipline's affinity at the level in `affinity_req` (lower of ceiling and realm cap), or the soul rung or heart level; otherwise **Latent** (known in form, not executable). A character with no affinity holds BDY, QIP and FRM manuals only. The Seal Rule (blocked types, effective realm) applies as on the weapon axis. Hero and Tier A and B kit rows are written later (DERIVED, flagged), not by this build.

## 11. Validator changes: `.claude/tools/manual_ledger_query.py` (specification; the tool stays read-only)

Do not edit the tool until the author approves; then:
1. New constants: `AXIS_DIR = "cultivation"`, header constants `H_CAFF`, `H_CMANUALS`, `H_CMOVES`, `H_CKINGDOM`, `H_CPERSONAL`, `H_CKITS`, `H_CCHARS`; regexes `RE_CMAN`, `RE_CMV`, `RE_CKING` (`CAZ|CGA`), `RE_PCM`, `RE_PCMMV`; `AFF_CODES` (65); `FUNCTIONS["Support"]` extended with `Revive` and `Cleanse`; `SR_CODES`, `HL_CODES`; the cultivation windows; the Soul-type Early Awakening exception.
2. `parse_id` returns the axis; `manual ID`, `moves ID`, `find-name`, `stats` accept both axes. New `affinity CODE` command (the `affinities.csv` row, its expected and present counts by grade). `--axis weapon|cultivation|both` (default both).
3. New checks: **C-23** cultivation headers and format (C-1/C-14 analogue); **C-24** row counts per discipline and grade against `affinities.csv` including `fus_n`, `cat_n`, `myt_n`; numbering and origin order (C-3/C-4 analogue); **C-25** floor: every `min_realm` at or above `Warrior L1 Low`, band valid, window valid (cultivation windows; Early Awakening exception); **C-26** `affinity_req` form by `req_kind` and the band cap; **C-27** composition, move counts and move rows (reuse C-6, C-7, C-8 with the cultivation IDs); **C-28** move fields including the extended function set and the grade floors (Revive from Advanced, Cleanse from Intermediate); **C-29** Support quota by `support_role` (primary at least 50 percent Support, secondary at least 15 percent, counted per discipline across its manuals; INFO below target, FAIL below half the target); **C-30** Move-Naming Law: FAIL on a name of four or more words, FAIL if the three-word share of a (grade, discipline) file exceeds 5 percent rounded down (Basic to Signature) or if more than half of a Fusion, Catastrophic or Mythic file's names are three words; **C-31** cross-axis uniqueness (C-13 across both axes).
4. `usable CHARACTER` reads `kits.csv` and `characters-ext.csv` and applies section 10.
5. The summary line prints both axes. The tool never writes; workers write the CSV content by hand (no script generates ledger content).

Weapon-axis checks C-1 to C-22 and the existing 80-line `weapons.csv` stay unchanged and green.

## 12. Work-unit split: 40 units (about 700 moves each)

Weights are estimated moves. Each worker owns the files `manuals/<grade>/<AFF>.csv` and `moves/<grade>/<AFF>.csv` of its disciplines for all eight grades and writes kingdom rows to `.claude/temp/cultivation-staging/<AFF>-kingdoms.csv` (merged later). U40 also builds `affinities.csv` and, after all units report, the merge and validate step.

| Units | Disciplines | Manuals each | Moves each |
|---|---|---|---|
| U01-U14 (one Prominent each) | EAR, FIR, WAT, WND, THN, MTL, WOD, SWD, STR, LIF, HEA, PRT, BDY, QIP | 59 | 588 |
| U15 ICE+TIM, U16 PSN+RNC, U17 SND+TAO, U18 SVB+FAT, U19 LGT+KRM, U20 DRK+TRU, U21 SUN+VOD, U22 SPC+CRE, U23 DTH+DST, U24 BLD+INF, U25 STM+BAL, U26 ILL+SOV | a Standard + a Rare | 78 | 781 |
| U27 WIL+CRY, U28 CHS+MGM, U29 ORD+GRV, U30 SEA+CEL, U31 BND+MOO, U32 SOW+BON, U33 SOD+SLA, U34 SOS+MST, U35 SOH+DRM, U36 HRT+MEM | a Standard + a Niche | 83 | 818 |
| U37 SOT+SOC, U38 SOP+SOB, U39 SOR+SON | two Niche | 70 | 689 |
| U40 FRM (+ affinities.csv, merge) | one Niche | 35 | 345 |

Total 40 units, 2,837 manuals, about 28,200 moves. Healing-source units (U11 HEA, U10 LIF, U35 SOH) and Sense/Empower primaries (U34 SOS, U39 SOR with SON) must honour section 7.

## 13. Open questions for the author

- OPEN-1: soul types open at Demigod (Part 4 Area 2.2, recommended) or at Warrior?
- OPEN-2: counts of section 6 (recommended) or heavier (the weapon Prominent 12/10/9/8/6)?
- OPEN-3: Fusion, Catastrophic and Mythic are Common-origin with no kingdom rows (recommended)?
- OPEN-4: the four "other" disciplines (Body Path, Qi Path, Heart, Formation) are in (recommended) or only the affinities and soul types?
- OPEN-5: three-word share read per (grade, discipline) file (recommended) or per manual?
- OPEN-6: Revive and Cleanse as new Support functions (recommended).
