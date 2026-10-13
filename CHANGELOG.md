# Changelog

The plugin version is set in `.claude-plugin/plugin.json`. Each skill's own version is `metadata.version` in its `SKILL.md`.

## 1.2.1 — 2026-10-13

- **Arithmetic fixes, re-applied by owner decision.** The 1.2.0 reverts restored three bugs that 1.1.0 had fixed. Only those fixes are re-applied here, without a gauntlet round; they change numbers, not method.
  - **integrated-reasoning 2.3.2:** the Direct Analysis threshold is reachable and consistent (top pattern ≤ 4.0, no dimension ≥ 4, time pressure < 4), replacing two conflicting cut-offs (< 2.5 and < 4.0). The worked example now scores every pattern, and its recommendation quotes the right figures.
  - **tree-of-thoughts 2.3.2:** the confidence likelihood ratio is `2^((score - 10) / 10)`, so a 10/20 score is neutral and confidence no longer saturates at the 95% cap. The worked examples are recomputed.
  - **breadth-of-thought 2.3.2:** every confidence input is on a 0–100 scale, so the formula reaches its full range. Every branch count agrees with the others (33–45 through Level 1, at most 70 with Level 2, 10–15 viable solutions).
- **Every skill now carries `license: MIT`** in its frontmatter. This is a frontmatter-only change.
- **Docs:** the round-by-round validation history moved to [docs/VALIDATION.md](docs/VALIDATION.md), and the README keeps a short current status. A README sentence that claimed the router threshold fix was still shipping, after its revert in 1.2.0, is corrected. The follow-up gauntlet records (`evolution/gauntlet-2026-10-r2/`, no skill changes) are summarised there.

## 1.2.0 — 2026-10-13

The suite gauntlet: every skill went through a pre-registered, blind [skill-gauntlet](skills/skill-gauntlet/) round against answering with no skill. Sonnet executed, Opus judged, and a Sonnet auditor and key verifiers checked the replies. Seven rounds also compared the 1.1.0 rewrite with v1.0.0. **No skill validated, and every rewrite was reverted.** Verdicts were applied mechanically from gates frozen before each round. The record is in [evolution/gauntlet-2026-10/](evolution/gauntlet-2026-10/LEDGER.md), and the design is in the [spec](docs/superpowers/specs/2026-10-13-suite-gauntlet-design.md) (about 19.2M subagent tokens, pilot included).

- **Rewrites reverted to the v1.0.0 body.** Each keeps its 1.1.0 frontmatter and gets a patch bump:
  - integrated-reasoning 2.3.1 ([scorecard](evolution/gauntlet-2026-10/integrated-reasoning/scorecard.md))
  - tree-of-thoughts 2.3.1 ([scorecard](evolution/gauntlet-2026-10/tree-of-thoughts/scorecard.md))
  - breadth-of-thought 2.3.1 ([scorecard](evolution/gauntlet-2026-10/breadth-of-thought/scorecard.md)); `context: fork` and `argument-hint` are dropped, because the restored body takes no `$ARGUMENTS`
  - self-reflecting-chain 2.3.1 ([scorecard](evolution/gauntlet-2026-10/self-reflecting-chain/scorecard.md))
  - parallel-execution 2.3.1 ([scorecard](evolution/gauntlet-2026-10/parallel-execution/scorecard.md))
  - reasoning-handover-protocol 2.3.1 ([scorecard](evolution/gauntlet-2026-10/reasoning-handover-protocol/scorecard.md))
  - premortem-evolved 2.2.2 ([scorecard](evolution/gauntlet-2026-10/premortem-evolved/scorecard.md)): the SKILL.md body and reference revert, and `scripts/pre_delivery_check.py` keeps its tested 1.1.0 bug fixes, because no gauntlet cell can run scripts
- **Not validated against no skill, text unchanged:**
  - hypothesis-elimination ([scorecard](evolution/gauntlet-2026-10/hypothesis-elimination/scorecard.md))
  - adversarial-reasoning ([scorecard](evolution/gauntlet-2026-10/adversarial-reasoning/scorecard.md))
  - dialectical-reasoning ([scorecard](evolution/gauntlet-2026-10/dialectical-reasoning/scorecard.md))
  - analogical-transfer ([scorecard](evolution/gauntlet-2026-10/analogical-transfer/scorecard.md))
  - rapid-triage-reasoning ([scorecard](evolution/gauntlet-2026-10/rapid-triage-reasoning/scorecard.md))
  - negotiated-decision-framework ([scorecard](evolution/gauntlet-2026-10/negotiated-decision-framework/scorecard.md))
  - option-synthesis ([scorecard](evolution/gauntlet-2026-10/option-synthesis/scorecard.md))
  - skill-gauntlet ([scorecard](evolution/gauntlet-2026-10/skill-gauntlet/scorecard.md))
- **What the rounds found:**
  - The skill scored higher value than no skill on every brief in 10 of 15 rounds, and value cleared its noise band in 4.
  - What blocked validation was mostly visible method machinery (the ceremony audit failed in 10 rounds), extra length, and two framing flips (rapid-triage-reasoning, option-synthesis).
  - premortem-evolved and option-synthesis deliver structured reports, which the rubric's machinery guard penalises by design.
  - The README's validation section summarises the findings and the instrument's limits.
- **Rulings made during the program** are in the ledger: the breadth-of-thought frontmatter (round 5), the premortem-evolved script (round 8), and an auditor output normalisation that changed no scored value (round 14).

## 1.1.0 — 2026-10-13

A format and bug pass across the suite, checked by a pre-registered blind regression round (88 agents, Haiku and Sonnet). The full record is in [evolution/thinkbetter-suite/regression-2026-10-13/](evolution/thinkbetter-suite/regression-2026-10-13/RESULTS.md), and the line-by-line audit in [docs/audits/](docs/audits/2026-10-13-skill-format-audit.md). The round's gate returned **NO ADOPTION**: the new versions lost the blind preference test and leaked more. Which skills to revert was decided by the owner after the results: the four that lost on both models, and the two whose judged leaks rose without a preference win. Every other rewrite, and the handover rewrite, ships by owner decision; see the record for the cells each one lost.

- **All 15 skills:**
  - Frontmatter is cleaned up. `model: opus`, `agent` and `user-invocable` are gone (reasoning-handover-protocol keeps `user-invocable: false`, a deliberate non-default). `context: fork` is gone everywhere except breadth-of-thought, which now receives its problem through `$ARGUMENTS`.
  - Descriptions are rewritten in third person. They lead with what the skill does and when to use it, and name sibling skills in full instead of using acronyms.
  - In the triggering test the new descriptions scored 39/40 on both Haiku and Sonnet; the old ones scored 40/40 and 39/40. After the test, two descriptions (adversarial-reasoning, dialectical-reasoning) were reworded so they no longer contradict the 1.0.0 bodies they front.
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
- **premortem-evolved 2.2.1, skill-gauntlet 1.1.1, option-synthesis 1.0.1:** format and script fixes, with the methodology unchanged except one wording change in premortem-evolved's length-discipline sentence (it no longer lists stage and section numbers, which the script still checks).
  - `pre_delivery_check.py` and `normalize.py` handle `--help`; `pre_delivery_check.py` reports a missing report file without a traceback, and `normalize.py` prints usage when run with no arguments.
  - `pre_delivery_check.py` now also flags any bracketed text identical to a placeholder in the skill's own report template, and its word list tolerates plurals.
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
