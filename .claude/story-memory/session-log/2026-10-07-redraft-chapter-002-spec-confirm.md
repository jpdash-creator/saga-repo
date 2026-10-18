# Session log — /redraft-chapter Chapter 002, Step 1 (/chapter-spec revise)

- **Date:** 2026-10-07
- **Mode and artifact:** `/chapter-spec revise`, Chapter Spec 1.1.1.002, v1.0 to v1.1 (Build mode whole; five Area blocks in four scenes S4 to S7; Areas 01 and 02 joined as one Day 1 scene)
- **Confirmation token:** [CONFIRM SPEC] (the author, 2026-10-07)
- **Checkpoint:** commit 8ff639a on main, before anything was changed
- **Light audit and final sweep:** 0 FAIL both times; every WARN answered by the author
- **Departures and the author's choice for each:** window and closing beat, check only (no duplicate note); Threads in (One Sky), keep the original entry as baseline; Tier D speakers' names, keep the original as baseline; Bison's look, amend the entry through `/part-spec revise`, run after this confirm in parallel with the chapter build. Variance notes written top-down, Section Spec first, then Part Spec.
- **Open and Deferred notes left:** Bison's first named move (Open); the new Tier D names (about nine, to Step 0 of `/create-chapter`); the trade word for the two men; address forms for later Chapters; village details left unset
- **Standing rulings:** both men chattier and ask freely, an [EVOLVE] for both (reason: a year in the village has made them at ease; entries written at the one Gate 2); the Deferred rows stay open; pointer rows kept for the four place names; rows kept at Step 2 keep name, kind, parent and code only
- **Status:** Areas 01 and 02 read WRITTEN until Step 2 (archive and rollback) rolls them to PLANNED. Nothing archived yet.

## Step 2 (archive and rollback), 2026-10-07
- Archived Areas 01 and 02 (4 files) to `projects/novel-starward-saga/_archive/2026-10-07_2140/` (way back: `/restore-archive 2026-10-07_2140`).
- Rollback written on the author's instruction (preview and confirm skipped by the author): hero ledgers (hercules, bison, hero index; all Evolution Entries kept; Deferred row 1 Date cells marked rolled back), world ledgers (location index pointer rows and Hercules/Bison position rows, azure-sky-kingdom, nine-suns-continent, travel and alder-bridge, calendar), side-character index (four Tier D rows kept, detail pending redraft), CDL-2 tracker (4 Areas; the deletions approved by the author; reading-convention blocks and two forward-projection notes left as history), Chapter Spec Area blocks to PLANNED, registry row.
- The author ruled greenhollow-cross.md and skyvein-forest.md stay as given by the author; skyvein-forest.md restored from checkpoint 8ff639a after an agent edit.
- `/part-spec revise` 1.1.1: light amendment of the Chapter 002 entry (Bison's look) done.

## Step 3 and Step 4 (rebuild whole and reconcile), 2026-10-08
- `/create-chapter` Chapter 002 (1.1.1.002): whole build, four scenes S4 to S7. Step 0 answers recorded in the spec notes (nine Tier D names, the miller explains the crane, address forms, Bison's first named move is a Wind move to be named later, work gloves EVOLVE ADD, carried Check #21 flags DEFER again).
- Draft by one area-maker, one edit pass plus one fail-loop pass by the chapter-editor. Measure: PASS, 5,344 words (59.4% of 9,000): 1,139 / 1,022 / 1,087 / 1,118 / 978.
- Gate 1: instance 1 (22 checks) first run 1 FAIL (Check #20, one sentence in Area 04), re-audit 0 FAIL; instance 2 (flow review) 0 FAIL, 14 sameness patterns. Author gave [CONFIRM WRITE] as it stands: accepted differences D1 to D10, left the 14 patterns as written.
- Written by chapter_builder.py: Chapter 002 - The Well at First Light.md and .docx in the Novel-Part folder.
- Gate 2 (five parallel lanes): post-write audit PASS; hero ledgers (Evolution Entries hercules 3, bison 4 and 5); world, side, calendar and named-items ledgers (Current Position 1247.1.3 / PD 3); Chapter Spec COMPLETED v1.1; CDL-2 block and Section 1 aggregate (12,411 words).
- Step 4 plain reconciliation: no blocking finding; 3 mechanical fixes; four Signature firings added to the hero Section 10 lists. Open for the author: registry Coverage cells of the Novel-Part and Section rows (2/9, 2/31) refresh at the next completion write step; the place files were rewritten from the Chapter by the world lane (originals in git checkpoint 8ff639a); reset_story.py matches only five-part Area refs.
