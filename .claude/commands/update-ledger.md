---
description: Manually update a specific entity's ledger entry outside the normal post-write flow (e.g. to correct or enrich a field directly).
argument-hint: <entity name>
user-invocable: true
---

# `/update-ledger`

Corresponds to canon command `[UPDATE LEDGER: entity]` (C-15). See
`.claude/guardrails/commands/guardrail-plan-then-auto-execution.md` for this command's Plan
Mode → Auto Mode execution shape.

## Plan Mode → Auto Mode

Step 2 (the correction confirmation) is this command's **Plan Mode** — the exact example
named in the guardrail itself: whether this is a routine enrichment or actually contradicts
a Baseline field (requiring a Canon Amendment instead of a routine update) is asked and
resolved here before anything is applied. Once resolved, Step 3 runs in **Auto Mode** — but
Auto Mode never waives the Step 2 stop itself: a Baseline-field contradiction still halts
for an explicit amendment decision every time, never silently proceeds
(`guardrails/commands/guardrail-plan-then-auto-execution.md`).

## Sequence

1. Invoke **continuity-checker** to read the entity's current ledger file. If the author's
   message did not state the change, ask the author for it before going on.
2. Confirm the proposed change: enrichment of a blank/Living field is fine; contradicting an
   existing Baseline (B) field requires a formal Canon Amendment, not a routine update
   (`.claude/guardrails/ledger/guardrail-ledger-schema-law.md`) — stop and ask if that's what's
   being requested. Three further rules apply: a Section 12 entry is never edited (append a
   superseding entry); a change to Section 11.2, 11.3 or 11.6, which are Baseline, goes through a
   Check #21 ruling or a Canon Amendment; and if the new value differs from what a written Area
   shows, name that Area and offer `/revise-area` for it (the ledger beats the Area on conflict,
   so it would otherwise win with no follow-up).
3. Show each field changed as old to new, then apply the change and append the old value to the
   file's changelog line (`Updated <date>: <old> to <new>, <reason>`). Update `Last Updated` /
   `Ledger Version`, and regenerate the folder's `_index.md` entry for this file. An agreed Canon
   Amendment is applied by the Canon Amendment procedure in
   `.claude/guardrails/ledger/guardrail-ledger-schema-law.md`, which appends `Amended <date>: ...`
   to the same changelog.

## Rename pass (Part 28 Rule 18.4.4)

Retitling a delivered Chapter or Area is one pass of this command with the container as the entity. The author names the old and the new name, and that ruling is the Canon amendment Step 2 asks for. The pass rewrites the old name to the new one in every ledger event row that carries one of the container's Reference Codes, keeps each row's full name-chain (Part 28 Rule 18.3.4) and changes nothing else. `/revise-area` is needed only for a Chapter name.

## Failure/abort

Never silently contradict a Baseline field — surface it as an amendment decision instead.
