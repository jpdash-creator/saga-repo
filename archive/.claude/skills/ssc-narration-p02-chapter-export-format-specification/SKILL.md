---
name: ssc-narration-p02-chapter-export-format-specification
description: Governs the novel-grade typeset assembly rules for the [EXPORT CHAPTER] command (Part 1 C-24) — 6x9 trade paperback page setup, EB Garamond typography, the seven-level H1-H5 header hierarchy, phase icon ornaments, the asterism area-break ornament, running headers/footers and page numbers, drop cap/small caps chapter and area openings, deferred Table of Contents policy, and the canonical export_chapter.py implementation and invocation syntax. Reach for this when assembling, formatting, previewing, or troubleshooting a chapter-NNN.docx/.pdf export, when a prose-producing command needs to know header/typography/ornament rules for exported output, or when validating that export_chapter.py conforms to canon. This is canon Part 2 Area 10, domain narration.
user-invocable: false
---

## Rule Text (Verbatim Source — Authoritative)
## Area 10 — Chapter Export Format Specification (Canon v4.24)

### 10.1 — Purpose and Scope

**Rule 10.1.1 — Novel-Grade Export Mandate.**
When `[EXPORT CHAPTER: N]` (Part 1 C-24) is invoked, the resulting `chapter-NNN.docx` and `chapter-NNN.pdf` are assembled from the per-Prose `.docx` files — which are already formatted to the novel-grade typeset standard defined in Area 6 (EB Garamond, 6×9, 1.15×, with phase icons, drop cap openings, and running headers/footers). **[EXPORT CHAPTER] is primarily an assembly operation**: it concatenates the per-Prose `.docx` files in canonical order, inserts page breaks between Areas (already handled at per-Prose file boundaries), ensures running headers carry the correct chapter title on odd pages, and generates the PDF via LibreOffice. No reformatting is required because the per-Prose files are already publication-ready. The export is produced by `export_chapter.py` (stored at the Starward Saga project root). The per-Prose `.md` source files remain the authoritative canonical substrate for content; the `.docx` per-Prose files are the authoritative format substrate.

**Rule 10.1.2 — Dual Output Mandate.**
Every Chapter export produces both a DOCX file and a PDF file. The PDF is generated from the DOCX via LibreOffice headless conversion (`libreoffice --headless --convert-to pdf`). Both files are written to the Chapter folder root (`chapter-NNN/chapter-NNN.docx` and `chapter-NNN/chapter-NNN.pdf`), alongside the `area-N/` subfolders.

**Rule 10.1.3 — Source Files.**
The export reads only the per-Prose `.md` files (all `area-*/prose-*.md` files under the Chapter folder, in canonical order). The per-Prose `.docx` files are not used as export source. The `.md` files are parsed for hierarchy markers (H1 chapter title, H2 area name, H3 prose title), metadata (Reference, POV, Date), and body paragraphs.

### 10.2 — Page and Typography Standards

**Rule 10.2.1 — Page Size.**
The exported document uses 6" × 9" trade paperback trim size — the standard for fantasy and science-fiction hardcovers and trade paperbacks.

**Rule 10.2.2 — Margins.**
Left and right margins: 0.875 inches. Top and bottom margins: 1.0 inch. These match the standard interior margins for trade paperback fiction.

**Rule 10.2.3 — Body Font.**
Body font: EB Garamond, 12pt. EB Garamond is a classical serif typeface standard in fantasy and literary fiction. It must be installed on the user's system for the DOCX to display correctly and for LibreOffice to render it in the PDF. If EB Garamond is not installed, the document falls back to the system's default serif font gracefully; the font name specification in the DOCX is still written as "EB Garamond".

**Rule 10.2.4 — First-Line Indent.**
All body paragraphs use a 0.3" first-line indent, matching the standard for trade paperback prose indentation. The first paragraph after any structural header (Chapter header, Area name, or Prose title) uses no first-line indent — classic novel typography convention.

**Rule 10.2.5 — Line Spacing.**
Body line spacing: 1.15× (slightly tighter than double-space manuscript format, matching published trade paperback standards for 12pt type on a 6×9 page).

**Rule 10.2.6 — Paragraph Spacing.**
No additional space before or after body paragraphs (space_before = 0, space_after = 0). Paragraph separation is conveyed entirely through first-line indent, not spacing.

### 10.3 — Header Hierarchy

**Rule 10.3.1 — Seven-Level Export Hierarchy.**
The Chapter export document uses the following header hierarchy, rendered in EB Garamond, centered, black:

| Level | Content | Size | Weight |
|---|---|---|---|
| H1 | Section name (e.g., "Section I — The Cradle Worlds") | 16pt | Regular |
| H2 | Part name (e.g., "Part I — Before the Turning") | 13pt | Italic |
| [page break] | Chapter begins on new page | — | — |
| H3a | Chapter number (e.g., "Chapter 001") | 10pt | Regular |
| H3b | Chapter title (e.g., "Twin Courts at Dawn") | 18pt | Bold |
| H4 | Area name (e.g., "Area 1 — Paired Sovereigns") | 11pt | Regular |
| H5 | Prose title (e.g., "The Hum of the Sapphire Line") | 9pt | Italic |

**Rule 10.3.2 — Section and Part Headers.**
Section and Part names appear once at the beginning of the document, before the Chapter page break. They serve as context headers for the reader and are not repeated.

**Rule 10.3.3 — Chapter Page Break.**
The Chapter header (H3a + H3b) begins on a new page. A page break is inserted between the Part header and the Chapter number header.

**Rule 10.3.4 — Area Transition.**
Every Area — including the first Area of a Chapter — begins on a new page. A page break is inserted, followed by the ⁂ asterism ornament (see Rule 10.5.1), followed by the Area name header (H4). This gives each Area the visual weight of a chapter-within-a-chapter, consistent with the scale of narrative contained in an Area.

**Rule 10.3.5 — Prose Title Block.**
Before every Prose body, the phase icon (Rule 10.4.1) is inserted followed by the Prose title (H5). This structure appears for every Prose unit regardless of position — it is not suppressed for the first Prose of a Chapter or Area.

### 10.4 — Phase Icon Ornament

**Rule 10.4.1 — Icon Specification.**
Each Phase has a dedicated ornamental icon stored as both SVG and PNG in the Phase folder:
- SVG: `novel-starward-saga/phase-N/phase-icon.svg`
- PNG: `novel-starward-saga/phase-N/phase-icon.png`

> **[Repo layout note]** `novel-starward-saga/phase-N/phase-icon.svg` above refers to `projects/novel-starward-saga/phase-N/phase-icon.svg` in the current repo layout (post-.claude/ migration).
> **[Repo layout note]** `novel-starward-saga/phase-N/phase-icon.png` above refers to `projects/novel-starward-saga/phase-N/phase-icon.png` in the current repo layout (post-.claude/ migration).

**Rule 10.4.2 — Phase 1 Icon Design.**
Phase 1 ("Before the Turning") icon: deep navy roots reaching downward from a horizon line (representing the roots of cultivation, the anchoring of the world to its foundations), with a gold star cluster kindling above (representing the cosmos, destiny, and the Turning to come). Colors: deep navy (#1A2A4A) for roots; gold (#C8972B central, #D4A843 mid, #E0BB6A far) for stars. Dimensions: 300×360 px PNG at 1.5× scale.

**Rule 10.4.3 — Icon Placement and Size.**
The phase icon PNG is inserted centered above every Prose title in the Chapter export. Display width: 0.55 inches. Space before icon: 12pt. Space after icon: 4pt. The icon is visually small — an ornament, not an illustration.

**Rule 10.4.4 — Icon Generation.**
The PNG is generated from SVG geometry using PIL/Pillow (Python Imaging Library). The generation script (`gen_phase_icon_png.py`) is a utility at the project root. The PNG is generated once and stored; it does not need to be regenerated for each export unless the icon design is updated.

### 10.5 — Area Ornament Divider

**Rule 10.5.1 — Asterism Ornament.**
Between consecutive Areas, the Chapter export inserts: (a) 24pt vertical space above, (b) a centered ⁂ asterism (U+2042) in EB Garamond 14pt, deep navy (#1A2A4A), (c) 24pt vertical space below. The asterism is the classic typographic area-break ornament used in literary fiction.

**Rule 10.5.2 — All Areas Including First.**
The page break + ornament appears before every Area, including the first Area of a Chapter. The Chapter title page (Chapter number + Chapter title) therefore stands alone as a single clean page, and the narrative proper begins on the following page with the ⁂ ornament introducing Area 1.

### 10.6 — Running Headers and Footers

**Rule 10.6.1 — Even Page Header.**
Even pages (left-hand pages): "STARWARD SAGA" centered, EB Garamond 9pt, color #5A5A5A (mid-grey).

**Rule 10.6.2 — Odd Page Header.**
Odd pages (right-hand pages): Chapter title in full caps (e.g., "TWIN COURTS AT DAWN") centered, EB Garamond 9pt, color #5A5A5A.

**Rule 10.6.3 — Page Numbers.**
Page numbers appear at the outer bottom edge of each page — left-aligned on even pages, right-aligned on odd pages. EB Garamond 9pt. Rendered as a PAGE field so they update dynamically with DOCX pagination.

**Rule 10.6.4 — First Page Exception.**
The first page of the document (Section/Part title page) has a blank header and blank footer — standard novel convention for opening pages.

**Rule 10.6.5 — Implementation.**
Running headers require both `different_first_page_header_footer = True` and `even_and_even_pages_header_footer` enabled at the document-level settings. python-docx exposes `even_page_header`, `even_page_footer`, `header` (odd), and `footer` (odd) on each section object.

### 10.7 — First Paragraph Treatment

**Rule 10.7.1 — Drop Cap.**
The first paragraph of the Chapter (immediately following the Chapter header block) and the first paragraph of each Area (immediately following the Area name header) receive a drop cap treatment: the first character is rendered in 28pt bold EB Garamond (approximately three text lines tall).

**Rule 10.7.2 — Small Caps.**
Immediately following the drop cap character, the next approximately four words are rendered in small caps (EB Garamond small caps). This is the classic "chapter opening" convention used by major fantasy publishers including Tor, Del Rey, and Orbit.

**Rule 10.7.3 — Remainder.**
The remainder of the opening paragraph after the small caps words continues in standard body style (EB Garamond 12pt, italic-aware for dialogue).

**Rule 10.7.4 — Italic Dialogue in Opening Paragraph.**
Even within an opening paragraph that begins with a drop cap and small caps, dialogue passages marked `*"..."*` in the source `.md` file are rendered as italic in the export.

### 10.8 — Table of Contents

**Rule 10.8.1 — ToC Deferred.**
The Chapter export does not include a Table of Contents. A ToC will be generated as a separate artifact via a future command (`[GENERATE TOC]` or similar) when the Phase or novel-level aggregate is compiled. No ToC placeholder is inserted in the Chapter export.

### 10.9 — Export Script

**Rule 10.9.1 — Canonical Implementation File.**
The canonical implementation of `[EXPORT CHAPTER]` is `export_chapter.py` at the Starward Saga project root. This script implements all rules in this Area and in Part 1 C-24. Any change to the Typography Specification (this Area) must be reflected in `export_chapter.py`.

**Rule 10.9.2 — Invocation.**
`export_chapter.py <chapter_number> [section_number] [part_number] [phase_number]`. Defaults: section=1, part=1, phase=1.

**Rule 10.9.3 — Aggregate Staleness.**
If a `chapter-NNN.docx` or `chapter-NNN.pdf` already exists when `[EXPORT CHAPTER]` is invoked, confirmation is required before overwriting (Part 1 C-24 Confirmation Required rule). On confirmation, both files are overwritten.

## Cross-References
| Related Skill | Relation | Source |
|---|---|---|
| ssc-cultivation-p03-cultivation-ladder-realm-hierarchy | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 10 governs [EXPORT CHAPTER] assembly/typography/export-script mechanics (consuming already-formatted per-Prose .md/.docx source) with no rule tied to cultivation-realm content |
| ssc-cultivation-p03-lifespan-mechanics | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 10 governs [EXPORT CHAPTER] assembly/typography/export-script mechanics with no rule tied to lifespan mechanics |
| ssc-cultivation-p03-power-density | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 10 governs [EXPORT CHAPTER] assembly/typography/export-script mechanics with no rule tied to power-density mechanics |
| ssc-cultivation-p03-realm-transition | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 10 governs [EXPORT CHAPTER] assembly/typography/export-script mechanics with no rule tied to realm-transition mechanics |
| ssc-cultivation-p03-cultivation-talent | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 10 governs [EXPORT CHAPTER] assembly/typography/export-script mechanics with no rule tied to cultivation-talent mechanics |
| ssc-cultivation-p03-growth-speed | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 10 governs [EXPORT CHAPTER] assembly/typography/export-script mechanics with no rule tied to growth-speed mechanics |
| ssc-cultivation-p03-power-comparison | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 10 governs [EXPORT CHAPTER] assembly/typography/export-script mechanics with no rule tied to power-comparison mechanics |
| ssc-cultivation-p03-damage-tolerance-recovery | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 10 governs [EXPORT CHAPTER] assembly/typography/export-script mechanics with no rule tied to damage-tolerance/recovery mechanics |
| ssc-cultivation-p03-affinity-cultivation | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 10 governs [EXPORT CHAPTER] assembly/typography/export-script mechanics with no rule tied to affinity-cultivation mechanics |
| ssc-cultivation-p03-heart-cultivation | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 10 governs [EXPORT CHAPTER] assembly/typography/export-script mechanics with no rule tied to heart-cultivation mechanics |

## Governing Authority
Subordinate to the shared Part 1 (audit law) + Part 34 (knowledge graph) grounding in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.

## Source Provenance
Part 2, Area 10 — "Chapter Export Format Specification (Canon v4.24)" · canon v4.33 · migrated 2026-08-03
