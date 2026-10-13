---
name: negotiated-decision-framework
description: Works out a decision that several people or groups with competing interests must all accept, by mapping stakeholders, finding common ground, sorting real conflicts from false ones, and designing an agreement each party can live with. Use when the user says "the teams disagree", "how do I get buy-in", "engineering and product want different things", "stakeholders won't agree", or when politics and power dynamics will decide whether the best answer is adopted. Not for a single decision-maker with clear criteria (use tree-of-thoughts), for a purely conceptual tension (use dialectical-reasoning), or when time pressure rules out negotiation (use rapid-triage-reasoning, then negotiate afterwards).
metadata:
  version: "2.3.0"
---

## Effort & Thinking Budget
- **Recommended effort**: medium/high — depends on stakeholder count and conflict complexity
- Use extended thinking only when analyzing complex multi-party conflicts with hidden agendas
- For simpler 2-party negotiations, effort: medium is sufficient

## Model Recommendation
Best with Opus for maximum reasoning depth. Stakeholder analysis and interest archaeology benefit from deep reasoning, but Sonnet can handle straightforward 2-3 party negotiations.

# Negotiated Decision Framework (NDF)

**Purpose**: Navigate multi-stakeholder decisions where different parties have legitimate but competing interests. NDF helps find decisions that stakeholders can live with, even if no one gets everything they want.

## When to Use NDF

**Use NDF when:**
- Multiple stakeholders must agree (or at least not block)
- Different parties have different success criteria
- Power dynamics or politics affect the decision
- Past decisions created winners/losers who remember
- "Best technical answer" won't get adopted due to stakeholder resistance
- Need buy-in for implementation success

**Don't use NDF when:**
- Single decision-maker with clear authority (use ToT)
- Stakeholders agree on criteria (use ToT with shared criteria)
- Conceptual tension, not stakeholder tension (use DR)
- Time pressure prevents negotiation (use RTR, negotiate later)

**NDF vs Other Patterns:**
- DR: Resolves conceptual/philosophical tensions (NDF: resolves people tensions)
- ToT: Finds optimal given criteria (NDF: finds optimal given stakeholders)
- BoT: Explores solution space (NDF: explores stakeholder space)

---

## Core Methodology: ALIGN Framework

### A - Analyze Stakeholder Landscape

**Goal**: Map who matters and what they care about

**Process:**
1. Identify all stakeholders (not just vocal ones)
2. Assess their power and interest
3. Understand their underlying interests (not just stated positions)
4. Map relationships and alliances

**Stakeholder Mapping Template:**
```markdown
## Stakeholder Analysis

### Power-Interest Grid

|           | Low Interest | High Interest |
|-----------|--------------|---------------|
| **High Power** | Keep Satisfied | Key Players |
| **Low Power** | Monitor | Keep Informed |

### Stakeholder Profiles

#### [Stakeholder 1]
- **Role**: [Title/Function]
- **Power Level**: [High/Medium/Low]
- **Interest Level**: [High/Medium/Low]
- **Stated Position**: [What they say they want]
- **Underlying Interest**: [Why they want it - the deeper need]
- **Success Criteria**: [How they'll judge the decision]
- **Potential Blockers**: [What would make them oppose]
- **Potential Sweeteners**: [What would win their support]
- **Relationships**: [Allies, conflicts with other stakeholders]

#### [Stakeholder 2]
...
```

**Interest Archeology:**
Don't just accept stated positions. Dig deeper:
- "We need feature X" → Why? What problem does X solve?
- "This must be done by Q2" → Why? What happens if Q3?
- "We can't change the database" → Why? What's the actual constraint?

---

### L - Locate Zones of Agreement

**Goal**: Find common ground before addressing differences

**Process:**
1. Identify shared goals (even if approaches differ)
2. Find overlapping interests
3. Establish agreed constraints
4. Build on areas of alignment

**Agreement Mapping:**
```markdown
## Zones of Agreement

### Shared Goals
- [Goal that all stakeholders want]
- [Another shared goal]

### Overlapping Interests
| Interest | Stakeholders Who Share |
|----------|------------------------|
| [Interest 1] | A, B, C |
| [Interest 2] | A, D |
| [Interest 3] | B, C, D |

### Agreed Constraints
- [Constraint everyone accepts]
- [Another constraint]

### Foundation Statement
"We all agree that [shared goal], within [constraints],
and we all want [overlapping interest]."
```

**Use agreement zones to:**
- Frame discussions positively
- Remind stakeholders of shared purpose when tensions rise
- Build solutions that honor common ground first

---

### I - Identify Irreducible Conflicts

**Goal**: Understand where genuine conflicts exist (not all conflicts are real)

**Conflict Classification:**

| Type | Description | Resolution Approach |
|------|-------------|---------------------|
| **False Conflict** | Misunderstanding, same goal different words | Clarify, reframe |
| **Resource Conflict** | Competing for same limited resource | Expand pie, prioritize, take turns |
| **Value Conflict** | Different fundamental values | Acknowledge, find higher-order value |
| **Interest Conflict** | Different parties want different outcomes | Trade, compromise, or escalate |
| **Relational Conflict** | History/politics, not the actual issue | Address relationship separately |

**Conflict Analysis Template:**
```markdown
## Conflict Analysis

### Conflict 1: [Name]
- **Parties**: [Stakeholder A] vs [Stakeholder B]
- **Type**: [False/Resource/Value/Interest/Relational]
- **A's Position**: [What A wants]
- **B's Position**: [What B wants]
- **Underlying Interests**:
  - A really needs: [Deeper interest]
  - B really needs: [Deeper interest]
- **Compatible?**: [Can both interests be met?]
- **Resolution Path**: [How to address]
```

**Key Insight**: Many conflicts are about HOW, not WHAT. If underlying interests are compatible, the conflict is solvable.

---

### G - Generate Integrative Options

**Goal**: Create solutions that satisfy multiple stakeholders' interests

**Integrative Strategies:**

1. **Expand the Pie**: Find resources to satisfy everyone
   - "Can we get more budget/time/people?"
   - "Can we do both sequentially instead of choosing?"

2. **Trade Across Issues**: Give on low-priority, get on high-priority
   - "You care more about X, we care more about Y - swap?"
   - "We'll accept your timeline if you accept our approach"

3. **Add Issues**: Bring in new elements to enable trades
   - "What if we also addressed Z, which you care about?"
   - "Can we package this with the other decision?"

4. **Compensate**: Make up for losses elsewhere
   - "You lose on this, but gain on that"
   - "This time your priority, next time ours"

5. **Reframe**: Find higher-order framing everyone can support
   - "We all want customer success - here's how this achieves it"
   - "This isn't A vs B, it's achieving C"

**Option Generation Template:**
```markdown
## Integrative Options

### Option 1: [Name]
- **How it works**: [Description]
- **Satisfies [Stakeholder A]**: [How it meets their interest]
- **Satisfies [Stakeholder B]**: [How it meets their interest]
- **Trade-offs**: [What each party gives up]
- **Feasibility**: [Can we actually do this?]

### Option 2: [Name]
...

### Comparison Matrix
| Option | Stakeholder A | Stakeholder B | Stakeholder C | Feasibility |
|--------|---------------|---------------|---------------|-------------|
| Opt 1  | [Score 1-5]   | [Score 1-5]   | [Score 1-5]   | [High/Med/Low] |
| Opt 2  | [Score 1-5]   | [Score 1-5]   | [Score 1-5]   | [High/Med/Low] |
```

---

### N - Negotiate Commitment

**Goal**: Move from options to agreement with genuine buy-in

**Negotiation Principles:**

1. **BATNA Awareness**: Know each party's Best Alternative To Negotiated Agreement
   - If their BATNA is better than your offer, they won't agree
   - Improve your offer or worsen their BATNA (ethically)

2. **Commitment Levels**: Not all agreement is equal
   - **Comply**: Will do it if required (weak)
   - **Accept**: Can live with it (moderate)
   - **Endorse**: Will support it (strong)
   - **Champion**: Will advocate for it (strongest)

3. **Legitimate Process**: Stakeholders accept outcomes better when process felt fair
   - Were they heard? Were their interests considered?
   - Is the decision-making process transparent?

**Commitment Template:**
```markdown
## Negotiated Agreement

### Decision Summary
[The agreed decision in clear terms]

### Stakeholder Commitments
| Stakeholder | Commitment Level | What They Get | What They Give |
|-------------|------------------|---------------|----------------|
| A | [Comply/Accept/Endorse/Champion] | [Their gain] | [Their concession] |
| B | [Comply/Accept/Endorse/Champion] | [Their gain] | [Their concession] |

### Conditions and Contingencies
- [Condition 1]: If [X], then [Y]
- [Review point]: Revisit at [date/milestone]

### Dispute Resolution
If disagreement arises: [How to handle]
```

---

## Power Dynamics Navigation

**When Power is Unequal:**

| Situation | Strategy |
|-----------|----------|
| You have low power | Build coalition, appeal to higher values, make strong case |
| You have high power | Use power sparingly, seek genuine input, explain reasoning |
| Power is unclear | Clarify decision rights before negotiating |
| Power is contested | Escalate to clarify, or negotiate decision process first |

**Political Patterns to Watch:**

1. **End-Run**: Stakeholder goes around you to higher authority
   - Prevention: Keep sponsors informed, address concerns early

2. **Pocket Veto**: Stakeholder agrees but doesn't implement
   - Prevention: Explicit commitment, visible milestones

3. **Relitigating**: Stakeholder reopens "settled" decisions
   - Prevention: Clear closure process, document agreements

4. **Coalition Building**: Stakeholders ally against you
   - Response: Build your own coalition, address their concerns

---

## Special Scenarios

### Scenario: Consensus Required but Not Achievable

When true consensus isn't possible:

1. **Consent-based**: "Can everyone live with this?" (not "Does everyone love it?")
2. **Disagree and Commit**: Document disagreement, commit to decision
3. **Conditional Agreement**: "I'll support this if [condition]"
4. **Escalation**: Transparent escalation to decision-maker with recommendation

### Scenario: Hidden Agendas

When you suspect unstated interests:

1. Ask "What would success look like for you?"
2. Observe what they fight for vs. what they say
3. Consider their incentives and pressures
4. Test hypotheses about real interests

### Scenario: Past Wounds

When history poisons current negotiation:

1. Acknowledge the history explicitly
2. Separate the people from the problem
3. Focus on future, not past blame
4. Consider symbolic gestures of recognition

---

## Common Mistakes

1. **Assuming Single Decision-Maker**: Not recognizing stakeholder complexity
   - Fix: Always do stakeholder analysis first

2. **Positional Bargaining**: Arguing positions instead of interests
   - Fix: Ask "Why?" five times to find real interest

3. **Ignoring Relationship**: Focusing only on this decision
   - Fix: Consider ongoing relationship, not just this transaction

4. **Winner-Take-All**: Trying to maximize one party's outcome
   - Fix: Seek integrative solutions that create value for all

5. **Premature Commitment**: Locking in before exploring options
   - Fix: Generate options before evaluating them

6. **Ignoring Implementation**: Agreement that can't be executed
   - Fix: Include implementers in negotiation, test feasibility

---

## Integration with Other Patterns

**Before NDF:**
- BoT: Explore full solution space before stakeholder negotiation
- DR: Resolve conceptual tensions first, then negotiate

**After NDF:**
- ToT: Optimize implementation details within agreed framework
- AR: Stress-test agreed solution before full commitment

**Parallel with NDF:**
- RTR: If time pressure, do quick stakeholder check, negotiate later
- SRC: Trace implementation steps after agreement reached

---

## Output Template

```markdown
# NDF Decision Record: [Decision Topic]

## Stakeholder Landscape
[Summary of key stakeholders and interests]

### Key Stakeholders
| Stakeholder (only those who can block or must act) | What they need | How they could block | What they get / give |
|-------------|----------|-------|---------------|
| [Name] | [Their real need, in plain words] | [Vote, veto, walk-out, quiet non-compliance] | [Gain] / [Concession] |

## Conflicts Addressed
| Conflict | Type | Resolution |
|----------|------|------------|
| [Conflict 1] | [Type] | [How resolved] |

## Negotiated Solution
[Description of agreed solution]

## Commitments and Conditions
- [Commitment 1]
- [Condition/Contingency]

## Implementation Notes
[How to execute with stakeholder buy-in]

## What would change this recommendation
[The fact that would flip it, and the cheapest way to check it first]
```

---

## Version History

**V1.0** (Current):
- Initial release
- ALIGN framework (Analyze, Locate, Identify, Generate, Negotiate)
- Stakeholder mapping and interest analysis
- Integrative bargaining strategies
- Power dynamics navigation
- Special scenario handling

## Backstage rule — the method never appears in the answer

This methodology is scaffolding, not content. In the user-facing answer: no method names ("Negotiated Decision Framework", "NDF", or any other pattern name), no method narration ("applying the method", "scoring the dimensions", "this branch scores 7/10"), no internal scores or affinity arithmetic, no confidence-aggregation or checkpoint talk. Structure earns its place only as content built from the problem's own facts — a hypothesis table in a diagnosis, an options-vs-criteria matrix in a selection — never as a display of process. Before delivering, run a literal text search over the answer for the names above and for "pattern", "branch", "affinity", "dimension score", "confidence aggregation", "checkpoint"; rewrite every hit as content or delete it. The reader sees findings, not the apparatus that produced them. The method's stage vocabulary is machinery too: never write "stated position" versus "underlying interest", "zones of agreement", "BATNA" or commitment-level labels; name the specific need instead. Lead with the recommendation and the blockers, describe each party once and only if it can block or must act, add no separate "what everyone agrees on" section, and stop at the last new point with no closing recap.
