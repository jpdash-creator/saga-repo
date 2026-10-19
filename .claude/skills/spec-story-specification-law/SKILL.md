---
name: spec-story-specification-law
description: Governs the spec chain under .claude/story-memory/phase-section-part-chapter-area-specs/, a tree mirroring the novel (phase-N/section-N/section-N-spec.md, phase-N/section-N/part-N/part-N-spec.md and phase-N/section-N/part-N/chapter-NNN-spec.md), giving every Section, every Novel-Part and every Chapter an author-approved plan before its Areas are written, each spec depending on the one above it (Section Spec, then Novel-Part Spec, then Chapter Spec). Its Master Rule Register (Rules 38.1-38.14) and eleven Areas define the Spec Chain Mandate, the Section Spec (built by /section-spec from the whole of Part 30), the Novel-Part Spec (built by /part-spec, every Chapter listed in depth), derivation, precedence and cascade between the three, and the Clarity Mandate for All Spec Builds; the Spec Authority Model — Locked Canon over ledger over spec over session-log, ledger supersedes spec, specs never establish canon facts; the NOT-a-ledger boundary with Part 37; the rich chapter-spec artifact schema (name-chain header with Establishment status, per-Area blocks, each the plan of one written Area and the bible that connects the chapter, with title, pacing, size target of 1,600, 1,800 or 2,000 words, opening and closing type, scene anchors, carry-over and the continues-in-next-Area flag, thread, viewpoint, planned time skips, story link, setups and payoffs, emotional line, world, setting and people, novel elements, optional tone or voice tag, Tier Scope Bracket range, standing exclusions, P30-L5 crisis-density tracking); the clean-body rule (Rule 38.14) under which a spec carries no inline settlement tags and gathers every settled, open, deferred, skipped, provenance, variance and audit note in a final Audit and Settlement Notes section; the build, light-continuity-audit and [CONFIRM SPEC] / [REVISE SPEC] / [SKIP SPEC] lifecycle (shared by all three kinds of spec) with mandatory Gate 2 as-built sync of the Chapter Spec and COMPLETED as the finished status; the Part 28 Rule 19.4 Decision Consultation Gate interface and its carve-outs; the Part 2 Area 9 Tier Scope Bracket backing store (the Areas-in-Chapter range only, no range stored above Chapter); blocking Gate 1 Check 18 (Spec Conformance, the chain must be in force); reset, rewind and redraft survivability; and the Part 38 Amendment Protocol. Reach for this whenever building or amending a Section Spec via /section-spec, a Novel-Part Spec via /part-spec or a Chapter Spec via /chapter-spec, planning the next Area, resolving spec-versus-ledger conflicts, or auditing spec conformance. This is canon Part 38, domain spec, the single consolidated authority for the whole Part.
user-invocable: false
---

# Story Specification Law

**Authority Tier:** 1 (Domain Authority — Story Specification)
**Canon Version:** Canon v10.0 | **Last Updated:** 2026-10-05
**Domain:** Spec — SSC Canon Story Specification Law: the spec chain (Section Spec, Novel-Part Spec, Chapter Spec) in `.claude/story-memory/phase-section-part-chapter-area-specs/` (tree mirroring the novel: `phase-N/section-N/section-N-spec.md`, `phase-N/section-N/part-N/part-N-spec.md`, `phase-N/section-N/part-N/chapter-NNN-spec.md`), covering the Master Rule Register (Rules 38.1–38.14); the spec chain itself (Area 9), the Section Spec (Area 10) and the Novel-Part Spec (Area 11); the Spec Authority Model (Locked Canon > ledger > spec chain > session-log; "Ledger supersedes spec"); the rich chapter-spec artifact schema (header name-chain with per-name Establishment status, per-Area blocks (the plan of one written Area: title, pacing, size target, scene anchors, opening and closing type, carry-over and the continues-in-next-Area flag, thread, viewpoint, time skips, story link, setups and payoffs, emotional line, world, setting and people, novel elements), chapter-level Tier Scope Bracket range, standing exclusions, P30-L5 crisis-density tracking); the clean-body rule and the Audit and Settlement Notes section (Rule 38.14); the build → light continuity audit → `[CONFIRM SPEC]` lifecycle with mandatory Gate 2 as-built sync; the Part 28 Decision Consultation Gate interface (spec-settled items as Rule 19.4 decision inputs, with the open-item / new-branch / clarity-reduction / Autonomous-Matter carve-outs); the Part 2 Area 9 Tier Scope Bracket backing-store interface; Gate 1 Check #18 (Spec Conformance, blocking); reset/rewind/redraft survivability; and the Part 38 Amendment Protocol with the cross-Part dependency table
**Governing Canon Parts Cross-Reference:** Parts 2, 28, 30, 35, 36, 37, 41; gate audit (FCIA/ALCA) in `guardrails/audit/guardrail-audit-gate-law.md`

---

## Overview

Part 38 is the Starward Saga Canon's Story Specification Law — the Tier 1 Domain Authority for the **spec chain** (the Section Spec, the Novel-Part Spec and the Chapter Spec, together "the spec chain") stored under `.claude/story-memory/phase-section-part-chapter-area-specs/`. It exists to give every Section, every Novel-Part and every Chapter a confirmed, author-approved plan **before** its Areas are written, so that the Part 28 Area 19 Decision Consultation Gate can ask meaningful per-Area questions against a settled chapter frame instead of re-deriving the chapter's direction one Area at a time.

The novel has five tiers: Phase, Section, Novel-Part, Chapter and Area. The **Area is the written unit**: it is not necessarily one complete scene, because a scene may run on across consecutive Areas of a Chapter (Part 2). A **Section Spec** (built by `/section-spec`, Command C-40) turns what Part 30 expects of a Section into its Novel-Parts and, at a high level, their Chapters. A **Novel-Part Spec** (built by `/part-spec`, Command C-41) lists every Chapter of one Novel-Part in depth. The **Chapter Spec** (built by `/chapter-spec`, Command C-39) is the plan of one Chapter and of every Area in it. Each spec depends on the one above it: a Chapter Spec cannot exist without a Novel-Part Spec, and a Novel-Part Spec cannot exist without a Section Spec (Rule 38.9). Every Area is written against a confirmed, author-approved plan, and the Chapter Spec is the plan that the Area-time gates read.

A spec of any of the three kinds is a plan, not a record. The record of what is true in the story remains the ledger system (Part 37 domain); the spec is the record of what is *intended*. That distinction is load-bearing and is codified as the Spec Authority Model (Rule 38.3): **Locked Canon > ledger (established by accepted Areas) > spec chain (intent) > session-log (never a decision input)**. Ledger supersedes spec. A spec is never a source of established canon facts — every name, description, and event a spec proposes remains a proposal until a Gate 1 delivery that is confirmed and written, or a Gate 2 write, establishes it (Part 28 Rule 18.4.4 Stability After First Use for Novel-Part, Chapter and Area names; Part 28 Area 20.3 for in-world names, fixed when the delivered Area is confirmed; Part 28 Area 3.4 name immutability).

A spec reads clean. Its body is plain plan text with no inline settlement tags, and every settled item, open item, deferral, ruling provenance, variance and audit note is gathered in one final section, **Audit and Settlement Notes**, at the end of the file (Rule 38.14).

Across eleven Areas, Part 38 defines: the foundational principles — purpose, folder law, the Spec Authority Model, and the NOT-a-ledger boundary with Part 37 (Area 1); the rich chapter-spec artifact schema — chapter header block with the full name-chain and per-name Establishment status, per-Area blocks (each the plan of one written Area and the bible that connects the chapter's Areas, section 2.4), chapter-level Tier Scope Bracket range, the standing-exclusions block, the P30-L5 crisis-density tracking row, and the Audit and Settlement Notes section (Area 2); the spec lifecycle — build at chapter open or retro-fit, the light continuity audit, the `[CONFIRM SPEC]` / `[REVISE SPEC]` / `[SKIP SPEC]` tokens (shared by all three kinds of spec), amendment via `/section-spec`, `/part-spec` and `/chapter-spec`, the mandatory Gate 2 as-built sync of the Chapter Spec, and completion (Area 3); the authority model and the Decision Consultation Gate interface — settling power under Part 28 Rule 19.4 with its exact carve-outs (Area 4); the Tier Scope Bracket interface with Part 2 Area 9 (Area 5); Gate integration — blocking Gate 1 **Check #18: Spec Conformance**, which asks that the whole chain is in force, and the Gate 2 as-built sync ownership (Area 6); reset, rewind, and redraft behavior (Area 7); the Part 38 Amendment Protocol plus the cross-Part dependency table (Area 8); the spec chain — dependency between the three kinds, build timing, derivation, precedence and cascade, writers, settling power downward, the clarity mandate for all spec builds, completion, retro-fit and the orphan rule, read sets and orchestration, and the clean-body and notes rule (Area 9); the Section Spec (Area 10) and the Novel-Part Spec (Area 11).

**Companion artifacts.** The spec folder's master registry is `.claude/story-memory/phase-section-part-chapter-area-specs/_index.md`. The operational guardrail is `.claude/guardrails/ledger/guardrail-story-spec-law.md`. The authoring and amendment commands are `/section-spec` (Command C-40), `/part-spec` (Command C-41) and `/chapter-spec` (Command C-39), one for each kind of spec. The Part 2 side of this law is recorded in `narration-novel-book-structure-law` Area 9 Rule 9.13 (Story Specification Interface), authored through the Rule 9.12.2 explicit-amendment doorway.

**Single source.** Per the One Skill Per Part law (`.claude/guardrails/authority/guardrail-consolidated-skill-reading.md`), Part 38 is this single skill, `spec-story-specification-law`, and this file is its sole rule text. `canon-manifest/skill-index.json` carries this entry with `consolidated: true` and its eleven Areas indexed in `areas[]`.

---

## Master Rule Register (Rules 38.1–38.14)

Part 38's fourteen master rules are numbered part-scoped (`Rule 38.N`) and are elaborated by the Areas below. Citations elsewhere in the repo (e.g., the spec folder `_index.md`) cite these master rules directly.

| Rule | Name | Statement (summary) | Elaborated in |
|---|---|---|---|
| **Rule 38.1** | Chapter Spec Mandate | Every Section, every Novel-Part and every Chapter has exactly one spec file at its canonical tree path. A confirmed spec chain must exist before a Chapter's Areas are written: the Chapter Spec is confirmed, and the Novel-Part Spec and the Section Spec above it are each CONFIRMED or COMPLETED. `[NEXT CHAPTER]` (C-6) requires the chain at chapter open: it builds the Chapter Spec only, and a missing link above the Chapter stops it, naming that link and the command that puts it right (Rule 3.1.1). `[NEXT AREA]` reads the chain and refuses to plan when any link is missing, naming the first missing link and the command that builds it. No Chapter's Areas are written without a confirmed spec. | Areas 1, 3, 6, 9 |
| **Rule 38.2** | Spec Schema Conformance | Every spec file follows the schema of its own kind: the Chapter Spec follows Area 2, the Section Spec follows Area 10 and the Novel-Part Spec follows Area 11. No spec file is free-form. | Areas 2, 10, 11 |
| **Rule 38.3** | Spec Authority Model | Locked Canon > ledger (established by accepted Areas) > spec chain (intent) > session-log (never a decision input). Ledger supersedes spec. Items the author explicitly settled at spec-build are settled decision inputs for Part 28 Rule 19.4 purposes. A spec is NEVER a source of established canon facts — spec contents are proposals until a Gate 1 delivery that is confirmed and written, or a Gate 2 write (Part 28 Rule 18.4.4). Inside the chain, a higher spec says what a level must do and the lower spec governs its own detail (Rule 38.12). | Areas 1, 4, 9 |
| **Rule 38.4** | DCG Interface and Carve-Outs | Spec-settled items are not re-asked at Area time (a settled item of the Section Spec or the Novel-Part Spec reaches Area time through the Chapter Spec, where it is carried in as an inherited note naming its source, Rule 9.5.1). No pacing question is asked at Area-writing time: pacing is decided in the Chapter Spec for every Area and carried. Always still asked: branches the spec records as open in its Audit and Settlement Notes; genuinely new branches; and anything whose clarity has reduced since spec-build (the author's standing "DO NOT ASSUME" rule). Part 36 Area 13 Autonomous Matters are never spec-fixed, except through the author's optional levers: the sensory anchor, tone and voice, and content fields (Rules 2.3.5a, 2.3.5b and 2.3.5d). | Areas 4, 9 |
| **Rule 38.5** | Bracket Backing Store | The active chapter spec is THE authoritative backing store for its Chapter-tier Tier Scope Bracket range (Areas in the Chapter; Part 2 Area 9; Part 28 Rule 18.7 draws through it). No range is stored above Chapter grain, because the Section Spec's Novel-Part plan and the Novel-Part Spec's Chapter entries are lists that guide the plan, and the length of a list is read as information (Part 2 Rule 9.3.1). Ranges stay tentative low–high and advisory-in-force — never stop-conditions, never fill-conditions; Part 2 Area 9 semantics (Part 2 Rules 9.6.1, 9.6.2, 9.7, 9.8, 9.9) are preserved unchanged. | Area 5 |
| **Rule 38.6** | Gate Integration | Gate 1 Post-Draft Audit gains blocking **Check #18: Spec Conformance**; its part (a) asks that the chain is in force (Rule 6.1.1), and its part (b) blocks on a core difference, a settled-item difference or a size outside 1,280 to 2,400 words, while pacing is listed only (Rules 6.1.1 to 6.1.4). Every Gate 2 execution performs a mandatory as-built spec sync, owned by the Post-Write Ledger Update continuity-checker instance (the Gate 2 pipeline stays 3-way); the sync writes the Chapter Spec only (Rule 6.2.1). | Areas 3, 6 |
| **Rule 38.7** | Reset Survivability | Spec files of all three kinds survive destructive/rewind commands, with `[HARD RESET]` (C-1) as the sole exception — it deletes every spec file of all three kinds and empties the registry. Per-Area statuses roll back to match the surviving Areas, with a variance note. When a rewind or reset removes written Areas, a COMPLETED Chapter Spec returns to CONFIRMED, and a COMPLETED Novel-Part Spec or Section Spec returns to CONFIRMED as soon as any spec under it is no longer COMPLETED; completion text is kept. `[REDRAFT CHAPTER]` (C-30) re-opens the Chapter Spec first. Intent outlives the written Areas, and only `[HARD RESET]` destroys it. | Areas 7, 9 |
| **Rule 38.8** | Amendment Protocol | Specs are amended any time via the command of their kind (`/section-spec`, `/part-spec`, `/chapter-spec`); substantial amendments re-audit and re-confirm. When a parent spec is amended after children exist, the continuity-checker reports every child entry or spec the change no longer fits, and the author decides for each one: keep it (variance noted), amend it, or mark it AMENDED-PENDING-RECONFIRM; nothing flips automatically and written Areas are never touched (Rule 38.12). Part 38 itself is amended only by the Area 8 protocol. | Areas 3, 8, 9 |
| **Rule 38.9** | Spec Chain Mandate | The Section Spec, the Novel-Part Spec and the Chapter Spec form one chain, and each depends on the one above it. A Chapter Spec is built or revised only while its Novel-Part Spec and its Section Spec are CONFIRMED or COMPLETED, and a Novel-Part Spec only while its Section Spec is; a parent that is DRAFT, AMENDED-PENDING-RECONFIRM or RETIRED refuses the child build, and the refusal names the right command. Specs are built at the boundary (the start of the story, a new Section, a new Novel-Part), top-down, each through its own `[CONFIRM SPEC]`; `[SKIP SPEC]` on any level stops the chain there. No Phase Spec exists: Part 30 is the Phase plan. | Area 9 |
| **Rule 38.10** | Section Spec | The Section Spec is the author-approved plan of one Section. It is built from the whole of Part 30 (cited by function name, never copied) and, through a series of questions, expands what Part 30 expects of the Section into its Novel-Parts and, at a high level, their Chapters. Its file is `phase-N/section-N/section-N-spec.md` (ref `P.S`). | Area 10 |
| **Rule 38.11** | Novel-Part Spec | The Novel-Part Spec (command `/part-spec`) is the author-approved plan of one Novel-Part. It lists every Chapter of the Novel-Part in depth. Its file is `phase-N/section-N/part-N/part-N-spec.md` (ref `P.S.P`). | Area 11 |
| **Rule 38.12** | Derivation, Precedence and Cascade | A lower spec is built from the entry of the spec above it, and an inherited item keeps its source note. For scope the order is Locked Canon > ledger > Section Spec > Novel-Part Spec > Chapter Spec (what the level must do); the lower spec governs its own detail, and a conflict found in a lower build is a question to the author, never a silent pick. A settled item of a higher spec is not re-asked in a lower build and is carried into the Chapter Spec as an inherited note naming its source. Amending a parent after children exist runs the cascade report (Rule 38.8). | Area 9 (sections 9.3 to 9.5) |
| **Rule 38.13** | Clarity Mandate for All Spec Builds | One definition of "done" governs the three builds: no unasked branch at the spec's own level, a final sweep (outline-planner and continuity-checker) that returns nothing new, the author's explicit "nothing further to steer", and then the confirm token. The planner never leaves an item open on its own; only the author may defer one. No score, no percentage and no round count. | Area 9 (section 9.6) |
| **Rule 38.14** | Clean Spec Body and Audit and Settlement Notes | A spec file carries no inline `[SETTLED …]`, `[OPEN …]`, `[ASKED …]`, `[SKIPPED …]` or `[FROM …]` tags and no provenance or audit tags in its body. The body reads clean, as plain plan text, start to finish. Every settled item, open item, deferral, skip, ruling provenance, variance and audit note is gathered in a single final section, **Audit and Settlement Notes**, at the end of the file, each note pointing back to the plan item it concerns by Area, field name or heading. An open item is found in that section, and every rule that looks for an open or settled item looks there. | Areas 2, 9 (section 9.10), 10, 11 |

---

## Area 1 — Foundational Principles

### 1.1 — Purpose: Spec-Grounded Planning

**Rule 1.1.1 — Why the spec exists.**
The Part 28 Area 19 Decision Consultation Gate is the author's rudder, but a rudder needs a charted course: without a chapter-grain plan, every `[NEXT AREA]` invocation must re-derive chapter direction from scratch, and DCG questions drift toward re-litigating direction the author has already given. The chapter spec fixes this. It is the author-approved chapter frame — Areas, planned beats, viewpoint, debuts, emphasis, and scope range — built once per Chapter through iterative author consultation, so that per-Area DCG questions can address only what is genuinely open at Area time. Spec-grounded planning makes DCG questions meaningful; it never replaces the DCG (Area 4).

**Rule 1.1.2 — What the spec is not.**
The spec is not prose, not an outline delivered to the reader, not a ledger, and not a container of established canon. It binds planning conduct (what the planner proposes, what the gate checks, what the brackets report) — it never binds the story itself against the author's Area-time choices, which flow through the DCG on record.

### 1.2 — Folder and File Law

**Rule 1.2.1 — Canonical location and tree.**
All specs (Section Specs, Novel-Part Specs and Chapter Specs) live under `.claude/story-memory/phase-section-part-chapter-area-specs/`, in a tree that mirrors the novel output tree tier-for-tier:

```
.claude/story-memory/phase-section-part-chapter-area-specs/
├── _index.md                      ← master registry (one registry, three tables)
└── phase-N/
    └── section-N/
        ├── section-N-spec.md         ← Section Spec     (ref P.S)
        └── part-N/
            ├── part-N-spec.md        ← Novel-Part Spec  (ref P.S.P)
            └── chapter-NNN-spec.md   ← Chapter Spec     (ref P.S.P.CCC)
```

Folder naming follows Part 2 Rules 5.2.2–5.2.5 exactly: `phase-N`, `section-N`, `part-N`, and chapter numbers zero-padded to three digits with numbering resetting per Novel-Part. Exactly one spec file exists per Chapter, one per Novel-Part and one per Section (Rule 38.1). Missing tree folders are created when the first spec within them is created. Spec files are written with the ordinary Write and Edit tools, and no script writes them.

**Rule 1.2.2 — Registry.**
`_index.md` is the master registry: ONE registry file with THREE tables, one for Section Specs, one for Novel-Part Specs and one for Chapter Specs. Every row carries the columns Spec File, Ref, Status, Spec Ver, Last Updated and Coverage. The Ref is `P.S` for a Section Spec (for example `1.2`), `P.S.P` for a Novel-Part Spec (for example `1.2.3`) and `P.S.P.CCC` for a Chapter Spec (for example `1.2.3.004`). Coverage reads "Novel-Parts completed / planned; Chapters completed / planned" for a Section Spec, "Chapters completed / planned" for a Novel-Part Spec, and "Areas written / planned" for a Chapter Spec. The Coverage of a Section row or a Novel-Part row is refreshed at that spec's own confirm, at any completion write step (the completion of a child spec included) and at a reset or rewind rollback, and never at Gate 2. The only tables in the file are the three registry tables, because the reset script empties every table in it; any legend or vocabulary is written in words. Every spec create, confirm, amendment, sync that changes status counts, and completion updates the registry row in the same write cycle.

**Rule 1.2.3 — Writers.**
Spec files are written only by: (a) the `/section-spec`, `/part-spec` and `/chapter-spec` command flows (outline-planner-led build and amendment, Area 3; the orchestrating command, not outline-planner, writes the spec file, its registry row and the session-log line); (b) the Gate 2 as-built sync (Post-Write Ledger Update continuity-checker instance, Areas 3.6 and 6.2), which writes the Chapter Spec only, also updates that spec's registry row (Rule 1.2.2) and sets its status to COMPLETED when its last Area is written (Rule 3.6.1 item 1); a redraft that re-opened a completed Chapter Spec is covered by the same sentence: the status returns to COMPLETED when its last Area is written again; (c) the destructive/rewind command reconciliation pass (the continuity-checker sync role of Rule 7.2.1), which may change per-Area statuses, name Establishment states, reference stamps, variance notes, registry coverage columns and the COMPLETED to CONFIRMED rollbacks of Rule 7.2.1 only — never plan content; (d) completion at `[NEXT CHAPTER]` (or `/chapter-spec complete`), at `[NEXT PART]` and at `[NEXT SECTION]` (Rule 3.7.1; Rules 9.7.2 and 9.7.3), which write the completion content of the outgoing Chapter Spec, Novel-Part Spec and Section Spec and set their status to COMPLETED; and (e) a lower-level flow, which may APPEND variance notes to the Audit and Settlement Notes of any higher spec it derives from (every spec above the departure, Rule 9.4.5) but may not change that spec's plan content (Rules 9.4.3 and 9.4.5). No other agent, command, or audit writes to a spec file. Area-producing commands read specs; they do not author them.

### 1.3 — The Spec Authority Model (Rule 38.3)

**Rule 1.3.1 — The ordering.**
Whenever two sources speak to the same question, authority descends in exactly this order:

1. **Locked Canon** (Part 30 Locked Canon, Part 28 Locked Canon designations, P30-L8 and every Authority Tier 0 law) — always prevails.
2. **Ledger** — established canon, written from accepted Areas under Part 37 schemas. What the ledger records as established IS the story's state.
3. **Spec chain** (the confirmed Section Spec, Novel-Part Spec and Chapter Spec) — author-confirmed intent. Valid decision input for planning and structural decisions; subordinate to everything established. Inside the chain, for scope, the order is Section Spec > Novel-Part Spec > Chapter Spec: the higher spec says what a level must do, and the lower spec governs its own detail (Rule 38.12; Rule 9.4.1).
4. **Session-log** — never a decision input at all (`.claude/guardrails/ledger/guardrail-session-log-not-canon.md`). Historical record only.

**Ledger supersedes spec.** If a confirmed spec plans one thing and accepted Areas (and hence the ledger) established another, the ledger governs; the spec is corrected to match reality at the next sync as a variance (Area 3.6), never the reverse. A Section Spec or Novel-Part Spec is not synced at Gate 2; it is corrected by the variance notes that the lower flows append to it (Rule 9.4.5) and by its completion record (Rule 9.7.3).

**Rule 1.3.2 — Specs never establish canon facts.**
A spec is NEVER a source of established canon facts. Names, descriptions, events, debuts, thread contents, and every other substantive item a spec carries are **proposals** until the first Gate 1 delivery that is confirmed and written (a draft discarded by `[SKIP WRITE]` establishes nothing) — Establishment under Part 28 Rule 18.4.4 (Stability After First Use) and Part 28 Area 3.4 (name immutability). No audit finding, consequence ruling, ledger entry, or continuity claim may cite a spec as evidence that something is true in the story. The Establishment status of each name (Rule 2.3.1) makes this boundary visible: `proposed` until first delivery, then `locked-at-Gate-1` for a Novel-Part, Chapter or Area name (Part 28 Rule 18.4.4) or `locked-at-Gate-2` for an in-world name once its Area is confirmed (Part 28 Area 20.3); the status is recorded in the Audit and Settlement Notes (Rule 38.14). This rule binds all three kinds of spec. A settled item of a Section Spec or a Novel-Part Spec establishes nothing either. Above Chapter grain a name is only a working label, and no Establishment status is stored in a Section Spec or a Novel-Part Spec; establishment is recorded in the Chapter Spec and in the delivered files (Areas 10 and 11).

**Rule 1.3.3 — Settling power (planning-side authority).**
Within its subordinate station, the spec has one real power: items the author **explicitly answered** during spec-build or spec-amendment are SETTLED for Part 28 Rule 19.4 purposes — they are valid "already-settled" decision inputs, and the DCG does not re-ask them at Area time. Area 4 defines this power and its exact carve-outs. The power runs down the chain: a settled item of a higher spec is not re-asked in a lower build, and it is carried into the Chapter Spec as an inherited note naming its source, because Area time reads only the Chapter Spec (Rules 9.5.1 to 9.5.3).

**Rule 1.3.4 — Counters inform; the confirmed spec chain and Part 30 prevail.**
A CONFIRMED spec chain (the confirmed Section Spec, Novel-Part Spec and Chapter Spec) and Part 30 prevail over every counter, floor, ceiling, budget and threshold in the Canon (`guardrails/authority/guardrail-authority-tier-system.md`). At Gate 1 and Gate 2 such a figure is information: it is shown in the report, it never forces content, never fails an Area, never blocks a scene and never puts a question to the author on its own, and nothing is added to or taken out of an Area to move it. What the spec plans for an Area (the scene, the size target, the pacing, the emphasis) stands against any figure; the same holds for what the Section Spec and the Novel-Part Spec plan at their own levels. This changes no tier and no place in the ordering of Rule 1.3.1: Locked Canon, the ledger and a settled spec item rank as that Rule says, and Locked Canon facts, content limits and the style bans are not counters. The Area size range of Rule 2.3.5e is structural and is not a counter. A count outside 1,280 to 2,400 words is a blocking finding: the write waits for the author to confirm the Area or send it back (Rule 6.1.4).

### 1.4 — NOT a Ledger (Part 37 Boundary)

**Rule 1.4.1 — Part 37 does not govern this folder.**
The spec folder is a story-memory artifact but is **not** a ledger folder. It does not appear in the Part 37 Area 4 Ledger Folder Registry; Part 37's entity creation thresholds, schema templates, and B/L field classification do not apply to it; C-38 `[FORCE LEDGER AUDIT AND UPDATE]` and all ledger tooling skip it. Part 38 (this Part) is the sole schema and lifecycle authority for spec files, exactly as Part 37 is for ledger files.

**Rule 1.4.2 — No duplication across spec and ledger (single-source discipline).**
A spec never restates ledger content. Where a spec needs an established fact — a character, a location, a relationship state, a realm level — it references the ledger entry **by name and/or reference code** (e.g., "Varya — see `ledger-character-hero/varya.md`") and says only what the *plan* adds (her role in the planned beat). Copying ledger field values into a spec creates a second, staleness-prone source of truth and is a Rule 1.4.2 violation. Symmetrically, ledgers never cite spec content as evidence (Rule 1.3.2). Spec-to-spec derivation is allowed and is noted: a lower spec may take an entry of the spec above it as its starting point, recorded in its Audit and Settlement Notes as a From note naming the entry, and a settled item it inherits is recorded as an Inherited note naming the higher spec; an inherited item never loses its note by being copied (Rules 9.3.1 and 9.3.4). A spec never restates ledger content, and the single-source discipline for facts is unchanged. The calendar ledger `ledger-worlds-calendar/` (Part 41 Area 9) owns every recorded date, and a spec states a calendar window only as a plan, in dates plus Phase Day, citing Part 41 and never copying its month table or its recorded dates; the as-built in-story time of Rule 3.6.1 item 2 mirrors the ledger without becoming a second source, and the ledger never cites a spec as evidence of a date.

### 1.5 — Non-Derogation of Story-Demanded Structure

**Rule 1.5.1 — Part 2 principles unchanged.**
Nothing in Part 38 converts any structural tier into a bureaucratic container. Chapters still close only at narrative closure (Part 2 Area 1 §1.4.1–1.4.5); Areas still open because the story demands them; the depth-and-pacing precedence and inter-tier continuity retain absolute precedence exactly as Part 2 Rules 9.7 and 9.8 state. A spec that the story outgrows is amended or varied on record — the Areas are never bent to fit the spec.

---

## Area 2 — The Chapter Spec Artifact Schema (Rich)

### 2.1 — Schema Mandate

**Rule 2.1.1 — One schema, all specs (of the Chapter Spec kind).**
Every `chapter-NNN-spec.md` follows the template in Rule 2.2.1. Forward specs (built before the chapter's Areas are written) and as-built specs (retro-fitted to an already-written chapter, Area 3.1) use the same schema; an as-built spec simply begins life with its Area statuses already set to `WRITTEN(ref)`. This Area is the schema of the Chapter Spec. The Section Spec follows the template of Rule 10.2.1 and the Novel-Part Spec follows the template of Rule 11.2.1; every spec file follows exactly one of the three (Rule 38.2).

**Rule 2.1.2 — Population discipline.**
Every field of the body holds a plain value. A decision the author answered at spec-build is recorded in the Audit and Settlement Notes as a Settled note; a field left genuinely open is recorded there as an Open note — never silently guessed, and never marked inline in the body (Rule 38.14; section 9.10). Establishment status is mandatory for every name the Chapter Spec introduces (Rule 1.3.2) and is recorded in the notes as a Name note. The planner never leaves a field open on its own. Every field is asked, and only the author may defer one; a deferral is recorded as a Deferred note naming where the question goes (Rule 9.5.2 and Rule 38.13). Above Chapter grain no Establishment status is stored, Rule 1.3.2.

### 2.2 — The Template

**Rule 2.2.1 — Canonical chapter spec template.**

```markdown
# Chapter Spec — [Chapter NNN: Chapter Name] (Ref prefix: P.S.P.CCC — e.g. 1.1.1.002)

**Governing Law:** Part 38 — Story Specification Law (spec-story-specification-law)
**Spec Status:** [DRAFT / CONFIRMED / AMENDED-PENDING-RECONFIRM / COMPLETED / RETIRED]
**Spec Version:** v1.0 | **Confirmed:** [YYYY-MM-DD via [CONFIRM SPEC] / — ]
**Last Updated:** [YYYY-MM-DD] | **Last Sync:** [Gate 2 of P.S.P.CCC.AA / —]
**Light Continuity Audit:** [PASS YYYY-MM-DD / pending]

---

## 1 — Chapter Header Block

**Name-Chain:**
- Phase [N] — [Phase Name] (locked, Part 30 Locked Canon)
- Section [N] — [Section Name] (locked, Part 30 Locked Canon)
- Novel-Part [N] — [Novel-Part Name]
- Chapter [NNN] — [Chapter Name]

**Chapter Purpose (Part 30 Section-mandate citations — by function name only, never copied text):**
[2–5 sentences: what this Chapter does for the Section arc. Cite the Part 30 mandates it
serves by their function names, e.g. "serves the Section 1 Diplomacy Scene mandate
and Law P30-L4" — the mandate text itself lives in Part 30 only.]

**Calendar Window (per Part 30 §1.3.2a Section-by-Section Time Allocation Map; nested inside the Novel-Part Spec's window; dates plus Phase Day, Part 41 Area 4):**
[in-story dates plus Phase Day this Chapter occupies, the first day and the last day each as Year, Month, Day and Phase Day (Part 41 Areas 4 and 5); protagonist ages if age-sensitive. Cites Part 41 and never copies its table]

**Threads Carried In:** [thread — source chapter/Area ref — state at entry; for a thread off the page longer than the stretch the author set, a planned re-entry beat (Part 36 Rule 26.4.4)]
**Threads Carried Out:** [thread — intended state at exit — destination if known]

**Opening hook:** [what draws the reader in at the first Area of the Chapter]
**Closing beat:** [what the Chapter ends on and what it hands to the next Chapter]
**New named things met by the reader this Chapter:** [at completion: each new proper name the Chapter put before the reader (person, place, group, thing), with the Area that introduced it, read from the Debuts fields of the Area blocks | — while the Chapter is open; information for the author, nothing counted or limited]
**Build mode:** [whole | by-area] *(Amended 2026-10-07; Rule 2.3.8. `whole`: the Chapter is drafted, audited, confirmed and written whole by `/create-chapter`, with no Area files. `by-area`: the Chapter is written one Area at a time by `/next-area` and condensed by `/chapter-builder`. The default for a new spec is `whole`.)*
**Chapter pacing:** [Fast | Medium | Slow] *(Amended 2026-10-07; Rule 2.3.9. The author's call for the Chapter as a whole, with the one-line reason.)*
**Chapter size target (words):** [N; default the sum of the Area size targets of section 5; the author may raise it, and a raised figure is carried into the Area size targets so the two always agree; no reason note required] *(Amended 2026-10-07; Rule 2.3.9. This is T, the figure the word band of Rule 2.3.10 is worked from.)*

**Protagonist Thread Map (Part 30 P30-7):**

| Protagonist | Presence in this Chapter (viewpoint / on the page / off the page) | Thread state at entry | Intended state at exit |
|---|---|---|---|
| [one row for each of the eight protagonists] | | | |

## 2 — Chapter-Level Tier Scope Bracket Range (authoritative backing store — Part 38 Rule 38.5)

*Tentative low–high range; advisory-in-force per Part 2 Area 9 (never a stop/fill condition;
calibration, not correction). This block is the authoritative source the Tier Scope Brackets
and Part 28 Rule 18.7 Position Header ranges read from while this spec is active.*

| Tier | Range (low–high) | Rationale (one line) | Last readjusted (ref) |
|---|---|---|---|
| Areas in this Chapter | N–M | [rationale] | [ref / spec-build] |

## 3 — Standing Exclusions (verify at build, audit, and every amendment)

- **P30-L8 Forbidden Entities (Locked Canon, Authority Tier 0):** the Three Moon Sects
  (Full Moon Sect, Fallen Moon Sect, Dark Moon Sect), Dragon Mountain, and the Empire of
  Gods may never be planned into any Phase 1 spec item — no beat, debut, thread, allusion,
  or open question may involve them.
- **P30-L9 Sentient Monsters (Locked Canon, Authority Tier 0):** no sentient monster (a
  talking beast; Part 40 Area 11) may be planned into any Phase 1 spec item — no beat,
  debut, thread, allusion, rumour, legend, idiom or open question may involve one. The
  non-sentient beasts Part 30 plans for Phase 1 are not excluded; the World Tree is not a monster. One narrow exception (Canon Amendment 2026-10-19, Law P30-L9): the artifact-made Skyvein lion-kind 'Monster King' may be planned only as the single mention by the unnamed man in Chapter 006 Scene 3.
- **Author-removed concepts:** the "Sapphire Line" (ambient hum/frequency/vibration
  bedrock relay) may never be planned in under any
  name. [Extend this list as further removal directives issue.]

## 4 — P30-L5 Crisis-Density Tracking

**This chapter carries:** [combat / political crisis / cultivation breakthrough / major
revelation / none — list which]
**Rolling 10-chapter window status:** [N of last 10 chapters carry a qualifying element —
Law P30-L5 names about 6 of any 10 as its guide; information only here and in Part 30]

## 5 — Area Blocks

### 5.0 — Scene Map *(Amended 2026-10-07; Rule 2.4.12)*

*A scene may span several Area blocks, several viewpoints and, in a later spec, several Chapters. One row for each scene of the Chapter, in order. Scene IDs `S1`, `S2`, … are unique within the Novel-Part.*

| Scene ID | Area blocks | POV sequence | Scene arc | Scene pacing | Scene word budget | Visible break before | Runs in from / out to | Join state at each Area seam |
|---|---|---|---|---|---|---|---|---|
| [S1] | [e.g. 01-02] | [each POV in order, with the Area block or beat where each takes over] | [a fight: opening, exchanges, turn, end; a conversation: turns and where the reveal lands; otherwise the movement of the scene] | [Fast / Medium / Slow] | [default the sum of its Area targets; stretch per Rule 2.3.10] | [yes / no] | [Chapter ref the scene runs in from or out to | none] | [the exact state at each seam between Area blocks of the scene: position, wounds, who knows what, whose floor it is | not applicable for a one-block scene] |

### Area [N] — [Area Name]
**Purpose:** [what happens in this Area, 1–3 sentences; the scene it is, or the part of a scene it carries]
**Want, obstacle, stake:** [what the viewpoint character wants; what stands in the way; what it costs to act or to fail to act; the planned turn, if any; the planned outcome, if the plan has one: win / win at a cost / loss / loss that teaches]
**Viewpoint:** [character; a change of viewpoint falls between Areas, so the Viewpoint fields of consecutive Areas record it; for a Dual-POV Area, both characters]
**Dual-POV Area:** [no | yes — the two viewpoint characters, named (Part 2 Rule 4.3.1)]
**Area status:** [PLANNED / DRAFTED / WRITTEN(P.S.P.CCC.AA) / DROPPED; in a `whole` Chapter the Chapter reference, WRITTEN(P.S.P.CCC) *(Amended 2026-10-07)*]

**Plan of the Area**
- **Pacing (planned):** [Fast / Medium / Slow, for the whole Area; the planner's recommendation with its anchor-type reason, confirmed or changed by the author in the build; carried to the Area as written]
- **Size target:** [1,600 / 1,800 / 2,000 words, chosen in the build; set apart from pacing; for a `by-area` Chapter the passing range is 1,280 to 2,400 words and a count outside it is a blocking finding, Rule 6.1.4; for a `whole` Chapter the author may state a raised or custom figure and the Area block is written to the word band of Rule 2.3.10 *(Amended 2026-10-07)*]
- **Budget stretch:** [none | up to 0.72 of target, with a one-line reason; only a `whole` Chapter carries a stretch, `by-area` Chapters read `none` — Rule 2.3.10] *(Amended 2026-10-07)*
- **Scene anchors:** [anchor 1; anchor 2; … the beats of the Area in order; the last anchor is where the Area ends]
- **Continuation:** [complete scene in this Area | the scene continues in the next Area, and what stays live where this Area ends; in a Chapter with a Scene Map the field agrees with its row of section 5.0 (Rule 2.4.6)]
- **Planned time skips:** [after anchor a — how much time — why (story context) — shown with ⁂ | none]
- **Fight (optional):** [tier E1 to E7 and duel type — sides and number — terrain and its one tactical feature — stakes and cost — Named Moves planned (new or established) — turning point — end class (the victory condition or a draw) — shape (duel, ambush, siege, escort, spar or endurance) and how it differs from the last fight | none]
- **Sensory anchor (optional):** [required — the plan demands a concrete sensory anchor for this Area | unset]
- **Tone or voice (optional):** [`TONE: …` / `VOICE: …` | unset — the drafter decides. For a scene that is single-register by nature (a chase, a grief scene), name the one register; Part 36 dimension 16-I reads it as the designation]
- **Content (optional):** [`CONTENT: …` | unset — the drafter decides under Part 28 Area 12.3]

**Opening, closing and connection**
- **Opening type:** [continues directly / time jump / cut to another thread / flashback, memory, dream or vision / in medias res / quiet opening] — [detail; "repeat on purpose: …" where the previous Area opened the same way]
- **Closing type:** [cliffhanger / turn or reveal / resolved / quiet landing / question left open]
- **Carry-over from the previous Area:** [what the reader and the characters know, where everyone is, what is unresolved; for an Area that continues the previous Area's scene, the exact state the previous Area left: the same place, moment and register]
- **Thread or storyline:** [thread — last Area of this thread (ref) | first Area of this thread]
- **Cross-references (optional):** [earlier and later Areas this Area connects to, by reference code]

**Story link and change**
- **Serves:** [Part 30 Section mandate and protagonist arc, by function name; a Part 30 pillar may be cited by its ID]
- **Change:** [what is different at the end of the Area]

**Setups and payoffs (optional; Planted here is required when the Closing type is cliffhanger, Rule 2.4.5)**
- **Planted here:** [item — foreshadowing / question / mystery / motif — pays off in (Area ref)]
- **Carried or paid off here:** [item — planted in (Area ref) — carried / paid off]
- **Consequences landing here (optional):** [pending cascade — whose, from which event (a character ledger Section 6 Pending Consequence Cascade) — how it shows in this Area | none]

**Emotional line**
- **Per viewpoint character:** [character — feeling at the start → feeling at the end, each written as a Part 26 Area 16 state, with the PIS grade when it is 3 or more (Standard N26-9)]
- **Reader and character knowledge (optional):** [the reader's row of the Part 24 N24-1 knowledge map: what the reader knows that a character does not, and the reverse]
- **Key secrets (optional):** [secret — the Part 24 N24-1 knowledge map for it: for each person who matters and for the reader, knows, believes (false), suspects, conceals, how learned, at the start → at the end]

**World, setting and people**
- **Place, in-story time, weather and light:** [place (ledger ref) — day or day range as dates plus Phase Day inside the Chapter window (Part 41 Areas 4 and 5), time of day, time since the previous Area, ages where age matters — weather and light; a stated distance or journey time cites its Registry B row (Part 14 Rule 8.4.1)]
- **Present:** [characters on the page, with the speakers expected to be new; ledger refs by name]
- **Debuts:** [each entity this Area is planned to introduce, by name | none]
- **Lore and world beats delivered (optional):** [lore or world facts the Area gives the reader]
- **Ledgers expected to change:** [ledger entry by name — what changes: power, resources, relationships, current condition, state]

**Novel elements carried:** [element names from the Part 36 element lookup table]
**CDL-2 emphasis:** [the Part 35 categories this Area is expected to score in]

*(one Area block for each Area of the Chapter, in the order planned)*

## 6 — Completion Record

[Written at completion (Rule 3.7.1); reads "not yet written" until then.]
**Final Variance Summary:** [written at [NEXT CHAPTER] time or by `/chapter-spec complete`]
**Reader now knows:** [a short list, by reference code, of what the reader has been shown by the end of the Chapter; it seeds the next spec's Carry-over]
**Chapter digest:** [the text /chapter-summary prints for the Chapter: for each Area what changed, who and the open threads; then the accepted sameness patterns and the accepted variances, each with its Area reference]

## 7 — Audit and Settlement Notes

[The last section of the file. Every settled, open, deferred, skipped, inherited, provenance, name-status, variance and audit note, each pointing to the plan item it concerns (Rule 38.14; section 9.10). Variance log lines are kept here with date, trigger (Gate 2 ref or command), the variance or status change, and whether it traced to a DCG answer.]
```

### 2.2a — The Behavioral Plan Block

Each per-Area block in the template above additionally carries a **Behavioral Plan**, whose content model is owned by Part 39 (Character Behavioral Synthesis Law) Area 46 and whose structure is owned by this Part. It is built during the `/chapter-spec` flow alongside the beat plan — never appended afterward — because Part 39 P39-2 requires conduct to be settled before the Area is written in the same way events already are.

**Monsters in an Area.** A monster that appears in an Area is listed in the Behavioral Plan beside the characters, by Kind (and by name and tier when it is an Individual), with the trait lines of Part 40 Area 5 that the Area will show; the Kind's Baseline traits are the plan, and a spec never invents a trait the Kind entry does not hold. A non-sentient monster has no Part 39 registration status; the Kind is `defined at this Chapter Spec` when the Chapter Spec is the one that defines it (Part 40 Rule 40.7.5.1). A sentient monster may not be planned into Phase 1 (Law P30-L9).

```markdown
#### Behavioral Plan (Part 39)

**Characters appearing:** [name — tier — Part 39 registration status]
**Active collective code(s):** [faction / location code, cross-referenced to its ledger]
**Signatures expected to fire:**
| Character | Signature code | In which beat | Repetition position (information) | Fired in Area (written at Gate 2) |
|---|---|---|---|---|

**Waiting beats planned (L29):** [character — beat]
**Contradiction or cost rendered:** [character — which, and where]
**Transmission rendered (L16):** [caregiver to dependent — behavior — where | none]
**Anticipated drift:**
| Character | Trigger | Class | Mapped? | Expected dimension change | Permanence |
|---|---|---|---|---|---|

**Off-register act planned:** [character — act — how it is marked | none]
```

**Rule 38.2.2a.1 — Unregistered characters block the plan.** A chapter spec that plans an acting appearance for a character holding no tier-compliant Part 39 registration records that fact as a blocking item. The registration is completed before the Area is drafted (Part 39 Rule 39.4.3.1).

The rule above applies to every registered tier. Part 19's Depth Spectrum has a fourth band, **Tier D — Named Conversational**, whose whole registration is a single row in `ledger-character-side/_index.md` written at Gate 2, and the rule meets it as follows:

- **Planning a Tier D character to SPEAK is NOT a blocking item.** The tier exists so that a planned conversation can have two sides without a full registration standing in the way. A spec is not required to name them — they are ordinarily introduced by the drafting agent inside the Area — and a spec that does name one records them as Tier D and carries no block.
- **Planning a Tier D character to ACT CONSEQUENTIALLY is FLAGGED TO THE AUTHOR, who rules every time.** A planned choice, a planned beat, or a planned story-state decision sits outside what the tier covers on its own — but **nothing promotes automatically**, and the planning agent does **not** decide the remedy. It surfaces the moment, states what the character would do and why it reads as consequential, and the author rules: **promote to Tier C**, or **keep them Tier D and let the moment stand**. Both outcomes are lawful. Recasting the act as conversation to avoid the question remains barred — the point is that the author sees it, not that the beat is softened.
- **Recurrence NEVER promotes and speech NEVER promotes.** A Tier D character may appear in any number of later Areas, and speak in all of them, without triggering anything.

**The spec-time test is the draft-time test:** *does the story have to remember what they did?* If no, it is talk and Tier D covers it; if yes, it is outside the tier. The Part 39 side of this reconciliation is Rule 39.4.3.1a and the note at Rule 39.46.2.3. **Behavioral Plan consequence:** a Tier D speaker owes no Signature row, no waiting beat and no drift row in the Area 2.2a block, because they carry no registered profile; where a spec lists one at all, the entry is the name, the descriptor and the word *Tier D*.

**Rule 38.2.2a.2 — Anticipated drift is a plan, not an establishment.** The Spec Authority Model of Area 1 applies unchanged: the ledger supersedes the spec, and a behavioral drift becomes canon only when it executes and is logged to Character Ledger Section 12 at Gate 2. A drift row in a spec never establishes a behavioral fact.

**Rule 38.2.2a.3 — Behavioral questions route through the Decision Consultation Gate.** Where the Behavioral Plan cannot be completed without an author decision — an unmapped trigger the chapter will reach, a Part 39 Layer that must open — the question is raised in the Part 28 Area 19 DCG during spec build (Area 4 of this Part), not left to surface mid-draft.

### 2.3 — Field Law

**Rule 2.3.1 — Name-chain and ref prefix.**
The header carries the full name-chain (Part 28 Rule 18.3.4 readability standard) and the numeric ref prefix `Phase.Section.Part.Chapter` (e.g., `1.1.1.002`). Phase and Section names are Locked Canon (Part 30) and are always shown as locked; Novel-Part, Chapter and Area working titles are `proposed` until their first Gate 1 delivery that is confirmed and written, then `locked-at-Gate-1` with the establishing Area ref (Part 28 Rule 18.4.4); each name's status is a Name note in the Audit and Settlement Notes. A `proposed` working title is a genuine proposal — the delivered name may differ (recorded as variance), and Part 28 Rules 18.4.1–18.4.3 register/uniqueness/coherence standards apply to it as a candidate, not as an established name. The Section Spec carries the name-chain through the Section and the ref prefix `P.S`, and the Novel-Part Spec carries it through the Novel-Part and the ref prefix `P.S.P` (Rules 10.3.1 and 11.3.1). In both, the Phase and Section names are shown as locked as here, while a Novel-Part or Chapter name is only a working label and carries no Establishment status; Part 28 Rules 18.4.1–18.4.3 apply to those labels as advice.

**Rule 2.3.2 — Chapter purpose cites Part 30, never copies it.**
The purpose block cites Part 30 Section mandates **by function name** ("the Section 1 Diplomacy Scene mandate," "Law P30-L4," "§1.3.2a window") and never reproduces mandate text. Part 30 remains the single source; a spec quoting Part 30 rule text is a Rule 1.4.2-class duplication violation. The same holds for the purpose lines of the Novel-Part Spec and the Section Spec, and for the Section Spec's block of what Part 30 expects, which holds citations only (Rule 10.3.2).

**Rule 2.3.3 — Pacing is decided in the Chapter Spec and carried.**
The Area block's Pacing (planned) field records the pacing of the whole Area: Fast, Medium or Slow, with the planner's one-line anchor-type reason, asked in the build as its own question and kept apart from the size target. The author confirms or changes it in the build, and the value then stands as the Area's pacing. Fast, Medium and Slow are the vocabulary the spec records; they are not a rule tied to the size of the Area, and no pacing-to-words relation exists. At Area-writing time the pacing is carried: no pacing question is asked at Gate 1, and the area-maker writes the Area at the pacing the Chapter Spec records. A change of pacing is a change to the Chapter Spec (a light amendment, Rule 3.5.2, which re-confirms nothing), made through `/chapter-spec revise` or recorded when the author rules it at a Decision Consultation Gate, and the Gate 2 sync then writes the new value as the plan (Rule 3.6.1 item 7).
*Amended 2026-10-07.* Pacing is recorded at four grains, each asked in the build and each the author's call: the Chapter (Rule 2.3.9), the Area block (this rule), the scene (the Scene Map, Rule 2.4.12) and, for the larger plans, each Chapter of a Novel-Part and each Novel-Part of a Section (Rules 11.3.7 and 10.3.9). The guidance the planner gives with the question is that fights are usually Fast; intrigue, deception, lore and thought are usually Slow; dialogue is usually Medium; the author decides, because it depends on the story. In a `whole` Chapter the pacing shapes the writing (Fast: tight, short beats; Medium: balanced; Slow: fuller interiority, sensory and world detail) inside the same word band for every pacing (Rule 2.3.10).

**Rule 2.3.4 — Debuts and naming interfaces.**
The Debuts field lists every entity the Area is planned to introduce. Each is recorded, in the Audit and Settlement Notes, with an Establishment-Rule flag (the name is `proposed`; establishment occurs only when the Area is delivered at Gate 1 and confirmed, per Part 28 Area 20.3) and its consultation status under the Part 28 Area 20.4 Major/Minor split and `.claude/guardrails/quality/guardrail-entity-naming-law.md` — MAJOR entities show `consulted [date]` (a spec-build consultation counts and settles the name-choice question per Area 4) or `consultation pending (DCG at Area time)`; MINOR entities show `minor — AI-named autonomously at drafting`.

**Rule 2.3.5 — CDL-2 emphasis targets.**
The CDL-2 emphasis field names which of Part 35's content categories (as Part 35 Area 1.2 names them) the planned Area is expected to score in, chosen from the Area's story; the active Section targets (Part 35 Area 3) and the Universal Anchor Floors are shown beside it for information. Emphasis notes are planning aids; scoring itself remains wholly Part 35's (area-scorer's) province and is never pre-judged by the spec.

**Rule 2.3.5a — Sensory anchor tag.**
An Area block may carry the optional Sensory anchor field set to `required` when the plan demands a concrete sensory anchor for that Area. The spec is the only place that requirement is set: an Area whose block carries it must leave the reader at least one concrete, specific sensory anchor (Part 36 Area 9.3); an Area whose block does not is judged under Part 36 Area 9.1, a quality law and not a quota law.

**Rule 2.3.5b — Tone and voice tags.**
An Area block may carry the optional Tone or voice field (`TONE: …` and `VOICE: …`). The words inside are the author's; what a register or a voice means and how it is rendered is Part 36's (Areas 12, 18 and 19). The field is optional: an Area with no entry is `unset`, and the drafter decides tone and voice under Part 36 exactly as when no field exists. An entry the author sets is an instruction: the drafter follows it, Check #18 lists it (Rule 6.1.1(d)) and the Part 36 dimensions test it. An entry that designates a single register for an Area is the spec designation that Part 36 dimension 16-I (Register Range) recognizes. The build never puts a tone or voice question to the author: every Area block shows the field as `unset` until the author sets it, in the build, in an amendment or in a Decision Consultation Gate answer.

**Rule 2.3.5d — Content tag.**
An Area block may carry the optional Content field (`CONTENT: …`) beside the sensory anchor and the tone and voice fields. The words inside are the author's; the limits themselves, and what a tag may and may not move, are Part 28 Area 12.3. The field is optional: a block with no entry is `unset`, and the drafter decides the level under Part 28 Area 12.3 exactly as when no field exists. An entry the author sets is an instruction: the drafter follows it, Check #18 lists it (Rule 6.1.1(d)) and Part 36 dimension 16-D tests it.

**Rule 2.3.5e — Size target.**
Each Area is written to one of three size targets: **1,600, 1,800 or 2,000 words**, decided in the Chapter Spec for that Area (Part 2 Rule P2-Area-7). The passing range is **1,280 to 2,400 words** (the three targets with 20 percent variation on both sides: 1,280–1,920, 1,440–2,160 and 1,600–2,400, read as one range). A count outside 1,280 to 2,400 words is a blocking finding: the write waits for the author to confirm the Area or send it back (Rule 6.1.4). The size target is not tied to pacing: a Fast Area may carry any of the three targets, and so may a Slow one.
*Amended 2026-10-07.* The passing range of 1,280 to 2,400 words and the blocking finding apply to a `by-area` Chapter, written an Area at a time. In a `whole` Chapter the Area block is not a file and is measured against the word band of Rule 2.3.10 (55 to 60 percent of its size target, counted in words), and the 1,280 to 2,400 range is not applied. In a `whole` Chapter the size target is one of the three figures by default and the author may state a raised or custom figure at spec time, with no reason note required.

**Rule 2.3.6 — Statuses and the notes that record decisions.**
The body of a spec holds no inline tag (Rule 38.14). Every decision the author answered at the build is a Settled note in the Audit and Settlement Notes (the settling record Area 4 relies on); every open question is an Open note; every decision the author skipped at the build (Rule 3.2.2) is a Skipped note, which records the planner's choice and is not a settled item (Rule 4.1.2); every deferral the author chose is a Deferred note naming where the question goes (a later spec, or Area writing); every item a lower spec took from the spec above it is a From note, and every settled item it inherited is an Inherited note (Rules 9.3.1 and 9.5.2; section 9.10). Each note points to the plan item it concerns. Per-Area status is exactly one of `PLANNED / DRAFTED / WRITTEN(ref) / DROPPED`; `WRITTEN` always carries the full reference code (*Amended 2026-10-07:* for an Area block of a `whole` Chapter the reference is the Chapter reference, `WRITTEN(P.S.P.CCC)`, because no Area file exists). `DROPPED` Areas are kept (with a variance note), never deleted — the spec preserves its own planning history.

**Rule 2.3.7 — Standing exclusions and crisis density.**
The standing-exclusions block (P30-L8 entities and P30-L9 sentient monsters, save the one narrow artifact-made exception of Canon Amendment 2026-10-19 (Law P30-L9); author-removed concepts, currently the Sapphire Line) is mandatory in every spec and is checked at build, at the light continuity audit, and at every substantial amendment. The P30-L5 row tracks whether the chapter carries combat / political crisis / cultivation breakthrough / major revelation and the rolling ten-chapter count (about 6 of any 10 is Part 30's guide); the row is advisory instrumentation here — the law itself is Part 30's. The standing-exclusions block and the P30-L5 row stay at Chapter grain. The Section Spec and the Novel-Part Spec carry the exclusions by reference to template section 3 of the Chapter Spec, without pasting the list, and every audit of theirs verifies them.

**Rule 2.3.8 — Build mode (Amended 2026-10-07).**
The Chapter Spec header carries `**Build mode:** whole | by-area`. A Chapter is built by one of two paths. `whole`: `/create-chapter` drafts, audits, confirms and writes the whole Chapter in one cycle from the confirmed Chapter Spec, with no Area files; the Area blocks of the spec are plan units and the Area rows read `WRITTEN(P.S.P.CCC)`. `by-area`: `/next-area` writes one Area per invocation and `/chapter-builder` condenses the written Areas into the Chapter file pair. The default for a new spec is `whole`; the author names `by-area` at the spec or asks for it later. `/create-chapter` refuses a Chapter that has Area files; `/next-area` and `/chapter-builder` refuse a Chapter whose Build mode is `whole` once it has been built whole. Changing the Build mode of a Chapter with no written text is a light amendment (Rule 3.5.2); changing it for a Chapter that has been written is not allowed except by `/redraft-chapter`, which archives the written Chapter first. Pacing and size are still the author's decision, recorded in the spec, whichever mode is set; the Build mode changes how the Chapter is written and measured, never who decides.

**Rule 2.3.9 — Chapter pacing and Chapter size target (Amended 2026-10-07).**
The Chapter Header Block carries `Chapter pacing:` (Fast, Medium or Slow, with the one-line reason) and `Chapter size target (words):` (T). T is the sum of the Area size targets of section 5 by default; the author may raise it, and a raised T is carried into the Area size targets so that T always equals their sum. Both are asked in the build as their own questions, with the guidance of Rule 2.3.3, and the author may raise any budget at the question. Chapter pacing is the Chapter's overall register; each Area block and each Scene Map row keeps its own pacing, which may differ from it. A `whole` Chapter whose Chapter pacing, Chapter size target, Area pacing, Area size targets or Scene Map is missing cannot be confirmed and cannot be built (Rule 2.4.2).

**Rule 2.3.10 — The word band and the budget stretch (Amended 2026-10-07).**
Words are counted, not characters; date lines, hidden Area markers and scene-break marks are not counted. A `whole` Chapter writes each Area block at **55 to 60 percent of its size target**. The allowed Chapter total is **0.55 T up to 0.72 T** (0.72 is 1.20 times 0.60, a stretch of 20 percent above the band top; for T of 8,000 the total runs from 4,400 to 5,760). Each Area block carries `Budget stretch:` set to `none` or to `up to 0.72 of target` with a one-line reason. Only an Area block that names a stretch may exceed 60 percent of its target, and never beyond 72 percent; no Area block goes below 55 percent. A stretch the spec does not name is refused. The band is a budget the spec records and the author decides; it is not a craft preference of the writer. The 1,280 to 2,400 passing range of Rule 2.3.5e is not applied to a `whole` Chapter and is replaced by this band check at Gate 1 (Rule 6.1.5); the by-area Chapters, Chapter 001 among them, are unaffected.

### 2.4 — The Area Block: the Bible That Connects the Story

**Rule 2.4.1 — What the Area block is.**
An Area block plans one written Area and places it in the story around it: what the Area is, how it opens and closes, what it takes in from the Area before it and what it hands to the Areas after it. The Area is the written unit of the by-area path: it may be a complete scene, or a scene may continue across consecutive Areas of the Chapter (Part 2). In a `whole` Chapter (Rule 2.3.8) the Area block is a plan unit and the Chapter is the written unit, and the Scene Map (Rule 2.4.12) says which blocks make each scene. The planner, the drafter, the checker and the sync all read the block, and it is the one place where the Areas of a chapter are joined into a single line of story. Its content is intent: it never establishes a canon fact (Rule 1.3.2) and never restates ledger content (Rule 1.4.2).

**Rule 2.4.2 — Fields, required and optional.**
The fields are those of the template (Rule 2.2.1, section 5). Area blocks are numbered `01`, `02` and so on, to match the `AA` of the reference code `P.S.P.CCC.AA`. Every field is required unless the template marks it `(optional)`. A required field is never blank: it holds a value or, where its rule allows, `none`. While a build runs, a field not yet answered is recorded as an Open note; at `[CONFIRM SPEC]` a field holds an answer, a skipped choice or an author deferral, each recorded in the notes (Rules 9.5.2 and 9.6.3). An optional field holds a value, `none` or `unset`. Scene anchors, Continuation, Pacing (planned) and Size target may not be left open at `[CONFIRM SPEC]`, because they are captured during spec formation. A spec with a blank required field cannot be confirmed (Rule 3.3.2(f)). *Amended 2026-10-07:* in a `whole` Chapter, Budget stretch, the Chapter pacing, the Chapter size target, the Build mode and the Scene Map (section 5.0) are required in the same way, and `/create-chapter` stops when any of them, or an Area block's pacing, size target or scene assignment, is missing.

**Rule 2.4.3 — Opening types and closing types.**
The two lists are fixed; a spec uses these words and no others. When the author uses a word that is on neither list, the planner shows the nearest listed word (a hook is a cliffhanger or a turn or reveal; a quiet image is a quiet landing), the author confirms it, and the author's own word is kept in the detail beside the type.
- Opening types: `continues directly` (begins in the place and moment the previous Area ended); `time jump` (the same line of story after a stated gap in time); `cut to another thread` (a different thread, place or group of people); `flashback, memory, dream or vision` (a moment from before the story's present, or a scene outside its ordinary present such as a dream or a vision); `in medias res` (begins inside a moment already under way); `quiet opening` (an unhurried entry into a place or a person's ordinary moment).
- Closing types: `cliffhanger` (stops at the peak of a live danger or choice); `turn or reveal` (ends on a change of direction or a fact shown for the first time); `resolved` (ends with its question answered); `quiet landing` (ends at rest after its movement); `question left open` (ends on a question the reader carries forward).
The detail beside an opening type says what the type needs: how long the jump, which thread or place the cut goes to, which past moment a flashback or memory returns to, and what source a dream or a vision has (Part 36 Rule 27.3.1).

**Rule 2.4.4 — Carry-over and opening variety.**
Every Area knows what happened in the Area before it (Part 2 Rule P2-Area-2). Carry-over records what the reader and the characters know at the opening, where everyone is and what is unresolved; the first Area of the story records `story start`; it has no Area before it, so its Opening type is `in medias res`, `quiet opening` or `flashback, memory, dream or vision`. For the first Area of a chapter the previous Area is the last Area of the previous chapter, so the rule runs across chapter boundaries. An Area that returns to an earlier thread records that thread as the reader last saw it, in the Area named under Thread or storyline. Consecutive Areas do not open the same way unless the spec says so: an Opening type equal to the previous Area's carries "repeat on purpose:" and the reason. An Area that continues the previous Area's scene (by its Continuation field or by the Scene Map, Rule 2.4.12) opens `continues directly` by Rule 2.4.6 and needs no repeat note. What the opening looks like on the page (its construction, images and first words) is Part 36's (Area 20 and the Area flow review of Check #16); the spec decides the type.

**Rule 2.4.5 — Cliffhangers, cuts and cut-backs are planned events.**
A break in time, place or thread between Areas is lawful only when the spec plans it (Part 2 Rule P2-Area-3 and Area 1 section 1.5.6); the plan is the Opening type of the Area after the break, with its detail. A cliffhanger, a cut away and the cut-back that returns to the interrupted thread are planned together: the Area that ends on a cliffhanger names, under Planted here, the Area that resolves it (or the question is recorded open in the notes); the Area that cuts away records in Carry-over the moment left hanging; the Area that cuts back names the interrupted Area under Thread or storyline and records that moment in Carry-over. A gap between Areas that no Opening type accounts for is a spec finding (Rule 3.3.2(f)); the same gap appearing in the Area without a planned Opening type is a Check #18 core difference (Rule 6.1.1).

**Rule 2.4.6 — Scene anchors, continuation and the Area as the written unit.**
The Area is the written unit. It may be a complete scene, or a scene may continue across consecutive Areas of the Chapter. The block lists the scene anchors, the beats of the Area in order, and the Continuation field says which it is: a complete scene in this Area, or a scene that continues in the next Area, with what stays live where this Area ends. The Area-to-Area carry-over rule of Part 2 (Rule P2-Area-6) governs the join: an Area that continues the previous Area's scene opens in motion from the exact state the previous Area left (the same place, the same moment, the same register) with no second opening and no recap, and its Opening type is `continues directly`; an Area that continues its scene into the next Area ends on live tension, so its Closing type is `cliffhanger`, `turn or reveal` or `question left open`, and never `resolved` or `quiet landing`. A scene is cut across Areas where a beat boundary falls, never at a word count. The planner proposes the anchors and, where a scene runs on, the Area at which each part ends, with the reason; the author confirms or changes them in the build. The bracket row "Areas in this Chapter" (template section 2) is written to contain the number of Areas planned and stays advisory (Rule 5.2.1). Where an Area as written runs on past its planned end or ends a scene sooner, the author may move the boundary, and the sync records it (Rule 3.6.1 item 5). *Amended 2026-10-07:* a scene continues across Area blocks by the Continuation field of the by-area path or by its row of the Scene Map (Rule 2.4.12), whichever the Chapter's Build mode uses; where both are present they agree, and the Area-by-Area rules above stand unchanged for a `by-area` Chapter. In a `whole` Chapter the join state at each seam is the Scene Map's column of that name.

**Rule 2.4.7 — Viewpoint is per Area.**
Each Area has one viewpoint, recorded in its Viewpoint field, except an Area the author marks as a Dual-POV Area. The Dual-POV Area field of the block reads `no` or names the two viewpoint characters (Part 2 Rule 4.3.1); the Area Maker never sets the mark itself, and the author confirms it at `[CONFIRM SPEC]` or sets it live at a Decision Consultation Gate, when the Gate 2 sync writes it. A change of viewpoint falls between two Areas, so the Viewpoint fields of the two blocks record it and no further entry is needed; where the new Area continues the previous Area's scene, its Carry-over says so. A viewpoint change or a Dual-POV mark that no Area block records is a Check #18 core difference. The change does not suspend the carry-over rule: the new Area begins where the last ended (Part 2). *Amended 2026-10-07:* the POV sequence column of the Scene Map (Rule 2.4.12) records every viewpoint of a scene in order, with the Area block or beat where each takes over; it agrees with the Viewpoint fields of the blocks, and a takeover at a beat inside an Area block makes that block a Dual-POV Area, set by the author as above.

**Rule 2.4.8 — Planned time skips are catalogued.**
A brief time skip inside an Area (the same place, the same people and the same dramatic movement, only the clock having moved on) is shown by the ⁂ mark (Part 2 Rule 6.3.5). Each skip is listed under Planned time skips: the anchor it follows, how much time passes and why. A break longer than the scene can hold, or one that changes the place, is an Area break, planned as the next Area's Opening type (Rule 2.4.5). A ⁂ in the Area with no listed skip is a Check #18 core difference.

**Rule 2.4.9 — The Area status.**
The Area status is exactly one of `PLANNED` (no draft yet), `DRAFTED` (a chat-accepted draft that is not written to file), `WRITTEN(P.S.P.CCC.AA)` (written at Gate 2; *Amended 2026-10-07:* `WRITTEN(P.S.P.CCC)` for an Area block of a `whole` Chapter, written by `/create-chapter`) and `DROPPED` (kept with a variance note). It is set by the Gate 2 sync and the reconciliation pass and never by hand. The written Area is the Area-close event for the checks and commands that read it: the Area flow review of Check #16, the Area-close enquiry of Check #21 (Part 39 Area 44), the Area-level CDL-2 block (Part 35) and the `/next-area` readiness test. A count outside the size range of Rule 2.3.5e is a blocking finding: the write waits for the author to confirm the Area or send it back (Rule 6.1.4).

**Rule 2.4.10 — What the remaining fields record.**
The fields not governed by a rule above record the following.
- **Want, obstacle, stake.** What the viewpoint character wants in this Area, what stands in the way, what it costs to act or to fail to act, the planned turn, if any, and the planned outcome where the plan has one (win, win at a cost, loss or loss that teaches). It is the plan of what Part 36 asks the reader to see: the character's want, fear and cost (Area 2.1(a)), the turn (Rule 20.2.1) and the personal stake (Rule 25.2.1). The planner proposes it from Part 30, the ledgers and the Area before it, and the author edits it in the build; it is intent and establishes nothing (Rule 1.3.2).
- **Fight.** An optional line for an Area that holds a combat event. Part 5 (Rule IP-1) asks that every combat event be classified, and this line is where the plan says how. It records the escalation tier E1 to E7 and, for a formal duel, the duel type (Part 5 Area 5); the sides and their number; the terrain and its one tactical feature; the stakes and the cost; the Named Moves planned, new or already established (Part 6); the turning point; the end class, which is the victory condition or a draw (Part 5 Area 12); and the fight's shape (duel, ambush, siege, escort, spar or endurance) with how it differs from the last fight. Two fights in a row of one shape are reported, never failed (Part 36 Dimension 16-J Read 2, item k). It gives the reviewer a planned tier to read the draft against and gives the writer a place to plan the fight. A Named Move listed as new is a proposal until its Area is confirmed (Rule 1.3.2). An Area with no combat reads `none`. Check #18 lists the line with the other listed elements (Rule 6.1.1(d)). *Added 2026-10-17 (Part 44, Canon Amendment):* for an Area with a fight the line also carries the **Engagement Ledger** of Part 44 Area 5.2, made at the build and fixed before drafting: both sides' anchors, each fighter's realm and Level, role, pairing, gap in minor steps, offset used and expected outcome, any registered gifted fighter, the price paid and the strain notes. It is a plan record and establishes nothing; Gate 1 Check #23 measures the text. The light continuity audit (Rule 3.3.2) lists, report-only, a fight Area with no Engagement Ledger. *Added 2026-10-19 (Part 45, Canon Amendment):* for an Area with a fight the line also carries the **Situation line** of Part 45 Area 12: the ground and space, light and weather, the postures that matter, the people to protect, the intent, the energy budget of each named fighter and the moves the fight may use as a menu with the situation each fits; never an order of moves and never "link codes met in scene". It is a plan record and establishes nothing; Gate 1 Check #24 measures the text. The light audit lists, report-only, a fight Area with no Situation line.
- **Pacing and size target.** Two separate fields, each asked in the build as its own question and neither tied to the other; see Rules 2.3.3 and 2.3.5e.
- **Connection.** Thread or storyline names a thread as the Chapter Header Block names it (Threads Carried In and Threads Carried Out), so that a thread can be followed from Area to Area. Cross-references list the earlier and later Areas this Area connects to, by reference code (`Phase.Section.Part.Chapter.Area`), so that a later spec and the sync can find them.
- **Story link and change.** Serves names the Part 30 Section mandate and the protagonist arc the Area serves, by function name (Rule 2.3.2); a Part 30 pillar may be cited by its ID. Change states what is different at the end of the Area: a fact, a relationship, a state of a character, something the reader or a character has learned.
- **Setups and payoffs.** Planted here lists each foreshadowing, question, mystery or motif the Area plants, with the Area that pays it off by reference code. Carried or paid off here lists each earlier item the Area carries on or pays off, with the Area that planted it. These two fields are where a setup or a payoff actually lands, and they are the register that Part 36 (Areas 21 to 23) reads. The Section Spec and the Novel-Part Spec each also carry a register of setups, payoffs and threads, as a guide and a suggestion only. The three registers are linked by shared keys, the Part 30 Setups-table row number or a short thread name: the Section Spec says in which Novel-Part a setup is planted and in which it pays, the Novel-Part Spec says which Chapter plants and which pays, and these Area fields say where it truly lands. The story may plant elsewhere, pay earlier or later, or drop a setup, and no check, gate or question is created by an unmet suggestion. How long a setup may wait is set by the Section and Novel-Part plan lines, with no figure. `/threads` shows the plan beside what happened as information only (Rule 9.5.4). Part 36 still reads these two fields, and no register ever blocks the story.
- **Consequences landing here.** An optional line listing each pending cascade (a character ledger's Section 6, Pending Consequence Cascades) that the plan lets land in this Area: whose it is, the event it comes from and how it shows. It is intent and establishes nothing (Rule 1.3.2). A cascade the plan places in no Area is not an error: the Chapter Spec decides when a consequence lands, and a cascade past its latest Section is shown to the author as a question, never as a block (Part 27).
- **Emotional line.** For each viewpoint character, the feeling at the start and at the end, judged against that character's own registration only, and written as a Part 26 Area 16 state with the PIS grade when it is 3 or more (Standard N26-9). Optionally, where the reader's knowledge and a character's differ, and, for a key secret, the Part 24 N24-1 knowledge map (who knows it, who believes otherwise, who suspects it, who conceals it and how each learned it, with the reader as a row of its own), at the start and at the end.
- **World, setting and people.** The place, with its ledger entry; the in-story time (the day or day range as dates plus Phase Day inside the Chapter window, and so inside the Section window of Part 30 §1.3.2a, in the forms of Part 41 Areas 4 and 5, citing Part 41 and never copying its table; the time of day, the time since the previous Area and, where age matters, the protagonists' ages at the opening); weather and light; the characters present, with the speakers expected to be new; the debuts; the lore and world facts the Area delivers; and the ledger entries expected to change, with what changes in them (power, resources, relationships, current condition, state), by name and reference only (Rule 1.4.2).
- **Novel elements carried.** The element names, as the Part 36 element lookup table (Area 15.5) spells them, that the Area is built to carry. The governing rules of a named element apply to the Area; naming an element restates none of its rules, and an element left unnamed is not thereby exempt. An element may carry a plain note that names a departure from its usual ingredients, for example `training: a clean win that costs only time`; Part 36 Rule 22.4.2 accepts the departure the note names, and Check #18 lists the note (Rule 6.1.1(d)).

**Rule 2.4.11 — Chapter-level fields.**
The Chapter Header Block (template section 1) carries the chapter's Opening hook (what draws the reader in at the first Area) and Closing beat (what the chapter ends on and hands to the next), and the Protagonist Thread Map: for each of the eight protagonists (Part 30 P30-7), whether the chapter carries them as a viewpoint, on the page or off the page, and their thread state at entry and at exit. The map is a plan. The POV counts reported at Section close are computed from the written Areas (Rule 3.7.2) and are not stored here.

The Epigraph is not a line of a Chapter Spec. It is a line of the Section Spec (Rule 10.3.1): the text, with its source, for the title page that opens the Section. The Phase epigraph is not a line of any spec: it is a line of Part 30, a Phase's first Area prints it, and the Section Spec of a Phase's first Section carries its own Epigraph line like every other Section Spec, so that a Phase's first Area prints two lines, the Phase's and Section 1's own. The author settles a Section's own epigraph when the Section Spec is confirmed and it reads `unset` until then; `unset` means that line is left out, and the title page carries no epigraph only when every line it would print is `unset`; no agent writes one. The command that writes the Area (`/next-area`, which `/start-story`, `/next-section` and `/next-phase` run for the opening Area of a Phase or a Section) passes TWO lines on a Phase's first Area (the Part 30 Phase epigraph and Section 1's own Epigraph from its Section Spec) and only the Section Spec's Epigraph on the opening Area of every other Section; a redraft of a Section's first Area reads them from the same places, so they are not lost. Each epigraph line is the author's, and the author alone settles it.

**Rule 2.4.12 — The Scene Map (Amended 2026-10-07).**
Section 5.0 of the Chapter Spec is the Scene Map: a table with one row for each scene of the Chapter, in order. A scene may span several Area blocks, several viewpoints and, in the larger plans, several Chapters or Novel-Parts. The columns are: **Scene ID** (`S1`, `S2`, …, unique within the Novel-Part); **Area blocks** (for example `01-02`); **POV sequence** (any number of viewpoints, in order, with the Area block or beat where each takes over); **Scene arc** (for a fight: opening, exchanges, turn, end; for a conversation: the turns and where the reveal lands; otherwise the movement of the scene); **Scene pacing** (Fast, Medium or Slow); **Scene word budget** (default the sum of its Area size targets; a stretch is allowed under Rule 2.3.10); **Visible break before** (yes or no); **Runs in from / out to** (the Chapter reference, for a scene that crosses Chapters); and **Join state at each Area seam** (the exact state: position, wounds, who knows what, whose floor it is). Every Area block belongs to exactly one scene of the map. The visible-break rule: a `---` scene break (md) and a centred `*   *   *` (docx) appear only when the scene changes or when the same scene moves to a different viewpoint; when one scene simply continues across Area blocks with the same viewpoint there is no visible break and only the hidden Area marker `<!-- AREA NN -->` in the md. A date line is printed at the top of the Chapter once; a scene whose date differs from the scene before it gets its own date line directly after its break. Same-date scenes do not repeat it. The Scene Map is a plan: it establishes nothing (Rule 1.3.2). It is asked in the build (Rules 3.2.4 and 9.6.2) and is a field of the Chapter Spec like any other; a `by-area` Chapter may carry one, and the Continuation field of each Area block stays and agrees with it. Part Spec and Section Spec carry the same kind of table for scenes that run across Chapters (Rule 11.3.7) and across Novel-Parts (Rule 10.3.9), with the prefixes `PS` and `SS` for their scene IDs.

### 2.5 — Illustration: A Filled Area Block

**Illustration, establishes nothing (Rule 1.3.2).** The block below plans an invented Area with placeholder names (Hero A, the Ford Keeper, Place A, Place B). Nothing in it is canon, and no name in it may be used in a spec or in an Area. It shows how the fields of the template (Rule 2.2.1, section 5) are filled. The settlements, open questions and name statuses it implies are not tags in the block; they are lines of the Audit and Settlement Notes (section 9.10 shows them). The Behavioral Plan block (section 2.2a) is built the same way and is not repeated here.

```markdown
### Area 02 — The Ford at Low Water
**Purpose:** Hero A is stopped at a river ford by the Ford Keeper, who will not let anyone cross until the water falls. The Area is the argument, the wait and the keeper's reason, a complete scene.
**Want, obstacle, stake:** Hero A wants to cross before dark with the sealed letter. The Ford Keeper stands in the way by a rule the keeper holds for a private reason. Waiting costs the day the letter is due; forcing the crossing may cost the pack animal and the letter. Planned turn: the rule turns out to be a grief and not a regulation. Planned outcome: win at a cost.
**Viewpoint:** Hero A
**Dual-POV Area:** no
**Area status:** PLANNED

**Plan of the Area**
- **Pacing (planned):** Medium, because the anchors are a talk and a reveal
- **Size target:** 2,000 words
- **Budget stretch:** none
- **Scene anchors:** Hero A reaches the ford and the Ford Keeper names the rule; the wait on the bank, and a first thaw between the two; the water falls and the keeper gives the reason, which closes the scene.
- **Continuation:** complete scene in this Area
- **Planned time skips:** after the second anchor: about two hours, because the river needs that long to fall; shown with ⁂
- **Fight (optional):** none
- **Sensory anchor (optional):** required
- **Tone or voice (optional):** unset
- **Content (optional):** unset

**Opening, closing and connection**
- **Opening type:** time jump: the same line of story after about a day's walk from Area 01; the gap is stated in the first lines.
- **Closing type:** turn or reveal: it ends on the keeper's reason, shown for the first time.
- **Carry-over from the previous Area:** The reader knows Hero A carries a sealed letter that must reach Place B by noon tomorrow, that the road was empty, and that Hero A left Area 01 angry. Nobody else knows about the letter. Unresolved: whether the letter arrives in time.
- **Thread or storyline:** the letter thread; last Area of this thread: Area 01 of this Chapter.
- **Cross-references (optional):** Area 01 (the deadline is set); Area 05 (the letter is delivered)

**Story link and change**
- **Serves:** the Section's journey mandate and Hero A's arc of learning to wait, each named by function (the real field names the Part 30 mandate and never copies its text).
- **Change:** Hero A has crossed and carries the keeper's reason; the keeper no longer treats Hero A as a stranger; the letter is still undelivered.

**Setups and payoffs (optional; Planted here is required when the Closing type is cliffhanger, Rule 2.4.5)**
- **Planted here:** the second pole the keeper leaves unused by the hut, a motif of someone missing; pays off in Area 05
- **Carried or paid off here:** the sealed letter; planted in Area 01; carried
- **Consequences landing here (optional):** none

**Emotional line**
- **Per viewpoint character:** Hero A: Stressed at the start (tight and impatient); Grounded at the end (quiet and uneasy)
- **Reader and character knowledge (optional):** the reader sees the second pole before Hero A understands it
- **Key secrets (optional):** the keeper's reason: at the start only the keeper knows it, and Hero A begins to suspect it during the second anchor; at the end Hero A knows it; nobody believes otherwise

**World, setting and people**
- **Place, in-story time, weather and light:** Place A, the ford (ledger entry: none yet); day 3 of the Chapter window, written as `<Year, Month, Day> (Phase Day <P>)`; afternoon to dusk; about a day after Area 01; brown river, low gold light
- **Present:** Hero A (hero-a.md); the Ford Keeper (a new speaker)
- **Debuts:** the Ford Keeper
- **Lore and world beats delivered (optional):** none
- **Ledgers expected to change:** Hero A: current condition (a rope burn on the left palm, heals in days); no other ledger change

**Novel elements carried:** Travel, journey; Dialogue; Reveals, secrets; Tension and stakes, irony
**CDL-2 emphasis:** TRAVEL & DISCOVERY; DIALOGUE & SOCIAL INTERACTION; INFORMATION & INTRIGUE; EMOTIONS
```

### 2.6 — The Audit and Settlement Notes Section

**Rule 2.6.1 — The last section of the Chapter Spec.**
Section 7 of the template, the Audit and Settlement Notes, is the last section of every Chapter Spec. It holds every note the body does not carry: Settled, Skipped, Open, Deferred, From, Inherited, Name, Variance and Audit notes, each pointing to the Area or field it concerns (Rule 38.14; section 9.10). The Gate 2 sync, the reconciliation pass and the completion step append their notes there and nowhere else in the file. The Area-time agents read the section with the rest of the spec, because an open item is found there (Rules 4.2.2 and 9.9.2).

---

## Area 3 — Spec Lifecycle

### 3.1 — Build Triggers

**Rule 3.1.1 — Forward build at chapter open.**
`[NEXT CHAPTER]` (C-6) requires the spec chain for the opening Chapter: a confirmed Chapter Spec whose Novel-Part Spec and Section Spec are CONFIRMED or COMPLETED (Rule 9.1.1). The Chapter must also have an entry in its Novel-Part Spec; if it has none, the command stops and offers to add the entry as a light amendment (Rule 9.1.2). `[NEXT CHAPTER]` builds the Chapter Spec only. If the Novel-Part Spec or the Section Spec above the Chapter is missing, DRAFT, AMENDED-PENDING-RECONFIRM or RETIRED, the command stops before anything is written, names the first such link counted from the top and the command that puts it right (`/section-spec` or `/part-spec`), and the Chapter does not open for Areas until the whole chain is confirmed (Rule 9.1.1). `[NEXT PART]` (C-7) and `[NEXT SECTION]` (C-8) are the commands that build the links above a Chapter, each at its own boundary: they build the new Novel-Part Spec (and, for a new Section, the Section Spec before it) and then the first Chapter Spec (Rule 9.2.1); `[NEXT PHASE]` (C-9) is covered by Rule 9.1.4. `[NEXT AREA]` reads the chain at command receipt and **refuses to plan when any link is missing**: it halts, names the first missing link and names the command that builds it (`/section-spec`, `/part-spec` or `/chapter-spec`), and Gate 1 Check #18 backstops this (Area 6). No Area is planned against a Chapter that has no confirmed spec.

**Rule 3.1.2 — Retro-fit (as-built) build.**
A chapter whose Areas predate Part 38 receives an **as-built spec**: built from the written Areas and ledger record, with Area statuses `WRITTEN(ref)` from birth, open questions only where genuinely still open, and a variance note "as-built — reconstructed [date]". As-built specs go through the same audit and `[CONFIRM SPEC]` flow. (The novel starts with no Areas written: Chapter 1 is a forward build.) The same holds for a Novel-Part Spec or a Section Spec built over a Novel-Part or Section that already has written Chapters. Statuses are taken from the record, a field the record does not evidence is left open or deferred as the author rules, and the variance note reads "as-built reconstructed"; Rule 9.8.2. At the start of the story, the Section Spec, the Novel-Part Spec and the Chapter Spec of Chapter 1 are all forward builds.

### 3.2 — The Build Process (Outline-Planner-Led Author Consultation)

**Rule 3.2.1 — Who builds.**
The `/chapter-spec` build is led by the outline-planner: it reads the consolidated canon (Part 30 arc position, Part 2 structure law, this Part), the ledger state, the prior chapter's close and, in full, the Novel-Part Spec and the Section Spec above the Chapter (Rule 9.9.2), then drafts the spec skeleton and drives the consultation. The `/part-spec` and `/section-spec` builds are led the same way, one outline-planner for each level: the Novel-Part Spec build reads the whole Section Spec, and the Section Spec build reads the whole of Part 30 every time. The orchestrating command writes the files, never the outline-planner (Rules 9.9.1, 10.4.1 and 11.5.1).

**Rule 3.2.2 — Iterative, exhaustive-clarity consultation.**
Spec-build consultation follows the Part 28 Rule 19.4 standards at the grain of the spec being built: assistant-proposed concrete options (2 to 3 per question) with the always-available `SKIP — let AI decide` (four in all); no asking what canon already settles; as many rounds as completeness requires — the build is done only as Rule 38.13 defines it, the same definition for all three builds (Area 9, section 9.6): no unasked branch at that spec's own level, a final sweep by the outline-planner and the continuity-checker that returns nothing new, the author's explicit "nothing further to steer", and then the confirm token (exhaustive clarity, per the author's standing "DO NOT ASSUME" rule). Every explicit author answer is recorded as a Settled note; every SKIP leaves the item to planner judgment and is recorded as a Skipped note (a SKIP is NOT a settled item — it does not acquire Rule 19.4 settling power); an item the author chooses to defer is recorded as a Deferred note naming where it goes (a later spec, or Area writing), and the planner never leaves an item open on its own (Rules 9.5.2 and 9.6.3). The author is asked everything that bears on the plan, and nothing is assumed.

**Rule 3.2.3 — Thematic previews on direction options.**
Every direction option presented during spec-build carries a 1–2 sentence narrative preview in Part 36 thematic voice, and exposition-risk options are flagged — the Part 36 Area 13 DCG Thematic Preview Mandate applies to spec-build consultation exactly as it applies to per-Area DCG questions. Part 36 Autonomous Matters are never asked (Rule 4.2.5). The same holds in the Section Spec and Novel-Part Spec builds, Rule 9.6.4.

**Rule 3.2.4 — The build captures every Area's plan.**
The plan of every Area is settled during the build, never left to Area time. For each Area, in chapter order, the planner proposes the scene anchors, the continuation (a complete scene, or a scene that runs on into the next Area, with the reason), the pacing and the size target (two separate questions, Rule 2.4.10; *Amended 2026-10-07:* for a `whole` Chapter also the Budget stretch, and before the Areas the Chapter's pacing and size target, Rule 2.3.9, and after them the Scene Map, Rule 2.4.12, each its own question), the Opening type and Closing type (set against the types of the Area before it), the viewpoint (with the Dual-POV mark, which the planner proposes only where two leads' simultaneous interiority is the scene's point, Part 2 Rule 4.3.1) and the planned time skips, and the author settles or changes them. The planner fills the remaining fields of the block from Part 30, the ledgers and the Area before it and shows them for the author to edit; it asks about them only where a genuine branch exists (a reveal with a Reader-Reveal Timing deadline, a cut away, lore the author owns). The build asks no tone or voice question (Rule 2.3.5b). Before the spec is presented, the planner lays the chapter's run of Opening types and Closing types side by side so the author sees the variety. A retro-fit build (Rule 3.1.2) fills the block from the written Areas: anchors as written, the continuation as written, the types as written, and any field the Areas and ledger give no evidence for as an open note or `none`. The one-line Area outline in a Novel-Part Spec's Chapter entry holds descriptors only. Anchors, continuation, opening and closing types, Area pacing and Area size targets are settled here, in the Chapter Spec, and nowhere above it (Rule 11.3.4). *Amended 2026-10-07:* the Novel-Part Spec and the Section Spec carry only guides for pacing and word budget at their own grain (Chapter pacing and Chapter word budget, Rule 11.3.7; Novel-Part pacing and word budget, Rule 10.3.9); the Chapter Spec settles the Chapter's pacing and size target in its header.

**Rule 3.2.5 — No quick build.**
No `build quick` mode exists for `/section-spec`, `/part-spec` or `/chapter-spec`, and every build follows the consultation of Rule 3.2.2 and Rule 38.13 in full. The per-question SKIP is the only shortcut, and it never settles anything; it is recorded as a Skipped note (Rule 2.3.6).

### 3.3 — Light Continuity Audit

**Rule 3.3.1 — When.**
Every new spec and every substantially-amended spec (Rule 3.5.2) receives a **light continuity audit** by the continuity-checker before the author is asked to confirm. This holds for a spec of each of the three kinds. The audit is report-only. Besides it, every build ends with the final sweep of Rule 38.13, which the same two agents run and which also re-lists every SKIP and every deferral for the author.

**Rule 3.3.2 — Scope (light, spec-grade).**
The light audit checks the plan, not the written Areas: (a) no Locked Canon conflict (Part 30 mandates, §1.3.2a calendar window, Phase 1 power/technology ceilings, with the narrow villain-side technology exception of Canon Amendment 2026-10-19); (b) standing exclusions clean (P30-L8 entities and P30-L9 sentient monsters, save the one narrow artifact-made exception of Canon Amendment 2026-10-19 (Law P30-L9); author-removed concepts); (c) no contradiction of established ledger state (threads-in match the prior chapter's actual close; entities-on-page exist or are flagged as debuts); (d) naming-register sanity on `proposed` names (Part 28 Rules 18.4.1–18.4.3, Area 20.3 methodology) — advisory at spec stage; (e) schema conformance (Rule 38.2) including the Establishment status of every name and the P30-L5 row; (f) Area-block connection: (i) every required field is filled, and every Area has scene anchors, a continuation, a pacing, a size target of 1,600, 1,800 or 2,000 words (*Amended 2026-10-07:* or, in a `whole` Chapter, the raised or custom figure the author stated), and a viewpoint; for a `whole` Chapter the header carries Build mode, Chapter pacing and Chapter size target, every Area block carries Budget stretch, and the Scene Map assigns every Area block to one scene; (ii) each Area's Opening type accounts for its gap from the Area before it (the first Area of the story uses one of the three types that need no earlier Area, Rule 2.4.4), consecutive Areas open differently or carry "repeat on purpose" (an Area that continues the previous Area's scene opens `continues directly` and needs no repeat note); (iii) each cliffhanger and cut away names its resolution or return, and an Area whose scene continues into the next Area ends on live tension (Rule 2.4.6); (iv) every planned time skip is listed and every viewpoint change falls between Areas whose Viewpoint fields record it; (v) setup, payoff and cross-reference codes resolve to Areas that exist or are recorded open in the notes; (vi) every element name appears in the Part 36 element lookup table; (vii) every tag field parses; (g) derivation: the header fields that the Novel-Part Spec's entry for the Chapter pre-fills are consistent with that entry, and each departure from it is noted and shown (Rules 9.3.2 and 9.3.3); the Chapter's calendar window sits inside the Novel-Part window, which sits inside the Section window (Rule 9.3.1; Part 30 Check 11-2); and every inherited item still carries its note (Rule 9.3.1); (h) clean body: the body holds no inline settlement tag, the Audit and Settlement Notes section stands at the end of the file, and every note points to a plan item that exists (Rule 38.14). Findings are reported to the author with the confirmation prompt; blocking findings (a)–(c), (f)(i)–(iv) and (h) must be resolved before `[CONFIRM SPEC]` is accepted. The list above is the scope for a Chapter Spec. The Section Spec and the Novel-Part Spec each have a scope of their own (Rules 10.5.1 and 11.6.1), and the carry-in item (c) is extended to them: a spec built ahead of its time (Rule 9.2.3) is checked against the ledger and the previous unit when its turn comes.

### 3.4 — Confirmation Tokens

**Rule 3.4.1 — The three tokens.**
After build (or substantial amendment), its light audit and the final sweep (Rule 38.13), the author is prompted with exactly three tokens, shared by all three kinds of spec. The prompt, the session-log line and the registry row name the artifact and its ref ("Section Spec 1.2", "Novel-Part Spec 1.2.3", "Chapter Spec 1.2.3.004"). Only ONE confirm prompt is open at a time in a chain, and confirmation runs strictly top-down (Section Spec, then Novel-Part Spec, then Chapter Spec).

- **`[CONFIRM SPEC]`** — the spec becomes CONFIRMED (active). Its settled items acquire Rule 19.4 settling power from this moment (Area 4). The registry row updates, and the new spec file is written at its own `[CONFIRM SPEC]`, so that it is durable at once (Rule 9.4.4).
- **`[REVISE SPEC]`** — the author directs changes; the build loop re-runs (consultation → re-audit if the changes are substantial → re-prompt).
- **`[SKIP SPEC]`** — confirmation is deferred. The spec (if drafted) stays DRAFT with no settling power, and the Rule 38.1 mandate stands: the Chapter remains blocked for Area-producing commands until the whole chain is confirmed. A `[SKIP SPEC]` on any level stops the chain there: no spec below it can be built, no outgoing spec is completed, and the command can be run again (Rule 9.1.1). The skip is recorded in the notes. (`[SKIP SPEC]` defers the work; it does not waive the mandate — only a formal Canon amendment to this Part could do that.)

### 3.5 — Amendment via `/section-spec`, `/part-spec` and `/chapter-spec`

**Rule 3.5.1 — Anytime amendment.**
The author may amend any spec at any time — before, during, or after its chapter's Areas are written — via the command of its kind (`/section-spec revise`, `/part-spec revise` or `/chapter-spec revise`). Amendments are consultation-driven (Rule 3.2.2 standards) and logged in the Audit and Settlement Notes with date and trigger. A spec with children (a Section Spec with Novel-Part Specs, or a Novel-Part Spec with Chapter Specs) runs the cascade report first, and the author decides for each affected child (Rule 9.4.2).

**Rule 3.5.2 — Substantial vs. light amendments.**
**Substantial** amendments — adding/removing/reordering planned Areas, changing a beat's meaning, changing viewpoint or the Dual-POV mark, changing debuts, changing a scene anchor, an Area's continuation, a scene's row of the Scene Map (which Area blocks make it, its viewpoint sequence or its visible break), an opening or closing type, a planned time skip or an Area's thread, changing settled answers, or widening/narrowing the bracket range beyond in-flow readjustment — set status AMENDED-PENDING-RECONFIRM and require the light continuity audit plus a fresh `[CONFIRM SPEC]` before the amended content has any force. **Light** amendments — typo-grade fixes, adding a variance note, changing an Area's pacing or size target, a Chapter's pacing or size target or the Budget stretch of an Area block, recording an in-flow bracket readjustment, setting a status per sync, setting or clearing a sensory anchor, tone, voice or content entry, recording a change the author ruled live at a Decision Consultation Gate (Rule 3.6.1 items 2 and 5) — take effect immediately with a log line and no re-confirmation. For the two other kinds of spec: changing a Novel-Part's or a Section's purpose, its closing state or hand-off, its calendar window or the reveals it owes is substantial; so is adding, removing or reordering the Novel-Parts of a Section Spec (Rule 9.4.2). Adding, splitting, merging or dropping a Chapter in the guide list of a Section Spec or Novel-Part Spec, and appending a variance note, are light. A variance note appended to a higher spec by a lower flow is always light, Rule 9.4.5. Substantial changes to a parent flip nothing below it by themselves; Rule 9.4.2.

### 3.6 — Mandatory As-Built Sync at Every Gate 2

**Rule 3.6.1 — The sync.**
At every Gate 2 execution for an Area in a spec-covered chapter, the **Post-Write Ledger Update continuity-checker instance** performs the as-built spec sync as part of its write pass (the Gate 2 pipeline stays 3-way; spec sync is owned by the ledger-update lane — no fourth lane exists). The write set of the sync is the ledger files, the active Chapter Spec and its registry row. A Section Spec or a Novel-Part Spec is never written at Gate 2; their statuses are derived or are written at the boundary (Rules 9.4.4 and 9.7.3). The sync writes plan-field changes into the Area block and every note into the Audit and Settlement Notes (Rule 38.14):

1. **Status flips** — the written Area's status goes to `WRITTEN(P.S.P.CCC.AA)`; a `proposed` Novel-Part, Chapter or Area name delivered at Gate 1 flips to `locked-at-Gate-1 (ref)`; a `proposed` in-world name flips to `locked-at-Gate-2 (ref)` when its Area is confirmed and written (each recorded as a Name note). When the Area just written is the last Area of the Chapter Spec still to be written, so that every Area is `WRITTEN` or `DROPPED` with its note, the sync also sets the spec's Spec Status to `COMPLETED` and updates its registry row. This is the status only; the completion content is written afterwards, Rule 3.7.1. The Area status `WRITTEN` is a different thing from the spec status.
2. **Deviations → plan corrected, variance noted** — every divergence between the plan and the delivered Area (beat, anchors, viewpoint, title, debuts, entities, order, and any Area-block field the Area bears on) is recorded as a Variance note. A core divergence carries the reference of the author answer that traced it (Check #18 already verified one exists, Area 6); a listed divergence accepted by `[CONFIRM WRITE]` carries the note `accepted at Gate 1`, and a sameness pattern that the audit report listed and `[CONFIRM WRITE]` accepted is recorded as `sameness accepted at Gate 1: <pattern>` on the Area it was reported on, so that `/chapter-summary` and the Chapter digest can list it. The written value replaces the planned value in the block, and the planned value is kept in the Variance note. Where the field is the Area block's in-story time, the written value is the date the written Area's date line states, and the as-built in-story time mirrors the calendar ledger, which owns every recorded date (Part 41 Areas 5 and 9); the sync never writes a second, different date, the planned date stays in the Variance note as this item says, and on a difference between spec and ledger the ledger stands (Rule 1.3.1).
3. **Resolved open questions → settled** — any open item answered on record during this invocation's DCG becomes a Settled note citing that answer (the Open note is marked answered).
4. **Bracket readjustments** — any Tier Scope Bracket readjustment made this Area (Part 2 Rule 9.5.3) is written back to the spec's bracket table (Area 5).
5. **Continuation and Area boundaries** — when an author answer at the Area's Decision Consultation Gate moves where the scene ends or runs on (the Continuation field of this Area, and the Opening type and Carry-over of the next Area that follow from it), or adds or drops an Area, the move is written to the blocks: an Area is added or set to `DROPPED` with its note, and the Areas-in-Chapter bracket row is readjusted (Rule 5.2.3). This is a traced variance, not an amendment (Rule 3.5.2).
6. **Setups and payoffs** — each setup this Area plants and each payoff it delivers is stamped with its reference code in the Area block's Planted here and Carried or paid off here fields. A planting Area that belongs to an earlier Chapter's COMPLETED spec is not edited by the sync (the sync writes only the active Chapter Spec, Rule 6.2.1): the payoff line carries the reference.
7. **Pacing and size** — pacing is decided in the Chapter Spec and carried, so the sync writes nothing for it unless the author amended the Area's pacing (a light amendment, Rule 3.5.2), when the new value becomes the plan and the planned value is kept in the Variance note. A written Area outside the size range of Rule 2.3.5e was a blocking finding at Gate 1 (Rule 6.1.4); when the author confirmed it, the notes carry `size exception N words, confirmed <date>`, so that a later revision, a neighbour check or a new session can see that the short or long Area was confirmed. An Area inside the range needs no note.
8. **Signatures fired** — the Behavioral Plan table of the Area block (Area 2.2a) is flipped to fired: each Signature the written Area rendered gets its Area reference in the Fired column, and a Signature that fired without being planned is added as a row. Part 39 Check #20 element 20-4 reads the last five as-built Area blocks for these records instead of re-reading their Areas.

*Amended 2026-10-07 — the sync for a `whole` Chapter.* `/create-chapter` runs the sync once, at the Chapter's Gate 2 (Rule 6.2.1 is unchanged: the ledger-update lane owns it). It sets every Area row to `WRITTEN(P.S.P.CCC)` (item 1), flips the Signatures-fired rows of every Area block using the hidden Area markers (item 8), writes variances and settlements for every block (items 2 and 3), reads the word band of Rule 2.3.10 in place of the size range (item 7; a written block outside its band was a blocking finding at Gate 1, and a confirmed exception is noted `band exception N words, confirmed <date>`), writes the Completion Record of Rule 3.7.1 in the same pass and sets the spec `COMPLETED` with the registry row. Every reference it writes is the Chapter reference. On `[SKIP WRITE]` for a `whole` Chapter nothing is written and the Area rows keep their status.

On `[SKIP WRITE]` nothing is written or updated: no file pair, no ledger entry and no spec change. The Area keeps its status, the differences listed for that Area are discarded with it, and the files, the ledger and the spec agree.

### 3.7 — Completion

**Rule 3.7.1 — Completion of the Chapter Spec.**
A Chapter Spec is completed, not closed. The spec status `COMPLETED` means every Area of the Chapter is written.

*How it is completed.* The Gate 2 sync sets the status to `COMPLETED` when the last Area of the Chapter is written (Rule 3.6.1 item 1). The completion content is written when `[NEXT CHAPTER]` opens the successor Chapter, or when the author runs `/chapter-spec complete`. In `[NEXT CHAPTER]` it is written in the one bottom-up write step at the last confirm of the chain (Rule 9.4.4), after the same author questions. Before it writes anything, the command checks that every Area is terminal (`WRITTEN`, or `DROPPED` with a variance note). It then asks the author, through AskUserQuestion, about everything left unresolved: each open item that remains, each setup planted in the Chapter that has no payoff written, and each cliffhanger left unresolved. For each one the author picks: resolve it, carry it forward to the successor's Threads Carried In or questions, or mark it lapsed. An item is marked lapsed only on the author's answer. The area-scorer is launched for the Chapter-Level CDL-2 Aggregate Block, which is information only (Part 35).

*What it writes.* The command then writes into the Completion Record (template section 6): a **final variance summary** (what was planned and what was written, in brief); a **Reader now knows** line (a short list, by reference code, of what the reader has been shown by the end of the Chapter; it seeds the next spec's Carry-over and is no new file); a **Chapter digest** (the text `/chapter-summary` prints for the Chapter: for each Area what changed, who and the open threads, then the accepted sameness patterns and the accepted variances, each with its Area reference; it is written from the written Areas, the Area blocks and the variance notes, is no new file, and is the carrier from which later work reads the Chapter's history without opening its Areas); and it completes the Chapter Header Block's **New named things met by the reader this Chapter** line from the written Areas (each new proper name with the Area that introduced it; information only, nothing counted). It sets the status to `COMPLETED` if the sync has not already done so, and the registry row updates.

*A COMPLETED spec stays living.* No rule refuses a revision because a spec is complete: `/chapter-spec revise` works at any time. A revision that changes plan content for Areas already written is the author's call whether to redraft those Areas. When a COMPLETED spec is revised, its completion pieces (the final variance summary, the Reader now knows line, the digest and the New named things line) are refreshed. A Chapter whose Areas are rolled back or redrafted returns to `CONFIRMED` when no plan content changes (with one variance line), or to `AMENDED-PENDING-RECONFIRM` when plan content changes, as any substantial amendment does (Rule 3.5.2), until `[CONFIRM SPEC]`. When the last Area is written again, the Gate 2 sync sets `COMPLETED` again and one line is added to the final variance summary. Completion of a Novel-Part Spec and of a Section Spec is Rule 9.7.3.

**Rule 3.7.2 — Section-close POV report.**
At every Section close the Continuity Checker reports, for each of the eight protagonists, the number of written Areas whose viewpoint was that protagonist, counted from the Viewpoint field of the `WRITTEN` Area blocks in the Section's Chapter Specs. The viewpoints of characters who are not protagonists are grouped in one line. The report is informational: it sets no target, no minimum and no order, raises no warning and blocks nothing; the author reads it against the ensemble principle of Part 30 (P30-7). The counts are computed when the report is made and are not stored in any spec. The report also carries four lists, all informational: every thread that has been off the page longer than the stretch the author set, with its planned re-entry (Thread Return, Part 36 Rule 26.4.4); every setup still open at the Section close, each with its planting Area, read from the Planted here and Carried or paid off here fields of the Section's specs; the Tier C and Tier B people who acted or spoke in several Areas of the Section (a guide: about three), each noted as a possible promotion; and each Series Villain with no on-page pressure in the Section (Part 18 Area 6.2, Section 9). A promotion is made only on the author's ruling (Part 19 Rule 19.9.2.1), and nothing in the third list forces a question. The written Areas and the Area blocks are in the Chapter Specs of the Section, so the counts and the setup list are read from them; the Section Spec and the Novel-Part Specs hold the plan lines only. The reports at the end of a Novel-Part and of a Section are informational in the same way and never block, Rule 9.7.4.

---

## Area 4 — Spec Authority and the Decision Consultation Gate Interface

### 4.1 — Settling Power (Rules 38.3/38.4)

**Rule 4.1.1 — What settles.**
An item is **spec-settled** when the author explicitly answered it during spec-build or a confirmed amendment — recorded as a Settled note in the Audit and Settlement Notes of a CONFIRMED spec of any of the three kinds. Spec-settled items are valid decision inputs under Part 28 Rule 19.4's No-Asking-What-Canon-Already-Settles Rule: at Area time they count as already-settled, the DCG does not re-ask them, and the drafting flow consumes them directly. (Rule 19.4's empirical test extends accordingly: if the answer is discoverable by reading the settled notes of the active CONFIRMED spec chain, the question must not be asked.) A settled item of the Section Spec or the Novel-Part Spec is not re-asked in a lower build either; it reaches Area time through the Chapter Spec, where it is carried in as an Inherited note naming its source (Section Spec or Novel-Part Spec), because Area time reads only the Chapter Spec (Rule 9.5.1).

**Rule 4.1.2 — What does not settle.**
Only explicit author answers settle. Planner-proposed content the author never answered (including everything under a SKIP), open items, DRAFT-spec content, and anything in a spec whose confirmation lapsed (AMENDED-PENDING-RECONFIRM) has no settling power. And per Rule 1.3.2, settling power is planning-side only — a settled item is still a proposal toward canon until a delivered Area establishes it. This holds for an item of the Section Spec and the Novel-Part Spec, and an item the author deferred has no settling power either. The carve-outs of Section 4.2 hold at every level of the chain, Rule 9.5.3.

### 4.2 — The Carve-Outs (Always Still Asked Per Area)

**Rule 4.2.1 — Pacing is not asked at Area time.**
Pacing is decided in the Chapter Spec for every Area (Rule 2.3.3) and is carried. No pacing question is asked at Gate 1 or at any Decision Consultation Gate, and no Area-writing step re-asks it. Fast, Medium and Slow are the vocabulary the spec records; the spec's pacing value is the pacing the Area is written at. A change of pacing is made in the Chapter Spec (a light amendment, Rule 3.5.2). No field of the Section Spec or the Novel-Part Spec carries a pacing value, Rule 9.5.3.

**Rule 4.2.2 — Open items.**
Every branch the spec records as an Open note that bears on the upcoming Area is asked at that Area's DCG (and its on-record answer flows back into the spec as a Settled note at the Gate 2 sync). A branch recorded as a Skipped note (Rule 2.3.6) is not re-asked at Area time, because the author left it to the planner; it is asked only if the plan would change the planner's choice. An author deferral to Area writing is copied into the Chapter Spec of the Chapter it bears on, as a Deferred note, and is asked at the Area-time gate exactly like an open item; the drafter never settles it silently. Rule 9.5.2.

**Rule 4.2.3 — New branches.**
Anything genuinely new — branches the spec never contemplated, branches created by variance between plan and written reality, and consequences of prior DCG answers per Rule 19.4's Exhaustive Clarity Mandate — is asked. A spec never forecloses a question it never answered.

**Rule 4.2.4 — Clarity reduction (the "DO NOT ASSUME" rule).**
If Area-time reality has made a settled answer ambiguous, stale, or contradicted (an intervening variance, an author revision, a ledger event the spec predates), the item's clarity has **reduced** and it is re-asked — surfacing the original settled answer and the source of ambiguity as context. Under the author's standing "DO NOT ASSUME" rule, reduced clarity is always resolved by asking, never by planner inference. The fresh answer supersedes and re-settles the item on record. The same rule applies at every level of the chain. When a Section Spec or Novel-Part Spec built ahead of its time meets reality at the boundary, only the affected items are re-asked, each with the original answer and the source of the change shown, Rule 9.2.3.

**Rule 4.2.5 — Part 36 Autonomous Matters are never spec-fixed.**
Part 36 Area 13.4 Autonomous Matters — sensory palette, living-scene execution criteria, and every Part 36 matter the AI governs autonomously in drafting — are never fixed by a spec field, never asked at spec-build, and never asked at Area time. A spec attempting to fix them is corrected at audit. The author's own optional levers are the one exception: the sensory anchor, tone and voice, and content fields (Rules 2.3.5a, 2.3.5b and 2.3.5d). Where a lever is unset, the matter stays autonomous and the drafter decides at drafting time under Part 36; setting a lever is the author's choice and no question is asked about it. The same holds above Chapter. Neither the Section Spec nor the Novel-Part Spec fixes an Autonomous Matter or sets a tone, voice, sensory or content tag; those stay at Area grain, Rule 9.5.3.

### 4.3 — Precedence Restated for the DCG

**Rule 4.3.1 — Conflict resolution at planning time.**
When sources conflict while composing a DCG or a plan: Locked Canon silently wins (and the spec is flagged for correction); ledger beats spec (variance recorded, spec corrected at sync); spec beats any session-log recollection (session-log is never an input); a live author answer at the DCG beats the spec (and re-settles it). No conflict is resolved silently in the other direction — every spec-losing conflict leaves a variance note. Between specs of the chain, a conflict found in a lower build is a question to the author, never a silent pick, and the author's answer amends the higher spec through the variance channel of Rule 9.4.5. Rules 9.4.1 and 38.12.

---

## Area 5 — Tier Scope Bracket Interface (Part 2 Area 9)

### 5.1 — The Backing Store (Rule 38.5)

**Rule 5.1.1 — Authority ceded on record.**
Part 2 cedes to this Part, through the explicit-amendment doorway of Part 2 Rule 9.12.2, chapter-grain story specification — including the persistence of the Tier Scope Bracket range at chapter grain — is governed by this Part. Part 2 Area 9 Rule 9.13 records the amendment on the Part 2 side. The same doorway also admits the Section Spec and the Novel-Part Spec under this Part, and Part 2 Rule 9.13 records that too. Those two specs hold no Tier Scope Bracket range at all, Rule 5.1.2.

**Rule 5.1.2 — The spec is THE backing store.**
Where an active (CONFIRMED) chapter spec exists, its Section 2 bracket table is the **authoritative backing store** for the Chapter-tier Tier Scope Bracket range within its scope: Areas-in-this-Chapter. Tier-open declarations, retroactive declarations, and every readjustment for that tier are persisted in the spec; the in-chat instruments **read** from it:

- the `TIER SCOPE BRACKET` lines of Part 2 Rule 9.10.1 emit the spec's current range;
- the post-Area Completeness Indicator (Part 2 Area 8) draws its chapter-grain `~M` planned-range estimates from the active spec;
- the Position Header Block low–high range fields (Part 28 Rule 18.7) draw from the Tier Scope Brackets, which draw from the spec — one chain, one source, no divergence (a divergence anywhere in the chain is a display mismatch reported for the author's ruling).

Above Chapter grain no range is stored in any spec. The Section Spec's Novel-Part plan and the Novel-Part Spec's Chapter entries are lists that guide the plan (the Novel-Part Spec may add, split, merge or drop Chapters of the Section Spec's high-level list as the story needs), and the length of a list is read as information only, with no separate range above Chapter (Part 2 Rule 9.3.1). The Chapter Spec remains the one backing store for the bracket range that exists, and Part 2 Area 9 semantics stay as Rule 5.2.1 says.

### 5.2 — Part 2 Area 9 Semantics Preserved (Explicit)

**Rule 5.2.1 — Advisory in force.**
Making the spec the range's authoritative *source* changes where the numbers live — it changes nothing about what the numbers are allowed to do. All Part 2 Area 9 semantics remain in full force over spec-backed ranges, explicitly including: Part 2 **Rule 9.6.1** (never a stop-condition), Part 2 **Rule 9.6.2** (never a fill-condition), Part 2 **Rule 9.6.3** (never a constraint on narrative choice), Part 2 **Rule 9.7** (immersion precedence — the depth-and-pacing mandate prevails absolutely), Part 2 **Rule 9.8** (continuity precedence), and Part 2 **Rule 9.9** (overrun/undershoot is calibration data, never correction). Citations prefixed "Part 2" refer to Part 2 and not to this Part's own Rules 9.6 to 9.9. Ranges stay tentative low–high bands. The bracket bends; the narration does not.

**Rule 5.2.2 — Calibration, not correction.**
Closure above or below a spec-backed range is recorded with a one-line reason (Part 2 Rule 9.9.1) in the spec's notes and carries no corrective, penalising, or revisionary weight. Systematic divergence is author-level calibration for future spec builds (Part 2 Rule 9.9.2) — it never modifies any rule of this Part or Part 2.

**Rule 5.2.3 — In-flow readjustment is free.**
Area-flow readjustments (confirm / narrow / widen / dissolve per Part 2 Rules 9.5.1–9.5.2) never require a spec re-confirmation: they are logged in the Position Display and written back to the spec's bracket table at the Gate 2 sync as light amendments (Rule 3.5.2). Dissolution of a bracket is recorded in the spec with the standard `story-demanded, bracket no longer informative` note.

---

## Area 6 — Gate Integration: Check #18 and the Gate 2 Sync

### 6.1 — Gate 1 Check #18: Spec Conformance (Blocking)

**Rule 6.1.1 — The check.**
The Gate 1 Post-Draft Audit sequence (`.claude/guardrails/audit/guardrail-audit-gate-law.md`) carries a blocking check, **Check #18 — Spec Conformance** (the sequence's current total is owned by `.claude/guardrails/audit/guardrail-audit-gate-law.md`), evaluated on every drafted Area:

- **(a) The chain is in force.** The Chapter Spec of the drafted Area's Chapter is CONFIRMED (or COMPLETED, for an Area revised after its Chapter was completed, `/revise-area`), AND the Novel-Part Spec it stands under is CONFIRMED or COMPLETED, AND the Section Spec above that is CONFIRMED or COMPLETED. A link that is DRAFT, AMENDED-PENDING-RECONFIRM or RETIRED does not count as in force (Rule 9.1.1). An Area revised after its Chapter was completed is checked against that Chapter's COMPLETED spec; the Gate 2 sync on it is a correction of record and does not change that spec's status. A missing or unconfirmed link is a FAIL: Critical where no chain stands (a link is missing, DRAFT or RETIRED), Major where a link stands but is AMENDED-PENDING-RECONFIRM (Part 38 Rules 6.1.3 and 9.1.3) — the chain must exist before Areas are written (Rules 38.1 and 38.9). The correction path is the command of the missing link (`/section-spec`, `/part-spec` or `/chapter-spec`) → `[CONFIRM SPEC]`, then re-run. No comparison of the Area with the Section Spec or the Novel-Part Spec is made: part (b) compares the draft with the Chapter Spec only, and the Check stays one check.
- **(b) Slot conformance.** The check compares every spec-planned element that bears on the drafted Area with what the draft contains, reading the Area together with the Areas of its Chapter already written: the Area block (purpose, scene anchors, continuation, viewpoint and Dual-POV mark, title, entities on the page, debuts, the sensory anchor, tone and voice and content fields) and every applicable field of it (Rule 2.4.2). The pacing is carried from the Chapter Spec (Rule 2.3.3) and is listed only: a pacing difference is shown and never blocks, because pacing is a craft matter independent of size. The CDL-2 emphasis (scored after the write, Rule 2.3.5) is not a Gate 1 comparison. The size is structural and blocks: a count outside 1,280 to 2,400 words is a blocking finding: the write waits for the author to confirm the Area or send it back (Rule 6.1.4). **Core items** are: the beat (the Area's purpose); the scene anchors (their order is part of the anchors); the Continuation; the viewpoint (the Dual-POV mark included); every planned time skip; the Behavioral Plan (Rule 6.1.2); the Opening type; the Closing type; the Thread or storyline; and every settled item. The drafted Area matches on every core item **OR** every core difference traces to an on-record author answer from **this invocation** (the author steered away from the plan live; that is always valid). An untraced core difference = FAIL. A settled item is the author's earlier answer: a difference on it is never accepted by `[CONFIRM WRITE]` and clears only by a new author answer or an amendment that re-settles it (Rule 4.2.4).
- **(c) Variance flagged for sync.** Every traced deviation and every accepted listed difference is flagged in the audit report for the Gate 2 as-built sync (Rule 3.6.1) so the spec is corrected to reality in the same cycle.
- **(d) Listed differences do not block.** Every other planned element (working titles, names, entities on the page, debuts, the order of debuts and appearances, pacing, carry-over, setups and payoffs, the emotional line, world, setting and people, ledgers expected to change, novel elements, story link and change, cross-references, purpose, want, obstacle and stake, fight) is compared, and a difference is a line in the plan-versus-written list (Rule 6.1.4), not a FAIL. A pacing difference is listed only and never blocks. Sensory anchor, tone, voice and content entries are listed and tested by the Part 36 dimensions that own them.
- **(e) The author accepts or rejects the list.** The list is presented with the Gate 1 result. `[CONFIRM WRITE]` accepts the listed differences that are not settled items, and the Gate 2 sync writes them into the spec (Rule 3.6.1). `[REVISE AREA]` rejects them and the revision loop runs. `[SKIP WRITE]` discards them with the Area.

**Rule 6.1.2 — Character of the check.**
**Behavioral Plan coverage.** Check #18 additionally tests the drafted Area against its Area block's Behavioral Plan (Area 2.2a): a Signature planned to fire and absent, a planned waiting beat not rendered, or a drift executed that the plan did not anticipate is a Check #18 variance, recorded and traced exactly as any other variance is and synced at Gate 2. This is a *conformance-to-plan* test only — whether the conduct matches the character's registered profile is Check #20's question (Part 39 Area 43), and whether the profile should now change is Check #21's (Part 39 Area 44). The three checks are distinct and none substitutes for another.

Check #18 is a planning-conformance check, not a canon-fact check: it never treats spec content as established fact (Rule 1.3.2), and Area-versus-spec mismatch is variance to trace and sync — never, by itself, a canon error. Canon facts remain the province of the other Gate 1 checks, CCIA, and the ledger law. Check #18 sits after Check #17 (Entity Naming, Part 28 Area 20.5) in the sequence; the standard Correction Protocol applies — a FAIL blocks Gate 1 delivery until corrected and re-run clean.

**Rule 6.1.3 — Failure grades.**
- **Listed, no grade.** A difference on a non-core, non-settled element (a working-title drift, a name, an entity, a debut, the order of appearances, pacing) is a line in the plan-versus-written list (Rule 6.1.4), not a failure. A pacing difference is only ever listed.
- **Size, blocking.** A count outside 1,280 to 2,400 words is a blocking finding: the write waits for the author to confirm the Area or send it back (Rule 6.1.4). It carries no Minor, Major or Critical grade, and it is a structural finding, not a craft one.
- **Minor.** One untraced, low-impact core difference (e.g., a scene anchor met at the neighbouring beat boundary with the Area still inside the size range) — correctable by tracing (re-issuing the missed DCG question) or by draft correction before Gate 1 delivery.
- **Major.** Deviation on beat, scene anchors (beyond the low-impact case above), the Continuation, viewpoint, a time skip, the opening or closing type, the thread or storyline, or a settled item without any tracing author answer; or drafting begun against an AMENDED-PENDING-RECONFIRM spec in any link of the chain (the Section Spec, the Novel-Part Spec or the Chapter Spec).
- **Critical.** An Area drafted (or written to file) for a chapter with no confirmed spec chain, that is, with a Chapter Spec, a Novel-Part Spec or a Section Spec that is missing, DRAFT or RETIRED; or a delivered Area contradicting a settled item with the DCG never consulted — handled per the Part 28 Area 19 Failure Mode A Critical protocol (file pair flagged for `[REVISE AREA]`, Ledger Update rolled back) plus a mandatory spec sync/amendment pass.

**Rule 6.1.4 — The plan-versus-written list.**
Check #18 produces a list for every drafted Area and shows it with the Gate 1 result, before the confirmation prompt (its place in the Gate 1 order is set by `guardrails/commands/guardrail-command-law.md`). Its columns are Element, Planned, Written, Kind (`core`, `settled`, `size` or `listed`) and Result. Every difference is shown in full; the matching elements are named in one line with their number, so nothing that was compared is hidden. Results are: `matches`; `traced to your answer (ref)`; `listed: accepted by [CONFIRM WRITE]`; `BLOCKS: core difference`; `BLOCKS: settled item`; `BLOCKS: size N words`. A list with a BLOCKS line is not presented with a confirmation prompt: the Correction Protocol runs first, by revising the draft to the plan or by asking the author for the ruling that clears the item. A count outside 1,280 to 2,400 words is a blocking finding: the write waits for the author to confirm the Area or send it back. The author's confirmation of an Area outside the range clears that line and is recorded as a size exception (Rule 3.6.1 item 7). A pacing difference is a listed line and never blocks. When the list holds only listed differences, the confirmation prompt says that `[CONFIRM WRITE]` accepts them.

**Rule 6.1.5 — Check #18 for a `whole` Chapter (Amended 2026-10-07).**
For a Chapter whose Build mode is `whole`, `/create-chapter` runs Check #18 once on the whole Chapter text. Part (a) is unchanged. Part (b) compares each Area block of the spec with its span of the Chapter (found by the hidden `<!-- AREA NN -->` markers) and the Scene Map with the scenes as written: the scene arcs, the viewpoint sequence, the visible breaks, the join state at each Area seam, the date lines, and every core item of Rule 6.1.1(b) for each block. The size test of Rule 6.1.1(b) is replaced by the band check: each Area block inside 55 to 60 percent of its size target in words (up to 72 percent where its Budget stretch names one), no block below 55 percent, and the Chapter total inside 0.55 T to 0.72 T (Rule 2.3.10). A count outside its band is a blocking finding: the write waits for the author to confirm the Chapter or send it back, recorded as a band exception. A missing, duplicated or out-of-order marker is a blocking finding. Pacing is listed only, as in Rule 6.1.1(b). The plan-versus-written list of Rule 6.1.4 carries one row for each Area block and one for the Scene Map.

### 6.2 — Gate 2 As-Built Sync (Ownership)

**Rule 6.2.1 — Ownership and pipeline shape.**
The mandatory as-built sync of Rule 3.6.1 executes at every Gate 2, owned exclusively by the **Post-Write Ledger Update continuity-checker instance**. The Gate 2 pipeline remains **3-way**, with spec sync writes riding the ledger-update lane; no new pipeline lane, no other writer (Rule 1.2.3). The write set of the sync is the ledger files, the active Chapter Spec and its registry row. The Section Spec and the Novel-Part Spec are never written at Gate 2; their statuses are derived or are written at the boundary, Rules 9.4.4 and 9.7.3. A Gate 2 that writes its files but does not complete the ledger update or the spec sync is an incomplete Gate 2: the `[STATUS]` report lists each such Area (a written Area whose spec status is not `WRITTEN`, or whose ledger rows are missing) as `incomplete Gate 2 at <ref>`, a pending action until reconciled. A standalone `/force-ledger-audit` then performs the Rule 3.6.1 sync for it, behind its preview.

---

## Area 7 — Resets, Rewinds, and Redrafts (Rule 38.7)

### 7.1 — Survivability

**Rule 7.1.1 — Specs survive destructive commands, except `[HARD RESET]`.**
No destructive or rewind command deletes a spec file. `[REWIND TO]` (C-16), `[RESET STORY]` (C-21), `[RESET CHAPTER]` (C-22), `[RESET PHASE]` (C-23), `[REDRAFT AREA]` (C-29), and `[REDRAFT CHAPTER]` (C-30) all leave every spec file of all three kinds (`section-N-spec.md`, `part-N-spec.md` and `chapter-NNN-spec.md`) and the `_index.md` registry on disk. The spec is the intent record; destroying written Areas does not destroy intent.

**Rule 7.1.2 — `[HARD RESET]` (C-1) is the sole exception.**
`[HARD RESET]` deletes every spec file, of all three kinds (every `section-N-spec.md`, every `part-N-spec.md` and every `chapter-NNN-spec.md`), along with the written Areas. The `_index.md` registry survives, emptied of rows down to its schema headers (its three tables keep their header rows). After a `[HARD RESET]` no spec remains, so `/start-story` is a fresh build of the whole chain. The reasoning is the reasoning of the command itself: C-1 returns the project to a pre-story state, and a spec is a plan written against a story that no longer exists — carrying it forward would seed the next Chapter 1 with intent the author has just discarded. This is the one command that destroys intent along with written Areas, and it is human-invocation-only precisely because of that. No status rollback applies, because no spec remains to roll back.

### 7.2 — Status Rollback

**Rule 7.2.1 — Statuses roll back to match surviving Areas.**
When a destructive/rewind command archives or deletes written Areas, the affected specs' per-Area statuses are rolled back to match what actually survives: `WRITTEN(ref)` Areas that were removed roll back to `PLANNED` (or `DRAFTED` where a chat-accepted draft survives the operation), and name statuses that were `locked-at-Gate-1` or `locked-at-Gate-2` solely via now-removed deliveries roll back to `proposed`; a reference stamp of Rule 3.6.1 item 6 that cites a removed Area reverts to its unstamped form (the stamp kept in the Variance note). Every rollback writes a **variance note** recording the command, date, and prior status — the rollback is visible history, never a silent rewrite. Where a redraft takes a whole Area as its target, that Area rolls back; where a rewind takes an Area as its target, that Area keeps its status and every Area after it rolls back. The rollback is performed by the same continuity-checker sync role, as part of the destructive command's ledger-reconciliation pass; `[REDRAFT AREA]` and `[REDRAFT CHAPTER]` run that pass first, at their Step 2, once the revised plan is confirmed, so the revise flow re-plans Areas that are still `WRITTEN` and does not roll them back itself. A COMPLETED Chapter Spec whose Areas roll back returns to CONFIRMED, keeps its completion text as history, and is completed again by the Gate 2 sync of its last Area and by the next completion step (Rule 3.7.1). A COMPLETED Novel-Part Spec or Section Spec returns to CONFIRMED when any spec under it returns to a status other than COMPLETED; its completion text is kept as history too, and it is completed again at its next boundary (Rules 9.7.3 and 9.8.1). The continuity-checker's pass changes statuses, stamps and the Coverage cells of the registry rows that a rollback changes (Rule 1.2.2), and never plan content. The Novel-Part Spec's Chapter entries carry a derived status and are never rewritten by it. The go-back pass of `[REDRAFT AREA]` and `[REDRAFT CHAPTER]` (their Step 2, run as a rewind does) is a rewind rollback for the Coverage rule of Rule 1.2.2, so it refreshes the Coverage cells of the rows it changes too. A rollback never loses the record.

**Rule 7.2.2 — Settled answers survive rollback.**
Settled notes are author decisions, not Area artifacts — they survive rollback untouched (subject to the Rule 4.2.4 clarity-reduction re-ask when the rewind itself made a settled answer stale). `[RESET STORY]`-scale operations leave specs on disk with every Area status at `PLANNED` (spec statuses move only as Rules 7.2.1 and 9.8.1 say); the author may retire a spec only explicitly, via an amendment through the command of its kind (`/section-spec`, `/part-spec` or `/chapter-spec`) marking it RETIRED — never silently. Orphan rule: retiring a Section Spec or a Novel-Part Spec that still has a child spec which is not RETIRED is refused until the author has ruled on each child, Rule 9.8.3.

### 7.3 — Redraft-Chapter Re-Opens the Spec First

**Rule 7.3.1 — Spec before redraft.**
`[REDRAFT CHAPTER]` (C-30) begins by **re-opening the chapter's spec**: the `/chapter-spec` amendment flow runs first (author consultation on what the redraft should change; light continuity audit if substantial; `[CONFIRM SPEC]`), and only then does redraft planning begin against the re-confirmed spec. A C-30 that starts redrafting Areas without the spec pass is a Rule 7.3.1 violation and a Check #18(b) FAIL at its first drafted Area. `[REDRAFT AREA]` (C-29), the full redraft of one Area, requires the lighter equivalent: the affected Area's block is re-opened and re-confirmed if the redraft intends to deviate from it; a redraft executing the existing plan needs no amendment. The amendment flow of `[REDRAFT CHAPTER]` is the `/chapter-spec revise` flow and so needs the chain in force (Rule 9.1.1). Its step 1 has one question: if the revised plan departs from what the Novel-Part Spec's entry for the Chapter fixes (Rule 9.3.3), the departure is recorded as a variance note on every spec above the Chapter, the Section Spec first and then the Novel-Part Spec, in one step (Rule 9.4.5), and the author is asked whether the plan is to be amended or the original left as the plan baseline. Splitting, merging, re-cutting or renaming Areas is the Chapter Spec's own business and asks nothing.

---

## Area 8 — Amendment Protocol and Cross-Part Dependency Table

### 8.1 — Part 38 Amendment Protocol

When Part 38 itself (this file's law — not an individual spec of any kind, which Area 3.5 governs) is amended:

1. The amendment is made on the author's explicit on-record directive (or formal `[CANON AMENDMENT]`), edited into this consolidated file.
2. The spec schema (Areas 2, 10 and 11) version-bumps if changed; existing spec files are migrated forward at their next touch of the command of their kind (`/section-spec`, `/part-spec` or `/chapter-spec`), never silently in place.
3. `.claude/story-memory/phase-section-part-chapter-area-specs/_index.md` (registry header) is updated.
4. The canon-manifest is updated in the same session: `skill-index.json` (this entry), `domain-map.json` (Part 38 row), `dependency-graph.json` (Part 38 edges).
5. Interfacing artifacts are reconciled where touched: `guardrail-story-spec-law.md`, `guardrail-audit-gate-law.md` (Check #18), the `/section-spec`, `/part-spec`, `/chapter-spec`, `start-story`, `next-chapter`, `next-part`, `next-section`, `next-phase` and `next-area` command texts (and `revise-area` and the reset, rewind and redraft commands where they name specs), and Part 2 Area 9 Rule 9.13. Conflicts are never resolved silently — escalate via `/run-canon-audit`.

### 8.2 — Cross-Part Dependency Table

| Dependency | Direction | Type | Impact |
|---|---|---|---|
| Part 2 Area 9 (Rule 9.12.2 doorway → Rule 9.13) → Part 38 | Part 2 cedes chapter-grain spec/bracket-store authority to Part 38 (on the author's on-record authorization); extended to the spec chain through the same doorway | HARD | Structure and brackets: spec is the authoritative backing store for the Chapter-tier Tier Scope Bracket range (the Areas-in-Chapter row of the Chapter Spec only; no range is stored above Chapter, the Section Spec's and Novel-Part Spec's lists are guides and their length is information, Part 2 Rule 9.3.1); Part 2 Area 9 advisory-in-force semantics (Part 2 Rules 9.6.1, 9.6.2, 9.7, 9.8, 9.9) govern range behavior unchanged |
| Part 2 Areas 1, 4, 5, 6, 8 → Part 38 | Part 2 governs | HARD | Five-tier hierarchy (the Area as the written unit, the Area-to-Area carry-over rule), POV law and the viewpoint change between Areas, the brief time-skip mark, path/naming conventions the spec tree mirrors (the Section Spec and Novel-Part Spec folders and files included), Completeness Indicator read-path |
| Part 28 Areas 19/19.4 → Part 38 | Part 28 governs the DCG; Part 38 supplies settled inputs | HARD | Spec-settled items are Rule 19.4 decision inputs, and the settled items of the confirmed Section Spec and Novel-Part Spec, carried into the Chapter Spec as Inherited notes naming their source, count too (Rule 19.3 category 1 and the Rule 19.4 No-Asking list, Rules 9.5.1 to 9.5.3); Rule 19.4's persistent consultation until 100% clarity cross-refers Rule 38.13, the one definition for the three spec builds; pacing is decided in the Chapter Spec and carried, never asked at Area time; open/new/clarity-reduction items asked |
| Part 28 Areas 3, 18, 20 → Part 38 | Part 28 governs naming/Establishment | HARD | `proposed` vs `locked-at-Gate-1` (structural names, Rule 18.4.4) or `locked-at-Gate-2` (in-world names, Area 20.3); name register standards 18.4.1–18.4.3; MAJOR/MINOR consultation split 20.4; Rule 18.7 Position Header ranges draw through the brackets the spec backs |
| Part 30 → Part 38 | Part 30 governs the macro arc | HARD | Chapter purpose cites Section mandates by function name (never copied); calendar window per §1.3.2a; P30-L5 crisis-density tracking row; P30-L8 forbidden entities and P30-L9 sentient monsters excluded from all planning. The Section Spec build reads the whole of Part 30 every time and cites it by function name only (Rules 10.3.2 and 10.4.2); Part 30 is the Phase-level plan and no Phase Spec exists (Rule 9.1.4); the windows nest Section, Novel-Part, Chapter (Part 30 Check 11-2); the three linked guide registers of setups, payoffs and threads sit beside the Part 30 Setups-table (Rule 9.5.4) |
| Part 40 → Part 38 | Part 40 governs monsters | SOFT | The template section 3 standing exclusion for sentient monsters (Law P30-L9); monsters in the Behavioral Plan by Kind and tier (Area 2.2a); a Phase 1 Kind is defined and named at its Chapter Spec as a `proposed` name (Part 40 Rule 40.7.5.1; Rule 1.3.2) |
| Part 41 → Part 38 | Part 41 governs the calendar | HARD | A calendar window in every spec (Section, Novel-Part, Chapter) and the in-story time of an Area are written as dates plus Phase Day, citing Part 41 Areas 4 and 5 and never copying its month table (Rules 2.4.10, 9.3.1, 10.3.1 and 11.3.1); the recorded date lives in `ledger-worlds-calendar/` (Part 41 Area 9), which a spec mirrors only as the as-built in-story time of Rule 3.6.1 item 2 (Rule 1.4.2); a window is a plan and establishes nothing (Rule 1.3.2); Part 30 still owns the Phase Day numbers and the Section durations |
| Part 35 → Part 38 | Part 35 governs CDL-2 | SOFT | Per-Area CDL-2 category emphasis notes planned beside the Part 35 Area 3 Section targets, which inform only; scoring remains Part 35's alone |
| Part 36 Areas 13, 15.5, 18 to 27 → Part 38 | Part 36 governs thematic voice and autonomy | SOFT | Spec-build direction options carry thematic previews and exposition-risk flags; Autonomous Matters (sensory palette, living-scene criteria) are never spec-fixed except through the author's optional sensory anchor, tone and voice, and content fields; the Area block names its novel elements from the Part 36 element lookup table (Area 15.5), and its tone tag, opening and closing types, and setups and payoffs are the plan that Part 36 Areas 18 to 27 and the Area flow review judge in the Area. The guide-post distance for how long a setup may wait (Part 36 Rule 23.2.5) and the thread-return stretch (Part 36 Rule 26.4.4) are set by the Section Spec and Novel-Part Spec plan lines, with no figure, and the thread-return stretch is a per-thread note in the Section Spec's threads table, default `unset` |
| Part 37 ↔ Part 38 | Mutual boundary | HARD | NOT-a-ledger delineation: Part 37 does not govern the spec folder; Part 38 does not govern ledger files; spec references ledger entries by name/ref, never restates their content; ledger supersedes spec |
| Gate audit (FCIA/ALCA) | Audit governance | HARD | `guardrails/audit/guardrail-audit-gate-law.md` governs all Area content produced under this Part: Check #18 joins the Gate 1 blocking sequence; Gate 2 as-built sync rides the Post-Write Ledger Update step (3-way pipeline preserved) |
| Command law → Part 38 | `guardrails/commands/guardrail-command-law.md` governs the commands | HARD | `/chapter-spec` and the C-6/C-16/C-21/C-22/C-23/C-29/C-30 interactions, and `/next-area`, execute under that command law. `/section-spec` (C-40), `/part-spec` (C-41) and the C-3 `[START STORY]`, C-7 `[NEXT PART]`, C-8 `[NEXT SECTION]` and C-9 `[NEXT PHASE]` interactions; the three spec commands carry the same Exhaustive-Clarity consultation and the confirm token is a hard pause that Auto Mode never waives (see `guardrails/commands/guardrail-plan-then-auto-execution.md`) |

---

## Area 9 — The Spec Chain

Areas 1 to 8 hold the law of the Chapter Spec. This Area holds the law of the **spec chain** of three kinds: the **Section Spec** (ref `P.S`, built by `/section-spec`, Command C-40), the **Novel-Part Spec** (ref `P.S.P`, built by `/part-spec`, Command C-41) and the **Chapter Spec** (ref `P.S.P.CCC`, built by `/chapter-spec`, Command C-39). It is the law of the chain itself: how the three depend on one another, how a lower spec is made from a higher one, who may write what and when, how the author's answers travel down and variance travels up, what "asked until clear" means, how a spec is completed, what happens to the chain on a reset, and how every spec keeps a clean body and gathers its notes at the end. Area 10 holds the Section Spec's template and field law, and Area 11 holds the Novel-Part Spec's. The Chapter Spec's schema stays in Areas 2 and 3.

**Words used in Areas 9 to 11.**

- **Novel-Part Spec** is always written in full in rule text, because "Part Spec" would read as "the spec of canon Part N". The command is `/part-spec`.
- **Spec status**, for all three kinds, is one of `DRAFT`, `CONFIRMED`, `AMENDED-PENDING-RECONFIRM`, `COMPLETED`, `RETIRED` (Rule 9.7.1). The *Area* status (`PLANNED` / `DRAFTED` / `WRITTEN` / `DROPPED`, Rule 2.4.9) is a different thing.
- **The three tokens** `[CONFIRM SPEC]`, `[REVISE SPEC]` and `[SKIP SPEC]` are shared by the three kinds (Rule 3.4.1). The prompt, the session-log line and the registry row name the artifact and its ref: "Section Spec 1.2", "Novel-Part Spec 1.2.3", "Chapter Spec 1.2.3.004".
- **The notes** are the kinds of line kept in the Audit and Settlement Notes section: Settled, Skipped, Open, Deferred, From, Inherited, Name, Variance and Audit (Rule 9.10.2). They are plain lines at the end of a spec, never tags in its body.

**Master rules this Area elaborates.**

- **Rule 38.9 — Spec Chain Mandate.** Every Section, every Novel-Part and every Chapter has exactly one spec at its canonical path. A spec can be built or revised only while the spec above it is `CONFIRMED` or `COMPLETED`; a Section Spec starts from the whole of Part 30; and a chain in force must stand before any Area is written (Areas 9.1, 9.2, 9.7 to 9.9; the Section Spec and the Novel-Part Spec are the subject of Rules 38.10 and 38.11 in Areas 10 and 11).
- **Rule 38.12 — Derivation, Precedence and Cascade.** A lower spec is made from its parent's entry and keeps the source note; the scope of a level runs Locked Canon, then ledger, then Section Spec, then Novel-Part Spec, then Chapter Spec; the author's settled answers carry downward; variance is noted upward; and when a parent is amended after children exist, each child is reported and the author decides each one (Areas 9.3 to 9.5).
- **Rule 38.13 — Clarity Mandate for All Spec Builds.** One definition of "done" governs the Section Spec build, the Novel-Part Spec build and the Chapter Spec build: nothing unasked at that spec's own level, a final sweep that finds nothing new, the author's own "nothing further to steer", and then the confirm token (Area 9.6).
- **Rule 38.14 — Clean Spec Body and Audit and Settlement Notes** (Area 9.10).

### 9.1 — Chain Dependency

**Rule 9.1.1 — The chain rule.**
A spec can be built or revised only while every spec above it is `CONFIRMED` or `COMPLETED`. A Chapter Spec needs its Novel-Part Spec and its Section Spec; a Novel-Part Spec needs its Section Spec; a Section Spec needs Part 30 to hold an entry for its Section (Rule 9.1.4). A parent that is `DRAFT` (saved by `[SKIP SPEC]`), `AMENDED-PENDING-RECONFIRM` or `RETIRED` refuses the child's build or revision, and the refusal names the command that puts the parent right: `/section-spec` for a Section Spec, `/part-spec` for a Novel-Part Spec, `/chapter-spec` for a Chapter Spec. A `[SKIP SPEC]` at any level saves that spec as `DRAFT` and stops the chain there; no spec below it is built in that run. A child's `[CONFIRM SPEC]` is not accepted while its parent is out of force. This widens Rule 38.1 (one confirmed Chapter Spec before the Chapter's Areas): no Area is written without a confirmed plan.

**Rule 9.1.2 — A Chapter needs an entry in its Novel-Part Spec.**
The Chapter being built must have an entry in its Novel-Part Spec (Rule 11.3.2). If it has none, because the story needs one Chapter more than the plan listed, `/chapter-spec` stops and offers to add the entry as a LIGHT amendment of the Novel-Part Spec (Rule 11.5.2): a short entry round on the fields the entry fixes (purpose, calendar window, threads in and out, who is on the page, key events, hook and closing beat), put to the author with its OWN `[CONFIRM SPEC]` / `[REVISE SPEC]` / `[SKIP SPEC]` prompt (the same three tokens as every spec), which names "Novel-Part Spec P.S.P, new entry for Chapter P.S.P.CCC". The entry is written at once, at that confirm (Rule 9.4.4), and only then does the Chapter build begin, from the new entry as from any other (Rule 9.3.1); the two prompts are never open together. A Chapter Spec is never written unless the Novel-Part Spec above it holds an entry for that Chapter and both it and the Section Spec exist and are CONFIRMED or COMPLETED (Rule 9.1.1). A new entry changes the Chapter list, so it is noted upward on the Section Spec, in the same write step as the entry, the Section Spec's note first (Rule 9.4.5). If the author declines or answers `[SKIP SPEC]`, the Novel-Part Spec is left as it was, no Chapter Spec is built and the Chapter stays blocked for Areas (Rule 9.1.1). Where the Novel-Part Spec has no further entry at all, the command does not decide what that means: it asks the author whether the Novel-Part has finished (the next step is `/next-part`) or the story needs one more Chapter (the light amendment above, or `/part-spec revise` for a larger change), because a Novel-Part ends where the story ends it (Rule 1.5.1).

**Rule 9.1.3 — Enforcement points.**
The chain rule is enforced at each place a spec is built, revised or relied on, and each refusal names the FIRST missing link counted from the top (Section Spec, then Novel-Part Spec, then Chapter Spec) with the command that makes it:

- the preconditions of `/section-spec`, `/part-spec` and `/chapter-spec`;
- `/next-area`, whose stop condition this is, and `/next-chapter` and `/revise-area`, which carry the same precondition;
- the pre-reads of the outline-planner and the continuity-checker;
- `/status`, which flags a story that has no confirmed Novel-Part Spec or Section Spec for the work in hand;
- **Gate 1 Check #18(a)**, which reads "the chain is in force" (Rule 6.1.1(a)): the Chapter Spec is `CONFIRMED` (or `COMPLETED`, for an Area revised later), and its Novel-Part Spec and its Section Spec are `CONFIRMED` or `COMPLETED`, none of the three being `DRAFT`, `AMENDED-PENDING-RECONFIRM` or `RETIRED`. A missing or unconfirmed link is a FAIL, graded under Rule 6.1.3: Critical where no chain stands (a link is missing, `DRAFT` or `RETIRED`), Major where a link stands but reads `AMENDED-PENDING-RECONFIRM`.

Check #18 adds no comparison of the Area with a Section Spec or a Novel-Part Spec, and the number of checks is unchanged. The Area is compared with the Chapter Spec, which carries from above what it needs, each item noted with its source (Rules 9.3.1 and 9.5.1). How well a Chapter fits its Novel-Part and its Section is looked at when the Chapter Spec is built, by the light audit (Rules 3.3.2, 10.5.1 and 11.6.1), and reported as information when a Novel-Part and a Section end (Rule 9.7.4).

**Rule 9.1.4 — No Phase Spec; Part 30 is the Phase plan.**
No Phase Spec exists and none is created. Part 30 is the plan at Phase level: it names the Phase, its Sections, their location anchors, durations and arcs. `/section-spec` refuses to build a Section Spec when Part 30 has no Section entry for the Section asked for, and tells the author that Part 30 must be expanded for it first; expanding Part 30 is the author's canon work and is not a spec flow. The spec chain for a later Phase therefore waits for Part 30 to be expanded for that Phase. `/next-phase` carries a note to this effect, and its Chapter Spec build step is refused by Rule 9.1.1 until the Section Spec and the Novel-Part Spec above that Chapter exist. `/next-phase` also closes the Phase's last Section (Section 8 at the end of Phase 1): it runs the Section-close reviews and asks the three completion confirmations once each, in the order Chapter, then Novel-Part, then Section (Rule 9.7.3); `/part-spec complete` and `/section-spec complete` remain available to the author. The Phase epigraph is a line of Part 30 and not of any spec, while the Section Spec of the Phase's first Section carries its own Epigraph line like every other Section Spec, and a Phase's first Area prints the two lines together, the Phase's first (Rule 10.3.1): no Phase Spec exists, and the author alone settles each line.

### 9.2 — Build Timing

**Rule 9.2.1 — Built at the boundary.**
Each spec is built when the story reaches the place that needs it. `/start-story` builds the first three, in this order: Section Spec 1.1, Novel-Part Spec 1.1.1, Chapter Spec 1.1.1.001. `/next-section` builds the new Section's Section Spec, then its first Novel-Part Spec, then its first Chapter Spec. `/next-part` builds the next Novel-Part Spec of the same Section, then its first Chapter Spec; the Section Spec must already hold an entry for that Novel-Part, and if it does not, the command stops and sends the author to `/section-spec revise` (Rule 11.5.1). `/next-chapter` builds the next Chapter Spec from the Novel-Part Spec's entry, and only that; it does not build a missing link above the Chapter (Rule 3.1.1). `/next-phase` builds nothing until Part 30 has been expanded (Rule 9.1.4). Inside one command the builds run top-down, each with its own consultation and its own `[CONFIRM SPEC]`, because each starts from its parent's confirmed answers (Rule 9.3.1). If a link already stands (built ahead under Rule 9.2.2, or kept through a reset under Rule 9.8.1), the command revises it, top-down, and never rebuilds it blind.

**Rule 9.2.2 — Built ahead, on request.**
The author may also run `/section-spec build` or `/part-spec build` for a LATER Section or Novel-Part, once its parent chain exists and is in force (Rule 9.1.1). A spec built ahead follows every rule of a spec built at the boundary: the same consultation, the same clarity mandate (Rule 9.6), the same light audit, the same confirm. Its settled items have settling power from its confirm, and stay open to the clarity-reduction re-ask of Rule 4.2.4 if the story moves before its boundary (Rule 9.2.3).

**Rule 9.2.3 — The built-against stamp and the boundary re-check.**
Every Section Spec and Novel-Part Spec records, in its header, a **built-against stamp** (Rules 10.2.1 and 11.2.1): the last completed Chapter reference (and the last completed Section reference, for a Section Spec) it was built against, the date, and which ledger entries its carry-in leaned on, by name and reference only, never as copied values (Rule 1.4.2). When the boundary command reaches a spec that was built ahead, it compares the stamp with the story as it now stands (the Chapters written since, the ledgers, the previous spec's Reader now knows line) and re-asks ONLY the items that the change touches. Each is a clarity-reduction question under Rule 4.2.4: it shows the original answer and the source of the change, and the fresh answer supersedes the old one on record. Items the stamp shows untouched are not re-asked. The carry-in item of the light audit (Rules 3.3.2, 10.5.1 and 11.6.1) makes the same comparison at Section and Novel-Part grain. What the comparison finds is shown to the author and never applied silently: a light change takes effect with a log line, and a substantial one follows Rule 9.4.2.

### 9.3 — Derivation

**Rule 9.3.1 — Pre-fill and provenance notes.**
A lower spec is built from the entry its parent keeps for it, and not from a blank page.

- The Section Spec's entry for a Novel-Part (Rule 10.3.3) pre-fills the Novel-Part Spec: its thematic movement, purpose, calendar window, who carries it, its opening state and closing state, and its Chapter list as a guide. Each pre-filled value is recorded in the Novel-Part Spec's notes as a From note naming the Section Spec entry.
- The Novel-Part Spec's entry for a Chapter (Rule 11.3.2) pre-fills the Chapter header (Rule 11.4.1): the title label, Chapter Purpose, Calendar Window, Threads Carried In and Out, Protagonist Thread Map, Opening hook and Closing beat. Each pre-filled value is recorded in the Chapter Spec's notes as a From note naming the Novel-Part Spec entry.
- Settled items of the Section Spec and Novel-Part Spec that bear on the unit are carried in as Inherited notes naming the source spec (Rule 9.5.1), and the author's deferrals to Area writing are carried in on the Chapter they bear on (Rule 9.5.2).

An inherited item never loses its note by being copied. The author refines a pre-filled value in the lower build. A value the author changes is recorded as the author's own answer in the lower spec, and where the change moves something the parent's entry fixes it is a departure (Rule 9.3.3). A pre-filled value the author does not change keeps its From note, and gains settling power only if the author explicitly answers it in the lower build (Rule 4.1.1), as with any other planner proposal (Rule 4.1.2).

*Names above Chapter grain are working labels.* A Novel-Part name in a Section Spec and a Chapter name in a Novel-Part Spec are labels for the plan. No Establishment status (`proposed` or `locked-at-Gate-1`) is stored in a Section Spec or a Novel-Part Spec; establishment is recorded in the Chapter Spec and in the delivered files (Rule 1.3.2). The light audit applies Part 28 Rules 18.4.1 to 18.4.3 to those labels as advice only. An Area named in a one-line outline is a descriptor and never a name (Rule 11.3.4).

*Calendar windows nest.* The Section's window (the Part 30 §1.3.2a anchor, or a value inside its latitude of two months either way) holds the windows of its Novel-Parts; each of those holds the windows of its Chapters; each Chapter holds its Areas. The light audit checks the nesting at each level (Part 30 Check 11-2). A window is cited from §1.3.2a and never copied (Rule 2.3.2). Every window is written as dates plus Phase Day, each end as Year, Month, Day and Phase Day. The Part 30 anchor is converted to dates by Part 41 Area 4, Phase Day conversion and Section windows, and a spec cites that Area and §1.3.2a, writes only its own window as the plan chooses it, and never copies Part 41's month table or its table of Section windows. The nesting is checked by dates: each lower window sits inside the one above it.

**Rule 9.3.2 — The Chapter header governs after confirm.**
After the Chapter's `[CONFIRM SPEC]`, the Chapter Spec, its header first, governs the Areas and Gate 1. The Novel-Part Spec's entry stays what it was when the Chapter was built, the **plan baseline**, and is not rewritten to follow the Chapter. Area-time agents read the Chapter Spec (Rule 9.9.2), and Check #18 compares the draft with the Chapter Spec and not with the entry (Rule 9.1.3). Every spec is intent, and the ledger supersedes it (Rule 1.3.1).

**Rule 9.3.3 — Materiality: what counts as a departure.**
A change flows back up the chain only for what the entry fixes: the Chapter's purpose, calendar window, threads in and out, who is on the page, key events, reveals owed, opening hook and closing beat. Splitting, merging, re-cutting or renaming Areas, and everything else the entry does not fix (anchors, continuation, opening and closing types, pacing, size targets, tags), is the Chapter Spec's own business and is not a departure. A departure is shown at the Chapter's confirm step, and also at the first step of `[REDRAFT CHAPTER]` and `[REDRAFT AREA]` when a revised plan departs from the fixed items (Rule 7.3.1). It is logged as a traced variance on EVERY spec above the Chapter, the Section Spec first and then the Novel-Part Spec, in one step, each note a LIGHT amendment appended by the Chapter flow (Rule 9.4.5). The author then says, for that departure, which it is: amend the plan (each spec above whose plan no longer fits is changed by its own command, Rule 9.4.3), or leave the original as the plan baseline. Both answers are lawful, and the Chapter Spec governs the Areas either way (Rule 9.3.2).

**Rule 9.3.4 — Spec-to-spec derivation is allowed (the neighbour of Rule 1.4.2).**
Rule 1.4.2 bars a spec from copying ledger content, and that bar is unchanged. A lower spec MAY copy or restate what its parent says about the unit it is built for, because the lower spec is the one the Area-time agents read (Rule 9.9.2); the copy is recorded with its source (Rule 9.3.1) so that nobody mistakes it for a second source of truth. Three limits stay: a copy never establishes canon (Rule 1.3.2); it never carries ledger values (Rule 1.4.2); and Part 30 is still cited by function name and never copied (Rule 2.3.2). Where a Reader now knows list or a thread list must be reused upward, it is cited by reference to the lower spec's own line, not copied (Rule 9.7.3).

### 9.4 — Precedence, Cascade, Writers

**Rule 9.4.1 — Precedence of scope.**
For what a level MUST DO, authority runs: Locked Canon, then the ledger, then the Section Spec, then the Novel-Part Spec, then the Chapter Spec. The lower spec governs its own detail. Rule 1.3.1 is unchanged (Locked Canon, ledger, spec chain as intent, session-log never). A conflict found while building a lower spec, between it and a higher spec or between a higher spec and the ledger, is a QUESTION to the author and never a silent pick. The author's answer amends the higher spec through the channel of Rule 9.4.5 (variance) or Rule 9.4.2 (amendment), and a ledger fact is never overruled by a spec (Rule 1.3.1). A lower spec that finds it cannot do what its parent asks of it does not quietly drop the duty: it raises it as that question.

**Rule 9.4.2 — Amending a parent after children exist.**
When the author amends a Section Spec or a Novel-Part Spec that already has children, the amending flow does not touch the children by itself. The continuity-checker reports every child entry and every child spec that the change no longer fits: which one, what no longer fits and why. For each, the author picks one of three: **keep** it (the variance is noted in the notes of the amended spec), **amend** it (through the child's own command), or **mark it `AMENDED-PENDING-RECONFIRM`**. Nothing flips automatically. Written Areas are never touched by a spec amendment: a correction there goes through `/revise-area` or a redraft (Rule 7.3.1), on the author's say.

- *Substantial* (Rule 3.5.2): changing a Section's or a Novel-Part's purpose, its closing state or hand-off, its calendar window, or the reveals it owes; and adding, removing or reordering the Novel-Parts of a Section Spec (a split or a merge counts as an adding and a removing). A substantial amendment sets the spec `AMENDED-PENDING-RECONFIRM`, runs the light audit, and needs a fresh `[CONFIRM SPEC]` before the amended content has any force. While a spec reads `AMENDED-PENDING-RECONFIRM` the chain is not in force below it (Rule 9.1.1), so the amending flow takes the audit and the confirm in the same run.
- *Light*: adding, splitting, merging or dropping Chapters in a Novel-Part Spec's list (the list is a guide); a change inside one Novel-Part Spec entry that leaves the Novel-Part's purpose, calendar window, reveals owed and closing state as they were (Rule 11.7.2); and writing a variance note. A light amendment takes effect at once with a log line.

A Chapter Spec's own amendments stay as Rule 3.5.2 sets them. Only substantial change needs a fresh confirm, for the two other kinds as for the Chapter Spec.

**Rule 9.4.3 — Writers.**
This rule extends Rule 1.2.3 to the chain. Spec files are written only by:

- (a) the `/section-spec`, `/part-spec` and `/chapter-spec` flows: the orchestrating command writes the spec file, its registry row and the session-log line, and the outline-planner builds each level but never writes a spec file;
- (b) the Gate 2 as-built sync, for the Chapter Spec and its registry row only (Rule 6.2.1); the Gate 2 pipeline stays three-way, and no Novel-Part Spec or Section Spec status is written at Gate 2;
- (c) the reconciliation pass of a reset or rewind, which changes statuses, stamps and the registry Coverage cells that the rollback changes (Rule 1.2.2), including the roll-backs of Rule 9.8.1, and never plan content (Rule 7.2.1);
- (d) completion, at `/next-chapter`, `/next-part` and `/next-section`, or by the `complete` mode of the matching spec command (Rule 9.7);
- (e) a lower-level flow, which may APPEND variance notes to the Audit and Settlement Notes of any higher spec it derives from (every spec above the departure, Rule 9.4.5) but may not change that spec's plan content. Plan content of a higher spec changes only through that spec's own command.

No other agent, command or audit writes to a spec file. Spec files are ordinary Markdown written with the Write and Edit tools; the authorized-scripts law covers novel output files only, no new script is created inside the repo for specs, and any helper a session needs lives outside the repo. The registry's Coverage cell for a Section row or a Novel-Part row is refreshed at that spec's own confirm, at any completion write step (a child's completion included) and at a reset or rewind rollback, and never at Gate 2 (Rule 1.2.2).

**Rule 9.4.4 — Write timing.**
Each new spec file is written at its OWN `[CONFIRM SPEC]`, so it is durable at once and a session that ends between two confirms loses nothing already confirmed. Only ONE confirm prompt is open at a time in a chain. The completion writes of the outgoing specs (the outgoing Chapter Spec, then its Novel-Part Spec, then its Section Spec, bottom-up, each only where the story has actually ended that unit, Rule 9.7.3) are made in ONE write step, at the LAST confirm of the chain, which is the new Chapter Spec's. The variance notes of Rule 9.4.5 are written in one step with the spec whose build, revision or departure gave rise to them, top-down: the note on the Section Spec first, then the note on the Novel-Part Spec, and then the lower spec itself. A Novel-Part entry added under Rule 9.1.2 has its own confirm and is written at once, not in the completion step. A `[SKIP SPEC]` at any level leaves every outgoing spec un-completed, and the command can be run again, as `/next-chapter` always could. A run again finds the chain partly built and revises it (Rule 9.2.1).

**Rule 9.4.5 — Variance flows upward (the traced channel).**
A lower-level flow appends a variance note to EVERY spec above the spec where a departure arose, written top-down in one step: the Section Spec first, then the Novel-Part Spec, and then the lower spec itself is updated (Rule 9.4.4). Three cases are fixed here. (1) A Chapter's departure from what its Novel-Part entry fixes (Rule 9.3.3) leaves a note on the Novel-Part Spec and a note on the Section Spec. (2) A Novel-Part Spec's departure from what the Section Spec's entry for it fixes (its purpose, calendar window or hand-off, Rule 11.4.3) leaves a note on the Section Spec. (3) A change of a Novel-Part Spec's Chapter list, whether a Chapter is added, split, merged or dropped (a Chapter added under Rule 9.1.2 included), leaves a note on the Section Spec and is shown to the author (Rule 11.4.3). Each note gives the date, the trigger, what differs and the author's answer, which the author gives for each departure: amend the plan, or leave the original as the plan baseline. A note is a light amendment: it changes no plan, re-opens nothing, and does not make the higher spec `AMENDED-PENDING-RECONFIRM`. Where the author chooses to amend the plan, each higher spec whose plan no longer fits is changed only through its own command, the Section Spec first (Rule 9.4.2); a lower flow never changes the plan content of a higher spec. Variance is a traced, light note in the higher record, and it reaches every spec above the departure. No range or count of Novel-Parts or Chapters is stored above Chapter grain (Part 2 Rule 9.3.1); a list is a guide, its length is information, and a list that grows or shrinks breaks no range.

### 9.5 — Settling Power and Deferrals

**Rule 9.5.1 — Settled items carry downward.**
A settled item in a Section Spec or a Novel-Part Spec that is `CONFIRMED` or `COMPLETED` is not re-asked in a lower BUILD. It is carried into the lower spec as an Inherited note naming its source (Section Spec or Novel-Part Spec) wherever it bears on that spec, and it reaches the Chapter Spec in the same form. Area-time agents read only the Chapter Spec (Rule 9.9.2), so the item has settling power at Area time through the Chapter Spec, and Rule 4.1.1's test reads accordingly: if the answer is discoverable in the settled and inherited notes of the active Chapter Spec, the question must not be asked. Only explicit author answers are carried this way. A Skipped note, a planner proposal, a pre-fill the author never answered, an open item, a `DRAFT` spec's content and the content of a spec that reads `AMENDED-PENDING-RECONFIRM` have no settling power to carry (Rule 4.1.2).

**Rule 9.5.2 — Deferrals: vocabulary and copy-down.**
Only the AUTHOR may defer a question. The planner never defers on its own (Rule 9.6.3). A deferral the author chooses is recorded as a Deferred note naming where the question goes: to a later spec (the planner brings the question up when that level is built, as an ordinary question), or to Area writing. A Section Spec may defer to any of the three destinations (the Novel-Part Spec, the Chapter Spec or Area writing); a Novel-Part Spec to a Chapter Spec or to Area writing; a Chapter Spec to Area writing. A spec may be `CONFIRMED` with such deferrals in it. A deferral to Area writing is copied into the Chapter Spec of each Chapter it bears on, as a Deferred note, so that the Area-time gate ASKS the author, as it asks about any open item (Rule 4.2.2). The drafter never settles it silently. When the author answers it at Area time, the Gate 2 sync settles it in that Chapter Spec (Rule 3.6.1 item 3), and the completion of the higher spec notes that the deferral was answered (Rule 9.7.3). An Open note is the state of a question raised and not yet answered: it appears while a build is under way, for a genuinely new branch that turns up after confirm (Rule 4.2.3), and in a retro-fit where the record gives no evidence and the author, asked, also leaves the matter open (Rule 9.8.2). A confirmed spec otherwise holds an item open only because the author deferred it.

**Rule 9.5.3 — Carve-outs: what settling power never reaches.**
The downward carry of Rule 9.5.1 never reaches the following, which stay as Part 38 Area 4 sets them:

- *Pacing.* Pacing is decided at Area grain in the Chapter Spec (Rule 2.3.3). No upper spec sets it, and no upper spec carries a pacing value.
- *Tone, voice, sensory and content fields.* They stay at Area grain (Rules 2.3.5a, 2.3.5b and 2.3.5d); no Section Spec or Novel-Part Spec carries one.
- *Part 36 Autonomous Matters.* They are never fixed above Area (Rule 4.2.5).
- *New branches and clarity reduction.* They apply at every level (Rules 4.2.3 and 4.2.4), with the stale higher answer shown to the author in the question.
- *Canon.* A settled item in an upper spec never establishes canon (Rule 1.3.2) and never outranks Locked Canon or the ledger (Rule 1.3.1).

**Rule 9.5.4 — Three linked guide registers: setups, payoffs and threads.**
The Section Spec, the Novel-Part Spec and the Chapter Spec each carry their own register of setups, payoffs and threads. Each is a GUIDE AND A SUGGESTION, never a block, so that the story keeps its freedom and the author keeps the choice of how it goes. They are linked by shared KEYS, which are the Part 30 Setups-table row number, or a short thread name:

- the Section Spec says which Novel-Part plants a setup and which pays it (Rule 10.3.4);
- the Novel-Part Spec says which Chapter plants it and which pays it (Rule 11.3.6);
- the Chapter Spec's Area fields, Planted here and Carried or paid off here, say where it actually lands (Rule 2.4.10). Those two fields are the register that Part 36 Areas 21 to 23 read.

The story may plant a setup elsewhere, pay it earlier or later, or drop it. `/threads` shows the plan beside what happened, as information. No check, gate, question or FAIL is created by a suggestion that was not met. How long a setup may wait is the plan's decision, set by the Section Spec and Novel-Part Spec plan lines, with no figure (Part 36 Rule 23.2.5); a thread-return stretch is a per-thread note in the Section Spec's threads table and reads `unset` until the author sets one (Part 36 Rule 26.4.4). One thing is asked about: a setup that has actually been planted (it stands in an Area's Planted here field) and is unpaid when a unit completes is put to the author at completion, as Rule 3.7.1 does for a Chapter (Rules 9.7.2 and 9.7.3). A suggestion nobody planted is never asked about. There are three linked guide registers, and the Chapter's Area fields are the one Part 36 reads; the Area-time register is single.

### 9.6 — Clarity Mandate (Rule 38.13)

**Rule 9.6.1 — The definition of done.**
One definition governs the Section Spec build, the Novel-Part Spec build and the Chapter Spec build. A build is done only when ALL of these hold, in this order:

1. there is no unasked branch at that spec's own level (Rule 9.6.2);
2. a final sweep by the outline-planner AND the continuity-checker finds nothing new (Rule 9.6.5);
3. the author gives an explicit "nothing further to steer";
4. then, and only then, the confirm token is asked for.

If the sweep returns anything, there are more rounds, and then a new sweep. There is no score, no percentage and no round count: the story decides when the author has said what the author wants to say. The author may stop earlier in two ways, a SKIP on a single question (recorded as a Skipped note) or `[SKIP SPEC]` for the whole spec (saved `DRAFT`, Rule 9.1.1). This is the same standard as Rule 3.2.2 (exhaustive clarity, the author's standing "DO NOT ASSUME" rule) and as Part 28 Rule 19.4 (persistent consultation until clarity), written once for all three builds; Rule 3.2.2 and Part 28 Rule 19.4 point here. A substantial amendment is consulted under Rule 3.5.1 on the items it touches.

**Rule 9.6.2 — The grain test.**
A question belongs to the level where the author's answer FIRST changes that level's own plan. A matter below that grain is not that spec's question at all: it is not deferred, it is simply asked when the level it belongs to is built. At the Section Spec the questions are the ones that set the Section's shape: the Novel-Parts and their order, thematic anchors, which Novel-Part carries each Part 30 function, the Chapter list at high level, setups by Novel-Part, protagonist arcs, the progression plan, opposition and reveals, the hand-off, the Epigraph (asked in every Section, the first Section of a Phase included, Rule 10.3.1; in the first Section of a Phase the build also puts the one question about the Part 30 `Epigraph:` line, which that Phase's first title page prints above Section 1's own), calendar windows, and the Part 30 rows that wait on the author (Rule 10.4.3). At the Novel-Part Spec they are the Chapters in depth (Rule 11.3.2), the cut and cliffhanger plan, the arc line and the closing state. At the Chapter Spec they are the Areas, anchors, continuation, types, pacing and sizes of section 2.4 and Rule 3.2.4. The direction and theme questions are asked inside the three builds, each at its own level: themes at the Section and Novel-Part, the opening beat at the Chapter. The grain test never bars a question that a new branch or a reduced clarity raises later (Rule 9.5.3).

**Rule 9.6.3 — The planner never leaves an item open on its own.**
Every field of every spec is put to the author: asked as a question where a real choice exists, or shown already filled from Part 30, the ledgers and the spec above it, for the author to edit (the practice of Rule 3.2.4). A field is never left blank, open or deferred by the planner, and the planner never settles a choice for the author. The planner may propose, and a proposal the author leaves alone has no settling power (Rule 4.1.2). Only the author may defer, and the deferral is recorded under Rule 9.5.2. The author may answer "let the first Area decide" to a question about the story, and that is recorded as a deferral to Area writing. The Section Spec build must surface every Part 30 `OPEN-AUTHOR` row due in, or planted by, its Section (Rule 10.4.3).

**Rule 9.6.4 — The shape of a question.**
The law of Rules 3.2.2 and 3.2.3, Part 28 Rule 19.4 and Part 36 Area 13 governs all three builds. Each question offers 2 to 3 concrete options plus `SKIP — let AI decide`, four in all; direction options carry a one- or two-sentence narrative preview in Part 36 thematic voice, with exposition-risk options flagged; up to four questions go in one `AskUserQuestion` call; as many rounds are put as the build needs; what canon or a higher settled item already settles is not asked (Rule 9.5.1); and the words are plain and everyday, as `guardrails/quality/guardrail-plain-language.md` requires of everything put to the author. Naming is never offered as a cost, risk or downside of an option, and where an option could name an entity or leave it unnamed the named one is the recommended one (Part 28 Rule 20.9). A SKIP never settles anything. **There is no quick build for any of the three** (Rule 3.2.5): the per-question SKIP and `[SKIP SPEC]` are the author's ways of going faster. A per-question SKIP is recorded as a Skipped note.

**Rule 9.6.5 — The final sweep.**
After the last round and before the author is asked whether anything is left to steer, the outline-planner AND the continuity-checker make a final sweep of the whole drafted spec. They look for conflicts with Part 30, with the ledgers and with the spec above, and they RE-LIST every Skipped note and every deferral, so that the author has a last chance to answer or change each one. The sweep is the same pair of agents as the light audit (Rule 3.3.1) and may share one pass with it. The checker only reports; the planner turns what is found into questions for the author. A sweep that finds nothing new leads to the question "Is there anything further you want to steer?"; a sweep that finds something leads to more rounds and a new sweep. Blocking findings of the light audit must be resolved before `[CONFIRM SPEC]` is accepted (Rules 3.3.2, 10.5.1 and 11.6.1).

### 9.7 — Completion

**Rule 9.7.1 — COMPLETED, never closed; specs stay living.**
No spec is closed. All specs are living records. The spec status for all three kinds is `COMPLETED`: all of the unit's Areas are written. For a Chapter Spec the Gate 2 sync sets the status when the last Area is written, and the completion pieces follow at `/next-chapter` or `/chapter-spec complete` (Rule 9.7.2); for a Novel-Part Spec and a Section Spec the status and the completion pieces are written together, in one step, on the author's yes (Rule 9.7.3). A `COMPLETED` spec stays open to revision. `revise` works on it at any time, there is no "only through redraft" refusal, and a revision that changes plan content for Areas already written does not by itself redraft anything: whether to redraft is the author's call. A light revision leaves the spec `COMPLETED`. A substantial one sets `AMENDED-PENDING-RECONFIRM` (Rule 3.5.2) and, once re-confirmed, the spec returns to `COMPLETED` if its record is still whole, or to `CONFIRMED` if written Areas have since rolled back. When a `COMPLETED` spec is revised, its completion pieces are refreshed. A completed spec is a durable planning record from which later work can read the history without opening the Areas.

**Rule 9.7.2 — Chapter completion.**
A Chapter Spec's status becomes `COMPLETED` through the Gate 2 sync when its last Area is written, every Area being terminal (`WRITTEN`, or `DROPPED` with its variance note) (Rule 3.6.1 item 1; this changes no write set, Rule 6.2.1). The completion CONTENT is written later, at `/next-chapter` or by `/chapter-spec complete`, after the same questions: the command verifies that every Area is terminal, puts the unresolved open items, the unpaid setups and the unresolved cliffhangers to the author through `AskUserQuestion` (resolve, carry forward, or mark lapsed, lapsed only on the author's answer), runs area-scorer for the Chapter-level CDL-2 Aggregate Block (information only), and then writes the final variance summary, the Reader now knows line, the Chapter digest and the completed New named things line (Rule 3.7.1). Until then the Completion Record of the spec reads as not yet written.

**Rule 9.7.3 — Novel-Part and Section completion, at the boundary, on the author's yes.**
The boundary command completes a Novel-Part Spec or a Section Spec, and only on the author's yes. `/next-part` asks "Has this Novel-Part finished?", and `/next-section` asks "Has this Section finished?", as part of their checks; the author judges, because the story and not the plan ends a unit (Rule 1.5.1). On yes, the spec becomes `COMPLETED` and its completion content is written in the same step that confirms the successor (Rule 9.4.4); on no, the command stops. A Novel-Part Spec is completed only when every Chapter Spec under it is `COMPLETED` (the last one in the same step) or `RETIRED` with a variance note, or was never written and is recorded as dropped on the author's yes, and a Section Spec only when every Novel-Part Spec under it is `COMPLETED` (the last one in the same step) or `RETIRED` with a variance note, or was never written and is recorded as dropped on the author's yes; if one is not, the command names it and stops. At the end of a Phase there is no next Section to open, so `/next-phase` is the boundary command: it runs the Section-close reviews and asks the completion of the last Chapter Spec, the last Novel-Part Spec and the Phase's last Section Spec (Section 8 at the end of Phase 1) once each, in that order, and writes them bottom-up in one step (Rule 9.7.2). The author may instead run `/part-spec complete` and then `/section-spec complete`, each of which writes at once, bottom-up; where the last Chapter's completion pieces are not yet written, `/part-spec complete` takes the `/chapter-spec complete` questions for that Chapter first and writes its pieces in the same bottom-up step. The completion content of a Novel-Part Spec or a Section Spec is:

- the final variance summary: the plan against what was written, including Chapters (or Novel-Parts) added or dropped, and the deferrals that were answered;
- the Reader now knows line, by reference to the last child's line plus what the unit itself adds, with no copy of lists;
- the digest;
- the threads and setups carried to the next unit, the author being asked about each one actually planted and still unpaid, and lapsed only on the author's answer.

Informational reports at the end of a Novel-Part or a Section (reveals not yet given, threads, Part 30 functions not carried) are shown to the author and never block (Rule 9.7.4). A `COMPLETED` Novel-Part Spec or Section Spec is a living record under Rule 9.7.1, as Rules 10.6.2 and 11.7.2 say for each.

**Rule 9.7.4 — The active unit, and informational reports.**
For `/status`, the "active" Section, Novel-Part and Chapter are, in each tier, the first spec whose status is neither `COMPLETED` nor `RETIRED`, so a confirmed successor that has not been opened (after a late skip, or a spec built ahead) is not "current". The statuses of the Novel-Part Spec's Chapter entries and of the Section Spec's Novel-Part entries are derived from the child spec and the registry, and are never stored (Rule 11.3.5). The reports at the end of a Novel-Part or a Section follow the pattern of Rule 3.7.2: they set no target, raise no warning and block nothing, and the author reads them against Part 30.

### 9.8 — Resets, Retro-fit, Orphans

**Rule 9.8.1 — Survivability and roll-back.**
Rule 7.1.1 applies to all three kinds: no reset, rewind, restore or redraft command deletes a spec file. `[HARD RESET]` (C-1) is the one exception, and it deletes ALL THREE kinds (Rule 7.1.2); it empties the registry to its three tables' header rows. The registry is one `_index.md` with three tables, and it holds nothing else that is a table, because the reset empties every table in it. Every other command keeps every spec. When a command removes written Areas, the reconciliation pass (Rule 9.4.3) makes these status changes and no others to plan content: a `COMPLETED` Chapter Spec returns to `CONFIRMED`; a `COMPLETED` Novel-Part Spec or Section Spec returns to `CONFIRMED` whenever any child returns to a status other than `COMPLETED`; completion text is kept as history, and is refreshed at the next completion. A Chapter re-opened for redraft returns to `CONFIRMED` where the plan does not change, or to `AMENDED-PENDING-RECONFIRM` where it does. Settled notes survive every roll-back (Rule 7.2.2). This extends Rules 7.1.1, 7.1.2 and 7.2.1: the spec is the record of intent and the loss of written Areas does not destroy intent.

**Rule 9.8.2 — Retro-fit.**
This generalises Rule 3.1.2. A standalone `/part-spec build` or `/section-spec build` over a Novel-Part or a Section that already has written Chapters is a retro-fit. Statuses come from the record; fields the record gives no evidence for are put to the author, and each is recorded as the author answers it, or as an author deferral, or as an Open note where the author also leaves it open; the notes say "as-built, reconstructed [date]". The retro-fit goes through the same consultation, audit and `[CONFIRM SPEC]` as any build, and needs its parent chain in force (Rule 9.1.1), so a retro-fitted chain is built top-down. The same applies where a higher spec file has been deleted by hand.

**Rule 9.8.3 — The orphan rule.**
Retiring a Section Spec or a Novel-Part Spec is explicit and never silent (Rule 7.2.2), and it is refused while any of its children is not itself `RETIRED`, until the author has ruled on each such child. The command lists the children, the author's ruling on each is recorded in the notes of the retiring spec, and the retirement then goes ahead. A spec that stands under a `RETIRED` parent is dormant: Rule 9.1.1 refuses its revision, and no Area is written under it. This keeps a spec from being left under a parent that has gone without the author having said so.

### 9.9 — Reads, Agents, Orchestration

**Rule 9.9.1 — Who builds, audits and writes.**
The outline-planner BUILDS each level, one planner for each level; it never confirms its own work and never writes a spec file, and it never writes an Epigraph (Rule 10.3.1). The continuity-checker runs the light audit and the final sweep, and it is report-only in a spec build and writes nothing. The orchestrating command writes the spec files and the registry rows (Rule 9.4.3). area-maker and area-scorer are unchanged. The scope of the light audit for each level is set once, where its spec is defined: the Chapter Spec in Rule 3.3.2 (with its item (g), that the header fields are consistent with the Novel-Part entry or are noted departures), the Section Spec in Rule 10.5.1 and the Novel-Part Spec in Rule 11.6.1. It reports only, and its blocking findings must be resolved before `[CONFIRM SPEC]` is accepted.

**Rule 9.9.2 — Read sets.**
The agents that BUILD or audit a spec read the whole chain above their level, IN FULL:

- the Section Spec build reads the whole of the Part 30 skill file, every time, consolidated file first (`guardrails/authority/guardrail-consolidated-skill-reading.md`);
- the Novel-Part Spec build reads the whole Section Spec;
- the Chapter Spec build reads the whole Section Spec and the whole Novel-Part Spec.

The PER-AREA agents (area-maker, area-scorer, both Gate 1 checker instances, and the outline-planner when it plans a single Area; the planner is a per-Area agent only then, and reads the whole chain above the level it builds when it builds a spec) read the Chapter Spec in full, its Audit and Settlement Notes included, and from the Novel-Part Spec only its header block and its closing-state block (blocks 0 and 8 of Rule 11.2.1). The Section Spec is not in the per-Area read set. This is an explicit exception to the standing rule that every mandatory read stays in full, and it cuts nothing down: those upper-spec reads are simply not mandatory for the per-Area agents, whose Chapter Spec carries what they need from above, each item noted with its source (Rules 9.3.1 and 9.5.1). Where an upper spec, or a block of one, is in an agent's mandatory set, it is read in full. No agent works from a half-read source.

**Rule 9.9.3 — Parallel orchestration, and Plan Mode to Auto Mode.**
At the start of a command that builds in the chain, everything that does not depend on an answer is launched together: the planner grounding for each level the command will build; the closing-unit reviews that already run side by side (the area-scorer aggregate, the Section-close continuity review, the FCIA and ALCA chain in `/next-section`); and one continuity-checker pre-read that serves all the audits. Consultation and confirmation then run strictly top-down (Section Spec, Novel-Part Spec, Chapter Spec), because each takes its parent's confirmed answers; each lower planner is told through `SendMessage` that its parent is confirmed and then finalises. In `/next-section`, the Section-close Check #21 ledger writes (steps 2a and 2b) land BEFORE the Section Spec's audit, because the audit's carry-in item reads the ledger. The two questions of step 2c and the Section Spec consultation are separate question streams and are never mixed in one `AskUserQuestion` call. The consultation of each of the three spec commands IS its Plan Mode (`guardrails/commands/guardrail-plan-then-auto-execution.md`, to which the three commands are added); the confirm token is a hard pause that Auto Mode never waives, as `[CONFIRM WRITE]` is at Gate 1.

**Rule 9.9.4 — Named items and naming in spec builds (the single paragraph; the three spec commands point here).**
A named item (Part 28 Rule 20.8.1: a made or used thing with a proper name of its own) is written in italic wherever it is mentioned in a spec file, whoever's words it came from, the name only and in the register's form for an item already registered (Part 28 Rule 20.8.2). Anything that is an item counts (an apparatus, remedy, gear, food, drink, dress, a relic or artifact, a formation array, an energy cache and the rest); the article is never part of the name (`the *Hourline*`); a word that is a registered item name is never italicised for emphasis; a named map, letter or other document is italic too, and an agreement, treaty or accord stays roman (Part 28 Rule 20.8.7). Item registration: a named item a spec plans is an in-world name that is `proposed` and establishes nothing (Rule 1.3.2); a name met in a consultation enters no register row; its row in `ledger-named-items/_index.md` is made at the Gate 2 of the Area that first writes it (Part 28 Rule 20.8.4; the Chapter Spec's Name note flips to `locked-at-Gate-2` with its reference, Rule 3.6.1 item 1). A monster name is set in roman, is never a named item, enters no ledger entry before its first Area (Part 40), and is `proposed` in the Chapter Spec that defines its Kind (Part 40 Rule 40.7.5.1). Naming is never a cost: in every round, option and recommendation of every spec build, naming a person, thing, place, move or any other entity is never presented as a cost, risk or downside, the ledger work a name creates is never weighed against an option, and where an option could name or leave unnamed, the named version is the `(Recommended)` one (Part 28 Rule 20.9; the consultation for MAJOR names stays as Part 28 Area 20.4 sets it).

### 9.10 — The Clean Body and the Audit and Settlement Notes (Rule 38.14)

**Rule 9.10.1 — The body reads clean.**
A spec file of any of the three kinds carries no inline `[SETTLED …]`, `[OPEN …]`, `[ASKED …]`, `[SKIPPED …]` or `[FROM …]` tag, and no provenance, ruling, date-of-answer or audit tag, anywhere in its body. The body is plain plan text, written so that it can be read start to finish as the plan. An item that a rule calls settled, open, deferred, skipped or inherited is recorded as a note in the final section (Rule 9.10.2), and a rule that asks whether an item is settled or open looks there. The body may hold ordinary statuses and values (a spec status in the header, an Area status in its block, a name, a window, a pacing), because those are plan and state and not provenance. The optional author levers of Rules 2.3.5a, 2.3.5b and 2.3.5d are plain fields of the Area block and are not tags in this sense.

**Rule 9.10.2 — The Audit and Settlement Notes section.**
Every spec ends with one section, **Audit and Settlement Notes**, the last section of the file (section 7 of the Chapter Spec template, block 12 of the Section Spec template, block 11 of the Novel-Part Spec template). It is the one place where the following are gathered, each as a plain line that begins with the plan item it concerns, named by Area, field or heading, and then the kind of note:

- **Settled** — the author's explicit answer to a question, with the answer and the date; it has settling power under Part 28 Rule 19.4 once the spec is CONFIRMED (Rule 4.1.1).
- **Skipped** — the author skipped the question and the planner chose a value; it records the planner's choice and has no settling power (Rule 4.1.2).
- **Open** — a question raised and not yet answered (Rule 9.5.2); asked at the build, or at the Area-time gate where it bears on the Area (Rule 4.2.2).
- **Deferred** — a question the author chose to defer, with where it goes (the Novel-Part Spec, the Chapter Spec, or Area writing) and the date (Rule 9.5.2).
- **From** — provenance of a pre-filled value, naming the entry of the spec above it was taken from (Rule 9.3.1).
- **Inherited** — a settled item of a higher spec carried in, naming the source spec, the answer and the date (Rule 9.5.1).
- **Name** — the Establishment status of a name (`proposed`, `locked-at-Gate-1`, `locked-at-Gate-2`, with the establishing reference) and, for a Debut, its consultation status (Rules 2.3.1 and 2.3.4). Chapter Spec only.
- **Variance** — a departure, a rollback, a sync correction or a note appended by a lower flow, with the date, the trigger (Gate 2 ref or command), what differs and the author's ruling where one was asked (kept as plan baseline, amended, or pending reconfirm) (Rules 3.6.1, 7.2.1 and 9.4.5).
- **Audit** — the result of the light continuity audit and the final sweep, and any note the sync leaves about itself (for example that a spec was built as-built, or that a size exception was accepted).

A note points back to the plan item by name so that the reader can find it from the notes, and the notes are the audit trail of the plan. A Settled, Skipped, Open or Deferred note whose plan item has been replaced by a later answer is not deleted: the later note is added beneath it, so the section stays an honest record. Notes are appended by the build flow, the Gate 2 sync (Chapter Spec only), the reconciliation pass, the completion step and a lower flow's variance channel (Rules 1.2.3 and 9.4.3), and by no one else. The section is kept in plain list form, in the order the notes were made, and is never a table that a reset script could empty.

**Rule 9.10.3 — Every rule that reads a settled or open item reads the notes.**
An open item is found in the Audit and Settlement Notes: Gate 1 Check #18, the Area-time Decision Consultation Gate, the light audit, the final sweep, `/status`, `/threads` and the completion questions all read open and deferred items there. A Settled note and an Inherited note are the settled inputs of Part 28 Rule 19.4. The light audit checks that the body is clean and that the section stands at the end of the file (Rules 3.3.2(h), 10.5.1(k) and 11.6.1(i)). A spec whose body holds an inline tag or whose last section is not the Audit and Settlement Notes is corrected by the build flow before `[CONFIRM SPEC]` is accepted.

**Illustration, establishes nothing (Rule 1.3.2).** The lines below are what the notes of the invented Area of section 2.5 would read as, in the last section of a Chapter Spec. Names are placeholders.

```markdown
## 7 — Audit and Settlement Notes

- **Area 02, Want, obstacle, stake** — Settled: win at a cost.
- **Area 02, Scene anchors** — Settled: three anchors, one complete scene in one Area.
- **Area 02, Size target** — Settled: 2,000 words.
- **Area 02, Pacing (planned)** — Settled: Medium.
- **Area 02, Cross-references** — Open: Area 05 is a proposal; the delivery Area is not yet fixed.
- **Area 02, Planted here** — Open: whether the second pole pays off in Area 05 or in no Area.
- **Area 02, Name** — The Ford at Low Water: proposed. The Ford Keeper: proposed, Area 20.3 pending, minor, AI-named at drafting.
- **Header, Opening hook** — From: Novel-Part Spec entry for Chapter 002.
- **Header, Calendar Window** — Inherited from Novel-Part Spec: days 2 and 3 of the Novel-Part window.
- **Area 02, whether Hero A offers payment at the ford** — Deferred by the author to Area writing.
- **Whole spec, light continuity audit** — Audit: PASS, no blocking finding.
```

---

## Area 10 — The Section Spec

This Area holds everything that belongs to the Section Spec alone: its file, its template, its field law, its build, its light audit and its completion. The rules that all three kinds of spec share — the chain rule, derivation and pre-fill, precedence and the cascade, settling power and deferrals, the clarity mandate, resets, retro-fit and orphans, reads and agents, the clean body and the notes — are in Area 9 and are cited here, never repeated. The Novel-Part Spec is Area 11. The Chapter Spec is Areas 2 to 4. In one sentence, **Rule 38.10 (Section Spec)**, which this Area elaborates, says: every Section has exactly one Section Spec at its tree path, built through an author consultation that always starts from the whole of Part 30 and runs until the clarity mandate (Rule 38.13) is met, and it must be CONFIRMED or COMPLETED before any Novel-Part Spec of that Section can be built or revised (Rule 9.1.1).

### 10.1 — Purpose and File Law

**Rule 10.1.1 — Purpose, and what the Section Spec is not.**
The Section Spec is the author-confirmed plan of one Section of the Phase, built before any Novel-Part of that Section is planned. It reads what Part 30 expects of the Section and, through the author's answers, turns that into the Section's Novel-Parts and, for each Novel-Part, a high-level list of Chapters. Its job is to give every Novel-Part Spec build a settled frame: the Section's arc and the order its turns come in, which Novel-Part carries which Part 30 function, where each thread is planted and paid, and where each of the eight protagonists stands, so that the Novel-Part Spec build asks only what is genuinely open at Novel-Part grain (Rule 9.6.2) and does not work the Section out again. The Section Spec is the top of the spec chain (Rule 9.1.1). Above it stands only Part 30, which is the Phase-level plan; no Phase Spec exists (Rule 9.1.4). The Section Spec is not prose and not an outline shown to the reader. It is not a ledger (Rule 1.4.1) and never restates a ledger value (Rule 1.4.2). It is not a copy of Part 30 (Rule 10.3.2). It is not a source of canon facts (Rule 1.3.2): every name, event and reveal in it is intent until delivered Areas establish it. It never stores a count or a range of Novel-Parts or Chapters, and it plans no tone, voice, pacing or sensory tag (Rule 10.3.8). Like every spec it binds planning conduct and never the story (Rule 1.1.2): a Section Spec that the story outgrows is amended, or varied on record, and the Areas are never bent to fit it (Rule 1.5.1). Deriving one spec from another is allowed and is noted; copying ledger values into a spec stays barred (Rule 9.3.4).

**Rule 10.1.2 — File path and reference.**
Each Section Spec lives at `.claude/story-memory/phase-section-part-chapter-area-specs/phase-N/section-N/section-N-spec.md`, as a sibling of the `part-N/` folders of that Section. Folder naming follows Part 2 Rules 5.2.2 to 5.2.5 and Rule 1.2.1. Its reference is `P.S`, Phase number then Section number (Section 2 of Phase 1 is `1.2`). Exactly one Section Spec exists per Section; a `build` over a Section that already has one is a revision (Rule 9.4.2) and never writes a second file. The file is written, with the ordinary Write and Edit tools by the `/section-spec` flow, at its own `[CONFIRM SPEC]` and is durable from that moment (Rule 9.4.4); the Gate 2 sync never writes it (Rule 9.4.3). Its registry row sits in the Section Specs table of `_index.md` (Rule 1.2.2) with the columns Spec File, Ref, Status, Spec Ver, Last Updated and Coverage. For a Section the Coverage cell reads "Novel-Parts completed / planned; Chapters completed / planned" and is refreshed at this spec's own confirm, at any completion write step (the completion of a Novel-Part Spec or a Chapter Spec under it included) and at a reset or rewind rollback, and never at Gate 2 (Rule 1.2.2); its "planned" figures are read off the lists as they stand: they are information and never a range.

### 10.2 — The Template

**Rule 10.2.1 — Canonical Section Spec template.**
One schema serves every Section Spec: Rule 2.1.1 applies to this template as it does to the Chapter Spec's, and decisions are recorded in the notes in the forms Rule 9.10.2 lists. The five spec statuses are those of every kind of spec (Rule 9.7.1). They describe the *spec* and are not the Area status of Rule 2.4.9.

```markdown
# Section Spec — [Section N: Section Name] (Ref: P.S — e.g. 1.2)

**Governing Law:** Part 38 — Story Specification Law (spec-story-specification-law)
**Spec Status:** [DRAFT / CONFIRMED / AMENDED-PENDING-RECONFIRM / COMPLETED / RETIRED]
**Spec Version:** v1.0 | **Confirmed:** [YYYY-MM-DD via [CONFIRM SPEC] / — ]
**Last Updated:** [YYYY-MM-DD]
**Light Continuity Audit:** [PASS YYYY-MM-DD / pending]
**Built-against stamp:** [the last completed Chapter reference and the last completed Section reference (or `story start`), the date, and the ledger entries the carry-in and the arcs lean on, by name only | — until built]

---

## 0 — Header Block

**Name-chain:**
- Phase [N] — [Phase Name] (locked, Part 30 Locked Canon)
- Section [N] — [Section Name] (locked, Part 30 Locked Canon)

**Epigraph (the title page of this Section):** [the epigraph text and its source | unset]
**Section calendar window (Part 30 §1.3.2a; dates plus Phase Day, Part 41 Area 4):** [`anchor`, or a chosen duration inside the ±2-month latitude with the reason; the window that results, as dates plus Phase Day (the first day and the last day, each as Year, Month, Day and Phase Day); protagonist ages at the opening and the close where age matters. Cites §1.3.2a and Part 41 and never copies either table]
**Carry-in from the previous Section:** [each thread coming in, with its state at entry; a reference to the previous Section Spec's Reader now knows line; unresolved questions and consequences arriving | `story start`]

## 1 — What Part 30 Expects of This Section (citations only — Rule 2.3.2)

| Part 30 item (by function name, section number or Law ID) | Locked / Negotiable | Where this spec carries it |
|---|---|---|
| Location anchor | [as Part 30 and Part 28 mark it] | [block] |
| Duration (§1.3.2a) | [Locked at the anchor; ±2 months Negotiable] | block 0 |
| Thematic focus | [mark] | block 2 |
| Section arc | [mark] | block 2 |
| [each Major Narrative Function, by name] | [mark] | [the Novel-Part entry in block 3 that carries it] |
| Section-close cultivation band for each protagonist (§1.3.2) | [Locked; the path is Negotiable] | block 6 |
| Power, technology and political-scale trajectory of the Section | [mark] | block 6 |
| Locked events for this Section | Locked | [block] |
| Protagonist arc advancement lines for this Section | [mark] | block 5 |
| Part 30 Setups and Payoffs Table rows that touch this Section [row numbers] | [mark] | block 4 |
| OPEN-AUTHOR and OPEN-AREA rows due in or planted by this Section [row numbers] | open | [answered in block 4 or 9, or deferred in the notes] |

## 2 — Section Arc as Planned

**How this Section realises the Part 30 arc:** [3–8 sentences: the Section's movement and the order its turns come in]
**Escalation order:** [the Section's turns in order, each marked with the Novel-Part (block 3) it lands in]

## 3 — Novel-Part Plan (one entry per Novel-Part; the list is a guide and never a count — Rule 10.3.3)

### Novel-Part [N] — [working label]
**Purpose (Part 30 functions by name):** [what the Novel-Part does for the Section arc]
**Thematic movement:** [where the Novel-Part starts and where it has moved to]
**Place or places:** [place — ledger reference by name, or `none yet`]
**Calendar window (inside the Section window):** [in-story span as dates plus Phase Day (Part 41 Area 4); ages where age matters]
**Part 30 functions this Novel-Part carries:** [function names, whole or in part]
**Carried by (the eight protagonists):** [each of the eight: carries / on the page / off the page, with where each off-page protagonist stands; no count and no target]
**Opening state:** [where the story, the protagonists and the threads stand as it opens]
**Closing state and hand-off:** [where it leaves them, and what the next Novel-Part inherits]
**Pacing:** [Fast | Medium | Slow | unset; the author's call, with the one-line reason] *(Amended 2026-10-07; Rule 10.3.9)*
**Word budget:** [N words for the Novel-Part, a guide the Novel-Part Spec and the Chapter Specs refine, or `unset`; the author may raise it] *(Amended 2026-10-07; Rule 10.3.9)*
**Chapters (high level — a guide the Novel-Part Spec may add to, split, merge or drop):**
1. [working title] — [one line]
2. [working title] — [one line]

### Scene Map (across Novel-Parts) *(Amended 2026-10-07; Rule 10.3.9)*

| Scene ID | Novel-Parts covered | POV sequence | Scene arc | Scene pacing | Scene word budget | Join state at each Novel-Part seam |
|---|---|---|---|---|---|---|
| [SS1] | [e.g. 2-3] | [each POV in order, with the Novel-Part where each takes over] | [the movement of the scene] | [Fast / Medium / Slow] | [N words] | [the exact state at each Novel-Part seam] |

*(an empty table means no scene runs across Novel-Parts)*

## 4 — Threads, Setups and Payoffs (a linked guide — advisory only)

| Key (Part 30 Setups table row number, or a short thread name) | What it is (short name) | Planted in Novel-Part | Returns in Novel-Part | Pays in Novel-Part | Thread-return stretch (optional) | Note |
|---|---|---|---|---|---|---|
| [key] | [name] | [N] | [N, or none] | [N, or none] | [note | unset] | [—] |

## 5 — Protagonist Arc Map (Part 30 P30-7)

| Protagonist | Part 30 arc line for this Section (cited by name) | Planned movement across the Section | Novel-Part or Novel-Parts that carry the main beats | Thread state at entry | Thread state at exit |
|---|---|---|---|---|---|
| [one row for each of the eight protagonists] | | | | | |

## 6 — Progression Plan (a guide against the Part 30 §1.3.2 map)

| Novel-Part | Cultivation beats | Technology beats | Named-move beats | Note |
|---|---|---|---|---|
| [N] | [step — protagonist] | [step] | [step] | [—] |

**Section-close band:** [each protagonist's band at the close is Locked in §1.3.2 and is cited here, never copied; nobody is planned above their band before the close]

## 7 — Opposition and Pressure

**Pressure by Novel-Part:** [which villain or faction pressure shows in which Novel-Part, and how it presses; Part 18 and the ledgers by name]
**Reveal timing (Reader-Reveal Timing Law, `.claude/guardrails/audit/guardrail-fcia.md`):** [each reveal about an opposing force: the Novel-Part it is planned for, and the latest Novel-Part it may arrive]

## 8 — Knowledge, Reveals and Consequence Carry-Over

**Reader and character knowledge:** [what the reader learns and when; where the reader knows more than a character, and the reverse (Part 24 N24-1, at Section grain)]
**Reveals owed this Section:** [each reveal, with the Novel-Part it is expected in]
**Consequences carried in and cast forward:** [pending cascades from earlier Sections that land here, and the shadows this Section casts into later ones (Part 30 P30-11; Part 27); ledger entries by name]

## 9 — Section Close Hand-Off

**Where the Section leaves the story:** [the closing state of the story, the protagonists and the threads]
**What the next Section inherits:** [residue, unresolved tension, planted seeds (Part 2 Tier 2, section 1.2.3, Inter-Section Relationships); for Section 8, the Phase Transition items]

## 10 — Standing Exclusions (by reference)

Standing exclusions are those of Chapter Spec template section 3 (Rule 2.2.1; Rule 2.3.7). They are verified at build and at every audit and amendment of this spec. The list is not pasted here.

## 11 — Completion Record

[Written at completion (Rule 10.6.1); reads "not yet written" until then.]
**Final Variance Summary:** [planned versus as-written, in brief, including Novel-Parts and Chapters added, split, merged or dropped]
**Reader now knows:** [by reference to the last Novel-Part Spec's line, plus the Section-level additions; no copy of lists]
**Section digest:** [for each Novel-Part what changed, who, and the open threads, by reference to the Novel-Part digests]
**Carried to the next Section:** [threads and setups still open, each marked carried or lapsed; lapsed only on the author's answer]

## 12 — Audit and Settlement Notes

[The last section of the file. Every settled, skipped, open, deferred, from, inherited, variance and audit note, each pointing to the plan item it concerns by block or heading (Rule 38.14; section 9.10). The variance log lines appended by this flow and by lower flows (Rule 9.4.5) are kept here, each with the date, the trigger (command, or the lower spec and entry), the variance and the author's ruling (kept as plan baseline / amended / pending reconfirm).]
```

### 10.3 — Field Law

**Rule 10.3.1 — Header, Epigraph, calendar window and carry-in.**
*Name-chain.* The Phase and Section names are Locked Canon from Part 30, copied from it and shown as locked.

*Epigraph.* This line is a line of the Section Spec (Rule 2.4.11). It holds the text of the epigraph for the Section's title page and its source. The author settles it at this spec's `[CONFIRM SPEC]`, and it reads `unset` until then. `unset` means this spec gives the title page no epigraph line, and no agent writes one. The Phase epigraph is not a line of this spec. It is a line of Part 30 (`narration-novel-macro-story-law`, the `Epigraph:` line of the Phase definition), which reads `unset` until the author gives the text and is never written by an agent; no Phase Spec exists to hold it (Rule 9.1.4). A Phase's first Area prints the Part 30 Phase epigraph first and then Section 1's own Epigraph from its Section Spec, as two lines of its title page, and the opening Area of every other Section prints only that Section's own Epigraph from its Section Spec. The Section Spec of a Phase's first Section carries its own Epigraph line in its header block, like every other Section Spec, and the Phase epigraph does not replace it: a Phase's first title page prints both. The build asks the Section epigraph question as it does for any other Section and, in the first Section of a Phase, also puts the one question about the Part 30 line (what the line reads now, and whether to give or change it), which `/section-spec` puts once (topic 12) and `/start-story` does not ask again. The author alone settles each line, and each is read from a confirmed source. The author sets the Phase epigraph by editing Part 30, or by telling the command that is running, which asks first and then records the author's words in Part 30 as an author-directed one-line edit; no agent ever writes epigraph text. Where the author skips the epigraph question of any Section, the planner's choice is always `unset`, recorded as a Skipped note. The command that writes the Area (`/next-area`, which `/start-story`, `/next-section` and `/next-phase` run for the opening Area of a Phase or a Section) passes TWO lines to the writers on a Phase's first Area, the Part 30 Phase epigraph and, below it, this spec's Epigraph (Section 1's own); on the opening Area of every other Section it passes this spec's Epigraph alone. `unset` means none, for either line. The two authorized writer scripts take the two values as `--phase-epigraph-file` (the Part 30 line, given only on a Phase's first Area, which a writer refuses on any other Area) and `--section-epigraph-file` (this spec's Epigraph). A redraft of a Section's first Area reads the line or lines from the same places, so they are not lost. The value of the Part 30 line is the text after the label `Epigraph:` on the Phase definition's Epigraph line, up to the end of that line (`Epigraph: unset` means none); the explanatory note beneath it, on its own line, is never part of the value. A command reads that one line itself, because Part 30 is not in the per-Area read set (Rule 9.9.2), and passes only that text, never the label. The value of a Section Spec's Epigraph is what its Epigraph line in the header block holds after the field label (the epigraph text and its source), and `unset` means none.

*Calendar window.* The Section's duration is the anchor value of Part 30 §1.3.2a or a value the author chooses inside the ±2-month latitude that section gives, and only while the Phase total stays exactly nine years and the §1.3.2 Section-close bands stay reachable in the time. The spec records the choice and the window that results, from the previous Section's close as the ledgers and the previous Section Spec stand. It cites §1.3.2a and never copies the table. The Section, Novel-Part and Chapter windows nest, each inside the one above, and the Area's dates sit inside the Chapter window (Part 30 §1.3.2a, Cross-Reference Discipline). The window is written as dates plus Phase Day, the first day and the last day each as Year, Month, Day and Phase Day. The Phase Day numbers stay the stable key (Part 30), the calendar date is derived from them by Part 41 Area 4, Phase Day conversion and Section windows, and the spec cites Part 41 as it cites §1.3.2a and never copies its month table or its table of Section windows. Each window is a plan: it establishes nothing (Rule 1.3.2), and the recorded dates live in the calendar ledger (Rule 1.4.2).

*Carry-in.* The carry-in lists each thread coming in with its state at entry, refers to the previous Section Spec's Reader now knows line without copying it, and names unresolved questions and consequences that arrive with it. For the first Section of the story it reads `story start`. The built-against stamp in the header is written at every build and revision. It names the last completed Chapter and the last completed Section (or `story start`), the date and, by name only, the ledger entries the carry-in and the arcs lean on; it carries no ledger value (Rule 1.4.2). At the boundary the stamp is checked against reality (Rule 9.2.3).

**Rule 10.3.2 — Part 30 by citation only, Locked and Negotiable marked.**
Block 1 cites what Part 30 expects of the Section by function name, section number (§1.3.2, §1.3.2a), Law ID (P30-L8) or Setups-table row number, and never copies Part 30 text (Rule 2.3.2; Rule 1.4.2). Each item is marked **Locked** or **Negotiable** as Part 30 and Part 28 mark it (Part 28, the Part 30 row of its cross-reference table: the location anchors, thematic focus designations, protagonist arc mandates and Phase 1 Story Laws are Locked, and the events inside them are Negotiable; Part 28 Area 18: the Phase and Section names are Locked; Law P30-L8 is Locked Canon of Authority Tier 0); an item that neither Part marks Locked is Negotiable. Part 30's own markers on open points are used as they stand: **OPEN-AREA** (the first Area that needs it may establish it, Part 28 Area 17) and **OPEN-AUTHOR** (only the author sets it). A Locked item is read and never asked (Part 28 Rule 19.4, the no-asking rule), and a Section Spec cannot change one: a plan that conflicts with a Locked item is a finding at audit (Rule 10.5.1), never an amendment of Part 30. Locked events that fall in the Section, and boundary events that Part 30 places between two Sections, are assigned to a Novel-Part or recorded as spanning the boundary into the next Section's carry-in; the staging inside what Part 30 leaves OPEN-AREA is asked where it changes the Section plan (Rule 9.6.2).

**Rule 10.3.3 — The Novel-Part plan.**
Block 3 holds one entry per Novel-Part, in the order the story takes them. Each entry carries the fields of the template: a working label, the purpose by Part 30 function name, the thematic movement, the place or places, the calendar window inside the Section window, the Part 30 functions the Novel-Part carries, who carries it, the opening state, the closing state and hand-off, and a high-level Chapter list. The following govern the entries.
- *Every Major Narrative Function is placed.* Each Major Narrative Function that Part 30 lists for the Section is carried, whole or in part, by some Novel-Part entry, or the author has deferred it (Rule 10.5.1). The function name is the shared key between this spec, the Novel-Part Specs and the Chapter Specs (Rule 2.3.2); Part 30 Check 11-4 reads function names.
- *Who carries it.* All eight protagonists are accounted for in every entry (Part 30 P30-7): each is marked as carrying the Novel-Part, on the page, or off the page, and an off-page protagonist's line says where they stand. Nothing is counted, no minimum or target is set, and no order is implied. The POV counts of Rule 3.7.2 are computed at Section close from the written Areas and are never stored in any spec.
- *Working labels.* A name above Chapter grain is a working label. It carries no Establishment status (`proposed` or `locked-at-Gate-1`), because nothing in a Section Spec would ever flip it; establishment is recorded in the Chapter Spec and in the delivered files (Rule 9.3.1 and Part 28 Rule 18.4.4). Part 28 Rules 18.4.1 to 18.4.3 apply to the labels as advice only. A label settles nothing and establishes nothing (Rule 1.3.2).
- *The Chapter list is a guide.* Each entry lists its Chapters by working title with one line each. The Novel-Part Spec may add, split, merge or drop them, and every such change is noted upward as variance (Rule 9.4.5; Rule 11.4.3). The Section Spec's list stays as the plan baseline and is not rewritten to match; the live list of a Novel-Part is its Novel-Part Spec's (Rule 11.3.2). No range or count of Novel-Parts or Chapters is stored anywhere above the Chapter, and the length of a list is read as information only (Part 2 Rule 9.13; Part 2 Rule 9.3.1).
- *Status is not stored.* How far a Novel-Part has got (no spec, DRAFT, CONFIRMED, COMPLETED) is derived from its Novel-Part Spec and the registry whenever it is shown, and is never written into this spec.

**Rule 10.3.9 — Novel-Part pacing, word budget and the Section Scene Map (Amended 2026-10-07).**
Each Novel-Part entry of block 3 carries a Pacing line and a Word budget line, asked in the `/section-spec` build for each Novel-Part (Rules 2.3.3 and 2.3.9 give the guidance: fights usually Fast, intrigue, deception, lore and thought usually Slow, dialogue Medium, always the author's call). Both are guides: the Novel-Part Spec refines them Chapter by Chapter (Rule 11.3.7) and nothing in the Section Spec is a count that a lower spec must meet (Rule 10.3.3). A value not yet settled reads `unset`. Block 3 also carries a Scene Map across Novel-Parts, one row for each scene that runs across a Novel-Part seam, with the columns of the template and scene IDs prefixed `SS` (`SS1`, `SS2`, …) unique within the Section; an empty table says no scene runs across Novel-Parts. The Scene Map is a plan and establishes nothing (Rule 1.3.2). A row the Novel-Part Spec's own Scene Map carries down to Chapters keeps its `SS` ID there as a reference.

**Rule 10.3.4 — Threads, setups and payoffs: a linked guide.**
Block 4 is one of three linked guide registers (Section, Novel-Part, Chapter), joined by shared keys: the Part 30 Setups-table row number, or a short thread name (Rule 9.5.4). Here it records which Novel-Part plants an item, in which it returns and in which it pays. It is a guide and a suggestion, never a block: the story may plant elsewhere, pay earlier or later, or drop an item, and no check, gate or question is created by a suggestion that goes unmet. `/threads` shows the plan beside what happened, as information only. The register that Part 36 Areas 21 to 23 read stays the Planted here and Carried or paid off here fields of the Chapter Spec's Area blocks (Rule 2.4.10). How long a setup may wait is shown by these plan lines and by nothing else; no figure for it is stored here (Part 36 Rule 23.2.5). The optional column, thread-return stretch, is a per-thread note on how long the author wants a thread to stay off the page, and it reads `unset` unless the author gives one; where it is `unset` nothing is reported (Part 36 Rule 26.4.4). The Part 30 Setups-table rows that touch the Section are listed by row number and given a Novel-Part where the plan gives one; a row left unassigned is shown as information and is never a failure. Dropping or moving a suggested item is a light amendment with a variance note (Rule 10.6.2), never a substantial one.

**Rule 10.3.5 — Protagonist arc map and progression plan.**
*Arc map (block 5).* One row for each of the eight protagonists (Part 30 P30-7): the Part 30 arc line for this Section, cited by name; the planned movement across the Section; the Novel-Part or Novel-Parts that carry the main beats; the thread state at entry and at exit (story-thread state only, never ledger values, Rule 1.4.2). The question P30-7 asks of every Section, are all the protagonists advancing, is answered here by naming a movement for each of them, never by a quota.
*Progression plan (block 6).* The cultivation, technology and named-move beats of the Section, placed by Novel-Part against the Part 30 §1.3.2 map. The map is Locked at the Section close and its path is Negotiable, so the plan is a guide: it says which step lands in which Novel-Part and never states a ledger value. The Section-close band is cited, never copied, and no protagonist is planned above their band before the close (Part 30 Check 11-1(a)). The progression-axis beat of Part 30 P30-14 is judged at the Area window (Part 30 Check 11-6), so the plan here is a guide and creates no check of its own.

**Rule 10.3.6 — Opposition, reveals and consequence carry-over.**
*Opposition (block 7).* Which villain or faction pressure shows in which Novel-Part and how it presses, by name and by reference to Part 18 and the ledgers. Reveals about an opposing force carry the latest Novel-Part they may arrive in, under the Reader-Reveal Timing Law (`.claude/guardrails/audit/guardrail-fcia.md`). Where Part 30 itself plans a reader's early sight of a force (the Setups table says where), the plan cites the row.
*Knowledge, reveals and consequences (block 8).* What the reader learns and when, and where the reader knows more than a character or the reverse, at Section grain (Part 24 N24-1); each reveal owed and the Novel-Part it is expected in; and the consequences that travel: cascades from earlier Sections that land here and the shadows this Section casts into later ones (Part 30 P30-11; Part 27), by ledger entry name and never copied. A consequence the plan places in no Novel-Part is not an error (Rule 2.4.10, Consequences landing here).

**Rule 10.3.7 — The hand-off.**
Block 9 records where the Section leaves the story, the protagonists and the threads, and what the next Section inherits: no Section begins from a clean slate, and the residue, the unresolved tension and the planted seeds are carried (Part 2 Tier 2, section 1.2.3, Inter-Section Relationships). The next Section Spec's carry-in reads this block. **Section 8 only:** the block also holds the Phase Transition items. The event itself is Part 30 Setups-table row 10, which Part 30 leaves OPEN-AUTHOR and says is to be set when the Section Spec exists; it is asked in the Section 8 build (Rule 10.4.3), set down in block 4 under its row key, and its closing items (which of the Phase's ceilings and scales it permanently changes, as Part 30 requires, and the foreshadowing of what follows) are summarised here. This is the last thing a Phase 1 spec records. No Phase 2 spec chain is created, and it waits for Part 30 to be expanded for Phase 2 (Rule 9.1.4).

**Rule 10.3.8 — What the Section Spec never holds.**
The following are never stored in a Section Spec. Tone, voice, sensory and content fields, which belong to Part 36 Autonomous Matters and to the author's optional levers at Area grain (Rules 2.3.5a, 2.3.5b and 2.3.5d, and Rule 4.2.5). Pacing, which is decided in the Chapter Spec for each Area (Rule 2.3.3). Any count or range of Novel-Parts or Chapters. Any Establishment status, or any "locked" mark on a name above Chapter grain. Any Area block, scene anchor, continuation, size target, opening type or closing type: these are Chapter Spec matters. The Behavioral Plan (section 2.2a). POV counts, targets or minimums (Rule 3.7.2). The P30-L5 crisis-density row, which is a Chapter-grain row (Rule 2.3.7). A copy of Part 30 text or of a ledger value. An inline settlement tag of any kind (Rule 38.14).

### 10.4 — The Build

**Rule 10.4.1 — Build sequence.**
The `/section-spec build` flow runs in this order. It is led by the outline-planner, audited by the continuity-checker, and written by the command (Rule 9.9.1). The planner never writes the spec file.
1. **Precondition.** Part 30 must carry an entry for the requested Section. If it does not (Phase 2 and later, until Part 30 is expanded for them), the build is refused and says that Part 30 must be expanded first (Rule 9.1.4). A Section that already has a Section Spec is revised, never rebuilt blind (Rule 10.1.2). A Section that already has written Chapters is built as a retro-fit (Rule 9.8.2). The build runs at the boundary (`/start-story` and `/next-section`; `/next-phase` builds nothing until Part 30 has been expanded for the new Phase, Rule 9.1.4), or earlier on the author's request for a later Section, in which case it records its built-against stamp (Rules 9.2.1 to 9.2.3).
2. **Reading.** The planner reads the whole of Part 30 (Rule 10.4.2), Part 2 Tiers 2 and 3, this Part, the ledgers, the registry and the previous Section Spec with its completion block, if one exists. At command start this grounding runs together with the other reviews the command already launches (Rule 9.9.3).
3. **Read-back and consultation.** The command prints the read-back of what Part 30 expects of the Section (Rule 10.4.2) and the consultation begins. The planner takes Section-grain topics in the order the story needs and asks every one that is a genuine branch: the Section's calendar window (the anchor or a chosen value inside the latitude); the Part 30 OPEN-AUTHOR rows due (Rule 10.4.3); the shape of the Section and the order of its turns; the Novel-Parts, their order, their working labels and their thematic movement; which Novel-Part carries each Part 30 function; who carries each Novel-Part, and where each of the eight protagonists' arc lines land; where each thread is planted, returns and pays; the progression beats by Novel-Part; opposition, reveal timing and consequence carry-over; the Section close hand-off; and the epigraph (asked in every Section, the first Section of a Phase included, so that every Section Spec holds its own Epigraph line, Rule 10.3.1; in the first Section of a Phase the build also asks the one question about the Part 30 `Epigraph:` line). A matter whose answer first changes a lower level's plan is not asked here (Rule 9.6.2). The planner asks no count or range of Novel-Parts or Chapters, and no question that Part 30 already settles.
4. **Question shape (Rule 9.6.4).** Two or three concrete options and `SKIP — let AI decide`, four in all; a short thematic preview on every direction option and a flag on any option that risks exposition (Rule 3.2.3); up to four questions in each `AskUserQuestion` call; as many rounds as the story needs. An answer is recorded as a Settled note. A SKIP is recorded as a Skipped note and settles nothing. A MAJOR entity's name, aim or leader, a Hero or Villain address-register gap and lore the author owns are never settled by a SKIP (Part 28 Area 20.4); they stay asked until the author answers or defers them. Only the author may defer an item, and a deferral is recorded as a Deferred note (Rule 9.5.2). The planner never leaves an item open on its own (Rule 9.6.3). A MAJOR entity's name that the author settles here stays a working label until an Area establishes it, and the consultation is carried into the Debuts field of the Chapter Spec that first introduces it (Rule 2.3.4; Part 28 Area 20.4). There is no quick build (Rule 3.2.5).
5. **Light audit.** The continuity-checker runs the audit of Rule 10.5.1. Findings are reported with the confirmation prompt, and blocking findings are resolved before `[CONFIRM SPEC]` is accepted.
6. **Final sweep.** The outline-planner and the continuity-checker sweep the whole spec for what is still unasked, for conflicts with Part 30, the ledgers and the previous Section Spec, and re-list every SKIP and every deferral so that the author has a last chance on each. If the sweep returns anything new, more rounds follow and then a new sweep. When it returns nothing, the author is asked whether there is anything further to steer, and only after an explicit "nothing further" is the confirmation prompt shown (Rule 9.6.5).
7. **Confirm.** The prompt names the artifact ("Section Spec 1.2") and offers `[CONFIRM SPEC]`, `[REVISE SPEC]` and `[SKIP SPEC]` (Rule 3.4.1). Only one confirm prompt is open at a time in a chain. `[SKIP SPEC]` saves the spec as DRAFT, stops the chain there, and leaves every Novel-Part Spec build refused until the Section Spec is CONFIRMED (Rule 9.1.1). At `[CONFIRM SPEC]` the file and its registry row are written and the settled items gain their settling power downward (Rule 9.5.1): they are carried into the Chapter Specs as Inherited notes naming the Section Spec and are not re-asked in a lower build, apart from the carve-outs and a clarity reduction (Rules 9.5.3 and 4.2.4).

**Rule 10.4.2 — The Part 30 read and the chat read-back.**
Every Section Spec build reads the whole of `skills/narration-novel-macro-story-law/SKILL.md`, in full, every time. An earlier read, a summary or a remembered reading does not stand in for it. After the read, the command prints in chat a read-back of "what Part 30 expects of this Section": the location anchor, the duration and its latitude, the thematic focus, the arc, each Major Narrative Function by name, the Section-close cultivation band, the Locked events, the OPEN-AUTHOR and OPEN-AREA rows due, and the Setups-table rows that touch the Section, each marked Locked or Negotiable. The read-back is information in plain words. It is shown to the author and never stored; the file keeps citations only (Rule 10.3.2). It asks nothing and settles nothing.

**Rule 10.4.3 — OPEN-AUTHOR rows are surfaced.**
The build surfaces every Part 30 OPEN-AUTHOR row that is due in, or planted by, the Section. The planner reads the rows from the Setups table of Part 30 at each build and never from this Rule, so a later edit to Part 30 is always picked up. Each such row is put to the author as a question. The author may settle it, may let the planner choose (a SKIP, recorded as such), or may answer "let the first Area decide", which is a deferral to Area writing and is recorded as a Deferred note. A deferral to Area writing is copied into the Chapter Spec of the Chapter it bears on, so the Area-time gate asks the author (Rule 9.5.2). A row that concerns a major entity is put with a name consultation (Part 28 Area 20.4). An OPEN-AREA row due in the Section is asked only where its answer first changes the Section plan (for example, an order of events that sets the order of Novel-Parts); otherwise it keeps Part 30's own marker and is shown in block 1. The Phase Transition event of Section 8 (Setups-table row 10) is asked in the Section 8 build and recorded in block 4 under its row key (Rule 10.3.7).

### 10.5 — Light Continuity Audit

**Rule 10.5.1 — Scope of the Section Spec's light audit.**
The continuity-checker audits the plan, not the written Areas, and is report-only: it writes nothing (Rule 9.9.1). It reads the Section Spec, Part 30, the ledgers and the previous Section Spec. In `/next-section` it reads the ledgers after the Section-close ledger writes of that command have landed, so that the carry-in item sees the state of the Section just closed (Rule 9.9.3). Findings are reported with the confirmation prompt (Rule 3.3.2). The checks are:
- (a) **Locked Canon scan.** The §1.3.2 Section-close band, the §1.3.2a window and its latitude (the Phase total stays exactly nine years), Laws P30-L8 and P30-L9, and the author-removed concepts. A conflict **blocks**.
- (b) **Standing exclusions** clean, by reference to Chapter Spec template section 3. A hit **blocks**.
- (c) **Every Major Narrative Function** that Part 30 lists for the Section is carried by some Novel-Part entry, or has been deferred by the author. A function neither carried nor deferred **blocks** until the author rules; the floors of Part 30 are information and force no content.
- (d) **Part 30 setups rows and open rows.** Setups-table rows that touch the Section are shown assigned or unassigned (information only; an unmet suggestion creates no check, Rule 9.5.4). The OPEN-AUTHOR rows due have been surfaced (Rule 10.4.3); one neither answered, skipped nor deferred **blocks**.
- (e) **Ensemble.** All eight protagonists are accounted for in every Novel-Part entry and in the arc map (P30-7), stated without counts. A protagonist with no line **blocks**.
- (f) **Reader-Reveal Timing** of the reveals in blocks 7 and 8. A reveal planned later than its latest allowed Novel-Part **blocks**.
- (g) **Carry-in** against the previous Section's record and the ledgers: threads in match where the previous Section left them. A contradiction **blocks**. For an ahead-built Section Spec the built-against stamp is checked against the ledger state as it now stands (Rule 9.2.3).
- (h) **Calendar nesting.** Each Novel-Part window lies inside the Section window (Part 30 Check 11-2). A window that falls outside **blocks**.
- (i) **Novel-Part working labels**, as advice only (Part 28 Rules 18.4.1 to 18.4.3): register, uniqueness inside the Section, coherence with the Section name.
- (j) **Schema conformance.** Every required field holds a value or an author deferral recorded in the notes (Rule 10.2.1; Rule 2.4.2, applied to this template). A blank required field **blocks**.
- (k) **Clean body.** The body holds no inline settlement tag and the Audit and Settlement Notes section stands as the last block of the file, each note pointing to a plan item that exists (Rule 38.14). A tag in the body or a missing section **blocks**.

The blocking set, in one list: a Locked Canon conflict (a); a standing-exclusion hit (b); a Part 30 function neither carried nor deferred (c); an OPEN-AUTHOR row neither answered, skipped nor deferred (d); a protagonist with no line (e); a reveal planned later than its latest allowed Novel-Part (f); a carry-in contradiction (g); a Novel-Part window outside the Section window (h); a blank required field (j); and a body that is not clean (k). Information only, and never blocking: the assignment of Part 30 setups rows to Novel-Parts (d) and the Novel-Part label advice (i). A finding that blocks is cleared by changing the plan or by the author's ruling, and never by the planner's inference.

### 10.6 — Completion and the Living Record

**Rule 10.6.1 — Completion.**
A Section Spec is completed at the boundary, on the author's yes (Rule 9.7.3): `/next-section` asks "Has this Section finished?" as part of its checks. On yes, every Novel-Part Spec of the Section is COMPLETED (or RETIRED with a variance note, or never written and recorded as dropped on the author's yes), the last one in the same bottom-up write step (Rule 9.4.4), and the Section Spec is set to COMPLETED with its completion content, in the one step that confirms the new chain. On no, the command stops. The completion content is the Completion Record block of the template (block 11): a Final Variance Summary (planned against as-written, including Novel-Parts and Chapters added, split, merged or dropped); the Reader now knows line, by reference to the last Novel-Part Spec's line plus the Section-level additions, with no list copied; the Section digest, by reference to the Novel-Part digests; and the threads and setups carried to the next Section. The author is asked about every setup still unpaid and every cliffhanger still unresolved, and an item is marked lapsed only on the author's answer. The registry row's Coverage is refreshed at the same event (Rule 1.2.2). The reports at the end of a Section (reveals that were not met, threads, Part 30 functions, and the POV report of Rule 3.7.2) are informational and never block (Rule 9.7.4); the POV counts are computed when reported and are not stored. The last Section of a Phase has no `/next-section` after it, so `/next-phase` completes it, asking the completions once each in the order Chapter, Novel-Part, Section (Rule 9.7.3); the author may instead run `/part-spec complete` and then `/section-spec complete`. `/next-phase` does not create a Phase Spec (Rule 9.1.4).

**Rule 10.6.2 — A living record.**
A COMPLETED Section Spec is not closed: it is a living record that stays revisable at any time through `/section-spec revise`, with a variance note. There is no refusal that confines a revision to a redraft. A revision refreshes the completion content, and one that changes plan content for Areas already written is the author's call whether to redraft; written Areas are never touched by a spec amendment (Rule 9.4.2). Where the Section has Novel-Part Specs or Chapter Specs, a revision first runs the cascade report, and the author decides for each affected child whether to keep it with a variance note, amend it, or mark it AMENDED-PENDING-RECONFIRM; nothing flips by itself (Rule 9.4.2). A **substantial** amendment of a Section Spec is any of these: a change of a Novel-Part's or the Section's purpose; a change of the Section's closing state and hand-off; a change of a calendar window; a change of the reveals owed; adding, removing or reordering a Novel-Part entry (a split or a merge counts as an adding and a removing). It sets AMENDED-PENDING-RECONFIRM and needs the light audit and a fresh `[CONFIRM SPEC]` (Rule 3.5.2). A **light** amendment is the adding, splitting, merging or dropping of Chapters in an entry (the guide list), moving or dropping a suggested thread, setup or payoff, setting or clearing the Section's own Epigraph or a thread-return note, a typo-grade fix, and any variance note appended by this flow or by a lower one, whether it records a Novel-Part Spec's departure or Chapter-list change or a Chapter Spec's departure, which is noted on the Section Spec as well as on its Novel-Part Spec (Rule 9.4.5: the Section Spec's notes take the variance notes of every spec below it); it takes effect at once with a log line. While a Section Spec is AMENDED-PENDING-RECONFIRM the chain is not in force below it (Rules 9.1.1 and 6.1.3). A Section Spec is retired only explicitly by the author, and not while any of its Novel-Part Specs is non-RETIRED, until the author has ruled on each of them (Rule 9.8.3). If a rewind or a reset removes written Areas so that a child returns to non-COMPLETED, a COMPLETED Section Spec returns to CONFIRMED and keeps its completion text as history (Rule 9.8.1).

### 10.7 — Illustration: A Filled Novel-Part Entry

**Illustration, establishes nothing (Rule 1.3.2).** The entry below is block 3 of an invented Section Spec, filled with placeholder names (Hero A to Hero H, Place A to Place C, Function A to Function C). Nothing in it is canon, and no name in it may be used in a spec or in an Area. A real entry names the Part 30 functions and cites no Part 30 text. The entry shows how the fields are filled. The answers behind it are lines of block 12, the Audit and Settlement Notes; they are not tags in the entry.

```markdown
### Novel-Part 2 — The Road Out
**Purpose (Part 30 functions by name):** carries Function A in full and opens Function C; the Section turns here from staying to leaving.
**Thematic movement:** from a house that holds Hero A and Hero B in place to a first honest wish to leave it; the Novel-Part ends with the wish said aloud.
**Place or places:** Place A (the home town, no ledger entry yet); the road; Place B (the first stop)
**Calendar window (inside the Section window):** from the third month to the sixth month of the Section window, written as `<first date> (Phase Day <P>)` to `<last date> (Phase Day <Q>)`; Hero A and Hero B a few months older at the close.
**Part 30 functions this Novel-Part carries:** Function A; Function C (opening only)
**Carried by (the eight protagonists):** Hero A and Hero B carry the viewpoint and the main thread. Hero C and Hero D are on the page in support throughout. Hero E is off the page, at Place C, waiting for a letter. Hero F is off the page, travelling, and comes back in the last third. Hero G and Hero H are on the page in the last third only.
**Opening state:** the town is quiet, the letter is unopened, and Hero A has said nothing to Hero B about it.
**Closing state and hand-off:** Hero A and Hero B stand at Place B with the wish said aloud and no plan; the letter is open, and the reader knows who sent it while Hero B does not. The next Novel-Part inherits the road behind and the sender ahead.
**Chapters (high level — a guide the Novel-Part Spec may add to, split, merge or drop):**
1. The Quiet Town — Hero A and Hero B in an ordinary day; the letter arrives.
2. What the Letter Asked — the house reads it; the first real disagreement.
3. The First Day on the Road — the leaving, shown without announcement.
4. Place B at Dusk — the arrival and the wish said aloud. How much of the sender's name is shown is left to the Chapter Spec.
```

and the matching lines of block 12:

```markdown
## 12 — Audit and Settlement Notes

- **Novel-Part 2, Purpose** — Settled: carry Function A here.
- **Novel-Part 2, Thematic movement** — Settled: the wish said aloud.
- **Novel-Part 2, Calendar window** — Settled: third to sixth month of the Section window.
- **Novel-Part 2, Carried by** — Settled.
- **Novel-Part 2, Chapter 3** — Skipped: planner chose "one Chapter for the whole leaving".
- **Novel-Part 2, Chapter 4, how much of the sender's name is shown** — Deferred by the author to the Chapter Spec.
```

---

## Area 11 — The Novel-Part Spec

*Elaborates Rule 38.11 (Novel-Part Spec). It works with Area 9 (the spec chain; rules written "Rule 9.x.y") and Area 10 (the Section Spec; rules written "Rule 10.x.y"). The vocabulary is fixed: the artifact is the **Novel-Part Spec**, its ref is `P.S.P`, and the command that builds it is `/part-spec` (C-41).*

### 11.1 — Purpose and File Law

**Rule 11.1.1 — Purpose: the plan of one whole Novel-Part, every Chapter in depth.**
The Novel-Part Spec is the confirmed, author-approved plan for one Novel-Part. It is the middle link of the spec chain (Section Spec, Novel-Part Spec, Chapter Spec; Rule 9.1.1). It takes the Section Spec's entry for the Novel-Part and lists **every Chapter of the Novel-Part in depth**, so that the author decides the story line of the Novel-Part, and how deep each Chapter goes, before any Chapter Spec is built. It exists for the reason the Chapter Spec exists (Rule 1.1.1): a charted course makes every later question meaningful, and the Chapter builds below it read one shared plan and do not work the Novel-Part's story out again. It is the one stored place where the plan of the whole Novel-Part is kept, read by every Chapter build in it. It is a plan and never a record: it establishes no canon fact (Rule 1.3.2), restates no ledger content (Rule 1.4.2), and binds planning conduct only (Rule 1.1.2). It holds no tone, voice, sensory or content tag, no pacing, no Area anchors, no size target (those are Area and Chapter Spec matters, Rule 9.5.3) and no count or range of Chapters (Rule 11.3.2). A Novel-Part Spec cannot be built or revised unless the Section Spec of its Section is CONFIRMED or COMPLETED, and a Chapter Spec cannot be built or revised unless its Novel-Part Spec is CONFIRMED or COMPLETED (Rule 9.1.1).

**Rule 11.1.2 — File path, ref and registry row.**
Each Novel-Part has exactly one Novel-Part Spec, in the same folder as the Chapter Specs of that Novel-Part: `.claude/story-memory/phase-section-part-chapter-area-specs/phase-N/section-N/part-N/part-N-spec.md` (folder naming per Rule 1.2.1). Its ref is `P.S.P` (for example `1.2.3`: Phase 1, Section 2, Novel-Part 3); the Chapter Specs beside it keep their refs `P.S.P.CCC` (Rule 2.3.1). Its registry row sits in the Novel-Part Specs table of `_index.md` (columns Spec File, Ref, Status, Spec Ver, Last Updated, Coverage). Coverage reads "Chapters completed / planned", where "planned" is the number of Chapter entries now listed, as information only (Rule 11.3.2). The row is written at the spec's own `[CONFIRM SPEC]`, at completion and at a status change made by a reconciliation pass (Rule 9.4.3). **The Coverage cell is refreshed at this spec's own confirm, at any completion write step (the completion of a Chapter Spec under it included) and at a reset or rewind rollback, and never at Gate 2** (Rule 1.2.2; the Gate 2 write set is unchanged, Rule 6.2.1). The file and its row are written with ordinary Write and Edit by the orchestrating command; no script is created for them (Rule 9.4.3).

### 11.2 — The Template

**Rule 11.2.1 — Canonical Novel-Part Spec template.**
Every `part-N-spec.md` follows this template, whether it is a forward build or a retro-fit (Rule 9.8.2; a retro-fit simply begins with statuses read from the record). A required field is never blank: it holds the author's answer, the planner's choice after a SKIP, or an author deferral to a Chapter Spec or to Area writing, each recorded in the notes (Rule 9.5.2). While a build is running an unanswered field is recorded as an Open note; none is left in that form at `[CONFIRM SPEC]` (Rule 9.6.3).

```markdown
# Novel-Part Spec — [Novel-Part N: Working Label] (Ref prefix: P.S.P — e.g. 1.2.3)

**Governing Law:** Part 38 — Story Specification Law (spec-story-specification-law)
**Spec Status:** [DRAFT / CONFIRMED / AMENDED-PENDING-RECONFIRM / COMPLETED / RETIRED]
**Spec Version:** v1.0 | **Confirmed:** [YYYY-MM-DD via [CONFIRM SPEC] / — ]
**Last Updated:** [YYYY-MM-DD]
**Light Continuity Audit:** [PASS YYYY-MM-DD / pending]
**Built-against stamp:** [the last completed Chapter reference (or `story start`) and the ledger state this spec was built against, YYYY-MM-DD]

---

## 0 — Header Block

**Name chain (working labels; no Establishment status above Chapter grain):**
- Phase [N] — [Phase Name] (locked, Part 30 Locked Canon)
- Section [N] — [Section Name] (locked, Part 30 Locked Canon)
- Novel-Part [N] — [working label]

**Section Spec:** [P.S — section-N-spec.md; its status when this spec was built]
**Purpose (Part 30 functions this Novel-Part carries, by function name only, Rule 2.3.2):** [2–4 sentences]
**Novel-Part calendar window (inside the Section window, Part 30 §1.3.2a; cited, never copied; dates plus Phase Day, Part 41 Area 4):** [in-story dates plus Phase Day, the first day and the last day each as Year, Month, Day and Phase Day; protagonist ages if age-sensitive]
**Carry-in from the previous Novel-Part:** [threads in, each with its state at entry; the previous Novel-Part Spec's Reader now knows line by reference, never copied | for the first Novel-Part of a Section, the last Novel-Part of the previous Section | `story start`]

## 1 — Thematic Movement

[where the Novel-Part moves from and to, in plain words; refined from the Section Spec's thematic movement for this Novel-Part]

## 2 — Chapter Entries (every Chapter of the Novel-Part, in depth)

### Chapter [NNN] — [working label]
**Purpose (Part 30 functions by name, Rule 2.3.2):** [what this Chapter does for the Novel-Part]
**Calendar window (inside the Novel-Part window):** [in-story dates plus Phase Day, the first day and the last day each as Year, Month, Day and Phase Day (Part 41 Area 4)]
**Threads in:** [thread — state at entry]
**Threads out:** [thread — intended state at exit]
**On the page:** viewpoint: [who holds the viewpoint] | on the page: [who else takes part] | off the page: [each protagonist away from this Chapter — where they stand: the place and the thread, in a short phrase]  *(all eight protagonists, each in exactly one part)*
**Key events:** [what must happen in this Chapter]
**Reveals and payoffs owed:** [each reveal or payoff this Chapter owes the reader | none]
**Opening hook:** [what draws the reader in at the Chapter's first Area]
**Closing beat:** [what the Chapter ends on and hands to the next]
**Chapter pacing:** [Fast | Medium | Slow | unset; the author's call with the guidance of Rule 2.3.3] *(Amended 2026-10-07; Rule 11.3.7)*
**Chapter word budget:** [N words, a guide the Chapter Spec settles as its Chapter size target, or `unset`; the author may raise it] *(Amended 2026-10-07; Rule 11.3.7)*
**Area outline (one line, scenes in order, descriptors only — no anchors, types, Area size targets, Area pacing or Area names):** [scene; scene; scene]
**Linked setup keys:** [Part 30 Setups-table row number or short thread name — planted / carried / paid here (a guide, Rule 9.5.4) | none]
**Status:** derived from the Chapter Spec's registry row; never stored here

*(one entry for each Chapter, in the order planned)*

### Scene Map (across Chapters) *(Amended 2026-10-07; Rule 11.3.7)*

| Scene ID | Chapters covered | POV sequence | Scene arc | Scene pacing | Scene word budget | Join state at each Chapter seam |
|---|---|---|---|---|---|---|
| [PS1] | [e.g. 004-005] | [each POV in order, with the Chapter where each takes over] | [the movement of the scene] | [Fast / Medium / Slow] | [N words] | [the exact state at each Chapter seam] |

*(an empty table means no scene runs across Chapters)*

## 3 — Threads, Setups and Payoffs (guide; Rule 9.5.4)

| Key (Part 30 Setups row or short thread name) | Planted in (Chapter) | Pays in (Chapter) | Note |
|---|---|---|---|

*Suggestions only. The story may plant elsewhere, pay earlier or later, or drop one; nothing here blocks or is checked.*

## 4 — Protagonist Arc Line

[one line for each of the eight protagonists (Part 30 P30-7): where they stand at the start of the Novel-Part and where the plan leaves them; no counts, no ranking]

## 5 — Progression Beats (guide)

[cultivation, technology and named-move beats set against the Part 30 §1.3.2 map, cited and never copied; the Section-close band is Locked and nobody is shown above their band earlier]

## 6 — Opposition, Pressure and Reveal Timing

[villain and faction pressure the Novel-Part carries; when each reveal reaches the reader (Reader-Reveal Timing); by function name]

## 7 — Cut and Cliffhanger Plan Across Chapters

| Chapter | How it ends | How the next Chapter opens | Cliffhanger or cut away: resolved or returned to in (Chapter) |
|---|---|---|---|

## 8 — Novel-Part Closing State and Hand-Off

[where the Novel-Part leaves the story, the protagonists and the threads; what it hands to the next Novel-Part; for the last Novel-Part of a Section, it agrees with the Section Spec's Section close hand-off]

## 9 — Standing Exclusions

By reference: Chapter Spec template section 3 (Rule 2.2.1). Verified at build, in every audit and at every amendment; the list is not pasted here.

## 10 — Completion Record

[Written at completion (Rule 11.7.1); reads "not yet written" until then.]
**Final variance summary:** [planned versus as-written in brief, including Chapters added, split, merged or dropped]
**Reader now knows:** [by reference to the last Chapter's line plus Novel-Part-level additions; no copy of lists]
**Novel-Part digest:** [what changed, who and the open threads, by reference to the Chapter digests]
**Carried to the next Novel-Part:** [threads and setups carried on; each unpaid one asked about; lapsed only on the author's answer]

## 11 — Audit and Settlement Notes

[The last section of the file. Every settled, skipped, open, deferred, from, inherited, variance and audit note, each pointing to the plan item it concerns by block, Chapter entry or field (Rule 38.14; section 9.10). Variance lines are kept here, each with the date, the trigger (command or Chapter ref), the variance noted and the author's ruling where one was asked (entry amended / original kept as plan baseline).]
```

### 11.3 — Field Law

**Rule 11.3.1 — Header block (block 0) and names.**
The header lines are the Section Spec's (Rule 10.2.1): Governing Law, Spec Status, Spec Version and Confirmed, Last Updated, Light Continuity Audit and Built-against stamp. There is no Last Sync line, because no Gate 2 writes a Novel-Part Spec (Rule 9.4.3). Block 0 holds the name chain, the Section Spec reference, the purpose, the calendar window and the carry-in. Phase and Section names are Locked Canon (Part 30) and read as locked (Rule 2.3.1). **Above Chapter grain every name is a working label:** the Novel-Part's name and every Chapter name in this spec carry no Establishment status, neither `proposed` nor `locked-at-Gate-1`; establishment is recorded in the Chapter Spec and in the delivered files (Rule 2.3.1), and the light audit applies Part 28 Rules 18.4.1–18.4.3 to the labels as advice only (Rule 11.6.1). The purpose cites Part 30 by function name and never copies its text (Rule 2.3.2). The calendar window sits inside the Section window (Part 30 §1.3.2a: the anchor, or a value inside its latitude, as the Section Spec set it) and cites §1.3.2a without copying it; every Chapter window of block 2 sits inside it. This window and every Chapter window are written as dates plus Phase Day, citing Part 41 Area 4 as well as §1.3.2a and never copying either table, as Rule 10.3.1 says of the Section window. The carry-in names the threads that come in with their state and points at the previous Novel-Part Spec's Reader now knows line by reference instead of copying it; for the first Novel-Part of a Section the previous Novel-Part is the last one of the previous Section, and for the first of the story the carry-in reads `story start`. Blocks 0 and 8 are the two blocks of this spec that per-Area agents read (Rule 9.9.2), so each is written to be understood without the rest of the file.

**Rule 11.3.2 — Chapter entries (block 2): every Chapter, in depth.**
Block 2 holds one entry for every Chapter of the Novel-Part, each in depth; no Chapter is left as a title alone. Every entry has these fields: working label; purpose (Part 30 functions by name); calendar window (inside the Novel-Part window); threads in and threads out; who is on the page (Rule 11.3.3); key events; reveals and payoffs owed; opening hook; closing beat; Chapter pacing and Chapter word budget (Rule 11.3.7, Amended 2026-10-07); a one-line Area outline (Rule 11.3.4); linked setup keys (Rule 9.5.4); and a derived status (Rule 11.3.5). Every field is asked in the build (Rule 9.6.3). The entries are listed in the order planned; Chapter numbers are zero-padded and restart in each Novel-Part (Part 2 Rules 5.2.2–5.2.5). The entries start from the Section Spec's high-level Chapter list for this Novel-Part, each recorded in the notes as a From note naming the Section Spec entry until the author's own answer replaces the text with a Settled note (Rule 9.3.1). **The list is the plan and a guide:** it states no range, no minimum and no maximum; the number of entries is information only (Part 2 Rule 9.3.1); and the Novel-Part ends where the story ends it (Rule 1.5.1). A Chapter may be added, split, merged or dropped when the story asks (Rules 11.4.3 and 11.5.2). An entry is never rewritten to match the Areas that follow: the Chapter Spec holds the as-built record, and a difference is a variance note in block 11, which is also noted on the Section Spec (Rules 11.4.2 and 9.4.5).

**Rule 11.3.3 — Who is on the page: one compact line, all eight protagonists.**
The "On the page" field is one compact line of three parts. **Viewpoint:** who holds the viewpoint in the Chapter, with any planned change of holder named in a few words. **On the page:** everyone else who takes part, the protagonists first, then any other character the plan needs, named by name or ledger reference and never described from the ledger (Rule 1.4.2). **Off the page:** each protagonist who is away from the Chapter, with where that protagonist stands: the place and the thread, in a short phrase. All eight protagonists are accounted in every entry: each appears in exactly one of the three parts (Part 30 P30-7), and a protagonist missing from the line is a finding of the light audit (Rule 11.6.1). The line states no count, no minimum and no order. The viewpoint figures reported at Section close are still worked out from the written Areas and are never stored (Rule 3.7.2). The line is the source of the Chapter Spec's Protagonist Thread Map (Rule 11.4.1).

**Rule 11.3.4 — The one-line Area outline and its limits.**
Each entry carries a one-line outline of the Chapter's scenes: the scenes in order, each a short plain descriptor of what happens, separated by semicolons (for example "the argument at the ford and the wait; the crossing and the walk on"). The outline holds **descriptors only**: no anchors, no continuation, no opening type or closing type, no Area pacing, no Area size target, no Area name, no Area reference code and no tag. (*Amended 2026-10-07:* the Chapter-level pacing and word budget of Rule 11.3.7 are separate fields of the entry and are not part of the outline.) Those stay in the Chapter Spec, which plans them in the Chapter build (Rules 2.4.1–2.4.10 for the Area block; Rule 9.5.3 for the carve-outs). The outline is the Chapter build's starting list of scenes and nothing more. The Chapter Spec may split, merge, re-cut, reorder, rename or drop Areas freely; that is its own business and is **not** a departure from the entry (Rule 11.4.2). The number of scenes in the line is not a count of Areas the Chapter must have.

**Rule 11.3.5 — Derived status.**
An entry's status is DERIVED from the Chapter Spec's registry row and is never stored. The file carries the fixed note shown in the template, and the value is read whenever the spec is shown (`/part-spec show`, `/status`): no Chapter Spec yet, or that Chapter Spec's status (in practice DRAFT, CONFIRMED or COMPLETED; AMENDED-PENDING-RECONFIRM or RETIRED where they apply). A stored copy would be a second source that goes stale the moment a Chapter Spec changes state (the reasoning of Rule 1.4.2). The Novel-Part Spec's own status is written only by the `/part-spec` flow (confirm, amendment, retirement), by the boundary commands at completion, and by the reconciliation pass after a reset or rewind (Rule 9.4.3); never at Gate 2.

**Rule 11.3.6 — Blocks 3 to 8.**
Blocks 3 to 8 are the plan of the Novel-Part as a whole, written at Novel-Part grain.
- **Block 3, threads, setups and payoffs.** One of the three linked guide registers (Rule 9.5.4). Each line is keyed by a Part 30 Setups-table row number or a short thread name, the same key the Section Spec and the Chapter entries use, and says which Chapter plants it and which Chapter pays it. It is a guide and a suggestion, never a block: the story may plant elsewhere, pay earlier or later, or drop a setup, and a line left unmet raises no check, no gate and no question (`/threads` shows plan and story side by side as information only). The Chapter Spec's Area fields Planted here and Carried or paid off here are where a setup actually lands and are the register Part 36 reads (Rule 2.4.10). How long a thread may stay off the page is the Section Spec's plan lines and its per-thread note (Rule 10.3.4); the Chapter Spec's Threads Carried In still holds a planned re-entry beat (Part 36 Rule 26.4.4).
- **Block 4, protagonist arc line.** One line for each of the eight protagonists through the Novel-Part (Part 30 P30-7): where each stands at the start and where the plan leaves them. No count and no ranking.
- **Block 5, progression beats.** The cultivation, technology and named-move beats of the Novel-Part set against the Part 30 §1.3.2 map, cited and never copied. A guide: the Section-close band is Locked, and nobody is shown above their band before the Section's close.
- **Block 6, opposition, pressure and reveal timing.** The villain and faction pressure the Novel-Part carries and when each reveal reaches the reader (Reader-Reveal Timing), by function name. Each reveal also appears in the "Reveals and payoffs owed" field of the entry of the Chapter that delivers it.
- **Block 7, cut and cliffhanger plan across Chapters.** How each Chapter ends and how the next one opens, in plain words, so that consecutive Chapters do not end and open alike; and, for each cliffhanger or cut away, the Chapter that resolves it or returns to it. The words of the Opening and Closing types (Rule 2.4.3) may be used as descriptors here; the actual types are set Area by Area in the Chapter Spec.
- **Block 8, Novel-Part closing state and hand-off.** Where the Novel-Part leaves the story, the protagonists and the threads, and what it hands to the next Novel-Part. For the last Novel-Part of a Section it must agree with the Section Spec's Section close hand-off (Rule 10.3.7); a difference is a question to the author and never a silent choice (Rule 9.4.1).

**Rule 11.3.7 — Chapter pacing, Chapter word budget and the Scene Map across Chapters (Amended 2026-10-07).**
Each Chapter entry of block 2 carries a Chapter pacing line and a Chapter word budget line, both asked in the `/part-spec` build for every Chapter, with the guidance of Rule 2.3.3, and the author may raise any budget at the question. Both are guides at this level: the Chapter Spec settles the Chapter's pacing and its Chapter size target in its header (Rule 2.3.9), and a different value there is the Chapter Spec's own business, noted upward as variance (Rule 9.4.5), not a departure that blocks. A value not yet settled reads `unset`. Block 2 also carries a Scene Map across Chapters, one row for each scene that runs across a Chapter seam, with the columns of the template and scene IDs prefixed `PS` (`PS1`, `PS2`, …) unique within the Novel-Part; an empty table says no scene runs across Chapters. A scene of the Chapter Spec's own Scene Map that runs in from or out to another Chapter names its `PS` row in its `Runs in from / out to` column. The Scene Map is a plan and establishes nothing (Rule 1.3.2).

Block 9 (standing exclusions) is stated by reference to template section 3 of the Chapter Spec and verified in every audit (Rule 2.3.7); the list is not pasted. Block 10 is the Completion Record (Rule 11.7.1), and block 11 the Audit and Settlement Notes (Rules 9.10.2, 11.4.2 and 11.4.3).

### 11.4 — Pre-Fill, Departures and Variance

**Rule 11.4.1 — What the entry pre-fills in the Chapter Spec.**
*(Elaborates Rules 9.3.1 and 9.3.4: spec-to-spec derivation is allowed and noted; copying ledger content stays barred, Rule 1.4.2.)* When the Chapter Spec is built, its entry in this spec pre-fills these header fields of the Chapter Spec (Rule 2.2.1, section 1):

| Chapter Spec header field | Filled from the entry's |
|---|---|
| Chapter name | working label (it becomes the Chapter's `proposed` name, the first place an Establishment status is recorded) |
| Chapter Purpose | Purpose |
| Calendar Window | Calendar window |
| Threads Carried In / Threads Carried Out | Threads in / Threads out |
| Protagonist Thread Map | the On the page line: the presence of each of the eight protagonists, and for an off-page protagonist the "where they stand" phrase as its thread state at entry; exit states are set in the Chapter build |
| Opening hook | Opening hook |
| Closing beat | Closing beat |

An entry field that this spec records as a Settled note arrives in the Chapter Spec as an Inherited note naming the Novel-Part Spec, and is not re-asked in the Chapter build (Rule 9.5.1); any other entry text arrives with a From note naming the entry, which records where the value came from and settles nothing (Rule 4.1.2). The same holds for items the Section Spec settled, which arrive as Inherited notes naming the Section Spec. An author deferral to Area writing is carried in as a Deferred note on the Chapter it bears on, so that the Area-time gate asks it (Rule 9.5.2). An inherited item never loses its note by being copied (Rule 9.3.1). The entry's key events, reveals and payoffs owed, one-line Area outline and linked setup keys have no header field: the Chapter build reads them as grounding for the Area blocks (the outline as the starting list of scenes; the keys as the setups the Area fields Planted here and Carried or paid off here are expected to pick up). The Epigraph is not carried: a Section's own epigraph lives in the Section Spec, and the Phase epigraph in Part 30 (Rule 10.3.1). A value the author changes in the Chapter build is the author's own answer there, recorded as a Settled note, and where it differs from what the entry fixes it is a departure (Rule 11.4.2).

**Rule 11.4.2 — The Chapter header governs after confirm; departures and variance.**
After the Chapter Spec's `[CONFIRM SPEC]` the **Chapter header governs the Areas and Gate 1**; the entry in this spec stays the plan baseline (Rule 9.3.2). **A departure flows back only for what the entry fixes** (Rule 9.3.3): purpose, calendar window, threads in and threads out, who is on the page, key events, reveals and payoffs owed, opening hook and closing beat. Nothing else is a departure. In particular these are the Chapter Spec's own business and are never one: splitting, merging, re-cutting, reordering or renaming Areas; the one-line Area outline itself; every field of an Area block; and the Chapter's working label (names are settled by delivery, not by plan). A departure is shown to the author at the confirm step of the Chapter Spec, each in plain words (what the entry says, what the Chapter says), and is logged as a traced variance in block 11 of this spec AND in the Audit and Settlement Notes of the Section Spec (block 12), written top-down in one step with the Chapter Spec, the Section Spec's note first and this spec's note next (Rules 9.4.4 and 9.4.5); each note is a light amendment appended by the Chapter build flow, adding a note and changing no plan content. The author then says, for each departure, which of two things to do. **Amend the plan:** the entry is changed through the `/part-spec revise` flow, as a light amendment when it touches only that entry and leaves the Novel-Part's own purpose, calendar window, reveals owed and closing state as they were, and otherwise as a substantial one, in which case the audit and the confirm are taken in the same run, because the chain is not in force below a spec that reads AMENDED-PENDING-RECONFIRM (Rules 9.4.2 and 11.7.2); where the change also reaches what the Section Spec fixes for this Novel-Part, the Section Spec's own command changes that first (Rule 11.4.3). **Leave the original as the plan baseline:** the variance notes stand and nothing else changes. The same question is asked when a later `/chapter-spec revise`, `/redraft-chapter` or `/redraft-area` changes a fixed item. Gate 1 Check #18 compares the draft with the Chapter Spec only, and no Area-against-upper-spec comparison exists (Rule 6.1.1(a)); a departure blocks nothing, and no question arises from it beyond the one at the confirm step.

**Rule 11.4.3 — Changes of the Chapter list are noted upward; so is a departure from the Section Spec's entry.**
When the Chapter list of this spec differs from the Section Spec's high-level Chapter list for this Novel-Part (a Chapter added, split, merged or dropped), two things are written: the change to this spec, as a light amendment (Rule 11.7.2); and a variance note appended to the Section Spec (Rule 9.4.5), so that the Section Spec shows how the plan moved. The Section Spec's own plan text is not changed by the note: its list is a guide. Both are shown to the author at the confirm step. Where the change touches what the Section Spec fixes for this Novel-Part (its purpose, calendar window or hand-off), it is a departure, as a Chapter's departure from its entry is (Rule 11.4.2): it is shown to the author at the confirm step, a variance note is appended to the Section Spec in the same step (Rule 9.4.5), and the author says which of two things to do. **Amend the plan:** the Section Spec's entry is changed through `/section-spec revise`, with the cascade report (Rules 9.4.1 and 9.4.2). **Leave the original as the plan baseline:** the note stands and nothing else changes. Both answers are lawful, and this spec governs the Chapters either way. A conflict with the spec above is put to the author and never settled silently (Rule 9.4.1).

### 11.5 — Build

**Rule 11.5.1 — The build sequence.**
The `/part-spec` build is led by one outline-planner for this level (Rule 9.9.1); the orchestrating command writes the spec and its registry row, and the outline-planner never writes a spec.
1. **Preconditions.** The Section Spec of the Novel-Part's Section is CONFIRMED or COMPLETED; if not, the command stops and names `/section-spec` (Rule 9.1.1). The Section Spec has an entry for this Novel-Part; if it has none (the story needs one more), the command stops and sends the author to `/section-spec revise` to add the entry first, because adding a Novel-Part to a Section Spec is a substantial amendment (Rules 9.4.2 and 10.6.2); nothing is built under a Novel-Part that the Section Spec does not know. A build over a Novel-Part that already has written Chapters is a retro-fit (Rule 9.8.2).
2. **Grounding.** The planner reads the whole Section Spec in full, the previous Novel-Part Spec's block 8 and Reader now knows line, the ledger state it needs, and the Part 30 passages that the Novel-Part's functions, window and Locked items point to (Rule 9.9.2). This grounding starts together with the other grounding of the command run (Rule 9.9.3).
3. **Draft.** The planner pre-fills the draft from the Section Spec's entry for this Novel-Part (Rule 9.3.1), recording each pre-filled value as a From note naming the entry: the entry's purpose into block 0, its thematic movement into block 1, its calendar window into block 0, who carries it into block 4 and the "On the page" lines, its opening state into the carry-in of block 0, its closing state and hand-off into block 8, and its high-level Chapter list into the Chapter entries of block 2. The planner carries the Section Spec's settled items as Inherited notes without asking them again (Rule 9.5.1). Anything the Section Spec deferred to the Novel-Part Spec is asked here, because it is now due.
4. **Consultation to full clarity.** Rounds of questions in the shape of Rule 9.6.4: two or three concrete options and `SKIP — let AI decide`, thematic previews on direction options (Rule 3.2.3), up to four questions to a call, as many rounds as the build needs. The topics are: the Chapter set and its order; for each Chapter its purpose, calendar window, threads in and out, who is on the page, key events, reveals and payoffs owed, opening hook, closing beat and one-line Area outline; the thematic movement of the Novel-Part (the direction questions of this level); the cut and cliffhanger plan across Chapters; the protagonist arc line; the progression beats; the opposition and reveal timing; and the closing state and hand-off. Only the author defers: a deferral is recorded as a Deferred note naming the Chapter Spec or Area writing (Rule 9.5.2), and a SKIP is recorded as a Skipped note and settles nothing (Rule 2.3.6). The grain test (Rule 9.6.2) decides what is asked here: a question belongs to this spec when the author's answer first changes the plan of the Novel-Part or of one of its Chapters at entry grain. Area anchors, continuation, pacing, size targets and opening and closing types are not asked in this build; tone, voice, sensory and content tags and Part 36 Autonomous Matters are never asked above Area (Rule 9.5.3). A conflict with the Section Spec found during the build is a question to the author, never a silent pick, and the answer is recorded through the variance channel, while the Section Spec's plan itself changes only through `/section-spec revise` (Rules 9.4.1, 9.4.5 and 11.4.3). Where a Section Spec answer has gone stale, clarity reduction applies (Rule 4.2.4): the original answer is shown beside the source of the change.
5. **Light audit and final sweep.** The continuity-checker's light audit (Rule 11.6.1) and the final sweep of Rule 9.6.5, run by the outline-planner and the continuity-checker together; the sweep also re-lists every SKIP and every deferral, so the author gets a last chance at each. If anything new comes back, more rounds follow and then a new sweep. The build is done only by the test of Rule 9.6.1: no unasked branch at this level, a sweep that returns nothing new, the author's explicit "nothing further to steer", and then the token. No score, no percentage and no round count is used.
6. **Confirm and write.** The author is asked with the three tokens, the prompt naming "Novel-Part Spec P.S.P" (Rule 3.4.1). At `[CONFIRM SPEC]` the command writes the file and its registry row and adds the session-log line (Rule 9.4.4); the spec is CONFIRMED and its settled items carry downward (Rule 9.5.1). `[REVISE SPEC]` re-runs the loop. `[SKIP SPEC]` saves the spec as DRAFT, and the chain stops here: no Chapter Spec can be built until it is confirmed (Rule 9.1.1). Only one confirm prompt is open at a time in a chain (Rule 9.4.4).

*When it is built:* at the boundary by `/start-story`, `/next-section` and `/next-part` (Rule 9.2.1), or ahead for a later Novel-Part on the author's request, with a built-against stamp (Rule 9.2.2). At the boundary the stamp is compared with what has since happened, and only the affected items are asked again, each with its original answer and the source of the change shown (Rule 9.2.3).

**Rule 11.5.2 — Adding an entry later.**
When the Chapter the story needs has no entry in this spec (every listed Chapter is written and one more is wanted, or a Chapter turns up that the list never contemplated), the Chapter build, or `/next-chapter`, **stops and says so** (Rule 9.1.2). It offers to add the entry as a **light amendment**: a short entry round that asks the entry's purpose, calendar window, threads in and out, who is on the page, key events, opening hook and closing beat, and, for the remaining fields (reveals and payoffs owed, the one-line Area outline, linked setup keys), asks the same way and lets the author defer any of them to the Chapter Spec. The amendment has its OWN `[CONFIRM SPEC]` / `[REVISE SPEC]` / `[SKIP SPEC]` prompt (it reads "Novel-Part Spec P.S.P, new entry for Chapter P.S.P.CCC"), put after a light audit of the new entry and what it touches (its window inside the Novel-Part window, all eight protagonists accounted, threads in matching the entry before it), and it is written at that confirm; only then does the Chapter Spec build begin, from the new entry, and the two prompts are never open together. A new entry changes the Chapter list, so it is also noted upward on the Section Spec, in the same write step as the entry (Rules 9.4.5 and 11.4.3). If the author declines or answers `[SKIP SPEC]`, this spec is left as it was and the command stops, because no Chapter Spec can be built without an entry (Rule 9.1.2). Where this spec has no further entry at all, the command does not decide what that means: it asks the author whether the Novel-Part has finished (the route is then `/next-part`) or the story needs one more Chapter (the light amendment above, or `/part-spec revise` for a larger change of plan, Rule 11.7.2). The list is never a reason to refuse a Chapter the story needs and never a reason to force one (Rule 1.5.1).

### 11.6 — Light Continuity Audit

**Rule 11.6.1 — Scope for a Novel-Part Spec.**
*(Rule 3.3.2 extended to the Novel-Part Spec.)* Every new Novel-Part Spec, and every substantial amendment of one (Rule 11.7.2), receives the continuity-checker's light audit before the author is asked to confirm (Rule 3.3.1). The audit is **report-only**: the checker writes nothing, and the orchestrating command writes the files (Rule 9.9.1). It checks the plan, not the written Areas, and covers:
- **(a) Calendar nesting.** The Novel-Part window sits inside the Section window, and every Chapter window sits inside the Novel-Part window (Part 30 §1.3.2a and Check 11-2).
- **(b) The Section Spec's duties.** Every duty the Section Spec assigns to this Novel-Part is covered: the Part 30 functions it carries, the setups assigned to it, the items deferred to this spec, and every item the Section Spec settled.
- **(c) The ensemble.** Every Chapter entry accounts for all eight protagonists (Rule 11.3.3).
- **(d) Carry-in.** The threads in match the previous Novel-Part's closing state and the ledgers; the built-against stamp still holds, or the affected items are listed for asking again (Rule 9.2.3).
- **(e) Labels.** The Novel-Part and Chapter labels read against Part 28 Rules 18.4.1–18.4.3, as advice only.
- **(f) Standing exclusions.** No entry plans any item of the standing exclusions (Chapter Spec template section 3: the P30-L8 entities, the P30-L9 sentient monsters, save the one narrow artifact-made exception of Canon Amendment 2026-10-19 (Law P30-L9), and the author-removed concepts).
- **(g) Schema conformance.** Every required field is filled, with an answer, a skipped choice or an author deferral recorded in the notes; each one-line Area outline holds descriptors only (Rule 11.3.4); no Establishment status, no count or range of Chapters and no stored status appears.
- **(h) Parent conformance.** Nothing contradicts a Locked Canon item or a settled item of the Section Spec, and for the last Novel-Part of a Section block 8 agrees with the Section Spec's hand-off.
- **(i) Clean body.** The body holds no inline settlement tag and the Audit and Settlement Notes section stands as the last block of the file, each note pointing to a plan item that exists (Rule 38.14).

Findings are reported with the confirmation prompt. Blocking findings, which are (a) to (d) and (f) to (i), must be resolved before `[CONFIRM SPEC]` is accepted; (e) is advice and blocks nothing. Within (b), a setup that the Section Spec assigned to this Novel-Part and that the plan does not carry is shown as information only and never blocks, because a setup is a guide and not a block (Rule 9.5.4; matching Rule 10.5.1(d)). The final sweep of Rule 9.6.5 is part of the same agent set and runs after the audit.

### 11.7 — Completion and a Living Record

**Rule 11.7.1 — Completion, on the author's yes.**
*(Rule 9.7.3 applied to the Novel-Part Spec.)* A Novel-Part Spec becomes COMPLETED, never closed (Rule 9.7.1). The boundary command writes it. `/next-part` asks "Has this Novel-Part finished?" as one of its checks, and `/next-section` asks "Has this Section finished?", whose yes also stands for the last Novel-Part and the last Chapter of the Section it closes. At the end of a Phase `/next-phase` completes the last Novel-Part Spec, asking the completions once each in the order Chapter, Novel-Part, Section (Rule 9.7.3); the author may instead run `/part-spec complete`. On the author's yes the spec is completed in the same bottom-up write step that confirms the successor (Rule 9.4.4): the outgoing Chapter Spec first, then this spec, then, at a Section end, the Section Spec. A Novel-Part Spec is completed only when every Chapter Spec under it is COMPLETED (the last one in that same step) or RETIRED with a variance note, or was never written and is recorded as dropped on the author's yes; if one is not, the command names it and stops. On no, the command stops. A Novel-Part Spec is never completed at Gate 2 (Rule 9.4.3), and it is not completed merely because its last Chapter is. The completion content is written into block 10:
- the **final variance summary**: planned versus as-written in brief, including every Chapter added, split, merged or dropped; an entry whose Chapter was never written is recorded there as dropped, with a note, on the author's yes;
- the **Reader now knows** line, by reference to the last Chapter's line plus the Novel-Part's own additions, with no copy of lists;
- a **Novel-Part digest**: what changed, who, and the open threads, by reference to the Chapter digests;
- the **threads and setups carried to the next Novel-Part**: the author is asked about each unpaid one (carry on, or mark lapsed), and a setup is lapsed only on the author's answer.

The reports made at a Novel-Part's end (reveals owed and not yet shown, threads, Part 30 functions) are information and never block (Rules 3.7.2 and 9.7.4). The registry row's Coverage cell is refreshed at this step (Rules 1.2.2 and 11.1.2).

**Rule 11.7.2 — A living record.**
A COMPLETED Novel-Part Spec stays living (Rule 9.7.1). `/part-spec revise` works at any time; there is no refusal "only through redraft", and the completion pieces of Rule 11.7.1 are refreshed when a COMPLETED spec is revised. A revision that changes plan content for Chapters already written leaves it to the author whether to redraft; written Areas are never touched by a spec amendment, and a correction there goes through `/revise-area` or a redraft (Rule 9.4.2). Amendments follow Rule 3.5.2 as extended to this kind of spec:
- **Substantial:** changing the Novel-Part's own purpose, closing state and hand-off, calendar window or reveals owed. The spec reads AMENDED-PENDING-RECONFIRM, receives the light audit and a fresh `[CONFIRM SPEC]`, and has no force until then. When it is re-confirmed it returns to COMPLETED if every one of its Chapter Specs is still COMPLETED and the author's yes of Rule 11.7.1 stands, and otherwise to CONFIRMED.
- **Light:** adding, splitting, merging or dropping a Chapter entry (Rule 11.4.3), a change inside one entry that leaves those four things as they were, and variance notes. These take effect at once with a log line and no re-confirmation.

Revising a Novel-Part Spec that has Chapter Specs runs the **cascade report** first: the continuity-checker lists every Chapter entry and Chapter Spec the change no longer fits, and for each the author chooses keep (with a variance note), amend it, or mark it AMENDED-PENDING-RECONFIRM; nothing flips by itself (Rule 9.4.2). When a rewind or reset removes written Areas, a COMPLETED Chapter Spec returns to CONFIRMED, and this spec returns from COMPLETED to CONFIRMED as soon as any of its Chapter Specs is no longer COMPLETED; the completion text is kept as history (Rule 9.8.1). A Novel-Part Spec is retired only explicitly, never silently, and not while it has Chapter Specs that are not RETIRED until the author has ruled on each (Rules 7.2.2 and 9.8.3).

### 11.8 — Illustration: A Filled Chapter Entry

**Illustration, establishes nothing (Rule 1.3.2).** The entry below plans an invented Chapter with placeholder names (Hero A to Hero H, Place A to Place C, the Ford Keeper). Nothing in it is canon, and no name in it may be used in a spec or in an Area. It continues the invented Area of section 2.5, and shows how the fields of the template (Rule 11.2.1, block 2) are filled, how all eight protagonists are accounted in one line, and how the Area outline stays a single line of descriptors with no names, anchors or types.

```markdown
### Chapter 002 — The Letter Road
**Purpose (Part 30 functions by name, Rule 2.3.2):** Carries the Section's journey function and Hero A's arc of learning to wait (each named by function in the real field).
**Calendar window (inside the Novel-Part window):** Days 2 and 3 of the Novel-Part window, from dawn on day 2 to dusk on day 3, written as `<first date> (Phase Day <P>)` to `<last date> (Phase Day <Q>)`.
**Threads in:** The letter thread (sealed, due at Place B by noon on day 4); Hero A's quarrel with the elders of Place A (unresolved).
**Threads out:** The letter thread (still undelivered, one day left); the Ford Keeper's private reason (planted, not yet named).
**On the page:** viewpoint: Hero A | on the page: Hero B (the first stretch of the road only), the Ford Keeper (a new speaker) | off the page: Hero C — Place A, held at the court by the inquiry; Hero D — Place A, in the records hall; Hero E — Place C, travelling with the escort; Hero F — Place C, resting at the escort's camp; Hero G — Place B, waiting for the letter; Hero H — Place B, at the gate
**Key events:** Hero A leaves Place A alone; the Ford Keeper refuses everyone passage; Hero A waits and learns why; Hero A crosses at low water.
**Reveals and payoffs owed:** The Ford Keeper's reason, shown to the reader and to Hero A at the end of the ford scene. Whether Hero A offers payment at the ford is left to Area writing.
**Opening hook:** Hero A walks out of Place A at dawn, still angry, with a deadline in a pocket.
**Closing beat:** Hero A on the far bank, carrying the keeper's reason, the letter still undelivered with a day to go.
**Area outline (one line, scenes in order, descriptors only):** the road out of Place A and the anger; the argument at the ford and the wait; the crossing and the walk on
**Linked setup keys:** `letter` (short thread name: carried here); `second pole` (short thread name: planted here, a suggestion that it pays in Chapter 004)
**Status:** derived from the Chapter Spec's registry row; never stored here
```

and the matching lines of block 11:

```markdown
## 11 — Audit and Settlement Notes

- **Chapter 002, Purpose** — From: Section Spec, Novel-Part 2, Chapter 2, "Hero A sets out with the sealed letter".
- **Chapter 002, Calendar window** — Settled: days 2 and 3.
- **Chapter 002, Reveals and payoffs owed, payment at the ford** — Deferred by the author to Area writing.
```

---

## Appendix A — Governing Authority

> Subordinate to the grounding in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.
