# ledger-worlds-travel — Ledger Index

**Ledger Domain:** World Systems — Named Travel Routes, Gate Networks, and Infrastructure
**Governed By:** Part 1 Area 5 (Ledger System), Part 15 (Travel Law)
**Template:** Part 1 Area 5.5.13 — Travel Ledger Format
**Last Updated:** 2026-05-10
**Index Version:** v1.1
**Total Entries:** 0 — no standalone route files yet; named routes in world-building lore noted below

> **Purpose:** This folder tracks named travel entities introduced in prose that require continuity under Part 15 (Travel Law). Three categories:
> - **Named Travel Routes** — specific named roads, paths, trade routes, sea lanes, or inter-system travel corridors that characters traverse and that have been given canonical names in prose. Example: "The Lyraen River Road," "The Dustway to Greythorn," "The Azure Starpath (inner-system trade lane)."
> - **Named Gate Networks** — Formation Teleportation Array (FTA) pairs, star gate networks, and named gate infrastructure that characters use for instantaneous or near-instantaneous transit. Example: "The Twin Pillars Gate (Azure Capital ↔ Gale Capital)," "The Cloudreach FTA Chain."
> - **Named Infrastructure** — canonical named waypoints, rest stations, toll gates, bridges, harbors, ports, and transit hubs that anchor travel narratively. Example: "Threeford Crossing," "The Highwatch Station."
>
> This ledger prevents continuity errors where a route is described inconsistently across prose units — different travel time, different hazards, different control by different factions, or different infrastructure status.

> **Part 15 Travel Paradigm Reference:**
> - ST-Band (Surface, Tiers 1–5): roads, waterways, atmospheric routes
> - OS-Band (Orbital/Inner-System, Tiers 5–7): orbital insertion, inner-system lanes
> - IS-Band (Interstellar, Tiers 8–10): FTL routes, star gates, long-haul lanes
> - GT-Band (Galactic, Tiers 11–14): galactic gate grids
> - CT-Band (Cosmological, Tiers 15–20): cosmological transit

> **Update Protocol:** Per Part 1 Area 6:
> - **New Route File Trigger:** Any prose unit that gives a travel route a proper name and establishes travel time, hazards, or faction control requires a new `[route-name].md` file at Gate 2.
> - **New Gate File Trigger:** Any prose unit that names a Formation Teleportation Array or star gate pair requires a new `[gate-name].md` file.
> - **New Infrastructure File Trigger:** Any prose unit that names a waypoint, station, or hub with canonical function requires a new `[hub-name].md` file.
> - **Update Trigger:** Route status change (route opens/closes/captured/destroyed); gate activation or deactivation; infrastructure construction or destruction; faction control shift; travel time change due to world events.

> **Mandatory Update Triggers:**
> - Named travel route introduced with canonical travel time or hazard profile
> - Named gate or FTA pair activated or deactivated in prose
> - Named infrastructure hub introduced with canonical function
> - Route captured, blocked, or destroyed (triggers CSS consequence event simultaneously)
> - Travel time revision (world event changes route conditions)
> - Sacred Ground pilgrimage route named (joint update with `ledger-worlds-location`)

---

## Registry A — Named Travel Routes

| File | Route Name | From | To | Paradigm Band | Travel Time | Faction Control | Status | Last Updated |
|---|---|---|---|---|---|---|---|---|

*No standalone files yet. Named routes established in world-building lore (location ledgers) pending prose-unit traversal:*
- **The Sapphire Road** — Azure Sky capital ↔ Gale Kingdom via Lyraen crossings (cross-ref: azure-sky-kingdom.md §5.11); travel time not yet established in prose
- **The Southern March Trail** — Azure Sky capital ↔ Ember Reach boundary and beyond (cross-ref: azure-sky-kingdom.md §5.11); travel time not yet established in prose
- **The Riverway** — Lyraen river-barge trade south from Windward headwaters to Southern Sea (cross-ref: azure-sky-kingdom.md §5.11, nine-suns-continent.md §5.9); travel time not yet established in prose
- **The Windward Passage** — seasonal Central Highlands ↔ Aerie Plateau; Northern Accord jurisdiction (cross-ref: nine-suns-continent.md §5.11); travel time and hazards not yet established in prose
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

*No entries yet. Files created as named infrastructure is introduced in prose.*

---

## Part 28 Area 17 — Lore Section Schema (Travel Domain)

**Governing Law:** Part 28 Area 17 (Lore Creation Law). **Audit Hook:** Part 1 Area 8.13 ALCA dimension AL-10.

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

*No entries yet.*

---

*ledger-worlds-travel _index — v1.1 (2026-05-10) — 0 standalone route files; 6 named routes and 1 described courier line noted from world-building lore; files to be created as routes are traversed in prose with travel-time or hazard detail. v1.1: Named routes from azure-sky-kingdom.md §5.11 and nine-suns-continent.md §5.9 catalogued; Windward courier dedicated line noted.*
