# Research note: tree-of-thoughts (Haiku uplift)

- Haiku with the skill vs Sonnet alone: **DOES NOT REACH**
- Haiku with the skill vs Haiku alone: **NOT VALIDATED**
- Sonnet with the skill vs Sonnet alone: **NOT VALIDATED**
- Agreement 0.985, freeze OK, extended True
- hs: value 5.17, keys 0.906, ceremony 0.08, leaks 0.0, length x0.8 of sn
- hn: value 5.05, keys 0.979, ceremony 0.08, leaks 0.0, length x0.9 of sn
- ss: value 6.42, keys 0.979, ceremony 0.33, leaks 0.0, length x1.26 of sn
- sn: value 5.78, keys 1.0, ceremony 0.17, leaks 0.0, length x1.0 of sn

## Autopsy

- **Haiku with the skill vs Sonnet alone: DOES NOT REACH.** Value -0.61, keys -0.09, rankings 0–6. Failing conditions: guard_judge_G3, value, ranking.
- **What the skill does for each model:** Haiku +0.12 on value (NOT VALIDATED); Sonnet +0.64 (NOT VALIDATED). Length: Haiku with the skill at 0.8× and Sonnet with the skill at 1.26× Sonnet alone.
- **Sources:** the pack and the Sonnet-alone replies come from `evolution/gauntlet-2026-10/tree-of-thoughts`; Sonnet with the skill is freshly run on the current text (see `reuse.json`).
