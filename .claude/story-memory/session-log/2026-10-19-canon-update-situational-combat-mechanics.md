# Canon Amendment log: Situational Combat Mechanics Law, Part 45, Gate 1 Check #24, and removal of the invented scene-ordering rule for moves (2026-10-19)

Not canon; an audit trail.

- Authority: the author (jpdash, sole canon authority), in chat, 2026-10-19, relayed by the orchestrating command, following the amendment procedure of the 2026-10-18 and 2026-10-17 logs. The author's words: no Intermediate or Advanced move has to follow a Basic move; anyone can use any move they have access to; effort and fatigue are the limit, not order; a couple of Advanced moves can finish a fight; build the fighting sequence around the situation (a crouching target cannot be kicked in the head); a decision model for the best move in a specific situation, with a skill, a guardrail and a Gate 1 check. Where the author names a move or a type (Elite, Signature) the author rules and the planner gives options. Second ruling of the same day: the law, the guardrail and the check apply to FUTURE writing only, starting with Chapter 006; Chapters 001 to 005 are left as written.
- Read: this procedure's precedent logs (2026-10-18 early raid and Vanguard code; 2026-10-17 Battle Plausibility Law; 2026-10-19 Chapter 006 amendments); `guardrail-ccia.md`, `guardrail-locked-vs-negotiable-canon.md`, `guardrail-ledger-update-law.md`, `guardrail-alca.md`, `guardrail-audit-gate-law.md` (Gate 1 list, Check #23 entry, Whole-Chapter section), the guardrails index and `guardrail-battle-plausibility.md` (the template); Parts 3 (Areas 12.4, 16.4), 5 (Areas 16 and Appendix A), 6 (Areas 2, 3, 5), 40 (Areas 5 and 10), 42 (Rules 42.3.3, 42.3.4, 42.6.3, 42.11.5, 42.11.6, 42.13.1), 44 (in full as the pattern), 38 Rule 2.4.10; `eligibility-rules.md`; the four canon-manifest files; `docs/index.html`.

## Decision: a new Part, not an Area

Part 45 (skill `cultivation-situational-combat-law`, 12 Areas, Tier 1, cultivation group) is the established pattern for a coherent new law with its own guardrail and Gate 1 check (Part 44 did the same on 2026-10-17). An Area inside Part 5, 6 or 44 would have been owned by a Part whose domain it is not (Part 5 is who may fight, Part 6 is the moves, Part 44 is the whole engagement). Part 45 owns one question, which move fits a moment, and the others get one-sentence pointers.

## Where the removed ordering rule appeared

There is no sentence in any skill, guardrail, agent or command that required a lower-type move before a higher one in a scene. The invented rule lived in four places:

1. `story-memory/ledger-manuals/eligibility-rules.md`, test E3: "A Tier C or Tier D character has no kit, so LINK codes count as met only if the scene or the author has shown the earlier manual." This is the only canon-side carrier. It is rewritten (see below).
2. `.claude/temp/chapter-006-proposal.md` line 66: "each Intermediate or Advanced move follows a Basic move of its own manual in the same Area, so its link codes are met in scene". NOT edited (it is the planner's working text).
3. `.claude/temp/chapter-006-spec-DRAFT.md` (NOT edited, listed): the Named Moves line 88; the scene anchors and Fight lines of Areas 03 and 04 (lines 437 and 440); Audit note lines 814, 845, 883 (eligibility, the link codes of sixteen moves) and 885 ("the order of the moves", where the planner reads the author's rule "each Intermediate or Advanced move after a Basic of its own manual" two ways).
4. Written history that applied the same reading to the Gale escort of Chapter 005: `story-memory/phase-section-part-chapter-area-specs/phase-1/section-1/part-1/chapter-005-spec.md` (lines 91, 174, 870, 915) and `.claude/temp/chapter-005-spec-DRAFT.md` (lines 91, 173, 779, 825); `.claude/temp/Chapter 005 - hand-off.md` line 158 ("Every Basic saber guard move stands in the text before the Intermediate move of the same person"); `ledger-named-moves/_index.md` lines 152 and 158 ("the link codes read as met by the scene" for Chapter 004 and Chapter 005). Also `chapter-004-spec.md` lines 97 and 946 name `eligibility-rules.md` E3 for Latent moves (the Latent rule is unchanged).

Kept, because they are different: LINK-PRIOR, LINK-STEP and LINK-GUARD in `manual-and-weapon-style-law` Rules 42.6.3.3 and 42.11.6.1 item 3, the manual rows with link codes, the Part 6 Access Table, and Rule 42.13.1.3 (a Latent move is never executed). These are eligibility prerequisites to hold a manual (Practiced mastery of a lower-grade manual, read from the kit and Named Moves) and never an order of moves in a scene.

## Files changed

| File | Change |
|---|---|
| `skills/cultivation-situational-combat-law/SKILL.md` (NEW, Part 45, 12 Areas, 430 lines, CRLF like Part 44) | Principles P45-1 to P45-9 (no order rule; eligibility is not order; any Usable move; effort not sequence; the situation chooses); the Situation Frame S1 to S14; ground, footing, cover, space, crowding and village-ground defaults; the posture table; reach, range, height, size and anatomy (person and beast table); tempo, telegraph, counter-windows; numbers, lines, protecting others; light, weather, concealment, witnesses and the Seal (Rule 42.3.4.2 restated, unchanged); hands and weapons (bare-handed geometry); cost, fatigue, the energy budget (a couple of Advanced moves can finish a fight), cause and options for the author; chaining, finishing, mercy; the Move Selection Test (ten ordered questions); the worked table of fifteen situations; the anti-patterns; the Situation line, Check #24 (24-1 to 24-8), send-back, scope in time (Rule 45.12.4.1, future writing only from Chapter 006), the record of what was removed (Rule 45.12.5.1), the cross-Part table. |
| `guardrails/quality/guardrail-situational-combat-selection.md` (NEW) | The guardrail and the Check #24 table (24-1 to 24-7 block, 24-8 information); not retroactive. |
| `guardrails/audit/guardrail-audit-gate-law.md` (CRLF) | Check #24 entry after Check #23; count 23 to 24 in every count sentence (the gate sequence, the flow review, the re-audit, the Whole-Chapter section); a Check #24 bullet in the Whole-Chapter section; "2-33 and 35-44 (Part 44 registered)" to "35-45 (Part 45 registered, 2026-10-19)" twice. |
| `guardrails/_index.md` | Header date; a "Situational combat" bullet; Counts (24 checks, Parts 35 to 45, 43 skills); a table row for the new guardrail; the 23-count in the audit-gate row (two places). |
| `guardrails/authority/guardrail-authority-tier-system.md`, `guardrail-consolidated-skill-reading.md` | Tier 1 list to Part 45 and one clause; 43 skills, Parts 35 to 45, Part 45 row of the table. |
| `guardrails/audit/guardrail-forced-read-discipline.md`; `quality/guardrail-behavioral-authenticity.md`, `guardrail-plain-language.md`, `guardrail-entity-naming-law.md` | Count wording 23 to 24 (and Check #24 named where Check #23 was). |
| `agents/area-maker.md`, `outline-planner.md`, `continuity-checker.md`, `chapter-editor.md` | Area Maker: a "Situational combat" drafting bullet. Outline Planner: a section "Situation line in every Chapter Spec fight" (menu, never order; no "link codes met in scene"; options for the author). Continuity Checker: the Check #24 paragraph and the count 23 to 24 throughout. Chapter Editor: never changes the moves, their order or their prices. |
| `commands/next-area.md` (CRLF), `create-chapter.md`, `revise-area.md`, `revise-chapter.md`, `chapter-spec.md` (CRLF) | Check #24 line (next-area, create-chapter), count 23 to 24, the Fight line carries the Situation line (chapter-spec). |
| `skills/cultivation-move-taxonomy-law/SKILL.md` (Part 6) Area 2.1; `manual-and-weapon-style-law/SKILL.md` (Part 42) Rule 42.11.6.4; `cultivation-combat-and-fight-law/SKILL.md` (Part 5) Appendix A row; `spec-story-specification-law/SKILL.md` (Part 38) Rule 2.4.10; `narration-novel-thematic-law/SKILL.md` (Part 36) | One pointer sentence or row each (Type is not a rung; link codes are eligibility only; the Fight line carries the Situation line); Part 36: "Eight checks follow it", Check #24 named, count 23 to 24. No rule weakened. |
| `story-memory/ledger-manuals/eligibility-rules.md` | E3: the sentence requiring a scene to show the earlier manual is replaced by a reading from the ledger alone and a note that link codes are eligibility only. |
| `canon-manifest/skill-index.json` (CRLF), `dependency-graph.json` (CRLF), `domain-map.json` (LF) | Part 45 entry (12 Areas with line counts and related edges); nine dependency rows (45 to 3, 5, 6, 42, 44, 40, 38, 29, 16); one domain entry. Files stay valid JSON. |
| `docs/index.html` | The four count mentions 23 to 24. |

## Searched, no restatement found, nothing changed

`area-scorer.md` (quotes no check count); every other guardrail and command (no order rule; no Check #23 count); `ledger-schema-law`, `character-behavioral-synthesis-law` (their "22 checks" and "twenty-three templates" are different counts); `ledger-architecture-map.json`; the Part 42 amendment notes at lines 1403 and 1411 and Part 36's old "22-check" phrase (written history); `names.json` and the CSV files of the Manual Ledger (no row changes: link codes are untouched); `agent-memory` files (they speak of E3 eligibility, not ordering); the hero ledgers (the Seal and the sheathing notes already stand).

## Left on purpose

- Per the author's second ruling, Part 45, its guardrail and Check #24 are NOT retroactive. Chapters 001 to 005 are left as written: Check #24 is not run on them, no redraft or revise of them is implied, and the Chapter 004 and 005 specs, the Chapter 005 hand-off and the Named Move register lines about link codes met by the scene are history and are not touched.
- `.claude/temp/chapter-006-proposal.md` and `chapter-006-spec-DRAFT.md`: not edited (the brief). They need the ordering rule taken out (see "Spec chain needs").
- The Seal: Part 42 Rule 42.3.4.2 is unchanged. Flag: Hercules and Bison still have Signature and Catastrophic blocked by the Seal and Elite, Fusion and Mythic Latent through the effective realm; Part 45 Rule 45.8.2.2 only restates this and says the choice among Basic, Intermediate and Advanced is free. Bison's sheathed transformation and horn and tail moves are unchanged.
- The link codes and manual rows in the Manual Ledger; the validator `manual_ledger_query.py` (no script change).
- Part 44 text (the Engagement Ledger and Check #23), Part 3, Part 29 and the Move-Naming Law: unchanged.

## Reported, not applied (CCIA escalation)

- The Part 42 Rule 42.11.6.1 item 3 text says link codes are met "by the character's kit and Named Moves"; for a Tier C or D person with no kit row the reading is now the ledger alone (eligibility-rules.md E3). Whether a Tier D person's Practiced mastery should be taken as met by default is a reading the author may want to state in Part 42 itself.
- The energy percentages in Part 6 Area 5.3 are kept in the spec and gate only (Rule 45.1.1.9); whether a fatigue figure per move type per fight should be a table is left to the author.
- The pre-existing gaps noted on 2026-10-18 (no Part 35 to Part 30 edge) still stand.

## Spec chain needs (off limits for this step)

- `chapter-006-spec-DRAFT.md` and `chapter-006-proposal.md`: remove the order rule everywhere it appears (listed above), do not state "link codes met in scene", spread the sixteen moves as a menu fitted to the Situation of each fight, add a Situation line under each fight Area's Engagement Ledger (ground and space in the lane and the square, light at dusk, postures, the people to protect, the intent, the energy budget of Hercules and Bison), and resolve the Open note at line 885 (the order of the moves) as "no order; menu".
- Section Spec 1.1 and Novel-Part Spec 1.1.1: note the amendment where the Named Move beats for Hercules and Bison are described; no other change.
- Chapter Specs 001 to 005: written history; no change.
