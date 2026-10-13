# Validation record

This is the full record behind the README's validation status: how each skill was tested, what each round found, and which versions ship by owner decision. Every round is pre-registered and blind; the raw records live under [evolution/](../evolution/).

## Owner decisions in 1.2.1

The 1.2.0 reverts restored the v1.0.0 bodies of integrated-reasoning, tree-of-thoughts and breadth-of-thought, and with them three arithmetic bugs that 1.1.0 had fixed. In 1.2.1 only those fixes were re-applied, by owner decision and without a gauntlet round. They change numbers, not method:

- **integrated-reasoning 2.3.2:** the Direct Analysis threshold is reachable and consistent, and the worked example recomputes.
- **tree-of-thoughts 2.3.2:** the confidence likelihood ratio no longer saturates at the 95% cap.
- **breadth-of-thought 2.3.2:** the confidence formula reaches its full range, and every branch count agrees with the others.

## Haiku uplift, October 2026

Does Haiku with a skill reach Sonnet without one? For each skill, four arms were judged together in one blind panel on that skill's sealed briefs: Haiku with the skill, Haiku alone, Sonnet with the skill and Sonnet alone. Sonnet replies were reused from the earlier rounds where the skill text was unchanged. **The answer is no, for all 15 skills.**

- **Mean value (1–7):** Sonnet with the skill 6.18, Sonnet alone 5.86, Haiku with the skill 4.85, Haiku alone 4.79.
- **Keys caught:** 95%, 93%, 81% and 81%.
- **The skills lift Sonnet (+0.31, positive for 14 of 15) far more than Haiku (+0.05, positive for 9 of 15).** They amplify a capable model rather than standing in for one.
- **Ruling:** only the two skills with the main question open were extended. Inconclusive uplift comparisons elsewhere stay inconclusive.

Record: [summary](../evolution/haiku-uplift-2026-10/SUMMARY.md), [ledger](../evolution/haiku-uplift-2026-10/LEDGER.md), [design](superpowers/specs/2026-10-13-haiku-uplift-design.md).

### Suite gauntlet, October 2026

- **Design.** Each round had three fictional briefs with planted keys sealed from the coordinator, a hype/skeptical framing pair of the same facts, and a task too small for the skill. Sonnet answered each brief twice per arm, or four times after the one allowed extension. Two Opus judges per brief scored the blinded replies on four value and three guard dimensions and ranked them. A Sonnet auditor counted visible method machinery, and Sonnet verifiers checked the planted keys. A skill validates only if every condition passes: value above the paired noise band, no guard regression, no extra method ceremony, and the same recommendation under both framings. Each round's gate was frozen before it ran. Design: [spec](superpowers/specs/2026-10-13-suite-gauntlet-design.md).
- **Rewrites.** Seven skills had a 1.1.0 body that differed from 1.0.0, so their rounds added a third arm. Every one of those rewrites lost to or tied v1.0.0 and was reverted to the v1.0.0 body, keeping the 1.1.0 frontmatter (now 2.3.1, or 2.2.2 for premortem-evolved). The restored bodies were compared with the rewrites, not with no skill.
- **Where the skills helped.** The skill arm scored higher value than no skill on every brief in 10 of 15 rounds, and won at least 5 of 6 blind rankings in 7. Value cleared its noise band in 4: tree-of-thoughts (the reverted 1.1.0 body), analogical-transfer, negotiated-decision-framework and option-synthesis.
- **What blocked them.** Mostly visible method. The ceremony audit failed in 10 of 15 rounds, and several skills made replies longer than the judges thought the task needed. rapid-triage-reasoning and option-synthesis changed their recommendation between the hype and skeptical framings of the same facts. premortem-evolved and option-synthesis deliver a structured report by design, which the rubric's machinery and length guards penalise, and both failed those guards decisively.
- **Limits of the instrument.** The audit band is strict: one extra hit in total fails, and each research note gives the tolerant reading where that mattered. The value band is the spread of the per-brief gains, so a gain that is positive on every brief but uneven can read as noise (adversarial-reasoning: +0.72, every brief positive, band 1.06). Executors were Sonnet only. The rubric scores every reply as a general answer, not as a report artifact.

### Follow-up rounds, October 2026 (r2)

A post-hoc review ([summary](../evolution/gauntlet-2026-10/_followup/SUMMARY.md)) found real but blocked gains in five skills and four misfiring gate rules. The owner amended the gates for a follow-up program ([Amendment 3](superpowers/specs/2026-10-13-suite-gauntlet-design.md)): a value sign path, a 0.25 floor on guard bands, one tolerated audit hit, auditor quote verification, and the framing pair on every arm. Each skill then got one targeted edit and a fresh round on new briefs ([ledger](../evolution/gauntlet-2026-10-r2/LEDGER.md)). **No edit was adopted, and all five skills ship unchanged.**

- **Two edits fixed what they targeted but failed elsewhere.** tree-of-thoughts' answer-shape rule made replies shorter than no skill's and better proportioned. adversarial-reasoning's edit removed its confidence heading, and the skill beat no skill by +1.04 on value, 6–0. Both then changed their recommendation between the hype and skeptical framings, while no skill did not.
- **Three edits lost to the shipped text.** analogical-transfer's template edit surfaced more method headings. negotiated-decision-framework's edit made replies tighter and more decisive but less calibrated. rapid-triage-reasoning did not beat no skill on fresh briefs.
- **The new quote check caught two misattributed auditor quotes,** and the identical-prompt re-runs passed.
- **The shipped analogical-transfer text beat no skill 6–0 on fresh briefs,** with fewer ceremony hits than no skill. Under the amended gates only G1 noise held it back; that is a post-hoc reading, not a verdict.
- **A sixth round tested a review mode for self-reflecting-chain,** cherry-picked from the old Cogito server ([audit](audits/2026-10-13-cogito-feature-audit.md), Amendment 4). It ran on drafts with planted flaws and was extended once. The edit caught more planted flaws (key rate 0.99, against 0.91 for the shipped text and 0.94 for no skill). But executors turned its delivery line into a heading, and the ceremony audit failed (5 hits against 2). Verdict REVERT. A second attempt ([r3](../evolution/gauntlet-2026-10-r3/LEDGER.md), Amendment 5) replaced the template with a description of what the reply must contain. That removed the template headings and improved proportionality (G1 5.83 against 5.00 for the shipped text), and the edit won the rankings 5–1 against no skill. But the ceremony audit still failed by one hit beyond tolerance (3 hits against 1, from closing summary sections), and calibration dipped (G3 4.83 against 5.67, noise by the gate). Verdict REVERT again, so the skill ships unchanged at 2.3.1.

### Earlier rounds

Several of these are NO ADOPTION verdicts that shipped by a disclosed owner decision, and each says so.

**integrated-reasoning (router).** One with-skill vs no-skill round was run on a frontier model, with 16 cells and sealed keys.
- **No measured lift in decision quality, and round 1 lost overall.** Detection and judged decision quality landed at exact parity, because the base model already reasoned at ceiling on the test briefs. The no-skill baseline won 5 of 6 blind forced choices, and the round-1 router regressed the proportionality guard (D5 −0.50) by narrating its scoring apparatus into answers.
- **The restraint fixtures passed.** The router deflated a trivial question, and the time-pressure fast-path opened an incident response with the rollback rather than analysis. (1.1.0 found that the v2.2 Direct Analysis threshold as written could never trigger, so the deflation came from the skill's general restraint guidance. The threshold fix shipped in 2.3.0, was reverted with that body in 1.2.0, and was re-applied on its own in 2.3.2 by owner decision.)
- **Round 2 fixed the leak and brought the router back to parity.** A backstage rule plus a mechanical leak scan eliminated the leaks (0 vs 9) and brought the guards back to statistical parity with no skill (D5 4.17 vs 4.50, total 28.25 vs 28.50). The gate still returned NO ADOPTION because planted-key detection came in at 93.8% vs 100%, so v2.2 ships by owner decision.

On strong models, treat the router as reasoning hygiene and restraint rather than a quality lift. Records are in [evolution/integrated-reasoning/](../evolution/integrated-reasoning/).

**The 1.1.0 format and bug pass was regression-tested** blind against 1.0.0 with Haiku and Sonnet. The gate returned NO ADOPTION: four rewritten skill bodies lost the blind comparison on both models. Those four bodies, plus two whose leaks rose without a preference win, stayed at their 1.0.0 text. Four other rewrites shipped by owner decision despite split or slightly negative cells (integrated-reasoning's leaks also rose 0 to 2). The reasoning-handover-protocol rewrite ships by owner decision, over a name-count check that penalises a hand-off for naming the next pattern. Record: [evolution/thinkbetter-suite/regression-2026-10-13/](../evolution/thinkbetter-suite/regression-2026-10-13/RESULTS.md). The October 2026 suite gauntlet later reverted all seven 1.1.0 rewrites to their v1.0.0 bodies (see above).

**premortem-evolved 2.2.0.** Each of these rounds beat the champion on totals and blind preference, and each was blocked by a regression guard:

- **Round 3 (Claude):** the v2.1 candidate won 12/12 blind forced choices and detected 97.2% of planted flaws versus the champion's 93.1%. It shipped as v2.1 by owner decision over a statistical-sufficiency line.
- **Kimi round 2:** the 2.2 deltas swept 6/6 forced choices, scored +2.06 on the total, and its `pre_delivery_check.py` linter closed the probability-honesty defect class completely. The gate still returned **NO ADOPTION** on two template-header leaks and a fatal-flaw label that flipped with framing.

2.2 ships by owner decision for the linter. The full record is in [evolution/premortem-evolved/](../evolution/premortem-evolved/).

**skill-gauntlet 1.1.0.** 1.1 merges the GitHub 1.0 line with three deltas that passed their own pre-registered gate (ADOPT): verifier-integrity hashing (`scripts/freeze.py`), degraded-mode gating, and held-in/held-out key splits. Record: [evolution/skill-gauntlet/](../evolution/skill-gauntlet/).
