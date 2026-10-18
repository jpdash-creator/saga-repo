---
name: tier-d-picking-recipe
description: Fast route for picking a Tier D compact code: which files to read, in what order, and which tokens are fixed by the formation
metadata:
  type: reference
---

1. Grep the Tier D registry in `ledger-character-side/_index.md` for the new name (collision) and read one existing row only to see the string form.
2. Read `character-behavioral-synthesis-law` Section 3.5 in full (Rules 39.3.5.1 to 39.3.5.7). Segments in order: role, age band, F, two PSM, three to six conduct codes (ascending Layer, one per Layer, one `[SIG]`), realm, stratum, affinity, soul, heart, ideology, stability, psychology (all `[AI]`), culture.
3. Find each dimension table with a Grep of `^#### \`L(01|03|10|13|21|22|27|29|30)-` in the same skill and read only the dimensions you pick from. Barred Layers (L14, L17 to L20, L26, L31 to L36) and the partial bars are in Rule 39.3.5.4.
4. Formation ledger gives the culture token (Azure Sky Kingdom state: `CPT-5`). Ideology codes: table in `character-ideology-law` (`OMI`, `LBI`, `PCI` and so on). Ordinary people: `RLM-UNAWAKENED`, `CC-S1`, `AFN-NONE`, `SOUL-NONE`, `HEART-NONE`, `IS-1`, `PIS-1`.
5. Pick the `[SIG]` code so it can be shown in one beat (a paper lifting, a voice pitched too high). Render conduct as action; never name it.

**Why:** the picking step is mandatory at Gate 1 and was the slowest part of Area 02.
6. Grep the code with backticks in `character-behavioral-synthesis-law/SKILL.md` and render from the catalog text, never from memory. A silent person is rendered through the conduct codes only.
7. Band codes met: `B39-L30-BAND-05` = 26 to 50, `-06` = 51 to 65, `-07` = 66 and over; YC-1 young child, YC-2 adolescent (three `L30-ANCHOR` codes, render at least one), YC-3 young adult; F3 = semi-formal, everyday. Confirm against Section 3.5 before use.
