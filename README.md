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
| [integrated-reasoning](skills/integrated-reasoning/) | 2.3.2 | Scores the problem and routes it to the right pattern, or to a plain answer when no framework is warranted | Gauntlet 2026-10: not validated; rewrite reverted ([scorecard](evolution/gauntlet-2026-10/integrated-reasoning/scorecard.md)) |
| [tree-of-thoughts](skills/tree-of-thoughts/) | 2.3.2 | Deep branching exploration with pruning: find THE best option | Gauntlet 2026-10: not validated; rewrite reverted ([scorecard](evolution/gauntlet-2026-10/tree-of-thoughts/scorecard.md)); follow-up edit not adopted ([r2](evolution/gauntlet-2026-10-r2/tree-of-thoughts/scorecard.md)) |
| [breadth-of-thought](skills/breadth-of-thought/) | 2.3.2 | Wide sweep with conservative pruning: don't miss options | Gauntlet 2026-10: not validated; rewrite reverted ([scorecard](evolution/gauntlet-2026-10/breadth-of-thought/scorecard.md)) |
| [self-reflecting-chain](skills/self-reflecting-chain/) | 2.3.1 | Stepwise reasoning with per-step validation and backtracking | Gauntlet 2026-10: not validated; rewrite reverted ([scorecard](evolution/gauntlet-2026-10/self-reflecting-chain/scorecard.md)) |
| [hypothesis-elimination](skills/hypothesis-elimination/) | 2.2.1 | Discriminating-evidence elimination: find THE cause | Gauntlet 2026-10: not validated ([scorecard](evolution/gauntlet-2026-10/hypothesis-elimination/scorecard.md)) |
| [adversarial-reasoning](skills/adversarial-reasoning/) | 2.2.1 | Systematic attack on a candidate solution before committing | Gauntlet 2026-10: not validated ([scorecard](evolution/gauntlet-2026-10/adversarial-reasoning/scorecard.md)); follow-up edit not adopted ([r2](evolution/gauntlet-2026-10-r2/adversarial-reasoning/scorecard.md)) |
| [dialectical-reasoning](skills/dialectical-reasoning/) | 2.2.1 | Thesis, antithesis, synthesis, for trade-offs where both sides are right | Gauntlet 2026-10: not validated ([scorecard](evolution/gauntlet-2026-10/dialectical-reasoning/scorecard.md)) |
| [analogical-transfer](skills/analogical-transfer/) | 2.2.1 | Structured cross-domain borrowing for novel problems | Gauntlet 2026-10: not validated ([scorecard](evolution/gauntlet-2026-10/analogical-transfer/scorecard.md)); follow-up edit not adopted ([r2](evolution/gauntlet-2026-10-r2/analogical-transfer/scorecard.md)) |
| [rapid-triage-reasoning](skills/rapid-triage-reasoning/) | 2.2.1 | Time-boxed, good-enough decisions for incidents | Gauntlet 2026-10: not validated ([scorecard](evolution/gauntlet-2026-10/rapid-triage-reasoning/scorecard.md)); follow-up edit not adopted ([r2](evolution/gauntlet-2026-10-r2/rapid-triage-reasoning/scorecard.md)) |
| [negotiated-decision-framework](skills/negotiated-decision-framework/) | 2.2.1 | Multi-stakeholder alignment that needs real buy-in | Gauntlet 2026-10: not validated ([scorecard](evolution/gauntlet-2026-10/negotiated-decision-framework/scorecard.md)); follow-up edit not adopted ([r2](evolution/gauntlet-2026-10-r2/negotiated-decision-framework/scorecard.md)) |
| [parallel-execution](skills/parallel-execution/) | 2.3.1 | Fan-out/fan-in for running patterns concurrently, with merge strategies | Gauntlet 2026-10: not validated; rewrite reverted ([scorecard](evolution/gauntlet-2026-10/parallel-execution/scorecard.md)) |
| [reasoning-handover-protocol](skills/reasoning-handover-protocol/) | 2.3.1 | How to hand off state between reasoning skills, with an optional `.reasoning/` folder | Gauntlet 2026-10: not validated; rewrite reverted ([scorecard](evolution/gauntlet-2026-10/reasoning-handover-protocol/scorecard.md)) |
| [premortem-evolved](skills/premortem-evolved/) | 2.2.2 | Assumes the plan already failed, reasons back to why, then rebuilds it | Gauntlet 2026-10: not validated; rewrite reverted ([scorecard](evolution/gauntlet-2026-10/premortem-evolved/scorecard.md)) |
| [option-synthesis](skills/option-synthesis/) | 1.0.1 | Pre-registers what a choice must satisfy, generates a wide field, kills finalists with premortems, synthesizes the winner | Gauntlet 2026-10: not validated ([scorecard](evolution/gauntlet-2026-10/option-synthesis/scorecard.md)) |
| [skill-gauntlet](skills/skill-gauntlet/) | 1.1.1 | Pre-registered, blind, regression-guarded A/B evaluation of skills, prompts and agent configs | Gauntlet 2026-10: not validated ([scorecard](evolution/gauntlet-2026-10/skill-gauntlet/scorecard.md)) |

## Validation status: read this before relying on a skill

**No skill in this repo is validated.** In October 2026 each of the 15 skills went through a pre-registered, blind [skill-gauntlet](skills/skill-gauntlet/) round against answering with no skill, and none passed. Treat each skill as a documented methodology, not a proven improvement.

- **Where they helped:** the skill scored higher than no skill on every brief in 10 of 15 rounds, and the gain cleared its noise band in 4.
- **What blocked validation:**
  - visible method (scaffolding and headings the reader didn't need) and extra length;
  - recommendations that changed when the same facts were framed hopefully or doubtfully.

  premortem-evolved and option-synthesis deliver structured reports, which the rubric's machinery guard penalises by design.
- **Follow-up:** five skills got a targeted edit and a fresh round under amended gates. None was adopted, so all five ship unchanged.
- **Owner decisions:** some versions ship over a NO ADOPTION verdict or with fixes made outside a round. 1.2.1 re-applies three arithmetic fixes that a revert had undone. Each owner decision is disclosed in the [CHANGELOG](CHANGELOG.md).

The full record, with design, per-round findings, the instrument's limits and earlier rounds, is in [docs/VALIDATION.md](docs/VALIDATION.md). Per-skill scorecards are in the [October ledger](evolution/gauntlet-2026-10/LEDGER.md) and the [follow-up ledger](evolution/gauntlet-2026-10-r2/LEDGER.md).

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
