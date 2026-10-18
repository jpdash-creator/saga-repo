# Canon Amendment log: Brackenhold in the Manual Register (2026-10-08)

Not canon; an audit trail.

- Authority: the author's word in chat, 2026-10-08 (Canon Amendment adding Brackenhold to the manual register, the validator edit, and new Brackenhold manuals and moves up to Signature).
- Rule text: Part 42 `SKILL.md` Rules 42.5.2.4 and 42.10.2.6 (new), and one-clause edits to 42.9.3.3, 42.10.2.1, 42.10.2.3, 42.10.2.4, 42.10.3.1, 42.10.4.1, 42.10.6.1, 42.10.6.2, 42.11.1.2, 42.12.3.1 and checks C-3, C-4, C-5, C-11.
- Ledger rows: `MAN-INT-HAL-011`, `MAN-INT-HAL-012`, `MAN-ADV-HAL-014`, `MAN-SIG-HAL-013` (4 manuals), 30 moves, `kingdoms/brackenhold.csv` (13 `BR-` rows). `weapons.csv` unchanged.
- Validator: `.claude/tools/manual_ledger_query.py` (origin list, `BR` ID, brackenhold file, extras-after-Gale origin and count rules, C-5 and C-17 third kingdom, C-19 kingdom value, stats and manual report).
- Defaults taken: one Signature manual waiver, neutral register, institution cells `OPEN-AUTHOR`, no character or kit rows yet.
- Result: `validate` 0 FAIL; `find-name` on the 34 new names returned one exact hit each (itself).
- Still to do: ALCA Mode A reconciliation by the Continuity Checker; the Redhaft Vanguard added to Rule 42.7.2.2 and the C-17 list once ledgered.
