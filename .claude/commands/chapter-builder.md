---
description: Condense a finished Chapter's Areas into one Chapter .md and .docx (50% to 60% of the Areas' characters), staged in .claude/temp for the author's review and then written into the Novel-Part folder.
argument-hint: "<chapter number> [section number] [part number] [phase number], each left out defaults to the current position"
user-invocable: true
---

# `/chapter-builder`

Corresponds to canon command `[CHAPTER BUILDER]` (C-24). It **replaces `/export-chapter`**, which is retired. It reads one
Chapter's Chapter Spec and its written Areas, has the Area Maker condense them into a single Chapter text, and (after the
author confirms) writes the Chapter as a coupled `.md` and `.docx` pair into the Novel-Part folder:

```
projects/novel-starward-saga/phase-P/section-S/part-N/Chapter NNN - <Chapter Name>.md
projects/novel-starward-saga/phase-P/section-S/part-N/Chapter NNN - <Chapter Name>.docx
```

The per-Area files in `chapter-NNN/` stay the authoritative canon source and are never changed by this command.
`/compile-phase`, `/compile-phase-md`, `/compile-novel` and `/compile-novel-md` only join these Chapter files; they never
condense (author ruling 2026-10-07).

The file pair is written **only** by `.claude/tools/chapter_builder.py` (authorized script 6,
`.claude/guardrails/tools/guardrail-authorized-scripts-only.md`). No other method of producing a Chapter file is allowed.

## The condensed Chapter, what it must be

- **Length.** Between **50% and 60%** of the characters, spaces counted, of the Chapter's written Areas. Both sides count the
  narration paragraphs only (no title blocks, date lines, scene breaks or line breaks). The script measures it and refuses a
  text outside the band.
- **Essence kept.** Every beat, change, reveal, named thing, planted setup, turn, closing beat and the narrative voice of
  the Areas and of the Chapter Spec survive; nothing is added that the Areas and the Chapter Spec do not carry. The Area
  Maker cuts repeated sensory passes, secondary detail and connective sentences, not events, meaning or lines the Chapter
  Spec relies on. The Areas' own wording is kept wherever it can be.
- **Structure.** One Chapter text. Each Area's scene is separated from the next by a `---` line, and nothing else marks an Area
  boundary: no Area title, no reference code, no comment marker.
- **Dates.** The Chapter opens with its date line (`*Year 1247, Ilovany, Orvil, Day 1*`), once. While the Areas stay on the same
  date the line is not repeated. When a scene's date differs from the scene before it, that scene opens, directly after its
  `---`, with its own date line, and the `.docx` gives that scene the drop cap an Area opening has.
- **Plain English** and the form of the Area text: `*"..."*` dialogue, `***Named Move***`, the Part 29 and Part 36 standards
  the Areas were written to.

## Sequence

1. **Resolve the Chapter.** Defaults come from `/status`. Read the Chapter Spec (`.claude/story-memory/phase-section-part-chapter-area-specs/phase-P/section-S/part-N/chapter-NNN-spec.md`).
   **Refuse a whole-built Chapter:** if its Build mode is `whole` and its Area rows read
   `WRITTEN(P.S.N.CCC)` (the Chapter file already exists and no `area-NN` files do), stop and say: "Chapter
   P.S.N.CCC was built whole by /create-chapter; there are no Areas to condense. Use /revise-chapter to
   change it or /redraft-chapter to write it afresh." This command condenses written Areas only
   (the condensed mode of the script, not `--mode whole`).
   Every Area row must be terminal (`WRITTEN`, or `DROPPED` with a variance note) and its `area-NN.md` present in `chapter-NNN/`
   (never the `_archive` folder). If any is not, stop and list them (see Failure/abort). Read the Chapter name, the Novel-Part
   name, the Phase and Section names, and, for a Chapter that opens a Phase or a Section, the Title Page epigraph lines
   exactly as `/next-area` Step 5 sources them (the Part 30 Phase line, the Section Spec's Epigraph line; never written
   by an agent).
2. **Existing file test.** If `Chapter NNN - <Name>.md` or `.docx` already exists in the Novel-Part folder, say whether it is
   stale (a per-Area file of the Chapter is newer than it, or files of the Chapter were moved to the archive since, Part 2
   Rule 5.3.5) or current, and ask before replacing it; nothing is written before the answer. Staging in step 3 and 4 is
   free; only step 6 replaces a file.
3. **Condense (Area Maker).** Start the `area-maker` agent with: the Chapter Spec (whole), every written `area-NN.md`, the length
   band, the Dates rule and the Essence rule above, and the staging path
   `.claude/temp/Chapter NNN - <Chapter Name>.md`. It writes the Chapter text there (date line first, `---` between scenes, no
   headers) and nothing in `projects/`. It has no Bash access, so it does not run the script.
4. **Measure.** Run
   `python .claude/tools/chapter_builder.py measure --text-file ".claude/temp/Chapter NNN - <Name>.md" --phase P --section S --part N --chapter C`.
   Outside the band: send the figures back to the Area Maker to extend or trim, and measure again.
5. **Audit and author review.** The `continuity-checker` reads the staged text against the Chapter Spec and the Areas and
   reports lost or changed canon: a missing beat, name, planted setup or closing beat, a changed fact, an added fact, a date
   error. Show the author the staged `.md` path, the character figures, the audit result and a short list of what was cut.
   The author may correct the text, ask for another pass, or confirm. Nothing is written to the Novel-Part folder until the
   author confirms in words (never by silence).
6. **Write.** On confirmation run
   `python .claude/tools/chapter_builder.py write --text-file ".claude/temp/Chapter NNN - <Name>.md" --phase P --section S --part N --chapter C --chapter-name "<name>" --phase-name "<name>" --section-name "<name>" --novel-part-name "<name>" [--first-of-phase] [--first-of-section] [--phase-epigraph-file "<file>"] [--section-epigraph-file "<file>"] [--overwrite]`
   Give `--first-of-phase` or `--first-of-section` only when the Chapter opens the Phase or Section (the script then prints
   the Title Page), `--phase-epigraph-file` only with `--first-of-phase`, and `--overwrite` only after the author said yes at step 2.
   The script measures again, then writes the `.docx` and the `.md` together; it writes nothing if the text is out of band,
   breaks the structure (no opening date line, a stray date line, a scene break at an edge) or the files exist without `--overwrite`.
7. **Verify and clean.** Read the written `.md` and `.docx` back (`pandoc`-free: open the `.docx` with python-docx, or
   read the paragraph list): the Chapter Header Block, the opening date line, the right number of scene breaks and no
   `Area N —` title. Then delete the staged file in `.claude/temp/` (it is an input, not a Chapter file).
8. **Report** the two output paths, the character figures (condensed, Areas, ratio) and the list of dates shown.

## Rules

- A Chapter is built from **finished Areas only**; a Chapter with an unfinished Area is not condensed.
- The Chapter file never replaces an Area, never feeds a ledger and never changes a spec. Gate 2 and the ledgers still read the
  per-Area files.
- Rebuilding is always allowed (after `/revise-area` or a redraft); the old file is replaced only after the author confirms.
- The condensing is prose work, so it has the Area Maker's standards, not a script's. The script only counts, structures and
  typesets what it is handed.

## Failure/abort

Stop, write nothing and name the problem when: an Area of the Chapter is not terminal or its `.md` is missing; the staged
text stays out of band; the author has not confirmed; the Phase or Section image a Title Page needs is missing
(`/create-image-phase`, `/create-image-section`); or the script refuses (its message is reported as it is).
