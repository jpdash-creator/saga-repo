---
name: revision-tasks-need-full-draft-text
description: Draft prose only exists in the invoking agent's context until Gate 2 writes the file — a revision task must include the full draft text inline or it cannot be done
metadata:
  type: project
---

A prose draft does not persist anywhere on disk between prose-maker invocations. The
`.docx`/`.md` file is only created at Gate 2 by the authorized scripts
(`.claude/tools/prose_docx_creator.py`, `.claude/tools/prose_md_creator.py`) after the
Gate 1 audit passes. `.claude/story-memory/` holds ledgers, not prose. Each prose-maker
invocation is a fresh context.

**Why:** A Gate 1 revision task for Prose 1 arrived asking for "the COMPLETE corrected text"
of a draft that existed only in the orchestrating agent's context. Nothing on disk held it,
so the revision was unexecutable as briefed.

**How to apply:** If asked to revise a pre-Gate-2 draft, first confirm the full draft text
is present in the task prompt. If it is not, stop and ask the invoking agent to paste it
verbatim — do NOT reconstruct or re-draft from the outline and call it a revision. A
regenerated scene silently changes wording, beats, and word count that were already
approved, which is a far worse failure than reporting the missing input. Post-Gate-2
revisions are different: those files can be read from the book output directory.

See also [[dialogue-italics-gate1-fail]], [[age-arithmetic-must-be-computed]].
