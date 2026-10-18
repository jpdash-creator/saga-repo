# Continuity Checker — Working Notes

Private, self-maintained notes for the continuity-checker agent only (not shared canon —
that lives in `.claude/story-memory/`, and never treat this file as a canon source either).
Use this file to record recurring drift patterns you keep catching, ledger schema quirks,
and audit edge cases worth remembering, so the same mistake doesn't need to be re-found
every session.

- [Grep word-count technique](reference_grep-word-count-technique.md) — Grep "count" mode counts matching lines, not matches; use offset+head_limit:1 binary search for exact word counts instead.
- [Azure Sky / Gale geography](project_azure-sky-gale-geography.md) — Gale Kingdom is EAST of Azure Sky across the Lyraen River, never west; check courier/travel direction against this.
- [Dialogue nested-quote check](feedback_dialogue-nested-quote-check.md) — Check #5 also requires scanning span contents for un-nested "X said/writes: ..." speech-within-speech, not just asterisk pairing.
