# Research note: analogical-transfer

- Validation (new vs none): **NOT VALIDATED**
- Agreement 0.988, freeze OK, extended False
- new: value 6.0, keys 1.0, ceremony 0.67, leaks 0.0, length x1.16, negative ok, framing True
- none: value 5.33, keys 0.938, ceremony 0.0, leaks 0.0, length x1.0, negative ok, framing None

## Autopsy

- **What drove the verdict:** the guards, not the value. The auditor found 4 ceremony hits across 6 replies against 0 for no skill, so that guard FAILs under the strict rule and under one-hit tolerance alike. G1 also FAILs: −0.25 on every brief. Identical per-brief drops give a band of 0, so even that small, consistent drop is outside it. G2 is NOISE (6.17 vs 6.83).
- **Value is the clearest win in the program so far:** +0.67 against a band of 0.19, positive on every brief (+0.69, +0.56, +0.75). The skill won all 6 rankings, and keys reached the ceiling (1.00 vs 0.94). The gain is in V3 soundness (+0.83), V1 and V4 (+0.75 each) and G3 calibration (+0.58).
- **Design vs compliance:** the skill improves the thinking but shows its working. The flagged lines are the method's own steps as reply sections: an abstraction step ("What the problem is, stripped of theatre") and an analogy check ("Is a fire-style firebreak right for ochre wilt?"). This is a compliance problem with a narrow fix: keep the method, hide the machinery. It is the best candidate in the suite for a targeted rewrite and a fresh round.
- **Not chased:** no extension, because the verdict was decided. Whether a no-machinery edit keeps the +0.67 is a new version and its own round.
