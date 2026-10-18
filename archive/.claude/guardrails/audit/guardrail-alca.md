# Guardrail: ALCA — Action-Law / Ledger Correctness Audit

**Source:** Part 1 (Governance and Audit Law), Area 8.13
**Applies to:** Continuity Checker (primary owner, especially for `.claude/story-memory/` writes)

## The rule

ALCA audits **operational correctness of rules and ledgers** — not prose quality (FCIA), not
governance structure (CCIA). It runs in two modes:

- **Mode A (reactive, AT-1–AT-8)** — fires immediately on specific triggers (e.g. a forbidden
  realm-vocabulary term appearing — this is dimension **AL-6 Cultivation Alignment**, the
  same check that enforces `authority/guardrail-prohibited-creative-acts.md`'s forbidden
  realm list).
- **Mode B (session-end)** — a full pass across all 10 dimensions at the close of every
  session, always run after FCIA end-of-session per the audit chain in `guardrail-fcia.md`.

## The 10 ALCA dimensions (AL-1–AL-10)

Rule Internal Consistency · Cross-Part Consistency · Version Consistency · Ledger Format
Compliance · Ledger Cross-Reference · Cultivation/World/Character Part Alignment ·
SSC_Canon.md (canon-index) Accuracy · **AL-10 Lore Completeness** per Part 28 Area 17.

## Hard rules

- A forbidden-vocabulary hit anywhere (prose, dialogue, ledger entry, or governance text
  itself) is an ALCA Mode A failure — correct it immediately, do not wait for session end.
- Ledger Format Compliance (AL-4) means every `.claude/story-memory/ledger-*/` file is checked
  against its Part 37 schema — drift (e.g. a missing Lore Section block) is *flagged*, not
  silently normalized; fixing schema drift is the Continuity Checker's ongoing job, done
  transparently, not folded into an unrelated prose update.

## Escalation

An ALCA finding that implies a ledger schema change (not just a data fix) routes to
`ledger/guardrail-ledger-schema-law.md` and requires explicit confirmation before altering
the schema itself.
