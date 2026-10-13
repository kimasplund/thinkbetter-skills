# Research note: adversarial-reasoning

- Validation (new vs none): **NOT VALIDATED**
- Agreement 0.982, freeze OK, extended True
- new: value 6.09, keys 0.854, ceremony 0.0, leaks 0.0, length x1.16, negative ok, framing True
- none: value 5.38, keys 0.833, ceremony 0.08, leaks 0.0, length x1.0, negative ok, framing None

## Autopsy

- **What drove the verdict:** after 2 runs validation was INCONCLUSIVE only on a G1 NOISE; value and rankings already passed. After the pre-registered extension the skill won all 6 rankings, with a value margin of +0.72. That margin sits inside the paired band (1.06), so value is NOISE and the verdict finalises conservatively as NOT VALIDATED. G2 was also NOISE (6.96 vs 7.00).
- **Why the band is wide:** the skill led on every brief (+0.53, +1.34 and +0.28). The band is the max−min spread of those per-brief gains, so a uniformly positive but uneven gain reads as noise. This is the strongest no-skill comparison in the program so far; the pre-registered rule, not a weak effect, decided it.
- **Design vs compliance:** the gain is mostly V3 soundness (+0.87) and G3 calibration (+0.71). Keys were level (0.85 vs 0.83), so the skill made replies better argued rather than more complete.
- **Not chased:** whether a band rule that tolerates heterogeneous positive gains (for example a one-sided per-brief sign rule) would be the better instrument. That is a harness question for after the program, not a change to make mid-run.
