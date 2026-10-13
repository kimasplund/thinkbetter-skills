# Scorecard: rapid-triage-reasoning

Agreement 0.98 · freeze OK · extended False

| arm | value | V1 | V2 | V3 | V4 | G1 | G2 | G3 | keys | ceremony | leaks | length vs sn |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hs | 4.88 | 4.83 | 5.25 | 4.17 | 5.25 | 5.67 | 6.50 | 4.58 | 0.85 | 0.17 | 0.00 | 0.71 |
| hn | 5.02 | 5.08 | 5.33 | 4.58 | 5.08 | 5.75 | 6.83 | 4.67 | 0.85 | 0.17 | 0.00 | 0.68 |
| ss | 6.06 | 6.17 | 6.25 | 5.67 | 6.17 | 4.83 | 7.00 | 5.33 | 0.94 | 0.00 | 0.00 | 0.97 |
| sn | 6.10 | 6.17 | 6.25 | 5.75 | 6.25 | 4.67 | 7.00 | 5.42 | 0.94 | 0.50 | 0.00 | 1.00 |

**Haiku+skill reaches Sonnet alone (hs vs sn): DOES NOT REACH** · rankings won 0, lost 6 · value margin -1.23 (band 0.19) · key margin -0.08 (band 0.25)
guard_judge_G1 PASS · guard_judge_G2 NOISE · guard_judge_G3 NOISE · guard_audit_ceremony PASS · guard_audit_leaks PASS · guard_audit_length PASS · value FAIL · keys PASS · ranking FAIL · agreement PASS

**Haiku uplift (hs vs hn): INCONCLUSIVE** · rankings won 1, lost 2 · value margin -0.15 (band 0.81) · key margin +0.00 (band 0.12)
guard_judge_G1 NOISE · guard_judge_G2 NOISE · guard_judge_G3 NOISE · guard_audit_ceremony PASS · guard_audit_leaks PASS · guard_audit_length PASS · value NOISE · ranking NOISE · agreement PASS

**Sonnet uplift (ss vs sn): INCONCLUSIVE** · rankings won 1, lost 2 · value margin -0.04 (band 0.31) · key margin +0.00 (band 0.12)
guard_judge_G1 PASS · guard_judge_G2 PASS · guard_judge_G3 NOISE · guard_audit_ceremony PASS · guard_audit_leaks PASS · guard_audit_length PASS · value NOISE · ranking NOISE · agreement PASS
