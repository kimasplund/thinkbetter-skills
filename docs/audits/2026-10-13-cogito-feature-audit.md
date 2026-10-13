# Cogito feature audit (2026-10-13)

Did the move from the old Cogito reasoning MCP server to these skills lose any functionality? **No.** Every Cogito version scored text the caller had already written, using keyword heuristics, and never called a model. Much of the v2 pattern code was simulated. Everything Cogito did for real is covered, usually more fully, by the 15 skills. What it had that the skills lack is a few method ideas, and the two most useful are being cherry-picked.

## What was audited

Each copy was checked by a separate audit. Every capability was listed with file evidence, marked implemented or only described, and compared with the skills.

| Copy (under `~/projects/`) | Date | Capabilities checked | Covered / partial / missing / server-only |
|---|---|---|---|
| `mcp-servers-dev/mcp-cogito` (latest, v0.3.2, with the v2 code and the 2.0 vision) | Jul 2025 | 58 | 23 / 12 / 7 / 16 |
| `mcp-servers-dev/cogito-claude-dev` | Apr 2025 | 40 | 14 / 6 / 2 / 18 |
| `mcp-servers-dev/cogito-playground` (five development copies) | Apr 2025 | 32 | 17 / 1 / 7 / 7 |
| `n8n/cogito-nexus` (n8n nodes and pattern blueprints) | May 2025 | 45 | 15 / 12 / 7 / 11 |

**Server-only:** semantic caching, batch jobs, metrics, logging, config and the MCP tool surface (`sequentialthinking`, `batchthinking`, `getBatchStatus` and others). These have no equivalent in a skill and need none.

**Promised but never built:** retries, persisted caches, revision flags and the "batches up to 100" claim were described in the Cogito READMEs and plans, but no code implemented them.

## Method ideas the skills lack

| Idea | Found in | State in Cogito | In the skills |
|---|---|---|---|
| Critique-and-revise loop on a finished draft (up to 3 passes, stop at a confidence threshold) | all four | Implemented as a heuristic | Partial: self-reflecting-chain only reflects while building a chain |
| Circular-reasoning check | all four | Keyword heuristic | Missing |
| Named-bias scan with mitigations | mcp-cogito v2, cogito-nexus | Code (v2), keyword rules (nexus) | Missing: only confirmation bias, in hypothesis-elimination |
| Checks that a chain stays on the original question; contradiction scan | cogito-claude-dev, playground, mcp-cogito v2 | Heuristic code | Missing or partial |
| Counterfactual ("what if the opposite") probe | mcp-cogito, cogito-nexus | Prototype or plan only | Missing |
| Confidence ranges instead of a single figure | mcp-cogito v2, cogito-nexus | Partly simulated | Partial |
| Switching pattern mid-run when confidence stalls | cogito-nexus | Recommends only | Partial: integrated-reasoning has time checkpoints |
| Breadth-of-thought extras (exploration scaled to complexity; legal, financial and environmental lenses) | cogito-nexus, cogito-claude-dev | Implemented | Partial |
| Learning across runs | mcp-cogito v2, cogito-nexus | In memory only or unwired | Not applicable: skill-gauntlet is the deliberate version |

## Cherry-picked

The first five ideas are one capability: checking a finished answer for flawed reasoning. They are added to self-reflecting-chain:

- a review mode that runs up to three critique-and-revise passes with a stop rule;
- a backstage checklist covering circular reasoning, named biases, contradictions, drift from the question, and the counterfactual probe.

Following the gauntlet's lesson that visible method costs a skill, the checks were meant to stay out of the reply. The change would ship only if its pre-registered round kept it.

**Outcome: not adopted.** Round 6 of the follow-up program ([scorecard](../../evolution/gauntlet-2026-10-r2/self-reflecting-chain/scorecard.md), [ledger](../../evolution/gauntlet-2026-10-r2/LEDGER.md)) returned REVERT after one extension. The review mode found more of the planted flaws (key rate 0.99, against 0.91 for the shipped text and 0.94 for no skill). But executors turned its "issues that changed the conclusion" delivery line into a heading, and the ceremony audit failed (5 hits against 2). self-reflecting-chain ships unchanged at 2.3.1. The candidate text stays in the history of branch `cogito-cherrypick` (commit `e78eb5d`) for a later attempt without a delivery template.
