# Quick Selection Guide

Read this when the right pattern seems obvious and full scoring would be overkill. If two lines seem to fit, go back to the scoring in SKILL.md.

```
"I need to find the BEST option among known choices"
  → tree-of-thoughts

"I need to explore ALL possible approaches"
  → breadth-of-thought

"I need to trace through a logical chain step by step"
  → self-reflecting-chain

"I need to find THE CAUSE of something"
  → hypothesis-elimination

"I need to VALIDATE a solution before committing"
  → adversarial-reasoning

"I'm stuck between two valid but opposing approaches"
  → dialectical-reasoning

"This problem is novel - no one has solved it in my domain"
  → analogical-transfer

"I need to decide RIGHT NOW (minutes, not hours)"
  → rapid-triage-reasoning

"Multiple stakeholders with competing interests must agree"
  → negotiated-decision-framework

"I'm not sure which to use"
  → Score the dimensions (Step 1 in SKILL.md)

--- Parallelism Quick-Reference ---

"Top 2 patterns scored within 0.3"
  → Run both in parallel, merge with "consensus" or "voting"

"Need to explore many options fast"
  → breadth-of-thought with max_concurrent_branches: 8

"Testing multiple hypotheses"
  → hypothesis-elimination with parallel evidence gathering

"Need diverse perspectives on same problem"
  → mixture of agents: parallel expert personas

"Running parallel but need to merge"
  → consensus (high-stakes) | voting (exclusive) | aggregation (additive) | best-of-n (speed)
```

Merge strategies are explained in parallel-config.md, in this folder.
