---
name: self-reflecting-chain
description: Works through a problem one dependent step at a time, reflecting on each step's validity and backtracking when a step fails. Use when order matters and each step builds on the last - tracing a known execution path, a proof or derivation, a causal chain, a plan where phase B needs phase A - or when the user says "walk me through it step by step", "check each step", "trace this through". Not for finding an unknown root cause among many candidates (use hypothesis-elimination), for choosing among options (use tree-of-thoughts or breadth-of-thought), or for steps that can run in any order.
metadata:
  version: "2.3.0"
---

# Self-Reflecting Chain Reasoning Methodology

Works best with extended thinking for the hardest phases.

## Backstage rule: the method never appears in the answer

This methodology is scaffolding, not content. In the user-facing answer: no method names ("Self-Reflecting Chain", "SRC", or any other pattern name), no method narration ("applying the method", "scoring the dimensions", "this branch scores 7/10"), no internal scores or affinity arithmetic, no confidence-aggregation or checkpoint talk. Structure earns its place only as content built from the problem's own facts — a hypothesis table in a diagnosis, an options-vs-criteria matrix in a selection — never as a display of process. Before delivering, run a literal text search over the answer for the names above and for "pattern", "branch", "affinity", "dimension score", "confidence aggregation", "checkpoint"; rewrite every hit as content or delete it. The reader sees findings, not the apparatus that produced them.

**Purpose**: Sequential step-by-step reasoning with deep self-reflection at each step. Unlike parallel exploration (tree-of-thoughts, breadth-of-thought), this follows a single logical chain, reflects on each step's validity, and backtracks when errors are detected.

## When to Use This Method

**✅ Use when:**
- Steps have dependencies (Step N depends on Step N-1)
- Logical reasoning required (mathematical, causal, deductive)
- Need to trace exact reasoning path
- Error detection and correction critical
- Sequential planning (Step A must complete before Step B)
- Tracing a known execution path (follow one code path or data flow step by step). To find an unknown root cause among several candidates, use hypothesis-elimination instead

**❌ Don't use when:**
- Multiple independent solution paths exist → Use tree-of-thoughts or breadth-of-thought
- Need to explore many options in parallel → Use breadth-of-thought
- Steps can execute in any order → Don't need sequential reasoning

**Examples**:
- "Trace this request through the handler, queue and worker step-by-step" ✅
- "Prove this mathematical theorem" ✅
- "Plan project where each phase depends on previous" ✅
- "Choose between 5 architectures" (parallel problem - use breadth-of-thought) ❌

---

## Core Methodology: Chain-Reflect-Backtrack

### Step 1: Problem Decomposition

**Objective**: Break problem into sequential logical steps

**Actions**:
1. Identify starting state
2. Define goal state
3. List steps to get from start to goal (sequential order)
4. Number steps clearly (Step 1, 2, 3...)
5. Identify dependencies between steps

**Example** (tracing a known path):
```
Start: System crashes when user clicks "Submit"
Goal: Find where the traced path diverges from the expected one

Steps:
1. Trace user action to event handler
2. Check event handler for errors
3. Trace data flow to backend
4. Check backend validation logic
5. Inspect database query execution
6. Pin down the exact point of divergence
```

---

### Step 2: Execute Step N with Deep Reflection

**For each step**:

1. **Execute**: Perform the reasoning/action for this step
2. **State Result**: What did you learn/discover?
3. **Self-Reflect**: Is this step correct?
4. **Check Validity**: Does logic hold? Any assumptions?
5. **Verify if you can**: If the step can be executed or checked (run the code, evaluate the arithmetic, read the file, query the config), do that before trusting it.
6. **Confidence**: How confident in this step (0-100%)?

**Verify before you trust.** A step you reasoned out but could have checked is a guess. Models are fluent at producing plausible code, math and claims that are wrong, and a wrong step silently poisons every step after it. So when a check is available, run it and record the command and its output. Rate an unchecked step lower than a checked one, and rate it lower still when it is the kind that often fails in practice (code behaviour, off-by-one counts, library semantics). When a check is impossible, say so in the step's assumptions and let that lower the confidence honestly; the threshold below then tells you whether to proceed.

**Confidence thresholds** (one rule, used everywhere below):
- **70% or more**: proceed.
- **60-69%**: do not proceed yet. Firm the step up first (run the check, test the assumption, re-derive it another way) and re-rate. Proceed only if it now reaches 70%; otherwise backtrack.
- **Below 60%**: backtrack.

**Step Template** (internal working, not for the answer):
```markdown
## Step [N]: [Action]

### Execution
[Perform the reasoning or analysis]

### Result
[What was discovered/concluded]

### Self-Reflection
- **Confidence**: [0-100]%
- **Assumptions**: [What assumptions does this step make?]
- **Logic Check**: [Is the reasoning sound?]
- **Dependencies**: [Does this depend on previous steps being correct?]
- **Potential Errors**: [What could be wrong with this step?]

### Decision
- ✅ **Proceed** to Step [N+1] (confidence ≥70%)
- ⚠️ **Firm up, then re-rate** (60-69%): proceed only if it reaches ≥70%
- ❌ **Backtrack** to Step [N-X] (confidence <60%, or still <70% after firming up)
```

---

### Step 3: Backtracking Protocol

**Trigger backtracking when:**
- Step confidence <60%, or still <70% after you tried to firm it up
- Logic error detected
- Assumption proven false
- Result contradicts known facts
- Dead end reached

**Backtracking Process**:
1. **Identify error point**: Which step was wrong?
2. **Return to that step**: Go back to Step N-X
3. **Try alternative**: Take different reasoning path
4. **Mark failed path**: Document why previous path failed
5. **Resume forward**: Continue from corrected step

**Backtracking Example**:
```markdown
## Step 5: [Attempted reasoning]
→ Result: Contradiction detected
→ Confidence: 25% (contradicts Step 3 result)

**Backtrack Decision**: Return to Step 3, try alternative interpretation

## Step 3 (Revised): [Alternative reasoning]
→ Result: New interpretation consistent
→ Confidence: 80%
→ Proceed to Step 4 with revised understanding...
```

---

### Step 4: Chain Validation

**At each step**, validate the entire chain so far:

1. **Forward Consistency**: Does Step N follow logically from Step N-1?
2. **Backward Consistency**: Do all previous steps still hold given new information?
3. **Assumption Check**: Have any assumptions been violated?
4. **Alternative Paths**: Should we backtrack and try different approach?

**Validation Checklist**:
- [ ] Each step's confidence ≥70%
- [ ] No logical contradictions
- [ ] All assumptions explicitly stated
- [ ] Dependencies satisfied
- [ ] No better alternative path obvious

---

### Step 5: Final Synthesis

**After completing chain**:

1. **Trace complete path**: List all steps from start to goal
2. **Confidence per step**: Show confidence for each step
3. **Overall confidence**: Minimum confidence across all steps
4. **Alternative paths explored**: Document backtracks and why
5. **Final answer**: Clear conclusion with reasoning trace

**Synthesis Template** (internal working, not for the answer; the answer states the conclusion, the steps that carry it, and the weakest step in plain words, with numbers only if the user asked for them):
```markdown
## Chain complete

### Complete Path
1. [Step 1] → Result: [X] (Confidence: 85%)
2. [Step 2] → Result: [Y] (Confidence: 90%)
3. [Step 3] → Result: [Z] (Confidence: 75%)
4. [Step 4] → Result: [A] (Confidence: 88%)
5. [Step 5] → Result: [B] (Confidence: 82%)

### Chain confidence
75%, set by Step 3, the weakest link

### Backtracks
- Backtracked from Step 4 to Step 2 (logic error)
- Alternative path tried at Step 3 (failed, original was correct)

### Conclusion
[Answer based on complete reasoning chain]
```

---

## Self-Critique Checklist

- [ ] **Step Independence**: Is each step clearly defined?
- [ ] **Logical Flow**: Does each step follow from previous?
- [ ] **Reflection Depth**: Did I genuinely reflect on each step (not boilerplate)?
- [ ] **Backtracking Used**: Did I backtrack when confidence low?
- [ ] **Assumptions Explicit**: Are all assumptions stated clearly?
- [ ] **Weakest Link**: Is chain confidence based on weakest step?
- [ ] **Alternative Paths**: Did I consider other approaches when stuck?

---

## Common Mistakes

1. **Skipping Reflection**: Moving to next step without genuine self-reflection
2. **Ignoring Low Confidence**: Proceeding when confidence is below 70%
3. **Missing Dependencies**: Not checking if later steps depend on earlier ones
4. **No Backtracking**: Never questioning previous steps when contradictions arise
5. **False Confidence**: High confidence without justification
6. **Hidden Assumptions**: Not explicitly stating what you're assuming

---

## Sequential vs Parallel Decision Guide

| Problem Type | Use self-reflecting-chain | Use tree-of-thoughts / breadth-of-thought |
|--------------|---------------------------|-------------|
| Dependencies | Sequential steps | Independent paths |
| Goal | Single logical conclusion | Explore options |
| Method | Step-by-step reasoning | Parallel branches |
| Backtracking | Return to previous step | Prune branches |
| Output | Reasoning trace | Multiple solutions |

---

## Summary

This methodology gives you:
1. **Sequential reasoning** (step-by-step)
2. **Deep self-reflection** (confidence at each step)
3. **Error detection** (validate logic continuously)
4. **Backtracking** (correct errors when found)
5. **Traceability** (clear reasoning path)

Use it when order matters, dependencies exist, and you need one correct answer with full reasoning trace.

**Remember**: Chain confidence = minimum step confidence. A 95% confident chain with one 60% step has 60% overall confidence. Strengthen the weakest link.
