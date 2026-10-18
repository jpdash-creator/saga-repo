---
description: Audit a character's consequence arc against the Part 27 Consequence Severity Scale to verify no consequence has been silently evaded.
argument-hint: <character name>
user-invocable: true
---

# `/consequence-audit`

Corresponds to canon command `[CONSEQUENCE AUDIT]` (C-18).

## Sequence

1. Read `character-consequence-law` — the primary single-file read for all of Part 27
   (Consequence Severity Scale, Consequence Propagation Mechanics, Resolution Pathways).
2. Read the character's ledger entry for its Consequence Arc section.
3. Invoke **continuity-checker**, starting from the character's Canon Events Log rows (ledger
   Section 10) and reading each cited Area under its Area window (not every written Area), to
   verify every consequence event those rows establish has either an ongoing state or a
   canon-compliant resolution pathway shown on the page — never a silent disappearance (`.claude/guardrails/authority/guardrail-prohibited-creative-acts.md`,
   Consequence Evasion; Part 27 Standard N27-6 applies even to the protagonist).
   Never read, list or count files under `_archive`; read each window file by its exact
   path.
4. Report any evaded or under-resolved consequence. List, as information only, each open CSS-3+ event
   whose IC class window (Part 27 Area 1.3) has passed with no effect shown on the page. The IC
   classes say when a consequence usually shows up; they are not a deadline. The story and the
   Chapter Spec decide when a consequence lands, and nothing here blocks an Area.

## When it runs

The author runs it. The Post-Write Ledger Update lists each CSS-7+ event written to a ledger and
prompts the author to run `/consequence-audit <character>`. It is never run automatically.
