# Scorecard: self-reflecting-chain

Agreement 0.97 · freeze OK · extended False

| arm | value | V1 | V2 | V3 | V4 | G1 | G2 | G3 | keys | ceremony | leaks | length | negative | framing |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| new | 5.90 | 5.92 | 6.00 | 5.08 | 6.58 | 5.83 | 7.00 | 4.83 | 0.98 | 0.50 | 0.00 | 1.00 | ok | ok |
| old | 5.69 | 5.67 | 5.75 | 5.50 | 5.83 | 5.00 | 6.83 | 5.67 | 0.92 | 0.17 | 0.00 | 1.11 | ok | ok |
| none | 5.69 | 5.75 | 5.92 | 5.42 | 5.67 | 5.17 | 6.83 | 5.67 | 0.94 | 0.17 | 0.00 | 1.00 | ok | ok |

**Validation (new vs none): NOT VALIDATED** · rankings won 5, lost 1 · value margin +0.21 (band 0.56) · key margin +0.04 (band 0.06)
guard_judge_G1 PASS · guard_judge_G2 PASS · guard_judge_G3 NOISE · guard_audit_ceremony FAIL · guard_audit_leaks PASS · guard_audit_length PASS · value NOISE · ranking PASS · negative PASS · framing PASS · agreement PASS

**Rewrite (new vs old): REVERT** · rankings won 3, lost 2 · value margin +0.21 (band 0.38) · key margin +0.06 (band 0.12)
guard_judge_G1 PASS · guard_judge_G2 PASS · guard_judge_G3 NOISE · guard_audit_ceremony FAIL · guard_audit_leaks PASS · guard_audit_length PASS · keys PASS · value PASS · negative PASS · framing PASS
