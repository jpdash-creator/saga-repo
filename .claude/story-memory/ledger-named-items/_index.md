# ledger-named-items — Ledger Index

**Ledger Domain:** Named Items (every made or used thing that the story gives a proper name of its own, of every Type, relics and artifacts included).
**Governed By:** `guardrails/ledger/guardrail-ledger-update-law.md`, Part 37 (Ledger Schema Law), Part 28 (Novel Creative Flexibility Law, Area 20 Rule 20.8)
**Template:** Part 37 Area 3.8 — Schema Template: Named-Item Register
**Last Updated:** 2026-10-21
**Index Version:** 10.0
**Total Entries:** 7

> **Purpose:** This folder is the register of every named item in the Starward Saga: each made or used thing that the story gives a proper name of its own, such as an apparatus, a piece of gear, a remedy, a system, a food, a drink, a garment or a relic. Anything that is an item gets registered here (the author: "anything that is an item gets registered here"). It exists so that an item named in one Area is written the same way in every later Area and every spec, can be found by name, and is never named twice. It is a register of names with pointers. It is not a second home for what an item is or does: where an item already has an entry in another ledger, that entry owns every descriptive fact and this register holds only the name, the Type and the first Area.
>
> **Why the names are in italic:** by author directive, every named item is set in italic at every mention in the prose and in every spec file, and in roman inside a passage that is already italic (Part 28 Rule 20.8.2). The Entity Name cell of this register is written in that italic form. **The article is never part of the name** (the author: "Never part of the name"): the cell holds the name without it, and the prose writes the article in plain type, `the *Name*`, and `The *Name*` at the start of a sentence. **Emphasis guard:** Part 28 Rule 20.8.2(f).

> **Manual titles (Part 42).** A manual title is a named item of Type `other item`. It is registered by its ID in the Manual Ledger (`ledger-manuals/`), and a pointer row is written here when the title is first written in prose, at the Gate 2 of that Area (Part 42 Rule 42.12.4.4). The row's Entity File is the CSV file of the Manual Ledger that holds the manual, and its cell names the `manual_id`; the row holds no value of the manual, and the Manual Ledger owns it (Part 28 Rule 20.8.4). The manuals' titles are not listed row by row here before they are written.

> **Where the author's directive and the rule live:** the author's words are quoted in Part 28 Rule 20.8.1 and Part 37 Area 3.8. This index states the scope and the schema for the people who keep the register. Part 28 Rule 20.8.1 is the definition and stands on any difference with this index.

> **Scope — what is a named item.** A named item is a made or used thing that the story gives a proper name of its own. The plain test: a character could hold it, carry it, wear it, eat or drink it, apply it, read it, ride or sail it, or run it, and the story calls it by that name. Anything that is an item gets registered here, whatever its kind. Its **Type** is one of the fourteen below (Part 28 Rule 20.8.1), and `other item` is the catch-all, so that no named item is left without a Type:
>
> | Type | What it covers | Home entry, when the item has one |
> |---|---|---|
> | apparatus or device | an apparatus, instrument, mechanism or invention, made and worked by hand or by power | `ledger-technology-scale` when it is a technology system at tier level |
> | remedy | a salve, tonic, draught, poultice or any other made preparation used to heal or ease | none |
> | gear or tool | a tool, a piece of kit, a pack, a harness or any other gear | none |
> | weapon | a named weapon | `ledger-technology-weapon` (Threshold O-2) |
> | system or service | a thing that is run, such as a signal line, and never the body that runs it | `ledger-technology-scale` |
> | material | a named made or worked substance (an alloy, a cloth, a dye, a paste); not the substance states and grades of Part 11, which are category terms | none |
> | food | a named dish, loaf, ration or any other thing eaten | none |
> | drink | a named brew, wine, tea or any other thing drunk | none |
> | dress or adornment | a named garment, cloak, robe, uniform, ornament, jewel or any other thing worn | none |
> | vessel or vehicle | a named boat, ship, cart, flightcraft or any other carrier | `ledger-technology-vehicle` (Threshold O-3) when it has an entry there; the row stays the whole record when it has none |
> | relic or artifact | a Named Relic or Named Artifact (Part 12) | `ledger-energy-relics-artifacts` (Threshold O-1) |
> | formation array | a named formation array (Part 12) | `ledger-energy-relics-artifacts` |
> | energy cache | a named energy resource cache (Part 12) | `ledger-energy-relics-artifacts` |
> | other item | any other made or used thing the story names that fits no Type above | none |
>
> A named document (a letter, charter, decree, map, codex, account book) is not a Type here: it is set in italic like an item and is registered in `ledger-society-information` (Part 28 Rule 20.8.7).
>
> **Scope — where the line is drawn.** The register does not claim anything that already has its own ledger or its own form. Nothing is entered twice, and nothing is written differently than it is today:
>
> | What the story names | Form in the prose | Where it is recorded |
> |---|---|---|
> | A named item (this register) | italic | this register, plus its home entry where it has one (below) |
> | A Named Move, Technique or Cultivation Practice | bold-italic (Part 2 Rule 3.2.1) | `ledger-named-moves` (the one generic register of Named Moves, Part 6 Rule 6.5), and the user's own character-ledger entry (Section 3) or the species entry's innate move catalog |
> | A cultivation level designation | bold-italic (Part 2 Rule 3.2.1a) | not a name; recorded as a level in the character ledger |
> | A Named Relic, Named Artifact, formation array or energy resource cache | italic (Part 12 Rule 2.2.3) | this register (Types relic or artifact, formation array, energy cache), plus its home entry in `ledger-energy-relics-artifacts` |
> | A person | as written today | the character ledgers |
> | A place, kingdom or state | as written today | `ledger-worlds-location`, `ledger-worlds-kingdom-state` |
> | A faction, guild or institution | as written today | `ledger-people-society-faction`; a technology institution also in `ledger-technology-scale` |
> | A title, honorific or form of address | as written today | the character ledger of the person addressed |
> | An agreement, treaty or accord | roman (Part 28 Rule 20.8.7) | `ledger-society-information` (a register row), with its agreement file in `ledger-people-society-affiliation` as the home entry |
> | A named map, letter or message, charter, decree, codex or other document | italic (Part 28 Rule 20.8.7) | `ledger-society-information` (a register row), not this register |
> | A research program | as written today | `ledger-technology-growth` |
> | A scientific framework or paradigm event | as written today | `ledger-technology-science` |
> | An intelligence operation | as written today | `ledger-society-information` |
> | A route, gate or named distance | as written today | `ledger-worlds-travel`, `ledger-worlds-distance` |
> | An event or festival | as written today | the ledger of the place or civilization that holds it |
> | A species-language term | italic (Part 16 Rule N16-14) | the civilization ledger; if it also names an item, the item is entered here as well |
> | A category term or tier label from the numbered Parts (Power Crystal, Core, Mortal-grade), or a description with no proper name | plain | none: it is not a coined name |
>
> A building, site or facility that people go to is a place. The apparatus used there is the item.
>
> The register row points at the home entry (the Home entry column of the Type table above) and holds none of its values.
>
> A named knowledge asset (a document that holds classified findings) is a named document, not an item: its home entry is `ledger-technology-science` (Registry C) and it is registered in `ledger-society-information`.
>
> The home entry is created by its own Part 37 threshold (O-1 for a relic, artifact, formation array or energy cache, O-2 for a weapon, O-3 for a vehicle, and the Area 3 thresholds), exactly as before. This register adds a row and never replaces or waives a home entry.

> **Entry schema (Part 37 Area 3.8).** One table below, one row per named item. A row records the named thing, not each copy of it. The six standard columns of Part 37 Area 2.11 come first, in their order (the second, Classification, is headed Type here); four more follow. The B and L marks follow Part 37 Area 5.
>
> | Column | What it holds |
> |---|---|
> | Entity Name (B) | the name exactly as the story writes it, in its italic form (`*Name*`), never with a leading article (the article is plain type in the prose). The one cell in this register that is set in italic. |
> | Type (B/L) | the item's Type, one of the fourteen above: apparatus or device; remedy; gear or tool; weapon; system or service; material; food; drink; dress or adornment; vessel or vehicle; relic or artifact; formation array; energy cache; other item. This is the standard second column of Part 37 Area 2.11 (Classification), headed Type in this register. |
> | First Area Appearance (B) | the Area that first wrote the name, `Area NN — Title (Ref: P.S.N.CCC.AA)`; or `Not yet established`; or `story start` on a row the author has directed to be entered before any Area, for an item the world already holds at the story's start |
> | Entity File (L) | the home ledger entry when the item has one (for example `ledger-technology-scale/[name].md`); otherwise `none — this entry is the item's whole ledger record` |
> | Status (L) | one of the status words below |
> | Last Updated (L) | `YYYY-MM-DD` |
> | One-Line Descriptor (B) | one line in plain words: what it is and what it is for. It holds no value that a home entry owns |
> | Made or Named By (B) | the person, faction or culture that made the item or gave it the name in the story; `OPEN-AREA` where the Area was silent |
> | Naming Checks (B) | the results of the Part 28 Rule 20.3 sequence settled at the time: the register the name follows (the culture or Part 25 cultural profile), the collision scan and its date, and the originality check (cleared, or flagged to the author) |
> | Aliases (B) | every other name or short form the story uses for the item, separated by semicolons, or `none`; each is set in italic too |

> **Status words.**
> - `Active`: the item exists and is in use or on hand.
> - `Dormant`: the item exists and is out of use.
> - `Lost`: the item exists and no one knows where it is.
> - `Destroyed`: the item no longer exists.
> - `Withdrawn`: the item is no longer made or used; it has been taken out of service.
>
> A row is never deleted. When the Area that first wrote an item is removed by a rewind, a redraft or a reset, the reconciliation returns that row's First Area Appearance to `Not yet established` and keeps the row, as every other ledger keeps its entities (the reset script does the same to the cell). A name changes only by Canon Amendment on the author's word (Part 28 Rule 20.8.2(d)); the old name then moves to Aliases.

> **Update Protocol:** Per `guardrails/ledger/guardrail-ledger-update-law.md`, Part 37 Threshold O-4 and Part 28 Rule 20.8.4:
> - **New Row Trigger:** any Area that writes a named item, including a name that appears once and a name that appears only in speech, requires a new row at Gate 2, made by the Post-Write Ledger Update after `[CONFIRM WRITE]`. There is no significance test. A name that exists only in a spec, or in a draft discarded by `[SKIP WRITE]`, is not entered.
> - **Pre-Write Ledger Check:** the check reads this register for every item the Area will use, resolving names through Entity Name and Aliases, so the item is written in its registered form. The Area 20.3 collision scan of a new name reads this register too.
> - **Hand-off route:** the Area Maker lists each new item; the Gate 1 checker reconciles the list with the italic names in the draft; the orchestrating command passes the checked list to the Gate 2 ledger instance.
> - **One owner:** where a home entry exists it owns every descriptive fact; the row mirrors only name, Type and first Area. On a difference the home entry stands, and the difference is a finding at the next ALCA pass.
> - **Update Trigger:** any event written in an Area that changes an item's status, gives it a home entry, or uses a new alias updates the row.

> **Mandatory Update Triggers:**
> - A named item written for the first time in a confirmed and written Area
> - A named item gains a home ledger entry (update Entity File)
> - A status change: lost, found, destroyed, withdrawn, back in use
> - A new alias used in an Area
> - A Canon Amendment of a name (old name to Aliases)
> - A rewind, redraft or reset that removes the Area that first wrote an item (First Area Appearance returns to `Not yet established`)

> **Not entered here:**
> - A name that appears only in a spec. Specs never establish canon (Part 38 Rule 1.3.2); a name proposed in a spec is a proposal, tagged `proposed` in a Chapter Spec and a working label above Chapter grain, and it enters this register at the Gate 2 of the Area that first writes it.
> - Items the other ledgers already record by name before any Area (for example the named entities noted in `ledger-technology-scale` and `ledger-energy-relics-artifacts`). They enter when the Area that writes them is confirmed. An author-directed backfill is allowed at any time and is not required.

> **Marker Legend:** These markers appear in the entries of this ledger. Open cells otherwise carry `OPEN-AREA` or `OPEN-AUTHOR` (Part 37 Area 5).
> - `[ASKED]`: the author chose this value.
> - `[DERIVED]`: the drafter inferred this value from cited evidence and the author reviewed it in the digest without overriding it (Part 39 Rule 39.3.3.1); it is pending only when the entry also says flagged for author confirmation.
> - `[AUTHOR-PENDING]`: a question about this value has been raised and is not yet answered.
> - `[MARKED SLOT]`: a slot left empty on purpose until the author rules.
> - "flag, do not invent": when a scene needs the value, the prose may establish one small fact at a time under Part 28 Area 17, logged in this ledger and offered to the author as a draft value at the next Section close. A name or a major entity (Part 28 Area 20.4) goes to the author first, through the Decision Consultation Gate.

---

## Register — Named Items

| Entity Name (B) | Type (B/L) | First Area Appearance (B) | Entity File (L) | Status (L) | Last Updated (L) | One-Line Descriptor (B) | Made or Named By (B) | Naming Checks (B) | Aliases (B) |
|---|---|---|---|---|---|---|---|---|---|
| *Skyveil* | other item | Chapter 002 — The Well at First Light (Ref: 1.1.1.002) | ledger-worlds-location/skyvein-forest.md (§5.5, item 2) | Active | 2026-10-08 | A kind of tree of Skyvein Forest, seen at the forest's edge past the village field; the home entry owns its description | The author (the tree list of 2026-10-06, `[ASKED]`) | Author-given and consulted 2026-10-06; no culture register applied; collision scan of 2026-10-08 (case-insensitive, whole repository, `_archive` not read): the name appears only in skyvein-forest.md, Chapter Spec 1.1.1.002, the written Chapter 002 and that Chapter's working files, so no collision; originality not cleared against published works and left flagged to the author for information | none |
| *Thornweft* | other item | Chapter 002 — The Well at First Light (Ref: 1.1.1.002) | ledger-worlds-location/skyvein-forest.md (§5.5, item 9) | Active | 2026-10-08 | A kind of tree of Skyvein Forest, seen at the forest's edge beyond the last cleared path; the home entry owns its description | The author (the tree list of 2026-10-06, `[ASKED]`) | Author-given and consulted 2026-10-06; no culture register applied; collision scan of 2026-10-08 (case-insensitive, whole repository, `_archive` not read): the name appears only in skyvein-forest.md, Chapter Spec 1.1.1.002, the written Chapter 002 and that Chapter's working files, so no collision; originality not cleared against published works and left flagged to the author for information | none |
| *Ironhush* | other item | Chapter 002 — The Well at First Light (Ref: 1.1.1.002) | ledger-worlds-location/skyvein-forest.md (§5.5, item 7) | Active | 2026-10-08 | A kind of tree of Skyvein Forest, seen at the forest's edge beside a tree marked with a red ring; the home entry owns its description | The author (the tree list of 2026-10-06, `[ASKED]`) | Author-given and consulted 2026-10-06; no culture register applied; collision scan of 2026-10-08 (case-insensitive, whole repository, `_archive` not read): the name appears only in skyvein-forest.md, Chapter Spec 1.1.1.002, the written Chapter 002 and that Chapter's working files, so no collision; originality not cleared against published works and left flagged to the author for information | none |
| *Hourline* | system or service | Chapter 003 — The Lone Banner (Ref: 1.1.1.003) | none — this entry is the item's whole ledger record | Active | 2026-10-17 | The new wire that carries slips between relay posts; three slips came in over it to the dispatch table, one from each of three different relay posts, none with a repair mark, every letter where it had been put | The author (the name was given 2026-10-04 and is carried by Section Spec 1.1, `[ASKED]`); on the page the thimble for the wire's relay joins is the work of Bramwell Cog's works ("the thimble we made for the relay joins"), and who strung the wire is not said (`OPEN-AREA`) | Author-given and consulted 2026-10-04; no culture register applied; collision scan of 2026-10-17 (case-insensitive, `.claude/story-memory` and the written Chapters, `_archive` not read): the name appears only in Section Spec 1.1, Novel-Part Spec 1.1.1, Chapter Specs 1.1.1.001 and 1.1.1.003 and the written Chapter 003, so no collision; originality not cleared against published works and left flagged to the author for information | none |
| *First Grip* | gear or tool | Chapter 003 — The Lone Banner (Ref: 1.1.1.003) | none — this entry is the item's whole ledger record | Active | 2026-10-17 | A cord-and-leather sleeve that closes on a small fist and keeps a child's sword from turning; the youngest children at the school take it up on their first morning; the cord is dyed by width (red for the narrow, blue for the middle, green for the wide) and a fourth, narrower width is to be cut | The author (the name was given 2026-10-04 and is carried by Section Spec 1.1, `[ASKED]`); made by Bramwell Cog's works (the page: "we made it strongest", "We cut it in three widths") | Author-given and consulted 2026-10-04; no culture register applied; collision scan of 2026-10-17 (case-insensitive, `.claude/story-memory` and the written Chapters, `_archive` not read): the name appears only in Section Spec 1.1, Novel-Part Spec 1.1.1, Chapter Specs 1.1.1.001, 1.1.1.002 and 1.1.1.003 and the written Chapter 003; the plain words "first grip" also occur, in lower case and as ordinary words, in the summary or tradition cells of six rows of the Manual Ledger (`manuals/` files HTH signature and advanced, HAX signature, GUA basic, BAT basic, BAX elite), which are not a manual title, a move name or an item name; so no collision; originality not cleared against published works and left flagged to the author for information | none |
| *Brightwater Wash* | remedy | Chapter 003 — The Lone Banner (Ref: 1.1.1.003) | none — this entry is the item's whole ledger record | Active | 2026-10-17 | A clear wash with no smell that goes onto a raw palm cold and takes the sting out; poured fresh each night and never ahead of the day it is wanted; sixty bottles in the second crate; it cost, in Cog's words, "forty-one washings" | The author (the name was given 2026-10-04 and is carried by Section Spec 1.1, `[ASKED]`); made by Bramwell Cog's works (the page: "It was exactly what she had asked of him", said of the wash that smells of nothing) | Author-given and consulted 2026-10-04; no culture register applied; collision scan of 2026-10-17 (case-insensitive, `.claude/story-memory` and the written Chapters, `_archive` not read): the name appears only in Section Spec 1.1, Novel-Part Spec 1.1.1, Chapter Specs 1.1.1.001 and 1.1.1.003 and the written Chapter 003, so no collision; originality not cleared against published works and left flagged to the author for information | none |
| *Kite Line* | system or service | Chapter 005 — The House With No Walls (Ref: 1.1.1.005) | ledger-worlds-location/aerie-plateau.md (§5.2, the third landmark, and §5.4, the page's lines of Chapter 005) | Active | 2026-10-19 | A chain of masts on the high ground of the Aerie Plateau, each whistling on its kite-chains in one thin note; word goes ahead of a rider along it on the plateau, its northern masts stand silent when weather sits on the Range, and it does not reach the mine road | The ledger (a working name, "The Kite Line (proposed working name)", in `aerie-plateau.md` §5.2), taken up by the text of Chapter 005 (Ref: 1.1.1.005), where it is set in italic in the narration of Area block 03 and in roman inside the lieutenant's speech in Area block 05; who named it in the story is `OPEN-AREA` | Working name of the plateau file; no culture register applied; collision scan of 2026-10-19 (case-insensitive, `.claude/story-memory` outside the archive, the written Chapters under `projects/` and the skills): the name appears only in `aerie-plateau.md` §5.2, Chapter Spec 1.1.1.005 and the written Chapter 005, so no collision; originality not cleared against published works and left flagged to the author for information | none |

*Seven entries so far. The first three are trees of Skyvein Forest first written in Chapter 002 (Ref: 1.1.1.002); the next three are items first written in Chapter 003 (Ref: 1.1.1.003): a system or service, a gear or tool and a remedy; the seventh is a system or service first written in Chapter 005 (Ref: 1.1.1.005). Type: the Type of item, one of the fourteen above; a tree name has no Type of its own, so each tree reads `other item`, the catch-all.*

**Returning use (Chapter 003, Ref: 1.1.1.003).** *Skyveil* is used again at the start of the raid on the lower road, as the hanging leaves that close the gaps between the trunks, white with frost, the screen the raiders step out through. Its row is unchanged: First Area Appearance stays Chapter 002, and the home entry `ledger-worlds-location/skyvein-forest.md` owns the description and any fact the page adds about it.

**Returning use (Chapter 004, Ref: 1.1.1.004; Gate 2 of 2026-10-18).** *First Grip* is used again, in the children's hands, at the practice rack of the foundation yard on the first morning of the unawakened intake (Phase Day 8), after the two crates of Chapter 003 are seen being carried in at the school gate on Phase Day 2 (both lids nailed down; the page names no item there, and the queen names the *First Grip* at dusk: "the cord-and-leather cover for a small fist"). The page adds, for the record of the item (it has no home entry, so this row is its whole ledger record and these facts belong to the row's descriptor): the sleeve is handed out at the rack before the benches fill; it is a leather cover that closes around a fist and a hilt together, crossed on the back of the hand by a cord, red for the narrow width, blue for the middle and green for the wide, so that a child can find its own; nobody shows anybody how it closes; Varya's is red and still too wide for her fist (the sword turns in her palm if she lets go of the cord), and Aegon's is blue; Brea Lawry binds hers with a strip torn from the hem of her own sleeve, wound twice around the leather and tied off, which holds (the Grandmaster's forecast of Chapter 003 begins to come true on the first morning); the narrower fourth width is reported, from "the man at the rack", to be coming on the second cart, and the crate that holds it is "still nailed shut", so it is not yet in the children's hands; the Grandmaster, naming Brea Lawry in her word at the close, says the *First Grip* "is bound to your fist already". The roman short form "grip" is not used for the item anywhere in the Chapter (the Gate 1 finding was fixed), so no alias is added. Its row is unchanged: First Area Appearance stays Chapter 003, and the *Brightwater Wash* is not mentioned in Chapter 004.

**Returning use (Chapter 005, Ref: 1.1.1.005; Gate 2 of 2026-10-19).** *First Grip* is named once more, in Prince Aegon's letter home, which King Aeries reads at the open edge of the Aerie Palace's terrace on 1247.1.12 / PD 12 (Area block 03; the letter is the text between corner brackets, and the queen reads the same page in Area block 04): "We each got a *First Grip* that goes on your fist so the sword does not turn. Mine is blue. I put it on upside down." The same letter says that a girl called Brea "tore a strip off her own sleeve with her teeth and bound hers on and it stayed" (Chapter 004 has the strip torn from the hem of her sleeve and wound twice around the leather; "with her teeth" is new on the page, and no other detail of her binding changes). The page adds for the record of the item, which has no home entry, so that this row is its whole ledger record: the boy first put his on upside down. Its row is unchanged: First Area Appearance stays Chapter 003, and no alias is added. The *Hourline* and the *Brightwater Wash* are not named in Chapter 005; the Gale end of the wire is shown by its absence ("The old wire stops at the corridor", Area blocks 03 and 05).

**Returning use (Chapter 007, Ref: 1.1.1.007; Gate 2 of 2026-10-21).** *First Grip* is used on 1247.2.21 / PD 49, six weeks after the intake's first morning, in Area block 05 at the practice rack of the foundation yard, in Aegon's view: the intake stands in three ranks before the rack, each child with a *First Grip* on the sword hand and its cord crossed over the back of the fist (red, blue and green), and the swords stay in their palms through the three calls of the drill; Varya has held her sword by the cord for the six weeks, her red cover being too wide for her fist. A lad in the Iron Dawn's brown apron brings a small crate on a barrow, draws its nails and takes the barrow away without a word; it holds five leather covers in straw, "smaller than the red", with a yellow cord on each, and the man at the rack, Jago Keverne, says "These are the narrow ones" and fits them, Varya first "since she has waited longest" (he closes the leather round her fist and draws the cord across the back of her hand; she lets go of the cord for the first time in six weeks and the sword stays), then Brea Lawry (who unties the strip of her own sleeve from the red cover with her teeth and closes her fist over it with the scrap she has kept), Ned Bolitho, Mabyn Tippett and Tamar Hendra. The page adds, for the record of the item, which has no home entry, so that this row is its whole ledger record: the narrower width that the earlier Chapters expected has come and its cord is yellow; the page calls the covers "the narrow ones" and does not number the width ("the fourth width" is the plan's term and not the page's); and the credit for the makers is given a third time, in a child's words (the first mouth was in Chapter 003 and the second is Max Pryce's in Area block 04, below; here it is Petroc Curnow: "The queen thought of the cord, and the Grand Artificer's people stitched it, and the Iron Dawn cut the leather", with Silas Uren answering "The Iron Dawn cuts iron" and Petroc "It cuts leather too, if it is asked"). The *Brightwater Wash* is used in two places. In Area block 04 Max Pryce (***Senior Level 3 High***) pours it from a clear bottle on the Fifth Hall's window sill over the scraped heel of his right hand and tells Petroc what it is ("That is the *Brightwater Wash*, Petroc, and it does not hurt, which is the whole of its charm. The queen asked for something that would clean a hand without stinging it, so the Grand Artificer worked out how to make it, and the Iron Dawn makes a new lot of it every night."); Aegon thinks it is Aunt Valia's and keeps that to himself; Varya asks how the wash knew where to be gentle and Max answers that he cannot say. In Area block 05 it stands in its clear bottle on a shelf at the foot of the rack beside a stack of cloths, where the children wipe their hands with it when Jago Keverne says "Clean your hands" (it has no smell, the palms come away pink from the leather and whole, and nobody says a word about the bottle). Both rows are unchanged: First Area Appearance stays Chapter 003 for each, and no alias is added.

---

## Part 28 Area 17 — Lore note (Named-Item Register)

A row is a register entry, not a lore file. The Part 28 Area 17 lore of an item, where the story needs it, is the lore of its home entry, and that entry carries its own Lore section. An item with no home entry keeps its one-line descriptor until the story needs more. When it does, the Pre-Write Ledger Check flags the gap, the Area may establish one small fact at a time (Part 28 Area 17, logged and offered to the author at the next Section close), and if the item needs a full file the author is asked which ledger it belongs in (Part 37 Area 1.6).

**Depth Test:** "Can a scene that uses this item be written without inventing what it is?" For an item with a home entry, the home entry answers it. For an item without one, the one-line descriptor is enough only until a scene needs more.

**Silent Overwrite Prohibition (Part 28 Area 17.5):** Once an item is registered, its name, Type and descriptor are fixed under the Establishment Threshold; later Areas may enrich it and never contradict it.
