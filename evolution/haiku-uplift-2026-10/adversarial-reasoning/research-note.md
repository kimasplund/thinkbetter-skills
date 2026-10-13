# Research note: adversarial-reasoning (Haiku uplift)

- Haiku with the skill vs Sonnet alone: **DOES NOT REACH**
- Haiku with the skill vs Haiku alone: **NOT VALIDATED**
- Sonnet with the skill vs Sonnet alone: **INCONCLUSIVE**
- Agreement 0.994, freeze OK, extended False
- hs: value 5.21, keys 0.75, ceremony 1.0, leaks 0.33, length x0.88 of sn
- hn: value 4.88, keys 0.792, ceremony 0.17, leaks 0.0, length x0.74 of sn
- ss: value 6.27, keys 0.875, ceremony 0.0, leaks 0.0, length x1.23 of sn
- sn: value 5.85, keys 0.875, ceremony 0.17, leaks 0.0, length x1.0 of sn
- Ruling: an INCONCLUSIVE uplift comparison is reported as such, without an extension. Reason: owner ruling: only the two skills with an open primary question (Haiku+skill vs Sonnet alone) were extended; this uplift comparison stays INCONCLUSIVE (see LEDGER)

## Autopsy

- **Haiku with the skill vs Sonnet alone: DOES NOT REACH.** Value -0.64, keys -0.12, rankings 1–5. Failing conditions: guard_judge_G2, guard_audit_ceremony, guard_audit_leaks. NOISE: value, keys.
- **What the skill does for each model:** Haiku +0.33 on value (NOT VALIDATED); Sonnet +0.42 (INCONCLUSIVE). Length: Haiku with the skill at 0.88× and Sonnet with the skill at 1.23× Sonnet alone.
- **Sources:** the pack and the Sonnet-alone replies come from `evolution/gauntlet-2026-10/adversarial-reasoning`; Sonnet with the skill is reused from the same round (see `reuse.json`).
