---
name: adversarial-reasoning
description: Stress-tests a design, decision or piece of code by attacking it the way an intelligent adversary would, then proposes countermeasures. Use when the user says "red-team this", "attack this design", "find the holes", "what could go wrong with this system", "security review" or "what are the edge cases", before something ships. Works through eight threat categories (spoofing through privilege escalation, supply chain, social engineering) plus eight edge-case categories. Not for plans about to launch (use premortem-evolved), for exploring options (use breadth-of-thought), for choosing between options (use tree-of-thoughts), or for diagnosing a failure that already happened (use hypothesis-elimination).
metadata:
  version: "2.3.0"
---

Works best with extended thinking for the hardest phases.

# Adversarial Reasoning

## Backstage rule — the method never appears in the answer

This methodology is scaffolding, not content. In the user-facing answer: no method names ("Adversarial Reasoning", or any other reasoning-skill name), no method narration ("applying the method", "scoring the dimensions", "this branch scores 7/10"), no internal scores or affinity arithmetic, no confidence-aggregation or checkpoint talk. Structure earns its place only as content built from the problem's own facts — a hypothesis table in a diagnosis, an options-vs-criteria matrix in a selection — never as a display of process. Before delivering, run a literal text search over the answer for the names above and for "pattern", "branch", "affinity", "dimension score", "confidence aggregation", "checkpoint"; rewrite every hit as content or delete it. The reader sees findings, not the apparatus that produced them.

**Purpose**: Systematically attack your own solutions to find weaknesses before reality does. Take the role of an intelligent adversary trying to break, exploit, or invalidate the design.

## When to Use Adversarial Reasoning

**✅ Use when:**
- Validating a proposed solution before implementation
- Security review of systems or processes
- Stress-testing business decisions
- Finding edge cases in algorithms
- Challenging group consensus (devil's advocate)

**❌ Don't use when:**
- Still exploring solution space (use breadth-of-thought first)
- Optimizing between options (use tree-of-thoughts first)
- Debugging existing issues (use hypothesis-elimination)
- A plan is about to launch and needs a failure analysis (use premortem-evolved)
- Need constructive ideation, not critique

**Examples:**
- "Attack our authentication design" ✅
- "What are the edge cases in this algorithm?" ✅
- "How could this product launch fail?" ❌ (use premortem-evolved)
- "What features should we build?" ❌ (use breadth-of-thought)

---

## Core Methodology: STRIKE Framework

The phase templates below are internal working, not for the answer. Deliver in the Output Template shape at the end.

### S - Specify the Target

**Goal**: Clearly define what you're attacking and success criteria

**Template:**
```markdown
## Attack Target Specification

**Subject**: [System/Decision/Design being attacked]
**Defender's Goal**: [What the subject is supposed to achieve]
**Attack Success Criteria**: [What counts as "breaking" it]
**Scope Boundaries**: [What's out of scope for this analysis]
**Assumed Adversary**: [Skill level: Script kiddie / Skilled / Nation-state]
```

**Example:**
```markdown
## Attack Target Specification

**Subject**: JWT-based authentication system
**Defender's Goal**: Only authenticated users access protected resources
**Attack Success Criteria**: Unauthorized access, token forgery, session hijacking
**Scope Boundaries**: Physical access attacks out of scope
**Assumed Adversary**: Skilled attacker with standard tools
```

---

### T - Threat Modeling (STRIDE+)

**Goal**: Systematically enumerate attack categories

**Use STRIDE+ Framework:**

| Category | Question | Examples |
|----------|----------|----------|
| **S**poofing | Can identity be faked? | Forged tokens, impersonation, credential theft |
| **T**ampering | Can data be modified? | MITM attacks, input manipulation, DB injection |
| **R**epudiation | Can actions be denied? | Missing audit logs, unsigned transactions |
| **I**nformation Disclosure | Can secrets leak? | Error messages, timing attacks, logs |
| **D**enial of Service | Can availability be attacked? | Resource exhaustion, algorithmic complexity |
| **E**levation of Privilege | Can access be escalated? | IDOR, role confusion, JWT claim manipulation |
| **+Supply Chain** | Can dependencies be compromised? | Malicious packages, compromised CI/CD |
| **+Social Engineering** | Can humans be exploited? | Phishing, pretexting, insider threats |

**Process:**
1. For each STRIDE+ category, brainstorm 3-5 specific attacks
2. Don't filter for feasibility yet - enumerate first
3. Include "obvious" attacks (they're often overlooked)

---

### R - Risk-Ranked Attack Generation

**Goal**: Prioritize attacks by impact and feasibility

**For each attack, assess:**

```markdown
## Attack: [Name]

**Category**: [STRIDE+ category]
**Description**: [How the attack works]
**Prerequisites**: [What attacker needs]
**Impact**: [1-5] - What damage if successful?
  - 5: Complete system compromise / data breach
  - 4: Significant unauthorized access
  - 3: Moderate data exposure or disruption
  - 2: Limited impact, contained damage
  - 1: Minimal impact, theoretical only

**Feasibility**: [1-5] - How easy to execute?
  - 5: Trivial (automated tools, no special access)
  - 4: Easy (basic skills, public exploits)
  - 3: Moderate (requires expertise or access)
  - 2: Difficult (advanced skills, insider access)
  - 1: Very difficult (nation-state resources)

**Risk Score**: Impact × Feasibility = [1-25]
```

**Priority Ranking:**
- **Critical (20-25)**: Must address before shipping
- **High (15-19)**: Address in current cycle
- **Medium (8-14)**: Plan mitigation
- **Low (1-7)**: Accept or defer

---

### I - Investigate Attack Paths

**Goal**: Develop detailed attack scenarios for top risks

**For each Critical/High risk attack, create attack narrative:**

```markdown
## Attack Path: [Name]

### Attacker Profile
- **Motivation**: [Financial / Ideological / Competitive / Chaos]
- **Resources**: [Time, tools, insider access, budget]
- **Risk Tolerance**: [Will they risk detection?]

### Attack Sequence
1. **Reconnaissance**: [How attacker discovers the vulnerability]
2. **Weaponization**: [Tools/techniques prepared]
3. **Delivery**: [How attack reaches the target]
4. **Exploitation**: [Exact steps to exploit]
5. **Installation**: [Persistence mechanisms if applicable]
6. **Command & Control**: [Ongoing access methods]
7. **Actions on Objectives**: [What attacker does with access]

### Detection Opportunities
- [Where could we detect this attack?]
- [What logs/alerts would trigger?]

### Current Mitigations
- [Existing defenses that apply]
- [Gaps in current defenses]
```

---

### K - Kill Chain Disruption

**Goal**: Design countermeasures that break attack paths

**For each attack path, identify disruption points:**

```markdown
## Countermeasures: [Attack Name]

### Prevention (Stop attack from succeeding)
| Kill Chain Stage | Countermeasure | Effort | Effectiveness |
|------------------|----------------|--------|---------------|
| Reconnaissance | [Control] | [L/M/H] | [%] |
| Delivery | [Control] | [L/M/H] | [%] |
| Exploitation | [Control] | [L/M/H] | [%] |

### Detection (Identify attack in progress)
- [Alert/monitor that would trigger]
- [Expected detection latency]

### Response (Limit damage if attack succeeds)
- [Containment procedures]
- [Recovery procedures]

### Recommended Prioritization
1. [Highest ROI countermeasure]
2. [Second priority]
3. [Third priority]
```

**Defense-in-Depth Principle**: Implement controls at multiple kill chain stages. No single control is sufficient.

---

### E - Edge Case Enumeration

**Goal**: Find non-malicious but problematic edge cases

**Categories:**

| Category | Questions |
|----------|-----------|
| **Boundary Conditions** | What happens at min/max values? Zero? Negative? |
| **Timing** | Race conditions? Timeout handling? Clock skew? |
| **Scale** | 10x users? 100x data? Empty inputs? |
| **State** | Invalid state transitions? Partial failures? |
| **Environment** | Different regions? Timezones? Languages? |
| **Integration** | Dependency failures? Version mismatches? |
| **Data** | Null? Unicode? Emoji? SQL injection characters? |
| **Concurrency** | Parallel requests? Duplicate submissions? |

**Template:**
```markdown
## Edge Case: [Name]

**Category**: [From table above]
**Scenario**: [Specific situation]
**Expected Behavior**: [What should happen]
**Potential Failure**: [What might go wrong]
**Test Case**: [How to verify handling]
```

---

## Plans About to Launch

For a project, launch or decision that needs a failure analysis rather than a security attack, use premortem-evolved.

---

## Red Team / Blue Team Exercise

**For comprehensive validation, run adversarial simulation:**

**Red Team (Attackers):**
1. Review target specification
2. Generate attacks using STRIDE+
3. Develop top 5 attack paths in detail
4. Attempt exploitation only with explicit authorization from the system's owner, and only in a test environment
5. Document successful attacks

**Blue Team (Defenders):**
1. Review same target specification
2. Implement defenses based on threat model
3. Monitor for red team activity
4. Respond to detected attacks
5. Document defensive gaps

**Purple Team (Collaboration):**
1. Red team shares successful attacks
2. Blue team explains what was missed
3. Jointly develop improved defenses
4. Update threat model with learnings

---

## Common Mistakes

1. **Being Too Nice**: Pulling punches, not exploring dark scenarios
   - Fix: Adopt genuine adversarial mindset

2. **Scope Creep**: Attacking things outside defined scope
   - Fix: Clear scope boundaries in target specification

3. **Ignoring Low-Tech Attacks**: Focusing only on sophisticated attacks
   - Fix: Include social engineering, misconfiguration, human error

4. **Attack Without Defense**: Finding problems without solutions
   - Fix: Every attack must have countermeasure recommendations

5. **One-Time Exercise**: Treating the review as a checkbox activity
   - Fix: Regular red team exercises, continuous threat modeling

---

## Integration with Other Skills

**tree-of-thoughts → adversarial-reasoning**: After tree-of-thoughts selects the best solution, attack it before implementation

**adversarial-reasoning → tree-of-thoughts**: If critical flaws turn up, evaluate fix options with tree-of-thoughts

**breadth-of-thought → adversarial-reasoning**: After breadth-of-thought generates options, attack the top candidates

**adversarial-reasoning → hypothesis-elimination**: If a vulnerability was actually exploited, investigate with hypothesis-elimination

---

## Output Template

```markdown
# Where [Subject] Can Break

## Summary
- **Target**: [What was analyzed]
- **Critical Findings**: [Top 3 risks]
- **Recommendation**: [Ship / Fix / Redesign]

## Threat Model
[Attack categories examined and what each turned up]

## Top 5 Attack Paths
[Detailed attack scenarios]

## Countermeasure Recommendations
[Prioritized defense improvements]

## Edge Cases Identified
[Non-malicious failure modes]

## Residual Risk
[What risks remain after mitigations]

## What This Review Did Not Cover
[Areas not examined, assumptions made, expertise that would sharpen the findings]
```
