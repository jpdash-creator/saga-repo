# Guardrail: The Session Log Is Never a Decision Input

**Source:** Part 1 Foundational Principle F-5 ("Files-Only Decision Governance")
**Applies to:** all 4 agents, always — this is the single most important epistemic rule in the whole system

## The rule

The only valid inputs to any canon decision are: the canon skill files
(`.claude/skills/ssc-*`), the guardrails (`.claude/guardrails/`), the story-memory ledger
files (`.claude/story-memory/ledger-*/`), and the written prose files themselves
(`projects/novel-starward-saga/`). **Chat context, prior conversation summaries, and
`.claude/story-memory/session-log/` are categorically excluded** as canonical decision
inputs, no matter how confident they sound.

Prose that was described or discussed in conversation but never actually written to a file
**is not canonical**. If it isn't on disk, it didn't happen yet.

## Why this exists

This is the direct migration of the original canon's own Rule F-5, which pre-dates this
`.claude/` restructuring — the source material independently arrived at the same principle
this whole project is built around: an agent's memory of "what we discussed" degrades and
drifts; files on disk do not. `.claude/story-memory/session-log/` exists purely as a human-readable
audit trail of what happened and why — useful for a person reviewing history, worthless (and
actively dangerous) as something an agent reasons from to decide what's true.

## Hard rules

- Never cite the session log, or "what was said earlier," as justification for a canon fact.
  Cite the actual skill, guardrail, ledger, or prose file.
- Every agent may (and should) *write* to the session log — it should never *read from* it
  as an authority.
- If a fact seems true only because "it was mentioned before" and isn't backed by a file,
  treat it as not-yet-established, not as quietly-true.

## Escalation

If you're unsure whether something is file-backed canon or just remembered conversation,
stop and check the file — don't proceed on the assumption.
