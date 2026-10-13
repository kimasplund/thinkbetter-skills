# Ledger: Haiku uplift (2026-10)

Does Haiku with a skill reach Sonnet without one? Four arms per skill in one blind panel: hs (Haiku with the skill), hn (Haiku alone), ss (Sonnet with the skill), sn (Sonnet alone).
Each skill reuses the sealed pack, and the Sonnet replies where the skill text is unchanged, of its latest round. Design: `docs/superpowers/specs/2026-10-13-haiku-uplift-design.md`. No skill text changes follow from this program.

| # | skill | state | reaches sonnet | haiku uplift | commit | subagent tokens |
|---|---|---|---|---|---|---|
| 1 | hypothesis-elimination | applied | DOES NOT REACH | INCONCLUSIVE |  |  |
| 2 | reasoning-handover-protocol | applied | DOES NOT REACH | NOT VALIDATED |  |  |
| 3 | integrated-reasoning | applied | DOES NOT REACH | NOT VALIDATED |  |  |
| 4 | tree-of-thoughts | applied | DOES NOT REACH | NOT VALIDATED |  |  |
| 5 | breadth-of-thought | applied | DOES NOT REACH | NOT VALIDATED |  |  |
| 6 | self-reflecting-chain | applied | DOES NOT REACH | INCONCLUSIVE |  |  |
| 7 | parallel-execution | applied | DOES NOT REACH | NOT VALIDATED |  |  |
| 8 | premortem-evolved | applied | DOES NOT REACH | NOT VALIDATED |  |  |
| 9 | adversarial-reasoning | applied | DOES NOT REACH | NOT VALIDATED |  |  |
| 10 | dialectical-reasoning | applied | DOES NOT REACH | NOT VALIDATED |  |  |
| 11 | analogical-transfer | applied | DOES NOT REACH | NOT VALIDATED |  |  |
| 12 | rapid-triage-reasoning | applied | DOES NOT REACH | INCONCLUSIVE |  |  |
| 13 | negotiated-decision-framework | applied | DOES NOT REACH | INCONCLUSIVE |  |  |
| 14 | option-synthesis | applied | DOES NOT REACH | NOT VALIDATED |  |  |
| 15 | skill-gauntlet | applied | DOES NOT REACH | INCONCLUSIVE |  |  |

## Rulings

- **Ruling (owner decision, after the first scoring):** the pre-registration gives every INCONCLUSIVE comparison an extension. The owner chose to extend only the two skills whose primary question was open (integrated-reasoning and tree-of-thoughts: Haiku with the skill vs Sonnet alone). The other skills keep their INCONCLUSIVE uplift comparisons (Haiku with vs without the skill, Sonnet with vs without), reported as INCONCLUSIVE without an extension. Nothing depends on those comparisons, and extending all twelve would have cost about 14M more subagent tokens. Each affected research note records the ruling.
