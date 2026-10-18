---
description: Force a full ledger audit and update across all story-memory folders -- reconciles every ledger against all accepted Areas written so far.
user-invocable: true
---

# `/force-ledger-audit`

Corresponds to canon command `[FORCE LEDGER AUDIT AND UPDATE]` (Command C-38). It has two modes (see
Modes): **Gate 2 mode**, the Post-Write Ledger Update that is mandatory at every Gate 2, and
**standalone mode**, a full reconciliation pass invoked on its own.

Scope note (Part 38): `.claude/story-memory/phase-section-part-chapter-area-specs/`
is NOT a ledger folder — this reconciliation never checks any spec in it (a Section Spec, a
Novel-Part Spec or a Chapter Spec) against a Part 37
schema and never regenerates the spec registry (its three tables) from the spec files, and
whether a spec's as-built sync actually happened is ALCA territory
(`guardrails/audit/guardrail-alca.md`). A spec file is nevertheless written by this same
continuity-checker instance where canon mandates that write by name: the Gate 2 as-built sync
(`spec-story-specification-law` Part 38 Rule 3.6.1; its write set is unchanged: the active Chapter
Spec and that spec's registry row; no Section Spec or Novel-Part Spec, and no Section or
Novel-Part registry row (its status or its Coverage cell), is written at Gate 2), the
destructive/rewind status rollback (Rule 7.2.1, with the COMPLETED rollback rule under Gate 2 and
destructive-command invocations below, which also returns a `COMPLETED` Novel-Part Spec or
Section Spec to `CONFIRMED`) and the restore re-sync of `/restore-archive` (the rows of the
restored Areas back to `WRITTEN`). Nothing else in this pass touches a spec file.

## Modes

| | Gate 2 mode | Standalone mode |
|---|---|---|
| When | At every Gate 2, as the Post-Write Ledger Update lane | Invoked on its own for a full reconciliation pass, and as the reconciliation pass of a destructive or rewind command or of `/restore-archive` |
| Reads | Only the new Area, the entities it names, the Area window, the Current Position block and the Area's row of the calendar ledger, and the active Chapter Spec | Every `ledger-*` folder and every written Area (never `_archive`) |
| Agents | One scoped **continuity-checker** instance | One **continuity-checker** per ledger folder, in parallel |
| Steps | The Gate 2 mode steps below (create-file, state record, Section 10 row, Section 12, summary, calendar rows, spec sync) | Steps 1 to 5 below |
| Confirmation | The author's `[CONFIRM WRITE]` at Gate 1 is the confirmation; what was changed is reported after the write | Preview and confirm before any write (Step 5) |

## Preconditions

- See `.claude/guardrails/commands/guardrail-plan-then-auto-execution.md` for this
  command's Plan Mode → Auto Mode execution shape, default agent model/effort, mandatory
  parallelism, and progress-checkpoint relay.

## Plan Mode → Auto Mode

This command has no pre-work consultation step of its own — the read/verify/regenerate
passes (Steps 1–4) begin immediately with no author-facing questions, so Plan Mode is
trivial/immediate here. In standalone mode Steps 1–4 run in Auto Mode; the existing Step 5
preview-and-confirm remains that mode's one mandatory confirmation, and Auto Mode never waives it —
nothing is written before that preview is explicitly confirmed. In Gate 2 mode the author's
`[CONFIRM WRITE]` at Gate 1 is the confirmation (see Modes)
(`guardrails/commands/guardrail-plan-then-auto-execution.md`).

## Parallel orchestration

In standalone mode the read/verify passes (steps 1–2) must fan out as parallel **continuity-checker** agents,
one per `ledger-*` folder (each folder's entity files are independent of the others') — this
is a binding requirement under
`.claude/guardrails/commands/guardrail-plan-then-auto-execution.md`, not a convenience to
skip "for simplicity." All findings are collected into the single unified preview of step 5
— no agent writes anything before that preview is confirmed. Gate 2 mode is one scoped instance and
does not fan out; it runs in parallel with the audit and scorer lanes, as `/next-area` sets out.

## Sequence

Steps 1 to 5 are standalone mode; Gate 2 mode follows them.

1. Invoke **continuity-checker** to read every `.claude/story-memory/ledger-*/` folder and
   every written Area file under `projects/novel-starward-saga/` (never the `_archive` folder).
2. For each entity: verify Baseline (B) fields are unmodified and Living (L) fields reflect
   the latest accepted Area (`.claude/guardrails/ledger/guardrail-ledger-schema-law.md`). The
   `ledger-character-monster/` folder is one of the `ledger-*` folders read and verified here:
   a Kind and its Individuals, Threat Role and Survival Status current, a Kind's habitat mirrored in the
   location's `Monster Kinds Present` line.
3. Regenerate each folder's `_index.md` registry from its entity files. **The calendar ledger** (Part 41 Area 9, The calendar ledger) has no entity files: rebuild
   `ledger-worlds-calendar/_index.md` from the first line of each written `.md` (never `_archive`): the Area
   rows, the rollups (the Chapter, Novel-Part, Section and Phase rows) and the
   Current Position block, each date with its Phase Day. Check every line by the dating check of Part 41 Area 6,
   weekday included, and show these in the preview as findings, never as edits to an Area file: an Area with no
   date line or a line in the wrong form, a weekday the formula does not give, a date that runs backward without
   a lawful cause, and a rebuilt row that differs from the row now in the ledger. A step back at a planned
   `cut to another thread` Area is information. The Baseline tables (epoch, months, weekdays, fixed days, birth
   years and the planned windows) are not rebuilt.
4. If an Area introduced an entity type with no existing ledger folder, flag
   `NEW ENTITY TYPE — Part 37 schema not yet defined` and stop for explicit direction
   (`.claude/guardrails/ledger/guardrail-ledger-schema-law.md`) rather than inventing a folder.
5. Preview all proposed changes and ask for confirmation through `AskUserQuestion` with a
   Cancel option before writing them; the confirming answer names the scope in words (for
   example "Write 14 ledger changes in 6 folders"), as
   `guardrails/commands/guardrail-command-law.md` requires. Cancel ends the pass with nothing
   written.

### Gate 2 mode

The Post-Write Ledger Update of one Area (`guardrails/ledger/guardrail-ledger-update-law.md`), run
beside the audit and scorer lanes. It is one scoped instance and it does not fan out. It reads only the
new Area, the entities the Area names (their ledger files), the Area window, the Current Position block
and the Area's row of `ledger-worlds-calendar/_index.md` (Part 41 Area 9) and the active Chapter
Spec; it does not read the other ledger folders or the other written Areas, and it neither reads nor
writes a Section Spec or a Novel-Part Spec. Its steps:

1. **Create-file.** Create the ledger file of each entity the Area introduces that meets a Part 37
   creation threshold, in the Part 37 template, with its row in the folder's `_index.md`. The
   `AskUserQuestion` that Part 37 Threshold C-2 requires for an antagonistic first appearance is still
   put to the author, through the orchestrating command. A new Tier D person is written as a registry
   row exactly as the orchestrating command passes it. Each named item the Area wrote (Part 28 Rule
   20.8.1) is entered as a row of `ledger-named-items/_index.md` (Part 37 Threshold O-4), as
   the orchestrating command passes it; the row points at the item's home ledger entry and never copies
   its values. Each named document and each named agreement, treaty or accord the Area wrote is entered as a row of
   `ledger-society-information/_index.md` (Part 28 Rule 20.8.7; Part 37 Area 3.4), an agreement's row
   pointing at its file in `ledger-people-society-affiliation/`. Each Named Move the Area wrote is entered as a row of
   `ledger-named-moves/_index.md` (Part 37 Threshold O-5; Part 6 Rule 6.5) and, in the same
   pass, in the Named Moves registry of each person who uses it, the row and the entry pointing at each other.
   Each monster Kind the Area first described is entered as a row of the Kind Registry of
   `ledger-character-monster/_index.md` carrying its tier (Part 37 Threshold M-1), and each Tier C or Tier D monster it
   introduced as a short entry or a row (Threshold M-2), as the orchestrating command passes the checked
   `MONSTERS (new in this unit)` list, at the tier the Area gave it; an ability the Area named is entered in
   the Named-Move register and in the monster's entry, each pointing at the other (Part 40 Rule 40.4.1.6).
   No monster is promoted here, and no sentient monster or Tier A or B monster Individual or Kind is created: the
   author builds those (`/new-character <name> monster`).
2. **State record.** Update the Living fields of each entity the Area changed, including the Current
   Condition of every character it affected, and the Substance Introduction Register when the Area
   introduces an energy substance state to the reader.
3. **Section 10 row.** Add the Canon Events Log row for the Area to each entity it changed.
4. **Section 12.** Append the drift entry for each behavioral drift the Area executed, and edit
   Section 11 where the drift is Permanent (Part 39 Areas 41 and 42). Section 11.3a: open the
   block if it is absent, and write the Area reference for each owed beat the Area showed
   (Part 39 Rule 39.41.5.2).
5. **Summary.** Enrich the narrative summary of each changed entity until the file passes the test
   "could I write the next scene using only this ledger file?"
6. **Calendar rows** (Part 41 Area 9; Part 37 Threshold D-1).
   Write the Area's dating into `ledger-worlds-calendar/_index.md` from the first line of the written `.md`
   and the checked `CALENDAR (this unit)` block as the orchestrating command passes it: the Area's row
   (its date and Phase Day from the date line), the rollups up the Chapter, Novel-Part,
   Section and Phase rows, and the Current Position block.
7. **Spec sync.** Perform the Part 38 as-built sync described below; its as-built in-story time mirrors the
   date line, and the calendar ledger owns the recorded date.

No preview is shown before the write: the author's `[CONFIRM WRITE]` at Gate 1 is the confirmation and
already covers this update. When the instance returns, the orchestrating command reports what was done
(files created, rows added, fields changed). An Area that introduces an entity type with no ledger folder
stops this instance as in Step 4.

**Gate 2 and destructive-command invocations.** When this command runs as the Gate 2
Post-Write Ledger Update, the same instance also performs the mandatory Part 38 as-built
sync on the active Chapter Spec file — Area status to `WRITTEN`, variance notes,
the moves of items from open to settled in the Audit and Settlement Notes section, and the Chapter Spec's own status to `COMPLETED` when the last
Area row is written (`spec-story-specification-law` Rule 3.6.1,
`guardrails/ledger/guardrail-story-spec-law.md`). When it runs as a destructive or rewind
command's reconciliation pass (`/rewind-to`, `/reset-chapter`, `/reset-phase`, and Step 2 of `/redraft-area` and
`/redraft-chapter`), it performs that command's per-Area status rollback instead (Rule
7.2.1); the closing reconciliation of a redraft performs no rollback. The same pass rolls the calendar
ledger back (Part 41 Area 9, resets and rewinds): the Area rows
of the archived or deleted Areas are removed, the Chapter, Novel-Part, Section and Phase rows are recomputed from the rows that remain, and the
Current Position block is rewritten from the last surviving Area, with nothing read from `_archive`; a
Section whose spec returns from `COMPLETED` to `CONFIRMED` is reopened there (its Section row Status
`OPEN`); the Baseline tables are not touched. The rollback carries the
`COMPLETED` rule (Part 38 Rule 9.8.1): a `COMPLETED` Chapter Spec whose rows roll back returns to
`CONFIRMED`; a `COMPLETED` Novel-Part Spec returns to `CONFIRMED` when any Chapter Spec of it is no
longer `COMPLETED`, and a `COMPLETED` Section Spec likewise when any Novel-Part Spec of it is no longer
`COMPLETED`. Only statuses, stamps and a variance note recording the rollback are changed; the
completion text of each spec is kept as history, no plan content is touched, and the registry rows
of the specs changed are updated to match, their Status and their Coverage cells. The Coverage cells
of the Section and Novel-Part rows are refreshed here because a reset or rewind rollback is one of
the three events that refresh them, the other two being the spec's own confirm and any completion
write step (a child's included); Gate 2 never refreshes them (Part 38 Rules 1.2.2, 10.1.2 and
11.1.2). When it runs as the reconciliation pass of `/restore-archive`, it does the reverse for
the restored Areas: their rows go back to `WRITTEN` with a variance note recording the restore, and
the Status and Coverage of the Chapter Spec rows are refreshed; their calendar rows are rebuilt from the
first line of each restored `.md`, and the Current Position block is recomputed (Part 41 Area 9). A restore is none of the three
events, so the Coverage cells of the Section and Novel-Part rows stay as stored until the next one
of them, and no Novel-Part Spec or Section Spec is made `COMPLETED` by it. The Gate 2 sync is part
of the update that `[CONFIRM WRITE]` confirmed; the rollback and the restore re-sync are part of the
step 5 preview set of the standalone-mode run and are confirm-gated with everything else; a
standalone reconciliation invocation performs none of these as routine. Two exceptions, each part of its step 5 preview
and written only on the confirmation. First, when spec rows say `WRITTEN` for an Area whose file
is absent from `projects/novel-starward-saga/` (outside `_archive`) — the *moved, not
reconciled* state a destructive or rewind command leaves when its reconciliation was declined
or stopped — the standalone run offers the Part 38 Rule 7.2.1 rollback for those rows, with the
`COMPLETED` rule above. Second, when a
written Area has a spec row that is not `WRITTEN`, or ledger rows that are missing — the
incomplete Gate 2 that `/status` lists as `incomplete Gate 2 at <ref>` (Part 38 Rule 6.2.1) —
the standalone run performs the Rule 3.6.1 sync for that Area; the missing ledger rows are
written by the ordinary reconciliation of Steps 1 to 3.

## Failure/abort

Never write ledger changes without a confirmation: the preview and confirm step above in standalone
mode, the author's `[CONFIRM WRITE]` in Gate 2 mode.
