---
name: ccia-amendment-propagation
description: Recipe for the CCIA reconciliation after a Canon Amendment or a ruling that removes a registered rule: where restatements hide, what to edit, what to leave, manifest handling
metadata:
  type: reference
---

Chapter-specific facts live in the specs, ledgers and session-log. Re-verify against the files.

**Find restatements by wording family, not one phrase.** For a timing or scope rule in Part 30 search `second half`, `late Section N`, `began in`, `begin`, the rule's noun (raid, skirmish) and the Section names, over `.claude` with the glob `!**/{phase-section-part-chapter-area-specs,session-log,ledger-manuals}/**`. Part 30 repeats one rule in its Section Time Allocation Notes, the Section Arc, the Major Narrative Function, the next Section's Phase Positioning, the Arc Summary Table and the Setups table. Part 35 Area 3.5 (Derivation Notes) restates Part 30's Section arcs. Hits like "violate Section 15.1" or "afraid" are noise; read each long omitted line with Read offset N limit 1 or a Grep window under 420 characters.

**Manifest.** The four manifest files hold no rule text; `skill-index.json` holds per-Area `line_count`, so edit skills in place and add no line (headings keep their line numbers). A relationship the Part states but the graph lacks (Part 35 to Part 30) is reported for the author, not added: the skill-index `related` entries would need the matching change.

**Edit minimal, one pointer wording everywhere.** Reuse the orchestrator's amendment wording as a short parenthetical (date and the exception) and let the one Major Narrative Function line hold the detail. Check line endings after: skills may be CRLF (Part 30) or LF (Part 35); ledgers here are LF; `\r` count 0 for LF, `^.*[^\r]$` count 0 for CRLF.

**A ruling that reverses something a written Chapter already says.** Remove or retire the registered rule itself (the code provision, its basis, its page note) and leave one dated ruling note in its place; keep the ledger lines that quote the written page as the page record, each with a short dated ruling note, and say in the report that the written Chapter needs `/revise-chapter`. Before deleting a page note, Grep that its facts stand elsewhere. Bump `Last Updated` in the file and the matching index row dates; add a dated Changelog line; leave old Changelog lines and event rows as history; never edit the session log or the spec folder (list them as left). Cite relayed rulings as relayed after a read-only Grep of the specs shows none on disk.
