# Scorecard: option-synthesis

Agreement 0.93 · freeze OK · extended False

| arm | value | V1 | V2 | V3 | V4 | G1 | G2 | G3 | keys | ceremony | leaks | length vs sn |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hs | 5.00 | 4.58 | 5.58 | 4.17 | 5.67 | 5.50 | 4.25 | 4.67 | 0.85 | 2.50 | 0.17 | 0.91 |
| hn | 4.25 | 4.08 | 4.58 | 3.83 | 4.50 | 5.83 | 7.00 | 4.67 | 0.83 | 0.00 | 0.00 | 0.75 |
| ss | 5.75 | 6.08 | 5.75 | 4.92 | 6.25 | 2.00 | 1.75 | 4.08 | 0.88 | 9.17 | 2.17 | 4.07 |
| sn | 5.17 | 5.08 | 5.75 | 4.50 | 5.33 | 5.50 | 6.50 | 4.83 | 0.85 | 0.00 | 0.00 | 1.00 |

**Haiku+skill reaches Sonnet alone (hs vs sn): DOES NOT REACH** · rankings won 0, lost 4 · value margin -0.17 (band 1.00) · key margin +0.00 (band 0.12)
guard_judge_G1 PASS · guard_judge_G2 NOISE · guard_judge_G3 PASS · guard_audit_ceremony FAIL · guard_audit_leaks PASS · guard_audit_length PASS · value PASS · keys PASS · ranking FAIL · agreement PASS

**Haiku uplift (hs vs hn): NOT VALIDATED** · rankings won 3, lost 1 · value margin +0.75 (band 0.81) · key margin +0.02 (band 0.19)
guard_judge_G1 NOISE · guard_judge_G2 FAIL · guard_judge_G3 PASS · guard_audit_ceremony FAIL · guard_audit_leaks PASS · guard_audit_length PASS · value PASS · ranking PASS · agreement PASS

**Sonnet uplift (ss vs sn): NOT VALIDATED** · rankings won 0, lost 5 · value margin +0.58 (band 0.75) · key margin +0.02 (band 0.06)
guard_judge_G1 FAIL · guard_judge_G2 FAIL · guard_judge_G3 NOISE · guard_audit_ceremony FAIL · guard_audit_leaks FAIL · guard_audit_length FAIL · value PASS · ranking FAIL · agreement PASS
