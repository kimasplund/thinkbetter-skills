# Scorecard: parallel-execution

Agreement 0.96 · freeze OK · extended False

| arm | value | V1 | V2 | V3 | V4 | G1 | G2 | G3 | keys | ceremony | leaks | length vs sn |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hs | 4.69 | 4.83 | 5.08 | 4.08 | 4.75 | 5.58 | 6.67 | 4.17 | 0.75 | 0.00 | 0.00 | 0.63 |
| hn | 4.48 | 4.75 | 5.00 | 3.50 | 4.67 | 5.92 | 7.00 | 4.58 | 0.77 | 0.33 | 0.00 | 0.61 |
| ss | 6.15 | 6.67 | 6.50 | 5.17 | 6.25 | 5.00 | 7.00 | 5.75 | 0.94 | 0.00 | 0.00 | 0.92 |
| sn | 6.06 | 6.33 | 6.42 | 5.50 | 6.00 | 4.67 | 7.00 | 5.83 | 0.98 | 0.33 | 0.00 | 1.00 |

**Haiku+skill reaches Sonnet alone (hs vs sn): DOES NOT REACH** · rankings won 0, lost 6 · value margin -1.38 (band 0.88) · key margin -0.23 (band 0.06)
guard_judge_G1 PASS · guard_judge_G2 NOISE · guard_judge_G3 NOISE · guard_audit_ceremony PASS · guard_audit_leaks PASS · guard_audit_length PASS · value FAIL · keys FAIL · ranking FAIL · agreement PASS

**Haiku uplift (hs vs hn): NOT VALIDATED** · rankings won 2, lost 2 · value margin +0.21 (band 0.94) · key margin -0.02 (band 0.19)
guard_judge_G1 FAIL · guard_judge_G2 NOISE · guard_judge_G3 NOISE · guard_audit_ceremony PASS · guard_audit_leaks PASS · guard_audit_length PASS · value NOISE · ranking PASS · agreement PASS

**Sonnet uplift (ss vs sn): INCONCLUSIVE** · rankings won 2, lost 2 · value margin +0.08 (band 0.62) · key margin -0.04 (band 0.06)
guard_judge_G1 PASS · guard_judge_G2 PASS · guard_judge_G3 NOISE · guard_audit_ceremony PASS · guard_audit_leaks PASS · guard_audit_length PASS · value NOISE · ranking PASS · agreement PASS
