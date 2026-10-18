# Guardrail: Authorized Scripts Only

**Source:** this guardrail (the tools layer has no skill file) · Canon v10.0
**Applies to:** all 4 agents; anyone authoring or modifying `.claude/commands/*.md`

## The rule

Exactly six scripts are canon-authorized, and they live at `.claude/tools/` (the fifth was added by author ruling on 2026-10-05, when the Part 42 Manual Ledger was approved; the sixth by author ruling on 2026-10-07, with `/chapter-builder`, which replaces `/export-chapter`; the rule's purpose, that no script writes Area output or ledger content, is unchanged):

1. `area_docx_creator.py` — writes one novel-typeset `.docx` per Area (`chapter-NNN/area-NN.docx`), joins the Chapter files
   written by script 6 into a Phase or novel `.docx` (`assemble`, used by `/compile-phase` and `/compile-novel`; it never
   joins Area files and never condenses) and reads a written file back for the Area Title Block (`check`, used by the
   Post-Write Audit).
2. `area_md_creator.py` — writes one `.md` companion per Area (`chapter-NNN/area-NN.md`), written as a coupled pair with the `.docx` at Gate 2.
3. `reset_story.py` — the sole authorized story/ledger reset utility.
4. `saga_image_creator.py` — the sole authorized phase/section image generator (commands
   `/create-image-phase`, `/create-image-section`).
5. `manual_ledger_query.py` — the sole authorized Manual Ledger lookup and validation tool (Part 42). It is
   **read-only**: it reads the CSV files under `.claude/story-memory/ledger-manuals/` and prints a manual, its moves, a
   character's kit or a Usable/Latent report by ID, and it validates the CSVs (unique IDs, unique move names, move
   counts against the Part 42 composition table, pointer integrity). It reads no move-name length or situation: the
   Move-Naming Law of Part 42 Rule 42.12.2.3 (Canon Amendment 2026-10-08) is read by the agents, not by the script,
   and the script is unchanged by that amendment. It never writes, edits, moves or deletes any
   story, ledger, spec or Area file, and it is never called to produce Area text. Any change that would make it write is
   a Tier 0 Critical Violation.

6. (Amended 2026-10-07: script 6 also writes whole-built Chapters. `/create-chapter` and `/revise-chapter` call it with
   `--mode whole`, alongside `/chapter-builder`'s condensed mode. It reads the Chapter Spec (read-only) for the Area
   blocks' size targets, `Budget stretch:` and Area block numbers, measures words per Area block, per band and for
   the Chapter total, checks the hidden `<!-- AREA NN -->` markers, and writes the `.md` with the markers and the
   `.docx` without. It refuses an out-of-band count, a missing or duplicated marker, a Chapter that has Area files
   and an existing file without `--overwrite`. No new script is added; the count stays six.)
   `chapter_builder.py` — writes one condensed Chapter as a coupled pair, `Chapter NNN - <Chapter Name>.md` and `.docx`, into the
   Novel-Part folder (`phase-N/section-N/part-N/`), used only by `/chapter-builder` after the author has confirmed the staged
   text. It writes no prose: it measures the text it is handed against the Chapter's Area files (50% to 60% of their characters,
   spaces counted), checks its structure (opening date line, `---` scene breaks, a date line only after a break) and typesets
   it with the helpers of scripts 1 and 2. It reads the Area `.md` files and never writes, edits, moves or deletes one.

**Creating any additional or overlapping script is a Tier 0 Critical Violation** — this is
not a style preference, it's the highest severity the canon defines. If a task seems to need
a new script, that is itself a signal to stop and ask, not to write one.

## Hard rules

- **Area and Chapter output files only.** The per-Area `.docx`/`.md` files under
  `projects/novel-starward-saga/` are created **only** through scripts 1 and 2 above, and the condensed Chapter files
  (`Chapter NNN - <Name>.docx`/`.md` in a Novel-Part folder, condensed or built whole) **only** through script 6 — any
  other method of producing an Area or Chapter output file is a Tier 0 Critical Violation: discard the
  file and remake it through the scripts. This
  rule governs novel *output* files and nothing else: files under `.claude/story-memory/` —
  ledger entity files, ledger `_index.md` registries, spec files of all three
  kinds (Section Spec, Novel-Part Spec and Chapter Spec; a spec is a planning file, not novel output) and the spec
  registry, session logs — are written with ordinary Write/Edit and are outside this
  rule. No script is created, or permitted, for writing a spec file of any kind: the spec
  commands (`/section-spec`, `/part-spec`, `/chapter-spec`) and the Gate 2 sync write them with
  Write/Edit.
- **Archiving prose is not writing it.** The archive move of `/rewind-to`, `/redraft-area`,
  `/redraft-chapter`, `/revise-area` and `/revise-chapter`, and the move back by `/restore-archive`, is a plain file move by the orchestrating command
  with the shell's move command: it creates no script and writes no prose file. The archive folder is
  `projects/novel-starward-saga/_archive/<date-time>/`, with `<date-time>` written
  `YYYY-MM-DD_HHMM`.
- These scripts are invoked by whichever command orchestrates the pipeline step that needs
  them (e.g. `/next-area` at Gate 2, `/chapter-builder`, `/create-chapter`, `/revise-chapter`, `/create-image-phase`) — none of the
  specialist agents (Area Maker, Chapter Editor, Outline Planner, Continuity Checker, Area Scorer) has
  Bash access itself; script invocation is a mechanical step, not an agent decision.
- If one of the 6 scripts needs a bug fix (e.g. a path-resolution fix), that's a direct edit
  to the existing authorized file — never a new script "to replace it."
- The condensed Chapter text that `/chapter-builder` hands script 6 is staged in `.claude/temp/` by the Area Maker (an input, not a script and not a Chapter file) and deleted after the write. The whole-Chapter text of `/create-chapter` is staged in `.claude/temp/` by the Area Maker (draft) and edited there by the Chapter Editor, which edits only that staged file (Amended 2026-10-07); it is deleted after the write.
- The writers are called from the command line (`write --text-file ...`; the exact call is in
  `/next-area` Step 5). The UTF-8 text file that carries the Area text is an input, not a script and
  not an Area file, so it is not an additional script; it is kept outside `projects/` and `.claude/`.
- **The date line is ordinary Area text** (Part 41, Area 5, The date line). It is one italic paragraph that
  opens the Area text, directly under the
  Area Title Block, and it travels in the same UTF-8 text file as the rest of the Area, so scripts 1 and 2 are
  handed it as they are handed any other paragraph, with no new argument. No script is created for it. `area_docx_creator.py` sets the
  date line as its own centred, smaller italic paragraph and puts the drop cap on the first narration
  paragraph after it (a direct edit of the authorized file, never a new script). Any further script change for the date line is raised to the author first.

## Escalation

Any apparent need for new tooling gets raised explicitly before anything is written, given the
Tier 0 severity set above.
