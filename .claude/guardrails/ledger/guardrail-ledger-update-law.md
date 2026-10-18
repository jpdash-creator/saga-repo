# Guardrail: Ledger Update Law

**Source:** this guardrail (the ledger layer's update law; Part 37 owns the schema) · Canon v10.0
**Applies to:** Continuity Checker (executes it); Area Maker / Outline Planner (must not skip triggering it)

## The rule

Ledgers are living canon records, not planning notes. **No prose may be written without a
Pre-Write Ledger Check. No prose may be accepted into canon without a Post-Write Ledger
Update.** Both are mandatory, every single time, with no exception for "minor" Areas.

- **Pre-Write Ledger Check**: read the relevant `.claude/story-memory/ledger-*/` entries
  *before* drafting, including the Step 2.5 Power Ceiling / Permitted-Forbidden Realm
  Vocabulary statement (Part 3 Rule 1.7) — know what's allowed to appear before writing it.
  Every character who appears is read with their Current Condition (Part 37 Section 13, or the
  Current Condition cell of their registry row), so a wound, a state of mind or a limit carried
  from an earlier Area is not lost.
  The check also refuses a first appearance of a hero, a villain or a Tier A or Tier B person
  who has no baseline ledger record (Sections 1 to 10, built by `/new-character`) and points the
  author to that command. A Tier D person is excepted (Part 19 Rule 19.1.2.7), and so is a Tier C
  or Tier D person the drafting agent improvises in the Area: that person is registered at
  Gate 2 (Part 39 Rule 39.4.3.1, Route 2). The same refusal covers a Tier A or Tier B monster
  Individual or Kind and any sentient monster with no baseline record (`/new-character <name> monster`;
  Part 40 Rule 40.7.4.1); a Tier C or Tier D monster the drafting agent improvises, and a monster
  Kind it first describes, are registered at Gate 2 (Part 37 Thresholds M-1 and M-2). The refusal
  never puts the villain-classification question for a non-sentient monster: its hostility is not
  qualifying behavior for Threshold C-2 (Part 40 Rule 40.12.2.1). The check reads every monster
  the Area uses, Kind and Individual, with its Current Condition.
  The check also reads the Current Position block of `ledger-worlds-calendar/_index.md` and the row of the
  Area being written (Part 41, Area 9, The calendar ledger), so the
  Area's date line is set from the recorded story clock and never from memory. The block and the one row are
  read, not the whole file.
  The check also reads the Collective Behavior Code block of every collective and location whose members
  appear together, and a code that is `Not yet registered` is asked and registered before drafting, never
  at Gate 2 and never inside the prose (Part 39 Rule 39.23.1.5; `/create-chapter` and `/next-area` Step 0).
- **Post-Write Ledger Update** (executed via `/force-ledger-audit`): after any
  accepted Area that changes canon state — new entity creation (with the mandatory
  `AskUserQuestion` for antagonistic first appearances), and a **dual content mandate**:
  (a) state-record fields updated, and (b) narrative-summary enrichment sufficient that the
  test *"could I write the next scene using only this ledger file?"* passes. The same
  update cycle also performs the mandatory Part 38 spec as-built sync on the active chapter
  spec file — status flips, variance notes and settlement notes in the Audit and Settlement Notes section
  (`.claude/guardrails/ledger/guardrail-story-spec-law.md`). This sync is on the active Chapter Spec
  file only: it writes no
  Novel-Part Spec, no Section Spec and no Coverage cell of a Section or Novel-Part registry row
  (`.claude/guardrails/audit/guardrail-audit-gate-law.md`, Gate 2 step 6). The same update also writes the Current
  Condition (Part 37 Section 13, or the registry-row cell) of every character the Area
  affected, whoever caused the change.
  The same update fills the Substance Introduction Register in
  `ledger-energy-relics-artifacts/_index.md` when an Area introduces an energy substance state
  to the reader for the first time (Part 11 Area 14.1), so the Pre-Write Ledger Check can read
  which states the reader has met.
  Each CSS-7 or higher event written to a ledger in that update is listed to the author with a
  prompt to run `/consequence-audit <character>` (Part 27 Area 18). The prompt is information,
  never a gate.

## Hard rules

- **No Stale Ledger State.** A ledger entry that hasn't been updated after a scene that
  changed it is itself a canon violation, not a deferred task.
- **Author Guidance Must Be Captured Immediately.** When the author gives
  explicit naming, register, or convention guidance in conversation (e.g. during a Decision
  Consultation Gate round), that guidance must be written into the relevant ledger file's
  exact field in the same Post-Write Ledger Update cycle it was given in. A field reading
  "Negotiable Canon, to be established in prose" is only valid when the author genuinely has
  not yet given guidance on it. If the author already gave guidance and it was not captured,
  that is itself an Incomplete Ledger Update (Major Violation, see below) the moment it is
  discovered — not a "will fix going forward" item — because it left the field open to
  autonomous invention that directly contradicts a decision the author had already made.
- **Open Cells Use Two Tokens.** A field that is not yet set is
  written `OPEN-AREA` (prose may establish it) or `OPEN-AUTHOR` (only the author sets it),
  with an optional Due by note (Part 37 Area 5). The Post-Write Ledger Update replaces a
  token with the value when an Area or a ruling sets it, and keeps the Scene-Ready and
  Stoppers columns of the cast registries current (Part 37 Area 2.11). The Pre-Write Ledger
  Check lists any open field the Area needs and raises each `OPEN-AUTHOR` one, and any Due
  by that has passed, to the author as a question; it never writes a value for an
  `OPEN-AUTHOR` field. These flags inform; they never block a scene that the confirmed
  Chapter Spec requires.
- **Ledger Supersedes Memory.** If conversational context and the ledger file disagree,
  the ledger file is right — re-read it rather than trusting what a prior turn implied.
- **Incomplete Ledger Update** is a Major Violation from the very first occurrence once the
  obligation was named at Gate 1 (not a "warn once, then enforce" rule).
- **Completeness Requirement.** The Area is formed first and the
  ledger entry is made at Gate 2. A character, faction or location that exists in an accepted
  Area and meets its Part 37 Area 1 threshold must have its ledger entry once Gate 2 has
  run, at the level its tier or threshold calls for (a Tier D person is a row in the
  side-character index, not a file). The drafting agent is free to create people in the
  Area with no prior ledger entry; that freedom is where Tier D and many Tier C people
  live. A name that is only mentioned (a character named but not present, a place named but
  not described) does not meet the threshold and needs no entry (Part 37 Thresholds C-1 and
  L-1). A person or place that meets its threshold and has no entry after Gate 2 is a canon
  violation: the entry must exist, even if thin, not be deferred indefinitely.
- **Named items are entered at Gate 2.** A named item
  (Part 28 Rule 20.8.1) has no mention-in-passing exception: every named item written into a
  confirmed and written Area is entered as a row of `ledger-named-items/_index.md`
  by the same Post-Write Ledger Update (Part 37 Threshold O-4, schema Area 3.8). The row points
  at the item's home ledger entry and never copies its values. A named item with no row after
  Gate 2 is the same canon violation as a person or place with no entry. The Pre-Write Ledger
  Check reads the register for every item the Area will use. A Named Relic, Named Artifact,
  formation array and energy cache are named items too:
  each also gets its row here, with its descriptive entry in `ledger-energy-relics-artifacts`.
- **Named documents and agreements are entered at Gate 2** (Part 28 Rule 20.8.7, Part 37 Area 3.4). Every named document (a map, letter, charter, decree,
  codex or record) and every named agreement, treaty or accord written into a confirmed and written
  Area is entered as a row of `ledger-society-information/_index.md` by the same Post-Write Ledger
  Update, with no mention-in-passing exception. The row of an agreement points at its file in
  `ledger-people-society-affiliation/`, which owns its terms. A named document is never entered in the
  named-item register.
- **Named Moves are entered twice at Gate 2.** Every Named
  Move written into a confirmed and written Area (or set in a ledger by the author) is entered as a
  row of `ledger-named-moves/_index.md` (Part 37 Threshold O-5, schema Area 3.9; Part 6
  Rule 6.5) and, in the same pass, in the Named Moves registry of each person who uses it (Section 3
  of the hero, villain or side-character ledger), the row and the entry each pointing at the other.
  There is no mention-in-passing exception. The entry owns every value of the move and the register
  holds none. A move with a row but no entry for a known user, or an entry with no row, is the same
  canon violation as a missing person or place entry. The Pre-Write Ledger Check reads the register
  for every move the Area will use.
- **The Manual Ledger is written at Gate 2 for what prose writes** (Part 42 Rules 42.12.5.1 and 42.11.8.1; Part 37 Threshold O-6,
  schema Area 3.12). When an Area first writes the name of a manual-borne move, the same Post-Write Ledger Update enters
  that move as a full row of `ledger-named-moves/_index.md` and sets its `first_area` in the CSV row of the Manual Ledger;
  when an Area first writes a manual title, the update enters a pointer row in `ledger-named-items/_index.md`; and the
  update keeps `character-kits.csv` and `characters.csv` as Part 42 Rule 42.11.8.1 states. The Manual Ledger rows themselves
  exist from the author's directive and need no prose. A rewind, redraft or reset that removes the Area restores the
  CSV cells by the rollback of Part 42 Rule 42.10.10.3. `[SKIP WRITE]` writes nothing.
- **Monsters are entered at Gate 2.** Every monster Kind
  a confirmed and written Area first describes, and every Tier C and Tier D monster it introduces,
  is entered in `ledger-character-monster/` by the same Post-Write Ledger Update (Part 37
  Thresholds M-1 and M-2, schema Area 3.10; Part 40 Area 7): the Kind as a row of the Kind
  Registry carrying its tier (C or D; a Tier A or B Kind is built by the author), with a full Kind file
  made at its first Named Move, at Section scale or when it is sentient, whatever its tier (Part 40 Rule
  40.6.1.4), a Tier C monster as a short entry, a Tier D monster as one row. Every distinct ability the
  Area named (never a regular attack) is entered in the Named-Move register and in the entry, each
  pointing at the other (Part 40 Rules 40.4.1.3 and 40.4.1.6). The update keeps each monster's Current Condition, exact stage and
  Survival Status current, and mirrors the Kind's habitat in the location's `Monster Kinds Present`
  line. A Tier C or Tier D monster that has crossed one of the four triggers of Part 40 Rule 40.6.2.2
  is flagged to the author and is never promoted by the update. A Kind or a Tier C or Tier D monster
  that meets its threshold and has no entry after Gate 2 is the same canon violation as a person
  or place with no entry. No Kind is entered before its Area, except one the author sets in an
  interview (`/new-character`, `/update-ledger`) or one that a Tier C or Tier D Individual named by
  a Chapter Spec points at (Part 37 Threshold M-2), and a sentient monster is never entered without
  the author.
- **The calendar is written at Gate 2** (Part 41, Area 9, The calendar
  ledger; Part 37 Threshold D-1, schema Area 3.11). Every confirmed and written Area is recorded in
  `ledger-worlds-calendar/_index.md` by the same Post-Write Ledger Update, with no mention-in-passing
  exception: the Area row is created, the Chapter, Novel-Part, Section and Phase rows are rolled
  up from the rows beneath them, and the Current Position block is rewritten. The date line printed in the
  written file and the ledger agree both ways (`.claude/guardrails/audit/guardrail-alca.md`). A written Area with no calendar
  record after Gate 2 is the same canon violation as a person or place with no entry. `[SKIP WRITE]` writes
  nothing, so the calendar ledger, the files and the spec agree. The ledger records the dates and never
  copies spec content; the specs write the Area's dates as dates plus Phase Day and the ledger owns what was
  written (`.claude/guardrails/ledger/guardrail-story-spec-law.md`).

- **Evolution entries are written at Gate 2** (2026-10-06; Part 43, the Character Evolution Law; ledger section 'Evolution Entries'). The Post-Write Ledger Update writes a dated evolution entry (number, date, layer or code, what it was and becomes, Area, who ruled, reason) for every evolution ruled at Gate 1, in every character ledger, and never overwrites the base profile. The earlier limit on editing hero ledgers is lifted FOR EVOLUTION ENTRIES (the author lifted it 2026-10-06); other hero-ledger protections stay. Gate 2 presents every evolution, all tiers, with its recorded information. A reset removes entries back to a date the author names.

- **A Chapter built whole is updated in one batch, citing the Chapter reference only** (Amended 2026-10-07; `/create-chapter`,
  `/revise-chapter`). A whole-built Chapter has no Area files, so every rule above that says "Area" reads "Chapter"
  for it, and the Post-Write Ledger Update runs once for the Chapter as one batched update: entities and Current
  Conditions, named items, named documents and agreements, Named Moves (the register and each user's registry),
  monsters, evolution entries, the Manual Ledger cells, the calendar rows (one per date segment of the Chapter, with
  the rollups and the Current Position block), the Canon Events Log rows and the spec as-built sync. Every entry
  cites the Chapter reference `P.S.N.CCC` (for example `1.1.1.002`) and nothing finer: no Area-level and no
  scene-level code is written into a ledger for a whole-built Chapter. First Appearance fields, Named Move rows,
  Evolution Entries, calendar rows and scoring rows carry the Chapter reference. Retrieval is by grep on the
  Chapter reference. Area-level references (`P.S.N.CCC.AA`) stay valid for Area-built Chapters and for history. The
  pre-write read set for a whole-built Chapter reads the Current Position block and the open Chapter's row, and the
  previous Chapter in full. `[SKIP WRITE]` writes nothing.

## Escalation

If a Pre-Write Check or Post-Write Update can't be completed (e.g. ambiguous entity
classification), stop and ask rather than proceeding with a guessed ledger state.
