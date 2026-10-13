# Ledger: 2026-10 second cherry-pick round (r3)

This program re-tests the Cogito review mode for self-reflecting-chain after round 6 of the r2 program (`evolution/gauntlet-2026-10-r2/`) reverted it. The candidate is on branch `cogito-cherrypick-2`.
`new` is the candidate at the branch HEAD, `old` is the shipped text at tag `v1.2.1`, and `none` means no skill.
The harness is a byte-identical copy of the r2 harness; only `skills.json` differs, holding one row. The gates are therefore the October gates with Amendment 3, and this round runs under Amendment 5: see the spec and `harness/PREREG-TEMPLATE.md`.
A 3-arm round keeps the candidate unless the rewrite gate says REVERT.

| # | skill | state | validation | rewrite | commit | subagent tokens |
|---|---|---|---|---|---|---|
| 1 | self-reflecting-chain | pending | | | | |

## Amendments and rulings
- **Amendment 5 (owner decision, before this round ran):** after round 6 reverted the review mode, the owner approved a second attempt that keeps the checks and drops the delivery template. Round 6 failed on ceremony: executors turned the Deliver line ("the corrected answer first; then each issue that changed the conclusion...") into headings. Judges also flagged a rewritten draft and a change list that repeated each other, and "below is X, then Y" signposting. The candidate now describes what the reply must contain, not its layout, and does three things. It bans headings that describe the review itself. It asks for a rewritten draft or a list of fixes, not both. It adds one backstage check of the reply's own consistency. Fresh briefs are written, and the designer is told to avoid every earlier pack, round 6's included.
