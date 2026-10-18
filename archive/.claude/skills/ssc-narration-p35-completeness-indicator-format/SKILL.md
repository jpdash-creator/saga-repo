---
name: ssc-narration-p35-completeness-indicator-format
description: Defines the exact CDL-2 Content Density Law completeness-indicator block formats — the Prose-Unit Score block (4.1), the Chapter-Level Aggregate block (4.2), and the Section-Close Audit block (4.3) — including their headers, category rows (Combat, Named Moves & Techniques, Cultivation Growth, Technology, Lore & World-Building, Dialogue & Social, Information & Intrigue, Consequence & Psychology, Travel & Discovery, Political & Faction), target-range and PASS/WARN/FAIL status notation; reach for this any time a Prose unit is completed and the standard Completeness Indicator is generated, at Chapter-close when displaying the running CDL-2 aggregate with WARN triggers, or at Section-close when running the enforcement CDL-2 Section Audit that gates Phase progression; this is canon Part 35 Area 4, domain narration.
user-invocable: false
---

## Rule Text (Verbatim Source — Authoritative)
## Area 4 — Completeness Indicator Format

### 4.1 — CDL-2 Prose-Unit Block

After every Prose unit is written and the standard Completeness Indicator is generated (per Part 2 and Part 1 Rule 7.1.1), the CDL-2 scoring block is appended. The format is:

```
═══════════════════════════════════════════════════════
CDL-2 CONTENT DENSITY — PROSE UNIT SCORE
Section: [Section Number — Section Name]
Prose Unit: [Novel-Part / Chapter / Area / Prose Name]
Prose Word Count: [estimated word count]
───────────────────────────────────────────────────────
★ COMBAT:                    [X%]
   NAMED MOVES & TECHNIQUES: [X%]
★ CULTIVATION GROWTH:        [X%]
   TECHNOLOGY:               [X%]
★ LORE & WORLD-BUILDING:     [X%]
★ DIALOGUE & SOCIAL:         [X%]
   INFORMATION & INTRIGUE:   [X%]
   CONSEQUENCE & PSYCHOLOGY: [X%]
   TRAVEL & DISCOVERY:       [X%]
   POLITICAL & FACTION:      [X%]
───────────────────────────────────────────────────────
SECTION RUNNING AGGREGATE (all Prose to date in Section [N]):
★ COMBAT:                    [X%] [target: 30–42–55%] [STATUS: ON TRACK / WARN / FAIL]
   NAMED MOVES & TECHNIQUES: [X%] [target: 10–18–28%] [STATUS: ON TRACK / WARN]
★ CULTIVATION GROWTH:        [X%] [target: 25–35–45%] [STATUS: ON TRACK / WARN / FAIL]
   TECHNOLOGY:               [X%] [target: 12–22–32%] [STATUS: ON TRACK / WARN]
★ LORE & WORLD-BUILDING:     [X%] [target: 42–55–65%] [STATUS: ON TRACK / WARN / FAIL]
★ DIALOGUE & SOCIAL:         [X%] [target: 45–58–68%] [STATUS: ON TRACK / WARN / FAIL]
   INFORMATION & INTRIGUE:   [X%] [target: 12–22–32%] [STATUS: ON TRACK / WARN]
   CONSEQUENCE & PSYCHOLOGY: [X%] [target: 18–28–38%] [STATUS: ON TRACK / WARN]
   TRAVEL & DISCOVERY:       [X%] [target: 8–15–25%]  [STATUS: ON TRACK / WARN]
   POLITICAL & FACTION:      [X%] [target: 18–28–38%] [STATUS: ON TRACK / WARN]
[Section N Prose units completed: X | Word count: X,XXX]
═══════════════════════════════════════════════════════
```

*Note: The Section target values shown in the Running Aggregate block update automatically to the correct Section's Low–Anchor–High range from Area 3 for the Section currently being authored.*

---

### 4.2 — Chapter-Level CDL-2 Aggregate Block

At Chapter-close, the CDL-2 aggregate is displayed with explicit WARN triggers for any Universal Anchor Floor category that is tracking below its Section Anchor on a trajectory that would produce a Section-close Hard FAIL:

```
═══════════════════════════════════════════════════════
CDL-2 CHAPTER-LEVEL AGGREGATE — [Chapter Name]
Chapter word count: [X,XXX]
Section [N] aggregate to date (all prose in Section [N]):
───────────────────────────────────────────────────────
★ COMBAT:                    [X%] → Section target: [Low–Anchor–High] [ON TRACK / ⚠ WARN]
   NAMED MOVES & TECHNIQUES: [X%] → Section target: [Low–Anchor–High] [ON TRACK / ⚠ WARN]
★ CULTIVATION GROWTH:        [X%] → Section target: [Low–Anchor–High] [ON TRACK / ⚠ WARN]
   TECHNOLOGY:               [X%] → Section target: [Low–Anchor–High] [ON TRACK / ⚠ WARN]
★ LORE & WORLD-BUILDING:     [X%] → Section target: [Low–Anchor–High] [ON TRACK / ⚠ WARN]
★ DIALOGUE & SOCIAL:         [X%] → Section target: [Low–Anchor–High] [ON TRACK / ⚠ WARN]
   INFORMATION & INTRIGUE:   [X%] → Section target: [Low–Anchor–High] [ON TRACK / ⚠ WARN]
   CONSEQUENCE & PSYCHOLOGY: [X%] → Section target: [Low–Anchor–High] [ON TRACK / ⚠ WARN]
   TRAVEL & DISCOVERY:       [X%] → Section target: [Low–Anchor–High] [ON TRACK / ⚠ WARN]
   POLITICAL & FACTION:      [X%] → Section target: [Low–Anchor–High] [ON TRACK / ⚠ WARN]
[If any ⚠ WARN is present: Narrative correction guidance for next prose unit]
═══════════════════════════════════════════════════════
```

---

### 4.3 — Section-Close CDL-2 Audit Block

At Section-close, a full CDL-2 Section Audit is conducted and displayed. This is the enforcement checkpoint:

```
═══════════════════════════════════════════════════════
CDL-2 SECTION-CLOSE AUDIT — Section [N]: [Section Name]
Total Section word count: [X,XXX]
Total Prose units: [X]
───────────────────────────────────────────────────────
★ COMBAT:
   Section Aggregate: [X%]
   Section Target:    [Low–Anchor–High]
   Status: [✓ PASS (within range) / ⚠ WARN (outside range) / ✗ FAIL (below Anchor floor)]

★ CULTIVATION GROWTH:
   Section Aggregate: [X%]
   Section Target:    [Low–Anchor–High]
   Status: [✓ PASS / ⚠ WARN / ✗ FAIL]

★ LORE & WORLD-BUILDING:
   Section Aggregate: [X%]
   Section Target:    [Low–Anchor–High]
   Status: [✓ PASS / ⚠ WARN / ✗ FAIL]

★ DIALOGUE & SOCIAL:
   Section Aggregate: [X%]
   Section Target:    [Low–Anchor–High]
   Status: [✓ PASS / ⚠ WARN / ✗ FAIL]

NAMED MOVES & TECHNIQUES:   [X%] → [Low–Anchor–High] → [✓ ON TRACK / ⚠ WARN]
TECHNOLOGY:                  [X%] → [Low–Anchor–High] → [✓ ON TRACK / ⚠ WARN]
INFORMATION & INTRIGUE:      [X%] → [Low–Anchor–High] → [✓ ON TRACK / ⚠ WARN]
CONSEQUENCE & PSYCHOLOGY:    [X%] → [Low–Anchor–High] → [✓ ON TRACK / ⚠ WARN]
TRAVEL & DISCOVERY:          [X%] → [Low–Anchor–High] → [✓ ON TRACK / ⚠ WARN]
POLITICAL & FACTION:         [X%] → [Low–Anchor–High] → [✓ ON TRACK / ⚠ WARN]
───────────────────────────────────────────────────────
CDL-2 SECTION RESULT:
[✓ PASS — All four Universal Anchor Floors met; no Hard FAIL categories]
[OR]
[✗ HARD FAIL — [Category/ies] below Anchor floor. Resolution required before Phase progression.]
[OR]
[⚠ ADVISORY WARN — All Anchor Floors met; [Category/ies] outside Advisory range. Logged to SSC Canon event log.]
═══════════════════════════════════════════════════════
```

---

## Cross-References
| Related Skill | Relation | Source |
|---|---|---|
| (none resolved from the manifest for this Area) | | |

## Governing Authority
Subordinate to the shared Part 1 (audit law) + Part 34 (knowledge graph) grounding in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.

## Source Provenance
Part 35, Area 4 — "Completeness Indicator Format" · canon v4.33 · migrated 2026-08-03
