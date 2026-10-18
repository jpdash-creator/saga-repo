---
description: Audit a character's ideology state and history against the Part 20 Ideology Ledger framework.
argument-hint: <character name>
user-invocable: true
---

# `/ideology-audit`

Corresponds to canon command `[IDEOLOGY AUDIT]` (C-17).

## Sequence

1. Read the relevant `ssc-character-p20-*` skills (Ideology Taxonomy, Ideology Ledger,
   Ideological Governance by Context).
2. Read the character's ledger entry in `.claude/story-memory/ledger-character-{hero,side,villain}/`.
3. Invoke **continuity-checker** to verify the character's ideology arc across all written
   prose is internally consistent (no unearned reversal — see
   `.claude/guardrails/authority/guardrail-prohibited-creative-acts.md`, Causally Unsupported
   Behavioral Reversals) and that the Ideology Ledger section is current.
4. Report findings; flag any gap between prose and ledger for a Post-Write Ledger Update.
