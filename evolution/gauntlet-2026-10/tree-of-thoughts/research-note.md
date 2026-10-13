# Research note: tree-of-thoughts

- Validation (new vs none): **NOT VALIDATED**; rewrite (new vs old): **REVERT**
- Agreement 0.992, freeze OK, extended False
- new: value 5.9, keys 0.938, ceremony 0.33, leaks 0.0, length x1.24, negative FAIL, framing True
- old: value 6.25, keys 1.0, ceremony 0.17, leaks 0.0, length x1.21, negative ok, framing True
- none: value 5.19, keys 0.979, ceremony 0.0, leaks 0.0, length x1.0, negative ok, framing None

## Autopsy

- **Rewrite gate: REVERT, and this verdict is robust.** v1.0.0 beat the 1.1.0 rewrite on value (6.25 vs 5.90; margin −0.35, outside the −0.25 non-inferiority limit by more than the 0.06 band) and won every decided ranking (5–0). The 1.1.0 changes made the skill worse on Sonnet.
- **Validation of the 1.1.0 body: NOT VALIDATED.** It did beat no skill on value (+0.71, band 0.12, rankings 5–0). It failed on two hair-trigger conditions: 2 auditor ceremony hits, and a negative-fixture reply of 67 words against a 1.5× limit of 64.5. The ceremony quotes are direct bottom-line sentences, for example "Don't sign the 18 t Alto Merida deal.", so they look like auditor noise rather than real ceremony.
- **The restored v1.0.0 body, reported descriptively and not as a pre-registered gate:** value 6.25 vs 5.19 for no skill (+1.06), keys 1.00 vs 0.98, 1 ceremony hit, negative fixture ok, framing ok. It was the strongest arm in the round.
- **Consequence:** the body reverts mechanically to v1.0.0 and keeps the modernised frontmatter.
