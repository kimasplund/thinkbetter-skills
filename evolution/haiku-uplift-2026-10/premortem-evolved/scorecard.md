# Scorecard: premortem-evolved

Agreement 0.95 · freeze OK · extended False

| arm | value | V1 | V2 | V3 | V4 | G1 | G2 | G3 | keys | ceremony | leaks | length vs sn |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hs | 4.83 | 5.08 | 5.25 | 3.83 | 5.17 | 2.50 | 1.50 | 3.75 | 0.90 | 7.67 | 5.17 | 3.36 |
| hn | 4.75 | 4.83 | 5.00 | 4.42 | 4.75 | 5.75 | 6.50 | 5.17 | 0.81 | 0.67 | 0.00 | 0.80 |
| ss | 6.15 | 6.75 | 6.08 | 5.42 | 6.33 | 1.92 | 1.00 | 4.58 | 0.96 | 9.00 | 5.67 | 4.51 |
| sn | 5.77 | 5.83 | 5.83 | 5.58 | 5.83 | 6.00 | 7.00 | 5.33 | 0.92 | 0.33 | 0.00 | 1.00 |

**Haiku+skill reaches Sonnet alone (hs vs sn): DOES NOT REACH** · rankings won 0, lost 6 · value margin -0.94 (band 0.44) · key margin -0.02 (band 0.25)
guard_judge_G1 FAIL · guard_judge_G2 FAIL · guard_judge_G3 NOISE · guard_audit_ceremony FAIL · guard_audit_leaks FAIL · guard_audit_length FAIL · value FAIL · keys PASS · ranking FAIL · agreement PASS

**Haiku uplift (hs vs hn): NOT VALIDATED** · rankings won 1, lost 5 · value margin +0.08 (band 1.25) · key margin +0.08 (band 0.38)
guard_judge_G1 FAIL · guard_judge_G2 FAIL · guard_judge_G3 FAIL · guard_audit_ceremony FAIL · guard_audit_leaks FAIL · guard_audit_length FAIL · value NOISE · ranking NOISE · agreement PASS

**Sonnet uplift (ss vs sn): NOT VALIDATED** · rankings won 0, lost 6 · value margin +0.38 (band 0.50) · key margin +0.04 (band 0.12)
guard_judge_G1 FAIL · guard_judge_G2 FAIL · guard_judge_G3 NOISE · guard_audit_ceremony FAIL · guard_audit_leaks FAIL · guard_audit_length FAIL · value NOISE · ranking FAIL · agreement PASS
