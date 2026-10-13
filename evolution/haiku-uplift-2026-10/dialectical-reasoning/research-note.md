# Research note: dialectical-reasoning (Haiku uplift)

- Haiku with the skill vs Sonnet alone: **DOES NOT REACH**
- Haiku with the skill vs Haiku alone: **NOT VALIDATED**
- Sonnet with the skill vs Sonnet alone: **INCONCLUSIVE**
- Agreement 0.988, freeze OK, extended False
- hs: value 4.56, keys 0.75, ceremony 0.5, leaks 0.0, length x0.89 of sn
- hn: value 4.81, keys 0.75, ceremony 0.5, leaks 0.0, length x0.79 of sn
- ss: value 6.06, keys 0.938, ceremony 0.17, leaks 0.0, length x1.25 of sn
- sn: value 5.83, keys 0.896, ceremony 0.17, leaks 0.0, length x1.0 of sn
- Ruling: an INCONCLUSIVE uplift comparison is reported as such, without an extension. Reason: owner ruling: only the two skills with an open primary question (Haiku+skill vs Sonnet alone) were extended; this uplift comparison stays INCONCLUSIVE (see LEDGER)

## Autopsy

- **Haiku with the skill vs Sonnet alone: DOES NOT REACH.** Value -1.27, keys -0.15, rankings 0–6. Failing conditions: guard_audit_ceremony, ranking. NOISE: guard_judge_G2, guard_judge_G3, value, keys.
- **What the skill does for each model:** Haiku -0.25 on value (NOT VALIDATED); Sonnet +0.23 (INCONCLUSIVE). Length: Haiku with the skill at 0.89× and Sonnet with the skill at 1.25× Sonnet alone.
- **Sources:** the pack and the Sonnet-alone replies come from `evolution/gauntlet-2026-10/dialectical-reasoning`; Sonnet with the skill is reused from the same round (see `reuse.json`).
