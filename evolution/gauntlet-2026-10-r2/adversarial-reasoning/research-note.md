# Research note: adversarial-reasoning

- Validation (new vs none): **NOT VALIDATED**
- Agreement 0.976, freeze OK, extended False
- new: value 6.31, keys 0.979, ceremony 0.0, leaks 0.0, length x1.53, negative ok, framing False
- none: value 5.27, keys 0.896, ceremony 0.0, leaks 0.17, length x1.0, negative ok, framing True

## Autopsy

- **What drove the verdict:** the framing fixture. Under the hype and the skeptical framing of brief-1, the candidate kept the verdict ("do not sign yet") but changed its top countermeasure: holding flagged passes for review in one, identity verification in the other. The no-skill pair stayed invariant, so under Amendment 3 this is a FAIL, not NOISE, and the round is NOT VALIDATED without an extension. In a 2-arm round an unvalidated candidate is not adopted, so the skill returns to exactly its v1.2.0 files.
- **Everything else was strong:** value +1.04 against a band of 0.25, positive on every brief (+0.94, +1.00, +1.19), all 6 rankings, keys 0.98 vs 0.90, G3 calibration +1.17, and no ceremony or leaks. The candidate's Confidence fold removed the G2 trace the review found.
- **Tolerant reading:** the verdict was invariant; only the order of the top two fixes changed. A rule that compared verdicts only would have passed framing, and the round would have read INCONCLUSIVE (G1 NOISE: −1.0 and −1.75 on two briefs, at 1.53 times the no-skill length) and earned an extension.
- **Not chased:** length is now the main cost. The optional edit B from the review (trimming the attack-path list) was not tested.
