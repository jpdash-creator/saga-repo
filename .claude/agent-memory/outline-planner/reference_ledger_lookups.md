---
name: reference-ledger-lookups
description: Manual Ledger Grep recipe and routes, move matching, collective-code stubs
metadata:
  type: reference
---

**Manual Ledger scan.** `ledger-manuals/` holds CSVs, generated mid-session: re-read before citing. Move names are column 4 of `moves/**/*.csv`: Grep `^[^,"]+,[^,"]+,[^,"]+,[^,"]*STEM[^,"]*,` (mind head_limit). The planner has no Bash, so it cannot run `manual_ledger_query.py find-name` (flags exact, reordered words, difflib ratio at or above 0.85, 0.93 for short names, or one name holding all words of the other): compute the ratio by hand and ask the Gate 1 checker to run the tool.
- Routes for a hero's technique: (A) own move outside every manual (Rules 42.12.5.4, 42.4.2.1, 42.12.7.2), the Recommended one; (B) kit move by exact ledger name (Rules 42.12.5.1, 6.5.2).
- Hard limits for an Area: N42-2, N42-3, N42-5, N42-7, N42-9.

**Move matching.**
- IDs: weapon `MV-{GRD}-{WPN}-{NNN}-{SS}`, cultivation `CMV-{GRD}-{AFF}-{NNN}-{SS}`. Names change in rename passes, IDs are stable: Grep `^ID,` for the current name.
- Two gates: the manual's `min_realm` and `affinity_req` (holding), the move's `move_type` and `unlock_realm` (execution; Part 6 Access Table). An Intermediate move can sit in an Advanced manual: check both.
- Persons with no recorded affinity use only affinity-free disciplines (BDY, QIP, FRM). Never invent an affinity.
- Who reads whom: Part 3 Area 21.3 (read the Area, do not copy numbers). Phase 1 prose names only Senior, Warrior, Champion, Ruler.
- `characters.csv` and `character-kits.csv` hold heroes and Tier A/B only; Tier C/D come from `eligibility-rules.md`. A viewpoint person's pronoun or level can be OPEN-AUTHOR: raise it.

**Collective codes.** The stub sits at the foot of each location file (`Code Status: Not yet registered`). A location that is only a row of `ledger-worlds-location/_index.md` is covered by its parent file's block. A location block points to the kingdom-state code and does not restate it (Part 37 one-home rule). Block template: Part 39 Area 41.4. Registration is a step in the commands (`/chapter-spec`, `/create-chapter`, `/next-area`, `/revise-chapter`): follow them.
