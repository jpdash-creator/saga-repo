---
name: gate1-audit-method
description: Reusable Gate 1 method for the continuity-checker: tool quirks, cheap reading, exact counts with no shell, record recovery, law-moves rule, judgement habits, flow-review recipes
metadata:
  type: reference
---

Chapter-specific findings live in the specs, ledgers and session-log, not here. Re-Grep headings; never trust a remembered line number.

**Tool quirks.**
- `Glob` of skills needs `**/*.md`; Glob truncates at 100 files, so one ledger folder at a time. Use Grep with a negated glob `!**/_archive/**`; `ledger-*/_index.md` and braced subpath globs give false "no matches" (use a basename glob plus `path`). Never Glob or Grep the repo root or `_archive`. A name Grep also hits agent-memory: ignore those hits.
- Read stops near 25K tokens: about 1,100 manifest lines, 220-270 SKILL lines, 70-100 Chapter Spec lines. Grep omits long lines: use `-o` with a window under about 420 characters, or Read with offset N and limit 1. Count mode counts lines, not matches; tally with `-o -n`. Keep parallel batches to 4 queries.
- A Write needs a prior Read of the file, even one made earlier in the session (Read with limit 12 is enough).

**Reading cheaply.** `skill-index.json`: Grep `"title": "<Area>"` with -B1 -A2; the Part-to-title map is `^  "(part|title)":`. For a Tier A/B person read from `### 11.2` to the end (about 16K) and fetch Section 1 voice or Section 7 address by Grep when the text uses it; Valia's and Varys's Section 1 hold the Check #21 flags. Read the Chapter Spec's Audit and Settlement Notes first; they name every guard. Write any report from the written text (read the whole .md once, Grep every line reference), never from a summary.

**Exact counts, no shell.** Whole file: multiline count mode `\A\S+(?:\s+\S+){N-1}`, probe N and N+1 (the `(?:\s*\S+){N}` form always matches, it is wrong). Area block: `<!-- AREA NN -->(?:\s+[^<\s]\S*){N}` (ripgrep has no look-around), bisect with parallel probes. Subtract date line 6, `---` 1, `* * *` 3. Reconcile with the script `measure`, report both, state the method.

**Recovering a record.** The maker's hand-off, my earlier report and the author's answers sit in the session `.jsonl`, `subagents/agent-<id>.jsonl` or `tasks/<id>.output`: count-mode Grep on each file for a unique token (or `"name":"SubagentHandback"`), then Read that line with limit 1 (never the tail; signatures are huge), or Grep `-o` with a window of 430 characters or less. Copy Tier D codes character for character. A relayed ruling is cited as relayed; look first for it on disk in the spec's Audit and Settlement Notes. My own reports can disagree across runs: state the conflict, do not choose.

**The ground moves.** A staged draft can be edited mid-audit (re-read and recount at the end); the law can change while you work or after a gap (Grep the current date and new check tokens such as `Part 44|Check #23|23-check` over guardrails, skills, agents and manifest; count mode, then `-o`). The agent definition runs ahead of the prompt. A re-audit of a revised draft is a new Gate 1 (re-read the manifest), logged in a second file. With two files side by side (edited and drafter copy) audit the edited one and diff by eye.

**Judgement habits.**
- 20-9 (Rule 39.40.2.5): Grep `usually|always|every day|any ground|as (he|she) (took|gave|read|counted|stood)|drilled`; the act stays, the narrator clause goes. A POV character's reading of another person is lawful.
- A quoted line from a role-only person FAILs Check #17(a) and 20-1: recommend the named version plus a Tier D code (naming is never a cost). Scan candidate names against story-memory, projects and skills.
- Name echo: compare stems and shapes (Rule 20.3 steps 1, 5, 6) against the side index, written Chapters AND each other and the seam neighbours. Retired names in `_rename-map` or `names.json` are not collisions.
- A name added at the Gate 1 fix loop (for 17(a) or an address ruling) opens Check #8 element 8-V: a new named person needs a level shown (Rule 29.12.1.3), and the loop may not have re-run that check; re-check every fix-loop name for a level and for collisions (Chapter 003 gives its runner a level string). Tier 1 stage designations take the form `***Mortal Tier 1 Skin Stage***` (Rule 29.2.1.1d(2)), so `Blood Stage` is correct.
- A gloss moved from first to later use leaves the first use bare (22-8); an inserted appositive can rebind `whose`. 22-9 hits only a word set up as a term and then reused. Canon words in no written Chapter are first uses (Grep the written Chapters).
- Check #21: a flagged item fires once at the character's first Area, even if untested; a "SILENT" report must still restate the flag line. Heroes and Tier A go to the author; Tier B, C, D the checker decides with reasons. For Tier D, elements 20-4, 5, 6, 7 and 10 do not apply.
- A planned callback is not sameness; a one-clause dip into another mind is a Check #9 note, not a 16-J FAIL. Spec claims about ledger facts get a Grep before reliance. Check #23: compare with the Engagement Ledger's order of exchanges and price lines; Grep `steps?|gap|percent|times as` for 23-7 (a physical gap between wagons is not arithmetic).

**Flow instance (second Gate 1 instance).** Phase A grounds, hands back "ready" and asks main to SendMessage the staged text (no wait tool; ending in plain text draws the handback-send-enforce nudge); never write a verdict table before the text exists. Read 2 Grep recipes: split speech `,"\* [^*]{2,70},? \*"`; similes `\b(as|like|than) (a|an|someone|at a) `; negated tails `did not (look|turn|move|answer)`, `Behind (him|her|them)`; paragraph openers `^[A-Za-z*<-]+`; clipped closers `, (and )?[^,."*]{4,34}\."\*`; level strings `\*\*\*(Senior|Warrior|Ruler|Champion)[^*]*\*\*\*`. Check #19-1 count: list paragraphs, drop purely spoken ones, classify each last sentence by the N28-15 test, exempt scene-final. Seams: a fight told in three views may overlap lawfully; judge against the Scene Map join state; a `* * *` skip needs a first sentence that states the new moment. The item (l) search reads the on-disk earlier Chapters. Quick re-check after fixes: re-read the whole file, quote each fixed line, Grep stale names, contractions and dashes (`n't|'ll|'re|'ve|—|–`), test replacement names pairwise. Check dates by the Part 41 formula (month lengths matter).
