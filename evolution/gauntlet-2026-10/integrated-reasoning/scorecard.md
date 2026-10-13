# Scorecard: integrated-reasoning

Agreement 1.00 · freeze OK · extended False

| arm | value | V1 | V2 | V3 | V4 | G1 | G2 | G3 | keys | ceremony | leaks | length | negative | framing |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| new | 5.46 | 5.58 | 5.67 | 4.75 | 5.83 | 4.83 | 6.33 | 4.75 | 0.88 | 0.00 | 0.17 | 1.06 | ok | ok |
| old | 5.77 | 5.83 | 5.92 | 5.33 | 6.00 | 4.83 | 6.67 | 5.25 | 0.92 | 0.17 | 0.00 | 1.10 | ok | ok |
| none | 5.46 | 5.42 | 5.75 | 4.92 | 5.75 | 5.17 | 7.00 | 5.25 | 0.88 | 0.00 | 0.00 | 1.00 | ok | - |

**Validation (new vs none): NOT VALIDATED** · rankings won 0, lost 2 · value margin +0.00 (band 0.56) · key margin +0.00 (band 0.19)
guard_judge_G1 NOISE · guard_judge_G2 NOISE · guard_judge_G3 NOISE · guard_audit_ceremony PASS · guard_audit_leaks FAIL · guard_audit_length PASS · value NOISE · ranking NOISE · negative PASS · framing PASS · agreement PASS

**Rewrite (new vs old): REVERT** · rankings won 0, lost 4 · value margin -0.31 (band 0.44) · key margin -0.04 (band 0.19)
guard_judge_G1 PASS · guard_judge_G2 NOISE · guard_judge_G3 NOISE · guard_audit_ceremony PASS · guard_audit_leaks FAIL · guard_audit_length PASS · keys NOISE · value NOISE · negative PASS · framing PASS
