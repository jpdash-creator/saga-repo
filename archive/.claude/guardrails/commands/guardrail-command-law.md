# Guardrail: Command Law

**Source:** Part 1 (Governance and Audit Law), Area 7
**Applies to:** whichever agent/context is executing a `.claude/commands/*.md` slash command

## The rule

Commands are the only sanctioned entry points into the writing pipeline. Every
prose-producing command runs a Full Canon Audit plus the Two-Gate Sequenced Output described
in `audit/guardrail-audit-gate-law.md` — a command file's body may streamline *how* that
happens, but may never skip Gate 1, skip the Inter-Gate Confirmation, or skip Gate 2.

- **One-Prose-Per-Invocation** — a single command invocation produces one prose unit's worth
  of Gate 1 → confirm → Gate 2, never a silent batch. This binds the *planning* step as much
  as the write step (Canon v4.35): a command must never ask Outline Planner to plan, or
  Prose Maker to draft, more than one Prose unit in a single pass, even when the structural
  moment plausibly calls for a wide beat and a close beat in sequence — that becomes two
  full, separately-confirmed invocations, not one combined one. A single response also never
  *presents* more than one Prose unit to the user at once — each Prose gets its own Gate 1
  chat delivery and its own confirmation.
- **Pre-Prose Read Mandate** — every governing skill + relevant `story-memory/` ledgers +
  all prior stored prose files, with no exception for session boundaries.
- **Decision Consultation Gate (Canon v4.35 — Exhaustive Clarity Mandate)** — every
  Prose-producing command runs the Decision Consultation Gate (`ssc-narration-p28-pre-prose-decision-consultation-gate`)
  before drafting, asking as many rounds of `AskUserQuestion` as it takes to reach no
  remaining open branch point — bounded by completeness, not by a fixed round count. The
  pacing classification question (Fast/Medium/Slow) is mandatory on every single invocation
  with no exception, per Rule 19.3a. `[SKIP]` remains always available per-question except
  on canon-compliance questions, which must be resolved, not skipped.
- **Gate 1 Chat Delivery format** — every Gate 1 presentation shows the complete six-tier
  name chain (Phase, Section, Novel-Part, Chapter, Area, Prose — per Part 28 Area 18 Rule
  18.3.1) directly above the prose body, and is otherwise clean: the canonical blocks
  (Position Header, prose body, audit summary, confirmation prompt) are what's shown, without
  additional assistant-authored commentary, framing, or summary text wrapped around them.
- **Confirmation tokens**: `[CONFIRM WRITE]`, `[REVISE PROSE]`, `[SKIP WRITE]`,
  `[NO CONSULT]`, `[CANCEL]`, and per-command `[CONFIRM <ACTION>]` tokens are the only valid
  ways to advance past a gate — a command body must wait for one, never assume consent.

## Hard rules

- Destructive/state-resetting commands (`hard-reset`, `reset-ledgers`, `reset-story`,
  `reset-chapter`, `reset-phase`, `rewind-to`) are marked `disable-model-invocation: true` —
  only an explicit human `/command` invocation may trigger them; no agent may decide on its
  own initiative that a reset is warranted.
- A command file's frontmatter and body are the *procedure*; they never substitute for the
  actual skill/guardrail content a step requires — a command says "run the Gate 1 audit,"
  it does not restate what Gate 1 checks.

## Escalation

If a command's documented sequence can't be completed as written (a precondition isn't met,
a required file is missing), stop and report rather than improvising a different sequence.
