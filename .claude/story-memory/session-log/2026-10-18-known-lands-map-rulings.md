# Known-lands map rulings recorded in the ledgers (2026-10-18)

Not canon; an audit trail.

- Authority: the author's question walk-through of 2026-10-18 (map consultation) for an author reference map of the known lands of the Nine Suns Continent. Every ruling below is `[ASKED]`, provenance "Author ruling, 2026-10-18 (map consultation)". Only what was ruled was written; nothing was inferred; the cold river at Ashford, the stream at the lower ford, the stream at Greenhollow Cross and the two larger towns on its cart road stay unnamed; every SKETCH distance stays SKETCH.
- **No map file was kept.** Partway through the run the author's scope change dropped the map files, so no Map pointer block was written anywhere: the pointer block first written as §5.14 of `nine-suns-continent.md` was removed, and the sketch notes about the map in `azor-river.md` were taken out. The map's scope notes (known lands only, no continent figure, the northern region names, DIST-C1 and DIST-C2 staying SKETCH) are therefore not recorded in any ledger. Nothing was written under `projects/`, and no script was run or created.
- `ledger-worlds-location/_index.md` and `ledger-worlds-distance/_index.md` were handed to other agents by the coordinator and this lane did not edit them (see "Left for the index owners").

## The seven rulings (the author's option and words)

1. **The Ember Reach ridge and region** ("Ridge is the region's east edge"): "The low volcanic ridge with the Boundary Towers marks Azure Sky's border and is the eastern rim of the Ember Reach region, which stretches west from it toward the coast and Cindervast."
2. **Where the Windward Range runs** ("West to east along the north"): "One range running west to east along the north of both kingdoms. The Windward Pass cuts its southern flank north-north-east of Azorion; the Aerie Plateau is tucked under its eastern stretch; Gale's 'climb' is through the Stormbreak Foothills on the Range's southern side."
3. **The Lyraen's course and delta** ("South then south-east to a near delta"): "From headwaters in the Range it runs south as the Azure Sky to Gale border past the crossings and Greyspan, then south-east through the lowland basin to a delta about 200 km east of Farrowharbor. The Tide March coast and Saltmere share one southern shoreline on the Southern Sea."
4. **The sea the Tide March faces** ("The Southern Sea"): "The same water the Lyraen delta empties into, one continuous southern shoreline from Saltmarsh east to Saltmere and Ironshore."
5. **The north-west frontier cluster** ("North-west frontier"): "Hill and timber country north-west of the Sapphire Basin, beyond Ashford's cold-river crossing: Skyvein Forest on the slopes below the Range's western end, Greenhollow Cross at its edge, the lower road and Bluecleft Mine in the hills, and Brackenhold the kingdom across the ford to the north-west, where Azure Sky, Brackenhold and the Ember Reach polities meet."
6. **Highgale** (new MAJOR name): "The high city of the Gale, in the plain-English register of Stormbreak, Long Coast and Wind Crossing." The Gale capital city on the Aerie Plateau floor, about 12 km east-south-east of the Aerie Palace (DIST-011 stays SKETCH; the name is `[ASKED]`). Not yet on the page.
7. **The Azor** (new MAJOR name): "Azorion reads as the city on the Azor, the way many old cities carry their river's name. Short, fits the Azure Sky register." Course: "a river rising in the Windward Reach, running south through Millbrook and Azorion, then east or south-east to join the Lyraen"; the exact confluence is OPEN-AREA. Not yet named on the page.

## Naming checks (Part 28 Area 20.3), 2026-10-18

- **Highgale.** Case-insensitive search of `.claude/story-memory/` (`_archive` excluded), the written Chapters and Area files under `projects/`, and the rest of `.claude/` for "Highgale", "High Gale", "High-Gale", "Highgate" and one-word compounds beginning or ending in "gale": no place, person, faction, item, monster or move is named Highgale. Close echo only, reported to the author and unchanged: the Manual Ledger holds the two-word "High Gale" as the cultivation move `CMV-ELI-WND-003-11`, in three Signature manual titles (`MAN-SIG-KUK-011`, `MAN-SIG-TON-011`, `MAN-SIG-CLB-012`) and in move descriptions ("the high gale"); none is written in an Area. The second element is the kingdom's own name, by design. Register is the author's own; originality against published works is not cleared and is flagged for information.
- **The Azor.** Whole-word search of the same places: no standalone "Azor" anywhere. The only name that contains it is Azorion, by design (recorded in `azorion.md` Section 1 beside the author's earlier azure/hawk naming rationale, which is not amended). "Azor" also begins "Azor Ahai" in A Song of Ice and Fire; the river's name does not equal it; flagged for information, nothing changed.
- Both names are MAJOR entities chosen by the author; no agent changed either.

## Files created

`ledger-worlds-location/highgale.md` and `ledger-worlds-location/azor-river.md` (Part 37 Area 2.4 template, Sections 1 to 5, STUB lore, Collective Behavior Code stub; LF line endings because they were made with Write, as with `lower-road.md`).

## Files changed

| Folder | Files |
|---|---|
| `ledger-worlds-location/` | `ember-reach.md`, `windward-range.md`, `windward-pass.md`, `aerie-plateau.md`, `aerie-palace.md`, `gale-kingdom.md`, `lyraen-river.md`, `southern-sea.md`, `southern-march.md`, `farrowharbor.md`, `saltmarsh.md`, `skyvein-forest.md`, `greenhollow-cross.md`, `lower-road.md`, `bluecleft-mine.md`, `ashford.md`, `millbrook.md`, `azorion.md`, `azure-sky-kingdom.md`, `nine-suns-continent.md` |
| `ledger-worlds-kingdom-state/` | `cindervast.md`, `saltmere.md`, `ironshore.md`, `brackenhold.md`, `gale-kingdom.md`, `_index.md` (Brackenhold status; Last Updated of the five changed rows) |

Each carries `Last Updated` 2026-10-18 and, where the file has an Events Log, a row citing "Author ruling, 2026-10-18 (map consultation)".

## Left for the index owners (not edited here)

- `ledger-worlds-location/_index.md`: registry rows for Highgale and The Azor (and the Total Entries count); Parent and Status cells for Brackenhold, Skyvein Forest (Parent now `azure-sky-kingdom.md`), Greenhollow Cross and Bluecleft Mine; Last Updated of the changed rows; Lore Compliance rows for the two new files and for `lyraen-river.md` and `ember-reach.md` (a §5.1 was added to each, so STUB becomes PARTIAL).
- `ledger-worlds-distance/_index.md`: DIST-015 and the DIST-011 rename; the Registry B intro sentence (DIST-015 is an `[ASKED]` value, not a SKETCH); and four context cells that still say a ruled item stays OPEN-AUTHOR: DIST-004 (which river: now the Azor), DIST-005 (which border: now the north-western frontier; the cold river stays unnamed), DIST-008 and DIST-C2 (the sea faced: now the Southern Sea). All four rows stay SKETCH.

## Open after this update

- Whether the two edges of Skyvein Forest (behind Greenhollow Cross and along the lower road) are one stretch.
- Whether the author wants the Azor reading of Azorion and the earlier azure/hawk rationale to stand together (both are recorded as given).
- Which stretch of coast Saltmere holds against Saltmarsh and Farrowharbor, and the order of Saltmarsh and Farrowharbor (DIST-009 stays a sketch).
- Greyspan's open item about where on the Lyraen its bridge stands was not touched.
- Older Chapter Spec text (Chapters 002 and 003) and the frozen hero ledgers still carry "which border" wording as plan history; they were not edited.
