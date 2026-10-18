---
name: ssc-narration-p02-novel-output-file-structure-law
description: Governs the per-Prose output file structure for the Starward Saga novel — the mandatory Word/Markdown file pair (prose-NNNNN.docx / prose-NNNNN.md) written at the fully nested phase-N/section-N/part-N/chapter-NNN/area-N/ path under novel-starward-saga, the Two-Gate trigger from Part 1 that gates when those files are created, folder naming and on-demand creation rules, the immutable-per-file lifecycle model, and the staleness treatment of on-demand Chapter/Phase/Novel aggregates. Reach for this whenever an agent is about to write, name, revise, redraft, reset, rewind, or compile any novel output file, is deciding a folder or file path for a Prose unit, or is reconciling per-Prose files against Ledger or aggregate state. This is canon Part 2 Area 5, domain narration.
user-invocable: false
---

## Rule Text (Verbatim Source — Authoritative)
## Area 5 — Novel Output File Structure Law

### 5.1 — Purpose and Mandate

**Rule 5.1.1 — Output File Mandate (Canon v2.3 — Per-Prose Granularity).**
Every Prose unit accepted into the canon and confirmed for file output must be written to its own dedicated per-Prose file pair: a Word document (`prose-NNNNN.docx`) and a Markdown file (`prose-NNNNN.md`), stored under the full nested narrative path `novel-starward-saga/phase-N/section-N/part-N/chapter-NNN/area-N/`. These per-Prose file pairs are the **authoritative reader-facing substrate** of the novel-writing process — the novel itself at canonical resolution. They are distinct from the SSC Canon governance files (novel-writer folder), the Ledger files, and the derived Chapter/Phase/Novel aggregate documents (which are produced on demand only).

> **[Repo layout note]** `novel-writer` above refers to `.claude/skills/` in the current repo layout (post-.claude/ migration).

Within a single Gate 2 execution, the `prose-NNNNN.docx` and `prose-NNNNN.md` writes for one Prose unit execute together as a coupled pair — the two files for a single Prose are never allowed to drift apart during a successful Gate 2 run. **No chapter-level append model exists under Canon v2.3** — each Prose inhabits its own file pair; Chapter-level, Phase-level, and Novel-level reading experiences are reconstructed on demand via `[EXPORT CHAPTER]` (C-24), `[COMPILE PHASE]` / `[COMPILE PHASE MD]` (C-25/C-26), and `[COMPILE NOVEL]` (C-27) from the per-Prose files.

**Rule 5.1.2 — Gated Trigger on Prose Acceptance (per Part 1 Rule 7.1.1).**
The output file write is **mandatory upon Inter-Gate Confirmation** but is NOT automatic on prose acceptance alone. Every time a Prose unit passes the Post-Output Audit (Part 1 Area 4.2.2), Rule 7.1.1's Two-Gate sequence runs:
1. **Gate 1 — Chat Delivery** executes automatically and unconditionally, displaying the prose in the conversation window.
2. The **Inter-Gate Confirmation Prompt** is displayed; execution halts pending `[CONFIRM WRITE]`, `[REVISE PROSE]`, or `[SKIP WRITE]`.
3. **Gate 2 — File Writes** runs only on `[CONFIRM WRITE]`. On that event, the Book Creation Law (Areas 6 and 7 of this Part) is triggered: the per-Prose `.docx` (Area 6) and per-Prose `.md` (Area 7) file pair is written at the Prose's canonical nested path as a coupled write pair. Any missing folders in the `phase-N/section-N/part-N/chapter-NNN/area-N/` path are created before the file pair is written.
4. On `[REVISE PROSE]`: the file write is held, the prose is revised, and Gate 1 re-executes on the revised prose.
5. On `[SKIP WRITE]`: the file write is skipped for this Prose unit; a divergence warning is issued; the Ledger update still runs against the chat-accepted prose so canonical state remains coherent, but the per-Prose file pair is not created and the filesystem lags chat history until a later corrective command reconciles it.

Part 2's Book Creation Law never triggers a file write independent of Rule 7.1.1's Inter-Gate Confirmation. Any automatic-on-acceptance file write is a Rule 7.1.1 violation and a Rule 5.1.2 violation simultaneously.

**Rule 5.1.3 — File System Authority.**
Part 2 Areas 5, 6, 7, and 8 are the sole authority governing the structure, naming conventions, formatting standards, update protocols, and per-Prose Completeness Indicator law for all novel output files. No other Part may define output file behavior. Part 1 Area 7 commands that produce prose (C-1, C-3, C-4, C-5, C-6, C-7, C-8, C-9, C-28, C-29, C-30) trigger the per-Prose output file write via this Part's law at Gate 2 of Rule 7.1.1; the commands do not independently define the output behavior, and no command may bypass the Inter-Gate Confirmation defined by Part 1 Rule 7.1.1. Commands C-11 `[WRITE N]` and C-12 `[FINISH CHAPTER]` are **DEPRECATED** as of Canon v2.3 per Part 1 Rule 7.1.1(h) — the One-Prose-Per-Invocation Mandate — and must not produce any prose or file write.

### 5.2 — Directory Structure Law (Canon v2.3 — Per-Prose Granularity)

**Rule 5.2.1 — Root Output Folder and Nested Narrative Path.**
All novel output files are stored within the `novel-starward-saga` folder, located at the same directory level as the `novel-writer` folder and all Ledger folders. The `novel-starward-saga` folder is the root of all reader-facing novel output. Under Canon v2.3, every accepted Prose unit inhabits its own file pair at a fully nested path that mirrors the six-tier narrative hierarchy from Phase down to Prose:

> **[Repo layout note]** `novel-starward-saga` above refers to `projects/novel-starward-saga` in the current repo layout (post-.claude/ migration).
> **[Repo layout note]** `novel-writer` above refers to `.claude/skills/` in the current repo layout (post-.claude/ migration).
> **[Repo layout note]** "Ledger folders" above refers to `.claude/story-memory/ledger-*/` in the current repo layout (post-.claude/ migration).

```
[workspace root]/
├── novel-writer/                         ← Canon governance (SSC Canon Parts)
├── ledger-character-hero/                ← Ledger system
├── ledger-character-villain/
├── ...
└── novel-starward-saga/                  ← Novel output (reader-facing per-Prose files)
    ├── phase-1/                          ← Phase 1 output
    │   ├── phase-1-complete.docx         ← (optional) on-demand Phase aggregate via C-25
    │   ├── phase-1-complete.md           ← (optional) on-demand Phase aggregate via C-26
    │   ├── section-1/
    │   │   ├── part-1/
    │   │   │   ├── chapter-001/
    │   │   │   │   ├── chapter-001.docx  ← (optional) on-demand Chapter aggregate via C-24
    │   │   │   │   ├── chapter-001.md    ← (optional) on-demand Chapter aggregate via C-24
    │   │   │   │   ├── area-1/
    │   │   │   │   │   ├── prose-00001.docx   ← per-Prose file pair (authoritative)
    │   │   │   │   │   ├── prose-00001.md
    │   │   │   │   │   ├── prose-00002.docx
    │   │   │   │   │   ├── prose-00002.md
    │   │   │   │   │   └── ...
    │   │   │   │   ├── area-2/
    │   │   │   │   │   └── ...
    │   │   │   │   └── ...
    │   │   │   ├── chapter-002/
    │   │   │   │   └── ...
    │   │   │   └── ...
    │   │   ├── part-2/
    │   │   │   └── ...
    │   │   └── ...
    │   ├── section-2/
    │   │   └── ...
    │   └── ...
    ├── phase-2/                          ← Phase 2 output (created when Phase 2 begins)
    │   └── ...
    └── starward-saga-complete.docx       ← (optional) on-demand Novel aggregate via C-27
```

> **[Repo layout note]** The `[workspace root]/` tree above, showing `novel-writer/` and `ledger-*/` as siblings of `novel-starward-saga/`, refers to the current repo layout where novel output lives at `projects/novel-starward-saga/`, governance skills live at `.claude/skills/`, and Ledger folders live at `.claude/story-memory/ledger-*/` (post-.claude/ migration).

Per-Prose `.docx` and `.md` file pairs at the deepest level are the **authoritative canonical source**. Chapter-aggregate, Phase-aggregate, and Novel-aggregate files are derived artifacts produced only on demand via the C-24 / C-25 / C-26 / C-27 commands; their presence is optional and, when present, must never diverge from the per-Prose substrate.

**Rule 5.2.2 — Phase Subfolder Naming.**
Each Phase of the novel has its own subfolder within `novel-starward-saga`. Phase subfolders are named using the pattern `phase-N` where N is the Phase number (zero-padded to two digits for Phases 10+). Phase 1 = `phase-1`. Phase 2 = `phase-2`. Phase 10 = `phase-10`.

> **[Repo layout note]** `novel-starward-saga` above refers to `projects/novel-starward-saga` in the current repo layout (post-.claude/ migration).

**Rule 5.2.3 — Section / Novel-Part / Chapter / Area Subfolder Naming.**
Within each Phase subfolder, Sections are represented as `section-N` subfolders (where N is the Section number within the Phase). Within each Section subfolder, Novel-Parts are represented as `part-N` subfolders (where N is the Novel-Part number within the Section). Within each Novel-Part subfolder, Chapters are represented as `chapter-NNN` subfolders (where NNN is the Chapter number zero-padded to three digits; Chapter numbering resets per Novel-Part, beginning at 1 for the first Chapter of each Novel-Part). Within each Chapter subfolder, Areas are represented as `area-N` subfolders (where N is the Area number within the Chapter, beginning at 1).

Examples:
- `novel-starward-saga/phase-1/section-1/part-1/chapter-001/area-1/` — Phase 1, Section 1, Novel-Part 1, Chapter 1, Area 1
- `novel-starward-saga/phase-1/section-2/part-1/chapter-003/area-4/` — Phase 1, Section 2, Novel-Part 1, Chapter 3, Area 4
- `novel-starward-saga/phase-2/section-1/part-1/chapter-001/area-1/` — Phase 2, Section 1, Novel-Part 1, Chapter 1, Area 1

> **[Repo layout note]** The bare `novel-starward-saga/phase-N/...` paths in the examples above refer to `projects/novel-starward-saga/phase-N/...` in the current repo layout (post-.claude/ migration).

**Rule 5.2.4 — On-Demand Folder Creation.**
None of the nested subfolders (`phase-N/`, `section-N/`, `part-N/`, `chapter-NNN/`, `area-N/`) are pre-created. Each is created at the moment the first Prose unit within it is accepted and `[CONFIRM WRITE]` triggers Gate 2. If `[START STORY]` (C-3) or `[HARD RESET]` (C-1) is the first prose-producing command, it creates the full path `phase-1/section-1/part-1/chapter-001/area-1/` in a single Gate 2 execution before writing the first Prose file pair. Subsequent `[NEXT PROSE]` calls within the same Area reuse that folder; `[NEXT AREA]` / `[NEXT CHAPTER]` / `[NEXT PART]` / `[NEXT SECTION]` / `[NEXT PHASE]` transitions create the missing folders for the new narrative position on first write.

**Rule 5.2.5 — Chapter Number Definition.**
Chapter numbers within a Novel-Part are sequential integers beginning at 1, zero-padded to three digits (`chapter-001`, `chapter-012`, `chapter-100`). Chapter numbering resets per Novel-Part. The Chapter number in the folder name is a count within its parent Novel-Part — not a Phase-wide absolute. The novel's internal structure is fully encoded by the nested folder path itself; no filename encoding is needed.

**Rule 5.2.6 — Contents Allowed in Narrative Subfolders.**
Phase subfolders may contain Section subfolders and, optionally, an on-demand Phase aggregate (`phase-N-complete.docx` / `phase-N-complete.md`). Section subfolders contain only Novel-Part subfolders. Novel-Part subfolders contain only Chapter subfolders. Chapter subfolders contain only Area subfolders and, optionally, an on-demand Chapter aggregate (`chapter-NNN.docx` / `chapter-NNN.md`) at the Chapter folder's root level. Area subfolders contain only per-Prose file pairs (`prose-NNNNN.docx` / `prose-NNNNN.md`). No other files — no outlines, no notes, no governance documents — are stored in any narrative subfolder. Governance documents remain in `novel-writer`. Ledger files remain in Ledger folders.

> **[Repo layout note]** `novel-writer` above refers to `.claude/skills/` in the current repo layout (post-.claude/ migration).
> **[Repo layout note]** "Ledger folders" above refers to `.claude/story-memory/ledger-*/` in the current repo layout (post-.claude/ migration).

**Rule 5.2.7 — Prose File Naming.**
Within each Area subfolder, Prose files are named using the pattern `prose-NNNNN` where NNNNN is the Prose number within the Area, zero-padded to five digits. Prose 1 of Area 1 of Chapter 1 of Novel-Part 1 of Section 1 of Phase 1 = `prose-00001`. Prose 27 of Area 3 of Chapter 5 of Novel-Part 2 of Section 1 of Phase 1 = `prose-00027`. Each Prose has exactly two files: `prose-NNNNN.docx` and `prose-NNNNN.md`, written as a coupled pair at Gate 2. Prose numbering resets per Area.

### 5.3 — File Lifecycle Law (Canon v2.3 — Per-Prose Granularity)

**Rule 5.3.1 — Per-Prose File Creation on Gate 2.**
Each Prose unit's `prose-NNNNN.docx` and `prose-NNNNN.md` file pair is created the first time that Prose unit passes Gate 2 (on `[CONFIRM WRITE]`). Before Gate 2 fires, no file exists for that Prose unit. On Gate 2 for a new Prose, both files in the pair are created simultaneously and the Prose's content is written to them. Any missing folders in the nested path `phase-N/section-N/part-N/chapter-NNN/area-N/` are created as part of the Gate 2 write.

**Rule 5.3.2' — Immutable-Per-File Model (replaces prior Append-Only Model).**
Each per-Prose file pair holds exactly one Prose unit. After creation, the file pair is modified **only** by the following operations:
- `[REVISE PROSE: reference]` (C-28), which overwrites both files with the revised Prose at Gate 2 of the revision sequence. The file's identity and path do not change; only its content does.
- `[REDRAFT AREA]` (C-29), which overwrites each in-scope Prose's file pair in place as the redraft progresses.
- `[REDRAFT CHAPTER]` (C-30), which archives the Chapter's per-Prose subtree with a timestamp and rebuilds fresh per-Prose file pairs under the Chapter folder.
- `[RESET CHAPTER]` / `[RESET PHASE]` / `[RESET STORY]` (C-22 / C-23 / C-21), which delete per-Prose files and associated folders per their command definitions.
- `[REWIND TO]` (C-16), which archives all per-Prose files at and after the rewind point as non-canonical pending revision (without immediately deleting them; new prose written forward replaces them one at a time).

No Prose's `.docx` or `.md` file is ever appended-to or extended beyond its single Prose payload. Per-Prose files are not shared across Prose units, and no editorial operation may splice multiple Prose payloads into a single `prose-NNNNN.{docx,md}` pair.

**Rule 5.3.3' — One File Pair Per Prose (replaces prior One File Per Chapter Rule).**
Each Prose has exactly one `.docx` file and exactly one `.md` file, written to its canonical nested path. An Area boundary creates a new Area subfolder, not a section-break within a file. A Chapter boundary creates a new Chapter subfolder. A Novel-Part boundary creates a new Novel-Part subfolder. A Section boundary creates a new Section subfolder. A Phase boundary creates a new Phase subfolder. In every case, the filesystem itself encodes the narrative hierarchy; no file ever contains content spanning more than one Prose unit.

**Rule 5.3.4 — File Integrity.**
Per-Prose output files must not be manually edited outside of the SSC Canon-governed writing process. Manual edits to output files are not tracked by the Ledger system and may create discrepancies between the Ledger record and the file content. If manual edits are made, the user accepts responsibility for any resulting continuity errors.

**Rule 5.3.5 — Aggregate Staleness.**
Any on-demand Chapter-aggregate (`chapter-NNN.docx` / `chapter-NNN.md`), Phase-aggregate (`phase-N-complete.docx` / `phase-N-complete.md`), or Novel-aggregate (`starward-saga-complete.docx`) file produced via C-24 / C-25 / C-26 / C-27 is treated as a **cache** of the per-Prose source and is marked stale on any revision (C-28, C-29, C-30) or reset (C-21, C-22, C-23) that affects any of its underlying per-Prose files. Stale aggregates must be regenerated on the next invocation of their producing command, or deleted outright. The per-Prose files are always authoritative; the aggregates are never permitted to silently diverge.

---

## Cross-References
| Related Skill | Relation | Source |
|---|---|---|
| ssc-cultivation-p03-cultivation-ladder-realm-hierarchy | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 5 governs output-file/folder path structure and file lifecycle mechanics, with no rule tied to cultivation-realm content |
| ssc-cultivation-p03-lifespan-mechanics | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 5 governs output-file/folder path structure and file lifecycle mechanics, with no rule tied to lifespan mechanics |
| ssc-cultivation-p03-power-density | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 5 governs output-file/folder path structure and file lifecycle mechanics, with no rule tied to power-density mechanics |
| ssc-cultivation-p03-realm-transition | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 5 governs output-file/folder path structure and file lifecycle mechanics, with no rule tied to realm-transition mechanics |
| ssc-cultivation-p03-cultivation-talent | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 5 governs output-file/folder path structure and file lifecycle mechanics, with no rule tied to cultivation-talent mechanics |
| ssc-cultivation-p03-growth-speed | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 5 governs output-file/folder path structure and file lifecycle mechanics, with no rule tied to growth-speed mechanics |
| ssc-cultivation-p03-power-comparison | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 5 governs output-file/folder path structure and file lifecycle mechanics, with no rule tied to power-comparison mechanics |
| ssc-cultivation-p03-damage-tolerance-recovery | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 5 governs output-file/folder path structure and file lifecycle mechanics, with no rule tied to damage-tolerance/recovery mechanics |
| ssc-cultivation-p03-affinity-cultivation | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 5 governs output-file/folder path structure and file lifecycle mechanics, with no rule tied to affinity-cultivation mechanics |
| ssc-cultivation-p03-heart-cultivation | SOFT | Inherited Part 2 ↔ Part 3 Part-level cross-reference only; Area 5 governs output-file/folder path structure and file lifecycle mechanics, with no rule tied to heart-cultivation mechanics |

## Governing Authority
Subordinate to the shared Part 1 (audit law) + Part 34 (knowledge graph) grounding in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.

## Source Provenance
Part 2, Area 5 — "Novel Output File Structure Law" · canon v4.33 · migrated 2026-08-03
