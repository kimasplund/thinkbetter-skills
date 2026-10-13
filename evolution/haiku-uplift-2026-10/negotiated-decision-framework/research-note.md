# Research note: negotiated-decision-framework (Haiku uplift)

- Haiku with the skill vs Sonnet alone: **DOES NOT REACH**
- Haiku with the skill vs Haiku alone: **INCONCLUSIVE**
- Sonnet with the skill vs Sonnet alone: **INCONCLUSIVE**
- Agreement 0.982, freeze OK, extended False
- hs: value 4.67, keys 0.729, ceremony 0.33, leaks 0.0, length x0.71 of sn
- hn: value 4.6, keys 0.625, ceremony 0.17, leaks 0.0, length x0.69 of sn
- ss: value 6.19, keys 0.896, ceremony 0.5, leaks 0.0, length x1.19 of sn
- sn: value 5.92, keys 0.979, ceremony 0.5, leaks 0.0, length x1.0 of sn
- Ruling: an INCONCLUSIVE uplift comparison is reported as such, without an extension. Reason: owner ruling: only the two skills with an open primary question (Haiku+skill vs Sonnet alone) were extended; this uplift comparison stays INCONCLUSIVE (see LEDGER)

## Autopsy

- **Haiku with the skill vs Sonnet alone: DOES NOT REACH.** Value -1.25, keys -0.25, rankings 0–6. Failing conditions: value, keys, ranking. NOISE: guard_judge_G2, guard_judge_G3.
- **What the skill does for each model:** Haiku +0.07 on value (INCONCLUSIVE); Sonnet +0.27 (INCONCLUSIVE). Length: Haiku with the skill at 0.71× and Sonnet with the skill at 1.19× Sonnet alone.
- **Sources:** the pack and the Sonnet-alone replies come from `evolution/gauntlet-2026-10-r2/negotiated-decision-framework`; Sonnet with the skill is reused from the same round (see `reuse.json`).
