# Research note: negotiated-decision-framework

- Validation (new vs none): **NOT VALIDATED**
- Agreement 1.0, freeze OK, extended True
- new: value 5.9, keys 0.958, ceremony 0.25, leaks 0.0, length x1.13, negative ok, framing True
- none: value 5.4, keys 0.896, ceremony 0.17, leaks 0.0, length x1.0, negative ok, framing None

## Autopsy

- **What drove the verdict:** after 2 runs everything was NOISE (value +0.17, rankings 1–2). After the pre-registered extension value PASSes: +0.50 against a band of 0.38, positive on every brief (+0.31, +0.50, +0.69), with rankings 5–1 and keys 0.96 vs 0.90. The ceremony guard FAILs on the strict rule: 3 hits vs 2 across 12 replies, exactly one more. G1 and G2 stay NOISE.
- **Tolerant reading:** under one-hit tolerance ceremony would PASS, but G1 and G2 NOISE after the extension would still finalise conservatively as NOT VALIDATED. The strict rule is not what decided it.
- **Design vs compliance:** the gain is V4 decision usefulness (+0.79) and V2 specificity (+0.58). The skill lands a recommendation that names who commits to what. The open costs are proportionality and machinery: G1 dropped on two briefs and G2 on two, by up to 1.0.
- **Instrument note:** the first auditor run failed strict validation (its reports missed replies) and was re-run with the identical prompt, as the protocol requires.
