---
name: reference-light-amendment-after-chat-rulings
description: Recipe for finishing a light amendment of a CONFIRMED Chapter Spec after author rulings given in chat (Chapter 007 v1.1, 2026-10-21): find what an interrupted pass deleted, restore and mark superseded notes, stale-status greps, Open notes for newly named persons
metadata:
  type: reference
---

**Find what an interrupted pass did.** The stale pre-confirm draft in `.claude/temp/<spec>-DRAFT.md` still holds the v1.0 note wording. Grep `Settled by default` (line numbers and count) and `quiet|silen|still` windows in both files: a missing hit shows an edited or deleted line. The interrupted pass had deleted the Settled-by-default note the ruling replaced, so it was restored word for word from the temp draft.

**Superseded Settled note (Rule 9.10.2).** Put the old note back in its place, add `SUPERSEDED on <date>, as to <scope>, by the author's ruling in the next note`, keep the first answer unchanged, and put the new Settled notes directly beneath it. A clause of the old note that the ruling does not touch (here the Hall 4 and Senior halls reading) stays as a planner's default, said in the SUPERSEDED note. Then: one Audit note with the first answer's reason and a second Audit note as the version changelog line; edit the section 7 intro ("a note that replaces an earlier one stands beneath it") and the Settled group heading; older Audit notes that count the old note stay as history.

**Newly named Tier D persons.** Each needs a 5.0a visibility row. Where the author gave no level, the row says "open item" and section 7 needs a matching Open note (grep body "open item" for a note that does not exist). Withdraw the Skipped pick that left them unnamed (keep the old words, add "withdrawn"), add a Names note with the scan (whole words, partial words, stems, near forms; zero hits outside the spec), extend the Tier D registration Open note, and keep body pointers to section 7 out.

**Registered-code swap, stale carriers to grep.** The Behavioral Plan code lines of every Area that used the location, the header stamp ("do not exist yet"), "Ledgers expected to change: the new place file", "the ledger text is owed" (Section 3 bullet and the 5.0b heading), Evolution Entry "owed" lines in Area 04, and the Open notes on the code, the voice scope and the ledger obligations. Verify each "written" claim in the files first (place file code block and version, location index rows, `azorion` and `azure-sky-kingdom` section 5.5 pointers, `max-pryce` Section 14, `varya` Section 7, `nine-halls` sections 6.1, 6.5 and the Depth Test). Resolve an Open note with a "Resolved <date>, a correction of record" suffix and turn its old proposal into past tense, so pointers such as "the first Open note" still hold. In the body write "Registered <date>" and leave "set by the author's ruling" to the Settled notes.

**Checks after the edits.** Non-empty line count (Grep `.` count) rises by exactly the number of added notes, the blank count stays, and the group heading line numbers shift only by the added notes. Grep contractions, "Section 7" and "Audit group" pointers (only the header status line and section 7 may carry them), and unitalicised named items.

**Why:** the Chapter 007 pass left the Behavioral Plans saying "Not yet registered" after the code was registered, and body lines saying a level was an open item with no Open note behind them.

**How to apply:** any post-confirm amendment that follows pre-draft ledger writes or a late author ruling in chat.
