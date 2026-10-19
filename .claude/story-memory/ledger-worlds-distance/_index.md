# ledger-worlds-distance — Ledger Index

**Ledger Domain:** World Systems — Named Distance Reference Points and Spatial Landmarks
**Governed By:** `guardrails/ledger/guardrail-ledger-update-law.md`, Part 37 (Ledger Schema Law), Part 14 (Distance Law)
**Template:** Part 37 Area 3.2 — Schema Template: Distance Ledger
**Last Updated:** 2026-10-19
**Index Version:** v1.0
**Total Entries:** 21

> **Purpose:** This folder tracks named spatial entities that anchor the world's distance framework — the reference points and landmarks characters use to understand where they are and how far they need to travel. Two categories:
> - **Named Spatial Landmarks** — specific named cosmic, stellar, planetary, or terrestrial reference points that have been introduced in prose as canonical navigation or distance anchors. These are points in space that have been given names and described with enough canonical detail that they function as distance reference points. Example: "Named Landmark (Place A)" (a landmark cultivators use to gauge distance on the continent), "Named Marker (Place B)" (a visible marker used to find the way).
> - **Named Established Measurements** — canonical distance values that have been established in prose — specific journey times, stated distances between named locations, or spatial-scale benchmarks that define the texture of the world's geography. Example: "Place A to Place B is N km via the Named Road at Ruler-realm sustained speed." These are not routes (tracked in `ledger-worlds-travel`) — they are the specific distance facts that define the world's spatial reality.
>
> This ledger prevents spatial continuity errors where a journey is described as three days in one Area and six days in another, or where a landmark is placed inconsistently across scenes.

> **CMS Reference (Part 14 Area 2):**
> mm / cm / m / km / Mm (~1,000 km) / Gm (1,000,000 km) / AU (~150 million km) / light-second / light-minute / light-hour / light-day / light-week / light-year (ly) / kilolight-year (kly) / megalight-year (Mly) / gigalight-year (Gly) / Trans-universal

> **Update Protocol:** Per `guardrails/ledger/guardrail-ledger-update-law.md`:
> - **New Landmark File Trigger:** Any Area that names a spatial landmark and uses it as a reference point for distance, navigation, or location requires a new `[landmark-name].md` file at Gate 2.
> - **New Measurement File Trigger:** Any Area that establishes a canonical distance value between two named points requires a new entry in Registry B, and a `[location-a]-[location-b]-distance.md` file if the measurement is complex enough to warrant its own file.
> - **Update Trigger:** Landmark destroyed or moved; canonical distance revised by world event (terrain change, formation array range extension, new route established).

> **Mandatory Update Triggers:**
> - Named spatial landmark introduced as a navigation reference
> - Canonical distance between two named locations established in prose for the first time
> - Landmark destroyed or altered (joint update with `ledger-worlds-location`)
> - Formation Array effect radius stated for a named array (joint update with `ledger-worlds-travel`)
> - Soul sense range stated for a specific character at a specific location (joint update with character ledger)

> **Marker Legend:** These markers appear in the entries of this ledger. Open cells otherwise carry `OPEN-AREA` or `OPEN-AUTHOR` (Part 37 Area 5).
> - `[ASKED]`: the author chose this value.
> - `[DERIVED]`: the drafter inferred this value from cited evidence and the author reviewed it in the digest without overriding it (Part 39 Rule 39.3.3.1); it is pending only when the entry also says flagged for author confirmation.
> - `[AUTHOR-PENDING]`: a question about this value has been raised and is not yet answered.
> - `[MARKED SLOT]`: a slot left empty on purpose until the author rules.
> - "flag, do not invent": when a scene needs the value, the prose may establish one small fact at a time under Part 28 Area 17, logged in this ledger and offered to the author as a draft value at the next Section close. A name or a major entity (Part 28 Area 20.4) goes to the author first, through the Decision Consultation Gate.

---

## Registry A — Named Spatial Landmarks

| File | Landmark Name | Location Tier | CMS Scale | Type | Faction Control | Status | Last Updated |
|---|---|---|---|---|---|---|---|

*No entries yet. Files created as named spatial landmarks appear in prose.*

---

## Registry B — Established Distance Measurements

Every row here except the Long Coast anchor in DIST-013 (the direct distance of about 480 km, fixed by the author) and the direct distance in DIST-015 (its "about 200 km" is an author ruling of 2026-10-18 (map consultation), an [ASKED] value with "about") is a SKETCH value: a guide that does not bind a scene until the author or a scene fixes it.

| ID | From | To | CMS Distance | Context | Established In | Last Updated |
|---|---|---|---|---|---|---|
| DIST-001 | Azorion (palace platform) | Stonemill Crossing | N, about 7 km (road 7 km) | SKETCH. Road: 28 minutes at 15 km/h. On foot: under 2 hours. Basis: Stonemill Crossing lies within the half hour's ride of the Hammer-and-Hilt Gate, north on the Sapphire Road (`stonemill-crossing.md` Section 2). | Sketch table, author, pending first Area | 2026-10-01 |
| DIST-002 | Azorion (palace platform) | Twinpost | NNE, about 65 km direct (road about 70 km by the descent road through the Windward Reach, joining the Sapphire Road at Stonemill Crossing) | SKETCH. Road: 4 h 40 min at 15 km/h, which is the established single morning for a hard but sustainable ride that leaves before sunrise and arrives before the paired bells (`twinpost.md` Section 2, `azorion.md` Section 2). On foot: 2 days. | Sketch table, author, pending first Area | 2026-10-01 |
| DIST-003 | Twinpost | Windward Pass (middle of the combined corridor) | NNE, about 30 km direct (track about 40 km) | SKETCH. Mountain pass factor 0.3 (Part 15 Area 9.6; the Pass is a steep, narrow channel of bare stone, `windward-pass.md` Section 5.1): ridden at 15 km/h times 0.3 is 4.5 km/h, about 9 h; on foot at 4.5 km/h times 0.3 is about 1.35 km/h, about 4 days at 8 hours a day. Basis: the Twinpost stands at the Azure Sky-facing end of the corridor where it splits from the Windward Reach (`twinpost.md`, `windward-pass.md`). | Sketch table, author, pending first Area | 2026-10-01 |
| DIST-004 | Azorion (palace platform) | Millbrook | NNW, about 60 km direct (river road about 70 km) | SKETCH. Road: 4 h 40 min at 15 km/h. Down the river by barge to Azorion: about 6 h at 12 km/h. On foot: 2 days. The river is the Azor, by author ruling of 2026-10-18 (map consultation; `azor-river.md`, `millbrook.md` open item 1 resolved). | Sketch table, author, pending first Area | 2026-10-18 |
| DIST-005 | Azorion (palace platform) | Ashford | NW, about 210 km direct (road about 250 km) | SKETCH. Road: 16 h 40 min at 15 km/h (about two days at 8 hours a day). On foot: 7 days. The border is the north-western frontier with Brackenhold, by author ruling of 2026-10-18 (map consultation); which cold river stays OPEN-AUTHOR (`ashford.md` open item 1). | Sketch table, author, pending first Area | 2026-10-18 |
| DIST-006 | Azorion (palace platform) | Fallowfield | SW, about 120 km direct (road about 140 km) | SKETCH. Road: 9 h 20 min at 15 km/h (just over a day). On foot: 4 days. Place inside the kingdom is a sketch (`fallowfield.md` Section 2 fixes none). | Sketch table, author, pending first Area | 2026-10-01 |
| DIST-007 | Azorion (palace platform) | Greyspan | ESE, about 190 km direct (road about 220 km) | SKETCH. Road: 14 h 40 min at 15 km/h (about two days). On foot: 6 days. Greyspan stands at a bridge over the Lyraen with the far bank in Gale's sphere (`greyspan.md`); the stretch of river is OPEN-AREA (`greyspan.md` open item 1). | Sketch table, author, pending first Area | 2026-10-01 |
| DIST-008 | Azorion (palace platform) | Farrowharbor | S, about 450 km direct (road about 520 km) | SKETCH. Road: 34 h 40 min at 15 km/h (four to five days at 8 hours a day). Relay courier: about a day and a half at 300 to 500 km a day. On foot: 15 days. Sea faced: the Southern Sea, by author ruling of 2026-10-18 (map consultation). | Sketch table, author, pending first Area | 2026-10-18 |
| DIST-009 | Farrowharbor | Saltmarsh | W along the coast, about 70 km direct (coast road about 85 km) | SKETCH. Road: 5 h 40 min at 15 km/h. On foot: 2.5 days. Their order along the coast is a sketch (`saltmarsh.md` open item 1). | Sketch table, author, pending first Area | 2026-10-01 |
| DIST-010 | Azorion (palace platform) | Aerie Palace | ENE, about 255 km direct (road about 320 km: the Sapphire Road north past Stonemill Crossing, over the Lyraen at the crossings, up the Stormbreak Foothills to the Aerie Plateau) | SKETCH. Road: 21 h 20 min at 15 km/h (two to three days at 8 hours a day). On foot: 9 days. The Sapphire Road joins the two capitals (`gale-kingdom.md` Section 5.11). | Sketch table, author, pending first Area | 2026-10-01 |
| DIST-011 | Aerie Palace | Highgale (the Gale capital city) | ESE, about 12 km direct (road about 15 km) | SKETCH. Road: 1 hour at 15 km/h. On foot: 3 h 20 min. Basis: the palace is the royal seat on the Aerie Plateau and the capital city is Highgale, named by the author on 2026-10-18 (`highgale.md`). **Chapter 005 (Ref: 1.1.1.005, Area block 03) confirms the time and the bearing:** from the palace terrace "the road ran down to Highgale, an hour at a rider's pace to the east-south-east". The page gives the rider's pace in no figure, so the 12 km, 15 km and 15 km/h values stay SKETCH. | Sketch table, author; time and bearing confirmed by Chapter 005 (Ref: 1.1.1.005) | 2026-10-19 |
| DIST-012 | Aerie Palace | Long Coast | E, about 255 km direct (road about 320 km down through the Tempest Valleys) | SKETCH. Road: 21 h 20 min at 15 km/h (two to three days). On foot: 9 days. | Sketch table, author, pending first Area | 2026-10-01 |
| DIST-013 | Azorion (palace platform) | Long Coast | E, about 480 km direct | Anchor: the direct distance of about 480 km is fixed (written in km). The road length and the times are SKETCH. Road about 640 km by way of the Aerie Palace: 42 h 40 min at 15 km/h (five to six days at 8 hours a day). On foot: 18 days. | Author ruling 2026-10-01; route sketched | 2026-10-01 |
| DIST-014 | Twinpost | Aerie Palace | E, about 210 km direct (road about 260 km: the Gale road east to the Lyraen crossings, then up to the plateau) | SKETCH. Road: 17 h 20 min at 15 km/h (about two days). On foot: 7.5 days. This is the road the Gale half of the Ninth takes home (`twinpost.md`). | Sketch table, author, pending first Area | 2026-10-01 |
| DIST-015 | Farrowharbor | The Lyraen delta (Saltmere at the mouth, Ironshore on the east bank) | E along the coast, about 200 km direct | [ASKED] Author ruling, 2026-10-18 (map consultation): the Lyraen runs south then south-east through the lowland basin "to a delta about 200 km east of Farrowharbor", and the Tide March coast and Saltmere share one southern shoreline on the Southern Sea. Road length and times not set. | Author ruling 2026-10-18 | 2026-10-18 |
| DIST-016 | Stirrup Ford, on the Seam Road (where the Ridgewatch patrol found the Whistledeep caravan on 1247.1.11 / PD 11) | Aerie Palace | Not stated on the page (OPEN-AREA): no distance, no bearing and no speed | A journey time stated on the page, not a sketch: the lieutenant of the Ridgewatch detachment found the caravan on 1247.1.11 / PD 11 and rode to the palace herself, arriving "from the north road at first light" on 1247.1.14 / PD 14 "after three days in the saddle" (Area blocks 05 and 06, the king's words and the narration); weather had stopped the Kite Line at the plateau's north edge on the night of the find, so no word went ahead of her. The page does not say where the ride began (the Ridgewatch outpost stands at the foot of the Mule Stair, `seam-road.md`), what her pace was, or whether she changed horses. One rider, one journey; no standard speed is derived from it. | Chapter 005 — The House With No Walls (Ref: 1.1.1.005) | 2026-10-19 |
| DIST-S1 | (standard speed) | On foot | 4.5 km/h walking, 8 hours a day: about 35 km a day | SKETCH. Part 15 Area 9.1 (walking 4 to 5 km/h, 30 to 40 km a day). Used for every "On foot" figure above. | Part 15 | 2026-10-01 |
| DIST-S2 | (standard speed) | By road | 15 km/h carried (carriage or cart) on a kept road, 8 hours a day: 120 km a day. Ridden single horse: 50 to 80 km a day. Mountain pass: the road speed times 0.3 (Part 15 Area 9.6). Relay courier: 300 to 500 km a day. | SKETCH. Part 15 Areas 9.1, 9.2 and 9.6 (horse riding 10 to 15 km/h sustained, 50 to 80 km a day; carriage 15 to 25 km/h on a road, 100 to 200 km a day on a road network; courier relay 300 to 500 km a day; mountain pass factor 0.3); Part 32 Area 2.3 (Express Carriage, Relay Post Rider). Phase 1 travels at these Tier 2 rates (the Phase 1 Texture Note, `nine-suns-continent.md` Section 5.6). Used for every "Road" figure above. | Part 15, Part 32 | 2026-10-01 |
| DIST-S3 | (standard speed) | By airship | 150 km/h cruise: 3,900 km a day if flown day and night (26-hour day) | SKETCH. No airship class exists in Part 15 or Part 32. The airship is the Section 8 vessel (Part 30 Law P30-L7), one large exception to a Phase 1 where nothing with an engine flies (`nine-suns-continent.md` Section 5.6); it is not a routine mode, and its class and speed are OPEN-AUTHOR. 150 km/h is the low end of the Tier 3 air band (Part 15 Area 9.3, early aircraft 150 to 400 km/h; Part 32 Area 2.4, Light Airskimmer 150 to 500 km/h). Used only in the crossing table and the continent rows. | Sketch, author, pending a Part 32 class | 2026-10-01 |
| DIST-C1 | Western Reach coast | Long Coast (east coast) | E-W, about 6,000 km at the widest. Azorion is about 480 km from the east coast and about 5,500 km from the west coast. | SKETCH. Crossing: on foot 171 days, by road 50 days, by airship 40 h. Basis: Part 14 Area 3.3 sizes a full continent at 5 to 30 Mm, so the sketch is at least 5 Mm; the Long Coast anchor (DIST-013) fixes the east coast and the rest of the width lies beyond the Western Reach. Section 1 is a regional slice of the continent; "central-western" for Azorion means within the Section 1 region. On 2026-10-18 the author chose no continent figure (no continent outline and no size) for the known-lands map consultation; this row stays SKETCH and binds nothing. | Sketch table, author, pending first Area | 2026-10-18 |
| DIST-C2 | Southern coast shore (Azure Sky coast, on the Southern Sea by author ruling of 2026-10-18) | Northern Ice shore | N-S, about 8,000 km. Azorion is about 450 km from the south shore and about 7,550 km from the north shore. | SKETCH. Crossing: on foot 229 days, by road 67 days, by airship 53 h 20 min. Basis: Part 14 Area 3.3, as in DIST-C1. The belt north of the Windward Range is Phase 2 and later ground and stays OPEN-AUTHOR (Part 30 Law P30-L8). On 2026-10-18 the author chose no continent figure (no continent outline and no size) for the known-lands map consultation; this row stays SKETCH and binds nothing. | Sketch table, author, pending first Area | 2026-10-18 |

> **How the sketch is built.** North is the way the Azure Sky Palace platform faces the Windward Range; east is the Long Coast direction. Azorion is one point (the palace platform); the Hammer-and-Hilt Gate is inside the city and is not told apart from it at sketch precision. "Direct" is the straight line. "Road" is the length of the usual road or track; it runs longer than the direct line by about a tenth on open ground and by a quarter to a third in hills or mountains. Every ride time is the road length divided by the standard speed of its row. A travelling day is 8 hours of moving (of Saha's 26-hour day). SKETCH means the first Area that states the distance or time confirms the row or changes it, and the row is then updated and every file that quoted it is corrected. A SKETCH row guides a scene; it never stops one.

Standard crossing times at a glance (distance divided by the three standard speeds; use these for any pair the table does not list). Every figure in this table is a SKETCH value: a guide that does not bind a scene until the author or a scene fixes it.

| Distance | On foot (35 km/day) | By road (120 km/day) | By airship (150 km/h) |
|---|---|---|---|
| 10 km | 2 hours | 40 minutes | 4 minutes |
| 100 km | 3 days | 7 hours | 40 minutes |
| 250 km | 7 days | 2 days | 1 h 40 min |
| 500 km | 14 days | 4 days | 3 h 20 min |
| 1,000 km | 29 days | 8 days | 6 h 40 min |
| 2,000 km | 57 days | 17 days | 13 h 20 min |

---

## Part 28 Area 17 — Lore Section Schema (Distance Domain)

**Governing Law:** Part 28 Area 17 (Lore Creation Law). **Audit Hook:** ALCA dimension AL-10 (`guardrails/audit/guardrail-alca.md`).

**For Named Spatial Landmarks — Required Minimum Lore Fields:**

1. **Landmark Name** — canonical name as established in prose.
2. **Location** — Part 13 cosmological tier; precise placement in CMS terms relative to named reference points.
3. **CMS Scale** — what scale of distance this landmark anchors (km-scale for continental landmarks, AU-scale for system landmarks, etc.).
4. **Type** — formation array marker / natural feature / constructed waypoint / stellar body / dimensional anomaly.
5. **Navigation Function** — how characters use this landmark (visual bearing, soul-sense anchor, technology beacon).
6. **Visibility Profile** — who can perceive this landmark and at what range (Part 14 soul sense range tables; Part 8 Type 13 sensor range).
7. **Faction Association** — which faction controls or maintains this landmark, if any.
8. **Current Status** — intact / damaged / destroyed / relocated.

**For Established Distance Measurements — Required Lore Fields:**

1. **From / To** — named locations; cross-references to `ledger-worlds-location`.
2. **CMS Value** — the canonical distance in Part 14 CMS units.
3. **Measurement Context** — what type of path or space this distance measures (direct line / route / orbital arc / interstellar).
4. **Journey Time at Standard Speed** — at relevant Part 15 paradigm speeds for the cultivation realm and technology tier of the story's current phase.
5. **Establishing Source** — which Area first established this measurement.
6. **Confidence Level** — whether this is a precisely stated measurement or an approximate range.

**Depth Test:** "Can a scene's spatial geography be rendered consistently using only the reference points and measurements in this ledger?" If yes, depth is satisfied.

---

## Lore Section Compliance Registry

| File | Entry Name | Type | CMS Scale | Depth-Test Certification | Last Lore Update |
|---|---|---|---|---|---|

*No entries yet.*

---

