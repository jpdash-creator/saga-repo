#!/usr/bin/env python3
"""
reset_story.py -- Starward Saga [HARD RESET AND START STORY] command.

Usage:
    python reset_story.py

What this script does (in order):
  1. Clears prose output files from projects/novel-starward-saga/ (prose-*.md and
     prose-*.docx); preserves phase-icon.png, phase-icon.svg, section-icon.png,
     section-icon.svg
  2. Deletes all files in .claude/story-memory/session-log/  (the audit-log analogue
     of the old memory/ folder -- see .claude/guardrails/ledger/guardrail-session-log-not-canon.md)
  3. Deletes all side-character ledger files  (keeps _index.md)
  4. Cleans every hero ledger in .claude/story-memory/ledger-character-hero/
  5. Cleans all other .claude/story-memory/ledger-* files (faction, affiliation,
     civilization, technology, worlds):
       - Strips all prose-event rows from event tables (any section label)
       - Removes individual bullet-point entries "established in Prose X"
       - Resets First Prose Appearance / First Prose Establishment fields
       - Refreshes Last Updated to today

NOT touched:
  - .claude/tools/  (the folder this script lives in)
  - .claude/skills/, .claude/guardrails/, .claude/canon-manifest/, .claude/agents/,
    .claude/commands/  (the canon structure itself)
  - _index.md files in any ledger folder
  - phase-icon.png / phase-icon.svg (Phase images are kept)
  - section-icon.png / section-icon.svg (Section images are kept)

Directory layout assumption: this script lives at REPO_ROOT/.claude/tools/reset_story.py.
story-memory lives at REPO_ROOT/.claude/story-memory/ and the novel output lives at
REPO_ROOT/projects/novel-starward-saga/ -- these are NOT siblings of each other or of this
script (unlike the old starward-saga/ layout where everything shared one parent), so the
repo root is resolved explicitly below rather than by counting parent directories.
"""

import os
import re
import shutil
from datetime import date

TODAY = date.today().isoformat()

# Icon file names to always preserve in Step 1
ICON_FILENAMES = {
    "phase-icon.png",
    "phase-icon.svg",
    "section-icon.png",
    "section-icon.svg",
}

# Prose output file patterns to delete in Step 1
PROSE_EXTENSIONS = {".md", ".docx"}

# Matches a prose reference:  1.1.1.001.1.00001
PROSE_REF_RE = re.compile(r'\d+\.\d+\.\d+\.\d{3}\.\d+\.\d{5}')

# Matches a prose-event table row.
# Two formats:
#   (a) | Prose 1.1.1.001.1.00001 ...   (hero ledger style)
#   (b) | 1.1.1.001.1.00001 ...         (general ledger style)
PROSE_ROW_RE = re.compile(r'^\|\s*(?:Prose\s+)?\d+\.\d+\.\d+\.\d{3}\.\d+\.\d{5}')

# Matches prior [RESET STORY] Canon-Update rows
RESET_ROW_RE = re.compile(r'^\|\s*Canon Update.*\[RESET STORY\]')


def get_repo_root():
    """
    REPO_ROOT/.claude/tools/reset_story.py -> three levels up is REPO_ROOT.
    Explicit by design (see module docstring) -- do not shorten this by
    "counting parent folders" if this script is ever moved again; instead,
    update the path joins in get_novel_dir() / get_story_memory_dir() directly.
    """
    tools_dir = os.path.dirname(os.path.abspath(__file__))
    claude_dir = os.path.dirname(tools_dir)
    return os.path.dirname(claude_dir)


def get_novel_dir(repo_root):
    return os.path.join(repo_root, "projects", "novel-starward-saga")


def get_story_memory_dir(repo_root):
    return os.path.join(repo_root, ".claude", "story-memory")


def write_text(path, text):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def read_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def clear_dir_contents(path, keep=None):
    """Delete everything inside *path* except items in *keep*."""
    keep = set(keep or [])
    deleted = []
    if not os.path.isdir(path):
        return deleted
    for item in os.listdir(path):
        if item in keep:
            continue
        full = os.path.join(path, item)
        if os.path.isdir(full):
            shutil.rmtree(full)
        else:
            os.remove(full)
        deleted.append(item)
    return deleted


def step1_clear_novel(novel_dir):
    """
    Step 1: Delete only prose output files (.md, .docx whose name starts with 'prose-')
    from projects/novel-starward-saga/ recursively. Phase/section icon files are PRESERVED.
    """
    print("\n[Step 1] Clearing prose files from projects/novel-starward-saga/ (preserving icons) ...")
    if not os.path.isdir(novel_dir):
        print("  (projects/novel-starward-saga/ not found -- skipping)")
        return

    deleted_count = 0
    for dirpath, dirnames, filenames in os.walk(novel_dir):
        for fname in filenames:
            if fname in ICON_FILENAMES:
                continue   # Always preserve icon files
            _, ext = os.path.splitext(fname)
            if ext.lower() in PROSE_EXTENSIONS and fname.startswith("prose-"):
                full = os.path.join(dirpath, fname)
                os.remove(full)
                rel = os.path.relpath(full, novel_dir)
                print("  deleted: " + rel)
                deleted_count += 1

    if deleted_count == 0:
        print("  (no prose files found)")
    print("  Done.")


def step2_clear_session_log(story_memory_dir):
    print("\n[Step 2] Clearing story-memory/session-log/ ...")
    log_dir = os.path.join(story_memory_dir, "session-log")
    deleted = clear_dir_contents(log_dir, keep={"README.md"})
    if deleted:
        for d in deleted:
            print("  deleted: " + d)
    else:
        print("  (already empty)")
    print("  Done.")


def step3_clear_side_ledgers(story_memory_dir):
    print("\n[Step 3] Clearing ledger-character-side/ (keeps _index.md) ...")
    side_dir = os.path.join(story_memory_dir, "ledger-character-side")
    deleted = clear_dir_contents(side_dir, keep={"_index.md"})
    if deleted:
        for d in deleted:
            print("  deleted: " + d)
    else:
        print("  (no side-character files present)")
    print("  Done.")


def charname_from_filename(filename):
    return os.path.splitext(filename)[0].upper()


def clean_hero_ledger(text, charname):
    lines = text.split('\n')
    out = []

    in_named_moves = False
    named_moves_placeholder_added = False

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.startswith('**First Prose Appearance:**') and PROSE_REF_RE.search(line):
            out.append('**First Prose Appearance:** Not yet established -- to be defined in prose')
            i += 1
            continue

        if line.startswith('**Last Updated:**'):
            out.append('**Last Updated:** ' + TODAY)
            i += 1
            continue

        if line.startswith('**Ledger Version:**'):
            out.append('**Ledger Version:** v1.0')
            i += 1
            continue

        if PROSE_ROW_RE.match(line):
            i += 1
            continue

        if RESET_ROW_RE.match(line):
            i += 1
            continue

        if re.match(r'\*\*Physical Description', line) and PROSE_REF_RE.search(line):
            if line.rstrip().endswith(':'):
                out.append('**Physical Description (key identifiers):** Not yet established -- to be defined in prose')
                i += 1
                while i < len(lines) and (
                    lines[i].startswith('- ') or
                    lines[i].startswith('  ') or
                    (lines[i].strip() == '' and
                     i + 1 < len(lines) and
                     lines[i + 1].startswith('- '))
                ):
                    i += 1
            else:
                out.append('**Physical Description (key identifiers):** Not yet established -- to be defined in prose')
                i += 1
            continue

        if re.match(r'\*\*Voice Register', line) and PROSE_REF_RE.search(line):
            if line.rstrip().endswith(':'):
                out.append('**Voice Register (per Part 29):** Not yet established -- to be defined in prose')
                i += 1
                while i < len(lines) and (
                    lines[i].startswith('- ') or
                    lines[i].startswith('  ') or
                    (lines[i].strip() == '' and
                     i + 1 < len(lines) and
                     lines[i + 1].startswith('- '))
                ):
                    i += 1
            else:
                out.append('**Voice Register (per Part 29):** Not yet established -- to be defined in prose')
                i += 1
            continue

        if line.startswith('**Aliases / Titles / Epithets:**') and PROSE_REF_RE.search(line):
            cleaned = re.sub(
                r';\s*"[^"]+"\s*\([^)]*(?:established\s+Prose|Prose\s+\d+\.\d+\.\d+)[^)]*\)',
                '', line
            )
            out.append(cleaned)
            i += 1
            continue

        if (line.startswith('**') and
                re.search(r'established\s+in\s+Prose\s+\d+\.\d+\.\d+', line) and
                'Locked Canon' not in line and
                'Phase 1 End-State' not in line):
            field_match = re.match(r'^(\*\*.*?:\*\*)', line)
            if field_match:
                out.append(field_match.group(1) + ' Not yet established -- to be defined in prose')
            else:
                out.append(line)
            i += 1
            continue

        if re.match(r'\*\*Signature Named Moves \(Part 6\):\*\*', line):
            in_named_moves = True
            named_moves_placeholder_added = False
            out.append(line)
            i += 1
            continue

        if in_named_moves:
            if line.startswith('##') or (
                line.startswith('**') and
                'Named Move' not in line and
                'Innate Move' not in line and
                'Part 6' not in line and
                line.strip() != ''
            ):
                in_named_moves = False

            elif (line.startswith('- **') or (
                line.startswith('- ') and
                len(line) > 60 and
                'Not yet established' not in line and
                'Part 6 v2' not in line and
                'schema-open' not in line and
                'none registered' not in line
            )):
                if not named_moves_placeholder_added:
                    out.append('- Not yet established -- to be defined in prose')
                    named_moves_placeholder_added = True
                i += 1
                continue

            else:
                if 'Not yet established' in line and line.startswith('- '):
                    named_moves_placeholder_added = True
                out.append(line)
                i += 1
                continue

        # Footer: *CHARNAME -- Hero Ledger -- v...
        footer_pat = r'^\*' + re.escape(charname) + r'\s*[-–—]\s*Hero Ledger'
        if re.match(footer_pat, line):
            out.append(
                '*' + charname + ' -- Hero Ledger -- v1.0 (' + TODAY + ') -- '
                'Post-reset: all prose-established content cleared. '
                'Framework baseline retained.*'
            )
            i += 1
            continue

        out.append(line)
        i += 1

    return '\n'.join(out)


def step4_clean_hero_ledgers(story_memory_dir):
    print("\n[Step 4] Cleaning ledger-character-hero/ ...")
    hero_dir = os.path.join(story_memory_dir, "ledger-character-hero")
    for filename in sorted(os.listdir(hero_dir)):
        if filename == '_index.md' or not filename.endswith('.md'):
            continue
        filepath = os.path.join(hero_dir, filename)
        charname = charname_from_filename(filename)
        original = read_text(filepath)
        cleaned  = clean_hero_ledger(original, charname)
        write_text(filepath, cleaned)
        print("  cleaned: " + filename)
    print("  Done.")


def clean_general_ledger(text):
    """
    For non-hero ledger files:
    - Remove ALL prose-event table rows
    - Remove prior [RESET STORY] Canon Update rows
    - Remove bullet-point lines established in a prose unit
    - Reset First Prose Appearance / First Prose Establishment fields
    - Refresh Last Updated to today
    """
    lines = text.split('\n')
    out = []

    for line in lines:
        if PROSE_ROW_RE.match(line):
            continue

        if RESET_ROW_RE.match(line):
            continue

        if (line.startswith('- ') or line.startswith('  - ')) and PROSE_REF_RE.search(line):
            if 'established in Prose' in line or 'established Prose' in line:
                continue

        if (line.startswith('**First Prose Appearance:**') or
                line.startswith('**First Prose Establishment:**') or
                line.startswith('**First Prose Reference:**')) and PROSE_REF_RE.search(line):
            field_match = re.match(r'^(\*\*[^*]+:\*\*)', line)
            if field_match:
                out.append(field_match.group(1) + ' Not yet established -- to be defined in prose')
            else:
                out.append(line)
            continue

        if line.startswith('**Last Updated:**'):
            out.append('**Last Updated:** ' + TODAY)
            continue

        out.append(line)

    return '\n'.join(out)


def step5_clean_other_ledgers(story_memory_dir):
    print("\n[Step 5] Cleaning other ledger-* folders ...")
    skip_dirs = {
        'ledger-character-hero',
        'ledger-character-side',
    }
    for entry in sorted(os.listdir(story_memory_dir)):
        if not entry.startswith('ledger-'):
            continue
        if entry in skip_dirs:
            continue
        folder = os.path.join(story_memory_dir, entry)
        if not os.path.isdir(folder):
            continue
        for filename in sorted(os.listdir(folder)):
            if filename == '_index.md' or not filename.endswith('.md'):
                continue
            filepath = os.path.join(folder, filename)
            original = read_text(filepath)
            cleaned  = clean_general_ledger(original)
            if cleaned != original:
                write_text(filepath, cleaned)
                print("  cleaned: " + entry + "/" + filename)
    print("  Done.")


def main():
    repo_root = get_repo_root()
    novel_dir = get_novel_dir(repo_root)
    story_memory_dir = get_story_memory_dir(repo_root)

    print("=" * 60)
    print("  STARWARD SAGA -- Story Reset")
    print("  Repo root:    " + repo_root)
    print("  Novel dir:    " + novel_dir)
    print("  Story memory: " + story_memory_dir)
    print("=" * 60)

    step1_clear_novel(novel_dir)
    step2_clear_session_log(story_memory_dir)
    step3_clear_side_ledgers(story_memory_dir)
    step4_clean_hero_ledgers(story_memory_dir)
    step5_clean_other_ledgers(story_memory_dir)

    print("\n" + "=" * 60)
    print("  Reset complete.")
    print("  * projects/novel-starward-saga/ -- prose files deleted; icons preserved")
    print("  * story-memory/session-log/     -- all files deleted (README.md preserved)")
    print("  * ledger-character-side         -- character files deleted")
    print("  * ledger-character-hero         -- prose content cleared")
    print("  * other ledger-* files          -- prose event rows cleared")
    print("=" * 60)


if __name__ == "__main__":
    main()
