# Changelog

The plugin version is set in `.claude-plugin/plugin.json`. Each skill's own version is `metadata.version` in its `SKILL.md`.

## 1.0.0 — 2026-10-13

This release brings the suite together in one repo, superseding `integrated-reasoning`, `premortem-skill` and `skill-gauntlet`.

- **integrated-reasoning suite 2.2.0** (router, nine patterns, `parallel-execution`, `reasoning-handover-protocol`): content identical to integrated-reasoning v2.2. Five descriptions that were invalid YAML (an unquoted `Example: "…"`) are now quoted. The strings themselves are unchanged.
- **premortem-evolved 2.2.0** is v2.1 plus four changes:
  - the calibration review becomes the last tripwire row;
  - `scripts/pre_delivery_check.py` is the mechanical pre-delivery scan (it checks for leaked machinery and template tokens, recomputes the probability ladder, and enumerates tied pairs);
  - the commitment ask stays in the conversation and off the page;
  - the budget wording is updated to match.

  Kimi round 2 returned NO ADOPTION (two template-header leaks and a framing label flip). 2.2 ships by owner decision for the linter, which closed the probability-honesty defect class. Markdown lost in that round's export has been restored.
- **skill-gauntlet 1.1.0** is a three-way merge of the GitHub 1.0 line (five operating rules, `normalize.py --strip-h2-ordinals`, scorecard fixes) with the 2026-08-22 cherry-pick that its own gate adopted: `scripts/freeze.py` verifier integrity, degraded-mode gating, and held-in/held-out key splits.
- **option-synthesis 1.0.0** is first published here. Its project-specific domain pack is not included.
