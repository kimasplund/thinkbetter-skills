# Research note: premortem-evolved

- Validation (new vs none): **NOT VALIDATED**; rewrite (new vs old): **REVERT**
- Agreement 0.913, freeze OK, extended False
- new: value 5.79, keys 0.917, ceremony 13.67, leaks 4.83, length x4.29, negative ok, framing True
- old: value 5.94, keys 0.938, ceremony 13.17, leaks 4.5, length x4.51, negative ok, framing True
- none: value 5.19, keys 0.917, ceremony 1.17, leaks 0.0, length x1.0, negative ok, framing None

## Autopsy

- **Validation: NOT VALIDATED, decisively on the guards.** Both premortem arms write reports 4.3 to 4.5 times the no-skill length. Against no skill, G1 is 2.67 vs 5.08 and G2 2.00 vs 6.00, and the auditor counts 13.7 ceremony hits and 4.8 leaks per reply vs 1.2 and 0. Value is +0.60 but inside the band (1.00), and rankings split 3–3.
- **Design vs instrument:** the skill's deliverable is a structured premortem artifact: autopsy, probability ladder, kill chain and tripwires. The rubric's G2 counts a visible method structure as leakage, so this skill can't pass G2 by design, even though it forbids backstage machinery itself. Measuring premortem-evolved fairly needs an owner decision on an artifact-aware rubric; this round measures it as a general reply.
- **Rewrite: REVERT on the strict audit rule.** 2.2.1 has 82 ceremony hits vs 79 and 29 leaks vs 27 across 6 replies. That is a few percent on large counts, but "less than 1 hit in total" is the band. The judges went the other way: G2 2.00 vs 1.00 and G1 2.67 vs 1.92 favour 2.2.1, which renamed the paper-tiger and gap-check labels into plain English, and 2.2.1 won rankings 4–2 with value non-inferior (−0.15, band 0.50). Under a proportional audit tolerance the rewrite would be INCONCLUSIVE (keys and G3 NOISE) and would have earned an extension.
- **Ruling:** the revert restores the measured text only. `scripts/pre_delivery_check.py` keeps its 1.1.0 bug fixes, because no gauntlet cell can run scripts; see the LEDGER ruling for round 8.
