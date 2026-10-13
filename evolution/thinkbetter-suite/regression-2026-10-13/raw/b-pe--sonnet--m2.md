Here is the plan. Nothing has been run.

## Should this be parallel?

Yes. Each provider can be evaluated independently, so the six evaluations have no dependencies on each other. The merge strategy has to be fixed before fan-out (see below). Six sub-tasks falls in the 4-8 range, so I would use six background subagents. Agent teams are unnecessary because the workers never need to talk to each other.

**Assumptions** (you didn't say, so I'm assuming):
- The providers are named and you have rough workload requirements (compute, region, budget, compliance).
- Evaluation is research and analysis only, with no code edits, so worktree isolation isn't needed.

## Step 0: Define the shared contract (sequential, before fan-out)

Do this in the main session first. Without it the six verdicts can't be compared.

1. **Requirements sheet**: workload type, must-haves (regions, compliance, SLAs), budget ceiling, migration constraints.
2. **Scoring rubric**: the same 5-7 criteria for every worker, each scored 0-10 with a one-line evidence note:
   - cost at the target workload
   - performance and reliability (SLA, track record)
   - security and compliance
   - ecosystem and managed services
   - support quality
   - lock-in and exit cost
   - operational fit with your team
3. **Weights** for each criterion, agreed up front so they can't be bent after seeing results.
4. **Hard-fail gates** (for example, "must offer region X"). A provider that fails a gate is eliminated whatever its score.
5. **Output schema**: JSON or markdown with fixed fields: scores, evidence, confidence 0-1, gate results, top risks, unknowns.

## Step 1: Fan-out (parallel, Branch-Solve-Merge)

Spawn six subagents at once with `run_in_background: true`, one per provider. Each gets only the requirements sheet, rubric and schema for its own provider.

| Setting | Choice | Why |
|---|---|---|
| Model | sonnet | Data gathering and scoring against a rubric |
| Effort | medium | Reading docs and pricing pages doesn't need deep reasoning |
| Output path | `eval/provider-<name>.md` | Isolated paths so workers never share state |

Workers must cite sources for every score and mark anything they couldn't verify as "unknown", not guess. Each worker has a 30-minute timeout.

## Step 2: Validate verdicts (parallel, light)

Before merging, run a quick fact-check over each report. Spot-check pricing and SLA claims against the cited sources. This is where fabricated or stale numbers get caught. Use sonnet with high effort, since checking claims is more careful work than gathering them. Make it one checker per report, or one pass over all six if you want to save cost.

## Step 3: Fan-in and merge (sequential, main session)

This is the judgment stage, so use opus with high effort.

1. **Gate filter**: remove providers that failed a hard gate.
2. **Weighted aggregation**: compute weighted scores from the shared rubric. This is mechanical, so do it in a script, not with an agent.
3. **Confidence adjustment**: discount scores that rest on many "unknown" fields.
4. **Conflict resolution**: if the top two providers are within about 5% of each other, don't just pick the higher number. Use dialectical synthesis. Name what each wins on and decide which trade-off matters more for your workload.
5. **Sensitivity check**: re-run the ranking with the weights shifted +/-20%. If the winner changes, say so in the recommendation.

## Step 4: Deliverable

One recommendation document:
- the recommended provider and a runner-up
- a comparison table (provider x criterion)
- the main risks and the open unknowns
- what would change the recommendation (for example, "if egress costs exceed X")
- a confidence level

## Failure handling and anti-patterns avoided

- **A worker fails or times out**: retry once, then merge with five and flag the gap. Don't block the whole evaluation.
- **No shared rubric**: scores wouldn't be comparable, so the rubric is fixed first.
- **Shared state**: each worker writes only to its own file. Only the merge step reads all of them.
- **Scope**: six is a reasonable fan-out. More than about 10 would give diminishing returns.
- **Bias**: workers don't see each other's scores, which prevents anchoring.

## Rough timeline

Contract definition (about 10 min), then parallel fan-out and fact-check (bounded by the slowest worker, around 15-30 min), then merge (about 10 min). Running all six in sequence would take several times longer.

If you tell me the six providers and your workload, I can turn this into a concrete rubric and the six worker prompts.
