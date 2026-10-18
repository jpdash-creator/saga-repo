---
description: Register or re-register a character's Part 39 Behavioral Signature — the 36-Layer behavioral profile written into Character Ledger Sections 11 and 12, built through an AskUserQuestion interview against the coded option catalog.
argument-hint: <character name> [| --review | --status | --derive-all]
user-invocable: true
---

# `/character-behavior`

Builds a character's **Part 39 Behavioral Signature** — the registered profile that governs how
they move, speak around speaking, decide, fight, practise, wait, care, conceal, and change
across the story. Writes Character Ledger **Section 11** (Behavioral Signature) and creates
**Section 12** (Behavioral Evolution Log).

Governing authority: `character-behavioral-synthesis-law` (Part 39, Tier 0), Areas 3, 4, 41 and 45.
Schema authority for the ledger sections: `ledger-schema-law` Areas 2.1/2.2/2.3.
Guardrail: `guardrails/quality/guardrail-behavioral-authenticity.md`.

## Why this exists

Part 28 Area 6.5 forbids rendering characters as governance outputs executing their category
definitions. That is a prohibition, not a specification — it tells the prose what not to read
like without giving anyone anywhere to record what this particular person actually does. This
command produces that record, before the prose is written (Part 39 P39-2).

## Modes

| Invocation | Effect |
|---|---|
| `/character-behavior <name>` | Full registration interview and write |
| `/character-behavior <name> --review` | Re-present the derived-value digest for override without re-asking the ASKED dimensions |
| `/character-behavior <name> --status` | Read-only: report registration completeness, Signature count and spread, missing usual drift entries |
| `/character-behavior <name> --derive-all` | Opt-in: no asked rounds; every dimension is derived with its evidence, and the author edits once, in the digest |

## Plan Mode / Auto Mode

Per `guardrails/commands/guardrail-plan-then-auto-execution.md`, this command's **Plan Mode**
is the interview: every author-facing question is asked and resolved, and the derived-value
digest is accepted, before any file is written. **Auto Mode** is the write
and the verification. The Exhaustive Clarity Mandate is not shortened by Auto Mode — asking
exhaustively and then proceeding autonomously are sequential requirements, not alternatives.

## Sequence (Part 39 Area 45.2)

1. **Ground** — read the character's full ledger file, their `_index.md` row, every ledger that
   cross-references them, their registered Part 29 prosodic signatures, and the Collective
   Behavior Code of every faction, civilization and location they are bound to. Read Part 39
   in full. Batch these reads in one message (parallel-execution mandate).
2. **Derive** — produce a provisional value for all 291 dimensions (L35's three are written `[N-A]`, Part 39 Area 39): `[DERIVED]` with inline
   evidence, `[N-A]` with a stated reason, or flagged `ASK`.
3. **Ask — identity core** — first `AskUserQuestion` round: Signature candidates, the immutable
   core (L31), the two contradiction pairs and the costly behavior (L36). These determine
   everything downstream and are asked first.
4. **Ask — layer defining** — one defining dimension per Layer not already settled, plus every
   `ASK`-flagged dimension. Roughly 10–13 calls total across steps 3–5 for a Hero, Villain or Tier A
   character; Tier B and Tier C use the lighter routes below.
5. **Ask — drift** — the Conditional Drift Map: the six usual entries (first kill, first
   significant defeat, first PIS-5, next realm/tier crossing, next age-band crossing, loss of
   the most significant relationship) plus any arc-specific triggers.
6. **(retired)** — Layer L35 is retired: no registration is checked against another. Its three
   dimensions are written `[N-A]` and count toward completeness (36/36 Layers, 291/291 dimensions
   addressed, 288 of them live).
7. **Digest** — present every derived value grouped by Layer, with its evidence, for
   plain-language override. Nothing is written until the digest is accepted.
8. **Write** — Section 11 (all seven blocks) and Section 12 (headers, empty log). Update the
   `_index.md` row and any collective code's member list.
9. **Verify** — Layer count, Signature count, Signature spread across Layers, contradiction
   pairs, costly behavior, usual drift entries, and the coherence sweep of the named overlapping
   dimension pairs (Part 39 Area 45.2 Step 9); each is reported as information, and no
   Signature is added or removed to meet a count.

## Question construction

- Options are **concrete behaviors quoted from the coded catalog with their codes shown**,
  never categories. "Disciplined / relaxed / severe" is a violation of Part 39 P39-3.
- Where derivation produced a favored value it is presented **first, with its evidence stated
  in the option description**, so the author confirms a reasoned proposal rather than deciding
  cold.
- The `-99` AUTHOR-SPECIFIED route is always reachable. The interview never forces a catalog
  option.

## Tier requirements (Part 39 Area 4.1)

The counts below are the interview's aim for each tier; they guide the registration and are never a gate on the story.

| Tier | Layers | Signatures | Contradiction pairs | Costly behavior |
|---|---|---|---|---|
| Hero / Villain (Tier A or Tier B) / Tier A / Tier B / sentient monster | all 36 | 12 | 2 | 1 |
| Tier C (a side character, or a Tier C side villain) | mandatory-core 6 (L01, L03, L08, L10, L29, L34) | 1 | 0 | 0 |
| Tier D (a side character, or a Tier D side villain) | none registered (a picked code, Part 39 Section 3.5) | 0 | 0 | 0 |

Hero, Villain, Tier A and Tier B write to their own ledger file (for Tier A and Tier B,
`ledger-character-side/[name].md`). Tier C writes a one-paragraph behavioral line in its
functional row. *(A Tier C or Tier D side villain keeps its line or code in
`ledger-character-villain/_index.md` (Part 18 Area 6.3). A sentient monster writes to its own file in
`ledger-character-monster/` with `B39-L32-TYPE-06`; a non-sentient monster has no Part 39 registration, only
the Part 40 trait lines, and this command does not run for it.)*

Tier D is not registered by this command: the drafting agent picks the Tier D code while it drafts
(Part 39 Section 3.5). This command runs for a Tier D person only on the
author's promotion ruling; the promotion digest then opens with the row's `[AI]` tokens and carries
the code as Part 39 Rule 39.4.3.2a says.

## Lighter routes for Tier B and Tier C (Part 39 Rule 39.45.1.4)

The registration written is the same at every tier; only the number of questions changes.

- **Tier B** — ask only the 12 Signatures (each with its origin), the two contradiction pairs and
  the costly behavior, usually about 16 dimensions in about 4 calls. Derive every other dimension,
  the six usual drift entries included, each with inline evidence. Present one digest batched
  for the scene cast, each character's block standing alone. A derived line with no evidence is
  marked `ASK` in the digest and answered there.
- **Tier C** — ground (step 1), derive the mandatory-core six with evidence, and ask only the one
  Signature and its origin, usually in 1 to 2 calls. The six derived lines are shown in the same
  round; nothing is written until they are accepted.
- The call counts are information only, never a gate. Hero, Villain and Tier A use the full route.

## The `--derive-all` route (opt-in)

Off unless the author passes `--derive-all`; the full interview above stands for every other
registration. With the flag, Steps 3 to 5 (the asked rounds) are not run. Step 2 derives every
dimension, including the ones the full route would have asked: the Signature candidates with
their origins, the immutable core, the two contradiction pairs, the costly behavior, one
defining dimension per Layer and the drift entries. Each is `[DERIVED]` with its evidence
inline (Part 39 Rule 39.45.1.2). A line with no evidence, and a Signature with no origin, is not
guessed: it is marked `ASK` in the digest and answered there, as in the Tier B route.

The author edits once, in the Step 7 digest, and nothing is written until the digest is
accepted. A value the author changes there is written `[ASKED]`; a value left as proposed stays
`[DERIVED]`. The tier requirements, Step 8 and Step 9 are unchanged.

## Hard rules

- **No prosodic re-registration.** Part 29's nine determinants stay in the Prosodic Signatures
  field and are never restated as Part 39 behavior (Rule 39.2.3.1).
- **No inner-state adjudication.** This command never sets or revises a PIS level, CSS grade,
  IE event, ideology category, Heart level or realm (Rule 39.2.3.2).
- **Every Signature names its origin** (Layer L34). A Signature without provenance is rejected.
- **Every `[DERIVED]` value cites its evidence inline.** "Seems likely" is not evidence.
- **Section 11 is populated in full at registration** (Part 39 Rule 39.41.5.1). A partially
  populated Section 11 is a registration in progress; the character is drafted into an acting
  appearance once the author has set what the story needs (Rule 39.4.3.1). For a Tier C person
  improvised in the prose, a Layer the prose did not settle is marked `OPEN-AREA` and set by the
  first Area that shows it (Rule 39.4.2.1).
- **Registration does not run for a character who already has one** except on tier promotion,
  on a Layer opening (e.g. L17 when an age gate lifts), or on explicit author instruction.
  Ordinary change flows through the drift mechanism and Check #21, never through re-interview.

## Related

`/review-ledger` and `/character-sheet` read the result. `/chapter-spec` consumes it into the
per-Area Behavioral Plan. `/next-area` enforces it at Gate 1 Checks #20 and #21.
`/character-behavior <name> --status` reports one character's registration gaps.
