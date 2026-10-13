Here is a plan for evaluating the six hosting providers in parallel and merging the verdicts. I have not run anything.

**Why this parallelizes well:** each provider can be assessed on its own, so there are no sequential dependencies between the six evaluations. Six is in the 4-8 range, so background subagents are the right tool. The merge step is the part that needs the most design, so I define it before the fan-out.

**1. Set the criteria and rubric first (before any fan-out)**
- Fix the criteria once, for example: price at our expected load, support quality and SLA, security and compliance, operational burden, lock-in and exit cost, and fit with our stack.
- Give each criterion a weight and a 1-5 scale with written anchors, such as "5 = 99.99% SLA with 24/7 phone support, 1 = email only, best-effort." Without anchors, six independent workers will score on different scales.
- Write the rubric and the provider list into one shared brief. Every worker gets the same brief, so scores are comparable.

**2. Fan out: one subagent per provider**
- Launch six subagents with `run_in_background: true`, one per provider.
- Each gets the brief, its single provider, and a fixed output format: a score per criterion, the evidence for each score with its source, and a list of unknowns.
- Each worker writes to its own isolated output file (for example `eval/<provider>.json`) so no two workers touch shared state.
- Workers should not compare providers with each other. Comparison belongs in the merge step.

**3. Fan in: merge into one recommendation**
- Collect the six JSON outputs. Check that every worker used the same format and the same scale. Re-run any worker that did not.
- Aggregate with a weighted sum for the score. Use union with deduplication for the evidence and the unknowns.
- Where two workers disagree on a fact (for example, two different SLA figures), flag it and resolve it from the source, not by averaging.
- Rank the providers and pick the top one only if it clearly leads. If the top two are within a small margin, report that as a tie and say which criterion decides it.

**4. Sensitivity check before recommending**
- Re-run the ranking with the weights shifted (for example, cost weighted higher, then security weighted higher). If the winner changes, the recommendation is conditional. Say so, and name the condition.
- Any "unknown" that could change the winner is a blocker. List it as a question to resolve before committing.

**5. Output**
- One recommendation, the score table, the sensitivity result, and the open unknowns.

**Things to avoid**
- Starting the workers before the rubric is fixed. Their scores will not be comparable.
- Letting workers share a file or write into the same report.
- Deciding the merge rule after seeing the scores.
- Using 20+ branches. Six is well within the useful range.
