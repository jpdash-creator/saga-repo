# Guardrail: Domain Ownership Rule

**Source:** this guardrail · Canon v10.0
**Applies to:** all 4 agents, always

## The rule

Every subject in the canon has exactly one governing Part. Full assignments live in
`.claude/canon-manifest/domain-map.json` — consult it rather
than guessing which Part owns a topic.

- **Exclusive Authority.** Only the registered governing Part may make binding rulings
  on its domain.
- **Routing by Subject, Not Scene.** A relic appearing in a combat scene is still Part
  12's domain, not Part 5's, just because the scene is a fight. Always route by *subject*,
  never by the *scene type it happens to appear in*.
- **Cross-Domain Dependencies.** When multiple Parts co-occur (e.g. a cultivation
  breakthrough during combat touches Parts 3, 5, and 27), each Part governs only its own
  slice — no single Part absorbs the others.
- **Domain Boundary Disputes.** If no Part clearly owns a subject, this is a **Joint
  Domain Resolution** case — escalate, do not pick one Part's authority by default.
- **No Domain Expansion Without Amendment.** A Part may never quietly start ruling on
  a neighboring Part's territory (e.g. Part 5 ruling on psychological trauma, which is Part
  26's domain) without a formal Canon Amendment. This applies equally to skills: a
  canon skill must stay inside its own Part's subject matter.

## Escalation

Any apparent domain overlap or gap is not resolved by an agent's own judgment. Mid-Area, the
agent stops and reports it to the orchestrating command, which asks the author; structural
doubt between Areas goes to `/run-canon-audit`. The route is set out in the Escalation rule
of `.claude/guardrails/_index.md`.
