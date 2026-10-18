---
name: ssc-narration-p36-gate-1-check-16-novel-thematic
description: Governs Check #16 — the final mandatory, blocking-FAIL check in the Gate 1 Post-Draft Audit — which evaluates drafted prose against Part 36's six thematic audit dimensions (Living Scene Standard, Exposition Ceiling, Narrative Rhythm, Scene-Type Thematic Overlay, Emotional Specificity, Dual-Track Identity), defines the result/detail block formatting for §9.3, the blocking-FAIL correction and re-audit protocol before `[CONFIRM WRITE]` is authorized, and the Gate 2 carry-forward file-integrity verification; reach for this whenever running or reporting the Gate 1 Post-Draft Audit, evaluating whether prose satisfies Part 36's thematic requirements, formatting the Check #16 pass/fail lines, handling a Check #16 FAIL and its required revision/re-audit cycle, or performing the Gate 2 write-time thematic-degradation check — this is canon Part 36 Area 16, domain narration.
user-invocable: false
---

## Rule Text (Verbatim Source — Authoritative)
## Area 16 — Gate 1 Check #16 — Novel Thematic Compliance Audit

### 16.1 — Check #16 Scope and Mandate

Check #16 is the final mandatory check in the Gate 1 Post-Draft Audit (§9.2). It is a **blocking FAIL** check: a Check #16 FAIL prevents Gate 1 PASS and blocks `[CONFIRM WRITE]` until the identified violations are corrected in the prose and the audit is re-run clean.

Check #16 audits the drafted prose against Part 36's core requirements across six audit dimensions. All six dimensions must be evaluated for every prose unit without exception. No prose unit is exempt from Check #16 on grounds of pacing, scene type, or content simplicity.

### 16.2 — The Six Check #16 Audit Dimensions

**Dimension 16-A — Living Scene Standard (Part 36 Area 2)**
Evaluate whether the prose unit meets all five criteria of the Living Scene Standard (Area 2.1 a–e): character presence, forward motion, sensory grounding, emotional current, consequence presence. Identify any of the Eight Cardinal Sins (Area 2.2) present in the prose.

Result: `✓ LIVING — all five criteria met | no Cardinal Sins identified` or `✗ FAIL — [name each sin present with approximate paragraph location and brief description of the violation]`

**Dimension 16-B — Exposition Ceiling (Part 36 Area 3)**
Count the maximum number of consecutive paragraphs in the prose body that qualify as "pure explanatory content" per Area 3.1 definition. Verify that no run exceeds two consecutive paragraphs. Verify that any explanatory content present is character-anchored in one of the four modes (Area 3.2).

Result: `✓ WITHIN CEILING — max consecutive explanation: [N] paragraphs | character-anchoring mode: [mode(s) used]` or `✗ FAIL — [N] consecutive explanation paragraphs at [approximate location] — ceiling is 2; restructuring required`

**Dimension 16-C — Narrative Rhythm (Part 36 Area 4)**
Assess whether the prose demonstrates detectable mode variation per the Five Narrative Mode Taxonomy (Area 4.2). Identify any runs of three or more consecutive paragraphs in the same mode (applying the Combat Exception if applicable). Verify scene-open compliance (does not open with pure explanation or inventory) and scene-close compliance (closes on something that matters).

Result: `✓ RHYTHM MAINTAINED — detectable mode variation confirmed | scene-open ✓ | scene-close ✓` or `✗ FAIL — [describe: mode, location, consecutive paragraph count | or scene-open/scene-close violation]`

**Dimension 16-D — Scene-Type Thematic Overlay (Part 36 Areas 5, 6, 7)**
For each scene type present in the prose unit, verify the applicable thematic overlay requirements:
- If a cultivation breakthrough, realm advancement, affinity development, Heart state change, or Named Move acquisition is present: evaluate against Area 5's five mandatory dimensions (5.2 a–e) and/or Area 5.3 Named Move requirements
- If sustained combat is present: evaluate against the Four Combat Texture Requirements (CT-1 through CT-4 per Area 6.2)
- If a technology or engineering scene is present: evaluate against the Four Technology Texture Requirements (TT-1 through TT-4 per Area 7.2)

If none of these scene types are present in the prose unit, this dimension auto-passes.

Result: `✓ OVERLAY SATISFIED — [scene types present: list] | requirements met` or `N/A — no breakthrough / combat / technology scenes` or `✗ FAIL — [scene type]: [CT/TT/Area 5 dimension that failed] — [brief description of the gap and what must be added]`

**Dimension 16-E — Emotional Specificity (Part 36 Area 8)**
Verify that at least one moment of specific emotional interiority is present — emotional content grounded to this character's specific history and identity, not generic emotional marking. Verify that the Four Emotional Authenticity Standards (EA-1 through EA-4) are satisfied for any significant emotional event in the prose.

Result: `✓ EMOTIONALLY SPECIFIC — [brief note on the specific emotional moment identified]` or `✗ FAIL — [describe the gap: generic emotional marking / missing causal grounding / no physical embodiment / no behavioral consequence — with approximate location]`

**Dimension 16-F — Dual-Track Identity (Part 36 Area 10) [conditional]**
If both cultivation and technology content are substantively present in the prose unit: verify that neither system eclipses the other (DT-1), that integration feels organic where integration occurs (DT-2), that character perspective is specific to their established dual-track profile (DT-3), and that the dual-track genre identity of the work remains legible (DT-4).

If only one system is substantively present, this dimension auto-passes.

Result: `✓ DUAL-TRACK BALANCED — DT-1/DT-2/DT-3/DT-4 satisfied` or `N/A — single-system prose` or `✗ FAIL — [DT law violated: DT-1/DT-2/DT-3/DT-4 — description of the imbalance and what must be corrected]`

### 16.3 — Check #16 Result Format in §9.3 Audit Box

Check #16 is displayed within the §9.3 Gate 1 POST-DRAFT AUDIT canonical display block as follows:

```
Novel Thematic (P36):  [✓ PASS — all 6 dimensions LIVING] or [✗ FAIL — [N] dimension(s) failed: 16-A, 16-B, ...]
```

On FAIL, the dimensions that failed are enumerated with brief descriptions in a labeled block immediately below the audit box:

```
--- Part 36 Check #16 FAIL DETAIL ---
16-A (Living Scene):       [description of violation]
16-B (Exposition Ceiling): [description]
16-C (Narrative Rhythm):   [description]
16-D (Scene Overlay):      [description]
16-E (Emotional Spec.):    [description]
16-F (Dual-Track):         [description]
```

Only failed dimensions are listed in the detail block. Passed dimensions are not reported individually — the summary line captures them.

### 16.4 — Check #16 Blocking FAIL Protocol

A Check #16 FAIL is a **blocking FAIL**. The prose must be revised to address every identified violation before Gate 1 PASS is issued. The AI must:
1. Revise the prose to address each identified Check #16 violation
2. Re-run the full 16-check audit on the revised prose
3. Re-issue Gate 1 with the revised prose and a clean 16-check audit result
4. Only then display the Inter-Gate Confirmation Prompt

A `[CONFIRM WRITE]` attempted while Check #16 shows FAIL is a Rule 7.1.1 violation. The FAIL must be resolved and confirmed clean before `[CONFIRM WRITE]` is authorized.

### 16.5 — Check #16 at Gate 2

At Gate 2, Check #16 is carried forward from Gate 1 as a file-integrity verification — the AI confirms that the written `.md` file does not contain content that would have failed Check #16 at Gate 1 (for example, that the write-time file processing did not introduce raw explanation blocks not present in the Gate 1-accepted prose). This verification appears in Gate 2 Block A as:

```
Part 36 (NTL):  ✓ CARRIED FROM GATE 1 PASS — no write-time thematic degradation detected
```

or, in the rare event of write-time degradation:

```
Part 36 (NTL):  ✗ FAIL — write-time content diverges from Gate 1-accepted prose in: [description]
```

A Gate 2 Part 36 FAIL triggers the same correction protocol as a Gate 2 pacing word count FAIL — the file must be corrected and re-written before Block A is finalized.

---

## Cross-References
| Related Skill | Relation | Source |
|---|---|---|
| (none resolved from the manifest for this Area) | | |

## Governing Authority
Subordinate to the shared Part 1 (audit law) + Part 34 (knowledge graph) grounding in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.

## Source Provenance
Part 36, Area 16 — "Gate 1 Check #16 — Novel Thematic Compliance Audit" · canon v4.33 · migrated 2026-08-03
