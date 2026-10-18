---
name: ssc-narration-p02-book-creation-law-chapter-document
description: Covers the full formatting, structural, and procedural law governing the per-Prose and Chapter-aggregate .docx output files of the Starward Saga novel-writing process — page setup, typography, dialogue/named-move/cultivation-level docx formatting, drop caps, Chapter Header Block / Area Divider / Prose Title Block placement and mandatory fields, phase icon insertion, the two-gate docx update protocol tied to [CONFIRM WRITE], rewind and aggregate invalidation behavior, governing constraints on reader-facing content, and the chat-only boundary of the Gate 1 Position Header Block. Reach for this Area whenever an agent is about to create or update a prose-NNNNN.docx file, run [NEXT PROSE]/[START STORY]/[EXPORT CHAPTER], decide what belongs in a Chapter Header Block, Area Divider, or Prose Title Block, resolve docx-vs-chat formatting questions, or invoke the authorized .claude/tools/prose_docx_creator.py script. This is canon Part 2 Area 6, domain narration.
user-invocable: false
---

## Rule Text (Verbatim Source — Authoritative)
## Area 6 — Book Creation Law: Chapter Document (.docx)

### 6.1 — Purpose and Mandate

**Rule 6.1.1 — Purpose.**
The chapter `.docx` file is the **primary publication-format output** of the novel-writing process. It is formatted to professional novel publishing standards, suitable for direct reading, editorial review, and eventual print or digital publication preparation. Every formatting decision in this Area is made in service of that standard — not convenience, not ease of parsing, but reader experience at the level of a published novel.

**Rule 6.1.2 — Governing Standard.**
The formatting standard for all `.docx` output — both per-Prose files written during `[START STORY]` / `[NEXT PROSE]` and Chapter-aggregate exports produced by `[EXPORT CHAPTER]` — is the **Starward Saga Novel-Grade Typeset Format**: 6" × 9" trade paperback, EB Garamond body font, 1.15× line spacing, with phase icon ornament, drop cap openings, and running headers/footers. This is a unified format: the per-Prose `.docx` files are already publication-ready; `[EXPORT CHAPTER]` assembles them without reformatting. The typeset standard is defined in full in Rules 6.2 through 6.7 of this Area and in Area 10 (Chapter Export Format Specification). The two Areas govern the same standard — Area 6 governs per-Prose implementation; Area 10 governs the assembly and export rules.

**Rule 6.1.3 — Gated Trigger Law.**
Every accepted Prose unit, after passing the Post-Output Audit and the Gate 1 chat delivery of Part 1 Rule 7.1.1, enters the Inter-Gate Confirmation state. The docx update protocol (Rule 6.5) executes only on explicit user `[CONFIRM WRITE]` at the Inter-Gate Confirmation Prompt. The docx write is mandatory once `[CONFIRM WRITE]` is received, but is never performed before that confirmation is received. The write occurs as part of the `[NEXT PROSE]` command's execution flow at Gate 2, after the Post-Output Audit passes, after Gate 1 chat delivery, after Inter-Gate Confirmation, and before the position display is updated.

### 6.2 — Document Formatting Standards

**Rule 6.2.1 — Page Setup.**
```
Page Size:          6" × 9" (trade paperback trim — standard for fantasy/sci-fi fiction)
Margins:            Top: 1.0" | Bottom: 1.0" | Left: 0.875" | Right: 0.875"
Header (even/left): "STARWARD SAGA"  — centered, EB Garamond 9pt, #5A5A5A
Header (odd/right): Chapter title in FULL CAPS — centered, EB Garamond 9pt, #5A5A5A
Footer:             Page number — left-aligned on even pages, right-aligned on odd pages
                    EB Garamond 9pt
```

**Rule 6.2.2 — Typography Standards.**
```
Body Font:              EB Garamond 12pt
Line Spacing:           1.15× (published trade paperback standard for 12pt type on 6×9 page)
First Line Indent:      0.3 inches — suppressed on first paragraph after any structural header
Alignment:              Left-aligned (NOT justified)
Space Before Paragraph: 0pt
Space After Paragraph:  0pt

Chapter Heading Font:        EB Garamond, Bold, centered, black
Chapter Heading Hierarchy:
  Series title (H1): 18pt   — "STARWARD SAGA"
  Phase + Section   (H2): 13pt  — "Phase 1 — The Roots of Becoming / Section 1 — The Citadels of Morning"
  Novel-Part        (H3): 13pt  — "Part 1 — [Novel-Part Name]"
  Chapter title     (H4): 22pt  — "Chapter 001 — [Chapter Name]"

Area Divider:
  Page break before every Area
  ⁂ asterism ornament (U+2042): EB Garamond 14pt, deep navy (#1A2A4A), centered
  24pt breathing space above ⁂, 24pt below ⁂
  Area name (H5): EB Garamond 11pt Bold Italic, centered — "[Area Name]"

Prose Title Block (on every Prose file):
  Phase icon PNG: 0.55" wide, centered; 12pt space before, 4pt space after
  Prose title (H6): EB Garamond 11pt Italic, centered — "Prose N — [Prose Name]"
  Reference code: EB Garamond 9pt Regular Italic, centered

Drop Cap + Small Caps (Chapter and Area openings):
  First character of opening paragraph: EB Garamond 28pt Bold (≈ 3 text lines tall)
  Next ~4 words: EB Garamond small caps
  Remainder: standard body style

Scene Break Symbol: ⁂ asterism (U+2042), EB Garamond 12pt, centered
                    Used between Prose units within an Area for significant time skip/location shift
```

**Rule 6.2.3 — Dialogue Formatting in Docx.**
Dialogue in Prose output is formatted in **double straight quotation marks AND italics simultaneously** in the docx file, following Part 2 Area 2 Rule 2.2.2 and Part 29 Rule 29.2.1.1. The italics are applied using the docx character-level italic style (not a paragraph style) to the full quoted span — the opening double quotation mark, the spoken text, and the closing double quotation mark are all inside the italic run. Dialogue is visually distinguished from narration within every paragraph by the simultaneous presence of both markers. Docx generation code must insert the straight double quotation mark characters (ASCII 0x22) rather than curly/smart quotes; no autocorrect-style substitution is permitted.

**Rule 6.2.4 — Named Move and Cultivation Level Formatting in Docx.**
All Named Moves, Named Techniques, and Named Cultivation Practice names (per Part 2 Area 3 Rule 3.2.1) are formatted in ***bold-italic*** using the docx character-level bold + italic style simultaneously — both inside dialogue and outside dialogue. There is no dialogue exception: bold-italic applies universally. Qualifying cultivation level designations (per Part 2 Area 3 Rule 3.2.1a) are formatted in ***bold-italic*** in the same manner: full realm+level strings, full affinity+level strings, tier designations, and named meridian designations. Standalone realm names (Champion, Warrior, Ruler, etc.) are plain text and are not formatted bold-italic. The Markdown input marker `***text***` is parsed by `_parse_inline_formatting()` in `prose_docx_creator.py` and rendered as a docx run with both `bold=True` and `italic=True`.

**Rule 6.2.5 — No Visible Structure Labels in Prose.**
Per Principle P2-4 (No Meta-Constructs in Prose), no structural labels — Phase, Section, Novel-Part, Area, Prose number — appear within the prose body text of the docx. These labels are visible only in the Chapter Heading and Area Divider formatting elements, which serve as navigational aids for the author and editor, not as narrative text visible to the reader. When the file is prepared for final publication, Area Dividers and structural notation are removed from the prose body, leaving only the chapter text.

### 6.3 — Chapter Structure in the Docx File (Canon v2.3 — Per-Prose Granularity)

**Rule 6.3.1 — Chapter Header Block Placement Under Per-Prose Granularity.**
The Chapter Header Block is written once per Chapter, and it resides in the **first Prose file of each Chapter** — i.e., the `prose-00001.docx` stored under `chapter-NNN/area-1/`. It is the leading block of that file, preceding the Area Divider and the Prose body. Subsequent Prose files within the same Chapter (Area 1 Prose 2, 3, …; Area 2 Prose 1, 2, …; etc.) do NOT repeat the Chapter Header Block. Format (amended v3.3 to mandate Novel-Part Name and Chapter Name per Part 28 Area 18 Rule 18.3.3):

```
[Phase icon PNG: phase-icon.png from novel-starward-saga/phase-N/ — 1.0" wide,
 centered; 24pt space before, 12pt space after — Rule 6.4.2]
STARWARD SAGA
PHASE [N] — [Phase Name]
SECTION [N] — [Section Name]
PART [N] — [Novel-Part Name]    (MANDATORY — Part 28 Area 18)

Chapter [Chapter Number] — [Chapter Name]    (MANDATORY — Part 28 Area 18)
[blank line — 24pt spacing]
```

**Rule 6.3.1a — Phase Icon in Chapter Header Block (Rule 6.4.2):** The phase icon PNG (`phase-icon.png` from `novel-starward-saga/phase-N/`) is the first element of the Chapter Header Block — placed above "STARWARD SAGA", centered, 1.0 inch wide, with 24pt space before and 12pt space after. If the icon file is not found, the header renders without it (graceful fallback). For Phase 1 the icon path is `novel-starward-saga/phase-1/phase-icon.png`.

> **[Repo layout note]** `novel-starward-saga/phase-N/` above refers to `projects/novel-starward-saga/phase-N/` in the current repo layout (post-.claude/ migration).

All text lines of the Chapter Header Block are center-aligned, Times New Roman, 16pt Bold. The Phase Name and Section Name are Locked Canon per Part 30 and must appear as authored there. The Novel-Part Name and Chapter Name are **categorically mandatory** under Part 28 Area 18 Rule 18.3.3 — no em-dash fallback, no "TBD" placeholder, and no blank rendering is permitted; a missing Novel-Part Name or Chapter Name in a written `prose-NNNNN.docx` first-Prose-of-Chapter file is an Audit Pass 2 FAIL under Part 1 Rule 7.1.1(k).

**Rule 6.3.2 — Area Dividers Under Per-Prose Granularity.**
Each time a new Area begins within the Chapter, an Area Divider is inserted as a leading block in the **first Prose file of that Area** — i.e., the `prose-00001.docx` stored under `chapter-NNN/area-N/`. It precedes the Prose body (and the Prose Title Block of Rule 6.3.2a) in that file. Subsequent Prose files within the same Area do NOT repeat the Area Divider. Format (amended v3.3 to mandate Area Name per Part 28 Area 18 Rule 18.3.3):

```
[blank line]
— Area [N]: [Area Name] —    (MANDATORY — Part 28 Area 18)
[blank line]
```

The Area Divider is Times New Roman 11pt Bold Italic, center-aligned. The Area Name is **categorically mandatory** under Part 28 Area 18 Rule 18.3.3 — the prior fallback "If no description is available, 'Area N' is used" is **retired under v3.3**. An Area cannot be opened for Prose delivery until an Area Name has been authored per Part 28 Rule 18.3.2, and a missing Area Name in a written first-Prose-of-Area file is an Audit Pass 2 FAIL under Part 1 Rule 7.1.1(k).

**Rule 6.3.2a — Prose Title Block (Mandatory on Every Prose File) — Authored v3.3.**
Every `prose-NNNNN.docx` file — without exception, and regardless of whether it is the first Prose of a Chapter, first Prose of an Area, or any subsequent Prose — must carry a **Prose Title Block** immediately preceding the Prose body. The Prose Title Block names the Prose unit in accordance with Part 28 Area 18 Rule 18.3.3 and is the in-file counterpart of the Gate 1 chat Position Header Block (which is chat-only per Rule 7.1.1). Format:

```
[blank line]
Prose [Prose Number] — [Prose Name]    (MANDATORY — Part 28 Area 18)
[Reference Code: Phase.Section.Part.Chapter.Area.Prose]
[blank line]
```

The Prose Title Block is Times New Roman 12pt Bold, center-aligned; the Reference Code line is 10pt Regular, center-aligned, italic. The Prose Name is **categorically mandatory** — a missing Prose Name in any written `prose-NNNNN.docx` file is an Audit Pass 2 FAIL under Part 1 Rule 7.1.1(k). When this file is the first Prose of a Chapter or the first Prose of an Area, the ordering of structural blocks is: Chapter Header Block (if applicable) → Area Divider (if applicable) → Prose Title Block → Prose body. When it is neither (e.g., `area-1/prose-00002.docx`), the ordering is simply: Prose Title Block → Prose body.

**Rule 6.3.3 — Prose Units in Per-Prose Files.**
Each `prose-NNNNN.docx` file contains the body of exactly one Prose unit. For the first Prose file of an Area (`area-N/prose-00001.docx`), the body begins immediately after the Prose Title Block (Rule 6.3.2a), which itself follows the Area Divider (Rule 6.3.2); additionally, for the first Prose file of the Chapter (`chapter-NNN/area-1/prose-00001.docx`), the body begins after the Chapter Header Block (Rule 6.3.1), the Area 1 Divider (Rule 6.3.2), and the Prose Title Block (Rule 6.3.2a) in that order. For all other per-Prose files, the body begins immediately after the Prose Title Block (Rule 6.3.2a) — the Prose Title Block is the one structural block that appears on **every** Prose file, not just first-of-Chapter or first-of-Area files. The first paragraph of the Prose body does NOT have a first-line indent (standard publishing convention of no indent after a break or at file start). All subsequent paragraphs within the Prose unit have a 0.5-inch first-line indent.

**Rule 6.3.4 — On-Demand Chapter Aggregate Structure.**
When `[EXPORT CHAPTER]` (C-24) is invoked, the resulting Chapter-aggregate `chapter-NNN.docx` is constructed by concatenating every per-Prose `.docx` under the Chapter folder in canonical order (Area 1 Prose 1, …, Area N Prose M). Because the Chapter Header Block and Area Dividers are already carried in the correct first-Prose files, simple concatenation preserves the intended structural layout. The aggregate is a derived artifact; the per-Prose files remain authoritative.

**Rule 6.3.4 — Scene Breaks Within a Prose Unit.**
If a scene break occurs within a Prose unit (a significant time skip or location shift), it is rendered as a three-centered-asterisk break:

```
[blank double-spaced line]
   ***
[blank double-spaced line]
```

The asterisk break is formatted in 12pt Times New Roman, center-aligned. This element is only used for scene breaks within a single Prose unit — it is not used between Prose units or between Areas.

### 6.4 — Python-docx Code Template

**Rule 6.4.1 — Implementation Standard.**
All `.docx` file creation and update operations use the `python-docx` library. The following code template defines the canonical implementation. This template is the authoritative implementation reference — any deviation from this template's formatting parameters constitutes a violation of the docx formatting standard.

**Rule 6.4.2 — Phase Icon Placement Law.**
The phase icon PNG (`phase-icon.png` located in the `novel-starward-saga/phase-N/` folder for each Phase N) must be inserted in two locations in every `.docx` file:
1. **Chapter Header Block** (first prose of each chapter only): Icon at top, 1.0" wide, centered, 24pt space before, 12pt space after — before "STARWARD SAGA" (Rule 6.3.1a).
2. **Prose Title Block** (every prose file, mandatory): Icon centered, 0.55" wide, 12pt space before, 4pt space after — immediately before the Prose title line (Rule 6.2.2).

The icon dimensions (300×360px RGBA PNG) allow for clean scaling at both sizes. If the icon file does not exist at the expected path, the DOCX is produced without the icon (graceful fallback) — but a missing icon is a non-critical Audit Pass 2 advisory. The canonical `get_phase_icon_path(phase_number)` helper (defined in the code template below) provides the path; callers check existence before inserting.

> **[Repo layout note]** `novel-starward-saga/phase-N/` above refers to `projects/novel-starward-saga/phase-N/` in the current repo layout (post-.claude/ migration).

**Rule 6.4.3 — Stored Python Script.**
The complete DOCX creation Python script is stored as a live, runnable file at `novel-writer/prose_docx_creator.py`. This file is the canonical implementation — it is used directly at Gate 2 for all prose DOCX creation. The code template in this Area is the specification; `prose_docx_creator.py` is the execution artifact. When the template is updated, `prose_docx_creator.py` must be updated to match in the same session.

> **[Repo layout note]** `novel-writer/prose_docx_creator.py` above refers to `.claude/tools/prose_docx_creator.py` in the current repo layout (post-.claude/ migration).

> **[Migration note]** This section originally embedded an outdated draft implementation, superseded by the authorized script `.claude/tools/prose_docx_creator.py` / `.claude/tools/prose_md_creator.py` — call it directly rather than reproducing code in canon text.

**Rule 6.4.2 — Dependency.**
The `python-docx` library must be installed in the Python environment. Installation: `pip install python-docx --break-system-packages`. The code template is executed in the sandboxed Linux shell via the Bash tool every time a Prose unit is accepted.

**Rule 6.4.3 — Error Handling.**
If the python-docx write operation fails (library not installed, disk error, path error), the failure is reported in chat immediately. The Prose acceptance is not rolled back — the prose has already been accepted into canon. The failed file write is flagged as a pending action in the `[STATUS]` report until it is successfully completed (by re-running the write operation or invoking `[EXPORT CHAPTER]`).

### 6.5 — Docx Update Protocol (Two-Gate Flow, Canon v2.3 — Per-Prose)

**Rule 6.5.1 — Trigger Point (Per-Prose).**
The per-Prose docx write is triggered at Gate 2 of Part 1 Rule 7.1.1 — after the Post-Output Audit returns PASS, after Gate 1 chat delivery, and after Inter-Gate Confirmation (`[CONFIRM WRITE]`) for that specific Prose unit. It executes immediately before the paired per-Prose markdown write (Rule 7.5.1) and before the Post-Write Ledger Update (Part 1 Area 6.3). Execution order within the `[NEXT PROSE]` command flow:

```
 1. Pre-Prose Read Mandate (Part 1 Rule 7.1.1(i)) — read all stored
    prose-NNNNN.md files for the current Chapter and adjacent positions.
 2. Pre-Write Ledger Check (Part 1 Area 6.2)
 3. Pre-Output Audit (Part 1 Area 4.2.1)
 4. Write Prose Unit (at pacing-appropriate depth: 3500%–5000%; Fast 1400–1800 words / Medium 1900–2300 / Slow 2400–2700, per-tier max ceilings 2000/2500/3000, absolute hard cap 3000; per Part 2 Area 6.2.1, Canon v4.34 Pacing Law Amendment)
 5. Post-Output Audit (Part 1 Area 4.2.2)
    → IF PASS: continue to step 6
    → IF FAIL: corrections required; do not proceed to Gate 1 until corrected
 6. GATE 1 — CHAT DELIVERY (Part 1 Rule 7.1.1 — automatic, unconditional)
    The Prose is displayed in full in chat.
 7. INTER-GATE CONFIRMATION (Part 1 Rule 7.1.1 — mandatory halt)
    Display FILE-WRITE CONFIRMATION REQUIRED prompt.
    → On [CONFIRM WRITE]: proceed to step 8
    → On [REVISE PROSE]: author revision, loop to step 6 on revised prose
    → On [SKIP WRITE]: skip steps 8–9, proceed directly to step 10 with divergence warning
 8. GATE 2a — *** PER-PROSE DOCX WRITE (Area 6.5.1 — this step) ***
    Create any missing folders in the nested path
    novel-starward-saga/phase-N/section-N/part-N/chapter-NNN/area-N/,
    then create and write prose-NNNNN.docx containing:
      - Chapter Header Block  (only if this is prose-00001 of Area 1 of the Chapter)
      - Area Divider          (only if this is prose-00001 of the Area)
      - Prose Title Block     (ALWAYS — Rule 6.3.2a: "Prose N — [Prose Name]" + Reference Code)
      - Prose body            (always)
 9. GATE 2b — *** PER-PROSE MD WRITE (Area 7.5.1) ***
10. Post-Write Ledger Update (Part 1 Area 6.3)
11. Post-Prose Completeness Indicator emission (Part 1 Rule 7.1.1(j); Part 2 Area 8)
12. Position display update
```

> **[Repo layout note]** `novel-starward-saga/phase-N/section-N/part-N/chapter-NNN/area-N/` above (step 8) refers to `projects/novel-starward-saga/phase-N/section-N/part-N/chapter-NNN/area-N/` in the current repo layout (post-.claude/ migration).

**Rule 6.5.2 — What is Written.**
Only the accepted, Post-Output-Audit-passed prose text is written to the `prose-NNNNN.docx` file (plus, where applicable, the Chapter Header Block and/or Area Divider prefix). Pre-audit drafts, planning notes, and audit reports are never written to any per-Prose output file.

**Rule 6.5.3 — Rewind Behavior.**
When `[REWIND TO]` (C-16) is invoked and per-Prose files from the rewind point onward are archived as non-canonical, those per-Prose `.docx` files are **marked for replacement** but not immediately deleted. When new prose replaces the archived prose at the same narrative position, the non-canonical `prose-NNNNN.docx` is deleted or overwritten as part of the new Gate 2 write at that position.

**Rule 6.5.4 — Aggregate Invalidation.**
If a Chapter-aggregate `chapter-NNN.docx` exists for the Chapter whose per-Prose file is being created or overwritten, the aggregate is marked stale (either deleted outright or flagged for regeneration on the next `[EXPORT CHAPTER]` invocation). Equivalent behavior applies to any Phase-aggregate `phase-N-complete.docx` or Novel-aggregate `starward-saga-complete.docx`.

### 6.6 — Governing Constraints (Canon v2.3 — Per-Prose)

**Rule 6.6.1 — Reader-Facing Content Only.**
Per-Prose docx output files contain only the novel's prose plus the three permitted structural elements: (a) **Chapter Header Block** on the first Prose file of each Chapter — reader-facing; (b) **Area Divider** on the first Prose file of each new Area — editorial annotation; (c) **Prose Title Block** on every Prose file without exception — author navigation aid (carries Prose Name and Reference Code). No other content appears: no audit reports, no ledger data, no canon rule citations, no structural position notation within the prose body, no planning notes, and no governance information. The Gate 1 Position Header Block is categorically excluded (chat-only per Rule 6.7.1).

**Rule 6.6.2 — Formatting Immutability.**
The formatting parameters defined in Rules 6.2.1 and 6.2.2 are Locked Canon for all Phase 1 per-Prose output. They may not be overridden per-Prose, per-Chapter, or per-Phase without a canon amendment. Consistency across all per-Prose files is required so that on-demand Chapter/Phase/Novel aggregates remain uniform.

**Rule 6.6.3 — No Prose Modification.**
The per-Prose docx write writes prose exactly as it was accepted. It does not paraphrase, summarize, expand, or alter the prose in any way. The python-docx code writes the accepted prose text and nothing else (plus the designated structural prefixes where applicable).

**Rule 6.6.4 — One Prose Per File.**
Each `prose-NNNNN.docx` contains the body of exactly one Prose unit. No `prose-NNNNN.docx` file may contain body content from more than one Prose unit. Appending additional Prose bodies to an existing per-Prose file is forbidden.

### 6.7 — Gate 1 Position Header Block Boundary (Chat-Only)

**Rule 6.7.1 — Chat-Only Placement.**
The Gate 1 Position Header Block mandated by Part 1 Rule 7.1.1 is a **chat-only** artefact. It orients the user to the current narrative position (Phase / Section / Part / Chapter / Area / Prose with names and counts, Reference code, Date Stamp) at the moment of Gate 1 Chat Delivery. It is **never** written to any `prose-NNNNN.docx` file. Any occurrence of the Position Header Block inside a `.docx` file is a structural contamination and a Rule 7.1.1(k) Post-Write Audit FAIL.

**Rule 6.7.2 — Distinction from Chapter Header Block and Area Divider.**
The Gate 1 Position Header Block is categorically distinct from the file-level Chapter Header Block (Rule 6.3.1) and the file-level Area Divider (Rule 6.3.2). The Chapter Header Block and Area Divider are **reader-facing** structural elements that live inside designated first-Prose `.docx` files; the Gate 1 Position Header Block is a **governance-facing** chat-only orientation block that never reaches any published file. The three artefacts have disjoint placements: Gate 1 Position Header Block → chat only; Chapter Header Block → first Prose file of each Chapter; Area Divider → first Prose file of each Area.

**Rule 6.7.3 — Cross-Reference.**
For the canonical format of the Gate 1 Position Header Block see Part 1 Rule 7.1.1 "Gate 1 Position Header Block (Mandatory)". For the Two-Audit Mandate that uses both Gate 1 (where the Position Header Block appears) and Gate 2 file integrity, see Part 1 Rule 7.1.1(k).

---

## Cross-References
| Related Skill | Relation | Source |
|---|---|---|
| ssc-cultivation-p03-cultivation-ladder-realm-hierarchy | SOFT | Rule 6.2.4 mandates bold-italic docx formatting for qualifying cultivation level designations (full realm+level strings, tier designations); this skill defines the realm/level naming that rule formats — a real but purely typographic tie, not a content dependency |
| ssc-cultivation-p03-affinity-cultivation | SOFT | Rule 6.2.4 mandates bold-italic docx formatting for full affinity+level strings; this skill defines the affinity-cultivation naming that rule formats — a real but purely typographic tie, not a content dependency |
| ssc-cultivation-p03-lifespan-mechanics | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 6 governs .docx typography/formatting mechanics with no rule tied to lifespan mechanics |
| ssc-cultivation-p03-power-density | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 6 governs .docx typography/formatting mechanics with no rule tied to power-density mechanics |
| ssc-cultivation-p03-realm-transition | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 6 governs .docx typography/formatting mechanics with no rule tied to realm-transition mechanics (Rule 6.2.4 formats realm+level naming, not transition mechanics) |
| ssc-cultivation-p03-cultivation-talent | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 6 governs .docx typography/formatting mechanics with no rule tied to cultivation-talent mechanics |
| ssc-cultivation-p03-growth-speed | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 6 governs .docx typography/formatting mechanics with no rule tied to growth-speed mechanics |
| ssc-cultivation-p03-power-comparison | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 6 governs .docx typography/formatting mechanics with no rule tied to power-comparison mechanics |
| ssc-cultivation-p03-damage-tolerance-recovery | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 6 governs .docx typography/formatting mechanics with no rule tied to damage-tolerance/recovery mechanics |
| ssc-cultivation-p03-heart-cultivation | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 6 governs .docx typography/formatting mechanics with no rule tied to heart-cultivation mechanics |

## Governing Authority
Subordinate to the shared Part 1 (audit law) + Part 34 (knowledge graph) grounding in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.

## Source Provenance
Part 2, Area 6 — "Book Creation Law: Chapter Document (.docx)" · canon v4.33 · migrated 2026-08-03
