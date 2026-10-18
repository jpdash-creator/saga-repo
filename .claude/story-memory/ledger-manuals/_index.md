# ledger-manuals — Ledger Index (Part 42 Manual Ledger)

**Ledger Domain:** Cultivation and Weapon Style: Manuals, the Named Moves they carry, the weapon types they teach, and who holds them
**Governed By:** Part 42 (Manual and Weapon Style Law, `skills/manual-and-weapon-style-law/SKILL.md`), Part 6 (Move Taxonomy Law, Areas 2 to 7 and 9), Part 33 (Weapon Law), Part 37 (Ledger Schema Law), `guardrails/ledger/guardrail-ledger-update-law.md`, `guardrails/tools/guardrail-authorized-scripts-only.md` (script 5 reads this ledger)
**Last Updated:** 2026-10-08 (Move-Naming Law recorded, ruling 13)
**Index Version:** 1.0 (design record; generation in progress)

> **Purpose.** One database-style ledger of every manual and every manual-borne Named Move, queried by ID and not by searching text. The author's directive of 2026-10-05: manuals graded Basic to Mythic; every weapon type in the weapon list; Azorion and Gale stocks; personal manuals in a personal file per person; every hero and every Tier A and Tier B side character linked by ID; "instead of using AI for grepping too much we will use IDs, like a database query."
>
> **Where this file stands.** Part 42 owns the rules. This file is the working design record and the folder map. Where it and Part 42 differ, Part 42 stands and the difference is a finding at the next ALCA pass.

## Author rulings recorded here (2026-10-05)

1. **Known but Latent.** Part 6 Area 4.1 (Access Table) is not amended. A character may hold a manual of any grade. Each move in it is **Usable** for that character (the effective realm allows that move type) or **Latent** (learned in form and theory, not executable yet). The manual is a growth track.
2. **School Signature versus Personal Signature.** Signature, Fusion, Catastrophic and Mythic type moves inside an institutional manual are School Moves (Part 6 Area 7.2), owned by the school and teachable. A hero's personal Signature stays identity-bound (Part 6 Rule 9.1, scope amended, purpose kept).
3. **Aalia learned from the Gale academies,** not the Azorion library.
4. **Full depth.** Every manual is named and every manual has its full move roster, in the ledger. Kingdom IDs point at generic IDs. Personal manuals live in one personal file pair per individual.
5. **Seal.** Hercules and Bison are under the Olympus Suppression Seal. Signature and Catastrophic are blocked by the seal. Elite is also Latent (the effective realm gives it no access). Basic, Intermediate and Advanced stay Usable.
6. **Olympus manuals** are personal files with origin Olympus. The origin stays in ledger fields only (Olympus rule in the Hercules and Bison ledgers).
7. **Hero weapon types** are picked by the drafter and marked DERIVED for the author to override.
8. **Tier A and Tier B** side characters get concrete manual IDs (DERIVED, flagged). **Tier C and Tier D** get the eligibility rule only (`eligibility-rules.md`).
10. **Gale firearms reduced** (author, 2026-10-05; Gale is Tier 2 and issues no firearms, Part 33 Area 3.3). For the six firearm types PST MUS RIF SHG CAN GRN: Gale has Common Basic and Common Intermediate manuals only. There are no Gale-origin Advanced, Elite or Signature manuals, and no Gale kingdom row for Common Advanced; Gale NNN numbers are simply not used there. Azorion keeps its full stock. `[DERIVED]` reading of "reduce Gale's firearm counts", flagged for the author to adjust.
11. **Housekeeping approved:** `ledger-manuals/` is the 22nd ledger folder (Threshold O-6); the name `found/` and `FND-` IDs are reserved; `reset_story.py` is to be changed so a reset restores the CSV `first_area` cells (edit of an authorized script, no new script). The skill folder keeps the name `manual-and-weapon-style-law`. The requirement ladders in Part 42 Area 6 are approved as drafted. Personal file stems are the lowercase character code (`personal/vrs-manuals.csv`).
12. **Brackenhold joins the register (Canon Amendment 2026-10-08).** The author authorized (2026-10-08, in chat) the origin `Brackenhold`, the kingdom ID prefix `BR-`, the file `kingdoms/brackenhold.csv`, and new halberd manuals up to Signature (no Fusion, Catastrophic or Mythic): `MAN-INT-HAL-011`, `MAN-INT-HAL-012`, `MAN-ADV-HAL-014`, `MAN-SIG-HAL-013`, with 30 moves, numbered as extras after Gale. Taken at the recommended defaults: one Signature manual for Brackenhold (the six-Signature pattern is waived), counts taken by the extras rule (`weapons.csv` unchanged), the neutral register, institution cells `OPEN-AUTHOR` until the Redhaft Vanguard is ledgered, and no character or kit row until a character file exists. Elite and Advanced stay latent and unshown for Warriors. Part 42 Rule 42.10.2.6 holds the rule text.
9. **One read-only tool,** `.claude/tools/manual_ledger_query.py` (script 5), looks up and validates by ID. It never writes.
13. **Move-Naming Law (Canon Amendment 2026-10-08).** The author ruled in chat on 2026-10-08, after the Chapter 003 draft review, that a move name is tied to the weapon type and to the level and grade of the move and never to the situation in which it is called: one or two words (at most 5 percent of a manual's moves at three words; Catastrophic and Mythic may use three words but are still mostly two), impact rising with the grade, generic and weapon-based up to Mortal Tier 2 Senior level and generic, weapon-anchored, cultivation-anchored or combined from Warrior level upward, a name that fits the move's function, and never a place, a setting, a tactic or an enemy. Part 42 Rule 42.12.2.3 holds the rule text. A read-only survey of 2026-10-08 found 39,990 moves (39,866 generic and 124 personal) with names of: one word, 6; two words, 4,253; three words, 25,529; four words, 8,497; five or more, 1,581 (whitespace count). The stock predates the law and stands until the author orders a rename pass; a replaced name is kept in the `notes` cell of the move's manual row, because the moves files have no `notes` cell. `validate` reads no length and is unchanged. One name written in prose is grandfathered: `Open Guard Reading Cut` (`PER-VRS-01-01`, Chapter 001).

14. **Cultivation axis (Canon Amendment 2026-10-16).** The author directed (chat, 2026-10-16, point 8) a second axis for cultivation-based manuals and moves beside weapons: 65 disciplines (50 affinities, 11 soul types, Body Path, Qi Path, Heart, Formation), usable from Warrior and above, all eight grades, counts scaled by prominence, columns as the weapon files plus `affinity_id`. Design: `_design-cultivation-axis.md`; law: Part 42 Area 16. Folder `cultivation/`; not generated yet (design only); the weapon axis below is unchanged.

## Folder map

```
ledger-manuals/
  _index.md                       this design record
  weapons.csv                     the 79 weapon types, their codes and manual counts
  manuals/<grade>/<WPN>.csv       generic manual definitions, one file per grade per weapon
  moves/<grade>/<WPN>.csv         the moves of those manuals, same split
  kingdoms/azorion.csv            Azorion kingdom IDs -> generic manual IDs, institution, channel, access
  kingdoms/gale.csv               Gale kingdom IDs -> generic manual IDs, institution, channel, access
  kingdoms/brackenhold.csv        Brackenhold kingdom IDs -> generic manual IDs (BR- rows; 13 today)
  personal/<char>-manuals.csv     a person's own manuals (mentor, master, archive, found), one pair per individual
  personal/<char>-moves.csv       the moves of those manuals
  characters.csv                  realm snapshot, seal, weapons for every linked character
  character-kits.csv              which manual each linked character holds, from which source
  eligibility-rules.md            the rule for Tier C and Tier D characters
```

`<grade>` is one of `basic, intermediate, advanced, elite, signature, fusion, catastrophic, mythic`. Fusion, Catastrophic and Mythic generic folders hold only a header row for now (the author's kingdom stock stops at Signature). Catastrophic manuals exist today only as personal manuals.

`<WPN>` is the three-letter code in `weapons.csv`. An ID names its own file: `MAN-ADV-STS-005` is in `manuals/advanced/STS.csv`, and its moves `MV-ADV-STS-005-07` are in `moves/advanced/STS.csv`.

## ID scheme

| Thing | ID | Example |
|---|---|---|
| Generic manual | `MAN-{GRD}-{WPN}-{NNN}` | `MAN-ADV-STS-005` |
| Move | `MV-{GRD}-{WPN}-{NNN}-{SS}` (SS = 01.. in manual order) | `MV-ADV-STS-005-07` |
| Azorion manual | `AZ-{GRD}-{WPN}-{NNN}` (same GRD, WPN, NNN as the generic row it points at) | `AZ-ADV-STS-005` |
| Gale manual | `GA-{GRD}-{WPN}-{NNN}` | `GA-ADV-STS-005` |
| Brackenhold manual | `BR-{GRD}-{WPN}-{NNN}` (Canon Amendment 2026-10-08) | `BR-SIG-HAL-013` |
| Personal manual | `PER-{CHR}-{NN}` | `PER-VRS-01` |
| Personal move | `PER-{CHR}-{NN}-{SS}` | `PER-VRS-01-07` |

`{GRD}` = `BAS INT ADV ELI SIG FUS CAT MYT`. Character codes: `VRS` Varys, `VLA` Valia, `AER` Aeries, `AAL` Aalia, `HRC` Hercules, `BSN` Bison, `VRY` Varya, `AEG` Aegon; side characters get a three-letter code in `characters.csv`.

**Numbering of `{NNN}` inside one grade and weapon:** Common first, then Azorion, then Gale, then Brackenhold extras (Canon Amendment 2026-10-08) (halberd today: Intermediate 011 and 012, Advanced 014, Signature 013).
- Basic and Intermediate: all Common, `001` upward.
- Advanced: Common `001` to `adv_common_n`, then the Azorion ones (`adv_kingdom_n` of them), then the Gale ones (`adv_kingdom_n`).
- Elite: Azorion `001` to `elite_n`, Gale `elite_n+1` to `2*elite_n`.
- Signature: Azorion `001` to `006`, Gale `007` to `012`. Inside each kingdom's six: the first four are Mortal Tier 2 manuals (minimum realms rise from Warrior to Ruler Level 1 Mid; none above Ruler Level 1 Mid), the fifth is Xiantian, the sixth is Core.

Kingdom rows: a Common manual has an Azorion row and a Gale row (and may have a Brackenhold row); an Azorion manual has an Azorion row; a Gale manual has a Gale row; a Brackenhold manual has a Brackenhold row.

## Canonical headers (Part 42 may refine; Part 42 stands on a difference)

- `weapons.csv`: `weapon_id,family,name,description,prominence,basic_n,inter_n,adv_n,adv_common_n,adv_kingdom_n,elite_n,sig_n`
- `manuals/<grade>/<WPN>.csv`: `manual_id,grade,weapon_id,origin,title,realm_band,min_realm,energy_req,cultivation_req,affinity_req,sovereignty_req,move_count,composition,tradition,summary,status,first_area,notes`
- `moves/<grade>/<WPN>.csv`: `move_id,manual_id,seq,name,move_type,function,form,cost_class,unlock_realm,description,status,first_area`
- `kingdoms/*.csv`: `kingdom_id,manual_id,kingdom,institution,channel,access,copy_control,local_note,status`
- `personal/<char>-manuals.csv`: the manuals header with `owner,source` added before `status`
- `personal/<char>-moves.csv`: the moves header
- `characters.csv`: `char_id,name,ledger_file,tier,kingdom,realm,effective_realm,blocked_types,affinity,sovereignty,primary_weapons,snapshot_date`
- `character-kits.csv`: `char_id,manual_id,kingdom_manual_id,source,learned_via,mastery,assign_status,note`

Values: `origin` is `Common`, `Azorion`, `Gale`, `Brackenhold`, `Personal` or `Olympus`. `realm_band` is `M1 M2 XT CF DV` (Mortal Tier 1, Mortal Tier 2, Xiantian, Core, Divine). `move_type` is `Basic Intermediate Advanced Elite Signature Fusion Catastrophic Mythic`. `status` is `Active Dormant Lost Superseded`. `first_area` reads `Not yet established` until an Area writes the name. `assign_status` is `ASKED` or `DERIVED`. CSV cells hold plain text with no bold or italic marks; prose adds them (manual title italic, move name bold-italic).

## Composition and move counts

The composition table (moves per type by grade and manual size N = 5 to 15) is fixed in Part 42. A manual's `composition` cell is written as in that table (`B6 I2`). Move counts by grade for generated manuals: Basic 5 to 8, Intermediate 6 to 10, Advanced 8 to 12, Elite 9 to 13, Signature 10 to 12, Fusion 10 to 14, Catastrophic 13 to 15, Mythic 12 to 15. Moves are listed in manual order, lowest type first.

## Names

- Every move name is unique across the whole ledger (all CSVs, all kingdoms, personal files). A manual title is unique too.
- Common manuals and moves use a neutral register. Azorion manuals and moves use the Azorion register: dual-track, paired, twin-court, hawk and azure, basin and river. Gale manuals and moves use the Gale register: wind-sworn, plateau, oath, bearing, no walls.
- Move names follow the Move-Naming Law of Part 42 Rule 42.12.2.3 (Canon Amendment 2026-10-08): one or two words (three only as the rule allows, never four or more), specific to the weapon type, tied to the level and grade of the move, fitted to its function, and never a place, a setting, a tactic or an enemy. The Part 6 Rule 6.2 patterns (Principle + Action, Natural Force + Form, Scale or Number + Effect, State + Consequence) are illustrations of how a name can be built and set no length. Names in the stock made before 2026-10-08 stand until a rename pass. No name may equal a proper name from a widely known published work. No contemporary-Earth anachronism.
- Do not name any new institution, person, place or relic. Institutions come from the existing ledgers (listed in Part 42); where none exists the cell reads `OPEN-AUTHOR` plus a role word.

## Generation protocol (workers)

1. Read this file, Part 42 (`SKILL.md`), `weapons.csv`, and the two kingdom ledgers for register and tech tier (`ledger-worlds-kingdom-state/azure-sky-kingdom.md`, `gale-kingdom.md`).
2. Own one weapon (or a short list). Write only your own files: `manuals/<grade>/<WPN>.csv` and `moves/<grade>/<WPN>.csv` for the grades basic, intermediate, advanced, elite, signature, and `.claude/temp/manual-staging/<WPN>-kingdoms.csv` (kingdom rows, headerless, merged later by the orchestrator).
3. Row counts must equal `weapons.csv`. Numbering as above. Composition and move counts as Part 42 fixes them. Every move row must carry the correct `move_type` count for its manual.
4. CSV rules: UTF-8, comma separated, double-quote any cell with a comma, no line breaks inside a cell, header row first. Descriptions are one sentence, 8 to 24 words, naming the physical action and what it does, without invented lore.
5. Do not write to any other path. Do not create scripts. Report only counts and any rule conflict.
6. A worker that writes or replaces a move name (new rows, or a rename pass the author orders) follows Part 42 Rule 42.12.2.3. A replaced name is kept in the `notes` cell of the move's manual row as `renamed <move_id> from "<old name>" <YYYY-MM-DD>`. Run `validate` and a name lookup for every new name before reporting.

## Marker legend

`[ASKED]` the author chose it. `[DERIVED]` the drafter inferred it and the author has not yet reviewed it. `OPEN-AUTHOR` a value only the author can set.
