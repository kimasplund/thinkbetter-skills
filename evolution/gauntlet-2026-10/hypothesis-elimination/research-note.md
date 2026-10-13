# Research note: hypothesis-elimination

- Validation (new vs none): **NOT VALIDATED**
- Agreement 0.97, freeze OK, extended True
- new: value 5.85, keys 0.969, ceremony 0.17, leaks 0.0, length x1.05, negative ok, framing True
- none: value 5.55, keys 0.969, ceremony 0.08, leaks 0.0, length x1.0, negative ok, framing None

## Autopsy

- **What drove the verdict:** the result was INCONCLUSIVE after 2 runs (value +0.60, band 0.75). The pre-registered extension narrowed it to value +0.30 (band 0.31), with the skill winning 4 rankings and losing 1. That stayed inside the band, so it resolved conservatively to NOT VALIDATED. The auditor also found one more ceremony hit in the skill arm (its candidate-cause tables), which the pre-registered one-hit rule counts as a FAIL.
- **Design vs compliance:** this is design, not a compliance failure. On Sonnet, the skill's structured elimination adds a little value, about 5% length (×1.05) and some table ceremony. Without the skill, Sonnet already finds the planted causes: keys were 0.97 in both arms, even after Amendment 2 made the keys harder.
- **Not chased:**
  - The key ceiling on diagnosis tasks.
  - Whether a weaker executor (for example Haiku) gains more from the skill. That is out of scope; Sonnet is the pre-registered executor.
- **Owner decision (2026-10-13):** the harness was accepted as fit for the remaining rounds, even though the literal reading of the pilot fitness check failed on this final scorecard. That check confuses a small real skill effect with an instrument that cannot discriminate. Agreement (0.97), the seal, and strict validation all worked.
