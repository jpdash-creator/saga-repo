# ledger-worlds-distance — Ledger Index

**Ledger Domain:** World Systems — Named Distance Reference Points and Spatial Landmarks
**Governed By:** Part 1 Area 5 (Ledger System), Part 14 (Distance Law)
**Template:** Part 1 Area 5.5.14 — Distance Ledger Format
**Last Updated:** 2026-05-10
**Index Version:** v1.1
**Total Entries:** 0

> **Purpose:** This folder tracks named spatial entities that anchor the world's distance framework — the reference points and landmarks characters use to understand where they are and how far they need to travel. Two categories:
> - **Named Spatial Landmarks** — specific named cosmic, stellar, planetary, or terrestrial reference points that have been introduced in prose as canonical navigation or distance anchors. These are points in space that have been given names and described with enough canonical detail that they function as distance reference points. Example: "The Saha Orbital Beacon" (a formation array marker at a specific orbital point), "The Greythorn Waystone" (a landmark cultivators use to gauge distance on the continent), "The Twin Star Pillars" (a visible stellar marker used for inter-system navigation).
> - **Named Established Measurements** — canonical distance values that have been established in prose — specific journey times, stated distances between named locations, or spatial-scale benchmarks that define the texture of the world's geography. Example: "The Lyraen River Compact — Azure Capital to Gale Capital is 1,400 km via the River Road at cultivator ground speed." These are not routes (tracked in `ledger-worlds-travel`) — they are the specific distance facts that define the world's spatial reality.
>
> This ledger prevents spatial continuity errors where a journey is described as three days in one prose unit and six days in another, or where a landmark is placed inconsistently across scenes.

> **CMS Reference (Part 14 Area 2):**
> mm / cm / m / km / Mm (~1,000 km) / Gm (~10,000 km) / AU (~150 million km) / light-second / light-minute / light-hour / light-day / light-week / light-year (ly) / kilolight-year (kly) / megalight-year (Mly) / gigalight-year (Gly) / Trans-universal

> **Update Protocol:** Per Part 1 Area 6:
> - **New Landmark File Trigger:** Any prose unit that names a spatial landmark and uses it as a reference point for distance, navigation, or location requires a new `[landmark-name].md` file at Gate 2.
> - **New Measurement File Trigger:** Any prose unit that establishes a canonical distance value between two named points requires a new entry in Registry B, and a `[location-a]–[location-b]-distance.md` file if the measurement is complex enough to warrant its own file.
> - **Update Trigger:** Landmark destroyed or moved; canonical distance revised by world event (terrain change, formation array range extension, new route established).

> **Mandatory Update Triggers:**
> - Named spatial landmark introduced as a navigation reference
> - Canonical distance between two named locations established in prose for the first time
> - Landmark destroyed or altered (joint update with `ledger-worlds-location`)
> - Formation Array effect radius stated for a named array (joint update with `ledger-worlds-travel`)
> - Soul sense range stated for a specific character at a specific location (joint update with character ledger)

---

## Registry A — Named Spatial Landmarks

| File | Landmark Name | Location Tier | CMS Scale | Type | Faction Control | Status | Last Updated |
|---|---|---|---|---|---|---|---|

*No entries yet. Files created as named spatial landmarks appear in prose.*

---

## Registry B — Established Distance Measurements

| ID | From | To | CMS Distance | Context | Established In | Last Updated |
|---|---|---|---|---|---|---|

*No entries yet. Measurements added when canonical distances are established in prose.*

---

## Part 28 Area 17 — Lore Section Schema (Distance Domain)

**Governing Law:** Part 28 Area 17 (Lore Creation Law). **Audit Hook:** Part 1 Area 8.13 ALCA dimension AL-10.

**For Named Spatial Landmarks — Required Minimum Lore Fields:**

1. **Landmark Name** — canonical name as established in prose.
2. **Location** — Part 13 cosmological tier; precise placement in CMS terms relative to named reference points.
3. **CMS Scale** — what scale of distance this landmark anchors (km-scale for continental landmarks, AU-scale for system landmarks, etc.).
4. **Type** — formation array marker / natural feature / constructed waypoint / stellar body / dimensional anomaly.
5. **Navigation Function** — how characters use this landmark (visual bearing, soul-sense anchor, technology beacon).
6. **Visibility Profile** — who can perceive this landmark and at what range (Part 14 soul sense range tables; Part 8 Type 13 sensor range).
7. **Faction Association** — which faction controls or maintains this landmark, if any.
8. **Current Status** — intact / damaged / destroyed / relocated.

**For Established Distance Measurements — Required Lore Fields:**

1. **From / To** — named locations; cross-references to `ledger-worlds-location`.
2. **CMS Value** — the canonical distance in Part 14 CMS units.
3. **Measurement Context** — what type of path or space this distance measures (direct line / route / orbital arc / interstellar).
4. **Journey Time at Standard Speed** — at relevant Part 15 paradigm speeds for the cultivation realm and technology tier of the story's current phase.
5. **Establishing Source** — which prose unit first established this measurement.
6. **Confidence Level** — whether this is a precisely stated measurement or an approximate range.

**Depth Test:** "Can a scene's spatial geography be rendered consistently using only the reference points and measurements in this ledger?" If yes, depth is satisfied.

---

## Lore Section Compliance Registry

| File | Entry Name | Type | CMS Scale | Depth-Test Certification | Last Lore Update |
|---|---|---|---|---|---|

*No entries yet.*

---

*ledger-worlds-distance _index — v1.1 (2026-05-10) — 0 entries; Prose 1–8 audit pass: 15-minute Northern Accord corridor relay propagation time established (Prose 8), but this is a signal-relay latency, not a CMS travel-distance measurement — no entry triggered. v1.1: Prose 1–8 audit pass confirmed.*
