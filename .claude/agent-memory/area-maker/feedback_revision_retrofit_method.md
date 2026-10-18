---
name: revision-retrofit-method
description: How to revise, rewrite or insert into an existing Area or Chapter without drift
metadata:
  type: feedback
---

**Before a REVISE.** Read the Gate 1 session log of the audited draft first (`.claude/story-memory/session-log/<date>-...md`): it lists the exact findings; the coordinator's change list repeats only some.

**Insert, never rewrite.** Change only the paragraphs the plan names; copy the rest from the Read output. Prove it: one Grep per Area, pattern `^(?:para1|para2|...)$` (escape `.` `?` `*`; an optional group `( inserted sentence)?` for each touched paragraph), run on BOTH the written file and the staged file; both must return the paragraph count. Across the repo use `glob: "*.md"` (a brace glob with a comma fails).

**Tag attribution.** An inserted sentence between narration about man A and a bare `he said` makes "he" the wrong man: insert after the speech or at paragraph end, and open with the name.

**Dialogue-only rewrite.** Count the original first and budget (cap minus kept narration). Flowing speech runs about +10 percent in words and tags cost about 0.3 words per spoken word; convert inner counts and rule statements into speech instead of adding lines; use unattributed turns and action beats. List the narration sentences that point at a line ("who had the horse") before reshaping speech; change speech, not narration. A line must not repeat the narration beside it. Verify narration verbatim with one `Grep -o` of about 20 anchor sentences per Area (each prints once).

**Vocabulary pass on an accepted Area.** Before swapping a phrase, Grep `.claude/story-memory` for the old wording (ledgers quote the prose); never edit a ledger in the pass, list the lines for the Gate 2 ledger instance; keep words a ledger records as fact; mark figure-to-plain changes FIGURE so the author can revert that row alone.
