---
name: reasoning-handover-protocol
description: "Keeps findings intact when one reasoning skill hands work to another: records the problem statement, the pattern used, findings so far, open questions and capped confidence, optionally saved in a .reasoning/ folder in the user's working directory. Use when an analysis moves from one reasoning skill to the next (e.g. breadth-of-thought into tree-of-thoughts), when parallel branches must be merged, when a long analysis may be compacted or resumed, or when the user says 'save where we are', 'pick this up later' or 'hand this off'. Not needed for a single-pattern analysis finished in one reply; integrated-reasoning decides which patterns to chain."
license: MIT
user-invocable: false
metadata:
  version: "2.3.0"
---

# Reasoning Handover Protocol

**Hand-off records are internal working, not for the answer.** Never show the record, pattern names or confidence arithmetic to the user unless they ask for them. The answer carries the findings, not the bookkeeping.

**Purpose**: When one reasoning skill finishes a phase and another takes over, the next one must start from what was learned, not from scratch. This guide says when that needs written state, what to write, where to put it, and how to stop hand-offs from looping.

## When a hand-off needs saved state

Write a hand-off record when the next phase **cannot see** the current findings:

- The next pattern runs in a forked or parallel subagent. breadth-of-thought runs as a fork, and parallel patterns run as separate Agent tool calls; neither sees conversation history, so the record is their only context. Forks increase the need for a hand-off, they do not remove it.
- The analysis spans many turns, so early findings may be lost to context compaction.
- Parallel branches must be merged into one conclusion.
- The user wants to pause now and resume later.

Skip the written record when a single pattern finishes in one reply, or when the next pattern runs inline in the same conversation with the findings still in view. A two-line summary in your own reasoning ("so far: X ruled out, Y likely at ~70%") is enough there.

## What to record

Use this template for every hand-off, whether it goes into a file, a subagent prompt or a message:

```markdown
# Hand-off [number]: [from skill] → [to skill]

**Problem statement:** [the problem in one or two sentences, in the user's terms]
**Constraints and success criteria:** [hard limits; what a good answer must satisfy]
**Chain so far:** [e.g. breadth-of-thought → tree-of-thoughts]

**Pattern used:** [skill name] — [how far it got: which steps were completed]
**Findings so far:**
- [finding] — evidence: [source, file, log line, or reasoning step]
**Ruled out (do not re-explore):**
- [option or hypothesis] — why: [reason]
**Assumptions:** [anything taken as true without evidence]
**Open questions:** [what is still unknown and would change the answer]

**Confidence:** [X]% — basis: [why this number]
**Next:** [to skill] should start at [step], focused on [what]
```

Keep each field short. The receiving pattern needs the evidence trail and the rule-outs most; losing them is how pruned options get re-explored.

## Confidence: one rule, shared with integrated-reasoning

- Record confidence as a percentage between a **10% floor and a 95% ceiling**. These are the same bounds integrated-reasoning applies to every result.
- **A hand-off never raises confidence.** Carry the number over unchanged. If the hand-off narrows scope or drops information, lower it and say why in "basis".
- Confidence rises only when independent patterns agree. When merging, use integrated-reasoning's Confidence Aggregation rules: full agreement gives the highest branch confidence + 5%, capped at 95%; subtract 5% when the branches share assumptions; partial agreement uses that skill's weighted formula; no agreement gives the lowest branch confidence − 10%, never below 10%.

## The optional `.reasoning/` folder

Writing files is **optional**. Use them only when you have file tools and the analysis is long enough that state could be lost; otherwise put the record in the subagent prompt or the conversation.

When you do use files, create the folder in **the user's current working directory** (the project you are working in), never inside this skill's folder. Tell the user it exists, and that they can delete it or add `.reasoning/` to `.gitignore` when done.

Minimal layout, one folder per problem:

```
.reasoning/
└── [short-topic-slug]/
    ├── handover-01-breadth-of-thought-to-tree-of-thoughts.md
    ├── handover-02-tree-of-thoughts-to-adversarial-reasoning.md
    └── merge-01.md        # only when parallel branches were merged
```

Number the files in order. Nothing else is required.

## Cycle prevention

A hand-off chain is the ordered list of patterns in "Chain so far".

**Rule:** a pattern may appear in a chain only once, and a chain holds at most 5 patterns. Before handing off, check the target against the chain:

- If the target pattern is already in the chain, do not hand off. Synthesize what you have and answer.
- If the chain already holds 5 patterns, stop and synthesize.
- If new evidence has genuinely changed the problem, re-score it with integrated-reasoning and start a **new** chain whose first record cites the old one.

Check patterns, not from→to pairs. A pair check misses most loops:

| Proposed chain | Result | Why |
|----------------|--------|-----|
| breadth-of-thought → tree-of-thoughts → adversarial-reasoning | Allowed | No pattern repeats |
| breadth-of-thought → tree-of-thoughts → breadth-of-thought | Blocked | breadth-of-thought already in chain |
| adversarial-reasoning → hypothesis-elimination → tree-of-thoughts → adversarial-reasoning | Blocked | adversarial-reasoning repeats, even though no from→to pair does |

## Merging parallel branches

Each branch (one subagent per pattern or per branch) returns its own record using the template above. Then write one merge record:

```markdown
# Merge [number] (internal working, not for the answer)

**Branches:** [pattern] — [conclusion] — [X]% | [pattern] — [conclusion] — [Y]%
**Agreement:** full | partial | none — [what they agree and disagree on]
**Merged conclusion:** [conclusion]
**Merged confidence:** [Z]% — [which integrated-reasoning rule produced it]
**Next:** [pattern or "synthesize and answer"]
```

## Resuming a saved analysis

1. Open the highest-numbered record in the topic folder.
2. Restate the problem statement and the chain so far to yourself.
3. Continue at the step named in "Next", and do not revisit anything under "Ruled out" without new evidence.

## Scenario examples

For filled-in hand-offs between specific pairs (breadth-of-thought to tree-of-thoughts, hypothesis-elimination to tree-of-thoughts and others), which pattern hands off well to which, and common mistakes, read [references/handover-templates.md](references/handover-templates.md) when preparing a hand-off between two specific skills and you want to see what the receiving one needs.
