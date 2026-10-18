---
name: canon-file-locations
description: Where the canon skills, guardrails and ledgers actually live on disk — the manifest's own output_path/source_file fields point at things that resolve differently than they read.
metadata:
  type: reference
---

- **Skills:** `.claude/skills/ssc-<domain>-p<NN>-<slug>/SKILL.md` (~614 files). Glob with
  `.claude/skills/**/SKILL.md` — a pattern like `.claude/skills/ssc-narration-p30-*`
  returns nothing because the skills are directories, not files.
- **Manifest:** `.claude/canon-manifest/skill-index.json` is ~1.4 MB and will not read
  whole. Use the per-skill stubs in `.claude/canon-manifest/_items/<skill-id>.json`
  instead, or Grep the big file.
- The `source_file` field in those stubs (e.g. `Part_30_Narrative_Theme_Novel_Macro_Story_Law.md`)
  refers to a **pre-migration source that is not in this repo** — do not go looking for the
  raw Part markdown. The migrated `SKILL.md` carries the verbatim rule text.
- **Guardrails:** `.claude/guardrails/` with `_index.md` as the entry table.
- **Ledgers:** `.claude/story-memory/ledger-*/` — each has an `_index.md` plus one file per
  entity. Prefer entity files over `_index.md` for current state; see
  [[ledger-reset-contamination]].
- **Novel output:** `projects/novel-starward-saga/phase-<N>/` — currently holds only phase
  icon assets; no prose on disk.
