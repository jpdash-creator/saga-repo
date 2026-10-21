---
name: draft-self-checks
description: Checks to run on every first draft before the guard search, the count and the hand-off
metadata:
  type: feedback
---

**Size.** First drafts run about 25 percent over the cap, or under it for a lean scene. Draft each beat at its planned size, cut description and never speech, never pad. A short draft is enriched by rendering registered codes and sensory anchors, never by restating (Vitality Sin 3). Before a revision that adds beats, list the adds and the cuts with word counts. Recount after every edit pass.

**Anchors.** Re-read the Area block's Scene anchors line by line against the draft, in the spec's order; add a missed one.

**Repetition (the author flags it every time).** Grep -o a tally of the verbs and nouns the scene leans on (came/come, went, door, level, hand, line, put, flags) and vary with plain synonyms; Grep the earlier Areas on disk for repeated figures and openers; stock shapes ("the way a", "as at a", "for some time", "would not wait", "strong man"); crutch watchlist (suddenly, slowly, very, just, quite, somehow, seemed to, began to, started to, for a moment); never three same-mode paragraphs in a row; vary closers (act, sound, image, speech); a simile frame once; no verb, halt, same verb build. A heavy word reserved for one job (weight, heat) carries no other.

**Double meanings to Grep.** turn, hold, set, put, saw, rest, still, open, low, last, close, line, flags, stroke, hand, floor, walk, grain, plain, sill, wound, range, press, round, whole, slip; also rank (level and smell), level (realm and even), line (stripe, row, spoken line, list entry), pace (speed and step), sense (power and judgment), window (opening and chance), hands (workers and body), reach (arm and sense), stand (idiom "stand to my account").

**Substring traps in the banned-word grep.** thumb and thumbnail (hum), tail, horn inside a registered name (Thornweft), human; swap the host word. Crutch words that slip in: very, quite, slowly, began to, beginning to. Pick a compass direction once and keep every light and left-right word consistent with it.

**POV.** Two same-gender actors: open the paragraph with the name or role. Deep POV never labels the POV person by title ("the king"). A second hero in the first hero's POV is seen from outside (the act, never "felt"). Vary "X was Name" introductions.

**Dialogue.** No paragraph is a bare quote (Grep `^\*"[^"]*"\*$`). Adjacent quotes from two speakers carry a tag or beat at the speaker change. One name per sentence; one new proper name per sentence with its picture. Vary tags (Grep `said|asked`; never five in a row).

**Habit clauses.** "As he did before anything new" states a registration: show the act, cut the clause. Render each Tier D code from its catalog text, not memory. Grep before hand-off: `\bas (he|she|they|it) (did|always|read|took|held|breathed|said|held out)|every (afternoon|morning|day|time)|as they always`; a whole Chapter drafted at pace carried about 15 (Chapter 007).

**Named-item short forms.** A lower-case roman short form of a registered item ("the red grip", "five grips") was a Gate 1 finding in Chapter 004. Grep the head noun of every named item and write the full italic name or a plain description ("leather cover"); never a plural of the name.

**One-job words met in Chapter 007.** board (floor planks, chalkboard, quest board: say floor for planks), level (cultivation Level, quest level, even, alongside), hold (qi, breath, opinion, grasp: "keep to it" for an opinion), cover and covered (the item, a roofed span, ground crossed). Grep each and give it one job per Area.

**Edit tool and blank lines.** An Edit that deletes a sentence at the very end of a paragraph (empty new_string) also swallows the newline after it, so the next paragraph fuses to the one above; give the Edit a non-empty replacement or re-Read the seam. Also Grep for hedge words ("I think", "perhaps") in a hero whose register bars them, and for registered words used as plain verbs (hold, level, step, edge, ring) before hand-off.

**Stage logic.** Read the plan's props, wind, clock and time words against the calendar row as a stage manager; report slips.
