# Haiku uplift: summary

**Question:** does Haiku with a skill reach Sonnet without one?

**Answer: no, for every one of the 15 skills.** The pre-registered non-inferiority gate (value, keys and judge guards within 0.25 of Sonnet alone, audit, length, rankings) returned DOES NOT REACH for all 15. Two were settled only by the pre-registered extension: integrated-reasoning and tree-of-thoughts, each 0–6 on rankings after it.

| Mean over 15 skills | Value (1–7) | Keys caught |
|---|---|---|
| Sonnet with the skill | 6.18 | 95% |
| Sonnet alone | 5.86 | 93% |
| Haiku with the skill | 4.85 | 81% |
| Haiku alone | 4.79 | 81% |

- **The gap to Sonnet stays at about a point.** Haiku with the skill trails Sonnet alone by -1.02 on average and is behind on every skill; the closest is option-synthesis.
- **The skills barely move Haiku:** +0.05 on average, positive for 9 of 15. The best are option-synthesis, skill-gauntlet, adversarial-reasoning and integrated-reasoning; for analogical-transfer and self-reflecting-chain the skill made Haiku worse.
- **The skills lift Sonnet more:** +0.31 on average, positive for 14 of 15. The methods pay off in proportion to the model's ability to carry them out. They amplify a capable model; they do not stand in for one.
- **Ruling:** the owner extended only the two skills whose main question was open. The other skills' INCONCLUSIVE uplift comparisons stay INCONCLUSIVE; see the [ledger](LEDGER.md).

| Skill | Haiku+skill | Haiku | Sonnet+skill | Sonnet | Haiku+skill − Sonnet | Skill effect: Haiku | Skill effect: Sonnet |
|---|---|---|---|---|---|---|---|
| [hypothesis-elimination](hypothesis-elimination/scorecard.md) | 5.17 | 5.15 | 6.23 | 6.08 | -0.91 | +0.02 | +0.15 |
| [reasoning-handover-protocol](reasoning-handover-protocol/scorecard.md) | 4.58 | 4.67 | 6.00 | 5.79 | -1.21 | -0.09 | +0.21 |
| [integrated-reasoning](integrated-reasoning/scorecard.md) | 4.89 | 4.57 | 6.32 | 5.96 | -1.07 | +0.32 | +0.36 |
| [tree-of-thoughts](tree-of-thoughts/scorecard.md) | 5.17 | 5.05 | 6.42 | 5.78 | -0.61 | +0.12 | +0.64 |
| [breadth-of-thought](breadth-of-thought/scorecard.md) | 4.62 | 4.69 | 6.06 | 5.88 | -1.26 | -0.07 | +0.18 |
| [self-reflecting-chain](self-reflecting-chain/scorecard.md) | 5.02 | 5.42 | 6.35 | 5.83 | -0.81 | -0.40 | +0.52 |
| [parallel-execution](parallel-execution/scorecard.md) | 4.69 | 4.48 | 6.15 | 6.06 | -1.37 | +0.21 | +0.09 |
| [premortem-evolved](premortem-evolved/scorecard.md) | 4.83 | 4.75 | 6.15 | 5.77 | -0.94 | +0.08 | +0.38 |
| [adversarial-reasoning](adversarial-reasoning/scorecard.md) | 5.21 | 4.88 | 6.27 | 5.85 | -0.64 | +0.33 | +0.42 |
| [dialectical-reasoning](dialectical-reasoning/scorecard.md) | 4.56 | 4.81 | 6.06 | 5.83 | -1.27 | -0.25 | +0.23 |
| [analogical-transfer](analogical-transfer/scorecard.md) | 4.44 | 4.94 | 6.46 | 5.96 | -1.52 | -0.50 | +0.50 |
| [rapid-triage-reasoning](rapid-triage-reasoning/scorecard.md) | 4.88 | 5.02 | 6.06 | 6.10 | -1.22 | -0.14 | -0.04 |
| [negotiated-decision-framework](negotiated-decision-framework/scorecard.md) | 4.67 | 4.60 | 6.19 | 5.92 | -1.25 | +0.07 | +0.27 |
| [option-synthesis](option-synthesis/scorecard.md) | 5.00 | 4.25 | 5.75 | 5.17 | -0.17 | +0.75 | +0.58 |
| [skill-gauntlet](skill-gauntlet/scorecard.md) | 4.98 | 4.62 | 6.17 | 5.96 | -0.98 | +0.36 | +0.21 |

The design is in [docs/superpowers/specs/2026-10-13-haiku-uplift-design.md](../../docs/superpowers/specs/2026-10-13-haiku-uplift-design.md). Each skill folder holds its scorecard, research note and `reuse.json` provenance for the reused Sonnet replies.
