---
name: ssc-narration-p29-dialogue-formatting-structural-standards
description: Governs the mechanical formatting and structural placement of dialogue in Starward Saga prose - double-quote-plus-italics mandate, single quotes for nested reported speech, the categorical prohibition of the em-dash and of contractions anywhere in the Prose body, bold-italic marking of Named Moves and cultivation level designations, the ban on script-format attribution, and the rules for dialogue frequency, deliberate silence, and conversation continuity across Area boundaries. Reach for this whenever drafting or auditing any scene containing spoken dialogue, when formatting a Named Move or cultivation-level string inside or outside dialogue, when checking prose for em-dashes or contractions before Gate 1/Gate 2 audit, or when deciding how much narration a dialogue-bearing scene needs. This is canon Part 29 Area 2, domain narration.
user-invocable: false
---

## Rule Text (Verbatim Source — Authoritative)
## Area 2 — Dialogue Formatting and Structural Standards

### 2.1 — Formatting Law

**Rule 29.2.1.1 — Double-Quote and Italics Mandate:** All direct speech is formatted in **double quotation marks AND italics simultaneously**. The canonical rendering is *"the exact spoken words"* — double straight quotation marks enclosing the spoken text, with the entire enclosed text (quotation marks and all) rendered in italics. This applies to every spoken word, from a single syllable to a speech of multiple paragraphs. Italics-only dialogue (no quotation marks) is a Rule 29.2.1.1 violation. Double-quoted dialogue with no italics is a Rule 29.2.1.1 violation. Single quotation marks for direct speech are prohibited (single quotes are reserved for quoted-speech-within-speech per Rule 29.2.1.1a). The mandate is not optional and is not situational. Every word a character speaks aloud is both double-quoted and italicized. This rule is jointly governed with Part 2 Rule 2.2.2 and both must be simultaneously satisfied.

**Rule 29.2.1.1a — Nested Quoted Speech:** When a character reports or quotes another character's speech within their own spoken line, the nested quotation uses single quotation marks inside the outer double-quoted italicized frame. The canonical rendering is *"and then she said to me, 'you will not pass this gate,' as if it were settled."* Single quotes are used only for nested reported speech; they are never used for primary direct speech.

**Rule 29.2.1.1b — Prohibition on the Em-Dash in Dialogue and in Prose:** The em-dash character (—) is **categorically prohibited** in all novel prose — both within dialogue and within narration. The em-dash is a typographical shortcut that compresses what novel-grade prose must render through full clause construction, and its pervasive use produces a reading rhythm that belongs to journalism, commentary, and governance documentation rather than to novel-grade literary fiction. When the author's impulse reaches for an em-dash, the prose must instead use one of the following: a full stop and a new sentence; a colon where the second clause grammatically completes or specifies the first; a semicolon where two independent clauses are closely related; a comma where the interruption is light; parentheses where the interruption is a genuine aside; or a restructuring of the sentence that removes the need for any interruption at all. An en-dash (–) is also not a valid substitute for an em-dash in prose. The prohibition applies to the Prose body only — governance artefacts (Position Header Blocks, Chapter Header Blocks, Area Dividers, Prose Title Blocks, Audit Reports, ledger tables, Cross-Part Dependency tables, and all Part file content) are outside the scope of this rule and may continue to use the em-dash where it serves structural clarity. The scope of "Prose body" is: the text written between the Prose Title Block and the end of the Prose file, excluding any file-level structural blocks. Audit Pass 1 (Rule 7.1.1(k)) and Audit Pass 2 both FAIL if the em-dash character is found anywhere in the Prose body.

**Rule 29.2.1.1c — Prohibition on Contractions in Dialogue and in Prose:** Contractions (*haven't, isn't, don't, won't, can't, I'm, you're, we're, they're, it's, that's, there's, he's, she's, what's, who's, where's, let's, I'll, you'll, we'll, they'll, I'd, you'd, we'd, they'd, I've, you've, we've, they've, wouldn't, couldn't, shouldn't, mustn't, needn't, hasn't, hadn't, weren't, wasn't, aren't, doesn't, didn't,* and all other forms produced by elision of letters and replacement with an apostrophe) are **categorically prohibited** in all novel prose — both within dialogue and within narration. Every contracted form must be rendered in its full expanded form: *have not, is not, do not, will not, cannot, I am, you are, we are, they are, it is, that is, there is, he is, she is, what is, who is, where is, let us, I will, you will, we will, they will, I would, you would, we would, they would, I have, you have, we have, they have, would not, could not, should not, must not, need not, has not, had not, were not, was not, are not, does not, did not.* This rule supersedes and broadens the earlier P29-7 rule (which restricted contractions only in formal and high-stakes speech) — contractions are now prohibited in **all** novel prose, including casual speech, intimate-register speech, combat speech, and narration across every Prose unit and every character voice. The expanded form reads with the weight, formality, and cadence appropriate to novel-grade cultivation fiction; contractions read with the casual register of contemporary conversational journalism and are categorically incompatible with the Starward Saga voice. Proper nouns, place names, and established cultivation-world lexemes that contain apostrophes for non-contraction reasons (possessives, transliterated names) are outside the scope of this rule. The scope of "Prose body" is as defined in Rule 29.2.1.1b. Audit Pass 1 and Audit Pass 2 both FAIL if any prohibited contraction is found anywhere in the Prose body.

**Rule 29.2.1.1d — Bold-Italic Inline Formatting for Named Moves and Cultivation Levels:** Two categories of prose elements must be rendered in ***bold-italic*** (triple-asterisk in Markdown; character-level bold + italic simultaneously in docx and .md) everywhere they appear in the Prose body — both inside dialogue and outside dialogue, at every use:

**(1) Named Moves, Named Techniques, and Named Cultivation Practice names** (as governed by Part 6 Move Taxonomy Law and Part 2 Area 3 Rule 3.2.1): any cultivation technique, combat move, or practice that bears a proper canon-registered name. Examples: ***Ruling Meridian Stance***, ***Sovereignty's Line***. Generic or unnamed references ("the sword form," "the morning form," "a technique") are plain text until a proper name is established in canon.

**(2) Cultivation level designations** (as governed by Part 2 Area 3 Rule 3.2.1a): four sub-categories —
- Full realm+level+sub-level strings: ***Ruler Level 3 Mid***, ***Champion Level 7 Peak***
- Full affinity+level designation strings: ***Sovereignty-Swords Level 8*** (partial refs without level number remain plain)
- Tier designations: ***Mortal Tier 2***, ***Mortal Tier 1 Skin Stage***
- Named meridian designations: ***Void Root***

**Standalone realm names** (Champion, Warrior, Ruler, Monarch, Champion-realm, Warrior-realm, etc.) are **plain text in all prose contexts** — whether describing a character's cultivation level ("a Champion-realm cultivator") or a technical power specification ("Champion-realm energy density"). Standalone realm names are not checked by Gate 1 Check #12 or Gate 2 Rule 10.5.8.

**Audit enforcement:** Gate 1 Check #12 and Gate 2 Rule 10.5.8 (Part 1 v2.23) verify that every qualifying string in the Prose body carries the `***text***` marker. A missing bold-italic on a Named Move or qualifying cultivation level designation is a **Gate 1 FAIL** — it blocks `[CONFIRM WRITE]`. This rule is jointly governed with Part 2 Area 3 Rules 3.2.1 and 3.2.1a and Part 6 Principle P6-2. All three must be simultaneously satisfied.

**Rule 29.2.1.2 — Embedded Mandate:** Dialogue is embedded within prose paragraphs. A spoken line never stands isolated. Before, within, or after every exchange, the paragraph contains: the physical state of the speaker (posture, breath, the way their hands sit, the micro-expression they suppress), the environmental response to the speech (how the air in the room shifts, what the light reveals, how other characters' bodies register the words), and the interior experience of the speaker or listener (what the words cost, what they reveal, what they are meant to conceal). The speech act is inseparable from its full experiential context.

**Rule 29.2.1.3 — Multiple Exchanges Within One Paragraph:** A single prose paragraph may contain multiple lines of dialogue from multiple speakers when those exchanges are rapid, overlapping in intent, or part of a rhythmically compressed sequence. Multiple-exchange paragraphs are governed by the requirement that each exchange is still embedded in sufficient physical and psychological context that the reader can track who is speaking, from what state, and to what effect. Compression of exchange does not permit compression of depth.

**Rule 29.2.1.4 — No Script Format:** Dialogue attribution is handled entirely through prose convention — dialogue tags, action beats, and contextual description. Character names followed by colons, numbered exchanges, bracketed stage directions, and any other form of script-format dialogue are prohibited. Every attribution of speech is a prose act.

**Rule 29.2.1.5 — Dialogue Tags Must Earn Their Place:** The standard attribution — "she said," "he replied" — is valid and should not be avoided out of a misguided search for variety. More specific attributions — "she demanded," "he said, though his voice made it a question" — are valid when they carry specific meaning. Attributions that do the work of the prose — that describe tone, physical state, and relational posture in the attribution itself — are preferred over generic tags surrounded by separate description. Attributions should never be so elaborate that they overwhelm the spoken line itself.

### 2.2 — Structural Placement Law

**Rule 29.2.2.1 — Conversation Frequency in Multi-Character Scenes:** In any scene involving two or more characters who are in proximity and capable of speech, dialogue must occur with sufficient frequency that no extended stretch of prose narration passes without the spoken voices of the present characters. The length of "extended stretch" is contextual — a combat scene has different dialogue rhythm than a diplomatic negotiation — but the principle is constant: characters who are present are speaking, unless silence is itself the narrative event.

**Rule 29.2.2.2 — Silence as Deliberate Choice:** Silence in a scene where speech would be expected is a narrative act of equal weight to speech. When a character chooses not to speak, refuses to answer, or finds that no words are available, that silence must be rendered with the same depth as speech — the physical sensation of the silence, what it communicates, how the other characters read and misread it, and what it costs the character who is not speaking.

**Rule 29.2.2.3 — Conversation Across Structural Boundaries:** Conversations that begin within one Area of a scene may carry into the next Area when narrative continuity requires it. The emotional state established by a conversation in Area 1 carries into Area 2. The unresolved tension of a conversation cannot be cancelled by a structural transition. The dialogue's consequence is as persistent as any other consequence.

---

## Cross-References
| Related Skill | Relation | Source |
|---|---|---|
| ssc-character-p20-nature-ideology | SOFT | Part 34 Area 5: Dialogue may constitute IE events triggering Part 20 audit |
| ssc-character-p20-ideology-taxonomy | SOFT | Part 34 Area 5: Dialogue may constitute IE events triggering Part 20 audit |
| ssc-character-p20-ideology-ledger | SOFT | Part 34 Area 5: Dialogue may constitute IE events triggering Part 20 audit |
| ssc-character-p20-ideological-governance-context | SOFT | Part 34 Area 5: Dialogue may constitute IE events triggering Part 20 audit |
| ssc-character-p20-specific-ideology-dynamics | SOFT | Part 34 Area 5: Dialogue may constitute IE events triggering Part 20 audit |
| ssc-character-p20-cultivation-specific-ideology-dynamics | SOFT | Part 34 Area 5: Dialogue may constitute IE events triggering Part 20 audit |
| ssc-character-p20-technology-specific-ideology-dynamics | SOFT | Part 34 Area 5: Dialogue may constitute IE events triggering Part 20 audit |
| ssc-character-p20-ideological-states-transitions | SOFT | Part 34 Area 5: Dialogue may constitute IE events triggering Part 20 audit |
| ssc-character-p20-ideology-interpersonal-dynamics | SOFT | Part 34 Area 5: Dialogue may constitute IE events triggering Part 20 audit |
| ssc-character-p20-ideological-alignment-all-other-parts | SOFT | Part 34 Area 5: Dialogue may constitute IE events triggering Part 20 audit |

## Governing Authority
Subordinate to the shared Part 1 (audit law) + Part 34 (knowledge graph) grounding in `.claude/guardrails/_index.md`. Conflicts are never resolved silently — escalate via `/run-canon-audit`.

## Source Provenance
Part 29, Area 2 — "Dialogue Formatting and Structural Standards" · canon v4.33 · migrated 2026-08-03
