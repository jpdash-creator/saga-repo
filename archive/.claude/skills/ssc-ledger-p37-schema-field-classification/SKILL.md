---
name: ssc-ledger-p37-schema-field-classification
description: Defines how every field in every ledger schema template is classified — Baseline Information (B, locked at entity creation, changeable only via Canon Amendment) versus Living Information (L, updated after every relevant prose unit) — plus the mandatory population rule requiring introducing prose to fully populate established fields at creation rather than leaving them "not yet established." Reach for this when creating a new ledger entry, deciding whether a field can be edited without a Canon Amendment, auditing whether a schema was populated correctly at creation, or reconciling "not yet established" placeholders against source prose. Canon Part 37 Area 5, domain ledger.
user-invocable: false
---

## Rule Text (Verbatim Source — Authoritative)
## Area 5 — Schema Field Classification

Every field in every schema template above is classified as one of two types, inherited from Part 1 Area 5.3:

**Baseline Information (B):** Established at entity creation and locked unless a Canon Amendment explicitly changes it. The initial establishment event is the Prose unit that introduces the entity — fields populated at creation from that prose. Subsequent prose may enrich B fields that are "not yet established" but may not contradict B fields already established without a Canon Amendment.

**Living Information (L):** Updated after every relevant prose unit. The `[L — Updated at...]` notation in each section's footer defines the trigger condition for that section's Living fields.

**Mandatory population rule:** Any field that the introducing prose has established must be populated at file creation. No field established in prose may be left as "not yet established" at creation time. "Not yet established" is reserved exclusively for fields where the introducing prose was genuinely silent.

---

## Cross-References
| Related Skill | Relation | Source |
|---|---|---|
| ssc-cultivation-p03-cultivation-ladder-realm-hierarchy | HARD | Part 34 Area 5: Character schema templates include Cultivation Realm field (Part 3 definitions) |
| ssc-cultivation-p03-lifespan-mechanics | HARD | Part 34 Area 5: Character schema templates include Cultivation Realm field (Part 3 definitions) |
| ssc-cultivation-p03-power-density | HARD | Part 34 Area 5: Character schema templates include Cultivation Realm field (Part 3 definitions) |
| ssc-cultivation-p03-realm-transition | HARD | Part 34 Area 5: Character schema templates include Cultivation Realm field (Part 3 definitions) |
| ssc-cultivation-p03-cultivation-talent | HARD | Part 34 Area 5: Character schema templates include Cultivation Realm field (Part 3 definitions) |
| ssc-cultivation-p03-growth-speed | HARD | Part 34 Area 5: Character schema templates include Cultivation Realm field (Part 3 definitions) |
| ssc-cultivation-p03-power-comparison | HARD | Part 34 Area 5: Character schema templates include Cultivation Realm field (Part 3 definitions) |
| ssc-cultivation-p03-damage-tolerance-recovery | HARD | Part 34 Area 5: Character schema templates include Cultivation Realm field (Part 3 definitions) |
| ssc-cultivation-p03-affinity-cultivation | HARD | Part 34 Area 5: Character schema templates include Cultivation Realm field (Part 3 definitions) |
| ssc-cultivation-p03-heart-cultivation | HARD | Part 34 Area 5: Character schema templates include Cultivation Realm field (Part 3 definitions) |

## Governing Authority
Subordinate to the shared Part 1 (audit law) + Part 34 (knowledge graph) grounding in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.

## Source Provenance
Part 37, Area 5 — "Schema Field Classification" · canon v4.33 · migrated 2026-08-03
