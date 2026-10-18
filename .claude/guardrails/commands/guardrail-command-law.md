# Guardrail: Command Law

**Source:** this guardrail (the command layer has no skill file) · Canon v10.0
**Applies to:** whichever agent/context is executing a `.claude/commands/*.md` slash command

## The rule

Commands are the only sanctioned entry points into the writing pipeline. Every
prose-producing command runs a Full Canon Audit plus the Two-Gate Sequenced Output described
in `.claude/guardrails/audit/guardrail-audit-gate-law.md` — a command file's body may streamline *how* that
happens, but may never skip Gate 1, skip the Inter-Gate Confirmation, or skip Gate 2.

- **One-Area-Per-Invocation** — a single `/next-area` or `/revise-area` invocation produces one Area's worth
  of Gate 1 → confirm → Gate 2, never a silent batch. (Amended 2026-10-07: this rule governs the Area pipeline,
  `/next-area` and `/revise-area`, only. It does not bind `/create-chapter` (Command C-42) and
  `/revise-chapter` (Command C-43), which are the lawful whole-Chapter writers: a second lawful path under a new
  rule, not an exception. `/create-chapter` writes one whole Chapter per invocation from its confirmed Chapter Spec,
  with no Area files, through the Whole-Chapter Gate 1 and Gate 2 of `.claude/guardrails/audit/guardrail-audit-gate-law.md`.
  A Chapter is built either by Area or whole, never both, and neither path batches Areas.)
  This binds the *planning* step as much
  as the write step: a command must never ask Outline Planner to plan, or
  Area Maker to draft, more than one Area in a single pass, even when the structural
  moment plausibly calls for two Areas in sequence — that becomes two
  full, separately-confirmed invocations, not one combined one. A single response also never
  *presents* more than one Area to the user at once — each Area gets its own Gate 1
  chat delivery and its own confirmation. The preceding Area is read, never batched: the flow
  review reads it, but only the new Area is planned, drafted,
  presented, confirmed and written, and lines quoted from earlier Areas as evidence are not
  a presentation of those Areas.
- **Pre-Area Read Mandate** — every governing skill + relevant `story-memory/` ledgers +
  the Area before it in full, as written on disk (and, where the scene being continued runs over
  several Areas, the earlier Areas of that scene in order); older Areas and Chapters reach the writer
  through the ledgers, and a fact from an older Area is checked by opening that Area by search
  (Part 28 Area 4.6), with no exception for session boundaries. Per
  `.claude/guardrails/authority/guardrail-consolidated-skill-reading.md`, each Part's skill is the read that
  satisfies this mandate.
  The archive folder is never read, listed or counted; each file read is read by its exact
  path (Part 2 Rule 5.3.2a).
- **Decision Consultation Gate (Exhaustive Clarity Mandate)** — every
  Area-producing command runs the Decision Consultation Gate (`narration-novel-creative-flexibility-law`
  §Area 19; `/revise-area` in its short form) before drafting, asking as many rounds of `AskUserQuestion` as it takes to reach no
  remaining open branch point — bounded by completeness, not by a fixed round count. Pacing is not asked at
  the Gate: the Chapter Spec decides the pacing of every Area, and the Gate carries that value. `[SKIP]` remains always available per-question except
  on canon-compliance questions, which must be resolved, not skipped. The per-Area
  `[NO CONSULT]` waiver (Part 28 Area 19) bypasses this Gate only; it is not a Gate 1 or
  Gate 2 confirmation and never substitutes for one. **Spec commands:**
  `/section-spec` (C-40), `/part-spec` (C-41) and `/chapter-spec` (C-39) run
  the same exhaustive-clarity consultation at their own level, with the one definition of "done"
  of Part 38 Rule 38.13: no unasked branch at that spec's own level, a final sweep that
  returns nothing new, the author's explicit "nothing further to steer", and then the confirm
  token. Like the Area Gate, they are bounded by completeness and not by a round count, and
  none of the three has a quick mode. Only the author may defer an item, and a deferral to
  writing time is carried into the Chapter Spec so the Area-time Gate asks it.
- **Gate 1 Chat Delivery format** — every Gate 1 presentation
  prints, in this order: (1) the Position Header Block, with the complete five-tier name
  chain (Phase, Section, Novel-Part, Chapter, Area — per Part 28 Area 18 Rule
  18.3.1), Reference Code (written `P.S.N.CCC.AA`: Phase, Section, Novel-Part, three-digit Chapter, two-digit Area), the Chapter Spec's pacing for the Area, a **Calendar line** (chat only: the date
  line as written, the Phase Day it stands for, and the date of the Area before it), and a
  "redraft in progress" line when later Areas sit after it on disk; (2) the **full text of the Area, verbatim, its date line first**; (3) the Contextual Earning
  Declaration; (4) the Post-Draft Audit Report, which names the Triggered Parts and every
  FAIL and gives one line counting the Not Triggered and N/A Parts (the full named-result
  list, every Part as Triggered, Not Triggered or N/A, goes to the session log, which meets
  the omission rule of the Full-Canon Named-Result Check in `.claude/guardrails/audit/guardrail-audit-gate-law.md`),
  and which carries the flow verdict, any
  reported flow pattern with its quoted lines (Check #16 dimension 16-J) and the
  plan-versus-written list (Part 38 Rule 6.1.4; a list with a BLOCKS line gets no
  confirmation prompt); (5) the confirmation prompt, which says that `[CONFIRM WRITE]`
  accepts the listed differences. The
  prose is never replaced by a summary, an excerpt, a paraphrase or a file path — at every
  Gate 1, after every revision, and in `/revise-area`. Revisions inside the FAIL loop that
  precede a clean audit are not printed; the draft that reaches the confirmation prompt, and
  every draft after `[REVISE AREA]`, is printed in full. When a question to the author is
  about the draft (a Check #21 enquiry, an earlier-Area repair, a spec difference), the
  Position Header and the full text are printed first and the question follows them.
  Otherwise the presentation is clean: no assistant-authored commentary, framing, or summary
  text is wrapped around these blocks.
- **Confirmation tokens**: `[CONFIRM WRITE]`, `[REVISE AREA]`, `[SKIP WRITE]`,
  `[CONFIRM SPEC]`, `[REVISE SPEC]`, `[SKIP SPEC]` (one set of three spec tokens serves the Section
  Spec, the Novel-Part Spec and the Chapter Spec),
  (for `/create-chapter` and `/revise-chapter` the gate tokens are `[CONFIRM WRITE]`, `[REVISE CHAPTER]` and `[SKIP WRITE]`; here `[REVISE CHAPTER]` at a gate rejects the staged text, while `[REVISE CHAPTER]` as a command is Command C-43),
  the destructive-command confirmation in the next bullet, and the author's ruling on an open Check #21 enquiry, flow finding or Tier D flag (each asked with the Area text printed first), are the only valid ways to advance
  past a gate — a command body must wait for one, never assume consent. A spec confirm prompt
  names the artifact and its reference in plain words ("Section Spec 1.2", "Novel-Part Spec 1.2.3",
  "Chapter Spec 1.2.3.004"), and only one spec confirm prompt is open at a time in a chain. `[CONFIRM WRITE]` accepts what the
  audit report lists as accepted by it (non-settled spec differences, sameness patterns);
  the bare token `[REVISE AREA]` rejects them (it is a confirmation token at a gate, never the command `[REVISE AREA: ref]` of Command C-28, which revises an already-written Area); `[SKIP WRITE]` discards the draft and everything with it —
  nothing is written or updated.
- **Destructive-command confirmation**: the commands that clear,
  delete, archive, roll back or restore story data (`hard-reset`, `reset-story`, `reset-ledgers`,
  `reset-chapter`, `reset-phase`, `rewind-to`, `redraft-area`, `redraft-chapter`, `restore-archive`) and the Step 5 preview of `force-ledger-audit`
  confirm through `AskUserQuestion`, never through an open-ended "yes". The question has a
  **Cancel** option, and the confirming answer names the scope in words (for example
  "Reset Chapter 12, 5 Areas, 2 archived pairs"), so a mistyped scope (a Phase for a Chapter)
  cannot be confirmed by accident. Cancel, or any answer that is not the confirming one, ends
  the command with nothing changed. The four commands that delete Area files (`hard-reset`,
  `reset-story`, `reset-chapter`, `reset-phase`) first ask the author, through
  `AskUserQuestion` with a Cancel option, to commit or copy `projects/` and `story-memory/`,
  and go on only when the author says that is done.

## Hard rules

- `/create-chapter` (Command C-42, `[CREATE CHAPTER]`) and `/revise-chapter` (Command C-43, `[REVISE CHAPTER]`) (Amended
  2026-10-07) are the whole-Chapter writer and reviser. The Chapter Spec header carries `**Build mode:** whole | by-area`
  (default `whole`). `/create-chapter` refuses a Chapter that has Area files (it names them and points to `/chapter-builder`
  or `/redraft-chapter`); `/next-area`, `/revise-area` and `/chapter-builder` refuse a Chapter built whole. They write no
  Area file: the only output is the Chapter file pair in the Novel-Part folder, written only by
  `.claude/tools/chapter_builder.py` after the author's confirmation. Both stop for the author at the build plan and at the
  staged text (see `guardrail-plan-then-auto-execution.md`). The deprecated `[WRITE NEXT N AREAS]` and
  `[WRITE TO END OF CHAPTER]` stay deprecated.
- `/chapter-builder` (Command C-24) is a Chapter-level command that writes no Area. Once per Chapter it calls the
  `area-maker` (to condense the Chapter's finished Areas) and the `continuity-checker` (to audit the condensed text), and
  the authorized script `.claude/tools/chapter_builder.py`, which alone writes the Chapter `.md` and `.docx`. It writes only
  after the author's explicit confirmation. It replaces the retired `/export-chapter` (author ruling 2026-10-07).
  `/compile-phase`, `/compile-phase-md`, `/compile-novel` and `/compile-novel-md` only join the Chapter files it writes.
- Any command whose frontmatter carries `disable-model-invocation: true` — currently
  `hard-reset`, `reset-ledgers`, `reset-story`, `reset-chapter`, `reset-phase`, `rewind-to`,
  `redraft-area`, `redraft-chapter`, `restore-archive` and `next-phase` (`/redraft-chapter` on a Chapter built whole archives it and runs `/create-chapter` again; `/rewind-to` on such a Chapter rewinds to the Chapter) — may be triggered only by an explicit
  human `/command` invocation; no agent may decide on its own initiative that a reset,
  rewind, redraft, restore or Phase advance is warranted. The frontmatter flag is the authority; this
  list is descriptive.
- A command file's frontmatter and body are the *procedure*; they never substitute for the
  actual skill/guardrail content a step requires — a command says "run the Gate 1 audit,"
  it does not restate what Gate 1 checks.

## Command codes

A command code is written **Command C-n** (for example Command C-4 for `/next-area`). Part 37
also uses C-1, C-2 and C-3 for its ledger-creation thresholds, which are written **Threshold C-n**.
Where a command name stands beside a bare code, as in "[HARD RESET] (C-1)", the code is read as
Command C-1.

| Command code | Slash command | Canon command |
|---|---|---|
| Command C-1 | `/hard-reset` | [HARD RESET] |
| Command C-2 | `/reset-ledgers` | [RESET LEDGERS] |
| Command C-3 | `/start-story` | [START STORY] |
| Command C-4 | `/next-area` | [NEXT AREA] |
| Command C-6 | `/next-chapter` | [NEXT CHAPTER] |
| Command C-7 | `/next-part` | [NEXT PART] |
| Command C-8 | `/next-section` | [NEXT SECTION] |
| Command C-9 | `/next-phase` | [NEXT PHASE] |
| Command C-10 | `/run-canon-audit` | [RUN CANON AUDIT] |
| Command C-13 | `/status` | [STATUS] |
| Command C-14 | `/review-ledger` | [REVIEW LEDGER: entity] |
| Command C-15 | `/update-ledger` | [UPDATE LEDGER: entity] |
| Command C-16 | `/rewind-to` | [REWIND TO: ref] |
| Command C-17 | `/ideology-audit` | [IDEOLOGY AUDIT] |
| Command C-18 | `/consequence-audit` | [CONSEQUENCE AUDIT] |
| Command C-19 | `/character-sheet` | [CHARACTER SHEET: name] |
| Command C-20 | `/canon-check` | [CANON CHECK: passage] |
| Command C-21 | `/reset-story` | [RESET STORY] |
| Command C-22 | `/reset-chapter` | [RESET CHAPTER: ref] |
| Command C-23 | `/reset-phase` | [RESET PHASE: N] |
| Command C-24 | `/chapter-builder` | [CHAPTER BUILDER] |
| Command C-25 | `/compile-phase` | [COMPILE PHASE: N] |
| Command C-26 | `/compile-phase-md` | [COMPILE PHASE MD] |
| Command C-27 | `/compile-novel` | [COMPILE NOVEL] |
| Command C-28 | `/revise-area` | [REVISE AREA: ref] |
| Command C-29 | `/redraft-area` | [REDRAFT AREA: ref] |
| Command C-30 | `/redraft-chapter` | [REDRAFT CHAPTER] |
| Command C-31 | `/preview-chapter` | [PREVIEW CHAPTER] |
| Command C-32 | `/chapter-summary` | [CHAPTER SUMMARY] |
| Command C-33 | `/area-history` | [AREA HISTORY: N] |
| Command C-34 | `/pause` | [PAUSE] |
| Command C-35 | `/load-canon` | [LOAD CANON] |
| Command C-36 | `/create-image-phase` | [CREATE IMAGE: PHASE N] |
| Command C-37 | `/create-image-section` | [CREATE IMAGE: SECTION N] |
| Command C-38 | `/force-ledger-audit` | [FORCE LEDGER AUDIT AND UPDATE] |
| Command C-39 | `/chapter-spec` | [CHAPTER SPEC] |
| Command C-40 | `/section-spec` | [SECTION SPEC] |
| Command C-41 | `/part-spec` | [PART SPEC] |
| Command C-42 | `/create-chapter` | [CREATE CHAPTER] |
| Command C-43 | `/revise-chapter` | [REVISE CHAPTER] |

Commands C-5, C-11 and C-12 are vacant: no command file carries them. `/new-character`,
`/character-behavior`, `/find`, `/timeline`, `/threads`, `/compile-novel-md` and `/restore-archive` have no command code.

Bare `[REVISE AREA]` at a gate is the confirmation token (Gate 1: it rejects the draft and returns to drafting); `[REVISE AREA: ref]` is the command (Command C-28).

## The amendment token

`[CANON AMENDMENT]` is the author's formal instruction that changes a Locked Canon rule; it is the only valid
override of a law that names it as such (Law P30-L8 and Law P30-L9 in Part 30, and the amendment route of
Part 38). It is not a gate-confirmation token and it is not a slash command. It is issued by the author
in chat, outside any active writing invocation, with explicit reference to the rule and its designation. No agent issues, infers or accepts a substitute for it; a Decision Consultation
Gate option, a Negotiable Canon decision and an instruction given inside a writing invocation never stand in
for it. Once the author has issued it, the change is edited into the owning skill file and the manifest and
ledgers are reconciled (CCIA).

## Escalation

If a command's documented sequence can't be completed as written (a precondition isn't met,
a required file is missing), stop and report rather than improvising a different sequence.
