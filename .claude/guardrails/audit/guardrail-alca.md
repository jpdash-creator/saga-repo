# Guardrail: ALCA — Action-Law / Ledger Correctness Audit

**Source:** this guardrail (the audit layer has no skill file) · Canon v10.0
**Applies to:** Continuity Checker (primary owner, especially for `.claude/story-memory/` writes)

## The rule

ALCA audits **operational correctness of rules and ledgers** — not prose quality (FCIA), not
governance structure (CCIA). It runs in two modes:

- **Mode A (reactive)** — fires immediately: on an edit to a Part's skill file, on an accepted
  Area (for Lore Completeness, AL-10), and the instant a forbidden realm-vocabulary
  term appears anywhere — that last is dimension **AL-6 Cultivation Alignment**, the
  same check that enforces `.claude/guardrails/authority/guardrail-prohibited-creative-acts.md`'s forbidden
  realm list.
- **Mode B (session-end)** — a full pass across all 10 dimensions at the close of every
  Section (the session end `guardrail-fcia.md` defines), run together with FCIA end-of-session
  as concurrent agents (the two read different layers) and followed by one Unified Audit
  Summary after both, per the audit chain there, over the Areas of the closing Section.

## The 10 ALCA dimensions (AL-1–AL-10)

| Id | Dimension |
|---|---|
| AL-1 | Rule Internal Consistency |
| AL-2 | Cross-Part Consistency |
| AL-3 | Version Consistency |
| AL-4 | Ledger Format Compliance |
| AL-5 | Ledger Cross-Reference |
| AL-6 | Cultivation Alignment |
| AL-7 | World Alignment |
| AL-8 | Character Law Alignment |
| AL-9 | Canon-Manifest (`.claude/canon-manifest/skill-index.json`) Accuracy |
| AL-10 | Lore Completeness, per Part 28 Area 17 |

These are the ids the Parts' closing audit notes and the ledgers' Audit Hook lines cite.

## Hard rules

- A forbidden-vocabulary hit anywhere (prose, dialogue, ledger entry, or governance text
  itself) is an ALCA Mode A failure — correct it immediately, do not wait for session end.
  Naming the terms inside a prohibition list (Part 28 Area 12.2, the prohibited-acts guardrail,
  a ledger's required "Forbidden Realm Vocabulary" statement) is not a hit.
- Ledger Format Compliance (AL-4) means every `.claude/story-memory/ledger-*/` file is checked
  against its Part 37 schema — drift (e.g. a missing Lore Section block) is *flagged*, not
  silently normalized; fixing schema drift is the Continuity Checker's ongoing job, done
  transparently, not folded into an unrelated prose update.
- Part 40: AL-4 checks `ledger-character-monster/` against Part 37 Area 3.10 and the
  villain tier tables against Area 2.11; AL-10 reads monsters in both directions (a monster Kind or
  a Tier C or D monster in a written Area with no entry; an entry whose Kind, stage or traits the
  Area contradicts); AL-8 reads the line between monster and villain (a non-sentient monster filed
  as a villain is a finding; so is a sentient monster in a Phase 1 file, Law P30-L9).
- Part 41: AL-4 checks `ledger-worlds-calendar/_index.md` against
  Part 37 Area 3.11, and AL-5 reads the date line and the calendar ledger in both directions: the date line,
  the first line of the text of each written Area file, agrees with the Area row that
  records that Area, and a recorded date has a written Area behind it; each Chapter, Novel-Part, Section and
  Phase row equals the rollup of the rows beneath it, and the Current Position block names the latest written
  Area and its date. A difference is flagged, never silently normalized. A ledger row that disagrees with a
  written line is rebuilt from the file (`/force-ledger-audit`), and a wrong line in a written file is
  corrected only through `/revise-area` or a redraft (Part 2 Rule 5.3.2a).

## Escalation

An ALCA finding that implies a ledger schema change (not just a data fix) routes to
`.claude/guardrails/ledger/guardrail-ledger-schema-law.md` and requires explicit confirmation before altering
the schema itself.
