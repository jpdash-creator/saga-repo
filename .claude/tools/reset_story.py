#!/usr/bin/env python3
"""
reset_story.py -- Starward Saga [HARD RESET] command.

Usage:
    python reset_story.py                    # [HARD RESET] -- the full wipe
    python reset_story.py --dry-run          # report every change, write nothing
    python reset_story.py --keep-specs \
                          --keep-agent-memory    # [RESET STORY] scope
    python reset_story.py --ledgers-only \
                          --keep-specs \
                          --keep-agent-memory    # [RESET LEDGERS] scope

The three reset commands differ only in which flags they pass:

    command           areas  session-log  specs  ledgers  agent-memory
    /hard-reset        yes       yes       yes     yes        yes
    /reset-story       yes       yes       no      yes        no
    /reset-ledgers     no        yes       no      yes        no

What this script does (in order):

  1. Clears the written Area files from projects/novel-starward-saga/ (every
     chapter-NNN/area-NN.md and area-NN.docx) and the exported files that hold their
     text (Chapter NNN - Name.docx / .md in the Novel-Part folder, phase-N-complete.docx / .md,
     starward-saga-complete.docx / .md), then prunes the directories those files
     emptied. Preserves phase-icon.png, phase-icon.svg, section-icon.png,
     section-icon.svg and any directory that still holds a preserved file.
  2. Deletes all files in .claude/story-memory/session-log/  (keeps README.md)
     -- see .claude/guardrails/ledger/guardrail-session-log-not-canon.md
  3. Deletes every story spec under
     .claude/story-memory/phase-section-part-chapter-area-specs/ -- all three kinds
     of the spec chain (Section Specs, Novel-Part Specs and Chapter Specs; everything in
     that folder except _index.md) -- and empties that folder's _index.md registry down to
     its headers. Every markdown table in _index.md is emptied, so that file must hold only
     the three registry tables (Section Specs, Novel-Part Specs, Chapter Specs) and no
     other table.
  4. Cleans EVERY .claude/story-memory/ledger-*/ entity file -- hero, side, and all
     others alike, under one shared cleaner:
       - Empties every Canon Events Log table to header + separator
       - Strips Area-event rows from any table
       - Resets First-Area / First-On-Page / Also-On-Page anchor fields
       - Drops ledger changelog footer lines that record an Area write
       - Strips clean parenthetical Area citations while KEEPING the descriptive
         value the citation annotated
       - Refreshes Last Updated
     Entity files are never deleted, and no descriptive value is ever discarded.
  5. Empties Area-reference rows from every ledger _index.md.
  6. Wipes .claude/agent-memory/ note files, leaving each agent's MEMORY.md at its
     header with no entries.
  7. Prints a REVIEW REQUIRED report of every line that still carries an Area
     reference the cleaner could not confidently resolve. Those lines are left
     untouched on purpose -- a regex must never mangle a descriptive sentence.
     Section 12 (Behavioral Evolution Log) rows are among them on purpose: a Permanent
     drift's prior value must first return to Section 11 from the superseded-behaviors
     table, and then the checker empties Section 12 (Part 39 Rule 39.41.6.2), so this
     script never empties Section 12 by itself.

NOT touched:
  - .claude/tools/  (the folder this script lives in)
  - .claude/skills/, .claude/guardrails/, .claude/canon-manifest/, .claude/agents/,
    .claude/commands/, .claude/docs/  (the canon structure itself)
  - Descriptive content in any ledger entity file
  - phase-icon.png / phase-icon.svg / section-icon.png / section-icon.svg

Specs are deleted by the hard reset only (Part 38 Rule 7.1.2); every other reset keeps them
(--keep-specs). With --keep-specs none of the three spec kinds is touched, and the status
rollback of every kind (a COMPLETED spec returns to CONFIRMED when a written Area is
removed) is owed by the invoking command, not done here (Part 38 Rules 7.2.1 and 9.8.1).
Side-character ledger files are cleaned rather than deleted, so the ledger layer keeps
describing every entity it knows while holding no record of the Areas that established it.
Agent memory is wiped, because notes about Areas that no longer exist are stale state, not
knowledge.

Directory layout assumption: this script lives at REPO_ROOT/.claude/tools/reset_story.py.
story-memory lives at REPO_ROOT/.claude/story-memory/ and the novel output lives at
REPO_ROOT/projects/novel-starward-saga/ -- these are NOT siblings of each other or of this
script, so the repo root is resolved explicitly below rather than by counting parents.
"""

import os
import re
import sys
import shutil
from datetime import date

TODAY = date.today().isoformat()

_VALID_FLAGS = {"--dry-run", "--keep-specs", "--keep-agent-memory", "--ledgers-only"}
_unknown = [a for a in sys.argv[1:] if a not in _VALID_FLAGS]
if _unknown:
    sys.exit("reset_story.py: unknown flag(s): " + ", ".join(_unknown) +
             "\nValid flags: " + ", ".join(sorted(_VALID_FLAGS)))

DRY_RUN = "--dry-run" in sys.argv
KEEP_SPECS = "--keep-specs" in sys.argv
KEEP_AGENT_MEMORY = "--keep-agent-memory" in sys.argv
LEDGERS_ONLY = "--ledgers-only" in sys.argv

# Files always preserved by the Step 1 Area sweep.
PRESERVED_FILENAMES = {
    "phase-icon.png",
    "phase-icon.svg",
    "section-icon.png",
    "section-icon.svg",
}

AREA_EXTENSIONS = {".md", ".docx"}

# A written Area file: chapter-NNN/area-NN.md or area-NN.docx (two-digit Area number, no Area subfolder).
AREA_FILE_RE = re.compile(r'^area-\d{2}\.(?:md|docx)$')
CHAPTER_DIR_RE = re.compile(r'^chapter-\d{3}$')

# Exported chapter, phase and novel files (Part 2 Rule 5.2.6). They hold the full text of the Areas that a
# reset discards, so Step 1 deletes them with it (Part 2 Rule 5.3.5).
EXPORT_NAME_RE = re.compile(
    r'^(?:chapter-\d{3}\.(?:md|docx)|Chapter \d{3}(?: - .+)?\.(?:md|docx)|phase-\d+-complete\.[A-Za-z0-9]+|starward-saga-complete\.[A-Za-z0-9]+)$')

# An Area reference:  1.1.1.001.01  (Phase.Section.Novel-Part.Chapter.Area)
AREA_REF = r'\d+\.\d+\.\d+\.\d{3}(?:\.\d{1,2})?(?!\d)'   # five parts; or Chapter-only (four parts) for whole-built Chapters
AREA_REF_RE = re.compile(AREA_REF)

# An Area-event table row, in either recorded style:
#   | Area 1.1.1.001.01 | ...        (hero style)
#   | 1.1.1.001.01 | ...              (general style)
AREA_ROW_RE = re.compile(r'^\s*\|\s*(?:Area\s+)?' + AREA_REF)

# A prior [RESET STORY] canon-update row.
RESET_ROW_RE = re.compile(r'^\s*\|\s*Canon Update.*\[RESET STORY\]')

# Any markdown table row (used to find the extent of an events table).
TABLE_ROW_RE = re.compile(r'^\s*\|')
TABLE_SEP_RE = re.compile(r'^\s*\|[\s:|-]+\|\s*$')

# Section heading that opens an events log, in every recorded spelling.
EVENTS_HEADING_RE = re.compile(
    r'^#{1,6}\s.*(Canon Events? Log|Events? Log|Event Log)', re.IGNORECASE)
ANY_HEADING_RE = re.compile(r'^#{1,6}\s')

# Anchor fields whose entire VALUE is an Area citation -- these reset to a placeholder.
ANCHOR_FIELDS = (
    'First Area Appearance',
    'First Area Establishment',
    'First Area Reference',
    'First On-Page Appearance',
    'Also On-Page',
)
ANCHOR_FIELD_RE = re.compile(
    r'^(\*\*(?:' + '|'.join(re.escape(f) for f in ANCHOR_FIELDS) + r')[^:]*:\*\*)')

# Ledger changelog / provenance footer lines. Every recorded form opens with a lone
# asterisk and announces a version or a Gate, for example:
#   *valia.md — v1.3 (Post-Write Ledger Update, Gate 2 post-Area ...)
#   *Version note (v1.29, Post-Write Ledger Update, Gate 2 post-Area ...)
#   *Gate 2 update: ...
# All of them record an Area write rather than describing the entity, so a line that
# matches one of these AND carries an Area reference is dropped.
CHANGELOG_RES = [
    re.compile(r'^\*[A-Za-z0-9._ -]+?\s*[-–—]+\s*v\d', re.IGNORECASE),
    re.compile(r'^\*Version note\s*\(', re.IGNORECASE),
    re.compile(r'^\*Gate \d+ update\s*\(', re.IGNORECASE),
    re.compile(r'^\*(?:Post-Write )?Ledger Update\b', re.IGNORECASE),
    re.compile(r'^Amendment revision of Area\b', re.IGNORECASE),
]

# Inline anchor markers that label a descriptive passage with the Area that produced
# it: "**Extended 1.1.1.002.02:** the quarter is also ..." The label goes; the
# description it introduces stays.
INLINE_ANCHOR_RES = [
    re.compile(r'\*\*(?:Extended|Established|Added|Confirmed|Re-established|Enriched)\s+'
               + AREA_REF + r'\s*[:.]\*\*\s*', re.IGNORECASE),
    re.compile(r'\*\*(?:Extended|Established|Added|Confirmed|Re-established|Enriched)\s+'
               + AREA_REF + r'\s*[-–—]\s*', re.IGNORECASE),
    re.compile(r'\((?:Gate \d+,?\s*)?(?:post-)?Area\s*' + AREA_REF + r'[^()]*\)\s*',
               re.IGNORECASE),
]

# Parenthetical citations safe to strip whole, keeping the sentence around them.
CITATION_PATTERNS = [
    # (Ref: 1.1.1.002.02)  /  (Area 1, Ref: 1.1.1.002.02)
    re.compile(r'\s*\((?:Area[^()]*,\s*)?Ref:\s*' + AREA_REF + r'[^()]*\)'),
    # (established in Area 1.1.1.002.02)  /  (established Area ...)
    re.compile(r'\s*\((?:first\s+)?(?:established|introduced|registered|debut(?:ed)?)'
               r'[^()]*' + AREA_REF + r'[^()]*\)', re.IGNORECASE),
    # (Area 1.1.1.002.02)
    re.compile(r'\s*\(Area\s+' + AREA_REF + r'[^()]*\)'),
    # trailing "; established in Area 1.1.1.002.02"
    re.compile(r';\s*(?:first\s+)?(?:established|introduced|registered)'
               r'[^;.]*' + AREA_REF + r'[^;.]*', re.IGNORECASE),
]

report_lines = []


def note(msg):
    print(msg)


def flag(path, lineno, text):
    report_lines.append((path, lineno, text.rstrip()))


def read_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def write_text(path, text):
    if DRY_RUN:
        return
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def get_repo_root():
    """
    REPO_ROOT/.claude/tools/reset_story.py -> three levels up is REPO_ROOT.
    Explicit by design -- if this script moves, update the joins below directly
    rather than re-counting parent folders.
    """
    tools_dir = os.path.dirname(os.path.abspath(__file__))
    claude_dir = os.path.dirname(tools_dir)
    return os.path.dirname(claude_dir)


def novel_dir(root):
    return os.path.join(root, "projects", "novel-starward-saga")


def story_memory_dir(root):
    return os.path.join(root, ".claude", "story-memory")


def agent_memory_dir(root):
    return os.path.join(root, ".claude", "agent-memory")


def specs_dir(root):
    return os.path.join(story_memory_dir(root),
                        "phase-section-part-chapter-area-specs")


def remove_dir(path):
    """
    Remove a directory, tolerating the Windows/OneDrive case where the files inside
    delete cleanly but the directory handle is briefly held and rmdir returns
    PermissionError. Files are what matter; a directory that survives is reported,
    not raised, so one locked folder never aborts the whole reset.
    """
    if DRY_RUN:
        return True
    for _attempt in range(3):
        shutil.rmtree(path, ignore_errors=True)
        if not os.path.isdir(path):
            return True
    # Directory still present: strip it to empty so nothing stale is left inside.
    for dirpath, _dirnames, filenames in os.walk(path, topdown=False):
        for fname in filenames:
            try:
                os.remove(os.path.join(dirpath, fname))
            except OSError:
                pass
        try:
            os.rmdir(dirpath)
        except OSError:
            pass
    if os.path.isdir(path):
        note("  NOTE: could not remove directory (emptied instead): " + path)
        return False
    return True


def clear_dir_contents(path, keep=None):
    keep = set(keep or [])
    deleted = []
    if not os.path.isdir(path):
        return deleted
    for item in sorted(os.listdir(path)):
        if item in keep:
            continue
        full = os.path.join(path, item)
        if not DRY_RUN:
            if os.path.isdir(full):
                remove_dir(full)
            else:
                try:
                    os.remove(full)
                except OSError as exc:
                    note("  NOTE: could not delete " + full + " (" + str(exc) + ")")
                    continue
        deleted.append(item)
    return deleted


# ---------------------------------------------------------------- step 1

def step1_clear_areas(nd):
    note("\n[Step 1] Clearing written Areas from projects/novel-starward-saga/ ...")
    if not os.path.isdir(nd):
        note("  (projects/novel-starward-saga/ not found -- skipping)")
        return

    deleted = 0
    exports = 0
    for dirpath, _dirnames, filenames in os.walk(nd):
        in_chapter = bool(CHAPTER_DIR_RE.match(os.path.basename(dirpath)))
        for fname in filenames:
            if fname in PRESERVED_FILENAMES:
                continue
            is_area = in_chapter and bool(AREA_FILE_RE.match(fname))
            is_export = bool(EXPORT_NAME_RE.match(fname))
            if is_area or is_export:
                full = os.path.join(dirpath, fname)
                if not DRY_RUN:
                    os.remove(full)
                note("  deleted: " + os.path.relpath(full, nd) + ("  (exported file)" if is_export else ""))
                if is_export:
                    exports += 1
                else:
                    deleted += 1
    if deleted == 0 and exports == 0:
        note("  (no Area or exported files found)")

    # Prune directories the sweep emptied. Bottom-up so parents see empty children.
    pruned = 0
    for dirpath, _dirnames, _filenames in os.walk(nd, topdown=False):
        if os.path.abspath(dirpath) == os.path.abspath(nd):
            continue
        if DRY_RUN:
            continue
        try:
            if os.listdir(dirpath):
                continue
        except OSError:
            continue
        for _attempt in range(3):
            try:
                os.rmdir(dirpath)
                break
            except OSError:
                continue
        if not os.path.isdir(dirpath):
            note("  pruned empty dir: " + os.path.relpath(dirpath, nd))
            pruned += 1
        else:
            note("  NOTE: empty dir could not be pruned (left in place): "
                 + os.path.relpath(dirpath, nd))
    note("  Done. (%d Area files, %d exported chapter/phase/novel files, %d empty folders)"
         % (deleted, exports, pruned))


# ---------------------------------------------------------------- step 2

def step2_clear_session_log(smd):
    note("\n[Step 2] Clearing story-memory/session-log/ ...")
    deleted = clear_dir_contents(os.path.join(smd, "session-log"),
                                 keep={"README.md"})
    for d in deleted:
        note("  deleted: " + d)
    if not deleted:
        note("  (already empty)")
    note("  Done.")


# ---------------------------------------------------------------- step 3

def step3_clear_specs(root):
    # This sweeps every spec file of all three kinds (Section Specs,
    # Novel-Part Specs, Chapter Specs) because it removes everything in the specs folder
    # except _index.md. empty_all_tables() below empties EVERY table in _index.md, so that
    # registry may hold only its three registry tables.
    note("\n[Step 3] Clearing story specs (Section, Novel-Part and Chapter) ...")
    sd = specs_dir(root)
    if not os.path.isdir(sd):
        note("  (specs folder not found -- skipping)")
        return
    deleted = clear_dir_contents(sd, keep={"_index.md"})
    for d in deleted:
        note("  deleted: " + d)
    if not deleted:
        note("  (no spec files present)")
    # (deleted lists the top-level items swept, the phase-N folders and anything else
    # that sits beside _index.md, so a dry run shows folders, not each spec file.)

    index = os.path.join(sd, "_index.md")
    if os.path.isfile(index):
        original = read_text(index)
        cleaned = empty_all_tables(original)
        cleaned = refresh_last_updated(cleaned)
        if cleaned != original:
            write_text(index, cleaned)
            note("  emptied registry rows: _index.md")
    note("  Done.")


# ---------------------------------------------------------------- cleaners

def empty_all_tables(text):
    """Drop every data row from every markdown table, keeping header + separator."""
    lines = text.split('\n')
    out = []
    i = 0
    while i < len(lines):
        if TABLE_ROW_RE.match(lines[i]):
            block = []
            while i < len(lines) and TABLE_ROW_RE.match(lines[i]):
                block.append(lines[i])
                i += 1
            # Keep the header row and the separator row; drop the data rows.
            if len(block) >= 2 and TABLE_SEP_RE.match(block[1]):
                out.extend(block[:2])
            else:
                out.extend(block)
            continue
        out.append(lines[i])
        i += 1
    return '\n'.join(out)


def empty_events_logs(lines):
    """
    Empty every Canon Events Log table to header + separator, leaving all other
    tables in the file alone.
    """
    out = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        out.append(line)
        if not EVENTS_HEADING_RE.match(line):
            i += 1
            continue
        # Inside an events-log section: copy through to the next heading, but
        # keep only the first two rows of any table encountered.
        i += 1
        while i < n and not ANY_HEADING_RE.match(lines[i]):
            if TABLE_ROW_RE.match(lines[i]):
                block = []
                while i < n and TABLE_ROW_RE.match(lines[i]):
                    block.append(lines[i])
                    i += 1
                if len(block) >= 2 and TABLE_SEP_RE.match(block[1]):
                    out.extend(block[:2])
                else:
                    out.extend(block)
                continue
            out.append(lines[i])
            i += 1
    return out


def strip_citations(line):
    """Remove parenthetical Area citations, keeping the sentence intact."""
    cleaned = line
    for pat in INLINE_ANCHOR_RES:
        cleaned = pat.sub('', cleaned)
    for pat in CITATION_PATTERNS:
        cleaned = pat.sub('', cleaned)
    # Tidy the punctuation a removed parenthetical can leave behind.
    cleaned = re.sub(r'\s+([,.;:])', r'\1', cleaned)
    cleaned = re.sub(r'\(\s*\)', '', cleaned)
    cleaned = re.sub(r'[ \t]{2,}', ' ', cleaned)
    return cleaned.rstrip()


def refresh_last_updated(text):
    return re.sub(r'^\*\*Last Updated:\*\*.*$',
                  '**Last Updated:** ' + TODAY,
                  text, flags=re.MULTILINE)


# A registry table's "First Area Appearance" column. Its cell can hold an Area title with no
# reference code, so the reference-code rules never see it; after a reset it goes back to the
# placeholder.
FIRST_AREA_HEADER_RE = re.compile(r'^First Area Appearance\b', re.IGNORECASE)
FIRST_AREA_PLACEHOLDER = 'Not yet established'


def reset_first_area_cell(line, table):
    """
    Set the First Area Appearance cell of a registry table row back to the placeholder.
    `table` is the state of the table being read: None outside a table, else (index of its
    First Area Appearance column or -1, cell count), taken from its header row. Returns
    (line, table). A cell that already reads "Not yet established..." is left as it is, and a
    row whose cell count differs from the header's is left alone.
    """
    if not TABLE_ROW_RE.match(line):
        return line, None
    stripped = line.strip()
    if not stripped.endswith('|'):
        return line, table
    cells = stripped[1:-1].split('|')
    if table is None:                                    # the header row of a new table
        column = next((i for i, c in enumerate(cells) if FIRST_AREA_HEADER_RE.match(c.strip())), -1)
        return line, (column, len(cells))
    column, count = table
    if column < 0 or len(cells) != count or TABLE_SEP_RE.match(line):
        return line, table
    if cells[column].strip().lower().startswith(FIRST_AREA_PLACEHOLDER.lower()):
        return line, table
    cells[column] = ' ' + FIRST_AREA_PLACEHOLDER + ' '
    lead = line[:len(line) - len(line.lstrip())]
    trail = line[len(line.rstrip()):]
    return lead + '|' + '|'.join(cells) + '|' + trail, table


def clean_ledger(text, relpath):
    """
    One cleaner for every ledger entity file. Hero and side-character files share exactly one cleaner.
    """
    lines = empty_events_logs(text.split('\n'))
    out = []
    table = None     # the table being read: (index of its First Area Appearance column or -1, cell count)

    for idx, line in enumerate(lines, start=1):
        # A registry row's First Area Appearance cell goes back to the placeholder.
        line, table = reset_first_area_cell(line, table)

        # Area-event rows and prior reset rows, wherever they appear.
        if AREA_ROW_RE.match(line) or RESET_ROW_RE.match(line):
            continue

        # Ledger changelog / provenance footers recording an Area write.
        if AREA_REF_RE.search(line) and any(p.match(line) for p in CHANGELOG_RES):
            continue

        # Last Updated is refreshed rather than examined for citations.
        if line.startswith('**Last Updated:**'):
            out.append('**Last Updated:** ' + TODAY)
            continue

        if not AREA_REF_RE.search(line):
            out.append(line)
            continue

        # Anchor fields: the value IS the citation, so the field resets.
        m = ANCHOR_FIELD_RE.match(line)
        if m:
            out.append(m.group(1) +
                       ' Not yet established — to be defined in prose')
            continue

        # Everything else: try to strip the citation and keep the value.
        stripped = strip_citations(line)
        if not AREA_REF_RE.search(stripped):
            out.append(stripped)
            continue

        # Could not resolve confidently -- keep the line and report it.
        out.append(line)
        flag(relpath, idx, line)

    return refresh_last_updated('\n'.join(out))


# ---------------------------------------------------------------- steps 4-5

def step4_clean_ledgers(smd):
    note("\n[Step 4] Cleaning every ledger-*/ entity file ...")
    touched = 0
    for entry in sorted(os.listdir(smd)):
        if not entry.startswith('ledger-'):
            continue
        folder = os.path.join(smd, entry)
        if not os.path.isdir(folder):
            continue
        for filename in sorted(os.listdir(folder)):
            if filename == '_index.md' or not filename.endswith('.md'):
                continue
            path = os.path.join(folder, filename)
            rel = entry + '/' + filename
            original = read_text(path)
            cleaned = clean_ledger(original, rel)
            if cleaned != original:
                write_text(path, cleaned)
                note("  cleaned: " + rel)
                touched += 1
    note("  Done. (%d files)" % touched)


def step5_clean_indexes(smd):
    note("\n[Step 5] Clearing Area rows from ledger _index.md files ...")
    touched = 0
    for entry in sorted(os.listdir(smd)):
        if not entry.startswith('ledger-'):
            continue
        path = os.path.join(smd, entry, '_index.md')
        if not os.path.isfile(path):
            continue
        original = read_text(path)
        cleaned = clean_ledger(original, entry + '/_index.md')
        if cleaned != original:
            write_text(path, cleaned)
            note("  cleaned: " + entry + "/_index.md")
            touched += 1
    note("  Done. (%d files)" % touched)


def step5b_reset_manual_ledger(smd):
    """
    Part 42 Manual Ledger: restore every `first_area` cell of the manual and move CSVs
    (manuals/, moves/, personal/, cultivation/manuals/, cultivation/moves/) to 'Not yet established'. Nothing else in the CSVs
    is touched, and no file is deleted. The script's other steps never read these files.
    """
    import csv
    import io
    note("\n[Step 5b] Resetting first_area cells in ledger-manuals/ CSV files ...")
    root = os.path.join(smd, 'ledger-manuals')
    if not os.path.isdir(root):
        note("  ledger-manuals/ not present. Skipped.")
        return
    touched = 0
    cells = 0
    for sub in ('manuals', 'moves', 'personal',
                os.path.join('cultivation', 'manuals'), os.path.join('cultivation', 'moves')):
        for dirpath, _dirs, files in os.walk(os.path.join(root, sub)):
            for filename in sorted(files):
                if not filename.endswith('.csv'):
                    continue
                path = os.path.join(dirpath, filename)
                with open(path, 'r', encoding='utf-8', newline='') as f:
                    rows = list(csv.reader(f))
                if not rows or 'first_area' not in rows[0]:
                    continue
                col = rows[0].index('first_area')
                changed = 0
                for row in rows[1:]:
                    if len(row) > col and row[col] != 'Not yet established':
                        row[col] = 'Not yet established'
                        changed += 1
                if changed:
                    buf = io.StringIO()
                    csv.writer(buf, lineterminator='\n').writerows(rows)
                    write_text(path, buf.getvalue())
                    touched += 1
                    cells += changed
    note("  Done. (%d cells in %d files)" % (cells, touched))


# ---------------------------------------------------------------- step 6

def step6_wipe_agent_memory(amd):
    note("\n[Step 6] Wiping .claude/agent-memory/ note files ...")
    if not os.path.isdir(amd):
        note("  (agent-memory not found -- skipping)")
        return
    for agent in sorted(os.listdir(amd)):
        folder = os.path.join(amd, agent)
        if not os.path.isdir(folder):
            continue
        for filename in sorted(os.listdir(folder)):
            if filename == 'MEMORY.md':
                continue
            if not DRY_RUN:
                os.remove(os.path.join(folder, filename))
            note("  deleted: " + agent + "/" + filename)

        index = os.path.join(folder, 'MEMORY.md')
        if not os.path.isfile(index):
            continue
        kept = []
        for line in read_text(index).split('\n'):
            if line.startswith('- [') or line.startswith('## '):
                break
            kept.append(line)
        while kept and not kept[-1].strip():
            kept.pop()
        kept.append('')
        kept.append('*(No entries. Notes are written back as the agent learns '
                    'something worth keeping.)*')
        kept.append('')
        write_text(index, '\n'.join(kept))
        note("  emptied: " + agent + "/MEMORY.md")
    note("  Done.")


# ---------------------------------------------------------------- main

def main():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")   # a printed title or path never crashes the run
        except (AttributeError, ValueError):
            pass
    root = get_repo_root()

    print("=" * 68)
    print("  STARWARD SAGA -- [HARD RESET]" + ("  (DRY RUN)" if DRY_RUN else ""))
    print("  Repo root:    " + root)
    print("  Novel dir:    " + novel_dir(root))
    print("  Story memory: " + story_memory_dir(root))
    print("=" * 68)

    if LEDGERS_ONLY:
        note("\n[Step 1] SKIPPED (--ledgers-only): written Areas left untouched.")
    else:
        step1_clear_areas(novel_dir(root))

    step2_clear_session_log(story_memory_dir(root))

    if KEEP_SPECS:
        note("\n[Step 3] SKIPPED (--keep-specs): Section, Novel-Part and Chapter specs left on disk."
             "\n         Their statuses (per-unit rows, COMPLETED back to CONFIRMED) must be"
             "\n         rolled back by the invoking command's continuity-checker pass"
             "\n         (Part 38 Rules 7.2.1 and 9.8.1).")
    else:
        step3_clear_specs(root)

    step4_clean_ledgers(story_memory_dir(root))
    step5_clean_indexes(story_memory_dir(root))
    step5b_reset_manual_ledger(story_memory_dir(root))

    if KEEP_AGENT_MEMORY:
        note("\n[Step 6] SKIPPED (--keep-agent-memory): agent notes left in place.")
    else:
        step6_wipe_agent_memory(agent_memory_dir(root))

    print("\n" + "=" * 68)
    print("  Reset complete." + ("  (DRY RUN -- nothing written)" if DRY_RUN else ""))
    if LEDGERS_ONLY:
        print("  * written Areas NOT touched (--ledgers-only)")
    else:
        print("  * Area files and exported chapter, phase and novel files deleted; icons and their folders preserved")
    print("  * session-log cleared (README.md preserved)")
    if KEEP_SPECS:
        print("  * Section, Novel-Part and Chapter specs KEPT (--keep-specs); status rollback owed by caller")
    else:
        print("  * Section, Novel-Part and Chapter specs deleted; specs _index.md emptied")
    print("  * every ledger entity file cleaned, none deleted")
    print("  * ledger _index.md Area rows cleared")
    print("  * ledger-manuals CSV first_area cells restored to 'Not yet established'")
    if KEEP_AGENT_MEMORY:
        print("  * agent-memory KEPT (--keep-agent-memory)")
    else:
        print("  * agent-memory notes wiped to MEMORY.md headers")
    print("=" * 68)

    if report_lines:
        print("\n" + "!" * 68)
        print("  REVIEW REQUIRED -- %d line(s) still carry an Area reference the"
              % len(report_lines))
        print("  cleaner would not resolve on its own. They were left UNTOUCHED.")
        print("!" * 68)
        current = None
        for path, lineno, text in report_lines:
            if path != current:
                print("\n--- " + path)
                current = path
            print("  L%-5d %s" % (lineno, text[:400]))
        print("\n  (%d line(s) flagged.)" % len(report_lines))
    else:
        print("\n  No unresolved Area references. Nothing needs review.")


if __name__ == "__main__":
    main()
