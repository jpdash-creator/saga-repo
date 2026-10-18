# Guardrail: Ledger Schema Authority

**Source:** Part 37 (SSC Canon Ledger Schema Law) · full detail: `ssc-ledger-p37-*` skills
**Applies to:** Continuity Checker (primary owner of `.claude/story-memory/` writes)

## The rule

Part 37 is the schema authority for every `.claude/story-memory/ledger-*/` file — both the
per-folder `_index.md` registries and the individual entity files. Where Part 1 Areas 5.4/
5.5 and Part 37 ever appear to disagree on a schema detail, **Part 37 governs** (this is an
explicit v2.32 amendment to Part 1 itself, not a default assumption).

- **10 active ledger types** have full schema templates in Part 37 Area 2; **7 additional
  types** are named (folder + entity-creation threshold) but schema-pending — if prose
  introduces an entity of one of the 7 pending types, flag it (`NEW ENTITY TYPE — Part 37
  schema not yet defined`) and get explicit direction before inventing a schema.
- **Entity Creation Thresholds** (Area 1) gate *when* a new ledger file may be created —
  not on first mention, but once the prose has established enough for a real entry. A
  Villain-Potential first appearance and a Hero-Ledger creation both require an explicit
  `AskUserQuestion` — neither is ever auto-created.
- **Baseline (B) vs. Living (L) fields**: B fields are locked at creation and may only be
  enriched, never contradicted, without a formal Canon Amendment. L fields are the ones
  expected to change and are the ones Post-Write Ledger Update (see
  `guardrail-ledger-update-law.md`) actually touches.

## Hard rules

- **Ledger beats prose on conflict.** If a ledger file and a piece of prose disagree, the
  ledger is authoritative until formally reconciled — never silently defer to whichever the
  agent saw most recently.
- **No Duplication Across Ledgers.** An entity gets exactly one canonical ledger file; do not
  create a second record of the same entity in a different folder.
- **Character Role Migration** (villain ↔ side character) is AI-executable; **Hero
  characters cannot be migrated without explicit user instruction** — the Hero Ledger's
  survival-protection status is not something an agent revokes on its own.

## Escalation

Schema drift (e.g. a ledger index missing a required section) is reported via ALCA, not
silently rewritten mid-unrelated-task.
