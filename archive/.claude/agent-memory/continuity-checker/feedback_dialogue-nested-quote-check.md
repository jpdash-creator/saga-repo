---
name: dialogue-nested-quote-check
description: Check #5 (dialogue format) is not just "every span has *"..."* with a closing asterisk" — a second, easy-to-miss failure mode is a character quoting/reading another character's exact words inside their own spoken line without the required nested single quotes (Part 29 Rule 29.2.1.1a).
metadata:
  type: feedback
---

Rule 29.2.1.1a requires single quotes for speech-within-speech: when a character's own
*"..."* dialogue span contains a reporting clause ("she said to me," "he writes:") followed
immediately by another character's exact quoted words, those inner words need single quotes
inside the outer double-quote-italic frame — e.g. *"He writes: 'I have set the rest of it
down...'"* not *"He writes: I have set the rest of it down..."*.

**Why this is easy to miss:** a narrow re-scan after fixing one specific instance (e.g. a
missing closing asterisk) checks for that same error class and reports "found none" — but a
nested-quote violation is a structurally different defect (correctly paired outer asterisks
and quotes, wrong inner punctuation) that a closing-asterisk-focused re-scan will not catch.
Caught exactly this in Prose 2 ("The Two Hands of the Morning") on a full fresh Check #5
pass after a prior audit's narrow fix-verification had already cleared the same span.

**How to tell it applies:** the outer dialogue span contains an internal framing clause
attributing the following words to someone other than the current speaker (patterns like
"X said," "X writes:", "X told me") followed by that other person's exact words, still
inside the same *"..."* span. A span that is simply reading a document's text aloud with no
internal framing clause (no "he writes:"/"she said" inside the quotation itself) is NOT this
case — that is ordinary direct speech and does not need nesting.

**How to apply:** when running Check #5, don't stop at "are all spans double-quoted and
italicized with matched asterisks" — also scan every span's *content* for an internal
reporting-clause-plus-quote pattern and verify single-quote nesting there.
