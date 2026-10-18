---
name: ssc-narration-p02-book-creation-law-chapter-markdown-file
description: Governs the canon Markdown (.md) companion output for Starward Saga chapters — the lightweight, git-friendly, plain-text-portable counterpart to the .docx publication file, covering purpose and parity mandate, per-Prose Chapter Header Block / Area Divider / Prose Title Block placement, paragraph and scene-break formatting, dialogue and Named-Move/cultivation-level bold-italic conventions, per-Prose file structure examples, the Gate 2b markdown update protocol and its coupling to the .docx write, rewind and aggregate-invalidation behavior, and the governing constraints (parity, no governance content, plain-text portability, one Prose per file). Reach for this Area whenever an agent is creating or updating a prose-NNNNN.md file, deciding what belongs in the Chapter Header Block/Area Divider/Prose Title Block, formatting dialogue or Named Moves/cultivation levels for markdown output, resolving .md/.docx parity questions, handling [REWIND TO] or aggregate staleness for .md files, or auditing whether a Gate 1 Position Header Block has wrongly leaked into a .md file. This is canon Part 2 Area 7, domain narration.
user-invocable: false
---

## Rule Text (Verbatim Source — Authoritative)
## Area 7 — Book Creation Law: Chapter Markdown File (.md)

### 7.1 — Purpose and Mandate

**Rule 7.1.1 — Purpose.**
The chapter `.md` file is the **lightweight companion output** of the novel-writing process. Where the `.docx` file is the publication-format deliverable, the `.md` file is optimized for quick reading, git-tracked revision history, diff review, and plain-text portability. It contains the same prose content as the `.docx` file, formatted using standard Markdown conventions that preserve the novel's structural organization and inline formatting.

**Rule 7.1.2 — Parity Requirement.**
The `.md` file and the `.docx` file always contain the same prose content for any Prose unit that has cleared Gate 2 of Part 1 Rule 7.1.1. Within any single Gate 2 execution, the `.docx` write and the `.md` write are coupled — both run, in the same Gate 2 cycle, for the same Prose unit. The two files are never out of sync for Gate 2-accepted prose. If they differ, the `.docx` is authoritative (as the publication-format file) and the `.md` must be regenerated to match.

Divergence between chat history and the `.docx`/`.md` files is possible — and expected — when the user has issued `[SKIP WRITE]` at an Inter-Gate Confirmation Prompt. In that case, chat has a prose unit that neither file contains. This is not a parity violation (parity governs `.docx` ↔ `.md`, not chat ↔ files); it is a documented Gate 2 skip and is reconciled via a later corrective command such as `[REVISE PROSE]` or `[REDRAFT CHAPTER]`.

**Rule 7.1.3 — Gated Trigger Law.**
The `.md` file update is triggered at Gate 2 of Part 1 Rule 7.1.1, at the same point as the `.docx` update (Rule 6.5.1, Step 6). It is mandatory, coupled to the `.docx` write, and runs only on explicit `[CONFIRM WRITE]` received at the Inter-Gate Confirmation Prompt. The `.md` update is NOT automatic on prose acceptance alone — it requires Inter-Gate Confirmation just as the `.docx` write does.

### 7.2 — Markdown Formatting Standards (Canon v2.3 — Per-Prose Granularity)

**Rule 7.2.1 — Chapter Header Block Placement in Per-Prose Markdown.**
The Chapter Header Block is written once per Chapter, and it resides in the **first Prose markdown file of each Chapter** — i.e., the `prose-00001.md` stored under `chapter-NNN/area-1/`. It is the leading block of that file, preceding the Area Divider and the Prose body. Subsequent `prose-NNNNN.md` files within the same Chapter do NOT repeat the Chapter Header Block. Format (amended v3.3 to mandate Novel-Part Name and Chapter Name per Part 28 Area 18 Rule 18.3.3):

```markdown
# STARWARD SAGA
## Phase [N] — [Phase Name]
## Section [N] — [Section Name]
## Part [N] — [Novel-Part Name]    <!-- MANDATORY — Part 28 Area 18 -->

# Chapter [N] — [Chapter Name]    <!-- MANDATORY — Part 28 Area 18 -->

---
```

The Phase Name and Section Name are Locked Canon per Part 30 and must appear as authored there. The Novel-Part Name and Chapter Name are **categorically mandatory** under Part 28 Area 18 Rule 18.3.3 — no em-dash, no "TBD", no blank rendering; a missing Novel-Part Name or Chapter Name in a written `prose-NNNNN.md` first-Prose-of-Chapter file is an Audit Pass 2 FAIL under Part 1 Rule 7.1.1(k).

**Rule 7.2.2 — Area Dividers in Per-Prose Markdown.**
Each Area within the Chapter is preceded by an Area Divider heading, written as the leading block of the **first Prose markdown file of that Area** (i.e., the `prose-00001.md` stored under `chapter-NNN/area-N/`). Subsequent `prose-NNNNN.md` files within the same Area do NOT repeat the Area Divider. Format (amended v3.3 to mandate Area Name per Part 28 Area 18 Rule 18.3.3):

```markdown
## Area [N] — [Area Name]    <!-- MANDATORY — Part 28 Area 18 -->

```

The Area Divider uses `##` (H2 heading). The Area Name is **categorically mandatory** under Part 28 Area 18 Rule 18.3.3 — the prior fallback "Area Description if available" is **retired under v3.3**. An Area cannot be opened for Prose delivery until an Area Name has been authored; a missing Area Name in a written first-Prose-of-Area `.md` file is an Audit Pass 2 FAIL under Part 1 Rule 7.1.1(k). The Area Divider is followed by one blank line before the Prose Title Block (Rule 7.2.2a).

**Rule 7.2.2a — Prose Title Block (Mandatory on Every Prose Markdown File) — Authored v3.3.**
Every `prose-NNNNN.md` file — without exception, regardless of whether it is the first Prose of a Chapter, first Prose of an Area, or any subsequent Prose — must carry a **Prose Title Block** immediately preceding the Prose body. The Prose Title Block names the Prose unit in accordance with Part 28 Area 18 Rule 18.3.3 and is the markdown counterpart of the Rule 6.3.2a docx Prose Title Block. Format:

```markdown
### Prose [N] — [Prose Name]    <!-- MANDATORY — Part 28 Area 18 -->
*Reference: Phase.Section.Part.Chapter.Area.Prose*

```

The Prose Title Block uses `###` (H3 heading) for the Prose-number-and-name line and an italic one-line Reference Code beneath it, followed by one blank line before the Prose body. The Prose Name is **categorically mandatory** — a missing Prose Name in any written `prose-NNNNN.md` file is an Audit Pass 2 FAIL under Part 1 Rule 7.1.1(k). When the file is the first Prose of a Chapter or first Prose of an Area, the ordering of structural blocks is: Chapter Header Block (if applicable) → Area Divider (if applicable) → Prose Title Block → Prose body. When it is neither, the ordering is simply: Prose Title Block → Prose body.

**Rule 7.2.3 — Prose Paragraphs in Markdown.**
Each paragraph of a Prose unit is separated by a blank line. There is no indentation in Markdown (indentation renders as code blocks). Paragraphs are left-aligned by default.

**Rule 7.2.4 — Prose Unit Separation in Per-Prose Files and Aggregates.**
Each `prose-NNNNN.md` contains exactly one Prose unit's body (plus the Chapter Header Block and/or Area Divider prefix where applicable). When an on-demand Chapter-aggregate `chapter-NNN.md` is generated via C-24, consecutive Prose units within the same Area are concatenated into the aggregate with only a blank line between them (no divider heading, no horizontal rule); they flow as continuous prose within the Area section. If a scene break occurs within a Prose unit, it is rendered as:

```markdown
&nbsp;

\* \* \*

&nbsp;
```

**Rule 7.2.5 — Dialogue Formatting in Markdown.**
Per Part 2 Area 2 Rule 2.2.2 and Part 29 Rule 29.2.1.1, all dialogue is formatted in **double straight quotation marks AND italics simultaneously**. In Markdown, this is rendered by enclosing the full quoted span (opening double quote, spoken text, closing double quote) inside single asterisks:

```markdown
She stepped forward, hand resting on the hilt of her blade. *"You have one chance to answer me truthfully,"* she said, *"and I suggest you take it."*
```

The double quotation marks are **inside** the italic span and are themselves italicized together with the spoken text. Straight ASCII double quotes (`"`) are used; curly / smart quotes are prohibited. Single quotation marks are reserved exclusively for nested reported speech (a character quoting another character inside their own spoken line per Part 29 Rule 29.2.1.1a), rendered as `*"and then she said to me, 'you will not pass this gate,' as if it were settled."*`. The dialogue formatting is applied only to the spoken text, not to the surrounding narration.

**Rule 7.2.6 — Named Move and Cultivation Level Formatting in Markdown.**
Per Part 2 Area 3 Rules 3.2.1 and 3.2.1a, all Named Moves and all cultivation level designations are formatted in ***bold-italic*** in Markdown using triple-asterisks, both inside and outside dialogue:

```markdown
He raised his hand and released the ***Crushing Void Palm***, a wave of force that struck the stone wall like a silent thunderclap.
```

Named Moves in dialogue use triple-asterisks within the italic dialogue span:

```markdown
*"Watch carefully,"* Varys said, his eyes distant. *"This is what I call the ***Void Fracture Strike***."*
```

Qualifying cultivation level designations (full level strings, affinity+level strings, tier designations, named meridian designations) use the same triple-asterisk convention. Standalone realm names (Warrior, Champion, Ruler) are plain text:

```markdown
At ***Ruler Level 3 Mid***, the sweep covered the complete circuit. The Warrior breakthrough at seventeen had opened the first tier. The ***Void Root*** meridian held without deviation. ***Sovereignty-Swords Level 8*** did not rush.
```

**Rule 7.2.7 — Section Continuity.**
No structural labels beyond the Chapter Header Block and Area Dividers appear in the `.md` file. Novel-Part numbers, Section numbers, Phase numbers (beyond the header), and Prose unit numbers do not appear in the prose body.

### 7.3 — File Structure in Markdown (Canon v2.3 — Per-Prose)

**Rule 7.3.1 — Per-Prose Markdown File Structure Examples.**

*First Prose of a Chapter (carries Chapter Header Block + Area 1 Divider) — `phase-1/section-1/part-1/chapter-001/area-1/prose-00001.md`:*

```markdown
# STARWARD SAGA
## Phase 1 — The Roots of Becoming

# Chapter 1: The Citadels of Morning

---

## Area 1: Dawn at the Azure Sky Capital

[Prose unit 1, paragraph 1]

[Prose unit 1, paragraph 2]
```

*Subsequent Prose in the same Area — `.../area-1/prose-00002.md`:*

```markdown
[Prose unit 2, paragraph 1]

[Prose unit 2, paragraph 2]
```

*First Prose of a new Area within the same Chapter (carries Area Divider) — `.../area-2/prose-00001.md`:*

```markdown
## Area 2: The King's Challenge

[Prose unit 3, paragraph 1]

[Prose unit 3, paragraph 2]
```

**Rule 7.3.2 — Horizontal Rule Between Chapter Header and First Area (On-Demand Aggregate).**
In the Chapter-aggregate file `chapter-NNN.md` produced on demand via `[EXPORT CHAPTER]` (C-24), a horizontal rule (`---`) separates the Chapter Header Block from the first Area Divider (carried naturally from the first Prose file's leading block). In addition, a horizontal rule is inserted between each pair of consecutive Area sections within the aggregate to improve readability in markdown renderers. Per-Prose files themselves do not include inter-Area horizontal rules — they carry only the Chapter Header Block / Area Divider prefix appropriate to their position.

### 7.4 — Python Implementation for .md Files

**Rule 7.4.1 — Implementation Standard.**
All `.md` file creation and update operations use standard Python file I/O. No external library is required.

> **[Migration note]** This section originally embedded an outdated draft implementation, superseded by the authorized script `.claude/tools/prose_docx_creator.py` / `.claude/tools/prose_md_creator.py` — call it directly rather than reproducing code in canon text.

**Rule 7.4.2 — Dependency.**
Standard Python file I/O. No external library required beyond the Python standard library.

**Rule 7.4.3 — Error Handling.**
Same as Rule 6.4.3. If the `.md` write fails, the failure is reported in chat and flagged as a pending action without rolling back prose acceptance.

### 7.5 — Markdown Update Protocol (Two-Gate Flow, Canon v2.3 — Per-Prose)

**Rule 7.5.1 — Trigger Point (Per-Prose).**
The per-Prose `.md` write occurs at Gate 2b (Step 9) of the `[NEXT PROSE]` command flow (see Rule 6.5.1). It executes immediately after the per-Prose `.docx` write (Gate 2a / Step 8) and before the Post-Write Ledger Update (Step 10). Both file writes occur in the same Gate 2 cycle, following a single Inter-Gate Confirmation (`[CONFIRM WRITE]`) for that specific Prose unit, maintaining guaranteed parity between the `prose-NNNNN.docx` and `prose-NNNNN.md` of that Prose.

**Rule 7.5.2 — Rewind Behavior.**
Same as Rule 6.5.3. When `[REWIND TO]` archives non-canonical prose, the corresponding `prose-NNNNN.md` files at and after the rewind point are marked for replacement; they are overwritten (or deleted and re-created) when new Prose is written forward at the same narrative positions.

**Rule 7.5.3 — Aggregate Invalidation.**
If a Chapter-aggregate `chapter-NNN.md` exists for the Chapter whose per-Prose file is being created or overwritten, the aggregate is marked stale. Equivalent behavior applies to any Phase-aggregate `phase-N-complete.md`. Stale aggregates must be regenerated on the next invocation of their producing command (C-24 for Chapter aggregates, C-26 for Phase aggregates), or deleted outright.

### 7.6 — Governing Constraints (Canon v2.3 — Per-Prose)

**Rule 7.6.1 — Per-Prose Parity.**
Each Prose's `.md` file must always contain exactly the same prose body as its paired `.docx` file. Any operation that writes to one must write to both. A `prose-NNNNN.md` file that is out of sync with its paired `prose-NNNNN.docx` is a canon output error.

**Rule 7.6.2 — No Governance Content.**
The `.md` file contains only the novel's prose, formatted per this Area's standards (plus the Chapter Header Block and/or Area Divider prefix where applicable). Audit reports, ledger data, governance citations, and planning notes are never written to per-Prose output files.

**Rule 7.6.3 — Plain-Text Portability.**
The `.md` file is formatted to be fully readable as plain text even without a Markdown renderer. Formatting markers (`*`, `**`, `***`, `##`) are minimal and do not obscure the prose when read as raw text.

**Rule 7.6.4 — One Prose Per File.**
Each `prose-NNNNN.md` contains the body of exactly one Prose unit. Appending additional Prose bodies to an existing per-Prose file is forbidden.

### 7.7 — Gate 1 Position Header Block Boundary (Chat-Only)

**Rule 7.7.1 — Chat-Only Placement.**
The Gate 1 Position Header Block mandated by Part 1 Rule 7.1.1 is a **chat-only** artefact. It is **never** written to any `prose-NNNNN.md` file. Any occurrence of the Position Header Block inside a `.md` file is a structural contamination and a Rule 7.1.1(k) Post-Write Audit FAIL.

**Rule 7.7.2 — Distinction from Markdown Chapter Header Block and Area Divider.**
The Gate 1 Position Header Block is categorically distinct from the Markdown-format Chapter Header Block (Rule 7.2.1) and Area Divider (Rule 7.2.2). The markdown Chapter Header Block and Area Divider are reader-facing `# / ## / ---` structures that live inside designated first-Prose `.md` files; the Gate 1 Position Header Block is a governance-facing chat-only orientation block. The three artefacts have disjoint placements: Gate 1 Position Header Block → chat only; Chapter Header Block → first Prose `.md` file of each Chapter; Area Divider → first Prose `.md` file of each Area.

**Rule 7.7.3 — Cross-Reference.**
For the canonical format of the Gate 1 Position Header Block see Part 1 Rule 7.1.1 "Gate 1 Position Header Block (Mandatory)". For the Two-Audit Mandate that verifies both chat-level Gate 1 delivery and `.md` / `.docx` Gate 2 file integrity, see Part 1 Rule 7.1.1(k).

---

## Cross-References
| Related Skill | Relation | Source |
|---|---|---|
| ssc-cultivation-p03-cultivation-ladder-realm-hierarchy | SOFT | Rule 7.2.6 mandates bold-italic markdown formatting for cultivation level designations (full realm+level strings, tier designations, e.g. "Ruler Level 3 Mid"); this skill defines the realm/level naming that rule formats — a real but purely typographic tie, not a content dependency |
| ssc-cultivation-p03-affinity-cultivation | SOFT | Rule 7.2.6 mandates bold-italic markdown formatting for full affinity+level strings; this skill defines the affinity-cultivation naming that rule formats — a real but purely typographic tie, not a content dependency |
| ssc-cultivation-p03-lifespan-mechanics | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 7 governs markdown companion-file formatting/parity rules with no rule tied to lifespan mechanics |
| ssc-cultivation-p03-power-density | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 7 governs markdown companion-file formatting/parity rules with no rule tied to power-density mechanics |
| ssc-cultivation-p03-realm-transition | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 7 governs markdown companion-file formatting/parity rules with no rule tied to realm-transition mechanics (Rule 7.2.6 formats realm+level naming, not transition mechanics) |
| ssc-cultivation-p03-cultivation-talent | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 7 governs markdown companion-file formatting/parity rules with no rule tied to cultivation-talent mechanics |
| ssc-cultivation-p03-growth-speed | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 7 governs markdown companion-file formatting/parity rules with no rule tied to growth-speed mechanics |
| ssc-cultivation-p03-power-comparison | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 7 governs markdown companion-file formatting/parity rules with no rule tied to power-comparison mechanics |
| ssc-cultivation-p03-damage-tolerance-recovery | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 7 governs markdown companion-file formatting/parity rules with no rule tied to damage-tolerance/recovery mechanics |
| ssc-cultivation-p03-heart-cultivation | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 7 governs markdown companion-file formatting/parity rules with no rule tied to heart-cultivation mechanics |

## Governing Authority
Subordinate to the shared Part 1 (audit law) + Part 34 (knowledge graph) grounding in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.

## Source Provenance
Part 2, Area 7 — "Book Creation Law: Chapter Markdown File (.md)" · canon v4.33 · migrated 2026-08-03
