---
name: dialectical-reasoning
description: Resolves a genuine conceptual or design tension, where two opposing positions are both valid and a binary choice is a false one, by steel-manning each side and building a synthesis that keeps the value of both. Use when the user asks "monolith or microservices", "consistency or availability", "move fast or don't break things", "centralize or decentralize", or is stuck between two approaches that each have a real case. Not for picking a winner among options (use tree-of-thoughts), exploring unknown options (use breadth-of-thought), or questions with an objective answer. When the decision needs several people's buy-in, use negotiated-decision-framework instead.
metadata:
  version: "2.3.0"
---

Works best with extended thinking for the hardest phases.

# Dialectical Reasoning

## Backstage rule — the method never appears in the answer

This methodology is scaffolding, not content. In the user-facing answer: no method names ("Dialectical Reasoning", or any other reasoning-skill name), no method narration ("applying the method", "scoring the dimensions", "this branch scores 7/10"), no internal scores or affinity arithmetic, no confidence-aggregation or checkpoint talk. Structure earns its place only as content built from the problem's own facts — a hypothesis table in a diagnosis, an options-vs-criteria matrix in a selection — never as a display of process. Before delivering, run a literal text search over the answer for the names above and for "pattern", "branch", "affinity", "dimension score", "confidence aggregation", "checkpoint"; rewrite every hit as content or delete it. The reader sees findings, not the apparatus that produced them.

**Purpose**: Navigate genuine tensions between valid but opposing forces through synthesis rather than selection. Many problems involve trade-offs where both sides have legitimate merit.

## When to Use Dialectical Reasoning

**✅ Use when:**
- Two valid perspectives are in genuine tension
- "Both/and" might be better than "either/or"
- The tension is conceptual or architectural: two valid principles or approaches pull against each other
- Historical debates suggest no clear winner
- The "right" answer depends on context that varies

**❌ Don't use when:**
- One option is clearly superior (use tree-of-thoughts)
- Need to explore unknown space (use breadth-of-thought)
- Problem has objective correct answer
- Time doesn't permit nuanced synthesis
- The decision needs several people's buy-in, with competing interests and politics (use negotiated-decision-framework)

**Examples:**
- "Monolith vs microservices" ✅ (genuine trade-off)
- "Consistency vs availability" ✅ (CAP theorem)
- "Move fast vs don't break things" ✅ (cultural tension)
- "Which sorting algorithm is fastest?" ❌ (objective answer exists)

---

## Core Methodology: Hegelian Spiral

The phase templates and the worked example below are internal working, not for the answer. Deliver in the Output Template shape at the end.

### Phase 1: Thesis Articulation

**Goal**: Steel-man the first position with maximum charity

**Process:**
1. State the thesis position clearly
2. Identify its strongest arguments (not strawmen)
3. Cite evidence, examples, and authorities supporting it
4. Explain WHY reasonable people hold this view
5. Acknowledge what this position gets RIGHT

**Template:**
```markdown
## Thesis: [Position Name]

### Core Claim
[One-sentence summary of the position]

### Strongest Arguments
1. [Argument 1 with evidence]
2. [Argument 2 with evidence]
3. [Argument 3 with evidence]

### Supporting Evidence
- [Data, case studies, expert opinions]

### What This Gets Right
- [Genuine insights and valid concerns]

### Ideal Conditions
- [When/where this position is clearly correct]
```

**Quality Check**: Could a genuine advocate of this position recognize their view?

---

### Phase 2: Antithesis Articulation

**Goal**: Steel-man the opposing position with equal charity

**Process:**
1. State the antithesis position clearly
2. Identify its strongest arguments (not reactions to thesis)
3. Cite evidence, examples, and authorities supporting it
4. Explain WHY reasonable people hold this view
5. Acknowledge what this position gets RIGHT

**Template:**
```markdown
## Antithesis: [Position Name]

### Core Claim
[One-sentence summary - not just negation of thesis]

### Strongest Arguments
1. [Argument 1 with evidence]
2. [Argument 2 with evidence]
3. [Argument 3 with evidence]

### Supporting Evidence
- [Data, case studies, expert opinions]

### What This Gets Right
- [Genuine insights and valid concerns]

### Ideal Conditions
- [When/where this position is clearly correct]
```

**Quality Check**: Is this position developed independently, not just as thesis-negation?

---

### Phase 3: Tension Analysis

**Goal**: Identify the genuine conflict and why simple compromise fails

**Process:**
1. Map the core tension
2. Identify failed compromise attempts
3. Understand why "just pick one" is unsatisfying
4. Find the deeper question beneath the surface conflict

**Template:**
```markdown
## Tension Analysis

### Core Conflict
[What specifically is in tension between thesis and antithesis]

### Why Compromise Fails
[Why "do a little of both" doesn't resolve the tension]

### False Dichotomy Check
- Is this actually a spectrum? [If yes, where on spectrum?]
- Are there hidden assumptions? [What if we question them?]
- Is the framing wrong? [Alternative framings?]

### Deeper Question
[The underlying issue that generates this surface tension]

### Context Variables
[What factors determine when thesis vs antithesis is more appropriate?]
```

---

### Phase 4: Synthesis Generation

**Goal**: Create a higher-order resolution that transcends the original opposition

**Synthesis Types:**

**Type 1: Contextual Synthesis**
- Thesis applies in context A
- Antithesis applies in context B
- Synthesis: Clear decision rules for context detection

**Type 2: Temporal Synthesis**
- Thesis applies at time/stage T1
- Antithesis applies at time/stage T2
- Synthesis: Evolutionary path from T1 to T2

**Type 3: Structural Synthesis**
- Thesis applies at level/layer L1
- Antithesis applies at level/layer L2
- Synthesis: Architecture with different principles at different layers

**Type 4: Dialectical Transcendence**
- Reframe the problem to dissolve the tension
- Find a third option that wasn't visible from either position
- Synthesis: New paradigm that makes original debate obsolete

**Template:**
```markdown
## Synthesis: [Name]

### Synthesis Type
[Contextual / Temporal / Structural / Transcendence]

### Core Resolution
[One-sentence summary of the synthesis]

### How It Preserves Thesis Insights
- [Thesis value 1 → How synthesis captures it]
- [Thesis value 2 → How synthesis captures it]

### How It Preserves Antithesis Insights
- [Antithesis value 1 → How synthesis captures it]
- [Antithesis value 2 → How synthesis captures it]

### What's New/Transcended
- [How synthesis goes beyond both original positions]

### Decision Framework
[Practical rules for applying the synthesis]

### Limitations
- [When does even the synthesis break down?]
- [What new tensions does synthesis create?]
```

---

### Phase 5: Recursive Application

**Goal**: Check if synthesis creates new tensions requiring further dialectic

**Process:**
1. Does the synthesis have its own antithesis?
2. If yes, repeat Phases 1-4 at higher level
3. Continue until reaching stable resolution or explicit trade-off acceptance

**Spiral Depth Limit**: Maximum 3 levels. If no stable synthesis by level 3, document as "productive tension to be managed, not resolved."

---

## Example: Monolith vs Microservices (internal working)

### Thesis: Monolith
- **Core Claim**: Single deployable unit provides simplicity and coherence
- **Strongest Arguments**:
  - Simpler operations (one thing to deploy, monitor, debug)
  - No network latency between components
  - Easier refactoring (IDE support, type checking across codebase)
  - Lower infrastructure cost
- **What It Gets Right**: Complexity has real costs; distribution is hard

### Antithesis: Microservices
- **Core Claim**: Independent services enable team autonomy and resilience
- **Strongest Arguments**:
  - Teams can deploy independently
  - Failure isolation (one service down ≠ everything down)
  - Technology heterogeneity (right tool per service)
  - Scale individual components
- **What It Gets Right**: Organizational scaling requires boundaries

### Tension Analysis
- **Core Conflict**: Coupling (ease of change) vs Decoupling (independence)
- **Why Compromise Fails**: "Small monolith" and "few microservices" inherit worst of both
- **Deeper Question**: How do we get team independence without distribution tax?

### Synthesis: Modular Monolith → Selective Extraction

**Synthesis Type**: Temporal

**Core Resolution**: Start with modular monolith (clear boundaries, shared deployment), extract to services only when specific benefits outweigh costs

**Decision Framework**:
```
Keep in monolith IF:
- Same team owns both sides of the boundary
- Shared deployment is acceptable
- No independent scaling requirement
- Technology homogeneity is fine

Extract to service IF:
- Different teams with different cadences
- Need independent scaling (10x difference)
- Need technology heterogeneity
- Need fault isolation for compliance
```

**What's New**: The question isn't "which architecture" but "which boundaries need which treatment"

---

## Common Mistakes

1. **Strawmanning**: Presenting weak version of thesis or antithesis
   - Fix: Steel-man test - could advocates recognize their view?

2. **False Balance**: Treating unequal positions as equal
   - Fix: If one position is clearly stronger, use tree-of-thoughts instead

3. **Premature Synthesis**: Jumping to "both!" without tension analysis
   - Fix: Explicitly analyze why simple compromise fails

4. **Infinite Regress**: Spiraling without convergence
   - Fix: 3-level limit; some tensions are managed, not resolved

5. **Abstract Synthesis**: Resolution too vague to be actionable
   - Fix: Require decision framework with concrete rules

---

## Integration with Other Skills

**Before**: Use when tree-of-thoughts reveals two branches are nearly tied and represent genuine perspectives

**After**: If the synthesis identifies context variables, use tree-of-thoughts to optimize within each context

**breadth-of-thought → dialectical-reasoning**: If breadth-of-thought shows options cluster into two camps, use this skill to understand the underlying tension

**dialectical-reasoning → negotiated-decision-framework**: Once the conceptual tension is resolved, if the people involved still disagree, hand over to negotiated-decision-framework

---

## Output Template

```markdown
# [Topic]: Two Positions and a Way Through

## [Position 1]
[Steel-manned presentation]

## [Position 2]
[Steel-manned presentation]

## Where They Collide
[Why neither alone suffices, why simple compromise fails]

## Resolution: [Name]
[Core idea, how it keeps what each side gets right, rules for applying it]

## What Stays Unresolved
[Tensions the resolution doesn't remove, and what would change the answer]
```
