---
description: Audit a character's ideology state and history against the Part 20 Ideology Ledger framework.
argument-hint: <character name>
user-invocable: true
---

# `/ideology-audit`

Corresponds to canon command `[IDEOLOGY AUDIT]` (C-17).

## Sequence

1. Read `character-ideology-law` — the primary single-file read for all of Part 20
   (Ideology Taxonomy, Ideology Ledger, Ideological Governance by Context).
2. Read the character's ledger entry in `.claude/story-memory/ledger-character-{hero,side,villain}/`.
3. Invoke **continuity-checker**, starting from the character's Canon Events Log rows (ledger
   Section 10) and reading each cited Area under its Area window (not every written Area), to
   verify the character's ideology arc is internally consistent (no unearned reversal — see
   `.claude/guardrails/authority/guardrail-prohibited-creative-acts.md`, Causally Unsupported
   Character Behavioral Reversals) and that the Ideology Ledger section is current.
   Never read, list or count files under `_archive`; read each window file by its exact
   path.
4. Report findings; flag any gap between the written Areas and the ledger for a Post-Write Ledger Update.
