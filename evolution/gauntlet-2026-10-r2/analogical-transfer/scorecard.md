# Scorecard: analogical-transfer

Agreement 1.00 · freeze OK · extended False

| arm | value | V1 | V2 | V3 | V4 | G1 | G2 | G3 | keys | ceremony | leaks | length | negative | framing |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| new | 6.10 | 6.25 | 6.25 | 5.75 | 6.17 | 4.75 | 4.83 | 6.08 | 0.92 | 1.83 | 0.00 | 1.24 | ok | ok |
| old | 5.79 | 6.08 | 6.00 | 5.25 | 5.83 | 5.25 | 6.83 | 5.58 | 0.96 | 0.17 | 0.00 | 1.24 | ok | ok |
| none | 5.21 | 5.33 | 5.42 | 4.83 | 5.25 | 5.33 | 6.75 | 4.83 | 0.94 | 0.50 | 0.00 | 1.00 | ok | ok |

**Validation (new vs none): NOT VALIDATED** · rankings won 5, lost 1 · value margin +0.90 (band 0.75) · key margin -0.02 (band 0.06)
guard_judge_G1 NOISE · guard_judge_G2 NOISE · guard_judge_G3 PASS · guard_audit_ceremony FAIL · guard_audit_leaks PASS · guard_audit_length PASS · value PASS · ranking PASS · negative PASS · framing PASS · agreement PASS

**Rewrite (new vs old): REVERT** · rankings won 1, lost 4 · value margin +0.31 (band 0.44) · key margin -0.04 (band 0.06)
guard_judge_G1 NOISE · guard_judge_G2 NOISE · guard_judge_G3 PASS · guard_audit_ceremony FAIL · guard_audit_leaks PASS · guard_audit_length PASS · keys NOISE · value PASS · negative PASS · framing PASS
