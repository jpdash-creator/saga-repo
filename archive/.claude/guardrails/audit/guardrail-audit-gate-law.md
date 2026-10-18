# Guardrail: The Two-Gate Audit Pipeline

**Source:** Part 1 (Governance and Audit Law), Areas 4, 7, 9, 10
**Applies to:** all 4 agents — this is the backbone every `/next-prose`-style command runs through

## The rule

Every narrative output is validated against the complete applicable canon before it is
accepted. No prose is written to disk, and no ledger is updated, outside this sequence:

1. **Pre-Write Ledger Check** (Part 1 Area 6.2) — read current state from
   `.claude/story-memory/ledger-*/` before drafting anything.
2. **Draft** — Prose Maker writes the prose unit (never the file yet).
3. **Gate 1 — Post-Draft Audit** (Area 9): a 16-check mandatory sequence run before any
   `[CONFIRM WRITE]` offer, performed by the Continuity Checker:
   Parts checked (all 36) · Ledgers checked (all folders) · no em-dashes · no contractions ·
   dialogue format `*"..."*` · filter language (advisory) · Named Moves / CDL2-L6 ·
   cultivation realm accuracy · deep POV maintained · pacing word count · Part 30
   Phase-1-framework compliance · bold-italic formatting · Part 34 dependency-map
   consultation · character ledger state verification · ledger obligation scan · Novel
   Thematic Compliance (Part 36 Check #16, 6 sub-dimensions). **A Gate 1 skipped entirely,
   or delivered with any single check FAILing, is a Rule 9.1 Critical Violation** — Gate 2
   is blocked until a clean re-audit.
4. **Inter-Gate Confirmation** — `[CONFIRM WRITE]` / `[REVISE PROSE]` / `[SKIP WRITE]`,
   required on every single prose unit, every time. No exceptions for "obviously fine" units.
5. **Gate 2 — Post-Write Audit** (Area 10): file creation only via the authorized
   `.claude/tools/prose_docx_creator.py` / `prose_md_creator.py` scripts (see
   `tools/guardrail-authorized-scripts-only.md`). Two mandatory blocks follow every write:
   Block A (Completeness Indicator: carry-forward checks, ledger-obligation discharge, tier
   hierarchy counts, CDL-2 ten-category scoring) and Block B (Tier Scope Brackets).
6. **Post-Write Ledger Update** (Part 1 Area 6.3 / command `/force-ledger-audit`) —
   mandatory, not optional, every time prose changes canon state.

## Hard rules

- **Full-Canon Named-Result Check.** Every audit pass evaluates all 36 applicable Parts by
  name — Triggered / Not Triggered / N/A. Silent omission of any Part is itself a POST-AUDIT
  FAIL.
- **One-Prose-Per-Invocation.** Never batch multiple prose units through a single Gate
  1→Gate 2 pass.
- **Pre-Prose Read Mandate.** All governing Parts + all relevant ledgers + all prior stored
  prose files must be (re-)read before drafting — no exception on grounds of session
  boundary (this is the files-only discipline; see `ledger/guardrail-session-log-not-canon.md`).
- **Correction Protocol** on any FAIL: Acknowledge → Prioritize → Revise → Re-Audit → Iterate.
  Termination only on Clean Audit, Diminishing Returns, Irreconcilable Conflict, or
  Structural Impossibility — never on "close enough."

## Escalation

A conflict discovered mid-audit is never resolved silently — surface it and, where the
canon itself calls for it (e.g. a new antagonistic character crossing into villain
territory), stop and ask via `AskUserQuestion` before proceeding.
