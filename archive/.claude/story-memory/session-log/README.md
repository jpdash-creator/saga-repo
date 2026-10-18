# Session Log

This folder is a human-readable audit trail — a running record of what each `/next-prose`,
`/run-canon-audit`, `/force-ledger-audit`, and reset-family command did and why.

**It is never a decision input.** Per `.claude/guardrails/ledger/guardrail-session-log-not-canon.md`
(Rule F-5, "Files-Only Decision Governance"), no agent may cite this log — or conversational
memory generally — as justification for a canon fact. The only valid canon sources are the
skills, guardrails, `story-memory/ledger-*/` files, and the written prose itself. If it
isn't in one of those, it isn't canon yet, no matter how clearly it was discussed.

Write here freely; read from here only for human review or debugging, never to decide what's true.

Suggested entry format (one per command invocation that changes state):

```
## 2026-05-24 -- /next-prose (phase-1/section-1/part-1/chapter-001/area-1/prose-00003)
Gate 1: PASS (clean). Gate 2: PASS. Ledger updates: ledger-character-hero/varys.md (L fields),
ledger-worlds-location/azure-sky-palace.md (Events Log). CDL-2: Combat 24%, Dialogue 31%, ...
```
