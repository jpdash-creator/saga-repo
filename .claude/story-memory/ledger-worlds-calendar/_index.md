# ledger-worlds-calendar — Ledger Index

**Ledger Domain:** World Systems — The Calendar and the Story Clock (the date of every Phase, Section, Novel-Part, Chapter and Area, in the Nine Suns calendar)
**Governed By:** `guardrails/ledger/guardrail-ledger-update-law.md`, Part 37 (Ledger Schema Law), Part 41 (Calendar Law)
**Template:** Part 37 Area 3.11 — Schema Template: Calendar Ledger
**Last Updated:** 2026-10-21
**Index Version:** 10.0
**Total Entries:** 28 (Phase rows: 1; Section rows: 1; Novel-Part rows: 1; Chapter rows: 7; Area-table rows: 18, of which 3 are the date-segment rows of the whole-built Chapter 1.1.1.002, 2 are the date-segment rows of the whole-built Chapter 1.1.1.003, 2 are the date-segment rows of the whole-built Chapter 1.1.1.004, 3 are the date-segment rows of the whole-built Chapter 1.1.1.005, 3 are the date-segment rows of the whole-built Chapter 1.1.1.006 and 1 is the date-segment row of the whole-built Chapter 1.1.1.007; the baseline tables below are not counted)

> **Purpose:** This folder is the one place that records when every Phase, Section, Novel-Part, Chapter and Area of the Starward Saga happens, as dates in the Nine Suns calendar. The author asked for a calendar ledger that records the time of every tier, kept as `_index.md` and kept simple; all five tiers are covered. The ledger holds three things: the calendar's baseline (the epoch, the months, the weekdays, the fixed days, the eight heroes' birth years and the planned Phase and Section windows), the recorded dates (one row per Area, rolled up to its Chapter, Novel-Part, Section and Phase), and the Current Position (the story clock). It is a register of dates and has no lore of its own.

> **Where the author's directive and the rule live:** the author's words are quoted in Part 41 (Area 1, Founding and scope, and Area 9, The calendar ledger) and in `.claude/guardrails/_index.md`. This index states the scope and the tables for the people who keep the ledger. Part 41 stands on any difference with this index, and a difference is a finding at the next ALCA pass for the author, never settled silently. Phase Day stays the stable key used by Part 30, the specs and the other ledgers: the calendar date is derived from it, and Part 30's Phase Day numbers, durations and ages are not changed.

> **Scope — what is here and what is not.**
> - The date of an Area is written first in the Area file itself, as the date line directly under the Area Title Block (Part 41 Area 5, The date line). This ledger records it after `[CONFIRM WRITE]` and does not replace it. The date line in each Area file and this ledger agree both ways (ALCA).
> - Only the Phase and Section windows are filled in before any Area is written, because they are a conversion of Part 30. The windows of a Novel-Part, a Chapter or an Area live in the specs and are not copied here (Part 38 Rules 1.3.2 and 1.4.2); this ledger records them only as written.
> - The hero ledgers are frozen and hold ages only, save for one added birthday line each in `varya.md` and `aegon.md` (the author: "Varya birthday is in month of Arvelle day 6, Aegon is Day 10 of Sorvelle - Record in Section and their ledgers"). The heroes' birth years are recorded here and nowhere else, and the two set birthdays are owned here.
> - What the calendar is, how the date line is written and how it is checked belong to Part 41 (Areas 2 to 8). This index holds the values for lookup.

> **How a date is written here.** `Y.M.D / PD N`: the Year, the month number, the day of the month, a slash, then the Phase Day. Example: `1247.3.27 / PD 86` is Year 1247, Sorevany, Day 27, which is Phase Day 86. "Day" is always the day of the month and never a Phase Day. A range is written first date, `to`, last date. A weekday is never stored in a recorded table: it is worked out from the formula under Weekdays. A month number appears only in a table of this ledger; in notes a month is written by its name. Month and weekday names are major names chosen by the author and immutable once chosen (Part 28 Area 3.4); they are set in roman in narration and notes, and only the date line in an Area is wholly italic.

> **Entry schema (Part 37 Area 3.11; the recorded tables follow Part 41 Rule 41.9.2.2).** Six tables. The B and L marks follow Part 37 Area 5: the baseline tables are B, and every recorded cell is L. The recorded tables sit each under its own heading that carries the words "Events Log", so that a reset empties them and leaves the baseline tables alone.
>
> | Table | One row is | Columns |
> |---|---|---|
> | Current Position (L) | the story clock; one row, replaced at every Gate 2 | Story clock (the latest present-time date); Last written Area; Its date and Phase Day; Open Chapter; Open Chapter's recorded window (First to Latest); Weekday of Ilovany, Day 1 this Year |
> | Phase (L) | one Phase | Ref; First; Latest |
> | Section (L) | one Section | Ref; First; Latest; Status (`OPEN` or `CLOSED`) |
> | Novel-Part (L) | one Novel-Part | Ref; First; Latest |
> | Chapter (L) | one Chapter | Ref; First; Latest |
> | Area (L) | one Area | Ref; First; Latest; Kind (`present` or `flashback`) |
>
> Refs: Phase `1`, Section `1.1`, Novel-Part `1.1.1`, Chapter `1.1.1.001`, Area `1.1.1.001.01`. First and Latest are the first and last day recorded in the unit. First and Latest of a Chapter, Novel-Part, Section and Phase roll up the `present` Area rows under it; a `flashback` Area row stays in the Area table and is left out of the rollups, because the story clock does not move at a flashback. A dream or vision carries the night it is dreamed and reads `present`. Section Status is `OPEN` from the Section's first written Area and `CLOSED` when Gate 2 confirms its closing Area. An Area's row carries its First and Latest day: the same day when the Area sits inside one day, and the first and last day when it runs across days (the date line in its file says the same, written first day, `to`, last day). A scene that opens in the last dark hour and runs on into a dawn takes the dawn's day, and its date line states that day only (Part 41 Rule 41.2.1.3a; the author: "Open in the last dark hour; one scoped Part 41 rule").

> **Update Protocol:** Per `guardrails/ledger/guardrail-ledger-update-law.md`, Part 37 Threshold D-1 and Part 41 Area 9 (The calendar ledger):
> - **New Row Trigger:** every Area confirmed and written is recorded at Gate 2, by the Post-Write Ledger Update after `[CONFIRM WRITE]`. The Area row is created; the Chapter, Novel-Part, Section and Phase rows are created or rolled up; the Current Position row is replaced; and a Section's Status in the Section table is set (`OPEN` at its first written Area, `CLOSED` at its closing Area). `[SKIP WRITE]` writes nothing. A date that exists only in a spec, or in a draft discarded by `[SKIP WRITE]`, is not entered (Part 38 Rule 1.3.2).
> - **Pre-Write Ledger Check:** the check reads the Current Position block and the open Chapter's row, never the whole file, so the next Area starts on the day the last one ended and carries the right weekday.
> - **One owner:** this ledger owns the recorded dates. The Chapter Spec's as-built in-story time mirrors it (Part 38 Rule 3.6.1 item 2), and on a difference with a spec the ledger stands (Part 38 Rule 1.3.1). A difference between this ledger and the date line in an Area file is a finding at the next ALCA pass, and `/force-ledger-audit` rebuilds the rows from the first line of each written Area `.md`.
> - **Rewind, redraft and reset:** when an Area is removed, its row is removed, and the rollups, the Section Status and the Current Position are recomputed from what remains. `/reset-story`, `/reset-ledgers` and `/hard-reset` empty the recorded tables, Section Status included, because each sits under an "Events Log" heading; the baseline tables, Planned windows included, hold no status and are left alone by the reset script.
> - **Housekeeping:** every Area row is kept, with the Current Position block as the short read. No archive folder exists, and no row count blocks an Area. To be revisited at the end of Phase 1.

> **Mandatory Update Triggers:**
> - An Area confirmed and written (Area row, rollups and Current Position)
> - A first Area in a new Chapter, Novel-Part, Section or Phase (the unit's row is created; a new Section row reads `OPEN`)
> - A Section's closing Area confirmed at Gate 2 (Section Status `CLOSED`; `section-spec complete` never sets it)
> - A flashback or memory (the Area's Kind reads `flashback`; the rollups skip it)
> - A rewind, redraft or reset that removes an Area
> - A birthday that an Area states (entered first in the birth-year table; Part 41 Area 8)
> - A Canon Amendment of a baseline value, on the author's word only

> **Marker Legend:** These markers appear in the entries of this ledger. Open cells otherwise carry `OPEN-AREA` or `OPEN-AUTHOR` (Part 37 Area 5).
> - `[ASKED]`: the author chose this value.
> - `[DERIVED]`: the drafter inferred this value from cited evidence and the author reviewed it in the digest without overriding it (Part 39 Rule 39.3.3.1); it is pending only when the entry also says flagged for author confirmation.
> - `[AUTHOR-PENDING]`: a question about this value has been raised and is not yet answered.
> - `[MARKED SLOT]`: a slot left empty on purpose until the author rules.
> - "flag, do not invent": when a scene needs the value, the prose may establish one small fact at a time under Part 28 Area 17, logged in this ledger and offered to the author as a draft value at the next Section close. A name or a major entity (Part 28 Area 20.4) goes to the author first, through the Decision Consultation Gate.

---

## Current Position — Events Log (one row, replaced at every Gate 2)

Read this first. The one row holds six fields: the story clock (the latest present-time date), the last Area written, its date and Phase Day, the open Chapter, the open Chapter's recorded window (First to Latest), and the weekday of Ilovany, Day 1 of the current Year, so that no one counts forward from Day One (the checker recomputes it at Gate 1). With no row, nothing is written yet: the story clock stands at Phase Day 1, Year 1247, Ilovany, Orvil, Day 1, the day the first Area opens on (a first Area that opens in the last dark hour and runs on into that day's dawn takes this date too, Part 41 Rule 41.2.1.3a), and no Area is named. Dates are written `Y.M.D / PD N`; the date of an Area that runs across days is written first day, `to`, last day. The story clock never moves backward; the date of the last written Area, and the open Chapter's window, may lie before it after a flashback or after a step back at a planned cut to another thread (Part 41 Rules 41.5.4.1 and 41.6.1.2), and the check reports such a step as information.

| Story clock | Last written Area | Its date and Phase Day | Open Chapter | Open Chapter's recorded window (First to Latest) | Weekday of Ilovany, Day 1 this Year |
|---|---|---|---|---|---|
| 1247.2.21 / PD 49 | 1.1.1.007 | 1247.2.21 / PD 49 | 1.1.1.007 | 1247.2.21 / PD 49 to 1247.2.21 / PD 49 | Orvil |

---

## Epoch (Baseline)

| Item | Value |
|---|---|
| The saga opens in | Year 1247 `[ASKED]` |
| Calendar | The Nine Suns calendar (Part 41 Area 1). The origin and the length of the "nine-sun cycle" stay the contested origin, OPEN-AREA: the calendar names no cycle length. |
| Phase Day 1 | `1247.1.1 / PD 1`: Year 1247, Ilovany (Month 1), Day 1, weekday Orvil (the third weekday: Sanvil and Mavil fall just before Day One, Part 41 Rule 41.3.1.4), the first day of spring `[ASKED]` |
| The year | 365 Saha days, no leap day, so Part 30's count of 365 Phase Days to a year holds `[ASKED]` |
| The Saha day | 26 standard hours (`ledger-worlds-location/saha.md`). A day runs from one dawn to the next; a night belongs to the day that began at the dawn before it, save that a scene that opens in the last dark hour and runs on into a dawn takes the date of that dawn (Part 41 Rule 41.2.1.3a; the author: "Open in the last dark hour; one scoped Part 41 rule"). The last dark hour is a plan word: no hour of dawn is fixed `[ASKED]` |
| Phase 1 | Years 1247 to 1255 (nine years, Part 30). The Phase 1 close is Phase Day 3285: `1255.12.27 / PD 3285`, Year 1255, Ulenor, Day 27, weekday Nuvil |
| Phase 2 | Opens `1256.1.1 / PD 3286`: Year 1256, Ilovany, Day 1 |
| Before Day One | Phase Day 0 is `1246.12.27 / PD 0`: Year 1246, Ulenor, Day 27, for flashbacks. The same tables serve every earlier Year. A present-time scene that opens in the last dark hour before the dawn of Day One and runs on into it is dated Phase Day 1 and not Phase Day 0 (Part 41 Rule 41.2.1.3a) |
| Phase Day N to a date | Year = 1247 + floor((N - 1) / 365); day of the year = ((N - 1) mod 365) + 1; then month and day from the month table. Floor and mod take the lower whole number, so Phase Day 0 gives Year 1246 and day 365 |

---

## Months (Baseline)

| No | Name | Season word | Days | Day of year | Phase Day, Year 1247 | Weekday offset |
|---|---|---|---|---|---|---|
| 1 | Ilovany | spring | 28 | 1 to 28 | 1 to 28 | 2 |
| 2 | Melorany | spring | 31 | 29 to 59 | 29 to 59 | 2 |
| 3 | Sorevany | spring | 33 | 60 to 92 | 60 to 92 | 5 |
| 4 | Arvelle | summer | 30 | 93 to 122 | 93 to 122 | 3 |
| 5 | Sorvelle | summer | 36 | 123 to 158 | 123 to 158 | 5 |
| 6 | Orvelle | summer | 25 | 159 to 183 | 159 to 183 | 6 |
| 7 | Mivoran | autumn | 33 | 184 to 216 | 184 to 216 | 3 |
| 8 | Laviran | autumn | 29 | 217 to 245 | 217 to 245 | 1 |
| 9 | Evoran | autumn | 29 | 246 to 274 | 246 to 274 | 2 |
| 10 | Nuvenor | winter | 27 | 275 to 301 | 275 to 301 | 3 |
| 11 | Anelor | winter | 37 | 302 to 338 | 302 to 338 | 2 |
| 12 | Ulenor | winter | 27 | 339 to 365 | 339 to 365 | 4 |

Total 365 days; the Phase Day column moves on by 365 for each later Year. The four seasons are the four quarters: spring (Ilovany to Sorevany) 92 days, summer (Arvelle to Orvelle) 91, autumn (Mivoran to Evoran) 91, winter (Nuvenor to Ulenor) 91. The season words are plan words only: Part 13 leaves the in-world season names, the weather and the climate to the first Area that shows them. The weekday offset is (the day of the year at the start of the month, minus 1, plus 2) mod 7, the two being the weekdays that fall before Day One (see Weekdays below). The month names are the author's own list, final `[ASKED]` (naming results below).

---

## Weekdays (Baseline)

| No | Name |
|---|---|
| 1 | Sanvil |
| 2 | Mavil |
| 3 | Orvil |
| 4 | Nuvil |
| 5 | Yevil |
| 6 | Mirovil |
| 7 | Alovil |

The week is seven days and runs on through the year without a break: it never restarts at a month or a year. A year is 365 = 52 x 7 + 1 days, so the weekday of Ilovany, Day 1 moves forward one each Year. The names are the author's own list, final `[ASKED]`. **The alignment is the author's choice and a major fact, like the names `[ASKED]`:** Phase Day 1 is weekday 3, Orvil, and the first weekday, Sanvil, falls two days before Day One (the author: "Phase Day 1 is the third weekday, Orvil"; the story still opens on Ilovany, Day 1). It changes only on the author's word (Part 41 Rule 41.3.1.4).

- **Formula:** `weekday number = ((Year - 1247) + offset[Month] + (Day - 1)) mod 7 + 1`, with mod always giving 0 to 6, so a Year before 1247 works.
- **From a Phase Day N:** `((N + 1) mod 7) + 1`. Phase Day 1 is weekday 3, Orvil; Phase Day 365 is Orvil; Phase Day 366 and Phase Day 3285 are weekday 4, Nuvil. Phase Day 0 is Mavil and Phase Day -1 is Sanvil.

| Month | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Offset | 2 | 2 | 5 | 3 | 5 | 6 | 3 | 1 | 2 | 3 | 2 | 4 |

| Year | 1247 | 1248 | 1249 | 1250 | 1251 | 1252 | 1253 | 1254 | 1255 | 1256 |
|---|---|---|---|---|---|---|---|---|---|---|
| Weekday of Ilovany, Day 1 | Orvil | Nuvil | Yevil | Mirovil | Alovil | Sanvil | Mavil | Orvil | Nuvil | Yevil |

---

## Fixed Days (Baseline)

| Day | Kingdom | Month | Day of the month | Phase Day, Year 1247 | Owning entry (points back here) |
|---|---|---|---|---|---|
| Festival of the Twin Oath | Azure Sky Kingdom | 5 (Sorvelle) | 16 | 138 | `ledger-worlds-location/azure-sky-kingdom.md` (§5.4) |
| Festival of the Gale Ascent | Gale Kingdom | 7 (Mivoran) | 8 | 191 | `ledger-worlds-location/gale-kingdom.md` (§5.4) |

Each repeats every Year on the same month and day: Phase Day in Year Y = Phase Day in Year 1247 + 365 x (Y - 1247). The weekday is not fixed: each festival falls one weekday later each Year (month and day only, the author) `[ASKED]`. What a festival is and requires stays with Part 25 and the owning entry. A festival scene falls on its festival's day (the dating check, Part 41 Area 6).

The four quarter-days are the first day of each season: Ilovany, Arvelle, Mivoran and Nuvenor, Day 1, which are Phase Days 1, 93, 184 and 275. They are named only; nothing is fixed to them (left open by the author). No other day is fixed; intervals stay the author's `[ASK]` items.

---

## Birth Years of the Eight Heroes (Baseline)

| Protagonist | Age on Phase Day 1 | Birth year | Birthday |
|---|---|---|---|
| Varys | 35 | 1211 | OPEN-AREA |
| Valia | 33 | 1213 | OPEN-AREA |
| Varya | 8 | 1238 | Arvelle, Day 6: `1247.4.6 / PD 98` `[ASKED]` |
| Aeries | 34 | 1212 | OPEN-AREA |
| Aalia | 33 | 1213 | OPEN-AREA |
| Aegon | 8 | 1238 | Sorvelle, Day 10: `1247.5.10 / PD 132` `[ASKED]` |
| Hercules | 28 | 1218 | OPEN-AREA |
| Bison | 27 | 1219 | OPEN-AREA |

`[DERIVED]` and recorded on the author's yes; the hero ledgers are frozen and hold the ages only, save for one added birthday line each in `varya.md` and `aegon.md`. The birth year is 1246 minus the age on Phase Day 1, because Phase Day 1 falls on the first day of Year 1247, before any birthday of that Year (Part 41 Area 8). Each hero is then the Part 30 start age on Phase Day 1 and the Part 30 end-state age (start + 9) on Phase Day 3285, the last day of Year 1255. Two birthdays are set and six stay OPEN-AREA. The author's word: "Varya birthday is in month of Arvelle day 6, Aegon is Day 10 of Sorvelle - Record in Section and their ledgers". So Varya's birthday is Arvelle, Day 6 (`1247.4.6 / PD 98` in Year 1247) and Aegon's is Sorvelle, Day 10 (`1247.5.10 / PD 132` in Year 1247). The birth years stand, so each is eight on Phase Day 1 and turns nine in the summer of Year 1247. Each birthday repeats every Year on its own month and day (Phase Day in Year Y = Phase Day in Year 1247 + 365 x (Y - 1247)), and its weekday moves one later each Year and is not stored. A birthday set in the calendar is the author's major choice, like the names, and changes only by Canon Amendment on the author's word. For the other six the rule stands as it was: the first Area that states one sets it (Part 28 Area 17), and it is entered here first. One day is barred: no birthday falls on Ilovany, Day 1, or the Part 30 ages would fail. Hercules and Bison are aged in Sol-system calendar years (Part 30, section 1.3.1a notes); an Olympus-subjective age stays Negotiable and must not contradict it.

---

## Naming Results — the Nineteen Names (Baseline)

The twelve month names and the seven weekday names are major names chosen by the author (Part 28 Area 3.4 and Rule 20.4): "This is final" (round 8 of the calendar consultation) `[ASKED]`. Naming checks (Part 28 Rule 20.3, as Part 41 Area 2 records them): the names are the author's own list, so no culture register was applied; the collision scan (a case-insensitive substring search of the whole repository) found none of the nineteen names anywhere else; no search of the open web was made. No meaning, origin or etymology is recorded for any name, and any such lore is `OPEN-AUTHOR`.

---

## Planned Windows — Phase and Section (Baseline)

| Ref | Title | Phase Day span (Part 30) | Calendar window (derived) |
|---|---|---|---|
| 1 | The Roots of Becoming (Phase 1) | 1 to 3285 | Year 1247, Ilovany, Day 1 to Year 1255, Ulenor, Day 27 |
| 1.1 | *Azure Sky and Gale* | 1 to 365 | Year 1247, Ilovany, Day 1 to Ulenor, Day 27 |
| 1.2 | *The First Trial of Blades* | about 366 to about 913 | Year 1248, Ilovany, Day 1 to Year 1249, Orvelle, Day 25 |
| 1.3 | *Courts and Tensions* | about 914 to about 1460 | Year 1249, Mivoran, Day 1 to Year 1250, Ulenor, Day 27 |
| 1.4 | *The Fallen Demigods* | about 1461 to about 1825 | Year 1251, Ilovany, Day 1 to Ulenor, Day 27 |
| 1.5 | *Guilds, Quests, and the World's Edge* | about 1826 to about 2373 | Year 1252, Ilovany, Day 1 to Year 1253, Orvelle, Day 25 |
| 1.6 | *The Seven World Trees* | about 2374 to about 2920 | Year 1253, Mivoran, Day 1 to Year 1254, Ulenor, Day 27 |
| 1.7 | *The World Tree's Trials and the Final War* | about 2921 to about 3194 | Year 1255, Ilovany, Day 1 to Evoran, Day 29 |
| 1.8 | *Snow Town and the Edge of the World* | about 3195 to 3285 | Year 1255, Nuvenor, Day 1 to Ulenor, Day 27 |

The Phase Day spans are Part 30's (section 1.3.2a and the Section arc blocks) and are not changed. The calendar windows are derived from them by the month table above, and every window converts both ways. Part 30 allows plus or minus 2 months per Section, so these are the anchor windows; the recorded rows below show the actual windows beside them, and the plan row is kept and never overwritten. The table carries no status: a Section's status lives in the Section Events Log table below (`OPEN` or `CLOSED`), and a Section with no row there is planned only. Phase and Section only: the windows of a Novel-Part, a Chapter and an Area are recorded as written.

---

## Phase — Events Log (recorded)

One row per Phase, written at Gate 2. First and Latest are dates, `Y.M.D / PD N`.

| Ref | First | Latest |
|---|---|---|
| 1 | 1247.1.1 / PD 1 | 1247.2.21 / PD 49 |

---

## Section — Events Log (recorded)

One row per Section, written at Gate 2. First and Latest are dates, `Y.M.D / PD N`. Status is `OPEN` or `CLOSED`.

| Ref | First | Latest | Status |
|---|---|---|---|
| 1.1 | 1247.1.1 / PD 1 | 1247.2.21 / PD 49 | OPEN |

---

## Novel-Part — Events Log (recorded)

One row per Novel-Part, written at Gate 2. First and Latest are dates, `Y.M.D / PD N`.

| Ref | First | Latest |
|---|---|---|
| 1.1.1 | 1247.1.1 / PD 1 | 1247.2.21 / PD 49 |

---

## Chapter — Events Log (recorded)

One row per Chapter, written at Gate 2. First and Latest are dates, `Y.M.D / PD N`.

| Ref | First | Latest |
|---|---|---|
| 1.1.1.001 | 1247.1.1 / PD 1 | 1247.1.1 / PD 1 |
| 1.1.1.002 | 1247.1.1 / PD 1 | 1247.1.3 / PD 3 |
| 1.1.1.003 | 1247.1.2 / PD 2 | 1247.1.2 / PD 2 |
| 1.1.1.004 | 1247.1.2 / PD 2 | 1247.1.8 / PD 8 |
| 1.1.1.005 | 1247.1.9 / PD 9 | 1247.1.14 / PD 14 |
| 1.1.1.006 | 1247.2.15 / PD 43 | 1247.2.20 / PD 48 |
| 1.1.1.007 | 1247.2.21 / PD 49 | 1247.2.21 / PD 49 |

---

## Area — Events Log (recorded)

One row per Area, written at Gate 2. First and Latest are dates, `Y.M.D / PD N`. Kind is `present` or `flashback`. A whole-built Chapter has no Area files, so it is recorded here as one row per date line of the Chapter, keyed `(date segment N)` and citing the Chapter reference only (`guardrails/ledger/guardrail-ledger-update-law.md`, the whole-built Chapter rule).

| Ref | First | Latest | Kind |
|---|---|---|---|
| 1.1.1.001.01 | 1247.1.1 / PD 1 | 1247.1.1 / PD 1 | present |
| 1.1.1.001.02 | 1247.1.1 / PD 1 | 1247.1.1 / PD 1 | present |
| 1.1.1.001.03 | 1247.1.1 / PD 1 | 1247.1.1 / PD 1 | present |
| 1.1.1.001.04 | 1247.1.1 / PD 1 | 1247.1.1 / PD 1 | present |
| 1.1.1.002 (date segment 1) | 1247.1.1 / PD 1 | 1247.1.1 / PD 1 | present |
| 1.1.1.002 (date segment 2) | 1247.1.2 / PD 2 | 1247.1.2 / PD 2 | present |
| 1.1.1.002 (date segment 3) | 1247.1.3 / PD 3 | 1247.1.3 / PD 3 | present |
| 1.1.1.003 (date segment 1) | 1246.12.8 / PD -19 | 1246.12.8 / PD -19 | flashback |
| 1.1.1.003 (date segment 2) | 1247.1.2 / PD 2 | 1247.1.2 / PD 2 | present |
| 1.1.1.004 (date segment 1) | 1247.1.2 / PD 2 | 1247.1.2 / PD 2 | present |
| 1.1.1.004 (date segment 2) | 1247.1.8 / PD 8 | 1247.1.8 / PD 8 | present |
| 1.1.1.005 (date segment 1) | 1247.1.9 / PD 9 | 1247.1.9 / PD 9 | present |
| 1.1.1.005 (date segment 2) | 1247.1.12 / PD 12 | 1247.1.12 / PD 12 | present |
| 1.1.1.005 (date segment 3) | 1247.1.14 / PD 14 | 1247.1.14 / PD 14 | present |
| 1.1.1.006 (date segment 1) | 1247.2.15 / PD 43 | 1247.2.15 / PD 43 | present |
| 1.1.1.006 (date segment 2) | 1247.2.17 / PD 45 | 1247.2.17 / PD 45 | present |
| 1.1.1.006 (date segment 3) | 1247.2.20 / PD 48 | 1247.2.20 / PD 48 | present |
| 1.1.1.007 (date segment 1) | 1247.2.21 / PD 49 | 1247.2.21 / PD 49 | present |

---

## Part 28 Area 17 — Lore note (Calendar Ledger)

A row is a record of when, not a lore file. This ledger carries no lore of its own: what the calendar is belongs to Part 41.

**Depth Test:** "Can a scene be dated without inventing the date?" The Current Position block, the month and weekday tables and the Area rows answer it, and the drafter never fills an open date silently.

**Silent Overwrite Prohibition (Part 28 Area 17.5):** Once a date is recorded, later Areas may extend it and never contradict it. The baseline values (the epoch, the month and weekday names and lengths, the fixed days) change only by Canon Amendment on the author's word.
