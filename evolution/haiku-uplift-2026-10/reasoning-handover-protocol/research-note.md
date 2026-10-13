# Research note: reasoning-handover-protocol (Haiku uplift)

- Haiku with the skill vs Sonnet alone: **DOES NOT REACH**
- Haiku with the skill vs Haiku alone: **NOT VALIDATED**
- Sonnet with the skill vs Sonnet alone: **NOT VALIDATED**
- Agreement 0.94, freeze OK, extended False
- hs: value 4.58, keys 0.833, ceremony 0.17, leaks 0.33, length x0.77 of sn
- hn: value 4.67, keys 0.833, ceremony 0.17, leaks 0.0, length x0.74 of sn
- ss: value 6.0, keys 0.979, ceremony 0.17, leaks 0.33, length x0.96 of sn
- sn: value 5.79, keys 0.958, ceremony 0.17, leaks 0.0, length x1.0 of sn

## Autopsy

- **Haiku with the skill vs Sonnet alone: DOES NOT REACH.** Value -1.21, keys -0.12, rankings 1–5. Failing conditions: guard_audit_leaks. NOISE: guard_judge_G2, guard_judge_G3, value, keys.
- **What the skill does for each model:** Haiku -0.09 on value (NOT VALIDATED); Sonnet +0.21 (NOT VALIDATED). Length: Haiku with the skill at 0.77× and Sonnet with the skill at 0.96× Sonnet alone.
- **Sources:** the pack and the Sonnet-alone replies come from `evolution/gauntlet-2026-10/reasoning-handover-protocol`; Sonnet with the skill is reused from the same round (see `reuse.json`).
