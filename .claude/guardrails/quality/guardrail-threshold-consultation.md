# Guardrail: Threshold Consultation

**Source:** this guardrail · Canon v10.0 · governing principle: Parts 28, 29, and 36 (Authority Tier 0)
**Applies to:** all four pipeline agents (Area Maker, Outline Planner, Continuity Checker, Area Scorer) and every command that computes a value against a stated line

## The rule

Every numeric line in the canon — floor, ceiling, band, budget, counter, or projection — is a
**guide post**, not a physical law. The story spec runs the story. The numbers describe how the
story is running; they exist to be computed, reported, and reviewed by the author, never to
govern the prose against the author's judgment.

When a computed value crosses one of those lines, the AI **reports it as information**: the
value, the line and the margin go into the audit report. It does not quietly fix it, and it does
not stop to ask the author on the number alone. The confirmed spec chain and Part 30 prevail over every counter.

This guardrail exists because the novel must read like living people, not like a system
satisfying its own arithmetic. That goal outranks every number below it.

## Hard rules

- **Compute and report.** Any agent whose work measures a value against a stated line reports
  that value plainly, whether it holds or not. Computing a number and staying silent about it
  is itself a violation of this guardrail.
- **Identify, do not remedy.** No agent expands, trims, restructures, re-scopes, or pads an
  Area in order to bring a number back inside its line. The crossing is named in the
  report and the prose stands unless the author asks for a change. This holds whether the
  value was measured from finished text or projected forward from a spec.
- **Show the reading plainly.** A crossing is shown with the number, the line it crossed and the
  margin. No `AskUserQuestion` is raised for it; the author sees the reading in the audit report
  that precedes every confirmation and may act on it or not.
- **Living-novel primacy.** Where satisfying a number would make the prose mechanical — padding
  to reach a floor, cutting a living beat to clear a ceiling, inserting a quota-filler to
  satisfy a counter — **the number yields.** The prose stands and the reading is recorded as
  information. Parts 28, 29, and 36 and the confirmed spec chain
  outrank numeric compliance.
- **No counting about counting.** This guardrail adds no margin tables, no near-miss bands, no
  iteration limits, and no numeric machinery of its own. A line is crossed or it is not.
  Elaborating this rule into further arithmetic is contrary to its purpose.
- **Drafting guidance is not a break.** An instruction telling the Area Maker what to write is
  guidance, not a threshold event. It becomes one only when an auditor measures a shortfall in
  a finished draft. Draft freely to the guide posts; report when a measurement crosses one.
- **Routing.** No pipeline agent holds `AskUserQuestion`. An agent that finds a conflict the
  author must rule on (a number crossing a line is only reported, never a question) reports it
  to the orchestrating command, which asks the author. An agent must never treat its inability
  to ask as licence to decide.
- **No word-count code.** `word_count` is declared in both authorized writer scripts, passed
  through, and never read, and no counting code is added. The size of an Area is read by the
  auditor against the Area size range of Part 2 (1,280 to 2,400 words), and the date line is not
  counted (Part 41 Area 5). The size range is the one structural limit: a count outside 1,280 to 2,400 words is a blocking finding: the write waits for the author to confirm the Area or send it back.

## The author's remedies

Accepting the reading and proceeding is the default, since a reading is information. The
author may also, at any time:

1. direct a revision, with suggestions;
2. revise the spec so the plan matches the story being told;
3. set the number aside for that Area.

## Escalation

Where a number's own definition is unclear or self-contradictory, **record the contradiction
plainly, keep the working reading, and bring it to the author** — do not resolve it by decree
and do not harden it into stricter law. (For example, the flat `≥20%` of CDL2-P4 is an information reading, not a Hard FAIL.)
