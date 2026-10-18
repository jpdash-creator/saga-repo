---
name: counting-without-shell
description: Grep-only exact word and character counts, staging-file assembly and the guard search, for an agent with no Bash
metadata:
  type: reference
---

No shell, so counts come from Grep. The script `measure` is the figure of record; the Grep count must agree (words = tokens holding a word character, asterisks stripped; date line, markers, `---` and `* * *` are not counted). State the method in the hand-off. The draft must be ASCII for exactness (the corner brackets of a wired notice attach to words and do not break it).

**Whole draft.** Put each Area in a scratch copy (marker, `---`, date line, text, `@@END@@`). Grep `\S+`, `output_mode` content, `-o`, `-n` false, `head_limit` 1, with `offset` set to a ladder (for example 2000, 2010, 2020, 2030) in ONE parallel batch; the offset that shows `@@END@@` is total tokens minus 1. Narration = total minus marker 4, `---` 1, date line 6, 3 per `* * *`, sentinel 1.

**Marker-offset method (whole staged Chapter, fastest).** Probe the offset that shows each `<!--` (steps of 50, then 10, then single values, one parallel batch per round; an offset past the end answers "No entries"). Narration of Area k = offset of marker k+1 minus offset of marker k minus 4, minus 1 per `---`, 6 per date line, 3 per `* * *` that sits between them; the last Area = total tokens minus its marker offset minus 4. Check the sum plus the 4/6/1/3 extras against the total tokens. Hand estimates ran 10 to 15 percent under the Grep figure: draft each beat to about 85 percent of its intended size, then count.

**Bracketing.** At-least form `\A\s*\S+(?:\s+\S+){N-1}` (never `\A(?:\s*\S+){N}`: `\S+` can split a word). Written Area file: skip the title block, `\A(?:[^\n]*\n){4}(?-u:(?:\s+\S+){N})`.

**Pinning in a staged file.** Marker-anchored, matches only at exactly N tokens: `<!-- AREA 02 -->\s+\S+(?:\s+\S+){N-1}\s+<!-- AREA 03 -->`. For an Area that opens on a break and date line anchor on the date line (`Nuvil, Day 2\*\s+\S+...`); last Area ends `\s*\z`. Repetition up to about 1,150 compiles; split by Area. Rerun every Area after every edit (hand arithmetic drifted by 1 to 2 words). Anchor trap: an anchor word followed by a comma must include the comma, or no k matches. By-area file with headers: anchor on header, reference line and date line (`\S+(?-u:(?:\s+\S+){k})\s+## Area N `).

**Area split by `* * *`.** Probe each section separately: ranges of 10, then 4, then single values, in parallel.

**Staging assembly.** One Write holding Area 01 plus a line `@@NEXT@@`; one Edit per later Area replacing the sentinel with the text plus a fresh sentinel; the last Edit drops it. Read the scratch files first so the copy is exact. Then confirm that each later marker sits at the predicted offset.

**Sentences.** Grep has no look-around and `count` counts lines: list with `-o -n` the pattern `[.?!]["*」]*(\s|$)` and count per paragraph; a quoted question plus tag counts 2; same rule on old and new text.

**Characters (for /chapter-builder).** `output_mode` count, pattern `\A(?:[^\n]*\n){K}(?:[\r\n*]*[^\r\n*]){N}`: matches when the text after K lines holds at least N characters (newlines and asterisks skipped). K=1 staged file (each `---` adds 3), K=4 written Area (more if a title page). Steps of 500, 100, 25, then 1. Pass the exact file path: a glob with spaces in the name matches nothing.

**Guard search before hand-off.** One alternation, case-insensitive, `-o -n`: em dash, contractions, banned words (as plain substrings: tail inside "tailboard"), digits, crutch words, non-ASCII.
