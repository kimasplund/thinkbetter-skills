# Scorecard: parallel-execution

Agreement 0.98 · freeze OK · extended True

| arm | value | V1 | V2 | V3 | V4 | G1 | G2 | G3 | keys | ceremony | leaks | length | negative | framing |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| new | 5.39 | 5.50 | 5.83 | 4.83 | 5.38 | 5.21 | 6.92 | 5.21 | 0.94 | 0.08 | 0.00 | 0.99 | ok | ok |
| old | 5.80 | 6.12 | 6.04 | 5.25 | 5.79 | 5.08 | 7.00 | 5.58 | 0.95 | 0.00 | 0.00 | 1.03 | ok | ok |
| none | 5.58 | 5.83 | 6.00 | 4.92 | 5.58 | 4.88 | 7.00 | 5.12 | 0.95 | 0.17 | 0.00 | 1.00 | ok | - |

**Validation (new vs none): NOT VALIDATED** · rankings won 3, lost 3 · value margin -0.20 (band 0.66) · key margin -0.01 (band 0.12)
guard_judge_G1 PASS · guard_judge_G2 NOISE · guard_judge_G3 PASS · guard_audit_ceremony PASS · guard_audit_leaks PASS · guard_audit_length PASS · value NOISE · ranking PASS · negative PASS · framing PASS · agreement PASS

**Rewrite (new vs old): REVERT** · rankings won 0, lost 6 · value margin -0.42 (band 0.16) · key margin -0.01 (band 0.06)
guard_judge_G1 PASS · guard_judge_G2 NOISE · guard_judge_G3 NOISE · guard_audit_ceremony FAIL · guard_audit_leaks PASS · guard_audit_length PASS · keys NOISE · value FAIL · negative PASS · framing PASS
