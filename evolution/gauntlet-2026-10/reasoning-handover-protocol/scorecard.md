# Scorecard: reasoning-handover-protocol

Agreement 0.99 · freeze OK · extended False

| arm | value | V1 | V2 | V3 | V4 | G1 | G2 | G3 | keys | ceremony | leaks | length | negative | framing |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| new | 5.62 | 5.58 | 5.67 | 5.33 | 5.92 | 5.67 | 6.83 | 5.42 | 0.94 | 0.17 | 0.00 | 0.85 | ok | ok |
| old | 5.77 | 6.00 | 5.83 | 5.50 | 5.75 | 5.08 | 6.67 | 5.92 | 0.96 | 0.00 | 0.33 | 0.96 | ok | ok |
| none | 5.62 | 5.83 | 5.75 | 5.42 | 5.50 | 4.92 | 6.75 | 5.58 | 0.96 | 0.00 | 0.00 | 1.00 | ok | - |

**Validation (new vs none): NOT VALIDATED** · rankings won 3, lost 2 · value margin +0.00 (band 0.75) · key margin -0.02 (band 0.06)
guard_judge_G1 PASS · guard_judge_G2 PASS · guard_judge_G3 NOISE · guard_audit_ceremony FAIL · guard_audit_leaks PASS · guard_audit_length PASS · value NOISE · ranking PASS · negative PASS · framing PASS · agreement PASS

**Rewrite (new vs old): REVERT** · rankings won 2, lost 4 · value margin -0.15 (band 1.69) · key margin -0.02 (band 0.19)
guard_judge_G1 PASS · guard_judge_G2 PASS · guard_judge_G3 NOISE · guard_audit_ceremony FAIL · guard_audit_leaks PASS · guard_audit_length PASS · keys NOISE · value PASS · negative PASS · framing PASS
