# Guardrail: The Session Log Is Never a Decision Input

**Source:** this guardrail (files-only decision governance) · Canon v10.0
**Applies to:** all 4 agents, always — this is the single most important epistemic rule in the whole system

## The rule

The only valid inputs to any canon decision are: the canon skill files
(`.claude/skills/`), the guardrails (`.claude/guardrails/`), the canon manifest
(`.claude/canon-manifest/`), the story-memory ledger files (`.claude/story-memory/ledger-*/`),
the confirmed spec chain (the Section Spec, Novel-Part Spec and Chapter Spec in
`.claude/story-memory/phase-section-part-chapter-area-specs/`),
which is a planning input and never established canon at any of its three levels
(`.claude/guardrails/ledger/guardrail-story-spec-law.md`), and the written prose files themselves (`projects/novel-starward-saga/`). **Chat context, prior conversation summaries, and
`.claude/story-memory/session-log/` are categorically excluded** as canonical decision
inputs, no matter how confident they sound.

Text that was described or discussed in conversation but never actually written to a file
**is not canonical**. If it isn't on disk, it didn't happen yet.

## Why this exists

This is the principle this whole project is built around: an agent's memory of "what we discussed" degrades and
drifts; files on disk do not. `.claude/story-memory/session-log/` exists purely as a human-readable
audit trail of what happened and why — useful for a person reviewing history, worthless (and
actively dangerous) as something an agent reasons from to decide what's true.

## Hard rules

- Never cite the session log, or "what was said earlier," as justification for a canon fact.
  Cite the actual skill, guardrail, ledger, or Area file.
- Every agent may (and should) *write* to the session log — it should never *read from* it
  as an authority. The orchestrating command writes the log line: one line per Area for `/next-area`, and (Amended
  2026-10-07) one line per Chapter for `/create-chapter` and `/revise-chapter`, citing the Chapter reference
  `P.S.N.CCC`; the full named-result list of the Gate 1 audit goes into that one line's entry.
- The private agent notes in `.claude/agent-memory/` record working technique only (how to
  read a file, which search works, a method that saved time), never a canon fact. An agent
  never reasons from one to decide what is true; a nuance that matters is written to the
  ledger or put to the author.
- If a fact seems true only because "it was mentioned before" and isn't backed by a file,
  treat it as not-yet-established, not as quietly-true.

## Escalation

If you're unsure whether something is file-backed canon or just remembered conversation,
stop and check the file — don't proceed on the assumption.
