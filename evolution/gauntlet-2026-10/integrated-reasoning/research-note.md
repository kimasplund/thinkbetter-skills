# Research note: integrated-reasoning

- Validation (new vs none): **NOT VALIDATED**; rewrite (new vs old): **REVERT**
- Agreement 1.0, freeze OK, extended False
- new: value 5.46, keys 0.875, ceremony 0.0, leaks 0.17, length x1.06, negative ok, framing True
- old: value 5.77, keys 0.917, ceremony 0.17, leaks 0.0, length x1.1, negative ok, framing True
- none: value 5.46, keys 0.875, ceremony 0.0, leaks 0.0, length x1.0, negative ok, framing None

## Autopsy

- **What drove the verdict:** value tied with no skill (5.46 vs 5.46) and keys were level (0.88 each). Against v1.0.0 the rewrite lost every decided ranking (0 to 4) and trailed on value (−0.31, band 0.44). One auditor leak hit in the new arm, a "Cause | Rough likelihood" rating table, FAILs both gates under the strict pre-registered rule.
- **The other reading (one-hit tolerance):** both gates would be INCONCLUSIVE. The rankings still point against the rewrite.
- **Design vs compliance:** this is design. On Sonnet, routing through the 2.3.0 router added no value over answering directly. The v1.0.0 router's replies ranked better, which suggests the 1.1.0 restructuring (sections moved into references, new thresholds) cost something.
- **Consequence:** the body reverts mechanically to v1.0.0, including its original single-file layout, and keeps the modernised frontmatter.
