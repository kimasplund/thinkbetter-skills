# Scorecard: hypothesis-elimination

Agreement 0.93 · freeze OK · extended False

| arm | value | V1 | V2 | V3 | V4 | G1 | G2 | G3 | keys | ceremony | leaks | length vs sn |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hs | 5.17 | 5.08 | 5.50 | 4.50 | 5.58 | 5.67 | 6.42 | 4.83 | 0.96 | 0.00 | 0.00 | 0.77 |
| hn | 5.15 | 5.00 | 5.33 | 4.75 | 5.50 | 5.67 | 7.00 | 5.08 | 0.96 | 0.17 | 0.00 | 0.76 |
| ss | 6.23 | 6.42 | 6.50 | 5.50 | 6.50 | 5.42 | 6.83 | 5.50 | 0.98 | 0.17 | 0.00 | 1.07 |
| sn | 6.08 | 6.08 | 6.33 | 5.42 | 6.50 | 5.33 | 7.00 | 5.50 | 0.96 | 0.33 | 0.00 | 1.00 |

**Haiku+skill reaches Sonnet alone (hs vs sn): DOES NOT REACH** · rankings won 0, lost 6 · value margin -0.92 (band 0.94) · key margin +0.00 (band 0.12)
guard_judge_G1 PASS · guard_judge_G2 NOISE · guard_judge_G3 NOISE · guard_audit_ceremony PASS · guard_audit_leaks PASS · guard_audit_length PASS · value NOISE · keys PASS · ranking FAIL · agreement PASS

**Haiku uplift (hs vs hn): INCONCLUSIVE** · rankings won 2, lost 3 · value margin +0.02 (band 1.25) · key margin +0.00 (band 0.00)
guard_judge_G1 PASS · guard_judge_G2 NOISE · guard_judge_G3 NOISE · guard_audit_ceremony PASS · guard_audit_leaks PASS · guard_audit_length PASS · value NOISE · ranking NOISE · agreement PASS

**Sonnet uplift (ss vs sn): INCONCLUSIVE** · rankings won 4, lost 2 · value margin +0.15 (band 0.94) · key margin +0.02 (band 0.06)
guard_judge_G1 PASS · guard_judge_G2 NOISE · guard_judge_G3 PASS · guard_audit_ceremony PASS · guard_audit_leaks PASS · guard_audit_length PASS · value NOISE · ranking PASS · agreement PASS
