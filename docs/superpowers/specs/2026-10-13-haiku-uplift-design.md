# Haiku uplift: does Haiku with a skill reach Sonnet without one?

Owner request, 2026-10-13. The October gauntlet ran every skill on Sonnet. This program asks whether a skill lets the smaller, cheaper model match the bigger one, across all 15 skills.

## Design

- **Arms, judged together in one blind panel per brief:** `hs` Haiku with the skill, `hn` Haiku alone, `ss` Sonnet with the skill, `sn` Sonnet alone. 3 briefs × 4 arms × 2 runs = 24 main cells per skill. There are no framing or negative fixtures, because the question is capability, not robustness.
- **Packs and reused replies:** each skill reuses the sealed pack of its latest round. October covers ten skills; the follow-up r2 covers analogical-transfer, negotiated-decision-framework and rapid-triage-reasoning, whose briefs are fresher. `sn` always reuses that round's no-skill replies, runs 1–2. `ss` reuses that round's replies from the arm whose text is the shipped text; the label is recorded in `skills.json`. Three skills get fresh `ss` runs because 1.2.1 changed their numbers: integrated-reasoning, tree-of-thoughts and breadth-of-thought. The shipped texts also gained a `license: MIT` frontmatter line after the reused replies were made; it is ignored. Reuse is recorded per cell in `reuse.json`, and reused replies are frozen with the pack.
- **Same instruments as the 2026-10 programs:** two Opus judges, a Sonnet auditor with the quote check, and Sonnet key verifiers. The rubric and executor prompts are unchanged.
- **Gates (binding text in `harness/PREREG-TEMPLATE.md`):**
  - **Reaches Sonnet:** `hs` vs `sn` is non-inferior. Value, keys and each judge guard are at most 0.25 below (0.10 for keys); at most one more audit hit; at most 2.0× the length; no clear ranking loss.
  - **Haiku uplift and Sonnet uplift:** `hs` vs `hn` and `ss` vs `sn` under the Amendment 3 validation gate, without the framing and negative conditions.
  - One extension on INCONCLUSIVE, then the conservative reading.
- **What follows:** no skill text changes. Results go into the README and `docs/VALIDATION.md`.

## Harness

`evolution/haiku-uplift-2026-10/harness` is a copy of the r2 harness. It adds per-arm executor models, reused arms (copied at build and at extension), main-only cells, the `reaches_gate`, and an `apply` that changes no skill or README. Tests: `tests/test_haiku_uplift.py`.
