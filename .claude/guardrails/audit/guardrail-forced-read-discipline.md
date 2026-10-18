# Guardrail: Forced-Read Discipline (Never Recall the Canon Manifest From Memory)

**Source:** this guardrail (the manifest has no skill file) · Canon v10.0
**Applies to:** all 4 agents, but binds the Continuity Checker most directly

## The rule

The canon manifest (`.claude/canon-manifest/*.json`, the canon's
knowledge graph) must be **physically re-read from disk**, never answered from memory or
from what a prior turn's summary said, at three fixed checkpoints:

1. **Pre-Area Read** — by the Continuity Checker, run beside the drafting and finished
   before the draft is evaluated.
2. **Gate 1 Audit Pass** — when the Continuity Checker consults the dependency graph to
   verify cross-Part consistency.
3. **Gate 2 Audit Pass** — when the Continuity Checker re-verifies against the manifest a
   second time, after the file is written, not just once before drafting.

**What a checkpoint read consists of.** Each read is targeted, and it is still a real
re-read from disk, never from memory:

- `dependency-graph.json`, `domain-map.json` and `ledger-architecture-map.json` are read in
  full (about 2,200 lines together).
- `skill-index.json` is read only for the Part and Area rows the Area touches, found by
  searching the file in that turn.
- Only this index file is read selectively. Every Part skill and every ledger is still read
  in full, as Gate 1 and Gate 2 require.
- At Gate 1 the read belongs to the 23-check instance. The Area flow review instance
  (Check #16 dimension 16-J) checks no cross-Part edge and makes no manifest re-read.
- **Spec reads are not part of this manifest rule, and one exception to the read-in-full rule
  applies to them (Part 38 Rule 9.9.2).** The
  per-Area agents (Area Maker, Area Scorer, both Gate 1 checker instances, and the Outline
  Planner when it plans one Area) read the Chapter Spec in full and, from its Novel-Part Spec,
  only the header block and the closing-state block; the Section Spec is not read. That is an
  explicit exception to "every mandatory read stays in full", and it cuts nothing down: those
  upper-spec reads are simply not mandatory for a per-Area agent, because the Chapter Spec
  carries what it needs from above, each item's source recorded in its Audit and Settlement Notes. An agent that BUILDS or
  audits a spec still reads the whole chain above that spec in full.

Omission of any of these three reads is a **blocking FAIL / Critical Violation**, not a
minor note. This is the single most load-bearing anti-hallucination rule in the whole
system: it exists specifically because an agent's confident recollection of "what the
knowledge graph probably says" is exactly the failure mode this project was restructured to
eliminate (see the "skill grain" decision — the same principle, applied to the manifest itself).

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
