# Research note: breadth-of-thought

- Validation (new vs none): **NOT VALIDATED**; rewrite (new vs old): **REVERT**
- Agreement 0.992, freeze OK, extended False
- new: value 5.38, keys 0.875, ceremony 0.17, leaks 0.0, length x1.27, negative ok, framing True
- old: value 5.77, keys 0.917, ceremony 0.0, leaks 0.0, length x1.3, negative ok, framing True
- none: value 5.29, keys 0.958, ceremony 0.0, leaks 0.0, length x1.0, negative ok, framing None

## Autopsy

- **What drove the verdict:** the 1.1.0 body was level with no skill on value (+0.08, band 1.31) and slightly behind on keys (0.88 vs 0.96). Against v1.0.0 it trailed on value (−0.40, inside a band of 1.00) and won only 1 of 5 decided rankings. One auditor ceremony hit in the new arm FAILs both gates under the strict pre-registered rule.
- **The other reading (one-hit tolerance):** both gates would be INCONCLUSIVE. The direction agrees with rounds 2 to 4: the v1.0.0 body outperforms its 1.1.0 rewrite.
- **Design vs compliance:** this is design. The 1.1.0 changes (reconciled counts, confidence formula, fork with `$ARGUMENTS`) added no measurable value in body-level testing. The fork itself is not exercised here, because executors read the body directly.
- **Consequence:** the body reverts mechanically to v1.0.0 and keeps the modernised frontmatter, except `context: fork` and `argument-hint`. Those were removed because the restored v1.0.0 body has no `$ARGUMENTS` problem block, so a forked run would start without the problem; that was the original audit defect. The skill now runs inline, like the other patterns. This is a coordinator ruling recorded in the ledger: frontmatter only, and the body is untouched.
