# Ledger: 2026-10 follow-up gauntlet (r2)

Candidate edits from the post-hoc review (`evolution/gauntlet-2026-10/_followup/`) are tested on branch `gauntlet-r2`.
`new` is the candidate at the branch HEAD, `old` is the shipped text at tag `v1.2.0`, and `none` means no skill.
The gates are the October gates with Amendment 3: see the spec and `harness/PREREG-TEMPLATE.md`.
A 2-arm round adopts the candidate only if it is VALIDATED; a 3-arm round keeps it unless the rewrite gate says REVERT.

| # | skill | state | validation | rewrite | commit | subagent tokens |
|---|---|---|---|---|---|---|
| 1 | tree-of-thoughts | pending | | | | |
| 2 | adversarial-reasoning | applied | NOT VALIDATED | - |  | ~0.89M |
| 3 | analogical-transfer | applied | NOT VALIDATED | REVERT |  | ~1.03M |
| 4 | negotiated-decision-framework | blinded |  |  |  |  |
| 5 | rapid-triage-reasoning | frozen | INCONCLUSIVE | KEEP |  |  |

## Amendments and rulings

