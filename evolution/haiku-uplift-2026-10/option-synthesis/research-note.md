# Research note: option-synthesis (Haiku uplift)

- Haiku with the skill vs Sonnet alone: **DOES NOT REACH**
- Haiku with the skill vs Haiku alone: **NOT VALIDATED**
- Sonnet with the skill vs Sonnet alone: **NOT VALIDATED**
- Agreement 0.929, freeze OK, extended False
- hs: value 5.0, keys 0.854, ceremony 2.5, leaks 0.17, length x0.91 of sn
- hn: value 4.25, keys 0.833, ceremony 0.0, leaks 0.0, length x0.75 of sn
- ss: value 5.75, keys 0.875, ceremony 9.17, leaks 2.17, length x4.07 of sn
- sn: value 5.17, keys 0.854, ceremony 0.0, leaks 0.0, length x1.0 of sn

## Autopsy

- **Haiku with the skill vs Sonnet alone: DOES NOT REACH.** Value -0.17, keys +0.00, rankings 0–4. Failing conditions: guard_audit_ceremony, ranking. NOISE: guard_judge_G2.
- **What the skill does for each model:** Haiku +0.75 on value (NOT VALIDATED); Sonnet +0.58 (NOT VALIDATED). Length: Haiku with the skill at 0.91× and Sonnet with the skill at 4.07× Sonnet alone.
- **Sources:** the pack and the Sonnet-alone replies come from `evolution/gauntlet-2026-10/option-synthesis`; Sonnet with the skill is reused from the same round (see `reuse.json`).
