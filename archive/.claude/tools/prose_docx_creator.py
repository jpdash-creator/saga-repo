# ═══════════════════════════════════════════════════════════════════════════
# STARWARD SAGA — Novel-Grade Per-Prose DOCX Creator
# Part 2 Area 6 — Book Creation Law: Chapter Document (.docx)
# Rule 6.4.1 — Implementation Standard
# Rule 6.4.2 — Phase Icon Placement Law
# Rule 6.4.3 — This file IS the stored canonical script (prose_docx_creator.py)
# Rule 10.5.13 — Authorised Novel-Output Script #1
#
# Title Page Law (Part 1 Rule 10.5.14):
#   When is_first_prose_of_phase=True OR is_first_prose_of_section=True,
#   a full-page title page is prepended BEFORE the Chapter Header Block:
#     1. Phase image (phase-icon.png, centered, full-width)
#     2. Phase name heading
#     3. Section image (section-icon.png, centered)
#     4. Section name heading
#     5. Thematic epigraph (italic, from Part 30 canon — passed via epigraph param)
#   Page break after epigraph → Chapter Header Block begins on fresh page.
#
# Usage (Gate 2 standard call):
#   from prose_docx_creator import write_prose_to_per_prose_docx
#   write_prose_to_per_prose_docx(
#       phase=1, section=1, part=1, chapter=1, area=1, prose=1,
#       prose_text="The hum arrived before the light...",
#       prose_name="The Hum of the Sapphire Line",
#       phase_name="The Roots of Becoming",
#       section_name="The Citadels of Morning",
#       novel_part_name="The Twin Oaths",
#       chapter_name="Twin Courts at Dawn",
#       area_name="Paired Sovereigns",
#       pacing="Slow",
#       word_count=3124,
#       is_first_prose_of_chapter=True,
#       is_first_prose_of_area=True,
#       is_first_prose_of_phase=False,
#       is_first_prose_of_section=False,
#       epigraph="",
#       output_root="/path/to/repo/projects/novel-starward-saga"
#   )
# ═══════════════════════════════════════════════════════════════════════════

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os
import re
import io

# ─── CONSTANTS (Novel-Grade Typeset — Rule 6.2.2) ─────────────────────────
FONT_NAME        = "EB Garamond"          # body font (Times New Roman fallback)
BODY_SIZE        = 12                     # pt
H1_SIZE          = 18                     # pt — Series title
H2_SIZE          = 13                     # pt — Phase/Section
H3_SIZE          = 13                     # pt — Novel-Part
H4_SIZE          = 22                     # pt — Chapter title
H5_SIZE          = 11                     # pt — Area name (bold italic)
H6_SIZE          = 11                     # pt — Prose title (italic)
HEADING_SIZE     = 16                     # pt — Chapter Header Block text
ORNAMENT_SIZE    = 14                     # pt — ⁂ asterism ornament
DIVIDER_SIZE     = 11                     # pt — Area Divider
FIRST_INDENT     = 0.3                    # inches (suppressed after headers)
LINE_SPACING     = 1.15                   # 1.15× (trade paperback standard)
MARGIN_TOP       = 1.0                    # inches
MARGIN_BOTTOM    = 1.0                    # inches
MARGIN_LEFT      = 0.875                  # inches (6×9 interior)
MARGIN_RIGHT     = 0.875                  # inches
PAGE_WIDTH       = 6.0                    # inches (trade paperback trim)
PAGE_HEIGHT      = 9.0                    # inches
HEADER_COLOR     = RGBColor(0x5A, 0x5A, 0x5A)   # mid-grey #5A5A5A
ORNAMENT_COLOR   = RGBColor(0x1A, 0x2A, 0x4A)   # deep navy #1A2A4A
DROP_CAP_SIZE    = 28                     # pt — 3-line drop cap
HEADER_FONT_SIZE = 9                      # pt — running headers/footers
ORNAMENT         = "\u2042"              # U+2042 asterism ornament ⁂

# ─── PHASE ICON CONSTANTS (Rule 6.4.2) ────────────────────────────────────
PHASE_ICON_WIDTH_CHAPTER        = 1.0    # inches — Chapter Header Block icon
PHASE_ICON_WIDTH_PROSE          = 0.55   # inches — Prose Title Block icon
PHASE_ICON_SPACE_BEFORE_CHAPTER = 24     # pt — before chapter-level icon
PHASE_ICON_SPACE_AFTER_CHAPTER  = 12     # pt — between chapter icon and "STARWARD SAGA"
PHASE_ICON_SPACE_BEFORE_PROSE   = 12     # pt — before prose-level icon
PHASE_ICON_SPACE_AFTER_PROSE    = 4      # pt — between prose icon and Prose title

PROSE_TITLE_SIZE = 12   # pt Bold, center
PROSE_REF_SIZE   = 10   # pt Regular Italic, center


def get_phase_icon_path(phase_number: int, output_root: str) -> str:
    """
    Return the canonical path to the phase icon PNG for a given phase.
    Rule 6.3.1a / Rule 6.4.2: located at novel-starward-saga/phase-N/phase-icon.png
    Returns path regardless of existence — caller must check with os.path.exists().
    """
    return os.path.join(output_root, f"phase-{phase_number}", "phase-icon.png")


def get_section_icon_path(phase_number: int, section_number: int,
                          output_root: str) -> str:
    """
    Return the canonical path to the section icon PNG for a given section.
    Rule 10.5.14: located at novel-starward-saga/phase-N/section-N/section-icon.png
    Returns path regardless of existence — caller must check with os.path.exists().
    """
    return os.path.join(
        output_root,
        f"phase-{phase_number}",
        f"section-{section_number}",
        "section-icon.png"
    )


def get_prose_path(phase: int, section: int, part: int,
                   chapter: int, area: int, prose: int,
                   output_root: str) -> str:
    """Return the canonical path for a per-Prose .docx file."""
    return os.path.join(
        output_root,
        f"phase-{phase}", f"section-{section}", f"part-{part}",
        f"chapter-{chapter:03d}", f"area-{area}",
        f"prose-{prose:05d}.docx"
    )


# ─── FONT AVAILABILITY CHECK ──────────────────────────────────────────────
def _resolve_font(preferred: str = FONT_NAME, fallback: str = "Times New Roman") -> str:
    """
    Attempt to use EB Garamond; fall back to Times New Roman if unavailable.
    python-docx will substitute silently if the font is missing, but we log.
    """
    return preferred   # python-docx will use the system fallback automatically


# ─── PARAGRAPH HELPERS ────────────────────────────────────────────────────
def _add_paragraph(doc: Document, text: str,
                   size: int = BODY_SIZE,
                   bold: bool = False,
                   italic: bool = False,
                   align = WD_ALIGN_PARAGRAPH.LEFT,
                   first_indent: float = FIRST_INDENT,
                   space_before: int = 0,
                   space_after: int = 0,
                   line_spacing: float = LINE_SPACING,
                   font_name: str = FONT_NAME) -> object:
    """Add a formatted paragraph with canonical Starward Saga styles."""
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.name = font_name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    pf = p.paragraph_format
    pf.alignment = align
    pf.first_line_indent = Inches(first_indent)
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing = line_spacing
    return p


def _add_inline_formatted_paragraph(doc: Document,
                                     segments: list,
                                     first_indent: float = FIRST_INDENT,
                                     font_name: str = FONT_NAME) -> object:
    """
    Add a paragraph with mixed inline formatting (normal/italic/bold/bold-italic).
    segments: list of (text, bold, italic) tuples.
    """
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.first_line_indent = Inches(first_indent)
    pf.line_spacing = LINE_SPACING
    pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
    pf.space_before = Pt(0)
    pf.space_after = Pt(0)
    for (text, bold, italic) in segments:
        run = p.add_run(text)
        run.font.name = font_name
        run.font.size = Pt(BODY_SIZE)
        run.font.bold = bold
        run.font.italic = italic
    return p


def _insert_phase_icon(doc: Document, icon_path: str,
                        width_inches: float,
                        space_before_pt: int,
                        space_after_pt: int) -> bool:
    """
    Insert the phase icon as a centered paragraph image.
    Returns True if inserted, False if icon file not found (graceful fallback).
    Rule 6.4.2 — Phase Icon Placement Law.
    """
    if not os.path.exists(icon_path):
        return False
    icon_para = doc.add_paragraph()
    icon_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    icon_para.paragraph_format.space_before = Pt(space_before_pt)
    icon_para.paragraph_format.space_after = Pt(space_after_pt)
    icon_para.paragraph_format.first_line_indent = Inches(0)
    icon_para.add_run().add_picture(icon_path, width=Inches(width_inches))
    return True


# ─── DROP CAP HELPER ──────────────────────────────────────────────────────
def apply_drop_cap_small_caps(paragraph, body_text: str,
                               font_name: str = FONT_NAME) -> None:
    """
    Apply drop cap (first char, 28pt bold) + small caps (~4 words) to the
    opening paragraph of a Chapter or Area (Rules 6.2.2 / 10.7.1-10.7.3).
    """
    if not body_text:
        return
    first_char = body_text[0]
    rest = body_text[1:]
    words = rest.split()
    sc_count = min(4, len(words))
    sc_words = " ".join(words[:sc_count])
    remainder = " ".join(words[sc_count:]) if len(words) > sc_count else ""
    r_drop = paragraph.add_run(first_char)
    r_drop.font.name = font_name
    r_drop.font.size = Pt(DROP_CAP_SIZE)
    r_drop.font.bold = True
    if sc_words:
        r_sc = paragraph.add_run(" " + sc_words)
        r_sc.font.name = font_name
        r_sc.font.size = Pt(BODY_SIZE)
        r_sc.font.small_caps = True
    if remainder:
        r_rem = paragraph.add_run(" " + remainder)
        r_rem.font.name = font_name
        r_rem.font.size = Pt(BODY_SIZE)


# ─── PAGE BREAK HELPER ───────────────────────────────────────────────────
def _add_page_break(doc: Document) -> None:
    """Insert a hard page break paragraph."""
    para = doc.add_paragraph()
    run  = para.add_run()
    br   = OxmlElement("w:br")
    br.set(qn("w:type"), "page")
    run._r.append(br)
    para.paragraph_format.space_before = Pt(0)
    para.paragraph_format.space_after  = Pt(0)


# ─── PHASE / SECTION TITLE PAGE ──────────────────────────────────────────
def _write_title_page(doc: Document,
                      phase: int,
                      section: int,
                      phase_name: str,
                      section_name: str,
                      epigraph: str,
                      output_root: str) -> None:
    """
    Write the Phase/Section full-page title page (Rule 10.5.14).

    Called when is_first_prose_of_phase or is_first_prose_of_section is True.
    A hard page break is appended after the epigraph so the Chapter Header
    Block starts on a fresh page.

    Structure:
        [Phase image — centered, 4.5" wide]
        PHASE N — PHASE NAME  (bold, centered)
        [blank spacer]
        [Section image — centered, 3.0" wide]
        Section N — Section Name  (bold, centered)
        [blank spacer]
        [Epigraph — italic, centered, if non-empty]
        [PAGE BREAK]
    """
    phase_icon   = get_phase_icon_path(phase, output_root)
    section_icon = get_section_icon_path(phase, section, output_root)

    # ── Phase image ──────────────────────────────────────────────────────
    if os.path.exists(phase_icon):
        img_para = doc.add_paragraph()
        img_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        img_para.paragraph_format.space_before = Pt(48)
        img_para.paragraph_format.space_after  = Pt(18)
        img_para.paragraph_format.first_line_indent = Inches(0)
        img_para.add_run().add_picture(phase_icon, width=Inches(4.5))
    else:
        # Placeholder text if icon not yet generated
        _add_paragraph(doc, "[Phase image not yet generated — run C-36]",
                       size=9, italic=True,
                       align=WD_ALIGN_PARAGRAPH.CENTER,
                       first_indent=0, space_before=48, space_after=18)

    # ── Phase heading ────────────────────────────────────────────────────
    phase_label = f"PHASE {phase}"
    if phase_name:
        phase_label += f" — {phase_name.upper()}"
    _add_paragraph(doc, phase_label,
                   size=20, bold=True,
                   align=WD_ALIGN_PARAGRAPH.CENTER,
                   first_indent=0, space_before=0, space_after=36)

    # ── Section image ────────────────────────────────────────────────────
    if os.path.exists(section_icon):
        img_para2 = doc.add_paragraph()
        img_para2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        img_para2.paragraph_format.space_before = Pt(0)
        img_para2.paragraph_format.space_after  = Pt(18)
        img_para2.paragraph_format.first_line_indent = Inches(0)
        img_para2.add_run().add_picture(section_icon, width=Inches(3.0))
    else:
        _add_paragraph(doc, "[Section image not yet generated — run C-37]",
                       size=9, italic=True,
                       align=WD_ALIGN_PARAGRAPH.CENTER,
                       first_indent=0, space_before=0, space_after=18)

    # ── Section heading ──────────────────────────────────────────────────
    section_label = f"Section {section}"
    if section_name:
        section_label += f" — {section_name}"
    _add_paragraph(doc, section_label,
                   size=16, bold=True,
                   align=WD_ALIGN_PARAGRAPH.CENTER,
                   first_indent=0, space_before=0, space_after=36)

    # ── Epigraph ─────────────────────────────────────────────────────────
    if epigraph and epigraph.strip():
        _add_paragraph(doc, epigraph.strip(),
                       size=11, italic=True,
                       align=WD_ALIGN_PARAGRAPH.CENTER,
                       first_indent=0, space_before=0, space_after=0)

    # ── Hard page break → Chapter Header Block starts on fresh page ───────
    _add_page_break(doc)


# ─── CHAPTER HEADER BLOCK ─────────────────────────────────────────────────
def _write_chapter_header_block(doc: Document,
                                 phase: int,
                                 section: int,
                                 part: int,
                                 chapter: int,
                                 phase_name: str,
                                 section_name: str,
                                 novel_part_name: str,
                                 chapter_name: str,
                                 icon_path: str) -> None:
    """
    Write the Chapter Header Block into doc.
    Called only for the first prose of a chapter (prose-00001 of area-1).
    Structure (Rule 6.3.1 + Rule 6.3.1a):
        [Phase icon — 1.0" wide]  ← Rule 6.3.1a
        STARWARD SAGA
        PHASE N — [Phase Name]
        SECTION N — [Section Name]
        PART N — [Novel-Part Name]
        [blank]
        Chapter NNN — [Chapter Name]
        [blank spacer]
    """
    # Phase icon at top of Chapter Header Block (Rule 6.3.1a / 6.4.2)
    icon_inserted = _insert_phase_icon(
        doc, icon_path,
        width_inches=PHASE_ICON_WIDTH_CHAPTER,
        space_before_pt=PHASE_ICON_SPACE_BEFORE_CHAPTER,
        space_after_pt=PHASE_ICON_SPACE_AFTER_CHAPTER
    )
    top_space = 0 if icon_inserted else 48   # if no icon, add breathing space

    _add_paragraph(doc, "STARWARD SAGA",
                   size=HEADING_SIZE, bold=True,
                   align=WD_ALIGN_PARAGRAPH.CENTER,
                   first_indent=0, space_before=top_space, space_after=0)

    phase_label = f"PHASE {phase}" + (f" \u2014 {phase_name.upper()}" if phase_name else "")
    _add_paragraph(doc, phase_label,
                   size=HEADING_SIZE, bold=True,
                   align=WD_ALIGN_PARAGRAPH.CENTER,
                   first_indent=0, space_before=0, space_after=0)

    section_label = f"SECTION {section}" + (f" \u2014 {section_name.upper()}" if section_name else "")
    _add_paragraph(doc, section_label,
                   size=HEADING_SIZE, bold=True,
                   align=WD_ALIGN_PARAGRAPH.CENTER,
                   first_indent=0, space_before=0, space_after=0)

    part_label = f"PART {part}" + (f" \u2014 {novel_part_name}" if novel_part_name else "")
    _add_paragraph(doc, part_label,
                   size=HEADING_SIZE, bold=True,
                   align=WD_ALIGN_PARAGRAPH.CENTER,
                   first_indent=0, space_before=0, space_after=0)

    # Blank line before chapter title
    _add_paragraph(doc, "",
                   size=HEADING_SIZE, first_indent=0,
                   space_before=0, space_after=0)

    chapter_label = f"Chapter {chapter:03d}" + (f" \u2014 {chapter_name}" if chapter_name else "")
    _add_paragraph(doc, chapter_label,
                   size=HEADING_SIZE, bold=True,
                   align=WD_ALIGN_PARAGRAPH.CENTER,
                   first_indent=0, space_before=0, space_after=24)


# ─── AREA DIVIDER ─────────────────────────────────────────────────────────
def _write_area_divider(doc: Document, area: int, area_name: str) -> None:
    """
    Write the Area Divider into doc.
    Called for the first prose of each new Area (Rule 6.3.2).
    Format: — Area N: [Area Name] —
    """
    label = f"\u2014 Area {area}"
    if area_name:
        label += f": {area_name}"
    label += " \u2014"
    _add_paragraph(doc, label,
                   size=DIVIDER_SIZE, bold=True, italic=True,
                   align=WD_ALIGN_PARAGRAPH.CENTER,
                   first_indent=0, space_before=24, space_after=12)


# ─── PROSE TITLE BLOCK ────────────────────────────────────────────────────
def _write_prose_title_block(doc: Document,
                              prose: int,
                              prose_name: str,
                              reference_code: str,
                              icon_path: str) -> None:
    """
    Write the mandatory Prose Title Block (Rule 6.3.2a).
    Includes the phase icon immediately before the title.
    Structure:
        [Phase icon — 0.55" wide]  ← Rule 6.2.2 / 6.4.2
        Prose N — [Prose Name]
        [Reference Code]
    """
    if not prose_name:
        raise ValueError(
            "Prose Name is mandatory per Part 28 Area 18 Rule 18.3.1 — cannot be empty")

    # Blank spacer before the icon/title block
    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_before = Pt(0)
    spacer.paragraph_format.space_after = Pt(0)

    # Phase icon before Prose title (Rule 6.2.2 / 6.4.2)
    _insert_phase_icon(
        doc, icon_path,
        width_inches=PHASE_ICON_WIDTH_PROSE,
        space_before_pt=PHASE_ICON_SPACE_BEFORE_PROSE,
        space_after_pt=PHASE_ICON_SPACE_AFTER_PROSE
    )

    # "Prose N — [Prose Name]"
    title_text = f"Prose {prose} \u2014 {prose_name}"
    _add_paragraph(doc, title_text,
                   size=PROSE_TITLE_SIZE, bold=True,
                   align=WD_ALIGN_PARAGRAPH.CENTER,
                   first_indent=0, space_before=0, space_after=0)

    # Reference code
    _add_paragraph(doc, reference_code,
                   size=PROSE_REF_SIZE, bold=False, italic=True,
                   align=WD_ALIGN_PARAGRAPH.CENTER,
                   first_indent=0, space_before=0, space_after=12)


# ─── INLINE FORMATTING PARSER ─────────────────────────────────────────────
def _emit_italic_inner(inner: str, segments: list) -> None:
    """
    Emit segments for the body of a *...* span.
    Plain text       → (text, False, True)
    ***...*** spans  → (text, True,  True)   bold+italic: *** bold inside italic outer
    """
    i = 0
    n = len(inner)
    while i < n:
        if inner[i:i+3] == '***':
            end = inner.find('***', i + 3)
            if end != -1:
                segments.append((inner[i+3:end], True, True))
                i = end + 3
                continue
        # Accumulate plain italic text up to next *** or end
        j = i
        while j < n and inner[j:j+3] != '***':
            j += 1
        if j > i:
            segments.append((inner[i:j], False, True))
            i = j
        else:
            # Safety: consume one char to avoid infinite loop
            segments.append((inner[i], False, True))
            i += 1


def _parse_inline_formatting(text: str) -> list:
    """
    Parse inline formatting markers into (text, bold, italic) segment tuples.

    Uses a character-by-character parser to correctly handle ***X*** sub-spans
    nested inside *"..."* italic dialogue spans (yields bold+italic, not bold-only).

    Priority order:
        ***text*** → bold=True,  italic=True   (Named Move / cultivation level)
        **text**   → bold=True,  italic=False  (non-move bold emphasis)
        *"..."*    → bold=False, italic=True   (dialogue — may contain *** sub-spans)
        *text*     → bold=False, italic=True   (other italic)
        plain text → bold=False, italic=False
    """
    segments = []
    i = 0
    n = len(text)

    while i < n:
        # ── bold+italic: ***...*** ──────────────────────────────────────────
        if text[i:i+3] == '***':
            end = text.find('***', i + 3)
            if end != -1:
                segments.append((text[i+3:end], True, True))
                i = end + 3
                continue

        # ── bold only: **...** ──────────────────────────────────────────────
        if text[i:i+2] == '**':
            end = text.find('**', i + 2)
            if end != -1:
                segments.append((text[i+2:end], True, False))
                i = end + 2
                continue

        # ── italic: *...* (may contain ***...*** sub-spans) ─────────────────
        if text[i] == '*':
            # Scan forward for the matching closing *, skipping over
            # any ***...*** sub-spans encountered along the way.
            j = i + 1
            found_close = False
            while j < n:
                if text[j:j+3] == '***':
                    k = text.find('***', j + 3)
                    if k != -1:
                        j = k + 3   # jump past entire ***...*** sub-span
                    else:
                        j += 1
                elif text[j] == '*':
                    found_close = True
                    break
                else:
                    j += 1
            if found_close:
                inner = text[i+1:j]
                _emit_italic_inner(inner, segments)
                i = j + 1
                continue
            # No matching closing * — fall through to plain-char treatment

        # ── plain character(s) ───────────────────────────────────────────────
        j = i
        while j < n and text[j] != '*':
            j += 1
        if j > i:
            segments.append((text[i:j], False, False))
            i = j
        else:
            # Lone/unmatched * — emit as plain character
            segments.append((text[i], False, False))
            i += 1

    return segments


# ─── PROSE BODY APPEND ────────────────────────────────────────────────────
def _append_prose_body(doc: Document, prose_text: str,
                        is_first_in_area: bool = False,
                        font_name: str = FONT_NAME) -> None:
    """
    Append the prose body paragraphs to doc.

    prose_text formatting conventions:
        *"..."*      = italic dialogue (the canonical Part 29 form)
        **text**     = bold Named Move
        ***text***   = bold italic Named Move in dialogue
        blank line   = paragraph break
        ***SCENE BREAK*** = scene break ornament

    is_first_in_area: suppresses first-line indent on the opening paragraph
                      (standard publishing convention after section break).
    """
    paragraphs = prose_text.strip().split("\n\n")
    first_paragraph = True

    for para_text in paragraphs:
        para_text = para_text.strip()
        if not para_text:
            continue

        # Scene break marker
        if para_text in ("***SCENE BREAK***", "* * *", "***"):
            _add_paragraph(doc, "   \u2042",   # ⁂ asterism
                           size=ORNAMENT_SIZE,
                           align=WD_ALIGN_PARAGRAPH.CENTER,
                           first_indent=0, space_before=12, space_after=12)
            first_paragraph = False
            continue

        segments = _parse_inline_formatting(para_text)
        indent = 0 if (first_paragraph and is_first_in_area) else FIRST_INDENT
        _add_inline_formatted_paragraph(doc, segments,
                                         first_indent=indent,
                                         font_name=font_name)
        first_paragraph = False


# ─── PAGE SETUP ───────────────────────────────────────────────────────────
def _apply_page_setup(doc: Document) -> None:
    """Apply the canonical 6×9 trade paperback page setup (Rule 6.2.1)."""
    sec = doc.sections[0]
    sec.page_width    = Inches(PAGE_WIDTH)
    sec.page_height   = Inches(PAGE_HEIGHT)
    sec.top_margin    = Inches(MARGIN_TOP)
    sec.bottom_margin = Inches(MARGIN_BOTTOM)
    sec.left_margin   = Inches(MARGIN_LEFT)
    sec.right_margin  = Inches(MARGIN_RIGHT)


# ─── PRIMARY GATE 2 ENTRY POINT ──────────────────────────────────────────
def write_prose_to_per_prose_docx(
        phase: int,
        section: int,
        part: int,
        chapter: int,
        area: int,
        prose: int,
        prose_text: str,
        prose_name: str,
        phase_name: str = "",
        section_name: str = "",
        novel_part_name: str = "",
        chapter_name: str = "",
        area_name: str = "",
        pacing: str = "Medium",
        word_count: int = 0,
        is_first_prose_of_chapter: bool = False,
        is_first_prose_of_area: bool = False,
        is_first_prose_of_phase: bool = False,
        is_first_prose_of_section: bool = False,
        epigraph: str = "",
        output_root: str = "projects/novel-starward-saga",
        font_name: str = FONT_NAME) -> str:
    """
    PRIMARY GATE 2 WRITER — creates a single per-Prose .docx file.

    Called by [NEXT PROSE], [START STORY], and [REVISE PROSE] at Gate 2.

    Structural block order (Part 2 Rules 6.3.1, 6.3.2, 6.3.2a, 6.3.1a, 6.4.2
                           + Part 1 Rule 10.5.14 Title Page Law):
      0. Title Page (full-page) — ONLY if is_first_prose_of_phase or
                                        is_first_prose_of_section is True
         a. Phase image (4.5" wide, centered)
         b. Phase N — PHASE NAME heading
         c. Section image (3.0" wide, centered)
         d. Section N — Section Name heading
         e. Epigraph (italic, centered) — from Part 30 canon, if provided
         f. PAGE BREAK → Chapter Header Block on fresh page
      1. Chapter Header Block  — ONLY if is_first_prose_of_chapter is True
         a. Phase icon (1.0" wide)               ← Rule 6.3.1a / 6.4.2
         b. STARWARD SAGA header text
         c. Phase / Section / Part / Chapter labels
      2. Area Divider          — ONLY if is_first_prose_of_area is True
      3. Phase icon (0.55" wide)                 ← Rule 6.2.2 / 6.4.2
      4. Prose Title Block     — ALWAYS (Rule 6.3.2a)
      5. Prose body            — ALWAYS

    Returns the path to the written .docx file.
    Raises ValueError if prose_name is empty (Part 28 Area 18 Rule 18.3.1).
    """
    if not prose_name:
        raise ValueError(
            f"Prose Name is mandatory (Part 28 Area 18 Rule 18.3.1). "
            f"Received empty prose_name for prose {prose:05d}.")

    prose_path = get_prose_path(phase, section, part, chapter, area, prose, output_root)
    os.makedirs(os.path.dirname(prose_path), exist_ok=True)

    doc = Document()
    _apply_page_setup(doc)

    icon_path = get_phase_icon_path(phase, output_root)

    # ── 0. Title Page (Phase / Section opening) ──────────────────────────
    if is_first_prose_of_phase or is_first_prose_of_section:
        _write_title_page(
            doc, phase, section,
            phase_name, section_name,
            epigraph, output_root
        )

    # ── 1. Chapter Header Block ──────────────────────────────────────────
    if is_first_prose_of_chapter:
        _write_chapter_header_block(
            doc, phase, section, part, chapter,
            phase_name, section_name, novel_part_name, chapter_name,
            icon_path
        )

    # ── 2. Area Divider ──────────────────────────────────────────────────
    if is_first_prose_of_area:
        _write_area_divider(doc, area, area_name)

    # ── 3 + 4. Phase Icon + Prose Title Block (ALWAYS) ───────────────────
    reference_code = f"{phase}.{section}.{part}.{chapter:03d}.{area}.{prose:05d}"
    _write_prose_title_block(doc, prose, prose_name, reference_code, icon_path)

    # ── 5. Prose Body ────────────────────────────────────────────────────
    _append_prose_body(doc, prose_text,
                       is_first_in_area=is_first_prose_of_area,
                       font_name=font_name)

    # Save
    buf = io.BytesIO()
    doc.save(buf)
    buf.seek(0)
    with open(prose_path, 'wb') as f:
        f.write(buf.read())

    return prose_path


# ─── CONVENIENCE: WRITE FROM DICT ────────────────────────────────────────────
def write_prose_from_metadata(metadata: dict, prose_text: str,
                                output_root: str = "projects/novel-starward-saga") -> str:
    """
    Convenience wrapper: pass a metadata dict with all position fields.
    metadata keys: phase, section, part, chapter, area, prose,
                   prose_name, phase_name, section_name, novel_part_name,
                   chapter_name, area_name, pacing, word_count,
                   is_first_prose_of_chapter, is_first_prose_of_area,
                   is_first_prose_of_phase, is_first_prose_of_section, epigraph
    """
    return write_prose_to_per_prose_docx(
        phase=metadata['phase'],
        section=metadata['section'],
        part=metadata['part'],
        chapter=metadata['chapter'],
        area=metadata['area'],
        prose=metadata['prose'],
        prose_text=prose_text,
        prose_name=metadata.get('prose_name', ''),
        phase_name=metadata.get('phase_name', ''),
        section_name=metadata.get('section_name', ''),
        novel_part_name=metadata.get('novel_part_name', ''),
        chapter_name=metadata.get('chapter_name', ''),
        area_name=metadata.get('area_name', ''),
        pacing=metadata.get('pacing', 'Medium'),
        word_count=metadata.get('word_count', 0),
        is_first_prose_of_chapter=metadata.get('is_first_prose_of_chapter', False),
        is_first_prose_of_area=metadata.get('is_first_prose_of_area', False),
        is_first_prose_of_phase=metadata.get('is_first_prose_of_phase', False),
        is_first_prose_of_section=metadata.get('is_first_prose_of_section', False),
        epigraph=metadata.get('epigraph', ''),
        output_root=output_root
    )


# ─── SELF-TEST ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import sys
    print("Starward Saga DOCX Creator — Part 2 Rule 6.4.3")
    print(f"python-docx version: ", end="")
    try:
        import docx
        print(docx.__version__)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    print("Script is ready. Import write_prose_to_per_prose_docx for Gate 2 use.")
