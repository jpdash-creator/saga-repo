# Guardrail: Deprecated Commands — Never Reintroduce

**Source:** this guardrail (the command layer has no skill file) · Canon v10.0
**Applies to:** anyone adding or modifying `.claude/commands/*.md`

## The rule

Two bracketed commands are canon-deprecated and are not commands:

- `[WRITE NEXT N AREAS]`
- `[WRITE TO END OF CHAPTER]`

Both violate the One-Area-Per-Invocation rule of the Area pipeline (`.claude/guardrails/commands/guardrail-command-law.md`) by
batching multiple Areas through a single Gate 1 → Gate 2 pass, which undermines the
per-Area audit discipline that pipeline depends on.

Amended 2026-10-07: they stay deprecated. `/create-chapter` (Command C-42) is not a revival of either: it is a new
rule, a second lawful writer, that writes one whole Chapter from its confirmed Chapter Spec with no Area files and
its own Whole-Chapter Gate 1 and Gate 2 (`.claude/guardrails/audit/guardrail-audit-gate-law.md`). It writes a
Chapter, not Areas, and it never runs on a Chapter that has Area files.

## Hard rule

Do not create a command (under these names or a new one) that writes more than one
Area through the Area pipeline per invocation without a full, independent Gate 1 → confirm → Gate 2 cycle for each
Area. The one lawful whole-unit writer is `/create-chapter` (and its reviser `/revise-chapter`), which write a whole
Chapter with no Area files (Amended 2026-10-07). If a need for faster iteration arises, solve it by making individual
invocations cheaper and faster, not by batching audits.

An Area is the written unit of `/next-area` and is written one Area per invocation: the Area before it
is read at each Gate 1 and never turns two Areas into a batching unit.
A command that plans, drafts, audits or writes more than one Area together through the Area pipeline is the
deprecated shape under any name. A Chapter built whole is written as one Chapter and has no Area files.

## The command set

The Canon v10.0 commands are exactly those in the table of `.claude/guardrails/commands/guardrail-command-law.md`:
`/hard-reset`, `/reset-ledgers`, `/start-story`, `/next-area`, `/next-chapter`, `/next-part`,
`/next-section`, `/next-phase`, `/run-canon-audit`, `/status`, `/review-ledger`, `/update-ledger`,
`/rewind-to`, `/ideology-audit`, `/consequence-audit`, `/character-sheet`, `/canon-check`,
`/reset-story`, `/reset-chapter`, `/reset-phase`, `/chapter-builder`, `/compile-phase`,
`/compile-phase-md`, `/compile-novel`, `/compile-novel-md`, `/revise-area`, `/redraft-area`,
`/redraft-chapter`, `/preview-chapter`, `/chapter-summary`, `/area-history`, `/pause`,
`/load-canon`, `/create-image-phase`, `/create-image-section`, `/force-ledger-audit`,
`/chapter-spec`, `/section-spec`, `/part-spec`, `/create-chapter`, `/revise-chapter`, `/new-character`, `/character-behavior`,
`/find`, `/timeline`, `/threads` and `/restore-archive`.

`/export-chapter` is deprecated (2026-10-07) and replaced by `/chapter-builder` (Command C-24); it is not a command and is
not to be reintroduced.

There is one command that writes an Area, `/next-area`, and one that writes a whole Chapter, `/create-chapter`
(Amended 2026-10-07); neither batches Areas. `/revise-area` revises one written Area
in place; `/revise-chapter` revises a whole-built Chapter in place; `/redraft-area` redrafts one whole Area;
`/redraft-chapter` redrafts a Chapter (a whole-built Chapter is redrafted by `/create-chapter`).

## Escalation

If asked to "speed things up" by writing several Areas at once, surface this guardrail
rather than quietly building a batching command.
