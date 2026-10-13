# Research note: analogical-transfer (Haiku uplift)

- Haiku with the skill vs Sonnet alone: **DOES NOT REACH**
- Haiku with the skill vs Haiku alone: **NOT VALIDATED**
- Sonnet with the skill vs Sonnet alone: **INCONCLUSIVE**
- Agreement 1.0, freeze OK, extended False
- hs: value 4.44, keys 0.604, ceremony 0.67, leaks 0.0, length x0.69 of sn
- hn: value 4.94, keys 0.771, ceremony 0.83, leaks 0.0, length x0.76 of sn
- ss: value 6.46, keys 0.917, ceremony 0.33, leaks 0.0, length x1.24 of sn
- sn: value 5.96, keys 0.958, ceremony 0.5, leaks 0.0, length x1.0 of sn
- Ruling: an INCONCLUSIVE uplift comparison is reported as such, without an extension. Reason: owner ruling: only the two skills with an open primary question (Haiku+skill vs Sonnet alone) were extended; this uplift comparison stays INCONCLUSIVE (see LEDGER)

## Autopsy

- **Haiku with the skill vs Sonnet alone: DOES NOT REACH.** Value -1.52, keys -0.35, rankings 0–6. Failing conditions: keys, ranking. NOISE: guard_judge_G3, value.
- **What the skill does for each model:** Haiku -0.50 on value (NOT VALIDATED); Sonnet +0.50 (INCONCLUSIVE). Length: Haiku with the skill at 0.69× and Sonnet with the skill at 1.24× Sonnet alone.
- **Sources:** the pack and the Sonnet-alone replies come from `evolution/gauntlet-2026-10-r2/analogical-transfer`; Sonnet with the skill is reused from the same round (see `reuse.json`).
