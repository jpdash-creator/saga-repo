# Collective and location code registration step added to the planning commands (2026-10-17)

Not canon; an audit trail.

- Authority: the author's ruling of 2026-10-17 to fix, in this clean-up, the gap that Part 39 Rule 39.23.1.5 requires a collective or location code to be registered before drafting while no command performed the registration (Chapter 003 had to do it by hand, see the 2026-10-08 pre-draft registration log and the 2026-10-17 re-level log).
- Rules read: Part 39 Rule 39.23.1.5 and Rules 39.23.1.1 to 39.23.1.4; Part 39 Area 41.4 (the block template); the Redhaft Vanguard and Skysworn patrol blocks as form models; the existing guardrails.
- The step, "Register new collective and location codes before drafting": the planner reads the Code Status; `Not yet registered`, an empty stub or no entry is a blocking item; the outline-planner proposes a short code from cited ledger facts (or none for an incidental crew); the author confirms, changes or rules none through `AskUserQuestion` (a new entity is always asked, a `[SKIP]` leaves the item blocking); the continuity-checker writes the confirmed block into the entity's own ledger file before the area-maker is launched (Baseline B/L, `Registered YYYY-MM-DD` or `None, by the author's ruling`); at Gate 2 the checker only verifies and updates Members.

## Files changed (hand edits)

| File | Change |
|---|---|
| `.claude/commands/create-chapter.md` | Step 0: new bullet with the full step; Step 2: a hold on launching the area-maker until a confirmed code is written. |
| `.claude/commands/next-area.md` | Step 0: the same bullet, Area-scoped; Step 2: the same hold. |
| `.claude/commands/chapter-spec.md` | Step 0: collective and location code raising at spec build (blocking Open note, Settled note on confirmation; the spec writes no ledger). |
| `.claude/commands/part-spec.md`, `.claude/commands/section-spec.md` | Step 0: one sentence each, a new collective or location is noted as owing a code and registered at the Chapter Spec build. |
| `.claude/commands/revise-chapter.md` | New Step 0: a collective or location brought in by a revision follows the same step before the chapter-editor starts. |
| `.claude/agents/outline-planner.md` | Behavioral planning: proposes, never writes the block, never leaves it to the drafter. |
| `.claude/agents/continuity-checker.md` | Ledger updates: writes the confirmed block before drafting; verifies it at Gate 2. |
| `.claude/guardrails/ledger/guardrail-ledger-update-law.md` | One sentence in the Pre-Write Ledger Check restating the law. |

## Variance to note

The author's brief said the checker writes the row at Gate 2 once confirmed. Rule 39.23.1.5 says the code is registered before the prose is drafted, so the write is placed before the area-maker is launched (as done for Chapter 003 on 2026-10-08), and Gate 2 verifies it. This is the only ledger write before Gate 2 and it is author-directed.

## Not done, on purpose

No agent-memory file, `.claude/temp` file, chapter text, ledger or spec was touched. The Part 39 skill text was not changed.
