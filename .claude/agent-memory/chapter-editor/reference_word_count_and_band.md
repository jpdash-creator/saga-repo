---
name: word-count-and-band
description: Exact word counts with Grep offset probes (no Bash), and the measure --mode whole stretch-wording trap
metadata:
  type: reference
---

**Token rule.** A token is any whitespace-separated chunk with a word character ("Hercules's" and `*"Full,"*` are one each). `---`, `<!--`, `-->` are not tokens. A date line is 6 tokens; a marker `<!-- AREA 03 -->` is 2 (`AREA`, `03`). Chapter words = total tokens - 6 per date line - 2 per marker. This matches the script's `_words`.

**Probe.** Grep pattern `\S*\w\S*`, output_mode content, `-o`, `-n`, `offset` K, `head_limit` 3 to 6: returns the K-th token (0-based) with its line. Probe the end of the file (largest offset that answers) for the total.

**Per Area.** Predict the index of each marker's `AREA` token = 6 + 2 per marker passed + 6 per later date line passed + words counted so far. Probe from two tokens before; if it shows the last word, `AREA`, `NN`, the count is exact. After a multi-line edit, recompute from the new totals and probe 3 or 4 tokens around each boundary.

**Warnings.** Hand tallies drift 1 to 3 words when a multi-token phrase is swapped ("at the same moment." 4 tokens, "for a moment," 3, "had begun to show" 4): the probe is the figure. Grep `count` mode counts lines, never tokens.

**Staged `/revise-chapter` copy shape (Chapter 006).** The file opens with a `#` heading block (5 lines, 36 tokens: STARWARD SAGA, Phase, Section, Part and Chapter lines with MANDATORY comments), then `---`, marker 01, the date line. The script skips any paragraph that starts with `#` (`measure_whole`, line 386), so Chapter words = total tokens - 36 - 6 per date line - 2 per marker; marker 01's `AREA` token is index 36 and Area 01 text starts at 44 (the "6 + 2 per marker" prediction above is for a file with no heading block). To find a boundary cheaply: probe a token inside the last paragraph before the marker (the output shows its line), count the rest of that one paragraph by hand, then confirm with one probe window of 8 to 10 tokens across the marker.

**Clause cuts (single-edit revise steps).** Count the cut clause token by token before quoting a figure, including the last word that loses its comma ("as Yestin had told him at the slide." is 8 tokens; a brief said 7). After the edit, probe the next marker's `AREA` token and the last token of the file: each must move by exactly the clause count, and nothing else may move. Area targets for Chapter 006 are 3,000 each with "up to 0.72" (band 1,650 to 2,160), Chapter target 21,000 (11,550 to 15,120).

**Script trap.** `chapter_builder.py measure --mode whole` honours a Budget stretch only when the spec's `Budget stretch:` text, stripped of `*`, `_`, spaces, starts with "up to" (`parse_spec_areas`, about line 318). Otherwise each Area tops at 60% and shows OUT OF BAND. Check the wording before telling the command to expect a script PASS; a mismatch is a spec-wording item reported to the author, never edited. Command shape: `python .claude/tools/chapter_builder.py measure --mode whole --spec-file <chapter-NNN-spec.md> --text-file <staged .md> --phase 1 --section 1 --part 1 --chapter N`.
