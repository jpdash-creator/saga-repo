---
description: Search the written Areas and the ledgers for a name or phrase and list every place it appears, with references. Read-only.
argument-hint: <name or phrase to find>
user-invocable: true
---

# `/find`

Read-only search of what is already written. The command has no command code. It looks for a name,
a word or a phrase in the written Areas and in the ledgers and lists each place it appears, so a
person, a place, a line of dialogue or a detail can be traced without opening files one by one. It
changes nothing.

## What is searched

- **Areas.** The `.md` file of every written Area under `projects/novel-starward-saga/`
  (`phase-N/section-N/part-N/chapter-NNN/area-NN.md`). The `_archive` folder is never
  read, listed, counted or searched (Part 2 Rule 5.3.2a).
- **Ledgers.** Every file under `.claude/story-memory/ledger-*/`, the `_index.md` registries
  included. An `_archive` folder there is skipped too.

The specs (Section Specs, Novel-Part Specs and Chapter Specs), the session log, skills and
guardrails are not searched. A spec holds plans and never establishes a fact (Part 38 Rule
1.3.2), and the session log is a trace, never a canon source
(`guardrails/ledger/guardrail-session-log-not-canon.md`). `/section-spec show`,
`/part-spec show`, `/chapter-spec show` and `/threads` read the specs.

## Sequence

1. Take the text as typed: a phrase is matched as a phrase, and capitals are ignored. With no
   argument, ask what to find and stop.
2. Search the Area files and the ledger files in one parallel batch, from disk and never from
   memory.
3. Report:
   - **Area hits**, in story order. For each file: the Reference Code (`P.S.N.CCC.AA`, read
     from the file's path) and the line that holds the text. When one file holds many hits, show
     the first few and say how many more it holds.
   - **Ledger hits**, grouped by ledger folder. For each file: the entity name, the section
     heading the hit sits under and the line that holds it.
   - One closing line: how many Area files and how many ledger files hold the text. When nothing
     is found, say so, and add that a name found only in a spec (Section, Novel-Part or Chapter)
     is a proposal and is not established.

## Related

`/review-ledger` shows one entity in full. `/canon-check` tests a claim against canon.
`/area-history` lists recent Areas. `/timeline` and `/threads` read the specs of the chain.
