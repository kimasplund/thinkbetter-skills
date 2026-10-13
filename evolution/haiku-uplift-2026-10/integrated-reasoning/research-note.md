# Research note: integrated-reasoning (Haiku uplift)

- Haiku with the skill vs Sonnet alone: **DOES NOT REACH**
- Haiku with the skill vs Haiku alone: **NOT VALIDATED**
- Sonnet with the skill vs Sonnet alone: **NOT VALIDATED**
- Agreement 0.985, freeze OK, extended True
- hs: value 4.89, keys 0.656, ceremony 0.25, leaks 0.0, length x0.74 of sn
- hn: value 4.57, keys 0.708, ceremony 0.67, leaks 0.0, length x0.81 of sn
- ss: value 6.32, keys 0.979, ceremony 0.25, leaks 0.25, length x1.05 of sn
- sn: value 5.96, keys 0.969, ceremony 0.33, leaks 0.0, length x1.0 of sn

## Autopsy

- **Haiku with the skill vs Sonnet alone: DOES NOT REACH.** Value -1.07, keys -0.31, rankings 0–6. Failing conditions: value, ranking. NOISE: guard_judge_G3, keys.
- **What the skill does for each model:** Haiku +0.32 on value (NOT VALIDATED); Sonnet +0.36 (NOT VALIDATED). Length: Haiku with the skill at 0.74× and Sonnet with the skill at 1.05× Sonnet alone.
- **Sources:** the pack and the Sonnet-alone replies come from `evolution/gauntlet-2026-10/integrated-reasoning`; Sonnet with the skill is freshly run on the current text (see `reuse.json`).
