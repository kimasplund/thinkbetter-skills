# Scorecard: premortem-evolved

Agreement 0.91 · freeze OK · extended False

| arm | value | V1 | V2 | V3 | V4 | G1 | G2 | G3 | keys | ceremony | leaks | length | negative | framing |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| new | 5.79 | 6.17 | 5.92 | 5.00 | 6.08 | 2.67 | 2.00 | 4.75 | 0.92 | 13.67 | 4.83 | 4.29 | ok | ok |
| old | 5.94 | 6.42 | 6.08 | 5.08 | 6.17 | 1.92 | 1.00 | 4.83 | 0.94 | 13.17 | 4.50 | 4.51 | ok | ok |
| none | 5.19 | 5.33 | 5.25 | 4.83 | 5.33 | 5.08 | 6.00 | 4.83 | 0.92 | 1.17 | 0.00 | 1.00 | ok | - |

**Validation (new vs none): NOT VALIDATED** · rankings won 3, lost 3 · value margin +0.60 (band 1.00) · key margin +0.00 (band 0.00)
guard_judge_G1 FAIL · guard_judge_G2 FAIL · guard_judge_G3 NOISE · guard_audit_ceremony FAIL · guard_audit_leaks FAIL · guard_audit_length FAIL · value NOISE · ranking PASS · negative PASS · framing PASS · agreement PASS

**Rewrite (new vs old): REVERT** · rankings won 4, lost 2 · value margin -0.15 (band 0.50) · key margin -0.02 (band 0.06)
guard_judge_G1 PASS · guard_judge_G2 PASS · guard_judge_G3 NOISE · guard_audit_ceremony FAIL · guard_audit_leaks FAIL · guard_audit_length PASS · keys NOISE · value PASS · negative PASS · framing PASS
