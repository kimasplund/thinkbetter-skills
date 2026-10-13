---
name: integrated-reasoning
description: "Chooses how to reason about a hard problem before diving in: scores the problem's traits and routes it to the best-fitting reasoning skill, a sequence of several, or plain direct analysis. Use when a complex or high-stakes problem mixes debugging, trade-offs, novelty or stakeholder politics and the approach is unclear, e.g. 'how should I approach this', 'which method fits here', 'help me think this through'. If the problem type is already clear, use that skill directly: hypothesis-elimination for a root cause, tree-of-thoughts for the best known option, dialectical-reasoning for a trade-off, rapid-triage-reasoning for an emergency."
metadata:
  version: "2.3.0"
---

# Integrated Reasoning — Meta-Orchestration

**The scoring pass is silent.** Dimension scores, affinity arithmetic, pattern names, and selection narration never appear in the user-facing answer — the reader sees the analysis, not the apparatus that chose it. A selected pattern's structure may appear only as content built from the problem's own facts (a hypothesis table, a criteria matrix), never as methodology narration. Announce nothing; just analyze.

**Turn discipline:** announcing this skill or a selected pattern is NOT a response. After any announcement, continue immediately in the same turn with the pattern's actual steps and the tool calls that do the work. Smaller models are especially prone to stopping after the announcement.

**Purpose**: Select and orchestrate the best reasoning pattern(s) for the problem, using weighted scoring instead of an order-dependent decision tree, with feedback checkpoints and bounded confidence aggregation.

## Available Reasoning Patterns (9)

Each pattern is a sibling skill. The shorthand in the second column is used only in the formulas and tables of this skill.

| Skill | Shorthand | Purpose | Best For |
|-------|-----------|---------|----------|
| **tree-of-thoughts** | ToT | Find optimal solution through deep exploration | Optimization, clear criteria, find THE best |
| **breadth-of-thought** | BoT | Map solution space comprehensively | Unknown space, need multiple options |
| **self-reflecting-chain** | SRC | Sequential reasoning with validation | Dependent steps, proofs, linear traces |
| **hypothesis-elimination** | HE | Systematic elimination through evidence | Diagnosis, debugging, root cause |
| **adversarial-reasoning** | AR | Stress-test through attack simulation | Validation, security, pre-mortems |
| **dialectical-reasoning** | DR | Synthesize opposing valid perspectives | Trade-offs, conceptual conflicts |
| **analogical-transfer** | AT | Solve via cross-domain parallels | Novel problems, no direct precedent |
| **rapid-triage-reasoning** | RTR | Fast decisions under time pressure | Incidents, emergencies, time-boxed choices |
| **negotiated-decision-framework** | NDF | Multi-stakeholder coordination | Politics, competing interests, buy-in needed |

For a one-line "if you need X, use Y" lookup, read [references/quick-selection-guide.md](references/quick-selection-guide.md) when the right pattern seems obvious and full scoring would be overkill.

---

## Pattern Selection: Weighted Multi-Dimensional Scoring

### Step 1: Assess Problem Characteristics

Score each dimension (1-5):

```markdown
| Dimension | Score | Description |
|-----------|-------|-------------|
| **Sequential Dependencies** | _/5 | Do steps depend on previous steps? |
| **Criteria Clarity** | _/5 | Can you clearly evaluate solutions? |
| **Solution Space Known** | _/5 | Do you know the options? |
| **Single Answer Needed** | _/5 | Need ONE answer vs multiple options? |
| **Evidence Available** | _/5 | Can you gather discriminating evidence? |
| **Opposing Valid Views** | _/5 | Are there legitimate conflicting perspectives? |
| **Problem Novelty** | _/5 | Is this unprecedented in your domain? |
| **Robustness Required** | _/5 | Need to stress-test before committing? |
| **Solution Exists** | _/5 | Do you have a candidate solution to evaluate? |
| **Time Pressure** | _/5 | How constrained is decision time? (5=minutes) |
| **Stakeholder Complexity** | _/5 | Multiple parties with competing interests? |
```

### Step 1.5: Time Pressure Fast-Path

**CRITICAL**: If Time Pressure = 5 (emergency/incident):
- Skip full scoring
- Use **rapid-triage-reasoning** directly
- It is optimized for decisions under extreme time constraints

If Time Pressure ≥ 4:
- Consider rapid-triage-reasoning unless the problem is clearly sequential (use self-reflecting-chain) or diagnostic (use hypothesis-elimination)
- Apply abbreviated scoring (skip orchestration considerations)

### Step 2: Calculate Pattern Affinity Scores

```
ToT  = (Criteria × 0.35) + (SingleAnswer × 0.30) + (SpaceKnown × 0.20) + ((6-Novelty) × 0.15)

BoT  = ((6-SpaceKnown) × 0.35) + ((6-SingleAnswer) × 0.30) + ((6-Criteria) × 0.20) + (Novelty × 0.15)

SRC  = (Sequential × 0.45) + (Criteria × 0.25) + (SingleAnswer × 0.20) + ((6-OpposingViews) × 0.10)

HE   = (Evidence × 0.40) + (SingleAnswer × 0.30) + ((6-Novelty) × 0.20) + ((6-OpposingViews) × 0.10)

AR   = (Robustness × 0.40) + (SolutionExists × 0.30) + ((6-Novelty) × 0.15) + (Evidence × 0.15)
       # NOTE: AR requires SolutionExists ≥ 3, otherwise score = 0

DR   = (OpposingViews × 0.50) + (Criteria × 0.20) + ((6-Evidence) × 0.15) + (MIN(SingleAnswer, OpposingViews) × 0.15)
       # NOTE: SingleAnswer is not penalized when OpposingViews is high

AT   = (Novelty × 0.45) + ((6-SpaceKnown) × 0.30) + ((6-Evidence) × 0.15) + ((6-Sequential) × 0.10)

RTR  = (TimePressure × 0.50) + (SingleAnswer × 0.25) + (Evidence × 0.15) + ((6-Novelty) × 0.10)
       # NOTE: RTR auto-selected when TimePressure = 5

NDF  = (StakeholderComplexity × 0.45) + (OpposingViews × 0.25) + ((6-Criteria) × 0.15) + ((6-TimePressure) × 0.15)
       # NOTE: NDF requires StakeholderComplexity ≥ 3 to be considered
```

**Formula Validation Rules**:
- AR returns 0 if SolutionExists < 3 (nothing to attack)
- RTR auto-triggers when TimePressure = 5 (emergency mode)
- NDF returns 0 if StakeholderComplexity < 3 (single decision-maker)
- If the top three patterns score within 0.3 of each other, use uncertainty propagation (Step 2.5); see the decision table below for the top-two rules

### Step 2.5: Uncertainty Propagation

When dimension scores are uncertain, propagate uncertainty to pattern selection:

```markdown
## Uncertainty Assessment

For each dimension where you're unsure (±1 point uncertainty):

1. Calculate pattern scores at LOW end (dimension - 1)
2. Calculate pattern scores at HIGH end (dimension + 1)
3. If different pattern wins at each end → **Flag as uncertain selection**

### Handling Uncertain Selections

**If same pattern wins both ends**: Proceed with confidence
**If different patterns win**:
  - Run BOTH patterns in parallel (if time permits)
  - OR use the pattern that's more robust to being wrong
  - OR gather more information to reduce dimension uncertainty

### Uncertainty Discount
Apply -5% to final confidence for each uncertain dimension that affects the winning pattern.
```

### Step 3: Interpret Scores

| Scenario | Action |
|----------|--------|
| One pattern scores >4.0 | Use that pattern directly |
| Top 2 within 0.5 of each other | Consider multi-pattern orchestration |
| Top 3 within 0.3 of each other | Apply uncertainty propagation first |
| Top pattern ≤4.0, no dimension scored ≥4, and Time Pressure <4 | None fit well; use Direct Analysis |
| All patterns <3.0 but Direct Analysis does not apply | Problem may need decomposition first |

To check your arithmetic against a fully scored case, read [references/worked-example.md](references/worked-example.md) when you are unsure how to score a dimension or interpret close scores.

### Direct Analysis (10th Pattern)

Use Direct Analysis (no specialized pattern) when all three hold:
- MAX(all pattern scores) ≤ 4.0 — no pattern is a clear fit, AND
- No dimension scored ≥ 4 — the problem has no strong characteristic a pattern is built for, AND
- Time Pressure < 4 — otherwise the fast-path applies

```markdown
## Direct Analysis

**Approach**:
1. No special framework needed
2. Just think through the problem directly, step by step
3. Use common sense and straightforward reasoning
4. Appropriate for simple problems that don't need cognitive overhead

**Examples**:
- Simple factual questions
- Straightforward calculations
- Basic lookups or translations
- Problems with obvious solutions

**Confidence**: Use intuitive confidence based on problem clarity
- Clear problem + clear answer = high confidence
- Any ambiguity = document it explicitly
```

Problems this simple often don't need scoring at all; if the answer is obvious, answer it.

---

## Effort Level Mapping

After selecting the optimal pattern, set effort level:

| Pattern | Default Effort | Max Effort Trigger |
|---------|---------------|-------------------|
| ToT | high | Critical optimization decisions |
| BoT | high | Unknown solution spaces |
| HE | high | Production incidents |
| SRC | medium | Standard step-by-step |
| AR | high | Security/safety validation |
| DR | high | Architecture trade-offs |
| AT | max | Completely novel domains |
| RTR | low | Time-critical (< 5 minutes) |
| NDF | medium | Standard stakeholder alignment |

For max effort, use extended thinking.

---

## Execution Modes

Only **breadth-of-thought** runs as a forked subagent (`context: fork`). A fork gets its own context window and cannot see conversation history, so pass it the full problem statement and constraints; it returns a summary.

All other patterns run inline, in the current conversation. **integrated-reasoning itself** always runs inline, because it orchestrates within the main context.

---

## Model-Aware Selection

When running on different models:
- **Opus**: All patterns available at full depth
- **Sonnet**: Reduce branch counts (tree-of-thoughts: 3 branches, breadth-of-thought: 5 approaches). self-reflecting-chain, hypothesis-elimination and rapid-triage-reasoning work well. dialectical-reasoning and analogical-transfer may lose synthesis quality.
- **Haiku**: Only rapid-triage-reasoning recommended; other patterns lose quality

---

## Sequential vs Parallel Execution Decision

### Use SEQUENTIAL when:
- Pattern B depends on Pattern A's output (e.g., BoT finds options → ToT optimizes)
- Confidence from A affects what to do in B
- Evidence from A eliminates need for B
- One pattern discovers the problem is different than expected

### Use PARALLEL when:
- Patterns explore independent dimensions
- No dependency between pattern outputs
- Need ensemble confidence (run same problem through 2 patterns)
- Time allows and you want cross-validation
- Patterns are complementary (e.g., different perspectives on same problem)

### Common Chains (Sequential):
```
BoT → ToT → AR     (explore → optimize → validate)
HE → SRC → AR      (diagnose → trace → validate fix)
AT → DR → ToT      (analogize → synthesize → optimize)
RTR → HE → ToT     (triage → root cause → proper fix)
NDF → ToT → AR     (align stakeholders → optimize → validate)
DR → NDF → ToT     (resolve concepts → negotiate politics → optimize)
AT → BoT → ToT     (find analogies → explore adaptations → select best)
```

### Common Parallel Combinations:
```
BoT || AT          (parallel exploration from different angles)
ToT || DR          (optimize while synthesizing trade-offs)
HE branches        (test multiple hypotheses simultaneously)
AR attack vectors  (stress-test from multiple directions at once)
```

---

## Full Reasoning Chain: Input → Output

Complete end-to-end flow:

```
1. **Problem Input**
   └─→ Receive problem statement, constraints, and context

2. **Score 11 Dimensions**
   └─→ Sequential Dependencies, Criteria Clarity, Solution Space Known,
       Single Answer Needed, Evidence Available, Opposing Valid Views,
       Problem Novelty, Robustness Required, Solution Exists,
       Time Pressure, Stakeholder Complexity

3. **Fast-Path Check**
   └─→ TimePressure = 5? → RTR immediately (skip remaining steps)

4. **Pattern Selection**
   └─→ Calculate affinity scores for all 9 patterns
   └─→ Apply validation rules (AR needs solution, NDF needs stakeholders)

5. **Direct Analysis Check**
   └─→ Top pattern ≤ 4.0, no dimension ≥ 4, TimePressure < 4? → Direct Analysis (no framework)

6. **Orchestration Decision**
   └─→ Single pattern > 4.0? → Use that pattern directly
   └─→ Top 2 within 0.5? → Consider multi-pattern orchestration
   └─→ Top 3 within 0.3? → Apply uncertainty propagation first
   └─→ Decide: Sequential or Parallel execution?

7. **Pattern Execution**
   └─→ Apply selected pattern(s) using their methodologies
   └─→ Track confidence and key findings

8. **Checkpoint (after each phase of the pattern)**
   └─→ Progress check, pattern fit check, new information check
   └─→ Re-evaluate and potentially switch patterns if needed

9. **Handover (if multi-pattern)**
   └─→ Record state as described in reasoning-handover-protocol
   └─→ Preserve insights from completed pattern
   └─→ Set up next pattern with full context

10. **Synthesis (if multi-pattern)**
    └─→ Combine findings from all patterns
    └─→ Resolve conflicts, identify agreements

11. **Confidence Aggregation**
    └─→ Single pattern: use internal confidence
    └─→ Multi-pattern: apply agreement analysis
    └─→ Apply uncertainty discounts if applicable

12. **Output**
    └─→ Deliver answer with reasoning trail
    └─→ Document confidence level and key uncertainties
    └─→ Provide actionable recommendations
```

---

## Multi-Pattern Orchestration

### When to Orchestrate

- Top 2 patterns within 0.5 points AND
- Problem is high-stakes (consequences matter) AND
- The user wants depth rather than a quick answer

### Orchestration Patterns

**Sequential Orchestration** (most common):
1. Use exploration pattern first (BoT, AT)
2. Use optimization pattern second (ToT, HE)
3. Use validation pattern last (AR, SRC)

**Parallel Orchestration** (when patterns are complementary):
- Run 2 patterns independently
- Compare conclusions
- Use agreement/disagreement to calibrate confidence

**Nested Orchestration** (when patterns address different aspects):
- Apply different patterns to different sub-problems
- Synthesize at the end

### Orchestration Decision Table

| Pattern A High | Pattern B High | Orchestration |
|----------------|----------------|---------------|
| BoT | ToT | Sequential: BoT (explore) → ToT (optimize top options) |
| BoT | HE | Sequential: BoT (generate hypotheses) → HE (eliminate) |
| ToT | AR | Sequential: ToT (select) → AR (validate before commit) |
| ToT | SRC | Sequential: ToT (decide) → SRC (plan implementation) |
| DR | ToT | Sequential: DR (resolve tension) → ToT (optimize within synthesis) |
| AT | ToT | Sequential: AT (find analogies) → ToT (evaluate derived solutions) |
| AT | BoT | Parallel: Both explore, merge findings |
| HE | SRC | Sequential: HE (find cause) → SRC (trace mechanism) |
| RTR | HE | Sequential: RTR (immediate triage) → HE (post-incident RCA) |
| RTR | AR | Sequential: RTR (quick decision) → AR (post-decision validation) |
| NDF | ToT | Sequential: NDF (get buy-in) → ToT (optimize within agreed bounds) |
| NDF | DR | Sequential: DR (resolve conceptual tension) → NDF (negotiate stakeholders) |
| BoT | NDF | Sequential: BoT (explore options) → NDF (negotiate which to pursue) |

**rapid-triage-reasoning Orchestration Rules**:
- It is typically a STARTING pattern, not an ending one
- After it stabilizes the situation, follow up with deeper analysis
- RTR → HE for incident root cause analysis
- RTR → ToT for revisiting decision with more time

**negotiated-decision-framework Orchestration Rules**:
- It typically FOLLOWS technical analysis (know options before negotiating)
- BoT → NDF: Explore space, then negotiate which options to pursue
- NDF → ToT: After stakeholder agreement, optimize implementation
- DR → NDF: Resolve conceptual tensions first, then stakeholder tensions

When a pattern hands work to the next one and the state is too large to carry in conversation, follow **reasoning-handover-protocol** (what to record, the optional `.reasoning/` folder, and cycle prevention).

---

## Parallel Pattern Execution

When the top 2 patterns score within 0.3 and neither needs the other's output (if one builds on the other, run them in sequence instead):
- Use parallel subagents (multiple calls to the Agent tool)
- Each pattern runs in its own subagent
- Merge results using agreement analysis

### When to Parallelize

Parallel execution is appropriate when independent reasoning paths can run concurrently without blocking each other:

| Condition | Parallelization Strategy |
|-----------|-------------------------|
| **Top 2 patterns within 0.3 of each other, and independent** | Run both patterns in parallel, compare results (dependent pairs run in sequence) |
| **BoT natural parallelism** | 8-10 branches can explore simultaneously |
| **Hypothesis testing (HE)** | Parallel evidence gathering for multiple hypotheses |
| **Multi-perspective needs (mixture of agents)** | Different "expert personas" analyze in parallel |

### Parallel Orchestration Patterns

| Pattern Combination | Parallel Strategy | Merge Approach |
|--------------------|-------------------|----------------|
| **BoT \|\| AT** | Parallel exploration from different angles | Merge findings, deduplicate insights |
| **ToT branches** | Parallel subtree exploration at each level | Take best-scoring subtree |
| **HE hypotheses** | Parallel evidence collection for each hypothesis | Aggregate evidence, eliminate losers |
| **AR attacks** | Parallel threat simulation (different attack vectors) | Union of discovered vulnerabilities |

For concurrency limits and choosing a merge strategy (consensus, voting, aggregation, best-of-n), read [references/parallel-config.md](references/parallel-config.md) when you are about to run patterns or branches in parallel.

---

## Feedback Loop: Phase Checkpoint

**After each completed phase of the selected pattern** (or every few turns on a long task — Claude cannot measure elapsed time, so count work, not minutes):

```markdown
## Checkpoint Evaluation

### Progress Check
- [ ] Have I made meaningful progress toward goal?
- [ ] Is my confidence increasing?

### Pattern Fit Check
- [ ] Am I fighting the methodology?
- [ ] Have I discovered new problem characteristics?

### New Information
- [ ] Has the problem changed?
- [ ] Do my characteristic scores need updating?

### Decision
If 2+ checks FAIL:
  → PAUSE: Re-score characteristics
  → If different pattern scores highest: SWITCH
  → If same pattern: Continue with awareness

If all checks PASS:
  → Continue current pattern
  → Checkpoint again after the next phase
```

---

## Confidence Aggregation

Additive confidence boosting is statistically invalid, so use agreement-based bounded adjustment.

**Confidence bounds (apply to every result, single or multi-pattern, and to every hand-off):**
- Floor: 10% (never report lower confidence)
- Ceiling: 95% (never report higher confidence)

### Single Pattern Confidence
Use the pattern's internal confidence score (per its methodology).

### Multi-Pattern Confidence

```markdown
## Multi-Pattern Synthesis (internal working, not for the answer)

### Raw Scores
- Pattern A conclusion: [Answer A] at [X]% confidence
- Pattern B conclusion: [Answer B] at [Y]% confidence
- Pattern C conclusion: [Answer C] at [Z]% (if used)

### Agreement Analysis

**FULL AGREEMENT** (same conclusion):
- Final Confidence = MIN(MAX(X, Y, Z) + 5%, 95%)
- Rationale: Independent paths converging increases trust

**PARTIAL AGREEMENT** (2/3 agree):
- Final Confidence = (AVG of agreeing × 0.7) + (disagreeing × 0.15)
- Must document the disagreement
- Consider: Why does one pattern disagree?

**NO AGREEMENT** (different conclusions):
- Final Confidence = MAX(MIN(X, Y, Z) - 10%, 10%)
- This is a FEATURE not a bug - disagreement reveals complexity
- Action: Either (a) gather more information, or (b) present trade-offs to stakeholder

### Shared Assumption Discount
If patterns share significant assumptions, apply -5% adjustment.
(Same LLM, same problem framing, same information = shared blind spots)
```

Each pattern has blind spots that cap how far its confidence should be trusted. Read [references/pattern-limitations.md](references/pattern-limitations.md) when deciding how much weight a single pattern's conclusion deserves, or why two patterns disagree.

---

## Before delivering — mechanical leak scan

Run a literal text search over the user-facing answer for: every pattern name and shorthand in the table above (ToT, BoT, SRC, HE, AR, DR, AT, RTR, NDF and their full names), "affinity", "dimension score", "scoring the", "confidence aggregation", "checkpoint", "pattern". Every hit is rewritten as content or deleted; deliver only at zero unrewritten hits. A hypothesis list, a criteria matrix built from the question's own stated criteria, or a confidence statement about the answer itself ("~85% this is the cause") are content — they stay.
