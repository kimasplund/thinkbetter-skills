# Research note: premortem-evolved (Haiku uplift)

- Haiku with the skill vs Sonnet alone: **DOES NOT REACH**
- Haiku with the skill vs Haiku alone: **NOT VALIDATED**
- Sonnet with the skill vs Sonnet alone: **NOT VALIDATED**
- Agreement 0.952, freeze OK, extended False
- hs: value 4.83, keys 0.896, ceremony 7.67, leaks 5.17, length x3.36 of sn
- hn: value 4.75, keys 0.812, ceremony 0.67, leaks 0.0, length x0.8 of sn
- ss: value 6.15, keys 0.958, ceremony 9.0, leaks 5.67, length x4.51 of sn
- sn: value 5.77, keys 0.917, ceremony 0.33, leaks 0.0, length x1.0 of sn

## Autopsy

- **Haiku with the skill vs Sonnet alone: DOES NOT REACH.** Value -0.94, keys -0.02, rankings 0–6. Failing conditions: guard_judge_G1, guard_judge_G2, guard_audit_ceremony, guard_audit_leaks, guard_audit_length, value, ranking. NOISE: guard_judge_G3.
- **What the skill does for each model:** Haiku +0.08 on value (NOT VALIDATED); Sonnet +0.38 (NOT VALIDATED). Length: Haiku with the skill at 3.36× and Sonnet with the skill at 4.51× Sonnet alone.
- **Sources:** the pack and the Sonnet-alone replies come from `evolution/gauntlet-2026-10/premortem-evolved`; Sonnet with the skill is reused from the same round (see `reuse.json`).
