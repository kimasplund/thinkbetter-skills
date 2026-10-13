# Research note: self-reflecting-chain (Haiku uplift)

- Haiku with the skill vs Sonnet alone: **DOES NOT REACH**
- Haiku with the skill vs Haiku alone: **INCONCLUSIVE**
- Sonnet with the skill vs Sonnet alone: **INCONCLUSIVE**
- Agreement 0.958, freeze OK, extended False
- hs: value 5.02, keys 1.0, ceremony 0.0, leaks 0.0, length x0.71 of sn
- hn: value 5.42, keys 0.958, ceremony 1.0, leaks 0.0, length x0.91 of sn
- ss: value 6.35, keys 1.0, ceremony 0.67, leaks 0.0, length x1.14 of sn
- sn: value 5.83, keys 1.0, ceremony 0.5, leaks 0.0, length x1.0 of sn
- Ruling: an INCONCLUSIVE uplift comparison is reported as such, without an extension. Reason: owner ruling: only the two skills with an open primary question (Haiku+skill vs Sonnet alone) were extended; this uplift comparison stays INCONCLUSIVE (see LEDGER)

## Autopsy

- **Haiku with the skill vs Sonnet alone: DOES NOT REACH.** Value -0.81, keys +0.00, rankings 0–6. Failing conditions: value, ranking. NOISE: guard_judge_G3.
- **What the skill does for each model:** Haiku -0.40 on value (INCONCLUSIVE); Sonnet +0.52 (INCONCLUSIVE). Length: Haiku with the skill at 0.71× and Sonnet with the skill at 1.14× Sonnet alone.
- **Sources:** the pack and the Sonnet-alone replies come from `evolution/gauntlet-2026-10/self-reflecting-chain`; Sonnet with the skill is reused from the same round (see `reuse.json`).
