# ledger-worlds-travel — Ledger Index

**Ledger Domain:** World Systems — Named Travel Routes, Gate Networks, and Infrastructure
**Governed By:** `guardrails/ledger/guardrail-ledger-update-law.md`, Part 37 (Ledger Schema Law), Part 15 (Travel Law)
**Template:** Part 37 Area 3.1 — Schema Template: Travel Ledger
**Last Updated:** 2026-10-17
**Index Version:** v1.0
**Total Entries:** 1 — one standalone file, a Named Infrastructure hub, `alder-bridge.md`, kept through the redraft of Chapter 002 by the author's ruling of 2026-10-07 and written from the whole-built Chapter 002 (Ref: 1.1.1.002); no standalone route files yet; named routes in world-building lore noted below

> **Purpose:** This folder tracks named travel entities introduced in prose that require continuity under Part 15 (Travel Law). Three categories:
> - **Named Travel Routes** — specific named roads, paths, trade routes, sea lanes, or inter-system travel corridors that characters traverse and that have been given canonical names in prose. Example: "Named Road (Place A to Place B)," "Named Trade Lane (Place C to Place D)."
> - **Named Gate Networks** — Formation Teleportation Array (FTA) pairs, star gate networks, and named gate infrastructure that characters use for instantaneous or near-instantaneous transit. Example: "Named Gate (Place A ↔ Place B)," "Named Gate Chain (Place C to Place E)."
> - **Named Infrastructure** — canonical named waypoints, rest stations, toll gates, bridges, harbors, ports, and transit hubs that anchor travel narratively. Example: "Named Crossing (Place A)," "Named Station (Place B)."
>
> This ledger prevents continuity errors where a route is described inconsistently across Areas — different travel time, different hazards, different control by different factions, or different infrastructure status.

> **Part 15 Travel Paradigm Reference:**
> - ST-Band (Surface, Tiers 1–5): roads, waterways, atmospheric routes
> - OS-Band (Orbital/Inner-System, Tiers 5–7): orbital insertion, inner-system lanes
> - IS-Band (Interstellar, Tiers 8–10): FTL routes, star gates, long-haul lanes
> - GT-Band (Galactic, Tiers 11–14): galactic gate grids
> - CT-Band (Cosmological, Tiers 15–20): cosmological transit

> **Update Protocol:** Per `guardrails/ledger/guardrail-ledger-update-law.md`:
> - **New Route File Trigger:** Any Area that gives a travel route a proper name and establishes travel time, hazards, or faction control requires a new `[route-name].md` file at Gate 2.
> - **New Gate File Trigger:** Any Area that names a Formation Teleportation Array or star gate pair requires a new `[gate-name].md` file.
> - **New Infrastructure File Trigger:** Any Area that names a waypoint, station, or hub with canonical function requires a new `[hub-name].md` file.
> - **Update Trigger:** Route status change (route opens/closes/captured/destroyed); gate activation or deactivation; infrastructure construction or destruction; faction control shift; travel time change due to world events.

> **Mandatory Update Triggers:**
> - Named travel route introduced with canonical travel time or hazard profile
> - Named gate or FTA pair activated or deactivated in prose
> - Named infrastructure hub introduced with canonical function
> - Route captured, blocked, or destroyed (triggers CSS consequence event simultaneously)
> - Travel time revision (world event changes route conditions)
> - Sacred Ground pilgrimage route named (joint update with `ledger-worlds-location`)

> **Marker Legend:** These markers appear in the entries of this ledger. Open cells otherwise carry `OPEN-AREA` or `OPEN-AUTHOR` (Part 37 Area 5).
> - `[ASKED]`: the author chose this value.
> - `[DERIVED]`: the drafter inferred this value from cited evidence and the author reviewed it in the digest without overriding it (Part 39 Rule 39.3.3.1); it is pending only when the entry also says flagged for author confirmation.
> - `[AUTHOR-PENDING]`: a question about this value has been raised and is not yet answered.
> - `[MARKED SLOT]`: a slot left empty on purpose until the author rules.
> - "flag, do not invent": when a scene needs the value, the prose may establish one small fact at a time under Part 28 Area 17, logged in this ledger and offered to the author as a draft value at the next Section close. A name or a major entity (Part 28 Area 20.4) goes to the author first, through the Decision Consultation Gate.

---

## Registry A — Named Travel Routes

| File | Route Name | From | To | Paradigm Band | Travel Time | Faction Control | Status | Last Updated |
|---|---|---|---|---|---|---|---|---|

*No standalone files yet. Named routes established in world-building lore (location ledgers) pending traversal in an Area:*
- **The Sapphire Road** — Azure Sky capital ↔ Gale Kingdom via Lyraen crossings (cross-ref: ledger-worlds-location/azure-sky-kingdom.md §5.11); travel time not yet established in prose (sketch legs: `ledger-worlds-distance` DIST-010, DIST-012 and DIST-013)
- **The Southern March Trail** — Azure Sky capital ↔ Southern March (cross-ref: ledger-worlds-location/azure-sky-kingdom.md §5.11, nine-suns-continent.md §5.11); travel time not yet established in prose
- **The Riverway** — Lyraen river-barge trade south from Windward headwaters to Southern Sea (cross-ref: ledger-worlds-location/azure-sky-kingdom.md §5.11, nine-suns-continent.md §5.11); travel time not yet established in prose
- **The Windward Trail** — seasonal Central Highlands ↔ Aerie Plateau; Northern Accord jurisdiction (cross-ref: nine-suns-continent.md §5.11); travel time and hazards not yet established in prose
- **The Long Coast Reach** — Gale Kingdom maritime frontier (cross-ref: nine-suns-continent.md §5.11); travel time not yet established in prose
- **Windward courier dedicated line** — courier route between Azure Sky Kingdom and Gale Kingdom via the Windward Range corridor; described but not yet given a proper route name in prose; will receive a standalone entry when properly named or traversed with travel-time detail

---

## Registry B — Named Gate Networks

| File | Gate Name | Node A | Node B | Gate Type | Range | Activation Status | Controller | Last Updated |
|---|---|---|---|---|---|---|---|---|

*No entries yet. Files created as named gate pairs are introduced in prose.*

---

## Registry C — Named Infrastructure

| File | Hub Name | Location | Type | Function | Faction Control | Status | Last Updated |
|---|---|---|---|---|---|---|---|
| alder-bridge.md | Alder Bridge | Greenhollow Cross (`ledger-worlds-location/greenhollow-cross.md`, §5.8) | Bridge with a toll collector | The cart road crosses the village stream here on grey planks over stone legs, and a toll collector at the near end works a bar (its short end is pulled down to raise the long pole clear of the road), counts each load and each person who goes through, and marks a slate that hangs from the post (Ref: 1.1.1.002) | Not established (the toll collector is Pasco Cobb; whom he answers to, the toll and who receives it are open) | Operational — shown in use on 1247.1.1 / PD 1 | 2026-10-08 |

*One entry so far. Further files are created as named infrastructure is introduced in prose.*

---

## Part 28 Area 17 — Lore Section Schema (Travel Domain)

**Governing Law:** Part 28 Area 17 (Lore Creation Law). **Audit Hook:** ALCA dimension AL-10 (`guardrails/audit/guardrail-alca.md`).

**For Named Travel Routes — Required Minimum Lore Fields:**

1. **Route Name** — canonical name as established in prose.
2. **Start / End Points** — Part 13 location hierarchy references; cross-reference to `ledger-worlds-location`.
3. **Paradigm Band** — Part 15 ST/OS/IS/GT/CT-Band; Part 8 Type 9 tier range.
4. **Travel Time** — canonical journey duration at standard paradigm speed; CMS distance expression per Part 14.
5. **Hazards** — canonical hazards along the route (environmental, political, cultivator threat profile).
6. **Faction Control** — which faction(s) control or patrol the route; toll or access conditions.
7. **Traffic Volume** — relative usage (major arterial / secondary / remote / restricted).
8. **Historical Notes** — origin of the route; major events that occurred on it.
9. **Current Status** — open / restricted / blocked / destroyed.

**For Named Gate Networks — Required Minimum Lore Fields:**

1. **Gate Name** — canonical name.
2. **Gate Type** — Formation Teleportation Array (FTA) vs. technology star gate (Part 15 Area 13).
3. **Node Locations** — Part 13 references for both ends; cross-reference to `ledger-worlds-location`.
4. **Range** — CMS distance expression; gate type determines range ceiling per Part 15 Area 13.
5. **Throughput** — maximum transit capacity (cultivator count or vessel SC class limit).
6. **Activation Energy** — CPM cost (FTA) or technology fuel requirement (star gate).
7. **Activation Status** — active / dormant / destroyed.
8. **Controller** — named faction or institution; access rules for non-aligned users.

**For Named Infrastructure — Required Minimum Lore Fields:**

1. **Hub Name** — canonical name.
2. **Location** — Part 13 location tier and class; cross-reference to `ledger-worlds-location`.
3. **Type** — waypoint / rest station / toll gate / bridge / harbor / port / transit hub.
4. **Canonical Function** — what service or constraint this hub imposes on travelers.
5. **Faction Control** — who operates it; access rules and fees.
6. **Capacity** — throughput or accommodation capacity.
7. **Current Status** — operational / damaged / destroyed / under construction.

**Depth Test:** "Can a journey scene using this route, gate, or infrastructure be written accurately from only this ledger file?" If yes, depth is satisfied.

---

## Lore Section Compliance Registry

| File | Entry Name | Type | Paradigm Band | Depth-Test Certification | Last Lore Update |
|---|---|---|---|---|---|
| alder-bridge.md | Alder Bridge | Named Infrastructure (bridge with a toll collector) | ST-Band (a surface cart road) | Kept through the redraft of Chapter 002 by the author's ruling of 2026-10-07 and written from the whole-built Chapter 002 (Ref: 1.1.1.002): the bar, the count, the slate, the planks on stone legs and the two ends are shown, so the Depth Test passes for the daytime crossing; the toll, who receives it, the keeper and the night practice stay open (OPEN-AREA) | 2026-10-17 |

---

