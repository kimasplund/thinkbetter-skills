# Research note: skill-gauntlet (Haiku uplift)

- Haiku with the skill vs Sonnet alone: **DOES NOT REACH**
- Haiku with the skill vs Haiku alone: **INCONCLUSIVE**
- Sonnet with the skill vs Sonnet alone: **INCONCLUSIVE**
- Agreement 0.994, freeze OK, extended False
- hs: value 4.98, keys 0.75, ceremony 0.0, leaks 0.0, length x0.66 of sn
- hn: value 4.62, keys 0.667, ceremony 0.17, leaks 0.0, length x0.72 of sn
- ss: value 6.17, keys 0.979, ceremony 0.33, leaks 0.0, length x1.11 of sn
- sn: value 5.96, keys 0.75, ceremony 0.17, leaks 0.0, length x1.0 of sn
- Ruling: an INCONCLUSIVE uplift comparison is reported as such, without an extension. Reason: owner ruling: only the two skills with an open primary question (Haiku+skill vs Sonnet alone) were extended; this uplift comparison stays INCONCLUSIVE (see LEDGER)

## Autopsy

- **Haiku with the skill vs Sonnet alone: DOES NOT REACH.** Value -0.98, keys +0.00, rankings 0–6. Failing conditions: value, ranking. NOISE: guard_judge_G2, guard_judge_G3.
- **What the skill does for each model:** Haiku +0.36 on value (INCONCLUSIVE); Sonnet +0.21 (INCONCLUSIVE). Length: Haiku with the skill at 0.66× and Sonnet with the skill at 1.11× Sonnet alone.
- **Sources:** the pack and the Sonnet-alone replies come from `evolution/gauntlet-2026-10/skill-gauntlet`; Sonnet with the skill is reused from the same round (see `reuse.json`).
