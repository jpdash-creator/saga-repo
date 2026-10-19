# Guardrail: One Skill Per Part

**Source:** the consolidated skill layer (skills named after their titles and grouped by domain)
**Applies to:** all 4 agents and every `.claude/commands/*.md` command

## The rule

Every canon Part **that has a skill** is represented by **exactly one skill**, in its own
folder `.claude/skills/<group>-<title>/`. `<group>` is the Part's domain (`character`,
`cultivation`, `energy`, `ledger`, `narration`, `society`, `spec`, `synergy`, `technology`,
`worlds`) and `<title>` is the Part's own title in kebab-case — Part 18, "Villain Law", is
`character-villain-law`. There are 43 of them — Parts 2–33 and 35–45 (Part 45 registered, 2026-10-19) — and they are the
entire canon skill layer (Part 40 is Monster Law; Part 41 is Calendar Law, `worlds-calendar-law`, in the `worlds` group beside Parts 13 to 15; Part 42 is Manual and Weapon Style Law, `manual-and-weapon-style-law`, a cultivation-domain Part whose folder name carries no group prefix: the one exception to `<group>-<title>`, open for the author). Each one carries the full, verbatim, independently-validated
rule text of every Area of its Part.

The folder name and the `name:` line of its `SKILL.md` are always identical, and neither
carries a Part number. **Never guess a folder name from a Part number.** Resolve it with the
table below, or with the `part` field of `canon-manifest/skill-index.json`.

## Part → skill

| Part | Skill | Part | Skill |
|---|---|---|---|
| 2 | `narration-novel-book-structure-law` | 21 | `society-civilization-law` |
| 3 | `cultivation-power-and-lifespan-law` | 22 | `society-faction-law` |
| 4 | `cultivation-affinity-heart-and-soul-law` | 23 | `society-affiliation-law` |
| 5 | `cultivation-combat-and-fight-law` | 24 | `society-information-and-secrecy-law` |
| 6 | `cultivation-move-taxonomy-law` | 25 | `society-culture-and-social-law` |
| 7 | `cultivation-fusion-law` | 26 | `character-psychological-law` |
| 8 | `technology-scale-law` | 27 | `character-consequence-law` |
| 9 | `technology-growth-law` | 28 | `narration-novel-creative-flexibility-law` |
| 10 | `technology-science-law` | 29 | `narration-dialogue-and-social-interaction-law` |
| 11 | `energy-substance-law` | 30 | `narration-novel-macro-story-law` |
| 12 | `energy-relics-and-artifacts-law` | 31 | `synergy-cultivation-technology-law` |
| 13 | `worlds-location-law` | 32 | `technology-vehicle-law` |
| 14 | `worlds-distance-law` | 33 | `technology-weapon-law` |
| 15 | `worlds-travel-law` | 35 | `narration-content-density-law` |
| 16 | `character-what-is-a-character-law` | 36 | `narration-novel-thematic-law` |
| 17 | `character-hero-law` | 37 | `ledger-schema-law` |
| 18 | `character-villain-law` | 38 | `spec-story-specification-law` |
| 19 | `character-side-character-law` | 39 | `character-behavioral-synthesis-law` |
| 20 | `character-ideology-law` | 40 | `character-monster-law` |
| | | 41 | `worlds-calendar-law` |
| 42 | `manual-and-weapon-style-law` | 43 | `character-evolution-law` |
| 44 | `cultivation-battle-plausibility-law` | 45 | `cultivation-situational-combat-law` |

**One non-canon skill sits beside the 43 (Part 45 registered, 2026-10-19):** `reference-military-organization-and-rank`, the
only skill in the `reference` group. It has no Part number, is not counted among the 42, and
is never cited as canon.

- **One Part, one file, one read.** When a Part's rules are needed, its consolidated skill
  *is* the read. There is no second place to look and no deeper file to open.
- **Area-level routing lives in the manifest, not in separate skills.**
  `canon-manifest/skill-index.json` holds one entry per consolidated skill with a nested
  `areas[]` array — `area`, `title`, `anchor`, `line_count`, and that Area's
  cross-Part `related` edges. Use it to find *which Part and Area* governs a topic, then read
  that Part's consolidated skill and jump to the Area.
- **An Area reference is a locator, not a file.** A citation of the form
  `narration-novel-creative-flexibility-law §Area 19` names a section inside the consolidated file. It
  never implies a separate skill exists for that Area.
- **Every rule citation names its Part.** Rule and Area numbers repeat across Parts (Rules 26.2.1
  and 26.2.2 exist in both Part 22 and Part 36), so a rule is cited as, for example, "Part 22
  Rule 26.2.1", never as the bare number.

## There is no layer beneath the 39

The canon skill layer is 39 files and nothing else. No per-Area file exists anywhere in this
repository, under any name, in any folder — and none may be created.

- **Never invent a deeper file.** A skill named for an Area of a Part (a
  `<group>-<title>-<area-slug>` folder) does not resolve to anything. Referring to one in a
  command, agent, guardrail, ledger, or audit is itself a defect to be corrected.
- **Never treat a missing file as missing canon.** If a rule appears absent from a
  consolidated skill, that is a **CCIA-worthy finding** — report it and ask the author.
  There is no fallback source to consult and no archive to reach into.
- **Never reintroduce a per-Area file.** If a Part's text needs to change, it changes in that
  Part's consolidated skill, through the normal author-approval path.
- **Never resolve a suspected gap by editing canon text on your own judgment.**

## Escalation

If a consolidated skill appears internally inconsistent, or if a command or agent points at a
skill name that does not exist, report it and ask the author — never silently patch canon text.

