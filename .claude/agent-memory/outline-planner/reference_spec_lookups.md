---
name: reference-spec-lookups
description: Read caps and chunk offsets, where spec vocabularies live, calendar and flashback rules, whole-mode band numbers, completion-prep checks
metadata:
  type: reference
---

Line numbers drift: re-verify before citing.

**Reading mechanics.** Read caps at 256 KB and 25K tokens per call.
- Part 38 `spec-story-specification-law/SKILL.md` is about 1,440 lines: chunks of 100 to 130 lines; Areas 9, 10, 11 start near lines 701, 951, 1198.
- Part 30 (`narration-novel-macro-story-law`): Area 1 to about line 414, Section 1 at about 425, Setups table about 828, Check #11 about 851. Part 41 is about 490 lines: 4 chunks.
- Hero ledgers run 800 to 1,270 lines: never read whole. Grep `\[IMMUTABLE\]`, `\[SIGNATURE\]`, `^- \`B39-L0[27]-`, `Novel-Part 1`; read Sections 1, 7 (open items), 9, 10, 11.2 to 11.7, 12 to 14.
- Specs of 700+ lines: chunks of about 125 lines. Skills with huge table lines (Parts 3, 6): narrow offsets. Single-line draft paragraphs: Grep -o with `.{0,60}term.{0,60}`.
- Grep here has no look-around. To find an item or move name that is NOT italic or bold-italic, use `(^|[^*])Name([^*]|$)`; a zero count means every mention is wrapped.
- A checker's report that the coordinator mentions but does not paste lives in the session's `tasks/<agent>.output` file as one huge JSON line (its SubagentHandback call): Grep it for the heading word to get the line number, then Read that line alone with `offset`, `limit: 1`, `allow_large: true`. Never Grep the `tasks` directory itself.
- After pasting or paraphrasing any checker text into a spec note, grep the spec for the whole Tier D roster and the checker's echo names (they list working names in their own notes); a spec carries roles only.
- Two copies of one draft (scratchpad deliverable plus a repo temp copy) with no copy tool: Read the second file once (Edit needs it), apply every edit to both in the same turn, then compare line count, `^\|` count, `^- \*\*` count, heading count and one 20+ term alternation count. Short files: Write them whole to both paths. A stale second copy: compare its line count and the line numbers of 4 anchor notes (the first and last Audit notes, one Open note, one Settled note) with the master's pre-task state; if they match, replay each Edit with the same strings (an Edit that fails to match is the drift alarm; Read that line then). This beats rewriting a 900-line spec in chunks. Apply the master first, then the copy, and settle the final wording of a note before replaying it (replay the end state, not each intermediate step, where the old text is whole).

**Where vocabularies live.**
- Part 38 Rules 2.2.1 (sections 1 to 7), 2.3, 2.4, Area 2.2a, Rule 9.10.2 (nine note kinds, plain list).
- 49 novel elements: `narration-novel-thematic-law` 15.5. CDL-2 categories: `narration-content-density-law`, written in capitals. Emotional-line states: Part 26 Area 16.1 (PIS grade only at 3 or more).
- Pillars: Part 30 1.6. Date line and weekday names: Part 41 Rule 41.5.1.1 and Area 3 (Phase Day 1 is Orvil; weekday = ((PD+1) mod 7)+1).
- Move-name checks: Part 6 Rule 6.2 plus the originality flag. Behavioral Plan: grep `B39-L..` codes in the hero file; N39-3; Check #20 element 20-11.
- Label trap: Part 28 is `narration-novel-creative-flexibility-law`; Part 29 is `narration-dialogue-and-social-interaction-law`.

**Calendar.** A flashback may be dated before the Chapter, Section or Phase window (Part 41 Rules 41.5.4.1, 41.6.1.3; Kind `flashback`, the clock does not move, Phase Day -k = Year 1246, Ulenor, Day 27-k). A step back in date is lawful only at flashback or `cut to another thread` Areas. Flashback form: Part 36 Area 27.2 and 27.8.

**Whole-mode numbers.** Block 55 to 60 percent of its size target; up to 72 percent with a named `Budget stretch` (Rules 2.3.9, 2.3.10); total 0.55T to 0.72T. A changed Chapter size T needs a light variance on the Novel-Part entry's word budget (Rule 11.3.7). Rule 2.4.12: a visible break before each scene and at each POV change.

**Completion-prep checks (/next-chapter step 1).** Closure check; Rule 3.7.1 questions with Recommended picks; drafted completion text; upward notes top-down. Repeat checks: grep ledgers and spec notes for words changed by a rewrite ("jest" also matches "Majesty"); grep written Areas for relation words the plan assumes; compare the variance notes on both parents; say "hearing ended", not "matter closed"; recommend naming an unnamed person.
