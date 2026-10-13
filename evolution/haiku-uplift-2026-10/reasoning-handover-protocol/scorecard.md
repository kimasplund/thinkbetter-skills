# Scorecard: reasoning-handover-protocol

Agreement 0.94 · freeze OK · extended False

| arm | value | V1 | V2 | V3 | V4 | G1 | G2 | G3 | keys | ceremony | leaks | length vs sn |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hs | 4.58 | 4.67 | 4.83 | 4.25 | 4.58 | 5.25 | 5.58 | 4.92 | 0.83 | 0.17 | 0.33 | 0.77 |
| hn | 4.67 | 4.75 | 5.08 | 4.33 | 4.50 | 5.67 | 6.92 | 4.83 | 0.83 | 0.17 | 0.00 | 0.74 |
| ss | 6.00 | 6.17 | 6.00 | 5.75 | 6.08 | 5.50 | 6.75 | 5.92 | 0.98 | 0.17 | 0.33 | 0.96 |
| sn | 5.79 | 6.08 | 5.83 | 5.67 | 5.58 | 5.00 | 7.00 | 5.67 | 0.96 | 0.17 | 0.00 | 1.00 |

**Haiku+skill reaches Sonnet alone (hs vs sn): DOES NOT REACH** · rankings won 1, lost 5 · value margin -1.21 (band 1.31) · key margin -0.12 (band 0.19)
guard_judge_G1 PASS · guard_judge_G2 NOISE · guard_judge_G3 NOISE · guard_audit_ceremony PASS · guard_audit_leaks FAIL · guard_audit_length PASS · value NOISE · keys NOISE · ranking PASS · agreement PASS

**Haiku uplift (hs vs hn): NOT VALIDATED** · rankings won 2, lost 3 · value margin -0.08 (band 1.06) · key margin +0.00 (band 0.19)
guard_judge_G1 FAIL · guard_judge_G2 FAIL · guard_judge_G3 PASS · guard_audit_ceremony PASS · guard_audit_leaks FAIL · guard_audit_length PASS · value NOISE · ranking NOISE · agreement PASS

**Sonnet uplift (ss vs sn): NOT VALIDATED** · rankings won 3, lost 1 · value margin +0.21 (band 0.75) · key margin +0.02 (band 0.06)
guard_judge_G1 PASS · guard_judge_G2 NOISE · guard_judge_G3 PASS · guard_audit_ceremony PASS · guard_audit_leaks FAIL · guard_audit_length PASS · value NOISE · ranking PASS · agreement PASS
