Here is a plan for evaluating the six hosting providers in parallel and merging the verdicts into one recommendation. I have not run it.

**1. Fix the criteria first (before any fan-out)**

The merge only works if every worker scores the same things. Define a shared rubric in the prompt, for example:
- Price at your expected usage (monthly estimate)
- Reliability and SLA terms
- Security and compliance fit (certifications, data residency)
- Operational effort for your team
- Lock-in and exit cost
- Fit with your stack

Give each criterion a 1 to 5 scale and a weight. Agree on the weights now, because changing them after the results arrive biases the merge.

**2. Fan out: one subagent per provider**

Six providers is in the 4 to 8 range, so use six parallel subagents with `run_in_background: true`, all launched in a single message. Each one gets a self-contained prompt, since it cannot see this conversation:
- The provider's name and the workload description
- The shared rubric and weights
- The output shape: a score per criterion, a one-paragraph verdict, and a list of unknowns or claims it could not verify

Each subagent works only on its own provider. None of them writes to a shared file or shares state with the others, so there are no collisions.

**3. Fan in and merge**

When all six notifications have arrived:
- Collect the six score sheets. Check that each one covers every criterion. If one is missing a criterion, rerun that worker rather than guessing.
- Aggregate with the weighted sum per provider. This is the Voting strategy from the parallel-execution skill: weighted score aggregation over competing options.
- Rank the providers. If two are within a small margin, say 0.2 on the weighted score, treat the result as a tie and break it on the criterion you care about most (for you, probably operational effort or security).
- Where workers disagree on a fact, such as a price or a certification, do not average the two numbers. Verify that fact yourself, because a wrong input weighs more than a missing one.

**4. Produce one recommendation**

The final answer has three parts:
- The top-ranked provider and why, with the score breakdown
- The runner-up and the one condition under which it would win
- The unverified claims that could change the ranking

**Known risks in this plan**
- Subagents know only what their prompt tells them. If pricing depends on your traffic profile, put the traffic numbers in every prompt.
- Six independent workers can each invent a plausible but unverified number. The merge step should flag any score that has no source.
- Do not parallelize the final weighting. The weights and the tie-break rule are decisions, so they stay in the main session.
