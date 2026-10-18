---
description: Move the Area files of one archive folder back to their original places, then reconcile the ledgers, set the spec Area blocks back to WRITTEN and score the restored Areas again. Human-invocation only.
argument-hint: <date-time of the archive folder, YYYY-MM-DD_HHMM>
user-invocable: true
disable-model-invocation: true
---

# `/restore-archive`

The way back from `/rewind-to`, `/redraft-area` and `/redraft-chapter`, which move Area files to
`projects/novel-starward-saga/_archive/<date-time>/` and never delete them (Part 2 Rule 5.3.2a in
`narration-novel-book-structure-law` Area 5). The command has no command code. It takes one
archive folder, named by its `<date-time>` (`YYYY-MM-DD_HHMM`), puts that folder's file pairs
(`area-NN.docx` and `area-NN.md`) back at the paths they came from and makes the Areas canon
again. It lists paths under `_archive/` and never opens a file's text.

## Sequence

1. Resolve the folder. With no argument, or a name that matches no folder, list the archive
   folders with the first and last Area reference each holds (read from the file paths) and ask
   which one through `AskUserQuestion`. Then list the file pairs in that one folder; the
   destination of each is its path below the archive folder, under
   `projects/novel-starward-saga/`. If any destination already holds a file (an Area written
   forward since the archive), stop with nothing moved and name the taken paths: a restore never
   overwrites, so the newer Area has to be moved out of the way first (for example by running
   `/rewind-to` to the same target, which archives it into its own folder). Otherwise confirm
   through `AskUserQuestion` with a Cancel option; the confirming answer names the scope in
   words (for example "Restore 5 Areas from archive 2026-10-01_1435"), in the form
   `guardrails/commands/guardrail-command-law.md` sets for the destructive commands.
2. Move the pairs back, never overwriting a file and creating any missing folders. It is a
   plain file move with the shell's move command: no script is created and no Area file is
   written (Part 2 Rule 5.3.2a). Then set the modified time of each restored file to now, so that a
   chapter, phase or novel aggregate made while the files were in the archive is found stale
   (Rule 5.3.5 in `narration-novel-book-structure-law` Area 5).
3. Invoke **continuity-checker** to run `/force-ledger-audit` as the reconciliation pass, with
   the restored Areas treated as canon again, so that every ledger matches the text as it now
   stands. Living (L) fields that only the restored Areas established return; ledger rows and
   entity files that the archive marked `archived` or set to `pending redraft` return to their
   earlier state, and any the archive removed are listed in the preview for re-creation. The
   calendar ledger is rebuilt the same way (Part 41 Area 9, The calendar ledger): the Area rows
   and rollups of the restored Areas come back from the first line of each
   restored `.md`, each line checked by the dating check of Part 41 Area 6, and the Current
   Position block is recomputed from the last Area now written. The same pass re-syncs the spec:
   the Area blocks of the restored Areas go back to `WRITTEN` with a variance note recording the
   restore (name tags and reference stamps that Part 38 Rule 7.2.1 rolled back return with their
   blocks; the pacing and size target the spec records were never changed), each Chapter's
   status is re-derived from its blocks, and the affected Chapter Spec rows in
   `.claude/story-memory/phase-section-part-chapter-area-specs/_index.md` are refreshed (Status
   and Coverage). A restore is none of the three events that refresh the Section and Novel-Part Coverage cells (`/force-ledger-audit`, "Gate 2 and destructive-command invocations"; Part 38 Rules 1.2.2, 10.1.2 and 11.1.2), so those cells stay as stored; `/status` shows the live count meanwhile. A Chapter Spec that a rollback returned
   to `CONFIRMED` returns to `COMPLETED` only when this re-sync finds every one of its Area
   blocks terminal again, the same event that sets `COMPLETED` at Gate 2 (Part 38 Rule 9.7.2);
   its earlier completion text is kept as history and refreshed at the next completion. A
   Novel-Part Spec or Section Spec that a rollback returned to `CONFIRMED` stays `CONFIRMED`:
   this pass never marks one `COMPLETED`, because those are completed only on the author's yes
   (by the boundary command, or by `/part-spec complete` or `/section-spec complete`; Part 38
   Rule 9.7.3). Built-against stamps are left as they are (Part 38 Rule 9.2.3). A restored Area
   whose spec block no longer exists, or now plans something else because the plan was revised
   after the archive, is listed in the preview as a plan-versus-written difference for the
   author, and its block is not flipped silently. The reconciliation shows its preview and
   waits for confirmation (`/force-ledger-audit` Step 5).
4. Invoke **area-scorer** — launched together with Step 3, since the two write disjoint files —
   to score each restored Area again from its written file, one after another in story order.
   Each gets its per-Area row in the CDL-2 tracker
   (`.claude/story-memory/cdl2-density-tracking/`), and the Section running aggregate is
   recomputed.

## Failure/abort

Do not run without the confirming answer that names the archive folder and the Areas in it;
Cancel, or any other answer, ends the command with nothing changed. A destination that already
holds a file stops the command in Step 1, before anything moves.

After Step 2 the Areas are back in place. If the reconciliation preview is declined, or the
audit stops (for example at `NEW ENTITY TYPE`), that state is named *restored, not reconciled*:
run `/force-ledger-audit` to finish it. A standalone run finds a written Area whose spec block
is not `WRITTEN` and puts the spec sync for it in its preview.
