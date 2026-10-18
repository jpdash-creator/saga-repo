---
description: Begin the Starward Saga from a clean state -- Prose 1 of Phase 1, Section 1, Novel-Part 1, Chapter 1, Area 1.
user-invocable: true
---

# `/start-story`

Corresponds to canon command `[START STORY]` (C-3). Use only when `projects/novel-starward-saga/`
has no existing prose (a true fresh start) or immediately after `/hard-reset`.

## Sequence

1. Confirm `projects/novel-starward-saga/phase-1/` has no `prose-*` files yet — if it does,
   stop and ask whether the intent was `/next-prose` instead.
2. Read `.claude/guardrails/_index.md` in full, plus the `ssc-narration-p02-*` (six-tier
   structure), `ssc-narration-p30-*` (macro arc / Phase 1 framework), and `ssc-narration-p28-*`
   (creative flexibility) skills that establish how a story opens.
3. Run the **Decision Consultation Gate** exactly as `/next-prose` Step 0 (Canon v4.35 —
   mandatory pacing question every time, plus persistent multi-round narrative-direction
   consultation until no genuine open branch remains). For the opening of the entire novel
   this typically has real, high-consequence open branches (which thread/character opens the
   book, what the opening beat is, and whether it needs a wide establishing unit before a
   close character unit per the Single-Prose scope rule) — do not under-consult here just
   because it is the first invocation of the session.
4. Invoke **outline-planner** to establish the opening scene/beat for Prose 1, using the
   answers from step 3. **Single-Prose scope applies**: this plans exactly one Prose unit
   (`phase-1/section-1/part-1/chapter-001/area-1/prose-00001`). If the opening genuinely
   needs a wide establishing unit before the first close character unit, that is Prose 1 and
   Prose 2 as two full, separately-confirmed `/next-prose`-equivalent cycles — never planned
   or drafted together.
5. Proceed exactly as `/next-prose` from step 2 onward (draft -> Gate 1 -> confirm -> Gate 2
   -> ledger update -> score) for that single Prose unit, including the Gate 1 presentation
   format rules (full six-tier name chain shown, no extra wrapper commentary, one Prose
   presented at a time).

## Failure/abort

If prose already exists, do not overwrite silently — escalate via `AskUserQuestion`.
