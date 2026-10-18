---
name: feedback-chapter-spec-draft-checks
description: Checks that caught real errors while drafting a whole-mode Chapter Spec (fight ledgers, stub claims, scene seams, address conflicts)
metadata:
  type: feedback
---

**Recount paired fight Areas.** When one fight runs across two Area blocks, recompute the dead and wounded of each side after drafting both Engagement Ledgers: the first draft of Chapter 005 gave different casualty totals in the Purpose, the table and the Price line. Positions are `4 x (Level - 1) + 0/1/2/3` (Low, Mid, High, Peak); recompute every gap range from the band ends, and make sure the group counts add up (a company equals its anchor, leaders and ranks).

**Why:** Part 44 Check #23 compares the draft with the spec's ledger; a count that differs between two rows is a finding the author sees.

**How to apply:** after the last fight block is written, Grep each side's count words ("five", "two", "seven left") and read the table rows against the Price paid line.

**Open the file before saying what a ledger "reads".** A location file may have a Collective Behavior Code stub (`highgale`) or no block at all (`aerie-palace`; its code is recorded as pending in `aeries` Section 11.5). Say which, with the file named, in the Behavioral Plan and in the Open note.

**Why:** a wrong claim about a ledger block turns a blocking item into a false statement.

**Scene seams in a multi-viewpoint scene.** Two Area blocks of one scene need a join state that both sides can honour: if a clock moves (a pause, a skip), the Area that keeps the earlier clock must not claim an event that falls after the skip. Check the anchors' order against the Planned time skips line.

**Ledger beats the author's ruling only on established facts.** When the author supersedes ledger text (an address system, a working name), write the ruling in the spec as Settled, name every carrier file by name only in an Open note for the Gate 2 ledger step, and do not edit the ledger.

**Revising a draft after rulings arrive.** When the author overrides planner picks after the hand-off, withdraw each contradicted Skipped pick, turn the Open notes the rulings close into Settled notes (keep the first answer's source and say the planner's pick is withdrawn), then Grep the old noun and its topic words (rank word, survivor, "alive", the omitted fact) across every Area field, the Scene Map, the visibility table and sections 3 and 7. Re-check every "(section 7, Open)" pointer afterwards: a pointer to a note that was removed or never existed is the usual leftover.

**Read the new registration before editing around it.** A ledger registered the same day (a villain's Sections 1, 4 and 11) carried a belief ("nothing is left on the road"), a voice ruling and a kill state that changed three plan lines. Plan traces and clues so they fit the registered belief (name what the clearing could not remove), keep ledger status tags such as `[N-A]` out of the spec body (write "marked not applicable"), and split an anchor into marked beats when it would stack three registered dimensions.

**Late tier and stage rulings.** When the author re-tiers named people (seven Gale people to Tier D) or leaves a field unset (the stage of a Level), Grep "Tier C", "registered before drafting", "blocking" and the old registration phrases across the header, every Behavioral Plan, Debuts, the visibility table and the Open, Audit and Variance notes. Keep the first answer's note, add the Settled replacement beside it, and quote the entry's original words in the Variance note. An unset stage is a step range from the band ends (a Level spans positions 4(L-1) to 4(L-1)+3), never a stage by implication. A coordinator's position numbers may be 1-based (21 to 24 for Level 6); the gaps agree, so state the rule's numbers and flag the difference once. Cite no ledger line the author has left open in a Behavioral Plan, even when the ledger file still shows it.

**Post-confirm light annotation and parent variance notes.** When the coordinator brings the author's confirm and asks for the checker's record notes as a light annotation (section 7 plus a few named body lines) and for variance notes on the parents: write Section Spec first, then Novel-Part Spec, then the Chapter Spec, so the Chapter Spec never claims a note that is not there; match the parents' own group format (a group heading, a trigger note, one note per departure with date, trigger, original beside new, the author's answer); after removing Open notes, grep "(section 7, Open)", "(blocking)" and "not yet given" for dangling pointers and unfilled answers; fix a stale status line in place with a "corrected, a correction of record" label and quote the old reading once. A "none, by the author's ruling" status is true only for what the author ruled: Part 39 lets a Behavioral Plan cite a location code as Registered or none by the author's ruling, so a planner's-reading none goes in a Skipped note and is flagged to the coordinator as a possible Gate 1 reading. Leave the header alone when the brief limits the edit to section 7 and named lines, and report its stale lines (status tail, the N1 to N8 count) instead.

**Why:** the Chapter 005 annotation of 2026-10-18 touched three files in one run and each of these slips would have left a false or dangling statement in a confirmed spec.

**How to apply:** at any post-confirm annotation, before the hand-off, run the three greps above and list the untouched stale lines in the report.

**Tooling.** No Bash: compress CSV lookups with Grep `-o` and a narrowed regex (id, manual, seq, name, type, unlock), and read long ledger files in slices of about 90 to 120 lines. A broad case-insensitive name scan returns noise from short surnames; scan whole words (`\b`) and keep short names in a separate pass.

**Edit-tool traps in a cleanup lane (2026-10-18, spec clean-up after a light audit).** (1) An Edit with an empty `new_string` that removes text at the end of a line also removes that line's break, so the blank line before the next heading is lost (it happened on the Section Spec carry-in line); keep the preceding words in `old_string` and `new_string`, and Grep the neighbour lines afterwards. (2) `section-1-spec.md` is CRLF (Grep `\r$` count equals the line count) while the Part Spec and Chapter Specs are LF; the Edit tool keeps CRLF on inserted lines, so single-line edits and end-of-file appends are safe, and a count of `^` before and after shows a lost or gained line. (3) The coordinator's line numbers shift after the first edit and may come from another snapshot: re-locate each target by content (Grep `-o` with a 100-character window), count repeats, then `replace_all` for the identical Backfilled strings. (4) Removing paired code-fence lines: put the heading line in `old_string` to make it unique, and turn a closing fence that sits before a bullet into a blank line.

**Why:** the clean-up touched five spec files in one run; the lost blank line was caught only by comparing the `##` line numbers with the first read.

**How to apply:** after the first batch of edits, Grep the `^## ` and group-heading line numbers against the first read, and use the same Grep to confirm the final line count.
