# Scorecard: breadth-of-thought

Agreement 1.00 · freeze OK · extended False

| arm | value | V1 | V2 | V3 | V4 | G1 | G2 | G3 | keys | ceremony | leaks | length vs sn |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hs | 4.62 | 4.50 | 4.67 | 4.25 | 5.08 | 5.67 | 7.00 | 4.83 | 0.81 | 0.33 | 0.00 | 0.75 |
| hn | 4.69 | 4.58 | 5.00 | 4.08 | 5.08 | 5.58 | 7.00 | 4.50 | 0.91 | 0.00 | 0.00 | 0.72 |
| ss | 6.06 | 6.58 | 6.00 | 5.67 | 6.00 | 4.83 | 7.00 | 5.67 | 0.96 | 0.17 | 0.00 | 1.08 |
| sn | 5.88 | 6.33 | 6.00 | 5.33 | 5.83 | 4.33 | 7.00 | 5.17 | 0.98 | 0.00 | 0.00 | 1.00 |

**Haiku+skill reaches Sonnet alone (hs vs sn): DOES NOT REACH** · rankings won 1, lost 5 · value margin -1.25 (band 0.56) · key margin -0.17 (band 0.12)
guard_judge_G1 PASS · guard_judge_G2 PASS · guard_judge_G3 NOISE · guard_audit_ceremony FAIL · guard_audit_leaks PASS · guard_audit_length PASS · value FAIL · keys NOISE · ranking PASS · agreement PASS

**Haiku uplift (hs vs hn): NOT VALIDATED** · rankings won 3, lost 3 · value margin -0.06 (band 1.00) · key margin -0.10 (band 0.10)
guard_judge_G1 PASS · guard_judge_G2 PASS · guard_judge_G3 PASS · guard_audit_ceremony FAIL · guard_audit_leaks PASS · guard_audit_length PASS · value NOISE · ranking PASS · agreement PASS

**Sonnet uplift (ss vs sn): INCONCLUSIVE** · rankings won 4, lost 1 · value margin +0.19 (band 0.56) · key margin -0.02 (band 0.06)
guard_judge_G1 PASS · guard_judge_G2 PASS · guard_judge_G3 PASS · guard_audit_ceremony PASS · guard_audit_leaks PASS · guard_audit_length PASS · value NOISE · ranking PASS · agreement PASS
