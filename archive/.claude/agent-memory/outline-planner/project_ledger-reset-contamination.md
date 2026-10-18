---
name: ledger-reset-contamination
description: The 2026-06-21 story reset cleared prose-event history from ledgers but left prior-run plot state in Living-Information fields and index files — how to tell binding lore from residue.
metadata:
  type: project
---

A prior authoring run produced roughly Prose 1–9 (opening Prose was titled *"Before the
Kingdom Wakes"*, Ref 1.1.1.001.1.00001) and its plot was written into the ledgers. That
prose was later deleted from disk. A reset pass dated **2026-06-21** cleared, on the
*entity* files: `First Prose Appearance` (back to "Not yet established"), Section 4/10
Events Logs (emptied), and hero ledger versions (back to v1.0). It did **not** clear
index files (still dated 2026-05-24) or several Living-Information (L) status fields.

**How to classify what you find:**
- **Binding** — Section 5 "Lore (Part 28 Area 17)" blocks on location/kingdom/faction
  files, and all Base Information (B). The reset deliberately preserved these; the hero
  index even notes "§5.1–§5.13 pre-prose Stage 4 content fully intact." Treat as
  established Negotiable Canon under the Part 28 Establishment Threshold, even where the
  text says "as established in Prose 00001" — the *attribution* is stale, the *content*
  is not.
- **Residue — do not treat as world-state** — anything describing prior-run *plot*:
  the Windward Pass CPM accumulation crisis, the 76-day threshold, the bilateral
  Azure Sky / Gale sessions ("session in 17 days", "second session in 4 days"),
  and the hero-index row giving Aeries a first appearance in Prose 00001.
  These were *created by* the deleted prose, so they are not pre-existing Phase Day 1
  conditions.

19 files under `.claude/story-memory/` still carry prior-run Prose references.

**Why:** Planning Prose 1 from the contaminated state would either import a crisis the
story has not yet caused, or would silently contradict a ledger row.

**How to apply:** When planning any early Phase 1 / Section 1 unit, read entity files
rather than index files for current state, and explicitly instruct Prose Maker which
prior-run threads are off-limits. Flag the residue to the orchestrator for the Continuity
Checker rather than fixing it yourself — ledger correction is not the planner's domain.
Related: [[prose-1-structural-decisions]].
