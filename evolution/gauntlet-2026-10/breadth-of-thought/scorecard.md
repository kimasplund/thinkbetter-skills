# Scorecard: breadth-of-thought

Agreement 0.99 · freeze OK · extended False

| arm | value | V1 | V2 | V3 | V4 | G1 | G2 | G3 | keys | ceremony | leaks | length | negative | framing |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| new | 5.38 | 5.42 | 5.50 | 4.92 | 5.67 | 4.83 | 6.75 | 5.17 | 0.88 | 0.17 | 0.00 | 1.27 | ok | ok |
| old | 5.77 | 6.00 | 5.75 | 5.50 | 5.83 | 4.75 | 7.00 | 5.50 | 0.92 | 0.00 | 0.00 | 1.30 | ok | ok |
| none | 5.29 | 5.42 | 5.50 | 4.92 | 5.33 | 5.33 | 7.00 | 5.00 | 0.96 | 0.00 | 0.00 | 1.00 | ok | - |

**Validation (new vs none): NOT VALIDATED** · rankings won 3, lost 2 · value margin +0.08 (band 1.31) · key margin -0.08 (band 0.19)
guard_judge_G1 NOISE · guard_judge_G2 NOISE · guard_judge_G3 PASS · guard_audit_ceremony FAIL · guard_audit_leaks PASS · guard_audit_length PASS · value NOISE · ranking PASS · negative PASS · framing PASS · agreement PASS

**Rewrite (new vs old): REVERT** · rankings won 1, lost 4 · value margin -0.40 (band 1.00) · key margin -0.04 (band 0.12)
guard_judge_G1 PASS · guard_judge_G2 NOISE · guard_judge_G3 NOISE · guard_audit_ceremony FAIL · guard_audit_leaks PASS · guard_audit_length PASS · keys NOISE · value NOISE · negative PASS · framing PASS
