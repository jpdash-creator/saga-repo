# Guardrail: Authorized Scripts Only

**Source:** Part 1 Rule 10.5.13
**Applies to:** all 4 agents; anyone authoring or modifying `.claude/commands/*.md`

## The rule

Exactly four scripts are canon-authorized, and they live at `.claude/tools/`:

1. `prose_docx_creator.py` — writes one novel-typeset `.docx` per prose unit.
2. `prose_md_creator.py` — writes one `.md` companion per prose unit.
3. `reset_story.py` — the sole authorized story/ledger reset utility.
4. `saga_image_creator.py` — the sole authorized phase/section image generator (commands
   `/create-image-phase`, `/create-image-section`).

**Creating any additional or overlapping script is a Tier 0 Critical Violation** — this is
not a style preference, it's the highest severity the canon defines. If a task seems to need
a new script, that is itself a signal to stop and ask, not to write one.

## Hard rules

- `.docx`/`.md` file creation happens **only** through scripts 1 and 2 above — any other
  method of producing those files is provisionally non-compliant.
- These scripts are invoked by whichever command orchestrates the pipeline step that needs
  them (e.g. `/next-prose` at Gate 2, `/export-chapter`, `/create-image-phase`) — none of the
  4 specialist agents (Prose Maker, Outline Planner, Continuity Checker, Prose Scorer) has
  Bash access itself; script invocation is a mechanical step, not an agent decision.
- If one of the 4 scripts needs a bug fix (e.g. a path-resolution fix), that's a direct edit
  to the existing authorized file — never a new script "to replace it."

## Escalation

Any apparent need for new tooling gets raised explicitly before anything is written, per
Rule 10.5.13's own severity.
