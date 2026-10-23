# Story Specification Registry — Master Index

**Governing law:** Part 38 — Story Specification Law. Primary skill: `spec-story-specification-law`. Guardrail:
`.claude/guardrails/ledger/guardrail-story-spec-law.md`.

**Index Version:** **10.0** | **Last Updated:** 2026-10-22 | **Canon v10.0**

## What this folder is

Three kinds of spec file, in a tree mirroring the novel output tree. Together they are the **spec chain**
(Part 38 Rule 38.9), and each one is the author-approved plan for its own level:

```
phase-N/
└── section-N/
    ├── section-N-spec.md          the Section Spec        (ref P.S, for example 1.2)
    └── part-N/
        ├── part-N-spec.md         the Novel-Part Spec     (ref P.S.P, for example 1.2.3)
        └── chapter-NNN-spec.md    the Chapter Spec        (ref P.S.P.CCC, for example 1.2.3.004)
```

- A **Section Spec** plans one Section from what Part 30 expects of it: its Novel-Parts and, at a high level,
  their Chapters.
- A **Novel-Part Spec** (command `/part-spec`) lists every Chapter of one Novel-Part in depth.
- A **Chapter Spec** is the plan of one Chapter: its Areas, and for each Area its block (title, pacing, size
  target of 1,600, 1,800 or 2,000 words, opening and closing type, scene anchors, whether the scene continues in
  the next Area, thread, viewpoint, time, story link, setups and payoffs, and the rest). The Area is the written
  unit.

Every spec reads clean: its body carries no inline settlement tags, and every settled, open, deferred,
skipped, provenance, variance and audit note is gathered in a final section, **Audit and Settlement Notes**, at
the end of the file (Part 38 Rule 38.14).

A Chapter Spec can only exist under a confirmed Novel-Part Spec, and a Novel-Part Spec only under a confirmed
Section Spec (Part 38 Rule 38.9).

**Authority (Part 38 Rule 38.3):** a spec is a valid decision input for planning and
structural decisions — items the author explicitly settled at spec-build are settled for
DCG Rule 19.4 purposes. A spec is NEVER a source of established canon facts: names,
descriptions, and events in a spec are proposals until a Gate 1 delivery that is confirmed and
written, or a Gate 2 write (Establishment Rule / Rule 18.4.4; Area 20.3 for in-world names). On conflict: Locked Canon > ledger (established) >
spec chain (intent) > session-log (never an input). Ledger supersedes spec. Inside the chain, the higher spec
says what a level must do and the lower spec governs its own detail (Part 38 Rule 38.12).

**This folder is NOT a ledger folder.** Part 37 does not govern it; `force-ledger-audit`
and ledger tooling skip it.

**Reset behaviour (Part 38 Rules 7.1.1–7.1.2 and Rule 9.8.1).** All three kinds of spec survive every
destructive and rewind command: `[REWIND TO]`, `[RESET STORY]`, `[RESET CHAPTER]`, `[RESET PHASE]`,
`[REDRAFT AREA]` and `[REDRAFT CHAPTER]`. A Chapter Spec has its per-Area statuses rolled back. When written
Areas are removed, a COMPLETED Chapter Spec returns to CONFIRMED, and a COMPLETED Novel-Part Spec or Section
Spec returns to CONFIRMED as soon as any spec under it is no longer COMPLETED; the completion text is kept.
The sole exception is `[HARD RESET]` (C-1), which deletes every spec file of all three kinds and
empties this registry to its headers.

## Registry

One registry, three tables, one for each kind of spec. The tables hold registry rows only: the reset script
empties every table in this file, so nothing else, such as a legend or a vocabulary list, may be written as a
table here. Notes on the columns follow, in words.

**Column notes.** *Spec File* is the path of the spec file below this folder. *Ref* is the spec's reference:
`P.S` for a Section Spec (phase, section; for example `1.2`), `P.S.P` for a Novel-Part Spec (phase, section,
novel-part; for example `1.2.3`), `P.S.P.CCC` for a Chapter Spec (phase, section, novel-part, chapter; for
example `1.1.1.001`). *Status* is one of `DRAFT`, `CONFIRMED`, `AMENDED-PENDING-RECONFIRM`, `COMPLETED`,
`RETIRED` (Part 38 Rule 2.2.1); this is the status of the spec, not the status of an Area inside a Chapter Spec
(`PLANNED`, `DRAFTED`, `WRITTEN`, `DROPPED`). *Spec Ver* is the spec version. *Last Updated* is the date of the
last write (`YYYY-MM-DD`). *Coverage* depends on the kind of spec. For a Section Spec it counts Novel-Parts
completed over Novel-Parts planned, then Chapters completed over Chapters planned. For a Novel-Part Spec it
counts Chapters completed over Chapters planned. For a Chapter Spec it counts Areas written over Areas planned,
for example `4/9 Areas`. For the Section and Novel-Part kinds the "planned" figures are simply the lists as they
stand in the spec; they are read as information, not as a target (Part 2 Rules 9.3.1 and 9.13.1–9.13.3). The
Coverage cell of a Section row or a Novel-Part row is refreshed in three cases only: when that spec is confirmed,
at any completion write step (a child's completion included, so a Chapter's completion refreshes the Coverage of
its Novel-Part row and its Section row), and at a reset or rewind rollback; never at Gate 2 (Part 38 Rules 1.2.2,
10.1.2 and 11.1.2). Between those events a stored figure can trail the live count, which `/status` shows.

**Sample rows, in words** (examples only, not real specs, so they are not table rows). Section Spec: Spec File
`phase-1/section-1/section-1-spec.md`, Ref `1.1`, Status `DRAFT`, Spec Ver `v1.0`, Last Updated the date of
the write, Coverage nothing completed yet of the Novel-Parts and Chapters listed. Novel-Part Spec: Spec File
`phase-1/section-1/part-1/part-1-spec.md`, Ref `1.1.1`, Status `DRAFT`, Spec Ver `v1.0`, Last Updated the date
of the write, Coverage nothing completed yet of the Chapters listed. Chapter Spec: Spec File
`phase-1/section-1/part-1/chapter-001-spec.md`, Ref `1.1.1.001`, Status `DRAFT`, Spec Ver `v1.0`, Last Updated
the date of the write, Coverage `0/6 Areas`.

### Section Specs

| Spec File | Ref | Status | Spec Ver | Last Updated | Coverage |
|---|---|---|---|---|---|
| phase-1/section-1/section-1-spec.md | 1.1 | CONFIRMED | v1.9 | 2026-10-22 | 0/4 Novel-Parts; 8/31 Chapters |

### Novel-Part Specs

| Spec File | Ref | Status | Spec Ver | Last Updated | Coverage |
|---|---|---|---|---|---|
| phase-1/section-1/part-1/part-1-spec.md | 1.1.1 | CONFIRMED | v1.11 | 2026-10-22 | 8/9 Chapters |

### Chapter Specs

| Spec File | Ref | Status | Spec Ver | Last Updated | Coverage |
|---|---|---|---|---|---|
| phase-1/section-1/part-1/chapter-001-spec.md | 1.1.1.001 | COMPLETED | v1.1 | 2026-10-17 | 4/4 Areas |
| phase-1/section-1/part-1/chapter-002-spec.md | 1.1.1.002 | COMPLETED | v1.1 | 2026-10-17 | 5 of 5 Areas written |
| phase-1/section-1/part-1/chapter-003-spec.md | 1.1.1.003 | COMPLETED | v1.2 | 2026-10-17 | 6/6 Areas |
| phase-1/section-1/part-1/chapter-004-spec.md | 1.1.1.004 | COMPLETED | v1.0 | 2026-10-18 | 6/6 Areas |
| phase-1/section-1/part-1/chapter-005-spec.md | 1.1.1.005 | COMPLETED | v1.0 | 2026-10-20 | 6/6 Areas |
| phase-1/section-1/part-1/chapter-006-spec.md | 1.1.1.006 | COMPLETED | v1.0 | 2026-10-20 | 7 / 7 Areas |
| phase-1/section-1/part-1/chapter-007-spec.md | 1.1.1.007 | COMPLETED | v1.1 | 2026-10-22 | 6/6 Areas |
| phase-1/section-1/part-1/chapter-008-spec.md | 1.1.1.008 | COMPLETED | v1.0 | 2026-10-22 | 6/6 Areas |
| phase-1/section-1/part-1/chapter-009-spec.md | 1.1.1.009 | COMPLETED | v1.0 | 2026-10-23 | 8/8 Areas |
