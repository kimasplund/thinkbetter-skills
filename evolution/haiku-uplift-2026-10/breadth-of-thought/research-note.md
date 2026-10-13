# Research note: breadth-of-thought (Haiku uplift)

- Haiku with the skill vs Sonnet alone: **DOES NOT REACH**
- Haiku with the skill vs Haiku alone: **NOT VALIDATED**
- Sonnet with the skill vs Sonnet alone: **INCONCLUSIVE**
- Agreement 1.0, freeze OK, extended False
- hs: value 4.62, keys 0.812, ceremony 0.33, leaks 0.0, length x0.75 of sn
- hn: value 4.69, keys 0.91, ceremony 0.0, leaks 0.0, length x0.72 of sn
- ss: value 6.06, keys 0.958, ceremony 0.17, leaks 0.0, length x1.08 of sn
- sn: value 5.88, keys 0.979, ceremony 0.0, leaks 0.0, length x1.0 of sn
- Ruling: an INCONCLUSIVE uplift comparison is reported as such, without an extension. Reason: owner ruling: only the two skills with an open primary question (Haiku+skill vs Sonnet alone) were extended; this uplift comparison stays INCONCLUSIVE (see LEDGER)

## Autopsy

- **Haiku with the skill vs Sonnet alone: DOES NOT REACH.** Value -1.26, keys -0.17, rankings 1–5. Failing conditions: guard_audit_ceremony, value. NOISE: guard_judge_G3, keys.
- **What the skill does for each model:** Haiku -0.07 on value (NOT VALIDATED); Sonnet +0.18 (INCONCLUSIVE). Length: Haiku with the skill at 0.75× and Sonnet with the skill at 1.08× Sonnet alone.
- **Sources:** the pack and the Sonnet-alone replies come from `evolution/gauntlet-2026-10/breadth-of-thought`; Sonnet with the skill is freshly run on the current text (see `reuse.json`).
