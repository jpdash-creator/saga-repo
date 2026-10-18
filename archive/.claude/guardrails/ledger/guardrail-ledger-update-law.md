# Guardrail: Ledger Update Law

**Source:** Part 1 (Governance and Audit Law), Areas 5, 6
**Applies to:** Continuity Checker (executes it); Prose Maker / Outline Planner (must not skip triggering it)

## The rule

Ledgers are living canon records, not planning notes. **No prose may be written without a
Pre-Write Ledger Check. No prose may be accepted into canon without a Post-Write Ledger
Update.** Both are mandatory, every single time, with no exception for "minor" prose units.

- **Pre-Write Ledger Check** (Area 6.2): read the relevant `.claude/story-memory/ledger-*/` entries
  *before* drafting, including the Step 2.5 Power Ceiling / Permitted-Forbidden Realm
  Vocabulary statement (Part 3 Rule 1.7) — know what's allowed to appear before writing it.
- **Post-Write Ledger Update** (Area 6.3, executed via `/force-ledger-audit`): after any
  accepted prose unit that changes canon state — new entity creation (with the mandatory
  `AskUserQuestion` for antagonistic first appearances), and a **dual content mandate**:
  (a) state-record fields updated, and (b) narrative-summary enrichment sufficient that the
  test *"could I write the next scene using only this ledger file?"* passes.

## Hard rules

- **No Stale Ledger State.** A ledger entry that hasn't been updated after a scene that
  changed it is itself a canon violation, not a deferred task.
- **Ledger Supersedes Memory.** If conversational context and the ledger file disagree,
  the ledger file is right — re-read it rather than trusting what a prior turn implied.
- **Incomplete Ledger Update** is a Major Violation from the very first occurrence once the
  obligation was named at Gate 1 (not a "warn once, then enforce" rule).
- **Completeness Requirement.** A named character/faction/location that appears in accepted
  prose without a ledger entry is itself a canon violation — the entry must exist, even if
  thin, not be deferred indefinitely.

## Escalation

If a Pre-Write Check or Post-Write Update can't be completed (e.g. ambiguous entity
classification), stop and ask rather than proceeding with a guessed ledger state.
