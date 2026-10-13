# Scorecard: self-reflecting-chain

Agreement 0.98 · freeze OK · extended True

| arm | value | V1 | V2 | V3 | V4 | G1 | G2 | G3 | keys | ceremony | leaks | length | negative | framing |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| new | 5.99 | 5.92 | 6.17 | 5.62 | 6.25 | 5.42 | 5.92 | 5.67 | 0.99 | 0.42 | 0.00 | 1.00 | ok | ok |
| old | 5.76 | 5.96 | 6.04 | 5.62 | 5.42 | 5.12 | 6.83 | 5.42 | 0.91 | 0.17 | 0.00 | 1.13 | ok | ok |
| none | 5.78 | 5.92 | 5.92 | 5.88 | 5.42 | 5.33 | 6.75 | 5.71 | 0.94 | 0.25 | 0.00 | 1.00 | ok | ok |

**Validation (new vs none): NOT VALIDATED** · rankings won 3, lost 3 · value margin +0.21 (band 0.31) · key margin +0.05 (band 0.16)
guard_judge_G1 PASS · guard_judge_G2 NOISE · guard_judge_G3 NOISE · guard_audit_ceremony FAIL · guard_audit_leaks PASS · guard_audit_length PASS · value NOISE · ranking PASS · negative PASS · framing PASS · agreement PASS

**Rewrite (new vs old): REVERT** · rankings won 3, lost 3 · value margin +0.23 (band 0.50) · key margin +0.08 (band 0.12)
guard_judge_G1 PASS · guard_judge_G2 NOISE · guard_judge_G3 PASS · guard_audit_ceremony FAIL · guard_audit_leaks PASS · guard_audit_length PASS · keys PASS · value PASS · negative PASS · framing PASS
