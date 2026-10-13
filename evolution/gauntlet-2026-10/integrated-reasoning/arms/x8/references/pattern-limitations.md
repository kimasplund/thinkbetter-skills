# Pattern Limitations

Read this when deciding how far to trust one pattern's conclusion, or when two patterns disagree and you need to know which blind spot is in play.

**tree-of-thoughts**:
- Requires clear evaluation criteria
- Deep recursion may overfit to evaluation function
- Fixed branching can force artificial distinctions

**breadth-of-thought**:
- Cannot truly be "exhaustive"
- 8-10 branches may not cover solution space
- Returns multiple options requiring further decision

**self-reflecting-chain**:
- Limited by weakest step in chain
- Backtracking is costly
- Assumes linear dependency structure

**hypothesis-elimination**:
- Requires discriminating evidence
- Can only find causes in the hypothesis set
- Time-sensitive (may not suit exploration)

**adversarial-reasoning**:
- Requires existing solution to attack
- Can be demoralizing if overused
- May miss non-adversarial failure modes

**dialectical-reasoning**:
- Requires genuinely opposing valid views
- Synthesis isn't always possible
- Can be slower than just deciding

**analogical-transfer**:
- Analogy quality varies widely
- Source domain may mislead
- Requires creativity in finding parallels

**rapid-triage-reasoning**:
- Sacrifices depth for speed
- May miss optimal solution (accepts "good enough")
- Requires follow-up analysis for important decisions
- Not suitable when time is actually available

**negotiated-decision-framework**:
- Requires multiple genuine stakeholders
- Time-intensive (relationship building takes time)
- May produce suboptimal technical solutions for political acceptance
- Doesn't help when one party has absolute authority
