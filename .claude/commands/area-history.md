---
description: List the last N written Areas with their references and one-line descriptions.
argument-hint: <N>
user-invocable: true
---

# `/area-history`

Corresponds to canon command `[AREA HISTORY: N]` (C-33). Read-only listing sourced from
`projects/novel-starward-saga/` file listings and the Chapter Specs, not from memory. The `_archive`
folder is never read, listed or counted (Part 2 Rule 5.3.2a).

- **Which Areas:** the last N written Areas by narrative position (Phase, Section, Novel-Part,
  Chapter, Area), not by the order they were written. After a redraft the two orders differ; the
  narrative order is the one listed. N defaults to 5 when absent; a value below 1 is asked.
- **Description:** the first sentence of narration in the written file, which is the first sentence
  after the date line, or, only when no narration sentence can be quoted, the working title plus the
  beat of the Area's row in its Chapter Spec. The
  date line is the first line of the Area text, under the Title Block, and is not narration, so it is
  never the description (Part 41 Area 5, The Date Line).

- **Whole-built Chapters.** A Chapter built whole by `/create-chapter` has no Area files. Each is listed as
  one line at Chapter level instead of Areas: `<P.S.N.CCC> | <Chapter name> | <word count> words |
  <description>`, the word count from the narration of the Chapter `.md` (date lines, hidden
  `<!-- AREA NN -->` markers and scene-break marks left out) and the description the first sentence of
  narration after the Chapter's date line. It counts as one entry toward N, in narrative position among the
  Areas of Area-built Chapters.

## Output

One line per Area:

`<Reference Code> | <Area name> | <word count> words | <description>`

The Reference Code (`P.S.N.CCC.AA`, Phase.Section.Novel-Part.Chapter.Area) is read from the file's
path (`phase-N/section-N/part-N/chapter-NNN/area-NN.md`), the Area name from the Chapter Spec, the word
count is counted from the narration of the `.md` file, the Title Block and the date line left out
(neither is narration, and the date line is no part of any word count or of the Area size; Part 41
Area 5, The Date Line, Rule 41.5.6.1), and the
description is the one defined above.
