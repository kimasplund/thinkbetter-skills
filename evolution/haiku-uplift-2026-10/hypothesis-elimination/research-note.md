# Research note: hypothesis-elimination (Haiku uplift)

- Haiku with the skill vs Sonnet alone: **DOES NOT REACH**
- Haiku with the skill vs Haiku alone: **INCONCLUSIVE**
- Sonnet with the skill vs Sonnet alone: **INCONCLUSIVE**
- Agreement 0.929, freeze OK, extended False
- hs: value 5.17, keys 0.958, ceremony 0.0, leaks 0.0, length x0.77 of sn
- hn: value 5.15, keys 0.958, ceremony 0.17, leaks 0.0, length x0.76 of sn
- ss: value 6.23, keys 0.979, ceremony 0.17, leaks 0.0, length x1.07 of sn
- sn: value 6.08, keys 0.958, ceremony 0.33, leaks 0.0, length x1.0 of sn
- Ruling: an INCONCLUSIVE uplift comparison is reported as such, without an extension. Reason: owner ruling: only the two skills with an open primary question (Haiku+skill vs Sonnet alone) were extended; this uplift comparison stays INCONCLUSIVE (see LEDGER)

## Autopsy

- **Haiku with the skill vs Sonnet alone: DOES NOT REACH.** Value -0.91, keys +0.00, rankings 0–6. Failing conditions: ranking. NOISE: guard_judge_G2, guard_judge_G3, value.
- **What the skill does for each model:** Haiku +0.02 on value (INCONCLUSIVE); Sonnet +0.15 (INCONCLUSIVE). Length: Haiku with the skill at 0.77× and Sonnet with the skill at 1.07× Sonnet alone.
- **Sources:** the pack and the Sonnet-alone replies come from `evolution/gauntlet-2026-10/hypothesis-elimination`; Sonnet with the skill is reused from the same round (see `reuse.json`).
