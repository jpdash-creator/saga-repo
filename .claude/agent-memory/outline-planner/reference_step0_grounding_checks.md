---
name: reference-step0-grounding-checks
description: Checks that surfaced real blockers or traps while grounding /create-chapter Step 0 (code state, Pending tables, move verification, stale ledger wording, map conflicts, Check #21 precedent)
metadata:
  type: reference
---

**State from the files, never from a session log.** A session-log line about a ledger lane's writes is a pointer only. Confirm each collective code by Grep of `Code Status` in the entity file, and read the `## Pending author confirmations` table of the hero index (line ~45) and the villain index (line ~96): they list the flagged lines Gate 1 Check #21 will raise.

**Verify every move of a Chapter in two Greps.** (1) `^(ID1|ID2|...),.{0,110}` with `-o` over `ledger-manuals/moves` returns name, grade, type and unlock for each ID. (2) Grep `kingdoms/gale.csv` and `kingdoms/brackenhold.csv` for the manual IDs (access rows). In the Named-Move register a hit on a "new" move name inside a "word echoes" note is an echo note, not a row.

**A location with no ledger file.** A spec's "none, the planner's reading" for a place where named people fight is not a ruling. The command words Rule 39.23.1.5 as blocking; Chapter 003 treated its road stub as OPEN-AUTHOR and drafted. Ask it, with "none, by your ruling" as the Recommended answer, and fold incidental background formations (a garrison that only stands by) into the same question.

**New frontier or place in a spec.** Read the kingdom-state file (Territorial Extent), `windward-range` 5.1, `azure-sky-kingdom` 5.1 and the Cultural Association lines before accepting the placement; the map rulings of 2026-10-18 can conflict with the plan and with Part 30 village wording. Put the conflict to the author as the Open map note, with a defer option.

**Stale ledger wording to put in the maker's launch brief.** The hero files carry a 2026-10-08 note that contractions are lawful in dialogue (the Canon Amendment of 2026-10-16 bars them in dialogue and narration). `aerie-palace` 5.3 uses "hum" (an author-removed concept for this Chapter). `aeries` `B39-L03-LEAK-99` says "the pupil wrong" (a form hint barred by the row 13 exclusion). Hero Section 9 arc cells read OPEN-AUTHOR until Gate 2 writes the spec's Settled values.

**Check #21 at Step 0, precedent.** Chapter 002 Step 0 asked the flagged hero lines and the author ruled DEFER; Chapters 003 and 004 were ruled at Gate 1 with the text printed (KEEP PROFILE, EVOLVE, DEFER). Offer "ask at Gate 1" as the Recommended option and "confirm as registered now" as the alternative; the author rules heroes, Tier A, villains and monsters, the checker rules Tiers B to D.

**Why:** found while grounding Chapter 005 Step 0 (2026-10-18); each item would otherwise have reached Gate 1 as a surprise stop or a false claim.

**How to apply:** run these before writing the Step 0 report; list the maker-brief traps as one block at the end of the report.
