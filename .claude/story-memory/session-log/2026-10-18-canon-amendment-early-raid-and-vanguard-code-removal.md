# CCIA reconciliation of the Canon Amendment of 2026-10-18 (one early raid on Phase Day 9) and removal of the Redhaft Vanguard code provision NO SOLDIER'S BLOOD (2026-10-18)

Not canon; an audit trail.

- Authority, both cited as relayed by the orchestrating command (no spec note on disk carries either yet; the specs are being revised through `/section-spec` and `/part-spec` and still read "Part 30 is not touched"): (1) the author's `[CANON AMENDMENT]` of 2026-10-18: one early Gale mine caravan raid by the Redhaft Vanguard of Brackenhold on Year 1247, Ilovany, Day 9 (Phase Day 9) is allowed in the first fortnight of Section 1; the second-half raids and the no-open-war rule are unchanged. The orchestrating command had already edited Part 30 line 450 (the Rival-Kingdom Raids and Skirmishes function) and the Phase table row at line 815. (2) The author's second ruling of the same day: the Redhaft Vanguard's registered code provision NO SOLDIER'S BLOOD is removed; the Vanguard may kill soldiers.
- Read: guardrails index, `guardrail-ccia.md`, `guardrail-forced-read-discipline.md`, `guardrail-ledger-update-law.md`, `guardrail-alca.md`, `guardrail-locked-vs-negotiable-canon.md`; the four canon-manifest files from disk (`dependency-graph.json`, `domain-map.json`, `ledger-architecture-map.json` in full, `skill-index.json` for the Part 30 row and its line counts); Part 30 (every raid, skirmish and "second half" line, the Laws P30-L4 and P30-L5, Check #11); Part 35 (Areas 3.5 and 7); the Redhaft Vanguard, Wulfric Rask, Brackenhold and villain-index files at the lines named below.

## Files changed

| File | Change |
|---|---|
| `.claude/skills/narration-novel-macro-story-law/SKILL.md` (Part 30) | Four lines that restate the second-half start were reconciled in place, no line added (headings still at 33, 415, 872 and 882; 886 lines; CRLF kept): line 258 (Section Time Allocation Notes) and line 437 (Section 1 Section Arc) gained "(one earlier raid on Phase Day 9 excepted, Canon Amendment 2026-10-18)"; line 476 (Section 2 Phase Positioning) "began in late Section 1" now reads "began in Section 1"; line 844 (Setups table row 11, Planted cell) gained the same parenthetical. Lines 450 and 815 are the orchestrating command's own edits and were not touched. |
| `.claude/skills/narration-content-density-law/SKILL.md` (Part 35) | Area 3.5 Derivation Notes: line 319 (Section 1) gained the same parenthetical; line 322 (Section 2) "began in late Section 1" now reads "began in Section 1". No Anchor or target figure changed. |
| `ledger-people-society-faction/redhaft-vanguard.md` | Last Updated 2026-10-18. The provision line NO SOLDIER'S BLOOD (with its basis and evidence) is replaced by one italic dated ruling note in the Shared conduct list; its provision-by-provision page note under "Shown at Chapter 003" is retired (the page facts it held, three soldiers hurt and none dead, stand in `azure-sky-military.md`, `azure-sky-kingdom.md`, `lower-road.md` and `ledger-character-side/_index.md`); a new Changelog line. The 2026-10-17 Changelog lines and the Section 5 event row ("No soldier is killed") are history and were left. |
| `ledger-people-society-faction/_index.md` | The Redhaft rows (registry and lore table): date 2026-10-18 and a short clause on the removal. |
| `ledger-character-side/wulfric-rask.md` | Last Updated 2026-10-18. Section 11.5 "Shown on the page": the clause "no soldier's blood (the stroke kills no one and the patrol loses none)" is taken out of the list of code provisions that show, with one dated note; a new Changelog line. Nothing else changed (`B39-L25-KILL` stays `OPEN-AUTHOR`). |
| `ledger-character-side/_index.md` | Wulfric Rask registry row: date 2026-10-18. |
| `ledger-worlds-kingdom-state/brackenhold.md` | Section 3 Political Posture: a dated italic note after the page quote of the king's order; Section 8: a new ruling row "Author ruling, 2026-10-18 (Vanguard code)"; a new Changelog line. The Chapter 003 page rows (Section 3 quote and the Section 8 row of 1.1.1.003) were left as the page record. |
| `ledger-character-villain/_index.md` | Hadric Stoll's Tier C row: Current Condition cell gained a dated note after "the king's standing order, no soldier's blood, is in his thought" (it records the Chapter 003 page as written); row date and index header date 2026-10-18. |

## Searched, no restatement found, nothing changed

The four canon-manifest files (no row names the raid rule or the code provision; Part 30 line counts 382 and 471 still hold because every edit was in place); every guardrail, agent, command, docs and template file; every other skill (Part 44's Chapter 3 worked example, Part 40, Part 22 and Part 23 mention raids and raiders without stating the timing); every other ledger file (the "second half" hits are figures of speech or Hercules and Bison's "first practised named move in the second half"; the Azure Sky "no soldier would cross the ford" lines are a different rule, the Non-Aggression Default).

## Left on purpose

- The Chapter 003 page (`Chapter 003 - The Lone Banner.md`, line 74, and the `.docx`) still says the company "must shed no soldier's blood"; a written file is changed only through `/revise-chapter` or a redraft, so every ledger line that quotes the page was kept as the page record and marked with the ruling.
- Part 30 setups row 11, "Source and open points": "Which kingdom sends the raiders and which side's officers fight are OPEN-AUTHOR" is unchanged; the amendment names Brackenhold for the Phase Day 9 raid only.
- `cdl2-density-tracking/phase-1/section-1-aggregate.md` line 224 (an Area Scorer record of the king's order in Chapter 003); the 2026-10-17 session log; the spec chain (off limits for this step).

## Reported, not applied (CCIA escalation)

- `dependency-graph.json` holds no edge from Part 35 to Part 30, though Part 35 Area 7 states "CDL-2 derives Section targets from Part 30 Area 2". A pre-existing manifest gap in Relationship Accuracy; adding the edge would also need the matching `related` entries in `skill-index.json`. For the author's decision.
