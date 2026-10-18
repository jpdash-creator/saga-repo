---
name: narration-novel-book-structure-law
description: Governs the shape of the Starward Saga novel itself — how it is structured, formatted, paced, and written to disk. Its ten Areas cover the Five-Tier Narrative Hierarchy (Phase, Section, Novel-Part, Chapter, Area), in which the Area is the written unit, either a complete scene or one written portion of a scene that continues across consecutive Areas of the Chapter; the Area size range (three targets of 1,600, 1,800 and 2,000 words, a passing range of 1,280 to 2,400 words, Rule P2-Area-7); the Area-to-Area carry-over rule (Rule P2-Area-6); the Area depth mandate and the Fast/Medium/Slow pacing vocabulary, decided for every Area in the Chapter Spec and carried to the writing (Rules P2-Pacing-1 through P2-Pacing-3); Conversation Rules (dialogue mandate, double-quotes-plus-italics, the em-dash prohibition and the contraction rule: barred in narration and in dialogue, Canon Amendment 2026-10-16); Combat and Move Rules (bold-italic Named Moves and cultivation levels, the four mandatory combat elements); Point of View Governance (stable Deep POV, Rule 4.3 Area-boundary shifts, the Dual-POV Area License); the Novel Output File Structure Law (area-NN.docx and area-NN.md pairs in the chapter-NNN folder on the nested phase/section/part/chapter path); Book Creation Law for the Area .docx and .md files and the Area Title Block; the Chapter built whole by /create-chapter (Rule 6.3.4a, 2026-10-07: Build mode, no Area files, hidden Area markers, the break rule, the 55% to 60% word band); the Post-Area Audit Completeness Indicator Law; the Scope Visibility Protocol; and the Chapter Export Format Specification. Reach for this whenever drafting or redrafting an Area, picking an Area size target, formatting dialogue or a Named Move, deciding POV, writing novel output files, building a Chapter file with /chapter-builder, or auditing an Area for structural and formatting compliance. This is canon Part 2, domain narration, the single consolidated authority for the whole Part.
user-invocable: false
---

# Novel Book Structure Law

**Authority Tier:** 1 (Domain Authority — Narration)
**Domain:** Narration — Novel Book Structure and Output Law: the Five-Tier Narrative Hierarchy (Phase, Section, Novel-Part, Chapter, Area) — the Area as the written unit, a complete scene or one portion of a scene that continues across consecutive Areas — with the Area size range (Rule P2-Area-7), the Area-to-Area carry-over rule (Rule P2-Area-6), the Area depth mandate and the Fast/Medium/Slow pacing vocabulary decided in the Chapter Spec (Rules P2-Pacing-1 through P2-Pacing-3), Conversation Rules (dialogue mandate, double-quotes-plus-italics formatting, the em-dash prohibition and the contraction rule: barred in narration and in dialogue, Canon Amendment 2026-10-16), Combat and Move Rules (bold-italic Named Move and cultivation level formatting, the four mandatory combat elements), Point of View Governance (single stable POV, Deep POV standard), the Novel Output File Structure Law (per-Area area-NN.docx / area-NN.md file pairs in the nested chapter-NNN folder), Book Creation Law for the Area Document (.docx) and the Area Markdown File (.md), the Post-Area Audit Completeness Indicator Law, the Scope Visibility Protocol (non-binding planning guidance), and the Chapter Export Format Specification
**Governing Canon Parts Cross-Reference:** Parts 3, 5, 6, 12, 27, 28, 29, 30, 35, 36, 38, 41
**Version:** Canon v10.0 — Last Updated 2026-10-05

---

## Overview

Part 2 is the Starward Saga Canon's Novel Book Structure Law — the Tier 1 Domain Authority for how the novel itself is structured, written, formatted, and written to disk. Where Parts 3–27 and 29–35 govern what is mechanically and consequentially true about the Starward Saga universe, Part 2 governs the shape of the book: the structural hierarchy every novel inhabits, the execution standards every Area must meet, and the complete output file law that turns accepted Areas into the reader-facing novel on the filesystem.

Part 2's ten Areas fall into three functional clusters. **Structure and writing execution (Areas 1–4):** the Five-Tier Narrative Hierarchy (Phase → Section → Novel-Part → Chapter → Area) with tier definitions, immutability and transition rules, inter-tier continuity requirements, the Area as the written unit, the Area size range, the Area-to-Area carry-over rule, and the Area depth mandate with the Fast/Medium/Slow pacing vocabulary that the Chapter Spec records (Area 1); the Conversation Rules governing dialogue mandate, formatting, content requirements, and the novel-wide em-dash prohibition and contraction rule (barred in narration and in dialogue, Canon Amendment 2026-10-16) (Area 2); the Combat and Move Rules governing bold-italic formatting of Named Moves and cultivation level designations and the four mandatory combat elements (Area 3); and Point of View Governance with the Deep POV standard (Area 4). **Output file law (Areas 5–7):** the Novel Output File Structure Law defining the per-Area `.docx`/`.md` file pair, the nested output path, the Two-Gate trigger, and the immutable-per-file lifecycle (Area 5); and the Book Creation Law for the Area Document (.docx) and Area Markdown File (.md) governing typography, structural blocks, update protocols, and the chat-only Gate 1 Position Header boundary (Areas 6–7). **Post-Area instrumentation and export (Areas 8–10):** the Post-Area Audit Completeness Indicator Law (Area 8); the Scope Visibility Protocol, a non-binding planning instrument (Area 9); and the Chapter Export Format Specification (Area 10), governing the novel-grade typeset of the condensed Chapter file that `/chapter-builder` writes into the Novel-Part folder (the retired `/export-chapter` joined Area files; amended 2026-10-07: a Chapter file is condensed text written by `chapter_builder.py`, never a join, and the Phase and Novel compiles only join Chapter files).

The Governing Authority paragraph that applies to every Area is stated once in Appendix B, and the Cross-References tables are in Appendix A, which keeps the rows that carry a tie. This file is the single authority for the whole of Part 2; there is no layer beneath it.

---

## Area 1 — The Five-Tier Narrative Hierarchy

### Overview

Every novel in the Starward Saga is organized through five structural tiers, arranged from broadest to most granular:

```
PHASE
  └── SECTION
        └── PART
              └── CHAPTER
                    └── AREA
```

Each tier has a distinct narrative function. No tier may perform the function of another tier. Skipping tiers is not permitted. The entire novel exists within this hierarchy and only within this hierarchy.

In this hierarchy the Area is the written unit. The novel is drafted, audited, confirmed, scored and filed one Area at a time. An Area may be a complete scene, or a scene may continue across consecutive Areas of its Chapter (Tier 5).

**Principle P2-2 — Structure Serves Story, Not the Reverse.**
The five tiers organize the story being told; they do not dictate it. Where a count, range or length bracket in this Part conflicts with what the story demands, the story-demanded principles prevail and the bracket bends (Area 9).

**Principle P2-4 — No Meta-Constructs in Prose.**
The structure of the novel (Phase, Section, Novel-Part, Chapter and Area labels, numbers and names) never appears inside the prose body the reader reads. It appears only in headings, dividers, titles and file names (Rule 6.2.5). A date is not a structure label: the date line of Rule 6.3.2b names a day in the calendar and never a position in the novel, so it is lawful in the Area text and is not a meta-construct.

---
### Tier 1 — Phase

#### 1.1.1 — Definition

A Phase is the broadest structural unit of a Starward Saga novel or novel series. It represents a **major story epoch** — a sustained period of the narrative in which the fundamental parameters of the world are fixed at a specific state. These parameters include:

- **Power Ceiling:** The maximum cultivation tier achievable or encountered within the Phase. No character may exceed the Phase's power ceiling within the Phase's narrative. A higher power ceiling belongs to the next Phase.
- **Technology Ceiling:** The maximum technological scale and capability present within the Phase. Technology that exists beyond the Phase's technology ceiling is unknown, inaccessible, or not yet discovered.
- **Political Scale:** The scope of political entities, conflicts, and power structures that are operative within the Phase. A Phase may be city-scale, regional-scale, continental-scale, or world-scale. The political scale defines the stakes and the reach of narrative events.

#### 1.1.2 — Phase Function

A Phase is not a chapter. It is not a story arc. It is an epoch — a geological layer of the narrative. Its function is to:

- Establish a coherent world-state against which the story's events take place.
- Define the hard limits of what is possible within its span.
- Create the context within which all lower structural tiers operate.

A Phase answers the implicit question every reader carries: "What kind of world is this, and how powerful are the forces at play?" The Phase answer must be consistent from its opening to its close.

#### 1.1.3 — Phase Immutability

Phases are **never renamed, merged, or retroactively altered once created.** This rule exists because:

- The Phase defines the canon-valid state of the world for all narrative output within its span.
- Retroactively altering a Phase would potentially invalidate all previously validated narrative output within it.
- Phase-level changes require a canonical in-world event that opens the next Phase — they are not editorial revisions.

If the story requires a change to the world's power ceiling, technology ceiling, or political scale, that change is not a Phase revision. It is the opening event of the next Phase.

#### 1.1.4 — Phase Transitions

A Phase ends when a world-state change of sufficient magnitude has permanently altered at least two of the three Phase parameters (power ceiling, technology ceiling, political scale). The transition event is itself narrative — it is the climax or turning point that concludes one Phase and opens the next. Phase transitions are among the most significant moments in the entire series. They must be earned through narrative events, not declared arbitrarily.

#### 1.1.5 — Phase Scope

A Phase may span a single novel or multiple novels. A single novel may contain multiple Phases, though this is rare and indicates a story of extraordinary scope and compressed transformation. A Phase with a single Section is valid. A Phase with many Sections is equally valid. There are no minimum or maximum Section counts per Phase.

---

### Tier 2 — Section

#### 1.2.1 — Definition

A Section is the second structural tier and represents a **location-anchored major arc** within a Phase. A Section is defined by its **dominant location** — the primary geographical, political, or cosmological setting in which the arc's events unfold. The location gives the Section its identity, its atmosphere, and its physical context.

Sections are **location-anchored** in the sense that the dominant location is constant enough to define the Section's character — but the story is not required to remain in a single room or even a single city for the entire Section. Movement within a location's sphere of influence (a city and its surrounding territory, a realm and its adjacent zones, a palace complex and its grounds) is valid within a single Section. What ends a Section is not minor movement — it is a fundamental relocation of the narrative's center of gravity to a new and different place.

#### 1.2.2 — Section Function

A Section's narrative function is to develop a **major arc within the Phase** — a sustained story development that has its own internal logic, conflict, escalation, and resolution (or deliberate irresolution that feeds the next Section). A Section may encompass:

- The development of a major relationship or enmity
- The investigation or revelation of a major secret
- A campaign, siege, or extended conflict
- A period of training, growth, or transformation
- A political struggle, negotiation, or collapse
- An exploration or discovery journey

A Section is large enough to contain significant narrative weight but is bounded by its location anchor. When the story must move to a fundamentally new setting to continue its development, a new Section begins.

#### 1.2.3 — Inter-Section Relationships

A Phase must feel whole. This wholeness is produced by ensuring **novelic relationships between Sections within the same Phase**. This means:

- No Section exists in narrative isolation. Each Section must carry consequences from the previous Section and plant seeds that the next Section will develop.
- The Sections of a Phase collectively tell a story that is larger than any individual Section's arc.
- The emotional and thematic journey of the Phase is the sum of its Sections in deliberate sequence.

#### 1.2.4 — Section Transitions

A Section does not begin as a narrative unit announcing itself. It begins **thematically** — as the story demands, following the thematic journey of the previous Section's close. The reader should feel the shift in location and arc as a natural story development, not as a chapter announcement or scene heading. The transition is produced through prose, through character momentum, through the pull of the new setting and its demands. The structural label "Section" never appears in the text.

---

### Tier 3 — Part (Novel-Part)

#### 1.3.1 — Definition

A Novel-Part is the third structural tier and represents a **thematic progression** within a Section. Where a Section is location-anchored, a Novel-Part is thematically anchored. It develops a specific thematic thread, emotional phase, or narrative movement within the broader arc of its Section.

#### 1.3.2 — Novel-Part Function

A Novel-Part exists to:

- Preserve **immersion** by organizing the narrative into thematically coherent blocks that do not overload the reader with tonal or contextual whiplash.
- Govern **pacing** by defining natural points of thematic completion or escalation that allow the story to breathe without losing momentum.
- Carry the reader through a specific emotional or intellectual journey within the Section, completing it sufficiently that the next Novel-Part begins from a new and evolved thematic position.

There are no artificial limits on the number of Novel-Parts within a Section. A Section requires as many Novel-Parts as its story demands — no more, no fewer.

#### 1.3.3 — Inter-Part Relationships

A Section must feel whole. Wholeness requires **novelic relationships between Novel-Parts within the same Section**:

- Each Novel-Part must emerge from the thematic state left by the previous Novel-Part's close.
- The transition between Novel-Parts must feel organic, not editorial. The new Novel-Part begins because the story's thematic journey has entered a new phase, not because a structural container has been filled.
- The Novel-Parts of a Section collectively develop the Section's arc in a way that feels like a single sustained experience of escalating depth.

#### 1.3.4 — Novel-Part Transitions

Novel-Part transitions follow the same principle as all structural transitions in this hierarchy: they begin **thematically as the story demands** after the previous Novel-Part ended in its thematic journey. No Novel-Part begins with a narrative clean-slate. It always inherits the emotional residue, the unresolved tensions, and the character states that the previous Novel-Part produced.

---

### Tier 4 — Chapter

#### 1.4.1 — Definition

A Chapter is the fourth structural tier and represents a **continuous narrative unit** — the largest structural unit in which the narrative is experienced as a single, unbroken reading experience. A Chapter has a beginning condition, a developing middle, and a closing condition. It is not closed until **narrative closure is achieved**.

#### 1.4.2 — Narrative Closure

Narrative closure does not mean resolution or happiness. It means the Chapter has reached a state in which the reader experiences a meaningful pause — a moment of consequence, revelation, transformation, transition, or resting tension that completes the immediate narrative thread. A Chapter may close on:

- A victory and its cost
- A defeat and its emotional aftermath
- A revelation that recontextualizes everything preceding
- A departure or arrival
- A moment of quiet after sustained intensity
- A cliffhanger whose immediate emotional charge has peaked

A Chapter does not close mid-tension, mid-action, mid-conversation, or mid-realization. It closes when the reader has been delivered to a complete experiential moment, even if the broader story is unresolved. How a Chapter's close is shaped as a hook, and how Chapter closings vary from one Chapter to the next, is governed by Part 36's Chapter and Area Openings, Closings, Hooks and Recaps Area.

#### 1.4.3 — Chapter Length

There are no artificial limits on Chapter length. A Chapter is as long as its narrative unit requires. A Chapter that ends early because of a perceived length limit has violated narrative closure. A Chapter that continues past its natural closure point because of a perceived length requirement has violated pacing. Length is always a function of story.

#### 1.4.4 — Inter-Chapter Relationships

A Novel-Part must feel whole. Wholeness requires **thematic relationships between Chapters within the same Novel-Part**:

- Each Chapter must continue the thematic development established by the previous Chapter.
- The transition between Chapters must carry thematic momentum — the new Chapter begins from the emotional state in which the previous Chapter left the story.
- Chapters within a Novel-Part collectively develop its thematic arc in a sequence of escalating or deepening narrative units.

#### 1.4.5 — Chapter Transitions

Every Chapter begins **thematically as the story demands** after the previous Chapter ended in its thematic journey. No Chapter begins as if the previous Chapter did not occur. The opening prose of every Chapter must be oriented in the emotional, psychological, and situational reality established by the previous Chapter's close. How the opening of a Chapter re-enters the reader (what is recalled, how much, and how without an information dump) is governed by Part 36's Chapter and Area Openings, Closings, Hooks and Recaps Area. The variety of Chapter openings is governed by the same Area; the openings of Areas follow Rule 1.5.6.

---

### Tier 5 — Area

#### 1.5.1 — Definition

An Area is the fifth and final structural tier and the unit in which the novel is written. It is a **Plot and Context Unit** within a Chapter: it defines the boundary of a discrete narrative event — what happens, why it matters in the context of the story, and who is involved — and it is the unit in which the novel is drafted, audited, confirmed, scored and filed. An Area may be a complete scene: one dramatic movement, in one place and one continuous stretch of story time, that opens on a situation, puts it under pressure, and closes on an altered or deliberately open one. Or a scene may continue across consecutive Areas of the Chapter, each Area carrying one written portion of it (Rule P2-Area-6). An Area never holds two scenes: a new scene begins in a new Area, when the dramatic movement has closed, when the place changes (other than along one unbroken passage, such as a chase or a march), or when story time breaks by more than the brief skip Rule 6.3.5 allows. Every Area is written to one of the three size targets of Rule P2-Area-7.

#### 1.5.2 — Area Function

An Area is the written unit of the novel in the Area-built path (`/next-area`). **[Amended 2026-10-07]** The Chapter is a second lawful written unit: a Chapter whose Chapter Spec carries `Build mode: whole` is drafted, audited, confirmed and written whole by `/create-chapter`, with no Area files (Rule 6.3.4a). This is a new rule, not an exception: a Chapter is built by Area or whole, never both, and the Area stays the written unit of `/next-area`. In a Chapter built whole the Area blocks of the Chapter Spec are the plan units and the hidden markers of Rule 6.3.4a are their only trace in the written file. The function of an Area is to:

- Define with precision what narrative event is occurring within its span.
- Establish who is present, where the action is located, and what the stakes of the event are.
- Ensure that the Chapter's total plot requirements are accounted for across its complete set of Areas.
- Provide the author (and the canon audit system) with a clear unit for tracking narrative completeness.
- Serve as the unit over which the standards of this canon are counted and reviewed (over the Area window where a rule reads the scene, Rule P2-Area-1).

An Area is not a summary of what happens. It renders the situation, the people and the movement at full literary depth. All structure above the Area exists to place the reader in the best possible position to receive each Area. The Area is where the novel is made: it is not a sketch, a placeholder, or a draft. Every Area is final-grade literature executed at the highest achievable standard.

#### 1.5.3 — Area Sequencing

Areas within a Chapter must **flow sequentially**. This means:

- Area 2 of a Chapter begins from the narrative position where Area 1 ended, or from a cut that the chapter spec plans (Rule 1.5.6).
- No Area may skip over narrative events required for continuity. If Event B follows Event A, there must be an Area that contains Event A and a subsequent Area (or the same Area) that contains Event B, with no unplanned narrative gap between them; a break that the chapter spec plans is not a gap (Rule 1.5.6).
- A closed Area is never reopened. The narrative moves forward, and it may return to an earlier thread in a new Area when the chapter spec plans the return (Rule 1.5.6).

#### 1.5.4 — Area Count

There can be as many Areas in a Chapter as the Chapter's plot requires to be completely and correctly executed. A scene may take one Area or several consecutive Areas. A single-Area Chapter is valid if the Chapter's narrative event fits one Area. A many-Area Chapter is equally valid if the Chapter requires many. There is no artificial limit. The Area count is recorded in the Chapter Spec (Part 38).

#### 1.5.5 — Area Size, Area Window and Unit of Count

**Rule P2-Area-7 — Area Size.** An Area is written to one of three size targets: **1,600, 1,800 or 2,000 words**. The Chapter Spec decides the target of each Area (Part 38). Each target holds a 20 percent variation on both sides (1,280 to 1,920 around 1,600; 1,440 to 2,160 around 1,800; 1,600 to 2,400 around 2,000), and together the three bands make one passing range for every Area: **1,280 to 2,400 words**. A count outside 1,280 to 2,400 words is a blocking finding: the write waits for the author to confirm the Area or send it back. The finding reports the word count, counted by the method of Part 35 Area 4.5. A figure inside the range is never a reason to pad an Area or to trim it. Size is the one structural limit that blocks; pacing is not (a pacing difference from the Chapter Spec is shown and never blocks). Size has no tie to pacing: the pacing and the size target of an Area are two separate fields of the Chapter Spec, and neither is derived from the other. A letter, an epigraph or a song lives inside an Area and does not take an Area of its own. The date line (Rule 6.3.2b) is not narration: its words are left out of the size, and no Area is lengthened or shortened for it. No counting code is added: the auditor reads the size.

**Rule P2-Area-1 — The Area Window.** The Area window is the read set of an Area: the Area under audit, the Area before it, and the earlier Areas of a scene that continues across Areas. This rule defines it once, and every other file points here. Standards of this canon that are stated for the scene, or counted per Area, run over the Area window. Where a rule needs the whole scene and the scene continues across consecutive Areas, the Areas of that scene are read in order. The Area before the Area under audit is read before drafting (Rule P2-Area-2); an Area of an earlier, different scene beyond that previous Area is not part of the window. The span of days that an Area covers is never called a window: it is called the Area's dates.

**Rule P2-Area-1a — The Unit of Count.** A count that a rule of this canon sets per scene runs over the Area under audit together with the earlier Areas of its scene when the scene continues across Areas (the Area window of Rule P2-Area-1, read as the scene, and without the previous Area when that Area belongs to a different scene): the countable elements 19-1 to 19-5 of Check #19 and the scene counts of Part 29 Rules 29.4.4.2 to 29.4.4.4 are such counts. Where a count exempts the scene-final paragraph, that paragraph is the last paragraph of the Area under audit. This rule supplies the unit; the rule that sets a count keeps its own figure. The date line (Rule 6.3.2b) is not narration and is no paragraph for any count of this rule: it is left out of every count, and it is neither the scene-final paragraph nor the first paragraph of an Area for any reading in this canon; the opening paragraph of an Area is its first paragraph of narration, the one after the date line.

#### 1.5.6 — Inter-Area Continuity

Each Area begins where the last ended, or from a cut that the chapter spec plans, so that the Chapter feels whole and complete. An unplanned disjoint between consecutive Areas (an unexplained gap in time, location, thread, or character state) is a failure of this rule; a planned cut is not a disjoint. If a transition in time, location, or character state occurs between Areas, that transition must be produced by the closing lines of the preceding Area or the opening lines of the new Area.

The chapter spec's Area block (Part 38) records what the rules below use: the opening type, the closing type, the size target, the pacing, the continuation (a complete scene or a scene that runs on, Part 38 Rule 2.4.6), the viewpoint, the carry-over from the previous Area, and the thread or storyline. The rules below govern how Areas connect.

**Rule P2-Area-2 — Every Area Knows What Came Before.** A new Area begins from the state the previous Area left: who is where, what each person knows and feels, what is still open. An Area that opens an unrelated scene does not contradict or ignore that state. The carry-over is recorded in the Area block, and the Area is drafted after the previous Area has been read.

**Rule P2-Area-3 — Planned Cuts.** A break in time, place or thread between consecutive Areas is lawful when the chapter spec plans it in the Area block. A planned cut may go forward in time, to another place, to another thread, back to an earlier thread (which resumes from where its own last Area left it), or to an earlier time (a memory, dream, vision or flashback scene, which takes its own Area and is rendered under Part 36's rules for such scenes). A cut may open a scene that is unrelated in content to the one before it, as part of the larger story the spec plans. The opening lines of the new Area ground the reader in when, where and whose thread. An unplanned break is a failure of Rule 1.5.6.

**Rule P2-Area-4 — An Area May Close Open.** An Area closes when its dramatic movement, or its written portion of the movement, is complete. It may close on an altered state, or on a cliffhanger or an open question, as the Area block's closing type plans. An open close is a chosen close: the story means to keep the question, and the next Area is planned to receive it or to cut away from it under Rule P2-Area-3.

**Rule P2-Area-5 — Openings Vary.** Two consecutive Areas do not open the same way unless the chapter spec says so. The test is the opening type recorded in the Area blocks; whether two openings feel the same is judged by the Area flow review (Check #16, dimension 16-J). An Area that continues the previous Area's scene (Rule P2-Area-6) opens in motion by that rule, and the opening type the spec records for it says so.

**Rule P2-Area-6 — Area-to-Area Carry-Over.** An Area is the written unit. It may be a complete scene, or a scene may continue across consecutive Areas of the Chapter, and the Continuation field of the Chapter Spec's Area blocks (Part 38 Rule 2.4.6) says which. An Area that continues the previous Area's scene opens in motion from the exact state the previous Area left: the same place, the same moment, the same register. It does not re-establish the setting, recap the Area before it, re-introduce people who are already present, or open as if a new scene were starting. An Area that continues a scene ends on live tension: a question unanswered, an exchange or a fight in progress, an action under way, a decision pending, a line not yet met. The first line of narration of the next Area takes that tension up: it answers, deepens or turns it. An Area that completes its scene closes at the closing type the spec plans (Rule P2-Area-4). The date line that opens every Area (Rule 6.3.2b) is no second opening: it is a plain italic paragraph of the Area's own text, and where an Area continues the previous Area's scene, no time has passed between them, so it normally repeats the line of the Area before (Part 41 Area 5, The date line). Where this rule speaks of the first line of an Area, it means its first line of narration, after the date line.

---

### 1.6 — Writing Standards for the Area

The sections below set the standards every Area is written to. Their section numbers are stable for cross-reference. Every section of Area 1 carries the prefix 1. (tier sections 1.1.n to 1.5.n, writing standards 1.6.n), so that no bare number of Area 1 repeats a number of Areas 2 to 10; a citation of a section of Area 1 writes the full number, and a bare Rule 4.3, 4.4, 5.x or 6.x always means Areas 4, 5 and 6.

#### 1.6.2 — Area Depth and Pacing Mandate

Every Area must be written at **full prose depth (Part 28 Area 4: Named Depth Pillars DP-1 through DP-10 simultaneously mandatory at all pacing levels; pacing is decided per Area in the Chapter Spec and recorded under §1.6.2.1, and the size of an Area is Rule P2-Area-7).** This is not a metaphor for "write well." It is a specific operational standard defined by the following requirements, every one of which is mandatory regardless of pacing category, the Named Depth Pillars being weighed on the Area window (Rule P2-Pacing-1). Immersion in an Area is achieved only when every unit of canon information within it satisfies the **Contextual Earning Law (Part 28 Area 15)**. Sensory precision, tonal fidelity, and depth of rendering are necessary but not sufficient conditions for immersion. Information that is accurate but unearned breaks immersion as surely as information that is tonally wrong.

**Named Depth Pillars at all pacing levels:** The ten Named Depth Pillars (DP-1 through DP-10, Part 28 Area 4) remain simultaneously mandatory regardless of pacing category. At fast pace the depth is expressed in concise, concentrated form — the mandate does not change, only the canvas. Compression in fast-paced prose means concision and efficiency; it never means omission of any of the ten pillars. The pillars are weighed on the scene, the Area window, as Part 28 Area 4.2 sets (Rule P2-Pacing-1).

**Three standing prohibitions:**

- **No Range Descriptions.** Prose does not describe what a scene is approximately like. It describes exactly what is happening, with sensory precision, physical detail, and experiential immediacy. "He was powerful" is forbidden. "The weight of his presence compressed the air around him, and she felt her own cultivation instinctively recoil, a cold, involuntary retreat of her qi like smoke before a flame she could not see" is correct.

- **No Shortcuts.** Prose does not skip events, compress them into summaries, or bracket them with ellipses of implication. Every moment that matters happens on the page. If a negotiation is critical to the plot, the reader witnesses the negotiation. If a walk through a hostile district matters, the reader walks it with the character. A moment that does not matter may be carried by a line of summary or a Rule 6.3.5 time skip.

- **No Tonal Collapse.** The prose voice must remain sustained and consistent within an Area. A scene of profound tension does not suddenly lapse into flat description. A scene of quiet melancholy does not abruptly adopt an action-prose rhythm. The tone is established by the scene's emotional context and held throughout.

##### 1.6.2.1 — Pacing Vocabulary

Every Area carries one of three pacing categories. The Chapter Spec decides it when the Area is planned (Part 38), and the writing of the Area carries that value. The pacing category says how the scene moves. It is the vocabulary the spec records, not a rule on the size of an Area: pacing and the size of an Area are two separate fields of the Chapter Spec (Rule P2-Area-7).

**The Three Pacing Categories:**

| Pacing Category | Narrative Character |
|---|---|
| **Fast** | High-momentum, action-driven, rapid exchange; information delivered at speed; depth expressed through concision |
| **Medium** | Balanced passage; dialogue-rich, mixed interiority and event; standard narrative pace |
| **Slow** | Deliberate, immersive; world-building, character establishment, psychological depth, cultivation milestones |

**Pacing Determination:** The pacing of an Area is determined in the Chapter Spec from the content type of the scene, using the Anchor Type Defaults table below and organic narrative assessment, and the author confirms it with the spec.

**Gate 1 Pacing Line (Rule P2-Pacing-2):** The Gate 1 Position Header carries the pacing line immediately below the Area title, read from the Chapter Spec:
> **Pacing: [Fast / Medium / Slow]**

**Anchor Type Defaults:**

The following content types have canonical default pacing assignments, offered as the recommended value when the Chapter Spec records an Area's pacing. Mixed-content scenes use the dominant content type as the primary determinant; the spec may adjust by one tier when a scene's secondary content significantly shifts the balance.

| Content Type | Default Pacing | Rationale |
|---|---|---|
| Pure combat / active battle sequence | **Fast** | Maximum momentum; depth through action precision |
| Chase sequence / physical pursuit / flight | **Fast** | Urgency governs; sensory compression required |
| Travel / journey montage | **Fast** | Coverage of ground without dwelling; environmental depth in efficient passes |
| Diplomatic / bilateral session / formal court exchange | **Medium** | Multi-register dialogue; political subtext; character positioning |
| Character interior / psychological depth scene | **Medium** | Interiority requires space but not the full slow render |
| Social / domestic scene / casual interaction | **Medium** | Relationship texture at standard pace |
| Information reveal / intelligence gathering / intrigue | **Medium** | Strategic disclosure requires care but not full-slow immersion |
| Tactical planning / strategic deliberation | **Medium** | Dialogue and interiority balanced; planning texture important |
| World / location establishment (first full rendering) | **Slow** | Immersive world-building; sensory + cultural + historical depth required |
| Cultivation breakthrough / awakening / realm milestone | **Slow** | Identity-level transformation; full psychological + physical rendering |
| First on-page appearance of a major character | **Slow** | Character establishment; voice, interiority, physical presence all required |
| Phase-climax or saga-turning confrontation | **Slow** | Maximum depth; milestone scene |
| Opening Area of a chapter or section | **Slow** | Setting, register, and world state must all be established |

**Rule P2-Pacing-1 — All 10 Named Depth Pillars at All Pacing Levels:** The Named Depth Pillars DP-1 through DP-10 (Part 28 Area 4) remain simultaneously mandatory at all pacing levels, weighed on the scene, the Area window (Rule P2-Area-1), and not paragraph by paragraph (Part 28 Area 4.2). A paragraph or an Area may be quiet as Part 28 Area 4.5 allows, because the Area window carries every Pillar. Fast-paced prose expresses each pillar more efficiently — the sensory detail is sharper, the interiority more concentrated, the cultural texture compressed into specific action — but no pillar is omitted from the scene. A combat scene must still carry, across its Area window, psychological ground, ideological texture, relational weight, environmental specificity, historical resonance, power honesty, consequence threading, authentic voice, and cultural embeddedness, and a concrete sensory anchor in every Area whose block sets the Sensory anchor field to required (Part 38 Rule 2.3.5a; Part 36 Area 9.3). The compression is in execution, never in coverage.

**Rule P2-Pacing-2 — The Position Header Shows the Spec's Pacing:** The pacing category of the Area appears in every Gate 1 Position Header Block, read from the Chapter Spec's Area block. The fields of the Position Header Block are defined once, in the Gate 1 Chat Delivery format of `.claude/guardrails/commands/guardrail-command-law.md`; this Part adds only the pacing line and the chat-only boundary of Rules 6.7.1 and 7.7.1. The pacing line carries the category alone: no immersion percentage. A header without the pacing line is a Gate 1 audit failure.

**Rule P2-Pacing-3 — Pacing Is Decided in the Chapter Spec:** The pacing of every Area is decided in the Chapter Spec, with the author, when the spec is built or revised. The writing of an Area carries that value: no pacing question is asked at Gate 1 or at the Decision Consultation Gate (Part 28 Area 19). A different pacing is a revision of the Chapter Spec through the spec's own revision path (Part 38), not a decision of the writing session.

---

#### 1.6.3 — Mandatory Area Elements

The following elements must appear in every Area where they are contextually relevant. This does not mean every element appears in every Area — it means that when the context calls for them, they may not be omitted:

- **Dialogue:** Conversations happen on the page. Characters speak to each other in full, contextually grounded exchanges. (Full rules in Area 2.)
- **Lore Depth:** The world's history, systems, and knowledge are woven into the prose through character awareness, environmental observation, and narrative voice. Lore is not dumped — it is revealed through the story as the story requires it.
- **Armor, Clothing, and Equipment:** When a character's physical presentation matters — in combat, in formal encounters, in social contexts — their armor, clothing, insignia, weapons, and tools are described with specificity. Names, materials, cultural significance, and functional purpose are embedded in the description.
- **Weapon Names and Usage:** Named weapons are identified by name. Their usage — grip style, draw, technique, weight, cultural history, the specific way a character has adapted to them — is rendered with precision.
- **Canon Information Delivery:** All canon information delivered in prose — power levels, classification vocabulary of every category, location references, faction references, relationship state, cultural detail, mechanics, and any other canon fact — must pass the **Three-Beat Test defined in Part 28 Area 15.4**. The **Heavenly Scale sensory system (Part 3 Area 3.3)** remains the canonical delivery mechanism for cultivation-power encounter and is the preferred register whenever power is sensed rather than named. Raw numerical multipliers remain prohibited without exception. Information that is tonally correct but scene-standalone is a violation of the Contextual Earning Law regardless of its technical accuracy. Explicit naming of any classification is permitted only as a Section 15.5 "consequential naming" subcase — where the naming itself does scene-work.
- **Psychology and Emotional State:** Every character's internal world — what they feel, what they fear, what they want, what they are concealing, what they are discovering about themselves — is present in the prose. Psychology is not told. It is rendered through action, micro-behavior, dialogue subtext, and physical sensation.
- **Cause and Consequence:** Every event in an Area produces effects. Those effects begin to manifest within the same Area when narratively appropriate. Consequence is not deferred indefinitely. If a character makes a choice that changes the world, the world begins to respond within the scene.
- **Discovery and Realization:** When a character learns something, understands something they previously misunderstood, or realizes the true nature of a situation or person — that moment is given full narrative weight. Discovery is not a parenthetical. It is a scene.
- **Combat:** When combat occurs, it is rendered with the full combat prose standard defined in Area 3. Combat is never compressed, skipped, or summarized.

#### 1.6.4 — Area Continuity

Every Area relates to the Area before it as Rule 1.5.6 and Rule P2-Area-6 set. The narrative must maintain continuous flow. Where an Area continues the previous Area's scene, there is no disjoint between them — no unexplained gaps, no sudden changes in location or character state without transitional grounding, no tonal discontinuities — and the reader can read those Areas in sequence and experience one unbroken scene. Between Areas of different scenes, a cut that the chapter spec plans is not a disjoint (Rule 1.5.6). The story always moves forward from a concrete narrative position. A POV change at an Area boundary under Rule 4.3 is a lens change, not a scene break: where the Area continues the previous Area's scene, every obligation of Rule P2-Area-6 applies to it in full.

**Worked sample, a good carry-over and a bad one (illustration only).** The figures are unnamed and the scene is invented. The labels "End of the first Area" and "Start of the next Area" are annotation; in the files each Area carries its Area Title Block and its date line (Rules 6.3.2a and 6.3.2b), which the samples leave out.

*A good carry-over.*

End of the first Area:

> *"Open it,"* the clerk said again, and held out his hand for the key. She did not move. The key was warm from her palm, and behind the door something knocked once, softly, as if it had heard its name.

Start of the next Area:

> She put the key into his hand. *"Quickly, then,"* he muttered, and turned it, and the knocking came again, closer, from lower down than a hand could reach.

The first ends on live tension: a decision pending and a sound at the door. The second takes the tension up in its first line, answers the pending decision and turns the sound, and it enters in motion without re-describing the room or the people (Rule P2-Area-6).

*A bad carry-over.*

End of the first Area:

> In the end she gave him the key, he opened the door, they looked inside and found nothing, and the matter was over. Everyone relaxed.

Start of the next Area:

> The cellar under the customs house was cold and smelled of tar. The clerk, who had kept the keys for twelve years, stood in the doorway beside the girl from the river town, and the two of them had come down at dusk with a single lamp.

The first closes the matter, so there is nothing for the next Area to take up. The second is a forbidden second opening: it re-establishes the place, re-introduces two people who are already present and recaps how they arrived, as if a new scene were starting. The fault is in the writing, not in the files. An Area that opens a new scene may establish the place and the people; an Area that continues a scene may not do it again.

---

## Area 2 — Conversation Rules

### 2.1 — Mandate

Dialogue is not decoration. It is one of the two primary instruments of the novel, written in plain, clear words — the other being interior prose (plain vocabulary, 2026-10-06). Every scene involving characters who are capable of speech and are in a position to speak must contain dialogue unless the narrative context renders silence itself the meaningful choice (which must then be rendered with the same depth as speech).

Minimal dialogue is a structural failure. Repetitive dialogue is a creative failure. Both are forbidden.

### 2.2 — Dialogue Formatting

**Rule 2.2.1 — Embedded in Paragraphs.**
Dialogue must be embedded within prose paragraphs. It is woven into the fabric of description, action, and interiority. Dialogue is never isolated as standalone lines without context. Before, within, or after each spoken exchange, the paragraph contains physical detail, psychological observation, environmental response, or some combination of these. The speech act is part of a complete experiential moment.

**Rule 2.2.2 — Written in Double Quotation Marks AND Italics.**
All dialogue is formatted in **double straight quotation marks AND italics simultaneously**. The canonical rendering is *"the exact spoken words"* — the double quotation marks and the spoken text are all rendered inside the italic span. This applies to direct speech of any length, from a single word to an extended speech of multiple paragraphs. Italics-only dialogue (no quotation marks) is a Rule 2.2.2 violation; double-quoted dialogue with no italics is a Rule 2.2.2 violation; single quotation marks for primary direct speech are prohibited (single quotes are reserved for quoted speech nested inside another character's spoken line, per Part 29 Rule 29.2.1.1a). Thought presented as interior monologue may also be italicized at the author's discretion, but interior monologue does NOT take double quotation marks; only spoken dialogue is double-quoted. This rule is jointly governed with Part 29 Rule 29.2.1.1 and both must be simultaneously satisfied. For a speech of several paragraphs, see the worked sample under Rule 7.2.5. The name of a named item inside the speech is set in roman, by the break described in Part 28 Rule 20.8.2(c); every other word of the speech stays double-quoted and italic.

*Pointer: plain-type channel speech forms are the one lawful exception to this rule — Part 29 Rule 29.14.3.3.*

**Rule 2.2.3 — No Script Format.**
Dialogue must never appear in script format — no character names followed by colons, no stage directions in brackets, no numbered exchanges. Dialogue attribution and context are handled entirely through prose convention: dialogue tags ("she said," "he demanded"), action beats (the character performing an action before or after speech), and contextual description (the environment responding to the speech act).

### 2.3 — Dialogue Content Requirements

**Rule 2.3.1 — Frequency.**
Conversations must be frequent within scenes involving multiple characters. The narrative must not spend extended passages in pure narration or action without incorporating the spoken voices of the present characters. When characters are together, they speak — unless silence is itself the point and is rendered accordingly.

**Rule 2.3.2 — Inclusion of All Characters.**
Dialogue must include all characters present in the scene who are relevant to the scene's events — heroes, antagonists, minor figures, mentors, rivals, bystanders who carry narrative weight. A scene in which only the protagonist speaks while others listen passively is a scene of failed characterization. Every present character has a voice, a perspective, and a reason to speak.

**Rule 2.3.3 — Emotional and Contextual Range.**
Dialogue must reflect the full spectrum of human communication. Within a given scene, dialogue may and should carry multiple of the following functions simultaneously or in rapid sequence:

- **Emotion:** Joy, grief, rage, love, contempt, tenderness, envy, despair, relief — genuine emotional states expressed through speech.
- **Conflict:** Disagreement, argument, struggle for dominance, ideological opposition, personal grievance.
- **Misunderstanding:** Characters hearing what they expect rather than what is said. Assumptions that reveal character. Crossed purposes that reveal the gulf between people.
- **Authority:** The language of rank, command, deference, challenge to power, the subtle assertion of superiority.
- **Fear:** Concealed dread, false confidence, the way fear reshapes what people choose to say and not to say.
- **Humor:** Wit, irony, dark comedy, gallows humor, teasing, the laughter that survives even terrible circumstances.
- **Doubt:** The hesitation before a hard truth, the question that reveals uncertainty, the statement that asks for reassurance without admitting it needs it.
- **Revelation:** Speech that changes what the listener believes. Confessions, accusations, truths delivered at the wrong moment.
- **Negotiation:** The bargaining of power, the careful dancing around what is really wanted.
- **Subtext:** What characters mean beneath what they say. What they will not say directly. The conversation beneath the conversation.

No scene's dialogue should be tonally flat or confined to a single register. Dialogue breathes because people breathe — with complexity, contradiction, and the full weight of who they are.

**Rule 2.3.4 — Prose Depth Match.**
Dialogue must match the depth of the surrounding prose. A scene written at full prose depth (Part 2 Area 1 §1.6.2) cannot contain functional, expository dialogue that serves only to convey information. Every line of dialogue must carry the scene's emotional charge, reveal character, advance conflict, or layer subtext — ideally multiple of these at once. The test is the exchange, not the single line: a plain functional line (for example, "Close the door.") is lawful when the exchange around it carries that charge.

**Rule 2.3.5 — Context-Driven Speech.**
All dialogue is governed by the full context of the scene: the characters' history with each other, their current emotional states, the political or social setting they are in, the stakes of the moment, and what each character knows, suspects, and is concealing. Speech without context is placeholder. Speech arising from full context, in plain and clear words, is what the novel needs (plain vocabulary, 2026-10-06).

**Rule 2.3.6 — Dependency on Part 29.**
When dialogue is written, it must satisfy the requirements of **Canon-Part 29 — Dialog and Social Interaction Law** in addition to the rules of this Area. Canon-Part 29 governs tone registers, speech pattern variation by character type, cultural and social formality rules, and the mechanics of how conversation shapes and reflects the social world. This Area (Part 2, Area 2) governs formatting and frequency. Canon-Part 29 governs voice, content, and social authenticity. Both must be simultaneously satisfied. Part 29 Rule 29.2.1.7 (Canon Amendment 2026-10-08) asks that speech be natural and flowing: sentence length varies, the moment sets the manner, and clipped, formulaic, tally-like or report-form speech is a fault.

**Rule 2.3.7 — Novel-Wide Punctuation and Register Prohibitions (Em-Dash; Contractions Anywhere).**
All Area body text written under this Part, dialogue and narration alike, is subject to the categorical em-dash prohibition (Part 29 Rule 29.2.1.1b). Narration and dialogue alike are also subject to the contraction prohibition (Part 29 Rule 29.2.1.1c; Canon Amendment 2026-10-16 reversed the dialogue allowance of 2026-10-08). Part 29 owns the substitution list, the expansion list, the definition of the body text the prohibitions cover, and the governance-artefact exemptions; the Gate 1 audit and the Post-Write Audit (`.claude/guardrails/audit/guardrail-audit-gate-law.md`, the gate law) both FAIL if the em-dash character is found in the Area body or a contraction is found anywhere in the Area body.

---

## Area 3 — Combat and Move Rules

### 3.1 — Mandate

Combat is not a pause in the novel. It is one of the novel's primary modes of meaning-making. A fight scene reveals character, tests ideology, establishes consequence, and renders the world's power systems in living, visceral reality. Combat prose must be executed at the same pacing-appropriate prose depth standard as every other Area (combat defaults to Fast pacing in the Chapter Spec, per Area 1 §1.6.2.1 Anchor Type Defaults), with additional specific requirements governing how it is rendered.

A combat scene that is unclear, rushed, consequence-free, or disconnected from the story's emotional and ideological context is a failed scene regardless of its technical action content.

### 3.2 — Move Name and Cultivation Level Formatting

**Rule 3.2.1 — Bold-Italic Move Names.**
All Named Moves, Named Techniques, and Named Cultivation Practice names (as defined by Canon-Part 6 Move Taxonomy Law) must be formatted in ***bold-italic*** at every point of use in the prose — both inside dialogue and outside dialogue. This applies to the first use and every subsequent use within an Area. The Markdown rendering is `***text***` (triple-asterisk); the docx rendering is character-level bold + italic simultaneously. The bold-italic serves two functions: it visually distinguishes canon-valid named techniques from general action description, and it signals to the reader (and to the audit system) that a named move governed by Canon-Part 6 is being invoked.

**Scope clarification:** Only proper canon-registered names receive bold-italic. Unnamed or generic references ("the sword form," "the morning form," "a cultivation technique," "the calibration") remain plain text until a proper canon name is established and registered. Once a name is established, every subsequent use of that specific name is bold-italic regardless of context. The coined name of a made or used thing that is not a move, a named item, is never bold-italic; it is set in plain italic, and in roman inside an italic passage, by Part 28 Rule 20.8.2. Named Relics and Artifacts are named items and are set in plain italic under Part 12 Rule 2.2.3; the article is never part of a name.

**Rule 3.2.1a — Bold-Italic Cultivation Level Designations.**
Four categories of cultivation level designations that appear in prose must be formatted in ***bold-italic***:

- **Full realm+level+sub-level strings:** The complete designation including realm name, level number, and sub-level — e.g., ***Ruler Level 3 Mid***, ***Champion Level 7 Peak***, ***Warrior Level 1 Low***. Formatted whenever the full string appears.
- **Full affinity+level designation strings:** The complete affinity designation including affinity name and level number — e.g., ***Swords Affinity Level 3***, ***Fire Affinity Level 5***. Partial affinity references without a level number ("the Sovereignty affinity," "the Sovereignty circuit," "Sovereignty-Swords affinity" without level number) are plain text.
- **Tier designations:** Mortal Tier labels with or without stage qualifiers — e.g., ***Mortal Tier 2***, ***Mortal Tier 1 Skin Stage***, ***Mortal Tier 1***.
- **Named meridian designations:** Proper names of meridian roots and named meridian structures — e.g., ***Void Root***. Generic structural terms ("the circuit," "the meridian pathway," "the dantian") are plain text.

**Standalone realm names** (e.g., Champion, Warrior, Ruler, Monarch, Champion-realm, Warrior-realm) are **plain text in all prose contexts** — whether characterizing a person's cultivation level ("a Champion-realm cultivator"), describing a technical power specification ("Champion-realm energy density"), or marking a historical milestone ("the Warrior breakthrough"). Only full realm+level strings qualify for bold-italic.

**Rule 3.2.2 — Name Authenticity.**
Move names used in an Area must be canon-valid — they must either exist in the established canon or be created in compliance with Canon-Part 6's naming conventions and tier classifications. A move cannot be invented mid-scene without retrospective canon registration.

**Rule 3.2.3 — Move Description Requirement.**
Every time a named move is used in combat, its effect must be described in the prose with sufficient specificity that the reader can perceive what the move does, how it operates, and what distinguishes it from general action. The name alone is not the combat. The name is the anchor for the full physical and energetic description that follows.

### 3.3 — Mandatory Combat Elements

Every combat scene must contain all of the following elements, rendered at full narrative depth. The four are weighed over the whole fight, the Area window (Rule P2-Area-1), and not in every combat Area: where a fight continues across consecutive Areas, the Areas of that fight are read in order, and each Area still serves the fight and carries at least one beat of it. Movement, Intent, Reaction and Consequence appear across the fight.

**Rule 3.3.1 — Movement.**
Combat is physical. The bodies of combatants move through space with specific intent and specific consequence. Footwork, repositioning, the claiming or surrendering of ground, the use of terrain and elevation, the distance management that separates survival from defeat — all of this must be rendered in the prose. A combat scene in which characters simply stand in place and exchange power blasts has failed the movement requirement. The physical space of the fight is a dynamic battlefield and the prose must make it live.

**Rule 3.3.2 — Intent.**
Every action in combat has a purpose beyond hitting the opponent. A character's strategic intent — what they are trying to achieve, what outcome they are working toward, what they fear and how that fear shapes their choices — must be legible in the prose. Intent is rendered through the character's internal voice, through their choice of technique, through their body language and micro-decisions, and through the way their actions reveal who they are as a fighter and as a person.

**Rule 3.3.3 — Reaction.**
Combat is not one character performing while the other waits. Every action produces a reaction — in the opponent, in the environment, in bystanders, in the combatant who acted. Reactions must be rendered with the same precision as actions. The opponent's dodge, block, counter, or failed evasion. The psychological response to a devastating blow received or delivered. The environmental consequences of power discharge. Reaction is what transforms a sequence of actions into a fight.

**Rule 3.3.4 — Consequence.**
Every exchange in combat produces consequence. Health is damaged. Energy is depleted. Confidence shifts. Fear enters or leaves. Strategy evolves. Ground is gained or lost. A combat scene in which the characters exchange a dozen moves and emerge in identical states to how they entered has violated the Consequence Rule. Every exchange must change something — even if the change is subtle, even if the character refuses to let it show.

Consequence extends beyond the combat itself. A fight has aftermath. Bodies bear marks. Minds bear impressions. Relationships between combatants are altered. The world around the fight has been changed by the power that moved through it. These post-combat consequences must be rendered in the Area window, or in the first Area that follows when the chapter spec plans that carry-over.

**Rule 3.3.5 — Valid Combat Outcomes.**
The following outcomes are fully valid in combat prose and may not be avoided for the sake of narrative comfort or character protection:

- **Fainting / Loss of Consciousness:** A character who is overwhelmed, exhausted, or struck beyond their endurance threshold may faint, collapse, or lose consciousness. This is a real and consequential combat outcome.
- **Death:** Characters may die in combat. Death is not a narrative failure — it is one of combat's authentic possibilities. When a character's death is canon-valid (compatible with Part 27 — Consequence Law and Part 5 — Combat and Fight Law) and within the Content Limits (Part 28 Area 12.3), it must not be avoided for emotional convenience.
- **Retreat:** A character may choose to retreat, disengage, flee, or surrender. Retreat is not weakness — it is a strategic decision with its own psychological and narrative weight. Retreat must be rendered with full consequence: the cost of leaving, what is abandoned, how it is perceived by others and by the retreating character themselves.
- **Collateral Damage:** Power released in combat affects the world. Structures collapse. Bystanders are threatened or harmed. The environment is scarred. Collateral damage is not background noise — it is part of the real cost of the fight and must be rendered in the prose.

**Rule 3.3.6 — Dependency on Part 5 and Part 6.**
All combat in an Area must satisfy the requirements of **Canon-Part 5 — Combat and Fight Law** and **Canon-Part 6 — Move Taxonomy Law** in addition to the rules of this Area. Canon-Part 5 governs: force legitimacy classification (combat vs assault vs assassination vs accident), escalation tier of the conflict being depicted, engagement recognition (when and how engagement begins), intensity containment boundaries by tier, third-party and proxy combat legitimacy, protected zone compliance, victory and defeat classification (which of the six victory types and five defeat classifications applies), surrender protocol rendering, and retreat/withdrawal/flight distinctions. Specifically: a combat scene depicting a surrender must render the surrender unambiguously; a scene depicting retreat must classify which of the three retreat forms is occurring; a scene depicting a Formal Duel must establish which duel type is in play and whether witnesses are present. Canon-Part 6 governs the classification, naming, tier assignment, and correct usage of moves. This Area (Part 2, Area 3) governs prose formatting and narrative execution. All three sets of rules are simultaneously applicable and must be simultaneously satisfied: Canon-Part 5 and Canon-Part 6 bind every combat Area, and the four combat elements of Rule 3.3 are weighed over the whole fight. Additionally, any consequence of combat — injury severity, death, retreat — must comply with **Canon-Part 27 — Consequence Law**.

---

## Area 4 — Point of View Governance

### 4.1 — Purpose

Point of View (POV) determines the narrative lens through which the reader experiences each Area. Because immersion is the governing standard of all prose, POV management is critical — an inconsistent or unexamined POV breaks immersion and fragments the reader's experience.

### 4.2 — POV Consistency Within an Area

Every Area is written from a single, stable POV. Within an Area, the narrative perspective does not shift. The reader accesses interiority, perception, and emotional experience through one character's lens per Area. If two characters' interior experiences are both needed within one scene, the scene may pass the lens from one to the other at the boundary between two Areas (Rule 4.3); inside a single Area the Area prioritizes the POV that most serves the scene's emotional function, with the other character's interior state rendered through external observation (expression, body language, speech subtext). The sole exception is an Area expressly designated as a Dual-POV Area under Rule 4.3.1 — in every other Area, the single stable POV standard is absolute.

### 4.3 — POV Transition

When a shift in POV is narratively necessary, the transition is handled at a structural boundary — the boundary between two Areas within the same Chapter, or between Chapters. A POV shift within a single continuous Area remains a violation of immersion, except inside an Area expressly designated under the Rule 4.3.1 Dual-POV Area License. A deliberate POV shift at a structural boundary, handled with clear narrative signaling in the opening lines of the new Area, is valid. At the boundary between two Areas of one Chapter the shift is valid when the Viewpoint fields of the two Areas in the Chapter Spec record it (Part 38 Rule 2.4.7); a shift that the spec does not record is a deviation from the spec (Part 38, Check #18) and comes to the author. At a Chapter boundary the POV of each Area is already stated in the spec. A POV shift between Areas that carry one scene does not suspend Rule 1.6.4 Area Continuity or Rule P2-Area-6 — the new Area still begins where the last ended, in the same place and moment; only the narrative lens changes.

#### 4.3.1 — Dual-POV Area License

An Area expressly designated as a **Dual-POV Area** may carry exactly two POV characters, alternating at paragraph-level segment breaks. This is a bounded license, not a relaxation of Rule 4.2:

- **Designation is explicit and author-confirmed.** An Area is a Dual-POV Area only when the Chapter Spec marks a Dual-POV Area (Part 38, the Viewpoint field of the Area block) and the author confirms that spec at `[CONFIRM SPEC]`, or the author designates it directly during that Area's Decision Consultation Gate. The Area Maker never self-designates a Dual-POV Area.
- **Exactly two POVs.** Never three or more; both POV characters are named in the designation.
- **Segment integrity.** Each segment holds one POV at the full Rule 4.4 deep-POV standard; every alternation lands on a clear paragraph-level break with unambiguous narrative signaling of whose lens opens the new segment. Blending or head-hopping inside a segment remains a violation.
- **Audit standard.** Gate 1's deep-POV check evaluates a Dual-POV Area per segment: each segment internally stable and deep, every alternation marked and signaled, and the total POV count exactly two.
- **Pacing and size.** A Dual-POV Area's pacing and size target are those the Chapter Spec records for it, as for any other Area.
- **Intended use.** Paired-perspective scenes where two leads' simultaneous interiority is the scene's point — deliberate and rare; single-POV depth remains the novel-wide norm.

### 4.4 — Deep POV Standard

All prose is written in **deep POV** — meaning the reader is not told what a character thinks and feels from a distance but is placed inside the character's perceptual and psychological experience directly. Deep POV eliminates filter language ("she noticed," "he thought," "she felt") in favor of direct experiential rendering ("the air was wrong, too still, too careful, the silence of something holding its breath"). Deep POV is what produces full prose depth (Part 2 Area 1 §1.6.2). Shallow POV produces distance and weakens literature.

**Gate 1 Check #6 (filter language, advisory).** For each Area, Check #6 reports how many times the narration uses saw, heard, felt, noticed, realized, seemed, watched, wondered or thought to introduce what the point-of-view character perceives or thinks, in any tense, and lists those sentences. Each use counts once. Spoken dialogue is not counted, and neither is a verb that names a physical action (for example, she felt along the wall). The count is information only: it sets no line, and no figure fails or blocks an Area.

---

## Area 5 — Novel Output File Structure Law

### 5.1 — Purpose and Mandate

**Rule 5.1.1 — Output File Mandate.**
Every Area accepted into the canon and confirmed for file output must be written to its own dedicated per-Area file pair: a Word document (`area-NN.docx`) and a Markdown file (`area-NN.md`), stored in its Chapter folder on the nested narrative path `novel-starward-saga/phase-N/section-N/part-N/chapter-NNN/`. NN is the Area number within the Chapter, written with two digits. These per-Area file pairs are the **authoritative reader-facing substrate** of the novel-writing process — the novel itself at canonical resolution. Within a pair, the `.md` file is authoritative for the words and the `.docx` file for the formatting (Rule 7.1.2). They are distinct from the SSC Canon governance files (novel-writer folder), the Ledger files, and the derived Chapter file (a condensed text written by `/chapter-builder`) and the Phase/Novel compiled documents (which join Chapter files and are produced on demand only).

> **[Repo layout note]** `novel-writer` above refers to `.claude/skills/` in the current repo layout.

Within a single Gate 2 execution, the `area-NN.docx` and `area-NN.md` writes for one Area execute together as a coupled pair — the two files for a single Area are never allowed to drift apart during a successful Gate 2 run. **No chapter-level append model exists:** each Area inhabits its own file pair; the Chapter-level reading experience is a condensed Chapter file written on demand by `/chapter-builder` (via `chapter_builder.py`, from the Chapter's finished Areas, never by joining Area files), and the Phase-level and Novel-level reading experiences are built on demand by `/compile-phase` / `/compile-phase-md` and `/compile-novel` / `/compile-novel-md`, which only join the Chapter files. **[Amended 2026-10-07]** `/export-chapter` is retired and replaced by `/chapter-builder`.

**Rule 5.1.2 — Gated Trigger on Area Acceptance (per the gate law).**
The output file write is **mandatory upon Inter-Gate Confirmation** but is NOT automatic on acceptance alone. Every time an Area passes the Post-Output Audit of the gate law (`.claude/guardrails/audit/guardrail-audit-gate-law.md`), its Two-Gate sequence runs:
1. **Gate 1 — Chat Delivery** executes automatically and unconditionally, displaying the complete text of the Area in the conversation window, verbatim: never a summary, an excerpt or a file path. The complete text is printed at every Gate 1 and after every revision; when the audit raises a question to the author about the draft, the complete text is printed first and the question follows.
2. The **Inter-Gate Confirmation Prompt** is displayed; execution halts pending `[CONFIRM WRITE]`, `[REVISE AREA]`, or `[SKIP WRITE]`.
3. **Gate 2 — File Writes** runs only on `[CONFIRM WRITE]`. On that event, the Book Creation Law (Areas 6 and 7 of this Part) is triggered: the per-Area `.docx` (Area 6) and per-Area `.md` (Area 7) file pair is written at the Area's canonical path as a coupled write pair. Any missing folders in the `phase-N/section-N/part-N/chapter-NNN/` path are created before the file pair is written.
4. On `[REVISE AREA]`: the file write is held, the Area is revised, and the full audit re-executes on the revised Area, every check and the flow review of the Area window, before the complete revised text is delivered again at Gate 1.
5. On `[SKIP WRITE]`: the draft is discarded and nothing is written or updated: no file pair, no Ledger update, no spec update, no Completeness Indicator, no score. Files, Ledger and spec agree, and the next invocation drafts the same position again.

Part 2's Book Creation Law never triggers a file write independent of the gate law's Inter-Gate Confirmation. Any automatic-on-acceptance file write is a violation of the gate law and of Rule 5.1.2 simultaneously.

**Rule 5.1.3 — File System Authority.**
Part 2 Areas 5, 6, 7, 8 and 10 are the sole authority governing the structure, naming conventions, formatting standards, update protocols, and per-Area Completeness Indicator law for all novel output files. No other Part may define output file behavior. The commands that produce an Area (`/start-story`, `/next-area`, `/next-chapter`, `/next-part`, `/next-section`, `/next-phase`, `/revise-area`, `/redraft-area`, `/redraft-chapter`) trigger the per-Area output file write via this Part's law at Gate 2 of the gate law; the commands do not independently define the output behavior, and no command may bypass the Inter-Gate Confirmation defined by the gate law. Each invocation of a writing command writes exactly one Area (the One-Area-Per-Invocation rule of `.claude/guardrails/commands/guardrail-command-law.md`).

### 5.2 — Directory Structure Law

**Rule 5.2.1 — Root Output Folder and Nested Narrative Path.**
All novel output files are stored within the `novel-starward-saga` folder, located at the same directory level as the `novel-writer` folder and all Ledger folders. The `novel-starward-saga` folder is the root of all reader-facing novel output. Every accepted Area inhabits its own file pair at a nested path that mirrors the five-tier narrative hierarchy from Phase down to Area:

> **[Repo layout note]** `novel-starward-saga` above refers to `projects/novel-starward-saga` in the current repo layout.
> **[Repo layout note]** `novel-writer` above refers to `.claude/skills/` in the current repo layout.
> **[Repo layout note]** "Ledger folders" above refers to `.claude/story-memory/ledger-*/` in the current repo layout.

```
[workspace root]/
├── novel-writer/                         ← Canon governance (SSC Canon Parts)
├── ledger-character-hero/                ← Ledger system
├── ledger-character-villain/
├── ...
└── novel-starward-saga/                  ← Novel output (reader-facing per-Area files)
    ├── phase-1/                          ← Phase 1 output
    │   ├── phase-1-complete.docx         ← (optional) on-demand Phase aggregate via /compile-phase
    │   ├── phase-1-complete.md           ← (optional) on-demand Phase aggregate via /compile-phase-md
    │   ├── section-1/
    │   │   ├── part-1/
    │   │   │   ├── Chapter 001 - <Chapter Name>.docx  ← (optional) condensed Chapter file via /chapter-builder (Novel-Part folder, not chapter-001/)
    │   │   │   ├── Chapter 001 - <Chapter Name>.md    ← (optional) condensed Chapter file via /chapter-builder
    │   │   │   ├── chapter-001/
    │   │   │   │   ├── area-01.docx      ← per-Area file pair (authoritative)
    │   │   │   │   ├── area-01.md
    │   │   │   │   ├── area-02.docx
    │   │   │   │   ├── area-02.md
    │   │   │   │   └── ...
    │   │   │   ├── chapter-002/
    │   │   │   │   └── ...
    │   │   │   └── ...
    │   │   ├── part-2/
    │   │   │   └── ...
    │   │   └── ...
    │   ├── section-2/
    │   │   └── ...
    │   └── ...
    ├── phase-2/                          ← Phase 2 output (created when Phase 2 begins)
    │   └── ...
    ├── starward-saga-complete.docx       ← (optional) on-demand Novel aggregate via /compile-novel
    └── starward-saga-complete.md         ← (optional) on-demand Novel aggregate via /compile-novel-md
```

> **[Repo layout note]** The `[workspace root]/` tree above, showing `novel-writer/` and `ledger-*/` as siblings of `novel-starward-saga/`, refers to the current repo layout where novel output lives at `projects/novel-starward-saga/`, governance skills live at `.claude/skills/`, and Ledger folders live at `.claude/story-memory/ledger-*/`.

Per-Area `.docx` and `.md` file pairs are the **authoritative canonical source**. The Chapter file (`Chapter NNN - <Chapter Name>.md` and `.docx`, stored in the Novel-Part folder, 50% to 60% of its Areas' characters, spaces counted), the Phase aggregate and the Novel aggregate are derived artifacts produced only on demand: the Chapter file by `/chapter-builder` (written only by `chapter_builder.py`, authorized script 6), the Phase and Novel aggregates by `/compile-phase`, `/compile-phase-md`, `/compile-novel` and `/compile-novel-md`, which only join Chapter files (Phase aggregate) or Phase aggregates (Novel aggregate) and never condense or join Area files; their presence is optional and, when present, must never diverge from the per-Area substrate. **[Amended 2026-10-07]** The Chapter file is no longer stored in `chapter-NNN/` and is no longer named `chapter-NNN.docx` / `chapter-NNN.md`.

**Rule 5.2.2 — Phase Subfolder Naming.**
Each Phase of the novel has its own subfolder within `novel-starward-saga`. Phase subfolders are named using the pattern `phase-N` where N is the Phase number (not zero-padded). Phase 1 = `phase-1`. Phase 2 = `phase-2`. Phase 10 = `phase-10`.

> **[Repo layout note]** `novel-starward-saga` above refers to `projects/novel-starward-saga` in the current repo layout.

**Rule 5.2.3 — Section / Novel-Part / Chapter Subfolder Naming.**
Within each Phase subfolder, Sections are represented as `section-N` subfolders (where N is the Section number within the Phase). Within each Section subfolder, Novel-Parts are represented as `part-N` subfolders (where N is the Novel-Part number within the Section). Within each Novel-Part subfolder, Chapters are represented as `chapter-NNN` subfolders (where NNN is the Chapter number zero-padded to three digits; Chapter numbering resets per Novel-Part, beginning at 1 for the first Chapter of each Novel-Part). Areas are not subfolders: each Area is a file pair inside its Chapter folder, named by Rule 5.2.7. The numbers in `phase-N`, `section-N` and `part-N` are not zero-padded, so every listing, status, preview, export and compile step sorts that number as an integer, never as text (`section-2` comes before `section-10`).

Examples:
- `novel-starward-saga/phase-1/section-1/part-1/chapter-001/area-01.md` — Phase 1, Section 1, Novel-Part 1, Chapter 1, Area 1
- `novel-starward-saga/phase-1/section-2/part-1/chapter-003/area-04.docx` — Phase 1, Section 2, Novel-Part 1, Chapter 3, Area 4
- `novel-starward-saga/phase-2/section-1/part-1/chapter-001/area-01.md` — Phase 2, Section 1, Novel-Part 1, Chapter 1, Area 1

> **[Repo layout note]** The bare `novel-starward-saga/phase-N/...` paths in the examples above refer to `projects/novel-starward-saga/phase-N/...` in the current repo layout.

**Rule 5.2.4 — On-Demand Folder Creation.**
None of the nested subfolders (`phase-N/`, `section-N/`, `part-N/`, `chapter-NNN/`) are pre-created. Each is created at the moment the first Area within it is accepted and `[CONFIRM WRITE]` triggers Gate 2. If `/start-story` is the first writing command, it creates the full path `phase-1/section-1/part-1/chapter-001/` in a single Gate 2 execution before writing the first Area file pair. Subsequent `/next-area` calls within the same Chapter reuse that folder; `/next-chapter` / `/next-part` / `/next-section` / `/next-phase` transitions create the missing folders for the new narrative position on first write.

**Rule 5.2.5 — Chapter Number Definition.**
Chapter numbers within a Novel-Part are sequential integers beginning at 1, zero-padded to three digits (`chapter-001`, `chapter-012`, `chapter-100`). Chapter numbering resets per Novel-Part. The Chapter number in the folder name is a count within its parent Novel-Part — not a Phase-wide absolute. The novel's internal structure is fully encoded by the nested folder path itself; no filename encoding is needed.

**Rule 5.2.6 — Contents Allowed in Narrative Subfolders.**
Phase subfolders may contain Section subfolders, the Phase icon files (`phase-icon.png` and `phase-icon.svg`, Rules 6.4.2 and 10.4.1) and, optionally, an on-demand Phase aggregate (`phase-N-complete.docx` / `phase-N-complete.md`). Section subfolders contain only Novel-Part subfolders and the Section icon files (`section-icon.png` and `section-icon.svg`, Rule 6.3.1b). Novel-Part subfolders contain the Chapter subfolders and, optionally, the on-demand Chapter files (`Chapter NNN - <Chapter Name>.docx` / `.md`, written by `/chapter-builder`). Chapter subfolders contain only the per-Area file pairs (`area-NN.docx` / `area-NN.md`). **[Amended 2026-10-07]** The Chapter file moved from the Chapter subfolder to the Novel-Part folder. No other files — no outlines, no notes, no governance documents — are stored in any narrative subfolder. Governance documents remain in `novel-writer`. Ledger files remain in Ledger folders.

> **[Repo layout note]** `novel-writer` above refers to `.claude/skills/` in the current repo layout.
> **[Repo layout note]** "Ledger folders" above refers to `.claude/story-memory/ledger-*/` in the current repo layout.

**Rule 5.2.7 — Area File Naming.**
Within each Chapter folder, Area files are named using the pattern `area-NN` where NN is the Area number within the Chapter, zero-padded to two digits. Area 1 of Chapter 1 of Novel-Part 1 of Section 1 of Phase 1 = `area-01`. Area 27 of Chapter 5 of Novel-Part 2 of Section 1 of Phase 1 = `area-27`. Each Area has exactly two files: `area-NN.docx` and `area-NN.md`, written as a coupled pair at Gate 2. Area numbering resets per Chapter.

### 5.3 — File Lifecycle Law

**Rule 5.3.1 — Per-Area File Creation on Gate 2.**
Each Area's `area-NN.docx` and `area-NN.md` file pair is created the first time that Area passes Gate 2 (on `[CONFIRM WRITE]`). Before Gate 2 fires, no file exists for that Area. On Gate 2 for a new Area, both files in the pair are created simultaneously and the Area's content is written to them. Any missing folders in the nested path `phase-N/section-N/part-N/chapter-NNN/` are created as part of the Gate 2 write.

**Rule 5.3.2 — Immutable-Per-File Model.**
Each per-Area file pair holds exactly one Area. After creation, the file pair is modified **only** by the following operations:
- `[REVISE AREA: reference]` (`/revise-area`), which, on `[CONFIRM WRITE]`, first moves the old file pair to the archive folder (below) and then writes the revised Area to both files at the same path at Gate 2 of the revision sequence. The file's identity and path do not change; only its content does, and the previous text is kept in the archive.
- `/redraft-area`, the full redraft of one Area, which, once the revised plan is confirmed, archives the Area's file pair to the archive folder (below) and then writes a fresh file pair at the same path, so that the ledgers, the plan statuses and the score tracker go back to the end of the previous Area before the new Area is drafted. A later Area already written stays canon, and only what the archived Area alone established rolls back.
- `/redraft-chapter`, which archives the Chapter's per-Area files to the archive folder (below) with a timestamp and rebuilds fresh per-Area file pairs under the Chapter folder, after the ledgers, the plan statuses and the score tracker have gone back to the end of the previous Chapter. A later Chapter already written stays canon, and only what the archived Areas alone established rolls back.
- `/reset-chapter` / `/reset-phase` / `/reset-story`, which delete per-Area files and associated folders per their command definitions.
- `/rewind-to`, which takes an Area reference, a Chapter reference or a Section reference as its target and archives all per-Area files after the rewind point as non-canonical pending revision (moved to the archive folder, never deleted; new prose written forward creates fresh file pairs). An Area reference as target keeps that Area and archives everything after it. A Chapter or Section reference is read as its last Area.
- `/restore-archive <date-time>`, which moves the file pairs of one archive folder back to the paths they were archived from, never overwriting a file, and then brings the ledgers, the plan statuses and the score tracker back in line with them.

**Rule 5.3.2a — The Archive Folder.** The archive folder is never read, listed or counted by any command (except that `/restore-archive` lists paths under it), and only `/revise-area` changes a written Area file in place (a redraft archives the file pair first and then writes a fresh pair). The one use of the archive is `/restore-archive`, which never reads a file's text. A move to the archive never deletes; archived file pairs are moved by the orchestrating command to `projects/novel-starward-saga/_archive/<date-time>/`, keeping their path below `projects/novel-starward-saga/`. The archive folder lies outside every narrative subfolder, so Rule 5.2.6 is unaffected. Every command that lists or reads written Areas (`/status`, `/preview-chapter`, `/chapter-builder`, `/force-ledger-audit`, `/area-history`, `/chapter-summary`, `/find`, `/load-canon`, `/consequence-audit`, `/ideology-audit` and the FCIA pass of `/run-canon-audit`) skips `_archive`. `/restore-archive <date-time>` is the way back: it lists paths under `_archive` (never a file's text), moves the pairs of the one folder it is given back to the paths they came from, and never overwrites a file. New prose written forward creates fresh file pairs through the authorized scripts. The archive move is a plain file move by the orchestrating command with the shell's move command: it creates no script and writes no Area file, and `<date-time>` is written `YYYY-MM-DD_HHMM`. A reset deletes the archive folders of its scope together with the written Areas and with the exported chapter, phase and novel files that hold their text (`/reset-chapter` and `/reset-phase` for their chapter or phase, `/reset-story` and `/hard-reset` for all of them).

No Area's `.docx` or `.md` file is ever appended-to or extended beyond its single Area payload. Per-Area files are not shared across Areas, and no editorial operation may splice multiple Area payloads into a single `area-NN.{docx,md}` pair.

**Rule 5.3.3 — One File Pair Per Area.**
Each Area has exactly one `.docx` file and exactly one `.md` file, written to its canonical nested path. A Chapter boundary creates a new Chapter folder. A Novel-Part boundary creates a new Novel-Part folder. A Section boundary creates a new Section folder. A Phase boundary creates a new Phase folder. In every case, the filesystem itself encodes the narrative hierarchy; no file ever contains content spanning more than one Area.

**Rule 5.3.4 — File Integrity.**
Per-Area output files must not be manually edited outside of the SSC Canon-governed writing process. Manual edits to output files are not tracked by the Ledger system and may create discrepancies between the Ledger record and the file content. If manual edits are made, the user accepts responsibility for any resulting continuity errors.

**Rule 5.3.5 — Aggregate Staleness.**
Any on-demand Chapter file (`Chapter NNN - <Chapter Name>.docx` / `.md` in the Novel-Part folder), Phase-aggregate (`phase-N-complete.docx` / `phase-N-complete.md`), or Novel-aggregate (`starward-saga-complete.docx` / `starward-saga-complete.md`) file produced via `/chapter-builder`, `/compile-phase`, `/compile-phase-md`, `/compile-novel` or `/compile-novel-md` is treated as a **cache** of the per-Area source (a Chapter file is a derived, condensed text, rebuilt with `/chapter-builder`). **An aggregate is stale when any per-Area file in its scope is newer than the aggregate, when an aggregate it is built from is newer than it, or when its scope lost files to the archive after it was made** (the date-time in the name of the `_archive` folder, Rule 5.3.2a, shows when). Nothing needs to mark an aggregate: a revision (`/revise-area`), a redraft (`/redraft-area`, `/redraft-chapter`), a rewind (`/rewind-to`), a restore (`/restore-archive`), a reset (`/reset-chapter`, `/reset-phase`, `/reset-story`) or a hard reset (`/hard-reset`) that touches a per-Area file in its scope makes it stale by this test alone. A command that builds from lower-level files (`/compile-phase` and `/compile-phase-md` from the Chapter files, `/compile-novel` and `/compile-novel-md` from Phase aggregates) applies the test to each one it uses, regenerates a stale one first, and reports which it regenerated. Stale aggregates must be regenerated on the next invocation of their producing command, or deleted outright. The per-Area files are always authoritative; the aggregates are never permitted to silently diverge. **[Amended 2026-10-07]** A Chapter file is stale when a per-Area file of its Chapter is newer than it (or the Chapter lost files to the archive after it was made); it is rebuilt only by `/chapter-builder`, with the author's confirmation, and the compile commands never condense, never join Area files and never regenerate a Chapter file themselves: they stop, name each missing or stale Chapter file and leave the rebuild to /chapter-builder.

---

## Area 6 — Book Creation Law: Area Document (.docx)

### 6.1 — Purpose and Mandate

**Rule 6.1.1 — Purpose.**
The Area `.docx` file is the **primary publication-format output** of the novel-writing process. It is formatted to professional novel publishing standards, suitable for direct reading, editorial review, and eventual print or digital publication preparation. Every formatting decision in this Area is made in service of that standard — not convenience, not ease of parsing, but reader experience at the level of a published novel.

**Rule 6.1.2 — Governing Standard.**
The formatting standard for all `.docx` output — both per-Area files written during `/start-story` / `/next-area` and the condensed Chapter files written by `/chapter-builder` — is the **Starward Saga Novel-Grade Typeset Format**: 6" × 9" trade paperback, EB Garamond body font, 1.15× line spacing, with phase icon ornament, drop cap openings, and running headers/footers. This is a unified format: the per-Area `.docx` files are already publication-ready, and `chapter_builder.py` typesets the Chapter file with the same helpers (imported from `area_docx_creator.py`), so one typeset fix reaches both. The typeset standard is defined in full in Rules 6.2 through 6.7 of this Area and in Area 10 (Chapter Export Format Specification). The two Areas govern the same standard — Area 6 governs per-Area implementation; Area 10 governs the Chapter file. **[Amended 2026-10-07]** `/export-chapter` (assembly of Area files) is retired.

**Rule 6.1.3 — Gated Trigger Law.**
Every accepted Area, after passing the Post-Output Audit and the Gate 1 chat delivery of the gate law, enters the Inter-Gate Confirmation state. The docx update protocol (Rule 6.5) executes only on explicit user `[CONFIRM WRITE]` at the Inter-Gate Confirmation Prompt. The docx write is mandatory once `[CONFIRM WRITE]` is received, but is never performed before that confirmation is received. The write occurs as part of the `/next-area` command's execution flow at Gate 2, after the Post-Output Audit passes, after Gate 1 chat delivery, after Inter-Gate Confirmation, and before the position display is updated.

### 6.2 — Document Formatting Standards

**Rule 6.2.1 — Page Setup.**
```
Page Size:          6" × 9" (trade paperback trim — standard for fantasy/sci-fi fiction)
Margins:            Top: 1.0" | Bottom: 1.0" | Left: 0.875" | Right: 0.875"
Header (even/left): "STARWARD SAGA"  — centered, EB Garamond 9pt, #5A5A5A
Header (odd/right): Chapter title in FULL CAPS — centered, EB Garamond 9pt, #5A5A5A
Footer:             Page number — left-aligned on even pages, right-aligned on odd pages
                    EB Garamond 9pt
```

**Rule 6.2.2 — Typography Standards.**
```
Body Font:              EB Garamond 12pt
Line Spacing:           1.15× (published trade paperback standard for 12pt type on 6×9 page)
First Line Indent:      0.3 inches — suppressed only on the first paragraph of narration of an Area
Alignment:              Left-aligned (NOT justified)
Space Before Paragraph: 0pt
Space After Paragraph:  0pt

Chapter Heading Font:        EB Garamond, Bold, centered, black, 16pt on every line
Chapter Header Block lines:
  Series title:  "STARWARD SAGA"
  Phase line:    "PHASE 1 — THE ROOTS OF BECOMING"
  Section line:  "SECTION 1 — AZURE SKY AND GALE"
  Novel-Part:    "PART 1 — [Novel-Part Name]"
  Chapter line:  "Chapter 001 — [Chapter Name]"

Area Title Block (on every Area file, Rules 6.3.2 and 6.3.2a):
  Phase icon PNG: 0.55" wide, centered; 12pt space before, 4pt space after
  Area title: EB Garamond 12pt Bold, centered — "Area N — [Area Name]"
  Reference code: EB Garamond 10pt Regular Italic, centered
  No page break and no ornament

Date line (every Area, Rule 6.3.2b):
  One italic paragraph, the first paragraph of the Area text, directly under the
  Area Title Block; not narration, so the drop cap and the small caps below
  belong to the first paragraph of narration after it
  In the .docx: centred, italic, 10.5pt, 8pt space below

Drop Cap + Small Caps (Chapter and Area openings):
  First character of opening paragraph: EB Garamond 28pt Bold (≈ 3 text lines tall)
  Next ~4 words: EB Garamond small caps
  Remainder: standard body style

Time-Skip Symbol:   ⁂ asterism (U+2042), EB Garamond 14pt, centered, 12pt space above and below
                    Used inside an Area for a brief time skip in the same place (Rule 6.3.5)
```

**Rule 6.2.3 — Dialogue Formatting in Docx.**
Dialogue in Area output is formatted in **double straight quotation marks AND italics simultaneously** in the docx file, following Part 2 Area 2 Rule 2.2.2 and Part 29 Rule 29.2.1.1. The italics are applied using the docx character-level italic style (not a paragraph style) to the full quoted span — the opening double quotation mark, the spoken text, and the closing double quotation mark are all inside the italic run. Dialogue is visually distinguished from narration within every paragraph by the simultaneous presence of both markers. Docx generation code must insert the straight double quotation mark characters (ASCII 0x22) rather than curly/smart quotes; no autocorrect-style substitution is permitted.

**Rule 6.2.4 — Named Move and Cultivation Level Formatting in Docx.**
All Named Moves, Named Techniques, and Named Cultivation Practice names (per Part 2 Area 3 Rule 3.2.1) are formatted in ***bold-italic*** using the docx character-level bold + italic style simultaneously — both inside dialogue and outside dialogue. There is no dialogue exception: bold-italic applies universally. Qualifying cultivation level designations (per Part 2 Area 3 Rule 3.2.1a) are formatted in ***bold-italic*** in the same manner: full realm+level strings, full affinity+level strings, tier designations, and named meridian designations. Standalone realm names (Champion, Warrior, Ruler, etc.) are plain text and are not formatted bold-italic. The Markdown input marker `***text***` is parsed by `_parse_inline_formatting()` in `area_docx_creator.py` and rendered as a docx run with both `bold=True` and `italic=True`.

**Rule 6.2.5 — No Visible Structure Labels in Prose.**
Per Principle P2-4 (No Meta-Constructs in Prose), no structural labels — Phase, Section, Novel-Part, Chapter, Area number — appear within the prose body text of the docx. These labels are visible only in the Chapter Header Block and the Area Title Block, which serve as navigational aids for the author and editor, not as narrative text visible to the reader. When the file is prepared for final publication, Area Title Blocks and structural notation are removed from the prose body, leaving only the chapter text. The date line of Rule 6.3.2b is not a structural label: it states a day, never a Phase, Section, Novel-Part, Chapter or Area number and never a Phase Day, so this rule does not bar it.

### 6.3 — Chapter Structure in the Docx File

**Rule 6.3.1 — Chapter Header Block Placement.**
The Chapter Header Block is written once per Chapter, and it resides in the **first Area file of each Chapter** — i.e., the `area-01.docx` stored in `chapter-NNN/`. It is the leading block of that file, preceding the Area Title Block and the Area body. Later Area files of the same Chapter (`area-02.docx`, `area-03.docx`, …) do NOT repeat the Chapter Header Block. Format (the Novel-Part Name and Chapter Name are mandatory per Part 28 Area 18 Rule 18.3.3):

```
[Phase icon PNG: phase-icon.png from novel-starward-saga/phase-N/ — 1.0" wide,
 centered; 24pt space before, 12pt space after — Rule 6.4.2]
STARWARD SAGA
PHASE [N] — [Phase Name]
SECTION [N] — [Section Name]
PART [N] — [Novel-Part Name]    (MANDATORY — Part 28 Area 18)

Chapter [Chapter Number] — [Chapter Name]    (MANDATORY — Part 28 Area 18)
[blank line — 24pt spacing]
```

**Rule 6.3.1a — Phase Icon in Chapter Header Block (Rule 6.4.2):** The phase icon PNG (`phase-icon.png` from `novel-starward-saga/phase-N/`) is the first element of the Chapter Header Block — placed above "STARWARD SAGA", centered, 1.0 inch wide, with 24pt space before and 12pt space after. If the icon file is not found, the header renders without it (graceful fallback). For Phase 1 the icon path is `novel-starward-saga/phase-1/phase-icon.png`.

> **[Repo layout note]** `novel-starward-saga/phase-N/` above refers to `projects/novel-starward-saga/phase-N/` in the current repo layout.

All text lines of the Chapter Header Block are center-aligned, EB Garamond (Rule 6.2.2), 16pt Bold. The Phase Name and Section Name are Locked Canon per Part 30 and must appear as authored there. The Novel-Part Name and Chapter Name are **categorically mandatory** under Part 28 Area 18 Rule 18.3.3 — no em-dash fallback, no "TBD" placeholder, and no blank rendering is permitted; a missing Novel-Part Name or Chapter Name in a written `area-01.docx` is a Post-Write Audit FAIL under the gate law.

**Rule 6.3.1b — Title Page (First Area of a Phase or of a Section).**
An Area that is the first of its Phase, or the first of its Section, opens its `area-NN.docx` with a **Title Page**: one full page, reader-facing, placed before the Chapter Header Block. It appears once at the opening of each Phase and once at the opening of each Section, so the first Area of the novel carries it for both. `.claude/tools/area_docx_creator.py` writes it whenever its first-Area-of-Phase or first-Area-of-Section argument is true. The page holds, in this order:

```
[Phase image: phase-icon.png from novel-starward-saga/phase-N/, centered, 4.5" wide]
PHASE [N] — [PHASE NAME IN CAPITALS]          (EB Garamond Bold 20pt, centered)
[Section image: section-icon.png from novel-starward-saga/phase-N/section-N/, centered, 3.0" wide]
Section [N] — [Section Name]                  (EB Garamond Bold 16pt, centered)
[Phase epigraph, when one is set]             (EB Garamond Italic 11pt, centered; first Area of a Phase only)
[Section epigraph, when one is set]           (EB Garamond Italic 11pt, centered; 12pt below the Phase epigraph when both print)
[page break: the Chapter Header Block starts on a fresh page]
```

> **[Repo layout note]** `novel-starward-saga/phase-N/` above refers to `projects/novel-starward-saga/phase-N/` in the current repo layout.

The Title Page holds up to two epigraph lines, and which it prints depends on the Area. On the first Area of a Phase (the Area that also opens that Phase's Section 1) it prints both, as two centered italic paragraphs: first the Phase epigraph, the `Epigraph:` line in the Phase definition block of Part 30 (`narration-novel-macro-story-law`), which reads `unset` until the author gives the text, and then Section 1's own Epigraph line in the header block of its Section Spec (Part 38 Rule 10.3.1). On the first Area of every other Section it prints only that Section's own Epigraph line in the header block of its Section Spec (Part 38 Rule 10.3.1). Every Section Spec holds its own Epigraph line; the Phase epigraph stays a line of Part 30 and is never copied into a Section Spec. The author settles a Section's Epigraph in the Section Spec build and confirms it at that spec's `[CONFIRM SPEC]`; the author alone sets the Part 30 line, either by editing Part 30 or by telling a command, which records it there as a one-line edit directed by the author, after asking. `unset` in either place means that line is left out: the page prints the one line that is set when only one is, and carries no epigraph when both are `unset`; no agent ever writes epigraph text, and the command reads the Part 30 line only to pass it on. Each writer script takes the two lines as two values: `--phase-epigraph` or `--phase-epigraph-file`, the Part 30 Phase line, which is given only on the first Area of a Phase and which the script refuses on any other Area (it writes nothing), and `--section-epigraph` or `--section-epigraph-file`, the Section Spec's Epigraph line; `--epigraph` and `--epigraph-file` also mean the Section line. The command passes both values on the first Area of a Phase (the Part 30 line and Section 1's Epigraph line) and only the Section value on the first Area of every other Section. When a file carries the Title Page, its structural blocks run in this order: Title Page, Chapter Header Block (if applicable), Area Title Block, date line, Area body.

**Rule 6.3.2 — The Area Divider.**
Every Area file begins its Area with the Area Divider, and the Area Divider is the Area Title Block (Rule 6.3.2a): there is no separate divider line. In the per-Area files the Area Title Block is the Area's opening; in the Chapter file (Area 10) there is no Area Title Block, and the boundary between the scenes of consecutive Areas is the centred `*   *   *` scene break (`---` in the `.md`). **[Amended 2026-10-07]** The Area Title Block stays in the per-Area files only. An Area cannot be opened for delivery until an Area Name has been authored per Part 28 Rule 18.3.2.

**Rule 6.3.2a — Area Title Block (Mandatory on Every Area File).**
Every `area-NN.docx` file, without exception, whether it is the first Area of a Chapter or any later Area, carries an **Area Title Block** immediately preceding the Area body (and its date line). The Area Title Block names the Area in accordance with Part 28 Area 18 Rule 18.3.3 and is the in-file counterpart of the Gate 1 chat Position Header Block (which is chat-only per Rule 6.7.1). Format:

```
[blank line]
[Phase icon PNG]
Area [Area Number] — [Area Name]    (MANDATORY — Part 28 Area 18)
[Reference Code: Phase.Section.Part.Chapter.Area]
[blank line]
```

The Area Title line is EB Garamond 12pt Bold, center-aligned; the Reference Code line is 10pt Regular, center-aligned, italic. The Area Name is **categorically mandatory** — a missing Area Name in the Area Title Block of a written `area-NN.docx` file is a Post-Write Audit FAIL under the gate law. When the file is the first Area of a Chapter, the ordering of structural blocks is: Chapter Header Block → Area Title Block → date line → Area body (preceded by the Title Page where Rule 6.3.1b applies). When it is not, the ordering is: Area Title Block → date line → Area body. An Area is always cited by its five-part reference (Phase.Section.Part.Chapter.Area), and the Ledger writes the Area name beside the reference (Part 28 Rule 18.3.4).

**Rule 6.3.2b — The Date Line (the Top of the Area Text).**
The text of every Area begins with its date line: one paragraph, wholly italic, typed `*...*` in the text handed to the writer scripts, stating the day the Area begins in the Nine Suns calendar. It stands directly under the Area Title Block (the Area title and the Reference Code line, Rule 6.3.2a). In every file the blocks therefore run: Title Page and Chapter Header Block (each where it applies), Area Title Block, then the date line, then the narration. The line's form, the moment it states, its range form, its handling of a flashback, a dream or a vision, and the dating rules belong to Part 41 (Area 5, The date line; Area 6, Dating rules and the check); this rule sets only its place and its standing in the file. Four things hold. (1) The date line is Area text and the one lawful mark at the top of an Area: it is not a heading, title, icon, reference code or ornament, and not a further structural block, so Rules 6.6.1 and 7.6.2 stand. (2) It is not a structure label (Principle P2-4, Rule 6.2.5). (3) It is not narration: it is left out of the Area size (Rule P2-Area-7) and of every count and reading of this canon, and it is never the first paragraph or the last paragraph of an Area for any reading (Rule P2-Area-1a). The Area's opening paragraph is its first paragraph of narration, the one after the date line, so the drop cap, the small caps and the unindented opening that Rules 6.2.2, 6.3.3, 10.2.4 and 10.7.1 give to "the first paragraph" belong to that paragraph. (4) The `.docx` and the `.md` of an Area carry the same date line (Rule 7.6.1; the markdown form is Rule 7.2.2b).

> **[Script note]** `.claude/tools/area_docx_creator.py` handles the date line: it detects it strictly, as the first paragraph of the text with the whole paragraph wrapped in single asterisks and beginning `Year `, a number and a comma (the single form and the range forms); it sets the line as its own paragraph, centred, in italic, in a smaller size than the body text, with a small space below it, on every Area file; and it gives the drop cap, the small caps and the no-indent opening to the first paragraph of narration after the date line, never to the date line. A text whose first paragraph is not a date line is written exactly as it stands. The script writes and checks no date: the line is typed in the Area text, and its form and its dates belong to Part 41. `.claude/tools/area_md_creator.py` passes every paragraph through as typed. Rule 6.4.3 says a formatting change is made to the rules and the script together in the same session.

**Rule 6.3.3 — One Area Per File.**
**[Amended 2026-10-07]** This rule governs the per-Area files of the Area-built path; a Chapter built whole has no Area files (Rule 6.3.4a). Each `area-NN.docx` file contains the body of exactly one Area. The body begins immediately after the Area Title Block (Rule 6.3.2a) and its date line; additionally, for the first Area file of the Chapter (`chapter-NNN/area-01.docx`), the Area Title Block follows the Chapter Header Block (Rule 6.3.1), and for the first Area of a Phase or of a Section the Title Page (Rule 6.3.1b) comes first of all. The first paragraph of narration of every Area does NOT have a first-line indent (standard publishing convention of no indent after a break). Every other paragraph — including the paragraph after a ⁂ — has a 0.3-inch first-line indent (Rule 6.2.2).

**Rule 6.3.4 — On-Demand Chapter File Structure.**
When `/chapter-builder` is invoked, the Chapter file `Chapter NNN - <Chapter Name>.docx` (with its `.md` pair) is written into the Novel-Part folder by `chapter_builder.py` from the condensed Chapter text, which the Area Maker writes from the Chapter's finished Areas in canonical order (Area 1, Area 2, …, Area N, sorted as integers) and the author confirms; it is never constructed by concatenating the per-Area `.docx` files. The Chapter file carries the Title Page (where Rule 6.3.1b applies) and the Chapter Header Block once, then the date line once, then the condensed scenes of the Areas in order, separated by the scene break, with no Area Title Block, no Area reference code and no per-Area heading (Rules 6.3.2 and 10.3.4). The Chapter file is a derived artifact; the per-Area files remain authoritative. **[Amended 2026-10-07]** Replaces the join of Area files by `/export-chapter`.

**Rule 6.3.4a — A Chapter Built Whole.** **[Amended 2026-10-07]**
A Chapter may be written whole, by `/create-chapter` (Command C-42), from its confirmed Chapter Spec. This is a second lawful path under a new rule, not an exception to Rules 6.3.3, 6.6.4 and 7.6.4, which govern the per-Area files. Eleven things hold.
1. **Build mode.** The Chapter Spec header carries `**Build mode:** whole | by-area` (default `whole` for a new spec). A Chapter is built one way only. `/create-chapter` refuses a Chapter that has Area files (it names them and points to `/chapter-builder` or `/redraft-chapter`); `/next-area`, `/revise-area` and `/chapter-builder` refuse a Chapter built whole.
2. **No Area files.** No `area-NN.docx` and no `area-NN.md` exist for a Chapter built whole. The only output is the Chapter file pair, `Chapter NNN - <Chapter Name>.md` and `.docx`, in the Novel-Part folder (`projects/novel-starward-saga/phase-N/section-N/part-N/`), the same location and file names as Rule 6.3.4, written only by `.claude/tools/chapter_builder.py` (`--mode whole`) after the author's confirmation. This file is the authoritative text of the Chapter, not a derived artifact.
3. **The unit.** The Chapter is the written unit; the Area blocks of the Chapter Spec are its plan units, and each Area block's planned beat, anchors, continuation, viewpoint and Behavioral Plan are written in order.
4. **Hidden markers.** The staged draft and the final `.md` carry, at the start of every Area block of the Chapter Spec, an HTML comment line `<!-- AREA NN -->` (NN the two-digit Area block number of the spec), invisible when rendered. The `.docx` carries none. A marker is bookkeeping only (it lets the script count words per Area block and lets Gate 2 flip the Behavioral Plan rows per Area block) and is never a citation or a structure label; every Area block of the spec appears once, in order.
5. **Break rule.** A visible break (`---` in the `.md`, centred `*   *   *` in the `.docx`) appears only where the scene changes, or where the same scene moves to a different POV. Where one scene continues across Area blocks in the same POV there is no visible break, only the hidden marker. A date line is printed once at the top of the Chapter; a scene whose date differs from the scene before it gets its own date line directly after its break (the drop cap on its first paragraph); a scene with the same date repeats no date line. Rule 10.5.1 states the same marks for the condensed Chapter file.
6. **Word band.** Counted in words (the date lines, the markers and the break marks are not counted). Each Area block is written at 55% to 60% of its size target (Rule P2-Area-7; the target is the Chapter Spec's). Only an Area block named in the Chapter Spec by `Budget stretch: up to 0.72 of target` (with its one-line reason) may exceed 60%, and never above 72%; no Area block goes below 55%. The Chapter total must fall from 0.55 T to 0.72 T, T being the sum of the Area targets (T = 8,000 gives 4,400 to 5,760). The 1,280 to 2,400 passing range of Rule P2-Area-7 is not applied to a Chapter built whole; this band replaces it for such a Chapter. Pacing (Fast, Medium, Slow) shapes the writing inside the band and never changes it.
7. **Pacing and size are read from the spec.** The Chapter Spec carries a Chapter pacing, a Chapter size target, per-Area pacing and size target, and a `5.0 Scene Map`; `/create-chapter` stops when the Chapter, any Area block or the Scene Map lacks one.
8. **Scenes.** A scene may span several Area blocks and several POVs; the Scene Map of the Chapter Spec states each scene's Area blocks, POV sequence, arc, pacing, word budget, break rule and the exact join state at each Area seam. An Area block never holds two scenes, as in Tier 5.
9. **Layout.** The Chapter file's layout is that of Rules 6.3.4, 10.3.3, 10.3.4, 10.4.3 and 10.5.2: Title Page where Rule 6.3.1b applies, Chapter Header Block once, the date line once, then the scenes; no Area Title Block, no Area reference code and no per-Area heading.
10. **References.** Every reference to a Chapter built whole is the Chapter reference `P.S.N.CCC` (for example `1.1.1.002`) alone. Chapter Spec Area rows read `WRITTEN(P.S.N.CCC)`. Area-level references remain valid for Area-built Chapters and for history.
11. **Revision.** `/revise-chapter` edits the written Chapter in place (archive of the old pair, then the script with `--overwrite`); `/redraft-chapter` on such a Chapter archives it and runs `/create-chapter` again.

**Rule 6.3.5 — Time Skips Within an Area (the ⁂ Mark).**
If a brief time skip occurs inside an Area (the same place, the same people, the same dramatic movement, and listed in the chapter spec; only the clock has moved on), it is rendered as a centered ⁂ asterism break:

```
[blank double-spaced line]
   ⁂
[blank double-spaced line]
```

The asterism break is formatted in 14pt EB Garamond, center-aligned (Rule 6.2.2). In the text handed to the writer scripts the mark is typed as a paragraph of its own reading `* * *`; the docx script renders it as the ⁂ mark and the markdown script keeps `* * *` (Rule 7.2.4). The ⁂ marks a brief time skip inside one Area; it is not a boundary between scenes or between Areas; the Area Title Block opens each Area in the per-Area files, and in the Chapter file the scene break (Rule 10.5.1) separates the scenes of consecutive Areas. Four rules bind its use. (1) It marks time only: a change of place, a change of scene, or a skip long enough to end the scene begins a new Area (Tier 5, §1.5.1), not a ⁂. Two examples, not a limit: two hours waiting in the same hall take the mark; a night that passes begins a new Area. In a borderline case the Chapter Spec decides. (2) The chapter spec plans it: each skip is listed under the Area block's planned time skips with its story-time context, and a ⁂ that no listed skip covers is a deviation from the spec (Part 38, Check #18). (3) The first sentence after it states the new moment in story time, so the reader never has to infer it. (4) It sits between two paragraphs inside an Area, never at the carry-over between Areas (Rule P2-Area-6).

### 6.4 — Python-docx Code Template

**Rule 6.4.1 — Implementation Standard.**
All `.docx` file creation and update operations use the `python-docx` library, through the authorized script `.claude/tools/area_docx_creator.py` (Rule 6.4.3). That script is the authoritative implementation reference — any deviation from its formatting parameters constitutes a violation of the docx formatting standard.

**Rule 6.4.1a — Title Page Images.**
A Title Page needs both images. If `phase-icon.png` or `section-icon.png` is missing, `area_docx_creator.py` raises an error and writes nothing; it never prints a placeholder line in its place. `/start-story`, `/next-section` and `/next-phase` check both files before any Area is planned and, when one is missing, stop and run `/create-image-phase` or `/create-image-section` first.

**Rule 6.4.2 — Phase Icon Placement Law.**
The phase icon PNG (`phase-icon.png` located in the `novel-starward-saga/phase-N/` folder for each Phase N) must be inserted in two locations in every `.docx` file where the block applies:
1. **Chapter Header Block** (first Area of each chapter only): Icon at top, 1.0" wide, centered, 24pt space before, 12pt space after — before "STARWARD SAGA" (Rule 6.3.1a).
2. **Area Title Block** (every Area file): Icon centered, 0.55" wide, 12pt space before, 4pt space after — immediately before the Area title line (Rule 6.2.2).

The icon dimensions (300×360px RGBA PNG) allow for clean scaling at both sizes. If the icon file does not exist at the expected path, the DOCX is produced without the icon (graceful fallback) — but a missing icon is a non-critical Post-Write Audit advisory. The images of the Title Page (Rule 6.3.1b) have no such fallback: the writer stops with an error when one is missing. The canonical `get_phase_icon_path(phase_number)` helper provides the path; callers check existence before inserting.

> **[Repo layout note]** `novel-starward-saga/phase-N/` above refers to `projects/novel-starward-saga/phase-N/` in the current repo layout.

**Rule 6.4.3 — Stored Python Script.**
The complete DOCX creation Python script is stored as a live, runnable file at `.claude/tools/area_docx_creator.py`. This file is the canonical implementation — it is used directly at Gate 2 for all Area DOCX creation. Rule 6.2.2 and Rules 6.3.1–6.3.3 describe the formatting it produces; a formatting change is made by amending those rules and the script together in the same session. Call the script directly rather than reproducing code in canon text.

**Rule 6.4.4 — Dependency.**
The `python-docx` library must be installed in the Python environment. Installation: `pip install -r .claude/tools/requirements.txt`. `/start-story` checks this first (`python -c "import docx"`) and stops with this install line if the import fails. The authorized script is run through the shell tool every time an Area is accepted.

**Rule 6.4.5 — Error Handling.**
If the python-docx write operation fails (library not installed, disk error, path error, an empty Area Name), the failure is reported in chat at once with its error, and Gate 2 stops there. A file of the pair that was already written is removed (a plain delete by the orchestrating command; it creates no script and writes no Area file), the Post-Write Ledger Update and the spec as-built sync do not run, and the Area is not counted as accepted or written. The confirmed text stays in the conversation. When the cause is fixed, the author re-issues `[CONFIRM WRITE]` and the write is tried again from that text. Files, Ledger and spec agree at every point (Rule 5.1.2 item 5).

### 6.5 — Docx Update Protocol (Two-Gate Flow)

**Rule 6.5.1 — Trigger Point (Per-Area).**
The per-Area docx write is triggered at Gate 2 of the gate law — after the Post-Output Audit returns PASS, after Gate 1 chat delivery, and after Inter-Gate Confirmation (`[CONFIRM WRITE]`) for that specific Area. It executes immediately before the paired per-Area markdown write (Rule 7.5.1) and before the Post-Write Ledger Update (`.claude/guardrails/ledger/guardrail-ledger-update-law.md`). Execution order within the `/next-area` command flow (the Two-Gate Audit Pipeline, `.claude/guardrails/audit/guardrail-audit-gate-law.md`, fixes the order of the audits and the writes; this list shows where the docx write sits in it):

```
 1. Pre-Area Read Mandate (gate law, Rule P2-Area-2) — read in full the previous
    Area (its area-NN.md), and for a scene that continues, every earlier Area
    of that scene; older history comes through the ledgers (Part 28 Area 4.6).
 2. Pre-Write Ledger Check (ledger update law)
 3. Write the Area (at full prose depth under the pacing and the size target
    the Chapter Spec records, Part 2 Area 1 §1.6.2.1; Area size per Rule P2-Area-7)
 4. Post-Output Audit (gate law): every check on the new Area, plus the flow review of the Area window (Rule P2-Area-1)
    → IF PASS: continue to step 5
    → IF FAIL: corrections required; do not proceed to Gate 1 until corrected
    → IF a question to the author about the draft arises (a behavioral-change enquiry, a spec difference): print the complete text first (Rule 5.1.2 item 1), then ask
 5. GATE 1 — CHAT DELIVERY (gate law — automatic, unconditional)
    The complete text of the Area is printed verbatim in chat: never a summary, an excerpt or a file path.
 6. INTER-GATE CONFIRMATION (gate law — mandatory halt)
    Display FILE-WRITE CONFIRMATION REQUIRED prompt.
    → On [CONFIRM WRITE]: proceed to step 7
    → On [REVISE AREA]: revise the Area (step 3), re-run the Post-Output Audit in full (step 4), then print the complete revised text (step 5)
    → On [SKIP WRITE]: discard the draft and skip steps 7–11; nothing is written or updated
 7. GATE 2a — *** PER-AREA DOCX WRITE (Area 6.5.1 — this step) ***
    Create any missing folders in the nested path
    novel-starward-saga/phase-N/section-N/part-N/chapter-NNN/,
    then create and write area-NN.docx containing:
      - Title Page            (only if this is the first Area of a Phase or of a Section — Rule 6.3.1b)
      - Chapter Header Block  (only if this is area-01 of the Chapter)
      - Area Title Block      (always — Rule 6.3.2a: "Area N — [Area Name]" + Reference Code)
      - Date line             (always — the first line of the Area text, Rule 6.3.2b)
      - Area body             (always)
 8. GATE 2b — *** PER-AREA MD WRITE (Area 7.5.1) ***
 9. Post-Write Ledger Update (ledger update law)
    The Post-Write Audit (gate law) runs beside this step, and neither waits for the other.
10. Post-Area Completeness Indicator emission (gate law; Part 2 Area 8)
11. Position display update
```

> **[Repo layout note]** `novel-starward-saga/phase-N/section-N/part-N/chapter-NNN/` above (step 7) refers to `projects/novel-starward-saga/phase-N/section-N/part-N/chapter-NNN/` in the current repo layout.

**Rule 6.5.2 — What is Written.**
Only the accepted, Post-Output-Audit-passed Area text is written to the `area-NN.docx` file (plus, where applicable, the Title Page, the Chapter Header Block and the Area Title Block). Pre-audit drafts, planning notes, and audit reports are never written to any per-Area output file.

**Rule 6.5.3 — Rewind Behavior.**
When `/rewind-to` is invoked and per-Area files after the rewind point are archived as non-canonical, those per-Area `.docx` files are moved to the archive folder (Rule 5.3.2a) and never deleted; new prose written at the same narrative position creates a fresh `area-NN.docx` at its Gate 2 write.

**Rule 6.5.4 — Aggregate Invalidation.**
If a Chapter file `Chapter NNN - <Chapter Name>.docx` exists in the Novel-Part folder for the Chapter whose per-Area file is being created or overwritten, the Chapter file is stale by the test of Rule 5.3.5 (it may be deleted outright, and it is rebuilt on the next `/chapter-builder` invocation). **[Amended 2026-10-07]** Equivalent behavior applies to any Phase-aggregate `phase-N-complete.docx` or Novel-aggregate `starward-saga-complete.docx`.

### 6.6 — Governing Constraints

**Rule 6.6.1 — Reader-Facing Content Only.**
Per-Area docx output files contain only the novel's prose plus the three permitted structural elements: (a) **Chapter Header Block** on the first Area file of each Chapter — reader-facing; (b) **Area Title Block** on every Area file — author navigation aid (carries Area Name and Reference Code) and the Area opening (the Chapter file has no Area Title Block, Area 10); (c) **Title Page** on the first Area file of each Phase and of each Section — reader-facing (Rule 6.3.1b). No other content appears: no audit reports, no ledger data, no canon rule citations, no structural position notation within the prose body, no planning notes, and no governance information. The Gate 1 Position Header Block is categorically excluded (chat-only per Rule 6.7.1).

**Rule 6.6.2 — Formatting Immutability.**
The formatting parameters defined in Rules 6.2.1 and 6.2.2 are Locked Canon for all Phase 1 per-Area output. They may not be overridden per-Area, per-Chapter, or per-Phase without a canon amendment. Consistency across all per-Area files is required so that on-demand Chapter/Phase/Novel aggregates remain uniform.

**Rule 6.6.3 — No Area Modification.**
The per-Area docx write writes the Area exactly as it was accepted. It does not paraphrase, summarize, expand, or alter the prose in any way. The python-docx code writes the accepted Area text and nothing else (plus the designated structural prefixes where applicable).

**Rule 6.6.4 — One Area Per File.**
**[Amended 2026-10-07]** Governs the per-Area files of the Area-built path only; a Chapter built whole has none (Rule 6.3.4a). Each `area-NN.docx` contains the body of exactly one Area. No `area-NN.docx` file may contain body content from more than one Area. Appending additional Area bodies to an existing per-Area file is forbidden.

### 6.7 — Gate 1 Position Header Block Boundary (Chat-Only)

**Rule 6.7.1 — Chat-Only Placement.**
The Gate 1 Position Header Block, whose fields are defined once in the Gate 1 Chat Delivery format of `.claude/guardrails/commands/guardrail-command-law.md`, is a **chat-only** artefact. It orients the user to the current narrative position at the moment of Gate 1 Chat Delivery. It is **never** written to any `area-NN.docx` file. Any occurrence of the Position Header Block inside a `.docx` file is a structural contamination and a Post-Write Audit FAIL under the gate law. The Calendar line is a chat-only line of the block, defined in Part 41 Area 5 and required by the gate law; it is a different thing from the date line that stands at the top of the Area.

**Rule 6.7.2 — Distinction from Chapter Header Block and Area Title Block.**
The Gate 1 Position Header Block is categorically distinct from the file-level Chapter Header Block (Rule 6.3.1) and the file-level Area Title Block (Rule 6.3.2a). The Chapter Header Block and Area Title Block are **reader-facing** structural elements that live inside designated `.docx` files; the Gate 1 Position Header Block is a **governance-facing** chat-only orientation block that never reaches any published file. The artefacts have disjoint placements: Gate 1 Position Header Block → chat only; Chapter Header Block → first Area file of each Chapter; Area Title Block → every Area file.

**Rule 6.7.3 — Cross-Reference.**
For the canonical format of the Gate 1 Position Header Block see the Gate 1 Chat Delivery format of `.claude/guardrails/commands/guardrail-command-law.md`. For the audits that cover both Gate 1 (where the Position Header Block appears) and Gate 2 file integrity, see `.claude/guardrails/audit/guardrail-audit-gate-law.md`.

---

## Area 7 — Book Creation Law: Area Markdown File (.md)

### 7.1 — Purpose and Mandate

**Rule 7.1.1 — Purpose.**
The Area `.md` file is the **lightweight companion output** of the novel-writing process. Where the `.docx` file is the publication-format deliverable, the `.md` file is optimized for quick reading, git-tracked revision history, diff review, and plain-text portability. It contains the same prose content as the `.docx` file, formatted using standard Markdown conventions that preserve the novel's structural organization and inline formatting.

**Rule 7.1.2 — Parity Requirement.**
The `.md` file and the `.docx` file always contain the same prose content for any Area that has cleared Gate 2 of the gate law. Within any single Gate 2 execution, the `.docx` write and the `.md` write are coupled — both run, in the same Gate 2 cycle, for the same Area. The two files are never out of sync for Gate 2-accepted prose. If they differ in the words, the `.md` is authoritative for the content and the `.docx` must be regenerated from it through `area_docx_creator.py`; the `.docx` remains authoritative for the formatting.

A skipped draft leaves no divergence: on `[SKIP WRITE]` the draft is discarded and nothing is written or updated (Rule 5.1.2 item 5), so chat history, the files, the Ledger and the spec agree. Parity governs `.docx` ↔ `.md`.

**Rule 7.1.3 — Gated Trigger Law.**
The `.md` file update is triggered at Gate 2 of the gate law, at the same point as the `.docx` update (Rule 6.5.1, Step 7). It is mandatory, coupled to the `.docx` write, and runs only on explicit `[CONFIRM WRITE]` received at the Inter-Gate Confirmation Prompt. The `.md` update is NOT automatic on acceptance alone — it requires Inter-Gate Confirmation just as the `.docx` write does.

### 7.2 — Markdown Formatting Standards

**Rule 7.2.1 — Chapter Header Block Placement in Per-Area Markdown.**
The Chapter Header Block is written once per Chapter, and it resides in the **first Area markdown file of each Chapter** — i.e., the `area-01.md` stored in `chapter-NNN/`. It is the leading block of that file, preceding the Area Title Block and the Area body. Later `area-NN.md` files within the same Chapter do NOT repeat the Chapter Header Block. Format (the Novel-Part Name and Chapter Name are mandatory per Part 28 Area 18 Rule 18.3.3):

```markdown
# STARWARD SAGA
## Phase [N] — [Phase Name]
## Section [N] — [Section Name]
## Part [N] — [Novel-Part Name]    <!-- MANDATORY — Part 28 Area 18 -->

# Chapter [N] — [Chapter Name]    <!-- MANDATORY — Part 28 Area 18 -->

---
```

The Phase Name and Section Name are Locked Canon per Part 30 and must appear as authored there. The Novel-Part Name and Chapter Name are **categorically mandatory** under Part 28 Area 18 Rule 18.3.3 — no em-dash, no "TBD", no blank rendering; a missing Novel-Part Name or Chapter Name in a written `area-01.md` is a Post-Write Audit FAIL under the gate law.

**Rule 7.2.1a — Title Page in Per-Area Markdown.**
The first Area markdown file of a Phase, or of a Section, opens with the markdown **Title Page** ahead of the Chapter Header Block, in the same cases and with the same words as the docx Title Page (Rule 6.3.1b), without the images. `.claude/tools/area_md_creator.py` writes it whenever its first-Area-of-Phase or first-Area-of-Section argument is true. Format:

```markdown
---

# PHASE [N] — [PHASE NAME IN CAPITALS]

## Section [N] — [Section Name]

*[Phase epigraph, when one is set; first Area of a Phase only]*

*[Section epigraph, when one is set]*

---
```

Each epigraph line and the blank line after it are left out when that line is not set; the sources are the ones named in Rule 6.3.1b: the `Epigraph:` line of the Phase definition block of Part 30 (printed first, on the first Area of a Phase only) and the Epigraph line in the header block of the Section's own Section Spec, Part 38 Rule 10.3.1 (printed second, or alone on the first Area of any other Section). The first Area of a Phase therefore prints the Phase line and Section 1's own line, one italic paragraph each. A file that carries the block holds, in order: Title Page, Chapter Header Block (if applicable), Area Title Block, date line, Area body.

**Rule 7.2.2 — The Area Divider in Per-Area Markdown.**
Every Area markdown file begins its Area with the Area Divider, and the Area Divider is the Area Title Block (Rule 7.2.2a): there is no separate divider heading. An Area cannot be opened for delivery until an Area Name has been authored; a missing Area Name in a written `.md` file is a Post-Write Audit FAIL under the gate law.

**Rule 7.2.2a — Area Title Block (Mandatory on Every Area Markdown File).**
Every `area-NN.md` file, without exception, whether it is the first Area of a Chapter or any later Area, carries an **Area Title Block** immediately preceding the Area body (and its date line). The Area Title Block names the Area in accordance with Part 28 Area 18 Rule 18.3.3 and is the markdown counterpart of the Rule 6.3.2a docx Area Title Block. Format:

```markdown
## Area [N] — [Area Name]    <!-- MANDATORY — Part 28 Area 18 -->
*Reference: Phase.Section.Part.Chapter.Area*

```

The Area Title Block uses `##` (H2 heading) for the Area-number-and-name line and an italic one-line Reference Code beneath it, followed by one blank line before the date line and the Area body. The Area Name is **categorically mandatory** — a missing Area Name in the Area Title Block of a written `area-NN.md` file is a Post-Write Audit FAIL under the gate law. When the file is the first Area of a Chapter, the ordering of structural blocks is: Chapter Header Block → Area Title Block → date line → Area body. When it is not, the ordering is: Area Title Block → date line → Area body. The date line of Rule 7.2.2b sits between the Area Title Block and the Area body.

**Rule 7.2.2b — The Date Line in Markdown.**
The `.md` file of every Area carries the date line of Rule 6.3.2b as the first paragraph of its text, one blank line after the `*Reference: ...*` line of the Area Title Block. It is one paragraph typed `*...*`, followed by one blank line before the first paragraph of narration, and the script passes it through as typed. It is plain text, not a heading and not a Reference line: it never begins with `#` and never begins `*Reference:`. Because the Reference line and the date line are both single italic lines, a read-back of a file looks for the `*Reference:` prefix and the `## Area` heading, never for "the first italic line". The markdown form of the date line is the same one the `.docx` carries (Rule 7.6.1); its content is Part 41's (Area 5, The date line).

**Rule 7.2.3 — Area Paragraphs in Markdown.**
Each paragraph of an Area is separated by a blank line. There is no indentation in Markdown (indentation renders as code blocks). Paragraphs are left-aligned by default.

**Rule 7.2.4 — Area Separation in Per-Area Files and the Chapter File.**
Each `area-NN.md` contains exactly one Area's body (plus its Area Title Block and date line, and, where applicable, the Title Page and the Chapter Header Block). When an on-demand Chapter file `Chapter NNN - <Chapter Name>.md` is written via `/chapter-builder`, the scenes of consecutive Areas appear in numeric Area order in the condensed text, separated by a `---` line, with no Area Title Block and no Area reference code (Rule 7.3.2); the Chapter file is never a concatenation of the Area files. **[Amended 2026-10-07]** If a brief time skip occurs inside an Area (Rule 6.3.5), it is rendered as:

```markdown
* * *
```

This is the same paragraph Rule 6.3.5 types; Markdown shows it as a horizontal rule.

**Rule 7.2.5 — Dialogue Formatting in Markdown.**
Per Part 2 Area 2 Rule 2.2.2 and Part 29 Rule 29.2.1.1, all dialogue is formatted in **double straight quotation marks AND italics simultaneously**. In Markdown, this is rendered by enclosing the full quoted span (opening double quote, spoken text, closing double quote) inside single asterisks:

```markdown
She stepped forward, hand resting on the hilt of her blade. *"You have one chance to answer me truthfully,"* she said, *"and I suggest you take it."*
```

The double quotation marks are **inside** the italic span and are themselves italicized together with the spoken text. Straight ASCII double quotes (`"`) are used; curly / smart quotes are prohibited. Single quotation marks are reserved exclusively for nested reported speech (a character quoting another character inside their own spoken line per Part 29 Rule 29.2.1.1a), rendered as `*"and then she said to me, 'you will not pass this gate,' as if it were settled."*`. The dialogue formatting is applied only to the spoken text, not to the surrounding narration.

**Worked sample, a speech of several paragraphs (illustration only).** The figure is unnamed and the scene is invented. Markdown shown as it is written.

```markdown
The old woman set down her cup and looked at each of them in turn.

*"I will say this once, and then I will not speak of it again.*

*"My husband did not leave the town of his own wish. The magistrate sent him, and I signed the paper, because I was told the harvest would be taxed lightly if I did.*

*"I do not ask you to forgive me. I ask only that the girl hear it from no one but me."* Her hand, when she lifted the cup again, was steady.
```

Each paragraph of the speech is its own italic span, closed by its own asterisk, because the docx converter reads one paragraph at a time and prints an unmatched asterisk as a literal character. The opening double quotation mark repeats at the start of every paragraph of the speech, and the closing mark appears once, at the end of the last paragraph; both marks sit inside the italic span, as Rule 2.2.2 requires. The narration before and after the speech is plain text. If a beat or a tag falls inside a paragraph of the speech, the span closes before it and opens again after it, as in the first example above. The name of a named item inside the speech is broken out the same way, so that it stands in roman (Part 28 Rule 20.8.2(c)).

**Rule 7.2.6 — Named Move and Cultivation Level Formatting in Markdown.**
Per Part 2 Area 3 Rules 3.2.1 and 3.2.1a, all Named Moves and all cultivation level designations are formatted in ***bold-italic*** in Markdown using triple-asterisks, both inside and outside dialogue:

```markdown
He raised his hand and released the ***Crushing Void Palm***, a wave of force that struck the stone wall like a silent thunderclap.
```

Named Moves in dialogue use triple-asterisks within the italic dialogue span:

```markdown
*"Watch carefully,"* Varys said, his eyes distant. *"This is what I call the ***Void Fracture Strike***."*
```

Qualifying cultivation level designations (full level strings, affinity+level strings, tier designations, named meridian designations) use the same triple-asterisk convention. Standalone realm names (Warrior, Champion, Ruler) are plain text:

```markdown
At ***Ruler Level 3 Mid***, the sweep covered the complete circuit. The Warrior breakthrough at seventeen had opened the first tier. The ***Void Root*** meridian held without deviation. ***Swords Affinity Level 3*** did not rush.
```

**Rule 7.2.7 — Section Continuity.**
No structural labels beyond the Chapter Header Block and Area Title Blocks appear in the `.md` file. Novel-Part numbers, Section numbers, Phase numbers (beyond the header), and Area numbers do not appear in the prose body.

### 7.3 — File Structure in Markdown

**Rule 7.3.1 — Per-Area Markdown File Structure Examples.**

*First Area of a Chapter (carries Chapter Header Block + Area Title Block) — `phase-1/section-1/part-1/chapter-001/area-01.md`:*

```markdown
# STARWARD SAGA
## Phase 1 — The Roots of Becoming
## Section 1 — Azure Sky and Gale
## Part 1 — [Novel-Part Name]    <!-- MANDATORY — Part 28 Area 18 -->

# Chapter 1 — [Chapter Name]    <!-- MANDATORY — Part 28 Area 18 -->

---

## Area 1 — [Area Name]    <!-- MANDATORY — Part 28 Area 18 -->
*Reference: 1.1.1.001.01*

*[Date line, Rule 7.2.2b]*

[Area 1, paragraph 1]

[Area 1, paragraph 2]
```

*A later Area of the same Chapter (Area Title Block, date line and body; no Chapter Header Block) — `.../chapter-001/area-02.md`:*

```markdown
## Area 2 — [Area Name]    <!-- MANDATORY — Part 28 Area 18 -->
*Reference: 1.1.1.001.02*

*[Date line, Rule 7.2.2b]*

[Area 2, paragraph 1]

[Area 2, paragraph 2]
```

The blocks are the output of `.claude/tools/area_md_creator.py`; text in square brackets stands for the names, the date line and the prose that are supplied (the date line's form and content are Part 41's, Area 5, The date line; the examples show only where it stands). The date line is typed as the first paragraph of the text handed to the script, and the script passes it through as typed (Rule 7.2.2b). A file whose Area is also the first of a Phase or of a Section opens with the Title Page of Rule 7.2.1a.

**Rule 7.3.2 — Scene Break Between Areas (On-Demand Chapter File).**
In the Chapter file `Chapter NNN - <Chapter Name>.md` produced on demand via `/chapter-builder`, the Chapter Header Block is followed by the Chapter's date line (once) and the first scene, and a horizontal rule (`---`) separates each pair of consecutive Areas' scenes; the `---` is the only Area boundary, with no Area Title Block and no reference code (the `.docx` shows it as a centred `*   *   *`). A scene whose date differs from the previous scene's opens, directly after its break, with its own date line; a scene on the same date has none. Per-Area files themselves do not include inter-Area horizontal rules — they carry only the Chapter Header Block / Area Title Block prefix appropriate to their position. **[Amended 2026-10-07]** Replaces the join of Area files with an Area Title Block per Area.

### 7.4 — Python Implementation for .md Files

**Rule 7.4.1 — Implementation Standard.**
All `.md` file creation and update operations use standard Python file I/O through the authorized script `.claude/tools/area_md_creator.py`. No external library is required. Call the script directly rather than reproducing code in canon text.

**Rule 7.4.2 — Dependency.**
Standard Python file I/O. No external library required beyond the Python standard library.

**Rule 7.4.3 — Error Handling.**
Same as Rule 6.4.5. If the `.md` write fails, the failure is reported in chat, the `.docx` already written for this Area is removed, Gate 2 stops before the Post-Write Ledger Update and the spec as-built sync, and the author re-issues `[CONFIRM WRITE]` to try again from the text still in the conversation.

### 7.5 — Markdown Update Protocol (Two-Gate Flow)

**Rule 7.5.1 — Trigger Point (Per-Area).**
The per-Area `.md` write occurs at Gate 2b (Step 8) of the `/next-area` command flow (see Rule 6.5.1). It executes immediately after the per-Area `.docx` write (Gate 2a / Step 7) and before the Post-Write Ledger Update (Step 9). Both file writes occur in the same Gate 2 cycle, following a single Inter-Gate Confirmation (`[CONFIRM WRITE]`) for that specific Area, maintaining guaranteed parity between the `area-NN.docx` and `area-NN.md` of that Area.

**Rule 7.5.2 — Rewind Behavior.**
Same as Rule 6.5.3. When `/rewind-to` archives non-canonical prose, the corresponding `area-NN.md` files after the rewind point are moved to the archive folder with their `.docx` pair (Rule 5.3.2a); new prose written forward creates fresh `.md` files at the same narrative positions.

**Rule 7.5.3 — Aggregate Invalidation.**
If a Chapter file `Chapter NNN - <Chapter Name>.md` exists in the Novel-Part folder for the Chapter whose per-Area file is being created or overwritten, the Chapter file is stale by the test of Rule 5.3.5. Equivalent behavior applies to any Phase-aggregate `phase-N-complete.md` or Novel-aggregate `starward-saga-complete.md`. Stale files must be regenerated on the next invocation of their producing command (`/chapter-builder` for Chapter files, `/compile-phase-md` for Phase aggregates, `/compile-novel-md` for the Novel aggregate), or deleted outright. **[Amended 2026-10-07]**

### 7.6 — Governing Constraints

**Rule 7.6.1 — Per-Area Parity.**
Each Area's `.md` file must always contain exactly the same prose body as its paired `.docx` file. Any operation that writes to one must write to both. An `area-NN.md` file that is out of sync with its paired `area-NN.docx` is a canon output error.

**Rule 7.6.2 — No Governance Content.**
The `.md` file contains only the novel's prose, formatted per this Area's standards, plus the three permitted structural elements where they apply: the Title Page block on the first Area file of a Phase or of a Section (Rule 7.2.1a), the Chapter Header Block on the first Area file of a Chapter, and the Area Title Block on every Area file. Audit reports, ledger data, governance citations, and planning notes are never written to per-Area output files, except the MANDATORY marker: the HTML comment `<!-- MANDATORY — Part 28 Area 18 -->` that the templates of Rules 7.2.1 and 7.2.2a place after the name lines. Most Markdown viewers do not display it, and it stays in every file.

**Rule 7.6.3 — Plain-Text Portability.**
The `.md` file is formatted to be fully readable as plain text even without a Markdown renderer. Formatting markers (`*`, `**`, `***`, `##`) are minimal and do not obscure the prose when read as raw text.

**Rule 7.6.4 — One Area Per File.**
**[Amended 2026-10-07]** Governs the per-Area files of the Area-built path only; a Chapter built whole has none (Rule 6.3.4a), and its Chapter `.md` carries the hidden `<!-- AREA NN -->` markers that file does not otherwise show. Each `area-NN.md` contains the body of exactly one Area. Appending additional Area bodies to an existing per-Area file is forbidden.

### 7.7 — Gate 1 Position Header Block Boundary (Chat-Only)

**Rule 7.7.1 — Chat-Only Placement.**
The Gate 1 Position Header Block (Rule 6.7.1) is a **chat-only** artefact. It is **never** written to any `area-NN.md` file. Any occurrence of the Position Header Block inside a `.md` file is a structural contamination and a Post-Write Audit FAIL under the gate law.

**Rule 7.7.2 — Distinction from Markdown Chapter Header Block and Area Title Block.**
The Gate 1 Position Header Block is categorically distinct from the Markdown-format Chapter Header Block (Rule 7.2.1) and Area Title Block (Rule 7.2.2a). The markdown Chapter Header Block and Area Title Block are reader-facing `# / ## / ---` structures that live inside designated `.md` files; the Gate 1 Position Header Block is a governance-facing chat-only orientation block. The artefacts have disjoint placements: Gate 1 Position Header Block → chat only; Chapter Header Block → first Area `.md` file of each Chapter; Area Title Block → every Area `.md` file.

**Rule 7.7.3 — Cross-Reference.**
For the canonical format of the Gate 1 Position Header Block see Rule 6.7.3. For the audits that verify both chat-level Gate 1 delivery and `.md` / `.docx` Gate 2 file integrity, see `.claude/guardrails/audit/guardrail-audit-gate-law.md`.

---

## Area 8 — Post-Area Audit Completeness Indicator Law

### 8.1 — Purpose and Mandate

**Rule 8.1.1 — Purpose.**
The Post-Area Audit Completeness Indicator is a two-component block emitted after every accepted Area:

**Component 1 — Narrative Position Block (governed by Part 2 Area 8):** A tentative, advisory block reporting the system's current best estimate of where that Area sits within the Phase 1 structural envelope defined by Part 30 (Macro Story Law) and the five-tier hierarchy of Part 2 Area 1. It is not a canon decision, not an enforcement mechanism, and not a commitment to a specific total Area/Chapter/Part/Section/Phase count — it is a navigation aid so the user can track progress toward Phase 1 end-state Locked Canon (Part 30 Section 1.3.1) without manually auditing the narrative position.

**Component 2 — CDL-2 Category Block (governed by Part 35 Area 4):** The mandatory content density scoring block showing the Area's CDL-2 scores across all content categories (Part 35 Area 1.2), the running Section aggregate, and ON TRACK / WARN status per category against the active Section targets from Part 35 Area 3, with an information line where an Anchor category is below its 20% reference line. This block is information only for every category, the four Universal Anchor Floors (Combat, Cultivation Growth, Dialogue & Social, Lore & World-Building) included. Part 35 Area 4 governs the CDL-2 block format; Part 2 Area 8 governs the narrative position block. Both blocks are emitted as a single post-Area output (Block A and Block B of the gate law).

**Rule 8.1.2 — Mandate.**
Every writing command (`/start-story`, `/next-area`, `/next-chapter`, `/next-part`, `/next-section`, `/next-phase`, `/revise-area`, `/redraft-area`, `/redraft-chapter`) that accepts an Area into canon must emit the Post-Area Audit Completeness Indicator block immediately after the Post-Write Ledger Update and before the next user prompt. This is required by the gate law and operationalized here.

### 8.2 — Canonical Block Format

**Rule 8.2.1 — Block Format.**
The indicator is emitted as the following ASCII block, with numeric estimates filled in per the current narrative position and the governing Phase 1 End-State Locked Canon. Each "~M" value is tentative — the system's current best estimate, subject to revision as the story develops. The "N" values are exact counts of accepted canon content.

```
┌─────────────────────────────────────────────────────────────┐
│ POST-AREA COMPLETENESS INDICATOR (tentative, advisory)      │
├─────────────────────────────────────────────────────────────┤
│ Areas in Chapter C of Part P:                  N of ~M      │
│ Chapters in Part P of Section S:               N of ~M      │
│ Parts in Section S of Phase Φ:                 N of ~M      │
│ Sections in Phase Φ:                           N of ~M      │
└─────────────────────────────────────────────────────────────┘
```

**Rule 8.2.2 — Tentativeness Marker.**
The `~` prefix on M is a mandatory tentativeness marker. It signals that M is an estimate and may shift as the story develops. N values carry no `~` because they are exact counts.

**Rule 8.2.3 — Phase 1 Envelope Source.**
M estimates at the Section level are anchored to Part 30 Section 1.3.1 (Phase 1 End-State Locked Canon) and Part 30's Phase 1 arc map (8 Sections). The M estimate at the Area row is drawn from the Chapter Spec's Area list (Part 38) and revised as the story progresses; it has no Locked Canon anchor and is labeled tentative to reflect this. The two rows "Chapters in Part P of Section S" and "Parts in Section S of Phase Φ" read no stored range, because none is stored above Chapter grain (Rule 9.3.1, Rule 9.13.2): their ~M reads the current length of the plan list in the Novel-Part Spec (Chapters) or the Section Spec (Novel-Parts), as information only, and reads `undeclared` while no such list is confirmed. Where no bracket is declared for a tier, its ~M reads `undeclared` (Rule 9.10.1 notation). The "Sections in Phase" row reads Part 30's eight Sections. The ~M values stay tentative, advisory and never a limit (Rule 8.3.1, Rule 8.3.2).

### 8.3 — Governing Constraints

**Rule 8.3.1 — Advisory Only.**
The Completeness Indicator is advisory. It does not constrain narrative structure. A Chapter may end before N reaches ~M, or continue after N exceeds ~M. The indicator tracks; it does not govern.

**Rule 8.3.2 — No Canon Authority.**
M estimates are not Locked Canon. They may not be cited as a rule basis for audit findings, consequence rulings, or structural decisions. The governing structure law remains Part 2 Area 1 (five-tier hierarchy) and Part 30 (Macro Story Law).

**Rule 8.3.3 — Skip Write Behavior.**
On `[SKIP WRITE]` the draft is discarded and no Completeness Indicator is emitted: no Area was accepted, so no count moves and there is no divergence to flag.

---

## Area 9 — Scope Visibility Protocol (Non-Binding Planning Guidance)

### 9.1 — Status of this Area

**Rule 9.1.1 — Non-Binding Status.**
This Area is non-binding planning guidance. It does not amend, override, or qualify Part 2's load-bearing principle that no tier exists as a bureaucratic container, that every tier opens because the story demands it and closes when its narrative event reaches closure, and that no tier carries a minimum or maximum count. The Scope Visibility Protocol defined below is a comfort instrument for the author. It is never a stop-condition, never a fill-condition, and never accrues canonical weight by repetition.

**Rule 9.1.2 — Subordination to Story-Demanded Principles.**
Where any provision of this Area appears to conflict with Principle P2-2 (Structure Serves Story, Not the Reverse), Area 1 Tier 1 §1.1.5 (Section count), Tier 3 §1.3.2 (Novel-Part count), Tier 4 §1.4.3 (Chapter length), Tier 5 §1.5.3 to §1.5.6 (Area sequencing, count, size and continuity), §1.6.4 (Area continuity), or Part 28's depth mandate, those story-demanded principles prevail without exception. The bracket bends; the narration does not.

### 9.2 — Purpose

**Rule 9.2.1 — Forward Visibility.**
The Protocol exists to surface scope questions at the point where they are cheapest to address — at tier-open, rather than at tier-close — by giving the author a declared, visible, and continuously readjusted tentative range for the number of child units the current tier is expected to contain. The range is a moving target. It is restated at every Area close and at every child-tier close, and is allowed to expand, contract, or dissolve based solely on what the tier's own plot-plus-context unit continues to demand.

**Rule 9.2.2 — Distinction from Area 8.**
The Post-Area Completeness Indicator (Area 8) reports the system's current best estimate of position within Phase 1's End-State Locked Canon envelope (N of ~M form). The Scope Visibility Protocol (this Area) declares per-tier *brackets* (N–M ranges with rationale and last-readjusted locator) for tiers below Phase. The two are complementary: Area 8 anchors to Locked Canon endpoints; Area 9 anchors to currently-active tier plot units. Both are advisory; neither governs.

### 9.3 — Scope of Application

**Rule 9.3.1 — Applicable Tiers.**
The Protocol applies at three tiers:
- **Section** (no separate range is declared or stored: the Novel-Part list in the Section Spec is the guide, and the length of that list is read as information only)
- **Novel-Part** (no separate range is declared or stored: the Chapter list in the Novel-Part Spec is the guide, and the length of that list is read as information only)
- **Chapter** (tentative Area count, read from the Chapter Spec's Area list)

It does not apply at **Phase** tier (governed by Part 30's locked Section count) and does not apply at **Area** tier (the Area is the atomic written unit and has no child count to bracket).

The Section Spec and the Novel-Part Spec (Part 38 Rule 38.10, Rule 38.11) carry a plan list of their children (Novel-Parts, and Chapters in depth), so the figure is not stored a second time. The bracket is never a stop-condition, a fill-condition or a limit on narrative choice (Rules 9.6.1 to 9.6.3 apply to a plan list's length exactly as they apply to a range). How the Section and Novel-Part tiers show in the Position Display and the Completeness Indicator is set in Rule 9.13.2 and Rule 8.2.3.

**Rule 9.3.2 — Optional at Any Tier.**
The Protocol is optional at any tier. The author may decline to declare a bracket at any tier-open without penalty where the tier's shape is judged too uncertain to bracket meaningfully at open. Declined brackets are recorded as `undeclared` per Rule 9.10.1.

### 9.4 — Declaration at Tier-Open

**Rule 9.4.1 — Tier-Open Declaration.**
When a tier opens — and before its first child unit's first Area is written — the author may declare a tentative range of the form `N–M` child units, accompanied by a one-line rationale tying the range to the tier's identified plot-plus-context unit per Part 2 §1.4.1 (Chapters), §1.3.1 (Novel-Parts), or §1.2.1 (Sections).

**Rule 9.4.2 — Declaration Recording.**
The declaration is recorded in the Position Display under a dedicated line labelled `TIER SCOPE BRACKET (tentative, non-binding)` per Rule 9.10.1. The label's wording makes the non-binding status visible on every subsequent Position Display emission, so the bracket cannot silently promote itself into a governing count.

**Rule 9.4.3 — Retroactive Declaration.**
Where a tier has already opened without a bracket declaration, the author may declare the bracket retroactively at any subsequent Area close within that tier. Retroactive declarations carry the same non-binding status as tier-open declarations and are recorded in the Position Display from that Area forward.

### 9.5 — Continuous Readjustment

**Rule 9.5.1 — Reassessment at Every Child-Unit Close.**
At every child-unit close within the tier (for the Chapter tier, at every Area close), the author reassesses the bracket. Three outcomes are permitted and none requires justification beyond one line on record:
- **Confirmed unchanged** — bracket bounds remain as declared
- **Narrowed** — lower bound raised, upper bound lowered, or both
- **Widened** — lower bound lowered, upper bound raised, or both

**Rule 9.5.2 — Bracket Dissolution.**
A fourth outcome — dissolution of the bracket with a `story-demanded, bracket no longer informative` note — is permitted whenever the tier's shape has diverged far enough from the original declaration that the bracket is misleading rather than helpful. Dissolution does not close the tier; only narrative closure closes the tier.

**Rule 9.5.3 — Readjustment Logging.**
Every readjustment is logged in the Position Display with the new range and a one-line reason per Rule 9.10.1. The readjustment log is planning telemetry, not canon. It generates no audit findings, no consequence rulings, and no structural commitments.

### 9.6 — Prohibited Uses

**Rule 9.6.1 — Never a Stop-Condition.**
The bracket must never be used as a stop-condition. Reaching or exceeding the upper bound is not a reason to close the tier. Only the tier's own narrative closure — plot unit resolved, context unit complete, continuity handoff ready per the relevant tier-continuity provision — closes the tier.

**Rule 9.6.2 — Never a Fill-Condition.**
The bracket must never be used as a fill-condition. Sitting below the lower bound is not a reason to extend the tier, introduce padding Areas, or delay closure. Only the tier's plot-plus-context unit's incompletion extends it.

**Rule 9.6.3 — Never a Constraint on Narrative Choice.**
If a scene demands more time on the page than the bracket anticipated, the scene gets its time. If a scene resolves faster than the bracket anticipated, the scene closes when it resolves. The bracket exists to inform the author of the shape ahead; it never overrides what the story is telling the author to do at the sentence level.

### 9.7 — Immersion Precedence

**Rule 9.7.1 — The Depth Mandate Prevails.**
Where the bracket and the depth mandate (Part 28 Area 4, Named Depth Pillars DP-1 through DP-10) appear to pull in opposite directions, the depth mandate prevails absolutely. An Area that requires fuller rendering to meet the Immersion Standard is rendered in full regardless of whether the bracket's upper bound has been reached. An Area that compresses cleanly without immersion loss is allowed to compress regardless of whether the bracket's lower bound has been reached.

**Rule 9.7.2 — Immersion as Ceiling and Floor.**
Immersion is the ceiling and the floor of every rendered Area. The bracket is the weather report — informative about what is ahead, never determinative of what is rendered now.

### 9.8 — Continuity Precedence

**Rule 9.8.1 — Inter-Tier Continuity Prevails.**
Where the bracket and the inter-tier continuity principles (Part 2 §1.5.6 and §1.6.4 for Areas, and the equivalent provisions at Chapter, Novel-Part, and Section tiers) appear to pull in opposite directions, continuity prevails absolutely. A tier closes where continuity permits it to close — at a natural handoff beat, with no narrative disjoint, with no unexplained gap in time, location, or character state — not where the bracket suggests.

**Rule 9.8.2 — Continuity-Driven Readjustment.**
If continuity requires an additional Area to land the handoff cleanly, the additional Area is written and the bracket is readjusted upward on record per Rule 9.5.3. If continuity permits closure earlier than bracketed, closure is taken and the bracket is readjusted downward on record.

### 9.9 — Amendment on Overrun or Undershoot

**Rule 9.9.1 — Closure-Time Recording.**
If a tier closes at a child-unit count above the declared upper bound or below the declared lower bound, the closure is recorded with a one-line reason for the divergence. The reason is calibration data for future tier-open declarations and carries no corrective, penalising, or revisionary weight.

**Rule 9.9.2 — Calibration Pattern Recognition.**
Over time, a pattern of systematic divergence at a given tier-type (for example, Chapters of audience scenes tending to budget four Areas and run six) becomes useful author-level calibration. It never becomes a canonical correction and never modifies any rule of this Part or any other Part.

### 9.10 — Position Display Integration

**Rule 9.10.1 — Position Display Line Format.**
The Position Display is the post-write display of the gate law, and its Block B carries the Tier Scope Bracket lines. The Protocol adds to it one line per active tier bracket, emitted after every Area close and after every tier close. The line's form is:

```
TIER SCOPE BRACKET (tentative, non-binding): [tier-name] N–M child-units | rationale: [one line] | last readjusted: [Area locator]
```

Where a tier declines to declare a bracket, the line is emitted as:

```
TIER SCOPE BRACKET (tentative, non-binding): [tier-name] undeclared | reason: [one line]
```

Dissolved brackets are emitted as:

```
TIER SCOPE BRACKET (tentative, non-binding): [tier-name] dissolved at [Area locator] — story-demanded, bracket no longer informative
```

**Rule 9.10.2 — Multi-Tier Emission.**
A Position Display may carry up to three active TIER SCOPE BRACKET lines simultaneously (one per active tier per Rule 9.3.1). The lines are emitted in tier order from broadest to most granular: Section, then Novel-Part, then Chapter. Undeclared and dissolved tiers are still emitted with their respective notation per Rule 9.10.1.

**Rule 9.10.3 — Emission Trigger.**
The TIER SCOPE BRACKET lines are emitted at every Position Display emission of the gate law — that is, after every accepted Area by every writing command (`/start-story`, `/next-area`, `/next-chapter`, `/next-part`, `/next-section`, `/next-phase`, `/revise-area`, `/redraft-area`, `/redraft-chapter`). They are also emitted on tier-close events (Chapter close, Novel-Part close, Section close) within the closing tier's terminal Area Position Display.

### 9.11 — Review on Phase Close

**Rule 9.11.1 — Optional Retrospective.**
At each Phase close (Part 30-governed boundary), the author may conduct a retrospective pass over the Phase's bracket history — all tier-open declarations, retroactive declarations, readjustments, dissolutions, overruns, and undershoots — to inform the next Phase's tier-open declarations.

**Rule 9.11.2 — Private Author Instrument.**
The retrospective is a private author-level instrument. It does not modify canon, does not appear in the Position Display, and does not generate binding rules. It is permitted to generate further non-binding author-level calibration notes filed outside the governing canon.

### 9.12 — Non-Promotion Clause

**Rule 9.12.1 — No Tacit Canonization.**
Nothing in this Area shall, by repetition, by consistency of author practice, or by accumulated readjustment telemetry, acquire binding force. Brackets remain forever advisory regardless of how many Areas, Chapters, Novel-Parts, or Sections have been authored under their declaration.

**Rule 9.12.2 — Explicit Amendment Required.**
If a future amendment to Part 2 wishes to convert any element of the Protocol into a binding rule, that amendment must be made explicitly through the standard Canon Part update process and must be made on the record. Tacit promotion is prohibited. This Rule exists to guarantee that the comfort instrument remains a comfort instrument in perpetuity.

### 9.13 — Story Specification Interface

**Rule 9.13.1 — On-Record Amendment Basis.**
Story specification at Section, Novel-Part and Chapter grain (the spec chain) is governed by **Part 38 — Story Specification Law** (`spec-story-specification-law`; spec files at `.claude/story-memory/phase-section-part-chapter-area-specs/`). Part 2 cedes to Part 38 the authority over the planning artifacts of the spec chain (the Section Spec, the Novel-Part Spec and the Chapter Spec) and over the persistence of Chapter-grain scope ranges; Part 2 retains all authority over the five-tier hierarchy itself, prose execution standards, output file law, and how brackets behave in prose flow. The cession of scope-range storage stops at Chapter grain, because no range is stored for the Section or Novel-Part tier (Rule 9.3.1). One place holds the plan, with Part 2 keeping the hierarchy, the prose standards and the file law.

**Rule 9.13.2 — Spec-Backed Bracket Ranges.**
Where an active (confirmed) chapter spec exists, its chapter-level bracket table is the **authoritative source** for the Chapter-tier Tier Scope Bracket range within its scope (Areas in the Chapter; Part 38 Rule 38.5). Tier-open declarations and readjustments at that tier are persisted in the spec; the Rule 9.10.1 `TIER SCOPE BRACKET` line, the Area 8 Completeness Indicator's Chapter-grain `~M` estimate, and (through the bracket) the Part 28 Rule 18.7 Position Header range fields all read from it — one chain, one source.

*Section and Novel-Part tiers.* No range is declared or stored for these two tiers (Rule 9.3.1), so Rules 9.4, 9.5 and 9.9 have nothing to declare, readjust or record there. The `TIER SCOPE BRACKET` line for each of the two tiers is still emitted (Rule 9.10.2), in the `undeclared` form of Rule 9.10.1, with the reason `plan list is the guide` and, once a confirmed Novel-Part list (Section Spec) or Chapter list (Novel-Part Spec) exists, `list length N (information only)`. The Part 28 Rule 18.7 Position Header total for the Novel-Part line and for the Chapter line is left out, as Rule 18.7 already provides where no range estimate has been authored. A plan list that grows, or is split, merged or cut, is variance noted in the spec chain (Part 38 Rule 9.4.5, Rule 9.7.3), never an overrun or an undershoot. The declaration and readjustment mechanics of Rules 9.4–9.5 apply at the Chapter tier, whose range lives in the Chapter Spec.

**Rule 9.13.3 — Spec-Settled Items as DCG Decision Inputs.**
Part 38 spec-settled items — items the author explicitly answered at spec-build or confirmed amendment — are valid decision inputs under Part 28 Rule 19.4 (No-Asking-What-Canon-Already-Settles) and are not re-asked at writing time, subject to Part 38 Area 4's carve-outs. The settled items of a confirmed Section Spec or Novel-Part Spec count the same way. They reach writing time through the Chapter Spec, which carries each one with its source in its Audit and Settlement Notes (Part 38 Rule 9.5.1, Rule 38.12); an author deferral to writing is carried into the Chapter Spec's Audit and Settlement Notes as a Deferred note and is asked at the writing-time gate like any other open item (Part 38 Rule 9.5.2). The carve-outs that govern settled items carried down from the upper specs are in Part 38 Rule 9.5.3. Part 38 Area 4's carve-outs are: open items in the spec's Audit and Settlement Notes, genuinely new branches, and any item whose clarity has reduced are asked; Part 36 Area 13 Autonomous Matters are never spec-fixed, except the author's optional levers: the sensory anchor, tone and voice, and content fields (Part 38 Rules 2.3.5a, 2.3.5b and 2.3.5d). A spec is never a source of established canon facts (Part 38 Rule 38.3 — Locked Canon > ledger > spec > session-log; ledger supersedes spec); this holds for every spec of the chain, and a settled item in a Section Spec or Novel-Part Spec never establishes canon either (Part 38 Rule 1.3.2, Rule 38.12).

**Rule 9.13.4 — Advisory-In-Force Semantics Unchanged.**
This Area's advisory-in-force semantics continue to govern how spec-backed ranges behave in prose flow, in full and without exception: Rule 9.6.1 (never a stop-condition), Rule 9.6.2 (never a fill-condition), Rule 9.7 (immersion precedence), Rule 9.8 (continuity precedence), and Rule 9.9 (overrun/undershoot as calibration, never correction). Spec-backed ranges remain tentative low–high bands; in-flow readjustments proceed per Rules 9.5.1–9.5.3 and are written back to the spec at Gate 2 by the Part 38 as-built sync. The bracket bends; the narration does not. The Gate 2 sync writes the Chapter Spec only. It never writes the Section Spec or the Novel-Part Spec, and the plan-list lengths of Rule 9.13.2 are information that the same Rules 9.6.1, 9.6.2 and 9.6.3 keep from ever acting as a stop-condition, a fill-condition or a constraint on narrative choice.

---

## Area 10 — Chapter Export Format Specification

### 10.1 — Purpose and Scope

**Rule 10.1.1 — Novel-Grade Export Mandate.**
When `/chapter-builder` is invoked, the resulting `Chapter NNN - <Chapter Name>.docx` is typeset to the novel-grade standard defined in Area 6 (EB Garamond, 6×9, 1.15×, with phase icon, drop cap openings, and running headers/footers) from the condensed Chapter text, and the companion `Chapter NNN - <Chapter Name>.md` is written from the same text (Rule 10.1.3). **`/chapter-builder` is a condensing operation, not an assembly**: the Area Maker condenses the Chapter's finished Areas into one text of 50% to 60% of the Areas' characters (spaces counted, narration paragraphs only), the author confirms it, and only then does `chapter_builder.py` write the pair; the script refuses a text outside the band. No per-Area `.docx` is concatenated. No PDF is produced. The pair is orchestrated by the `/chapter-builder` command and written exclusively by `.claude/tools/chapter_builder.py` (authorized script 6, which imports its typeset helpers from `area_docx_creator.py` and `area_md_creator.py`). The per-Area `.md` source files remain the authoritative canonical substrate for content; the `.docx` per-Area files are the authoritative format substrate (Rule 7.1.2). **[Amended 2026-10-07]** Replaces the `/export-chapter` assembly.

**Rule 10.1.2 — Dual Output Mandate.**
Every Chapter file build produces both a DOCX file and a Markdown file: the publication-format `Chapter NNN - <Chapter Name>.docx` and the coupled `Chapter NNN - <Chapter Name>.md`, written together. Both files are written to the Novel-Part folder (`phase-N/section-N/part-N/`), beside the `chapter-NNN/` folders and not inside them. No PDF is produced. **[Amended 2026-10-07]** Formerly `chapter-NNN/chapter-NNN.docx` and `chapter-NNN/chapter-NNN.md`.

**Rule 10.1.3 — Source Files.**
The Chapter file is built from the Chapter's finished Areas (every Area row of the Chapter Spec terminal and its `area-NN.md` present, `_archive` never read), read in canonical order (Area number, sorted as an integer), and from the Chapter Spec. The Area Maker writes the condensed text to the staging folder `.claude/temp/`, the author confirms it, and `chapter_builder.py` writes the `.docx` and `.md` from that text: one date line at the top, the scenes of the Areas separated by `---` (`.md`) or a centred `*   *   *` (`.docx`), no Area Title Block, no Area reference code, no per-Area heading, and a scene date line only where its date differs from the previous scene's (Rules 7.2.4 and 7.3.2). The per-Area files are read and never changed. **[Amended 2026-10-07]** Replaces the join of Area files.

### 10.2 — Page and Typography Standards

**Rule 10.2.1 — Page Size.**
The exported document uses 6" × 9" trade paperback trim size — the standard for fantasy and science-fiction hardcovers and trade paperbacks.

**Rule 10.2.2 — Margins.**
Left and right margins: 0.875 inches. Top and bottom margins: 1.0 inch. These match the standard interior margins for trade paperback fiction.

**Rule 10.2.3 — Body Font.**
Body font: EB Garamond, 12pt. EB Garamond is a classical serif typeface standard in fantasy and literary fiction. It must be installed on the user's system for the DOCX to display correctly. If EB Garamond is not installed, the document falls back to the system's default serif font gracefully; the font name specification in the DOCX is still written as "EB Garamond".

**Rule 10.2.4 — First-Line Indent.**
All body paragraphs use a 0.3" first-line indent, matching the standard for trade paperback prose indentation. The first paragraph of narration of an Area (after the Area Title Block and the date line; in the Chapter file, the first paragraph after the opening date line or after a scene's own date line) uses no first-line indent — classic novel typography convention.

**Rule 10.2.5 — Line Spacing.**
Body line spacing: 1.15× (slightly tighter than double-space manuscript format, matching published trade paperback standards for 12pt type on a 6×9 page).

**Rule 10.2.6 — Paragraph Spacing.**
No additional space before or after body paragraphs (space_before = 0, space_after = 0). Paragraph separation is conveyed entirely through first-line indent, not spacing.

### 10.3 — Header Hierarchy

**Rule 10.3.1 — Export Header Hierarchy.**
The Chapter file document uses the following header hierarchy, rendered in EB Garamond, centered, black (the H4 row applies to the per-Area `.docx` files only; the Chapter file has no Area title, **amended 2026-10-07**):

| Level | Content | Size | Weight |
|---|---|---|---|
| H1 | Section name (e.g., "SECTION 1 — AZURE SKY AND GALE") | 16pt | Bold |
| H2 | Part name (e.g., "PART 1 — Before the Turning") | 16pt | Bold |
| H3a | Chapter number (e.g., "Chapter 001") | 16pt | Bold |
| H3b | Chapter title (e.g., "Twin Courts at Dawn"), on the same line as the number after an em dash | 16pt | Bold |
| H4 | Area title (e.g., "Area 1 — Paired Sovereigns"), with the phase icon above it and the Reference Code line below it (Rule 10.3.5) | 12pt | Bold |

The Reference Code line below the Area title is 10pt Regular Italic (Rule 6.3.2a), and "STARWARD SAGA" and the Phase line sit above the Section line in the Section line's style (Rule 6.3.1). These sizes and weights are the ones `area_docx_creator.py` applies.

**Rule 10.3.2 — Section and Part Headers.**
Section and Part names appear once at the beginning of the document, before the Chapter line. They serve as context headers for the reader and are not repeated.

**Rule 10.3.3 — Chapter Opening.**
The Chapter Header Block opens the chapter document: the Part line is followed by one blank line and then the Chapter line (H3a and H3b together on one line, Rule 6.3.1). The script inserts no page break between them.

**Rule 10.3.4 — Area Transition.**
In the per-Area files every Area — including the first Area of a Chapter — opens with its Area Title Block (H4), the line "Area N — [Area Name]" with the phase icon above it and the Reference Code line below it (Rule 6.3.2a). In the Chapter file there is no Area Title Block: the transition from one Area's scene to the next is the centred `*   *   *` scene break (Rule 10.5.1), and the scenes run on within the chapter document. **[Amended 2026-10-07]**

**Rule 10.3.5 — Area Title Block.**
Before the body of every Area in a per-Area file, the phase icon (Rule 10.4.1) is inserted, followed by the Area title (H4) and the Reference Code line; this holds for the first Area of a Chapter as it does for every later Area. In the per-Area files the Area Title Block is the Area's opening, and the one other mark at the top of an Area is the date line (Rule 6.3.2b), a plain italic paragraph that is not a heading, icon or reference code. The Chapter file carries no Area Title Block, and no Area title, icon or reference code appears in it. **[Amended 2026-10-07]**

### 10.4 — Phase Icon Ornament

**Rule 10.4.1 — Icon Specification.**
Each Phase has a dedicated ornamental icon stored as both SVG and PNG in the Phase folder:
- SVG: `novel-starward-saga/phase-N/phase-icon.svg`
- PNG: `novel-starward-saga/phase-N/phase-icon.png`

> **[Repo layout note]** `novel-starward-saga/phase-N/phase-icon.svg` above refers to `projects/novel-starward-saga/phase-N/phase-icon.svg` in the current repo layout (post-.claude/ migration).
> **[Repo layout note]** `novel-starward-saga/phase-N/phase-icon.png` above refers to `projects/novel-starward-saga/phase-N/phase-icon.png` in the current repo layout (post-.claude/ migration).

**Rule 10.4.2 — Phase 1 Icon Design.**
Phase 1 ("The Roots of Becoming") icon: deep navy roots reaching downward from a horizon line (representing the roots of cultivation, the anchoring of the world to its foundations), with a gold star cluster kindling above (representing the cosmos, destiny, and the Turning to come). Colors: deep navy (#1A2A4A) for roots; gold (#C8972B central, #D4A843 mid, #E0BB6A far) for stars. Dimensions: 300×360 px PNG at 1.5× scale.

**Rule 10.4.3 — Icon Placement and Size.**
The phase icon PNG is inserted centered above every Area title in the per-Area files, and so once per Area (Rule 10.3.5); in the Chapter file it appears only where the Chapter Header Block carries it (Rule 6.3.1), not once per Area. **[Amended 2026-10-07]** Display width: 0.55 inches. Space before icon: 12pt. Space after icon: 4pt. The icon is visually small — an ornament, not an illustration.

**Rule 10.4.4 — Icon Generation.**
The PNG is generated by `.claude/tools/saga_image_creator.py`, the sole authorized phase/section image generator (`.claude/guardrails/tools/guardrail-authorized-scripts-only.md`), via the `/create-image-phase` and `/create-image-section` commands. The PNG is generated once and stored; it does not need to be regenerated for each export unless the icon design is updated.

### 10.5 — Area Separation

**Rule 10.5.1 — Area Separation.**
Between the scenes of consecutive Areas the Chapter file carries one scene break and nothing else: a centred `*   *   *` line in the `.docx` and a `---` line in the `.md`. There is no Area Title Block, no Area reference code, no page break and no extra heading. A scene opens with its own date line (Rule 6.3.2b) directly after the break only when its date differs from the previous scene's; on the same date the line is not repeated. The ⁂ asterism appears only as the mark of a brief time skip inside an Area (Rule 6.3.5); it is never the boundary between Areas. In a Chapter built whole (Rule 6.3.4a) the break appears only at a change of scene or a change of POV within a scene, and a scene continuing across Area blocks in one POV has no visible break. **[Amended 2026-10-07]** Formerly the Area Title Block carried in each Area file was the boundary.

**Rule 10.5.2 — All Areas Including First.**
The Chapter file's text opens with the date line once, directly after the Chapter Header Block (and the Title Page where it applies), and then the first Area's scene begins; no Area Title Block precedes the first Area or any later Area. In the per-Area files the Area Title Block still appears before every Area, including the first Area of a Chapter, where it follows the Chapter Header Block directly on the same page. **[Amended 2026-10-07]**

### 10.6 — Running Headers and Footers

**Rule 10.6.1 — Even Page Header.**
Even pages (left-hand pages): "STARWARD SAGA" centered, EB Garamond 9pt, color #5A5A5A (mid-grey).

**Rule 10.6.2 — Odd Page Header.**
Odd pages (right-hand pages): Chapter title in full caps (e.g., "TWIN COURTS AT DAWN") centered, EB Garamond 9pt, color #5A5A5A.

**Rule 10.6.3 — Page Numbers.**
Page numbers appear at the outer bottom edge of each page — left-aligned on even pages, right-aligned on odd pages. EB Garamond 9pt. Rendered as a PAGE field so they update dynamically with DOCX pagination.

**Rule 10.6.4 — First Page Exception.**
The first page of the document (the Title Page where one applies, otherwise the Chapter Header Block page) has a blank header and blank footer — standard novel convention for opening pages.

**Rule 10.6.5 — Implementation.**
Running headers require both `different_first_page_header_footer = True` and `odd_and_even_pages_header_footer` enabled at the document-level settings. python-docx exposes `even_page_header`, `even_page_footer`, `header` (odd), and `footer` (odd) on each section object.

### 10.7 — First Paragraph Treatment

**Rule 10.7.1 — Drop Cap.**
The first paragraph of narration of each Area, including the first Area of the Chapter (after the Area Title Block and the date line), receives a drop cap treatment (in the Chapter file, the first paragraph after the opening date line and the first paragraph of any scene that carries its own date line; a scene with no date line starts with no indent and no drop cap, **amended 2026-10-07**): the first character is rendered in 28pt bold EB Garamond (approximately three text lines tall). The date line (Rule 6.3.2b) is not that paragraph: the drop cap of this rule and the small caps of Rule 10.7.2 fall on the first paragraph of narration, the one after the date line.

**Rule 10.7.2 — Small Caps.**
Immediately following the drop cap character, the next approximately four words are rendered in small caps (EB Garamond small caps). This is the classic "chapter opening" convention used by major fantasy publishers including Tor, Del Rey, and Orbit.

**Rule 10.7.3 — Remainder.**
The remainder of the opening paragraph after the small caps words continues in standard body style (EB Garamond 12pt, italic-aware for dialogue).

**Rule 10.7.4 — Italic Dialogue in Opening Paragraph.**
Even within an opening paragraph that begins with a drop cap and small caps, dialogue passages marked `*"..."*` in the source `.md` file are rendered as italic in the export.

### 10.8 — Table of Contents

**Rule 10.8.1 — Contents Page in the Compiled Documents.**
The Chapter file does not include a Table of Contents, and no placeholder is inserted in it. A compiled Phase document (`/compile-phase`) and a compiled novel document (`/compile-novel`) each carry a contents page, built from the Chapter files they join: the Chapter lines (number and title) only, grouped under their Phase, Section and Novel-Part, in reading order; there are no Area lines under a Chapter, because a Chapter file carries no Area names. **[Amended 2026-10-07]** In a Phase document the contents page follows the Phase title page and comes before the first Chapter. The novel contents page covers every Phase and replaces the Phase contents pages in the novel document.

### 10.9 — Export Script

**Rule 10.9.1 — Canonical Implementation.**
The canonical implementation of the Chapter file is the `/chapter-builder` command, which has the Area Maker condense the Chapter's finished Areas into a staged text (`.claude/temp/`), measures it against the 50% to 60% band, and, after the author confirms, writes the pair with `.claude/tools/chapter_builder.py` (`python .claude/tools/chapter_builder.py measure|write ...`), authorized script 6 under `.claude/guardrails/tools/guardrail-authorized-scripts-only.md`. No other method of producing a Chapter file is allowed, and the Chapter file is never joined from per-Area `.docx` files. `.claude/tools/area_docx_creator.py` still joins Chapter files into a Phase file (`assemble_phase_docx`) and Phase files into the novel (`assemble_novel_docx`) and reads one written file back (`check`); these are direct additions to that authorized script, which the guardrail allows, and its former Area-joining function (`assemble_chapter_docx`) was removed on 2026-10-07. There is no separate export script, and none may be created beyond the authorized set; creating an unauthorized script is a Tier 0 Critical Violation. Any change to the Typography Specification (this Area) is reflected in `area_docx_creator.py`, since `chapter_builder.py` imports its typeset helpers from it (and from `area_md_creator.py`). The Area Title Block is decided at write time in the per-Area files only: `.claude/tools/area_docx_creator.py` writes the block of Rule 6.3.2a and `.claude/tools/area_md_creator.py` the block of Rule 7.2.2a for every Area; the Chapter file carries none. **[Amended 2026-10-07]**

**Rule 10.9.2 — Invocation.**
`/chapter-builder <chapter_number> [section_number] [part_number] [phase_number]`. Defaults: the Section, Novel-Part and Phase of the current position (the position `/status` reports), so `/chapter-builder 4` builds the Chapter file of Chapter 4 of the Novel-Part the story is in now; an argument that is given replaces its default. `/compile-phase` and `/compile-phase-md` take `<phase_number>` (default: the current Phase). `/compile-novel` and `/compile-novel-md` take no argument and join every completed Phase.

**Rule 10.9.3 — Overwrite Confirmation.**
If a `Chapter NNN - <Chapter Name>.docx` or `.md` already exists in the Novel-Part folder when `[CHAPTER BUILDER]` is invoked, confirmation is required before overwriting (the `/chapter-builder` confirmation rule); nothing is written before the author's answer. On confirmation, both files are overwritten (`--overwrite`). **[Amended 2026-10-07]** The same holds for every compile command: if its output file already exists, the author is asked before it is replaced, so a copy the author has edited by hand is never replaced silently. Rule 5.3.5 decides whether an existing aggregate is stale or up to date. The output files are `part-N/Chapter NNN - <Chapter Name>.docx` and `part-N/Chapter NNN - <Chapter Name>.md` (`/chapter-builder`), `phase-N/phase-N-complete.docx` (`/compile-phase`), `phase-N/phase-N-complete.md` (`/compile-phase-md`), `starward-saga-complete.docx` (`/compile-novel`) and `starward-saga-complete.md` (`/compile-novel-md`).

### 10.10 — Reader Aids

**Rule 10.10.1 — Reader Aids at Compile Time.**
When a Phase or the novel is compiled (`/compile-phase`, `/compile-phase-md`, `/compile-novel`, `/compile-novel-md`), a cast list, a glossary and a map note may be produced to go with the compiled document. They are built only from facts already established in written prose: no unwritten lore, no planned fact that lives only in a spec, and no ledger fact the prose has not yet shown. Every entry cites the reference code of the Area in which its subject first appears (Phase.Section.Part.Chapter.Area, Rule 6.3.2a). No aid is placed in a compiled document until the author has approved that edition of it; a later compile that has more written prose behind it is a new edition and is approved again. The Chapter file carries none of them (Rule 10.8.1). The compile commands only join Chapter files (Phase) and Phase aggregates (Novel); they never condense and never join Area files. **[Amended 2026-10-07]** The Reference Code of the Area where a subject first appears is still read from the per-Area files, not from the Chapter file.

---

## Appendix A — Cross-References

Part 2's Areas share Cross-References tables. The table that is identical across Areas 1, 2, 3 and 4 is given once in A.1. Areas 6 and 7 each carry Area-specific rows that carry a tie, in A.2 and A.3.

### A.1 — Shared Cross-References Table (Areas 1, 2, 3, 4)

The following table applies to Area 1 (Five-Tier Narrative Hierarchy), Area 2 (Conversation Rules), Area 3 (Combat and Move Rules), and Area 4 (Point of View Governance).

| Related Skill | Relation | Source |
|---|---|---|
| Gate audit (FCIA/ALCA) | Audit governance | `guardrails/audit/guardrail-audit-gate-law.md` governs all Area content produced under this Part |
| `cultivation-power-and-lifespan-law` §Areas 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 | SOFT | Prose depth requires cultivation realm reference for accurate scene-setting |

### A.2 — Area 6 Cross-References (Book Creation Law: Area Document (.docx))

| Related Skill | Relation | Source |
|---|---|---|
| `cultivation-power-and-lifespan-law` §Area 1 | SOFT | Rule 6.2.4 mandates bold-italic docx formatting for qualifying cultivation level designations (full realm+level strings, tier designations); this skill defines the realm/level naming that rule formats — a real but purely typographic tie, not a content dependency |
| `cultivation-power-and-lifespan-law` §Area 9 | SOFT | Rule 6.2.4 mandates bold-italic docx formatting for full affinity+level strings; this skill defines the affinity-cultivation naming that rule formats — a real but purely typographic tie, not a content dependency |

### A.3 — Area 7 Cross-References (Book Creation Law: Area Markdown File (.md))

| Related Skill | Relation | Source |
|---|---|---|
| `cultivation-power-and-lifespan-law` §Area 1 | SOFT | Rule 7.2.6 mandates bold-italic markdown formatting for cultivation level designations (full realm+level strings, tier designations, e.g. "Ruler Level 3 Mid"); this skill defines the realm/level naming that rule formats — a real but purely typographic tie, not a content dependency |
| `cultivation-power-and-lifespan-law` §Area 9 | SOFT | Rule 7.2.6 mandates bold-italic markdown formatting for full affinity+level strings; this skill defines the affinity-cultivation naming that rule formats — a real but purely typographic tie, not a content dependency |

Every other Part 2 x Part 3 pair: no tie.

## Appendix B — Governing Authority (Shared Across All 10 Areas)

The following Governing Authority statement applies to all 10 Areas.

> Subordinate to the guardrails indexed in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.
