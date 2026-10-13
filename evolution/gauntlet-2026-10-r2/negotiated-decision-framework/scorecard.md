# Scorecard: negotiated-decision-framework

Agreement 0.98 · freeze OK · extended True

| arm | value | V1 | V2 | V3 | V4 | G1 | G2 | G3 | keys | ceremony | leaks | length | negative | framing |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| new | 5.79 | 5.58 | 5.79 | 5.08 | 6.71 | 5.46 | 5.96 | 4.79 | 0.98 | 0.17 | 0.00 | 0.98 | ok | ok |
| old | 5.65 | 5.88 | 5.83 | 5.04 | 5.83 | 4.50 | 6.46 | 5.12 | 0.98 | 0.08 | 0.00 | 1.22 | ok | ok |
| none | 5.56 | 6.00 | 5.67 | 5.33 | 5.25 | 4.50 | 6.67 | 5.29 | 0.99 | 0.25 | 0.00 | 1.00 | ok | ok |

**Validation (new vs none): NOT VALIDATED** · rankings won 4, lost 2 · value margin +0.23 (band 1.12) · key margin -0.01 (band 0.09)
guard_judge_G1 PASS · guard_judge_G2 NOISE · guard_judge_G3 FAIL · guard_audit_ceremony PASS · guard_audit_leaks PASS · guard_audit_length PASS · value NOISE · ranking PASS · negative PASS · framing PASS · agreement PASS

**Rewrite (new vs old): REVERT** · rankings won 2, lost 4 · value margin +0.15 (band 0.72) · key margin +0.00 (band 0.12)
guard_judge_G1 PASS · guard_judge_G2 FAIL · guard_judge_G3 NOISE · guard_audit_ceremony PASS · guard_audit_leaks PASS · guard_audit_length PASS · keys PASS · value PASS · negative PASS · framing PASS
