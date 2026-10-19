---
name: reference-gate2-sync-precedent
description: How a whole-mode Chapter's Gate 2 spec sync and completion write was done for Chapters 004 and 005 (version rule, parent notes, Coverage basis, group shape, tool traps)
metadata:
  type: reference
---

**Version rule (checked 2026-10-19).** Part 38 has no version rule for the as-built sync. Chapter Specs 001 to 004 all kept their version at COMPLETED (v1.1, v1.1, v1.2, v1.0); a version moves at a confirm or at a plan-content revise. Variance-only notes on a parent say "no version is bumped"; only Last Updated moves (the header line and the registry row).

**Coverage cells.** Rule 1.2.2 and the story-spec guardrail say the Section and Novel-Part Coverage is refreshed at a completion write step and "never at Gate 2"; the Chapter 004 lane left it to `/next-chapter` step 3. Rule 3.6.1's whole-Chapter paragraph makes the whole-Chapter Gate 2 also the completion write, and the coordinator ruled (2026-10-19) to refresh at Gate 2 and cite Rule 3.6.1 with Rule 1.2.2 as the basis in the notes, never the author's standing instruction.

**Write order.** Section Spec note group, then Novel-Part Spec, then the Chapter Spec (so it claims no note that is not there), then the registry rows (Chapter row, the two Coverage cells, the registry header date). Parent group shape: a heading line "Variance of <date> (Chapter NNN, <title>, as built: ...)", a trigger note, one information note per item that touches what the entry fixes (closing beat, key events, on the page; a Novel-Part word-budget note), one Audit note on threads and locks as built. Tier D names stay out of the parents (roles only); the Chapter Spec holds them.

**Chapter Spec sync shape (mirror Chapter 004).** Header lines 4 to 6 and the New named things line; Area status x6; one stamp clause on each Planted here line; Fired cells stay the Chapter ref, with narrow renderings named in one Audit note; Section 6 (Final Variance Summary with D1 to Dn, Reader now knows by Area plus numbered seeds, digest, Completion answers "not yet asked" with the item list for `/next-chapter`); a last group "As-built sync at the Gate 2" with Audit, D-notes (Planned / Written), Settled and Deferred, Name flips (Chapter label locked-at-Gate-1, in-world names locked-at-Gate-2, Area titles stay proposed), Open updates, and one note "plan text replaced by the written value". Replace the planned wording in a block only for definite divergences, and keep the planned value in the D-note.

**Lane facts.** The ledger lane (2b) runs in parallel: claim no ledger or calendar state (a whole-word scan of the new Tier D names finds no hit until it writes). Word figures come from the Maker's hand-off (script `measure`); say the lane ran no script.

**Tool traps.** Grep `glob` splits on spaces: no spaces inside a brace glob (use `**/*Walls.*`, not the file name). A 2,600-character line replaces cleanly with one full-line `old_string` copied from the Read. Edit on the CRLF Section Spec keeps CRLF on multi-line inserts (489 of 489 lines after the append). `Grep -o` omits long lines: proofread an edited long line with Read, offset and limit 1.
