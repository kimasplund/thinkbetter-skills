---
name: parallel-execution
description: Guides running independent work in parallel, as several tool calls or several subagents in one message, and merging the results. Use when a task splits into independent sub-problems, when the user says "do these in parallel", "fan out", "explore several approaches at once", "run these agents at the same time", or when several branches, hypotheses or perspectives need to be explored together. Also covers parallel code editing in isolated worktrees and advanced ensemble and tree-search patterns. Not for steps that depend on each other (use self-reflecting-chain).
license: MIT
metadata:
  version: "2.3.0"
---

# Parallel Execution Patterns

Read [references/parallel-patterns-advanced.md](references/parallel-patterns-advanced.md) when you need the detailed algorithms behind the advanced patterns below: pruning and worker reallocation formulas, tree-search selection, multi-layer ensembles, graph operations, clustering, checkpoint and recovery shapes, or configuration profiles. The core of this skill is enough for most tasks.

## Built-in Parallel Patterns (no skill needed)

Use these first before reaching for advanced patterns.

| Pattern | How | Best For |
|---------|-----|----------|
| **Parallel tool calls** | Several tool calls in one message | Reading files, searching, independent lookups |
| **Parallel subagents** | Several Agent calls in one message, optionally with `run_in_background: true` | Independent research, analysis, exploration |
| **Worktree isolation** | An Agent call with `isolation: "worktree"` | Parallel agents editing code without colliding |
| **Agent teams** (Claude Code only, experimental) | Enabled by an environment variable; check the Claude Code docs for the current name | Coordinated multi-file work with shared tasks |
| **Background execution** | `run_in_background: true`, or Ctrl+B in Claude Code | Long-running work you don't need immediately |

The harness decides what is available. Where a tool or option above does not exist (other agents, claude.ai), run the same work sequentially and keep the same fan-out and merge structure.

### Parallel Tool Calls

Make the independent calls in one message; they run together:

```
- Read file A
- Read file B
- Grep for pattern X
- Glob for *.ts files
```

### Parallel Subagents

Send several Agent calls in one message so they run concurrently:

```
# Fan-out: one message, three Agent calls (run_in_background: true on each)
Agent 1: "Analyze database performance"
Agent 2: "Review API response times"
Agent 3: "Check frontend bundle size"

# Fan-in: each background agent's result arrives as a notification when it finishes.
# Wait for all three, then synthesize the findings.
```

Give each agent a self-contained prompt (it cannot see your conversation) and say what shape of result you want back, so the merge is easy.

### Agent Teams (Claude Code only, experimental)

For coordinated parallel work where agents need to communicate and share a task list with dependencies, for example refactor models, then update routes and tests in parallel, then update docs. This is an experimental Claude Code feature behind an environment variable and may change; prefer plain parallel subagents unless the agents genuinely need to coordinate.

### Worktree Isolation

For parallel code editing without conflicts, give each editing agent its own working copy of the repository:

```
Agent call 1: isolation: "worktree", prompt: "Implement feature A in src/features/a/"
Agent call 2: isolation: "worktree", prompt: "Implement feature B in src/features/b/"
```

Each agent works on its own copy. Review and merge the resulting branches when done.

## When to Parallelize

**Parallelize when:**
- Problem decomposes into independent sub-problems
- Multiple solution approaches need exploration (breadth-of-thought, tree-of-thoughts branching)
- High confidence required (ensemble methods)
- Multiple hypotheses need simultaneous testing (hypothesis-elimination)
- Cross-domain analogies need parallel investigation (analogical-transfer)

**Do not parallelize when:**
- Steps have sequential dependencies (use self-reflecting-chain instead)
- Each step depends on previous results
- Problem is inherently linear (tracing one execution path)
- Merge strategy is undefined

### Decision Tree

```
Is the task decomposable?
├─ NO -> Use sequential execution
└─ YES -> Are sub-tasks independent?
    ├─ NO -> Use sequential with checkpoints
    └─ YES -> Is merge strategy clear?
        ├─ NO -> Define merge strategy first
        └─ YES -> How many sub-tasks?
            ├─ 2-3 -> Parallel tool calls or subagents
            ├─ 4-8 -> Subagents with run_in_background
            └─ 8+  -> Batches of subagents, or agent teams (Claude Code, experimental)
```

---

## Advanced Cognitive Patterns

These patterns complement the built-in execution with structured reasoning strategies.

### Pattern 1: Dynamic Parallel Tree Search (DPTS)

Adaptive parallel exploration that dynamically allocates resources to promising branches while pruning unpromising ones.

**Key Mechanisms:**
- Dynamic worker allocation: more workers on promising branches
- Adaptive pruning thresholds: adjust based on best-found confidence
- Early termination: stop when confidence exceeds threshold
- Resource rebalancing: move workers from exhausted/pruned branches

**Integration with tree-of-thoughts:**

```markdown
## DPTS + tree-of-thoughts

### Phase 1: Initial Parallel Expansion
- Spawn N workers for Level 0 branches (N = 5-10)
- Each worker explores one branch independently
- Workers report confidence scores as they complete

### Phase 2: Dynamic Reallocation
- Rank branches by score
- Top 2 branches get 3 workers each for Level 1
- Prune branches below dynamic threshold

### Phase 3: Convergence
- Continue until winning branch > 85% confidence
- OR all branches at Level 4+

### Pruning Threshold Formula
dynamic_threshold = max(0.40, best_confidence - 0.30)
```

**Example:**

```
Level 0: 5 branches, 5 workers (parallel subagents)
├─ Branch A: 75% (3 workers for L1)
├─ Branch B: 68% (2 workers for L1)
├─ Branch C: 52% (1 worker)
├─ Branch D: 48% (1 worker)
└─ Branch E: 35% (PRUNED)

Best found: A.2 at 82% -> New threshold: 52%
-> Branch D PRUNED (48% < 52%)
```

---

### Pattern 2: Branch-Solve-Merge (BSM)

Decompose problems, solve sub-problems in parallel, merge results. Use when problems partition cleanly.

```markdown
## Branch Phase
1. Analyze problem structure
2. Identify independent sub-problems
3. Define interfaces between sub-problems

## Solve Phase (parallel subagents)
1. Spawn worker per sub-problem (run_in_background: true)
2. Each worker solves independently
3. Workers report partial solutions

## Merge Phase
1. Collect all partial solutions
2. Apply merge strategy
3. Resolve conflicts
4. Synthesize final solution
```

**Merge Strategies:**

| Strategy | When to Use | Method |
|----------|-------------|--------|
| **Consensus** | Multiple workers on same problem | Majority agreement |
| **Voting** | Competing approaches | Weighted score aggregation |
| **Aggregation** | Complementary results | Union with deduplication |
| **Synthesis** | Conflicting valid results | Dialectical resolution |

---

### Pattern 3: Mixture of Agents (MoA)

Layered proposer/aggregator architecture for ensemble confidence.

```
┌────────────────────────────────────────┐
│            Aggregator Layer             │
│  (Synthesizes proposals, resolves      │
│   conflicts)                           │
└──────────────────┬─────────────────────┘
                   │ Proposals flow up
┌────────────────────────────────────────┐
│            Proposer Layer               │
│  ┌────────┐ ┌────────┐ ┌────────┐      │
│  │Prop 1  │ │Prop 2  │ │Prop 3  │      │
│  │tree-of-│ │breadth-│ │analog- │      │
│  │thoughts│ │of-thght│ │transfer│      │
│  └────────┘ └────────┘ └────────┘      │
└────────────────────────────────────────┘
```

**Conflict Resolution:**
- If proposers agree: Boost confidence +5%
- If 2/3 agree: Use majority, document minority
- If no agreement: Escalate to dialectical-reasoning

---

### Pattern 4: Graph of Thoughts (GoT)

Arbitrary graph-structured reasoning with merge, split, and cycle operations.

| Operation | Description | Use Case |
|-----------|-------------|----------|
| **Branch** | Split one thought into multiple | Generate alternatives |
| **Merge** | Combine multiple thoughts into one | Synthesize findings |
| **Refine** | Iterate on a single thought | Improve solution |
| **Backtrack** | Return to previous thought | Error correction |
| **Cycle** | Re-evaluate with new information | Iterative improvement |

```
     [Problem]
        │
    ┌───┴───┐
    ▼       ▼
  [A]     [B]
    │       │
    └───┬───┘
        ▼
    [Merged]
        │
        ▼
    [Refined] <── Cycle
        │
        ▼
    [Solution]
```

---

### Pattern 5: Self-Consistency with Clustering (RASC)

Generate multiple reasoning paths, cluster by rationale similarity, use representative answers.

```markdown
## Phase 1: Generate K reasoning paths (parallel subagents)
## Phase 2: Cluster paths by rationale similarity
## Phase 3: Select representative from each cluster
## Phase 4: Weighted vote among representatives

Cluster A (size 3): "team autonomy" -> Microservices
Cluster B (size 3): "scalability" -> Microservices
Cluster C (size 2): "simplicity" -> Monolith

Final: Microservices (70% weighted agreement)
```

---

## Integration with Cognitive Skills

### breadth-of-thought: Parallel Branch Exploration

```markdown
Spawn 8-10 parallel workers (Agent calls in one message)
Each explores one approach independently
Prune after ALL Level 0 workers have reported (static 40% threshold)
```

### tree-of-thoughts: MCTS-Style Search

```markdown
UCB1(branch) = avg_score + C * sqrt(ln(N) / n_branch)
Run parallel rollouts from each branch (subagents)
Use UCB1 to decide which branches get more rollouts
```

### hypothesis-elimination: Parallel Hypothesis Testing

```markdown
Phase 1: Generate hypotheses
Phase 2: Identify independent evidence (parallel subagents)
Phase 3: Parallel evidence gathering
Phase 4: Synchronized hypothesis update + elimination
```

### analogical-transfer: Multi-Perspective via MoA

```markdown
Proposer 1: Technology domain analogies (subagent)
Proposer 2: Nature/biology analogies (subagent)
Proposer 3: Business/economics analogies (subagent)
Aggregator: Cross-analogy synthesis (main session)
```

---

## Pruning Strategies

| Pattern | Threshold | Rationale |
|---------|-----------|-----------|
| **breadth-of-thought** | Static 40% | Conservative breadth |
| **tree-of-thoughts** | Static top-1/top-2 | Aggressive, find single best |
| **DPTS** | Dynamic (best - 30%) | Adaptive to landscape |
| **hypothesis-elimination** | Evidence-based | Prune when evidence eliminates |
| **MoA** | Agreement-based | Prune minority after consensus |

## Anti-Patterns

1. **Parallelizing sequential dependencies** - If step 2 needs step 1's output, don't parallelize
2. **Too many branches** - 5-10 at Level 0 is reasonable; 20+ causes diminishing returns
3. **No merge strategy defined** - Always know how to combine results before fan-out
4. **Ignoring shared state** - Workers must write to isolated paths; merge in fan-in
5. **Parallel everything** - Some problems are inherently sequential; accept it

## Quick Reference

| Situation | Pattern | Why |
|-----------|---------|-----|
| Independent file reads | Parallel tool calls | Built-in, zero overhead |
| Independent research | Parallel subagents | Concurrent execution |
| Coordinated editing | Worktrees (or agent teams in Claude Code) | Avoid conflicts |
| Explore unknown space | DPTS + breadth-of-thought | Dynamic pruning, parallel breadth |
| Find optimal option | MCTS + tree-of-thoughts | Simulation-guided depth |
| Decomposable problem | BSM | Clean partition and merge |
| Need ensemble confidence | MoA or RASC | Multiple perspectives |
| Iterative refinement | GoT | Merge and cycle support |
| Test hypotheses | Parallel hypothesis-elimination | Independent evidence gathering |

## Configuration

> **Note**: The configuration below is illustrative — these are conceptual thresholds for reasoning about parallelization, not actual Claude Code configuration settings.

```json
{
  "parallel_execution": {
    "max_workers": 10,
    "worker_timeout_minutes": 30,
    "pruning": {
      "bot_threshold": 0.40,
      "tot_keep_top": 2,
      "dpts_margin": 0.30
    },
    "merge_strategies": {
      "default": "aggregation",
      "conflict_resolution": "weighted_voting",
      "confidence_agreement_boost": 0.05
    }
  }
}
```
