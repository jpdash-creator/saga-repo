---
description: Show a Section's in-story timeline from the spec chain and the calendar ledger -- the Section's calendar window, each Novel-Part's window and each Chapter's window, as dates plus Phase Day, with each spec's status, beside each Area's place, in-story time, recorded dates and planned time skips. Read-only.
argument-hint: "[section reference such as 1.2, default the current Section]"
user-invocable: true
---

# `/timeline`

Read-only view of when things happen in the story. The command has no command code. It lays out
the in-story dates of one Section, Novel-Part by Novel-Part, Chapter by Chapter and Area by Area, so
the order of events, the gaps between Areas and the planned time skips can be seen without opening
every spec. It changes nothing.

## What is read

- **The specs of the Section**, found through the registry
  `.claude/story-memory/phase-section-part-chapter-area-specs/_index.md`, each kind from its
  own table (Section Specs, Novel-Part Specs, Chapter Specs); the registry row gives each spec's
  status.
  - From the **Section Spec**: the **Section calendar window** (block 0) and each Novel-Part's
    planned window (block 3).
  - From each **Novel-Part Spec**: the **Novel-Part calendar window** (block 0) and the calendar
    window of each Chapter entry (block 2).
  - From each **Chapter Spec**: the Chapter's **Calendar Window** line, and for each Area block the
    **Place, in-story time, weather and light** line (day or day range, time of day, time since the
    previous Area, ages where age matters), the **Planned time skips** line, the **Opening type**
    when it is a time jump or a flashback, memory, dream or vision, and the Area row status (Part 38
    Rules 2.4.8, 2.4.9 and 2.4.10).
- **The Section's calendar window in Part 30** (`narration-novel-macro-story-law`, §1.3.2a, the
  Section-by-Section Time Allocation Map), read for comparison: the anchor length and its
  plus-or-minus two-month latitude.
- **The calendar ledger** (`.claude/story-memory/ledger-worlds-calendar/_index.md`; Part 41 Area 9, The calendar ledger): the recorded dates of the Section (its Area,
  Chapter and Novel-Part rows), the story clock (the Current Position block)
  and the planned Section window, each date with its Phase Day. Read beside the plan, so that what was
  planned and what was written sit side by side. Every window in the specs is written as dates plus Phase
  Day (Part 41 Area 4).

A date in a spec is a plan until its Area is written. For a written Area the recorded date is the calendar ledger's,
and the Chapter Spec's as-built value mirrors it (Part 38 Rule 3.6.1 item 2; on a difference the ledger
stands); an Area not yet written is shown as planned. The Section
Spec's and the Novel-Part Spec's windows are plan values: Gate 2 writes only the Chapter Spec, so
they are not rewritten when an Area is written. A spec never establishes a fact: Locked Canon is
above the ledger, and the ledger is above the spec chain (Part 38 Rules 1.3.1 and 1.3.2).

## How the windows nest

The windows sit one inside another: the Section window, inside it each Novel-Part window, inside
that each Chapter window, then the Areas. The Section window is the Part 30 anchor
duration or a chosen value inside the plus-or-minus two-month latitude that §1.3.2a gives it,
and the Phase total stays at exactly nine years (Part 30 §1.3.2a; Part 38 Rules 9.3.1 and 10.3.1). After a
Chapter Spec is confirmed, its Chapter header governs the writing; the Novel-Part Spec's entry stays
the plan baseline (Part 38 Rule 9.3.2), so the two can differ, and a difference is shown, not
judged.

## Sequence

1. Take the Section from the argument, a reference such as `1.2` (Phase, Section). With none, use the
   Section of the current position, found as `/status` finds it (from disk, with the active Section
   Spec taken when no Area is written yet).
2. Read the registry, the Section Spec, every Novel-Part Spec of the Section, every Chapter Spec of
   the Section and the Part 30 window in one parallel batch. A Novel-Part with no Novel-Part Spec is
   shown with the window from the Section Spec's entry and marked "planned, no Novel-Part Spec". A
   Chapter with no Chapter Spec is shown with the window from its Novel-Part Spec entry, marked
   "planned, no Chapter Spec", and its Area rows are left blank.
3. Print, in story order:
   - the **Section** line: Section Spec reference and status, the Section's calendar window, and the
     Part 30 anchor and latitude beside it;
   - for each **Novel-Part**, its line: Novel-Part Spec reference and status, and its calendar window;
   - under each Novel-Part, each **Chapter** in story order: Chapter Spec reference and status, and
     the Chapter's Calendar Window, then one row per Area with the Area (reference and name), Place,
     in-story time, time since the previous Area, planned time skips and Area row status.
   Each spec's status is the spec status from the registry (`DRAFT`, `CONFIRMED`,
   `AMENDED-PENDING-RECONFIRM`, `COMPLETED`, `RETIRED`), not the Area row status.
4. After the tables, print these notes, each only where it applies. They are information for the
   author and never block or fail anything:
   - an Area whose in-story time is empty or open (an open item in the Audit and Settlement Notes of its Chapter Spec);
   - an Area dated earlier than the Area before it, where its Opening type is not a flashback,
     memory, dream or vision (a step back at a planned `cut to another thread` Area is shown as
     information, Part 41 Area 6);
   - a recorded date, in the calendar ledger, that runs backward from the date before it with no lawful cause
     (Part 41 Area 6, rules R1 and R2), and a written Area that has no row in the calendar ledger or a
     written Area whose first line is not a date line (found by reading the first line of each written
     `.md` of the Section, never `_archive`; `/force-ledger-audit` rebuilds the rows);
   - a date or day range that lies outside the Chapter's Calendar Window;
   - a Chapter window that lies outside its Novel-Part window, a Novel-Part window that lies
     outside the Section window, and a Section window that lies outside the Part 30 anchor and its
     two-month latitude (the nesting: Section, then Novel-Part, then Chapter, then Area);
   - a window that differs from the entry above it, for example a Chapter's Calendar Window that
     differs from its Novel-Part Spec entry, or a Novel-Part's window that differs from the Section
     Spec's entry for it. The note shows both windows and says which one governs the writing (the
     lower one, once confirmed), and names the variance note that records it in the log of each
     spec above it that holds one (a departure is noted on every spec above it, so a Chapter's
     window departure stands on the Novel-Part Spec and on the Section Spec; Part 38 Rule 9.4.5).

## Related

`/chapter-spec show`, `/part-spec show` and `/section-spec show` render one spec whole. `/threads`
lists open setups and cliffhangers across all specs. `/status` reports the current position and the
chain's statuses.
