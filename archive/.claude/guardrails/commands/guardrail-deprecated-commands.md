# Guardrail: Deprecated Commands — Never Reintroduce

**Source:** Part 1 (Governance and Audit Law), Area 7
**Applies to:** anyone adding or modifying `.claude/commands/*.md`

## The rule

Two of the original canon's 38 bracketed commands are explicitly canon-deprecated and were
deliberately **not** migrated to `.claude/commands/`:

- `[WRITE NEXT N PROSE UNITS]`
- `[WRITE TO END OF CHAPTER]`

Both violated the One-Prose-Per-Invocation rule (`commands/guardrail-command-law.md`) by
batching multiple prose units through a single Gate 1 → Gate 2 pass, which undermines the
per-unit audit discipline the whole pipeline depends on.

## Hard rule

Do not recreate a command (under this name or a new one) that writes more than one prose
unit per invocation without a full, independent Gate 1 → confirm → Gate 2 cycle for each
unit. If a future need for faster iteration arises, solve it by making individual
invocations cheaper/faster, not by batching audits.

## Escalation

If asked to "speed things up" by writing several prose units at once, surface this guardrail
rather than quietly building a batching command.
