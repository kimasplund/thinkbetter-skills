# Scorecard: self-reflecting-chain

Agreement 0.99 · freeze OK · extended True

| arm | value | V1 | V2 | V3 | V4 | G1 | G2 | G3 | keys | ceremony | leaks | length | negative | framing |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| new | 5.79 | 5.71 | 5.79 | 5.67 | 6.00 | 5.42 | 6.62 | 5.75 | 1.00 | 0.58 | 0.00 | 1.06 | ok | ok |
| old | 5.76 | 5.96 | 5.92 | 5.12 | 6.04 | 5.12 | 6.88 | 5.29 | 1.00 | 0.50 | 0.00 | 1.04 | ok | ok |
| none | 5.62 | 5.62 | 5.79 | 5.17 | 5.92 | 5.38 | 6.96 | 5.25 | 0.99 | 0.50 | 0.00 | 1.00 | ok | - |

**Validation (new vs none): NOT VALIDATED** · rankings won 5, lost 1 · value margin +0.17 (band 0.19) · key margin +0.01 (band 0.03)
guard_judge_G1 PASS · guard_judge_G2 NOISE · guard_judge_G3 PASS · guard_audit_ceremony FAIL · guard_audit_leaks PASS · guard_audit_length PASS · value FAIL · ranking PASS · negative PASS · framing PASS · agreement PASS

**Rewrite (new vs old): REVERT** · rankings won 2, lost 3 · value margin +0.03 (band 0.78) · key margin +0.00 (band 0.00)
guard_judge_G1 PASS · guard_judge_G2 NOISE · guard_judge_G3 PASS · guard_audit_ceremony FAIL · guard_audit_leaks PASS · guard_audit_length PASS · keys PASS · value PASS · negative PASS · framing PASS
