# thinkbetter-skills

Reasoning skills for coding agents. The repo holds a scored router that picks the right reasoning method for a problem, nine reasoning-pattern skills, a premortem that stress-tests plans before launch, an option-synthesis skill for choosing between approaches, and a blind A/B harness for proving that a skill revision is actually better before you adopt it.

The skills are plain [Agent Skills](https://agentskills.io) (`skills/<name>/SKILL.md`), so they install into Claude Code, claude.ai, and any agent that reads that format.

## Install

**Claude Code (plugin).** Add the marketplace, then install the plugin:

```
/plugin marketplace add kimasplund/thinkbetter-skills
/plugin install thinkbetter@thinkbetter
```

Skills appear as `/thinkbetter:<skill>`, for example `/thinkbetter:premortem-evolved`, and Claude also invokes them on its own when a task matches. Updates arrive when the plugin version is bumped: run `/plugin marketplace update thinkbetter`, or turn on auto-update under `/plugin` → Marketplaces.

**Any agent (Codex, Kimi Code, Gemini CLI, Cursor, OpenCode, Copilot, Claude Code, and others).** Use the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add kimasplund/thinkbetter-skills                       # pick interactively
npx skills add kimasplund/thinkbetter-skills -s premortem-evolved  # one skill
npx skills add kimasplund/thinkbetter-skills -a codex -g           # all skills, one agent, global
```

**claude.ai and Claude Desktop.** Download `<skill>.zip` from the [latest release](https://github.com/kimasplund/thinkbetter-skills/releases/latest) and upload it under Settings → Capabilities → Skills. The zips carry only the spec frontmatter keys that claude.ai accepts.

**Manual.** Copy `skills/<name>/` into your agent's skills directory. Every skill directory is self-contained.

## Skills

| Skill | Version | The move | Validation |
|---|---|---|---|
| [integrated-reasoning](skills/integrated-reasoning/) | 2.3.1 | Scores the problem and routes it to the right pattern, or to a plain answer when no framework is warranted | Gauntlet 2026-10: not validated; rewrite reverted ([scorecard](evolution/gauntlet-2026-10/integrated-reasoning/scorecard.md)) |
| [tree-of-thoughts](skills/tree-of-thoughts/) | 2.3.1 | Deep branching exploration with pruning: find THE best option | Gauntlet 2026-10-r2: not validated; edit not adopted ([scorecard](evolution/gauntlet-2026-10-r2/tree-of-thoughts/scorecard.md)) |
| [breadth-of-thought](skills/breadth-of-thought/) | 2.3.1 | Wide sweep with conservative pruning: don't miss options | Gauntlet 2026-10: not validated; rewrite reverted ([scorecard](evolution/gauntlet-2026-10/breadth-of-thought/scorecard.md)) |
| [self-reflecting-chain](skills/self-reflecting-chain/) | 2.3.1 | Stepwise reasoning with per-step validation and backtracking | Gauntlet 2026-10: not validated; rewrite reverted ([scorecard](evolution/gauntlet-2026-10/self-reflecting-chain/scorecard.md)) |
| [hypothesis-elimination](skills/hypothesis-elimination/) | 2.2.1 | Discriminating-evidence elimination: find THE cause | Gauntlet 2026-10: not validated ([scorecard](evolution/gauntlet-2026-10/hypothesis-elimination/scorecard.md)) |
| [adversarial-reasoning](skills/adversarial-reasoning/) | 2.2.1 | Systematic attack on a candidate solution before committing | Gauntlet 2026-10-r2: not validated; edit not adopted ([scorecard](evolution/gauntlet-2026-10-r2/adversarial-reasoning/scorecard.md)) |
| [dialectical-reasoning](skills/dialectical-reasoning/) | 2.2.1 | Thesis, antithesis, synthesis, for trade-offs where both sides are right | Gauntlet 2026-10: not validated ([scorecard](evolution/gauntlet-2026-10/dialectical-reasoning/scorecard.md)) |
| [analogical-transfer](skills/analogical-transfer/) | 2.2.1 | Structured cross-domain borrowing for novel problems | Gauntlet 2026-10-r2: not validated; edit reverted ([scorecard](evolution/gauntlet-2026-10-r2/analogical-transfer/scorecard.md)) |
| [rapid-triage-reasoning](skills/rapid-triage-reasoning/) | 2.2.1 | Time-boxed, good-enough decisions for incidents | Gauntlet 2026-10-r2: not validated; edit reverted ([scorecard](evolution/gauntlet-2026-10-r2/rapid-triage-reasoning/scorecard.md)) |
| [negotiated-decision-framework](skills/negotiated-decision-framework/) | 2.2.1 | Multi-stakeholder alignment that needs real buy-in | Gauntlet 2026-10: not validated ([scorecard](evolution/gauntlet-2026-10/negotiated-decision-framework/scorecard.md)) |
| [parallel-execution](skills/parallel-execution/) | 2.3.1 | Fan-out/fan-in for running patterns concurrently, with merge strategies | Gauntlet 2026-10: not validated; rewrite reverted ([scorecard](evolution/gauntlet-2026-10/parallel-execution/scorecard.md)) |
| [reasoning-handover-protocol](skills/reasoning-handover-protocol/) | 2.3.1 | How to hand off state between reasoning skills, with an optional `.reasoning/` folder | Gauntlet 2026-10: not validated; rewrite reverted ([scorecard](evolution/gauntlet-2026-10/reasoning-handover-protocol/scorecard.md)) |
| [premortem-evolved](skills/premortem-evolved/) | 2.2.2 | Assumes the plan already failed, reasons back to why, then rebuilds it | Gauntlet 2026-10: not validated; rewrite reverted ([scorecard](evolution/gauntlet-2026-10/premortem-evolved/scorecard.md)) |
| [option-synthesis](skills/option-synthesis/) | 1.0.1 | Pre-registers what a choice must satisfy, generates a wide field, kills finalists with premortems, synthesizes the winner | Gauntlet 2026-10: not validated ([scorecard](evolution/gauntlet-2026-10/option-synthesis/scorecard.md)) |
| [skill-gauntlet](skills/skill-gauntlet/) | 1.1.1 | Pre-registered, blind, regression-guarded A/B evaluation of skills, prompts and agent configs | Gauntlet 2026-10: not validated ([scorecard](evolution/gauntlet-2026-10/skill-gauntlet/scorecard.md)) |

## Validation status: read this before relying on a skill

**No skill in this repo is validated.** In October 2026 each of the 15 skills went through a pre-registered, blind [skill-gauntlet](skills/skill-gauntlet/) round against answering with no skill, and none passed. Treat each skill as a documented methodology, not a proven improvement. Per-skill verdicts, scorecards, research notes and every ruling are in the [ledger](evolution/gauntlet-2026-10/LEDGER.md).

### Suite gauntlet, October 2026

- **Design.** Each round had three fictional briefs with planted keys sealed from the coordinator, a hype/skeptical framing pair of the same facts, and a task too small for the skill. Sonnet answered each brief twice per arm, or four times after the one allowed extension. Two Opus judges per brief scored the blinded replies on four value and three guard dimensions and ranked them. A Sonnet auditor counted visible method machinery, and Sonnet verifiers checked the planted keys. A skill validates only if every condition passes: value above the paired noise band, no guard regression, no extra method ceremony, and the same recommendation under both framings. Each round's gate was frozen before it ran. Design: [spec](docs/superpowers/specs/2026-10-13-suite-gauntlet-design.md).
- **Rewrites.** Seven skills had a 1.1.0 body that differed from 1.0.0, so their rounds added a third arm. Every one of those rewrites lost to or tied v1.0.0 and was reverted to the v1.0.0 body, keeping the 1.1.0 frontmatter (now 2.3.1, or 2.2.2 for premortem-evolved). The restored bodies were compared with the rewrites, not with no skill.
- **Where the skills helped.** The skill arm scored higher value than no skill on every brief in 10 of 15 rounds, and won at least 5 of 6 blind rankings in 7. Value cleared its noise band in 4: tree-of-thoughts (the reverted 1.1.0 body), analogical-transfer, negotiated-decision-framework and option-synthesis.
- **What blocked them.** Mostly visible method. The ceremony audit failed in 10 of 15 rounds, and several skills made replies longer than the judges thought the task needed. rapid-triage-reasoning and option-synthesis changed their recommendation between the hype and skeptical framings of the same facts. premortem-evolved and option-synthesis deliver a structured report by design, which the rubric's machinery and length guards penalise, and both failed those guards decisively.
- **Limits of the instrument.** The audit band is strict: one extra hit in total fails, and each research note gives the tolerant reading where that mattered. The value band is the spread of the per-brief gains, so a gain that is positive on every brief but uneven can read as noise (adversarial-reasoning: +0.72, every brief positive, band 1.06). Executors were Sonnet only. The rubric scores every reply as a general answer, not as a report artifact.

### Earlier rounds

Several of these are NO ADOPTION verdicts that shipped by a disclosed owner decision, and each says so.

**integrated-reasoning (router).** One with-skill vs no-skill round was run on a frontier model, with 16 cells and sealed keys.
- **No measured lift in decision quality, and round 1 lost overall.** Detection and judged decision quality landed at exact parity, because the base model already reasoned at ceiling on the test briefs. The no-skill baseline won 5 of 6 blind forced choices, and the round-1 router regressed the proportionality guard (D5 −0.50) by narrating its scoring apparatus into answers.
- **The restraint fixtures passed.** The router deflated a trivial question, and the time-pressure fast-path opened an incident response with the rollback rather than analysis. (1.1.0 found that the v2.2 Direct Analysis threshold as written could never trigger, so the deflation came from the skill's general restraint guidance; the threshold is fixed in 2.3.0.)
- **Round 2 fixed the leak and brought the router back to parity.** A backstage rule plus a mechanical leak scan eliminated the leaks (0 vs 9) and brought the guards back to statistical parity with no skill (D5 4.17 vs 4.50, total 28.25 vs 28.50). The gate still returned NO ADOPTION because planted-key detection came in at 93.8% vs 100%, so v2.2 ships by owner decision.

On strong models, treat the router as reasoning hygiene and restraint rather than a quality lift. Records are in [evolution/integrated-reasoning/](evolution/integrated-reasoning/).

**The 1.1.0 format and bug pass was regression-tested** blind against 1.0.0 with Haiku and Sonnet. The gate returned NO ADOPTION: four rewritten skill bodies lost the blind comparison on both models. Those four bodies, plus two whose leaks rose without a preference win, stayed at their 1.0.0 text. Four other rewrites shipped by owner decision despite split or slightly negative cells (integrated-reasoning's leaks also rose 0 to 2). The reasoning-handover-protocol rewrite ships by owner decision, over a name-count check that penalises a hand-off for naming the next pattern. Record: [evolution/thinkbetter-suite/regression-2026-10-13/](evolution/thinkbetter-suite/regression-2026-10-13/RESULTS.md). The October 2026 suite gauntlet later reverted all seven 1.1.0 rewrites to their v1.0.0 bodies (see above).

**premortem-evolved 2.2.0.** Each of these rounds beat the champion on totals and blind preference, and each was blocked by a regression guard:

- **Round 3 (Claude):** the v2.1 candidate won 12/12 blind forced choices and detected 97.2% of planted flaws versus the champion's 93.1%. It shipped as v2.1 by owner decision over a statistical-sufficiency line.
- **Kimi round 2:** the 2.2 deltas swept 6/6 forced choices, scored +2.06 on the total, and its `pre_delivery_check.py` linter closed the probability-honesty defect class completely. The gate still returned **NO ADOPTION** on two template-header leaks and a fatal-flaw label that flipped with framing.

2.2 ships by owner decision for the linter. The full record is in [evolution/premortem-evolved/](evolution/premortem-evolved/).

**skill-gauntlet 1.1.0.** 1.1 merges the GitHub 1.0 line with three deltas that passed their own pre-registered gate (ADOPT): verifier-integrity hashing (`scripts/freeze.py`), degraded-mode gating, and held-in/held-out key splits. Record: [evolution/skill-gauntlet/](evolution/skill-gauntlet/).

## Provenance

This repo supersedes three single-skill repos, which keep their original histories:

- [kimasplund/integrated-reasoning](https://github.com/kimasplund/integrated-reasoning)
- [kimasplund/premortem-skill](https://github.com/kimasplund/premortem-skill)
- [kimasplund/skill-gauntlet](https://github.com/kimasplund/skill-gauntlet)

Earlier copies of the reasoning suite lived in [claude_cognitive_reasoning](https://github.com/kimasplund/claude_cognitive_reasoning). Validation records live in [evolution/](evolution/), and example premortem reports in [examples/](examples/). See [CHANGELOG.md](CHANGELOG.md) for versions.

## Development

```bash
git config core.hooksPath .githooks         # once per clone: validator + tests run before every push
python3 -m unittest discover -s tests       # script tests
python3 scripts/validate_skills.py          # spec + privacy checks (needs PyYAML)
claude plugin validate . --strict           # marketplace manifest
claude plugin validate .claude-plugin/plugin.json --strict
claude plugin validate ./skills --strict
python3 scripts/build_zips.py               # dist/<skill>.zip for claude.ai
scripts/link_local.sh                       # symlink skills into ~/.claude/skills
```

Rules for changing a skill are in [.claude/CLAUDE.md](.claude/CLAUDE.md).

## License

[MIT](LICENSE)
