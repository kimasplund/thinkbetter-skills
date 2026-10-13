# Parallel Configuration and Merge Strategies

Read this when integrated-reasoning has decided to run two patterns, or many branches of one pattern, in parallel subagents.

## Parallel Configuration

The values below are illustrative defaults, not settings any tool reads. Treat them as a checklist of limits to decide on before fanning out.

```yaml
parallel_config:
  max_concurrent_patterns: 3      # Max patterns running simultaneously
  max_concurrent_branches: 8      # Max branches within a single pattern
  merge_strategy: "consensus"     # "consensus" | "voting" | "aggregation" | "best-of-n"
  turns_per_branch: 1             # Illustrative: one subagent call per branch (Claude counts turns, not milliseconds)
  early_termination_threshold: 0.95  # Stop early once confidence reaches the 95% ceiling
```

**Configuration Guidelines**:
- Use `max_concurrent_patterns: 2` for typical orchestration
- Use `max_concurrent_branches: 8` for breadth-of-thought exploration
- Give a branch more turns (or split it) for complex sub-problems
- Lower `early_termination_threshold` (e.g., 0.85) when speed matters more than certainty

## Merge Strategies

| Strategy | When to Use | Behavior |
|----------|-------------|----------|
| **Consensus** | High-stakes, need confidence | All must agree → apply the Full Agreement rule (+5%, capped at 95%); any disagreement → flag for review |
| **Voting** | Multiple viable options | Majority wins; ties broken by highest individual confidence |
| **Aggregation** | Complementary findings | Synthesize all findings into unified result; no filtering |
| **Best-of-N** | Competitive exploration | Take highest confidence result; discard others |

**Merge Strategy Selection**:
```
If robustness critical → "consensus"
If options are mutually exclusive → "voting"
If findings are additive → "aggregation"
If racing for speed → "best-of-n"
```

Merged confidence always follows the Confidence Aggregation rules and the 10%–95% bounds in SKILL.md.
