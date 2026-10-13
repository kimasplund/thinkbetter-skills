## Plan: evaluating six hosting providers in parallel

**Assumptions:** I don't know your workload, so I'm assuming a typical web app with a database. Budget, region and compliance needs are unspecified, so they become inputs to step 1. If subagents aren't available, the same structure runs sequentially.

**Why parallel works here:** Evaluating provider A doesn't depend on provider B's results, so the six evaluations are independent. The merge strategy is defined before fan-out (below). That's the key precondition. Six workers is within the range where background subagents make sense (4-8).

### Step 0: Shared rubric (sequential, done by me first)
Everything downstream depends on this, so it is not parallelized. Define:
- **Hard requirements (pass/fail):** region, compliance (e.g. SOC 2, GDPR), required services, budget ceiling.
- **Weighted criteria (score 1-5 each):** cost at your expected load, performance and latency, reliability/SLA, operational effort, security features, scalability, support quality, lock-in risk.
- **Weights:** agreed with you before launch, so workers can't skew them.
- **Evidence rule:** every score must cite a source (docs, pricing page, SLA, status history) and be marked *verified* or *assumed*.

### Step 1: Fan-out (one message, six Agent calls, `run_in_background: true`)
One subagent per provider. Each prompt is self-contained, since agents can't see this conversation, and contains the workload description, the rubric, the evidence rule, and the exact output format. Each agent:
- Researches only its own provider (read-only; nothing to edit, so no worktrees needed).
- Writes its result to its own isolated file (e.g. `eval/provider-X.json`) so there is no shared state to collide on.
- Returns a fixed schema: hard-requirement pass/fail, scores per criterion with evidence and confidence, estimated monthly cost under stated assumptions, top 3 risks, a one-line verdict.

Model split: gathering workers on a mid-tier model, medium effort; the merge/judgment stage on the strongest model, high effort.

### Step 2: Fan-in and merge
Results arrive as notifications. I wait for all six (or a timeout, around 30 minutes, with missing providers flagged rather than silently dropped). Then merge with a **layered strategy**:
1. **Filter (consensus on facts):** drop providers failing any hard requirement.
2. **Aggregate (weighted voting):** compute weighted scores for survivors in a script, not by judgment.
3. **Cross-check:** normalize across workers. Independent agents score differently, e.g. one rates "4/5 support" more generously than another. Spot-check any score with no cited evidence, and re-check the top 2-3 providers' key claims (especially price and SLA) with a second pass.
4. **Resolve conflicts (synthesis):** where the cost ranking and the quality ranking disagree, lay out the trade-off explicitly instead of averaging it away.

### Step 3: Recommendation
One page with:
- Ranked shortlist, a clear top pick, and the runner-up with the conditions under which it wins instead.
- Score table, with evidence-backed vs assumed scores marked.
- Sensitivity check: does the winner change if cost weight goes up or down 10 points?
- Open risks and what to verify before signing (e.g. a proof-of-concept or quote).
- Confidence level, lowered if many scores rest on assumptions.

### Pitfalls I'm designing around
- **Undefined rubric:** the main cause of unmergeable results, hence Step 0.
- **Inconsistent scoring across workers:** fixed schema plus normalization.
- **Stale or marketing-driven data:** require sources and mark unverified claims.
- **Silent failures:** a missing agent is reported, not ignored.

**To start**, I need from you: the workload description, budget ceiling, region/compliance needs, and the six provider names, plus sign-off on the criteria weights.
