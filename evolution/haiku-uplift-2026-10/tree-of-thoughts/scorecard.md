# Scorecard: tree-of-thoughts

Agreement 0.99 · freeze OK · extended True

| arm | value | V1 | V2 | V3 | V4 | G1 | G2 | G3 | keys | ceremony | leaks | length vs sn |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hs | 5.17 | 5.42 | 5.21 | 4.75 | 5.29 | 5.92 | 6.92 | 4.88 | 0.91 | 0.08 | 0.00 | 0.80 |
| hn | 5.05 | 5.38 | 5.25 | 4.71 | 4.88 | 5.50 | 6.83 | 5.25 | 0.98 | 0.08 | 0.00 | 0.90 |
| ss | 6.42 | 6.71 | 6.58 | 5.83 | 6.54 | 4.96 | 7.00 | 5.96 | 0.98 | 0.33 | 0.00 | 1.26 |
| sn | 5.78 | 5.88 | 6.00 | 5.33 | 5.92 | 5.75 | 7.00 | 5.50 | 1.00 | 0.17 | 0.00 | 1.00 |

**Haiku+skill reaches Sonnet alone (hs vs sn): DOES NOT REACH** · rankings won 0, lost 6 · value margin -0.61 (band 0.16) · key margin -0.09 (band 0.16)
guard_judge_G1 PASS · guard_judge_G2 PASS · guard_judge_G3 FAIL · guard_audit_ceremony PASS · guard_audit_leaks PASS · guard_audit_length PASS · value FAIL · keys PASS · ranking FAIL · agreement PASS

**Haiku uplift (hs vs hn): NOT VALIDATED** · rankings won 4, lost 2 · value margin +0.11 (band 0.72) · key margin -0.07 (band 0.19)
guard_judge_G1 PASS · guard_judge_G2 PASS · guard_judge_G3 NOISE · guard_audit_ceremony PASS · guard_audit_leaks PASS · guard_audit_length PASS · value NOISE · ranking PASS · agreement PASS

**Sonnet uplift (ss vs sn): NOT VALIDATED** · rankings won 5, lost 1 · value margin +0.64 (band 0.16) · key margin -0.02 (band 0.06)
guard_judge_G1 FAIL · guard_judge_G2 PASS · guard_judge_G3 PASS · guard_audit_ceremony FAIL · guard_audit_leaks PASS · guard_audit_length PASS · value PASS · ranking PASS · agreement PASS
