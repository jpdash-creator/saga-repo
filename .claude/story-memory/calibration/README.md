# Calibration Passages

**What this folder is.** A small set of short, deliberately faulty passages used to test the
checker (the Continuity Checker's own detection), not the story. There is one passage for each
Cardinal Sin of Part 36 Area 2.2 and each Vitality Sin of Part 36 Area 17.2.

**What a passage is not.** Every passage is invented test material. It is not Starward Saga
prose, it establishes nothing in the story, and no agent may cite it as canon, treat it as a
source of any fact, enter anything from it in a ledger, or read it as an Area.
Nothing here is ever written under `projects/`. This is not a ledger folder, and no ledger
command reads it.

**How a passage is laid out.** The file opens with a header that says it is test material,
names the sin under test, names the check and dimension the checker must name, and gives the
position to assume (for example, an Area that closes its scene). The passage text follows the
header. It is written in house style (no em-dashes, no contractions anywhere, narration or dialogue, Canon Amendment 2026-10-16; dialogue as `*"..."*`)
so that the one named fault is the thing the checker has to find. Files are named
`cal-cs<n>-<slug>.md` for Cardinal Sin n and `cal-vs<n>-<slug>.md` for Vitality Sin n.

**Who runs them and when.** `/run-canon-audit` runs the checker over every passage in this
folder after a change to an agent file (`.claude/agents/`) or to Part 28, 29, 36 or 39 (the
calibration check in that command). The checker reads only the passage and the Part its header
names, runs only the check the header names, and reports whether it named the sin.

**What counts as caught.** The checker names the sin on the dimension the header names: as a
FAIL where that dimension can FAIL, and as a finding reported for the author's ruling where the
dimension is advisory (Part 36 Area 2.2 and the guidance-post clause of Parts 29 and 36). A
passage whose sin the checker does not name is MISSED. A MISSED passage means the checker no
longer sees that fault. It is reported to the author for a decision, and no agent edits an
agent file, a Part or a passage to make it pass.

**Who owns the set.** The author approves each passage before it is placed here and adds,
changes or removes passages. Only passages the author has approved are kept in this folder.
