# Follow-up review of the most promising skills

This is a post-hoc, non-binding review written after the program closed. The recorded verdicts stand. Its job is to separate real skill gains from instrument artifacts, and to name the smallest fix worth a fresh pre-registered round. Each skill has a full report in this folder.

## Per skill

| Skill | Gain real? | What blocked it | Smallest fix | Odds (fix beats current / validates vs none) |
|---|---|---|---|---|
| [tree-of-thoughts](tree-of-thoughts.md) (shipped v1.0.0 body) | **Real.** +1.06 vs no skill on every brief, 6–0 rankings; about +0.82 survives a length control | Its one ceremony hit was an auditor misattribution (corrected: 0 vs 1). G1 NOISE, mostly length, plus restatement driven by the synthesis template | An "answer shape" paragraph: lead with the recommendation, give each rejected option its reason once, no recaps | — / 25–35% (10–15% as-is) |
| [adversarial-reasoning](adversarial-reasoning.md) | **Real, modest.** 6–0, within-brief permutation p ≈ 0.0002, every brief positive in both halves | Value NOISE is an instrument artifact: the band rule is non-monotone (a smaller brief-2 gain would have passed). G2 NOISE is one judge docking one `## Confidence` heading | Fold the Confidence heading into residual risk as plain words | — / 12–18% under the current gate, about 45% with the sign rule below |
| [analogical-transfer](analogical-transfer.md) | **Real in direction, size soft.** Part of the soundness gain comes from arithmetic slips in no-skill replies | Ceremony is a skill defect: the template asks for a title, a "Problem Abstraction" section and a confidence close. G1 is mostly a zero-band artifact | About 11 lines: open with the answer, no abstraction section, no mapping labels, "Where I could be wrong" carries new information only | about 65% / about 30% |
| [negotiated-decision-framework](negotiated-decision-framework.md) | **Partly.** True effect is about +0.3; the +0.50 came mostly from weak no-skill replies in the extension | G1 is a skill defect: two stakeholder tables restate each other. G2 is a mild defect: a Confidence line and an agreement section. Ceremony is mostly noise | About 15 lines: one "can block or must act" table, no duplicate sections, "What would change this" replaces the Confidence line | 55–60% / about 25% |
| [rapid-triage-reasoning](rapid-triage-reasoning.md) | **Real, modest.** 6–0, V3 and G3 better on every brief | The framing flip is a genuine but narrow defect: the skeptical reply called an irreversible refund reversible, and guessed against a checkable fact. The fixture also broke its own rule: the skeptical framing added a co-producer who wants to cancel | About 9 lines: decide on the facts with the requester's tone set aside, judge reversibility by the action, and when a checkable fact decides, recommend the reversible step now with a named check and cutoff | 35–40% / 20–25% (framing holds about 70%) |

## Instrument findings across all 15 rounds

1. **The auditor sometimes credits a quote to the wrong reply.** Checking every quote against the blinded reply it was credited to found two cross-arm misattributions:
   - **tree-of-thoughts:** the brief-3 attributions are shifted by one slot.
   - **hypothesis-elimination:** "Bottom line for the board" was credited to a skill reply but sits in a no-skill reply.

   No recorded verdict changes, because each affected round also fails on other conditions. But under the strict rule a single hit decides a guard, so the harness needs a quote check before scoring.
2. **The value band is non-monotone.** It is the max−min spread of the per-brief gains, so a larger gain on one brief can turn PASS into NOISE. adversarial-reasoning had +0.72 with every brief positive and a band of 1.06; before the extension it had passed.
3. **Identical per-brief differences give a band of zero,** so any drop on a guard fails. analogical-transfer was −0.25 on G1 on every brief.
4. **The framing pair runs only on the skill arm,** so a baseline's framing sensitivity is unknown. One fixture also added a fact that isn't in brief-1 (rapid-triage-reasoning).
5. **The restored v1.0.0 bodies were never gated against no skill.** A post-hoc application of the same gate, old vs none, gives:
   - **tree-of-thoughts:** +1.06 and 6–0. With the corrected ceremony count only G1 NOISE remains, so it would have earned an extension.
   - **breadth-of-thought:** +0.48 and 6–0, INCONCLUSIVE.
   - **parallel-execution:** +0.22, INCONCLUSIVE.
   - **The others:** NOT VALIDATED.
