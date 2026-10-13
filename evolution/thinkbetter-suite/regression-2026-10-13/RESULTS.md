# Regression round, 2026-10-13: v1.0.0 vs the format and bug pass

## Method

The gate and the fixtures were pre-registered before any run. [PRE-REGISTRATION.md](PRE-REGISTRATION.md) and [fixtures/fixtures.json](fixtures/fixtures.json) are hash-locked in [fixtures.sha256](fixtures.sha256).

The arms were blind-coded `m1` and `m2`. The mapping is in [SEALED.json](SEALED.json): `m1` = new, `m2` = old.

The round used 88 agents:
- **Triggering:** 4 agents (Haiku and Sonnet, each run against both arms' catalogs).
- **Executors:** 56 agents, one per fixture × model × arm, all reading the skill body directly.
- **Judges:** 28 blind Sonnet judges, one per fixture × model. The A/B order alternated by index.

Judge rows are in [rows.json](rows.json). The scorer is [score.py](score.py), and its full output is in [scorecard.txt](scorecard.txt).

## Gate result: NO ADOPTION

| Gate | Result | Detail |
|---|---|---|
| G1 triggering | PASS | Haiku: old 40/40, new 39/40. Sonnet: 39/40 for both. |
| G2 preference | **FAIL** | The old version was preferred in 14 of 28 cells. Four skills lost on both models. |
| G3 leakage | **FAIL** | Mechanical scan: old 19, new 23. Judged: old 21, new 33. |
| G4 restraint | PASS | The trivial fixture deflated on both models. The urgent fixture opened with the action. |
| G5 quality guard | PASS | No cell dropped 3 or more quality points. |

## Per skill

| Skill | Preference (Haiku, Sonnet) | Quality old→new | Judged leaks old→new | Shipped in 1.1.0 |
|---|---|---|---|---|
| reasoning-handover-protocol | new, new | 10 → 15 | 16 → 10 | new (owner decision; see below) |
| integrated-reasoning (3 fixtures) | 4× new, tie, old | 50 → 51 | 0 → 2 | new |
| tree-of-thoughts | new, tie | 15 → 16 | 2 → 1 | new |
| breadth-of-thought | tie, old | 16 → 16 | 0 → 0 | new |
| self-reflecting-chain | new, old | 17 → 17 | 0 → 0 | new |
| parallel-execution | old, new | 16 → 15 | 3 → 2 | new |
| adversarial-reasoning | old, old | 18 → 15 | 0 → 7 | v1.0.0 body |
| dialectical-reasoning | old, old | 18 → 15 | 0 → 0 | v1.0.0 body |
| analogical-transfer | old, old | 16 → 15 | 0 → 1 | v1.0.0 body |
| rapid-triage-reasoning | old, old | 17 → 15 | 0 → 4 | v1.0.0 body |
| negotiated-decision-framework | new, old | 15 → 16 | 0 → 4 | v1.0.0 body |
| hypothesis-elimination | old, tie | 16 → 16 | 0 → 2 | v1.0.0 body |

## What we learned

The four skills that lost on both models were all rewritten by the same implementer.

**What went wrong:**
- **Exhaustive templates:** the new output templates and category lists made answers longer.
- **More ceremony:** answers carried decision-record scaffolding into an emergency, plus risk scores and every-category sweeps.

This is the failure the skills' own backstage rule exists to prevent. The lesson for future edits is that a format pass must not grow the output template.

## Owner decisions, made after the results were known

1. **Remedy for the six losing or leakier skills.** Their bodies return to v1.0.0 (the champion that won). The only change is the reworded `ultrathink` preamble line, one line per skill. They keep the modernized frontmatter and the new descriptions.
   - The descriptions passed G1.
   - The frontmatter keys don't change what the body instructs: the executors read the body directly, so these keys were never tested here. They do matter at runtime in Claude Code, where `context: fork` had hidden the conversation from the skill.
   - These skills ship as 2.2.1.
2. **reasoning-handover-protocol ships rewritten, by disclosed owner decision.**
   - **Strict gate:** the rewrite alone fails the mechanical G3 leg (11 → 17 name hits), so the strict reading would revert it.
   - **Why the mechanical count misleads here:** that scan counts skill names. A hand-off document must name the next pattern, and its own template requires a "pattern used" field.
   - **What the blind judges found:** on both models they rated the rewrite far better (quality 10 → 15) and less leaky (16 → 10).
   - **Instrument fix:** a future round should exempt the "pattern used" field when scanning hand-off fixtures.
3. **Gate after both decisions:** the gate is not re-run on the shipped mix. This record is the disclosure.
