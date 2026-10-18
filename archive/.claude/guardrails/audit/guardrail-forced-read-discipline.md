# Guardrail: Forced-Read Discipline (Never Recall Part 34 From Memory)

**Source:** Part 34 (Knowledge Graph), Rule 1.1.6
**Applies to:** all 4 agents, but binds the Continuity Checker most directly

## The rule

The canon manifest (`.claude/canon-manifest/*.json`, the migrated form of Part 34's
knowledge graph) must be **physically re-read from disk**, never answered from memory or
from what a prior turn's summary said, at three fixed checkpoints:

1. **Pre-Prose Read** — before Outline Planner or Prose Maker commits to what happens next.
2. **Gate 1 Audit Pass** — when the Continuity Checker consults the dependency graph to
   verify cross-Part consistency.
3. **Gate 2 Audit Pass** — when the Continuity Checker re-verifies against the manifest a
   second time, after the file is written, not just once before drafting.

Omission of any of these three reads is a **blocking FAIL / Critical Violation**, not a
minor note. This is the single most load-bearing anti-hallucination rule in the whole
system: it exists specifically because an agent's confident recollection of "what the
knowledge graph probably says" is exactly the failure mode this project was restructured to
eliminate (see the "skill grain" decision — the same principle, applied to Part 34 itself).

## Hard rules

- A cross-reference cited in a skill's "Cross-References" table, an agent's reasoning, or an
  audit report must trace back to an actual row read from `canon-manifest/dependency-graph.json`,
  `domain-map.json`, or `skill-index.json` in *that same turn* — not to a remembered impression of it.
- The Symbolic layer (formal dependency/edge facts) always prevails over any semantic/
  similarity-style inference in a conflict — semantic similarity is advisory only, never
  authoritative.

## Escalation

If the manifest appears stale, incomplete, or contradicts what a skill file says, that is a
CCIA-worthy finding — report it, don't silently patch around it.
