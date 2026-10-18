---
description: Write the next Starward Saga prose unit through the full Two-Gate pipeline (outline confirm -> draft -> Gate 1 audit -> confirm -> Gate 2 write -> ledger update -> score).
user-invocable: true
---

# `/next-prose`

The pipeline workhorse — corresponds to canon command `[NEXT PROSE]` (C-4).

## Preconditions

- Read `.claude/guardrails/_index.md` and `.claude/guardrails/audit/guardrail-audit-gate-law.md`.
- Pre-Write Ledger Check: confirm the relevant `.claude/story-memory/ledger-*/` entries for
  every entity about to appear are current.
- Pacing targets are governed by the Canon v4.34 Pacing Law Amendment
  (`ssc-narration-p02-six-tier-narrative-hierarchy`, Part 2 Area 6.2.1): Fast 1400–1800
  words (ceiling 2000) · Medium 1900–2300 words (ceiling 2500) · Slow 2400–2700 words
  (ceiling 3000) — absolute hard cap 3000 words for any category, never exceeded without
  the user's explicit on-record permission. Thematic quality (Gate 1 Check #16) is governed
  primarily by `ssc-story-control-narration-novel-thematic-law`
  (`.claude/guardrails/quality/guardrail-tier0-narrative-quality.md`).

## Sequence

0. **Decision Consultation Gate** (`ssc-narration-p28-pre-prose-decision-consultation-gate`,
   Canon v4.35 Exhaustive Clarity Mandate) — before any planning or drafting, run the
   consultation. This has two parts, both mandatory every time:
   - **Mandatory pacing question (Rule 19.3a):** always ask Fast/Medium/Slow via
     `AskUserQuestion`, with the Anchor-Type-Defaults-derived category marked
     `(Recommended)` and `SKIP — let AI decide` always offered. Never skipped, never assumed,
     regardless of how obvious the default seems.
   - **Narrative-direction branches (Rule 19.3):** ask about any genuine open branch
     (direction, new-character naming, cultivation/technology/combat outcome, emotional/
     relational fork, scope) that outline-planner or this command's own reading of the Canon
     surfaces. Keep asking in further rounds — not just one round — if an answer opens a new
     branch, until no genuine open branch remains (answered or explicitly SKIPped). Never ask
     about anything already settled by the Canon.
1. Invoke **outline-planner** to confirm exactly what this next prose unit covers, using the
   pacing and any branch answers from step 0. **Single-Prose scope:** this plans exactly one
   Prose unit, never more — if outline-planner indicates the structural moment needs a
   second unit afterward, note that for the *next* invocation, do not fold it into this one.
2. Invoke **prose-maker** to draft the unit (one unit only).
3. Invoke **continuity-checker** to run the Gate 1 Post-Draft Audit (16 checks, including
   Part 36 Check #16). On any FAIL: revise via prose-maker and re-audit until clean
   (`guardrails/audit/guardrail-audit-gate-law.md` Correction Protocol) — never proceed with
   a FAIL outstanding.
4. Present the Gate 1 result and wait for an explicit `[CONFIRM WRITE]` / `[REVISE PROSE]` /
   `[SKIP WRITE]` — never assume confirmation. **Presentation format:** show the complete
   six-tier name chain (Phase / Section / Novel-Part / Chapter / Area / Prose, Part 28 Area
   18 Rule 18.3.1) plus Reference Code and declared pacing directly above the prose body,
   then the prose itself, then a concise audit summary — no additional assistant-authored
   commentary wrapped around these blocks. Exactly one Prose unit is ever presented at once.
5. On `[CONFIRM WRITE]`: write the `.docx` and `.md` files via
   `.claude/tools/prose_docx_creator.py` and `.claude/tools/prose_md_creator.py`
   (`guardrails/tools/guardrail-authorized-scripts-only.md` — no other write method).
6. Invoke **continuity-checker** again for the Gate 2 Post-Write Audit (Completeness
   Indicator + Tier Scope Brackets) and the Post-Write Ledger Update
   (`guardrails/ledger/guardrail-ledger-update-law.md`).
7. Invoke **prose-scorer** to record the CDL-2 density score for this unit and update the
   Section running aggregate.
8. Log the outcome to `.claude/story-memory/session-log/`.

## Failure/abort

`[SKIP WRITE]` aborts cleanly with no file written and no ledger update. Any irreconcilable
Gate 1 conflict is escalated via `AskUserQuestion`, never force-written.
