# ═══════════════════════════════════════════════════════════════════════════
# STARWARD SAGA — Novel-Grade Per-Area DOCX Creator
# Part 2 Area 6 — Book Creation Law: Area Document (.docx)
# Rule 6.4.1 — Implementation Standard
# Rule 6.4.2 — Phase Icon Placement Law
# Rule 6.4.3 — This file IS the stored canonical script (area_docx_creator.py)
# Authorised Novel-Output Script #1 (guardrails/tools/guardrail-authorized-scripts-only.md)
#
# File layout: one Area is one file, projects/novel-starward-saga/phase-N/section-N/part-N/
#   chapter-NNN/area-NN.docx  (two-digit Area number, resets per Chapter; no Area subfolders).
#   The .docx is written as a coupled pair with the .md of the same Area at Gate 2.
#   The Chapter file is NOT made here: /chapter-builder (chapter_builder.py, script 6) writes
#   'Chapter NNN - Name.docx' into the Novel-Part folder from a condensed text. This script joins
#   those Chapter files into a Phase and the novel.
#
# Title Page (Part 2 Rule 6.3.1b):
#   When is_first_area_of_phase=True OR is_first_area_of_section=True,
#   a full-page title page is prepended BEFORE the Chapter Header Block:
#     1. Phase image (phase-icon.png, centered, full-width)
#     2. Phase name heading
#     3. Section image (section-icon.png, centered)
#     4. Section name heading
#     5. Epigraph lines (italic, centered; each value is optional, empty or `unset` means none).
#        Two values, both passed in by the calling command:
#          phase_epigraph   (--phase-epigraph, --phase-epigraph-file): the Phase epigraph line of Part 30.
#                           Printed FIRST, and only on the first Area of a Phase (is_first_area_of_phase=True);
#                           given on any other Area the script refuses and writes nothing.
#          section_epigraph (--section-epigraph, --section-epigraph-file; --epigraph and --epigraph-file
#                           and the epigraph parameter are aliases): the Epigraph line in the header block
#                           of that Section's Section Spec, Part 38 Rule 10.3.1. Printed SECOND when both
#                           are set, alone when it is the only one.
#        So the first Area of a Phase (it opens the Phase and Section 1) prints the Phase line and then
#        Section 1's own line as two paragraphs; the first Area of every other Section prints only that
#        Section's own line. See Part 2 Rule 6.3.1b. This script reads no spec and no skill and writes
#        no epigraph text.
#   Page break after the epigraph lines → Chapter Header Block begins on fresh page.
#   Both images are required. A missing Phase image or Section image raises FileNotFoundError and
#   nothing is written; the script never prints a placeholder line in its place.
#
# Opening paragraph and running heads:
#   The first paragraph of narration of every Area (the paragraph after the date line, see "Date line"
#   below) opens with a 28pt bold drop cap and about four small-caps words (Rules 10.7.1-10.7.3);
#   inline italic and bold-italic survive the split (Rule 10.7.4). Every file carries running
#   heads (even pages: STARWARD SAGA; odd pages: the Chapter title in caps), outer-edge page
#   numbers and a blank first-page header and footer (Rules 6.2.1, 10.6.1-10.6.5).
#
# Area Title Block (Rule 6.3.2a): every Area file carries it: the phase icon, the "Area N — [Area Name]"
#   title and the reference code (P.S.N.CCC.AA). It is the Area separator when the Area files are joined
#   into a Chapter file.
#
# Date line (Part 2 Rule 6.3.2b, Part 41 Area 5):
#   The Area text begins with its date line: the first body paragraph of the text, the whole paragraph
#   wrapped in single asterisks and beginning "Year ", a number and a comma, for example
#   *Year 1247, Ilovany, Orvil, Day 1* or a range such as *Year 1247, Sorevany, Nuvil, Day 27 to Mirovil, Day 29*.
#   _date_line_text() detects it strictly; a text whose first paragraph is anything else is written without one.
#   The date line is its own paragraph: centred, italic, DATE_LINE_SIZE (smaller than the body), no first-line
#   indent, a small space below it, and kept on the page with the paragraph after it. The drop cap, the small
#   caps and the no-indent opening go to the first narration paragraph after the date line, never to the date
#   line. Since the Chapter join copies paragraphs as they are, every Area of the Chapter file carries its
#   own date line. The script writes no date and checks no date: the calendar is Part 41's and the line is
#   typed in the Area text.
#
# Usage (Gate 2 standard call):
#   from area_docx_creator import write_area_to_per_area_docx
#   write_area_to_per_area_docx(
#       phase=1, section=1, part=1, chapter=1, area=1,
#       area_text="*Year 1247, ...*  First light crossed the basin fields...",
#       area_name="First Light Over the Basin",
#       phase_name="The Roots of Becoming",
#       section_name="Azure Sky and Gale",
#       novel_part_name="The Twin Oaths",
#       chapter_name="Twin Courts at Dawn",
#       pacing="Slow",
#       word_count=1800,
#       is_first_area_of_chapter=True,
#       is_first_area_of_phase=False,
#       is_first_area_of_section=False,
#       phase_epigraph="",     # the Part 30 Phase line, passed only on the first Area of a Phase
#       section_epigraph="",   # the Section Spec's Epigraph line
#       output_root="/path/to/repo/projects/novel-starward-saga"
#   )
#
#   output_root defaults to REPO_ROOT/projects/novel-starward-saga, computed from this script's
#   own location (REPO_ROOT is the folder that holds .claude/), so the novel is written to the
#   same place whatever folder the session runs from.
#
# Usage (command line; this is how /next-area calls the script at Gate 2):
#   python .claude/tools/area_docx_creator.py write --text-file AREA.txt \
#       --phase 1 --section 1 --part 1 --chapter 1 --area 1 \
#       --area-name "..." --phase-name "..." --section-name "..." --novel-part-name "..." \
#       --chapter-name "..." [--first-of-chapter] [--first-of-phase] [--first-of-section] \
#       [--phase-epigraph-file PHASE_EPIGRAPH.txt] [--section-epigraph-file SECTION_EPIGRAPH.txt] \
#       [--output-root DIR] [--overwrite]
#   (--phase-epigraph "text" and --section-epigraph "text" give a line inline. Give
#   --phase-epigraph-file only on the first Area of a Phase.)
#   python .claude/tools/area_docx_creator.py assemble --scope phase|novel [--phase N] [--overwrite]
#   python .claude/tools/area_docx_creator.py check --file PATH [--expect present|absent]
#   AREA.txt is a UTF-8 text file holding the Area text. With no arguments the script runs
#   its self-test. A writer refuses to replace an Area that is already on disk unless
#   --overwrite is given (only /revise-area gives it).
# ═══════════════════════════════════════════════════════════════════════════

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.opc.exceptions import PackageNotFoundError
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os
import re
import io
import argparse
import sys
import copy

# ─── OUTPUT ROOT (Part 2 Rule 5.2.1) ──────────────────────────────────────
def _default_output_root() -> str:
    """
    The novel output folder, computed from this script's own location so the files land in
    the same place whatever folder a session runs from (the method reset_story.py uses).
    This file lives at REPO_ROOT/.claude/tools/area_docx_creator.py, so two folders above the tools
    folder is REPO_ROOT and the output folder is REPO_ROOT/projects/novel-starward-saga.
    """
    tools_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(os.path.dirname(tools_dir))
    return os.path.join(repo_root, "projects", "novel-starward-saga")


DEFAULT_OUTPUT_ROOT = _default_output_root()

# ─── CONSTANTS (Novel-Grade Typeset — Rule 6.2.2) ─────────────────────────
FONT_NAME        = "EB Garamond"          # body font (Times New Roman fallback)
BODY_SIZE        = 12                     # pt
H1_SIZE          = 18                     # pt — Series title
H2_SIZE          = 13                     # pt — Phase/Section
H3_SIZE          = 13                     # pt — Novel-Part
H4_SIZE          = 22                     # pt — Chapter title
HEADING_SIZE     = 16                     # pt — Chapter Header Block text
ORNAMENT_SIZE    = 14                     # pt — ⁂ asterism ornament
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
TIME_SKIP_MARKERS = ("* * *", "***", "***SCENE BREAK***")   # paragraph forms of the Rule 6.3.5 time-skip mark; the writers type "* * *"

# ─── DATE LINE CONSTANTS (Part 2 Rule 6.3.2b) ─────────────
DATE_LINE_SIZE         = 10.5                   # pt — centred italic, smaller than the 12pt body
DATE_LINE_SPACE_BEFORE = 0                      # pt — none; the author chose "small space below" only
DATE_LINE_SPACE_AFTER  = 8                      # pt — the small space below the date line
# The whole first paragraph wrapped in single asterisks, "Year ", a number, a comma, then text; no asterisk
# or line break inside, so a bold, bold-italic or mixed-formatting paragraph is never taken for a date line.
_DATE_LINE_RE          = re.compile(r"^\*(Year \d+,[^*\n]+)\*$")

# ─── PHASE ICON CONSTANTS (Rule 6.4.2) ────────────────────────────────────
PHASE_ICON_WIDTH_CHAPTER        = 1.0    # inches — Chapter Header Block icon
PHASE_ICON_WIDTH_AREA           = 0.55   # inches — Area Title Block icon
PHASE_ICON_SPACE_BEFORE_CHAPTER = 24     # pt — before chapter-level icon
PHASE_ICON_SPACE_AFTER_CHAPTER  = 12     # pt — between chapter icon and "STARWARD SAGA"
PHASE_ICON_SPACE_BEFORE_AREA    = 12     # pt — before the Area-level icon
PHASE_ICON_SPACE_AFTER_AREA     = 4      # pt — between the Area icon and the Area title

AREA_TITLE_SIZE = 12   # pt Bold, center
AREA_REF_SIZE   = 10   # pt Regular Italic, center


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
    Part 2 Rule 6.3.1b: located at novel-starward-saga/phase-N/section-N/section-icon.png
    Returns path regardless of existence — caller must check with os.path.exists().
    """
    return os.path.join(
        output_root,
        f"phase-{phase_number}",
        f"section-{section_number}",
        "section-icon.png"
    )


def get_area_path(phase: int, section: int, part: int,
                  chapter: int, area: int,
                  output_root: str) -> str:
    """Return the canonical path for a per-Area .docx file: chapter-NNN/area-NN.docx."""
    return os.path.join(
        output_root,
        f"phase-{phase}", f"section-{section}", f"part-{part}",
        f"chapter-{chapter:03d}",
        f"area-{area:02d}.docx"
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


def _date_line_text(para_text: str):
    """
    The text of a date line (without its asterisks) when `para_text` is one, otherwise None.
    A date line is the whole paragraph wrapped in single asterisks and beginning "Year ", a number
    and a comma, e.g. *Year 1247, Ilovany, Orvil, Day 1* (Part 2 Rule 6.3.2b). The caller asks
    only about the first paragraph of the text; the check itself is strict, so anything else
    (dialogue in italics, a bold or bold-italic paragraph, a line with other formatting inside it) is None.
    """
    m = _DATE_LINE_RE.match(para_text.strip())
    return m.group(1).strip() if m else None


def _add_date_line_paragraph(doc: Document, text: str,
                             font_name: str = FONT_NAME) -> object:
    """
    Add the date line as its own paragraph: centred, italic, a
    smaller size than the body, no first-line indent, a small space below, and kept on the same
    page as the paragraph that follows it (a date line is never left alone at the foot of a page).
    """
    p = _add_paragraph(doc, text,
                       size=DATE_LINE_SIZE, italic=True,
                       align=WD_ALIGN_PARAGRAPH.CENTER,
                       first_indent=0,
                       space_before=DATE_LINE_SPACE_BEFORE,
                       space_after=DATE_LINE_SPACE_AFTER,
                       font_name=font_name)
    p.paragraph_format.keep_with_next = True
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
                      section_epigraph: str,
                      output_root: str,
                      phase_epigraph: str = "") -> None:
    """
    Write the Phase/Section full-page title page (Part 2 Rule 6.3.1b).

    Called when is_first_area_of_phase or is_first_area_of_section is True.
    A hard page break is appended after the epigraph lines so the Chapter Header
    Block starts on a fresh page.

    Epigraph lines: phase_epigraph, when set, prints first and section_epigraph second,
    each as its own centered italic paragraph; either alone prints alone; both empty prints
    none. The caller gives phase_epigraph only on the first Area of a Phase.

    Both images are required: a missing Phase image or Section image raises
    FileNotFoundError (there is no placeholder line).

    Structure:
        [Phase image — centered, 4.5" wide]
        PHASE N — PHASE NAME  (bold, centered)
        [blank spacer]
        [Section image — centered, 3.0" wide]
        Section N — Section Name  (bold, centered)
        [blank spacer]
        [Phase epigraph — italic, centered, if non-empty; first Area of a Phase only]
        [Section epigraph — italic, centered, if non-empty]
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
        # No placeholder line: a Title Page without its Phase image is never written
        # (Part 2 Rule 6.3.1b). The page is built in memory, so no file exists yet.
        raise FileNotFoundError(
            f"The Title Page needs the Phase image {phase_icon}, which does not exist. "
            f"Run /create-image-phase {phase} first. No file was written.")

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
        raise FileNotFoundError(
            f"The Title Page needs the Section image {section_icon}, which does not exist. "
            f"Run /create-image-section {phase} {section} first. No file was written.")

    # ── Section heading ──────────────────────────────────────────────────
    section_label = f"Section {section}"
    if section_name:
        section_label += f" — {section_name}"
    _add_paragraph(doc, section_label,
                   size=16, bold=True,
                   align=WD_ALIGN_PARAGRAPH.CENTER,
                   first_indent=0, space_before=0, space_after=36)

    # ── Epigraph lines: the Phase line first, then the Section's own line ─────
    lines = [t.strip() for t in (phase_epigraph, section_epigraph) if t and t.strip()]
    for n, line in enumerate(lines):
        _add_paragraph(doc, line,
                       size=11, italic=True,
                       align=WD_ALIGN_PARAGRAPH.CENTER,
                       first_indent=0, space_before=0,
                       space_after=12 if n < len(lines) - 1 else 0)

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
    Called only for the first Area of a Chapter (area-01).
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


# ─── AREA TITLE BLOCK ─────────────────────────────────────────────────────
def _write_area_title_block(doc: Document,
                            area: int,
                            area_name: str,
                            reference_code: str,
                            icon_path: str) -> None:
    """
    Write the mandatory Area Title Block (Rule 6.3.2a) on every Area file. It is the Area
    separator when Area files are joined into a Chapter file.
    Includes the phase icon immediately before the title.
    Structure:
        [Phase icon — 0.55" wide]  ← Rule 6.2.2 / 6.4.2
        Area N — [Area Name]
        [Reference Code]
    """
    if not area_name:
        raise ValueError(
            "Area Name is mandatory per Part 28 Area 18 Rule 18.3.1 — cannot be empty")

    # Blank spacer before the icon/title block
    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_before = Pt(0)
    spacer.paragraph_format.space_after = Pt(0)

    # Phase icon before the Area title (Rule 6.2.2 / 6.4.2)
    _insert_phase_icon(
        doc, icon_path,
        width_inches=PHASE_ICON_WIDTH_AREA,
        space_before_pt=PHASE_ICON_SPACE_BEFORE_AREA,
        space_after_pt=PHASE_ICON_SPACE_AFTER_AREA
    )

    # "Area N — [Area Name]"
    title_text = f"Area {area} — {area_name}"
    _add_paragraph(doc, title_text,
                   size=AREA_TITLE_SIZE, bold=True,
                   align=WD_ALIGN_PARAGRAPH.CENTER,
                   first_indent=0, space_before=0, space_after=0)

    # Reference code
    _add_paragraph(doc, reference_code,
                   size=AREA_REF_SIZE, bold=False, italic=True,
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


# ─── OPENING PARAGRAPH: DROP CAP + SMALL CAPS (Rules 6.2.2, 10.7.1-10.7.4) ─────────
def _coalesce_chars(chars: list) -> list:
    """Merge (char, bold, italic) triples back into (text, bold, italic) segments."""
    out = []
    for ch, b, i in chars:
        if out and out[-1][1] == b and out[-1][2] == i:
            out[-1][0] += ch
        else:
            out.append([ch, b, i])
    return [(text, b, i) for text, b, i in out]


def _add_drop_cap_paragraph(doc: Document, segments: list,
                             font_name: str = FONT_NAME) -> object:
    """
    Opening paragraph of a Chapter or Area: the first character (with any leading
    punctuation, such as an opening quotation mark) in 28pt bold, the rest of the first
    ~4 words in small caps, the remainder in the body style. Inline bold/italic
    (dialogue, Named Moves) is preserved through the split (Rule 10.7.4).
    segments: list of (text, bold, italic) tuples. No first-line indent (Rule 6.2.2).
    """
    chars = [(ch, b, i) for (text, b, i) in segments for ch in text]
    n = len(chars)
    first_alnum = next((idx for idx, c in enumerate(chars) if c[0].isalnum()), 0)
    drop_end = min(first_alnum + 1, n)
    idx, words = drop_end, 0
    while idx < n and words < 4:
        while idx < n and chars[idx][0].isspace():
            idx += 1
        if idx >= n:
            break
        while idx < n and not chars[idx][0].isspace():
            idx += 1
        words += 1
    small_end = idx
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.first_line_indent = Inches(0)
    pf.line_spacing = LINE_SPACING
    pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
    pf.space_before = Pt(0)
    pf.space_after = Pt(0)
    for (text, b, i) in _coalesce_chars(chars[:drop_end]):
        run = p.add_run(text)
        run.font.name = font_name
        run.font.size = Pt(DROP_CAP_SIZE)
        run.font.bold = True
        run.font.italic = i
    for (text, b, i) in _coalesce_chars(chars[drop_end:small_end]):
        run = p.add_run(text)
        run.font.name = font_name
        run.font.size = Pt(BODY_SIZE)
        run.font.bold = b
        run.font.italic = i
        run.font.small_caps = True
    for (text, b, i) in _coalesce_chars(chars[small_end:]):
        run = p.add_run(text)
        run.font.name = font_name
        run.font.size = Pt(BODY_SIZE)
        run.font.bold = b
        run.font.italic = i
    return p


# ─── AREA BODY APPEND ─────────────────────────────────────────────────────
def _append_area_body(doc: Document, area_text: str,
                      font_name: str = FONT_NAME) -> None:
    """
    Append the Area body paragraphs to doc.

    area_text formatting conventions:
        *Year 1247, ...* = the date line, the first paragraph of the text
        *"..."*      = italic dialogue (the canonical Part 29 form)
        **text**     = bold emphasis (never a Named Move)
        ***text***   = bold-italic Named Move or cultivation level, in narration and in dialogue
        blank line   = paragraph break
        * * *        = time-skip mark, rendered as the centered ⁂ ornament (Rule 6.3.5)

    Date line (Rule 6.3.2b): when the first paragraph of the text is a date line (_date_line_text), it
    is written as its own centred, smaller, italic paragraph with a small space below
    (_add_date_line_paragraph), and it is not the "first paragraph" below: the opening treatment goes
    to the first paragraph of narration after it. A text that does not begin with a date line is
    written without one.

    Every Area opens with the drop cap and small caps (Rules 10.7.1-10.7.3) and no first-line indent
    on its first narration paragraph (the standard publishing convention after a title block).
    """
    area_text = area_text.replace("\r\n", "\n").replace("\r", "\n")   # Windows and old Mac line endings
    paragraphs = area_text.strip().split("\n\n")
    first_paragraph = True    # True until the first paragraph of narration (or a time-skip mark) is met
    at_top = True             # True until the first paragraph of the text has been looked at

    for para_text in paragraphs:
        para_text = para_text.strip()
        if not para_text:
            continue

        # Date line (Rule 6.3.2b): only the first paragraph of the text can be one; first_paragraph stays
        # True, so the opening treatment falls on the narration paragraph that follows it.
        if at_top:
            at_top = False
            date_text = _date_line_text(para_text)
            if date_text is not None:
                _add_date_line_paragraph(doc, date_text, font_name=font_name)
                continue

        # Time-skip mark (Rule 6.3.5)
        if para_text in TIME_SKIP_MARKERS:
            _add_paragraph(doc, "   ⁂",   # ⁂ asterism
                           size=ORNAMENT_SIZE,
                           align=WD_ALIGN_PARAGRAPH.CENTER,
                           first_indent=0, space_before=12, space_after=12)
            first_paragraph = False
            continue

        segments = _parse_inline_formatting(para_text)
        if first_paragraph:
            _add_drop_cap_paragraph(doc, segments, font_name=font_name)
        else:
            _add_inline_formatted_paragraph(doc, segments,
                                             first_indent=FIRST_INDENT,
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



# ─── RUNNING HEADERS, FOOTERS, PAGE NUMBERS (Rules 6.2.1, 10.6.1-10.6.5) ─────────
def _style_hf_run(run, font_name: str = FONT_NAME) -> None:
    """Running header/footer text style: EB Garamond 9pt, mid-grey #5A5A5A."""
    run.font.name = font_name
    run.font.size = Pt(HEADER_FONT_SIZE)
    run.font.color.rgb = HEADER_COLOR


def _set_header_text(header, text: str, font_name: str = FONT_NAME) -> None:
    """Centered running-head text in one header part (empty text leaves it blank)."""
    header.is_linked_to_previous = False
    p = header.paragraphs[0]
    for r in list(p.runs):
        r._r.getparent().remove(r._r)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Inches(0)
    if text:
        _style_hf_run(p.add_run(text), font_name)


def _set_footer_page_number(footer, align, font_name: str = FONT_NAME) -> None:
    """Page number as a PAGE field, so it updates with the DOCX pagination (Rule 10.6.3)."""
    footer.is_linked_to_previous = False
    p = footer.paragraphs[0]
    for r in list(p.runs):
        r._r.getparent().remove(r._r)
    p.alignment = align
    p.paragraph_format.first_line_indent = Inches(0)
    run = p.add_run()
    _style_hf_run(run, font_name)
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    sep = OxmlElement("w:fldChar")
    sep.set(qn("w:fldCharType"), "separate")
    txt = OxmlElement("w:t")
    txt.text = "1"
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    for el in (begin, instr, sep, txt, end):
        run._r.append(el)


def _apply_section_running_heads(sec, chapter_title_caps: str,
                                  font_name: str = FONT_NAME) -> None:
    """
    Running heads and page numbers for one section (Rules 10.6.1-10.6.4): even pages carry
    STARWARD SAGA, odd pages the Chapter title in caps, page numbers sit at the outer edge, and
    the first page of the section has a blank header and footer.
    """
    sec.different_first_page_header_footer = True
    _set_header_text(sec.first_page_header, "", font_name)
    sec.first_page_footer.is_linked_to_previous = False
    _set_header_text(sec.even_page_header, "STARWARD SAGA", font_name)
    _set_footer_page_number(sec.even_page_footer, WD_ALIGN_PARAGRAPH.LEFT, font_name)
    _set_header_text(sec.header, chapter_title_caps, font_name)
    _set_footer_page_number(sec.footer, WD_ALIGN_PARAGRAPH.RIGHT, font_name)


def _apply_running_headers_footers(doc: Document, chapter_name: str,
                                    font_name: str = FONT_NAME) -> None:
    """
    Even (left-hand) pages: "STARWARD SAGA" centered; odd (right-hand) pages: the Chapter
    title in full caps centered (Rules 10.6.1, 10.6.2). Page numbers at the outer bottom
    edge, left on even pages and right on odd pages (Rule 10.6.3). The first page of the
    file has a blank header and footer (Rule 10.6.4). Rule 10.6.5: odd/even headers are a
    document-level setting and the blank first page is a section-level setting.
    """
    doc.settings.odd_and_even_pages_header_footer = True
    _apply_section_running_heads(doc.sections[0], (chapter_name or "").upper(), font_name)


# ─── PRIMARY GATE 2 ENTRY POINT ──────────────────────────────────────────
def write_area_to_per_area_docx(
        phase: int,
        section: int,
        part: int,
        chapter: int,
        area: int,
        area_text: str,
        area_name: str,
        phase_name: str = "",
        section_name: str = "",
        novel_part_name: str = "",
        chapter_name: str = "",
        pacing: str = "Medium",
        word_count: int = 0,
        is_first_area_of_chapter: bool = False,
        is_first_area_of_phase: bool = False,
        is_first_area_of_section: bool = False,
        epigraph: str = "",
        output_root: str = DEFAULT_OUTPUT_ROOT,
        font_name: str = FONT_NAME,
        overwrite: bool = False,
        phase_epigraph: str = "",
        section_epigraph: str = "") -> str:
    """
    PRIMARY GATE 2 WRITER — creates a single per-Area .docx file (chapter-NNN/area-NN.docx).

    Epigraph values: phase_epigraph is the Part 30 Phase line, given only on the first Area of a
    Phase; section_epigraph is the Epigraph line of the Section's Section Spec. `epigraph` is an
    alias of the Section line and is used when section_epigraph is empty. Both lines print on the
    Title Page, Phase line first.

    Called by /next-area and /revise-area at Gate 2 (/start-story and the redraft commands reach it through /next-area).

    Structural block order (Part 2 Rules 6.3.1, 6.3.2, 6.3.2a, 6.3.1a, 6.4.2
                           + Part 2 Rule 6.3.1b Title Page):
      0. Title Page (full-page) — ONLY if is_first_area_of_phase or
                                        is_first_area_of_section is True
         a. Phase image (4.5" wide, centered)
         b. Phase N — PHASE NAME heading
         c. Section image (3.0" wide, centered)
         d. Section N — Section Name heading
         e. Phase epigraph (italic, centered) — the Part 30 Phase epigraph line, if set; the first Area of a Phase only
         f. Section epigraph (italic, centered) — the Section Spec's Epigraph line, if set (Part 2 Rule 6.3.1b;
            Part 38 Rule 10.3.1; the first Area of a Phase prints both e and f, every other Section's first
            Area prints f alone)
         g. PAGE BREAK → Chapter Header Block on fresh page
      1. Chapter Header Block  — ONLY if is_first_area_of_chapter is True
         a. Phase icon (1.0" wide)               ← Rule 6.3.1a / 6.4.2
         b. STARWARD SAGA header text
         c. Phase / Section / Part / Chapter labels
      2. Area Title Block      — ALWAYS (Rule 6.3.2a)
         a. Phase icon (0.55" wide)              ← Rule 6.2.2 / 6.4.2
         b. Area N — [Area Name]
         c. Reference code P.S.N.CCC.AA
      3. Area body             — ALWAYS
         a. Date line          — when the text begins with one (Rule 6.3.2b): its own centred, smaller,
                                 italic paragraph with a small space below
         b. Narration          — the first narration paragraph (the one after the date line, if there is
                                 one) takes the drop cap and small caps

    Returns the path to the written .docx file.
    Raises ValueError if area_name is empty (Part 28 Area 18 Rule 18.3.1).
    Raises FileNotFoundError, before any file is written, if a Title Page is due and its Phase image or
    Section image does not exist (Part 2 Rule 6.3.1b).
    Raises ValueError, before any file is written, if phase_epigraph is given on an Area that is not
    the first of its Phase (the Phase line prints only on the Title Page that opens a Phase).
    Raises FileExistsError if the file already exists and overwrite is False; only /revise-area
    passes overwrite=True, so a wrong Area number or a repeated call cannot replace a
    written Area.
    """
    if not area_name:
        raise ValueError(
            f"Area Name is mandatory on every Area (Part 28 Area 18 Rule 18.3.1). "
            f"Received empty area_name for area {area:02d}.")
    if phase_epigraph.strip() and not is_first_area_of_phase:
        raise ValueError(
            "A Phase epigraph line is printed only on the first Area of a Phase (Part 2 Rule 6.3.1b). "
            f"Received phase_epigraph for area {area:02d}, which is not the first of its Phase.")
    section_epigraph = section_epigraph or epigraph

    area_path = get_area_path(phase, section, part, chapter, area, output_root)
    if os.path.exists(area_path) and not overwrite:
        raise FileExistsError(
            f"{area_path} already exists. A written Area is replaced only by /revise-area, "
            f"which passes overwrite=True (--overwrite on the command line).")
    os.makedirs(os.path.dirname(area_path), exist_ok=True)

    doc = Document()
    _apply_page_setup(doc)
    _apply_running_headers_footers(doc, chapter_name, font_name)

    icon_path = get_phase_icon_path(phase, output_root)

    # ── 0. Title Page (Phase / Section opening) ──────────────────────────
    if is_first_area_of_phase or is_first_area_of_section:
        _write_title_page(
            doc, phase, section,
            phase_name, section_name,
            section_epigraph, output_root,
            phase_epigraph=phase_epigraph
        )

    # ── 1. Chapter Header Block ──────────────────────────────────────────
    if is_first_area_of_chapter:
        _write_chapter_header_block(
            doc, phase, section, part, chapter,
            phase_name, section_name, novel_part_name, chapter_name,
            icon_path
        )

    # ── 2. Area Title Block (every Area) ─────────────────────────────────
    reference_code = f"{phase}.{section}.{part}.{chapter:03d}.{area:02d}"
    _write_area_title_block(doc, area, area_name, reference_code, icon_path)

    # ── 3. Area Body ─────────────────────────────────────────────────────
    _append_area_body(doc, area_text, font_name=font_name)

    # Save
    buf = io.BytesIO()
    doc.save(buf)
    buf.seek(0)
    with open(area_path, 'wb') as f:
        f.write(buf.read())

    return area_path


# ─── CONVENIENCE: WRITE FROM DICT ────────────────────────────────────────────
def write_area_from_metadata(metadata: dict, area_text: str,
                             output_root: str = DEFAULT_OUTPUT_ROOT,
                             overwrite: bool = False) -> str:
    """
    Convenience wrapper: pass a metadata dict with all position fields.
    metadata keys: phase, section, part, chapter, area,
                   area_name, phase_name, section_name, novel_part_name,
                   chapter_name, pacing, word_count,
                   is_first_area_of_chapter,
                   is_first_area_of_phase, is_first_area_of_section,
                   phase_epigraph, section_epigraph (epigraph is an alias of section_epigraph)
    """
    return write_area_to_per_area_docx(
        phase=metadata['phase'],
        section=metadata['section'],
        part=metadata['part'],
        chapter=metadata['chapter'],
        area=metadata['area'],
        area_text=area_text,
        area_name=metadata.get('area_name', ''),
        phase_name=metadata.get('phase_name', ''),
        section_name=metadata.get('section_name', ''),
        novel_part_name=metadata.get('novel_part_name', ''),
        chapter_name=metadata.get('chapter_name', ''),
        pacing=metadata.get('pacing', 'Medium'),
        word_count=metadata.get('word_count', 0),
        is_first_area_of_chapter=metadata.get('is_first_area_of_chapter', False),
        is_first_area_of_phase=metadata.get('is_first_area_of_phase', False),
        is_first_area_of_section=metadata.get('is_first_area_of_section', False),
        epigraph=metadata.get('epigraph', ''),
        phase_epigraph=metadata.get('phase_epigraph', ''),
        section_epigraph=metadata.get('section_epigraph', ''),
        output_root=output_root,
        overwrite=overwrite
    )


# ─── AREA TITLE BLOCK READ-BACK (Rules 6.3.2a, 10.9.1) ───────────────────────
_AREA_TITLE_RE     = re.compile(r"^Area \d+ — \S")
_REFERENCE_CODE_RE = re.compile(r"^\d+\.\d+\.\d+\.\d{3}\.\d{2}$")
_AREA_PATH_RE      = re.compile(
    r"phase-(\d+)[\\/]section-(\d+)[\\/]part-(\d+)[\\/]chapter-(\d{3})[\\/]"
    r"area-(\d{2})\.docx$")


def reference_code_from_path(path: str):
    """
    The Reference Code (P.S.N.CCC.AA) that a per-Area .docx path stands for,
    or None when the path is not a per-Area path.
    """
    m = _AREA_PATH_RE.search(os.path.abspath(path))
    if not m:
        return None
    phase, section, part, chapter, area = m.groups()
    return f"{int(phase)}.{int(section)}.{int(part)}.{chapter}.{area}"


def _find_title_blocks(paragraphs) -> list:
    """
    Positions of every Area Title Block in a list of paragraphs: an "Area N — Name" line
    followed directly by a reference-code line (Rule 6.3.2a).
    """
    found = []
    for i in range(len(paragraphs) - 1):
        if (_AREA_TITLE_RE.match(paragraphs[i].text.strip())
                and _REFERENCE_CODE_RE.match(paragraphs[i + 1].text.strip())):
            found.append(i)
    return found


def read_title_block(path: str):
    """
    Read a written per-Area .docx back and return its first Area Title Block as
    {"title", "reference", "icon"}, or None when the file has none. "icon" is True when the
    paragraph just before the title holds the phase icon.
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(f"{path} does not exist")
    paragraphs = Document(path).paragraphs
    found = _find_title_blocks(paragraphs)
    if not found:
        return None
    i = found[0]
    icon = i > 0 and next(paragraphs[i - 1]._p.iter(qn("w:drawing")), None) is not None
    return {"title": paragraphs[i].text.strip(),
            "reference": paragraphs[i + 1].text.strip(),
            "icon": icon}


def check_title_block(path: str, expect: str = ""):
    """
    Post-Write Audit read-back of one written per-Area .docx (Rule 10.9.1).
    expect is "present" (every Area file should carry its Area Title Block), "absent" or "" (report only).
    Also compares the Reference Code inside the file with the position of the path it was
    written to. Returns (ok, lines); lines are plain report lines for the audit.
    """
    block = read_title_block(path)
    from_path = reference_code_from_path(path)
    lines = [f"file: {os.path.abspath(path)}",
             "position from path: " + (from_path or "not a per-Area path"),
             "Area Title Block: " + ("present" if block else "absent")]
    ok = True
    if block:
        lines.append("title in file: " + block["title"])
        lines.append("reference code in file: " + block["reference"])
        if from_path and block["reference"] != from_path:
            ok = False
            lines.append(f"MISMATCH: the file carries {block['reference']} but sits at {from_path}")
    if expect in ("present", "absent") and (block is not None) != (expect == "present"):
        ok = False
        lines.append(f"UNEXPECTED: the Area Title Block should be {expect} in this file")
    lines.append("result: " + ("OK" if ok else "FAIL"))
    return ok, lines


# ─── JOINING .docx FILES (Rule 10.9.1) ───────────────────────────────────────
def _section_chunks(doc) -> list:
    """
    Split a document's body into its sections. Returns (elements, head_text) pairs, one per
    section, in order; head_text is the section's odd-page running head. The section-break
    properties stay behind: the joined file builds its own.
    """
    chunks, current = [], []
    for el in list(doc.element.body):
        if el.tag == qn("w:sectPr"):
            continue
        current.append(el)
        ppr = el.find(qn("w:pPr")) if el.tag == qn("w:p") else None
        if ppr is not None and ppr.find(qn("w:sectPr")) is not None:
            chunks.append(current)
            current = []
    chunks.append(current)
    heads = [(s.header.paragraphs[0].text if s.header.paragraphs else "") for s in doc.sections]
    return [(elements, heads[min(i, len(heads) - 1)]) for i, elements in enumerate(chunks)]


def _is_blank_paragraph(p) -> bool:
    """True for a paragraph with no text, no picture and no break."""
    has_object = next(p.iter(qn("w:drawing"), qn("w:br")), None) is not None
    return not has_object and not "".join(p.itertext()).strip()


def _append_elements(out, src, elements) -> None:
    """Copy body elements of `src` to the end of `out`, re-linking pictures into `out`."""
    sentinel = out.element.body.find(qn("w:sectPr"))
    for el in elements:
        new = copy.deepcopy(el)
        if new.tag == qn("w:p"):
            ppr = new.find(qn("w:pPr"))
            sect = ppr.find(qn("w:sectPr")) if ppr is not None else None
            if sect is not None:
                ppr.remove(sect)
                if _is_blank_paragraph(new):
                    continue          # the source's own section-break paragraph
        for blip in new.iter(qn("a:blip")):
            rid = blip.get(qn("r:embed"))
            if rid:
                blob = src.part.related_parts[rid].blob
                new_rid, _image = out.part.get_or_add_image(io.BytesIO(blob))
                blip.set(qn("r:embed"), new_rid)
        sentinel.addprevious(new)


# ─── CONTENTS PAGE OF A COMPILED PHASE OR NOVEL (Rule 10.8.1) ─────────────────
_CONTENTS_BOOKMARK = "ssc-contents"
_CONTENTS_LINE_RES = (
    ("phase",   re.compile(r"^PHASE \d+( — .+)?$")),
    ("section", re.compile(r"^SECTION \d+( — .+)?$")),
    ("part",    re.compile(r"^PART \d+( — .+)?$")),
    ("chapter", re.compile(r"^Chapter \d{3}( — .+)?$")),
)
_AREA_LINE_RE = re.compile(r"^Area (\d+) — (.+)$")


def _contents_entries(doc) -> list:
    """
    (kind, text) for every Phase, Section, Novel-Part, Chapter and Area line of `doc`, in reading
    order. The lines come from the Chapter Header Blocks and the Area Title Blocks the writer put into
    the files; a Phase, Section or Novel-Part heading is listed once, where it begins.
    """
    entries, last = [], {}
    for p in doc.paragraphs:
        text = p.text.strip()
        for kind, rx in _CONTENTS_LINE_RES:
            if rx.match(text):
                if kind == "chapter":
                    entries.append((kind, text))
                elif last.get(kind) != text:
                    entries.append((kind, text))
                    last[kind] = text
                    if kind == "phase":
                        last.pop("section", None)
                        last.pop("part", None)
                    elif kind == "section":
                        last.pop("part", None)
                break
        else:
            m = _AREA_LINE_RE.match(text)
            if m:
                entries.append(("area", "Area " + m.group(1) + ": " + m.group(2)))
    return entries


def _first_page_break_paragraph(doc):
    """The first paragraph of `doc` that holds a hard page break (the end of its first title page), or None."""
    for el in doc.element.body:
        if el.tag == qn("w:p") and any(b.get(qn("w:type")) == "page" for b in el.iter(qn("w:br"))):
            return el
    return None


def _add_contents_page(out, entries: list, font_name: str = FONT_NAME) -> None:
    """
    Put a contents page into `out`, after its first title page (at its start when it has none): the
    Chapter lines (number and title) with the Area names beneath each, grouped under their Section
    and Novel-Part (Rule 10.8.1). The page carries a bookmark so that a later join can replace it.
    """
    if not any(kind == "chapter" for kind, _text in entries):
        return
    anchor = _first_page_break_paragraph(out)
    show_phase = len({text for kind, text in entries if kind == "phase"}) > 1
    made = []

    def add(text, size, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.LEFT,
            indent=0.0, before=0, after=2):
        para = out.add_paragraph()
        pf = para.paragraph_format
        pf.alignment = align
        pf.first_line_indent = Inches(0)
        pf.left_indent = Inches(indent)
        pf.space_before = Pt(before)
        pf.space_after = Pt(after)
        pf.line_spacing = LINE_SPACING
        run = para.add_run(text)
        run.font.name = font_name
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.italic = italic
        made.append(para._p)
        return para

    heading = add("Contents", HEADING_SIZE, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER,
                  before=24, after=18)
    for kind, text in entries:
        if kind == "phase":
            if show_phase:
                add(text, 13, bold=True, before=14)
        elif kind == "section":
            add(text, 12, bold=True, before=12)
        elif kind == "part":
            add(text, 11, italic=True, before=6, indent=0.2)
        elif kind == "chapter":
            add(text, 11, before=4, indent=0.4)
        else:
            add(text, 10, italic=True, indent=0.7)
    _add_page_break(out)
    closing = out.paragraphs[-1]._p
    made.append(closing)
    start = OxmlElement("w:bookmarkStart")
    start.set(qn("w:id"), "1")
    start.set(qn("w:name"), _CONTENTS_BOOKMARK)
    ppr = heading._p.find(qn("w:pPr"))
    heading._p.insert(list(heading._p).index(ppr) + 1 if ppr is not None else 0, start)
    end = OxmlElement("w:bookmarkEnd")
    end.set(qn("w:id"), "1")
    closing.append(end)
    body = out.element.body
    for el in made:
        body.remove(el)
    if anchor is None:
        for i, el in enumerate(made):
            body.insert(i, el)
    else:
        for el in made:
            anchor.addnext(el)
            anchor = el


def _strip_contents_page(elements: list) -> list:
    """Drop the contents page (the elements from its bookmark start to its bookmark end) from a list of body elements."""
    start = next((i for i, el in enumerate(elements)
                  if any(b.get(qn("w:name")) == _CONTENTS_BOOKMARK for b in el.iter(qn("w:bookmarkStart")))),
                 None)
    if start is None:
        return elements
    end = next((i for i in range(start, len(elements))
                if next(elements[i].iter(qn("w:bookmarkEnd")), None) is not None), None)
    return elements if end is None else elements[:start] + elements[end + 1:]


def _join_documents(paths: list, one_section: bool, font_name: str = FONT_NAME,
                    contents: bool = False, strip_contents: bool = False):
    """
    Build one new Document from the .docx files in `paths`, in the order given.
    one_section=True : one run of pages under the first file's running head (the per-Area
                       files of one Chapter).
    one_section=False: every section of every file starts a new page and keeps its own running
                       head (the Chapter files of a Phase, the Phase files of the novel).
    contents=True      : put a contents page after the first title page (Rule 10.8.1), built from
                         the Chapter Header Blocks and Area Title Blocks of everything joined.
    strip_contents=True: leave out the contents page of each file first (Phase files joined into
                         the novel, whose one contents page replaces theirs).
    Nothing else is reformatted: paragraphs and pictures are copied as they are.
    """
    out = Document()
    _apply_page_setup(out)
    out.settings.odd_and_even_pages_header_footer = True
    first = True
    for path in paths:
        src = Document(path)
        for elements, head in _section_chunks(src):
            if strip_contents:
                elements = _strip_contents_page(elements)
            if first:
                _apply_section_running_heads(out.sections[0], head, font_name)
            elif not one_section:
                out.add_section(WD_SECTION.NEW_PAGE)
                _apply_section_running_heads(out.sections[-1], head, font_name)
            _append_elements(out, src, elements)
            first = False
    if contents:
        _add_contents_page(out, _contents_entries(out), font_name)
    for n, el in enumerate(out.element.body.iter(qn("wp:docPr")), start=1):
        el.set("id", str(n))          # copied pictures would otherwise repeat their ids
    return out


def _save_joined(doc, out_path: str) -> None:
    """Write the joined document whole or not at all."""
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    tmp = out_path + ".part"
    doc.save(tmp)
    os.replace(tmp, out_path)


def _sorted_numbered(folder: str, pattern: str) -> list:
    """(number, path) for the entries of `folder` whose names match `pattern`, sorted by the
    number as an integer (area-10 follows area-9), never as text."""
    rx = re.compile(pattern)
    found = []
    if os.path.isdir(folder):
        for name in os.listdir(folder):
            m = rx.match(name)
            if m:
                found.append((int(m.group(1)), os.path.join(folder, name)))
    return sorted(found)


def get_chapter_dir(phase: int, section: int, part: int, chapter: int,
                    output_root: str) -> str:
    """Return the Chapter folder: phase-N/section-N/part-N/chapter-NNN."""
    return os.path.join(output_root, f"phase-{phase}", f"section-{section}",
                        f"part-{part}", f"chapter-{chapter:03d}")


def _chapter_area_files(chapter_dir: str) -> list:
    """(area, path) of every per-Area .docx of a Chapter (chapter-NNN/area-NN.docx), in reading order."""
    return [(area, path) for area, path in _sorted_numbered(chapter_dir, r"^area-(\d{2})\.docx$")]


_CHAPTER_FILE_RE = r"^Chapter (\d{3})( - .+)?\.docx$"


def _part_chapter_files(part_dir: str) -> list:
    """(chapter number, path) of every Chapter file ('Chapter NNN - Name.docx', made by /chapter-builder)
    in a Novel-Part folder, in Chapter order (numbers sorted as integers)."""
    return _sorted_numbered(part_dir, _CHAPTER_FILE_RE)


def _phase_chapters(phase_dir: str) -> list:
    """(chapter number, Chapter file, per-Area files) for every Chapter of a Phase that has Areas or a Chapter
    file, in Section, Novel-Part, Chapter order (numbers sorted as integers). The Chapter file is the one
    /chapter-builder wrote into the Novel-Part folder, or None when it has not been built."""
    chapters = []
    for _s, s_dir in _sorted_numbered(phase_dir, r"^section-(\d+)$"):
        for _p, p_dir in _sorted_numbered(s_dir, r"^part-(\d+)$"):
            files = dict(_part_chapter_files(p_dir))
            numbers = set(files) | {n for n, _d in _sorted_numbered(p_dir, r"^chapter-(\d{3})$")
                                    if _chapter_area_files(os.path.join(p_dir, f"chapter-{n:03d}"))}
            for c_no in sorted(numbers):
                areas = _chapter_area_files(os.path.join(p_dir, f"chapter-{c_no:03d}"))
                chapters.append((c_no, files.get(c_no), areas))
    return chapters


def _newest_change(areas: list) -> float:
    """Latest change among a Chapter's Area files (0 when it has none)."""
    return max((os.path.getmtime(f) for _a, f in areas), default=0.0)


def _chapter_file_problems(chapters: list) -> tuple:
    """(Chapter files in order, problems): a Chapter file that is missing, or older than the latest change
    to its Chapter's Area files, is stale (Rule 5.3.5)."""
    sources, problems = [], []
    for c_no, chapter_file, areas in chapters:
        if chapter_file is None:
            problems.append(f"Chapter {c_no:03d} has no Chapter file; run /chapter-builder for it")
        elif os.path.getmtime(chapter_file) < _newest_change(areas):
            problems.append(f"{chapter_file} is older than a change to its Chapter's Areas; "
                            f"run /chapter-builder again for it")
        else:
            sources.append(chapter_file)
    return sources, problems


def assemble_phase_docx(phase: int, output_root: str = DEFAULT_OUTPUT_ROOT,
                        overwrite: bool = False) -> str:
    """
    Join the Chapter files ('Chapter NNN - Name.docx', made by /chapter-builder in each Novel-Part folder)
    of one Phase into phase-N/phase-N-complete.docx, in Section, Novel-Part, Chapter order. Every Chapter
    must already have an up-to-date Chapter file; a missing or stale one stops the join and is named
    (Rule 5.3.5). Nothing is condensed here: the join copies the Chapter files as they are. The Phase title
    page already opens the Phase's first Chapter file; the contents page (Rule 10.8.1) is put after it, built
    from the Chapter headings of the Chapters joined, and nothing else comes before the first Chapter. Each
    Chapter starts a new page under its own running head. Raises FileExistsError if the file exists and
    overwrite is False. Returns the path of the joined file.
    """
    phase_dir = os.path.join(output_root, f"phase-{phase}")
    chapters = _phase_chapters(phase_dir)
    if not chapters:
        raise FileNotFoundError(f"no Chapters found under {phase_dir}")
    out_path = os.path.join(phase_dir, f"phase-{phase}-complete.docx")
    if os.path.exists(out_path) and not overwrite:
        raise FileExistsError(
            f"{out_path} already exists; it is replaced only after the author confirms "
            f"(overwrite=True)")
    sources, problems = _chapter_file_problems(chapters)
    if problems:
        raise ValueError("the Phase was not joined; fix these first:\n  " + "\n  ".join(problems))
    _save_joined(_join_documents(sources, one_section=False, contents=True), out_path)
    return out_path


def assemble_novel_docx(output_root: str = DEFAULT_OUTPUT_ROOT,
                        overwrite: bool = False) -> str:
    """
    Join the Phase files (phase-N-complete.docx, made by assemble_phase_docx) of every Phase
    into starward-saga-complete.docx at the novel output folder, in Phase order. A Phase file
    that is missing, or older than a Chapter file or a change to the Areas of its Phase, stops the join and
    is named (Rule 5.3.5). One contents page (Rule 10.8.1) covering every Phase follows the first Phase
    title page and replaces the contents page of each Phase file. Raises FileExistsError if the file
    exists and overwrite is False. Returns the path of the joined file.
    """
    out_path = os.path.join(output_root, "starward-saga-complete.docx")
    if os.path.exists(out_path) and not overwrite:
        raise FileExistsError(
            f"{out_path} already exists; it is replaced only after the author confirms "
            f"(overwrite=True)")
    sources, problems = [], []
    for ph_no, ph_dir in _sorted_numbered(output_root, r"^phase-(\d+)$"):
        chapters = _phase_chapters(ph_dir)
        if not chapters:
            continue
        agg = os.path.join(ph_dir, f"phase-{ph_no}-complete.docx")
        newest = max(max(_newest_change(areas), os.path.getmtime(f) if f else 0.0)
                     for _c, f, areas in chapters)
        if not os.path.isfile(agg):
            problems.append(f"{agg} is missing; run /compile-phase for Phase {ph_no}")
        elif os.path.getmtime(agg) < newest:
            problems.append(f"{agg} is older than its Chapter files or Areas; "
                            f"run /compile-phase again for Phase {ph_no}")
        else:
            sources.append(agg)
    if not sources and not problems:
        raise FileNotFoundError(f"no Phases with Chapters found under {output_root}")
    if problems:
        raise ValueError("the novel was not joined; fix these first:\n  " + "\n  ".join(problems))
    _save_joined(_join_documents(sources, one_section=False, contents=True, strip_contents=True), out_path)
    return out_path


# ─── COMMAND LINE (the Gate 2 call, the Chapter/Phase/Novel join, the read-back) ─────────────
def _read_utf8(path: str) -> str:
    """Read a UTF-8 text file; a leading byte-order mark is dropped and line endings become \\n."""
    with open(path, "r", encoding="utf-8-sig") as fh:
        return fh.read()


def _build_parser():
    """The command line: write (the Gate 2 call), assemble (join) and check (read-back)."""
    parser = argparse.ArgumentParser(
        prog="area_docx_creator.py", allow_abbrev=False,
        description="Starward Saga per-Area .docx writer, joiner and Title Block read-back "
                    "(authorized script 1, guardrails/tools/guardrail-authorized-scripts-only.md). With no arguments it runs the self-test.")
    sub = parser.add_subparsers(dest="command", required=True)

    w = sub.add_parser("write", allow_abbrev=False, help="write one per-Area .docx (the Gate 2 call)")
    w.add_argument("--text-file", required=True, help="UTF-8 file holding the confirmed Area text")
    for field in ("phase", "section", "part", "chapter", "area"):
        w.add_argument("--" + field, type=int, required=True)
    for field in ("area-name", "phase-name", "section-name", "novel-part-name",
                  "chapter-name"):
        w.add_argument("--" + field, default="")
    for field in ("chapter", "phase", "section"):
        w.add_argument("--first-of-" + field, action="store_true",
                       help="this Area is the first of its " + field.capitalize())
    w.add_argument("--phase-epigraph", default="",
                   help="the Part 30 Phase epigraph line (the first Area of a Phase only; printed first)")
    w.add_argument("--phase-epigraph-file", default="", help="UTF-8 file holding the Phase epigraph line")
    w.add_argument("--section-epigraph", "--epigraph", dest="section_epigraph", default="",
                   help="the Section's own Epigraph line, from its Section Spec (first Area of a Section)")
    w.add_argument("--section-epigraph-file", "--epigraph-file", dest="section_epigraph_file", default="",
                   help="UTF-8 file holding the Section's Epigraph line")
    w.add_argument("--output-root", default=DEFAULT_OUTPUT_ROOT)
    w.add_argument("--overwrite", action="store_true",
                   help="replace an Area that is already written (only /revise-area passes this)")

    a = sub.add_parser("assemble", allow_abbrev=False, help="join the Chapter .docx files of a Phase, or the Phase files of the novel, in reading order")
    a.add_argument("--scope", choices=("phase", "novel"), required=True)
    a.add_argument("--phase", type=int)
    a.add_argument("--output-root", default=DEFAULT_OUTPUT_ROOT)
    a.add_argument("--overwrite", action="store_true",
                   help="replace an existing joined file (after the author has confirmed)")

    c = sub.add_parser("check", allow_abbrev=False,
                       help="read a written per-Area .docx back and report its Area Title Block")
    c.add_argument("--file", required=True)
    c.add_argument("--expect", choices=("present", "absent"), default=None)
    return parser


def main(argv=None) -> int:
    """
    Command-line entry point. With no arguments it runs the self-test; otherwise it runs write,
    assemble or check. Exit code 0 is success, 1 is a read-back that failed, 2 is a refusal
    (an existing file, a missing file or a bad input).
    """
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")   # a printed title or path never crashes the run
        except (AttributeError, ValueError):
            pass
    argv = sys.argv[1:] if argv is None else list(argv)
    if not argv:
        _self_test()
        return 0
    parser = _build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "write":
            phase_epigraph = (_read_utf8(args.phase_epigraph_file) if args.phase_epigraph_file
                              else args.phase_epigraph).strip()
            section_epigraph = (_read_utf8(args.section_epigraph_file) if args.section_epigraph_file
                                else args.section_epigraph).strip()
            # `unset` (the Part 30 Phase epigraph line, or the Section Spec's Epigraph line) means no epigraph
            if phase_epigraph.lower() == "unset":
                phase_epigraph = ""
            if section_epigraph.lower() == "unset":
                section_epigraph = ""
            path = write_area_to_per_area_docx(
                phase=args.phase, section=args.section, part=args.part, chapter=args.chapter,
                area=args.area, area_text=_read_utf8(args.text_file),
                area_name=args.area_name, phase_name=args.phase_name,
                section_name=args.section_name, novel_part_name=args.novel_part_name,
                chapter_name=args.chapter_name,
                is_first_area_of_chapter=args.first_of_chapter,
                is_first_area_of_phase=args.first_of_phase,
                is_first_area_of_section=args.first_of_section,
                phase_epigraph=phase_epigraph, section_epigraph=section_epigraph,
                output_root=os.path.abspath(args.output_root),
                overwrite=args.overwrite)
            print("wrote: " + os.path.abspath(path))
            return 0
        if args.command == "assemble":
            root = os.path.abspath(args.output_root)
            if args.scope == "phase":
                if args.phase is None:
                    parser.error("--scope phase needs --phase")
                path = assemble_phase_docx(args.phase, root, args.overwrite)
            else:
                path = assemble_novel_docx(root, args.overwrite)
            print("wrote: " + os.path.abspath(path))
            return 0
        ok, lines = check_title_block(args.file, args.expect or "")
        print("\n".join(lines))
        return 0 if ok else 1
    except (FileExistsError, FileNotFoundError, ValueError, PackageNotFoundError) as exc:
        print("refused: " + str(exc), file=sys.stderr)
        return 2


# ─── SELF-TEST ───────────────────────────────────────────────────────────────────────
def _self_test() -> None:
    """The self-test; it runs when the script is started with no arguments. It writes only to temporary folders."""
    import sys
    print("Starward Saga DOCX Creator — Part 2 Rule 6.4.3")
    print(f"python-docx version: ", end="")
    try:
        import docx
        print(docx.__version__)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    print("Script is ready. Import write_area_to_per_area_docx for Gate 2 use.")

    # Sample test: every Area file carries its Area Title Block and sits at chapter-NNN/area-NN.docx.
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        common = dict(phase=1, section=1, part=1, chapter=1,
                      area_text="First light crossed the basin.\n\nThe second paragraph followed.",
                      phase_name="P", section_name="S", novel_part_name="N",
                      chapter_name="C", output_root=tmp)
        p1 = write_area_to_per_area_docx(area=1, area_name="Opening",
                                         is_first_area_of_chapter=True, **common)
        p2 = write_area_to_per_area_docx(area=2, area_name="Second", **common)
        t1 = "\n".join(p.text for p in Document(p1).paragraphs)
        t2 = "\n".join(p.text for p in Document(p2).paragraphs)
        ok = ("Area 1" in t1 and "1.1.1.001.01" in t1
              and "Area 2" in t2 and "1.1.1.001.02" in t2 and "STARWARD SAGA" not in t2
              and p1.replace("\\", "/").endswith("chapter-001/area-01.docx")
              and p2.replace("\\", "/").endswith("chapter-001/area-02.docx")
              and check_title_block(p1, "present")[0] and check_title_block(p2, "present")[0])
        print("Area Title Block sample test:", "PASS" if ok else "FAIL")
        if not ok:
            sys.exit(1)

    # Sample test (Title Page epigraph lines): the first Area of a Phase prints the Phase line then the
    # Section line; a later Section prints its own line alone; the Phase line is refused on any Area that
    # is not the first of its Phase. The images are 1x1 placeholders made inside the temporary folder.
    import struct
    import zlib
    def _png_chunk(kind: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data))
    png = (b"\x89PNG\r\n\x1a\n"
           + _png_chunk(b"IHDR", struct.pack(">IIBBBBB", 1, 1, 8, 2, 0, 0, 0))
           + _png_chunk(b"IDAT", zlib.compress(b"\x00\x00\x00\x00"))
           + _png_chunk(b"IEND", b""))
    with tempfile.TemporaryDirectory() as tmp:
        for rel in ("phase-1/phase-icon.png", "phase-1/section-1/section-icon.png",
                    "phase-1/section-2/section-icon.png"):
            os.makedirs(os.path.dirname(os.path.join(tmp, rel)), exist_ok=True)
            with open(os.path.join(tmp, rel), "wb") as fh:
                fh.write(png)
        common = dict(part=1, chapter=1, area=1, area_text="First light crossed the basin.",
                      phase_name="P", section_name="S", novel_part_name="N", chapter_name="C",
                      area_name="A", output_root=tmp, is_first_area_of_chapter=True)
        both = write_area_to_per_area_docx(
            phase=1, section=1, is_first_area_of_phase=True,
            is_first_area_of_section=True, phase_epigraph="PHASE LINE", section_epigraph="SECTION LINE",
            **common)
        only_section = write_area_to_per_area_docx(
            phase=1, section=2, is_first_area_of_section=True,
            epigraph="SECTION ONLY LINE", **common)
        texts = [[p.text for p in Document(f).paragraphs] for f in (both, only_section)]
        refused = False
        try:
            write_area_to_per_area_docx(phase=1, section=2, is_first_area_of_section=True,
                                        phase_epigraph="PHASE LINE", overwrite=True, **common)
        except ValueError:
            refused = True
        ok = (texts[0].index("PHASE LINE") + 1 == texts[0].index("SECTION LINE")
              and "PHASE LINE" not in texts[1] and "SECTION ONLY LINE" in texts[1]
              and check_title_block(both, "present")[0] and refused)
        print("Title Page epigraph sample test:", "PASS" if ok else "FAIL")
        if not ok:
            sys.exit(1)

    # Sample test (date line, Part 2 Rule 6.3.2b): a date line first is its own centred, smaller, italic
    # paragraph at every Area, the drop cap falls on the first narration paragraph after it, a text without
    # a date line still opens with the drop cap.
    with tempfile.TemporaryDirectory() as tmp:
        dl = "Year 1247, Ilovany, Orvil, Day 1"
        common = dict(phase=1, section=1, part=1, chapter=1, phase_name="P", section_name="S",
                      novel_part_name="N", chapter_name="C", output_root=tmp)
        first = write_area_to_per_area_docx(
            area=1, area_name="Opening", is_first_area_of_chapter=True,
            area_text=f"*{dl}*\n\nFirst light crossed the basin.\n\nThe second paragraph followed.", **common)
        second = write_area_to_per_area_docx(
            area=2, area_name="Next", area_text=f"*{dl}*\n\nThe wind turned.", **common)
        plain = write_area_to_per_area_docx(
            area=3, area_name="Plain",
            area_text="First light crossed the basin.\n\nThe second paragraph followed.", **common)
        italic_first = write_area_to_per_area_docx(
            area=4, area_name="Other",
            area_text='*"Hush," she said.*\n\nYear after year the basin filled.', **common)

        def _is_date_para(p):
            return (p.text == dl and p.alignment == WD_ALIGN_PARAGRAPH.CENTER
                    and p.paragraph_format.first_line_indent == Inches(0)
                    and all(r.font.italic and r.font.size == Pt(DATE_LINE_SIZE) for r in p.runs))

        def _drop_cap(p):
            return bool(p.runs) and p.runs[0].font.size == Pt(DROP_CAP_SIZE)

        pf_ = Document(first).paragraphs
        i = [p.text for p in pf_].index(dl)
        ps_ = Document(second).paragraphs
        j = [p.text for p in ps_].index(dl)
        pp_ = Document(plain).paragraphs
        k = next(n for n, p in enumerate(pp_) if p.text.startswith("First light"))
        pi_ = Document(italic_first).paragraphs
        m = next(n for n, p in enumerate(pi_) if p.text.startswith('"Hush'))
        ok = (_is_date_para(pf_[i]) and not _drop_cap(pf_[i])
              and pf_[i].paragraph_format.space_after == Pt(DATE_LINE_SPACE_AFTER)
              and pf_[i + 1].text == "First light crossed the basin." and _drop_cap(pf_[i + 1])
              and not _drop_cap(pf_[i + 2]) and pf_[i + 2].paragraph_format.first_line_indent == Inches(FIRST_INDENT)
              and _REFERENCE_CODE_RE.match(pf_[i - 1].text.strip())      # directly under the Area Title Block
              and _is_date_para(ps_[j]) and _drop_cap(ps_[j + 1])
              and _drop_cap(pp_[k]) and _drop_cap(pi_[m])                 # no date line: drop cap still opens the Area
              and not any(_is_date_para(p) for p in pp_ + pi_)
              and _date_line_text("*Year 1247, Sorevany, Nuvil, Day 27 to Mirovil, Day 29*") is not None
              and _date_line_text("*Year 1247, Ulenor, Mavil, Day 26 to Year 1248, Ilovany, Mirovil, Day 3*") is not None
              and _date_line_text("*Year of the Ox rose.*") is None
              and _date_line_text("**Year 1247, Ilovany, Orvil, Day 1**") is None
              and _date_line_text("Year 1247, Ilovany, Orvil, Day 1") is None
              and _date_line_text("*Year 1247, Ilovany, Orvil, Day 1* and more") is None)
        print("Date line sample test:", "PASS" if ok else "FAIL")
        if not ok:
            sys.exit(1)


if __name__ == "__main__":
    sys.exit(main())
