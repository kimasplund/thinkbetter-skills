# Changelog

The plugin version is set in `.claude-plugin/plugin.json`. Each skill's own version is `metadata.version` in its `SKILL.md`.

## 1.1.0 — 2026-10-13

A format and bug pass across the suite, checked by a pre-registered blind regression round (88 agents, Haiku and Sonnet). The full record is in [evolution/thinkbetter-suite/regression-2026-10-13/](evolution/thinkbetter-suite/regression-2026-10-13/RESULTS.md), and the line-by-line audit in [docs/audits/](docs/audits/2026-10-13-skill-format-audit.md). The round's gate returned **NO ADOPTION**: the new versions lost the blind preference test and leaked more. The skills that regressed were therefore reverted, and one rewrite ships by owner decision.

- **All 15 skills:**
  - Frontmatter is cleaned up. `model: opus`, `agent` and `user-invocable` are gone, along with `context: fork`, except in breadth-of-thought, which now receives its problem through `$ARGUMENTS`.
  - Descriptions are rewritten in third person. They lead with what the skill does and when to use it, and name sibling skills in full instead of using acronyms.
  - The new descriptions route as well as the old ones (triggering test: 39 to 40 out of 40 on Haiku and Sonnet).
- **New bodies (2.3.0):**
  - **integrated-reasoning:** cut to under 500 lines, with sections moved into linked references. The Direct Analysis threshold is now the one the formulas can actually reach, and the worked example recomputes.
  - **tree-of-thoughts:** the confidence formula no longer saturates at the cap.
  - **breadth-of-thought:** the confidence formula can reach its full range, and the branch counts agree with each other.
  - **self-reflecting-chain:** a single confidence gate.
  - **parallel-execution:** uses the current Agent-tool vocabulary.
  - All of these drop stale names: "Task tool", TodoWrite, `ultrathink` and IR-v2.
- **reasoning-handover-protocol 2.3.0** is rewritten from a 1,217-line spec for an orchestrator that doesn't exist into a 116-line guide.
  - Blind judges preferred it on both models (quality 10 to 15).
  - It ships by **owner decision** over the gate's mechanical name-count leg, which penalises a hand-off for naming the next pattern.
- **Champion bodies kept (2.2.1):** adversarial-reasoning, dialectical-reasoning, analogical-transfer, rapid-triage-reasoning, negotiated-decision-framework and hypothesis-elimination.
  - Their rewrites lost the blind comparison or leaked more method machinery, so the v1.0.0 bodies stay. Only the `ultrathink` line is reworded.
  - The new frontmatter and descriptions do apply.
- **premortem-evolved 2.2.1, skill-gauntlet 1.1.1, option-synthesis 1.0.1:** format and script fixes only, with the methodology unchanged.
  - `pre_delivery_check.py` and `normalize.py` handle `--help` and missing input.
  - `normalize.py` now honours its documented flat mapping, which it used to ignore silently.
  - `pre_delivery_check.py`'s template-token check matches whole words only.
  - Code fences are fixed, and the stale option-synthesis footer is removed.
  - The script fixes are covered by `tests/test_skill_scripts.py`.

## 1.0.0 — 2026-10-13

This release brings the suite together in one repo, superseding `integrated-reasoning`, `premortem-skill` and `skill-gauntlet`.

- **integrated-reasoning suite 2.2.0** (router, nine patterns, `parallel-execution`, `reasoning-handover-protocol`): content identical to integrated-reasoning v2.2. Five descriptions that were invalid YAML (an unquoted `Example: "…"`) are now quoted. The strings themselves are unchanged. The reference links in `breadth-of-thought` and `tree-of-thoughts` pointed at `~/.claude/skills/...`, which doesn't exist on plugin, npx or claude.ai installs; they are now relative links, and breadth-of-thought's now names the right file.
- **premortem-evolved 2.2.0** is v2.1 plus four changes:
  - the calibration review becomes the last tripwire row;
  - `scripts/pre_delivery_check.py` is the mechanical pre-delivery scan (it checks for leaked machinery and template tokens, recomputes the probability ladder, and enumerates tied pairs);
  - the commitment ask stays in the conversation and off the page;
  - the budget wording is updated to match.

  Kimi round 2 returned NO ADOPTION (two template-header leaks and a framing label flip). 2.2 ships by owner decision for the linter, which closed the probability-honesty defect class. Markdown lost in that round's export has been restored.
- **skill-gauntlet 1.1.0** is a three-way merge of the GitHub 1.0 line (five operating rules, `normalize.py --strip-h2-ordinals`, scorecard fixes) with the 2026-08-22 cherry-pick that its own gate adopted: `scripts/freeze.py` verifier integrity, degraded-mode gating, and held-in/held-out key splits.
- **option-synthesis 1.0.0** is first published here. Its project-specific domain pack is not included, and the claude.ai authoring metadata is dropped from its frontmatter.
