# ═══════════════════════════════════════════════════════════════════════════
# STARWARD SAGA — Novel-Grade Per-Area Markdown Creator
# Part 2 Area 7 — Book Creation Law: Area Markdown File (.md)
# Rule 7.2.1 — Chapter Header Block Placement in the Per-Area Markdown
# Rule 7.4.1 — Implementation Standard
# Rule 7.4.2 — Area Title Block Law
# Rule 7.4.3 — This file IS the stored canonical script (area_md_creator.py)
# Authorised Novel-Output Script #2 (guardrails/tools/guardrail-authorized-scripts-only.md)
#
# File layout: one Area is one file, projects/novel-starward-saga/phase-N/section-N/part-N/
#   chapter-NNN/area-NN.md  (two-digit Area number, resets per Chapter; no Area subfolders).
#   The .md is written as a coupled pair with the .docx of the same Area at Gate 2.
#
# Area file blocks, in order:
#   0. Title Block (only on the first Area of a Phase or of a Section):
#        --- (HR)
#        # PHASE N — PHASE NAME
#        ## Section N — Section Name
#        *Phase epigraph text* (if provided; the Part 30 Phase epigraph line, passed only on the first Area of a
#                               Phase; a Phase epigraph on any other Area is refused and nothing is written)
#        *Section epigraph text* (if provided; the Epigraph line of that Section's Section Spec, Part 38 Rule 10.3.1)
#        --- (HR)
#      The first Area of a Phase prints the Phase line and then Section 1's own line, one italic paragraph each;
#      the first Area of every other Section prints only that Section's own line. Empty or `unset` means none.
#      This script reads no spec and no skill and writes no epigraph text.
#   1. Chapter Header Block (only on the first Area of a Chapter)
#   2. Area Title Block (on EVERY Area file): the Area heading and the Reference line
#   3. Area body. The body may begin with its date line (one italic line, "*Year 1247, ...*"), passed through
#      exactly as the text gives it.
#
# Usage (Gate 2 standard call):
#   from area_md_creator import write_area_to_per_area_md
#   write_area_to_per_area_md(
#       phase=1, section=1, part=1, chapter=1, area=1,
#       area_text="*Year 1247, ...*  First light crossed the basin fields...",
#       area_name="Paired Sovereigns",
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
#   python .claude/tools/area_md_creator.py write --text-file AREA.txt \
#       --phase 1 --section 1 --part 1 --chapter 1 --area 1 \
#       --area-name "..." --phase-name "..." --section-name "..." --novel-part-name "..." \
#       --chapter-name "..." [--first-of-chapter] [--first-of-phase] [--first-of-section] \
#       [--phase-epigraph-file PHASE_EPIGRAPH.txt] [--section-epigraph-file SECTION_EPIGRAPH.txt] \
#       [--output-root DIR] [--overwrite]
#   (--phase-epigraph "text" and --section-epigraph "text" give a line inline.)
#   The arguments are the same as area_docx_creator.py write. AREA.txt is a UTF-8 text file
#   holding the Area text. With no arguments the script runs its self-test. A writer refuses to
#   replace an Area that is already on disk unless --overwrite is given (only /revise-area
#   gives it).
#
# Companion to area_docx_creator.py — identical function signature.
# ═══════════════════════════════════════════════════════════════════════════

import os
import re
import argparse
import sys

# ─── OUTPUT ROOT (Part 2 Rule 5.2.1) ──────────────────────────────────────
def _default_output_root() -> str:
    """
    The novel output folder, computed from this script's own location so the files land in
    the same place whatever folder a session runs from (the method reset_story.py uses).
    This file lives at REPO_ROOT/.claude/tools/area_md_creator.py, so two folders above the tools
    folder is REPO_ROOT and the output folder is REPO_ROOT/projects/novel-starward-saga.
    """
    tools_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(os.path.dirname(tools_dir))
    return os.path.join(repo_root, "projects", "novel-starward-saga")


DEFAULT_OUTPUT_ROOT = _default_output_root()


# ─── TIME-SKIP MARKERS ───────────────────────────────────────────────────
TIME_SKIP_MARKERS = {"***SCENE BREAK***", "* * *", "***"}   # "* * *" is the typed form (Rule 6.3.5)
TIME_SKIP_MD      = "* * *"          # canonical Markdown time-skip mark (Rule 7.2.4)


def get_area_md_path(phase: int, section: int, part: int,
                     chapter: int, area: int,
                     output_root: str) -> str:
    """Return the canonical path for a per-Area .md file: chapter-NNN/area-NN.md."""
    return os.path.join(
        output_root,
        f"phase-{phase}", f"section-{section}", f"part-{part}",
        f"chapter-{chapter:03d}",
        f"area-{area:02d}.md"
    )


# ─── CHAPTER HEADER BLOCK ─────────────────────────────────────────────────
def _md_chapter_header_block(phase: int, section: int, part: int, chapter: int,
                              phase_name: str, section_name: str,
                              novel_part_name: str, chapter_name: str) -> list:
    """
    Return the Markdown Chapter Header Block lines (Rule 7.2.1).
    Called only for the first Area file of a Chapter (`area-01.md`). Precedes the
    Area Title Block and the Area body (and any Phase/Section Title Block, which
    itself precedes this block when is_first_area_of_phase/section is True).

    Structure (Rule 7.2.1):
        # STARWARD SAGA
        ## Phase N — Phase Name
        ## Section N — Section Name
        ## Part N — Novel-Part Name    <!-- MANDATORY — Part 28 Area 18 -->

        # Chapter N — Chapter Name    <!-- MANDATORY — Part 28 Area 18 -->

        ---

    Phase Name and Section Name are Locked Canon per Part 30 (no mandatory
    comment marker). Novel-Part Name and Chapter Name are categorically
    mandatory per Part 28 Area 18 Rule 18.3.3 (mandatory comment marker
    carried, matching the canon-specified format exactly).
    """
    phase_label = f"## Phase {phase}" + (f" — {phase_name}" if phase_name else "")
    section_label = f"## Section {section}" + (f" — {section_name}" if section_name else "")
    part_label = (f"## Part {part}"
                  + (f" — {novel_part_name}" if novel_part_name else "")
                  + "    <!-- MANDATORY — Part 28 Area 18 -->")
    chapter_label = (f"# Chapter {chapter}"
                      + (f" — {chapter_name}" if chapter_name else "")
                      + "    <!-- MANDATORY — Part 28 Area 18 -->")
    return [
        "# STARWARD SAGA",
        phase_label,
        section_label,
        part_label,
        "",
        chapter_label,
        "",
        "---",
    ]


# ─── AREA TITLE BLOCK ─────────────────────────────────────────────────────
def _md_area_title_block(area: int, area_name: str, reference_code: str) -> list:
    """
    Return the Area Title Block lines (Rule 7.2.2) — written on every Area file, and it is
    the Area separator when Area files are joined into a Chapter file.

    Structure:
        ## Area N — [Area Name]    <!-- MANDATORY — Part 28 Area 18 -->
        *Reference: P.S.N.CCC.AA*
    """
    if not area_name:
        raise ValueError(
            "Area Name is mandatory per Part 28 Area 18 Rule 18.3.1 — cannot be empty")
    return [
        f"## Area {area} — {area_name}"
        "    <!-- MANDATORY — Part 28 Area 18 -->",
        f"*Reference: {reference_code}*",
    ]


# ─── AREA BODY FORMATTER ──────────────────────────────────────────────────
def _md_area_body(area_text: str) -> list:
    """
    Return the Area body as a list of Markdown lines, blank-line separated.

    Input formatting conventions (pass-through — already Markdown-compatible):
        *Year 1247, ...*  = the date line, the first paragraph of the text (one italic line)
        *"..."*      = italic dialogue
        **text**     = bold emphasis (never a Named Move)
        ***text***   = bold-italic Named Move or cultivation level, in narration and in dialogue
        blank line   = paragraph break
        * * * (also *** or ***SCENE BREAK***) = time-skip mark → "* * *"

    Each paragraph is emitted as-is; time-skip marks are normalized.
    """
    lines = []
    area_text = area_text.replace("\r\n", "\n").replace("\r", "\n")   # Windows and old Mac line endings
    paragraphs = area_text.strip().split("\n\n")

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        if para in TIME_SKIP_MARKERS:
            lines.append("")
            lines.append(TIME_SKIP_MD)
            lines.append("")
        else:
            lines.append(para)
            lines.append("")   # blank line between paragraphs

    # Remove trailing blank line if present
    while lines and lines[-1] == "":
        lines.pop()

    return lines


# ─── PRIMARY GATE 2 ENTRY POINT ──────────────────────────────────────────
def write_area_to_per_area_md(
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
        font_name: str = "EB Garamond",
        overwrite: bool = False,
        phase_epigraph: str = "",
        section_epigraph: str = "") -> str:
    """
    PRIMARY GATE 2 WRITER — creates a single per-Area .md file (chapter-NNN/area-NN.md).

    Identical function signature to write_area_to_per_area_docx().

    Epigraph values: phase_epigraph is the Part 30 Phase line, given only on the first Area of a
    Phase; section_epigraph is the Epigraph line of the Section's Section Spec. `epigraph` is an
    alias of the Section line and is used when section_epigraph is empty. Both lines print in the
    title block, Phase line first.

    Structural block order (Rule 7.2.1, 7.4.2 + Part 2 Rule 7.2.1a):
      0. Title Block         — ONLY if is_first_area_of_phase or is_first_area_of_section
                               ---
                               # PHASE N — PHASE NAME
                               ## Section N — Section Name
                               *Phase epigraph* (if provided; first Area of a Phase only)
                               *Section epigraph* (if provided)
                               ---
      1. Chapter Header Block — ONLY if is_first_area_of_chapter is True (Rule 7.2.1)
                               # STARWARD SAGA
                               ## Phase N — Phase Name
                               ## Section N — Section Name
                               ## Part N — Novel-Part Name    <!-- MANDATORY — Part 28 Area 18 -->
                               (blank line)
                               # Chapter N — Chapter Name    <!-- MANDATORY — Part 28 Area 18 -->
                               (blank line)
                               ---
      2. Area Title Block — ALWAYS (every Area file)
                          ## Area N — [Area Name]    <!-- MANDATORY — Part 28 Area 18 -->
                          *Reference: P.S.N.CCC.AA*
                          (blank line)
      3. Area body      — ALWAYS (the date line is the first paragraph of the text)

    font_name, pacing and word_count are accepted but unused in .md output (signature parity).

    Returns the path to the written .md file.
    Raises ValueError if area_name is empty (Part 28 Area 18 Rule 18.3.1).
    Raises ValueError, before any file is written, if phase_epigraph is given on an Area that is not
    the first of its Phase (the Phase line prints only in the title block that opens a Phase).
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

    area_path = get_area_md_path(phase, section, part, chapter, area, output_root)
    if os.path.exists(area_path) and not overwrite:
        raise FileExistsError(
            f"{area_path} already exists. A written Area is replaced only by /revise-area, "
            f"which passes overwrite=True (--overwrite on the command line).")
    os.makedirs(os.path.dirname(area_path), exist_ok=True)

    reference_code = f"{phase}.{section}.{part}.{chapter:03d}.{area:02d}"

    md_lines = []

    # ── 0. Phase / Section Title Block ───────────────────────────────────
    if is_first_area_of_phase or is_first_area_of_section:
        md_lines.append("---")
        md_lines.append("")
        phase_heading = f"# PHASE {phase}"
        if phase_name:
            phase_heading += f" — {phase_name.upper()}"
        md_lines.append(phase_heading)
        md_lines.append("")
        section_heading = f"## Section {section}"
        if section_name:
            section_heading += f" — {section_name}"
        md_lines.append(section_heading)
        md_lines.append("")
        for line in (phase_epigraph, section_epigraph):   # the Phase line first, then the Section's own
            if line and line.strip():
                md_lines.append(f"*{line.strip()}*")
                md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

    # ── 1. Chapter Header Block ──────────────────────────────────────────
    if is_first_area_of_chapter:
        md_lines.extend(_md_chapter_header_block(
            phase, section, part, chapter,
            phase_name, section_name, novel_part_name, chapter_name
        ))
        md_lines.append("")   # blank line after Chapter Header Block

    # ── 2. Area Title Block (every Area) ─────────────────────────────────
    md_lines.extend(_md_area_title_block(area, area_name, reference_code))
    md_lines.append("")   # blank line before body

    # ── 3. Area Body ─────────────────────────────────────────────────────
    md_lines.extend(_md_area_body(area_text))

    # Write file (UTF-8, LF line endings for cross-platform consistency)
    content = "\n".join(md_lines) + "\n"
    with open(area_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

    return area_path


# ─── CONVENIENCE: WRITE FROM DICT ────────────────────────────────────────────
def write_area_from_metadata(metadata: dict, area_text: str,
                             output_root: str = DEFAULT_OUTPUT_ROOT,
                             overwrite: bool = False) -> str:
    """
    Convenience wrapper: pass a metadata dict with all position fields.
    Identical interface to area_docx_creator.write_area_from_metadata().

    metadata keys: phase, section, part, chapter, area,
                   area_name, phase_name, section_name, novel_part_name,
                   chapter_name, pacing, word_count,
                   is_first_area_of_chapter,
                   is_first_area_of_phase, is_first_area_of_section,
                   phase_epigraph, section_epigraph (epigraph is an alias of section_epigraph)
    """
    return write_area_to_per_area_md(
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


# ─── COMMAND LINE (the Gate 2 call) ───────────────────────────────────────────────
def _read_utf8(path: str) -> str:
    """Read a UTF-8 text file; a leading byte-order mark is dropped and line endings become \\n."""
    with open(path, "r", encoding="utf-8-sig") as fh:
        return fh.read()


def _build_parser():
    """The command line: write, the Gate 2 call (identical arguments to area_docx_creator.py)."""
    parser = argparse.ArgumentParser(
        prog="area_md_creator.py", allow_abbrev=False,
        description="Starward Saga per-Area .md writer (authorized script 2, guardrails/tools/guardrail-authorized-scripts-only.md). "
                    "With no arguments it runs the self-test.")
    sub = parser.add_subparsers(dest="command", required=True)

    w = sub.add_parser("write", allow_abbrev=False, help="write one per-Area .md (the Gate 2 call)")
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
    return parser


def main(argv=None) -> int:
    """
    Command-line entry point. With no arguments it runs the self-test; otherwise it runs write.
    Exit code 0 is success, 2 is a refusal (an existing file or a bad input).
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
    args = _build_parser().parse_args(argv)
    try:
        phase_epigraph = (_read_utf8(args.phase_epigraph_file) if args.phase_epigraph_file
                          else args.phase_epigraph).strip()
        section_epigraph = (_read_utf8(args.section_epigraph_file) if args.section_epigraph_file
                            else args.section_epigraph).strip()
        # `unset` (the Part 30 Phase epigraph line, or the Section Spec's Epigraph line, Part 38 Rule 10.3.1) means no epigraph
        if phase_epigraph.lower() == "unset":
            phase_epigraph = ""
        if section_epigraph.lower() == "unset":
            section_epigraph = ""
        path = write_area_to_per_area_md(
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
    except (FileExistsError, FileNotFoundError, ValueError) as exc:
        print("refused: " + str(exc), file=sys.stderr)
        return 2


# ─── SELF-TEST ───────────────────────────────────────────────────────────────
def _self_test() -> None:
    """The self-test; it runs when the script is started with no arguments. It writes only to a temp folder."""
    import tempfile

    print("Starward Saga MD Creator — Part 2 Rule 7.4.3")
    print("Testing write_area_to_per_area_md()...\n")

    test_text = (
        '*Year 1247, Ilovany, Orvil, Day 1*\n\n'
        'First light crossed the basin fields.\n\n'
        '*"This is the way,"* she said.\n\n'
        'He stepped forward. The ***Ruling Meridian Stance*** held.\n\n'
        '* * *\n\n'
        'Silence followed.'
    )

    with tempfile.TemporaryDirectory() as tmp:
        out = write_area_to_per_area_md(
            phase=1, section=1, part=1, chapter=1, area=7,
            area_text=test_text,
            area_name="The Verification Area",
            phase_name="The Roots of Becoming",
            section_name="Azure Sky and Gale",
            novel_part_name="The Twin Oaths",
            chapter_name="Twin Courts at Dawn",
            is_first_area_of_chapter=True,   # emits Chapter Header Block (Rule 7.2.1)
            output_root=tmp
        )
        with open(out, encoding="utf-8") as f:
            content = f.read()

    print("Output path:", out.replace(tmp, "<tmp>"))
    print()
    print("─" * 60)
    print(content)
    print("─" * 60)

    checks = [
        (out.replace("\\", "/").endswith("chapter-001/area-07.md"),
         "Path is chapter-001/area-07.md (no Area subfolder)"),
        ("# STARWARD SAGA" in content,
         "Chapter Header Block present (Rule 7.2.1)"),
        ("## Part 1 — The Twin Oaths    <!-- MANDATORY — Part 28 Area 18 -->" in content,
         "Chapter Header Block Part line present with MANDATORY marker"),
        ("# Chapter 1 — Twin Courts at Dawn    <!-- MANDATORY — Part 28 Area 18 -->" in content,
         "Chapter Header Block Chapter line present with MANDATORY marker"),
        ("## Area 7 — The Verification Area    <!-- MANDATORY — Part 28 Area 18 -->" in content,
         "Area Title Block heading present"),
        ("*Reference: 1.1.1.001.07*" in content,
         "Reference Code present"),
        ("---" in content,
         "HR separator present"),
        ("*Reference: 1.1.1.001.07*\n\n*Year 1247," in content,
         "Date line is the first body paragraph, after the Area Title Block"),
        ("***Ruling Meridian Stance***" in content,
         "Bold-italic pass-through intact"),
        ("* * *" in content,
         "Time-skip mark kept as * * *"),
    ]

    all_pass = True
    for result, label in checks:
        status = "PASS" if result else "FAIL"
        if not result:
            all_pass = False
        print(f"  [{status}] {label}")

    # Every Area file carries the Area Title Block; a non-first Area has no Chapter Header Block.
    with tempfile.TemporaryDirectory() as tmp2:
        out2 = write_area_to_per_area_md(
            phase=1, section=1, part=1, chapter=1, area=2,
            area_text=test_text, area_name="Second Area", output_root=tmp2)
        with open(out2, encoding="utf-8") as f:
            content2 = f.read()
    for result, label in [
        ("## Area 2 — Second Area" in content2, "Later Area: Area Title Block present"),
        ("*Reference: 1.1.1.001.02*" in content2, "Later Area: Reference line present"),
        ("# STARWARD SAGA" not in content2, "Later Area: no Chapter Header Block"),
    ]:
        status = "PASS" if result else "FAIL"
        if not result:
            all_pass = False
        print(f"  [{status}] {label}")

    # Title block epigraph lines: the first Area of a Phase prints the Phase line then the Section line;
    # a later Section prints its own line alone; the Phase line is refused on an Area that is not the
    # first of its Phase.
    with tempfile.TemporaryDirectory() as tmp3:
        common = dict(part=1, chapter=1, area=1, area_text=test_text, area_name="Opening",
                      phase_name="P", section_name="S", output_root=tmp3)
        both = write_area_to_per_area_md(
            phase=1, section=1, is_first_area_of_phase=True, is_first_area_of_section=True,
            phase_epigraph="PHASE LINE", section_epigraph="SECTION LINE", **common)
        only_section = write_area_to_per_area_md(
            phase=1, section=2, is_first_area_of_section=True, epigraph="SECTION ONLY LINE", **common)
        with open(both, encoding="utf-8") as f:
            text_both = f.read()
        with open(only_section, encoding="utf-8") as f:
            text_only = f.read()
        refused = False
        try:
            write_area_to_per_area_md(phase=1, section=2, is_first_area_of_section=True,
                                      phase_epigraph="PHASE LINE", overwrite=True, **common)
        except ValueError:
            refused = True
    for result, label in [
        ("*PHASE LINE*\n\n*SECTION LINE*\n\n---" in text_both, "First Area of a Phase: Phase line, then Section line"),
        ("PHASE LINE" not in text_only and "*SECTION ONLY LINE*\n\n---" in text_only,
         "First Area of another Section: its own line alone"),
        (refused, "Phase line refused on an Area that is not the first of its Phase"),
    ]:
        status = "PASS" if result else "FAIL"
        if not result:
            all_pass = False
        print(f"  [{status}] {label}")

    print()
    if all_pass:
        print("All checks passed. Script is ready for Gate 2 use.")
    else:
        print("One or more checks FAILED. Review output above.")
        sys.exit(1)


if __name__ == "__main__":
    sys.exit(main())
