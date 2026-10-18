---
name: grep-word-count-technique
description: How to get an exact prose word count with only Read/Write/Edit/Grep/Glob tools (no Bash) — the Grep "count" output mode counts matching LINES, not matches, so it silently gives the wrong number for word counts.
metadata:
  type: reference
---

The Grep tool's `output_mode: "count"` reports the number of **matching lines**, not the
number of matches — this holds true even with `-o: true` set. Confirmed empirically: a
3-line file with 10 total words (`one two three` / `four five six seven eight` / `nine ten`)
returns `3` for pattern `\S+` with `-o: true`, not `10`. Any Check #10 pacing word count
verification that uses `count` mode on a pattern like `\S+` against prose written with one
paragraph per line will return the paragraph/line count, not the word count — a silent,
plausible-looking wrong number that is easy to mistake for a real word count.

**Working technique instead:** write the prose to a scratchpad file, then binary-search for
the exact word count using `output_mode: "content"`, `-o: true`, `-n: false`, pattern `\S+`,
and the `offset` + `head_limit: 1` parameters. `offset: N-1` with `head_limit: 1` returns the
Nth word if it exists, or "No entries at this offset" if the document has fewer than N
words. ~12 probes converge on the exact count for a ~2500-word document. This is far more
token-efficient than dumping the whole word list via `head_limit: 0`.

**How to apply:** Use this whenever independently re-verifying Check #10 (pacing word count)
rather than trusting a `count`-mode Grep result at face value — the count-mode number will
look plausible (it correlates with paragraph structure) but is not the word count. Related
technique note: the same line-count-vs-match-count gotcha applies to any other Grep-based
tallying (e.g. counting dialogue spans, counting em-dash occurrences per line vs. total).
