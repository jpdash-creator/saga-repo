---
description: List what the story has promised and not yet delivered, read from the spec chain -- the plan in the Section Spec and the Novel-Part Spec set beside what the Chapter Specs show happened -- setups planted and not paid off, cliffhangers and open questions not yet resolved, and threads carried between Chapters. Read-only.
user-invocable: true
---

# `/threads`

Read-only view of the story's open promises. The command has no command code. It reads the specs
of the chain and lists the setups planted and not yet paid off, the cliffhangers and open questions
not yet resolved, and the threads carried from one Chapter to the next, with the plan beside what
happened. It is the on-demand list across all specs; the Section-close report (Part 38 Rule 3.7.2)
gives the open-setup list for one Section at its close. It changes nothing.

## What is read

The registry
`.claude/story-memory/phase-section-part-chapter-area-specs/_index.md` holds three tables, one
for each kind of spec. The command reads each kind from its own table (the Section Specs table, the
Novel-Part Specs table and the Chapter Specs table; a row is never taken from another kind's table)
and then every spec file those tables name, across all Phases and Sections, in story order. Story
order is the order of the Ref numbers, compared number by number (`1.2` comes before `1.10`).

The **three linked guide registers** (Part 38 Rule 9.5.4), each read from its own spec:

- **The Section plan.** In each Section Spec, block 4, Threads, Setups and Payoffs: for each key, the
  Novel-Part that plants it, the Novel-Part it returns in and the Novel-Part that pays it, with the
  optional per-thread **thread-return stretch** note (default `unset`) (Part 38 Rule 10.3.4).
- **The Novel-Part plan.** In each Novel-Part Spec, block 3, Threads, Setups and Payoffs: for each
  key, the Chapter that plants it and the Chapter that pays it, with each Chapter entry's threads in
  and out and its linked setup keys (Part 38 Rules 11.3.2 and 11.3.6).
- **What happened.** In each Chapter Spec, per Area block: **Planted here** and **Carried or paid
  off here** (the setup and motif register that Part 36 Areas 21 to 23 read, Part 38 Rule 2.4.10),
  the **Closing type** with the Area it names as resolving a cliffhanger or an open question
  (Rule 2.4.5), and **Thread or storyline**. Per Chapter: **Threads Carried In**, **Threads Carried
  Out** and the chapter-grain open questions (read from the spec's Audit and Settlement Notes section).

The three registers are joined by shared **keys**: a Part 30 Setups-table row number, or a short
thread name. A setup in a Chapter Spec's Area fields is joined to its key by the key or short name
written with it, or by the linked setup keys of that Chapter's entry in its Novel-Part Spec when that
entry names it; an item that cannot be joined to a key is listed with its planting Area and no key,
never as an error. A setup is matched to its payoff by reference code: the planting Area names where
it pays off, and the paying Area names where it was planted.

Every plan line is a guide and a suggestion, never a block (Part 38 Rule 9.5.4). The story may plant
a setup somewhere else, pay it earlier or later, or drop it, and the author keeps the choice. An
entry in a spec is a plan until its Area is written (Rule 1.3.2). Only a setup that has actually
been planted, and is unpaid when a Chapter, Novel-Part or Section is completed, is put to the author,
and that happens at completion (Part 38 Rules 3.7.1, 9.7.2 and 9.7.3), never in this command.

## Sequence

1. Read the registry by kind and every spec file it names in one parallel batch. The Area row
   statuses are read from the Chapter Specs; the spec statuses come from the registry
   rows.
2. Print three lists, each in story order of the first place the item appears. They are information
   for the author and never block or fail anything, and they ask nothing:
   - **Setups, the plan beside what happened.** One line for each key: the Section plan (the
     Novel-Part that plants it and the one that pays it, where the Section Spec names them), the
     Novel-Part plan (the Chapter that plants it and the one that pays it, where the Novel-Part Spec
     names them), and then what happened: the planting Area and one of: paid off (the paying Area,
     written), payoff planned (the Area named, not yet written), carried (the Area that carries it
     on), or payoff open (an open item in the Audit and Settlement Notes). Where what happened sits where the plan suggested, say so. Where it
     differs, say it plainly and without a verdict: for example "the plan suggested Novel-Part 2, the
     story planted it in Novel-Part 1" or "the plan suggested payoff in Chapter 004, paid in Chapter
     006". A suggestion with nothing planted yet reads "suggested, not yet planted". An item the
     author dropped or moved, as a variance note on the Section Spec or the Novel-Part Spec records,
     is shown with that note.
     No waiting time is shown, no count of Chapters or Areas since planting, and no age: how long a
     setup may wait is the plan's decision, set by the Section and Novel-Part plan lines and by no
     figure (Part 36 Rule 23.2.5).
   - **Cliffhangers and open questions.** Each Area that closes as a cliffhanger or a question left
     open, with the Area that resolves it and whether that Area is written, or open (an open item in the Audit and Settlement Notes).
   - **Threads.** Each thread as the plan names it, then as the Chapters carry it: the Section Spec's
     line (where it returns and where it pays), the Novel-Part Spec's line, each Thread Carried Out
     of a Chapter and the Chapter that carries it in, and any thread carried out that no Chapter
     carries in yet. Beside each thread, its **thread-return stretch** note exactly as the Section
     Spec stores it, `unset` when none is set; nothing is worked out from the note here, and where it
     is `unset` nothing more is said about it (the Thread Return report of Part 36 Rule 26.4.4 is
     made when a Chapter opens and at Section close, not by this command).
3. Close with the items marked lapsed, each with its reason and the Chapter, Novel-Part or Section
   completion at which it was marked. An item is marked lapsed only on the author's answer at that
   completion (`/chapter-spec complete`, `/part-spec complete` or `/section-spec complete`, or
   `/next-chapter`, `/next-part` or `/next-section` as the boundary that reaches it; Part 38 Rules
   3.7.1, 9.7.2 and 9.7.3), and it is listed apart and not shown as open.

## Related

`/timeline` shows the in-story dates of a Section. `/find` searches the written Areas and the
ledgers. `/chapter-spec show`, `/part-spec show` and `/section-spec show` render one spec.
