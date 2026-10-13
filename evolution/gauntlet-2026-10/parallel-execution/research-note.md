# Research note: parallel-execution

- Validation (new vs none): **NOT VALIDATED**; rewrite (new vs old): **REVERT**
- Agreement 0.984, freeze OK, extended True
- new: value 5.39, keys 0.938, ceremony 0.08, leaks 0.0, length x0.99, negative ok, framing True
- old: value 5.8, keys 0.948, ceremony 0.0, leaks 0.0, length x1.03, negative ok, framing True
- none: value 5.58, keys 0.948, ceremony 0.17, leaks 0.0, length x1.0, negative ok, framing None

## Autopsy

- **What drove the verdict:** after 2 runs both gates were INCONCLUSIVE. After the pre-registered extension, validation is NOT VALIDATED: the value margin is −0.20 against no skill, well inside the noise band (0.66), and rankings split 3–3. Keys were at the ceiling in all arms (0.94 to 0.95).
- **Rewrite: REVERT on value.** The rewrite lost all 6 rankings to v1.0.0, with a value margin of −0.42 outside the band (0.16). The ceremony FAIL is the strict one-hit rule (1 hit in 12 replies vs 0). Under one-hit tolerance the verdict would still be REVERT, because the value FAIL decides it alone.
- **Design vs compliance:** v1.0.0 scored the highest value of the three arms (5.80, against 5.58 for no skill), mostly on V1 and V3. No gate tests old vs none, so this is a direction, not a finding.
- **Not chased:** the restored v1.0.0 body names Claude Code version specifics (v2.1.76, the agent-teams environment variable) that the rewrite had made harness-neutral. The mechanical rule restores them as they were; a later round could test a harness-neutral edit of the v1.0.0 body on its own.
