# Scorecard: rapid-triage-reasoning

Agreement 1.00 · freeze OK · extended True

| arm | value | V1 | V2 | V3 | V4 | G1 | G2 | G3 | keys | ceremony | leaks | length | negative | framing |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| new | 5.72 | 5.79 | 6.00 | 5.08 | 6.00 | 5.38 | 7.00 | 5.12 | 0.98 | 0.00 | 0.00 | 0.88 | ok | ok |
| old | 5.78 | 5.88 | 5.92 | 5.42 | 5.92 | 5.08 | 7.00 | 5.29 | 1.00 | 0.08 | 0.00 | 0.94 | ok | ok |
| none | 5.76 | 5.92 | 5.96 | 5.17 | 6.00 | 4.71 | 6.92 | 5.21 | 0.98 | 0.58 | 0.00 | 1.00 | ok | ok |

**Validation (new vs none): NOT VALIDATED** · rankings won 4, lost 2 · value margin -0.04 (band 0.28) · key margin +0.00 (band 0.06)
guard_judge_G1 PASS · guard_judge_G2 PASS · guard_judge_G3 NOISE · guard_audit_ceremony PASS · guard_audit_leaks PASS · guard_audit_length PASS · value FAIL · ranking PASS · negative PASS · framing PASS · agreement PASS

**Rewrite (new vs old): REVERT** · rankings won 2, lost 4 · value margin -0.06 (band 0.16) · key margin -0.02 (band 0.06)
guard_judge_G1 PASS · guard_judge_G2 PASS · guard_judge_G3 NOISE · guard_audit_ceremony PASS · guard_audit_leaks PASS · guard_audit_length PASS · keys NOISE · value PASS · negative PASS · framing PASS
