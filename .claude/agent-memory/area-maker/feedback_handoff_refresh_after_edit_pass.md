---
name: handoff-refresh-after-edit-pass
description: How to refresh a Chapter hand-off file after an editing pass or audit (text final) without leaving stale figures, tallies, join notes or Tier D lines
metadata:
  type: feedback
---

When asked to edit only the hand-off after an editing pass, treat every figure, name, tally and join statement in it as stale until re-proved on the final text.

**Why:** an editing pass rewrites openings, names persons and swaps words, so the size table, the Stranger Pass tallies, the join notes, the Tier D closing lines and the variance notes all drift. On Chapter 005 the stale items were a "post" and a "hold" tally for Areas that no longer used those words, a "rounded numbers" line, a count of "four parts" where the text had three, an unnamed-neighbour note and an "unnamed Stone Vigil" line.

**How to apply:**
- Sizes: probe `\S+` with `-o`, `head_limit` 2 at the predicted marker indices (previous marker + 4 + break + date tokens + the stated words) in one parallel batch; a `<!--` at each predicted index confirms the given per-Area figures; total tokens = last index + 1.
- Tallies: Grep `\b[Ll]ines?\b|\b[Pp]osts?\b`, hold/held, set, turn, weight, company, boards with `-o -n`, map the line numbers to Areas through the marker lines, and rewrite each per-Area statement to the real count and sense.
- Names: whole-word, case-insensitive Grep of every new first name and surname over story-memory, skills, guardrails, commands, agents and projects (`glob: "*.md"` for projects).
- Tier D table: count rows with a 5-cell regex such as `^\| [A-Z][a-z]+ [A-Z][a-z]+ \| 0[1-5] \|([^|]*\|){3}$`; confirm every backticked conduct code resolves with one alternation Grep of the codes in the synthesis skill.
- The Grep tool prints "[Omitted long matching line]" for very long ledger or skill lines: read those with Read offset and limit.
- Pick a `[SIG]` for a reported or merely present person from the beat the narrator shows (someone who "went deep into his slate" fits a stress code of turning to craft; a sentry who "stood watch with faces to the plateau" fits a held-stance code) and quote the beat in the row's last column.
- `[ASKED]` replaces `[AI]` only on the realm token the author set; the stratum token stays `[AI]`.
