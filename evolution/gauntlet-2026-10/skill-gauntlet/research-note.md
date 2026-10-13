# Research note: skill-gauntlet

- Validation (new vs none): **NOT VALIDATED**
- Agreement 0.976, freeze OK, extended False
- new: value 6.06, keys 0.958, ceremony 0.5, leaks 0.0, length x1.11, negative ok, framing True
- none: value 5.56, keys 0.75, ceremony 0.17, leaks 0.0, length x1.0, negative ok, framing None

## Autopsy

- **What drove the verdict:** the ceremony guard FAILs: 3 hits vs 1 across 6 replies. That fails under the strict rule and under one-hit tolerance alike, so the round is decided without an extension. The flagged lines are gate-by-gate verdict scaffolding ("Verdict by criterion", "What passes and what doesn't, against your own criteria").
- **Value and keys:** the skill won rankings 5–1. Value is +0.50, but brief-3 is −0.12 against +0.81 on the other two, which makes the band 0.94 and value NOISE. Keys are the largest gain in the program: 0.96 vs 0.75 (+0.21, band 0.38). The skill catches evaluation traps a capable reply misses, such as post-hoc rule changes. Most of the gain is V1 insight (+1.00) and V3 soundness (+0.66).
- **Design vs compliance:** the skill's method is a pre-registered conjunctive gate, and replies show it as a per-criterion verdict table. G2 (−0.42) and G3 (−0.41, lower on every brief) are NOISE but lean the wrong way. Calibration is worth a look, because a verdict-by-gate format reads as more certain than the evidence.
- **Not chased:** whether presenting the gate result as prose instead of a criterion table keeps the key gain without the ceremony hits.
