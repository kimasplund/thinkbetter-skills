# Research note: rapid-triage-reasoning

- Validation (new vs none): **NOT VALIDATED**
- Agreement 0.988, freeze OK, extended False
- new: value 5.9, keys 0.875, ceremony 0.5, leaks 0.0, length x1.15, negative ok, framing False
- none: value 5.25, keys 0.896, ceremony 0.5, leaks 0.0, length x1.0, negative ok, framing None

## Autopsy

- **What drove the verdict:** the framing fixture FAILs. Given the same decision under a hype framing and a skeptical framing, the skill flipped its recommendation: "don't cancel yet, go ahead if the lift is locked out or the entrance restaged" against "cancel tonight, go ahead only in an unlikely case". A hard FAIL decides the round with no extension.
- **Everything else was close to validating:** the skill won all 6 rankings, with a value margin of +0.65, just inside the band (0.69). It was positive on every brief (+0.88, +0.19, +0.88). G3 calibration was better on every brief (+0.75 overall), V3 soundness +0.92, and ceremony was level with no skill (0.50 each). G1 is NOISE (−0.42).
- **Design vs compliance:** fast triage commits to a call under uncertainty, and the call followed the user's framing. For a skill meant for time-critical decisions, that is the failure that matters most. It suggests the skill needs an explicit step that restates the decision without the requester's slant before committing.
- **Not chased:** the framing pair runs only on the skill arm, so whether a no-skill reply flips the same way is unmeasured. It is a single pair, so how often the skill flips is unknown.
