# Scorecard: tree-of-thoughts

Agreement 0.99 · freeze OK · extended False

| arm | value | V1 | V2 | V3 | V4 | G1 | G2 | G3 | keys | ceremony | leaks | length | negative | framing |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| new | 5.90 | 5.92 | 6.00 | 5.50 | 6.17 | 4.92 | 6.92 | 5.33 | 0.94 | 0.33 | 0.00 | 1.24 | FAIL | ok |
| old | 6.25 | 6.33 | 6.08 | 6.00 | 6.58 | 5.33 | 7.00 | 6.00 | 1.00 | 0.17 | 0.00 | 1.21 | ok | ok |
| none | 5.19 | 5.25 | 5.25 | 4.75 | 5.50 | 5.67 | 7.00 | 5.08 | 0.98 | 0.00 | 0.00 | 1.00 | ok | - |

**Validation (new vs none): NOT VALIDATED** · rankings won 5, lost 0 · value margin +0.71 (band 0.12) · key margin -0.04 (band 0.19)
guard_judge_G1 NOISE · guard_judge_G2 NOISE · guard_judge_G3 PASS · guard_audit_ceremony FAIL · guard_audit_leaks PASS · guard_audit_length PASS · value PASS · ranking PASS · negative FAIL · framing PASS · agreement PASS

**Rewrite (new vs old): REVERT** · rankings won 0, lost 5 · value margin -0.35 (band 0.06) · key margin -0.06 (band 0.12)
guard_judge_G1 NOISE · guard_judge_G2 NOISE · guard_judge_G3 NOISE · guard_audit_ceremony FAIL · guard_audit_leaks PASS · guard_audit_length PASS · keys NOISE · value FAIL · negative FAIL · framing PASS
