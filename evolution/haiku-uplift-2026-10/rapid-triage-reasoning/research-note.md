# Research note: rapid-triage-reasoning (Haiku uplift)

- Haiku with the skill vs Sonnet alone: **DOES NOT REACH**
- Haiku with the skill vs Haiku alone: **INCONCLUSIVE**
- Sonnet with the skill vs Sonnet alone: **INCONCLUSIVE**
- Agreement 0.976, freeze OK, extended False
- hs: value 4.88, keys 0.854, ceremony 0.17, leaks 0.0, length x0.71 of sn
- hn: value 5.02, keys 0.854, ceremony 0.17, leaks 0.0, length x0.68 of sn
- ss: value 6.06, keys 0.938, ceremony 0.0, leaks 0.0, length x0.97 of sn
- sn: value 6.1, keys 0.938, ceremony 0.5, leaks 0.0, length x1.0 of sn
- Ruling: an INCONCLUSIVE uplift comparison is reported as such, without an extension. Reason: owner ruling: only the two skills with an open primary question (Haiku+skill vs Sonnet alone) were extended; this uplift comparison stays INCONCLUSIVE (see LEDGER)

## Autopsy

- **Haiku with the skill vs Sonnet alone: DOES NOT REACH.** Value -1.22, keys -0.08, rankings 0–6. Failing conditions: value, ranking. NOISE: guard_judge_G2, guard_judge_G3.
- **What the skill does for each model:** Haiku -0.14 on value (INCONCLUSIVE); Sonnet -0.04 (INCONCLUSIVE). Length: Haiku with the skill at 0.71× and Sonnet with the skill at 0.97× Sonnet alone.
- **Sources:** the pack and the Sonnet-alone replies come from `evolution/gauntlet-2026-10-r2/rapid-triage-reasoning`; Sonnet with the skill is reused from the same round (see `reuse.json`).
