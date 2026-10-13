# Ledger: 2026-10 follow-up gauntlet (r2)

Candidate edits from the post-hoc review (`evolution/gauntlet-2026-10/_followup/`) are tested on branch `gauntlet-r2`.
`new` is the candidate at the branch HEAD, `old` is the shipped text at tag `v1.2.0`, and `none` means no skill.
The gates are the October gates with Amendment 3: see the spec and `harness/PREREG-TEMPLATE.md`.
A 2-arm round adopts the candidate only if it is VALIDATED; a 3-arm round keeps it unless the rewrite gate says REVERT.

| # | skill | state | validation | rewrite | commit | subagent tokens |
|---|---|---|---|---|---|---|
| 1 | tree-of-thoughts | applied | NOT VALIDATED | - |  | ~0.75M |
| 2 | adversarial-reasoning | applied | NOT VALIDATED | - |  | ~0.83M |
| 3 | analogical-transfer | applied | NOT VALIDATED | REVERT |  | ~1.03M |
| 4 | negotiated-decision-framework | applied | NOT VALIDATED | REVERT |  | ~2.23M (extended) |
| 5 | rapid-triage-reasoning | applied | NOT VALIDATED | REVERT |  | ~1.89M (extended) |
| 6 | self-reflecting-chain | applied | NOT VALIDATED | REVERT |  | ~1.68M (extended) |

## Amendments and rulings
- **Amendment 4 (owner decision, before round 6 ran):** a sixth round under the same Amendment 3 gates tests a review mode for self-reflecting-chain, cherry-picked from the old Cogito server (see `docs/audits/2026-10-13-cogito-feature-audit.md`). It adds up to three critique-and-revise passes on a finished draft, plus backstage reasoning checks: circular reasoning, named biases, contradictions, drift from the question, a counterfactual probe and unsupported leaps. new = branch `cogito-cherrypick` HEAD, old = tag `v1.2.1`. The briefs are user drafts with planted flaws, and the rewrite gate keeps the edit unless it is worse than the shipped text.
- **Round 6 audit check (after scoring, before apply):** the REVERT comes from the ceremony audit: 5 hits for the edit, 2 for the shipped text, against a tolerance of one extra hit. All 5 of the edit's hits are the same heading, "Issues that changed (or change) the conclusion", which executors lifted from the review mode's Deliver line. The quotes are real and correctly attributed, so the verdict stands. For the record, the edit raised the planted-flaw key rate (0.99 vs 0.91 for the shipped text and 0.94 for no skill), and its value gain over the shipped text (+0.23) was within the band (0.50). G2, machinery leakage, also fell on two of three briefs. A future attempt would need the review mode without a delivery template that executors can turn into headings.
