# Guardrail: Tier-0 Narrative Quality (Novel Primacy Mandate)

**Source:** Part 36 (Narration Novel Thematic Law), Areas 1, 16, 17 · Parts 28/29 (Tier-0 craft layer) · Canon v10.0
**Primary reference:** `narration-novel-thematic-law` — a single-file, fully-authored consolidation of all 27 Areas of Part 36 (Novel Primacy, Living Scene Standard, Exposition Ceiling, Narrative Rhythm, Breakthrough Thematic Law, Combat Texture, Technology Texture, Character Interiority, Sensory Palette, Dual-Track Identity, World-Building Texture, Tone Register, DCG Preview, Conflict Resolution, Sovereignty Delineation, Gate 1 Check #16, Prose Vitality Law — Area 17; and Areas 18 to 27: narrator voice, tone, scene shape, motif and the story-craft Areas). Read this skill in full before drafting or auditing any Area — it is the authoritative Tier 0 thematic reference.
**Applies to:** Area Maker (primarily); Outline Planner (DCG Thematic Preview, Area 13, and the Areas that shape a plan: 4, 12, 17 and 18 to 27); Continuity Checker (enforces at Gate 1 Checks #16 and #19); Area Scorer (report-only Voice and Variety block)
**Companion:** `.claude/guardrails/quality/guardrail-behavioral-authenticity.md` — Part 39 joins Parts 28, 29 and 36 at Tier 0 and adds Checks #20 and #21. Checks #16 and #19 audit the *prose*; Checks #20 and #21 audit the *people*. Neither layer absorbs the other, and where both bear on one passage both are reported.

## The rule

Part 36 is Authority Tier 0 for narrative *feel*, and Parts 28 and 29 sit at Tier 0 beside it as the narration-craft and
dialogue/voice layers of the same craft authority. Four foundational principles govern
every Area without exception:

- **P36-1 — We Are Writing a Novel.** Technical accuracy is mandatory, but technical accuracy
  delivered as a textbook lecture is itself a violation even when every fact is correct.
- **P36-2 — The Scene Must Be Living.** The reader must be inside the experience, not
  observing it from outside.
- **P36-3 — All Canon Parts Serve the Novel.** Every Part's technical requirements govern
  what is true; Part 36 governs that it must also feel like it matters. Both are required —
  there is no exemption from either.
- **P36-4 — The Novel Must Feel Like a Novel.** A consistent thematic identity across every
  scene, not just stylistic polish.

## Hard rules

- When another Part's technical requirement — including those of Parts 28, 29 and 39 and of
  `.claude/guardrails/quality/guardrail-plain-language.md` — can be fulfilled multiple ways, Part 36 chooses the
  form (Part 36 Area 14.1), and nothing is waived. (plain vocabulary, 2026-10-06) That guardrail now
  also covers clarity and one meaning per word (a special word explained at first use, no jargon wall,
  figures clear at first read); its Check #22 elements 22-3, 22-6 and 22-8 to 22-11 block, the rest inform.
  When it can only be fulfilled one way and that way conflicts with the living-scene
  mandate, **the conflict must be escalated via `AskUserQuestion`, through the orchestrating command, before drafting proceeds —
  there is no silent resolution, even for minimal variance.**
- **Gate 1 Check #16** (defined in `narration-novel-thematic-law` §Area 16)
  is a **blocking FAIL** check across twelve dimensions (16-A Living Scene, 16-B Exposition
  Ceiling, 16-C Narrative Rhythm, 16-D Scene-Type and Element Overlay, 16-E Emotional Specificity,
  16-F Dual-Track Identity, 16-G Voice Signature,
  16-H Demonstrated-Then-Named, 16-I Register Range,
  16-J Area Flow Review, 16-K Voice and Variety, and the named dimension 16-DP Depth Pillars and
  quota-filler test, reported for the author's ruling) — a
  `[CONFIRM WRITE]` attempted while Check #16 shows FAIL is itself a Critical Violation of the Two-Gate law
  (`.claude/guardrails/audit/guardrail-audit-gate-law.md`).
  The counted readings inside it (the exposition ceiling of 16-B and the three-consecutive-mode
  rule of 16-C) inform only and never produce a FAIL.
  The craft findings of dimensions 16-A, 16-C, 16-D, 16-E, 16-F, 16-H, 16-K and 16-DP are reported for the author's
  ruling and never FAIL; a content-limit breach under 16-D and any
  contradiction of canon or a ledger, spec conformance or continuity fact still FAIL.
- Check #16 is re-verified at Gate 2 as a file-integrity check — the written file must not
  have degraded relative to the Gate 1-accepted prose (e.g. a save process re-introducing a
  raw explanation block).
- **Gate 1 Check #19 (Prose Vitality)** — defined canonically in Part 36
  Area 17 (`narration-novel-thematic-law`) — is likewise a **blocking FAIL** check for its
  qualitative half: Check #16's dimensions 16-G and 16-I can FAIL it, and a 16-H finding is
  reported and fails neither check. Its countable half reads Part 28 Area
  13's Closer-Variety and Single-Statement rules and Part 29 Area 4's Voice Signature, Epigram
  Budget, and Friction Floor / Human Texture rules as information only: a count is reported with
  its value and never produces a FAIL, and nothing is added or cut to meet it. Its counts run
  over the Area under audit (Part 36 Area 17). A `[CONFIRM WRITE]`
  attempted while Check #19's qualitative half shows FAIL is itself a Critical Violation of the Two-Gate law, and
  Check #19 is re-verified at Gate 2 as a file-integrity check exactly like Check #16. The Friction Floor norm is at
  least a few beats in an Area that carries speech (Part 29 Rule 29.4.4.4, Canon Amendment 2026-10-08), still
  information only; the natural-speech standard (Part 29 Rule 29.2.1.7) is read under dimension 16-DP and never FAILs
  on its own.
- **Check #16 dimension 16-J (Area flow review)** reviews the Area against the Area before it,
  as one flow, at every Gate 1: breaks of time, place, point of view or character state
  block; sameness patterns are reported with quoted lines and the author rules
  (`.claude/guardrails/audit/guardrail-audit-gate-law.md`).
- **Check #16 dimension 16-K (Voice and Variety)** is a judged dimension whose findings are reported for the author's ruling; none blocks. The Area
  Scorer's Voice and Variety block is report-only: never scored, never a pass or fail, never
  auto-fixed. Any count in either is shown as information under
  `.claude/guardrails/quality/guardrail-threshold-consultation.md`.
- **The date line is not narration** (Part 41,
  Area 5, The date line; the Part 2 rules on the Area text). The italic line that opens every Area is a
  lawful mark and not part of the narration. It is not read by Checks #16, #19 or #22 and it is never the
  Area's opening paragraph for the opening-hook, first-sentence or opening-pattern readings; the first
  paragraph of narration stays the opening. It is not a closer shape, it does not count in an Area's
  size or word count, and nothing is added to it or cut from it for a count. Its form and dates are read by
  Gate 1 Check #12 and Check #11 element 11-2 (`.claude/guardrails/audit/guardrail-audit-gate-law.md`).
- **Prosodic Signature Menu item 7 — technical-register default — has a switching law of its
  own: Part 29 Rule 29.4.4.1a.** Before writing any
  speaker's reach for trade or domain vocabulary, that rule **MUST** be read in
  `narration-dialogue-and-social-interaction-law` §Area 4 §4.4; its on/off behaviour **MUST NOT** be
  inferred from the menu clause, from the speaker's subject, from the setting, or from who is
  listening. Every speaker carrying item 7 sits in exactly one of the three registration
  states that rule defines, and prose contradicting the state recorded in that speaker's
  ledger is reported at Check #19 for the author's ruling. The rule's substance is stated there and is **not** restated
  here.
- Element-to-rule lookup: `narration-novel-thematic-law` §Area 15.5 (Novel Elements
  Lookup). Rule 22.1.1 attaches the rules of Areas 22 to 27, and of the element Areas in
  Parts 13, 25 and 29, to the elements a Chapter Spec names. The table adds no rule.

## Escalation

Never trade narrative quality for technical compliance or vice versa — when they conflict,
that conflict is the thing to surface, not silently pick a winner.

This governs numeric compliance too. Where satisfying a number would make the prose mechanical
— padding to reach a floor, cutting a living beat to clear a ceiling, inserting a quota-filler
to satisfy a counter — **the number yields**: the prose stands and the reading is recorded as
information under `.claude/guardrails/quality/guardrail-threshold-consultation.md`, never resolved in the number's
favour by default.
