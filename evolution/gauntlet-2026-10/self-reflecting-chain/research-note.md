# Research note: self-reflecting-chain

- Validation (new vs none): **NOT VALIDATED**; rewrite (new vs old): **REVERT**
- Agreement 0.992, freeze OK, extended True
- new: value 5.79, keys 1.0, ceremony 0.58, leaks 0.0, length x1.06, negative ok, framing True
- old: value 5.76, keys 1.0, ceremony 0.5, leaks 0.0, length x1.04, negative ok, framing True
- none: value 5.62, keys 0.99, ceremony 0.5, leaks 0.0, length x1.0, negative ok, framing None

## Autopsy

- **What drove the verdict:** after 2 runs both gates were INCONCLUSIVE. After the pre-registered extension, validation is NOT VALIDATED on value: +0.17, decisively short of +0.5 (band 0.19), even though the skill won rankings 5–1. Keys were at the ceiling in all arms (0.99 to 1.00).
- **Rewrite: REVERT.** The rewrite is level with v1.0.0 (value +0.03, keys equal, G3 slightly better). The verdict turns on a ceremony count of 7 vs 6 hits across 12 replies. With one-hit tolerance it would still be REVERT, because a G2 NOISE after the extension finalises conservatively.
- **Instrument note:** the auditor found ceremony in about half of all replies in every arm (0.50 to 0.58 per reply), including no skill. Ceremony hits are therefore not specific to the skill on this task family.
- **Consequence:** the body reverts mechanically to v1.0.0 and keeps the modernised frontmatter.
