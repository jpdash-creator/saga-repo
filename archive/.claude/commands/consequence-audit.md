---
description: Audit a character's consequence arc against the Part 27 Consequence Severity Scale to verify no consequence has been silently evaded.
argument-hint: <character name>
user-invocable: true
---

# `/consequence-audit`

Corresponds to canon command `[CONSEQUENCE AUDIT]` (C-18).

## Sequence

1. Read the relevant `ssc-character-p27-*` skills (Consequence Severity Scale, Consequence
   Propagation Mechanics, Resolution Pathways).
2. Read the character's ledger entry for its Consequence Arc section.
3. Invoke **continuity-checker** to verify every consequence event established in prose has
   either an ongoing state or a canon-compliant resolution pathway shown on the page — never
   a silent disappearance (`.claude/guardrails/authority/guardrail-prohibited-creative-acts.md`,
   Consequence Evasion; P27-1 applies even to the protagonist).
4. Report any evaded or under-resolved consequence.
