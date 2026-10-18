# Guardrail: Tier-0 Narrative Quality (Novel Primacy Mandate)

**Source:** Part 36 (Narration Novel Thematic Law), Areas 1, 16
**Primary reference (Canon v4.34):** `ssc-story-control-narration-novel-thematic-law` — a single-file, fully-authored consolidation of all 17 Areas of Part 36 (Novel Primacy, Living Scene Standard, Exposition Ceiling, Narrative Rhythm, Breakthrough Thematic Law, Combat Texture, Technology Texture, Character Interiority, Sensory Palette, Dual-Track Identity, World-Building Texture, Tone Register, DCG Preview, Conflict Resolution, Sovereignty Delineation, Gate 1 Check #16). Read this skill in full before drafting or auditing any prose unit — it is the authoritative Tier 0 thematic reference.
**Secondary/legacy reference:** the 19 split `ssc-narration-p36-*` skills remain on disk and are consistent with the consolidated skill above; consult them for area-by-area detail if needed, but the consolidated skill is the primary read.
**Applies to:** Prose Maker (primarily); Outline Planner (DCG Thematic Preview, Area 13); Continuity Checker (enforces at Gate 1 Check #16)

## The rule

Part 36 is Authority Tier 0 for narrative *feel* — the highest tier in the system for this
purpose, layered on top of (not replacing) Parts 1 and 34's authority. Four foundational
principles govern every prose unit without exception:

- **P36-1 — We Are Writing a Novel.** Technical accuracy is mandatory, but technical accuracy
  delivered as a textbook lecture is itself a violation even when every fact is correct.
- **P36-2 — The Scene Must Be Living.** The reader must be inside the experience, not
  observing it from outside.
- **P36-3 — All Canon Parts Serve the Novel.** Parts 1-35 govern what is technically true;
  Part 36 governs that it must also feel like it matters. Both are required — there is no
  exemption from either.
- **P36-4 — The Novel Must Feel Like a Novel.** A consistent thematic identity across every
  scene, not just stylistic polish.

## Hard rules

- When a Part 1-35 requirement can be fulfilled multiple ways, Part 36 decides which way.
  When it can only be fulfilled one way and that way conflicts with the living-scene
  mandate, **the conflict must be escalated via `AskUserQuestion` before drafting proceeds —
  there is no silent resolution, even for minimal variance.**
- **Gate 1 Check #16** (see `ssc-narration-p36-gate-1-check-16-novel-thematic`)
  is a **blocking FAIL** check across 6 dimensions (Living Scene, Exposition Ceiling,
  Narrative Rhythm, Scene-Type Overlay, Emotional Specificity, Dual-Track Identity) — a
  `[CONFIRM WRITE]` attempted while Check #16 shows FAIL is itself a Rule 7.1.1 violation.
- Check #16 is re-verified at Gate 2 as a file-integrity check — the written file must not
  have degraded relative to the Gate 1-accepted prose (e.g. a save process re-introducing a
  raw explanation block).

## Escalation

Never trade narrative quality for technical compliance or vice versa — when they conflict,
that conflict is the thing to surface, not silently pick a winner.
