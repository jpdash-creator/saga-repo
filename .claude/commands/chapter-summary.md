---
description: Summarize the current or a specified Chapter's events, without reproducing full prose.
argument-hint: "[chapter reference]"
user-invocable: true
---

# `/chapter-summary`

Corresponds to canon command `[CHAPTER SUMMARY]` (C-32). Read-only summary drawn from the
actual written Area files (never the `_archive` folder) and relevant `.claude/story-memory/ledger-*/` Events Log sections — not
from conversational memory (`.claude/guardrails/ledger/guardrail-session-log-not-canon.md`).

## Output

The summary is plain text, in this order. It is read-only and writes nothing.

1. **Header.** The Chapter's name chain and reference prefix, and the status of each of its
   Areas (`PLANNED`, `DRAFTED`, `WRITTEN` or `DROPPED`), read from the Chapter Spec. When the Novel-Part Spec of
   the Chapter's Novel-Part is `COMPLETED`, one optional line may carry that Novel-Part's
   digest, read from its completion block (Part 38 Rule 11.7.1), so the Chapter is read in
   its Novel-Part's context; the line is read, never worked out again, and is left out when
   the Novel-Part is not `COMPLETED`.
2. **One block per Area, in Area order, at most 15 lines each:**
   - *What changed*: what is different at the end of the Area, as the written Area shows it.
   - *Who*: the viewpoint characters and the other people on the page.
   - *Open threads*: setups planted and not yet paid off, and a cliffhanger or open question
     with the Area that is to resolve it (read from the Area block's Planted here, Carried or
     paid off here and Closing type).

   An Area not yet written is one line: its status and its one-line purpose.
3. **Accepted sameness patterns.** Each sameness pattern the author accepted at
   `[CONFIRM WRITE]`, with the Reference Code of the Area it was reported on.
4. **Accepted variances.** Each plan-versus-written difference accepted at `[CONFIRM WRITE]`
   or traced to an author answer, with the Reference Code of the Area and its variance note.

Lists 3 and 4 are read from the Variance Notes and the variance log of the Chapter Spec (Part
38 Rule 3.6.1 item 2) and read "none recorded" when empty. The summary quotes no more than a
few words from the Areas and never reproduces a passage.

**Whole-built Chapters.** A Chapter built whole by `/create-chapter` has no Area files and its Area rows
read `WRITTEN(P.S.N.CCC)`. The summary then reads the Chapter file (`Chapter NNN - <Name>.md`) and the
Chapter Spec's Area blocks and gives the header, then one block per Area block of the spec (the hidden
`<!-- AREA NN -->` markers locate it in the Chapter text) with the same three lines (what changed, who,
open threads), at most 15 lines each; lists 3 and 4 are read as above, with the Chapter reference
`P.S.N.CCC` in place of an Area reference.

## Chapter digest

When a Chapter is completed (`/chapter-spec complete`, reached through `/next-chapter`) the same
text is written into the Chapter Spec as the **Chapter digest** (Part 38 Rules 3.7.1 and 9.7.2).
Later work can then read the Chapter's history from the digest without opening its Areas. The
Novel-Part Spec and the Section Spec each carry a digest of their own once completed (Part 38 Rules
9.7.3, 11.7.1 and 10.6.1); this command reads the Chapter's digest only, apart from the optional
Novel-Part line in the header.
