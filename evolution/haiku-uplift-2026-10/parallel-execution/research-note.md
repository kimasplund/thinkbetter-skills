# Research note: parallel-execution (Haiku uplift)

- Haiku with the skill vs Sonnet alone: **DOES NOT REACH**
- Haiku with the skill vs Haiku alone: **NOT VALIDATED**
- Sonnet with the skill vs Sonnet alone: **INCONCLUSIVE**
- Agreement 0.964, freeze OK, extended False
- hs: value 4.69, keys 0.75, ceremony 0.0, leaks 0.0, length x0.63 of sn
- hn: value 4.48, keys 0.771, ceremony 0.33, leaks 0.0, length x0.61 of sn
- ss: value 6.15, keys 0.938, ceremony 0.0, leaks 0.0, length x0.92 of sn
- sn: value 6.06, keys 0.979, ceremony 0.33, leaks 0.0, length x1.0 of sn
- Ruling: an INCONCLUSIVE uplift comparison is reported as such, without an extension. Reason: owner ruling: only the two skills with an open primary question (Haiku+skill vs Sonnet alone) were extended; this uplift comparison stays INCONCLUSIVE (see LEDGER)

## Autopsy

- **Haiku with the skill vs Sonnet alone: DOES NOT REACH.** Value -1.37, keys -0.23, rankings 0–6. Failing conditions: value, keys, ranking. NOISE: guard_judge_G2, guard_judge_G3.
- **What the skill does for each model:** Haiku +0.21 on value (NOT VALIDATED); Sonnet +0.09 (INCONCLUSIVE). Length: Haiku with the skill at 0.63× and Sonnet with the skill at 0.92× Sonnet alone.
- **Sources:** the pack and the Sonnet-alone replies come from `evolution/gauntlet-2026-10/parallel-execution`; Sonnet with the skill is reused from the same round (see `reuse.json`).
