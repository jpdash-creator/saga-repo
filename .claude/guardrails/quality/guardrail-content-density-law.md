# Guardrail: Content Density Law (CDL-2)

**Source:** Part 35 (Content Density Law CDL-2) · Canon v10.0 · full detail: `narration-content-density-law`
**Applies to:** Area Scorer (primary owner); Area Maker (reads the readings as guidance; the Chapter Spec decides what the scene holds)

## The rule

Every Area is scored across **11 content-density categories** (Combat, Named Moves &
Techniques, Cultivation Growth, Technology, Lore & World-Building, Dialogue & Social,
Information & Intrigue, Emotions, Character Development, Travel & Discovery, Political &
Faction), tracked as an Area score for each Area, and as a running
Section aggregate against a Phase 1 Section×Category target table (Low–Anchor–High ranges).

- **Universal Anchor Floors (information only)**: Combat, Cultivation Growth, Dialogue & Social,
  and Lore & World-Building are marked ★ and read against a **20% per-Section line**. The line
  informs and never governs: it fails no Area or Section, and no content is added to meet it. A
  Section whose story does not call for one of these categories simply shows a lower reading.
  The confirmed spec chain and Part 30 prevail.
- The Completeness Indicator (Gate 2 Block A, whose CDL-2 block is the area-scorer's) reports this scoring every time, with
  a reading per category against the target range (inside, below or above it; information only,
  never a pass or a fail) — this is not an end-of-Section-only report.
- **The Area is the scored unit.** The Area score is computed and displayed once, when the Area is
  written (`narration-content-density-law` §4.1a), and recorded in the Section tracker; it is
  record-and-display and never a pass or a fail. The content floor (CDL2-P9) and the Named-Move
  runs (CDL2-L6, CDL2-L7) count Areas, and are information only.
- **The Section tracker.** The tracker is
  `.claude/story-memory/cdl2-density-tracking/phase-N/section-M-aggregate.md` (N the Phase,
  M the Section); the Area Scorer creates it from the headings of the Section 1 file at the
  Section's first scored Area and is the only writer of it.

## Hard rules

- Scoring is the Area Scorer's job specifically, and it is run with consistency, not chased for maximal depth on any single pass. The Area Scorer runs at the system-wide default model and effort owned by
  `.claude/guardrails/commands/guardrail-plan-then-auto-execution.md`. Consistency across scoring passes is achieved by holding the rubric, category definitions, and target tables fixed
  (never adjusted pass-to-pass); comparisons across passes must stay reliable.
- CDL-2 is the only density framework; never reference CDL-1 category names or thresholds.
- A category running persistently low against its target is reported plainly in the running
  Section aggregate, not smoothed over or excused by strong performance elsewhere.
- The Voice and Variety block (Part 36) is reported beside the CDL-2 score, for each Area. It has six rows, named in the Area Scorer's charter; it
  is shown in chat only and is not stored. It adds no category, target or status to this
  rubric and is never scored into a category (`narration-content-density-law` §4.4).
- **The date line is not scored** (Part 41,
  Area 5, The date line). The italic line that opens every Area is not narration: CDL-2 reads the Area with
  the line set aside, so it adds no word to any category, no weight to the Area or Section aggregate and no
  line to the Voice and Variety block. It is not a Lore and World-Building passage and not a Travel and
  Discovery passage, and nothing is written to raise or lower a reading because of it.

## Escalation

If a Section is trending below an Anchor Floor line, the running aggregate shows it as the
Section goes, so the author can see it before the Section closes. An Anchor Floor reading,
whether measured from finished prose or forecast from the running aggregate, is information: it
is reported with the number, the line it crossed and the margin, and it raises no question and
no FAIL. The Area Scorer never directs prose changes to close a density gap; it reports the
gap, and the story decides.

The Anchor Floor line is the flat `≥20%` at Section close (`narration-content-density-law`
§CDL2-P4); it is an information reading and not a Hard FAIL (counters
inform only).
