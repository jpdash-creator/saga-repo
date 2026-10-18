---
description: Assemble a Chapter's per-Prose files into a single novel-grade Chapter .docx (and companion export), via the authorized script.
user-invocable: true
---

# `/export-chapter`

Corresponds to canon command `[EXPORT CHAPTER]` (C-24). Each prose unit's
per-Prose `.docx` is produced exclusively via `.claude/tools/prose_docx_creator.py`
(`write_prose_to_per_prose_docx()` / `write_prose_from_metadata()`)
(`.claude/guardrails/tools/guardrail-authorized-scripts-only.md`) — never a new/ad-hoc
per-Prose writing method.

## Sequence

1. Confirm the target Chapter's prose units are all Gate-2-complete (no pending
   `[CONFIRM WRITE]`), i.e. each already has its per-Prose `.docx` written by
   `prose_docx_creator.py`.
2. Assemble the Chapter document by concatenating the existing per-Prose `.docx`
   files under `projects/novel-starward-saga/.../chapter-NNN/`, in canonical
   Area/Prose order, at 6x9 novel-grade typeset (Rule 6.1.2 / 6.2.2).
   `prose_docx_creator.py` has no chapter-assembly/concatenation function or CLI
   entry point — this concatenation step is separate from that script.
3. Report the output path.

## Failure/abort

Do not export a Chapter with unresolved prose units — surface which ones are incomplete.
