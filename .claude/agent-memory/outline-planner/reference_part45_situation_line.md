---
name: part45-situation-line-recipe
description: How to write the Part 45 Situation line under a Chapter Spec Fight line (no order rule, menu not ladder, Seal ceiling) and the move-type and attribution traps found while doing it for Chapter 006
metadata:
  type: reference
---

Part 45 (`cultivation-situational-combat-law`, guardrail `guardrail-situational-combat-selection.md`, Gate 1 Check #24) starts at Chapter 006; Chapters 001 to 005 are not touched.

- **No order rule.** Never plan that an Intermediate or Advanced move follows a Basic move, never plan a Basic-Intermediate-Advanced ladder, never write that link codes are "met in the scene". Link codes (LINK-PRIOR, LINK-STEP, LINK-GUARD) are eligibility met by the kit rows' mastery (Practiced or better; the author ruled Expert for the Chapter 006 heroes). Any Usable move may open, carry or end a fight; a couple of Advanced moves may finish one; effort and fatigue are the limit.
- **Seal ceiling.** Hercules and Bison fight at an effective Champion Level 8 High: Basic, Intermediate and Advanced types are Usable; Signature and Catastrophic are Seal-blocked; Elite, Fusion and Mythic are Latent (Rule 45.8.2.2). Cite the rule, do not write "the author confirmed" unless the coordinator relayed it as the author's word.
- **Shape of the line** (a sibling bullet after the Engagement Ledger): Ground and space; Light and weather; Postures that matter; People to protect; Intent; Energy budget; one Menu per fighter (move, its type, cost class, and the situation it fits and does not fit); Seal and access. Say "any may be used directly, at any point"; do not write "in any order" or "whatever order" (it echoes the removed rule).
- **Move type is the CSV `type` column, not the ID prefix.** `CMV-ADV-STR-001-01 Mastered Palm` is Basic type; `CMV-INT-STR-007-01 Torso Guard` and `CMV-INT-BDY-007-01 Bull Rush` are Basic; only the row whose type column reads Advanced counts as Advanced (`Staggering Blow`). Check the CSV under `ledger-manuals/cultivation/moves/<tier>/<code>.csv` before labelling a menu.
- **Caps are "sparingly", not a sequence.** The earlier cap (three each in Area 03, four in Area 04) stays as the reading of the author's "sparingly".
- **Audit notes about a removed rule** say that a scene-ordering requirement existed and was removed; do not restate its wording, so a grep for the old phrases returns only denials.
- Final greps for this kind of pass: inline tags, `[Ss]ection 7` before the section-7 heading, contractions, `ladder|rung|climb|in any order|follow a Basic|its own manual|link codes? (are )?met in`, unitalicised moves (`[^*](Move Name)|(Move Name)[^*]`), and a line count.
