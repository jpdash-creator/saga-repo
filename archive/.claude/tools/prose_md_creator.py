# ═══════════════════════════════════════════════════════════════════════════
# STARWARD SAGA — Novel-Grade Per-Prose Markdown Creator
# Part 2 Area 7 — Book Creation Law: Chapter Document (.md)
# Rule 7.4.1 — Implementation Standard
# Rule 7.4.2 — Area Divider and Title Block Law
# Rule 7.4.3 — This file IS the stored canonical script (prose_md_creator.py)
# Rule 10.5.13 — Authorised Novel-Output Script #2
#
# Title Page Law (Part 1 Rule 10.5.14):
#   When is_first_prose_of_phase=True OR is_first_prose_of_section=True,
#   a Markdown title block is prepended:
#     --- (HR)
#     # PHASE N — PHASE NAME
#     ## Section N — Section Name
#     *Epigraph text* (if provided)
#     --- (HR)
#
# Usage (Gate 2 standard call):
#   from prose_md_creator import write_prose_to_per_prose_md
#   write_prose_to_per_prose_md(
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
#
# Companion to prose_docx_creator.py — identical function signature.
# ═══════════════════════════════════════════════════════════════════════════

import os
import re


# ─── SCENE BREAK MARKERS ─────────────────────────────────────────────────
SCENE_BREAK_MARKERS = {"***SCENE BREAK***", "* * *", "***"}
SCENE_BREAK_MD      = "* * *"          # canonical Markdown scene break


def get_prose_md_path(phase: int, section: int, part: int,
                       chapter: int, area: int, prose: int,
                       output_root: str) -> str:
    """Return the canonical path for a per-Prose .md file."""
    return os.path.join(
        output_root,
        f"phase-{phase}", f"section-{section}", f"part-{part}",
        f"chapter-{chapter:03d}", f"area-{area}",
        f"prose-{prose:05d}.md"
    )


# ─── AREA DIVIDER ─────────────────────────────────────────────────────────
def _md_area_divider(area: int, area_name: str) -> str:
    """
    Return the Markdown Area Divider line.
    Format: — Area N: [Area Name] —
    Called only when is_first_prose_of_area is True (Rule 7.4.2).
    """
    label = f"— Area {area}"
    if area_name:
        label += f": {area_name}"
    label += " —"
    return label


# ─── PROSE TITLE BLOCK ────────────────────────────────────────────────────
def _md_prose_title_block(prose: int, prose_name: str,
                           reference_code: str) -> list:
    """
    Return the Prose Title Block lines (Rule 7.4.2).
    Structure:
        **Prose N — [Prose Name]**
        *Reference: P.S.P.CCC.A.NNNNN*

        ---
    """
    if not prose_name:
        raise ValueError(
            "Prose Name is mandatory per Part 28 Area 18 Rule 18.3.1 — cannot be empty")
    return [
        f"**Prose {prose} — {prose_name}**",
        f"*Reference: {reference_code}*",
        "",
        "---",
    ]


# ─── PROSE BODY FORMATTER ─────────────────────────────────────────────────
def _md_prose_body(prose_text: str) -> list:
    """
    Return prose body as a list of Markdown lines, blank-line separated.

    Input formatting conventions (pass-through — already Markdown-compatible):
        *"..."*      = italic dialogue
        **text**     = bold (Named Move)
        ***text***   = bold-italic (Named Move in dialogue or narration)
        blank line   = paragraph break
        ***SCENE BREAK*** / * * * / *** = scene break → "* * *"

    Each paragraph is emitted as-is; scene break markers are normalized.
    """
    lines = []
    paragraphs = prose_text.strip().split("\n\n")

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        if para in SCENE_BREAK_MARKERS:
            lines.append("")
            lines.append(SCENE_BREAK_MD)
            lines.append("")
        else:
            lines.append(para)
            lines.append("")   # blank line between paragraphs

    # Remove trailing blank line if present
    while lines and lines[-1] == "":
        lines.pop()

    return lines


# ─── PRIMARY GATE 2 ENTRY POINT ──────────────────────────────────────────
def write_prose_to_per_prose_md(
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
        font_name: str = "EB Garamond") -> str:
    """
    PRIMARY GATE 2 WRITER — creates a single per-Prose .md file.

    Identical function signature to write_prose_to_per_prose_docx().

    Structural block order (Rule 7.4.2 + Part 1 Rule 10.5.14):
      0. Title Block    — ONLY if is_first_prose_of_phase or is_first_prose_of_section
                          ---
                          # PHASE N — PHASE NAME
                          ## Section N — Section Name
                          *Epigraph* (if provided)
                          ---
      1. Area Divider   — ONLY if is_first_prose_of_area is True
                          Format: — Area N: [Area Name] —
      2. Prose Title Block — ALWAYS
                          **Prose N — [Prose Name]**
                          *Reference: P.S.P.CCC.A.NNNNN*
                          (blank line)
                          ---
      3. Prose body     — ALWAYS

    Note: is_first_prose_of_chapter is accepted but produces no structural
    output in .md format (retained for signature parity with docx creator).
    font_name accepted but unused in .md output (signature parity).

    Returns the path to the written .md file.
    Raises ValueError if prose_name is empty (Part 28 Area 18 Rule 18.3.1).
    """
    if not prose_name:
        raise ValueError(
            f"Prose Name is mandatory (Part 28 Area 18 Rule 18.3.1). "
            f"Received empty prose_name for prose {prose:05d}.")

    prose_path = get_prose_md_path(phase, section, part, chapter,
                                    area, prose, output_root)
    os.makedirs(os.path.dirname(prose_path), exist_ok=True)

    reference_code = (
        f"{phase}.{section}.{part}.{chapter:03d}.{area}.{prose:05d}"
    )

    md_lines = []

    # ── 0. Phase / Section Title Block ───────────────────────────────────
    if is_first_prose_of_phase or is_first_prose_of_section:
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
        if epigraph and epigraph.strip():
            md_lines.append(f"*{epigraph.strip()}*")
            md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

    # ── 1. Area Divider ──────────────────────────────────────────────────
    if is_first_prose_of_area:
        md_lines.append(_md_area_divider(area, area_name))
        md_lines.append("")   # blank line after divider

    # ── 2. Prose Title Block ─────────────────────────────────────────────
    md_lines.extend(_md_prose_title_block(prose, prose_name, reference_code))
    md_lines.append("")   # blank line before body

    # ── 3. Prose Body ────────────────────────────────────────────────────
    md_lines.extend(_md_prose_body(prose_text))

    # Write file (UTF-8, LF line endings for cross-platform consistency)
    content = "\n".join(md_lines) + "\n"
    with open(prose_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

    return prose_path


# ─── CONVENIENCE: WRITE FROM DICT ────────────────────────────────────────────
def write_prose_from_metadata(metadata: dict, prose_text: str,
                               output_root: str = "projects/novel-starward-saga") -> str:
    """
    Convenience wrapper: pass a metadata dict with all position fields.
    Identical interface to prose_docx_creator.write_prose_from_metadata().

    metadata keys: phase, section, part, chapter, area, prose,
                   prose_name, phase_name, section_name, novel_part_name,
                   chapter_name, area_name, pacing, word_count,
                   is_first_prose_of_chapter, is_first_prose_of_area,
                   is_first_prose_of_phase, is_first_prose_of_section, epigraph
    """
    return write_prose_to_per_prose_md(
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


# ─── SELF-TEST ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import sys
    import tempfile

    print("Starward Saga MD Creator — Part 2 Rule 7.4.3")
    print("Testing write_prose_to_per_prose_md()...\n")

    # Minimal test: Area Divider + Title Block + prose body with mixed formatting
    test_text = (
        'The hum arrived before the light.\n\n'
        '*"This is the way,"* she said.\n\n'
        'He stepped forward. The ***Ruling Meridian Stance*** held.\n\n'
        '***SCENE BREAK***\n\n'
        'Silence followed.'
    )

    with tempfile.TemporaryDirectory() as tmp:
        out = write_prose_to_per_prose_md(
            phase=1, section=1, part=1, chapter=1, area=7, prose=1,
            prose_text=test_text,
            prose_name="Test Prose — MD Creator",
            area_name="The Verification Area",
            is_first_prose_of_chapter=True,   # accepted but no .md output
            is_first_prose_of_area=True,
            output_root=tmp
        )
        with open(out, encoding="utf-8") as f:
            content = f.read()

    print("Output path:", out.replace(tmp, "<tmp>"))
    print()
    print("─" * 60)
    print(content)
    print("─" * 60)

    # Verify structural elements
    checks = [
        ("— Area 7: The Verification Area —" in content,
         "Area Divider present"),
        ("**Prose 1 — Test Prose — MD Creator**" in content,
         "Prose Title present"),
        ("*Reference: 1.1.1.001.7.00001*" in content,
         "Reference Code present"),
        ("---" in content,
         "HR separator present"),
        ("***Ruling Meridian Stance***" in content,
         "Bold-italic pass-through intact"),
        ("* * *" in content,
         "Scene break normalised"),
    ]

    all_pass = True
    for result, label in checks:
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
