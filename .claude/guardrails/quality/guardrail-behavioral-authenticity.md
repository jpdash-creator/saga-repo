# Guardrail: Behavioral Authenticity and the Behavioral Signature Registry

**Source:** Part 39 (SSC Canon Character Behavioral Synthesis Law) · Canon v10.0 · full detail: `character-behavioral-synthesis-law`
**Applies to:** all 4 agents. Area Maker renders registered behavior; Continuity Checker runs Checks #20 and #21 and owns Sections 11/12; Outline Planner builds the Behavioral Plan into Chapter Specs; Area Scorer reads behavioral density into CDL-2 categories.

## The rule

Part 39 is Authority Tier 0 — a **fourth craft-layer authority** alongside Parts 28, 29 and 36. Like Parts 28, 29 and 36, its Tier 0 governs *how* a character is rendered, never
*whether* another Part's technical requirement applies. It cannot waive a Part 3 realm
constraint, a Part 5 escalation ceiling, a Part 30 locked end-state, or a Part 29 formatting
prohibition, and a behavioral registration that would require such a waiver is invalid on its
face rather than a conflict to be resolved in Part 39's favour (P39-14).

Part 39 exists because Part 28 Area 6.5 already forbids robotic character rendering and a
prohibition is not a specification. Part 28 says behavior must not be mechanical; Part 39 says
what this particular person does instead, and records it.

- **36 Behavioral Layers** (`L01`–`L36`) across eight Groups, **291 dimensions**, with options
  coded in the form `B39-Lnn-DIM-nn`. Codes are permanent and never reassigned.
- **Every governed character holds a registered profile before they are written**
  (P39-2). Registration lives in Character Ledger **Section 11** (Behavioral Signature) with
  the running change record in **Section 12** (Behavioral Evolution Log). The character
  ledger template is thirteen sections (Section 13 is Current Condition).
- **Villains and monsters.** "Villain" in the next bullet reads
  a Tier A or Tier B villain: a Tier C side villain addresses the mandatory-core six with one Signature
  and a Tier D side villain is a registry row with a compact code (Part 18 Area 6.3; Part 39 Area 4.1).
  A **sentient monster** is registered in full. A **non-sentient monster** holds no registration; its
  twelve traits (Part 40 Area 5) reuse Part 39 dimensions by pointer, and Check #20 element 20-2 reads
  them in light form. No new Layer is added.
- **Per-tier requirement:** Hero, Villain, Tier A and Tier B all address **all 36 Layers** with
  about **12 Signatures** as the interview's aim, never a gate. Tier C addresses the
  **mandatory-core six** — L01 Kinesic, L03 Emotional Expression, L08 Moral Reflex, L10
  Speech-Adjacent, L29 Idle/Waiting, L34 Provenance — with about **1 Signature**, again never a
  gate. **Tier D (Named Conversational) has NO Layer register and
  NO registered Signature** — its whole registration is a row in `ledger-character-side/_index.md`
  carrying a name, a descriptor and **a compact code the drafting agent picks alone** (Part 39 Section 3.5). The code is a picked string, not a registration.
- **Tier D never promotes automatically.** **Recurrence
  never promotes. Speech never promotes.** A Tier D character may appear in any number of later
  Areas, and speak in all of them, without triggering anything. Where one is about to do
  something with **genuine story-state consequence**, the agent **flags it to the author** via
  `AskUserQuestion`, through the orchestrating command, and the author rules every time — promote to Tier C, or keep them Tier D
  and let the moment stand. **The agent never decides this, and never promotes on its own.**
  An open flag blocks Gate 2 exactly as a FAIL does. Part 19 Rule 19.1.2.4 owns the rule;
  Part 39 Rule 39.4.3.1a is its behavioral-registry side.
- **Tier D is expressly NEGOTIABLE canon** (Part 28 Area 2). Behaviour is drawn from **existing
  registered systems** — the applicable Collective Behavior Codes, the institutional or military
  ladder the character sits on, their formation's culture, their trade, the role itself. This is
  a licence to use existing knowledge, **never** to invent a new system, address form, honorific,
  rank, rung, rite or oath.
- **The Tier D code.** A new Tier D row carries one compact code, picked by
  the drafting agent alone while it drafts (Part 39 Section 3.5; Part 19 Rule 19.1.2.7). Authority-bearing
  tokens are picked within stated limits and carry an `[AI]` mark; only the author changes them. Check #20
  element 20-1 validates the code (tests V1 to V9) and element 20-2 runs in light form; the code is never printed in
  chat, and a failure still open when Gate 1 closes is reported like any other FAIL. The code is not a registration and is never compared with another character's
  code. It never widens Tier D: the tier stays cheap, speech is what it is for, nothing promotes
  automatically, and consequence goes to the author.
- **Collective codes** live on the faction, civilization and location ledgers (Part 37 Areas
  2.4/2.6/2.7, Collective Behavior Code block), never on the character. A character records
  only their conformance and their named deviation.

## Hard rules

- **No unregistered actor.** A character may not be drafted into an Area in which they
  act or speak until their tier's registration is complete (Rule 39.4.3.1), except a Tier C or
  Tier D person the drafting agent improvises in the Area, who is identified at Gate 1 and
  registered at Gate 2 (Route 2 of that rule). Blocking at
  Check #20 element 20-1. A character merely named in passing is not "acting".
- **No prosodic re-registration.** Part 29 Rule 29.4.4.1's nine prosodic determinants are
  Part 29's exclusively and are never restated as Part 39 behavior (Rule 39.2.3.1). A
  character carries both a Prosodic Signatures field and a Section 11 Layer Register, and
  neither substitutes for the other.
- **No inner-state adjudication.** Part 39 never assigns, grades or revises a PIS level, CSS
  grade, IE event, ideology category, Heart level, or realm (Rule 39.2.3.2). It records the
  observable transfer function only.
- **Every Signature names its origin.** A Signature with no stated provenance is not
  registered; it is decoration, and it is rejected (Layer L34, Rule 39.38.1.1).
- **Each character is separate.** Characters are registered standalone; overlapping values,
  identical Signature pairs included, are permitted and carry no clearing, exchange or named
  axis.
- **Demonstrated, never named.** No prose sentence states a Part 39 registration as a
  property. The narrator does not report that a character is careful or guarded; the
  registration reaches the page as the act alone (Rule 39.40.2.5, N39-2). Absolute, no
  exception.
- **Signatures move only through a logged drift event.** Section 11's Signature Set,
  Contradiction/Cost block and Conditional Drift Map are Baseline. They change only via a
  Section 12 entry with a named trigger — never by editorial revision.
- **Behavior must change across a Phase, and change must be earned.** A character who absorbs
  defeat, betrayal, a first kill and a breakthrough and behaves identically afterward fails
  Part 39 as surely as one who changes for no reason (P39-8). There is no drift budget: how much
  a character changes in a Section follows the story and the character, and a count of
  dimensions is shown only as information.
- **Old behavior persists.** A superseded behavior is never deleted; it is preserved in
  Section 12 and may resurface under its registered reversion condition (P39-10).

## The two gate checks

Gate 1 runs **24 checks**; Check #22 is Plain Language and Narrative Impact and Check #23 is Battle Plausibility (Part 44) and Check #24 is Situational Combat Selection (Part 45). Both checks defined below are blocking and both sit after
Check #19.

- **Check #20 — Behavioral Conformance** (Part 39 Area 43). Eleven live elements (20-3 is retired): 20-1
  registration completeness · 20-2 signature conformance · 20-4 signature
  recurrence · 20-5 contradiction and cost presence · 20-6 waiting beat · 20-7 off-register count ·
  20-8 collective code conformance · 20-9 demonstrated-not-named · 20-10 provenance integrity ·
  20-11 age-band anchors · 20-12 boundary integrity. A FAIL blocks Gate 2.
  **The count elements are the single list in Part 39 Area 43.3** and follow
  `.claude/guardrails/quality/guardrail-threshold-consultation.md`: the value and the line it crossed are reported
  as information, never a FAIL and never auto-revised. Elements 20-5 (contradiction and cost
  presence) and 20-6 (waiting beat) are shown when the scene carries them and are never added to
  meet the rule.
- **Check #21 — Behavioral Change Detection** (Part 39 Area 44). **Blocks by asking, not by
  failing.** Fires as Part 39 Area 44.2 sets out: on an unmapped trigger (or a mapped one that
  breaks L34-END), on a contradicted Signature, on a flagged item the author has not yet ruled,
  in an Area in which the prose shows a POV character's profile moving, at the
  close of a Section for the characters whose profiles the prose shows moving, and
  automatically at any PIS-7, CSS-8, age-band crossing or realm crossing; a review that finds
  nothing reports SILENT and asks nothing. Four detection classes: D-1 signature
  contradiction · D-2 unmapped trigger · D-3 cumulative pressure without change (a story
  judgement; the count and the clock, where kept, are information only) · D-4 band or
  tier crossing. The author rules one of **`[KEEP PROFILE]` / `[EVOLVE]` / `[REVISE AREA]` /
  `[PROVISIONAL]` / `[DEFER]`**, and the Continuity Checker always presents a reasoned
  recommendation rather than asking cold. Every `[EVOLVE]` and `[PROVISIONAL]` ruling is
  written back into the character's Conditional Drift Map.
  **Check #21 widened (evolution, 2026-10-06; Part 43, Character Evolution Law):** at Gate 1 it detects EVERY behaviour change in the draft for every character (the 36 Layers, the 12 Signatures and the bound properties). For heroes and Tier A side characters, villains and monsters it asks the author with `AskUserQuestion`; for Tier B, C and D side characters, villains and monsters the Gate 1 continuity-checker decides itself and records its decision and reasons, asking nothing. A change to an immutable trait always needs the author's explicit ruling and a recorded reason, for every tier. Gate 2 presents every evolution (all tiers) with its recorded information. A `[REVISE AREA]` send-back goes through `/revise-area`. No new command exists, and evolution is not drift. The base profile is never overwritten: every evolution is a dated entry (Part 43, the Character Evolution Law; ledger section 'Evolution Entries'), the current profile is the base profile plus the entries in order, and a reset removes entries back to a date the author names.

Check #20 polices drift-as-error; Check #21 surfaces drift-as-growth. The same line may appear
in both, and where it does the Check #21 ruling governs: an `[EVOLVE]` retrospectively clears
the Check #20 finding for that line.

## Boundaries with the neighbouring Tier-0 Parts

| If the question is | The owner is |
|---|---|
| May a character behave this way at all | Part 28 Area 6 |
| How does this speaker build a sentence | Part 29 Area 4.4 (nine determinants) |
| What may this character be called | Part 29 Area 16 |
| Is this scene alive; is the prose manufactured | Part 36 Areas 2, 17 (Checks #16, #19) |
| What does *this person* do, and is it recorded | **Part 39** (Checks #20, #21) |
| What is the ledger's structure | Part 37 (governs on any schema disagreement) |
| What is a spec's structure (Section, Novel-Part or Chapter) | Part 38 (governs on any spec-structure disagreement) |

## Escalation

A behavioral registration that appears to require breaching another Part is not resolved by an
agent — it is invalid, and the attempt is surfaced. Conduct that fits no registered dimension
is **flagged, never forced** into the nearest fit (Part 39 Area 48, Rule 39.48.2.1); the flag
does not block Gate 1. A proposed thirty-seventh Layer is an author decision under the Part 39
Amendment Protocol, never a drafting convenience.

## Distinctness is the author's, not the registry's

*"Each character is separate — stop creating comparison derivations — there can be overlaps — I
will decide each thing through AskUserQuestions."* Characters are derived and designed standalone.
Overlapping values — identical pairs included — are permitted and need no clearing or named axis.
Agents never
generate character-vs-character comparison material; the only cross-character check that remains
is CANON CONSISTENCY — a choice contradicting an explicit citation in a frozen ledger is surfaced
to the author once, plainly.

## Scene-chronicle evidence rule

No Part 39 behavior and no Part 29 determinant is derived from, cited to, or reconstructed out of a
scene chronicle in a world, faction or affiliation ledger. This binds every agent that derives,
registers, or audits character material:

1. **Behavior enters a character ledger by registration (Part 39) or from a written Area at
   Gate 2, never from a scene record in another ledger.** The character ledgers carry no
   characterization that no registration or written Area supports.
2. **A scene chronicle in a world, faction or affiliation ledger is not character evidence.**
   A passage that narrates what a character said or did in a scene is **not citable in support of
   any character behavior, Signature, or prosodic determinant.** Structural facts in those same
   files (geography, architecture, institutions, treaties, offices, species) remain fully citable.
3. **A drafting agent that needs a register a character does not have stops and says so.**
4. **A character-ledger field carrying a `WITHDRAWN` notice is empty.** It is never inverted,
   alluded to, or treated as "someone who used to" hold the habit.
