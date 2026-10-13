# Worked Example: Scoring a Strategic Problem

Read this when you are unsure how to score a dimension, or want to check your affinity arithmetic and how close scores are interpreted. This is internal working; none of it appears in the answer to the user.

**Problem**: "Design our company's approach to AI governance"

## Characteristic Scoring

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| Sequential Dependencies | 2 | Not really step-by-step |
| Criteria Clarity | 3 | Some criteria, but subjective |
| Solution Space Known | 2 | Emerging field, options unclear |
| Single Answer Needed | 4 | Need one policy |
| Evidence Available | 2 | Few precedents to learn from |
| Opposing Valid Views | 5 | Big tension: innovation vs caution |
| Problem Novelty | 5 | Very new challenge |
| Robustness Required | 4 | High stakes, need validation |
| Solution Exists | 1 | No candidate solution yet |
| Time Pressure | 2 | Strategic decision, not urgent |
| Stakeholder Complexity | 3 | Legal, product and engineering differ, but one executive owner decides |

Time Pressure is 2, so there is no fast-path. Several dimensions score 4 or more, so Direct Analysis does not apply.

## Pattern Affinity Scores

- ToT: (3×.35)+(4×.30)+(2×.20)+(1×.15) = 2.80
- BoT: (4×.35)+(2×.30)+(3×.20)+(5×.15) = 3.35
- SRC: (2×.45)+(3×.25)+(4×.20)+(1×.10) = 2.55
- HE: (2×.40)+(4×.30)+(1×.20)+(1×.10) = 2.30
- AR: **0** (SolutionExists=1 < 3, nothing to attack yet)
- DR: (5×.50)+(3×.20)+(4×.15)+(4×.15) = 4.30
- **AT: (5×.45)+(4×.30)+(4×.15)+(4×.10) = 4.45** ← Highest
- RTR: (2×.50)+(4×.25)+(2×.15)+(1×.10) = 2.40
- NDF: (3×.45)+(5×.25)+(3×.15)+(4×.15) = 3.65

## Interpretation

- AT (4.45) is above 4.0, but DR (4.30) is only 0.15 behind, so the top 2 are within 0.5: orchestrate.
- The top 3 (4.45, 4.30, 3.65) are not within 0.3 of each other, so no uncertainty propagation is needed.
- DR builds on the analogies AT produces, so run them in sequence rather than in parallel.

## Recommendation

**Primary**: analogical-transfer (4.45) - Look at how other governance challenges were solved
**Secondary**: dialectical-reasoning (4.30) - Innovation vs caution tension needs synthesis

**Orchestration**: AT → DR → AR
1. Use analogical-transfer to find analogous governance frameworks (environmental, financial, medical)
2. Use dialectical-reasoning to synthesize the innovation/caution tension
3. Use adversarial-reasoning to stress-test the proposed governance approach (a candidate now exists, so Solution Exists is at least 3)
