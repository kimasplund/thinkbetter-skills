# Suite gauntlet ledger, 2026-10

States: pending → designed → frozen → ran → blinded → judged → scored → applied. Resume at the first row that is not `applied`.

| # | skill | state | validation | rewrite | commit | subagent tokens |
|---|---|---|---|---|---|---|
| 1 | hypothesis-elimination | applied | NOT VALIDATED | - |  | 1.15M (+0.61M pilot 1) |
| 2 | reasoning-handover-protocol | applied | NOT VALIDATED | REVERT |  | 0.94M |
| 3 | integrated-reasoning | applied | NOT VALIDATED | REVERT |  | 0.96M |
| 4 | tree-of-thoughts | applied | NOT VALIDATED | REVERT |  | 0.91M |
| 5 | breadth-of-thought | applied | NOT VALIDATED | REVERT |  | 1.07M |
| 6 | self-reflecting-chain | applied | NOT VALIDATED | REVERT |  | 1.66M (extended) |
| 7 | parallel-execution | applied | NOT VALIDATED | REVERT |  | ~2.1M (extended) |
| 8 | premortem-evolved | applied | NOT VALIDATED | REVERT |  | ~2.16M |
| 9 | adversarial-reasoning | applied | NOT VALIDATED | - |  | ~1.53M (extended) |
| 10 | dialectical-reasoning | applied | NOT VALIDATED | - |  | ~1.26M (extended) |
| 11 | analogical-transfer | applied | NOT VALIDATED | - |  | ~0.76M |
| 12 | rapid-triage-reasoning | applied | NOT VALIDATED | - |  | ~0.69M |
| 13 | negotiated-decision-framework | applied | NOT VALIDATED | - |  | ~1.51M (extended) |
| 14 | option-synthesis | applied | NOT VALIDATED | - |  | ~1.30M |
| 15 | skill-gauntlet | applied | NOT VALIDATED | - |  | ~0.59M |

## Amendments

- **Amendment 1:** made before any round. See spec Amendment 1.
- **Amendment 2:** pilot 1 found the harness unfit (keys at the ceiling; plain confidence statements counted as leaks). The designer prompt, leak rule and rubric G2 anchor were fixed before the pilot re-run. The record is in `_pilot-1-unfit-hypothesis-elimination/`, and that pilot used ~0.61M subagent tokens.
- **Owner decision after pilot 2:** the harness is accepted as fit. The literal pilot fitness check failed only because the skill's real effect on Sonnet is small (value +0.30 after the extension), not because the instruments couldn't discriminate. See `hypothesis-elimination/research-note.md`.
- **Ruling (round 5):** removed `context: fork` and `argument-hint` from breadth-of-thought's frontmatter after the mechanical revert. The restored v1.0.0 body has no `$ARGUMENTS` block, so a forked run would start without the problem. This is a frontmatter-only change, and the body remains exactly v1.0.0.

- **Ruling (round 8):** premortem-evolved's mechanical revert restored the v1.0.0 SKILL.md body and `references/`, but `scripts/pre_delivery_check.py` was kept at its 1.1.0 version. Gauntlet workers have no Bash, so the script never ran in any cell and the verdict carries no evidence about it. Its 1.1.0 changes are mechanical bug fixes (whole-word token matching, template-token detection, `-h`, read errors) covered by `tests/test_skill_scripts.py`, and it doesn't depend on the 1.1.0 wording. Cost if wrong: one `git checkout v1.0.0 -- skills/premortem-evolved/scripts/` plus dropping the affected tests.
- **Ruling (round 14):** the auditor failed strict validation three times with the identical prompt. Each time it also reported on the two framing-pair replies (N5G, O2C), on top of every main and negative reply. The prompt asks for "every main and negative code" without forbidding extras, so this is a prompt ambiguity, not corruption. The third output's two framing entries were removed from `reports`, after asserting that the extras were exactly the framing codes and nothing was missing. The unmodified output is kept as `option-synthesis/audit/audit.raw.json`. The scorer reads `reports` only for main replies and takes framing and negative results from their own sections, so no scored value changed. Fix after the program: make the auditor prompt exclude framing codes from `reports`, or make the validator ignore them. Cost if wrong: a fourth identical re-run.
