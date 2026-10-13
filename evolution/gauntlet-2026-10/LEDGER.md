# Suite gauntlet ledger, 2026-10

States: pending → designed → frozen → ran → blinded → judged → scored → applied. Resume at the first row that is not `applied`.

| # | skill | state | validation | rewrite | commit | subagent tokens |
|---|---|---|---|---|---|---|
| 1 | hypothesis-elimination | applied | NOT VALIDATED | - |  | 1.15M (+0.61M pilot 1) |
| 2 | reasoning-handover-protocol | applied | NOT VALIDATED | REVERT |  | 0.94M |
| 3 | integrated-reasoning | applied | NOT VALIDATED | REVERT |  | 0.96M |
| 4 | tree-of-thoughts | applied | NOT VALIDATED | REVERT |  | 0.91M |
| 5 | breadth-of-thought | pending | | | | |
| 6 | self-reflecting-chain | pending | | | | |
| 7 | parallel-execution | pending | | | | |
| 8 | premortem-evolved | pending | | | | |
| 9 | adversarial-reasoning | pending | | | | |
| 10 | dialectical-reasoning | pending | | | | |
| 11 | analogical-transfer | pending | | | | |
| 12 | rapid-triage-reasoning | pending | | | | |
| 13 | negotiated-decision-framework | pending | | | | |
| 14 | option-synthesis | pending | | | | |
| 15 | skill-gauntlet | pending | | | | |

## Amendments

- **Amendment 1:** made before any round. See spec Amendment 1.
- **Amendment 2:** pilot 1 found the harness unfit (keys at the ceiling; plain confidence statements counted as leaks). The designer prompt, leak rule and rubric G2 anchor were fixed before the pilot re-run. The record is in `_pilot-1-unfit-hypothesis-elimination/`, and that pilot used ~0.61M subagent tokens.
- **Owner decision after pilot 2:** the harness is accepted as fit. The literal pilot fitness check failed only because the skill's real effect on Sonnet is small (value +0.30 after the extension), not because the instruments couldn't discriminate. See `hypothesis-elimination/research-note.md`.
