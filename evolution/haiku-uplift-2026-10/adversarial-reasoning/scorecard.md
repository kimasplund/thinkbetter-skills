# Scorecard: adversarial-reasoning

Agreement 0.99 · freeze OK · extended False

| arm | value | V1 | V2 | V3 | V4 | G1 | G2 | G3 | keys | ceremony | leaks | length vs sn |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hs | 5.21 | 5.17 | 5.50 | 4.75 | 5.42 | 4.75 | 4.67 | 5.08 | 0.75 | 1.00 | 0.33 | 0.88 |
| hn | 4.88 | 4.67 | 5.17 | 4.42 | 5.25 | 5.42 | 6.83 | 4.83 | 0.79 | 0.17 | 0.00 | 0.74 |
| ss | 6.27 | 6.58 | 6.33 | 5.67 | 6.50 | 4.17 | 6.58 | 5.50 | 0.88 | 0.00 | 0.00 | 1.23 |
| sn | 5.85 | 6.17 | 6.00 | 5.42 | 5.83 | 4.33 | 6.83 | 5.08 | 0.88 | 0.17 | 0.00 | 1.00 |

**Haiku+skill reaches Sonnet alone (hs vs sn): DOES NOT REACH** · rankings won 1, lost 5 · value margin -0.65 (band 1.75) · key margin -0.12 (band 0.19)
guard_judge_G1 PASS · guard_judge_G2 FAIL · guard_judge_G3 PASS · guard_audit_ceremony FAIL · guard_audit_leaks FAIL · guard_audit_length PASS · value NOISE · keys NOISE · ranking PASS · agreement PASS

**Haiku uplift (hs vs hn): NOT VALIDATED** · rankings won 3, lost 3 · value margin +0.33 (band 1.75) · key margin -0.04 (band 0.06)
guard_judge_G1 FAIL · guard_judge_G2 FAIL · guard_judge_G3 PASS · guard_audit_ceremony FAIL · guard_audit_leaks FAIL · guard_audit_length PASS · value NOISE · ranking PASS · agreement PASS

**Sonnet uplift (ss vs sn): INCONCLUSIVE** · rankings won 3, lost 2 · value margin +0.42 (band 0.94) · key margin +0.00 (band 0.00)
guard_judge_G1 NOISE · guard_judge_G2 NOISE · guard_judge_G3 PASS · guard_audit_ceremony PASS · guard_audit_leaks PASS · guard_audit_length PASS · value NOISE · ranking PASS · agreement PASS
